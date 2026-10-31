#!/usr/bin/env python3
"""Sync App Store artwork URLs from the iTunes Lookup API into _data/app_icons.yml."""

from __future__ import annotations

import json
import re
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPS_PATH = ROOT / "_data" / "apps.yml"
ICONS_PATH = ROOT / "_data" / "app_icons.yml"
LOOKUP_REGIONS = ("us", "cn", "hk", "tw", "jp", "sg")


def parse_apps(text: str) -> list[tuple[str, str | None, dict[str, str] | None]]:
    blocks = re.split(r"(?:^|\n)- id: ", text)
    apps: list[tuple[str, str | None, dict[str, str] | None]] = []
    for block in blocks:
        if not block.strip():
            continue
        app_id = block.split("\n", 1)[0].strip()
        match = re.search(r"apple_id:\s*(\d+)", block)
        apple_id = match.group(1) if match else None
        manual: dict[str, str] | None = None
        icon_url = re.search(r'^\s*icon_url:\s*"([^"]+)"', block, re.M)
        icon_url_sm = re.search(r'^\s*icon_url_sm:\s*"([^"]+)"', block, re.M)
        if icon_url:
            manual = {
                "icon_url": icon_url.group(1),
                "icon_url_sm": icon_url_sm.group(1) if icon_url_sm else "",
            }
        apps.append((app_id, apple_id, manual))
    return apps


def fetch_artwork(apple_id: str) -> dict[str, str] | None:
    for region in LOOKUP_REGIONS:
        for entity in ("&entity=software", ""):
            url = f"https://itunes.apple.com/{region}/lookup?id={apple_id}{entity}"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.load(resp)
            if not data.get("resultCount"):
                continue
            item = data["results"][0]
            artwork = {
                "icon_url": item.get("artworkUrl512", ""),
                "icon_url_sm": item.get("artworkUrl100", ""),
            }
            if artwork["icon_url"]:
                return artwork
    return None


def main() -> None:
    apps = parse_apps(APPS_PATH.read_text(encoding="utf-8"))
    lines = [
        "# App Store artwork URLs synced from the iTunes Lookup API.",
        "# Manual overrides: set icon_url / icon_url_sm in _data/apps.yml.",
        "# Regenerate: python3 scripts/sync_app_icons.py",
        "",
    ]
    updated = 0
    skipped = 0

    for app_id, apple_id, manual in apps:
        artwork: dict[str, str] | None = None
        source = ""

        if manual and manual.get("icon_url"):
            artwork = manual
            source = "manual"
        elif apple_id:
            print(f"sync {app_id} ({apple_id})… ", end="", flush=True)
            artwork = fetch_artwork(apple_id)
            if artwork and artwork.get("icon_url"):
                print("ok")
                source = "itunes"
            else:
                print("no artwork")
        else:
            print(f"skip {app_id}: no apple_id or icon_url")
            skipped += 1
            continue

        if not artwork or not artwork.get("icon_url"):
            skipped += 1
            continue

        if source == "manual":
            print(f"sync {app_id}… manual")

        lines.extend(
            [
                f"{app_id}:",
                f'  icon_url: "{artwork["icon_url"]}"',
                f'  icon_url_sm: "{artwork["icon_url_sm"]}"',
                "",
            ]
        )
        updated += 1
        if source == "itunes":
            time.sleep(0.15)

    ICONS_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nDone: {updated} updated, {skipped} skipped → {ICONS_PATH}")


if __name__ == "__main__":
    main()
