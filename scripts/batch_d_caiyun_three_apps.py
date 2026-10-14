#!/usr/bin/env python3
"""Generate missing _locale_sections for iMusic, iVideo, iAppManager (index/faq/privacy)."""

from __future__ import annotations

import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from batch_index_locales_caiyun import (  # noqa: E402
    load_cache,
    save_cache,
    translate_text_caiyun,
)
from generate_locale_sections import (  # noqa: E402
    extract_section,
    translate_markdown_body,
    NEW_LOCALES,
    SEC_ROOT,
)

import generate_classics_locale_sections as gcs  # noqa: E402

APPS = ("iMusic", "iVideo", "iAppManager")
PAGES = ("index", "faq", "privacy")


def main(*, force: bool = False) -> None:
    gcs.translate_text = translate_text_caiyun  # type: ignore[attr-defined]
    cache = load_cache()
    written = 0
    for app_id in APPS:
        for page in PAGES:
            md_path = ROOT / app_id / f"{page}.md"
            if not md_path.exists():
                continue
            en_body = extract_section(md_path.read_text(encoding="utf-8"), "en")
            if not en_body:
                print(f"skip no en: {app_id}/{page}")
                continue
            out_dir = SEC_ROOT / app_id / page
            for loc in NEW_LOCALES:
                out_path = out_dir / f"{loc}.md"
                if out_path.exists() and not force:
                    continue
                print(f"{app_id}/{page} → {loc}", flush=True)
                out_dir.mkdir(parents=True, exist_ok=True)
                try:
                    body = translate_markdown_body(en_body, loc, app_id, cache)
                except RuntimeError as err:
                    print(f"  SKIP: {err}", flush=True)
                    continue
                out_path.write_text(body.strip() + "\n", encoding="utf-8")
                written += 1
                if written % 3 == 0:
                    save_cache(cache)
                time.sleep(2.5)
    save_cache(cache)
    print(f"batch_d_caiyun_three_apps: wrote {written}")


if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("--force", action="store_true")
    args = p.parse_args()
    main(force=args.force)
