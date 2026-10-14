#!/usr/bin/env python3
"""Adapt iCouplet hand privacy locales to batch-11 apps (no MT APIs)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC = ROOT / "_locale_sections"
TEMPLATE_PRIVACY = SEC / "iThree" / "privacy"
LANGS = ("ja", "ko", "ru", "th", "de", "fr", "tr")

SECTION_RE = re.compile(
    r'<section lang="en"[^>]*>\n?(?P<body>.*?)(?=\n<section lang=|\Z)',
    re.DOTALL,
)


def en_body(app: str) -> str:
    text = (ROOT / app / "privacy.md").read_text(encoding="utf-8")
    m = SECTION_RE.search(text)
    if not m:
        raise ValueError(f"no en section: {app}/privacy")
    return m.group("body").strip()


def adapt_privacy(lang: str, app: str) -> str:
    en = en_body(app)
    three = TEMPLATE_PRIVACY / f"{lang}.md"
    coup = SEC / "iCouplet" / "privacy" / f"{lang}.md"
    tpl_path = three if three.exists() else coup
    text = tpl_path.read_text(encoding="utf-8")

    bundle_m = re.search(r"Bundle ID `([^`]+)`", en)
    bundle = bundle_m.group(1) if bundle_m else f"com.iHTCboy.{app}"
    zh_m = re.search(r'also known as "([^"]+)"', en)
    if not zh_m:
        zh_m = re.search(r"\(([^)]+), Bundle ID", en)
    zh = zh_m.group(1).strip() if zh_m else app
    date_m = re.search(r"\*\*Last updated:\*\* (.+)", en)
    date_en = date_m.group(1).strip() if date_m else ""

    group = f"group.{bundle}" if bundle.startswith("com.") else f"group.{bundle.replace('com.', '')}"

    rep = {
        "iCouplet": app,
        "iThree": app,
        "爱对联 / 愛對聯": zh,
        "「爱对联」/「愛對聯」": f"「{zh.replace(' / ', '」/「')}」" if " / " in zh else f"「{zh}」",
        "爱三字经 / 愛三字經": zh,
        "`com.iHTCboy.iCouplet`": f"`{bundle}`",
        "`com.iHTCboy.iThree`": f"`{bundle}`",
        "group.com.iHTCboy.iCouplet": group,
        "group.com.iHTCboy.iThree": group,
    }
    for a, b in rep.items():
        text = text.replace(a, b)
    text = text.replace("{CNNAME}", zh)
    if " / " in zh:
        parts = [p.strip() for p in re.split(r"\s*/\s*", zh, maxsplit=1)]
        if len(parts) == 2:
            zh_s, zh_t = parts
            text = text.replace("爱对联", zh_s).replace("愛對聯", zh_t)
            text = text.replace("爱三字经", zh_s).replace("愛三字經", zh_t)

    net_m = re.search(r"\| Network \| ([^\n|]+)", en)
    if net_m:
        en_net = net_m.group(1).strip()
        text = re.sub(
            r"\| Network \| [^\n|]+\|",
            f"| Network | {en_net} |",
            text,
            count=1,
        )

    if date_en:
        for old in (
            "July 23, 2026",
            "23. Juli 2026",
            "2026年7月31日",
            "2026년 7월 31일",
            "July 31, 2026",
            "2026年7月23日",
            "2026年7月31日",
        ):
            if old in text:
                text = text.replace(old, date_en)
                break
        if "**Last updated:**" in en.splitlines()[0]:
            pass
        elif date_en and "**" in text.splitlines()[0]:
            text = re.sub(r"^\*\*[^*]+\*\*.*$", f"**Last updated:** {date_en}", text, count=1, flags=re.M)

    return text.strip()


def write_all(apps: tuple[str, ...]) -> None:
    for app in apps:
        for lang in LANGS:
            body = adapt_privacy(lang, app)
            dest = SEC / app / "privacy" / f"{lang}.md"
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(body + "\n", encoding="utf-8")
