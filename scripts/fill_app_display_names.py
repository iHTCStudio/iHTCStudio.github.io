#!/usr/bin/env python3
"""Copy names.en to new locales when the app id matches the English display name."""

from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
NEW = [x["code"] for x in CONFIG["languages"] if x["code"] not in ("en", "zh-CN", "zh-TW")]

apps = yaml.safe_load((ROOT / "_data/apps.yml").read_text(encoding="utf-8"))
n = 0
for app in apps:
    names = app.setdefault("names", {})
    en = (names.get("en") or app.get("display_name") or app["id"]).strip()
    for loc in NEW:
        if names.get(loc):
            continue
        if loc in ("ja", "ko") and names.get("zh-CN"):
            names[loc] = names["zh-CN"]
        else:
            names[loc] = en
        n += 1
(ROOT / "_data/apps.yml").write_text(
    yaml.dump(apps, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8"
)
print("filled display names:", n)
