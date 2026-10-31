"""Shared glossary / MT placeholder restoration for markdown locale content."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ("ja", "ko", "ru", "th", "de", "fr", "tr")

SEC_RE = re.compile(
    r'<section lang="(?P<lang>[^"]+)"[^>]*>\n?(?P<body>.*?)(?=\n<section lang=|\Z)',
    re.DOTALL,
)
SPAN_RE = re.compile(r"```[\s\S]*?```|`[^`\n]+`")
INLINE_SPAN_RE = re.compile(r"`[^`\n]+`")

STATIC: dict[str, str] = {
    "___IHTC_STUDIO___": "iHTC Studio",
    "__IHTC_STUDIO___": "iHTC Studio",
    "___APPLE___": "Apple",
    "__APPLE___": "Apple",
    "___ICLOUD___": "iCloud",
    "__ICLOUD___": "iCloud",
    "___ ICLOUD ___": "iCloud",
    "___KEYCHAIN___": "Keychain",
    "__KEYCHAIN___": "Keychain",
    "___APP_STORE___": "App Store",
    "__APP_STORE___": "App Store",
    "___APP_STORE_CONNECT___": "App Store Connect",
    "__APP_STORE_CONNECT___": "App Store Connect",
    "___DATA_NOT_COLLECTED___": "Data Not Collected",
    "___DATEN_NICHT_GESAMMELT___": "Data Not Collected",
    "___DATA_NOT_COLECTED___": "Data Not Collected",
    "___ДАННЫЕ_НЕ_СОБРАНЫ___": "Data Not Collected",
    "___WIFI___": "Wi-Fi",
    "__WIFI___": "Wi-Fi",
    "___IPHONE___": "iPhone",
    "__IPHONE___": "iPhone",
    "___IPAD___": "iPad",
    "__IPAD___": "iPad",
    "___MAC___": "Mac",
    "__MAC___": "Mac",
    "___MACOS___": "macOS",
    "__MACOS___": "macOS",
    "___IOS___": "iOS",
    "__IOS___": "iOS",
    "___TESTFLIGHT___": "TestFlight",
    "__TESTFLIGHT___": "TestFlight",
    "___SWIFTUI___": "SwiftUI",
    "__SWIFTUI___": "SwiftUI",
    "___URL_SCHEME___": "URL Scheme",
    "__URL_SCHEME___": "URL Scheme",
}

GLOSS_KEY_TO_VALUE: dict[str, str] = {
    "IPHONE": "iPhone",
    "İPHONE": "iPhone",
    "IPAD": "iPad",
    "İPAD": "iPad",
    "MAC": "Mac",
    "MACOS": "macOS",
    "IOS": "iOS",
    "İOS": "iOS",
    "IOs": "iOS",
    "ICLOUD": "iCloud",
    "İCLOUD": "iCloud",
    "APPLE": "Apple",
    "IHTC_STUDIO": "iHTC Studio",
    "APP_STORE": "App Store",
    "APP_STORE_CONNECT": "App Store Connect",
    "DATA_NOT_COLLECTED": "Data Not Collected",
    "KEYCHAIN": "Keychain",
    "SWIFTUI": "SwiftUI",
    "SWİFTUİ": "SwiftUI",
    "TESTFLIGHT": "TestFlight",
    "WIFI": "Wi-Fi",
    "URL_SCHEME": "URL Scheme",
    "URL-СХЕМА": "URL Scheme",
}

# MT sometimes translated placeholder labels instead of restoring glossary tokens.
TRANSLATED_LEAKS: dict[str, str] = {
    "мобильный": "iPhone",
    "айпад": "iPad",
    "맥": "Mac",
}

INDEXED = re.compile(
    r"_{2,}(?:"
    r"FENCE|ZAUN|ZAUN_|"
    r"ограждения|ОГРАЖДЕНИЯ|ЗАБОР|ЗАБOR|"
    r"fence|zaun|รั้ว|"
    r"フェンス|ウォール|울타리|펜스|"
    r"CLÔTURE|clôture|ÇİT|çit"
    r")_?(\d+)__+",
    re.IGNORECASE,
)
EMBEDDED_FENCE = re.compile(
    r"(?:FENCE|フェンス|울타리|펜스|CLÔTURE|ÇİT|รั้ว)_(\d+)[^\s`|]*",
    re.IGNORECASE,
)
BROKEN_FENCE_TAIL = re.compile(r"___\s*FENCE_\.", re.IGNORECASE)
IOS_TRAILING = re.compile(r"_ _ _\s*IOS\s*_+", re.IGNORECASE)
ICLOUD_TRAILING = re.compile(r"_ _ _\s*ICLOUD\s*_+", re.IGNORECASE)
APP_STORE_CHUNK = re.compile(r"_ _ _\s*APP\s*_+\s*STORE\s*_ _ _", re.IGNORECASE)
MANGLED_FENCE_EXTRA = re.compile(
    r"(?:_ _ _\s*)+fence\s*_?\s*(\d+)\s*(?:_ _ _)+",
    re.IGNORECASE,
)
LOOSE_INDEXED = re.compile(r"_{4,}(\d+)__+")
MANGLED_FENCE_WORD = re.compile(
    r"_ _ _\s*(?:CLÔTURE|clôture|FENCE|fence|ZAUN|zaun|ЗАБОР|ограждения)\s*_?\s*(\d+)\s*_ _ _",
    re.IGNORECASE,
)
SPACED_FENCE = re.compile(r"___\s*FENCE_(\d+)\s*___", re.IGNORECASE)
FENCE_SLOPPY = re.compile(r"___\s*FENCE\s*_?\s*(\d+)\s*___", re.IGNORECASE)
SPACE_UNDERS = re.compile(r"_ _ _\s*([A-Z0-9_\-]+)\s*_ _ _?", re.IGNORECASE)
FLEX_UNDERS = re.compile(
    r"_ _ _\s*([A-Za-z0-9_\-]+(?:\s+[A-Za-z0-9_\-]+)*?)\s*_ _ _?",
    re.IGNORECASE,
)
LOOSE_TRIPLE = re.compile(
    r"_{3}\s+([A-Z0-9_\-]+(?:\s+[A-Z0-9_\-]+)*)\s+_{3}",
    re.IGNORECASE,
)
SPACED_GLOSS = re.compile(r"_{2,}\s*([A-Za-zА-Яа-яİıÖöÜüÇçĞğŞş0-9 \-]+?)\s*_{2,}")
DATA_KO = re.compile(r"_ _ _\s*데이터\s*_\s*수집되지\s*않음\s*_\s*")
DATA_MANGLED = re.compile(r"_ _ _\s*DATA\s*_\s*[^_]+_\s*", re.IGNORECASE)
DATA_NOT_LEAK = re.compile(
    r"_{2,}DATA_NOT_(?:COLLECTED|[A-Za-z0-9_\u0080-\uffff]+?)_{2,}",
    re.IGNORECASE,
)
MANGLED_ICLOUD_SYNC = re.compile(
    r"\*\*\s*_\s*I\s*cloud\s*_ _ _\s*Sync",
    re.IGNORECASE,
)
LOOSE_GLOSS_TRIPLE = re.compile(r"_{3}(.+?)_{3}")
SPACED_CIT_FENCE = re.compile(
    r"_{3}\s*(?:ÇİT|CIT|FENCE|ZAUN|CLÔTURE|clôture)\s*_?\s*(\d+)\s*_{3}",
    re.I,
)
PARTIAL_ICLOUD = re.compile(r"_{3}\s*ICLOUD\b[^_|\n]*", re.I)
PARTIAL_APP_STORE = re.compile(
    r"\[?\*?\*?\s*_{3}\s*APP[^_\n]*STORE[^_\n]*_{3}",
    re.I,
)
URL_SCHEME_GLOSS = re.compile(r"_{3}\s*URL[^_\n]*(?:ŞEMA|SCHEME|SCHEMA)[^_\n]*_{3}", re.I)


def parent_markdown(path: Path) -> Path | None:
    parts = path.parts
    if "_locale_sections" not in parts:
        return path if path.suffix == ".md" else None
    idx = parts.index("_locale_sections")
    if idx + 2 >= len(parts):
        return None
    return ROOT / parts[idx + 1] / f"{parts[idx + 2]}.md"


def spans_from_en_text(text: str) -> list[str]:
    for m in SEC_RE.finditer(text):
        if m.group("lang") == "en":
            return SPAN_RE.findall(m.group("body"))
    return []


def en_spans_for_path(path: Path, *, inline_only: bool = True) -> list[str]:
    body = en_body_for_path(path)
    if not body:
        return []
    pat = INLINE_SPAN_RE if inline_only else SPAN_RE
    return pat.findall(body)


def en_body_for_path(path: Path) -> str:
    parent = parent_markdown(path)
    if parent and parent.is_file():
        for m in SEC_RE.finditer(parent.read_text(encoding="utf-8")):
            if m.group("lang") == "en":
                return m.group("body")
    text = path.read_text(encoding="utf-8")
    if "<section lang=" in text:
        for m in SEC_RE.finditer(text):
            if m.group("lang") == "en":
                return m.group("body")
    return ""


def _gloss_value(key: str) -> str | None:
    k = key.strip().upper().replace(" ", "_")
    for cand in (key.strip(), k):
        if cand in GLOSS_KEY_TO_VALUE:
            return GLOSS_KEY_TO_VALUE[cand]
    if k in GLOSS_KEY_TO_VALUE:
        return GLOSS_KEY_TO_VALUE[k]
    return None


def fix_spaced_and_leaks(text: str) -> tuple[str, int]:
    n = 0

    def space_repl(m: re.Match[str]) -> str:
        nonlocal n
        raw = m.group(1).strip()
        val = _gloss_value(raw)
        if val:
            n += 1
            return val
        low = raw.lower()
        if low in TRANSLATED_LEAKS:
            n += 1
            return TRANSLATED_LEAKS[low]
        return m.group(0)

    def su_repl(m: re.Match[str]) -> str:
        nonlocal n
        val = _gloss_value(m.group(1))
        if val:
            n += 1
            return val
        return m.group(0)

    out = DATA_KO.sub("Data Not Collected", text)
    if out != text:
        n += 1
    out2 = DATA_MANGLED.sub("Data Not Collected", out)
    if out2 != out:
        n += 1
        out = out2
    out2, c = DATA_NOT_LEAK.subn("Data Not Collected", out)
    if c:
        n += c
        out = out2

    def loose_gloss(m: re.Match[str]) -> str:
        nonlocal n
        inner = m.group(1).strip()
        key = re.sub(r"\s+", "_", inner).upper()
        if "ICLOUD" in key or "ICLOUD" in inner.upper():
            n += 1
            return "iCloud"
        if "APP" in key and "STORE" in key:
            n += 1
            return "App Store"
        if "URL" in key and any(x in key for x in ("SCHEME", "ŞEMA", "SCHEMA")):
            n += 1
            return "URL Scheme"
        if "DATA" in key and "COLLECT" in key:
            n += 1
            return "Data Not Collected"
        val = _gloss_value(key) or _gloss_value(inner)
        if val:
            n += 1
            return val
        return m.group(0)

    out = re.sub(r"_{2,}\s+(?=`)", "", out)
    out = re.sub(r"_{2,}\s+(`#[0-9A-Fa-f]{3,8}`)", r"\1", out)
    out = re.sub(
        r"_{3}\s*UYGULAMA(?:_[A-Za-zİıĞğÜüÖöÇçŞş]+)?\s*_{3}",
        "App Store",
        out,
        flags=re.I,
    )
    out = re.sub(r"_{3}\s*APP\s*_?\s*STORE[^_]*_{3}", "App Store", out, flags=re.I)
    out = PARTIAL_ICLOUD.sub("iCloud", out)
    out = PARTIAL_APP_STORE.sub("App Store", out)
    out = URL_SCHEME_GLOSS.sub("URL Scheme", out)
    out = LOOSE_GLOSS_TRIPLE.sub(loose_gloss, out)
    out = MANGLED_ICLOUD_SYNC.sub("**iCloud Sync", out)
    out = LOOSE_TRIPLE.sub(space_repl, out)
    out = SPACE_UNDERS.sub(su_repl, out)
    out = FLEX_UNDERS.sub(su_repl, out)
    out = SPACED_GLOSS.sub(space_repl, out)
    return out, n


def fix_body(body: str, spans: list[str]) -> tuple[str, int]:
    n = 0

    def idx_repl(m: re.Match[str]) -> str:
        nonlocal n
        idx = int(m.group(1))
        if idx < len(spans):
            n += 1
            return spans[idx]
        return m.group(0)

    out = body
    for pat in (
        MANGLED_FENCE_EXTRA,
        MANGLED_FENCE_WORD,
        SPACED_CIT_FENCE,
        SPACED_FENCE,
        FENCE_SLOPPY,
        EMBEDDED_FENCE,
        INDEXED,
        LOOSE_INDEXED,
    ):
        out = pat.sub(idx_repl, out)
    if BROKEN_FENCE_TAIL.search(out):
        out = BROKEN_FENCE_TAIL.sub("`review`", out)
        n += 1
    for pat, val in (
        (IOS_TRAILING, "iOS"),
        (ICLOUD_TRAILING, "iCloud"),
        (APP_STORE_CHUNK, "App Store"),
    ):
        out2 = pat.sub(val, out)
        if out2 != out:
            n += len(pat.findall(out))
            out = out2
    for bad, good in STATIC.items():
        if bad in out:
            c = out.count(bad)
            out = out.replace(bad, good)
            n += c
    out2, c2 = fix_spaced_and_leaks(out)
    return out2, n + c2


def fix_line_aligned(en_body: str, loc_body: str, doc_spans: list[str]) -> tuple[str, int]:
    en_lines = en_body.splitlines()
    loc_lines = loc_body.splitlines()
    n = 0
    out_lines: list[str] = []
    for i, loc_line in enumerate(loc_lines):
        if "___" not in loc_line and "_ _ _" not in loc_line:
            out_lines.append(loc_line)
            continue
        en_line = en_lines[i] if i < len(en_lines) else ""
        line_spans = INLINE_SPAN_RE.findall(en_line) if en_line else doc_spans
        fixed, c = fix_body(loc_line, line_spans)
        n += c
        out_lines.append(fixed)
    return "\n".join(out_lines), n


def fix_locale_only_body(body: str, spans: list[str], en_body: str = "") -> tuple[str, int]:
    if en_body:
        aligned, n = fix_line_aligned(en_body, body, spans)
        fixed, c = fix_body(aligned, spans)
        return fixed, n + c
    return fix_body(body, spans)


def fix_full_markdown(text: str, spans: list[str] | None = None) -> tuple[str, int]:
    if spans is None:
        spans = spans_from_en_text(text)
    total = 0
    new = text
    if spans:
        for loc in LOCALES:
            pat = re.compile(
                rf'(<section lang="{re.escape(loc)}"[^>]*>\n\n)(.*?)(\n</section>)',
                re.DOTALL,
            )

            def sub(m: re.Match[str]) -> str:
                nonlocal total
                fixed, c = fix_body(m.group(2), spans)
                total += c
                return m.group(1) + fixed + m.group(3)

            new = pat.sub(sub, new, count=1)
    else:
        fixed, c = fix_body(text, [])
        total += c
        new = fixed
    return new, total
