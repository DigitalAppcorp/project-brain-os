#!/usr/bin/env python3
"""Editorial evidence preflight: rejects fake narrative claims, not a taste/quality AI.
Accepts declarations produced from reviewed *actual* footage. Independent
human film/audio review is still required; PASS is never automatic.
"""
from dataclasses import dataclass
import unittest


@dataclass(frozen=True)
class ShotEvidence:
    action_visible: bool = False
    reaction_visible: bool = False
    changes_situation: bool = False
    motivation_for_cut: str = ""
    audio_function: str = ""
    actual_media_verified: bool = False


def review_readiness(claimed_format, shots, *, sound_reviewed=False):
    if not shots:
        return "BLOCKED", ["No actual shots supplied"]
    if not all(x.actual_media_verified for x in shots):
        return "BLOCKED", ["Declared media is not verified on the final timeline"]
    if claimed_format in ("narrative_comedy", "cinematic_story", "acted_3d"):
        if not any(x.action_visible and x.changes_situation for x in shots):
            return "CREATIVE_FAIL", ["No acted action changes the situation"]
        if not any(x.reaction_visible for x in shots):
            return "CREATIVE_FAIL", ["No visible reaction to the action"]
        if not any(x.motivation_for_cut for x in shots):
            return "CREATIVE_FAIL", ["Cuts have no articulated editorial purpose"]
    elif claimed_format == "interactive_product_demo":
        if not any(x.action_visible and x.changes_situation for x in shots):
            return "CREATIVE_FAIL", ["No real completed interaction demonstrated"]
    if not sound_reviewed:
        return "NOT_EVALUATED", ["Sound has not been actually reviewed"]
    return "INDEPENDENT_EDITOR_REVIEW_REQUIRED", [
        "Evidence preflight only: aesthetic and narrative merit cannot be auto-certified"
    ]


class EditorialFixtures(unittest.TestCase):
    def test_stock_caption_montage_rejected_as_acted_comedy(self):
        montage = [
            ShotEvidence(actual_media_verified=True, motivation_for_cut="every four seconds", audio_function="music"),
            ShotEvidence(actual_media_verified=True, motivation_for_cut="every four seconds", audio_function="music"),
            ShotEvidence(actual_media_verified=True, motivation_for_cut="brand card", audio_function="music"),
        ]
        self.assertEqual(review_readiness("narrative_comedy", montage, sound_reviewed=True)[0], "CREATIVE_FAIL")

    def test_static_screens_rejected_as_interactive_demo(self):
        still = [ShotEvidence(actual_media_verified=True, motivation_for_cut="next screenshot", audio_function="music")]
        self.assertEqual(review_readiness("interactive_product_demo", still, sound_reviewed=True)[0], "CREATIVE_FAIL")

    def test_real_story_still_requires_editorial_review(self):
        shots = [
            ShotEvidence(True, False, True, "cut on reaction", "ambience", True),
            ShotEvidence(False, True, False, "hold for pause", "silence", True),
        ]
        self.assertEqual(review_readiness("cinematic_story", shots, sound_reviewed=True)[0],
                         "INDEPENDENT_EDITOR_REVIEW_REQUIRED")

    def test_audio_not_heard_never_marks_ready(self):
        shot = [ShotEvidence(True, True, True, "reveal", "dialogue", True)]
        self.assertEqual(review_readiness("narrative_comedy", shot)[0], "NOT_EVALUATED")

    def test_unverified_stills_never_pass(self):
        shot = [ShotEvidence(True, True, True, "response", "sound", False)]
        self.assertEqual(review_readiness("narrative_comedy", shot, sound_reviewed=True)[0], "BLOCKED")


if __name__ == "__main__":
    unittest.main()
