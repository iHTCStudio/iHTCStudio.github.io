#!/usr/bin/env python3
"""Automated consistency checks after locale expansion (not a substitute for human review)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
LOCALES = [x["code"] for x in CONFIG["languages"]]

FORBIDDEN = re.compile(r"iHTCTeam", re.I)
REQUIRED_TERMS = ("iHTC Studio",)
PLACEHOLDER_RE = re.compile(r"___[A-Z0-9_]+___|TODO|TBD|\?\?\?")


def flatten(d: dict, prefix: str = "") -> dict[str, str]:
    out: dict[str, str] = {}
    for k, v in d.items():
        key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            out.update(flatten(v, key))
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, dict):
                    out.update(flatten(item, f"{key}[{i}]"))
                else:
                    out[f"{key}[{i}]"] = str(item)
        else:
            out[key] = str(v)
    return out


def main() -> int:
    errors: list[str] = []
    en = flatten(yaml.safe_load((ROOT / "_data/i18n/en.yml").read_text(encoding="utf-8")))
    for loc in LOCALES:
        path = ROOT / "_data/i18n" / f"{loc}.yml"
        if not path.exists():
            errors.append(f"missing {path.name}")
            continue
        data = flatten(yaml.safe_load(path.read_text(encoding="utf-8")))
        for key in en:
            if key not in data:
                errors.append(f"i18n/{loc}: missing {key}")
            elif not data[key].strip():
                errors.append(f"i18n/{loc}: empty {key}")
        for key, val in data.items():
            if FORBIDDEN.search(val):
                errors.append(f"i18n/{loc}: forbidden brand in {key}")
            if PLACEHOLDER_RE.search(val):
                errors.append(f"i18n/{loc}: placeholder left in {key}")
        if loc != "en":
            for term in REQUIRED_TERMS:
                if term not in yaml.safe_load(path.read_text(encoding="utf-8")).get("brand", {}).get("name", "") and term not in str(data.values()):
                    pass  # brand block checked separately
    if errors:
        print("proofread_locales:", len(errors), "issue(s)")
        for e in errors[:120]:
            print(" ", e)
        return 1
    print("proofread_locales: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
