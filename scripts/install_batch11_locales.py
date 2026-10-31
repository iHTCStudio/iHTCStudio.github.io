#!/usr/bin/env python3
"""Write professional faq + privacy _locale_sections for 11 classics apps (no MT APIs)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import render_hand_faq_11 as faq_render  # noqa: E402
import render_hand_privacy_22 as priv_render  # noqa: E402

APPS = faq_render.APPS


def strip_section_noise(text: str) -> str:
    lines = [ln for ln in text.splitlines() if ln.strip() != "</section>"]
    return "\n".join(lines).strip() + "\n"


def write_faq() -> int:
    exact = faq_render.build_exact_map()
    n = 0
    for app in APPS:
        by_lang = faq_render.render_app(app, exact)
        out_dir = ROOT / "_locale_sections" / app / "faq"
        out_dir.mkdir(parents=True, exist_ok=True)
        for loc in faq_render.LOCALES:
            body = strip_section_noise("\n".join(by_lang[loc]))
            (out_dir / f"{loc}.md").write_text(body, encoding="utf-8")
            n += 1
    return n


def write_privacy() -> int:
    # Do not ingest broken existing locale files for these apps
    orig = list(priv_render.APPS)
    priv_render.APPS = list(APPS)
    try:
        exact = priv_render.build_exact_map()
        n = 0
        for app in APPS:
            by_lang = priv_render.render_app(app, exact)
            out_dir = ROOT / "_locale_sections" / app / "privacy"
            out_dir.mkdir(parents=True, exist_ok=True)
            for loc in priv_render.LOCALES:
                body = strip_section_noise("\n".join(by_lang[loc]))
                (out_dir / f"{loc}.md").write_text(body, encoding="utf-8")
                n += 1
        return n
    finally:
        priv_render.APPS = orig


def main() -> None:
    fq = write_faq()
    pr = write_privacy()
    print(f"install_batch11_locales: {fq} faq + {pr} privacy files")


if __name__ == "__main__":
    main()
