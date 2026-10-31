#!/usr/bin/env python3
"""Fork locale privacy markdown by diffing English sections and swapping translated chunks."""

from __future__ import annotations

import difflib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC_ROOT = ROOT / "_locale_sections"
LOCALES = ("ja", "ko", "ru", "th", "de", "fr", "tr")

SECTION_RE = re.compile(
    r'<section lang="([^"]+)"[^>]*>\n?(?P<body>.*?)(?=\n<section lang=|\Z)',
    re.DOTALL,
)
EN_ONLY = re.compile(
    r'<section lang="en"[^>]*>\n?(?P<body>.*?)(?=\n<section lang=|\Z)',
    re.DOTALL,
)


def read_sections(md_path: Path) -> dict[str, list[str]]:
    text = md_path.read_text(encoding="utf-8")
    out: dict[str, list[str]] = {}
    for m in SECTION_RE.finditer(text):
        out[m.group(1)] = [ln.rstrip() for ln in m.group("body").splitlines()]
    return out


def read_en_lines(app: str) -> list[str]:
    text = (ROOT / app / "privacy.md").read_text(encoding="utf-8")
    m = EN_ONLY.search(text)
    if not m:
        raise SystemExit(f"no en: {app}")
    return [ln.rstrip() for ln in m.group("body").splitlines()]


def load_chunk_trans(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def fork_lines(
    base_en: list[str],
    base_loc: list[str],
    target_en: list[str],
    chunk_trans: dict[str, dict[str, str]],
    lang: str,
) -> list[str]:
    if len(base_en) != len(base_loc):
        raise ValueError(f"base en/loc length mismatch for {lang}: {len(base_en)} vs {len(base_loc)}")
    out: list[str] = []
    sm = difflib.SequenceMatcher(None, base_en, target_en)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            out.extend(base_loc[i1:i2])
        elif tag == "replace":
            new = "\n".join(target_en[j1:j2]).strip("\n")
            if new in chunk_trans and lang in chunk_trans[new]:
                out.extend(chunk_trans[new][lang].splitlines())
            else:
                out.extend(target_en[j1:j2])
        elif tag == "insert":
            new = "\n".join(target_en[j1:j2]).strip("\n")
            if new in chunk_trans and lang in chunk_trans[new]:
                out.extend(chunk_trans[new][lang].splitlines())
            else:
                out.extend(target_en[j1:j2])
        elif tag == "delete":
            continue
    return out


def write_locale(app: str, lang: str, lines: list[str]) -> None:
    out_dir = SEC_ROOT / app / "privacy"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"{lang}.md").write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--chunks", required=True, help="JSON: en_chunk -> {locale: translated}")
    args = parser.parse_args()

    chunk_trans = load_chunk_trans(Path(args.chunks))
    base_secs = read_sections(ROOT / args.base / "privacy.md")
    base_en = read_en_lines(args.base)
    target_en = read_en_lines(args.target)

    for lang in LOCALES:
        base_loc = base_secs.get(lang)
        if not base_loc:
            raise SystemExit(f"missing embedded {lang} in {args.base}/privacy.md")
        lines = fork_lines(base_en, base_loc, target_en, chunk_trans, lang)
        write_locale(args.target, lang, lines)
        print(f"wrote {args.target} {lang} ({len(lines)} lines)")


if __name__ == "__main__":
    main()
