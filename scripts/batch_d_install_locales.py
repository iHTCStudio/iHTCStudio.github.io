#!/usr/bin/env python3
"""Install scripts/batch_d_data/{App}_{page}_{locale}.md → _locale_sections/{App}/{page}/{locale}.md"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "scripts" / "batch_d_data"
SEC = ROOT / "_locale_sections"
APPS = ("iMusic", "iVideo", "iAppManager")
PAGES = ("index", "faq", "privacy")
LANGS = ("ja", "ko", "ru", "th", "de", "fr", "tr")


def main() -> None:
    written = 0
    skipped = 0
    for app in APPS:
        for page in PAGES:
            for lang in LANGS:
                src = DATA / f"{app}_{page}_{lang}.md"
                dst = SEC / app / page / f"{lang}.md"
                if not src.exists():
                    continue
                if dst.exists():
                    skipped += 1
                    continue
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_text(src.read_text(encoding="utf-8").strip() + "\n", encoding="utf-8")
                written += 1
    print(f"batch_d_install: wrote {written}, skipped existing {skipped}")


if __name__ == "__main__":
    main()
