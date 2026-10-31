#!/usr/bin/env python3
"""Add hand translations for remaining privacy table rows into _privacy_gaps_22.json."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import render_hand_privacy_22 as r

GAPS_PATH = ROOT / "scripts" / "_privacy_gaps_22.json"
STILL = Path("/tmp/still150.txt")


def L(ja, ko, ru, th, de, fr, tr):
    return {"ja": ja, "ko": ko, "ru": ru, "th": th, "de": de, "fr": fr, "tr": tr}


# Column 1 labels (data / permission names)
COL1: dict[str, dict[str, str]] = {
    "Background audio (iOS)": L("バックグラウンド音声 (iOS)", "배경 오디오(iOS)", "Фоновое аудио (iOS)", "เสียงพื้นหลัง (iOS)", "Hintergrundaudio (iOS)", "Audio de fond (iOS)", "Arka plan sesi (iOS)"),
    "Background audio": L("バックグラウンド音声", "배경 오디오", "Фоновое аудио", "เสียงพื้นหลัง", "Hintergrundaudio", "Audio de fond", "Arka plan sesi"),
    "Card preferences": L("カード設定", "카드 설정", "Настройки карточек", "การตั้งค่าการ์ด", "Karten-Einstellungen", "Préférences de cartes", "Kart tercihleri"),
    "Chant counts & sound prefs": L("唱和回数と音設定", "염불 횟수·음향 설정", "Счётчики chant и звук", "จำนวน chant และเสียง", "Chant-Zähler & Ton", "Compteurs de chant et son", "Chant sayıları ve ses"),
    "Check-in streak": L("チェックイン連続", "체크인 연속", "Серия отметок", "สตรีคเช็คอין", "Check-in-Serie", "Série de check-in", "Check-in serisi"),
    "Content library": L("コンテンツライブラリ", "콘텐츠 라이브러리", "Библиотека контента", "คลังเนื้อหา", "Inhaltsbibliothek", "Bibliothèque de contenu", "İçerik kitaplığı"),
    "Copy-sutra drawings (iOS)": L("写経データ (iOS)", "필경 데이터(iOS)", "Рисунки Copy-sutra (iOS)", "ภาพ Copy-sutra (iOS)", "Copy-sutra-Zeichnungen (iOS)", "Dessins Copy-sutra (iOS)", "Copy-sutra çizimleri (iOS)"),
    "Favorites & Zen lists": L("お気に入りと禅リスト", "즐겨찾기·선 리스트", "Избранное и списки Zen", "รายการโปรด Zen", "Favoriten & Zen-Listen", "Favoris et listes Zen", "Favoriler ve Zen listeleri"),
    "Favorites & lists (essay lists)": L("お気に入りとリスト（essay lists）", "즐겨찾기·목록(essay lists)", "Избранное (essay lists)", "รายการโปรด (essay lists)", "Favoriten (essay lists)", "Favoris (essay lists)", "Favoriler (essay lists)"),
    "Favorites & lists (贤单)": L("お気に入りとリスト（贤单）", "즐겨찾기·목록(贤单)", "Избранное (贤单)", "รายการโปรด (贤单)", "Favoriten (贤单)", "Favoris (贤单)", "Favoriler (贤单)"),
    "Favorites & study lists": L("お気に入りと学習リスト", "즐겨찾기·학습 목록", "Избранное и учебные списки", "รายการโปรดและเรียน", "Favoriten & Lernlisten", "Favoris et listes d’étude", "Favoriler ve çalışma listeleri"),
    "Favorites & surname lists": L("お気に入りと姓氏リスト", "즐겨찾기·성씨 목록", "Избранное и списки фамилий", "รายการโปรดและนามสกุล", "Favoriten & Familienlisten", "Favoris et listes de noms", "Favoriler ve soyadı listeleri"),
    "Habit check-ins (洒扫应对)": L("習慣チェックイン（洒扫应对）", "습관 체크인(洒扫应对)", "Привычки (洒扫应对)", "เช็คอินนิสัย (洒扫应对)", "Gewohnheits-Check-ins (洒扫应对)", "Check-ins d’habitude (洒扫应对)", "Alışkanlık check-in (洒扫应对)"),
    "Health (Mindfulness)": L("ヘルス（マインドフルネス）", "건강(마음챙김)", "Health (осознанность)", "Health (Mindfulness)", "Health (Achtsamkeit)", "Santé (pleine conscience)", "Health (Mindfulness)"),
    "Health (Mood)": L("ヘルス（気分）", "건강(기분)", "Health (настроение)", "Health (อารมณ์)", "Health (Stimmung)", "Santé (humeur)", "Health (Ruh hali)"),
    "Journal, assessments, three tasks, cognitive entries": L("ジャーナル、評価、三タスク、認知記録", "저널·평가·세 과제·인지 기록", "Журнал, оценки, три задачи, записи", "บันทึก การประเมิน สามงาน ความคิด", "Journal, Assessments, drei Aufgaben", "Journal, évaluations, trois tâches", "Günlük, değerlendirmeler, üç görev"),
    "Knowing-Acting journal": L("知行合一ジャーナル", "지행합일 저널", "Журнал Knowing-Acting", "บันทึก Knowing-Acting", "Knowing-Acting-Tagebuch", "Journal Knowing-Acting", "Knowing-Acting günlüğü"),
    "Live Activities (iOS)": L("Live Activities (iOS)", "Live Activities(iOS)", "Live Activities (iOS)", "Live Activities (iOS)", "Live Activities (iOS)", "Live Activities (iOS)", "Live Activities (iOS)"),
    "Live Activities": L("Live Activities", "Live Activities", "Live Activities", "Live Activities", "Live Activities", "Live Activities", "Live Activities"),
    "Lüshi Chunqiu database": L("呂氏春秋データベース", "여씨춘추 DB", "База Lüshi Chunqiu", "ฐาน Lüshi Chunqiu", "Lüshi-Chunqiu-Datenbank", "Base Lüshi Chunqiu", "Lüshi Chunqiu veritabanı"),
    "Meditation streak & session prefs": L("瞑想連続とセッション設定", "명상 연속·세션 설정", "Серия медитации и настройки", "สตรีคสมาธิและการตั้งค่า", "Meditations-Serie & Sitzungen", "Série méditation et prefs", "Meditasyon serisi ve oturum"),
    "Morning / evening practice & dedication": L("朝夕の修行と回向", "아침·저녁 수행", "Утро/вечер практика", "ปฏิบัติเช้า-ค่ำ", "Morgen/Abend-Praxis", "Pratique matin/soir", "Sabah/akşam uygulama"),
    "My Surname": L("わたしの姓", "내 성씨", "Моя фамилия", "นามสกุลของฉัน", "Mein Familienname", "Mon nom de famille", "Soyadım"),
    "Notes": L("メモ", "메모", "Заметки", "บันทึก", "Notizen", "Notes", "Notlar"),
    "Notifications": L("通知", "알림", "Уведомления", "การแจ้งเตือน", "Benachrichtigungen", "Notifications", "Bildirimler"),
    "Optional Apple services": L("任意の Apple サービス", "선택 Apple 서비스", "Необязательные сервисы Apple", "บริการ Apple เสริม", "Optionale Apple-Dienste", "Services Apple facultatifs", "İsteğe bağlı Apple hizmetleri"),
    "Passage & character database": L("篇目・文字データベース", "구절·문자 DB", "База фрагментов и иероглифов", "ฐานข้อความและตัวอักษร", "Passagen- & Zeichendatenbank", "Base passages et caractères", "Pasaj ve karakter veritabanı"),
    "Photo Library (Add Only)": L("写真ライブラリ（追加のみ）", "사진 보관함(추가 전용)", "Фототека (только добавление)", "คลังรูปภาพ (เพิ่มอย่างเดียว)", "Fotomediathek (nur Hinzufügen)", "Photothèque (ajout uniquement)", "Fotoğraf Kitaplığı (yalnızca ekleme)"),
    "Photos (add)": L("写真（追加）", "사진(추가)", "Фото (добавление)", "รูปภาพ (เพิ่ม)", "Fotos (Hinzufügen)", "Photos (ajout)", "Fotoğraflar (ekleme)"),
    "Preferences": L("設定", "설정", "Настройки", "การตั้งค่า", "Einstellungen", "Préférences", "Tercihler"),
    "Reading history / last read": L("閲読履歴 / 最後に読んだ位置", "읽기 기록 / 마지막 읽기", "История / последнее чтение", "ประวัติ / อ่านล่าสุด", "Leseverlauf / zuletzt gelesen", "Historique / dernière lecture", "Okuma geçmişi / son okuma"),
    "Recent searches": L("最近の検索", "최근 검색", "Недавние запросы", "การค้นหาล่าสุด", "Letzte Suchen", "Recherches récentes", "Son aramalar"),
    "Reflection journal entries": L("省思ジャーナル", "성찰 저널", "Записи рефлексии", "บันทึกสะท้อนคิด", "Reflexionstagebuch", "Journal de réflexion", "Yansıma günlüğü"),
    "Sage-card preferences": L("賢カード設定", "현카드 설정", "Настройки sage-карт", "การตั้งค่า sage", "Sage-Karten-Einstellungen", "Préférences cartes sage", "Sage kart tercihleri"),
    "Saved characters & famous-line favorites": L("保存文字と名文お気に入り", "저장 글자·명문 즐겨찾기", "Сохранённые иероглифы и строки", "ตัวอักษรที่บันทึกและบรรทัดโปรด", "Gespeicherte Zeichen & Zeilen", "Caractères et lignes favorites", "Kayıtlı karakterler ve dizeler"),
    "Session history": L("セッション履歴", "세션 기록", "История сессий", "ประวัติเซสชัน", "Sitzungsverlauf", "Historique de session", "Oturum geçmişi"),
    "Shangjunshu library": L("商君書ライブラリ", "상군서 라이브러리", "Библиотека Shangjunshu", "คลัง Shangjunshu", "Shangjunshu-Bibliothek", "Bibliothèque Shangjunshu", "Shangjunshu kitaplığı"),
    "Share-card preferences": L("共有カード設定", "공유 카드 설정", "Настройки share-карт", "การตั้งค่าการ์ดแชร์", "Share-Karten-Einstellungen", "Préférences cartes partagées", "Paylaşım kartı tercihleri"),
    "Spotlight": L("Spotlight", "Spotlight", "Spotlight", "Spotlight", "Spotlight", "Spotlight", "Spotlight"),
    "Streaks & stats": L("連続と統計", "연속·통계", "Серии и статистика", "สตรีคและสถิติ", "Serien & Statistik", "Séries et stats", "Seriler ve istatistik"),
    "Study progress & high scores": L("学習進捗とハイスコア", "학습 진행·최고 점수", "Прогресс и рекорды", "ความคืบหน้าและคะแนนสูง", "Lernfortschritt & Highscores", "Progression et scores", "İlerleme ve skorlar"),
    "Study streak / check-in": L("学習連続 / チェックイン", "학습 연속 / 체크인", "Серия учёбы / check-in", "สตรีคเรียน / เช็คอין", "Lernserie / Check-in", "Série d’étude / check-in", "Çalışma serisi / check-in"),
    "Surname database & stroke glyphs": L("姓氏 DB と筆順", "성씨 DB·획순", "База фамилий и штрихи", "ฐานนามสกุลและลำดับขีด", "Familiennamen-DB & Striche", "Base noms et traits", "Soyadı DB ve vuruşlar"),
    "Sutra database (indexes, shards, large volumes)": L("経典 DB（索引・シャード・大容量）", "불경 DB(색인·샤드)", "База сутр (индексы, шарды)", "ฐานสutra (ดัชนี·ชards)", "Sutra-Datenbank (Indizes, Shards)", "Base sutras (index, shards)", "Sutra DB (indeks, parçalar)"),
    "Widget / Live Activity snapshots": L("Widget / Live Activity スナップショット", "Widget / Live Activity 스냅샷", "Снимки Widget / Live Activity", "สแนป Widget / Live Activity", "Widget-/Live-Activity-Schnappschüsse", "Instantanés Widget / Live Activity", "Widget / Live Activity anlık görüntüleri"),
    "Zengzi-line library": L("曾子系ライブラリ", "曾子 계열 라이브러리", "Библиотека линии Zengzi", "คลังสาย Zengzi", "Zengzi-Linien-Bibliothek", "Bibliothèque ligne Zengzi", "Zengzi hattı kitaplığı"),
    "Zisi-line library": L("子思系ライブラリ", "子思 계열 라이브러리", "Библиотека линии Zisi", "คลังสาย Zisi", "Zisi-Linien-Bibliothek", "Bibliothèque ligne Zisi", "Zisi hattı kitaplığı"),
    "iCloud": L("iCloud", "iCloud", "iCloud", "iCloud", "iCloud", "iCloud", "iCloud"),
}

COL2: dict[str, dict[str, str]] = {
    "You enable background recitation": L("バックグラウンド朗誦を有効にする", "배경 낭송 사용", "Включаете фоновое чтение", "เปิดท่องพื้นหลัง", "Hintergrundrezitation aktivieren", "Récitation en arrière-plan", "Arka planda okuma"),
    "You enable sync": L("同期を有効にする", "동기화 사용", "Включаете синхронизацию", "เปิดซิงค์", "Sync aktivieren", "Activez la sync", "Senkronizasyonu açarsınız"),
    "Optional sync": L("任意の同期", "선택 동기화", "Необяз. синхронизация", "ซิงค์เสริม", "Optionale Sync", "Sync facultative", "İsteğe bağlı sync"),
    "You enable Reading Live Activity": L("Reading Live Activity を有効", "Reading Live Activity 사용", "Reading Live Activity", "เปิด Reading Live Activity", "Reading Live Activity", "Reading Live Activity", "Reading Live Activity"),
    "You enable Reading or Chant Live Activity": L("Reading / Chant Live Activity", "Reading/Chant Live Activity", "Reading or Chant Live Activity", "Reading/Chant Live Activity", "Reading/Chant Live Activity", "Reading/Chant Live Activity", "Reading/Chant Live Activity"),
    "You enable Reading or Meditation Live Activity": L("Reading / Meditation Live Activity", "Reading/Meditation Live Activity", "Reading or Meditation Live Activity", "Reading/Meditation Live Activity", "Reading/Meditation Live Activity", "Reading/Meditation Live Activity", "Reading/Meditation Live Activity"),
    "You enable reading activity": L("閲読アクティビティを有効", "읽기 활동 사용", "Активность чтения", "เปิดกิจกรรมอ่าน", "Leseaktivität aktivieren", "Activité de lecture", "Okuma etkinliği"),
    "You enable reminders": L("リマインダーを有効", "알림 사용", "Включаете напоминания", "เปิดการเตือน", "Erinnerungen aktivieren", "Activez les rappels", "Hatırlatıcıları açarsınız"),
    "You enable journal sync in Settings": L("設定でジャーナル同期", "설정에서 저널 동기화", "Синхронизация журнала в Настройках", "ซิงค์บันทึกในตั้งค่า", "Journal-Sync in Einstellungen", "Sync journal dans Réglages", "Ayarlar’da günlük sync"),
    "You save a Dharma card or export": L("法カード保存または書き出し", "법 카드 저장/내보내기", "Сохранение Dharma-карты/экспорт", "บันทึก Dharma/ส่งออก", "Dharma-Karte speichern/exportieren", "Carte Dharma/enregistrement", "Dharma kartı/kaydet"),
    "You save a card": L("カードを保存", "카드 저장", "Сохраняете карту", "บันทึกการ์ด", "Karte speichern", "Enregistrer une carte", "Kart kaydetme"),
    "You save a classic card": L("古典カードを保存", "고전 카드 저장", "Сохранение classic card", "บันทึกการ์ดคลาสสิก", "Classic-Karte speichern", "Carte classique", "Klasik kart"),
    "You save a sage card": L("賢カードを保存", "현카드 저장", "Sage-карта", "บันทึก sage", "Sage-Karte speichern", "Carte sage", "Sage kartı"),
    "You save a share card or character image": L("共有カード/文字画像を保存", "공유 카드/글자 이미지 저장", "Share card / иероглиф", "บันทึกการ์ดแชร์/ตัวอักษร", "Share-Karte/Zeichenbild", "Carte partagée/caractère", "Paylaşım kartı/karakter"),
    "You save a share card": L("共有カードを保存", "공유 카드 저장", "Share card", "บันทึกการ์ดแชร์", "Share-Karte speichern", "Carte partagée", "Paylaşım kartı"),
    "Daily Zen / assessment reminders": L("Daily Zen / 評価リマインダー", "Daily Zen/평가 알림", "Daily Zen / оценки", "Daily Zen / ประเมิน", "Daily Zen / Assessment", "Daily Zen / évaluation", "Daily Zen / değerlendirme"),
    "Optional, off by default": L("任意・既定オフ", "선택·기본 끔", "Необяз., по умолчанию выкл.", "เสริม·ปิดตั้งต้น", "Optional, standardmäßig aus", "Facultatif, désactivé par défaut", "İsteğe bağlı, varsayılan kapalı"),
    "Save share cards": L("共有カードを保存", "공유 카드 저장", "Share cards", "บันทึกการ์ดแชร์", "Share-Karten speichern", "Enregistrer cartes partagées", "Paylaşım kartları"),
}

COL3: dict[str, dict[str, str]] = {
    "Continue TTS in background": L("バックグラウンドで TTS 継続", "백그라운드 TTS", "TTS в фоне", "TTS พื้นหลัง", "TTS im Hintergrund", "TTS en arrière-plan", "Arka planda TTS"),
    "Last style / ratio choices": L("最後のスタイル / 比率", "마지막 스타일/비율", "Последний стиль/ratio", "สไตล์/อัตราส่วนล่าสุด", "Letzter Stil/Verhältnis", "Dernier style/ratio", "Son stil/oran"),
    "Wooden-fish totals, goals, tones": L("木魚の合計・目標・音色", "목어 합계·목표·음색", "Wooden-fish, цели, тоны", "ปลาไม้ เป้า เสียง", "Wooden-fish, Ziele, Töne", "Wooden-fish, objectifs, tons", "Wooden-fish, hedefler, tonlar"),
    "Daily habit": L("毎日の習慣", "매일 습관", "Ежедневная привычка", "นิสัยรายวัน", "Tägliche Gewohnheit", "Habitude quotidienne", "Günlük alışkanlık"),
    "Bundled practices, quotes, science, crisis helplines": L("同梱の実践・引用・科学・危機ホットライン", "번들 실천·인용·과학·위기 helpline", "Встроенные практики, цитаты, наука, helpline", "แนวปฏิบัติ คำคม วิทย์ helpline", "Gebündelte Praktiken, Zitate, Wissenschaft, Helplines", "Pratiques, citations, science, helplines", "Paket uygulamalar, alıntılar, bilim, helpline"),
    "Per-line tracing drafts": L("行ごとのなぞり書き草稿", "줄별 따라쓰기 초안", "Черновики по строкам", "ร่างลากตามบรรทัด", "Entwürfe pro Zeile", "Brouillons par ligne", "Satır başına taslak"),
    "Starred items and custom collections": L("星付きとカスタムコレクション", "별표·사용자 모음", "Избранное и коллекции", "รายการติดดาวและคอลเลกชัน", "Favoriten & Sammlungen", "Favoris et collections", "Yıldızlı ve koleksiyonlar"),
    "Starred passages and user lists": L("星付きの篇とユーザーリスト", "별표 구절·목록", "Отмеченные фрагменты и списки", "ข้อความติดดาวและรายการ", "Markierte Passagen & Listen", "Passages favoris et listes", "Yıldızlı pasajlar ve listeler"),
    "Starred sayings and user lists": L("星付きの言葉とリスト", "별표 격언·목록", "Избранные sayings и списки", "คำคมติดดาวและรายการ", "Markierte Sayings & Listen", "Sayings favoris et listes", "Yıldızlı sözler ve listeler"),
    "Starred works and user lists": L("星付き作品とリスト", "별표 작품·목록", "Избранные произведения", "ผลงานติดดาวและรายการ", "Markierte Werke & Listen", "Œuvres favorites et listes", "Yıldızlı eserler ve listeler"),
    "Starred surnames and user lists": L("星付き姓氏とリスト", "별표 성씨·목록", "Избранные фамилии", "นามสกุลติดดาวและรายการ", "Markierte Familiennamen", "Noms favoris et listes", "Yıldızlı soyadları ve listeler"),
    "Life Guidance daily habits": L("Life Guidance 毎日の習慣", "Life Guidance 일일 습관", "Привычки Life Guidance", "นิสัยรายวัน Life Guidance", "Life-Guidance-Gewohnheiten", "Habitudes Life Guidance", "Life Guidance alışkanlıkları"),
    "Write minutes you choose": L("選択した分数を書き込み", "선택한 분 기록", "Запись выбранных минут", "บันทึกนาทีที่เลือก", "Gewählte Minuten schreiben", "Écrire les minutes choisies", "Seçilen dakikaları yaz"),
    "Write today’s three-axis mark to **your** Health app; never on first launch": L("今日の三軸を**お客様の**ヘルスへ書き込み（初回起動では要求しません）", "오늘 3축을 **Health**에 기록(첫 실행 시 요청 안 함)", "Трёхосевую отметку в **ваше** Health; не при первом запуске", "เขียนเครื่องหมายสามแกนไป **Health** ไม่ถามตอนเปิดครั้งแรก", "Dreier-Achsen-Mark ins **Health**; nicht beim Erststart", "Marque trois axes dans **Santé** ; pas au premier lancement", "Bugünün üç eksenini **Health**’e; ilk açılışta değil"),
    "Your structured logs": L("構造化ログ", "구조화된 로그", "Структурированные журналы", "บันทึกที่มีโครงสร้าง", "Strukturierte Protokolle", "Journaux structurés", "Yapılandırılmış günlükler"),
    "Daily known / acted / reflect entries": L("知・行・省の日次記録", "지·행·성찰 일일", "Ежедневные записи know/act/reflect", "บันทึกรู้/ทำ/สะท้อนรายวัน", "Tägliche know/act/reflect", "Entrées savoir/agir/réfléchir", "Günlük bil/eyle/yansıt"),
    "Show the saying you are reading on Lock Screen / Dynamic Island": L("読んでいる言葉をロック画面 / Dynamic Island に表示", "읽는 격언을 잠금/Dynamic Island", "Saying на Lock Screen / Dynamic Island", "แสดงคำคมบนหน้าจอล็อก/Dynamic Island", "Saying auf Sperrbildschirm/Dynamic Island", "Saying sur écran verrouillé/Dynamic Island", "Okunan söz Kilit Ekranı/Dynamic Island"),
    "Show reading / chant progress on Lock Screen / Dynamic Island": L("閲読 / 唱和進捗をロック画面 / Dynamic Island に", "읽기/chant 진행 표시", "Прогресс чтения/chant на Lock Screen", "ความคืบหน้าบนหน้าจอล็อก", "Lesen/Chant auf Sperrbildschirm", "Lecture/chant sur écran verrouillé", "Okuma/chant Kilit Ekranı"),
    "Lock Screen / Dynamic Island": L("ロック画面 / Dynamic Island", "잠금 화면 / Dynamic Island", "Lock Screen / Dynamic Island", "หน้าจอล็อก / Dynamic Island", "Sperrbildschirm / Dynamic Island", "Écran verrouillé / Dynamic Island", "Kilit Ekranı / Dynamic Island"),
    "Offline reading & study": L("オフライン閲読と学習", "오프라인 읽기·학습", "Офлайн-чтение и обучение", "อ่านและเรียนออฟไลน์", "Offline-Lesen und -Lernen", "Lecture et étude hors ligne", "Çevrimdışı okuma ve çalışma"),
    "Offline reading, literacy cards & study": L("オフライン閲読・識字カード・学習", "오프라인·识读 카드·학습", "Офлайн, карточки грамотности", "อ่าน การ์ดอักษร เรียน", "Offline, Literacy-Karten", "Lecture, cartes d’alphabétisation", "Çevrimdışı, okuryazarlık kartları"),
    "Offline reading, tracing & study": L("オフライン閲読・なぞり書き・学習", "오프라인·따라쓰기·학습", "Офлайн, обводка, обучение", "อ่าน ลากลาย เรียน", "Offline, Nachzeichnen, Lernen", "Lecture, tracé, étude", "Çevrimdışı, izleme, çalışma"),
    "Meditation continuity": L("瞑想の継続", "명상 연속", "Непрерывность медитации", "ความต่อเนื่องสมาธิ", "Meditationskontinuität", "Continuité méditation", "Meditasyon sürekliliği"),
    "Daily liturgy checklist": L("日課チェックリスト", "일과 체크리스트", "Ежедневный чеклист", "รายการพิธีรายวัน", "Tägliche Liturgie-Checkliste", "Checklist liturgie", "Günlük liturji listesi"),
    "Personalized home & widgets": L("ホームとウィジェットのパーソナライズ", "홈·위젯 개인화", "Персонализация дома и виджетов", "ปรับหน้าแรกและวิดเจ็ต", "Personalisierte Startseite & Widgets", "Accueil et widgets personnalisés", "Kişiselleştirilmiş ana ekran"),
    "Passage notes you write": L("篇についてのメモ", "구절 메모", "Заметки к фрагментам", "บันทึกข้อความ", "Passagen-Notizen", "Notes de passages", "Pasaj notları"),
    "Surname notes you write": L("姓氏についてのメモ", "성씨 메모", "Заметки о фамилиях", "บันทึกนามสกุล", "Familien-Notizen", "Notes sur noms", "Soyadı notları"),
    "Local scheduling only": L("ローカルスケジュールのみ", "로컬 예약만", "Только локальное планирование", "กำหนดในเครื่องเท่านั้น", "Nur lokale Planung", "Planification locale uniquement", "Yalnızca yerel zamanlama"),
    "Local Daily Classic reminders": L("Daily Classic ローカルリマインダー", "Daily Classic 로컬 알림", "Локальные Daily Classic", "เตือน Daily Classic ในเครื่อง", "Lokale Daily-Classic-Erinnerungen", "Rappels Daily Classic locaux", "Yerel Daily Classic hatırlatıcıları"),
    "Local Daily Saying reminders": L("Daily Saying ローカルリマインダー", "Daily Saying 로컬 알림", "Локальные Daily Saying", "เตือน Daily Saying ในเครื่อง", "Lokale Daily-Saying-Erinnerungen", "Rappels Daily Saying locaux", "Yerel Daily Saying hatırlatıcıları"),
    "Write the rendered image / PDF; we do not need full library read access": L("描画画像/PDF を書き込み（ライブラリ読取は不要）", "렌더 이미지/PDF 기록(전체 읽기 불필요)", "Запись изображения/PDF; без чтения библиотеки", "เขียนภาพ/PDF ไม่ต้องอ่านคลังทั้งหมด", "Gerendetes Bild/PDF; kein Vollzugriff", "Image/PDF rendu ; pas de lecture complète", "İşlenmiş görsel/PDF; tam okuma yok"),
    "Write the rendered image; we do not need full library read access": L("描画画像を書き込み（読取不要）", "렌더 이미지 기록", "Запись изображения; без чтения", "เขียนภาพที่เรนเดอร์", "Gerendetes Bild schreiben", "Image rendu", "İşlenmiş görsel yaz"),
    "Save rendered images": L("描画画像を保存", "렌더 이미지 저장", "Сохранение изображений", "บันทึกภาพที่เรนเดอร์", "Gerenderte Bilder speichern", "Enregistrer images rendues", "İşlenmiş görselleri kaydet"),
    "On-device images you choose": L("端末上の選択画像", "선택한 기기 내 이미지", "Изображения на устройстве", "รูปบนเครื่องที่คุณเลือก", "Bilder auf dem Gerät", "Images sur l’appareil", "Cihazdaki seçilen görseller"),
    "Theme, accent, breathing defaults, notifications, Live Activity, Spotlight": L("テーマ、アクセント、呼吸、通知、Live Activity、Spotlight", "테마·강조·호흡·알림·Live Activity·Spotlight", "Тема, акцент, дыхание, уведомления, Live Activity, Spotlight", "ธีม สี หายใจ แจ้งเตือน Live Activity Spotlight", "Theme, Akzent, Atmung, Benachrichtigungen, Live Activity, Spotlight", "Thème, accent, respiration, notifications, Live Activity, Spotlight", "Tema, vurgu, nefes, bildirimler, Live Activity, Spotlight"),
    "Continue browsing, history UI": L("閲覧続行・履歴 UI", "탐색 계속·기록 UI", "Продолжение просмотра, UI истории", "ท่องต่อ·UI ประวัติ", "Weiterstöbern, Verlaufs-UI", "Poursuite, UI historique", "Gezinme, geçmiş UI"),
    "Search history you typed": L("入力した検索履歴", "입력 검색 기록", "История введённого поиска", "ประวัติที่พิมพ์", "Suchverlauf Ihrer Eingaben", "Historique saisi", "Yazdığınız arama geçmişi"),
    "Life Guidance journal": L("Life Guidance ジャーナル", "Life Guidance 저널", "Журнал Life Guidance", "บันทึก Life Guidance", "Life-Guidance-Tagebuch", "Journal Life Guidance", "Life Guidance günlüğü"),
    "Hard-character bookmarks, starred lines": L("難字ブックマーク・星付き行", "어려운 글자·별표 줄", "Закладки сложных иероглифов", "ที่คั่นตัวยาก·บรรทัดติดดาว", "Schwierige Zeichen, markierte Zeilen", "Caractères difficiles, lignes favorites", "Zor karakterler, yıldızlı satırlar"),
    "Breathing / tool session records": L("呼吸 / ツールセッション記録", "호흡/도구 세션 기록", "Записи дыхания / инструментов", "บันทึกหายใจ/เซสชันเครื่องมือ", "Atem-/Tool-Sitzungen", "Sessions respiration/outils", "Nefes/araç oturumları"),
    "Index content on device": L("端末上でコンテンツを索引", "기기에서 콘텐츠 색인", "Индексирование на устройстве", "จัดทำดัชนีบนเครื่อง", "Inhalte auf dem Gerät indizieren", "Indexer sur l’appareil", "Cihazda dizinleme"),
    "Recovery dashboard and pressure curve": L("回復ダッシュボードと圧力曲線", "회복 대시보드·압력 곡선", "Панель recovery и кривая", "แดชบอร์ดฟื้นตัวและเส้นแรงดัน", "Recovery-Dashboard und Kurve", "Tableau recovery et courbe", "İyileşme panosu ve eğri"),
    "Study Hall state": L("Study Hall 状態", "Study Hall 상태", "Состояние Study Hall", "สถานะ Study Hall", "Study-Hall-Status", "État Study Hall", "Study Hall durumu"),
    "Daily Study habit": L("Daily Study 習慣", "Daily Study 습관", "Привычка Daily Study", "นิสัย Daily Study", "Daily-Study-Gewohnheit", "Habitude Daily Study", "Daily Study alışkanlığı"),
    "Display text / chant state you already opened": L("既に開いたテキスト / chant 状態を表示", "연 텍스트/chant 상태 표시", "Отображение открытого текста/chant", "แสดงข้อความ/chant ที่เปิดแล้ว", "Anzeige geöffneter Text/Chant", "Texte/chant déjà ouverts", "Açılmış metin/chant durumu"),
    "Mirror your progress": L("進捗をミラー", "진행 미러", "Зеркалирование прогресса", "สะท้อนความคืบหน้า", "Fortschritt spiegeln", "Miroir de progression", "İlerlemeyi yansıt"),
}

# Daily cache rows share col3 patterns
for suffix in (
    "Today’s ID, schedule time, contextual toggle",
    "Today’s ID, schedule time",
    "Today’s ID and schedule",
):
    COL3[suffix] = L(
        suffix.replace("Today’s ID", "今日の ID").replace("schedule time", "時刻").replace("contextual toggle", "文脈トグル").replace("and schedule", "とスケジュール"),
        suffix.replace("Today’s ID", "오늘 ID").replace("schedule time", "시간"),
        "ID на сегодня, время, переключатели",
        suffix.replace("Today’s ID", "ID วันนี้"),
        suffix.replace("Today’s ID", "Heutige ID"),
        suffix.replace("Today’s ID", "ID du jour"),
        suffix.replace("Today’s ID", "Bugünün ID’si"),
    )

SYNC_SCOPES = {
    "Sync favorites, lists, progress, notes": L("お気に入り、リスト、進捗、メモを同期", "즐겨찾기·목록·진행·메모 동기화", "Избранное, списки, прогресс, заметки", "ซิงค์รายการโปรด รายการ ความคืบหน้า บันทึก", "Favoriten, Listen, Fortschritt, Notizen", "Favoris, listes, progression, notes", "Favoriler, listeler, ilerleme, notlar"),
    "Sync favorites / lists / history / progress / streaks / notes": L("お気に入り/リスト/履歴/進捗/連続/メモを同期", "즐겨찾기/목록/기록/진행/연속/메모", "Избранное/списки/история/прогресс/серии/заметки", "ซิงค์รายการโปรด/รายการ/ประวัติ/ความคืบหน้า/สตรีค/บันทึก", "Favoriten/Listen/Verlauf/Fortschritt/Serien/Notizen", "Favoris/listes/historique/progression/séries/notes", "Favoriler/listeler/geçmiş/ilerleme/seriler/notlar"),
    "Sync favorites / lists / history / mastery / notes / chant & practice prefs": L("お気に入り/リスト/履歴/習熟/メモ/唱和・修行設定を同期", "즐겨찾기/목록/기록/숙달/메모/chant·수행 설정", "Избранное/списки/история/mastery/заметки/chant", "ซิงค์รายการโปรด/รายการ/ประวัติ/mastery/บันทึก/chant", "Favoriten/Listen/Verlauf/Mastery/Notizen/Chant", "Favoris/listes/historique/maîtrise/notes/chant", "Favoriler/listeler/geçmiş/ustalık/notlar/chant"),
    "Sync favorites / lists / history / progress / streaks / journal / habits": L("お気に入り/リスト/履歴/進捗/連続/ジャーナル/習慣を同期", "즐겨찾기/목록/기록/진행/연속/저널/습관", "Избранное/списки/история/прогресс/серии/журнал/привычки", "ซิงค์รายการโปรด/รายการ/ประวัติ/ความคืบหน้า/สตรีค/บันทึก/นิสัย", "Favoriten/Listen/Verlauf/Fortschritt/Serien/Journal/Gewohnheiten", "Favoris/listes/historique/progression/séries/journal/habitudes", "Favoriler/listeler/geçmiş/ilerleme/seriler/günlük/alışkanlıklar"),
    "Sync favorites / lists / history / progress / streaks / notes / journal": L("お気に入り/リスト/履歴/進捗/連続/メモ/ジャーナルを同期", "즐겨찾기/목록/기록/진행/연속/메모/저널", "Избранное/списки/история/прогресс/серии/заметки/журнал", "ซิงค์รายการโปรด/รายการ/ประวัติ/ความคืบหน้า/สตรีค/บันทึก/บันทึกย่อ", "Favoriten/Listen/Verlauf/Fortschritt/Serien/Notizen/Journal", "Favoris/listes/historique/progression/séries/notes/journal", "Favoriler/listeler/geçmiş/ilerleme/seriler/notlar/günlük"),
    "Sync favorites / lists / history / progress / streaks / notes / saved characters": L("お気に入り/リスト/履歴/進捗/連続/メモ/保存文字を同期", "즐겨찾기/목록/기록/진행/연속/메모/저장 글자", "Избранное/списки/история/прогресс/серии/заметки/сохранённые иероглифы", "ซิงค์รายการโปรด/รายการ/ประวัติ/ความคืบหน้า/สตรีค/บันทึก/ตัวอักษรที่บันทึก", "Favoriten/Listen/Verlauf/Fortschritt/Serien/Notizen/gespeicherte Zeichen", "Favoris/listes/historique/progression/séries/notes/caractères enregistrés", "Favoriler/listeler/geçmiş/ilerleme/seriler/notlar/kayıtlı karakterler"),
}


def tr_cell(en: str, table: dict[str, dict[str, str]]) -> dict[str, str]:
    if en in table:
        return table[en]
    return L(en, en, en, en, en, en, en)


def build_row(en_line: str) -> dict[str, str] | None:
    parts = [p.strip() for p in en_line.strip().split("|")[1:-1]]
    if len(parts) == 2:
        c1, c2 = parts
        t1 = tr_cell(c1, COL1)
        if c1.startswith("Daily ") and "cache" in c1:
            t1 = tr_cell(c1.replace(" cache & notification prefs", ""), COL1)
        if c1.startswith("Today’s ") and "cache" in c1:
            pass
        t2 = tr_cell(c2, COL2 if c2 in COL2 else COL3)
        if c2 in SYNC_SCOPES:
            t2 = SYNC_SCOPES[c2]
        elif c2.startswith("Sync "):
            t2 = SYNC_SCOPES.get(c2, tr_cell(c2, COL3))
        elif "**iCloud**" in c2:
            t2 = L(
                c2.replace("optional tipping", "任意チップ"),
                c2,
                c2,
                c2,
                c2.replace("optional tipping", "optionales Trinkgeld"),
                c2.replace("optional tipping", "pourboire facultatif"),
                c2,
            )
        out = {}
        for lang in r.LOCALES:
            out[lang] = f"| {t1[lang]} | {t2[lang]} |"
        return out
    if len(parts) == 3:
        c1, c2, c3 = parts
        t1, t2, t3 = tr_cell(c1, COL1), tr_cell(c2, COL2), tr_cell(c3, COL3)
        if c2 == "App Group UserDefaults":
            t2 = L("App Group UserDefaults", "App Group UserDefaults", "UserDefaults App Group", "UserDefaults ของ App Group", "UserDefaults der App Group", "UserDefaults de l’App Group", "App Group UserDefaults")
        if c2 == "Standard UserDefaults (device)":
            t2 = tr_cell(c2, COL2)
        if c2 == "App / Widget bundle":
            t2 = L("App / Widget バンドル", "App / Widget 번들", "Пакет App / Widget", "App / Widget bundle", "App-/Widget-Bundle", "Bundle App / Widget", "App / Widget paketi")
        if c2 == "App bundle":
            t2 = L("App バンドル", "App 번들", "Пакет приложения", "App bundle", "App-Bundle", "Bundle de l’app", "App paketi")
        if c2 == "Application Support (`CopySutra/`)":
            t2 = L("Application Support（`CopySutra/`）", "Application Support(`CopySutra/`)", "Application Support (`CopySutra/`)", "Application Support (`CopySutra/`)", "Application Support (`CopySutra/`)", "Application Support (`CopySutra/`)", "Application Support (`CopySutra/`)")
        if c2 == "App Group / ActivityKit":
            t2 = L("App Group / ActivityKit", "App Group / ActivityKit", "App Group / ActivityKit", "App Group / ActivityKit", "App Group / ActivityKit", "App Group / ActivityKit", "App Group / ActivityKit")
        if c3 in SYNC_SCOPES:
            t3 = SYNC_SCOPES[c3]
        out = {}
        for lang in r.LOCALES:
            out[lang] = f"| {t1[lang]} | {t2[lang]} | {t3[lang]} |"
        return out
    return None


def main() -> None:
    gaps = json.loads(GAPS_PATH.read_text(encoding="utf-8"))
    added = 0
    for line in STILL.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line.startswith("|") or line in gaps:
            continue
        row = build_row(line)
        if row:
            gaps[line] = row
            added += 1
    GAPS_PATH.write_text(json.dumps(gaps, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"build_all_table_gaps: added {added}, total gaps {len(gaps)}")


if __name__ == "__main__":
    main()
