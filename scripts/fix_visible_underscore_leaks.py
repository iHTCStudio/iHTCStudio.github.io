#!/usr/bin/env python3
"""Remove visible ___ leaks before backticks/fences and align table cells from English."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

CONFIG = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
NEW_LOCALES = [
    c["code"]
    for c in CONFIG["languages"]
    if c["code"] not in ("en", "zh-CN", "zh-TW")
]

SEC_RE = re.compile(
    r'(<section lang="(?P<lang>[^"]+)"[^>]*>\n\n)(?P<body>.*?)(\n</section>)',
    re.DOTALL,
)
INLINE = re.compile(r"`[^`\n]+`")
LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
APPS_URL = re.compile(r"https://apps\.apple\.com[^\s)>\"]+")

DATA_LEAK = re.compile(
    r"_{2,}(?:VER[İI]_TOPLANMADI|DONN[ÉE]ES[^_]*|DATEN[^_]*|DATA[^_]*COLLECT[^_]*)_{2,}",
    re.IGNORECASE,
)
ICLOUD_LEAK = re.compile(r"_{2,}ICLOUD[^_|\n]*_{2,}|_{2,}ICLOUD(?=\*\*)|\*\*_{2,}ICLOUD", re.I)
APPLE_MAIL = re.compile(r"_{2,}APPLE_OSer", re.I)
ICLOUD_STAR = re.compile(r"\*{4,}_ICLOUD_{2,}", re.I)

BRAND_CELL = re.compile(
    r"_{2,}(?:앱_스토어|APP_ร้านค้า|APP_STORE|UYGULAMA[^_]*|아이폰|맥코스|맥|ไอโฟน|แม็ค)_{2,}",
    re.I,
)


def clean_simple(line: str) -> str:
    s = line
    s = re.sub(r"_{2,}```", "```", s)
    s = re.sub(r"_{2,}(?=```)", "", s)
    s = re.sub(r"_{2,}\s+(?=`)", "", s)
    s = re.sub(r"_{2,}(?=`)", "", s)
    s = re.sub(r"_{2,}\s+(`#[0-9A-Fa-f]{3,8}`)", r"\1", s)
    s = re.sub(
        r"\[_{2,}URL[^_\]]*_{2,}\s*([^\]]*)\]",
        lambda m: f"[URL Scheme {m.group(1).strip()}]",
        s,
        flags=re.I,
    )
    s = re.sub(
        r"\[\*?\*?\s*_{2,}APP[^_\]]*STORE[^_\]]*_{2,}[^\]]*\]",
        "[Download on the App Store →]",
        s,
        flags=re.I,
    )
    s = re.sub(r"_{3}\s*UYGULAMA(?:_[A-Za-zİıĞğÜüÖöÇçŞş]+)?\s*_{3}", "App Store", s, flags=re.I)
    s = re.sub(r"_{3}\s*APP\s*_?\s*STORE[^_]*_{3}", "App Store", s, flags=re.I)
    s = re.sub(
        r"\[_{3}\s*APP[^_\]]*STORE[^_\]]*_{3}[^\]]*\]",
        "[Download on the App Store →]",
        s,
        flags=re.I,
    )
    s = re.sub(
        r"\[_{3}\s*URL[^_\]]*(?:ŞEMA|SCHEME)[^_\]]*_{3}\s*([^\]]*)\]",
        r"[URL Scheme \1]",
        s,
        flags=re.I,
    )
    s = re.sub(r"\[_{3}\s*URL[^_\]]*(?:ŞEMA|SCHEME)[^_\]]*_{3}\s*\]", "[URL Scheme]", s, flags=re.I)
    s = re.sub(r"_{2,}\s+APP\s*STORE_{2,}", "App Store", s, flags=re.I)
    s = re.sub(r"(URL Scheme)_+", r"\1**", s, flags=re.I)
    s = re.sub(r"\(`([^`]+)`\s*_{2,}\)", r"(`\1`)", s)
    s = re.sub(r"_{2,}\s*\(`([^`]+)`", r" (`\1`", s)
    s = re.sub(r"(`[^`]+`)_{2,}", r"\1", s)
    s = re.sub(r"_{2,}(`[^`]+`)", r"\1", s)
    s = re.sub(r"_{2,}\s*(`[^`]+`)\s*_{2,}", r" \1", s)
    s = re.sub(r"__\s*(`[^`]+`)\s*__", r" \1", s)
    s = re.sub(r"__\s*,\s*__", "", s)
    s = re.sub(r",\s*__\s*,", ", ", s)
    s = ICLOUD_STAR.sub("**iCloud**", s)
    s = ICLOUD_LEAK.sub("iCloud", s)
    s = APPLE_MAIL.sub("AppleOSer", s)
    s = DATA_LEAK.sub("Data Not Collected", s)
    s = BRAND_CELL.sub(
        lambda m: "App Store"
        if "앱" in m.group(0) or "APP" in m.group(0).upper() or "UYGULAMA" in m.group(0).upper()
        else "iPhone"
        if "아이폰" in m.group(0) or "ไอโฟน" in m.group(0)
        else "macOS"
        if "맥코스" in m.group(0)
        else "Mac"
        if "맥" in m.group(0) or "แม็ค" in m.group(0)
        else m.group(0),
        s,
    )
    s = re.sub(r"Im\s+_{2,}APP_STORE[^_\[]*\[([^\]]+)\]", r"[\1]", s, flags=re.I)
    s = re.sub(
        r"\[_{3}\s*UYGULAMA[^]]*_{3}[^\]]*\]",
        "[App Store'dan indirin]",
        s,
        flags=re.I,
    )
    s = re.sub(r"_{3}iOS", "iOS", s, flags=re.I)
    s = re.sub(r"\*{2,}_ICLOUD_{2,}", "**iCloud**", s, flags=re.I)
    s = re.sub(r"`([^`]+)`\s*_{2,}(?=\s|/|—|$|\))", r"`\1`", s)
    s = re.sub(r"_{3}\s*/", " /", s)
    s = re.sub(r"_{3}\s*—", " —", s)
    s = re.sub(r"_{3,}", "", s)
    return s


def fix_table_row(en_line: str, loc_line: str) -> str:
    en_cols = [c.strip() for c in en_line.strip().strip("|").split("|")]
    loc_cols = [c.strip() for c in loc_line.strip().strip("|").split("|")]
    if len(en_cols) != len(loc_cols):
        return clean_simple(loc_line)
    out: list[str] = []
    for ec, lc in zip(en_cols, loc_cols):
        if "___" not in lc and "____" not in lc:
            out.append(lc)
            continue
        lc_clean = clean_simple(lc)
        if "___" not in lc_clean and "____" not in lc_clean:
            out.append(lc_clean)
            continue
        en_link = LINK.search(ec)
        url_m = APPS_URL.search(lc) or APPS_URL.search(ec)
        if en_link and url_m:
            text = LINK.search(lc_clean)
            link_text = (
                text.group(1)
                if text and "___" not in text.group(1) and "____" not in text.group(1)
                else en_link.group(1)
            )
            out.append(f"[{link_text}]({url_m.group(0).rstrip(' )')})")
            continue
        if "___" in lc_clean and "`" in ec and "___" not in ec:
            out.append(ec)
            continue
        if ec and "___" not in ec and re.fullmatch(r"[A-Za-z0-9 /.+]+", ec.replace("`", "")):
            out.append(ec)
            continue
        out.append(lc_clean)
    return "| " + " | ".join(out) + " |"


def fix_loc_line(en_line: str, loc_line: str) -> str:
    if "___" not in loc_line and "____" not in loc_line:
        return loc_line
    if en_line.strip().startswith("|") and loc_line.strip().startswith("|"):
        return fix_table_row(en_line, loc_line)
    en_codes = INLINE.findall(en_line)
    if en_codes:
        loc2 = loc_line
        for code in en_codes:
            loc2 = re.sub(
                r"_{2,}`[^`]+`_{2,}|_{2,}`[^`]+`|_{2,}`[^`]+`_{0,2}|`[^`]+`_{2,}",
                code,
                loc2,
                count=1,
            )
        loc2 = clean_simple(loc2)
        if "___" not in loc2 and "____" not in loc2:
            return loc2
    return clean_simple(loc_line)


def fix_locale_body(en_body: str, loc_body: str) -> tuple[str, int]:
    en_lines = en_body.splitlines()
    loc_lines = loc_body.splitlines()
    n = 0
    out: list[str] = []
    for i, loc_line in enumerate(loc_lines):
        en_line = en_lines[i] if i < len(en_lines) else ""
        if "___" in loc_line or "____" in loc_line:
            fixed = fix_loc_line(en_line, loc_line)
            if fixed != loc_line:
                n += 1
            out.append(fixed)
        else:
            out.append(loc_line)
    return "\n".join(out), n


def fix_markdown(text: str) -> tuple[str, int]:
    total = 0
    en_body = ""
    for m in SEC_RE.finditer(text):
        if m.group("lang") == "en":
            en_body = m.group("body")
            break
    if not en_body:
        new, c = fix_locale_body("", text)
        return (new if c else text, c)

    def sub(m: re.Match[str]) -> str:
        nonlocal total, en_body
        lang = m.group("lang")
        if lang == "en" or lang not in NEW_LOCALES:
            return m.group(0)
        fixed, c = fix_locale_body(en_body, m.group("body"))
        total += c
        return m.group(1) + fixed + m.group(3)

    new = SEC_RE.sub(sub, text)
    return new, total


def fix_part(path: Path) -> int:
    old = path.read_text(encoding="utf-8")
    if not re.search(r"_{3,}", old):
        return 0
    if "<section lang=" in old:
        new, n = fix_markdown(old)
    else:
        parent = path
        if "_locale_sections" in path.parts:
            idx = path.parts.index("_locale_sections")
            parent = ROOT / path.parts[idx + 1] / f"{path.parts[idx + 2]}.md"
        en_body = ""
        if parent.is_file():
            for m in SEC_RE.finditer(parent.read_text(encoding="utf-8")):
                if m.group("lang") == "en":
                    en_body = m.group("body")
                    break
        new, n = fix_locale_body(en_body, old)
    if n and new != old:
        path.write_text(new, encoding="utf-8")
    return n


def main() -> None:
    files = 0
    reps = 0
    for base in (ROOT, ROOT / "_locale_sections"):
        for path in sorted(base.rglob("*.md")):
            n = fix_part(path)
            if n:
                files += 1
                reps += n
                print(path.relative_to(ROOT), n)
    print(f"fix_visible_underscore_leaks: {files} files, {reps} line fixes")


if __name__ == "__main__":
    main()
