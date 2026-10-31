#!/usr/bin/env python3
"""Remove misaligned iDao / fence artifacts from _privacy_line_map_partial.json."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTIAL = ROOT / "scripts" / "_privacy_line_map_partial.json"


def bad_value(val: dict[str, str]) -> bool:
    blob = json.dumps(val, ensure_ascii=False)
    if "iDao" in blob and "iDao" not in val.get("_en_key", ""):
        # allow if english key itself mentions iDao
        pass
    if "__FENCE" in blob:
        return True
    if "`group.com.iHTCboy.iDao`" in blob:
        return True
    return False


def main() -> None:
    partial: dict[str, dict[str, str]] = json.loads(PARTIAL.read_text(encoding="utf-8"))
    kept: dict[str, dict[str, str]] = {}
    dropped = 0
    for key, val in partial.items():
        if bad_value(val):
            dropped += 1
            continue
        if "iDao" in json.dumps(val, ensure_ascii=False) and "iDao" not in key:
            dropped += 1
            continue
        kept[key] = val
    PARTIAL.write_text(json.dumps(kept, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"sanitize_privacy_partial: kept={len(kept)} dropped={dropped}")


if __name__ == "__main__":
    main()
