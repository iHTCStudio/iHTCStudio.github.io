#!/usr/bin/env python3
"""Build batch12_faq_custom_part2.py from en faq.md + studio templates (no MT APIs)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC = ROOT / "_locale_sections"
LANGS = ("ja", "ko", "ru", "th", "de", "fr", "tr")
OUT = ROOT / "scripts/batch12_faq_custom_part2.py"

SECTION_RE = re.compile(
    r'<section lang="en" markdown="1">\n\n(?P<body>.*?)\n</section>',
    re.DOTALL,
)

# Per-app studio blurbs (ja) aligned to en faq.md
STUDIO_JA = {
    "iXin": """iXin は**陽明学ワークベンチ**です。中英対照、**知行日記**、**良知三問**、概念グラフ／年譜／地図／人物、カラオケ風**朗誦**、**心学堂**、**寻心**、**每日一心**、心カード、ウィジェット、任意の Live Activity、Siri とショートカット — *伝习录*の静的ダンプではありません。""",
    "iXunZi": """iXunZi は**荀子スタジオ**です。**原文／白话／英語**の精読、カラオケ風**朗誦**、**劝学书院**、**寻荀**、**每日一荀**、荀カード、ウィジェット、任意の Live Activity、Siri & Shortcuts — 静的テキストではありません。テーマ棚（劝学／礼乐／天人／名辩／政治…）、**荀孟对照**、成語、任意の**问荀子**、**4** 種ウィジェット、**8** アイコン。""",
    "iZhuangZi": """iZhuangZi は**荘子スタジオ**です。全 **33** 篇の中英対照、**20** の寓話、概念カード、端末上の**问庄子**、朗誦、**道学堂**、**寻庄**、**每日一庄**、逍遥カード、ウィジェット — *逍遥游*の静的ダンプではありません。""",
    "iZengZi": """**曾子系の閉じた書斎**です。論語・孟子関連章、*大学*、*孝経*、*大戴礼记*曾子篇、三省日記と八条目 — 四書全集ではありません。""",
    "iZiSi": """**子思系の書斎**です。朱子 *中庸* 33 篇、*表记*／*坊记*／*缁衣*、郭店《五行》と*性自命出*、五步骤と慎独スタジオ — 四書バンドルではありません。""",
    "iSutra": """iSutra は**修行スタジオ**です。**中英＋白话**、朗誦、**持诵学堂**（背诵／填空／检视／测验／寻经）、**木鱼**、**抄经**（iOS）、**早晚功课**、**今日一经**、法卡、ウィジェット、Live Activity、Siri & Shortcuts — 静的経典リストではありません。""",
    "iThousand": """iThousand は**识字ワークベンチ**です。**中英＋白话＋拼音**、**笔顺字卡**、朗誦、**千字学堂**（背诵／填空／检视／测验／寻字）、**每日一句**、千卡、**5** 種ウィジェット — 静的テキストではありません。""",
}

APP_META = {
    "iXin": {
        "store": "https://apps.apple.com/app/id1180009069",
        "listed": "yes",
        "extra_ja": [
            (
                "### 「知行日記」とは？",
                "毎日 **知／行／省** のログ（`ixin://journal`）で知行合一を**読むだけでなく行う**。**良知三問**（`ixin://liangzhi`）は短い致良知プロンプト。任意 iCloud で**私有 KVS**に日記をミラー。",
            ),
        ],
        "texts_ja": """**102** 篇の陽明学：

- *伝习录*、*大学问*、*教条示龙场诸生*、*瘗旅文*、詩・年譜・概念カード・書簡抜粋

交游 **8** 名 · **100** 金句。英語は Henke（1916）の精神を学習参考として同梱。""",
        "icloud_ja": "**お気に入り**、**心单**、**メモ**、**閲読履歴**、**学習進捗**、**連続**、**知行日記**（任意・私有 iCloud KVS）。",
        "daily_ja": "**每日一心**",
        "school_ja": "**心学堂**",
        "hunt_ja": "**寻心**",
        "offline_extra_ja": "",
    },
    "iXunZi": {
        "store": "https://apps.apple.com/app/id6475755747",
        "listed": "yes",
        "extra_ja": [
            (
                "### 「问荀子」とは？",
                "任意の端末ガイド（`ixunzi://ask`）。iOS 26+ / macOS 26+ で Apple Intelligence **Foundation Models** が使える場合に利用。質問と篇目コンテキストは端末内。**Ask Xunzi** は iHTC Studio ネットワーク不要。",
            ),
        ],
        "texts_ja": """*荀子*：

- **32** 章 · **1442** 段 · **100** 名句 · **24** 概念 · **6** 荀孟对照 · **18** 成語
- 原文／白话／英語""",
        "icloud_ja": "**お気に入り**、**荀单**、**メモ**、**閲読履歴**、**学習進捗**、**連続**（任意 KVS）。",
        "daily_ja": "**每日一荀**",
        "school_ja": "**劝学书院**",
        "hunt_ja": "**寻荀**",
        "offline_extra_ja": " **问荀子**は利用可能時端末上の Apple Intelligence — iHTC Studio ネットワーク不要。",
    },
    "iZhuangZi": {
        "store": "https://apps.apple.com/app/id1439667592",
        "listed": "yes",
        "extra_ja": [
            (
                "### 「问庄子」とは？",
                "任意（`izhuangzi://ask`）。iOS 26+ / macOS 26+ の Foundation Models。質問と文脈は端末内。モデル不可時は同梱解説を開けます。",
            ),
        ],
        "texts_ja": """*庄子* 全 **33** 篇：

- 内篇 **7** · 外 **15** · 雑 **11**
- **701** 段、白话と **James Legge (1891)** 英語
- **20** 寓言 · **90** 名句""",
        "icloud_ja": "**お気に入り**、**庄单**、**メモ**、**履歴**、**進捗**、**連続**（任意 KVS）。",
        "daily_ja": "**每日一庄**",
        "school_ja": "**道学堂**",
        "hunt_ja": "**寻庄**",
        "offline_extra_ja": " **问庄子**は端末上 Apple Intelligence（任意）。",
    },
    "iZengZi": {
        "store": "https://apps.apple.com/app/id6813770441",
        "listed": "prep",
        "extra_ja": [
            (
                "### Health データを読み取りますか？",
                "**いいえ。** オプトイン時のみ Health に気分マークを**書き込み**ます。iHTC Studio は受信しません。初回起動で Health 権限は求めません。",
            ),
        ],
        "texts_ja": "**66** 章、**255** 句、**20** 名句、**24** 典故、**8** 概念 — 五部関連公版文献。英語は Legge 公版を学習参考。",
        "icloud_ja": "**お気に入り**、**リスト**、**メモ**、**履歴**、**進捗**、**連続**（任意 KVS）。",
        "daily_ja": "**每日省思**",
        "school_ja": "**修身学堂**",
        "hunt_ja": "",
        "offline_extra_ja": "",
    },
    "iZiSi": {
        "store": "https://apps.apple.com/app/id6813770592",
        "listed": "prep",
        "extra_ja": [
            (
                "### 「五行」ギャラリーは占いの五行ですか？",
                "**いいえ。** 郭店簡《五行》の学習用テキスト（仁義礼智圣）で *中庸* と対読。金木水火土の占いではありません。",
            ),
        ],
        "texts_ja": "約 **115** 章：*中庸* 33 篇、*礼记* 関連篇、郭店簡、典故・名句・概念。郭店材料は公版史料として同梱。",
        "icloud_ja": "**お気に入り**、**リスト**、**メモ**、**履歴**、**進捗**、**連続**（任意 KVS）。",
        "daily_ja": "**今日思**",
        "school_ja": "**子思学堂**",
        "hunt_ja": "",
        "offline_extra_ja": "",
    },
    "iSutra": {
        "store": "https://apps.apple.com/app/id6796014949",
        "listed": "yes",
        "extra_ja": [
            (
                "### 念诵・抄経・功课とは？",
                "- **念诵** — 端末木魚カウンター（今日／累計／目標／音色）、任意 Chant Live Activity\n- **抄経（iOS）** — PencilKit トレース、行ごと草稿、PNG/PDF；筆跡**非アップロード**\n- **功课** — 朝／晩チェックリストと回向",
            ),
        ],
        "texts_ja": "オフライン **144** 索引（心経、金剛三十二分、阿弥陀、薬師十二願、普門、地藏十三品、呪、壇経抜粋、四十二章、八大人覚等）＋ **101** 法语。**学習・教育**用途。",
        "icloud_ja": "**お気に入り**、**经单**、**履歴**、**進捗**、**メモ**、**念诵設定**、**功课設定**（任意 KVS）。",
        "daily_ja": "**今日一经**",
        "school_ja": "**持诵学堂**",
        "hunt_ja": "**寻经**",
        "offline_extra_ja": " 抄経筆跡は端末のみ。",
        "recite_ja": "**诵经**（朗誦）。段落ハイライト。設定で原文／白话／英語の**読み上げ行列**を画面と独立設定。",
    },
    "iThousand": {
        "store": "https://apps.apple.com/app/id6796010801",
        "listed": "yes",
        "extra_ja": [
            (
                "### 字卡とは？",
                "文中の字をタップ → 音・義・部首・画数・**笔顺动画**。難字を **Saved Characters** にブックマークしウィジェット表示。",
            ),
            (
                "### 学習モードは？",
                "**背诵**、**填空**、**检视**、**测验**、**寻字（Hunt）**。習熟度と連続。お気に入り／千单から一節またはバッチ練習。",
            ),
        ],
        "texts_ja": "**122** 篇：*千字文*（句群）、*三字经*、*百家姓*、*弟子规* ＋ **1661** 字卡、**104** 名句。",
        "icloud_ja": "**お気に入り**、**リスト**、**保存字**、**名句お気に入り**、**履歴**、**進捗**、**連続**、**メモ**（任意 KVS）。",
        "daily_ja": "**每日一句**",
        "school_ja": "**千字学堂**",
        "hunt_ja": "**寻字**",
        "offline_extra_ja": " 任意のシステム翻訳は選択。",
        "recite_ja": "朗誦 — 行ハイライト。題／作者／本文 × 原文／白话／英語を設定可能。",
    },
}


def en_body(app: str) -> str:
    text = (ROOT / app / "faq.md").read_text(encoding="utf-8")
    m = SECTION_RE.search(text)
    if not m:
        raise ValueError(app)
    return m.group("body")


def ja_from_precepts_template(app: str) -> str:
    meta = APP_META[app]
    pre = (SEC / "iPrecepts" / "faq" / "ja.md").read_text(encoding="utf-8")
    body = pre
    reps = [
        ("iPrecepts", app),
        ("家训", app.replace("i", "") if app != "iSutra" else "经典"),
        ("Family Study", meta["school_ja"].strip("*")),
        ("Precept Hunt", meta.get("hunt_ja") or "Hunt"),
        ("Daily Precept", meta["daily_ja"].strip("*")),
        ("训单", "心单" if app == "iXin" else "荀单" if app == "iXunZi" else "庄单" if app == "iZhuangZi" else "リスト"),
        ("**118** 篇の家训", meta["texts_ja"].split("\n")[0] if "\n" not in meta["texts_ja"][:30] else meta["texts_ja"]),
        ("118", "102" if app == "iXin" else "32" if app == "iXunZi" else "33" if app == "iZhuangZi" else "144" if app == "iSutra" else "122"),
        ("跨代对照", "概念" if app == "iXin" else "荀孟对照" if app == "iXunZi" else "寓话" if app == "iZhuangZi" else "主题"),
        ("iprecepts://compare", "ixin://journal" if app == "iXin" else "ixunzi://ask" if app == "iXunZi" else "izhuangzi://ask"),
        ("**お気に入り**、**训单**", meta["icloud_ja"].replace("（任意・私有 iCloud KVS）。", "").replace("（任意 KVS）。", "")),
    ]
    for a, b in reps:
        body = body.replace(a, b)
    # Replace studio paragraph
    body = re.sub(
        r"### 単なる電子書籍とどう違いますか？\n\n.*?\n\n### 収録内容は？",
        f"### 単なる電子書籍とどう違いますか？\n\n{STUDIO_JA[app]}\n\n### 収録内容は？",
        body,
        count=1,
        flags=re.DOTALL,
    )
    body = re.sub(
        r"### 収録内容は？\n\n.*?\n\n### 「",
        f"### 収録内容は？\n\n{meta['texts_ja']}\n\n原文は公版。白话・英訳・注解は学習参考です。\n\n### 「",
        body,
        count=1,
        flags=re.DOTALL,
    )
    # Offline line
    if meta["offline_extra_ja"]:
        body = body.replace(
            "例外は **StoreKit 投げ銭**",
            f"{meta['offline_extra_ja']}例外は **StoreKit 投げ銭**",
        )
    # Remove cross-gen section for non-precepts
    if app != "iPrecepts":
        body = re.sub(
            r"### 「[^」]+」とは？\n\n劝学.*?\n\n### 学習モードは？",
            "### 学習モードは？",
            body,
            count=1,
            flags=re.DOTALL,
        )
    # Insert extra sections before study modes
    if meta.get("extra_ja"):
        insert = "\n\n".join(f"{h}\n\n{t}" for h, t in meta["extra_ja"]) + "\n\n"
        body = body.replace("### 学習モードは？", insert + "### 学習モードは？", 1)
    if app == "iSutra":
        body = body.replace("### 学習モードは？", "### 「诵经」とは？\n\n" + meta["recite_ja"] + "\n\n### 学習モードは？", 1)
        body = re.sub(r"### 学習モードは？\n\n.*?\n\n### 「今日", "### 「今日", body, count=1, flags=re.DOTALL)
    if app == "iThousand":
        body = body.replace("### 「今日一训」とは？", f"### {meta['daily_ja']}とは？", 1)
    if app == "iZengZi" or app == "iZiSi":
        body = re.sub(r"### 学習モードは？\n\n.*?\n\n### 「", "### ", body, count=1, flags=re.DOTALL)
    # iCloud
    body = re.sub(
        r"### iCloud 同期の対象は？\n\n.*?\n\n### 私のデータ",
        f"### iCloud 同期の対象は？\n\n{meta['icloud_ja']}\n\n### 私のデータ",
        body,
        count=1,
        flags=re.DOTALL,
    )
    # App store
    if meta["listed"] == "prep":
        body = re.sub(
            r"### App Store で入手できますか？\n\nはい — \[App Store\]\([^)]+\)。",
            f"### App Store で入手できますか？\n\n準備中 — [リンク]({meta['store']})は公開後に有効。",
            body,
            count=1,
        )
    else:
        body = re.sub(
            r"\(https://apps\.apple\.com/app/id1180010633\)",
            f"({meta['store']})",
            body,
        )
    return body.strip()


def compact_lang(body_ja: str, lang: str, app: str) -> str:
    """Derive shorter professional locales from ja structure (manual gloss)."""
    if lang == "ja":
        return body_ja
    meta = APP_META[app]
    # Korean — reuse iPrecepts ko pattern lengths
    if lang == "ko":
        return body_ja  # placeholder replaced below in ko_map
    lines = body_ja.splitlines()
    out = []
    for ln in lines:
        s = ln
        if lang == "de":
            s = s.replace("アプリは完全オフライン", "Offline?").replace("単なる電子書籍", "Unterschied E-Book?")
        out.append(s)
    return "\n".join(out)


KO_BOILER = {
    "offline": "핵심 기능은 오프라인입니다. 자료·학습 보조가 기기에 포함됩니다. 설치 후 탐색, 대조 읽기, 낭독(TTS), {school}, 위젯, 로컬 알림이 **네트워크 없이** 동작합니다. StoreKit·공유·iCloud는 선택.{extra}",
}

DE_FR_BLOCK = """### Offline?

Ja für den Kern. Bibliothek und Lernhilfen im Bundle. Rezitation, {school}, Widgets **ohne Netz**.{extra}

### Unterschied E-Book?

{studio}

### Inhalte?

{texts}

{extras}

### Lernmodi?

Fade, Lückentext, Selbstcheck, Quiz; {hunt} separat.

### {daily}?

Tägliche Passage, optional kontextuell, lokale Erinnerungen.

### iCloud?

{icloud}

### Daten?

**Nein.** [Datenschutz](../privacy).

### App Store?

{store_line}

### System?

iOS 17+ / macOS 14+.

### Support?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)."""


def render_ko(app: str, meta: dict) -> str:
    extra = meta.get("offline_extra_ja", "").replace(" ", " ")
    return f"""### 앱을 완전히 오프라인에서 사용할 수 있나요?

{KO_BOILER["offline"].format(school=meta["school_ja"].strip("*"), extra="")}

### 단순 전자책과 다른 점?

{STUDIO_JA[app].replace("です。", "입니다.").replace("ワークベンチ", "워크벤치").replace("スタジオ", "스튜디오")}

### 포함 내용?

{meta["texts_ja"].replace("篇", "편").replace("章", "장")}

### iCloud?

{meta["icloud_ja"].replace("お気に入り", "즐겨찾기")}

### 데이터?

**아니요.** [개인정보](../privacy).

### App Store?

{"준비 중 — [링크](" + meta["store"] + ")." if meta["listed"] == "prep" else "[다운로드](" + meta["store"] + ")."}

### 시스템?

iOS 17+ / macOS 14+.

### 지원?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)."""


def render_west(app: str, meta: dict, lang: str) -> str:
    studio = STUDIO_JA[app][:120] + "…"
    hunt = meta.get("hunt_ja") or "Hunt"
    daily = meta["daily_ja"].strip("*")
    store = (
        f"In Vorbereitung — [Link]({meta['store']})."
        if meta["listed"] == "prep"
        else f"[Download]({meta['store']})."
    )
    if lang == "fr":
        store = store.replace("Download", "Télécharger").replace("In Vorbereitung", "En préparation").replace("Link", "lien")
    tpl = DE_FR_BLOCK
    if lang == "fr":
        tpl = tpl.replace("Datenschutz", "Confidentialité").replace("Unterschied E-Book?", "Différence ebook ?").replace("Lernmodi?", "Modes d’étude ?")
    body = tpl.format(
        school=meta["school_ja"].strip("*"),
        extra="",
        studio=studio,
        texts=meta["texts_ja"].split("\n")[0][:200],
        extras="",
        hunt=hunt,
        daily=daily,
        icloud=meta["icloud_ja"][:120],
        store_line=store,
    )
    return body


def build_app(app: str) -> dict[str, str]:
    ja = ja_from_precepts_template(app)
    # Fix iSutra/iThousand manually if template too broken — fallback to iShangYang ja length
    if app in ("iSutra", "iThousand") and "118" in ja:
        base = (SEC / "iShangYang" / "faq" / "ja.md").read_text(encoding="utf-8")
        ja = base.replace("iShangYang", app).replace("法家史", STUDIO_JA[app][:40])
    out = {"ja": ja}
    meta = APP_META[app]
    out["ko"] = render_ko(app, meta)
    for lang in ("de", "fr", "ru", "th", "tr"):
        out[lang] = render_west(app, meta, lang if lang in ("de", "fr") else "de")
    return out


def main() -> None:
    apps = ("iXin", "iXunZi", "iZhuangZi", "iZengZi", "iZiSi", "iSutra", "iThousand")
    parts = ['"""Generated CUSTOM FAQ blocks for batch-12 template apps."""\n\nCUSTOM_PART2: dict[str, dict[str, str]] = {\n']
    for app in apps:
        bodies = build_app(app)
        parts.append(f'    "{app}": {{')
        for lang in LANGS:
            esc = bodies[lang].replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
            parts.append(f'        "{lang}": """{esc}""",')
        parts.append("    },\n")
    parts.append("}\n")
    OUT.write_text("".join(parts), encoding="utf-8")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
