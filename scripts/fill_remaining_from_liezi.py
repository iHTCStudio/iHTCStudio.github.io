#!/usr/bin/env python3
"""Add remaining exact EN lines to partial map using iLiezi embedded alignment by normalize()."""

from __future__ import annotations

import json
import re
from pathlib import Path

import render_hand_privacy_22 as r
from fork_privacy_locales import read_sections

ROOT = Path(__file__).resolve().parents[1]
PARTIAL = ROOT / "scripts" / "_privacy_line_map_partial.json"
pat = re.compile(
    r"\b(the|and|for|your|with|when|not|We|Network|Optional|Bundled|Library|reading|study|require|ship|upload)\b",
    re.I,
)


def still_english() -> set[str]:
    need: set[str] = set()
    for app in r.APPS:
        en = [ln.rstrip() for ln in r.extract_en(app).splitlines()]
        for lang in r.LOCALES:
            path = ROOT / "_locale_sections" / app / "privacy" / f"{lang}.md"
            tr = [
                ln.rstrip()
                for ln in path.read_text(encoding="utf-8").splitlines()
                if ln.strip() != "</section>"
            ]
            for el, tl in zip(en, tr):
                if el == tl and el.strip() and pat.search(el):
                    need.add(el)
    return need


def main() -> None:
    partial: dict[str, dict[str, str]] = json.loads(PARTIAL.read_text(encoding="utf-8"))
    liezi = read_sections(ROOT / "iLiezi" / "privacy.md")
    en = liezi["en"]
    norm_map: dict[str, dict[str, str]] = {}
    for lang in r.LOCALES:
        loc = liezi[lang]
        for el, tl in zip(en, loc):
            if el.strip() and tl.strip():
                norm_map.setdefault(r.normalize(el), {})[lang] = tl.rstrip()

    added = 0
    for line in still_english():
        if line in partial and len(partial[line]) >= 7:
            continue
        norm = r.normalize(line)
        if norm in norm_map and len(norm_map[norm]) >= 7:
            partial[line] = norm_map[norm]
            added += 1

    PARTIAL.write_text(json.dumps(partial, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"fill_remaining_from_liezi: added {added} lines, partial={len(partial)}")


if __name__ == "__main__":
    main()
