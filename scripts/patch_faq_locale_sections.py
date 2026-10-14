#!/usr/bin/env python3
"""Replace <section lang="..."> bodies in TwinPolarCam/faq.md from _locale_sections."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FAQ = ROOT / "TwinPolarCam/faq.md"
SEC = ROOT / "_locale_sections/TwinPolarCam/faq"
LANGS = ("ja", "ko", "ru", "th", "de", "fr", "tr")

SECTION_RE = re.compile(
    r'(<section lang="(?P<lang>[^"]+)" markdown="1">\n\n)'
    r"(?P<body>.*?)"
    r"(\n</section>)",
    re.DOTALL,
)


def main() -> None:
    text = FAQ.read_text(encoding="utf-8")
    for lang in LANGS:
        part = SEC / f"{lang}.md"
        if not part.exists():
            continue
        body = part.read_text(encoding="utf-8").strip()

        def repl(m: re.Match[str]) -> str:
            if m.group("lang") != lang:
                return m.group(0)
            return f'{m.group(1)}{body}{m.group(3)}'

        text, n = SECTION_RE.subn(repl, text, count=1)
        if n:
            print(f"patched {lang}")
    FAQ.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
