#!/usr/bin/env python3
"""
Build _data/app_locale/{ja,ko,ru,th,de,fr,tr}.yml from English in apps.yml.
Uses deterministic rules + embedded professional translations for zh-display names.
For taglines/blurbs/highlights: translate from en (maintained in TRANSLATIONS dict).
Run: python3 scripts/generate_app_locale_overlays.py && python3 scripts/merge_app_locale_overlays.py
"""

from __future__ import annotations

import copy
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
APPS = yaml.safe_load((ROOT / "_data/apps.yml").read_text(encoding="utf-8"))
LOCALES = ["ja", "ko", "ru", "th", "de", "fr", "tr"]
OUT = ROOT / "_data" / "app_locale"
CACHE = ROOT / "scripts" / ".app_locale_translations.json"

# Populated by agent batches; script merges cache into overlay files.
if CACHE.exists():
    TRANSLATIONS: dict[str, dict[str, dict]] = json.loads(CACHE.read_text(encoding="utf-8"))
else:
    TRANSLATIONS = {}


def overlay_for_locale(locale: str) -> dict:
    out: dict = {}
    for app in APPS:
        aid = app["id"]
        block = TRANSLATIONS.get(aid, {}).get(locale)
        if not block:
            continue
        out[aid] = block
    return out


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for loc in LOCALES:
        data = overlay_for_locale(loc)
        path = OUT / f"{loc}.yml"
        path.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")
        print(loc, "apps", len(data))


if __name__ == "__main__":
    main()
