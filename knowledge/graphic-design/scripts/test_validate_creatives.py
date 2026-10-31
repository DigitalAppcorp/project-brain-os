"""Regression suite: fail misleading creative handoffs, not just bad JSON."""
import hashlib
import importlib.util
from pathlib import Path
import struct
import tempfile
import unittest
import zlib

SPEC = importlib.util.spec_from_file_location(
    "creative_validator", Path(__file__).with_name("validate_creatives.py"))
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)


def make_png(path, color):
    def chunk(tag, data):
        return (struct.pack(">I", len(data)) + tag + data +
                struct.pack(">I", zlib.crc32(tag + data) & 0xffffffff))
    w, h = 301, 301
    scan = b"".join(b"\x00" + bytes([color, color // 2, color // 3]) * w
                    for _ in range(h))
    path.write_bytes(b"\x89PNG\r\n\x1a\n" +
                     chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)) +
                     chunk(b"IDAT", zlib.compress(scan)) +
                     chunk(b"IEND", b""))


class EvidenceGateTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        make_png(self.root / "logo.png", 21)
        logo_hash = mod.sha256(self.root / "logo.png")
        arts = []
        styles = [("photography", "editorial-asymmetry", "observational-portrait"),
                  ("expressive_typography", "fullbleed-type", "visual-wordplay"),
                  ("conceptual_collage", "diagonal-cut-paper", "physical-metaphor")]
        for n, (medium, layout, rhetoric) in enumerate(styles, 1):
            img = self.root / f"ad{n}.png"
            make_png(img, n * 30)
            digest = mod.sha256(img)
            arts.append({
                "id": f"P{n}", "image": img.name, "sha256": digest,
                "single_visual_idea": "Visible action of a pet with a distinct design idea",
                "primary_medium": medium, "composition_signature": layout,
                "visual_rhetoric": rhetoric, "category_in_art": True,
                "free_claim_in_art": True, "specific_action_in_art": True,
                "fictitious_interface": False, "unverified_claims": False,
                "brand": {"brand_id": "pazo", "active_version": "logo-v-current",
                          "usage_variant": "dark-ground-white-wordmark",
                          "master_asset": "logo.png", "master_sha256": logo_hash,
                          "exact_asset_composited": True, "visual_match_checked": True},
                "visual_review": {
                    "inspected_sha256": digest, "result": "PASS",
                    "visible_evidence": "Opened the final full image and checked copy placement, visual idea, source provenance, and logo at mobile size.",
                    "strongest_rejection_reason": "The pet action may be generic if the photography lacks causality."
                },
                "source_asset_ids": [f"new-photo-{n}"],
                "blind_comprehension": {"status": "NOT_TESTED"},
                "rights_verified": False, "owner_approved": False,
            })
        self.m = {"schema_version": 2, "requested_count": 3,
                  "prior_inventory_checked": True, "prior_asset_ids": ["old-photo-1"],
                  "brand_registry": {
                      "brand_id": "pazo", "active_version": "logo-v-current",
                      "status": "verified_active",
                      "authoritative_asset_id": "verified-library-master-asset",
                      "master_asset": "logo.png", "master_sha256": logo_hash,
                      "approval_authority": "product-owner",
                      "approval_evidence": "recorded-decision-from-owner",
                      "usage_variant": "dark-ground-white-wordmark",
                      "conflict_resolution": "resolved_by_owner",
                      "verified_against_latest_owner_feedback": True,
                  }, "creatives": arts}

    def problems(self, target="review"):
        return mod.validate(self.m, self.root, target)

    def expect(self, phrase):
        self.assertTrue(any(phrase in x for x in self.problems()), self.problems())

    def test_pilot_packet_evidence_complete_not_art_certified(self):
        self.assertEqual(self.problems(), [])
        self.assertTrue(any("blind comprehension" in x for x in self.problems("publish")))

    def test_collage_substitutes_for_three_ads(self):
        self.m["creatives"] = self.m["creatives"][:1]
        self.expect("requested_count")

    def test_exact_duplicate_artwork(self):
        one, two = self.m["creatives"][:2]
        two["image"] = one["image"]
        two["sha256"] = one["sha256"]
        two["visual_review"]["inspected_sha256"] = one["sha256"]
        self.expect("identical final artwork")

    def test_photo_reused_from_rejected_batch(self):
        self.m["creatives"][0]["source_asset_ids"] = ["old-photo-1"]
        self.expect("source asset reused")

    def test_photo_repeated_in_this_batch(self):
        self.m["creatives"][1]["source_asset_ids"] = ["new-photo-1"]
        self.expect("source asset repeated")

    def test_repeated_layout_templates(self):
        for a in self.m["creatives"]:
            a.update(primary_medium="photography",
                     composition_signature="same-template",
                     visual_rhetoric="stock-pet-portrait")
        self.expect("insufficient material differences")

    def test_wrong_logo(self):
        self.m["creatives"][0]["brand"]["master_sha256"] = "0" * 64
        self.expect("wrong official logo")

    def test_generated_logo_instead_of_master(self):
        self.m["creatives"][0]["brand"]["exact_asset_composited"] = False
        self.expect("not AI-recreated")

    def test_old_image_review_reused(self):
        self.m["creatives"][0]["visual_review"]["inspected_sha256"] = "0" * 64
        self.expect("not been individually visually inspected")

    def test_generic_happiness_without_real_action(self):
        self.m["creatives"][0]["specific_action_in_art"] = False
        self.expect("real-use-case")

    def test_fake_phone_interface(self):
        self.m["creatives"][0]["fictitious_interface"] = True
        self.expect("fictitious UI")

    def test_visual_rejection_is_final(self):
        self.m["creatives"][0]["visual_review"]["result"] = "REJECT"
        self.expect("visual review did not PASS")

    def test_missing_artifact(self):
        self.m["creatives"][0]["image"] = "missing.png"
        self.expect("missing/unsafe image")

    def test_no_prior_inventory_rejected(self):
        self.m["prior_inventory_checked"] = False
        self.expect("prior asset inventory")

    def test_historical_logo_is_not_active_brand(self):
        self.m["brand_registry"]["status"] = "historical"
        self.expect("historical is not current")

    def test_unresolved_brand_identity_conflict_blocks_all(self):
        self.m["brand_registry"]["conflict_resolution"] = "unresolved"
        self.expect("brand identity conflict unresolved")

    def test_newer_owner_feedback_not_verified(self):
        self.m["brand_registry"]["verified_against_latest_owner_feedback"] = False
        self.expect("latest owner feedback")

    def test_creative_points_to_historical_logo_version(self):
        self.m["creatives"][0]["brand"]["active_version"] = "concept-4-legacy"
        self.expect("creative logo differs from active brand registry")

    def test_creative_uses_unapproved_logo_variant(self):
        self.m["creatives"][0]["brand"]["usage_variant"] = "unknown-colorway"
        self.expect("creative logo differs from active brand registry")

    def test_missing_brand_provenance_source(self):
        self.m["brand_registry"]["approval_evidence"] = ""
        self.expect("brand registry missing documented approval_evidence")

    def test_publish_needs_separate_human_approvals(self):
        for a in self.m["creatives"]:
            a["blind_comprehension"] = {
                "status": "TESTED",
                "observed_answers": ["free pet app with pet profile"]
            }
            a["rights_verified"] = True
            a["owner_approved"] = True
        self.assertEqual(self.problems("publish"), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
