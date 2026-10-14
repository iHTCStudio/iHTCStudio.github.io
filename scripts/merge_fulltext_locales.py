#!/usr/bin/env python3
"""Merge fulltext_faq_{lang}.py and fulltext_privacy_{lang}.py into _locale_sections."""
from __future__ import annotations

import importlib
import re
from pathlib import Path

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
    for lang in LANGS:
        faq_mod = importlib.import_module(f"fulltext_faq_{lang}")
        priv_mod = importlib.import_module(f"fulltext_privacy_{lang}")
        for app, body in faq_mod.FAQ.items():
            write(app, "faq", lang, body)
            n += 1
        for app, body in priv_mod.PRIVACY.items():
            write(app, "privacy", lang, body)
            n += 1
    print("merge_fulltext_locales: wrote", n, "files")


if __name__ == "__main__":
    main()
