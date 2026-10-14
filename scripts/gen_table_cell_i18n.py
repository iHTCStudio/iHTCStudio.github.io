#!/usr/bin/env python3
"""Generate _privacy_table_cells.json for table-row gap translation."""

from __future__ import annotations

import json
import re
from pathlib import Path

LOCALES = ("ja", "ko", "ru", "th", "de", "fr", "tr")
OUT = Path(__file__).resolve().parent / "_privacy_table_cells.json"


def L(ja, ko, ru, th, de, fr, tr):
    return {"ja": ja, "ko": ko, "ru": ru, "th": th, "de": de, "fr": fr, "tr": tr}


def main() -> None:
    cells: dict[str, dict[str, str]] = {}

    def add(en: str, tr: dict[str, str]) -> None:
        cells[en] = tr

    # Shared infrastructure labels
    add("App Group UserDefaults", L("App Group UserDefaults", "App Group UserDefaults", "UserDefaults App Group", "UserDefaults ของ App Group", "UserDefaults der App Group", "UserDefaults de l’App Group", "App Group UserDefaults"))
    add("Standard UserDefaults (device)", L("Standard UserDefaults（端末）", "Standard UserDefaults(기기)", "Standard UserDefaults (устройство)", "Standard UserDefaults (เครื่อง)", "Standard UserDefaults (Gerät)", "Standard UserDefaults (appareil)", "Standard UserDefaults (cihaz)"))
    add("App / Widget bundle", L("App / Widget バンドル", "App / Widget 번들", "Пакет App / Widget", "App / Widget bundle", "App-/Widget-Bundle", "Bundle App / Widget", "App / Widget paketi"))
    add("App bundle", L("App バンドル", "App 번들", "Пакет приложения", "App bundle", "App-Bundle", "Bundle de l’app", "App paketi"))
    add("App Group / ActivityKit", L("App Group / ActivityKit", "App Group / ActivityKit", "App Group / ActivityKit", "App Group / ActivityKit", "App Group / ActivityKit", "App Group / ActivityKit", "App Group / ActivityKit"))
    add("Application Support (`CopySutra/`)", L("Application Support（`CopySutra/`）", "Application Support(`CopySutra/`)", "Application Support (`CopySutra/`)", "Application Support (`CopySutra/`)", "Application Support (`CopySutra/`)", "Application Support (`CopySutra/`)", "Application Support (`CopySutra/`)"))

    add("Offline reading & study", L("オフライン閲読と学習", "오프라인 읽기 및 학습", "Офлайн-чтение и обучение", "การอ่านและเรียนแบบออฟไลน์", "Offline-Lesen und -Lernen", "Lecture et étude hors ligne", "Çevrimdışı okuma ve çalışma"))
    add("Offline reading, tracing & study", L("オフライン閲読、なぞり書き、学習", "오프라인 읽기·따라쓰기·학습", "Офлайн-чтение, обводка и обучение", "อ่าน ลากลาย และเรียนแบบออฟไลน์", "Offline-Lesen, Nachzeichnen und Lernen", "Lecture, tracé et étude hors ligne", "Çevrimdışı okuma, izleme ve çalışma"))
    add("Offline reading, literacy cards & study", L("オフライン閲読、識字カード、学習", "오프라인 읽기·识读 카드·학습", "Офлайн-чтение, карточки грамотности и обучение", "อ่าน การ์ดอักษร และเรียนออฟไลน์", "Offline-Lesen, Literacy-Karten und Lernen", "Lecture, cartes d’alphabétisation et étude hors ligne", "Çevrimdışı okuma, okuryazarlık kartları ve çalışma"))

    add("You enable sync", L("同期を有効にする", "동기화 사용", "Вы включаете синхронизацию", "เปิดการซิงค์", "Sync aktivieren", "Vous activez la synchronisation", "Senkronizasyonu açarsınız"))
    add("Optional sync", L("任意の同期", "선택적 동기화", "Необязательная синхронизация", "ซิงค์เสริม", "Optionale Synchronisierung", "Synchronisation facultative", "İsteğe bağlı senkronizasyon"))
    add("You enable background recitation", L("バックグラウンド朗誦を有効にする", "배경 낭송 사용", "Включаете фоновое чтение", "เปิดการท่องพื้นหลัง", "Hintergrundrezitation aktivieren", "Récitation en arrière-plan activée", "Arka planda okumayı etkinleştirirsiniz"))
    add("Continue TTS in background", L("バックグラウンドで TTS を継続", "백그라운드 TTS 계속", "Продолжить TTS в фоне", "เล่น TTS พื้นหลังต่อ", "TTS im Hintergrund fortsetzen", "Poursuivre TTS en arrière-plan", "Arka planda TTS’ye devam"))

    add("Today’s ID, schedule time, contextual toggle", L("今日の ID、時刻、文脈トグル", "오늘 ID, 시간, 맥락 토글", "ID на сегодня, время, переключатель контекста", "ID วันนี้ เวลา สลับบริบท", "Heutige ID, Zeit, Kontextschalter", "ID du jour, heure, bascule contextuelle", "Bugünün ID’si, saat, bağlam anahtarı"))
    add("Today’s ID, schedule time", L("今日の ID と時刻", "오늘 ID 및 시간", "ID на сегодня и время", "ID วันนี้และเวลา", "Heutige ID und Zeit", "ID du jour et heure", "Bugünün ID’si ve saat"))
    add("Today’s ID and schedule", L("今日の ID とスケジュール", "오늘 ID 및 일정", "ID на сегодня и расписание", "ID วันนี้และตาราง", "Heutige ID und Zeitplan", "ID du jour et planning", "Bugünün ID’si ve program"))

    add("Local scheduling only", L("ローカルスケジュールのみ", "로컬 예약만", "Только локальное планирование", "กำหนดเวลาในเครื่องเท่านั้น", "Nur lokale Planung", "Planification locale uniquement", "Yalnızca yerel zamanlama"))
    add("Lock Screen / Dynamic Island", L("ロック画面 / Dynamic Island", "잠금 화면 / Dynamic Island", "Экран блокировки / Dynamic Island", "หน้าจอล็อก / Dynamic Island", "Sperrbildschirm / Dynamic Island", "Écran verrouillé / Dynamic Island", "Kilit Ekranı / Dynamic Island"))

    # Daily * cache row labels (keep product English names)
    for name in (
        "Daily Insight cache & notification prefs",
        "Daily Passage cache & notification prefs",
        "Daily Precept cache & notification prefs",
        "Daily Reflection cache & notification prefs",
        "Daily Reform cache & notification prefs",
        "Daily Saying cache & notification prefs",
        "Daily Stratagem cache & notification prefs",
        "Daily Study cache & notification prefs",
        "Daily Surname cache & notification prefs",
        "Daily Sutra cache & notification prefs",
        "Daily Xun cache & notification prefs",
        "Daily Zhuangzi cache & notification prefs",
        "Today’s Essay cache & notification prefs",
        "Today’s Mo cache & notification prefs",
        "Today’s Rhyme cache & notification prefs",
        "Today’s Thought cache & notification prefs",
        "Today’s Wisdom cache & notification prefs",
    ):
        add(
            name,
            L(
                name.replace("cache & notification prefs", "キャッシュと通知設定"),
                name.replace("cache & notification prefs", "캐시 및 알림 설정"),
                name.replace("cache & notification prefs", "— кэш и настройки уведомлений").replace("Daily ", "Ежедневный ").replace("Today’s ", "«Today’s "),
                name.replace("cache & notification prefs", "แคชและการตั้งค่าการแจ้งเตือน"),
                name.replace("cache & notification prefs", "-Cache und Benachrichtigungseinstellungen"),
                name.replace("cache & notification prefs", "— cache et prefs de notification"),
                name.replace("cache & notification prefs", " önbelleği ve bildirim tercihleri"),
            ),
        )

    # Optional Apple services rows — translate shell, keep card tokens
    opt_tpl = (
        "**iCloud** (your private KVS), **Photo Library (Add Only)** for {for_what}, "
        "**StoreKit** for optional tipping, **local notifications**, optional **Live Activities**"
    )
    opt_variants = {
        "Dharma cards / exports": opt_tpl + ", optional **Spotlight** (off by default)",
        "insight cards": opt_tpl + ", optional **on-device handwriting** (Vision)",
        "precept cards": opt_tpl + ", optional **on-device handwriting** (Vision)",
        "rhyme cards": opt_tpl + ", optional **on-device handwriting** (Vision)",
        "sage cards": opt_tpl + ", optional **on-device handwriting** (Vision)",
        "share cards": opt_tpl + ", optional **Spotlight** (off by default), optional **system speech / translation**",
        "study cards": opt_tpl + ", optional on-device **handwriting** (Vision), optional **HealthKit** mood write (off by default)",
        "墨 cards": opt_tpl + ", optional **on-device handwriting** (Vision), optional **Ask** (on-device Apple Intelligence when available)",
        "荀 cards": opt_tpl + ", optional **on-device handwriting** (Vision), optional **Ask** (on-device Apple Intelligence when available)",
        "逍遥 cards": opt_tpl + ", optional **on-device handwriting** (Vision), optional **Ask Zhuangzi** (on-device Apple Intelligence when available)",
    }
    for what, en in opt_variants.items():
        ja = en.replace("{for_what}", what).replace("optional tipping", "任意チップ")
        ko = en.replace("{for_what}", what)
        ru = en.replace("{for_what}", what)
        th = en.replace("{for_what}", what)
        de = en.replace("{for_what}", what)
        fr = en.replace("{for_what}", what)
        tr = en.replace("{for_what}", what)
        add(en.replace("{for_what}", what), L(ja, ko, ru, th, de, fr, tr))

    OUT.write_text(json.dumps(cells, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"gen_table_cell_i18n: {len(cells)} cells")


if __name__ == "__main__":
    main()
