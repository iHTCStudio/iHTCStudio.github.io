#!/usr/bin/env python3
"""Build privacy locale files: iDao→iMencius fork, then EN-diff token replace to other apps."""

from __future__ import annotations

import difflib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC_ROOT = ROOT / "_locale_sections"
LOCALES = ("ja", "ko", "ru", "th", "de", "fr", "tr")
APPS = [
    "iBaiJia",
    "iGuanZhi",
    "iGuige",
    "iHanFei",
    "iLvShi",
    "iMencius",
    "iMoZi",
    "iPrecepts",
    "iPrimer",
    "iRhyme",
    "iSage",
    "iShangYang",
    "iSiShu",
    "iSutra",
    "iThousand",
    "iWuJing",
    "iXin",
    "iXunZi",
    "iZen",
    "iZengZi",
    "iZhuangZi",
    "iZiSi",
]

EN_ONLY = re.compile(
    r'<section lang="en"[^>]*>\n?(?P<body>.*?)(?=\n<section lang=|\Z)',
    re.DOTALL,
)
SEC_ANY = re.compile(
    r'<section lang="([^"]+)"[^>]*>\n?(?P<body>.*?)(?=\n<section lang=|\Z)',
    re.DOTALL,
)


def en_lines(app: str) -> list[str]:
    m = EN_ONLY.search((ROOT / app / "privacy.md").read_text(encoding="utf-8"))
    assert m
    return [ln.rstrip() for ln in m.group("body").splitlines()]


def read_embedded_loc(app: str, lang: str) -> list[str]:
    sections = {}
    for m in SEC_ANY.finditer((ROOT / app / "privacy.md").read_text(encoding="utf-8")):
        sections[m.group(1)] = [ln.rstrip() for ln in m.group("body").splitlines()]
    return sections[lang]


def write_loc(app: str, lang: str, lines: list[str]) -> None:
    d = SEC_ROOT / app / "privacy"
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{lang}.md").write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def fork(base_en, base_loc, tgt_en, chunk_trans, lang):
    out = []
    sm = difflib.SequenceMatcher(None, base_en, tgt_en)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            out.extend(base_loc[i1:i2])
        elif tag in ("replace", "insert"):
            chunk = "\n".join(tgt_en[j1:j2])
            if chunk in chunk_trans and lang in chunk_trans[chunk]:
                out.extend(chunk_trans[chunk][lang].splitlines())
            else:
                out.extend(tgt_en[j1:j2])
    return out


def pair_replace(base_en, tgt_en):
    pairs = []
    sm = difflib.SequenceMatcher(None, base_en, tgt_en)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "replace" and i2 - i1 == 1 and j2 - j1 == 1:
            o, n = base_en[i1], tgt_en[j1]
            if o.strip() and n.strip() and o != n:
                pairs.append((o, n))
    return pairs


def apply_pairs(text: str, pairs: list[tuple[str, str]]) -> str:
    for o, n in sorted(pairs, key=lambda x: -len(x[0])):
        text = text.replace(o, n)
    return text


def main() -> None:
    chunk_dao_m = json.loads(
        (ROOT / "scripts" / "chunk_trans_dao_mencius.json").read_text(encoding="utf-8")
    )
    exact = json.loads((ROOT / "scripts" / "_privacy_exact_map.json").read_text(encoding="utf-8"))

    dao_en = en_lines("iDao")
    men_en = en_lines("iMencius")

    # 1) Fork iDao embedded → iMencius locale files
    for lang in LOCALES:
        base_loc = read_embedded_loc("iDao", lang)
        lines = fork(dao_en, base_loc, men_en, chunk_dao_m, lang)
        write_loc("iMencius", lang, lines)

    # Fill gaps in iMencius from exact map line-by-line
    for lang in LOCALES:
        path = SEC_ROOT / "iMencius" / "privacy" / f"{lang}.md"
        out_lines = []
        for line in men_en:
            if line in exact and lang in exact[line]:
                out_lines.append(exact[line][lang])
            else:
                # keep forked line if already translated (heuristic: not mostly ASCII words)
                out_lines.append(line)
        # merge: prefer exact map when fork left English
        merged = []
        forked = path.read_text(encoding="utf-8").splitlines()
        for i, eline in enumerate(men_en):
            if eline in exact and lang in exact[eline]:
                merged.append(exact[eline][lang])
            elif i < len(forked):
                merged.append(forked[i])
            else:
                merged.append(eline)
        write_loc("iMencius", lang, merged)

    men_loc = {lang: (SEC_ROOT / "iMencius" / "privacy" / f"{lang}.md").read_text(encoding="utf-8") for lang in LOCALES}

    # 2) Other apps: line-pair replace from iMencius EN diff + exact map override
    for app in APPS:
        if app == "iMencius":
            continue
        tgt = en_lines(app)
        pairs = pair_replace(men_en, tgt)
        for lang in LOCALES:
            body = men_loc[lang]
            body = apply_pairs(body, pairs)
            # line-wise exact map for target EN
            lines_out = []
            for line in tgt:
                if line in exact and lang in exact[line]:
                    lines_out.append(exact[line][lang])
                else:
                    # try pair-updated single line from men line at same index - fallback apply_pairs on line
                    lines_out.append(line if line not in body else line)
            # rebuild from tgt en using best effort: apply pairs to whole doc then align by line count via exact
            rebuilt = []
            for line in tgt:
                if line in exact and lang in exact[line]:
                    rebuilt.append(exact[line][lang])
                else:
                    rebuilt.append(apply_pairs(line, pairs) if line.strip() else line)
            write_loc(app, lang, rebuilt)

    print("batch_privacy_22_from_mencius: done")


if __name__ == "__main__":
    main()
