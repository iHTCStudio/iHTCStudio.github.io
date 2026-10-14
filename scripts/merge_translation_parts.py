#!/usr/bin/env python3
"""Merge scripts/.app_locale_translations.part*.json into .app_locale_translations.json"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
merged: dict = {}
for path in sorted(ROOT.glob("scripts/.app_locale_translations.part*.json")):
    part = json.loads(path.read_text(encoding="utf-8"))
    merged.update(part)
    print("merged", path.name, len(part), "apps")
out = ROOT / "scripts/.app_locale_translations.json"
out.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")
print("total apps", len(merged))
