#!/usr/bin/env python3
"""Retry until all iMusic/iVideo/iAppManager locale sections exist."""

from __future__ import annotations

import sys
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from batch_d_caiyun_three_apps import main as run_once  # noqa: E402


def missing_count() -> int:
    config = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
    langs = [c["code"] for c in config["languages"] if c["code"] not in ("en", "zh-CN", "zh-TW")]
    sec = ROOT / "_locale_sections"
    apps = ("iMusic", "iVideo", "iAppManager")
    pages = ("index", "faq", "privacy")
    return sum(
        1
        for a in apps
        for p in pages
        for l in langs
        if not (sec / a / p / f"{l}.md").exists()
    )


def main() -> None:
    for round_i in range(1, 80):
        left = missing_count()
        print(f"round {round_i}: missing {left}", flush=True)
        if left == 0:
            break
        run_once()
        time.sleep(45)
    print("final missing", missing_count(), flush=True)


if __name__ == "__main__":
    main()
