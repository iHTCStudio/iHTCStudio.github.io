#!/usr/bin/env python3
"""Content QA for 7 new locales in app markdown (beyond validate_locales structure)."""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
NEW = [c["code"] for c in CONFIG["languages"] if c["code"] not in ("en", "zh-CN", "zh-TW")]
BRAND = set(yaml.safe_load((ROOT / "_data/locale_policies.yml").read_text())["brand_fixed_content"])
SEC = re.compile(r'<section lang="([^"]+)"[^>]*>\n?(.*?)(?=\n<section lang=|\Z)', re.DOTALL)
PLACEHOLDER = re.compile(r"_{3,}")
BAD_HEAD = re.compile(r"^#{1,6}\s+#\s+", re.M)
FORBIDDEN = re.compile(r"iHTCTeam", re.I)


def main() -> int:
    issues: Counter[str] = Counter()
    by_app: defaultdict[str, Counter[str]] = defaultdict(Counter)
    for name in ("index.md", "faq.md", "privacy.md", "url-scheme.md"):
        for path in ROOT.glob(f"**/{name}"):
            if "_locale_sections" in path.parts or path.parent.name in BRAND:
                continue
            text = path.read_text(encoding="utf-8")
            for loc in NEW:
                m = re.search(rf'<section lang="{re.escape(loc)}"[^>]*>\n?(.*?)(?=\n<section lang=|\Z)', text, re.DOTALL)
                if not m:
                    continue
                body = m.group(1)
                if PLACEHOLDER.search(body):
                    issues["placeholder_token"] += len(PLACEHOLDER.findall(body))
                    by_app[path.parent.name]["placeholder"] += 1
                if BAD_HEAD.search(body):
                    issues["bad_heading"] += len(BAD_HEAD.findall(body))
                    by_app[path.parent.name]["bad_heading"] += 1
                if FORBIDDEN.search(body):
                    issues["forbidden_brand"] += 1
                    by_app[path.parent.name]["forbidden"] += 1
    print("proofread_markdown_content summary:")
    for k, v in issues.most_common():
        print(f"  {k}: {v}")
    worst = sorted(by_app.items(), key=lambda x: sum(x[1].values()), reverse=True)[:12]
    if worst:
        print("  apps with most flags:", ", ".join(f"{a}({sum(c.values())})" for a, c in worst))
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
