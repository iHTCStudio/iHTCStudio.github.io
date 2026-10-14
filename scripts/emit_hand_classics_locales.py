#!/usr/bin/env python3
"""
Emit hand-maintained FAQ & privacy locale bodies for 11 apps.
Translations are authored in scripts/hand_classics_locale_data.py (no MT APIs).
"""
from __future__ import annotations

import re
from pathlib import Path

from hand_classics_locale_data import FAQ, PRIVACY

ROOT = Path(__file__).resolve().parents[1]
SEC = ROOT / "_locale_sections"
LANGS = ("ja", "ko", "ru", "th", "de", "fr", "tr")
APPS = (
    "iBaiJia",
    "iGuanZhi",
    "iGuige",
    "iHanFei",
    "iLiezi",
    "iLvShi",
    "iMencius",
    "iMoZi",
    "iPrimer",
    "iRhyme",
    "iSage",
)


def write(app: str, doc: str, lang: str, body: str) -> None:
    body = body.strip()
    body = re.sub(r"\n</section>\s*$", "", body)
    p = SEC / app / doc / f"{lang}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body + "\n", encoding="utf-8")


def main() -> None:
    n = 0
    for app in APPS:
        for lang in LANGS:
            if faq := FAQ.get(app, {}).get(lang):
                write(app, "faq", lang, faq)
                n += 1
            if priv := PRIVACY.get(app, {}).get(lang):
                write(app, "privacy", lang, priv)
                n += 1
    print("emit_hand_classics_locales: wrote", n, "files")


if __name__ == "__main__":
    main()
