#!/usr/bin/env python3
"""
Write _locale_sections/{App}/{page}/{locale}.md from English <section lang="en"> bodies.

Uses glossary-safe translation (Google → MyMemory) with scripts/.locale_translate_cache.json.
Skip existing files unless --force. Then run: python3 scripts/append_locale_sections.py
"""

from __future__ import annotations

import argparse
import re
import sys
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import translate_ui_locales as translate_ui  # noqa: E402
from translate_ui_locales import load_cache, save_cache, translate_text  # noqa: E402

CONFIG = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
NEW_LOCALES = [
    c["code"]
    for c in CONFIG["languages"]
    if c["code"] not in ("en", "zh-CN", "zh-TW")
]
SEC_ROOT = ROOT / "_locale_sections"
PAGES = ("privacy", "faq", "index", "url-scheme")

SECTION_RE = re.compile(
    r'(?P<open><section lang="(?P<lang>[^"]+)"[^>]*>\n?)'
    r"(?P<body>.*?)"
    r"(?=\n<section lang=|\Z)",
    re.DOTALL,
)
FENCE_RE = re.compile(r"```[\s\S]*?```|`[^`\n]+`")
CHINESE_CHAR = re.compile(r"[\u4e00-\u9fff]")


def extract_section(text: str, lang: str) -> str | None:
    for m in SECTION_RE.finditer(text):
        if m.group("lang") == lang:
            return m.group("body").strip()
    return None


def translate_markdown_body(body: str, dest: str, app_id: str, cache: dict[str, str]) -> str:
    fences: list[str] = []

    def stash(match: re.Match[str]) -> str:
        fences.append(match.group(0))
        return f"___FENCE_{len(fences) - 1}___"

    tmp = FENCE_RE.sub(stash, body)
    paragraphs = tmp.split("\n\n")
    out: list[str] = []
    for para in paragraphs:
        stripped = para.strip()
        if not stripped or stripped.startswith("___FENCE_"):
            out.append(para)
            continue
        if stripped.startswith("|"):
            out.append(para)
            continue
        if stripped.startswith("#"):
            out.append(translate_text(stripped, dest, cache))
            continue
        if CHINESE_CHAR.search(para) and dest not in ("zh-CN", "zh-TW"):
            ratio = len(CHINESE_CHAR.findall(para)) / max(len(para), 1)
            if ratio > 0.35 and "Bundle ID" not in para:
                out.append(para)
                continue
        out.append(translate_text(para, dest, cache))
        time.sleep(0.55)
    result = "\n\n".join(out)
    for i, fence in enumerate(fences):
        result = result.replace(f"___FENCE_{i}___", fence)
    return result


def generate_for_app(app_id: str, *, force: bool, cache: dict[str, str]) -> int:
    written = 0
    for page in PAGES:
        md_path = ROOT / app_id / f"{page}.md"
        if not md_path.exists():
            print(f"skip missing {md_path.relative_to(ROOT)}", flush=True)
            continue
        en_body = extract_section(md_path.read_text(encoding="utf-8"), "en")
        if not en_body:
            print(f"skip no en section {md_path.relative_to(ROOT)}", flush=True)
            continue
        for loc in NEW_LOCALES:
            out_path = SEC_ROOT / app_id / page / f"{loc}.md"
            if out_path.exists() and not force:
                continue
            print(f"  {app_id}/{page} → {loc}", flush=True)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            for attempt in range(6):
                try:
                    translated = translate_markdown_body(en_body, loc, app_id, cache)
                    break
                except RuntimeError as err:
                    if attempt >= 5:
                        print(f"  skip {out_path.relative_to(ROOT)}: {err}", flush=True)
                        translated = None
                        break
                    wait = 8.0 * (attempt + 1)
                    print(f"  retry in {wait:.0f}s ({err})", flush=True)
                    time.sleep(wait)
            if translated is None:
                continue
            out_path.write_text(translated.strip() + "\n", encoding="utf-8")
            written += 1
            save_cache(cache)
    return written


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("apps", nargs="*", help="App ids (default: all with index.md)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing locale files")
    parser.add_argument(
        "--provider",
        choices=("google-then-memory", "google", "memory"),
        default="google-then-memory",
        help="Translation backend (use memory when Google rate-limits)",
    )
    args = parser.parse_args()
    translate_ui._PROVIDER = args.provider
    apps = args.apps or sorted(p.parent.name for p in ROOT.glob("*/index.md"))
    cache = load_cache()
    total = 0
    for app_id in apps:
        print(f"{app_id} …", flush=True)
        total += generate_for_app(app_id, force=args.force, cache=cache)
    save_cache(cache)
    print(f"generate_locale_sections: wrote {total} file(s)", flush=True)


if __name__ == "__main__":
    main()
