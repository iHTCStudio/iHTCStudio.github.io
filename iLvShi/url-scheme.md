---
layout: doc
title: iLvShi — Shortcut Links
app_id: iLvShi
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: ilvshi:// deep links for iLvShi — passage, daily, recite, study, hunt, settings guides, and more.
---

<section lang="en" markdown="1">

iLvShi supports **`ilvshi://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
ilvshi://{host}?{params}
```

## Passages & authors

| URL | Opens |
|-----|-------|
| `ilvshi://passage?id={id}` | Passage detail |
| `ilvshi://saying?id={id}` / `ilvshi://couplet?id={id}` / `ilvshi://poem?id={id}` | Same as passage (compatibility) |
| `ilvshi://passage?id={id}&card=1` | Passage detail and card sheet |
| `ilvshi://card?id={id}` / `ilvshi://share-card?id={id}` | 秋 cards |
| `ilvshi://author?id={id}` | Author detail |
| `ilvshi://recite` / `ilvshi://recite?id={id}` | Recite flow |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `ilvshi://home` | Home |
| `ilvshi://daily` | Daily Passage |
| `ilvshi://random` | Random passage |
| `ilvshi://favorites` | Favorites |
| `ilvshi://famous` | Famous lines |
| `ilvshi://search` / `ilvshi://search?q={query}` | Search |
| `ilvshi://study` / `ilvshi://study?id={id}` | Spring–Autumn Study |
| `ilvshi://hunt` | Autumn Hunt (`keyword-hunt` / `flyflower`) |
| `ilvshi://handwriting` | Handwriting search (`handwrite`; iOS) |
| `ilvshi://mastered` | Mastered (`progress`) |
| `ilvshi://categories` / `ilvshi://categories?section=` | Browse |
| `ilvshi://collection?id=` | Collection / book |
| `ilvshi://corpus` | All passages (`all`) |
| `ilvshi://last-read` | Last read |
| `ilvshi://reading-history` | Reading history |
| `ilvshi://notes` | Notes |
| `ilvshi://fables` / `ilvshi://allegories` / `ilvshi://concepts` | Specialty shelves when available |

## Settings & guides

| URL | Opens |
|-----|-------|
| `ilvshi://settings` | Settings |
| `ilvshi://usage-guide` | Usage guide |
| `ilvshi://widget-guide` | Widget guide |
| `ilvshi://shortcuts-guide` | Shortcuts guide |
| `ilvshi://feature-guide` | Replay onboarding |
| `ilvshi://feedback` | Feedback email |
| `ilvshi://in-app-review` | In-app / Store review entry |

## Examples

```
ilvshi://daily
ilvshi://passage?id=1
ilvshi://study
ilvshi://hunt
```

</section>
<section lang="zh-CN" markdown="1">

爱吕氏春秋 支持 **`ilvshi://`** 快捷链接（URL Scheme）。冷启动与主屏幕快捷方式经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
ilvshi://{host}?{params}
```

## 篇目与作者

| URL | 打开 |
|-----|------|
| `ilvshi://passage?id={id}` | 篇目详情 |
| `ilvshi://saying?id={id}` / `ilvshi://couplet?id={id}` / `ilvshi://poem?id={id}` | 同 passage（兼容） |
| `ilvshi://passage?id={id}&card=1` | 篇目详情并打开分享卡 |
| `ilvshi://card?id={id}` / `ilvshi://share-card?id={id}` | 秋卡 |
| `ilvshi://author?id={id}` | 作者详情 |
| `ilvshi://recite` / `ilvshi://recite?id={id}` | 诵读 |

## 发现与练习

| URL | 打开 |
|-----|------|
| `ilvshi://home` | 首页 |
| `ilvshi://daily` | 每日一文 |
| `ilvshi://random` | 随机一篇 |
| `ilvshi://favorites` | 收藏 |
| `ilvshi://famous` | 名句 |
| `ilvshi://search` / `ilvshi://search?q={query}` | 搜索 |
| `ilvshi://study` / `ilvshi://study?id={id}` | 春秋学堂 |
| `ilvshi://hunt` | 寻秋（`keyword-hunt` / `flyflower`） |
| `ilvshi://handwriting` | 手写寻句（`handwrite`；iOS） |
| `ilvshi://mastered` | 已掌握（`progress`） |
| `ilvshi://categories` / `ilvshi://categories?section=` | 浏览 |
| `ilvshi://collection?id=` | 合集／分册 |
| `ilvshi://corpus` | 全部篇目（`all`） |
| `ilvshi://last-read` | 上次阅读 |
| `ilvshi://reading-history` | 阅读历史 |
| `ilvshi://notes` | 笔记 |
| `ilvshi://fables` / `ilvshi://allegories` / `ilvshi://concepts` | 专属书架（如有） |

## 设置与指南

| URL | 打开 |
|-----|------|
| `ilvshi://settings` | 设置 |
| `ilvshi://usage-guide` | 使用说明 |
| `ilvshi://widget-guide` | 小组件说明 |
| `ilvshi://shortcuts-guide` | 快捷指令说明 |
| `ilvshi://feature-guide` | 重看功能导览 |
| `ilvshi://feedback` | 反馈邮件 |
| `ilvshi://in-app-review` | 应用内／商店评价入口 |

## 示例

```
ilvshi://daily
ilvshi://passage?id=1
ilvshi://study
ilvshi://hunt
```

</section>
<section lang="zh-TW" markdown="1">

愛呂氏春秋 支援 **`ilvshi://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複打開。

## 連結格式

```
ilvshi://{host}?{params}
```

## 篇目與作者

| URL | 打開 |
|-----|------|
| `ilvshi://passage?id={id}` | 篇目詳情 |
| `ilvshi://saying?id={id}` / `ilvshi://couplet?id={id}` / `ilvshi://poem?id={id}` | 同 passage（相容） |
| `ilvshi://passage?id={id}&card=1` | 篇目詳情並打開分享卡 |
| `ilvshi://card?id={id}` / `ilvshi://share-card?id={id}` | 秋卡 |
| `ilvshi://author?id={id}` | 作者詳情 |
| `ilvshi://recite` / `ilvshi://recite?id={id}` | 誦讀 |

## 探索與練習

| URL | 打開 |
|-----|------|
| `ilvshi://home` | 首頁 |
| `ilvshi://daily` | 每日一文 |
| `ilvshi://random` | 隨機一篇 |
| `ilvshi://favorites` | 收藏 |
| `ilvshi://famous` | 名句 |
| `ilvshi://search` / `ilvshi://search?q={query}` | 搜尋 |
| `ilvshi://study` / `ilvshi://study?id={id}` | 春秋學堂 |
| `ilvshi://hunt` | 尋秋（`keyword-hunt` / `flyflower`） |
| `ilvshi://handwriting` | 手寫尋句（`handwrite`；iOS） |
| `ilvshi://mastered` | 已掌握（`progress`） |
| `ilvshi://categories` / `ilvshi://categories?section=` | 瀏覽 |
| `ilvshi://collection?id=` | 合集／分冊 |
| `ilvshi://corpus` | 全部篇目（`all`） |
| `ilvshi://last-read` | 上次閱讀 |
| `ilvshi://reading-history` | 閱讀歷史 |
| `ilvshi://notes` | 筆記 |
| `ilvshi://fables` / `ilvshi://allegories` / `ilvshi://concepts` | 專屬書架（如有） |

## 設定與指南

| URL | 打開 |
|-----|------|
| `ilvshi://settings` | 設定 |
| `ilvshi://usage-guide` | 使用說明 |
| `ilvshi://widget-guide` | 小工具說明 |
| `ilvshi://shortcuts-guide` | 捷徑說明 |
| `ilvshi://feature-guide` | 重看功能導覽 |
| `ilvshi://feedback` | 回饋郵件 |
| `ilvshi://in-app-review` | 應用內／商店評價入口 |

## 範例

```
ilvshi://daily
ilvshi://passage?id=1
ilvshi://study
ilvshi://hunt
```

</section>
<section lang="ja" markdown="1">

iLvShiは、** `ilvshi://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
ilvshi://{host}?{params}
```


## パスポートと著者

| URL | 開く画面 |
|-----|-------|
| `ilvshi://passage?id={id}` | 章句の詳細 |
| `ilvshi://saying?id={id}` / `ilvshi://couplet?id={id}` / `ilvshi://poem?id={id}` | 通路と同じ(互換性) |
| `ilvshi://passage?id={id}&card=1` | 通路の細部およびカード シート |
| `ilvshi://card?id={id}` / `ilvshi://share-card?id={id}` | 秋のカード |
| `ilvshi://author?id={id}` | 作者の詳細 |
| `ilvshi://recite` / `ilvshi://recite?id={id}` | 誦読フロー |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `ilvshi://home` | ホーム |
| `ilvshi://daily` | 毎日のパッセージ |
| `ilvshi://random` | ランダムな章句 |
| `ilvshi://favorites` | お気に入り |
| `ilvshi://famous` | 名句一覧 |
| `ilvshi://search` / `ilvshi://search?q={query}` | 検索 |
| `ilvshi://study` / `ilvshi://study?id={id}` | 春-秋学研究 |
| `ilvshi://hunt` | 秋のハント (`keyword-hunt`/`flyflower`) |
| `ilvshi://handwriting` | 手書き検索 (`handwrite`; iOS) |
| `ilvshi://mastered` | マスタード (`progress`) |
| `ilvshi://categories` / `ilvshi://categories?section=` | ブラウズ |
| `ilvshi://collection?id=` | コレクション/書籍 |
| `ilvshi://corpus` | すべての通路 (`all`) |
| `ilvshi://last-read` | 最後に読んだ項目 |
| `ilvshi://reading-history` | 閲覧履歴 |
| `ilvshi://notes` | ノート |
| `ilvshi://fables` / `ilvshi://allegories` / `ilvshi://concepts` | 利用できる場合の特別な棚 |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `ilvshi://settings` | 設定 |
| `ilvshi://usage-guide` | 使い方ガイド |
| `ilvshi://widget-guide` | ウィジェットガイド |
| `ilvshi://shortcuts-guide` | ショートカットガイド |
| `ilvshi://feature-guide` | オンボーディングの再生 |
| `ilvshi://feedback` | フィードバックメール |
| `ilvshi://in-app-review` | アプリ内／App Store レビュー |

## 例


```
ilvshi://daily
ilvshi://passage?id=1
ilvshi://study
ilvshi://hunt
```

</section>
<section lang="ko" markdown="1">

iLvShi는 ** `ilvshi://` ** 단축키 링크 (URL 계획)를 지원합니다. 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
ilvshi://{host}?{params}
```


## 책임 & 저자

| URL | 열리는 화면 |
|-----|-------|
| `ilvshi://passage?id={id}` | 구절 상세 |
| `ilvshi://saying?id={id}` / `ilvshi://couplet?id={id}` / `ilvshi://poem?id={id}` | 통행과 같 ( 겸용성) |
| `ilvshi://passage?id={id}&card=1` | 통행 세부사항과 카드 장 |
| `ilvshi://card?id={id}` / `ilvshi://share-card?id={id}` | 秋 카드 |
| `ilvshi://author?id={id}` | 작가 상세 |
| `ilvshi://recite` / `ilvshi://recite?id={id}` | 낭독 흐름 |

## 디스커버리 & 연습

| URL | 열리는 화면 |
|-----|-------|
| `ilvshi://home` | 홈 |
| `ilvshi://daily` | 매일 통행 |
| `ilvshi://random` | 무작위 구절 |
| `ilvshi://favorites` | 즐겨찾기 |
| `ilvshi://famous` | 명구 목록 |
| `ilvshi://search` / `ilvshi://search?q={query}` | 검색 |
| `ilvshi://study` / `ilvshi://study?id={id}` | 봄–학사 |
| `ilvshi://hunt` | 가을 사냥 (`keyword-hunt`/`flyflower`) |
| `ilvshi://handwriting` | Handwriting search (`handwrite`; iOS) |
| `ilvshi://mastered` | 마스터 (`progress`) |
| `ilvshi://categories` / `ilvshi://categories?section=` | 둘러보기 |
| `ilvshi://collection?id=` | 컬렉션 / 책 |
| `ilvshi://corpus` | 모든 통행 (`all`) |
| `ilvshi://last-read` | 마지막으로 읽은 항목 |
| `ilvshi://reading-history` | 읽기 기록 |
| `ilvshi://notes` | 메모 |
| `ilvshi://fables` / `ilvshi://allegories` / `ilvshi://concepts` | 사용할 때 특수 선반 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `ilvshi://settings` | 설정 |
| `ilvshi://usage-guide` | 사용 가이드 |
| `ilvshi://widget-guide` | 위젯 가이드 |
| `ilvshi://shortcuts-guide` | 단축어 가이드 |
| `ilvshi://feature-guide` | 온보딩 다시 보기 |
| `ilvshi://feedback` | 피드백 이메일 |
| `ilvshi://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
ilvshi://daily
ilvshi://passage?id=1
ilvshi://study
ilvshi://hunt
```

</section>
<section lang="ru" markdown="1">

iLvShi поддерживает ярлыки ** `ilvshi://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
ilvshi://{host}?{params}
```


## Проходы и авторы

| URL | Открывает |
|-----|-------|
| `ilvshi://passage?id={id}` | Страница отрывка |
| `ilvshi://saying?id={id}` / `ilvshi://couplet?id={id}` / `ilvshi://poem?id={id}` | Совместимость (Compatibility) |
| `ilvshi://passage?id={id}&card=1` | Детали проезда и карточный лист |
| `ilvshi://card?id={id}` / `ilvshi://share-card?id={id}` | карты |
| `ilvshi://author?id={id}` | Страница автора |
| `ilvshi://recite` / `ilvshi://recite?id={id}` | Режим чтения вслух |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `ilvshi://home` | Главная |
| `ilvshi://daily` | Ежедневный проход |
| `ilvshi://random` | Случайный отрывок |
| `ilvshi://favorites` | Избранное |
| `ilvshi://famous` | Знаменитые строки |
| `ilvshi://search` / `ilvshi://search?q={query}` | Поиск |
| `ilvshi://study` / `ilvshi://study?id={id}` | Весеннее-осеннее исследование |
| `ilvshi://hunt` | Осенняя охота («охота за ключевыми словами» / «флайфлауэр») |
| `ilvshi://handwriting` | Поиск почерка («handwrite»; iOS) |
| `ilvshi://mastered` | Мастеринг («Прогресс») |
| `ilvshi://categories` / `ilvshi://categories?section=` | Обзор |
| `ilvshi://collection?id=` | Коллекция / книга |
| `ilvshi://corpus` | Все пассажи («All») |
| `ilvshi://last-read` | Последнее прочитанное |
| `ilvshi://reading-history` | История чтения |
| `ilvshi://notes` | Заметки |
| `ilvshi://fables` / `ilvshi://allegories` / `ilvshi://concepts` | Специальные полки, когда они доступны |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `ilvshi://settings` | Настройки |
| `ilvshi://usage-guide` | Руководство по использованию |
| `ilvshi://widget-guide` | Руководство по виджетам |
| `ilvshi://shortcuts-guide` | Руководство по «Командам» |
| `ilvshi://feature-guide` | Повторное знакомство |
| `ilvshi://feedback` | Письмо с отзывом |
| `ilvshi://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
ilvshi://daily
ilvshi://passage?id=1
ilvshi://study
ilvshi://hunt
```

</section>
<section lang="th" markdown="1">

ILvShi รองรับ~ `ilvshi://` BAR * ลิงก์ลัด (URL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
ilvshi://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `ilvshi://passage?id={id}` | รายละเอียดข้อความ |
| `ilvshi://saying?id={id}` / `ilvshi://couplet?id={id}` / `ilvshi://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `ilvshi://passage?id={id}&card=1` | รายละเอียดและนามบัตร |
| `ilvshi://card?id={id}` / `ilvshi://share-card?id={id}` | ○ การ์ด |
| `ilvshi://author?id={id}` | รายละเอียดผู้แต่ง |
| `ilvshi://recite` / `ilvshi://recite?id={id}` | โฟลว์การท่อง |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `ilvshi://home` | หน้าแรก |
| `ilvshi://daily` | แบบพาเนลทุกวัน |
| `ilvshi://random` | ข้อความแบบสุ่ม |
| `ilvshi://favorites` | รายการโปรด |
| `ilvshi://famous` | บรรทัดขึ้นชื่อ |
| `ilvshi://search` / `ilvshi://search?q={query}` | ค้นหา |
| `ilvshi://study` / `ilvshi://study?id={id}` | ฤดูใบไม้ผลิ- Autumn การศึกษา |
| `ilvshi://hunt` | Outlook Hunt ('คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน') |
| `ilvshi://handwriting` | สืบค้นเมื่อเขียนด้วยมือ ('เขียนเอง'; OS) |
| `ilvshi://mastered` | สําเร็จการศึกษาแล้ว ('รุก') |
| `ilvshi://categories` / `ilvshi://categories?section=` | เรียกดู |
| `ilvshi://collection?id=` | ชุดสะสม / หนังสือ |
| `ilvshi://corpus` | ทุกช่อง (ทั้งหมด) |
| `ilvshi://last-read` | รายการที่อ่านล่าสุด |
| `ilvshi://reading-history` | ประวัติการอ่าน |
| `ilvshi://notes` | บันทึก |
| `ilvshi://fables` / `ilvshi://allegories` / `ilvshi://concepts` | ชั้นวางพิเศษเมื่อมี |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `ilvshi://settings` | การตั้งค่า |
| `ilvshi://usage-guide` | คู่มือการใช้งาน |
| `ilvshi://widget-guide` | คู่มือวิดเจ็ต |
| `ilvshi://shortcuts-guide` | คู่มือทางลัด |
| `ilvshi://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `ilvshi://feedback` | อีเมลข้อเสนอแนะ |
| `ilvshi://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
ilvshi://daily
ilvshi://passage?id=1
ilvshi://study
ilvshi://hunt
```

</section>
<section lang="de" markdown="1">

iLvShi unterstützt ** `ilvshi://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
ilvshi://{host}?{params}
```


## Passagen & Autoren

| URL | Öffnet |
|-----|-------|
| `ilvshi://passage?id={id}` | Passagen-Detail |
| `ilvshi://saying?id={id}` / `ilvshi://couplet?id={id}` / `ilvshi://poem?id={id}` | Wie Passage (Kompatibilität) |
| `ilvshi://passage?id={id}&card=1` | Angaben zum Durchgang und Kartenblatt |
| `ilvshi://card?id={id}` / `ilvshi://share-card?id={id}` | 秋 Karten |
| `ilvshi://author?id={id}` | Autorendetail |
| `ilvshi://recite` / `ilvshi://recite?id={id}` | Rezitationsablauf |

## Entdeckung und Praxis

| URL | Öffnet |
|-----|-------|
| `ilvshi://home` | Startseite |
| `ilvshi://daily` | Tägliche Passage |
| `ilvshi://random` | Zufällige Passage |
| `ilvshi://favorites` | Favoriten |
| `ilvshi://famous` | Berühmte Zeilen |
| `ilvshi://search` / `ilvshi://search?q={query}` | Suche |
| `ilvshi://study` / `ilvshi://study?id={id}` | Frühjahr-Herbst-Studie |
| `ilvshi://hunt` | Autumn Hunt (`keyword-hunt` / `flyflower`) |
| `ilvshi://handwriting` | Handschriftsuche (`handwrite`; iOS) |
| `ilvshi://mastered` | gemeistert („Fortschritt) |
| `ilvshi://categories` / `ilvshi://categories?section=` | Durchsuchen |
| `ilvshi://collection?id=` | Sammlung/Buch |
| `ilvshi://corpus` | Alle Passagen (`all`) |
| `ilvshi://last-read` | Zuletzt gelesen |
| `ilvshi://reading-history` | Leseverlauf |
| `ilvshi://notes` | Notizen |
| `ilvshi://fables` / `ilvshi://allegories` / `ilvshi://concepts` | Spezialregale, wenn verfügbar |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `ilvshi://settings` | Einstellungen |
| `ilvshi://usage-guide` | Nutzungsanleitung |
| `ilvshi://widget-guide` | Widget-Anleitung |
| `ilvshi://shortcuts-guide` | Kurzbefehle-Anleitung |
| `ilvshi://feature-guide` | Einführung erneut abspielen |
| `ilvshi://feedback` | Feedback-E-Mail |
| `ilvshi://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
ilvshi://daily
ilvshi://passage?id=1
ilvshi://study
ilvshi://hunt
```

</section>
<section lang="fr" markdown="1">

iLvShi prend en charge les liens de raccourci ** `ilvshi://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
ilvshi://{host}?{params}
```


## Passages et auteurs

| URL | Ouvre |
|-----|-------|
| `ilvshi://passage?id={id}` | Détail du passage |
| `ilvshi://saying?id={id}` / `ilvshi://couplet?id={id}` / `ilvshi://poem?id={id}` | Même chose que le passage (compatibilité) |
| `ilvshi://passage?id={id}&card=1` | Détails du passage et feuille de carte |
| `ilvshi://card?id={id}` / `ilvshi://share-card?id={id}` | Cartes |
| `ilvshi://author?id={id}` | Détail de l’auteur |
| `ilvshi://recite` / `ilvshi://recite?id={id}` | Flux de récitation |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `ilvshi://home` | Accueil |
| `ilvshi://daily` | Passage quotidien |
| `ilvshi://random` | Passage aléatoire |
| `ilvshi://favorites` | Favoris |
| `ilvshi://famous` | Vers célèbres |
| `ilvshi://search` / `ilvshi://search?q={query}` | Recherche |
| `ilvshi://study` / `ilvshi://study?id={id}` | Étude printemps-automne |
| `ilvshi://hunt` | Chasse d'automne ( ' chasse aux mots clés ' / 'flyflower ') |
| `ilvshi://handwriting` | Recherche d'écriture (`handwrite`; iOS) |
| `ilvshi://mastered` | Maîtrise ('progrès') |
| `ilvshi://categories` / `ilvshi://categories?section=` | Parcourir |
| `ilvshi://collection?id=` | Collection / livre |
| `ilvshi://corpus` | Tous les passages |
| `ilvshi://last-read` | Dernière lecture |
| `ilvshi://reading-history` | Historique de lecture |
| `ilvshi://notes` | Notes |
| `ilvshi://fables` / `ilvshi://allegories` / `ilvshi://concepts` | Étagères spéciales lorsque disponibles |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `ilvshi://settings` | Réglages |
| `ilvshi://usage-guide` | Guide d'utilisation |
| `ilvshi://widget-guide` | Guide des widgets |
| `ilvshi://shortcuts-guide` | Guide Raccourcis |
| `ilvshi://feature-guide` | Rejouer l’accueil |
| `ilvshi://feedback` | E-mail de commentaires |
| `ilvshi://in-app-review` | Avis in-app / App Store |

## Exemples


```
ilvshi://daily
ilvshi://passage?id=1
ilvshi://study
ilvshi://hunt
```

</section>
<section lang="tr" markdown="1">

iLvShi, ** `ilvshi://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
ilvshi://{host}?{params}
```


## Geçişler ve yazarlar

| URL | Açar |
|-----|-------|
| `ilvshi://passage?id={id}` | Pasaj ayrıntısı |
| `ilvshi://saying?id={id}` / `ilvshi://couplet?id={id}` / `ilvshi://poem?id={id}` | Aynı geçiş (compatability) |
| `ilvshi://passage?id={id}&card=1` | Pasaj detay ve kart sayfası |
| `ilvshi://card?id={id}` / `ilvshi://share-card?id={id}` | kartları |
| `ilvshi://author?id={id}` | Yazar ayrıntısı |
| `ilvshi://recite` / `ilvshi://recite?id={id}` | Okuma akışı |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `ilvshi://home` | Ana sayfa |
| `ilvshi://daily` | Günlük Geçiş |
| `ilvshi://random` | Rastgele pasaj |
| `ilvshi://favorites` | Favoriler |
| `ilvshi://famous` | Ünlü dizeler |
| `ilvshi://search` / `ilvshi://search?q={query}` | Ara |
| `ilvshi://study` / `ilvshi://study?id={id}` | Spring-Autumn Study |
| `ilvshi://hunt` | Sonbahar Av ('keyword-hunt' / 'flyflower') |
| `ilvshi://handwriting` | Hand writing search ('handwrite'; iOS) |
| `ilvshi://mastered` | Mastered ('progress') |
| `ilvshi://categories` / `ilvshi://categories?section=` | Gözat |
| `ilvshi://collection?id=` | Koleksiyon / kitap |
| `ilvshi://corpus` | Bütün geçitler ('all') |
| `ilvshi://last-read` | Son okunan |
| `ilvshi://reading-history` | Okuma geçmişi |
| `ilvshi://notes` | Notlar |
| `ilvshi://fables` / `ilvshi://allegories` / `ilvshi://concepts` | Mevcut özel raflar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `ilvshi://settings` | Ayarlar |
| `ilvshi://usage-guide` | Kullanım kılavuzu |
| `ilvshi://widget-guide` | Widget kılavuzu |
| `ilvshi://shortcuts-guide` | Kısayol kılavuzu |
| `ilvshi://feature-guide` | Tanıtımı yeniden oynat |
| `ilvshi://feedback` | Geri bildirim e-postası |
| `ilvshi://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
ilvshi://daily
ilvshi://passage?id=1
ilvshi://study
ilvshi://hunt
```

</section>
