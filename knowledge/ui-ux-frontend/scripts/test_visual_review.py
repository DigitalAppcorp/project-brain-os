"""Reproducible counterexamples for evidence/authority, not an agent benchmark."""
import hashlib
from pathlib import Path
import tempfile
import unittest
from visual_review import evaluate


class VisualReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / 'synthetic.png').write_bytes(b'synthetic fixture, not a product capture')
        self.record = dict(lane='new_authorized_ui', authorization_source='synthetic user order',
            languages=['es', 'en'], viewports=[320, 390, 430],
            applicable_states=['pending', 'content', 'empty', 'error', 'recovery'],
            forced_conditions_and_limits='Synthetic state fixture; not a real product evaluation.',
            coverage=[dict(language=l, width=w, state=s, path='synthetic.png',
                sha256=hashlib.sha256((self.root / 'synthetic.png').read_bytes()).hexdigest(),
                frame='full_runtime', inspected_by='synthetic reviewer')
                for l in ['es', 'en'] for w in [320, 390, 430]
                for s in ['pending', 'content', 'empty', 'error', 'recovery']],
            professional_review={k:'synthetic reason' for k in ('brief_alignment','composition','hierarchy','continuity',
                'negative_space','actions','identity','states','better_than_no_addition')},
            adversarial={k:'synthetic evidence' for k in ('reviewer_or_separate_pass','defects',
                'corrections','recapture_comparison')}, design_decision='DESIGN_QA_PASS',
            po_visual={'status':'NOT_REQUESTED'})
    def tearDown(self):
        self.temp.cleanup()
    def error(self, r, error):
        self.assertIn(error, evaluate(r, self.root)['errors'])
    def test_new_ui_requires_no_routine_po_vote_or_release(self):
        result = evaluate(self.record, self.root)
        self.assertEqual(result['status'], 'RECORD_COMPLETE')
        self.assertFalse(result['grants_release'])
    def test_old_build_targets_overflow_only_report_fails(self):
        self.error(dict(lane='new_authorized_ui', build=True, targets=True, overflow=False,
            design_decision='DESIGN_QA_PASS'), 'ADVERSARIAL_CORRECTION_MISSING')
    def test_missing_feed_states_fails(self):
        self.record['coverage'].pop()
        self.error(self.record, 'RUNTIME_STATE_COVERAGE_MISSING')
    def test_component_crop_is_not_whole_runtime(self):
        self.record['coverage'][0]['frame']='component_crop'
        self.error(self.record, 'FULL_RUNTIME_NOT_INSPECTED')
    def test_captured_but_unseen_is_not_reviewed(self):
        self.record['coverage'][0]['inspected_by']=''
        self.error(self.record, 'FULL_RUNTIME_NOT_INSPECTED')
    def test_changed_capture_is_rejected(self):
        (self.root/'synthetic.png').write_bytes(b'changed')
        self.error(self.record, 'CAPTURE_CHANGED')
    def test_po_directed_redesign_preserves_gate(self):
        self.record['lane']='po_directed_redesign'
        self.error(self.record, 'DIRECTED_REDESIGN_REQUIRES_PO_DECISION')
        self.record['po_visual']={'status':'YES','source':'synthetic exact approval'}
        self.assertEqual(evaluate(self.record,self.root)['status'],'RECORD_COMPLETE')
    def test_internal_pass_cannot_invent_po_acceptance(self):
        self.record['po_visual']={'status':'YES'}
        self.error(self.record, 'PO_ACCEPTANCE_INVENTED')
    def test_technical_nonvisual_needs_no_art_package(self):
        self.assertEqual(evaluate({'lane':'technical_nonvisual'},self.root)['status'],'NOT_APPLICABLE')
    def test_decision_cannot_replace_composition_reasoning(self):
        self.record['professional_review'].pop('composition')
        self.error(self.record,'REASONING_MISSING:composition')
    def test_external_or_missing_capture_is_rejected(self):
        self.record['coverage'][0]['path']='../outside.png'
        self.error(self.record,'CAPTURE_UNAVAILABLE')

    def test_composition_pass_without_alignment_to_explicit_brief_fails(self):
        self.record['professional_review'].pop('brief_alignment')
        self.error(self.record,'REASONING_MISSING:brief_alignment')


if __name__ == '__main__':
    unittest.main()
