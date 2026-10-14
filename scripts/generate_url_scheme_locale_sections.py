#!/usr/bin/env python3
"""
Generate _locale_sections/{App}/url-scheme/{locale}.md from English sections.

Curated glossary for common phrases; Argos Translate (local packs) for the rest — no HTTP translation APIs.
Preserves ``` fences and `backticks`. Skip existing unless --force.
Then: python3 scripts/append_locale_sections.py
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SEC_ROOT = ROOT / "_locale_sections"
CACHE_PATH = ROOT / "scripts" / ".url_scheme_mt_cache.json"
SKIP_APPS = frozenset({"Weber", "GLUT"})
PHRASEBOOK_PATH = ROOT / "scripts" / "url_scheme_phrasebook.json"
SKIP_LINES = frozenset({"---", "</section>", ""})

CONFIG = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
NEW_LOCALES = [
    c["code"]
    for c in CONFIG["languages"]
    if c["code"] not in ("en", "zh-CN", "zh-TW")
]

SECTION_RE = re.compile(
    r'<section lang="en"[^>]*>\n?(?P<body>.*?)(?=\n<section lang=|\Z)',
    re.DOTALL,
)
FENCE_RE = re.compile(r"```[\s\S]*?```")
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
TABLE_SEP_RE = re.compile(r"^\|[\s\-:|]+\|$")

# Offline Argos Translate (installed language packs); no HTTP translation APIs.

TABLE_HDR: dict[str, dict[str, str]] = {
    "ja": {"URL": "URL", "Link": "リンク", "Opens": "開く画面"},
    "ko": {"URL": "URL", "Link": "링크", "Opens": "열리는 화면"},
    "ru": {"URL": "URL", "Link": "Ссылка", "Opens": "Открывает"},
    "th": {"URL": "URL", "Link": "ลิงก์", "Opens": "เปิด"},
    "de": {"URL": "URL", "Link": "Link", "Opens": "Öffnet"},
    "fr": {"URL": "URL", "Link": "Lien", "Opens": "Ouvre"},
    "tr": {"URL": "URL", "Link": "Bağlantı", "Opens": "Açar"},
}

# Professional hand-maintained strings (most frequent url-scheme table / heading text).
CURATED: dict[str, dict[str, str]] = {
    "Widget guide": {
        "ja": "ウィジェットガイド",
        "ko": "위젯 가이드",
        "ru": "Руководство по виджетам",
        "th": "คู่มือวิดเจ็ต",
        "de": "Widget-Anleitung",
        "fr": "Guide des widgets",
        "tr": "Widget kılavuzu",
    },
    "Usage guide": {
        "ja": "使い方ガイド",
        "ko": "사용 가이드",
        "ru": "Руководство по использованию",
        "th": "คู่มือการใช้งาน",
        "de": "Nutzungsanleitung",
        "fr": "Guide d'utilisation",
        "tr": "Kullanım kılavuzu",
    },
    "Shortcuts guide": {
        "ja": "ショートカットガイド",
        "ko": "단축어 가이드",
        "ru": "Руководство по «Командам»",
        "th": "คู่มือทางลัด",
        "de": "Kurzbefehle-Anleitung",
        "fr": "Guide Raccourcis",
        "tr": "Kısayol kılavuzu",
    },
    "Feedback email": {
        "ja": "フィードバックメール",
        "ko": "피드백 이메일",
        "ru": "Письмо с отзывом",
        "th": "อีเมลข้อเสนอแนะ",
        "de": "Feedback-E-Mail",
        "fr": "E-mail de commentaires",
        "tr": "Geri bildirim e-postası",
    },
    "Settings": {
        "ja": "設定",
        "ko": "설정",
        "ru": "Настройки",
        "th": "การตั้งค่า",
        "de": "Einstellungen",
        "fr": "Réglages",
        "tr": "Ayarlar",
    },
    "Favorites": {
        "ja": "お気に入り",
        "ko": "즐겨찾기",
        "ru": "Избранное",
        "th": "รายการโปรด",
        "de": "Favoriten",
        "fr": "Favoris",
        "tr": "Favoriler",
    },
    "Search": {
        "ja": "検索",
        "ko": "검색",
        "ru": "Поиск",
        "th": "ค้นหา",
        "de": "Suche",
        "fr": "Recherche",
        "tr": "Ara",
    },
    "Home": {
        "ja": "ホーム",
        "ko": "홈",
        "ru": "Главная",
        "th": "หน้าแรก",
        "de": "Startseite",
        "fr": "Accueil",
        "tr": "Ana sayfa",
    },
    "Reading history": {
        "ja": "閲覧履歴",
        "ko": "읽기 기록",
        "ru": "История чтения",
        "th": "ประวัติการอ่าน",
        "de": "Leseverlauf",
        "fr": "Historique de lecture",
        "tr": "Okuma geçmişi",
    },
    "Notes": {
        "ja": "ノート",
        "ko": "메모",
        "ru": "Заметки",
        "th": "บันทึก",
        "de": "Notizen",
        "fr": "Notes",
        "tr": "Notlar",
    },
    "Famous lines": {
        "ja": "名句一覧",
        "ko": "명구 목록",
        "ru": "Знаменитые строки",
        "th": "บรรทัดขึ้นชื่อ",
        "de": "Berühmte Zeilen",
        "fr": "Vers célèbres",
        "tr": "Ünlü dizeler",
    },
    "Replay onboarding": {
        "ja": "オンボーディングの再生",
        "ko": "온보딩 다시 보기",
        "ru": "Повторное знакомство",
        "th": "เล่นทัวร์แนะนำอีกครั้ง",
        "de": "Einführung erneut abspielen",
        "fr": "Rejouer l’accueil",
        "tr": "Tanıtımı yeniden oynat",
    },
    "Browse": {
        "ja": "ブラウズ",
        "ko": "둘러보기",
        "ru": "Обзор",
        "th": "เรียกดู",
        "de": "Durchsuchen",
        "fr": "Parcourir",
        "tr": "Gözat",
    },
    "Last read": {
        "ja": "最後に読んだ項目",
        "ko": "마지막으로 읽은 항목",
        "ru": "Последнее прочитанное",
        "th": "รายการที่อ่านล่าสุด",
        "de": "Zuletzt gelesen",
        "fr": "Dernière lecture",
        "tr": "Son okunan",
    },
    "Random passage": {
        "ja": "ランダムな章句",
        "ko": "무작위 구절",
        "ru": "Случайный отрывок",
        "th": "ข้อความแบบสุ่ม",
        "de": "Zufällige Passage",
        "fr": "Passage aléatoire",
        "tr": "Rastgele pasaj",
    },
    "In-app / Store review entry": {
        "ja": "アプリ内／App Store レビュー",
        "ko": "앱 내 / App Store 리뷰",
        "ru": "Отзыв в приложении / App Store",
        "th": "รีวิวในแอป / App Store",
        "de": "In-App- / App-Store-Bewertung",
        "fr": "Avis in-app / App Store",
        "tr": "Uygulama içi / App Store değerlendirme",
    },
    "Passage detail": {
        "ja": "章句の詳細",
        "ko": "구절 상세",
        "ru": "Страница отрывка",
        "th": "รายละเอียดข้อความ",
        "de": "Passagen-Detail",
        "fr": "Détail du passage",
        "tr": "Pasaj ayrıntısı",
    },
    "Recite flow": {
        "ja": "誦読フロー",
        "ko": "낭독 흐름",
        "ru": "Режим чтения вслух",
        "th": "โฟลว์การท่อง",
        "de": "Rezitationsablauf",
        "fr": "Flux de récitation",
        "tr": "Okuma akışı",
    },
    "Author detail": {
        "ja": "作者の詳細",
        "ko": "작가 상세",
        "ru": "Страница автора",
        "th": "รายละเอียดผู้แต่ง",
        "de": "Autorendetail",
        "fr": "Détail de l’auteur",
        "tr": "Yazar ayrıntısı",
    },
    "Search with query": {
        "ja": "キーワード付き検索",
        "ko": "검색어와 함께 검색",
        "ru": "Поиск с запросом",
        "th": "ค้นหาพร้อมคำค้น",
        "de": "Suche mit Suchbegriff",
        "fr": "Recherche avec requête",
        "tr": "Sorgu ile arama",
    },
    "Home tab": {
        "ja": "ホームタブ",
        "ko": "홈 탭",
        "ru": "Вкладка «Главная»",
        "th": "แท็บหน้าแรก",
        "de": "Register „Start“",
        "fr": "Onglet Accueil",
        "tr": "Ana sayfa sekmesi",
    },
    "Feature guide": {
        "ja": "機能ガイド",
        "ko": "기능 가이드",
        "ru": "Обзор функций",
        "th": "คู่มือฟีเจอร์",
        "de": "Funktionsübersicht",
        "fr": "Guide des fonctionnalités",
        "tr": "Özellik kılavuzu",
    },
    "In-app App Store rating": {
        "ja": "アプリ内 App Store 評価",
        "ko": "앱 내 App Store 평가",
        "ru": "Оценка в App Store из приложения",
        "th": "ให้คะแนน App Store ในแอป",
        "de": "App-Store-Bewertung in der App",
        "fr": "Note App Store in-app",
        "tr": "Uygulama içi App Store puanı",
    },
    "Link format": {
        "ja": "リンク形式",
        "ko": "링크 형식",
        "ru": "Формат ссылки",
        "th": "รูปแบบลิงก์",
        "de": "Linkformat",
        "fr": "Format de lien",
        "tr": "Bağlantı biçimi",
    },
    "Examples": {
        "ja": "例",
        "ko": "예시",
        "ru": "Примеры",
        "th": "ตัวอย่าง",
        "de": "Beispiele",
        "fr": "Exemples",
        "tr": "Örnekler",
    },
    "Destinations": {
        "ja": "行き先",
        "ko": "대상 화면",
        "ru": "Назначения",
        "th": "ปลายทาง",
        "de": "Ziele",
        "fr": "Destinations",
        "tr": "Hedefler",
    },
    "Discovery": {
        "ja": "発見",
        "ko": "탐색",
        "ru": "Обзор",
        "th": "ค้นพบ",
        "de": "Entdecken",
        "fr": "Découverte",
        "tr": "Keşfet",
    },
    "Settings & guides": {
        "ja": "設定とガイド",
        "ko": "설정 및 가이드",
        "ru": "Настройки и руководства",
        "th": "การตั้งค่าและคู่มือ",
        "de": "Einstellungen & Anleitungen",
        "fr": "Réglages et guides",
        "tr": "Ayarlar ve kılavuzlar",
    },
    "Learning": {
        "ja": "学習",
        "ko": "학습",
        "ru": "Обучение",
        "th": "การเรียนรู้",
        "de": "Lernen",
        "fr": "Apprentissage",
        "tr": "Öğrenme",
    },
    "Browse & search": {
        "ja": "閲覧と検索",
        "ko": "탐색 및 검색",
        "ru": "Обзор и поиск",
        "th": "เรียกดูและค้นหา",
        "de": "Durchsuchen & Suche",
        "fr": "Parcourir et rechercher",
        "tr": "Gözat ve ara",
    },
    "Navigation & guides": {
        "ja": "ナビゲーションとガイド",
        "ko": "탐색 및 가이드",
        "ru": "Навигация и руководства",
        "th": "การนำทางและคู่มือ",
        "de": "Navigation & Anleitungen",
        "fr": "Navigation et guides",
        "tr": "Gezinme ve kılavuzlar",
    },
    "Common links": {
        "ja": "よく使うリンク",
        "ko": "자주 쓰는 링크",
        "ru": "Частые ссылки",
        "th": "ลิงก์ที่ใช้บ่อย",
        "de": "Häufige Links",
        "fr": "Liens courants",
        "tr": "Sık kullanılan bağlantılar",
    },
    "Random entry": {
        "ja": "ランダムな項目",
        "ko": "무작위 항목",
        "ru": "Случайная запись",
        "th": "รายการแบบสุ่ม",
        "de": "Zufälliger Eintrag",
        "fr": "Entrée aléatoire",
        "tr": "Rastgele kayıt",
    },
    "Daily word": {
        "ja": "今日の単語",
        "ko": "오늘의 단어",
        "ru": "Слово дня",
        "th": "คำประจำวัน",
        "de": "Wort des Tages",
        "fr": "Mot du jour",
        "tr": "Günün kelimesi",
    },
    "SRS review session": {
        "ja": "SRS 復習セッション",
        "ko": "SRS 복습 세션",
        "ru": "Сессия повторения SRS",
        "th": "เซสชันทบ SRS",
        "de": "SRS-Wiederholung",
        "fr": "Session de révision SRS",
        "tr": "SRS tekrar oturumu",
    },
    "Learn center": {
        "ja": "学習センター",
        "ko": "학습 센터",
        "ru": "Центр обучения",
        "th": "ศูนย์การเรียนรู้",
        "de": "Lernzentrum",
        "fr": "Centre d’apprentissage",
        "tr": "Öğrenme merkezi",
    },
    "Browse all modules": {
        "ja": "すべてのモジュールを閲覧",
        "ko": "모든 모듈 탐색",
        "ru": "Обзор всех модулей",
        "th": "เรียกดูทุกโมดูล",
        "de": "Alle Module durchsuchen",
        "fr": "Parcourir tous les modules",
        "tr": "Tüm modüllere göz at",
    },
    "Browse idioms": {
        "ja": "熟語を閲覧",
        "ko": "관용구 탐색",
        "ru": "Обзор идиом",
        "th": "เรียกดูสำนวน",
        "de": "Idiome durchsuchen",
        "fr": "Parcourir les idiomes",
        "tr": "Deyimlere göz at",
    },
    "Specific entry": {
        "ja": "特定の項目",
        "ko": "특정 항목",
        "ru": "Конкретная запись",
        "th": "รายการที่ระบุ",
        "de": "Bestimmter Eintrag",
        "fr": "Entrée spécifique",
        "tr": "Belirli kayıt",
    },
    "Poem detail (e.g. id 1)": {
        "ja": "詩の詳細（例: id 1）",
        "ko": "시 상세(예: id 1)",
        "ru": "Страница стихотворения (напр. id 1)",
        "th": "รายละเอียดบทกวี (เช่น id 1)",
        "de": "Gedichtdetail (z. B. id 1)",
        "fr": "Détail du poème (p. ex. id 1)",
        "tr": "Şiir ayrıntısı (ör. id 1)",
    },
    "Poet detail": {
        "ja": "詩人の詳細",
        "ko": "시인 상세",
        "ru": "Страница поэта",
        "th": "รายละเอียดกวี",
        "de": "Dichterdetail",
        "fr": "Détail du poète",
        "tr": "Şair ayrıntısı",
    },
    "Recitation mode for a poem": {
        "ja": "詩の暗誦モード",
        "ko": "시 암송 모드",
        "ru": "Режим декламации стиха",
        "th": "โหมดท่องบทกวี",
        "de": "Rezitationsmodus für ein Gedicht",
        "fr": "Mode récitation pour un poème",
        "tr": "Şiir için ezber modu",
    },
    "Daily poem": {
        "ja": "今日の詩",
        "ko": "오늘의 시",
        "ru": "Стих дня",
        "th": "บทกวีประจำวัน",
        "de": "Gedicht des Tages",
        "fr": "Poème du jour",
        "tr": "Günün şiiri",
    },
    "Random poem": {
        "ja": "ランダムな詩",
        "ko": "무작위 시",
        "ru": "Случайное стихотворение",
        "th": "บทกวีแบบสุ่ม",
        "de": "Zufälliges Gedicht",
        "fr": "Poème aléatoire",
        "tr": "Rastgele şiir",
    },
    "Food detail": {
        "ja": "食品の詳細",
        "ko": "음식 상세",
        "ru": "Страница продукта",
        "th": "รายละเอียดอาหาร",
        "de": "Lebensmitteldetail",
        "fr": "Détail de l’aliment",
        "tr": "Yiyecek ayrıntısı",
    },
    "Nutrient encyclopedia entry": {
        "ja": "栄養素百科の項目",
        "ko": "영양소 백과 항목",
        "ru": "Статья энциклопедии нутриентов",
        "th": "รายการสารานุกรมสารอาหาร",
        "de": "Nährstoff-Lexikoneintrag",
        "fr": "Entrée encyclopédique nutriment",
        "tr": "Besin ansiklopedisi kaydı",
    },
    "Knowledge article": {
        "ja": "ナレッジ記事",
        "ko": "지식 아티클",
        "ru": "Обучающая статья",
        "th": "บทความความรู้",
        "de": "Wissensartikel",
        "fr": "Article de connaissances",
        "tr": "Bilgi makalesi",
    },
    "AI Label Reader (iOS 26+)": {
        "ja": "AI ラベルリーダー（iOS 26+）",
        "ko": "AI 라벨 리더(iOS 26+)",
        "ru": "AI Label Reader (iOS 26+)",
        "th": "AI Label Reader (iOS 26+)",
        "de": "AI Label Reader (iOS 26+)",
        "fr": "AI Label Reader (iOS 26+)",
        "tr": "AI Label Reader (iOS 26+)",
    },
    "BMI calculator": {
        "ja": "BMI 計算機",
        "ko": "BMI 계산기",
        "ru": "Калькулятор ИМТ",
        "th": "เครื่องคำนวณ BMI",
        "de": "BMI-Rechner",
        "fr": "Calculateur IMC",
        "tr": "BMI hesaplayıcı",
    },
    "BMR calculator": {
        "ja": "BMR 計算機",
        "ko": "BMR 계산기",
        "ru": "Калькулятор BMR",
        "th": "เครื่องคำนวณ BMR",
        "de": "BMR-Rechner",
        "fr": "Calculateur BMR",
        "tr": "BMR hesaplayıcı",
    },
    "TDEE calculator": {
        "ja": "TDEE 計算機",
        "ko": "TDEE 계산기",
        "ru": "Калькулятор TDEE",
        "th": "เครื่องคำนวณ TDEE",
        "de": "TDEE-Rechner",
        "fr": "Calculateur TDEE",
        "tr": "TDEE hesaplayıcı",
    },
    "All tools list": {
        "ja": "ツール一覧",
        "ko": "모든 도구 목록",
        "ru": "Список всех инструментов",
        "th": "รายการเครื่องมือทั้งหมด",
        "de": "Liste aller Tools",
        "fr": "Liste de tous les outils",
        "tr": "Tüm araçlar listesi",
    },
    "today’s Daily Classic": {
        "ja": "今日の Daily Classic",
        "ko": "오늘의 Daily Classic",
        "ru": "сегодняшний Daily Classic",
        "th": "Daily Classic วันนี้",
        "de": "heutiges Daily Classic",
        "fr": "Daily Classic du jour",
        "tr": "bugünün Daily Classic’i",
    },
    "recite a passage": {
        "ja": "章句を誦読",
        "ko": "구절 낭독",
        "ru": "прочитать отрывок вслух",
        "th": "ท่องข้อความ",
        "de": "Passage rezitieren",
        "fr": "réciter un passage",
        "tr": "pasaj okuma",
    },
    "study a passage": {
        "ja": "章句を学習",
        "ko": "구절 학습",
        "ru": "изучить отрывок",
        "th": "เรียนข้อความ",
        "de": "Passage studieren",
        "fr": "étudier un passage",
        "tr": "pasaj çalışma",
    },
    "a classic collection": {
        "ja": "古典コレクション",
        "ko": "고전 컬렉션",
        "ru": "классическую коллекцию",
        "th": "คอลเลกชันคลาสสิก",
        "de": "klassische Sammlung",
        "fr": "collection classique",
        "tr": "klasik koleksiyon",
    },
    "a theme": {
        "ja": "テーマ",
        "ko": "테마",
        "ru": "тему",
        "th": "ธีม",
        "de": "Thema",
        "fr": "thème",
        "tr": "tema",
    },
    "Search for poems containing 月": {
        "ja": "「月」を含む詩を検索",
        "ko": "「月」가 포함된 시 검색",
        "ru": "Поиск стихов с 月",
        "th": "ค้นหาบทกวีที่มี 月",
        "de": "Gedichte mit 月 suchen",
        "fr": "Rechercher des poèmes contenant 月",
        "tr": "月 içeren şiirleri ara",
    },
}


def load_phrasebook() -> dict[str, dict[str, str]]:
    book = dict(CURATED)
    if PHRASEBOOK_PATH.exists():
        extra = json.loads(PHRASEBOOK_PATH.read_text(encoding="utf-8"))
        book.update(extra)
    return book


PHRASEBOOK: dict[str, dict[str, str]] = {}

INTRO_TEMPLATES: dict[str, str] = {
    "ja": "{app} は **`{scheme}://`** ショートカットリンクに対応しています。",
    "ko": "{app}는 **`{scheme}://`** 바로가기 링크를 지원합니다.",
    "ru": "{app} поддерживает **`{scheme}://`** — ссылки-ярлыки.",
    "th": "{app} รองรับลิงก์ทางลัด **`{scheme}://`**",
    "de": "{app} unterstützt **`{scheme}://`**-Verknüpfungslinks.",
    "fr": "{app} prend en charge les liens **`{scheme}://`**.",
    "tr": "{app}, **`{scheme}://`** kısayol bağlantılarını destekler.",
}

_argos: dict[str, object] = {}
_mt_cache: dict[str, str] = {}


def load_mt_cache() -> None:
    global _mt_cache
    if CACHE_PATH.exists():
        _mt_cache = json.loads(CACHE_PATH.read_text(encoding="utf-8"))


def save_mt_cache() -> None:
    CACHE_PATH.write_text(json.dumps(_mt_cache, ensure_ascii=False, indent=0), encoding="utf-8")


def get_argos(locale: str):
    if locale in _argos:
        return _argos[locale]
    import argostranslate.translate

    tr = argostranslate.translate.get_translation_from_codes("en", locale)
    if tr is None:
        raise RuntimeError(f"Argos pack en→{locale} not installed")
    _argos[locale] = tr
    return tr


def mt_fallback(text: str, locale: str) -> str:
    key = f"{locale}:{text}"
    if key in _mt_cache:
        return _mt_cache[key]
    tr = get_argos(locale)
    # Argos works best on short segments; split long lines.
    if len(text) <= 500:
        out = tr.translate(text).strip()
    else:
        parts = re.split(r"(?<=[.!?])\s+", text)
        buf: list[str] = []
        chunk = ""
        for part in parts:
            piece = (chunk + " " + part).strip() if chunk else part
            if len(piece) > 450 and chunk:
                buf.append(tr.translate(chunk))
                chunk = part
            else:
                chunk = piece
        if chunk:
            buf.append(tr.translate(chunk))
        out = " ".join(buf).strip()
    _mt_cache[key] = out
    if len(_mt_cache) % 50 == 0:
        save_mt_cache()
    return out


def translate_phrase(text: str, locale: str) -> str:
    text = text.strip()
    if not text or text == "—":
        return text
    if text in PHRASEBOOK and locale in PHRASEBOOK[text]:
        return PHRASEBOOK[text][locale]
    if text.startswith("**") and text.endswith("**"):
        inner = text[2:-2]
        if inner in PHRASEBOOK and locale in PHRASEBOOK[inner]:
            return f"**{PHRASEBOOK[inner][locale]}**"
    return mt_fallback(text, locale)


def translate_intro(line: str, locale: str, app_id: str) -> str | None:
    m = re.match(
        r"^(\w+) supports \*\*`([a-z0-9]+)://`\*\* shortcut links\.?$",
        line.strip(),
        re.I,
    )
    if not m:
        return None
    scheme = m.group(2).lower()
    tpl = INTRO_TEMPLATES[locale]
    return tpl.format(app=app_id, scheme=scheme)


def translate_table_row(line: str, locale: str) -> str:
    if TABLE_SEP_RE.match(line.strip()):
        return line
    cells = line.split("|")
    inner = [c.strip() for c in cells[1:-1]]
    if len(inner) < 2:
        return line
    hdr = TABLE_HDR[locale]
    if inner[0].lower() in ("url", "link"):
        return "| " + " | ".join([hdr.get(inner[0], inner[0]), hdr.get(inner[1], inner[1])]) + " |"
    desc = translate_phrase(inner[-1], locale)
    return "| " + " | ".join(inner[:-1] + [desc]) + " |"


def translate_list_item(line: str, locale: str) -> str:
    m = re.match(r"^(\s*[-*+]\s+)(.+)$", line)
    if not m:
        return line
    prefix, rest = m.group(1), m.group(2)
    if " — " in rest:
        url_part, desc = rest.split(" — ", 1)
        return prefix + url_part + " — " + translate_phrase(desc, locale)
    return prefix + translate_phrase(rest, locale)


def translate_line(line: str, locale: str, app_id: str) -> str:
    stripped = line.strip()
    if stripped in SKIP_LINES or stripped.startswith("```"):
        return line
    if not stripped:
        return line
    if re.match(r"^[-*+]\s+", stripped):
        return translate_list_item(line, locale)
    if stripped.startswith("|"):
        return translate_table_row(line, locale)

    intro = translate_intro(stripped, locale, app_id)
    if intro:
        return intro

    codes: list[str] = []

    def stash(m: re.Match[str]) -> str:
        codes.append(m.group(0))
        return f"___C{len(codes)-1}___"

    tmp = INLINE_CODE_RE.sub(stash, line)
    hm = re.match(r"^(#{1,6})\s+(.*)$", tmp)
    if hm:
        title = hm.group(2).strip()
        translated = translate_phrase(title, locale) if title else title
        out = f"{hm.group(1)} {translated}"
    elif re.match(r"^>\s?", tmp):
        body = re.sub(r"^>\s?", "", tmp).strip()
        out = "> " + translate_phrase(body, locale) if body else line
    elif re.match(r"^[-*+]\s+", tmp):
        bm = re.match(r"^([-*+]\s+)(.*)$", tmp)
        out = bm.group(1) + translate_phrase(bm.group(2), locale) if bm else line
    else:
        out = translate_phrase(tmp, locale) if tmp.strip() else line

    for i, code in enumerate(codes):
        out = out.replace(f"___C{i}___", code)
    return out


def translate_body(body: str, locale: str, app_id: str) -> str:
    parts = re.split(r"(```[\s\S]*?```)", body)
    out_parts: list[str] = []
    for part in parts:
        if part.startswith("```"):
            out_parts.append(part)
            continue
        lines_out: list[str] = []
        for line in part.split("\n"):
            lines_out.append(translate_line(line, locale, app_id))
        out_parts.append("\n".join(lines_out))
    return "\n".join(out_parts).strip()


def extract_en(md_path: Path) -> str | None:
    m = SECTION_RE.search(md_path.read_text(encoding="utf-8"))
    return m.group("body").strip() if m else None


def main() -> None:
    global PHRASEBOOK
    PHRASEBOOK = load_phrasebook()
    parser = argparse.ArgumentParser()
    parser.add_argument("apps", nargs="*", help="App ids (default: all url-scheme.md)")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--locale", action="append", dest="locales", choices=NEW_LOCALES)
    args = parser.parse_args()
    load_mt_cache()

    apps = args.apps or sorted(
        p.parent.name for p in ROOT.glob("*/url-scheme.md") if p.parent.name not in SKIP_APPS
    )
    locales = args.locales or NEW_LOCALES
    written = skipped = 0

    for app_id in apps:
        md_path = ROOT / app_id / "url-scheme.md"
        if not md_path.exists():
            continue
        en_body = extract_en(md_path)
        if not en_body:
            print(f"skip no en: {app_id}", flush=True)
            continue
        for loc in locales:
            out_path = SEC_ROOT / app_id / "url-scheme" / f"{loc}.md"
            if out_path.exists() and not args.force:
                skipped += 1
                continue
            print(f"{app_id}/url-scheme → {loc}", flush=True)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(translate_body(en_body, loc, app_id) + "\n", encoding="utf-8")
            written += 1

    save_mt_cache()
    print(f"generate_url_scheme_locale_sections: wrote {written}, skipped {skipped}", flush=True)


if __name__ == "__main__":
    main()
