#!/usr/bin/env python3
"""Add ja/ko/ru/th/de/fr/tr names and taglines to collections.yml (model-maintained strings)."""

from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "_data" / "collections.yml"

# names + taglines per collection id
LOCALE_STRINGS: dict[str, dict[str, dict[str, str]]] = {
    "english": {
        "names": {"ja": "英語", "ko": "영어", "ru": "Английский", "th": "ภาษาอังกฤษ", "de": "Englisch", "fr": "Anglais", "tr": "İngilizce"},
        "taglines": {
            "ja": "語彙・語根・バイリンガル読書——英語学習向け。",
            "ko": "어휘, 어근, 이중언어 읽기——영어 학습자용.",
            "ru": "Лексика, корни и bilingual-чтение для изучающих английский.",
            "th": "คำศัพท์ รากศัพท์ และการอ่านสองภาษา สำหรับผู้เรียนภาษาอังกฤษ",
            "de": "Wortschatz, Wurzeln und bilingual lesen — für Englischlernende.",
            "fr": "Vocabulaire, racines et lecture bilingue — pour apprendre l'anglais.",
            "tr": "Kelime, kök ve iki dilli okuma — İngilizce öğrenenler için.",
        },
    },
    "typing": {
        "names": {"ja": "中国語入力", "ko": "중국어 입력", "ru": "Китайский ввод", "th": "การป้อนภาษาจีน", "de": "Chinesische Eingabe", "fr": "Saisie chinoise", "tr": "Çince giriş"},
        "taglines": {
            "ja": "五筆・倉頡・漢字と語句——オフラインで調べて練習。",
            "ko": "五笔, 창jie, 한자와 어구——오프라인 조회·연습.",
            "ru": "Уби, Цанцзе, иероглифы и фразы — офлайн поиск и практика.",
            "th": "五笔 仓颉 ตัวอักษรและวลี — ค้นหาและฝึกแบบออฟไลน์",
            "de": "Wubi, Cangjie, Zeichen und Wörter — offline nachschlagen und üben.",
            "fr": "Wubi, Cangjie, caractères et mots — recherche et pratique hors ligne.",
            "tr": "Wubi, Cangjie, karakterler ve sözcükler — çevrimdışı arama ve pratik.",
        },
    },
    "tech": {
        "names": {"ja": "技術・開発", "ko": "기술·개발", "ru": "Разработка", "th": "เทคนิคและพัฒนา", "de": "Tech & Entwicklung", "fr": "Tech & dev", "tr": "Teknik ve geliştirme"},
        "taglines": {
            "ja": "コマンド、アルゴリズム、面接、ASC、開発者ツール。",
            "ko": "명령, 알고리즘, 면접, ASC, 개발자 도구.",
            "ru": "Команды, алгоритмы, собеседования, ASC и инструменты разработчика.",
            "th": "คำสั่ง อัลกอริทึม สัมภาษณ์ ASC และเครื่องมือนักพัฒนา",
            "de": "Befehle, Algorithmen, Interviews, ASC und Entwickler-Tools.",
            "fr": "Commandes, algorithmes, entretiens, ASC et outils développeur.",
            "tr": "Komutlar, algoritmalar, mülakat, ASC ve geliştirici araçları.",
        },
    },
    "productivity": {
        "names": {"ja": "効率ツール", "ko": "생산성", "ru": "Продуктивность", "th": "ประสิทธิภาพ", "de": "Produktivität", "fr": "Productivité", "tr": "Verimlilik"},
        "taglines": {
            "ja": "カレンダー、ウィジェット、集中、App Store ツール、Excel、お得情報、ブラウザ、Web ツール、換算、ローカル連携。",
            "ko": "캘린더, 위젯, 집중, App Store 도구, Excel, 할인, 브라우저, 웹 도구, 변환, 로컬 P2P.",
            "ru": "Календарь, виджеты, фокус, App Store, Excel, скидки, браузер, веб-инструменты, конвертеры, локальный P2P.",
            "th": "ปฏิทิน วิดเจ็ต โฟกัส เครื่องมือ App Store Excel ดีล เบราว์เซอร์ เว็บเครื่องมือ แปลงหน่วย และ P2P ในเครื่อง",
            "de": "Kalender, Widgets, Fokus, App-Store-Tools, Excel, Deals, Browser, Web-Tools, Umrechner und lokales P2P.",
            "fr": "Calendrier, widgets, focus, outils App Store, Excel, bons plans, navigateur, outils web, convertisseurs et P2P local.",
            "tr": "Takvim, widget, odak, App Store araçları, Excel, fırsatlar, tarayıcı, web araçları, dönüştürücüler ve yerel P2P.",
        },
    },
    "media": {
        "names": {"ja": "映像・創作", "ko": "미디어", "ru": "Медиа", "th": "สื่อ", "de": "Medien", "fr": "Médias", "tr": "Medya"},
        "taglines": {
            "ja": "写真編集、動画ツール、デュアルカメラ——すべて端末内。",
            "ko": "사진, 동영상 도구, 듀얼 카메라——기기에서만.",
            "ru": "Фото, видео и двойная камера — только на устройстве.",
            "th": "ตัดต่อภาพ วิดีโอ และกล้องคู่ — บนเครื่องเท่านั้น",
            "de": "Fotos, Video-Toolbox und Dual-Kamera — alles auf dem Gerät.",
            "fr": "Photo, vidéo et double caméra — entièrement sur l'appareil.",
            "tr": "Fotoğraf, video araçları ve çift kamera — yalnızca cihazda.",
        },
    },
    "music": {
        "names": {"ja": "音楽", "ko": "음악", "ru": "Музыка", "th": "ดนตรี", "de": "Musik", "fr": "Musique", "tr": "Müzik"},
        "taglines": {
            "ja": "キュレーション視聴——曲が記憶に残る理由を聴く。",
            "ko": "큐레이션 청취——노래가 기억에 남는 이유.",
            "ru": "Кураторское прослушивание — почему песня остаётся с вами.",
            "th": "ฟังแบบคัดสรร — ได้ยินว่าทำไมเพลงจึงอยู่ในใจ",
            "de": "Kuratiertes Hören — warum ein Song bleibt.",
            "fr": "Écoute guidée — entendre pourquoi une chanson reste.",
            "tr": "Seçilmiş dinleme — bir şarkının neden akılda kaldığını duyun.",
        },
    },
    "lifestyle": {
        "names": {"ja": "生活・健康", "ko": "라이프스타일", "ru": "Образ жизни", "th": "ไลฟ์สไตล์", "de": "Lifestyle", "fr": "Bien-être", "tr": "Yaşam"},
        "taglines": {
            "ja": "栄養とリラックス——プライバシー優先。",
            "ko": "영양과 회복——프라이버시 우선.",
            "ru": "Питание и спокойное восстановление — приватность важнее.",
            "th": "โภชนาการและการฟื้นตัว — ให้ความเป็นส่วนตัวเป็นอันดับแรก",
            "de": "Ernährung und ruhige Erholung — Datenschutz zuerst.",
            "fr": "Nutrition et détente — la confidentialité d'abord.",
            "tr": "Beslenme ve sakin toparlanma — gizlilik öncelikli.",
        },
    },
    "campus": {
        "names": {"ja": "キャンパス", "ko": "캠퍼스", "ru": "Кампус", "th": "มหาวิทยาลัย", "de": "Campus", "fr": "Campus", "tr": "Kampüs"},
        "taglines": {
            "ja": "桂林理工大学のキャンパス情報と資料。",
            "ko": "桂林理工大学 캠퍼스 소식과 자료.",
            "ru": "Новости и ресурсы кампуса Guilin University of Technology.",
            "th": "ข่าวและทรัพยากร Guilin University of Technology",
            "de": "Campus-News und Ressourcen der Guilin University of Technology.",
            "fr": "Actualités et ressources du campus Guilin University of Technology.",
            "tr": "Guilin University of Technology kampüs haberleri ve kaynakları.",
        },
    },
    "classics": {
        "names": {"ja": "国学", "ko": "국학", "ru": "Классика", "th": "คลาสสิกจีน", "de": "Klassik", "fr": "Classiques", "tr": "Klasikler"},
        "taglines": {
            "ja": "国学の全体像——字詞・詩詞・蒙學・四書五經・諸子にも分類。",
            "ko": "국학 전체——자词·시词·蒙学·四书五经·诸子로도 볼 수 있습니다.",
            "ru": "Полная полка классики — также по лексике, поэзии, primer, Четырём книгам и мастерам.",
            "th": "ชั้นคลาสสิกทั้งหมด — แยกตามคำศัพท์ บทกวี 蒙学 四书五经 และ诸子",
            "de": "Gesamtes Klassik-Regal — auch Lexikon, Poesie, Primers, Vier Bücher und Meister.",
            "fr": "Étagère classique complète — aussi lexique, poésie, primers, Quatre Livres et maîtres.",
            "tr": "Tam klasik raf — ayrıca sözlük, şiir, primer, Dört Kitap ve ustalar.",
        },
    },
    "poetry": {
        "names": {"ja": "詩詞曲連", "ko": "시词曲联", "ru": "Поэзия", "th": "บทกวี", "de": "Poesie", "fr": "Poésie", "tr": "Şiir"},
        "taglines": {
            "ja": "唐詩、宋詞、元曲、対聯、声律——オフラインで読む。",
            "ko": "唐詩·宋詞·元曲·对联·声律——오프라인 감상.",
            "ru": "Тан, Сун, Юань, couplets и рифмы — офлайн.",
            "th": "唐诗 宋词 元曲 对联 และส韵律 — อ่านออฟไลน์",
            "de": "Tang-Gedichte, Song-Lyrik, Yuan, Couplets und Reime — offline.",
            "fr": "Poèmes Tang, ci Song, qu Yuan, couplets et rimes — hors ligne.",
            "tr": "Tang şiirleri, Song ci, Yuan qu, couplet ve kafiyeler — çevrimdışı.",
        },
    },
    "four-classics": {
        "names": {"ja": "四書五経", "ko": "四书五经", "ru": "Четыре книги и Пять классиков", "th": "四书五经", "de": "Vier Bücher & Fünf Klassiker", "fr": "Quatre Livres et Cinq Classiques", "tr": "Dört Kitap ve Beş Klasik"},
        "taglines": {
            "ja": "論語、孟子、中庸、大学、周易と四書・五経全集。",
            "ko": "論語·孟子·中庸·大学·周易 및 四书·五经 전체.",
            "ru": "Аналекты, Мэн-цзы, Чжун Юн, Да Сюэ, И Цzin и полные полки.",
            "th": "論語 孟子 中庸 大学 周易 และชั้นหนังสือ四书五经",
            "de": "Analects, Mencius, Doctrine of the Mean, Great Learning, Yi Jing und vollständige Regale.",
            "fr": "Entretiens, Mencius, Juste milieu, Grande étude, Yi Jing et étagères complètes.",
            "tr": "Analects, Mencius, Orta Yol, Büyük Öğrenme, Yi Jing ve tam raflar.",
        },
    },
    "masters": {
        "names": {"ja": "諸子百家", "ko": "诸子百家", "ru": "Мастера", "th": "诸子等", "de": "Meister", "fr": "Maîtres", "tr": "Ustalar"},
        "taglines": {
            "ja": "道・法・墨・兵・医、戦国の諸子——一家一棚。",
            "ko": "道·法·墨·兵·医와 战国诸子——학파별 책상.",
            "ru": "Дaoists, legalists, mohists, военные, медики и мастера Сражающихся царств.",
            "th": "道 法 墨 兵 医 และ诸子战国 — สำนักละโต๊ะ",
            "de": "Daoisten, Legalisten, Mohisten, Militär, Medizin und Meister der Streitenden Reiche.",
            "fr": "Daoïstes, légistes, mohistes, militaires, médecine et maîtres des Royaumes combattants.",
            "tr": "Taoist, legalist, Mohist, askeri, tıp ve Savaşan Devletler ustaları.",
        },
    },
    "primers": {
        "names": {"ja": "蒙学", "ko": "蒙学", "ru": "Primers", "th": "蒙学", "de": "Primers", "fr": "Primers", "tr": "Başlangıç metinleri"},
        "taglines": {
            "ja": "三字経、弟子規、千字文、百家姓、家訓、声律。",
            "ko": "三字经·弟子规·千字文·百家姓·家训·声律.",
            "ru": "San Zi Jing, Di Zi Gui, тысяча иероглифов, фамилии, семейные наставления и рифмы.",
            "th": "三字经 弟子规 千字文 百家姓 家训 และ声律",
            "de": "San Zi Jing, Di Zi Gui, Tausend Zeichen, Nachnamen, Familienregeln und Reime.",
            "fr": "San Zi Jing, Di Zi Gui, mille caractères, noms, préceptes familiaux et rimes.",
            "tr": "San Zi Jing, Di Zi Gui, bin karakter, soyadları, aile öğütleri ve kafiyeler.",
        },
    },
    "characters": {
        "names": {"ja": "漢字・語彙", "ko": "한자·어휘", "ru": "Иероглифы и слова", "th": "ตัวอักษรและคำ", "de": "Zeichen & Wörter", "fr": "Caractères & mots", "tr": "Karakterler ve sözcükler"},
        "taglines": {
            "ja": "漢字辞典と成語——オフラインで調べる。",
            "ko": "한자 사전과 성어——오프라인 조회.",
            "ru": "Словарь иероглифов и идиом — офлайн.",
            "th": "พจนานุกรมตัวอักษรและสำนวน — ค้นแบบออฟไลน์",
            "de": "Zeichenwörterbuch und Idiome — offline.",
            "fr": "Dictionnaire de caractères et idiomes — hors ligne.",
            "tr": "Karakter sözlüğü ve deyimler — çevrimdışı.",
        },
    },
}


def main() -> None:
    cols = yaml.safe_load(PATH.read_text(encoding="utf-8"))
    for col in cols:
        cid = col["id"]
        loc = LOCALE_STRINGS.get(cid)
        if not loc:
            continue
        for field in ("names", "taglines"):
            col.setdefault(field, {})
            col[field].update(loc[field])
    PATH.write_text(yaml.dump(cols, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")
    print("patch_collections_locales: OK")


if __name__ == "__main__":
    main()
