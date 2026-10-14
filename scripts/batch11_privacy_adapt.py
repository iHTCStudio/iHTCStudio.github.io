#!/usr/bin/env python3
"""Adapt iCouplet hand-translated privacy templates to other apps (no MT)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC = ROOT / "_locale_sections"
LANGS = ("ja", "ko", "ru", "th", "de", "fr", "tr")

SECTION_RE = re.compile(
    r'<section lang="en"[^>]*>\n?(?P<body>.*?)(?=\n<section lang=|\Z)',
    re.DOTALL,
)


def en_privacy(app: str) -> str:
    text = (ROOT / app / "privacy.md").read_text(encoding="utf-8")
    m = SECTION_RE.search(text)
    if not m:
        raise ValueError(app)
    return m.group("body").strip()


def meta_from_en(en: str, app: str) -> dict[str, str]:
    bundle_m = re.search(r"Bundle ID `([^`]+)`", en)
    bundle = bundle_m.group(1) if bundle_m else f"com.iHTCboy.{app}"
    zh_m = re.search(r'also known as "([^"]+)"', en)
    zh = zh_m.group(1) if zh_m else app
    date_m = re.search(r"\*\*Last updated:\*\* (.+)", en)
    date_en = date_m.group(1).strip() if date_m else ""
    group = f"group.{bundle}" if bundle.startswith("com.") else f"group.{bundle}"
    return {"bundle": bundle, "group": group, "zh": zh, "date_en": date_en, "app": app}


def adapt(lang: str, app: str) -> str:
    tpl_path = SEC / "iCouplet" / "privacy" / f"{lang}.md"
    if not tpl_path.exists():
        raise FileNotFoundError(tpl_path)
    en = en_privacy(app)
    meta = meta_from_en(en, app)
    text = tpl_path.read_text(encoding="utf-8")

    # Pull app-specific summary rows from English (keep structure, translate key phrases manually per app family)
    net_m = re.search(r"\| Network \| (.+) \|", en)
    network_en = net_m.group(1).strip() if net_m else ""

    rep = [
        ("iCouplet", meta["app"]),
        ("爱对联 / 愛對聯", meta["zh"]),
        ("`com.iHTCboy.iCouplet`", f"`{meta['bundle']}`"),
        ("group.com.iHTCboy.iCouplet", meta["group"]),
        ("Couplet", meta["app"].replace("i", "", 1) if meta["app"].startswith("i") else meta["app"]),
        ("couplet", meta["app"].lower()),
        ("対聯", "テキスト"),
        ("couplets", "passages"),
        ("Couplet database", f"{meta['app']} database"),
        ("今日の対聯", "今日の一句"),
        ("Daily Line", "Daily passage"),
        ("3,369", "library"),
    ]
    for a, b in rep:
        text = text.replace(a, b)

    # Replace network row in template per language (iCouplet ja line)
    if network_en and lang == "ja":
        old = "対聯ライブラリ、閲読、朗誦、学習、ウィジェット、毎日の通知は、インストール後は**オフライン**で動作します"
        # crude: inject English network row translated in template by replacing whole cell
        if "| ネットワーク |" in text and network_en:
            text = re.sub(
                r"\| ネットワーク \| [^|]+ \|",
                f"| ネットワーク | {network_en} |",
                text,
                count=1,
            )

    if meta["date_en"]:
        for old in ("2026 年 7 月 23 日", "July 23, 2026", "2026년 7월 23일"):
            text = text.replace(old, meta["date_en"])

    # Merge: for lines still English-heavy, prefer English privacy body translated via line map
    return text.strip() + "\n"


def write_all(apps: tuple[str, ...]) -> int:
    n = 0
    for app in apps:
        for lang in LANGS:
            body = adapt(lang, app)
            dest = SEC / app / "privacy" / f"{lang}.md"
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(body, encoding="utf-8")
            n += 1
    return n
