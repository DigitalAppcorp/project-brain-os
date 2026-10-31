"""Regression: an export list with QA label is NOT an evidence-reviewed campaign.

This reproduces the shape of an Oct-2026 ad pack, without shipping any
marketing artworks or customer assets to the OS repository.
"""
import importlib.util
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

spec = importlib.util.spec_from_file_location(
    "validator", Path(__file__).with_name("validate_creatives.py"))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class SimplifiedManifestRegression(unittest.TestCase):
    def test_ten_exported_pngs_are_not_a_creative_review(self):
        unsafe_manifest = {
            "package": "Example static ads collection",
            "production_status": "CREATIVE_REVIEW_CANDIDATE",
            "brand_verification": "PENDING",
            "third_party_comprehension": "NOT_TESTED",
            "requested_count": 10,
            "creatives": [
                {"filename": f"ad_{n:02}.png",
                 "sha256": "f" * 64, "resolution": "1080x1350"}
                for n in range(1, 11)
            ],
        }
        with TemporaryDirectory() as directory:
            errors = module.validate(unsafe_manifest, Path(directory), target="review")
        self.assertTrue(errors)
        self.assertTrue(any("schema_version" in e for e in errors))
        self.assertTrue(any("brand registry" in e for e in errors))
        self.assertTrue(any("missing/unsafe image" in e for e in errors))

    def test_claimed_review_label_never_substitutes_real_verification(self):
        claimed = {
            "schema_version": 2, "requested_count": 1,
            "production_status": "CREATIVE_REVIEW_CANDIDATE",
            "prior_inventory_checked": True, "prior_asset_ids": [],
            "brand_registry": {"status": "verified_active",
                               "conflict_resolution": "not_applicable",
                               "verified_against_latest_owner_feedback": True},
            "creatives": [{"id": "test-01", "image": "not-created.png"}],
        }
        with TemporaryDirectory() as directory:
            errors = module.validate(claimed, Path(directory), target="review")
        self.assertTrue(any("missing/unsafe image" in e for e in errors))


if __name__ == "__main__":
    unittest.main(verbosity=2)
