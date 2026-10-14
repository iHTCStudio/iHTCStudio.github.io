#!/usr/bin/env python3
"""Merge _data/app_locale/{locale}.yml overlays into _data/apps.yml localized fields."""

from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
APPS_PATH = ROOT / "_data" / "apps.yml"
OVERLAY_DIR = ROOT / "_data" / "app_locale"
FIELDS = ("names", "taglines", "blurbs", "highlights")


def main() -> None:
    apps = yaml.safe_load(APPS_PATH.read_text(encoding="utf-8"))
    by_id = {a["id"]: a for a in apps}
    merged = 0
    for path in sorted(OVERLAY_DIR.glob("*.yml")):
        locale = path.stem
        overlay = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for app_id, block in overlay.items():
            app = by_id.get(app_id)
            if not app:
                continue
            for field in FIELDS:
                if field not in block:
                    continue
                app.setdefault(field, {})
                val = block[field]
                if isinstance(val, dict) and locale in val:
                    app[field][locale] = val[locale]
                    merged += 1
                elif isinstance(val, list):
                    app[field][locale] = val
                    merged += 1
                elif isinstance(val, str):
                    app[field][locale] = val
                    merged += 1
    APPS_PATH.write_text(
        yaml.dump(apps, allow_unicode=True, sort_keys=False, width=120),
        encoding="utf-8",
    )
    print(f"merge_app_locale_overlays: {merged} field updates")


if __name__ == "__main__":
    main()
