#!/usr/bin/env python3
"""Assemble FAQ/privacy locale files from hand-authored section fragments."""
from __future__ import annotations

import re
from pathlib import Path

from hand_sections_data import FAQ_BUILDERS, PRIVACY_BUILDERS

ROOT = Path(__file__).resolve().parents[1]
SEC = ROOT / "_locale_sections"
LANGS = ("ja", "ko", "ru", "th", "de", "fr", "tr")


def write(app: str, doc: str, lang: str, body: str) -> None:
    body = body.strip()
    body = re.sub(r"\n</section>\s*$", "", body)
    p = SEC / app / doc / f"{lang}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body + "\n", encoding="utf-8")


def main() -> None:
    n = 0
    for app, builders in FAQ_BUILDERS.items():
        for lang in LANGS:
            write(app, "faq", lang, builders[lang]())
            n += 1
    for app, builders in PRIVACY_BUILDERS.items():
        for lang in LANGS:
            write(app, "privacy", lang, builders[lang]())
            n += 1
    print("build_hand_locales_from_sections: wrote", n, "files")


if __name__ == "__main__":
    main()
