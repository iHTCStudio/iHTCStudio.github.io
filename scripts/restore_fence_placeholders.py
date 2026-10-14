#!/usr/bin/env python3
"""Replace leaked ___FENCE_n___ / ___ZAUN_n___ placeholders from English inline/code spans."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from _glossary_token_fix import (  # noqa: E402
    en_spans_for_path,
    fix_body,
    fix_full_markdown,
    parent_markdown,
)

NEEDLE = ("___FENCE", "___ZAUN", "___ZAUN_", "ЗАБОР", "ограждения", "_____")


def fix_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    spans = en_spans_for_path(path)
    if not spans:
        return 0
    if "<section lang=" in text:
        new, total = fix_full_markdown(text, spans)
    else:
        new, total = fix_body(text, spans)
    if total and new != text:
        path.write_text(new, encoding="utf-8")
    return total


def main() -> None:
    fixed_files = 0
    replacements = 0
    for base in (ROOT, ROOT / "_locale_sections"):
        for path in sorted(base.rglob("*.md")):
            raw = path.read_text(encoding="utf-8")
            if not any(x in raw for x in NEEDLE):
                continue
            n = fix_file(path)
            if n:
                fixed_files += 1
                replacements += n
                print(path.relative_to(ROOT), n)
    print(f"restore_fence_placeholders: {fixed_files} files, {replacements} replacements")


if __name__ == "__main__":
    main()
