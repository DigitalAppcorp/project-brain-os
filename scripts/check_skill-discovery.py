#!/usr/bin/env python3
"""Check project-discoverable Agent Skills and optional Windows installation."""
from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    "project-brain-os": "SKILL.md",
    "marketing-brain": "knowledge/marketing/SKILL.md",
    "design-intelligence": "knowledge/ui-ux-frontend/SKILL.md",
    "video-production": "knowledge/video-production/SKILL.md",
    "graphic-art-direction": "knowledge/graphic-design/SKILL.md",
    "expert-evidence-review": "patterns/EXPERT_EVIDENCE_PROTOCOL.md",
}
for folder in (".agents/skills", ".claude/skills"):
    for name, target in SKILLS.items():
        if folder == ".agents/skills" and name in {"graphic-art-direction", "expert-evidence-review"}:
            pass  # existing adapters must still be validated
        path = ROOT / folder / name / "SKILL.md"
        content = path.read_text(encoding="utf-8")
        assert content.startswith("---\n"), path
        assert re.search(r"^name:\s*" + re.escape(name) + r"\s*$", content, re.M), path
        assert re.search(r"^description:\s*\S.+$", content, re.M), path
        for link in re.findall(r"\]\((\.\./[^)#]+)\)", content):
            assert (path.parent / link).resolve().is_file(), (path, link)
        assert (ROOT / target).is_file(), target
path = ROOT / ".claude/skills/find-skills/SKILL.md"
assert path.is_file()
assert (ROOT / ".agents/skills/find-skills/SKILL.md").is_file()
parser = argparse.ArgumentParser()
parser.add_argument("--installed", type=Path)
args = parser.parse_args()
if args.installed:
    for home_dir in (".agents/skills", ".claude/skills"):
        for name in SKILLS:
            skill = args.installed / home_dir / name / "SKILL.md"
            data = skill.read_text(encoding="utf-8")
            assert "managed-by: project-brain-os-install-user-skills" in data, skill
            assert (str(ROOT) in data), skill
print("BRAIN_SKILLS_DISCOVERY_PASS")
