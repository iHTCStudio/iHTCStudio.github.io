#!/usr/bin/env python3
"""Fill _privacy_line_map_partial.json via normalized line alignment from embedded privacy sections."""

from __future__ import annotations

import json
import re
from pathlib import Path

import render_hand_privacy_22 as r

ROOT = Path(__file__).resolve().parents[1]
PARTIAL = ROOT / "scripts" / "_privacy_line_map_partial.json"
SEC_ANY = re.compile(
    r'<section lang="([^"]+)"[^>]*>\n?(?P<body>.*?)(?=\n<section lang=|\Z)',
    re.DOTALL,
)


def embedded_lines(app: str, lang: str) -> list[str]:
    text = (ROOT / app / "privacy.md").read_text(encoding="utf-8")
    for m in SEC_ANY.finditer(text):
        if m.group(1) == lang:
            return [ln.rstrip() for ln in m.group("body").splitlines()]
    raise KeyError(app, lang)


def main() -> None:
    partial: dict[str, dict[str, str]] = {}
    if PARTIAL.exists():
        partial = json.loads(PARTIAL.read_text(encoding="utf-8"))

    sources = [
        "iVirtue",
        "iLiezi",
        "iDao",
        "iLunYu",
        "iCouplet",
        "iThree",
        "iSongCi",
        "iArtOfWar",
        "iYiJing",
    ]

    norm_to_trans: dict[str, dict[str, str]] = {}
    for app in sources:
        try:
            en = embedded_lines(app, "en")
        except KeyError:
            continue
        for lang in r.LOCALES:
            try:
                loc = embedded_lines(app, lang)
            except KeyError:
                continue
            if len(en) != len(loc):
                continue
            for el, tl in zip(en, loc):
                if not el.strip() or not tl.strip():
                    continue
                norm = r.normalize(el)
                bucket = norm_to_trans.setdefault(norm, {})
                if lang not in bucket:
                    bucket[lang] = tl.rstrip()

    added = 0
    for app in r.APPS:
        en = r.extract_en(app).splitlines()
        for line in en:
            line = line.rstrip()
            if not line.strip():
                continue
            if line in partial and all(lang in partial[line] for lang in r.LOCALES):
                continue
            norm = r.normalize(line)
            if norm not in norm_to_trans:
                continue
            langs = norm_to_trans[norm]
            if len(langs) < 7:
                continue
            partial.setdefault(line, {}).update(langs)
            added += 1

    PARTIAL.write_text(json.dumps(partial, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"enrich_privacy_line_map: entries={len(partial)} new_line_keys~={added}")


if __name__ == "__main__":
    main()
