#!/usr/bin/env python3
"""
Append <section lang="..."> blocks from _locale_sections/{relative_path}/{lang}.md
Example: _locale_sections/iCouplet/privacy/ko.md -> iCouplet/privacy.md
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SEC_ROOT = ROOT / "_locale_sections"
CONFIG = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
LOCALES = [x["code"] for x in CONFIG["languages"]]
NEW = [c for c in LOCALES if c not in ("en", "zh-CN", "zh-TW")]
POL = yaml.safe_load((ROOT / "_data/locale_policies.yml").read_text(encoding="utf-8"))
BRAND = set(POL.get("brand_fixed_content", []))

SECTION_BLOCK_RE = re.compile(
    r'(<section lang="(?P<lang>[^"]+)" markdown="1">\n\n)'
    r"(?P<body>.*?)"
    r"(\n</section>)",
    re.DOTALL,
)
SECTION_LANG_RE = re.compile(r'<section lang="([^"]+)"')


def append_sections(md_path: Path) -> int:
    app_id = md_path.parent.name
    if app_id in BRAND:
        return 0
    rel = md_path.relative_to(ROOT)
    key = rel.with_suffix("")  # iCouplet/privacy
    text = md_path.read_text(encoding="utf-8")
    present = set(SECTION_LANG_RE.findall(text))
    changed = 0
    chunks: list[str] = []
    for lang in NEW:
        part = SEC_ROOT / key / f"{lang}.md"
        if not part.exists():
            continue
        body = part.read_text(encoding="utf-8").strip()

        block_re = re.compile(
            rf'(<section lang="{re.escape(lang)}" markdown="1">\n\n)'
            rf".*?"
            rf"(\n</section>)",
            re.DOTALL,
        )
        def block_repl(m: re.Match[str]) -> str:
            return f"{m.group(1)}{body}{m.group(2)}"

        new_text, n = block_re.subn(block_repl, text, count=1)
        if n:
            text = new_text
            changed += 1
            continue
        if lang in present:
            continue
        chunks.append(f'\n<section lang="{lang}" markdown="1">\n\n{body}\n\n</section>\n')
        changed += 1
    if chunks:
        text = text.rstrip() + "".join(chunks)
    if changed:
        md_path.write_text(text, encoding="utf-8")
    return changed


def main() -> None:
    total = 0
    for name in ("index.md", "faq.md", "privacy.md", "url-scheme.md"):
        for path in sorted(ROOT.glob(f"**/{name}")):
            if "_locale_sections" in path.parts:
                continue
            total += append_sections(path)
    print("append_locale_sections: added", total, "sections")


if __name__ == "__main__":
    main()
