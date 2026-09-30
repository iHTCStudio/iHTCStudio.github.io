#!/usr/bin/env python3
"""Replace iHTCTeam legal entity with iHTC Studio (+ formerly note in intros)."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP = {
    ROOT / "CLAUDE.md",
    ROOT / "README.md",
    ROOT / "_config.yml",
    ROOT / "scripts" / "rebrand_legal_entity.py",
}

GLOBS = ["**/privacy.md", "**/faq.md", "**/index.md"]

SECTION_START = re.compile(
    r'(?P<open><section lang="(?P<lang>en|zh-CN|zh-TW)"[^>]*>\n?)'
)

# Intro-line patterns (also used to fix partially migrated files)
CN_INTRO_QUOTED = re.compile(
    r'^iHTC Studio（[""\u201c\u201d]我们[""\u201c\u201d]）', re.MULTILINE
)


def split_sections(text: str) -> tuple[str, list[tuple[str, str]]]:
    matches = list(SECTION_START.finditer(text))
    if not matches:
        return text, []

    preamble = text[: matches[0].start()]
    sections: list[tuple[str, str]] = []
    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections.append((match.group("open"), match.group("lang"), text[start:end]))
    return preamble, sections


def process_section(body: str, lang: str) -> str:
    protected = {
        "___FORMERLY_IHTCTEAM___": "formerly iHTCTeam",
        "___YUAN_IHTCTEAM___": "原 iHTCTeam",
    }
    for placeholder, original in protected.items():
        body = body.replace(original, placeholder)

    body = body.replace("formerly iHTC Studio", "___FORMERLY_IHTCTEAM___")

    if lang == "en":
        body = re.sub(
            r'iHTCTeam \("we", "us" or "our"\)',
            'iHTC Studio ("we", "us" or "our"; ___FORMERLY_IHTCTEAM___)',
            body,
            count=1,
        )
        body = re.sub(
            r'^iHTCTeam built ',
            "iHTC Studio (___FORMERLY_IHTCTEAM___) built ",
            body,
            count=1,
            flags=re.MULTILINE,
        )
    elif lang == "zh-CN":
        body = re.sub(
            r'^iHTCTeam（[""\u201c\u201d]我们[""\u201c\u201d]）',
            "爱火腿肠工作室（iHTC Studio）（「我们」；___YUAN_IHTCTEAM___）",
            body,
            count=1,
            flags=re.MULTILINE,
        )
        body = re.sub(
            r'^iHTCTeam 开发了',
            "爱火腿肠工作室（iHTC Studio；___YUAN_IHTCTEAM___）开发了",
            body,
            count=1,
            flags=re.MULTILINE,
        )
        body = re.sub(
            r'^iHTC Studio（[""\u201c\u201d]我们[""\u201c\u201d]）',
            "爱火腿肠工作室（iHTC Studio）（「我们」；___YUAN_IHTCTEAM___）",
            body,
            count=1,
            flags=re.MULTILINE,
        )
        body = re.sub(
            r'^iHTC Studio 开发了',
            "爱火腿肠工作室（iHTC Studio；___YUAN_IHTCTEAM___）开发了",
            body,
            count=1,
            flags=re.MULTILINE,
        )
    elif lang == "zh-TW":
        body = re.sub(
            r'^iHTCTeam（「我們」）',
            "愛火腿腸工作室（iHTC Studio）（「我們」；___YUAN_IHTCTEAM___）",
            body,
            count=1,
            flags=re.MULTILINE,
        )
        body = re.sub(
            r'^iHTCTeam 開發了',
            "愛火腿腸工作室（iHTC Studio；___YUAN_IHTCTEAM___）開發了",
            body,
            count=1,
            flags=re.MULTILINE,
        )
        body = re.sub(
            r'^iHTC Studio（「我們」）',
            "愛火腿腸工作室（iHTC Studio）（「我們」；___YUAN_IHTCTEAM___）",
            body,
            count=1,
            flags=re.MULTILINE,
        )
        body = re.sub(
            r'^iHTC Studio 開發了',
            "愛火腿腸工作室（iHTC Studio；___YUAN_IHTCTEAM___）開發了",
            body,
            count=1,
            flags=re.MULTILINE,
        )

    if "iHTCTeam" in body:
        body = body.replace("iHTCTeam", "iHTC Studio")

    for placeholder, original in protected.items():
        body = body.replace(placeholder, original)

    return body


def process_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "iHTCTeam" not in text and "formerly iHTC Studio" not in text:
        # Still fix zh intros missing formerly
        if not SECTION_START.search(text):
            return False

    preamble, sections = split_sections(text)
    if not sections:
        new_text = text.replace("formerly iHTC Studio", "formerly iHTCTeam")
        if "iHTCTeam" in new_text:
            new_text = new_text.replace("iHTCTeam", "iHTC Studio")
        if new_text == text:
            return False
        path.write_text(new_text, encoding="utf-8")
        return True

    rebuilt = [preamble]
    for open_tag, lang, body in sections:
        rebuilt.append(open_tag)
        rebuilt.append(process_section(body, lang))

    new_text = "".join(rebuilt)
    if new_text == text:
        return False
    path.write_text(new_text, encoding="utf-8")
    return True


def main() -> None:
    changed: list[Path] = []
    for pattern in GLOBS:
        for path in sorted(ROOT.glob(pattern)):
            if path in SKIP or "node_modules" in path.parts:
                continue
            if process_file(path):
                changed.append(path)
    print(f"Updated {len(changed)} files")
    for p in changed:
        print(f"  {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
