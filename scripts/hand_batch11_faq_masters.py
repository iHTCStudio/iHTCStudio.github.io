# -*- coding: utf-8 -*-
"""Hand-maintained FAQ bodies for batch-11 classics (iMencius masters + per-lang clone rules)."""
from __future__ import annotations

LANGS = ("ja", "ko", "ru", "th", "de", "fr", "tr")

IMENCIUS: dict[str, str] = {
    "ja": """### 主要な機能はオフラインで使えますか？

はい、コア機能についてはオフラインで利用できます。ライブラリと学習補助は端末に同梱されています。インストール後、閲覧、精読、朗誦（システム TTS）、養気学堂、ウィジェット、ローカルの毎日の通知は**ネットワークなし**で動作します。例外は、**StoreKit による投げ銭**（Apple）、お客様が選んだ別アプリへの共有、任意の iCloud です。

### 単純な電子書籍とどう違いますか？

iMencius は**孟子スタジオ**です。**原文／口語／Legge 英訳**による精読、カラオケ風の**朗誦**、**養気学堂**、**易ハント**、**今日の一句**、孟カード、ウィジェット、任意のライブアクティビティ、Siri とショートカット — 静的なテキストのダンプではありません。**たとえギャラリー**と**対話マップ**、パブリックドメインの Legge 英訳、**4 種類**のウィジェット、**6 個**の代替アイコンも含みます。

### どのようなテキストが含まれますか？

*孟子*（Mencius）:

- 690 章 · 3549 節 · 100 名句 · 26 のたとえ · 7 つの対話ボイス
- レイヤー：原文／口語／Legge 英語

原文はパブリックドメインです。口語・英語・注釈は学習用に整えた補助資料であり、学術的な校訂版ではありません。

### どのような学習モードがありますか？

**フェード**、**穴埋め**、**自己チェック**、**クイズ**があり、習熟度を記録します。ホーム画面の **易ハント** は、別の「段落探し」ゲームです。

### 「今日の一句」とは？

ホーム画面で毎日の一節を表示します。**文脈に合わせた**表示と、任意の**ローカル**リマインダーに対応します。ウィジェットでホーム画面、ロック画面、StandBy にも表示できます。

### iCloud 同期の対象は？

**お気に入り**、**リスト（读孟单）**、**メモ**、**閲読履歴**、**学習の進捗**、**連続記録**を、プライベートな iCloud KVS 経由で任意同期できます。

### データを収集していますか？

**いいえ。** [プライバシーポリシー](../privacy)をご覧ください。iHTC Studio はデータを収集せず、広告・分析 SDK もなく、アカウントも不要です。

### App Store Connect 用のプライバシーポリシー URL はどこですか？

本サイトの[プライバシーポリシー](../privacy)ページを開き、ブラウザのアドレスバーから URL をコピーしてください。

### App Store に掲載されていますか？

はい — [App Store でダウンロード](https://apps.apple.com/app/id6808957787)。

### システム要件は？

iPhone / iPad **iOS 17.0+**、Mac **macOS 14.0+**。

### サポートへの連絡方法は？

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 通常 48 時間以内に返信します。""",
    "ko": """### 앱은 완전히 오프라인으로 사용할 수 있나요?

핵심 기능은 오프라인으로 사용할 수 있습니다. 라이브러리와 학습 보조 자료는 기기에 포함되어 있습니다. 설치 후에는 탐색, 정독, 낭송(시스템 TTS), 양기 학당, 위젯, 로컬 일일 알림을 **네트워크 없이** 이용할 수 있습니다. 예외는 **StoreKit 후원**(Apple), 사용자가 선택한 다른 앱으로의 공유, 선택적 iCloud입니다.

### 단순 전자책과 무엇이 다른가요?

iMencius는 **孟子 스튜디오**입니다. **원문 / 백화 / Legge 영어** 정독, 노래방 스타일 **낭송**, **양기 학당**, **역 헌트**, **오늘의 한 구**, 孟 카드, 위젯, 선택적 라이브 액티비티, Siri 및 단축어 — 정적인 텍스트 덤프가 아닙니다. **비유 갤러리**와 **대화 지도**, 공용 도메인 Legge 영어, 위젯 **4종**, 대체 아이콘 **6개**가 포함됩니다.

### 어떤 텍스트가 포함되어 있나요?

*孟子*(Mencius):

- 690장 · 3549절 · 100명구 · 26비유 · 7대화 목소리
- 레이어: 원문 / 백화 / Legge 영어

원문은 공용 도메인입니다. 백화, 영어, 주석은 학습용으로 정리한 보조 자료이며 학술 교정본이 아닙니다.

### 어떤 학습 모드가 있나요?

**페이드**, **빈칸 채우기**, **자가 확인**, **퀴즈**와 숙달도 추적이 있습니다. 홈의 **역 헌트**는 별도의 「구절 찾기」 게임입니다.

### 「오늘의 한 구」란?

홈에서 매일 한 절을 보여 줍니다. **맥락형** 표시와 선택적 **로컬** 알림을 지원합니다. 위젯으로 홈 화면, 잠금 화면, StandBy에 둘 수 있습니다.

### iCloud 동기화 범위는?

개인 iCloud KVS를 통해 **즐겨찾기**, **목록(读孟单)**, **메모**, **독서 기록**, **학습 진행**, **연속 기록**을 선택적으로 동기화할 수 있습니다.

### 제 데이터를 수집하나요?

**아니요.** [개인정보 처리방침](../privacy)을 참고하세요. iHTC Studio는 데이터를 수집하지 않으며 광고/분석 SDK도, 계정도 없습니다.

### App Store Connect용 개인정보 처리방침 URL은?

이 사이트의 [개인정보 처리방침](../privacy) 페이지를 열고 브라우저 주소 표시줄에서 URL을 복사하세요.

### App Store에 있나요?

예 — [App Store에서 다운로드](https://apps.apple.com/app/id6808957787).

### 시스템 요구 사항?

iPhone / iPad **iOS 17.0 이상**, Mac **macOS 14.0 이상**.

### 지원 문의?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 보통 48시간 이내에 답변합니다.""",
    "ru": """### Приложение полностью офлайн?

Для основных функций — да. Библиотека и учебные материалы встроены в устройство. После установки просмотр, внимательное чтение, декламация (системный TTS), «Школа питания ци», виджеты и локальные ежедневные уведомления работают **без сети**. Исключения: **чаевые через StoreKit** (Apple), отправка в выбранное вами приложение и необязательный iCloud.

### Чем это отличается от простой электронной книги?

iMencius — **студия «Мэн-цзы»**: чтение **оригинал / vernacular / Legge English**, **декламация** в стиле караоке, **«Школа питания ци»**, **«Охота за И»**, **«Строка дня»**, карточки 孟, виджеты, необязательная Live Activity, Siri и «Команды» — не статичный дамп текста. **Галерея аналогий** и **карта диалогов**, Legge на public domain, **4** вида виджетов, **6** альтернативных иконок.

### Какие тексты включены?

*Мэн-цзы* (Mencius):

- 690 глав · 3549 строф · 100 знаменитых строк · 26 аналогий · 7 голосов диалога
- Слои: оригинал / vernacular / Legge English

Оригиналы — public domain. Vernacular, английский и примечания — учебные материалы, не академические критические издания.

### Какие режимы обучения?

**Затухание**, **заполнение пропусков**, **самопроверка** и **викторина** с отслеживанием мастерства. **«Охота за И»** на главном экране — отдельная игра «найди отрывок».

### Что такое «Строка дня»?

Ежедневный отрывок на главном экране, необязательно **контекстный**, с необязательными **локальными** напоминаниями. Виджеты — на Home Screen, Lock Screen и StandBy.

### Что синхронизирует iCloud?

Необязательная синхронизация **избранного**, **списков (读孟单)**, **заметок**, **истории чтения**, **прогресса** и **серий** через ваш частный iCloud KVS.

### Вы собираете мои данные?

**Нет.** См. [Политику конфиденциальности](../privacy): Data Not Collected от iHTC Studio; без рекламных/анalytic SDK; без аккаунта.

### URL политики конфиденциальности для App Store Connect?

Откройте на этом сайте страницу [Политики конфиденциальности](../privacy) и скопируйте URL из адресной строки браузера.

### Уже в App Store?

Да — [Скачать в App Store](https://apps.apple.com/app/id6808957787).

### Системные требования?

iPhone / iPad — **iOS 17.0+**, Mac — **macOS 14.0+**.

### Как связаться с поддержкой?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — обычно в течение 48 часов.""",
    "th": """### แอปใช้งานออฟไลน์ได้เต็มที่หรือไม่?

ฟังก์ชันหลักใช้ได้ออฟไลน์ ห้องสมุดและเครื่องมือเรียนอยู่ในเครื่อง หลังติดตั้ง การเรียกดู อ่านละเอียด ท่อง (TTS ระบบ) โรงเรียนบ่มปลูกชี่ วิดเจ็ต และการแจ้งเตือนรายวันแบบ local ทำงาน **โดยไม่ต้องใช้เครือข่าย** ข้อยกเว้น: **ทิปผ่าน StoreKit** (Apple) การแชร์ไปแอปที่คุณเลือก และ iCloud แบบเลือกได้

### ต่างจาก ebook ธรรมดาอย่างไร?

iMencius คือ **สตูดิโอ孟子**: อ่าน **ต้นฉบับ / ภาษาพูด / Legge English** ท่องแบบคาราโอเกะ **โรงเรียนบ่มปลูกชี่** **Yi Hunt** **Daily Saying** การ์ด 孟 วิดเจ็ต Live Activity (เลือกได้) Siri และ Shortcuts — ไม่ใช่ข้อความนิ่ง **แกลเลอรีอุปมา** และ **แผนที่บทสนทนา** Legge สาธารณสมบัติ วิดเจ็ต **4** แบบ ไอคอนสำรอง **6** แบบ

### มีข้อความอะไรบ้าง?

*孟子* (Mencius):

- 690 บท · 3549 บทย่อย · 100 บรรทัดมีชื่อ · 26 อุปมา · 7 เสียงบทสนทนา
- ชั้น: ต้นฉบับ / ภาษาพูด / Legge English

ต้นฉบับเป็นสาธารณสมบัติ ภาษาพูด อังกฤษ และหมายเหตุเป็นสื่อเรียนที่คัดสรร ไม่ใช่ฉบับวิชาการ

### โหมดเรียนมีอะไรบ้าง?

**Fade** **เติมช่องว่าง** **ตรวจเอง** และ **แบบทดสอบ** พร้อมติดตามความชำนาญ **Yi Hunt** บนหน้าแรกเป็นเกมหาข้อความแยกต่างหาก

### Daily Saying คืออะไร?

ข้อความประจำวันบนหน้าแรก อาจ **ตามบริบท** พร้อมการเตือน **local** แบบเลือกได้ วิดเจ็ตวางบน Home Screen Lock Screen และ StandBy ได้

### iCloud Sync ครอบคลุมอะไร?

ซิงก์ **รายการโปรด** **รายการ (读孟单)** **บันทึก** **ประวัติการอ่าน** **ความคืบหน้า** และ **สตรีค** ผ่าน iCloud KVS ส่วนตัวของคุณ (เลือกได้)

### คุณเก็บข้อมูลของฉันหรือไม่?

**ไม่** ดู [นโยบายความเป็นส่วนตัว](../privacy): Data Not Collected โดย iHTC Studio ไม่มี SDK โฆษณา/วิเคราะห์ ไม่มีบัญชี

### URL นโยบายความเป็นส่วนตัวสำหรับ App Store Connect?

เปิดหน้า [นโยบายความเป็นส่วนตัว](../privacy) ของไซต์นี้ แล้วคัดลอก URL จากแถบที่อยู่เบราว์เซอร์

### มีใน App Store แล้วหรือยัง?

มี — [ดาวน์โหลดบน App Store](https://apps.apple.com/app/id6808957787)

### ความต้องการของระบบ?

iPhone / iPad **iOS 17.0+** Mac **macOS 14.0+**

### ติดต่อฝ่ายสนับสนุน?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — โดยทั่วไปภายใน 48 ชั่วโมง""",
    "de": """### Ist die App vollständig offline?

Für die Kernfunktionen ja. Bibliothek und Lernhilfen liegen auf dem Gerät. Nach der Installation funktionieren Durchsuchen, intensives Lesen, Rezitation (System-TTS), „Qi-Nährende Schule“, Widgets und lokale Tagesbenachrichtigungen **ohne Netzwerk**. Ausnahmen: **StoreKit-Trinkgeld** (Apple), Teilen in eine App Ihrer Wahl und optionales iCloud.

### Worin unterscheidet sich das von einem einfachen E-Book?

iMencius ist ein **Mencius-Studio**: intensives Lesen mit **Original / Umgangssprache / Legge English**, **Rezitation** im Karaoke-Stil, **„Qi-Nährende Schule“**, **„Yi-Jagd“**, **„Satz des Tages“**, 孟-Karten, Widgets, optionale Live Activity, Siri & Kurzbefehle — kein statischer Textdump. **Analogie-Galerie** und **Dialogkarte**, Legge public domain, **4** Widget-Arten, **6** alternative Icons.

### Welche Texte sind enthalten?

*孟子* (Mencius):

- 690 Kapitel · 3549 Abschnitte · 100 berühmte Zeilen · 26 Analogien · 7 Dialogstimmen
- Ebenen: Original / Umgangssprache / Legge English

Originale sind gemeinfrei. Umgangssprache, Englisch und Anmerkungen sind Lernhilfen, keine wissenschaftlichen kritischen Ausgaben.

### Welche Lernmodi gibt es?

**Ausblenden**, **Lückentext**, **Selbstkontrolle** und **Quiz** mit Fortschrittsverfolgung. **„Yi-Jagd“** auf dem Home-Bildschirm ist ein separates Passagen-Suchspiel.

### Was ist „Satz des Tages“?

Ein täglicher Abschnitt auf dem Home-Bildschirm, optional **kontextbezogen**, mit optionalen **lokalen** Erinnerungen. Widgets für Home Screen, Sperrbildschirm und StandBy.

### Was umfasst iCloud-Sync?

Optionaler Sync für **Favoriten**, **Listen (读孟单)**, **Notizen**, **Leseverlauf**, **Lernfortschritt** und **Serien** über Ihre private iCloud KVS.

### Sammeln Sie meine Daten?

**Nein.** Siehe [Datenschutzerklärung](../privacy): Data Not Collected by iHTC Studio; keine Werbe-/Analytics-SDKs; kein Konto.

### Datenschutz-URL für App Store Connect?

Öffnen Sie auf dieser Website die [Datenschutzerklärung](../privacy) und kopieren Sie die URL aus der Adressleiste.

### Schon im App Store?

Ja — [Im App Store laden](https://apps.apple.com/app/id6808957787).

### Systemanforderungen?

iPhone / iPad mit **iOS 17.0+**, Mac mit **macOS 14.0+**.

### Support kontaktieren?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — in der Regel innerhalb von 48 Stunden.""",
    "fr": """### L’app est-elle entièrement hors ligne ?

Pour l’essentiel, oui. La bibliothèque et les aides à l’étude sont embarquées. Après installation, navigation, lecture attentive, récitation (TTS système), « École du souffle nourricier », widgets et notifications locales quotidiennes fonctionnent **sans réseau**. Exceptions : **pourboire StoreKit** (Apple), partage vers une app de votre choix et iCloud optionnel.

### En quoi diffère-t-elle d’un simple livre numérique ?

iMencius est un **studio Mencius** : lecture **original / vernaculaire / Legge English**, **récitation** façon karaoké, **« École du souffle nourricier »**, **« Chasse au Yi »**, **« Vers du jour »**, cartes 孟, widgets, Live Activity optionnelle, Siri et Raccourcis — pas un texte statique. **Galerie d’analogies** et **carte des dialogues**, Legge domaine public, **4** types de widgets, **6** icônes alternatives.

### Quels textes sont inclus ?

*孟子* (Mencius) :

- 690 chapitres · 3549 versets · 100 vers célèbres · 26 analogies · 7 voix de dialogue
- Couches : original / vernaculaire / Legge English

Les originaux sont du domaine public. Vernaculaire, anglais et notes sont des aides d’étude, pas des éditions critiques académiques.

### Quels modes d’étude ?

**Fondu**, **texte à trous**, **auto-vérification** et **quiz**, avec suivi de maîtrise. **« Chasse au Yi »** sur l’accueil est un jeu séparé pour trouver un passage.

### Qu’est-ce que « Vers du jour » ?

Un passage quotidien sur l’accueil, optionnellement **contextuel**, avec rappels **locaux** optionnels. Widgets sur écran d’accueil, écran verrouillé et StandBy.

### Que couvre la synchronisation iCloud ?

Sync optionnelle des **favoris**, **listes (读孟单)**, **notes**, **historique de lecture**, **progrès** et **séries** via votre iCloud KVS privé.

### Collectez-vous mes données ?

**Non.** Voir la [Politique de confidentialité](../privacy) : Data Not Collected par iHTC Studio ; pas de SDK pub/analytics ; pas de compte.

### URL de politique de confidentialité pour App Store Connect ?

Ouvrez la page [Politique de confidentialité](../privacy) de ce site et copiez l’URL depuis la barre d’adresse.

### Déjà sur l’App Store ?

Oui — [Télécharger sur l’App Store](https://apps.apple.com/app/id6808957787).

### Configuration requise ?

iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+** requis.

### Contacter l’assistance ?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — en général sous 48 h.""",
    "tr": """### Uygulama tamamen çevrimdışı mı?

Temel kullanım için evet. Kütüphane ve çalışma yardımcıları cihazda gelir. Kurulumdan sonra gezinme, dikkatli okuma, okuma (sistem TTS), «Qi Besleyen Okul», widget’lar ve yerel günlük bildirimler **ağ olmadan** çalışır. İstisnalar: **StoreKit bahşişi** (Apple), seçtiğiniz başka bir uygulamaya paylaşım ve isteğe bağlı iCloud.

### Basit bir e-kitaptan farkı nedir?

iMencius bir **Mencius stüdyosu**: **özgün / sade / Legge English** dikkatli okuma, karaoke tarzı **okuma**, **«Qi Besleyen Okul»**, **«Yi Avı»**, **«Günün Dizesi»**, 孟 kartları, widget’lar, isteğe bağlı Live Activity, Siri ve Kısayollar — statik metin yığını değil. **Benzetme galerisi** ve **diyalog haritası**, Legge kamu malı, **4** widget türü, **6** alternatif simge.

### Hangi metinler var?

*孟子* (Mencius):

- 690 bölüm · 3549 ayet · 100 ünlü dize · 26 benzetme · 7 diyalog sesi
- Katmanlar: özgün / sade / Legge English

Özgün metinler kamu malıdır. Sade, İngilizce ve notlar çalışma yardımcısıdır; akademik eleştirel baskı değildir.

### Hangi çalışma modları?

**Solma**, **boşluk doldurma**, **öz denetim** ve **quiz**, ustalık takibiyle. Ana ekrandaki **«Yi Avı»** ayrı bir pasaj bulma oyunudur.

### «Günün Dizesi» nedir?

Ana ekranda günlük bir pasaj, isteğe bağlı **bağlamsal**, isteğe bağlı **yerel** hatırlatıcılarla. Widget’lar Ana Ekran, Kilit Ekranı ve StandBy’da.

### iCloud eşitlemesi neleri kapsar?

Özel iCloud KVS üzerinden **favoriler**, **listeler (读孟单)**, **notlar**, **okuma geçmişi**, **ilerleme** ve **seriler** için isteğe bağlı eşitleme.

### Verilerimi topluyor musunuz?

**Hayır.** [Gizlilik Politikası](../privacy): iHTC Studio tarafından Data Not Collected; reklam/analytics SDK yok; hesap yok.

### App Store Connect gizlilik politikası URL’si?

Bu sitenin [Gizlilik Politikası](../privacy) sayfasını açın ve tarayıcı adres çubuğundan URL’yi kopyalayın.

### App Store’da mı?

Evet — [App Store’da indir](https://apps.apple.com/app/id6808957787).

### Sistem gereksinimleri?

iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+** gerekir.

### Destek?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — genelde 48 saat içinde.""",
}

# Per-language clone rules: (from, to) applied to iMencius master text.
CLASSIC_RULES: dict[str, dict[str, list[tuple[str, str]]]] = {
    "ja": {
        "iHanFei": [
            ("iMencius", "iHanFei"),
            ("孟子", "韩非子"),
            ("Mencius", "Han Feizi"),
            ("*孟子*", "*韩非子*"),
            ("養気学堂", "法家学堂"),
            ("易ハント", "法ハント"),
            ("今日の一句", "今日の計略"),
            ("690 章 · 3549 節", "55 章 · 5376 句"),
            ("100 名句 · 26 のたとえ", "225 名句 · 85 寓言"),
            ("7 つの対話ボイス", "47 概念"),
            ("Legge 英語", "英語"),
            ("たとえギャラリー", "寓言ギャラリー"),
            ("対話マップ", "法・术・势 概念マップ"),
            ("读孟单", "简册"),
            ("孟カード", "韓カード"),
            ("6808957787", "6808957997"),
        ],
        "iLvShi": [
            ("iMencius", "iLvShi"),
            ("孟子", "吕氏春秋"),
            ("Mencius", "Lüshi Chunqiu"),
            ("*孟子*", "*吕氏春秋*"),
            ("養気学堂", "春秋学堂"),
            ("易ハント", "秋ハント"),
            ("今日の一句", "今日の一篇"),
            ("690 章 · 3549 節", "160 篇 · 約1061 節"),
            ("100 名句 · 26 のたとえ", "100 名句 · 月令"),
            ("7 つの対話ボイス", "四層読書"),
            ("Legge 英語", "英語（四層）"),
            ("たとえギャラリー", "月令"),
            ("対話マップ", "四層読書"),
            ("读孟单", "秋单"),
            ("孟カード", "秋カード"),
            ("6808957787", "6808957717"),
        ],
        "iGuanZhi": [
            ("iMencius", "iGuanZhi"),
            ("孟子", "古文观止"),
            ("Mencius", "Guwen Guanzhi"),
            ("*孟子*", "*古文观止*"),
            ("養気学堂", "古文观止学堂"),
            ("易ハント", "文章ハント"),
            ("今日の一句", "今日の一文"),
            ("690 章 · 3549 節", "222 篇 · 6495 句"),
            ("100 名句 · 26 のたとえ", "221 名句 · 18 逸話"),
            ("7 つの対話ボイス", "12 文体コンセプト"),
            ("Legge 英語", "英語"),
            ("たとえギャラリー", "逸話ギャラリー"),
            ("対話マップ", "文体コンセプト"),
            ("读孟单", "文単"),
            ("孟カード", "古カード"),
            ("6808957787", "6808958120"),
        ],
        "iMoZi": [
            ("iMencius", "iMoZi"),
            ("孟子", "墨子"),
            ("Mencius", "Mozi"),
            ("*孟子*", "*墨子*"),
            ("養気学堂", "墨家学堂"),
            ("易ハント", "句ハント"),
            ("今日の一句", "今日の墨"),
            ("690 章 · 3549 節", "53 章 · 634 句"),
            ("100 名句 · 26 のたとえ", "108 名句 · 十論・三表"),
            ("7 つの対話ボイス", "三表法"),
            ("Legge 英語", "英語（Mei 1929 など）"),
            ("たとえギャラリー", "十論マップ"),
            ("対話マップ", "公輸盤 叙事"),
            ("读孟单", "墨单"),
            ("孟カード", "墨カード"),
            ("6808957787", "1240858394"),
        ],
    },
    "ko": {
        "iHanFei": [
            ("iMencius", "iHanFei"),
            ("孟子", "韩非子"),
            ("Mencius", "Han Feizi"),
            ("*孟子*", "*韩非子*"),
            ("孟子 스튜디오", "韩非子 스튜디오"),
            ("양기 학당", "법가 학당"),
            ("역 헌트", "법 헌트"),
            ("오늘의 한 구", "오늘의 계략"),
            ("690장 · 3549절", "55장 · 5376구"),
            ("100명구 · 26비유", "225명구 · 85우화"),
            ("7대화 목소리", "47개념"),
            ("Legge 영어", "영어"),
            ("비유 갤러리", "우화 갤러리"),
            ("대화 지도", "법·术·势 개념 지도"),
            ("读孟单", "简册"),
            ("孟 카드", "韓 카드"),
            ("6808957787", "6808957997"),
        ],
        "iLvShi": [
            ("iMencius", "iLvShi"),
            ("孟子", "吕氏春秋"),
            ("Mencius", "Lüshi Chunqiu"),
            ("*孟子*", "*吕氏春秋*"),
            ("孟子 스튜디오", "吕氏春秋 스튜디오"),
            ("양기 학당", "春秋 학당"),
            ("역 헌트", "秋 헌트"),
            ("오늘의 한 구", "오늘의 한 편"),
            ("690장 · 3549절", "160편 · 약1061절"),
            ("100명구 · 26비유", "100명구 · 月令"),
            ("7대화 목소리", "4층 독서"),
            ("Legge 영어", "영어(4층)"),
            ("비유 갤러리", "月令"),
            ("대화 지도", "4층 독서"),
            ("读孟单", "秋单"),
            ("孟 카드", "秋 카드"),
            ("6808957787", "6808957717"),
        ],
        "iGuanZhi": [
            ("iMencius", "iGuanZhi"),
            ("孟子", "古文观止"),
            ("Mencius", "Guwen Guanzhi"),
            ("*孟子*", "*古文观止*"),
            ("孟子 스튜디오", "古文观止 스튜디오"),
            ("양기 학당", "古文观止 학당"),
            ("역 헌트", "文章 헌트"),
            ("오늘의 한 구", "오늘의 한 문장"),
            ("690장 · 3549절", "222편 · 6495구"),
            ("100명구 · 26비유", "221명구 · 18일화"),
            ("7대화 목소리", "12문체 개념"),
            ("Legge 영어", "영어"),
            ("비유 갤러리", "일화 갤러리"),
            ("대화 지도", "문체 개념"),
            ("读孟单", "文单"),
            ("孟 카드", "古 카드"),
            ("6808957787", "6808958120"),
        ],
        "iMoZi": [
            ("iMencius", "iMoZi"),
            ("孟子", "墨子"),
            ("Mencius", "Mozi"),
            ("*孟子*", "*墨子*"),
            ("孟子 스튜디오", "墨子 스튜디오"),
            ("양기 학당", "墨家 학당"),
            ("역 헌트", "구 헌트"),
            ("오늘의 한 구", "오늘의 墨"),
            ("690장 · 3549절", "53장 · 634구"),
            ("100명구 · 26비유", "108명구 · 十論·三表"),
            ("7대화 목소리", "三表法"),
            ("Legge 영어", "영어(Mei 1929 등)"),
            ("비유 갤러리", "十論 지도"),
            ("대화 지도", "公輸盤 서사"),
            ("读孟单", "墨单"),
            ("孟 카드", "墨 카드"),
            ("6808957787", "1240858394"),
        ],
    },
    "ru": {
        "iHanFei": [
            ("iMencius", "iHanFei"),
            ("«Мэн-цзы»", "«Хань Фэй-цзы»"),
            ("Mencius", "Han Feizi"),
            ("*Мэн-цзы*", "*Хань Фэй-цзы*"),
            ("студия «Мэн-цзы»", "студия «Хань Фэй-цзы»"),
            ("«Школа питания ци»", "«Школа Legalism»"),
            ("«Охота за И»", "«Охота за стратегией»"),
            ("«Строка дня»", "«Стратегема дня»"),
            ("690 глав · 3549 строф", "55 глав · 5376 предложений"),
            ("100 знаменитых строк · 26 аналогий", "225 знаменитых строк · 85 притч"),
            ("7 голосов диалога", "47 понятий"),
            ("Legge English", "английский"),
            ("Галерея аналогий", "Галерея притч"),
            ("карта диалогов", "карта понятий 法·术·势"),
            ("读孟单", "简册"),
            ("карточки 孟", "карточки 韓"),
            ("6808957787", "6808957997"),
        ],
        "iLvShi": [
            ("iMencius", "iLvShi"),
            ("«Мэн-цзы»", "«Лüshi chunqiu»"),
            ("Mencius", "Lüshi Chunqiu"),
            ("*Мэн-цзы*", "*吕氏春秋*"),
            ("студия «Мэн-цзы»", "студия «Лüshi chunqiu»"),
            ("«Школа питания ци»", "«Школа «Весны и осени»»"),
            ("«Охота за И»", "«Охота «Осень»»"),
            ("«Строка дня»", "«Отрывок дня»"),
            ("690 глав · 3549 строф", "160 статей · ~1061 сегментов"),
            ("100 знаменитых строк · 26 аналогий", "100 знаменитых строк · 月令"),
            ("7 голосов диалога", "чтение в 4 слоя"),
            ("Legge English", "английский (4 слоя)"),
            ("Галерея аналогий", "月令"),
            ("карта диалогов", "чтение в 4 слоя"),
            ("读孟单", "秋单"),
            ("карточки 孟", "карточки 秋"),
            ("6808957787", "6808957717"),
        ],
        "iGuanZhi": [
            ("iMencius", "iGuanZhi"),
            ("«Мэн-цзы»", "«Guwen Guanzhi»"),
            ("Mencius", "Guwen Guanzhi"),
            ("*Мэн-цзы*", "*古文观止*"),
            ("студия «Мэн-цзы»", "студия «Guwen Guanzhi»"),
            ("«Школа питания ци»", "«Школа «Guwen Guanzhi»»"),
            ("«Охота за И»", "«Охота за эссе»"),
            ("«Строка дня»", "«Эссе дня»"),
            ("690 глав · 3549 строф", "222 эссе · 6495 предложений"),
            ("100 знаменитых строк · 26 аналогий", "221 знаменитая строка · 18 анекдотов"),
            ("7 голосов диалога", "12 жанровых понятий"),
            ("Legge English", "английский"),
            ("Галерея аналогий", "Галерея анекдотов"),
            ("карта диалогов", "жанровые понятия"),
            ("读孟单", "文单"),
            ("карточки 孟", "карточки 古"),
            ("6808957787", "6808958120"),
        ],
        "iMoZi": [
            ("iMencius", "iMoZi"),
            ("«Мэн-цзы»", "«Мо-цзы»"),
            ("Mencius", "Mozi"),
            ("*Мэн-цзы*", "*墨子*"),
            ("студия «Мэн-цзы»", "студия «Мо-цзы»"),
            ("«Школа питания ци»", "«Школа Mohism»"),
            ("«Охота за И»", "«Охота за предложением»"),
            ("«Строка дня»", "«Мо дня»"),
            ("690 глав · 3549 строф", "53 главы · 634 предложения"),
            ("100 знаменитых строк · 26 аналогий", "108 знаменитых строк · Ten Theses · Three Tests"),
            ("7 голосов диалога", "«Три критерия»"),
            ("Legge English", "английский (Mei 1929 и др.)"),
            ("Галерея аналогий", "карта «Ten Theses»"),
            ("карта диалогов", "повествование «Gongshu Pan»"),
            ("读孟单", "墨单"),
            ("карточки 孟", "карточки 墨"),
            ("6808957787", "1240858394"),
        ],
    },
    "th": {
        "iHanFei": [
            ("iMencius", "iHanFei"),
            ("孟子", "韩非子"),
            ("Mencius", "Han Feizi"),
            ("*孟子*", "*韩非子*"),
            ("สตูดิโอ孟子", "สตูดิโอ韩非子"),
            ("โรงเรียนบ่มปลูกชี่", "โรงเรียน Legalism"),
            ("Yi Hunt", "Law Hunt"),
            ("Daily Saying", "Daily Stratagem"),
            ("690 บท · 3549 บทย่อย", "55 บท · 5376 ประโยค"),
            ("100 บรรทัดมีชื่อ · 26 อุปมา", "225 บรรทัดมีชื่อ · 85 นิทาน"),
            ("7 เสียงบทสนทนา", "47 แนวคิด"),
            ("Legge English", "อังกฤษ"),
            ("แกลเลอรีอุปมา", "แกลเลอรีนิทาน"),
            ("แผนที่บทสนทนา", "แผนที่แนวคิด 法·术·势"),
            ("读孟单", "简册"),
            ("การ์ด 孟", "การ์ด 韓"),
            ("6808957787", "6808957997"),
        ],
        "iLvShi": [
            ("iMencius", "iLvShi"),
            ("孟子", "吕氏春秋"),
            ("Mencius", "Lüshi Chunqiu"),
            ("*孟子*", "*吕氏春秋*"),
            ("สตูดิโอ孟子", "สตูดิโอ吕氏春秋"),
            ("โรงเรียนบ่มปลูกชี่", "โรงเรียนฤดูใบไม้"),
            ("Yi Hunt", "Autumn Hunt"),
            ("Daily Saying", "Daily Passage"),
            ("690 บท · 3549 บทย่อย", "160 บทความ · ~1061 ท่อน"),
            ("100 บรรทัดมีชื่อ · 26 อุปมา", "100 บรรทัดมีชื่อ · 月令"),
            ("7 เสียงบทสนทนา", "อ่าน 4 ชั้น"),
            ("Legge English", "อังกฤษ (4 ชั้น)"),
            ("แกลเลอรีอุปมา", "月令"),
            ("แผนที่บทสนทนา", "อ่าน 4 ชั้น"),
            ("读孟单", "秋单"),
            ("การ์ด 孟", "การ์ด 秋"),
            ("6808957787", "6808957717"),
        ],
        "iGuanZhi": [
            ("iMencius", "iGuanZhi"),
            ("孟子", "古文观止"),
            ("Mencius", "Guwen Guanzhi"),
            ("*孟子*", "*古文观止*"),
            ("สตูดิโอ孟子", "สตูดิโอ古文观止"),
            ("โรงเรียนบ่มปลูกชี่", "โรงเรียน古文观止"),
            ("Yi Hunt", "Essay Hunt"),
            ("Daily Saying", "Today’s Essay"),
            ("690 บท · 3549 บทย่อย", "222 บทความ · 6495 ประโยค"),
            ("100 บรรทัดมีชื่อ · 26 อุปมา", "221 บรรทัดมีชื่อ · 18 เกร็ด"),
            ("7 เสียงบทสนทนา", "12 แนวคิดแนวเขียน"),
            ("Legge English", "อังกฤษ"),
            ("แกลเลอรีอุปมา", "แกลเลอรีเกร็ด"),
            ("แผนที่บทสนทนา", "แนวคิดแนวเขียน"),
            ("读孟单", "文单"),
            ("การ์ด 孟", "การ์ด 古"),
            ("6808957787", "6808958120"),
        ],
        "iMoZi": [
            ("iMencius", "iMoZi"),
            ("孟子", "墨子"),
            ("Mencius", "Mozi"),
            ("*孟子*", "*墨子*"),
            ("สตูดิโอ孟子", "สตูดิโอ墨子"),
            ("โรงเรียนบ่มปลูกชี่", "โรงเรียน Mohism"),
            ("Yi Hunt", "Sentence Hunt"),
            ("Daily Saying", "Today’s Mo"),
            ("690 บท · 3549 บทย่อย", "53 บท · 634 ประโยค"),
            ("100 บรรทัดมีชื่อ · 26 อุปมา", "108 บรรทัดมีชื่อ · Ten Theses · Three Tests"),
            ("7 เสียงบทสนทนา", "Three Tests"),
            ("Legge English", "อังกฤษ (Mei 1929 ฯลฯ)"),
            ("แกลเลอรีอุปมา", "แผนที่ Ten Theses"),
            ("แผนที่บทสนทนา", "เรื่องเล่า Gongshu Pan"),
            ("读孟单", "墨单"),
            ("การ์ด 孟", "การ์ด 墨"),
            ("6808957787", "1240858394"),
        ],
    },
    "de": {
        "iHanFei": [
            ("iMencius", "iHanFei"),
            ("Mencius", "Han Feizi"),
            ("*Mencius*", "*Han Feizi*"),
            ("Mencius-Studio", "Han-Feizi-Studio"),
            ("„Qi-Nährende Schule“", "„Legalismus-Schule“"),
            ("„Yi-Jagd“", "„Strategie-Jagd“"),
            ("„Satz des Tages“", "„Stratagem des Tages“"),
            ("690 Kapitel · 3549 Abschnitte", "55 Kapitel · 5376 Sätze"),
            ("100 berühmte Zeilen · 26 Analogien", "225 berühmte Zeilen · 85 Fabeln"),
            ("7 Dialogstimmen", "47 Konzepte"),
            ("Legge English", "Englisch"),
            ("Analogie-Galerie", "Fabel-Galerie"),
            ("Dialogkarte", "Konzeptkarte 法·术·势"),
            ("读孟单", "简册"),
            ("孟-Karten", "韓-Karten"),
            ("6808957787", "6808957997"),
        ],
        "iLvShi": [
            ("iMencius", "iLvShi"),
            ("Mencius", "Lüshi Chunqiu"),
            ("*Mencius*", "*Lüshi Chunqiu*"),
            ("Mencius-Studio", "Lüshi-Chunqiu-Studio"),
            ("„Qi-Nährende Schule“", "„Frühlings-und-Herbst-Schule“"),
            ("„Yi-Jagd“", "„Herbst-Jagd“"),
            ("„Satz des Tages“", "„Passage des Tages“"),
            ("690 Kapitel · 3549 Abschnitte", "160 Abhandlungen · ~1061 Segmente"),
            ("100 berühmte Zeilen · 26 Analogien", "100 berühmte Zeilen · 月令"),
            ("7 Dialogstimmen", "Vier-Schicht-Lesen"),
            ("Legge English", "Englisch (vier Schichten)"),
            ("Analogie-Galerie", "月令"),
            ("Dialogkarte", "Vier-Schicht-Lesen"),
            ("读孟单", "秋单"),
            ("孟-Karten", "秋-Karten"),
            ("6808957787", "6808957717"),
        ],
        "iGuanZhi": [
            ("iMencius", "iGuanZhi"),
            ("Mencius", "Guwen Guanzhi"),
            ("*Mencius*", "*Guwen Guanzhi*"),
            ("Mencius-Studio", "Guwen-Guanzhi-Studio"),
            ("„Qi-Nährende Schule“", "„Guwen-Guanzhi-Schule“"),
            ("„Yi-Jagd“", "„Essay-Jagd“"),
            ("„Satz des Tages“", "„Essay des Tages“"),
            ("690 Kapitel · 3549 Abschnitte", "222 Essays · 6495 Sätze"),
            ("100 berühmte Zeilen · 26 Analogien", "221 berühmte Zeilen · 18 Anekdoten"),
            ("7 Dialogstimmen", "12 Genre-Konzepte"),
            ("Legge English", "Englisch"),
            ("Analogie-Galerie", "Anekdoten-Galerie"),
            ("Dialogkarte", "Genre-Konzepte"),
            ("读孟单", "文单"),
            ("孟-Karten", "古-Karten"),
            ("6808957787", "6808958120"),
        ],
        "iMoZi": [
            ("iMencius", "iMoZi"),
            ("Mencius", "Mozi"),
            ("*Mencius*", "*Mozi*"),
            ("Mencius-Studio", "Mozi-Studio"),
            ("„Qi-Nährende Schule“", "„Mohismus-Schule“"),
            ("„Yi-Jagd“", "„Satz-Jagd“"),
            ("„Satz des Tages“", "„Mo des Tages“"),
            ("690 Kapitel · 3549 Abschnitte", "53 Kapitel · 634 Sätze"),
            ("100 berühmte Zeilen · 26 Analogien", "108 berühmte Zeilen · Ten Theses · Three Tests"),
            ("7 Dialogstimmen", "Three Tests"),
            ("Legge English", "Englisch (Mei 1929 u. a.)"),
            ("Analogie-Galerie", "Ten-Theses-Karte"),
            ("Dialogkarte", "Gongshu-Pan-Erzählung"),
            ("读孟单", "墨单"),
            ("孟-Karten", "墨-Karten"),
            ("6808957787", "1240858394"),
        ],
    },
    "fr": {
        "iHanFei": [
            ("iMencius", "iHanFei"),
            ("Mencius", "Han Feizi"),
            ("*Mencius*", "*Han Feizi*"),
            ("studio Mencius", "studio Han Feizi"),
            ("« École du souffle nourricier »", "« École legalist »"),
            ("« Chasse au Yi »", "« Chasse à la stratégie »"),
            ("« Vers du jour »", "« Stratagème du jour »"),
            ("690 chapitres · 3549 versets", "55 chapitres · 5376 phrases"),
            ("100 vers célèbres · 26 analogies", "225 vers célèbres · 85 fables"),
            ("7 voix de dialogue", "47 concepts"),
            ("Legge English", "anglais"),
            ("Galerie d’analogies", "Galerie de fables"),
            ("carte des dialogues", "carte des concepts 法·术·势"),
            ("读孟单", "简册"),
            ("cartes 孟", "cartes 韓"),
            ("6808957787", "6808957997"),
        ],
        "iLvShi": [
            ("iMencius", "iLvShi"),
            ("Mencius", "Lüshi Chunqiu"),
            ("*Mencius*", "*Lüshi Chunqiu*"),
            ("studio Mencius", "studio Lüshi Chunqiu"),
            ("« École du souffle nourricier »", "« École Printemps et Automne »"),
            ("« Chasse au Yi »", "« Chasse automne »"),
            ("« Vers du jour »", "« Passage du jour »"),
            ("690 chapitres · 3549 versets", "160 pièces · ~1061 segments"),
            ("100 vers célèbres · 26 analogies", "100 vers célèbres · 月令"),
            ("7 voix de dialogue", "lecture en 4 couches"),
            ("Legge English", "anglais (4 couches)"),
            ("Galerie d’analogies", "月令"),
            ("carte des dialogues", "lecture en 4 couches"),
            ("读孟单", "秋单"),
            ("cartes 孟", "cartes 秋"),
            ("6808957787", "6808957717"),
        ],
        "iGuanZhi": [
            ("iMencius", "iGuanZhi"),
            ("Mencius", "Guwen Guanzhi"),
            ("*Mencius*", "*Guwen Guanzhi*"),
            ("studio Mencius", "studio Guwen Guanzhi"),
            ("« École du souffle nourricier »", "« École Guwen Guanzhi »"),
            ("« Chasse au Yi »", "« Chasse à l’essai »"),
            ("« Vers du jour »", "« Essai du jour »"),
            ("690 chapitres · 3549 versets", "222 essais · 6495 phrases"),
            ("100 vers célèbres · 26 analogies", "221 vers célèbres · 18 anecdotes"),
            ("7 voix de dialogue", "12 concepts de genre"),
            ("Legge English", "anglais"),
            ("Galerie d’analogies", "Galerie d’anecdotes"),
            ("carte des dialogues", "concepts de genre"),
            ("读孟单", "文单"),
            ("cartes 孟", "cartes 古"),
            ("6808957787", "6808958120"),
        ],
        "iMoZi": [
            ("iMencius", "iMoZi"),
            ("Mencius", "Mozi"),
            ("*Mencius*", "*Mozi*"),
            ("studio Mencius", "studio Mozi"),
            ("« École du souffle nourricier »", "« École mohiste »"),
            ("« Chasse au Yi »", "« Chasse à la phrase »"),
            ("« Vers du jour »", "« Mo du jour »"),
            ("690 chapitres · 3549 versets", "53 chapitres · 634 phrases"),
            ("100 vers célèbres · 26 analogies", "108 vers célèbres · Ten Theses · Three Tests"),
            ("7 voix de dialogue", "Three Tests"),
            ("Legge English", "anglais (Mei 1929, etc.)"),
            ("Galerie d’analogies", "carte Ten Theses"),
            ("carte des dialogues", "récit Gongshu Pan"),
            ("读孟单", "墨单"),
            ("cartes 孟", "cartes 墨"),
            ("6808957787", "1240858394"),
        ],
    },
    "tr": {
        "iHanFei": [
            ("iMencius", "iHanFei"),
            ("Mencius", "Han Feizi"),
            ("*Mencius*", "*Han Feizi*"),
            ("Mencius stüdyosu", "Han Feizi stüdyosu"),
            ("«Qi Besleyen Okul»", "«Legalist Okul»"),
            ("«Yi Avı»", "«Strateji Avı»"),
            ("«Günün Dizesi»", "«Günün Stratejisi»"),
            ("690 bölüm · 3549 ayet", "55 bölüm · 5376 cümle"),
            ("100 ünlü dize · 26 benzetme", "225 ünlü dize · 85 fabl"),
            ("7 diyalog sesi", "47 kavram"),
            ("Legge English", "İngilizce"),
            ("Benzetme galerisi", "Fabl galerisi"),
            ("diyalog haritası", "法·术·势 kavram haritası"),
            ("读孟单", "简册"),
            ("孟 kartları", "韓 kartları"),
            ("6808957787", "6808957997"),
        ],
        "iLvShi": [
            ("iMencius", "iLvShi"),
            ("Mencius", "Lüshi Chunqiu"),
            ("*Mencius*", "*Lüshi Chunqiu*"),
            ("Mencius stüdyosu", "Lüshi Chunqiu stüdyosu"),
            ("«Qi Besleyen Okul»", "«Bahar Sonbahar Okulu»"),
            ("«Yi Avı»", "«Sonbahar Avı»"),
            ("«Günün Dizesi»", "«Günün Pasajı»"),
            ("690 bölüm · 3549 ayet", "160 parça · ~1061 segment"),
            ("100 ünlü dize · 26 benzetme", "100 ünlü dize · 月令"),
            ("7 diyalog sesi", "4 katmanlı okuma"),
            ("Legge English", "İngilizce (4 katman)"),
            ("Benzetme galerisi", "月令"),
            ("diyalog haritası", "4 katmanlı okuma"),
            ("读孟单", "秋单"),
            ("孟 kartları", "秋 kartları"),
            ("6808957787", "6808957717"),
        ],
        "iGuanZhi": [
            ("iMencius", "iGuanZhi"),
            ("Mencius", "Guwen Guanzhi"),
            ("*Mencius*", "*Guwen Guanzhi*"),
            ("Mencius stüdyosu", "Guwen Guanzhi stüdyosu"),
            ("«Qi Besleyen Okul»", "«Guwen Guanzhi Okulu»"),
            ("«Yi Avı»", "«Deneme Avı»"),
            ("«Günün Dizesi»", "«Günün Denemesi»"),
            ("690 bölüm · 3549 ayet", "222 deneme · 6495 cümle"),
            ("100 ünlü dize · 26 benzetme", "221 ünlü dize · 18 anekdot"),
            ("7 diyalog sesi", "12 tür kavramı"),
            ("Legge English", "İngilizce"),
            ("Benzetme galerisi", "Anekdot galerisi"),
            ("diyalog haritası", "tür kavramları"),
            ("读孟单", "文单"),
            ("孟 kartları", "古 kartları"),
            ("6808957787", "6808958120"),
        ],
        "iMoZi": [
            ("iMencius", "iMoZi"),
            ("Mencius", "Mozi"),
            ("*Mencius*", "*Mozi*"),
            ("Mencius stüdyosu", "Mozi stüdyosu"),
            ("«Qi Besleyen Okul»", "«Mohist Okul»"),
            ("«Yi Avı»", "«Cümle Avı»"),
            ("«Günün Dizesi»", "«Günün Mo’su»"),
            ("690 bölüm · 3549 ayet", "53 bölüm · 634 cümle"),
            ("100 ünlü dize · 26 benzetme", "108 ünlü dize · Ten Theses · Three Tests"),
            ("7 diyalog sesi", "Three Tests"),
            ("Legge English", "İngilizce (Mei 1929 vb.)"),
            ("Benzetme galerisi", "Ten Theses haritası"),
            ("diyalog haritası", "Gongshu Pan anlatısı"),
            ("读孟单", "墨单"),
            ("孟 kartları", "墨 kartları"),
            ("6808957787", "1240858394"),
        ],
    },
}


def clone(text: str, rules: list[tuple[str, str]]) -> str:
    for a, b in rules:
        text = text.replace(a, b)
    return text


def classic_faq(lang: str, app: str) -> str:
    master = IMENCIUS[lang]
    rules = CLASSIC_RULES.get(lang, {}).get(app)
    if not rules:
        raise KeyError(f"no rules {lang} {app}")
    return clone(master, rules)
