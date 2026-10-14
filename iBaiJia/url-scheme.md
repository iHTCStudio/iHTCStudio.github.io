---
layout: doc
title: iBaiJia — Shortcut Links
app_id: iBaiJia
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: ibaijia:// deep links for iBaiJia — surname, daily, recite, study, search, naming, categories, settings guides, and more.
---

<section lang="en" markdown="1">

iBaiJia supports **`ibaijia://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
ibaijia://{host}?{params}
```

## Core navigation

| URL | Opens |
|-----|-------|
| `ibaijia://home` | Home tab |
| `ibaijia://categories` | Browse / categories |
| `ibaijia://surname?id={id}` | Surname detail |
| `ibaijia://daily` | Today's Daily Surname |
| `ibaijia://random` | Random surname |
| `ibaijia://mySurname` | My Surname |
| `ibaijia://recite` | Recitation studio |
| `ibaijia://favorites` | Favorites |
| `ibaijia://search` / `ibaijia://search?q={query}` | Search |
| `ibaijia://study` | Study Hall |
| `ibaijia://stats` | Statistics |
| `ibaijia://naming` | Naming inspiration |
| `ibaijia://settings` | Settings |

## History & notes

| URL | Opens |
|-----|-------|
| `ibaijia://last-read` | Last read surname |
| `ibaijia://reading-history` | Reading history |
| `ibaijia://notes` | Notes list |
| `ibaijia://mastered` | Mastered / study progress |

## Help & feedback

| URL | Opens |
|-----|-------|
| `ibaijia://feature-guide` | Feature guide (onboarding replay) |
| `ibaijia://usage-guide` | Usage guide |
| `ibaijia://widget-guide` | Widget guide |
| `ibaijia://shortcuts-guide` | Shortcuts guide |
| `ibaijia://feedback` | Feedback mail compose |
| `ibaijia://in-app-review` | In-app review prompt |

## Notes

- Parameters are case-sensitive where IDs are numeric.
- Siri, Shortcuts, widgets, and Control Center controls use the same deep-link routes.
- See the in-app **Settings → Help** guides for the latest list.

</section>
<section lang="zh-CN" markdown="1">

爱百家姓支持 **`ibaijia://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导页结束后重复打开。

## 链接格式

```
ibaijia://{host}?{params}
```

## 核心导航

| URL | 打开 |
|-----|------|
| `ibaijia://home` | 首页 |
| `ibaijia://categories` | 分类浏览 |
| `ibaijia://surname?id={id}` | 姓氏详情 |
| `ibaijia://daily` | 今日一姓 |
| `ibaijia://random` | 随机姓氏 |
| `ibaijia://mySurname` | 我的姓氏 |
| `ibaijia://recite` | 四言诵读 |
| `ibaijia://favorites` | 收藏 |
| `ibaijia://search` / `ibaijia://search?q={query}` | 搜索 |
| `ibaijia://study` | 姓氏学堂 |
| `ibaijia://stats` | 统计 |
| `ibaijia://naming` | 取名灵感 |
| `ibaijia://settings` | 设置 |

## 历史与笔记

| URL | 打开 |
|-----|------|
| `ibaijia://last-read` | 上次阅读 |
| `ibaijia://reading-history` | 阅读历史 |
| `ibaijia://notes` | 笔记列表 |
| `ibaijia://mastered` | 已掌握 / 学堂进度 |

## 帮助与反馈

| URL | 打开 |
|-----|------|
| `ibaijia://feature-guide` | 功能引导（重播引导） |
| `ibaijia://usage-guide` | 使用说明 |
| `ibaijia://widget-guide` | 小组件指南 |
| `ibaijia://shortcuts-guide` | 快捷指令指南 |
| `ibaijia://feedback` | 反馈邮件 |
| `ibaijia://in-app-review` | 应用内好评 |

## 说明

- ID 类参数为数字时请保持正确格式。
- Siri、快捷指令、小组件与控制中心控件使用相同深链路由。
- 最新列表见应用内 **设置 → 帮助**。

</section>
<section lang="zh-TW" markdown="1">

愛百家姓支援 **`ibaijia://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導頁結束後重複開啟。

## 連結格式

```
ibaijia://{host}?{params}
```

## 核心導覽

| URL | 開啟 |
|-----|------|
| `ibaijia://home` | 首頁 |
| `ibaijia://categories` | 分類瀏覽 |
| `ibaijia://surname?id={id}` | 姓氏詳情 |
| `ibaijia://daily` | 今日一姓 |
| `ibaijia://random` | 隨機姓氏 |
| `ibaijia://mySurname` | 我的姓氏 |
| `ibaijia://recite` | 四言誦讀 |
| `ibaijia://favorites` | 收藏 |
| `ibaijia://search` / `ibaijia://search?q={query}` | 搜尋 |
| `ibaijia://study` | 姓氏學堂 |
| `ibaijia://stats` | 統計 |
| `ibaijia://naming` | 取名靈感 |
| `ibaijia://settings` | 設定 |

## 歷史與筆記

| URL | 開啟 |
|-----|------|
| `ibaijia://last-read` | 上次閱讀 |
| `ibaijia://reading-history` | 閱讀歷史 |
| `ibaijia://notes` | 筆記列表 |
| `ibaijia://mastered` | 已掌握 / 學堂進度 |

## 說明

- Siri、捷徑、小工具與控制中心控件使用相同深鏈路由。
- 最新列表見應用內 **設定 → 幫助**。

</section>
<section lang="ja" markdown="1">

iBaiJiaは** `ibaijia://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
ibaijia://{host}?{params}
```


## コアナビゲーション

| URL | 開く画面 |
|-----|-------|
| `ibaijia://home` | ホームタブ |
| `ibaijia://categories` | 閲覧/カテゴリ |
| `ibaijia://surname?id={id}` | 姓の詳細 |
| `ibaijia://daily` | 今日の毎日の姓 |
| `ibaijia://random` | ランダム名 |
| `ibaijia://mySurname` | 私の姓名 |
| `ibaijia://recite` | リサイティングスタジオ |
| `ibaijia://favorites` | お気に入り |
| `ibaijia://search` / `ibaijia://search?q={query}` | 検索 |
| `ibaijia://study` | スタディホール |
| `ibaijia://stats` | 統計データ |
| `ibaijia://naming` | ネーミングインスピレーション |
| `ibaijia://settings` | 設定 |

## 歴史とノート

| URL | 開く画面 |
|-----|-------|
| `ibaijia://last-read` | 姓 名 名 |
| `ibaijia://reading-history` | 閲覧履歴 |
| `ibaijia://notes` | ノートリスト |
| `ibaijia://mastered` | マスタード/学習進捗 |

## ヘルプ&フィードバック

| URL | 開く画面 |
|-----|-------|
| `ibaijia://feature-guide` | 特徴ガイド(オンボーディング再生) |
| `ibaijia://usage-guide` | 使い方ガイド |
| `ibaijia://widget-guide` | ウィジェットガイド |
| `ibaijia://shortcuts-guide` | ショートカットガイド |
| `ibaijia://feedback` | フィードバックメールコンポーズ |
| `ibaijia://in-app-review` | アプリ内レビュー プロンプト |

## ノート

- パラメータはIDが数値である場合感度です。
- シリ、ショートカット、ウィジェット、およびコントロールセンターコントロールは、同じディープリンクルートを使用します。
- 最新リストのアプリ内設定 → Help** ガイドを参照してください。

</section>
<section lang="ko" markdown="1">

iBaiJia 지원 ** `ibaijia://` ** 단축키 링크 (URL 계획). 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
ibaijia://{host}?{params}
```


## 핵심 항법

| URL | 열리는 화면 |
|-----|-------|
| `ibaijia://home` | 홈 탭 |
| `ibaijia://categories` | 카테고리 |
| `ibaijia://surname?id={id}` | Surname 상세 정보 |
| `ibaijia://daily` | 오늘의 일상 생활 |
| `ibaijia://random` | 무작위 성 |
| `ibaijia://mySurname` | 내 이름 |
| `ibaijia://recite` | Recitation 스튜디오 |
| `ibaijia://favorites` | 즐겨찾기 |
| `ibaijia://search` / `ibaijia://search?q={query}` | 검색 |
| `ibaijia://study` | 연구 홀 |
| `ibaijia://stats` | 관련 기사 |
| `ibaijia://naming` | 남림 영감 |
| `ibaijia://settings` | 설정 |

## 역사 & 노트

| URL | 열리는 화면 |
|-----|-------|
| `ibaijia://last-read` | 마지막 읽기 성 |
| `ibaijia://reading-history` | 읽기 기록 |
| `ibaijia://notes` | 공지사항 |
| `ibaijia://mastered` | 석사 / 연구 진행 |

## 도움 & 의견

| URL | 열리는 화면 |
|-----|-------|
| `ibaijia://feature-guide` | 기능 가이드 (Replay에) |
| `ibaijia://usage-guide` | 사용 가이드 |
| `ibaijia://widget-guide` | 위젯 가이드 |
| `ibaijia://shortcuts-guide` | 단축어 가이드 |
| `ibaijia://feedback` | 피드백 메일 compose |
| `ibaijia://in-app-review` | In-app 검토 신속한 |

## 메모

- 매개 변수는 ID가 숫자인지 여부를 감지합니다.
- Siri, Shortcuts, 위젯 및 제어 센터 제어는 동일한 딥 링크 루트를 사용합니다.
- in-app**Settings → 도움말** 최신 목록 안내

</section>
<section lang="ru" markdown="1">

iBaiJia поддерживает ярлыки ** `ibaijia://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
ibaijia://{host}?{params}
```


## Основная навигация

| URL | Открывает |
|-----|-------|
| `ibaijia://home` | Вкладка «Главная» |
| `ibaijia://categories` | Просмотр / Категории |
| `ibaijia://surname?id={id}` | Подробная фамилия |
| `ibaijia://daily` | Ежедневная фамилия сегодня |
| `ibaijia://random` | Случайная фамилия |
| `ibaijia://mySurname` | Моя фамилия |
| `ibaijia://recite` | Студия цитирования |
| `ibaijia://favorites` | Избранное |
| `ibaijia://search` / `ibaijia://search?q={query}` | Поиск |
| `ibaijia://study` | Учебный зал |
| `ibaijia://stats` | Статистика |
| `ibaijia://naming` | Наименование вдохновения |
| `ibaijia://settings` | Настройки |

## История и заметки

| URL | Открывает |
|-----|-------|
| `ibaijia://last-read` | Последнее прочитанное имя |
| `ibaijia://reading-history` | История чтения |
| `ibaijia://notes` | Список примечаний |
| `ibaijia://mastered` | Мастеринг / Study Progress |

## Помощь и обратная связь

| URL | Открывает |
|-----|-------|
| `ibaijia://feature-guide` | Функциональное руководство (onboarding replay) |
| `ibaijia://usage-guide` | Руководство по использованию |
| `ibaijia://widget-guide` | Руководство по виджетам |
| `ibaijia://shortcuts-guide` | Руководство по «Командам» |
| `ibaijia://feedback` | Обратная связь Mail Compose |
| `ibaijia://in-app-review` | Быстрый обзор в приложении |

## Заметки

- Параметры чувствительны к регистру, где идентификаторы являются числовыми.
- Siri, ярлыки, виджеты и элементы управления Центра управления используют одни и те же маршруты глубокой связи.
- Смотрите в приложении ** Настройки → Справочные руководства ** для последнего списка.

</section>
<section lang="th" markdown="1">

iBaijia รองรับ~ `ibaijia://` BAR * ลิงก์ลัด (URL scheme). การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
ibaijia://{host}?{params}
```


## การนําทางแกนหลัก

| URL | เปิด |
|-----|-------|
| `ibaijia://home` | แท็บหน้าแรก |
| `ibaijia://categories` | เลือก / ประเภท |
| `ibaijia://surname?id={id}` | รายละเอียดของชื่อแฟ้ม |
| `ibaijia://daily` | วันนี้ชื่อเดลิเซอร์ |
| `ibaijia://random` | สุ่มขนาด |
| `ibaijia://mySurname` | ชื่อ ของ ผม |
| `ibaijia://recite` | สตูดิโอของโครงการ |
| `ibaijia://favorites` | รายการโปรด |
| `ibaijia://search` / `ibaijia://search?q={query}` | ค้นหา |
| `ibaijia://study` | หอ ประชุม ศึกษา |
| `ibaijia://stats` | สถิติ |
| `ibaijia://naming` | แรงบันดาลใจในการตั้งชื่อ |
| `ibaijia://settings` | การตั้งค่า |

## ประวัติและบันทึก

| URL | เปิด |
|-----|-------|
| `ibaijia://last-read` | นามสกุลที่อ่านล่าสุด |
| `ibaijia://reading-history` | ประวัติการอ่าน |
| `ibaijia://notes` | รายการบันทึกย่อ |
| `ibaijia://mastered` | ความ ก้าว หน้า ใน การ ศึกษา |

## การตอบกลับช่วยเหลือ

| URL | เปิด |
|-----|-------|
| `ibaijia://feature-guide` | มัคคุเทศก์ อาวุโส (เริ่มเล่นอีกครั้ง) |
| `ibaijia://usage-guide` | คู่มือการใช้งาน |
| `ibaijia://widget-guide` | คู่มือวิดเจ็ต |
| `ibaijia://shortcuts-guide` | คู่มือทางลัด |
| `ibaijia://feedback` | เขียนจดหมายที่ส่งแล้ว |
| `ibaijia://in-app-review` | แจ้งเตือนการทบทวนข้อมูลภายใน |

## บันทึก

- พารามิเตอร์คือความไวของตัวเลข
- ไซรี, ทางลัด, วิดเจ็ต, และศูนย์ควบคุม ใช้เส้นทางลับเดียวกัน
- ดู In-appings-Cettings softs for the list ล่าสุด

</section>
<section lang="de" markdown="1">

iBaiJia unterstützt ** `ibaijia://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
ibaijia://{host}?{params}
```


## Kernnavigation

| URL | Öffnet |
|-----|-------|
| `ibaijia://home` | Register „Start“ |
| `ibaijia://categories` | Browsen / Kategorien |
| `ibaijia://surname?id={id}` | Angaben zum Namen |
| `ibaijia://daily` | Der heutige tägliche Nachname |
| `ibaijia://random` | Zufallsname |
| `ibaijia://mySurname` | Mein Nachname |
| `ibaijia://recite` | Rezitationsstudio |
| `ibaijia://favorites` | Favoriten |
| `ibaijia://search` / `ibaijia://search?q={query}` | Suche |
| `ibaijia://study` | Studienhalle |
| `ibaijia://stats` | Statistik |
| `ibaijia://naming` | Namensgebung Inspiration |
| `ibaijia://settings` | Einstellungen |

## Geschichte und Notizen

| URL | Öffnet |
|-----|-------|
| `ibaijia://last-read` | Zuletzt gelesener Nachname |
| `ibaijia://reading-history` | Leseverlauf |
| `ibaijia://notes` | Erläuterungen |
| `ibaijia://mastered` | Mastering / Studienfortschritt |

## Hilfe & Feedback

| URL | Öffnet |
|-----|-------|
| `ibaijia://feature-guide` | Feature Guide (Onboarding-Wiedergabe) |
| `ibaijia://usage-guide` | Nutzungsanleitung |
| `ibaijia://widget-guide` | Widget-Anleitung |
| `ibaijia://shortcuts-guide` | Kurzbefehle-Anleitung |
| `ibaijia://feedback` | Feedback Mail Compost |
| `ibaijia://in-app-review` | In-App Review prompt |

## Notizen

- Parameter sind fallsensibel, wo IDs numerisch sind.
- Siri, Shortcuts, Widgets und Control Center-Steuerelemente verwenden die gleichen Deep-Link-Routen.
- Sehen Sie sich die In-App **Einstellungen → Hilfe ** Anleitungen für die neueste Liste an.

</section>
<section lang="fr" markdown="1">

iBaiJia prend en charge les liens de raccourci ** `ibaijia://` ** (système URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
ibaijia://{host}?{params}
```


## Navigation de base

| URL | Ouvre |
|-----|-------|
| `ibaijia://home` | Onglet Accueil |
| `ibaijia://categories` | Parcourir / catégories |
| `ibaijia://surname?id={id}` | Détail du nom de famille |
| `ibaijia://daily` | Le nom quotidien d'aujourd'hui |
| `ibaijia://random` | Nom de famille aléatoire |
| `ibaijia://mySurname` | Mon nom |
| `ibaijia://recite` | Atelier de récitation |
| `ibaijia://favorites` | Favoris |
| `ibaijia://search` / `ibaijia://search?q={query}` | Recherche |
| `ibaijia://study` | Salle d'étude |
| `ibaijia://stats` | Statistiques |
| `ibaijia://naming` | Inspiration |
| `ibaijia://settings` | Réglages |

## Historique et notes

| URL | Ouvre |
|-----|-------|
| `ibaijia://last-read` | Nom de famille de la dernière lecture |
| `ibaijia://reading-history` | Historique de lecture |
| `ibaijia://notes` | Liste des notes |
| `ibaijia://mastered` | Maîtrise / progrès de l'étude |

## Aide & feedback

| URL | Ouvre |
|-----|-------|
| `ibaijia://feature-guide` | Guide des caractéristiques (reprise à bord) |
| `ibaijia://usage-guide` | Guide d'utilisation |
| `ibaijia://widget-guide` | Guide des widgets |
| `ibaijia://shortcuts-guide` | Guide Raccourcis |
| `ibaijia://feedback` | Messages de rétroaction |
| `ibaijia://in-app-review` | Révision rapide de l'application |

## Notes

- Les paramètres sont sensibles aux cas où les ID sont numériques.
- Les commandes Siri, Shortcuts, Widgets et Control Center utilisent les mêmes itinéraires de liaison profonde.
- Voir la page d'application **Paramètres → Aide** pour la dernière liste.

</section>
<section lang="tr" markdown="1">

iBaiJia ** `ibaijia://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
ibaijia://{host}?{params}
```


## Core navigasyon

| URL | Açar |
|-----|-------|
| `ibaijia://home` | Ana sayfa sekmesi |
| `ibaijia://categories` | Göz / kategoriler |
| `ibaijia://surname?id={id}` | Soyad detayı |
| `ibaijia://daily` | Bugünün Günlük Soyadı |
| `ibaijia://random` | Rastgele soyadı |
| `ibaijia://mySurname` | Benim Soyadım |
| `ibaijia://recite` | Recitation studio studio |
| `ibaijia://favorites` | Favoriler |
| `ibaijia://search` / `ibaijia://search?q={query}` | Ara |
| `ibaijia://study` | Çalışma Salonu |
| `ibaijia://stats` | İstatistikler İstatistik |
| `ibaijia://naming` | Naming ilham kaynağı |
| `ibaijia://settings` | Ayarlar |

## Tarih ve notlar

| URL | Açar |
|-----|-------|
| `ibaijia://last-read` | Son okuma soyadı |
| `ibaijia://reading-history` | Okuma geçmişi |
| `ibaijia://notes` | Notlar listesi |
| `ibaijia://mastered` | Mastered / çalışma ilerleme |

## Yardım ve geri bildirimler

| URL | Açar |
|-----|-------|
| `ibaijia://feature-guide` | Özel kılavuz (oylama replay) |
| `ibaijia://usage-guide` | Kullanım kılavuzu |
| `ibaijia://widget-guide` | Widget kılavuzu |
| `ibaijia://shortcuts-guide` | Kısayol kılavuzu |
| `ibaijia://feedback` | Geri bildirim posta formu |
| `ibaijia://in-app-review` | In-app review Hızlı |

## Notlar

- Parametreler, kimliklerin sayısal olduğu durumlarda hassastır.
- Siri, Shortcuts, widgets ve Control Center kontrolleri aynı derin bağlantı yollarını kullanır.
- In-app **Settings → Yardım** en son liste için kılavuzlar.

</section>
