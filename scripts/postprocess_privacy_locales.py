#!/usr/bin/env python3
"""Fill remaining English lines in _locale_sections privacy files via line map + templates."""

from __future__ import annotations

import re
from pathlib import Path

import render_hand_privacy_22 as r

ROOT = Path(__file__).resolve().parents[1]
SEC_ROOT = ROOT / "_locale_sections"


def main() -> None:
    exact = r.build_exact_map()
    fixed = 0
    for app in r.APPS:
        en_lines = [ln.rstrip() for ln in r.extract_en(app).splitlines()]
        for lang in r.LOCALES:
            path = SEC_ROOT / app / "privacy" / f"{lang}.md"
            if not path.exists():
                continue
            tr_lines = [
                ln.rstrip()
                for ln in path.read_text(encoding="utf-8").splitlines()
                if ln.strip() != "</section>"
            ]
            out: list[str] = []
            for i, el in enumerate(en_lines):
                tl = tr_lines[i] if i < len(tr_lines) else el
                if tl == el and el.strip():
                    cand = r.translate_line(el, lang, exact)
                    if cand != el:
                        tl = cand
                        fixed += 1
                out.append(tl)
            path.write_text("\n".join(out).strip() + "\n", encoding="utf-8")
    print(f"postprocess_privacy_locales: fixed {fixed} lines")


if __name__ == "__main__":
    main()
