#!/usr/bin/env python3
"""Validate locale coverage for site data and markdown sections."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
I18N_DIR = ROOT / "_data" / "i18n"
CONFIG = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
LOCALES = [x["code"] for x in CONFIG.get("languages", [])]
POLICIES = yaml.safe_load((ROOT / "_data/locale_policies.yml").read_text(encoding="utf-8"))
BRAND_FIXED = set(POLICIES.get("brand_fixed_content", []))

SECTION_RE = re.compile(
    r'<section lang="(?P<lang>[^"]+)"[^>]*>',
    re.MULTILINE,
)

LOCALIZED_KEYS = ("names", "taglines", "blurbs", "highlights")


def load_i18n_keys() -> dict[str, set[str]]:
    def flatten(d: dict, prefix: str = "") -> set[str]:
        keys: set[str] = set()
        for k, v in d.items():
            path = f"{prefix}.{k}" if prefix else k
            if isinstance(v, dict):
                keys |= flatten(v, path)
            else:
                keys.add(path)
        return keys

    out: dict[str, set[str]] = {}
    for path in I18N_DIR.glob("*.yml"):
        code = path.stem
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        out[code] = flatten(data)
    return out


def check_i18n(keys_by_locale: dict[str, set[str]]) -> list[str]:
    errors: list[str] = []
    base = keys_by_locale.get("en", set())
    for code in LOCALES:
        if code not in keys_by_locale:
            errors.append(f"missing _data/i18n/{code}.yml")
            continue
        missing = base - keys_by_locale[code]
        extra = keys_by_locale[code] - base
        if missing:
            errors.append(f"i18n/{code}: missing keys vs en: {sorted(missing)[:8]}… ({len(missing)} total)")
        if extra:
            errors.append(f"i18n/{code}: extra keys vs en: {sorted(extra)[:8]}… ({len(extra)} total)")
    return errors


def check_apps() -> list[str]:
    apps = yaml.safe_load((ROOT / "_data/apps.yml").read_text(encoding="utf-8"))
    errors: list[str] = []
    for app in apps:
        app_id = app["id"]
        for field in LOCALIZED_KEYS:
            block = app.get(field)
            if not isinstance(block, dict):
                errors.append(f"apps.yml {app_id}: missing {field}")
                continue
            for loc in LOCALES:
                if loc not in block or block[loc] in (None, ""):
                    errors.append(f"apps.yml {app_id}.{field}.{loc} empty")
    return errors


def check_collections() -> list[str]:
    cols = yaml.safe_load((ROOT / "_data/collections.yml").read_text(encoding="utf-8"))
    errors: list[str] = []
    for col in cols:
        cid = col.get("id", "?")
        for field in ("names", "taglines"):
            block = col.get(field, {})
            for loc in LOCALES:
                if loc not in block or not str(block[loc]).strip():
                    errors.append(f"collections.yml {cid}.{field}.{loc} empty")
    return errors


def expected_langs_for_app(app_id: str) -> list[str]:
    if app_id in BRAND_FIXED:
        return ["en", "zh-CN", "zh-TW"]
    return LOCALES


def check_markdown() -> list[str]:
    errors: list[str] = []
    for path in ROOT.glob("**/index.md"):
        errors.extend(_check_md(path))
    for name in ("faq.md", "privacy.md", "url-scheme.md"):
        for path in ROOT.glob(f"**/{name}"):
            errors.extend(_check_md(path))
    return errors


def _check_md(path: Path) -> list[str]:
    errors: list[str] = []
    app_id = path.parts[-2] if path.parts[-2] != ROOT.name else ""
    text = path.read_text(encoding="utf-8")
    langs = SECTION_RE.findall(text)
    if not langs:
        return errors
    expected = expected_langs_for_app(app_id)
    present = set(langs)
    for loc in expected:
        if loc not in present:
            errors.append(f"{path.relative_to(ROOT)}: missing section lang={loc}")
    return errors


def main() -> int:
    errors: list[str] = []
    errors.extend(check_i18n(load_i18n_keys()))
    if (ROOT / "_data/apps.yml").exists():
        errors.extend(check_apps())
    if (ROOT / "_data/collections.yml").exists():
        errors.extend(check_collections())
    errors.extend(check_markdown())

    if errors:
        print(f"validate_locales: {len(errors)} issue(s)")
        for e in errors[:200]:
            print(" ", e)
        if len(errors) > 200:
            print(f"  … and {len(errors) - 200} more")
        return 1
    print("validate_locales: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
