#!/usr/bin/env python3
"""
Generate _locale_sections/{app}/{doc}/{locale}.md from English <section> bodies.
Uses deep_translator (Google → MyMemory) with glossary protection; skips existing files.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import translate_ui_locales as ui_locales  # noqa: E402
from translate_ui_locales import load_cache, save_cache, translate_text  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SEC_ROOT = ROOT / "_locale_sections"
CONFIG = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
NEW = [x["code"] for x in CONFIG["languages"] if x["code"] not in ("en", "zh-CN", "zh-TW")]
POL = yaml.safe_load((ROOT / "_data/locale_policies.yml").read_text(encoding="utf-8"))
BRAND = set(POL.get("brand_fixed_content", []))

SECTION_RE = re.compile(
    r'<section lang="en"[^>]*markdown="1"[^>]*>\s*\n(?P<body>.*?)\n\s*</section>',
    re.DOTALL,
)
SECTION_RE2 = re.compile(
    r'<section lang="en"[^>]*>\s*\n(?P<body>.*?)\n\s*</section>',
    re.DOTALL,
)
FENCE_RE = re.compile(r"```[\s\S]*?```|`[^`\n]+`")
CHINESE_CHAR = re.compile(r"[\u4e00-\u9fff]")


def translate_table_block(para: str, dest: str, cache: dict[str, str]) -> str:
    lines = para.split("\n")
    out: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            out.append(line)
            continue
        if stripped.replace("|", "").replace("-", "").replace(":", "").strip() == "":
            out.append(line)
            continue
        if "`" in stripped and "://" in stripped:
            out.append(line)
            continue
        out.append(translate_text(stripped, dest, cache))
    return "\n".join(out)


def translate_markdown_body(body: str, dest: str, app_id: str, cache: dict[str, str]) -> str:
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
        if stripped.startswith("#"):
            out_paragraphs.append(translate_text(stripped, dest, cache))
            continue
        if stripped.startswith("|"):
            out_paragraphs.append(translate_table_block(para, dest, cache))
            continue
        if stripped.startswith(">"):
            inner = stripped.lstrip(">").strip()
            out_paragraphs.append("> " + translate_text(inner, dest, cache))
            continue
        if stripped.startswith("- ") or stripped.startswith("* ") or re.match(r"^\d+\.", stripped):
            lines = para.split("\n")
            fixed: list[str] = []
            for ln in lines:
                m = re.match(r"^(\s*[-*]|\s*\d+\.)\s+(.*)$", ln)
                if m:
                    fixed.append(f"{m.group(1)} {translate_text(m.group(2), dest, cache)}")
                else:
                    fixed.append(ln)
            out_paragraphs.append("\n".join(fixed))
            continue
        if app_id.startswith("i") and CHINESE_CHAR.search(para):
            ratio = len(CHINESE_CHAR.findall(para)) / max(len(para), 1)
            if ratio > 0.35 and "Bundle ID" not in para:
                out_paragraphs.append(para)
                continue
        out_paragraphs.append(translate_text(para, dest, cache))
    result = "\n\n".join(out_paragraphs)
    for i, fence in enumerate(fences):
        result = result.replace(f"___FENCE_{i}___", fence)
    return result


def extract_en_body(md_text: str) -> str | None:
    m = SECTION_RE.search(md_text) or SECTION_RE2.search(md_text)
    return m.group("body").strip() if m else None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--apps",
        help="Comma-separated app ids (e.g. iBrowser,iMencius). Default: all apps.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing locale section files.")
    parser.add_argument(
        "--provider",
        choices=("google", "memory", "google-then-memory"),
        default="google-then-memory",
    )
    args = parser.parse_args()
    ui_locales._PROVIDER = args.provider
    app_filter: set[str] | None = None
    if args.apps:
        app_filter = {a.strip() for a in args.apps.split(",") if a.strip()}

    cache = load_cache()
    docs = ("privacy.md", "faq.md", "url-scheme.md", "index.md")
    created = 0
    skipped = 0
    for doc in docs:
        for md_path in sorted(ROOT.glob(f"**/{doc}")):
            if "_locale_sections" in md_path.parts:
                continue
            app_id = md_path.parent.name
            if app_id in BRAND:
                continue
            if app_filter is not None and app_id not in app_filter:
                continue
            rel = md_path.relative_to(ROOT)
            key = rel.with_suffix("")
            en_body = extract_en_body(md_path.read_text(encoding="utf-8"))
            if not en_body:
                continue
            for loc in NEW:
                out = SEC_ROOT / key / f"{loc}.md"
                if out.exists() and not args.force:
                    skipped += 1
                    continue
                out.parent.mkdir(parents=True, exist_ok=True)
                try:
                    translated = translate_markdown_body(en_body, loc, app_id, cache)
                except RuntimeError as err:
                    print("FAIL", out, err, flush=True)
                    save_cache(cache)
                    continue
                out.write_text(translated.strip() + "\n", encoding="utf-8")
                created += 1
                print(out.relative_to(ROOT), flush=True)
                sys.stdout.flush()
                if created % 5 == 0:
                    save_cache(cache)
    save_cache(cache)
    print(f"translate_markdown_sections: created={created} skipped={skipped}")


if __name__ == "__main__":
    main()
