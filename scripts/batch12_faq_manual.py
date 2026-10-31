#!/usr/bin/env python3
"""Professional FAQ bodies derived from iLunYu / iCouplet locale templates + per-app replacements."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC = ROOT / "_locale_sections"
LANGS = ("ja", "ko", "ru", "th", "de", "fr", "tr")

# (template_app, per-lang list of (old, new))
FROM_LUNYU = {
    "iXunZi": {
        "ja": [
            ("iLunYu", "iXunZi"),
            ("論語", "荀子"),
            ("*論語*", "*荀子*"),
            ("512", "32"),
            ("512** 章", "32** 章"),
            ("二十篇", "全書"),
            ("9** 名", "6** 件"),
            ("162", "100"),
            ("寻章", "寻荀"),
            ("読経単", "荀单"),
            ("意味チェック", "自己チェック"),
            ("Lernklasse", "Encouraging Learning Academy"),
            ("Nurturing", "Encouraging Learning"),
        ],
        "ko": [("iLunYu", "iXunZi"), ("논어", "순자"), ("512", "32"), ("寻章", "寻荀")],
        "de": [("iLunYu", "iXunZi"), ("Analects", "Xunzi"), ("512", "32"), ("寻章", "Xun Hunt")],
        "fr": [("iLunYu", "iXunZi"), ("Analects", "Xunzi"), ("512", "32")],
        "ru": [("iLunYu", "iXunZi"), ("512", "32")],
        "th": [("iLunYu", "iXunZi"), ("512", "32")],
        "tr": [("iLunYu", "iXunZi"), ("512", "32")],
    },
    "iZhuangZi": {
        "ja": [
            ("iLunYu", "iZhuangZi"),
            ("論語", "荘子"),
            ("512", "33"),
            ("寻章", "寻庄"),
            ("読経単", "庄单"),
        ],
        "ko": [("iLunYu", "iZhuangZi"), ("512", "33")],
        "de": [("iLunYu", "iZhuangZi"), ("512", "33")],
        "fr": [("iLunYu", "iZhuangZi"), ("512", "33")],
        "ru": [("iLunYu", "iZhuangZi"), ("512", "33")],
        "th": [("iLunYu", "iZhuangZi"), ("512", "33")],
        "tr": [("iLunYu", "iZhuangZi"), ("512", "33")],
    },
}

FROM_COUPLET = {
    "iSutra": {
        "ja": [
            ("iCouplet", "iSutra"),
            ("対聯", "经典"),
            ("3,369", "144"),
            ("寻联", "寻句"),
            ("今日の対聯", "今日经"),
            ("爱对联", "爱经文"),
        ],
        "ko": [("iCouplet", "iSutra"), ("3,369", "144")],
        "de": [("iCouplet", "iSutra"), ("3.369", "144")],
        "fr": [("iCouplet", "iSutra"), ("3 369", "144")],
        "ru": [("iCouplet", "iSutra"), ("3,369", "144")],
        "th": [("iCouplet", "iSutra"), ("3,369", "144")],
        "tr": [("iCouplet", "iSutra"), ("3,369", "144")],
    },
    "iThousand": {
        "ja": [
            ("iCouplet", "iThousand"),
            ("対聯", "字课"),
            ("3,369", "122"),
            ("寻联", "寻字"),
            ("今日の対聯", "今日一句"),
        ],
        "ko": [("iCouplet", "iThousand"), ("3,369", "122")],
        "de": [("iCouplet", "iThousand"), ("3.369", "122")],
        "fr": [("iCouplet", "iThousand"), ("3 369", "122")],
        "ru": [("iCouplet", "iThousand"), ("3,369", "122")],
        "th": [("iCouplet", "iThousand"), ("3,369", "122")],
        "tr": [("iCouplet", "iThousand"), ("3,369", "122")],
    },
}

CUSTOM: dict[str, dict[str, str]] = {
    "iPrecepts": {
        "ja": """### アプリは完全オフラインで使えますか？

主要な機能についてはオフラインで使えます。語料、白话、英訳、学習補助は端末に同梱されています。インストール後は、閲覧、対照閲読、朗誦（システム TTS）、家训学堂、ウィジェット、ローカルの毎日通知を**ネットワークなし**で利用できます。例外は **StoreKit 投げ銭**（Apple）、お客様が選んだ App への共有、任意の iCloud です。

### 単なる電子書籍とどう違いますか？

iPrecepts は**家训ワークベンチ**です。中英対照、**跨代对照**、カラオケ風**朗誦**、**家训学堂**、**寻训**、**今日一训**、训卡、ウィジェット、任意の Live Activity、Siri とショートカット — 静的テキストの置き場ではありません。

### 収録内容は？

**118** 篇の家训。朱子・朱柏廬、顔之推、諸葛亮、曽国藩、袁采、銭氏、康熙《庭訓格言》など。**14** 名 · **93** 金句。原文は公版。白话・英訳・注解は学習参考です。

### 「跨代对照」とは？

劝学・勤俭・言语・亲亲など**同じテーマ**を時代横断で並読。`iprecepts://compare` で開けます。

### 学習モードは？

**フェード**、**穴埋め**、**自己チェック**、**クイズ**、習熟度付き。ホームの **寻训** は別ゲームです。

### 「今日一训」とは？

ホームの毎日一篇。状況に合わせた選定と**ローカル**リマインダー（任意）。ウィジェット対応。

### iCloud 同期の対象は？

**お気に入り**、**训单**、**メモ**、**閲読履歴**、**学習進捗**、**連続記録**（任意・私有 iCloud KVS）。

### 私のデータを収集していますか？

**いいえ。** [プライバシーポリシー](../privacy)参照。Data Not Collected、広告/分析 SDK なし、アカウント不要。

### App Store Connect 用プライバシー URL？

[プライバシーポリシー](../privacy)を開き、URL をコピー。

### App Store で入手できますか？

はい — [App Store](https://apps.apple.com/app/id1180010633)。

### システム要件？

iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+**.

### サポート？

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 48 時間以内目安。""",
        "ko": """### 앱을 완전히 오프라인에서 사용할 수 있나요?

핵심 기능은 오프라인입니다. 라이브러리·白话·영어·학습 보조가 기기에 포함됩니다. 설치 후 탐색, 대조 읽기, 낭독(TTS), 가훈 학당, 위젯, 로컬 알림이 **네트워크 없이** 동작합니다. StoreKit 팁·공유·iCloud는 선택.

### 단순 전자책과 다른 점?

iPrecepts는 **가훈 워크벤치**: 이중 언어, **세대 간 대조**, 카라오ke式 낭독, **가훈 학당**, **寻训**, **오늘의 한 훈**, 카드, 위젯, Live Activity, Siri & Shortcuts.

### 포함 내용?

**118** 편, **14** 저자, **93** 명구. 공版 원문, 학습용 白话/영어.

### 세대 간 대조?

`iprecepts://compare` — 같은 가정·학습 테마를 시대별로 병렬 읽기.

### 학습 모드?

페이드, 빈칸, 자가 점검, 퀴즈, **寻训** 게임.

### 오늘의 한 훈?

홈 매일 구절, 맥락 추천, 로컬 알림(선택).

### iCloud?

즐겨찾기, 训单, 메모, 기록, 진행, 연속(선택).

### 데이터 수집?

**아니요.** [개인정보](../privacy).

### App Store?

[다운로드](https://apps.apple.com/app/id1180010633).

### 시스템?

iOS 17+ / macOS 14+.

### 지원?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com).""",
        "de": """### Offline?

Ja für den Kern. Bibliothek, Umgangssprache, Englisch und Lernhilfen im Bundle. Rezitation, Family Study, Widgets **ohne Netz**.

### Unterschied zum E-Book?

**Familien-Precept-Studio**: zweisprachig, **Parallelvergleich** über Generationen, Rezitation, Family Study, Precept Hunt, Daily Precept, Karten, Widgets.

### Inhalte?

**118** Werke, **14** Autoren, **93** berühmte Zeilen.

### Parallelvergleich?

Gleiches Haushaltsthema über Dynastien — `iprecepts://compare`.

### Lernmodi?

Fade, Lückentext, Selbstcheck, Quiz; Precept Hunt separat.

### Daily Precept?

Tägliche Passage, optional kontextuell, lokale Erinnerungen.

### iCloud?

Favoriten, Listen (训单), Notizen, Verlauf, Fortschritt, Serien (optional).

### Daten?

**Nein.** [Datenschutz](../privacy).

### App Store?

[Download](https://apps.apple.com/app/id1180010633).

### System?

iOS 17+ / macOS 14+.

### Support?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com).""",
        "fr": """### Hors ligne ?

Oui pour l’essentiel. Bibliothèque, vernaculaire, anglais et aides d’étude inclus. **Sans réseau** pour lire, réciter, Family Study, widgets.

### Différence avec un ebook ?

**Studio de préceptes familiaux** : lecture bilingue, **comparaison parallèle**, récitation, Family Study, Precept Hunt, Daily Precept, cartes, widgets.

### Textes ?

**118** œuvres, **14** auteurs, **93** citations.

### Comparaison parallèle ?

Même thème domestique à travers les dynasties — `iprecepts://compare`.

### Modes d’étude ?

Fade, lacunes, auto-vérification, quiz ; Precept Hunt séparé.

### Daily Precept ?

Passage quotidien, rappels locaux optionnels.

### iCloud ?

Favoris, listes (训单), notes, historique, progression, séries.

### Données ?

**Non.** [Confidentialité](../privacy).

### App Store ?

[Télécharger](https://apps.apple.com/app/id1180010633).

### Système ?

iOS 17+ / macOS 14+.

### Assistance ?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com).""",
        "ru": """### Офлайн?

Да для основного. Библиотека, vernacular, English в bundle. Чтение, декламация, Family Study, виджеты **без сети**.

### Отличие от ebook?

**Студия семейных наставлений**: двуязычие, **параллельное сравнение**, речь, Family Study, Precept Hunt, Daily Precept.

### Тексты?

**118** произведений, **14** авторов, **93** строки.

### Параллельное сравнение?

`iprecepts://compare`.

### Режимы?

Fade, пропуски, самопроверка, quiz; Precept Hunt отдельно.

### Daily Precept?

Ежедневный отрывок, локальные напоминания.

### iCloud?

Избранное, списки, заметки, история, прогресс, серии.

### Данные?

**Нет.** [Политика](../privacy).

### App Store?

[Загрузить](https://apps.apple.com/app/id1180010633).

### Система?

iOS 17+ / macOS 14+.

### Поддержка?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com).""",
        "th": """### ออฟไลน์?

ใช่สำหรับหลัก ไลบรารีและเครื่องมือเรียนในเครื่อง อ่าน ท่อง Family Study widgets **ไม่ใช้เน็ต**

### ต่างจาก ebook?

**สตูดิโอคำสอนครอบครัว** สองภาษา **เปรียบเทียบขนาน** ท่อง Family Study Precept Hunt Daily Precept

### เนื้อหา?

**118** เรื่อง **14** ผู้แต่ง **93** บรรทัด

### เปรียบเทียบขนาน?

`iprecepts://compare`

### โหมดเรียน?

Fade ช่องว่าง ตรวจเอง quiz

### Daily Precept?

ข้อความรายวัน แจ้งเตือนท้องถิ่น

### iCloud?

รายการโปรด ลists บันทึก ประวัติ

### ข้อมูล?

**ไม่** [นโยบาย](../privacy)

### App Store?

[ดาวน์โหลด](https://apps.apple.com/app/id1180010633)

### ระบบ?

iOS 17+ / macOS 14+

### ติดต่อ?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)""",
        "tr": """### Çevrimdışı?

Temel kullanım evet. Kütüphane cihazda. Okuma, ezber, Family Study, widget **internetsiz**.

### E-kitaptan fark?

**Aile öğüt stüdyosu**: iki dil, **paralel karşılaştırma**, ezber, Family Study, Precept Hunt, Daily Precept.

### Metinler?

**118** eser, **14** yazar, **93** dize.

### Paralel karşılaştırma?

`iprecepts://compare`

### Modlar?

Fade, boşluk, self-check, quiz.

### Daily Precept?

Günlük pasaj, yerel hatırlatıcı.

### iCloud?

Favoriler, listeler, notlar, geçmiş.

### Veri?

**Hayır.** [Gizlilik](../privacy).

### App Store?

[İndir](https://apps.apple.com/app/id1180010633).

### Sistem?

iOS 17+ / macOS 14+.

### Destek?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com).""",
    },
    "iShangYang": {
        "ja": """### アプリは完全オフラインで使えますか？

主要機能はオフラインです。語料と学習補助は端末同梱。閲覧、対照閲読、朗誦（TTS）、变法学堂、ウィジェット、毎日通知は**ネットワークなし**で利用できます。StoreKit・共有・iCloud は任意です。

### 単なる電子書籍とどう違いますか？

**法家史の書斎**です。四层読み（Duyvendak 1928 含む）、約 60 の变法詔、紀元前 361–338 年の編年、十四人の関係図 — 今日の統治口号的なものではなく**研究**向けです。

### 収録内容？

現存 24 篇、佚失 2 題、六法断片；1222 句の四層对齐；204 名句；60 詔；50 概念；30 編年；14 人物。原文と 1928 英訳は公版。白话は学習補助です。

### 「How to use」は今日の治国術？

**いいえ。** 制度設計理解のための自問チェック（誤り/正解/次の一歩）です。敏感な措置にはアプリ内注意があります。

### iCloud 同期？

お気に入り、リスト、メモ、履歴、進捗、連続（任意 KVS）。

### データ収集？

**いいえ。** [プライバシーポリシー](../privacy)。

### プライバシー URL？

[プライバシーポリシー](../privacy)から URL をコピー。

### App Store？

準備中 — [リンク](https://apps.apple.com/app/id6813769520)は公開後に有効。

### システム？

iOS 17+ / macOS 14+.

### サポート？

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com).""",
        "ko": """### 오프라인?

핵심 기능 오프라인. 자료·학습 보조 번들. 열람, 낭독, Reform Study, 위젯, 알림 **네트워크 없이**.

### 전자책과 차이?

**법가史 책상**: 4층 읽기, ~60 변법 조령, 기원전 361–338 연표, 14인 그래프 — **학술 연구**용.

### 내용?

24편, 1222문장, 204명구, 60조, 50개념, 30연표, 14인물.

### «How to use»는 통치법?

**아니요.** 제도 이해용 자가 점검.

### iCloud?

즐겨찾기, 목록, 메모, 기록, 진행, 연속.

### 데이터?

**아니요.** [개인정보](../privacy).

### App Store?

준비 중 — [링크](https://apps.apple.com/app/id6813769520).

### 시스템?

iOS 17+ / macOS 14+.

### 지원?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com).""",
        "de": """### Offline?

Kern offline. Reform Study, Widgets ohne Netz.

### Unterschied?

**Legalist history desk** — vier Schichten, ~60 Edikte, Chronik 361–338 v. Chr., Personengraph; **Studium**, keine Regierungsanleitung.

### Inhalte?

24 Kapitel, 1222 Sätze, 204 Zitate, 60 Edikte.

### «How to use»?

**Nein.** Selbstcheck zum Verständnis institutionellen Designs.

### iCloud?

Favoriten, Listen, Notizen, Verlauf, Fortschritt.

### Daten?

**Nein.** [Datenschutz](../privacy).

### App Store?

In Vorbereitung — [Link](https://apps.apple.com/app/id6813769520).

### System?

iOS 17+ / macOS 14+.""",
        "fr": """### Hors ligne ?

Oui pour l’essentiel. Reform Study, widgets sans réseau.

### Différence ?

**Bureau d’histoire légaliste** — lecture en quatre niveaux, ~60 édits, chronique, graphe ; **étude**, pas manuel de gouvernance.

### Textes ?

24 chapitres, 1222 phrases, 204 citations.

### « How to use » ?

**Non.** Aide de lecture pour comprendre le design institutionnel.

### iCloud ?

Favoris, listes, notes, historique, progression.

### Données ?

**Non.** [Confidentialité](../privacy).

### App Store ?

En préparation — [lien](https://apps.apple.com/app/id6813769520).""",
        "ru": """### Офлайн?

Да для основного. Reform Study, виджеты без сети.

### Отличие?

**Исторический desk легизма** — четыре слоя, ~60 указов, хроника, граф ; **учёба**, не руководство правителю.

### Тексты?

24 главы, 1222 предложения, 204 строки.

### «How to use»?

**Нет.** Самопроверка для понимания институтов.

### iCloud?

Избранное, списки, заметки, история.

### Данные?

**Нет.** [Политика](../privacy).

### App Store?

Готовится — [ссылка](https://apps.apple.com/app/id6813769520).""",
        "th": """### ออฟไลน์?

ใช่สำหรับหลัก Reform Study widgets ไม่ใช้เน็ต

### ต่างอย่างไร?

โต๊ะประวัติ **Legalist** สี่ชั้น ~60 ประกาศ ไทม์ไลน์ — **การศึกษา**

### เนื้อหา?

24 บท 1222 ประโยค

### How to use คือกฎเกณฑ์ปกครอง?

**ไม่** เป็นแบบทดสอบความเข้าใจ

### iCloud?

รายการโปรด ลists

### ข้อมูล?

**ไม่**

### App Store?

เตรียมลisting [ลิงก์](https://apps.apple.com/app/id6813769520)""",
        "tr": """### Çevrimdışı?

Temel kullanım evet. Reform Study, widget internetsiz.

### Fark?

**Legalist tarih masası** — dört katman, ~60 ferman; **araştırma**, yönetim rehberi değil.

### Metinler?

24 bölüm, 1222 cümle.

### «How to use»?

**Hayır.** Kurumsal tasarım için öz kontrol.

### iCloud?

Favoriler, listeler.

### Veri?

**Hayır.**

### App Store?

Hazırlanıyor — [bağlantı](https://apps.apple.com/app/id6813769520).""",
    },
    "iSiShu": {
        "ja": """### アプリは完全オフラインで使えますか？

主要機能はオフラインです。**四书**ライブラリは端末に同梱。閲覧、朗誦、学習、ウィジェット、ローカル通知は**ネットワークなし**で利用できます。

### 単なる電子書籍とどう違いますか？

iSiShu は**三語対照**の読書、朗誦、集中学習、今日の一言、ウィジェット、Spotlight、ディープリンクを備えた**学習空間**です。

### 収録内容は？

*大学*・*中庸*・*論語*・*孟子* から **1257** 篇。

### iCloud 同期の対象は？

お気に入り、リスト、履歴、進捗、連続記録、メモ（任意・私有 iCloud KVS）。

### 私のデータを収集していますか？

**いいえ。** [プライバシーポリシー](../privacy)を参照。

### App Store で入手できますか？

はい — [App Store でダウンロード](https://apps.apple.com/app/id6797013698)。""",
        "ko": """### 앱을 완전히 오프라인에서 사용할 수 있나요?

핵심 기능은 오프라인입니다. **四书** 라이브러리가 기기에 포함됩니다.

### 단순 전자책과 무엇이 다른가요?

iSiShu는 삼어 독서, 낭독, 학습, 오늘의 한 구절, 위젯, Spotlight, 딥링크가 있는 **학습 공간**입니다.

### 어떤 내용?

*대학*·*중용*·*논어*·*맹자* **1257** 편.

### iCloud 동기화?

즐겨찾기, 목록, 기록, 진행, 연속, 메모(선택).

### 데이터 수집?

**아니요.** [개인정보 처리방침](../privacy).

### App Store?

[다운로드](https://apps.apple.com/app/id6797013698).""",
        "de": """### Offline?

Kernfunktionen offline. Vier-Bücher-Bibliothek im Bundle.

### Unterschied zum E-Book?

iSiShu: dreisprachiges Lesen, Rezitation, Lernen, Daily Saying, Widgets, Spotlight, Deep Links.

### Inhalte?

**1257** Passagen aus den Vier Büchern.

### iCloud?

Favoriten, Listen, Verlauf, Fortschritt, Serien, Notizen (optional).

### Datenerhebung?

**Nein.** [Datenschutz](../privacy).

### App Store?

[Download](https://apps.apple.com/app/id6797013698).""",
        "fr": """### Hors ligne ?

Oui pour l’essentiel. Bibliothèque des Quatre Livres incluse.

### Différence avec un ebook ?

iSiShu : lecture trilingue, récitation, étude, Daily Saying, widgets, Spotlight, liens profonds.

### Contenus ?

**1257** passages.

### iCloud ?

Favoris, listes, historique, progression, séries, notes (optionnel).

### Données ?

**Non.** [Confidentialité](../privacy).

### App Store ?

[Télécharger](https://apps.apple.com/app/id6797013698).""",
        "ru": """### Офлайн?

Да для основного. Библиотека «Четырёх книг» в bundle.

### Отличие от ebook?

iSiShu: три языка, декламация, учёба, Daily Saying, виджеты, Spotlight.

### Тексты?

**1257** отрывков.

### iCloud?

Избранное, списки, история, прогресс, серии, заметки.

### Данные?

**Нет.** [Политика](../privacy).

### App Store?

[Загрузить](https://apps.apple.com/app/id6797013698).""",
        "th": """### ออฟไลน์?

ใช่สำหรับหลัก ไลบรารีสี่หนังสือในแอป

### ต่างจาก ebook?

iSiShu: อ่านสามภาษา ท่อง เรียน Daily Saying widgets Spotlight

### เนื้อหา?

**1257** ตอน

### iCloud?

รายการโปรด ลists ประวัติ ความคืบหน้า

### ข้อมูล?

**ไม่** [นโยบาย](../privacy)

### App Store?

[ดาวน์โหลด](https://apps.apple.com/app/id6797013698)""",
        "tr": """### Çevrimdışı?

Temel kullanım evet. Dört Kitap kütüphanesi cihazda.

### E-kitaptan fark?

iSiShu: üç dil, ezber, çalışma, Daily Saying, widget, Spotlight.

### İçerik?

**1257** pasaj.

### iCloud?

Favoriler, listeler, geçmiş, ilerleme.

### Veri?

**Hayır.** [Gizlilik](../privacy).

### App Store?

[İndir](https://apps.apple.com/app/id6797013698).""",
    },
    "iZen": {
        "ja": """### アカウントやネットワークは必要ですか？

**アカウント不要。** インストール後、練習、语录、科学、呼吸、音景、ツール、ウィジェット、ローカル通知は **オフライン** です。任意の iCloud、HealthKit（正念）、危機 Web リンク、StoreKit、メールは任意です。

### 瞑想アプリとどう違いますか？

iZen は**三層リカバリー**の道具箱：即時呼吸＋音景、日々の再構築（日誌・習慣）、根本の軽減（三つの課題・認知再構成）。**47** 練習、**約 500** 语录、**17** 科学ブリーフ同梱 — ループ音だけではありません。

### 三層とは？

1. **即時回復** — 呼吸、SOS、グラウンディング  
2. **日々の再構築** — マイクロ習慣、睡眠、日誌、運動・栄養  
3. **根本の軽減** — 三つの課題、境界、認知再構成  

`izen://browse/instant` などのディープリンクあり。

### 呼吸モードは？

**4-7-8**、**ボックス**、**生理的 sigh** など。テーマは水墨 / ソフトグロー。Live Activity・HealthKit は既定オフ。

### 音景はダウンロード音源？

**大容量トラックなし。** 端末上の**手続き合成**（雨、風など）。

### 1 分アセスメント？

睡眠・タスク・社交消耗から Home おすすめを調整。

### 危機ホットライン？

`crisis_helplines.json`（30+ 地域）同梱。**緊急サービスではありません。**

### iCloud は全部同期？

任意 KVS：お気に入り、禅リスト、ログ、自評、連続など。**iHTC Studio サーバーなし。**

### Spotlight は既定でオン？

**いいえ。** 設定で Spotlight 索引をオンにすると、ホーム画面検索から条文を探せます。

### Live Activity / HealthKit が動かない？

**既定オフ。** 設定で有効化し、**フォアグラウンド**で呼吸を開始。

### App Store Connect 用プライバシー URL？

[プライバシーポリシー](../privacy)を開き URL をコピー。

### システム要件？

iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+**.

### サポート？

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 48 時間以内目安。""",
        "ko": """### 계정·인터넷 필요?

**계정 불필요.** 설치 후 연습·명언·과학·호흡·사운드스케이프·도구·위젯·로컬 알림 **오프라인**. iCloud·HealthKit·위기 웹·StoreKit·메일은 선택.

### 명상 앱과 차이?

iZen: **3층 회복** 도구상자 — 즉시 호흡, 일일 재구축, 근본 완화. **47** 연습, **~500** 명언, **17** 과학 브리프.

### 3층?

즉시 / 일일 재구축 / 근본 완화. `izen://browse/instant` 딥링크.

### 호흡?

4-7-8, box, physiological sigh 등. Live Activity·HealthKit 기본 꺼짐.

### 사운드?

**대용량 다운로드 없음** — 기기 **합성**.

### 1분 평가?

수면·업무·소진 → Home 추천.

### 위기 helpline?

30+ 지역 JSON. **응급 서비스 아님.**

### iCloud?

선택 KVS — 즐겨찾기·선 리스트·로그·연속. **서버 없음.**

### Live Activity / HealthKit?

**기본 꺼짐** — 설정에서 켜고 포그라운드 호흡.

### 개인정보 URL?

[개인정보](../privacy) URL 복사.

### 요구 사항?

iOS 17+ / macOS 14+.

### 지원?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com).""",
        "de": """### Konto / Internet?

**Kein Konto.** Nach Installation offline für Übungen, Zitate, Wissenschaft, Atmung, Soundscape, Tools, Widgets, lokale Benachrichtigungen.

### Unterschied zur Meditations-App?

**Drei-Schichten-Recovery-Toolbox** mit 47 Übungen, ~500 Zitaten, 17 Wissenschaftsbriefs — nicht nur eine Schleife.

### Drei Schichten?

Sofort / täglicher Neuaufbau / Wurzelentlastung. Deep Links wie `izen://browse/instant`.

### Atmung?

4-7-8, Box, physiological sigh. Live Activity & HealthKit standardmäßig aus.

### Soundscape?

Prozedurale Synthese on-device, keine großen Downloads.

### 1-Minuten-Assessment?

Schlaf, Aufgabenlast, soziale Belastung → Home-Empfehlungen.

### Krisen-Hotlines?

Bundled JSON (30+ Regionen). **Kein Notdienst.**

### iCloud?

Optional KVS — Favoriten, Listen, Logs, Serien. Kein iHTC-Backend.

### Live Activity / HealthKit?

Standard aus — in Einstellungen aktivieren.

### Datenschutz-URL?

[Datenschutz](../privacy) öffnen und URL kopieren.

### System?

iOS 17+ / macOS 14+.

### Support?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com).""",
        "fr": """### Compte / Internet ?

**Pas de compte.** Usage principal hors ligne après installation.

### Différence avec une app de méditation ?

**Boîte à outils en trois couches** : 47 pratiques, ~500 citations, 17 briefs science.

### Trois couches ?

Récupération instantanée / reconstruction quotidienne / soulagement racine.

### Respiration ?

4-7-8, box, sigh physiologique. Live Activity & HealthKit désactivés par défaut.

### Paysage sonore ?

Synthèse procédurale sur l’appareil.

### Lignes d’aide ?

Répertoire bundled — **pas** un service d’urgence.

### iCloud ?

KVS privé optionnel. Pas de backend iHTC Studio.

### URL confidentialité ?

Ouvrir [confidentialité](../privacy) et copier l’URL.

### Système ?

iOS 17+ / macOS 14+.

### Assistance ?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com).""",
        "ru": """### Нужен аккаунт или интернет?

**Без аккаунта.** Основные функции офлайн после установки.

### Отличие от медитации?

**Трёхслойный набор восстановления**: 47 практик, ~500 цитат, 17 научных briefs.

### Три слоя?

Мгновенное / ежедневное / корневое облегчение.

### Дыхание?

4-7-8, box, physiological sigh. Live Activity и HealthKit выкл. по умолчанию.

### Звук?

Синтез на устройстве, без больших загрузок.

### Кризисные линии?

JSON в bundle. **Не** экстренная служба.

### iCloud?

Опциональный private KVS.

### URL политики?

[Политика](../privacy).

### Система?

iOS 17+ / macOS 14+.

### Поддержка?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com).""",
        "th": """### ต้องมีบัญชีหรือเน็ต?

**ไม่ต้องมีบัญชี** ใช้หลักออฟไลน์

### ต่างจากแอปสมาธิ?

กล่องเครื่องมือ **3 ชั้น** 47 แบบฝึก ~500 คำคม

### ชั้นสาม?

ทันที / สร้างใหม่รายวัน / ราก

### ลมหายใจ?

4-7-8 box sigh — Live Activity/HealthKit ปิดตามค่าเริ่ม

### เสียง?

สังเคราะห์บนเครื่อง

### สายด่วน?

JSON ในแอป **ไม่ใช่** ฉุกเฉิน

### iCloud?

KVS ทางเลือก

### URL นโยบาย?

[นโยบาย](../privacy)

### ระบบ?

iOS 17+ / macOS 14+

### ติดต่อ?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)""",
        "tr": """### Hesap / internet?

**Hesap gerekmez.** Kurulumdan sonra çevrimdışı çekirdek.

### Meditasyon farkı?

**Üç katmanlı iyileşme** — 47 pratik, ~500 alıntı.

### Üç katman?

Anında / günlük yeniden inşa / kök rahatlama.

### Nefes?

4-7-8, box, physiological sigh.

### Ses?

Cihazda sentez.

### Kriz hatları?

Bundle JSON — **acil servis değil**.

### iCloud?

İsteğe bağlı KVS.

### Gizlilik URL?

[Gizlilik](../privacy).

### Sistem?

iOS 17+ / macOS 14+.

### Destek?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com).""",
    },
    "iWuJing": {
        "ja": """### アプリは完全オフラインで使えますか？

はい。五経ライブラリは端末に同梱。閲読、朗誦、学習、ウィジェット、通知はオフラインです。

### 単なる読本との違いは？

iWuJing は**学習机**：二言語、注釈、異文、朗誦、五经学堂、Daily Classic、ウィジェット、Spotlight、ディープリンク。

### 収録内容？

**819** 篇（*詩経*・*書経*・*礼記*・*易経*・*春秋*左伝）。

### 周易は占いですか？

**いいえ。** 古典研究のみ。占い・予測機能はありません。

### iCloud 同期？

お気に入り、リスト、履歴、進捗、連続、メモ。

### データ収集？

**いいえ。** [プライバシーポリシー](../privacy)。

### App Store？

[ダウンロード](https://apps.apple.com/app/id6797013704)。""",
        "ko": """### 오프라인?

예. 오경 라이브러리 번들.

### 차이점?

iWuJing: 이중 언어, 주석, 낭독, 학습, Daily Classic, 위젯, Spotlight.

### 내용?

**819** 편.

### 주역 점?

**아니요.** 고전 연구만.

### iCloud?

즐겨찾기, 목록, 기록, 진행.

### 데이터?

**아니요.** [개인정보](../privacy).

### App Store?

[다운로드](https://apps.apple.com/app/id6797013704).""",
        "de": """### Offline?

Ja. Fünf-Klassiker-Bibliothek im Bundle.

### Unterschied?

iWuJing: zweisprachig, Glossen, Rezitation, Classics Study, Widgets.

### Inhalte?

**819** Passagen.

### Zhouyi-Wahrsagerei?

**Nein.** Nur Studium.

### iCloud?

Favoriten, Listen, Verlauf, Fortschritt.

### Daten?

**Nein.** [Datenschutz](../privacy).

### App Store?

[Download](https://apps.apple.com/app/id6797013704).""",
        "fr": """### Hors ligne ?

Oui. Bibliothèque des Cinq Classiques incluse.

### Différence ?

Lecture bilingue, gloses, récitation, étude, widgets.

### Contenus ?

**819** passages.

### Divination Zhouyi ?

**Non.** Étude classique seulement.

### iCloud ?

Favoris, listes, historique, progression.

### Données ?

**Non.** [Confidentialité](../privacy).

### App Store ?

[Télécharger](https://apps.apple.com/app/id6797013704).""",
        "ru": """### Офлайн?

Да. Пять классиков в bundle.

### Отличие?

Двуязычие, глоссы, декламация, учёба, виджеты.

### Тексты?

**819** отрывков.

### Гадание?

**Нет.** Только учёба.

### iCloud?

Избранное, списки, история.

### Данные?

**Нет.** [Политика](../privacy).

### App Store?

[Загрузить](https://apps.apple.com/app/id6797013704).""",
        "th": """### ออฟไลน์?

ใช่ ห้าคัมภีร์ในแอป

### ต่างอย่างไร?

อ่านสองภาษา ท่อง เรียน widgets

### เนื้อหา?

**819** ตอน

### โหราศาสตร์?

**ไม่**

### iCloud?

รายการโปรด ลists

### ข้อมูล?

**ไม่**

### App Store?

[ดาวน์โหลด](https://apps.apple.com/app/id6797013704)""",
        "tr": """### Çevrimdışı?

Evet. Beş Klasik bundle.

### Fark?

İki dil, ezber, çalışma, widget.

### İçerik?

**819** pasaj.

### Fal?

**Hayır.**

### iCloud?

Favoriler, listeler.

### Veri?

**Hayır.**

### App Store?

[İndir](https://apps.apple.com/app/id6797013704).""",
    },
}

try:
    from batch12_faq_custom_part2 import CUSTOM_PART2  # noqa: E402

    CUSTOM.update(CUSTOM_PART2)
except ImportError:
    pass


def _apply(template: str, reps: list[tuple[str, str]]) -> str:
    out = template
    for old, new in reps:
        out = out.replace(old, new)
    return out.strip()


def faq_body(app: str, lang: str) -> str:
    if app in CUSTOM and lang in CUSTOM[app]:
        return CUSTOM[app][lang]
    if app in FROM_COUPLET:
        base = (SEC / "iCouplet" / "faq" / f"{lang}.md").read_text(encoding="utf-8")
        reps = FROM_COUPLET[app].get(lang, FROM_COUPLET[app].get("ja", []))
        return _apply(base, reps)
    if app in FROM_LUNYU:
        base = (SEC / "iLunYu" / "faq" / f"{lang}.md").read_text(encoding="utf-8")
        reps = FROM_LUNYU[app].get(lang, FROM_LUNYU[app].get("ja", []))
        return _apply(base, reps)
    # default studio desk from iLunYu
    base = (SEC / "iLunYu" / "faq" / f"{lang}.md").read_text(encoding="utf-8")
    return _apply(base, [( "iLunYu", app)])


def all_faq_bodies() -> dict[str, dict[str, str]]:
    apps = (
        "iPrecepts",
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
    )
    return {a: {lang: faq_body(a, lang) for lang in LANGS} for a in apps}
