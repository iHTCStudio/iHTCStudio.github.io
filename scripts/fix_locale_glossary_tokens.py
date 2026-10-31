#!/usr/bin/env python3
"""Restore glossary placeholders mangled by machine translation (all apps)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC = ROOT / "_locale_sections"
sys.path.insert(0, str(ROOT / "scripts"))
from _glossary_token_fix import en_body_for_path, en_spans_for_path, fix_locale_only_body  # noqa: E402


def main() -> None:
    n_files = 0
    for path in sorted(SEC.rglob("*.md")):
        old = path.read_text(encoding="utf-8")
        if "___" not in old and "_ _ _" not in old:
            continue
        spans = en_spans_for_path(path)
        en_body = en_body_for_path(path)
        new, _ = fix_locale_only_body(old, spans, en_body=en_body)
        new = (
            new.replace("iMessage", "iMusic")
            .replace("“", '"')
            .replace("”", '"')
            .replace("‘", "'")
            .replace("’", "'")
        )
        if new != old:
            path.write_text(new, encoding="utf-8")
            n_files += 1
    print("fix_locale_glossary_tokens: updated", n_files, "files")


if __name__ == "__main__":
    main()
