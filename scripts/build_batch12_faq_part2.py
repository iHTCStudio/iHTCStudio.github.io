#!/usr/bin/env python3
"""Build scripts/batch12_faq_custom_part2.py (hand-tuned, no MT)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC = ROOT / "_locale_sections"
OUT = ROOT / "scripts/batch12_faq_custom_part2.py"
LANGS = ("ja", "ko", "ru", "th", "de", "fr", "tr")


def from_precepts_ja(
    app: str,
    *,
    studio: str,
    texts: str,
    school: str,
    hunt: str,
    daily: str,
    list_name: str,
    icloud: str,
    store: str,
    listed: bool,
    offline_lead: str,
    mid_extra: str = "",
    drop_study: bool = False,
) -> str:
    b = (SEC / "iPrecepts/faq/ja.md").read_text(encoding="utf-8")
    b = b.replace("iPrecepts", app)
    b = re.sub(
        r"主要な機能についてはオフラインで使えます。.*?任意の iCloud です。",
        offline_lead,
        b,
        count=1,
        flags=re.S,
    )
    b = re.sub(
        r"### 単なる電子書籍とどう違いますか？\n\n.*?\n\n### 収録内容は？",
        f"### 単なる電子書籍とどう違いますか？\n\n{studio}\n\n### 収録内容は？",
        b,
        count=1,
        flags=re.S,
    )
    b = re.sub(
        r"### 収録内容は？\n\n.*?\n\n### 「",
        f"### 収録内容は？\n\n{texts}\n\n原文は公版。白话・英訳・注解は学習参考です。\n\n### 「",
        b,
        count=1,
        flags=re.S,
    )
    if mid_extra:
        b = re.sub(
            r"(### 「[^」]+」とは？\n\n.*?\n\n)(### 学習モードは？)",
            mid_extra + r"\2",
            b,
            count=1,
            flags=re.S,
        )
    else:
        b = re.sub(
            r"### 「[^」]+」とは？\n\n.*?\n\n### 学習モードは？",
            "### 学習モードは？",
            b,
            count=1,
            flags=re.S,
        )
    if drop_study:
        b = re.sub(
            r"### 学習モードは？\n\n.*?\n\n### 「",
            "### 「",
            b,
            count=1,
            flags=re.S,
        )
        b = re.sub(
            r"### 「[^」]+」とは？\n\nホームの毎日一篇.*?\n\n### iCloud",
            "### iCloud",
            b,
            count=1,
            flags=re.S,
        )
    if app == "iSutra":
        b = re.sub(
            r"### 学習モードは？\n\n.*?\n\n### 「今日",
            "### 「今日",
            b,
            count=1,
            flags=re.S,
        )
    b = b.replace("家训学堂", school.strip("*")).replace("寻训", hunt.strip("*")).replace("今日一训", daily.strip("*"))
    b = b.replace("训单", list_name)
    b = re.sub(
        r"### iCloud 同期の対象は？\n\n.*?\n\n### 私のデータ",
        f"### iCloud 同期の対象は？\n\n{icloud}\n\n### 私のデータ",
        b,
        count=1,
        flags=re.S,
    )
    b = b.replace("**フェード**、**穴埋め**、**自己チェック**、**クイズ**", "**フェード**、**穴埋め**、**自己チェック**、**クイズ**")
    b = b.replace("Precept Hunt", hunt).replace("寻章", hunt.strip("*"))
    if listed:
        b = re.sub(r"https://apps\.apple\.com/app/id\d+", store, b)
        b = re.sub(
            r"(### App Store で入手できますか？\n\n)はい — \[App Store\]\([^)]+\)。",
            rf"\1はい — [App Store]({store})。",
            b,
            count=1,
        )
    else:
        b = re.sub(
            r"(### App Store で入手できますか？\n\n)はい — \[App Store\]\([^)]+\)。",
            rf"\1準備中 — [リンク]({store})は公開後に有効。",
            b,
            count=1,
        )
    return b.strip()


def west_short(app: str, lang: str, meta: dict) -> str:
    labels = {
        "de": ("Offline?", "Unterschied?", "Inhalte?", "Daten?", "Datenschutz", "Support"),
        "fr": ("Hors ligne ?", "Différence ?", "Textes ?", "Données ?", "Confidentialité", "Assistance"),
        "ru": ("Офлайн?", "Отличие?", "Тексты?", "Данные?", "Политика", "Поддержка"),
        "th": ("ออฟไลน์?", "ต่างอย่างไร?", "เนื้อหา?", "ข้อมูล?", "นโยบาย", "ติดต่อ"),
        "tr": ("Çevrimdışı?", "Fark?", "Metinler?", "Veri?", "Gizlilik", "Destek"),
    }
    L = labels[lang]
    store = meta["store"]
    sl = (
        f"[Link]({store})." if lang == "de" else f"[lien]({store})." if lang == "fr" else f"[Store]({store})."
    )
    if not meta["listed"]:
        sl = "Listing vorbereitet — " + sl if lang == "de" else "En préparation — " + sl if lang == "fr" else sl
    no = {"de": "**Nein.**", "fr": "**Non.**", "ru": "**Нет.**", "th": "**ไม่**", "tr": "**Hayır.**"}[lang]
    return f"""### {L[0]}

Core offline — {meta['school']}, widgets, local notifications (see English FAQ).

### {L[1]}

{meta['studio_short']}

### {L[2]}

{meta['texts_short']}

### iCloud?

{meta['icloud_short']}

### {L[3]}

{no} [{L[4]}](../privacy).

### App Store?

{sl}

### System?

iOS 17+ / macOS 14+.

### {L[5]}?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)."""


def ko_body(meta: dict) -> str:
    store = meta["store"]
    listed = meta["listed"]
    return f"""### 앱을 완전히 오프라인에서 사용할 수 있나요?

{meta['offline_ko']}

### 단순 전자책과 다른 점?

{meta['studio_ko']}

### 포함 내용?

{meta['texts_ko']}

{meta.get('extra_ko', '')}

### iCloud?

{meta['icloud_ko']}

### 데이터 수집?

**아니요.** [개인정보](../privacy).

### App Store?

{"[다운로드](" + store + ")." if listed else "준비 중 — [링크](" + store + ")."}

### 시스템?

iOS 17+ / macOS 14+.

### 지원?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)."""


def build_all() -> dict[str, dict[str, str]]:
    apps: dict[str, dict[str, str]] = {}

    xun = from_precepts_ja(
        "iXunZi",
        studio="iXunZi は**荀子スタジオ**：原文／白话／英語、朗誦、**劝学书院**、**寻荀**、**每日一荀**、荀カード、ウィジェット、Live Activity、Siri & Shortcuts。テーマ棚、**荀孟对照**、成語、任意 **问荀子**、**4** ウィジェット、**8** アイコン。",
        texts="*荀子*：**32** 章 · **1442** 段 · **100** 名句 · **24** 概念 · **6** 荀孟对照 · **18** 成語（原文／白话／英語）。",
        school="劝学书院",
        hunt="寻荀",
        daily="每日一荀",
        list_name="荀单",
        icloud="**お気に入り**、**荀单**、**メモ**、**閲読履歴**、**学習進捗**、**連続**（任意 KVS）。",
        store="https://apps.apple.com/app/id6475755747",
        listed=True,
        offline_lead="主要機能はオフライン。語料と学習補助は端末同梱。インストール後、閲覧、朗誦、劝学书院、ウィジェット、通知は**ネットワークなし**。**问荀子**は利用可能時端末 Apple Intelligence（iHTC Studio ネットワーク不要）。StoreKit・共有・iCloud は任意。",
        mid_extra="### 「问荀子」とは？\n\n任意（`ixunzi://ask`）。iOS 26+ / macOS 26+ の Foundation Models。質問と篇目は端末内。\n\n",
    )
    apps["iXunZi"] = {"ja": xun}

    xin = from_precepts_ja(
        "iXin",
        studio="iXin は**陽明学ワークベンチ**：中英対照、**知行日記**、**良知三問**、概念グラフ／年譜／地図／人物、朗誦、**心学堂**、**寻心**、**每日一心**、心カード、ウィジェット — *伝习录*の静的ダンプではありません。",
        texts="**102** 篇：*伝习录*、*大学问*、*教条示龙场诸生*、*瘗旅文*、詩・年譜・概念カード。**8** 名 · **100** 金句。英語は Henke（1916）精神を学習参考。",
        school="心学堂",
        hunt="寻心",
        daily="每日一心",
        list_name="心单",
        icloud="**お気に入り**、**心单**、**メモ**、**履歴**、**進捗**、**連続**、**知行日記**（任意 KVS）。",
        store="https://apps.apple.com/app/id1180009069",
        listed=True,
        offline_lead="主要機能はオフライン。語料・白话・英訳・学習補助は同梱。心学堂・ウィジェット・通知は**オフライン**。StoreKit・共有・iCloud は任意。",
        mid_extra="### 「知行日記」とは？\n\n毎日 **知／行／省**（`ixin://journal`）。**良知三問**（`ixin://liangzhi`）。任意 iCloud で私有 KVS にミラー。\n\n",
    )
    apps["iXin"] = {"ja": xin}

    zhuang = from_precepts_ja(
        "iZhuangZi",
        studio="iZhuangZi は**荘子スタジオ**：全 **33** 篇、**20** 寓話、概念カード、**问庄子**、朗誦、**道学堂**、**寻庄**、**每日一庄**、逍遥カード。",
        texts="*庄子* **33** 篇（内 **7**・外 **15**・雑 **11**）、**701** 段、白话と Legge（1891）英語、**20** 寓言・**90** 名句。",
        school="道学堂",
        hunt="寻庄",
        daily="每日一庄",
        list_name="庄单",
        icloud="**お気に入り**、**庄单**、**メモ**、**履歴**、**進捗**、**連続**（任意 KVS）。",
        store="https://apps.apple.com/app/id1439667592",
        listed=True,
        offline_lead="主要機能オフライン。**问庄子**は端末 Apple Intelligence（任意）。StoreKit・共有・iCloud は任意。",
        mid_extra="### 「问庄子」とは？\n\n任意（`izhuangzi://ask`）。Foundation Models（iOS/macOS 26+）。\n\n",
    )
    apps["iZhuangZi"] = {"ja": zhuang}

    zeng = from_precepts_ja(
        "iZengZi",
        studio="**曾子系の閉じた書斎**：論孟関連、*大学*、*孝経*、大戴曾子、三省日記と八条目 — 四書全集ではありません。",
        texts="**66** 章、**255** 句、**20** 名句、**24** 典故、**8** 概念（五部公版）。英語は Legge 公版参考。",
        school="修身学堂",
        hunt="",
        daily="每日省思",
        list_name="リスト",
        icloud="**お気に入り**、**リスト**、**メモ**、**履歴**、**進捗**、**連続**（任意 KVS）。",
        store="https://apps.apple.com/app/id6813770441",
        listed=False,
        offline_lead="主要機能オフライン。修身学堂・ウィジェット・通知はネットワーク不要。StoreKit・共有・iCloud は任意。",
        mid_extra="### Health データを読み取りますか？\n\n**いいえ。** オプトイン時のみ Health に気分を**書き込み**。初回起動で Health 権限は要求しません。\n\n",
        drop_study=True,
    )
    apps["iZengZi"] = {"ja": zeng}

    zisi = from_precepts_ja(
        "iZiSi",
        studio="**子思系書斎**：*中庸* 33 篇、*表记*／*坊记*／*缁衣*、郭店《五行》・*性自命出*、五步骤と慎独 — 四書バンドルではありません。",
        texts="約 **115** 章：*中庸*、*礼记* 関連、郭店簡、典故・名句・概念（公版史料として同梱）。",
        school="子思学堂",
        hunt="",
        daily="今日思",
        list_name="リスト",
        icloud="**お気に入り**、**リスト**、**メモ**、**履歴**、**進捗**、**連続**（任意 KVS）。",
        store="https://apps.apple.com/app/id6813770592",
        listed=False,
        offline_lead="主要機能オフライン。子思学堂・ウィジェット・通知はネットワーク不要。",
        mid_extra="### 「五行」ギャラリーは占い？\n\n**いいえ。** 郭店《五行》学習用（仁義礼智圣）で *中庸* と対読。\n\n",
        drop_study=True,
    )
    apps["iZiSi"] = {"ja": zisi}

    sutra = from_precepts_ja(
        "iSutra",
        studio="iSutra は**修行スタジオ**：中英＋白话、朗誦、**持诵学堂**、**木鱼**、**抄経**（iOS）、**早晚功课**、**今日一经**、法卡、ウィジェット。",
        texts="**144** 索引（心経、金剛三十二分、阿弥陀、薬師、普門、地藏十三品、呪、壇経抜粋、四十二章、八大人覚等）＋ **101** 法语。学習・教育用途。",
        school="持诵学堂",
        hunt="寻经",
        daily="今日一经",
        list_name="经单",
        icloud="**お気に入り**、**经单**、**履歴**、**進捗**、**メモ**、**念诵設定**、**功课設定**（任意 KVS）。",
        store="https://apps.apple.com/app/id6796014949",
        listed=True,
        offline_lead="**144** 索引と経典データは同梱。閲覧・诵经・学堂・念诵・功课・ウィジェットは**オフライン**。抄経筆跡は端末のみ。StoreKit・共有は任意。",
        mid_extra="### 「诵经」とは？\n\n**诵经**＝朗誦。段落ハイライト。設定で原文／白话／英語の読み上げ。\n\n### 念诵・抄経・功课？\n\n木魚カウント、PencilKit 抄経（非アップロード）、朝夕チェックリスト。\n\n",
    )
    apps["iSutra"] = {"ja": sutra}

    thou = from_precepts_ja(
        "iThousand",
        studio="iThousand は**识字ワークベンチ**：中英＋白话＋拼音、**笔顺字卡**、朗誦、**千字学堂**、**每日一句**、千卡、**5** ウィジェット。",
        texts="**122** 篇（*千字文*、*三字经*、*百家姓*、*弟子规*）＋ **1661** 字卡、**104** 名句。",
        school="千字学堂",
        hunt="寻字",
        daily="每日一句",
        list_name="千单",
        icloud="**お気に入り**、**千单**、**保存字**、**名句お気に入り**、**履歴**、**進捗**、**連続**、**メモ**（任意 KVS）。",
        store="https://apps.apple.com/app/id6796010801",
        listed=True,
        offline_lead="**122** 篇・**1661** 字卡同梱。閲覧・千字学堂・寻字・ウィジェットは**オフライン**。StoreKit・任意翻訳・共有は選択。",
        mid_extra="### 字卡とは？\n\nタップで音・義・部首・**笔顺动画**。難字を Saved Characters へ。\n\n### 「朗誦」とは？\n\n製品用語＝朗读。行ハイライトに合わせる。設定で朗誦内容行列（題／作者／本文 × 原文／白话／英語）。\n\n",
    )
    apps["iThousand"] = {"ja": thou}

    meta_west = {
        "iXunZi": {
            "store": "https://apps.apple.com/app/id6475755747",
            "listed": True,
            "school": "Encouraging Learning Academy",
            "studio_short": "Xunzi studio — original/vernacular/English, recite, Ask Xunzi on-device.",
            "texts_short": "32 chapters, 1442 segments, 100 famous lines.",
            "icloud_short": "Favorites, lists (荀单), notes, history, progress, streaks.",
        },
        "iXin": {
            "store": "https://apps.apple.com/app/id1180009069",
            "listed": True,
            "school": "Heart School",
            "studio_short": "Yangming studio — Knowing-Acting journal, Daily Insight.",
            "texts_short": "102 passages; 8 authors; 100 lines.",
            "icloud_short": "Favorites, lists, notes, journal (optional KVS).",
        },
        "iZhuangZi": {
            "store": "https://apps.apple.com/app/id1439667592",
            "listed": True,
            "school": "Dao Study",
            "studio_short": "Zhuangzi studio — 33 chapters, Ask Zhuangzi.",
            "texts_short": "701 paragraphs; 20 parables; 90 lines.",
            "icloud_short": "Favorites, lists (庄单), notes, history.",
        },
        "iZengZi": {
            "store": "https://apps.apple.com/app/id6813770441",
            "listed": False,
            "school": "Cultivation Hall",
            "studio_short": "Closed Zengzi-line desk — 66 chapters.",
            "texts_short": "66 chapters, 255 sentences, 20 famous lines.",
            "icloud_short": "Favorites, lists, notes, history, streaks.",
        },
        "iZiSi": {
            "store": "https://apps.apple.com/app/id6813770592",
            "listed": False,
            "school": "Zisi Study",
            "studio_short": "Zisi-line desk — Zhongyong & Guodian slips.",
            "texts_short": "~115 chapters; Guodian Five Conducts for study.",
            "icloud_short": "Favorites, lists, notes, history.",
        },
        "iSutra": {
            "store": "https://apps.apple.com/app/id6796014949",
            "listed": True,
            "school": "Study Hall",
            "studio_short": "Practice studio — chant, copy-sutra, Daily Sutra.",
            "texts_short": "144-entry offline index; 101 famous lines.",
            "icloud_short": "Favorites, sutra lists, chant & practice prefs.",
        },
        "iThousand": {
            "store": "https://apps.apple.com/app/id6796010801",
            "listed": True,
            "school": "Primer Hall",
            "studio_short": "Literacy studio — 1661 character cards.",
            "texts_short": "122 passages; Thousand/Sanz/Bai/Dizi.",
            "icloud_short": "Favorites, lists, saved characters, notes.",
        },
    }

    for app, ja in list(apps.items()):
        m = meta_west[app]
        apps[app]["ko"] = ko_body(
            {
                "store": m["store"],
                "listed": m["listed"],
                "offline_ko": "핵심 오프라인. " + m["school"] + "·위젯·로컬 알림.",
                "studio_ko": m["studio_short"],
                "texts_ko": m["texts_short"],
                "icloud_ko": m["icloud_short"],
            }
        )
        for lang in ("de", "fr", "ru", "th", "tr"):
            apps[app][lang] = west_short(app, lang, m)

    return apps


def main() -> None:
    data = build_all()
    lines = [
        '"""CUSTOM FAQ blocks for batch-12 apps (aligned to en faq.md)."""\n\n',
        "CUSTOM_PART2: dict[str, dict[str, str]] = {\n",
    ]
    for app, by_lang in data.items():
        lines.append(f'    "{app}": {{\n')
        for lang in LANGS:
            body = by_lang[lang].replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
            lines.append(f'        "{lang}": """{body}""",\n')
        lines.append("    },\n")
    lines.append("}\n")
    OUT.write_text("".join(lines), encoding="utf-8")
    print("wrote", OUT, "apps", len(data))


if __name__ == "__main__":
    main()
