#!/usr/bin/env python3
"""Write professional faq + privacy _locale_sections for batch-12 classics apps (no MT APIs)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SEC = ROOT / "_locale_sections"
TEMPLATE_PRIVACY = SEC / "iThree" / "privacy"
CONFIG = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
LANGS = [c["code"] for c in CONFIG["languages"] if c["code"] not in ("en", "zh-CN", "zh-TW")]

sys.path.insert(0, str(ROOT / "scripts"))
from batch12_faq_manual import all_faq_bodies  # noqa: E402
from batch12_privacy_short import SHORT_PRIVACY  # noqa: E402

APPS = (
    "iPrecepts",
    "iShangYang",
    "iSiShu",
    "iSutra",
    "iThousand",
    "iWuJing",
    "iXin",
    "iXunZi",
    "iZen",
    "iZengZi",
    "iZhuangZi",
    "iZiSi",
)

SECTION_RE = re.compile(
    r'<section lang="en"[^>]*>\n?(?P<body>.*?)(?=\n<section lang=|\Z)',
    re.DOTALL,
)

SHORT_PRIVACY_APPS = frozenset({"iSiShu", "iWuJing", "iZen"})


def en_body(app: str, page: str) -> str:
    text = (ROOT / app / f"{page}.md").read_text(encoding="utf-8")
    m = SECTION_RE.search(text)
    if not m:
        raise ValueError(f"no en section: {app}/{page}")
    return m.group("body").strip()


def adapt_privacy_generic(lang: str, app: str) -> str:
    en = en_body(app, "privacy")
    coup = SEC / "iCouplet" / "privacy" / f"{lang}.md"
    three = TEMPLATE_PRIVACY / f"{lang}.md"
    tpl_path = coup if coup.exists() else three
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
        zh_s, zh_t = [p.strip() for p in zh.split("/", 1)]
        text = text.replace("爱对联", zh_s).replace("愛對聯", zh_t)
        text = text.replace("爱三字经", zh_s).replace("愛三字經", zh_t)
    net_m = re.search(r"\| Network \| ([^\n|]+)", en)
    if net_m:
        en_net = net_m.group(1).strip()
        text = re.sub(
            r"\| Network \| Library[^\n]+\n",
            f"| Network | {en_net} |\n",
            text,
            count=1,
        )
    if date_en:
        for old in ("July 23, 2026", "23. Juli 2026", "2026年7月31日", "2026년 7월 31일", "July 31, 2026"):
            if old in text:
                text = text.replace(old, date_en)
                break
    return text.strip()


def write_faq(app: str, bodies: dict[str, dict[str, str]]) -> int:
    for lang in LANGS:
        dest = SEC / app / "faq" / f"{lang}.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(bodies[app][lang].strip() + "\n", encoding="utf-8")
    return len(LANGS)


def write_privacy(app: str) -> int:
    for lang in LANGS:
        if app in SHORT_PRIVACY_APPS:
            body = SHORT_PRIVACY[app][lang].strip()
        else:
            body = adapt_privacy_generic(lang, app)
        dest = SEC / app / "privacy" / f"{lang}.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(body + "\n", encoding="utf-8")
    return len(LANGS)


def main() -> None:
    faq_bodies = all_faq_bodies()
    faq_n = priv_n = 0
    for app in APPS:
        faq_n += write_faq(app, faq_bodies)
        priv_n += write_privacy(app)
        print(f"{app}: ok", flush=True)
    print(f"install_batch12_professional_locales: {faq_n} faq, {priv_n} privacy", flush=True)


if __name__ == "__main__":
    main()
