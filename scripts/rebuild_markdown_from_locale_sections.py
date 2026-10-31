#!/usr/bin/env python3
"""
Rebuild index/faq/privacy/url-scheme from en/zh sections in place + _locale_sections for 7 new langs.

Fixes duplicated locale bodies and missing/extra </section> tags from broken append history.
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

OPEN_RE = re.compile(r'<section lang="([^"]+)"[^>]*>\n\n')


def extract_bodies(text: str) -> dict[str, str]:
    """First occurrence wins per lang (strips stray </section> in body)."""
    matches = list(OPEN_RE.finditer(text))
    out: dict[str, str] = {}
    for i, m in enumerate(matches):
        lang = m.group(1)
        if lang in out:
            continue
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end]
        body = re.sub(r"</section>\s*", "", body)
        out[lang] = body.strip()
    return out


def frontmatter(text: str) -> str:
    m = OPEN_RE.search(text)
    if not m:
        return text
    return text[: m.start()].rstrip() + "\n\n"


def rebuild_file(path: Path) -> bool:
    app_id = path.parent.name
    if app_id in BRAND:
        return False
    rel = path.relative_to(ROOT)
    key = rel.with_suffix("")
    raw = path.read_text(encoding="utf-8")
    fm = frontmatter(raw)
    bodies = extract_bodies(raw)
    expected = (
        ["en", "zh-CN", "zh-TW"]
        if app_id in BRAND
        else LOCALES
    )
    for lang in NEW:
        part = SEC_ROOT / key / f"{lang}.md"
        if part.is_file():
            part_body = part.read_text(encoding="utf-8").strip()
            part_body = re.sub(r"</section>\s*", "", part_body)
            bodies[lang] = part_body.strip()
    blocks: list[str] = []
    for lang in expected:
        body = bodies.get(lang, "").strip()
        if not body:
            print("  skip missing body:", path.relative_to(ROOT), lang)
            continue
        blocks.append(f'<section lang="{lang}" markdown="1">\n\n{body}\n\n</section>')
    new_text = fm + "\n".join(blocks) + "\n"
    if new_text != raw:
        path.write_text(new_text, encoding="utf-8")
        return True
    return False


def main() -> None:
    n = 0
    for name in ("index.md", "faq.md", "privacy.md", "url-scheme.md"):
        for path in sorted(ROOT.glob(f"**/{name}")):
            if "_locale_sections" in path.parts:
                continue
            if rebuild_file(path):
                n += 1
                print("rebuilt", path.relative_to(ROOT))
    print(f"rebuild_markdown_from_locale_sections: {n} files")


if __name__ == "__main__":
    main()
