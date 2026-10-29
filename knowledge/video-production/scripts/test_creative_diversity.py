#!/usr/bin/env python3
"""Limited, declarative diversity preflight.

This rejects obvious template repetition; it cannot inspect video pixels, prove
artistic quality or infer audience response. Human review of actual media is
required per CREATIVE_EVIDENCE_GATE.md.
"""
from collections import Counter
from dataclasses import dataclass
import unittest


@dataclass(frozen=True)
class Candidate:
    id: str
    screen_language: str
    editing_grammar: str
    story_engine: str
    audio_role: str
    underlying_sources: tuple[str, ...]


def preflight(candidates):
    if len(candidates) < 2:
        return ("NOT_A_BATCH", ["Need at least two outputs"])
    # Shared brand endcards are intentionally not a negative condition.
    pairs = Counter((c.screen_language, c.editing_grammar) for c in candidates)
    repeated = [pair for pair, n in pairs.items() if n >= 2]
    if repeated:
        return ("DIVERSITY_NOT_DEMONSTRATED", [
            f"{n} candidates reuse primary method and grammar {pair!r}"
            for pair, n in pairs.items() if n >= 2
        ])
    if len({c.screen_language for c in candidates}) < 2:
        return ("DIVERSITY_NOT_DEMONSTRATED", ["Only one screen language"])
    return ("MANUAL_REVIEW_REQUIRED", [
        "Declared methods differ, but actual clips and rights must be reviewed"
    ])


class PreflightFixtures(unittest.TestCase):
    def test_rejects_repeated_stock_caption_template_despite_different_scripts(self):
        videos = [
            Candidate("emotive", "stock_pets", "stock_4sec_caption_cut", "emotive", "music", ("a", "b", "c")),
            Candidate("humor", "stock_pets", "stock_4sec_caption_cut", "humor", "music", ("b", "d", "e")),
            Candidate("product", "stock_plus_still", "stock_4sec_caption_cut", "utility", "music", ("d", "screenshot")),
            Candidate("dialogue", "stock_pets", "stock_4sec_caption_cut", "dialogue_copy", "music", ("a", "e")),
        ]
        verdict, reasons = preflight(videos)
        self.assertEqual(verdict, "DIVERSITY_NOT_DEMONSTRATED")
        self.assertTrue(reasons)

    def test_different_production_methods_still_require_manual_review(self):
        videos = [
            Candidate("acted", "continuous_acted_scene", "continuity_editing", "tension_payoff", "diegetic_dialogue", ("original_actor",)),
            Candidate("3d", "rigged_character_animation", "animated_shot_reverse_shot", "character_comedy", "acted_voice", ("licensed_rig",)),
            Candidate("ugc", "real_handheld_pet", "observational_smash_cut", "pet_reaction", "natural_audio", ("original_video",)),
            Candidate("demo", "real_app_interaction", "task_screen_recording", "task_completion", "walkthrough_voice", ("real_UI_capture",)),
        ]
        verdict, _ = preflight(videos)
        self.assertEqual(verdict, "MANUAL_REVIEW_REQUIRED")

    def test_single_video_is_not_batch(self):
        verdict, _ = preflight([Candidate("a", "stock", "cut", "a", "music", ())])
        self.assertEqual(verdict, "NOT_A_BATCH")

    def test_change_of_words_not_sufficient(self):
        items = [
            Candidate("a", "same_stock", "same_template", "sad", "music", ("a",)),
            Candidate("b", "same_stock", "same_template", "funny", "new_music", ("b",)),
        ]
        verdict, _ = preflight(items)
        self.assertEqual(verdict, "DIVERSITY_NOT_DEMONSTRATED")


if __name__ == "__main__":
    unittest.main()
