#!/usr/bin/env python3
"""Contracts for reusable Video Production OS, independent of installed video software."""
import ast
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULES = [
    'README.md', 'SKILL.md', 'PRODUCTION_PLAYBOOK.md',
    'QUALITY_AND_RIGHTS.md', 'EXPERIMENTS_AND_MEASUREMENT.md',
    'TOOLS_AND_EVIDENCE.md', 'templates/CREATIVE_BRIEF.md',
    'templates/SHOTLIST.md', 'templates/EXPERIMENT_SCORECARD.md',
    'scripts/render_smoke.py',
]


class TestVideoOS(unittest.TestCase):
    def test_complete_module(self):
        for name in MODULES:
            with self.subTest(name=name):
                self.assertTrue((ROOT / name).is_file())

    def test_skill_contract(self):
        s = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        self.assertIn('version: 0.1.0', s)
        for token in ('READ_ONLY_AUDIT', 'PILOT_PRODUCTION', 'NOT_VALIDATED',
                      'Marketing Brain', 'Design Intelligence OS', 'derechos',
                      'producción', 'publicar', 'presupuesto'):
            with self.subTest(token=token):
                self.assertIn(token, s)

    def test_four_routes_and_separation_of_validations(self):
        content = (ROOT / 'PRODUCTION_PLAYBOOK.md').read_text(encoding='utf-8')
        for token in ('A. Comercial', 'B. Caricatura', 'C. Contenido natural',
                      'D. Demostración', 'NOT_VALIDATED', 'TECHNICAL_SMOKE_PASS',
                      'PILOT_QA_PASS', 'G7.'):
            with self.subTest(token=token):
                self.assertIn(token, content)

    def test_privacy_and_experiment_guards(self):
        q = (ROOT / 'QUALITY_AND_RIGHTS.md').read_text(encoding='utf-8')
        e = (ROOT / 'EXPERIMENTS_AND_MEASUREMENT.md').read_text(encoding='utf-8')
        for token in ('licencia', 'testimonios', 'ffprobe', 'subtítulos', 'FTC'):
            self.assertIn(token, q)
        for token in ('denominador', 'INSUFFICIENT_DATA', 'Ronda 0', 'Ronda 1', 'Ronda 2'):
            self.assertIn(token, e)

    def test_relative_markdown_links_and_runnable_python(self):
        for name in MODULES:
            if not name.endswith('.md'):
                continue
            text = (ROOT / name).read_text(encoding='utf-8')
            for target in re.findall(r'\]\(([^)]+)\)', text):
                if target.startswith(('https://','http://','#','mailto:')):
                    continue
                if '#' in target:
                    target = target.split('#')[0]
                self.assertTrue((ROOT / name).parent.joinpath(target).exists(),
                                f'{name} refers to missing {target}')
        ast.parse((ROOT / 'scripts/render_smoke.py').read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
