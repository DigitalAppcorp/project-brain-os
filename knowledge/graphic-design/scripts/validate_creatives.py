#!/usr/bin/env python3
"""Fail-closed evidence preflight for static creative packs.

Checks file existence, SHA, PNG/JPEG dimensions, declared image provenance,
portfolio differentiation, image-by-image inspection and stage approval.
DOES NOT automatically verify aesthetics, visible copy, exact logo shape,
copyright permissions or actual audience comprehension.

Usage: python validate_creatives.py manifest.json --root DIR --target review|publish
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import struct
import sys

ALLOWED_MEDIA = {"photography", "expressive_typography", "illustration",
                 "conceptual_collage", "product_documentation", "mixed_media"}


def dimensions(path: Path):
    with path.open("rb") as stream:
        start = stream.read(32)
    if start[:8] == b"\x89PNG\r\n\x1a\n" and len(start) >= 24:
        return "PNG", *struct.unpack(">II", start[16:24])
    if start[:2] == b"\xff\xd8":
        blob = path.read_bytes()
        i = 2
        while i + 8 < len(blob):
            if blob[i] != 0xff:
                i += 1
                continue
            marker = blob[i + 1]
            i += 2
            if marker in (0xd8, 0xd9, 0x01) or 0xd0 <= marker <= 0xd7:
                continue
            if i + 2 > len(blob):
                break
            length = int.from_bytes(blob[i:i + 2], "big")
            if length < 2 or i + length > len(blob):
                break
            if marker in {0xc0, 0xc1, 0xc2, 0xc3, 0xc5, 0xc6, 0xc7,
                          0xc9, 0xca, 0xcb, 0xcd, 0xce, 0xcf} and length >= 7:
                height = int.from_bytes(blob[i + 3:i + 5], "big")
                width = int.from_bytes(blob[i + 5:i + 7], "big")
                return "JPEG", width, height
            i += length
    return None, 0, 0


def sha256(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe_file(root: Path, name: str):
    if not isinstance(name, str) or not name.strip():
        return None
    target = (root / name).resolve()
    if not target.is_relative_to(root.resolve()) or not target.is_file():
        return None
    return target


def validate(m: dict, root: Path, target: str = "review") -> list[str]:
    problems = []
    add = problems.append
    if target not in {"review", "publish"}:
        return ["invalid target"]
    if m.get("schema_version") != 1:
        add("schema_version must be 1")
    qty, arts = m.get("requested_count"), m.get("creatives")
    if not isinstance(arts, list) or not isinstance(qty, int) or qty < 1 or len(arts) != qty:
        return problems + ["requested_count must equal individual creative files (contact sheet does not count)"]
    if m.get("prior_inventory_checked") is not True or not isinstance(m.get("prior_asset_ids"), list):
        add("prior asset inventory must be explicitly reviewed and supplied")
    seen_ids, hashes, sources = set(), set(), set()
    previous = set(m.get("prior_asset_ids", []))
    observed = []
    for i, art in enumerate(arts, 1):
        name = f"creative[{i}]"
        if not isinstance(art, dict):
            add(f"{name}: not an object")
            continue
        ident = art.get("id")
        if not isinstance(ident, str) or not ident or ident in seen_ids:
            add(f"{name}: missing or duplicated id")
        seen_ids.add(ident)
        p = safe_file(root, art.get("image"))
        if p is None:
            add(f"{name}: missing/unsafe image file")
            continue
        suffix = p.suffix.lower()
        fmt, w, h = dimensions(p)
        if ((suffix == ".png" and fmt != "PNG") or
            (suffix in {".jpg", ".jpeg"} and fmt != "JPEG") or fmt is None):
            add(f"{name}: unsupported or mislabeled image")
        if w < 300 or h < 300:
            add(f"{name}: image resolution too small")
        digest = sha256(p)
        if digest != art.get("sha256"):
            add(f"{name}: image SHA256 differs from inspected manifest; regenerate review")
        if digest in hashes:
            add(f"{name}: identical final artwork reused")
        hashes.add(digest)
        if len(str(art.get("single_visual_idea", "")).strip()) < 20:
            add(f"{name}: missing concrete visual idea")
        if art.get("primary_medium") not in ALLOWED_MEDIA:
            add(f"{name}: missing/invalid medium")
        if not art.get("composition_signature"):
            add(f"{name}: missing composition_signature")
        if not all(art.get(k) is True for k in
                   ("category_in_art", "free_claim_in_art", "specific_action_in_art")):
            add(f"{name}: missing category/free/real-use-case verification")
        if art.get("fictitious_interface") is not False or art.get("unverified_claims") is not False:
            add(f"{name}: fictitious UI or claims not explicitly ruled out")
        brand = art.get("brand", {})
        logo = safe_file(root, brand.get("master_asset")) if isinstance(brand, dict) else None
        if not logo:
            add(f"{name}: missing official logo master asset")
        elif sha256(logo) != brand.get("master_sha256"):
            add(f"{name}: wrong official logo asset fingerprint")
        if (not isinstance(brand, dict) or
            brand.get("exact_asset_composited") is not True or
            brand.get("visual_match_checked") is not True):
            add(f"{name}: official logo must be composited and inspected (not AI-recreated)")
        review = art.get("visual_review", {})
        if not isinstance(review, dict) or review.get("inspected_sha256") != digest:
            add(f"{name}: final file has not been individually visually inspected")
        else:
            if review.get("result") not in {"PASS", "REVISE", "REJECT"}:
                add(f"{name}: missing visual verdict")
            if review.get("result") != "PASS":
                add(f"{name}: visual review did not PASS")
            if len(str(review.get("visible_evidence", "")).strip()) < 40:
                add(f"{name}: visual evidence too generic or missing")
            if len(str(review.get("strongest_rejection_reason", "")).strip()) < 20:
                add(f"{name}: missing contrary review / strongest reason to reject")
        asset_ids = art.get("source_asset_ids")
        if (not isinstance(asset_ids, list) or not asset_ids or
            not all(isinstance(s, str) and s for s in asset_ids)):
            add(f"{name}: declare provenance of photograph/illustration assets")
            asset_ids = []
        for asset_id in asset_ids:
            if asset_id in previous:
                add(f"{name}: source asset reused from rejected/prior batch: {asset_id}")
            if asset_id in sources:
                add(f"{name}: source asset repeated across this series: {asset_id}")
            sources.add(asset_id)
        observed.append(art)
        if target == "publish":
            blind = art.get("blind_comprehension", {})
            if (not isinstance(blind, dict) or
                blind.get("status") != "TESTED" or not blind.get("observed_answers")):
                add(f"{name}: independent blind comprehension not verified")
            if art.get("rights_verified") is not True or art.get("owner_approved") is not True:
                add(f"{name}: rights/PO publication authorization missing")
    if qty > 1:
        for i, left in enumerate(observed):
            for right in observed[i + 1:]:
                diff = sum(left.get(key) != right.get(key) for key in
                           ("primary_medium", "composition_signature", "visual_rhetoric"))
                if diff < 2:
                    add("portfolio: insufficient material differences between "
                        f"{left.get('id')} and {right.get('id')} "
                        "(need 2/3 of medium, composition, rhetoric)")
    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest")
    parser.add_argument("--root", default=".")
    parser.add_argument("--target", choices=("review", "publish"), default="review")
    args = parser.parse_args()
    m = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    problems = validate(m, Path(args.root), args.target)
    if problems:
        print("EVIDENCE_GATE_REJECT")
        for problem in problems:
            print(" -", problem)
        return 1
    print("EVIDENCE_GATE_COMPLETE: evidence and metadata present; "
          "ARTISTIC QUALITY NOT AUTOMATICALLY CERTIFIED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
