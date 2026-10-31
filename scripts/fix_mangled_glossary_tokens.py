#!/usr/bin/env python3
"""Restore mangled glossary/MT tokens in locale sections from English spans and known maps."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from _glossary_token_fix import (  # noqa: E402
    en_body_for_path,
    en_spans_for_path,
    fix_full_markdown,
    fix_locale_only_body,
    fix_line_aligned,
    spans_from_en_text,
)


def process_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    if not any(x in text for x in ("___", "__APPLE", "__ICLOUD", "_ _ _", "ZAUN", "FENCE", "ЗАБОР", "ограждения")):
        return 0
    is_locale_part = "_locale_sections" in path.parts
    if is_locale_part:
        spans = en_spans_for_path(path)
        en_body = en_body_for_path(path)
        new, total = fix_locale_only_body(text, spans, en_body=en_body)
    elif "<section lang=" in text:
        spans = spans_from_en_text(text)
        new, total = fix_full_markdown(text, spans)
        en_body = en_body_for_path(path)
        if en_body:
            for loc in ("ja", "ko", "ru", "th", "de", "fr", "tr"):
                pat = re.compile(
                    rf'(<section lang="{re.escape(loc)}"[^>]*>\n\n)(.*?)(\n</section>)',
                    re.DOTALL,
                )

                def sub(m, _sp=spans, _eb=en_body):  # type: ignore[no-untyped-def]
                    nonlocal total, new
                    aligned, c = fix_line_aligned(_eb, m.group(2), _sp)
                    total += c
                    return m.group(1) + aligned + m.group(3)

                new = pat.sub(sub, new, count=1)
    else:
        spans = en_spans_for_path(path)
        new, total = fix_locale_only_body(text, spans)
    if total and new != text:
        path.write_text(new, encoding="utf-8")
    return total


def main() -> None:
    files = 0
    reps = 0
    for base in (ROOT, ROOT / "_locale_sections"):
        for path in sorted(base.rglob("*.md")):
            n = process_file(path)
            if n:
                files += 1
                reps += n
                print(path.relative_to(ROOT), n)
    print(f"fix_mangled_glossary_tokens: {files} files, {reps} replacements")


if __name__ == "__main__":
    main()
