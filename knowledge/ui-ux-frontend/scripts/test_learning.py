"""Small offline behavioral checks; no product runtime or external services."""
from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import learning


def event(eid, status="APPROVED", pattern="transparent", **changes):
    result = {"schema_version": 1, "id": eid, "product": "example", "date": "2026-10-26",
              "screen": "feed", "component": "follow", "context": {}, "stage": "PREVIEW",
              "decision": status, "source": {"kind": "PO_DIRECT", "ref": f"review:{eid}"},
              "feedback": f"Explicit decision {eid}", "artifact_status": "AVAILABLE", "result": "Preview reviewed; runtime not tested",
              "aspects": [{"key": "style", "pattern": pattern, "dimension": "surface", "status": status, "lesson": "Local preference"}]}
    result.update(changes)
    return result


class LearningChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.store = Path(self.temp.name) / "feedback.jsonl"
        self.store.touch()

    def scores(self, **kwargs):
        options = dict(product="example", screen="feed", component="follow", context={}, as_of="2026-10-26")
        options.update(kwargs)
        return {item["pattern"]: item["score"] for item in learning.query(learning.load(self.store), **options)["patterns"]}

    def test_approval_increases_correct_pattern(self):
        self.assertEqual(self.scores(), {})
        learning.record(self.store, [event("a")])
        self.assertEqual(self.scores(), {"transparent": 2})

    def test_rejection_reduces_only_contextual_priority(self):
        learning.record(self.store, [event("a", "REJECTED", "solid")])
        self.assertEqual(self.scores(), {"solid": -2})

    def test_mixed_feedback_retains_success(self):
        mixed = event("mixed", "PARTIAL")
        mixed["aspects"] = [event("a")["aspects"][0],
                            {"key": "spacing", "pattern": "crowded", "dimension": "spacing", "status": "REJECTED", "lesson": "Reduce crowding"}]
        learning.record(self.store, [mixed])
        self.assertEqual(self.scores(), {"transparent": 2, "crowded": -2})

    def test_feed_does_not_contaminate_profile_project_or_component(self):
        learning.record(self.store, [event("a")])
        self.assertEqual(self.scores(screen="profile"), {})
        self.assertEqual(self.scores(product="another"), {})
        self.assertEqual(self.scores(component="card"), {})

    def test_later_explicit_supersession_and_reversal(self):
        old, new = event("old"), event("new", "APPROVED", "solid")
        new["aspects"][0]["supersedes"] = ["old#style"]
        learning.record(self.store, [old, new])
        self.assertEqual(self.scores(), {"solid": 2})
        reversal = {"schema_version": 1, "kind": "retraction", "id": "undo", "target": "new", "product": "example", "date": "2026-10-26",
                    "source": {"kind": "DOCUMENTED_PO", "ref": "review:correction"}, "feedback": "Wrong source attribution; retain audit history"}
        learning.record(self.store, [reversal])
        self.assertEqual(self.scores(), {"transparent": 2})

    def test_new_session_recovers_versioned_files(self):
        learning.record(self.store, [event("a")])
        output = subprocess.check_output([sys.executable, "-X", "utf8", str(Path(learning.__file__)), "query", "--store", str(self.store),
                                          "--product", "example", "--screen", "feed", "--component", "follow", "--as-of", "2026-10-26"])
        self.assertEqual(json.loads(output)["patterns"][0]["score"], 2)

    def test_ci_cannot_award_approval_and_unknown_scores_zero(self):
        technical = event("ci", source={"kind": "TECHNICAL", "ref": "ci:success"})
        with self.assertRaises(ValueError):
            learning.record(self.store, [technical])
        unknown = event("unknown", "UNVERIFIED", source={"kind": "TECHNICAL", "ref": "ci:success"})
        learning.record(self.store, [unknown])
        self.assertEqual(self.scores()["transparent"], 0)

    def test_duplicate_is_idempotent_and_replay_cannot_inflate(self):
        first = event("a")
        learning.record(self.store, [first])
        self.assertEqual(learning.record(self.store, [first])["added"], 0)
        replay = deepcopy(first)
        replay["id"] = "other-id"
        with self.assertRaises(ValueError):
            learning.record(self.store, [replay])

    def test_invalid_batch_does_not_partially_write(self):
        bad = event("bad")
        bad["aspects"][0]["supersedes"] = ["missing#style"]
        with self.assertRaises(ValueError):
            learning.record(self.store, [event("valid"), bad])
        self.assertEqual(self.store.read_text(), "")

    def test_context_expiry_and_future_date(self):
        learning.record(self.store, [event("a", context={"theme": "dark"}), event("b", pattern="expired", valid_until="2026-10-26"),
                                     event("c", pattern="future", date="2026-10-28")])
        self.assertNotIn("transparent", self.scores())
        self.assertEqual(self.scores(context={"theme": "dark"})["transparent"], 2)
        self.assertNotIn("expired", self.scores(as_of="2026-10-27"))
        self.assertNotIn("future", self.scores())

    def test_partial_supersession_preserves_unaffected_aspect(self):
        old = event("old", "PARTIAL")
        old["aspects"] = [event("a")["aspects"][0], {"key": "density", "pattern": "dense", "dimension": "density", "status": "REJECTED", "lesson": "Too dense"}]
        new = event("new", pattern="spacious")
        new["aspects"][0].update(dimension="density", supersedes=["old#density"])
        learning.record(self.store, [old, new])
        self.assertEqual(self.scores(), {"transparent": 2, "spacious": 2})

    def test_process_recurrence_without_erasing_rejected_history(self):
        a, b = event("a", "REJECTED"), event("b", "REJECTED")
        for item in [a, b]:
            item["aspects"][0]["process_issue"] = "fidelity-without-comparison"
        learning.record(self.store, [a, b])
        issues = learning.audit(learning.load(self.store), "example", "2026-10-26")["process_issues"]
        self.assertEqual((issues[0]["count"], issues[0]["recurring"]), (2, True))

    def test_correction_weight_and_no_unverified_or_cross_scope_override(self):
        learning.record(self.store, [event("old", "CORRECTED", "too-small")])
        self.assertEqual(self.scores(), {"too-small": -1})
        unknown = event("unknown", "UNVERIFIED")
        unknown["aspects"][0]["supersedes"] = ["old#style"]
        with self.assertRaises(ValueError):
            learning.record(self.store, [unknown])
        other = event("other", screen="profile")
        other["aspects"][0]["supersedes"] = ["old#style"]
        with self.assertRaises(ValueError):
            learning.record(self.store, [other])


if __name__ == "__main__":
    unittest.main()
