#!/usr/bin/env python3
"""Write _locale_sections/{App}/{doc}/{locale}.md from English <section lang="en"> bodies."""

from __future__ import annotations

import argparse
import re
import sys
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SEC_ROOT = ROOT / "_locale_sections"
CONFIG = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
NEW_LOCALES = [
    c["code"]
    for c in CONFIG["languages"]
    if c["code"] not in ("en", "zh-CN", "zh-TW")
]
POLICIES = yaml.safe_load((ROOT / "_data/locale_policies.yml").read_text(encoding="utf-8"))
BRAND_FIXED = set(POLICIES.get("brand_fixed_content", []))

import hashlib
import json

import translators as ts

CACHE_PATH = ROOT / "scripts" / ".classics_locale_translate_cache.json"


def load_cache() -> dict[str, str]:
    if CACHE_PATH.exists():
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    return {}


def save_cache(cache: dict[str, str]) -> None:
    CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=0), encoding="utf-8")


def cache_key(dest: str, text: str) -> str:
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]
    return f"{dest}:{digest}"


def translate_text(text: str, dest: str, cache: dict[str, str]) -> str:
    if not text or not str(text).strip():
        return text
    ck = cache_key(dest, text)
    if ck in cache:
        return cache[ck]
    last_err: Exception | None = None
    for attempt in range(6):
        for translator in ("alibaba", "bing", "google"):
            try:
                time.sleep(0.25 + attempt * 0.35)
                result = ts.translate_text(
                    text,
                    translator=translator,
                    from_language="en",
                    to_language=dest,
                )
                if result:
                    cache[ck] = result
                    return result
            except Exception as e:  # noqa: BLE001
                last_err = e
                continue
    raise RuntimeError(f"translate failed ({dest}, {len(text)} chars): {last_err}")

SECTION_RE = re.compile(
    r'<section lang="en"[^>]*>\n?(?P<body>.*?)(?=\n<section lang=|\Z)',
    re.DOTALL,
)
FENCE_RE = re.compile(r"```[\s\S]*?```|`[^`\n]+`")
CHINESE_CHAR = re.compile(r"[\u4e00-\u9fff]")
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
BUNDLE_RE = re.compile(r"(Bundle ID `[^`]+`|com\.iHTCboy\.\w+|group\.com\.iHTCboy\.\w+)")

DEFAULT_APPS = [
    "iThree",
    "iRootWise",
    "iDao",
    "iYiJing",
    "iZen",
    "iSutra",
    "iPrimer",
    "iThousand",
    "iBaiJia",
    "iWuJing",
    "iSiShu",
    "iSage",
    "iPrecepts",
    "iRhyme",
    "iWuBi",
]
DOC_NAMES = ("index.md", "faq.md", "privacy.md", "url-scheme.md")


def extract_en_body(text: str) -> str | None:
    m = SECTION_RE.search(text)
    if not m:
        return None
    return m.group("body").strip("\n")


def _chunk_text(text: str, max_len: int = 1200) -> list[str]:
    if len(text) <= max_len:
        return [text]
    parts: list[str] = []
    buf = ""
    for block in text.split("\n\n"):
        piece = block if not buf else buf + "\n\n" + block
        if len(piece) > max_len and buf:
            parts.append(buf)
            buf = block
        elif len(piece) > max_len:
            parts.append(block)
            buf = ""
        else:
            buf = piece
    if buf:
        parts.append(buf)
    return parts


def translate_markdown_body(body: str, dest: str, app_id: str, cache: dict) -> str:
    fences: list[str] = []
    bundles: list[str] = []

    def stash_fence(m: re.Match) -> str:
        fences.append(m.group(0))
        return f"___FENCE_{len(fences)-1}___"

    def stash_bundle(m: re.Match) -> str:
        bundles.append(m.group(0))
        return f"___BUNDLE_{len(bundles)-1}___"

    inline_codes: list[str] = []

    def stash_inline(m: re.Match) -> str:
        inline_codes.append(m.group(0))
        return f"___INLINE_{len(inline_codes)-1}___"

    tmp = FENCE_RE.sub(stash_fence, body)
    tmp = INLINE_CODE_RE.sub(stash_inline, tmp)
    tmp = BUNDLE_RE.sub(stash_bundle, tmp)
    chunks = _chunk_text(tmp)
    translated: list[str] = []
    for chunk in chunks:
        translated.append(translate_text(chunk, dest, cache))
    result = "\n\n".join(translated)
    for i, fence in enumerate(fences):
        result = result.replace(f"___FENCE_{i}___", fence)
    for i, bundle in enumerate(bundles):
        result = result.replace(f"___BUNDLE_{i}___", bundle)
    for i, code in enumerate(inline_codes):
        result = result.replace(f"___INLINE_{i}___", code)
    result = re.sub(r"\s*</[^>\n]+>\s*\Z", "", result)
    return result.strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--app", action="append", dest="apps")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--doc", action="append", choices=DOC_NAMES)
    args = parser.parse_args()
    apps = args.apps or DEFAULT_APPS
    docs = args.doc or list(DOC_NAMES)
    cache = load_cache()
    written = 0
    skipped = 0
    for app_id in apps:
        if app_id in BRAND_FIXED:
            continue
        for doc in docs:
            src = ROOT / app_id / doc
            if not src.exists():
                continue
            en_body = extract_en_body(src.read_text(encoding="utf-8"))
            if not en_body:
                print(f"skip (no en): {src.relative_to(ROOT)}", flush=True)
                continue
            key = src.relative_to(ROOT).with_suffix("")
            out_dir = SEC_ROOT / key
            out_dir.mkdir(parents=True, exist_ok=True)
            for loc in NEW_LOCALES:
                out_path = out_dir / f"{loc}.md"
                if out_path.exists() and not args.force:
                    skipped += 1
                    continue
                print(f"{key} → {loc}", flush=True)
                body = translate_markdown_body(en_body, loc, app_id, cache)
                out_path.write_text(body.strip() + "\n", encoding="utf-8")
                written += 1
                if written % 5 == 0:
                    save_cache(cache)
                time.sleep(0.08)
    save_cache(cache)
    print(f"done: wrote {written}, skipped existing {skipped}", flush=True)


if __name__ == "__main__":
    main()
