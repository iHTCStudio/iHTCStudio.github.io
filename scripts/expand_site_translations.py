#!/usr/bin/env python3
"""
Expand apps.yml, collections.yml, and markdown sections to all site locales.

Uses en (or existing zh) as source, glossary-safe machine translation, and
skips brand-fixed apps (Weber, GLUT) for new markdown sections.
"""

from __future__ import annotations

import copy
import re
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
LOCALES = [x["code"] for x in CONFIG["languages"]]
NEW_LOCALES = [c for c in LOCALES if c not in ("en", "zh-CN", "zh-TW")]
POLICIES = yaml.safe_load((ROOT / "_data/locale_policies.yml").read_text(encoding="utf-8"))
BRAND_FIXED = set(POLICIES.get("brand_fixed_content", []))

from translate_ui_locales import GLOSSARY, protect, restore, translate_text  # noqa: E402

SECTION_RE = re.compile(
    r'(?P<open><section lang="(?P<lang>[^"]+)"[^>]*>\n?)'
    r"(?P<body>.*?)"
    r"(?=\n<section lang=|\Z)",
    re.DOTALL,
)

FENCE_RE = re.compile(r"```[\s\S]*?```|`[^`\n]+`")
CHINESE_CHAR = re.compile(r"[\u4e00-\u9fff]")


def translate_markdown_body(body: str, dest: str, app_id: str) -> str:
    """Translate prose but preserve fenced code and most Chinese literals in classical apps."""
    fences: list[str] = []

    def stash(m: re.Match) -> str:
        fences.append(m.group(0))
        return f"___FENCE_{len(fences)-1}___"

    tmp = FENCE_RE.sub(stash, body)
    paragraphs = tmp.split("\n\n")
    out_paragraphs: list[str] = []
    for para in paragraphs:
        stripped = para.strip()
        if not stripped or stripped.startswith("___FENCE_"):
            out_paragraphs.append(para)
            continue
        if stripped.startswith("|") or stripped.startswith("#"):
            # Tables / headings: translate heading text only on # lines
            if stripped.startswith("#"):
                out_paragraphs.append(translate_text(stripped, dest))
            else:
                out_paragraphs.append(para)
            continue
        # Keep paragraph if mostly Chinese tokens in input apps (optional minimal change)
        if app_id.startswith("i") and CHINESE_CHAR.search(para) and dest not in ("zh-CN", "zh-TW"):
            ratio = len(CHINESE_CHAR.findall(para)) / max(len(para), 1)
            if ratio > 0.35 and "Bundle ID" not in para:
                out_paragraphs.append(para)
                continue
        out_paragraphs.append(translate_text(para, dest))
    result = "\n\n".join(out_paragraphs)
    for i, fence in enumerate(fences):
        result = result.replace(f"___FENCE_{i}___", fence)
    return result


def expand_localized_block(block: dict, dest: str, *, copy_name: bool = False) -> None:
    if dest in block and block[dest]:
        return
    src = block.get("en") or block.get("zh-CN") or next(iter(block.values()), "")
    if copy_name or (isinstance(src, str) and src.startswith("i") and src[1:2].isupper()):
        block[dest] = copy.deepcopy(src)
        return
    if isinstance(src, list):
        block[dest] = [translate_text(x, dest) for x in src]
    else:
        block[dest] = translate_text(str(src), dest)


def expand_apps() -> None:
    path = ROOT / "_data/apps.yml"
    apps = yaml.safe_load(path.read_text(encoding="utf-8"))
    for app in apps:
        app_id = app["id"]
        for field in ("names", "taglines", "blurbs", "highlights"):
            block = app.setdefault(field, {})
            for loc in NEW_LOCALES:
                expand_localized_block(block, loc, copy_name=(field == "names"))
    path.write_text(yaml.dump(apps, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")
    print("expanded apps.yml", flush=True)


def expand_collections() -> None:
    path = ROOT / "_data/collections.yml"
    cols = yaml.safe_load(path.read_text(encoding="utf-8"))
    for col in cols:
        for field in ("names", "taglines"):
            block = col.setdefault(field, {})
            for loc in NEW_LOCALES:
                expand_localized_block(block, loc)
    path.write_text(yaml.dump(cols, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")
    print("expanded collections.yml", flush=True)


def expand_markdown(path: Path) -> bool:
    app_id = path.parent.name
    if app_id in BRAND_FIXED:
        return False
    text = path.read_text(encoding="utf-8")
    matches = list(SECTION_RE.finditer(text))
    if not matches:
        return False
    existing = {m.group("lang") for m in matches}
    if all(loc in existing for loc in LOCALES):
        return False
    en_body = None
    for m in matches:
        if m.group("lang") == "en":
            en_body = m.group("body")
            break
    if en_body is None:
        return False
    additions = []
    for loc in NEW_LOCALES:
        if loc in existing:
            continue
        print(f"  {path.relative_to(ROOT)} → {loc}", flush=True)
        body = translate_markdown_body(en_body, loc, app_id)
        additions.append(f'<section lang="{loc}" markdown="1">\n{body}\n</section>\n')
        time.sleep(0.05)
    if not additions:
        return False
    path.write_text(text.rstrip() + "\n\n" + "\n".join(additions) + "\n", encoding="utf-8")
    return True


def expand_all_markdown() -> None:
    patterns = ["**/index.md", "**/faq.md", "**/privacy.md", "**/url-scheme.md"]
    changed = 0
    for pattern in patterns:
        for path in sorted(ROOT.glob(pattern)):
            if "node_modules" in path.parts:
                continue
            if expand_markdown(path):
                changed += 1
    print(f"markdown files updated: {changed}", flush=True)


def main() -> None:
    expand_apps()
    expand_collections()
    expand_all_markdown()


if __name__ == "__main__":
    main()
