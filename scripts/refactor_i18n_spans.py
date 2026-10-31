#!/usr/bin/env python3
"""Replace en/zh-CN/zh-TW i18n span triplets with {% include i18n-spans.html %}."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TRIPLET = re.compile(
    r'<span lang="en"( class="inline")?>\{\{ site\.data\.i18n\[\'en\'\]\.([a-zA-Z0-9_]+)\.([a-zA-Z0-9_]+) \}\}</span>\s*'
    r'<span lang="zh-CN"( class="inline")?>\{\{ site\.data\.i18n\[\'zh-CN\'\]\.\2\.\3 \}\}</span>\s*'
    r'<span lang="zh-TW"( class="inline")?>\{\{ site\.data\.i18n\[\'zh-TW\'\]\.\2\.\3 \}\}</span>',
    re.MULTILINE,
)


def refactor(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    count = 0

    def repl(m: re.Match) -> str:
        nonlocal count
        count += 1
        section, key = m.group(2), m.group(3)
        inline = ' inline="true"' if m.group(1) or m.group(3) or m.group(4) else ' inline="false"'
        if inline == ' inline="true"':
            return f'{{% include i18n-spans.html section="{section}" key="{key}" %}}'
        return f'{{% include i18n-spans.html section="{section}" key="{key}" inline=false %}}'

    new = TRIPLET.sub(repl, text)
    if new != text:
        path.write_text(new, encoding="utf-8")
    return count


for rel in ("_layouts/home.html", "_includes/footer.html", "_layouts/app.html", "collections/index.html"):
    p = ROOT / rel
    if p.exists():
        n = refactor(p)
        print(rel, n, "replacements")
