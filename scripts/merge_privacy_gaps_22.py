#!/usr/bin/env python3
"""Merge hand-maintained gap translations into _privacy_line_map_partial.json."""

from __future__ import annotations

import json
from pathlib import Path

PARTIAL = Path(__file__).resolve().parent / "_privacy_line_map_partial.json"
GAPS_PATH = Path(__file__).resolve().parent / "_privacy_gaps_22.json"


def main() -> None:
    partial: dict[str, dict[str, str]] = {}
    if PARTIAL.exists():
        partial = json.loads(PARTIAL.read_text(encoding="utf-8"))
    GAPS: dict[str, dict[str, str]] = json.loads(GAPS_PATH.read_text(encoding="utf-8"))
    added = 0
    for key, langs in GAPS.items():
        if key not in partial or len(partial.get(key, {})) < 7:
            partial[key] = langs
            added += 1
        else:
            for lang, text in langs.items():
                if not partial[key].get(lang, "").strip():
                    partial[key][lang] = text
                    added += 1
    PARTIAL.write_text(json.dumps(partial, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"merge_privacy_gaps_22: touched ~{added} entries, total={len(partial)}")


if __name__ == "__main__":
    main()
