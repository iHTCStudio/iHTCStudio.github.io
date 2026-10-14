#!/usr/bin/env python3
"""Write all batch-11 faq/privacy locale bodies, then patch docs + append."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC = ROOT / "_locale_sections"
LANGS = ("ja", "ko", "ru", "th", "de", "fr", "tr")
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
CLASSIC_APPS = ("iHanFei", "iLvShi", "iGuanZhi", "iMoZi")
RENDER_APPS = ("iBaiJia", "iGuige", "iLiezi", "iPrimer", "iRhyme", "iSage")

sys.path.insert(0, str(ROOT / "scripts"))

from fulltext_faq_ja import FAQ as FAQ_JA  # noqa: E402
from hand_batch11_faq_masters import IMENCIUS, classic_faq  # noqa: E402


def write_text(app: str, kind: str, lang: str, body: str) -> None:
    p = SEC / app / kind / f"{lang}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    body = body.strip()
    body = re.sub(r"\n</section>\s*$", "", body)
    p.write_text(body + "\n", encoding="utf-8")


def write_faq_classics() -> None:
    for lang in LANGS:
        write_text("iMencius", "faq", lang, IMENCIUS[lang])
        for app in CLASSIC_APPS:
            write_text(app, "faq", lang, classic_faq(lang, app))


def write_faq_ja_uniques() -> None:
    for app, body in FAQ_JA.items():
        if app in APPS:
            write_text(app, "faq", "ja", body)


def write_faq_render_apps() -> None:
    import render_hand_faq_11 as rf

    exact = rf.build_exact_map()
    for app in RENDER_APPS:
        by = rf.render_app(app, exact)
        for lang in LANGS:
            if app == "iBaiJia" and lang == "ja":
                continue
            body = "\n".join(by[lang])
            write_text(app, "faq", lang, body)


def write_privacy() -> None:
    from batch11_privacy_from_icouplet import write_all as write_privacy_adapted

    write_privacy_adapted(APPS)


def patch_docs() -> None:
    subprocess.check_call(
        [sys.executable, str(ROOT / "scripts/patch_doc_locale_sections.py"), *APPS],
        cwd=str(ROOT),
    )


def append_docs() -> None:
    subprocess.check_call(
        [sys.executable, str(ROOT / "scripts/append_locale_sections.py")],
        cwd=str(ROOT),
    )


def main() -> None:
    write_faq_classics()
    write_faq_ja_uniques()
    write_faq_render_apps()
    write_privacy()
    patch_docs()
    append_docs()
    print("batch11_write_all_locales: done")


if __name__ == "__main__":
    main()
