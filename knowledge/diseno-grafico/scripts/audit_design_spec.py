#!/usr/bin/env python3
"""Auditoría estática no destructiva de tokens de contraste/tamaño.

Uso: python scripts/audit_design_spec.py assets/design-spec-example.json
Este programa NO certifica cumplimiento WCAG: revisa solo datos explícitos del JSON.
"""
import argparse
import json
import re
from pathlib import Path

HEX_RE = re.compile(r"^#([0-9a-fA-F]{6})$")
THRESHOLDS = {"normal-text": 4.5, "large-text": 3.0, "non-text": 3.0}


def luminance(hexcolor):
    m = HEX_RE.match(str(hexcolor))
    if not m:
        raise ValueError(f"Color inválido {hexcolor!r}; usar #RRGGBB")
    values = [int(m.group(1)[i:i+2], 16) / 255 for i in (0, 2, 4)]
    adjusted = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in values]
    return 0.2126 * adjusted[0] + 0.7152 * adjusted[1] + 0.0722 * adjusted[2]


def ratio(fg, bg):
    a, b = luminance(fg), luminance(bg)
    return (max(a, b) + 0.05) / (min(a, b) + 0.05)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("spec", type=Path)
    args = p.parse_args()
    data = json.loads(args.spec.read_text(encoding="utf-8"))
    checks = data.get("contrast_checks", [])
    targets = data.get("pointer_targets", [])
    if not checks and not targets:
        print("SIN CONTROLES: no se encontraron contrast_checks ni pointer_targets")
        return 2
    issues = 0
    print(f"Proyecto: {data.get('project', '(sin nombre)')}")
    for chk in checks:
        typ = chk.get("type", "normal-text")
        if typ not in THRESHOLDS:
            print(f"ERROR: tipo de contraste desconocido: {typ}")
            issues += 1
            continue
        value = ratio(chk.get("foreground"), chk.get("background"))
        required = THRESHOLDS[typ]
        passed = value >= required
        issues += not passed
        print(f"{'PASS' if passed else 'FAIL'} contraste | {chk.get('name','(sin nombre)')} | {value:.2f}:1 | mínimo {required:.1f}:1")
    for target in targets:
        try:
            w, h = float(target["width_css_px"]), float(target["height_css_px"])
            passed = w >= 24 and h >= 24
            issues += not passed
            print(f"{'PASS' if passed else 'REVISAR'} tamaño de objetivo | {target.get('name','(sin nombre)')} | {w:g}×{h:g} CSS px | referencia WCAG 2.5.8: 24×24 con excepciones")
        except (KeyError, TypeError, ValueError) as e:
            issues += 1
            print(f"ERROR objetivo: {e}")
    print("ALCANCE: datos declarados; no certifica accesibilidad, no evalúa espacios entre objetivos ni excepciones WCAG.")
    print("RESULTADO:", "Sin fallos detectados en estos campos" if not issues else f"{issues} cuestiones detectadas")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
