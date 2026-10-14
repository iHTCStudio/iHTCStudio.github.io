#!/usr/bin/env python3
"""Fork iLiezi embedded privacy locales to each classics app via EN diff + line translation."""

from __future__ import annotations

import difflib
import re
from pathlib import Path

import render_hand_privacy_22 as r
from fork_privacy_locales import fork_lines, read_en_lines, read_sections, write_locale

ROOT = Path(__file__).resolve().parents[1]
APPS = list(r.APPS)


def build_chunk_trans(
    base_en: list[str],
    target_en: list[str],
    exact: dict[str, dict[str, str]],
) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    sm = difflib.SequenceMatcher(None, base_en, target_en)
    for tag, _i1, _i2, j1, j2 in sm.get_opcodes():
        if tag not in ("replace", "insert"):
            continue
        chunk = "\n".join(target_en[j1:j2]).strip("\n")
        if not chunk or chunk in out:
            continue
        loc: dict[str, str] = {}
        for lang in r.LOCALES:
            tr_lines = [r.translate_line(ln, lang, exact) for ln in chunk.splitlines()]
            loc[lang] = "\n".join(tr_lines)
        out[chunk] = loc
    return out


def count_untranslated(app: str, lang: str) -> int:
    en = r.extract_en(app).splitlines()
    path = ROOT / "_locale_sections" / app / "privacy" / f"{lang}.md"
    if not path.exists():
        return len(en)
    tr = path.read_text(encoding="utf-8").splitlines()
    n = 0
    for el, tl in zip(en, tr):
        el, tl = el.rstrip(), tl.rstrip()
        if el == tl and el.strip() and re.search(r"[A-Za-z]{4,}", el):
            n += 1
    return n


def main() -> None:
    exact = r.build_exact_map()
    base_en = read_en_lines("iLiezi")
    base_secs = read_sections(ROOT / "iLiezi" / "privacy.md")

    for app in APPS:
        target_en = read_en_lines(app)
        chunk_trans = build_chunk_trans(base_en, target_en, exact)
        for lang in r.LOCALES:
            base_loc = base_secs[lang]
            lines = fork_lines(base_en, base_loc, target_en, chunk_trans, lang)
            write_locale(app, lang, lines)
        miss = {lang: count_untranslated(app, lang) for lang in r.LOCALES}
        print(f"{app} untranslated (identical to EN): {miss}")


if __name__ == "__main__":
    main()
