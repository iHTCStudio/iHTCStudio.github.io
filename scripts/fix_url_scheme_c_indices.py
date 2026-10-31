#!/usr/bin/env python3
"""Restore C0/C1/… inline placeholders in url-scheme locale section files."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC = ROOT / "_locale_sections"
sys.path.insert(0, str(ROOT / "scripts"))
from _glossary_token_fix import en_spans_for_path  # noqa: E402

C_IDX = re.compile(r"\s+C(\d+)\s+")


def fix_file(path: Path) -> int:
    spans = en_spans_for_path(path)
    if not spans:
        return 0
    text = path.read_text(encoding="utf-8")
    n = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal n
        idx = int(m.group(1))
        if idx < len(spans):
            n += 1
            return f" {spans[idx]} "
        return m.group(0)

    new = C_IDX.sub(repl, text)
    if n and new != text:
        path.write_text(new, encoding="utf-8")
    return n


def main() -> None:
    files = 0
    reps = 0
    for path in sorted(SEC.glob("*/url-scheme/*.md")):
        n = fix_file(path)
        if n:
            files += 1
            reps += n
    print(f"fix_url_scheme_c_indices: {files} files, {reps} replacements")


if __name__ == "__main__":
    main()
