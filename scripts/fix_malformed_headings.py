#!/usr/bin/env python3
"""Fix '# # ' / '# # #' leaked MT heading markers in locale sections."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BAD = re.compile(r"^(#{1,6})\s+#\s+")


def fix_text(text: str, locale_only: bool) -> tuple[str, int]:
    n = 0
    out: list[str] = []
    in_en = not locale_only
    for line in text.split("\n"):
        m = re.match(r'<section lang="([^"]+)"', line)
        if m:
            in_en = m.group(1) == "en"
        if (locale_only or not in_en) and m is None:
            m2 = BAD.match(line)
            if m2:
                hashes = m2.group(1)
                rest = line[m2.end() :].lstrip()
                line = f"{hashes} {rest}"
                n += 1
        out.append(line)
    return "\n".join(out), n


def main() -> None:
    total = 0
    files = 0
    for path in sorted(ROOT.glob("**/*.md")):
        if path.parts[0] == "scripts":
            continue
        text = path.read_text(encoding="utf-8")
        if "# #" not in text:
            continue
        locale_only = "_locale_sections" in path.parts
        new, n = fix_text(text, locale_only=locale_only)
        if n:
            path.write_text(new, encoding="utf-8")
            files += 1
            total += n
            print(path.relative_to(ROOT), n)
    print(f"fix_malformed_headings: {files} files, {total} lines")


if __name__ == "__main__":
    main()
