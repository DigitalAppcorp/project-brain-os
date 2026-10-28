"""Check review evidence completeness; never judge beauty or grant release.

Input is an explicit professional record. A valid record does NOT prove that
its claims are true; inspect the referenced runtime images and source first.
"""
import argparse
import hashlib
import json
from pathlib import Path


def evaluate(record, root):
    if record.get('lane') == 'technical_nonvisual':
        return {'status': 'NOT_APPLICABLE', 'errors': []}
    errors = []
    if record.get('lane') not in ('new_authorized_ui', 'po_directed_redesign'):
        errors.append('CLASSIFY_SCOPE')
    if not record.get('authorization_source'):
        errors.append('IMPLEMENTATION_AUTHORIZATION_MISSING')
    coverage = record.get('coverage', [])
    expected = {(lang, width, state) for lang in record.get('languages', [])
                for width in record.get('viewports', [])
                for state in record.get('applicable_states', [])}
    if not expected or not expected.issubset({(c.get('language'), c.get('width'), c.get('state')) for c in coverage}):
        errors.append('RUNTIME_STATE_COVERAGE_MISSING')
    if not record.get('forced_conditions_and_limits'):
        errors.append('EVIDENCE_LIMITS_MISSING')
    for capture in coverage:
        file = (root / capture.get('path', '')).resolve()
        if not file.is_relative_to(root.resolve()) or not file.is_file():
            errors.append('CAPTURE_UNAVAILABLE')
            continue
        if hashlib.sha256(file.read_bytes()).hexdigest() != capture.get('sha256'):
            errors.append('CAPTURE_CHANGED')
        if capture.get('frame') != 'full_runtime' or not capture.get('inspected_by'):
            errors.append('FULL_RUNTIME_NOT_INSPECTED')
    review = record.get('professional_review', {})
    for field in ('composition', 'hierarchy', 'continuity', 'negative_space', 'actions', 'identity', 'states', 'better_than_no_addition'):
        if not review.get(field):
            errors.append('REASONING_MISSING:' + field)
    adversarial = record.get('adversarial', {})
    if not all(adversarial.get(f) for f in ('reviewer_or_separate_pass', 'defects', 'corrections', 'recapture_comparison')):
        errors.append('ADVERSARIAL_CORRECTION_MISSING')
    if record.get('design_decision') != 'DESIGN_QA_PASS':
        errors.append('PROFESSIONAL_PASS_NOT_GIVEN')
    po = record.get('po_visual', {})
    if po.get('status') == 'YES' and not po.get('source'):
        errors.append('PO_ACCEPTANCE_INVENTED')
    if record.get('lane') == 'po_directed_redesign' and not (
        po.get('status') == 'YES' and po.get('source') or record.get('po_delegation_source')
    ):
        errors.append('DIRECTED_REDESIGN_REQUIRES_PO_DECISION')
    return {'status': 'RECORD_COMPLETE' if not errors else 'RECORD_INCOMPLETE',
            'errors': sorted(set(errors)), 'grants_release': False,
            'limitation': 'Completeness is not visual quality or proof of truthful review.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('record', type=Path)
    parser.add_argument('--root', type=Path, required=True)
    args = parser.parse_args()
    result = evaluate(json.loads(args.record.read_text(encoding='utf-8-sig')), args.root)
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if result['status'] in ('RECORD_COMPLETE', 'NOT_APPLICABLE') else 1)
