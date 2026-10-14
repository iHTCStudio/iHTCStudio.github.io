#!/usr/bin/env python3
"""Render _locale_sections/{App}/faq/{locale}.md from English FAQ (line map + templates)."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC_ROOT = ROOT / "_locale_sections"
LOCALES = ("ja", "ko", "ru", "th", "de", "fr", "tr")
APPS = (
    "iBaiJia",
    "iGuanZhi",
    "iGuige",
    "iHanFei",
    "iLiezi",
    "iLvShi",
    "iMencius",
    "iMoZi",
    "iPrimer",
    "iRhyme",
    "iSage",
)

SECTION_RE = re.compile(
    r'<section lang="en"[^>]*>\n?(?P<body>.*?)(?=\n<section lang=|\Z)',
    re.DOTALL,
)
SEC_ANY = re.compile(
    r'<section lang="([^"]+)"[^>]*>\n?(?P<body>.*?)(?=\n<section lang=|\Z)',
    re.DOTALL,
)


def extract_en(app: str) -> str:
    text = (ROOT / app / "faq.md").read_text(encoding="utf-8")
    m = SECTION_RE.search(text)
    if not m:
        raise SystemExit(f"no en section: {app}")
    return m.group("body").strip()


def build_exact_map() -> dict[str, dict[str, str]]:
    exact: dict[str, dict[str, str]] = {}

    def ingest(sections: dict[str, list[str]]) -> None:
        en = sections.get("en")
        if not en:
            return
        for lang in LOCALES:
            tr = sections.get(lang)
            if not tr or len(tr) != len(en):
                continue
            for el, tl in zip(en, tr):
                el, tl = el.rstrip(), tl.rstrip()
                if el.strip() and tl.strip() and el != tl:
                    exact.setdefault(el, {})[lang] = tl

    for p in ROOT.glob("**/faq.md"):
        if "_locale_sections" in p.parts or p.parent.name in APPS:
            continue
        sections: dict[str, list[str]] = {}
        for m in SEC_ANY.finditer(p.read_text(encoding="utf-8")):
            sections[m.group(1)] = m.group("body").strip().splitlines()
        ingest(sections)

    for loc in SEC_ROOT.glob("*/faq/*.md"):
        app = loc.parent.parent.name
        lang = loc.stem
        if app in APPS or lang not in LOCALES:
            continue
        main = ROOT / app / "faq.md"
        if not main.exists():
            continue
        en_m = SECTION_RE.search(main.read_text(encoding="utf-8"))
        if not en_m:
            continue
        en_lines = en_m.group("body").strip().splitlines()
        tr_lines = loc.read_text(encoding="utf-8").strip().splitlines()
        tr_lines = [x for x in tr_lines if x.strip() != "</section>"]
        if len(en_lines) != len(tr_lines):
            continue
        for el, tl in zip(en_lines, tr_lines):
            el, tl = el.rstrip(), tl.rstrip()
            if el.strip() and tl.strip() and el != tl:
                exact.setdefault(el, {})[lang] = tl

    partial = ROOT / "scripts" / "_faq_line_map_partial.json"
    if partial.exists():
        data = json.loads(partial.read_text(encoding="utf-8"))
        for el, langs in data.items():
            for lang, tl in langs.items():
                if lang in LOCALES and tl.strip():
                    exact.setdefault(el, {})[lang] = tl.rstrip()

    sys_path = ROOT / "scripts"
    if str(sys_path) not in __import__("sys").path:
        __import__("sys").path.insert(0, str(sys_path))
    import hand_faq_line_ext as ext  # noqa: WPS433

    ext.merge_into(exact)

    return exact


def translate_line(line: str, lang: str, exact: dict[str, dict[str, str]]) -> str:
    if line in exact and lang in exact[line]:
        return exact[line][lang]
    return line


def render_app(app: str, exact: dict[str, dict[str, str]]) -> dict[str, list[str]]:
    en_lines = [x for x in extract_en(app).splitlines() if x.strip() != "</section>"]
    out: dict[str, list[str]] = {loc: [] for loc in LOCALES}
    missing: dict[str, int] = {loc: 0 for loc in LOCALES}
    for line in en_lines:
        for loc in LOCALES:
            tr = translate_line(line, loc, exact)
            if tr == line and line.strip() and re.search(r"[A-Za-z]{4,}", line):
                missing[loc] += 1
            out[loc].append(tr)
    if any(missing.values()):
        print(f"  {app} faq untranslated:", missing)
    return out


def main() -> None:
    exact = build_exact_map()
    n = 0
    for app in APPS:
        print("faq", app)
        by_lang = render_app(app, exact)
        out_dir = SEC_ROOT / app / "faq"
        out_dir.mkdir(parents=True, exist_ok=True)
        for loc in LOCALES:
            body = "\n".join(by_lang[loc]).strip() + "\n"
            (out_dir / f"{loc}.md").write_text(body, encoding="utf-8")
            n += 1
    print("render_hand_faq_11: wrote", n, "files")


if __name__ == "__main__":
    main()
