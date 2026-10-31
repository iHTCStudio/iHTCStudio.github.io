#!/usr/bin/env python3
"""Sync App Store screenshot URLs into _data/app_screenshots.yml.

Fetches three locale-specific sets aligned with site languages:
  en     → US storefront, en-US catalog locale
  zh-CN  → CN storefront, zh-Hans-CN catalog locale
  zh-TW  → TW storefront, zh-Hant-TW catalog locale

Primary source: apps.apple.com Catalog API (customScreenshotsByType).
Fallback: iTunes Lookup API (screenshotUrls / ipadScreenshotUrls).

Regenerate: python3 scripts/sync_app_screenshots.py
"""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPS_PATH = ROOT / "_data" / "apps.yml"
SCREENSHOTS_PATH = ROOT / "_data" / "app_screenshots.yml"

CATALOG_BASE = "https://apps.apple.com/api/apps/v1/catalog"

IPHONE_SHOT_ORDER = ("iphone_6_5", "iphone_d74", "iphone6+", "iphone6", "iphone5", "iphone_5_8")
IPAD_SHOT_ORDER = ("ipadPro_2018", "ipadPro", "ipad")
MAC_SHOT_ORDER = ("mac",)

DISPLAY_WIDTH = 480
FULL_WIDTH = 1290

SITE_LANGS = ("en", "zh-CN", "zh-TW")

LANG_PROFILES: dict[str, dict[str, object]] = {
    "en": {
        "catalog_region": "us",
        "catalog_locale": "en-US",
        "lookup_regions": ("us", "sg", "jp"),
    },
    "zh-CN": {
        "catalog_region": "cn",
        "catalog_locale": "zh-Hans-CN",
        "lookup_regions": ("cn", "hk"),
    },
    "zh-TW": {
        "catalog_region": "tw",
        "catalog_locale": "zh-Hant-TW",
        "lookup_regions": ("tw", "hk", "cn"),
    },
}

CATALOG_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
    ),
    "Accept": "*/*",
    "Referer": "https://apps.apple.com/",
    "x-apple-client-version": "2624.6.0-external",
}


def parse_apps(text: str) -> list[dict]:
    blocks = re.split(r"(?:^|\n)- id: ", text)
    apps: list[dict] = []
    for block in blocks:
        if not block.strip():
            continue
        app_id = block.split("\n", 1)[0].strip()
        apple_match = re.search(r"apple_id:\s*(\d+)", block)
        platforms_match = re.search(r"platforms:\s*\[(.*?)\]", block, re.S)
        platforms: list[str] = []
        if platforms_match:
            platforms = [
                p.strip().strip('"').strip("'")
                for p in platforms_match.group(1).split(",")
                if p.strip()
            ]
        apps.append(
            {
                "id": app_id,
                "apple_id": apple_match.group(1) if apple_match else None,
                "platforms": platforms,
            }
        )
    return apps


def infer_catalog_platforms(platforms: list[str]) -> list[str]:
    names = {p.lower() for p in platforms}
    result: list[str] = []
    if "iphone" in names:
        result.append("iphone")
    if "ipad" in names:
        result.append("ipad")
    if "mac" in names:
        result.append("mac")
    if not result:
        result.append("iphone")
    return result


def http_json(url: str, headers: dict[str, str] | None = None, timeout: int = 45) -> dict | None:
    req = urllib.request.Request(url, headers=headers or {"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.load(resp)
    except (urllib.error.HTTPError, urllib.error.URLError, json.JSONDecodeError, TimeoutError):
        return None


def find_custom_screenshots_by_type(obj: object) -> dict[str, list[dict]] | None:
    if isinstance(obj, dict):
        raw = obj.get("customScreenshotsByType")
        if isinstance(raw, dict):
            result: dict[str, list[dict]] = {}
            for key, value in raw.items():
                if isinstance(value, list) and value:
                    result[key] = value
            if result:
                return result
        for value in obj.values():
            found = find_custom_screenshots_by_type(value)
            if found:
                return found
    elif isinstance(obj, list):
        for item in obj:
            found = find_custom_screenshots_by_type(item)
            if found:
                return found
    return None


def int_value(value: object) -> int:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    return 0


def resolve_template_url(
    template: str,
    native_width: int,
    native_height: int,
    target_width: int,
) -> str:
    if "{" not in template:
        return template
    width = max(1, target_width)
    if native_width > 0 and native_height > 0:
        height = max(1, int(round(width * native_height / native_width)))
    else:
        height = width
    fmt = "png" if ".png" in template.lower() else "jpg"
    return (
        template.replace("{w}", str(width))
        .replace("{h}", str(height))
        .replace("{c}", "bb")
        .replace("{f}", fmt)
    )


def pick_assets(
    by_type: dict[str, list[dict]],
    priority: tuple[str, ...],
    key_filter,
) -> list[dict]:
    for key in priority:
        items = by_type.get(key)
        if items:
            return items
    for key in sorted(by_type):
        if key_filter(key) and by_type.get(key):
            return by_type[key]
    return []


def parse_catalog_assets(items: list[dict]) -> list[dict]:
    shots: list[dict] = []
    for item in items:
        template = item.get("url") or item.get("template")
        if not template or not isinstance(template, str):
            continue
        native_w = int_value(item.get("width"))
        native_h = int_value(item.get("height"))
        full_w = native_w if native_w > 0 else FULL_WIDTH
        url = resolve_template_url(template, native_w, native_h, DISPLAY_WIDTH)
        full = resolve_template_url(template, native_w, native_h, full_w)
        shots.append(
            {
                "url": url,
                "full": full,
                "width": native_w,
                "height": native_h,
            }
        )
    return shots


def parse_catalog_response(data: dict) -> dict[str, list[dict]] | None:
    items = data.get("data")
    if not isinstance(items, list) or not items:
        return None
    attrs = items[0].get("attributes")
    if not isinstance(attrs, dict):
        return None
    by_type = find_custom_screenshots_by_type(attrs)
    if not by_type:
        return None

    bundle: dict[str, list[dict]] = {}
    iphone_items = pick_assets(
        by_type,
        IPHONE_SHOT_ORDER,
        lambda k: k.lower().startswith("iphone"),
    )
    ipad_items = pick_assets(
        by_type,
        IPAD_SHOT_ORDER,
        lambda k: k.lower().startswith("ipad"),
    )
    mac_items = pick_assets(
        by_type,
        MAC_SHOT_ORDER,
        lambda k: k.lower().startswith("mac"),
    )
    if iphone_items:
        bundle["iphone"] = parse_catalog_assets(iphone_items)
    if ipad_items:
        bundle["ipad"] = parse_catalog_assets(ipad_items)
    if mac_items:
        bundle["mac"] = parse_catalog_assets(mac_items)
    return bundle or None


def fetch_catalog_bundle(
    apple_id: str,
    platform: str,
    region: str,
    locale: str,
) -> dict[str, list[dict]] | None:
    url = (
        f"{CATALOG_BASE}/{region}/apps/{apple_id}"
        f"?platform={platform}&extend=customScreenshotsByType&l={locale}"
    )
    data = http_json(url, CATALOG_HEADERS)
    if not data:
        return None
    return parse_catalog_response(data)


def upscale_itunes_url(url: str, target_width: int) -> tuple[str, str, int, int]:
    match = re.search(r"/(\d+)x(\d+)(bb|sr)\.(png|jpe?g|webp)$", url, re.I)
    if not match:
        height = int(target_width * 19.5 / 9)
        return url, url, target_width, height
    src_w, src_h = int(match.group(1)), int(match.group(2))
    ratio = src_h / src_w if src_w else 19.5 / 9
    new_h = max(1, int(round(target_width * ratio)))
    suffix = match.group(3)
    ext = match.group(4)
    display_h = max(1, int(round(DISPLAY_WIDTH * ratio)))
    display = re.sub(
        rf"/{src_w}x{src_h}{suffix}\.{ext}$",
        f"/{DISPLAY_WIDTH}x{display_h}{suffix}.{ext}",
        url,
        flags=re.I,
    )
    full = re.sub(
        rf"/{src_w}x{src_h}{suffix}\.{ext}$",
        f"/{target_width}x{new_h}{suffix}.{ext}",
        url,
        flags=re.I,
    )
    return display, full, target_width, new_h


def parse_itunes_urls(urls: list[str]) -> list[dict]:
    shots: list[dict] = []
    for raw in urls:
        if not raw:
            continue
        display, full, width, height = upscale_itunes_url(raw, FULL_WIDTH)
        shots.append({"url": display, "full": full, "width": width, "height": height})
    return shots


def fetch_lookup_screenshots_for_region(apple_id: str, region: str) -> dict[str, list[dict]] | None:
    for entity in ("&entity=software", ""):
        url = f"https://itunes.apple.com/{region}/lookup?id={apple_id}{entity}"
        data = http_json(url)
        if not data or not data.get("resultCount"):
            continue
        item = data["results"][0]
        bundle: dict[str, list[dict]] = {}
        phone = parse_itunes_urls(item.get("screenshotUrls") or [])
        pad = parse_itunes_urls(item.get("ipadScreenshotUrls") or [])
        if phone:
            bundle["iphone"] = phone
        if pad:
            bundle["ipad"] = pad
        if bundle:
            return bundle
    return None


def merge_bundles(primary: dict[str, list[dict]], extra: dict[str, list[dict]]) -> dict[str, list[dict]]:
    merged = dict(primary)
    for key, shots in extra.items():
        if key not in merged or not merged[key]:
            merged[key] = shots
    return merged


def bundle_is_empty(bundle: dict[str, list[dict]] | None) -> bool:
    if not bundle:
        return True
    return all(not shots for shots in bundle.values())


def fetch_screenshots_for_lang(
    apple_id: str,
    platforms: list[str],
    lang: str,
) -> tuple[dict[str, list[dict]] | None, str, str, str | None]:
    profile = LANG_PROFILES[lang]
    catalog_platforms = infer_catalog_platforms(platforms)
    catalog_region = str(profile["catalog_region"])
    catalog_locale = str(profile["catalog_locale"])
    lookup_regions = tuple(str(r) for r in profile["lookup_regions"])  # type: ignore[arg-type]

    combined: dict[str, list[dict]] = {}
    for platform in catalog_platforms:
        bundle = fetch_catalog_bundle(apple_id, platform, catalog_region, catalog_locale)
        if bundle:
            combined = merge_bundles(combined, bundle)
        time.sleep(0.28)

    if not bundle_is_empty(combined):
        return combined, "catalog", catalog_region, None

    for region in lookup_regions:
        lookup = fetch_lookup_screenshots_for_region(apple_id, region)
        if lookup:
            return lookup, "itunes", region, None
        time.sleep(0.15)

    return None, "none", "", None


def fetch_all_lang_screenshots(
    apple_id: str,
    platforms: list[str],
) -> dict[str, dict]:
    result: dict[str, dict] = {}
    en_bundle: dict[str, list[dict]] | None = None

    for lang in SITE_LANGS:
        bundle, source, region, _ = fetch_screenshots_for_lang(apple_id, platforms, lang)
        if bundle_is_empty(bundle) and lang != "en" and en_bundle:
            result[lang] = {
                "source": result["en"]["source"],
                "region": result["en"]["region"],
                "fallback_from": "en",
                "platforms": en_bundle,
            }
            continue
        if bundle_is_empty(bundle):
            continue
        assert bundle is not None
        entry = {"source": source, "region": region, "platforms": bundle}
        result[lang] = entry
        if lang == "en":
            en_bundle = bundle
        time.sleep(0.12)

    return result


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def write_platform_shots(lines: list[str], platforms: dict[str, list[dict]]) -> None:
    for platform in ("iphone", "ipad", "mac"):
        shots = platforms.get(platform) or []
        if not shots:
            continue
        lines.append(f"    {platform}:")
        for shot in shots:
            lines.append(f"      - url: {yaml_quote(shot['url'])}")
            if shot.get("full") and shot["full"] != shot["url"]:
                lines.append(f"        full: {yaml_quote(shot['full'])}")
            if shot.get("width"):
                lines.append(f"        width: {shot['width']}")
            if shot.get("height"):
                lines.append(f"        height: {shot['height']}")


def write_screenshots_yaml(entries: dict[str, dict]) -> None:
    lines = [
        "# App Store screenshot URLs synced by scripts/sync_app_screenshots.py",
        "# Three locale sets: en (US), zh-CN (CN), zh-TW (TW) — aligned with site languages.",
        "# Primary: apps.apple.com Catalog API · Fallback: iTunes Lookup",
        "# Regenerate: python3 scripts/sync_app_screenshots.py",
        "",
    ]
    for app_id in sorted(entries.keys()):
        app_entry = entries[app_id]
        lines.append(f"{app_id}:")
        for lang in SITE_LANGS:
            lang_entry = app_entry.get(lang)
            if not lang_entry:
                continue
            lines.append(f"  {lang}:")
            lines.append(f"    source: {lang_entry['source']}")
            if lang_entry.get("region"):
                lines.append(f"    region: {lang_entry['region']}")
            if lang_entry.get("fallback_from"):
                lines.append(f"    fallback_from: {lang_entry['fallback_from']}")
            write_platform_shots(lines, lang_entry["platforms"])
        lines.append("")
    SCREENSHOTS_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    apps = parse_apps(APPS_PATH.read_text(encoding="utf-8"))
    entries: dict[str, dict] = {}
    updated = 0
    skipped = 0

    for index, app in enumerate(apps, start=1):
        app_id = app["id"]
        apple_id = app["apple_id"]
        if not apple_id:
            print(f"[{index}/{len(apps)}] skip {app_id}: no apple_id")
            skipped += 1
            continue

        print(f"[{index}/{len(apps)}] sync {app_id} ({apple_id})… ", end="", flush=True)
        lang_entries = fetch_all_lang_screenshots(apple_id, app["platforms"])
        if not lang_entries:
            print("no screenshots")
            skipped += 1
            time.sleep(0.15)
            continue

        entries[app_id] = lang_entries
        updated += 1
        parts = []
        for lang in SITE_LANGS:
            if lang not in lang_entries:
                continue
            le = lang_entries[lang]
            total = sum(len(v) for v in le["platforms"].values())
            fb = "→en" if le.get("fallback_from") else ""
            parts.append(f"{lang}={total}{fb}")
        print("ok (" + ", ".join(parts) + ")")
        time.sleep(0.2)

    write_screenshots_yaml(entries)
    print(f"\nDone: {updated} with screenshots, {skipped} skipped → {SCREENSHOTS_PATH}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted.", file=sys.stderr)
        sys.exit(130)
