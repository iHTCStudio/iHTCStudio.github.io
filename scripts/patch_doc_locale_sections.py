#!/usr/bin/env python3
"""Replace or append <section lang="..."> bodies from _locale_sections into doc markdown."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC_ROOT = ROOT / "_locale_sections"
LANGS = ("ja", "ko", "ru", "th", "de", "fr", "tr")

SECTION_RE = re.compile(
    r'(<section lang="(?P<lang>[^"]+)" markdown="1">\n\n)'
    r"(?P<body>.*?)"
    r"(\n</section>)",
    re.DOTALL,
)


def patch_file(md_path: Path) -> int:
    rel = md_path.relative_to(ROOT)
    key = rel.with_suffix("")
    text = md_path.read_text(encoding="utf-8")
    changed = 0
    for lang in LANGS:
        part = SEC_ROOT / key / f"{lang}.md"
        if not part.exists():
            continue
        body = part.read_text(encoding="utf-8").strip()
        if f'<section lang="{lang}"' in text:

            def repl(m: re.Match[str]) -> str:
                if m.group("lang") != lang:
                    return m.group(0)
                return f'{m.group(1)}{body}{m.group(3)}'

            text, n = SECTION_RE.subn(repl, text, count=1)
            if n:
                changed += 1
        else:
            text = text.rstrip() + f'\n<section lang="{lang}" markdown="1">\n\n{body}\n\n</section>\n'
            changed += 1
    if changed:
        md_path.write_text(text, encoding="utf-8")
    return changed


def main() -> None:
    apps = sys.argv[1:] if len(sys.argv) > 1 else None
    total = 0
    for name in ("faq.md", "privacy.md"):
        for path in sorted(ROOT.glob(f"**/{name}")):
            if "_locale_sections" in path.parts:
                continue
            if apps and path.parent.name not in apps:
                continue
            total += patch_file(path)
    print("patch_doc_locale_sections: updated", total, "sections")


if __name__ == "__main__":
    main()
