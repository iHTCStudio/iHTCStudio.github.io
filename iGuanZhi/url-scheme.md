---
layout: doc
title: iGuanZhi — Shortcut Links
app_id: iGuanZhi
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: iguanzhi:// deep links for iGuanZhi — passage, daily, recite, study, hunt, settings guides, and more.
---

<section lang="en" markdown="1">

iGuanZhi supports **`iguanzhi://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
iguanzhi://{host}?{params}
```

## Passages & authors

| URL | Opens |
|-----|-------|
| `iguanzhi://passage?id={id}` | Passage detail |
| `iguanzhi://saying?id={id}` / `iguanzhi://couplet?id={id}` / `iguanzhi://poem?id={id}` | Same as passage (compatibility) |
| `iguanzhi://passage?id={id}&card=1` | Passage detail and card sheet |
| `iguanzhi://card?id={id}` / `iguanzhi://share-card?id={id}` | 古 cards |
| `iguanzhi://author?id={id}` | Author detail |
| `iguanzhi://recite` / `iguanzhi://recite?id={id}` | Recite flow |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `iguanzhi://home` | Home |
| `iguanzhi://daily` | Today’s Essay |
| `iguanzhi://random` | Random passage |
| `iguanzhi://favorites` | Favorites |
| `iguanzhi://famous` | Famous lines |
| `iguanzhi://search` / `iguanzhi://search?q={query}` | Search |
| `iguanzhi://study` / `iguanzhi://study?id={id}` | Classics Study |
| `iguanzhi://hunt` | Essay Hunt (`keyword-hunt` / `flyflower`) |
| `iguanzhi://handwriting` | Handwriting search (`handwrite`; iOS) |
| `iguanzhi://mastered` | Mastered (`progress`) |
| `iguanzhi://categories` / `iguanzhi://categories?section=` | Browse |
| `iguanzhi://collection?id=` | Collection / book |
| `iguanzhi://corpus` | All passages (`all`) |
| `iguanzhi://last-read` | Last read |
| `iguanzhi://reading-history` | Reading history |
| `iguanzhi://notes` | Notes |
| `iguanzhi://fables` / `iguanzhi://allegories` / `iguanzhi://concepts` | Specialty shelves when available |

## Settings & guides

| URL | Opens |
|-----|-------|
| `iguanzhi://settings` | Settings |
| `iguanzhi://usage-guide` | Usage guide |
| `iguanzhi://widget-guide` | Widget guide |
| `iguanzhi://shortcuts-guide` | Shortcuts guide |
| `iguanzhi://feature-guide` | Replay onboarding |
| `iguanzhi://feedback` | Feedback email |
| `iguanzhi://in-app-review` | In-app / Store review entry |

## Examples

```
iguanzhi://daily
iguanzhi://passage?id=1
iguanzhi://study
iguanzhi://hunt
```

</section>
<section lang="zh-CN" markdown="1">

爱古文观止 支持 **`iguanzhi://`** 快捷链接（URL Scheme）。冷启动与主屏幕快捷方式经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
iguanzhi://{host}?{params}
```

## 篇目与作者

| URL | 打开 |
|-----|------|
| `iguanzhi://passage?id={id}` | 篇目详情 |
| `iguanzhi://saying?id={id}` / `iguanzhi://couplet?id={id}` / `iguanzhi://poem?id={id}` | 同 passage（兼容） |
| `iguanzhi://passage?id={id}&card=1` | 篇目详情并打开分享卡 |
| `iguanzhi://card?id={id}` / `iguanzhi://share-card?id={id}` | 古卡 |
| `iguanzhi://author?id={id}` | 作者详情 |
| `iguanzhi://recite` / `iguanzhi://recite?id={id}` | 诵读 |

## 发现与练习

| URL | 打开 |
|-----|------|
| `iguanzhi://home` | 首页 |
| `iguanzhi://daily` | 今日一文 |
| `iguanzhi://random` | 随机一篇 |
| `iguanzhi://favorites` | 收藏 |
| `iguanzhi://famous` | 名句 |
| `iguanzhi://search` / `iguanzhi://search?q={query}` | 搜索 |
| `iguanzhi://study` / `iguanzhi://study?id={id}` | 古文学堂 |
| `iguanzhi://hunt` | 寻章（`keyword-hunt` / `flyflower`） |
| `iguanzhi://handwriting` | 手写寻句（`handwrite`；iOS） |
| `iguanzhi://mastered` | 已掌握（`progress`） |
| `iguanzhi://categories` / `iguanzhi://categories?section=` | 浏览 |
| `iguanzhi://collection?id=` | 合集／分册 |
| `iguanzhi://corpus` | 全部篇目（`all`） |
| `iguanzhi://last-read` | 上次阅读 |
| `iguanzhi://reading-history` | 阅读历史 |
| `iguanzhi://notes` | 笔记 |
| `iguanzhi://fables` / `iguanzhi://allegories` / `iguanzhi://concepts` | 专属书架（如有） |

## 设置与指南

| URL | 打开 |
|-----|------|
| `iguanzhi://settings` | 设置 |
| `iguanzhi://usage-guide` | 使用说明 |
| `iguanzhi://widget-guide` | 小组件说明 |
| `iguanzhi://shortcuts-guide` | 快捷指令说明 |
| `iguanzhi://feature-guide` | 重看功能导览 |
| `iguanzhi://feedback` | 反馈邮件 |
| `iguanzhi://in-app-review` | 应用内／商店评价入口 |

## 示例

```
iguanzhi://daily
iguanzhi://passage?id=1
iguanzhi://study
iguanzhi://hunt
```

</section>
<section lang="zh-TW" markdown="1">

愛古文觀止 支援 **`iguanzhi://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複打開。

## 連結格式

```
iguanzhi://{host}?{params}
```

## 篇目與作者

| URL | 打開 |
|-----|------|
| `iguanzhi://passage?id={id}` | 篇目詳情 |
| `iguanzhi://saying?id={id}` / `iguanzhi://couplet?id={id}` / `iguanzhi://poem?id={id}` | 同 passage（相容） |
| `iguanzhi://passage?id={id}&card=1` | 篇目詳情並打開分享卡 |
| `iguanzhi://card?id={id}` / `iguanzhi://share-card?id={id}` | 古卡 |
| `iguanzhi://author?id={id}` | 作者詳情 |
| `iguanzhi://recite` / `iguanzhi://recite?id={id}` | 誦讀 |

## 探索與練習

| URL | 打開 |
|-----|------|
| `iguanzhi://home` | 首頁 |
| `iguanzhi://daily` | 今日一文 |
| `iguanzhi://random` | 隨機一篇 |
| `iguanzhi://favorites` | 收藏 |
| `iguanzhi://famous` | 名句 |
| `iguanzhi://search` / `iguanzhi://search?q={query}` | 搜尋 |
| `iguanzhi://study` / `iguanzhi://study?id={id}` | 古文學堂 |
| `iguanzhi://hunt` | 尋章（`keyword-hunt` / `flyflower`） |
| `iguanzhi://handwriting` | 手寫尋句（`handwrite`；iOS） |
| `iguanzhi://mastered` | 已掌握（`progress`） |
| `iguanzhi://categories` / `iguanzhi://categories?section=` | 瀏覽 |
| `iguanzhi://collection?id=` | 合集／分冊 |
| `iguanzhi://corpus` | 全部篇目（`all`） |
| `iguanzhi://last-read` | 上次閱讀 |
| `iguanzhi://reading-history` | 閱讀歷史 |
| `iguanzhi://notes` | 筆記 |
| `iguanzhi://fables` / `iguanzhi://allegories` / `iguanzhi://concepts` | 專屬書架（如有） |

## 設定與指南

| URL | 打開 |
|-----|------|
| `iguanzhi://settings` | 設定 |
| `iguanzhi://usage-guide` | 使用說明 |
| `iguanzhi://widget-guide` | 小工具說明 |
| `iguanzhi://shortcuts-guide` | 捷徑說明 |
| `iguanzhi://feature-guide` | 重看功能導覽 |
| `iguanzhi://feedback` | 回饋郵件 |
| `iguanzhi://in-app-review` | 應用內／商店評價入口 |

## 範例

```
iguanzhi://daily
iguanzhi://passage?id=1
iguanzhi://study
iguanzhi://hunt
```

</section>
<section lang="ja" markdown="1">

iGuanZhiは** `iguanzhi://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
iguanzhi://{host}?{params}
```


## パスポートと著者

| URL | 開く画面 |
|-----|-------|
| `iguanzhi://passage?id={id}` | 章句の詳細 |
| `iguanzhi://saying?id={id}` / `iguanzhi://couplet?id={id}` / `iguanzhi://poem?id={id}` | 通路と同じ(互換性) |
| `iguanzhi://passage?id={id}&card=1` | 通路の細部およびカード シート |
| `iguanzhi://card?id={id}` / `iguanzhi://share-card?id={id}` | 古カード |
| `iguanzhi://author?id={id}` | 作者の詳細 |
| `iguanzhi://recite` / `iguanzhi://recite?id={id}` | 誦読フロー |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `iguanzhi://home` | ホーム |
| `iguanzhi://daily` | 今日のエッセイ |
| `iguanzhi://random` | ランダムな章句 |
| `iguanzhi://favorites` | お気に入り |
| `iguanzhi://famous` | 名句一覧 |
| `iguanzhi://search` / `iguanzhi://search?q={query}` | 検索 |
| `iguanzhi://study` / `iguanzhi://study?id={id}` | 古典スタディ |
| `iguanzhi://hunt` | エッセイハント (`keyword-hunt`/`flyflower`) |
| `iguanzhi://handwriting` | 手書き検索 (`handwrite`; iOS) |
| `iguanzhi://mastered` | マスタード (`progress`) |
| `iguanzhi://categories` / `iguanzhi://categories?section=` | ブラウズ |
| `iguanzhi://collection?id=` | コレクション/書籍 |
| `iguanzhi://corpus` | すべての通路 (`all`) |
| `iguanzhi://last-read` | 最後に読んだ項目 |
| `iguanzhi://reading-history` | 閲覧履歴 |
| `iguanzhi://notes` | ノート |
| `iguanzhi://fables` / `iguanzhi://allegories` / `iguanzhi://concepts` | 利用できる場合の特別な棚 |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `iguanzhi://settings` | 設定 |
| `iguanzhi://usage-guide` | 使い方ガイド |
| `iguanzhi://widget-guide` | ウィジェットガイド |
| `iguanzhi://shortcuts-guide` | ショートカットガイド |
| `iguanzhi://feature-guide` | オンボーディングの再生 |
| `iguanzhi://feedback` | フィードバックメール |
| `iguanzhi://in-app-review` | アプリ内／App Store レビュー |

## 例


```
iguanzhi://daily
iguanzhi://passage?id=1
iguanzhi://study
iguanzhi://hunt
```

</section>
<section lang="ko" markdown="1">

iGuanZhi는 ** `iguanzhi://` ** 단축키 링크 (URL 계획)를 지원합니다. 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
iguanzhi://{host}?{params}
```


## 책임 & 저자

| URL | 열리는 화면 |
|-----|-------|
| `iguanzhi://passage?id={id}` | 구절 상세 |
| `iguanzhi://saying?id={id}` / `iguanzhi://couplet?id={id}` / `iguanzhi://poem?id={id}` | 통행과 같 ( 겸용성) |
| `iguanzhi://passage?id={id}&card=1` | 통행 세부사항과 카드 장 |
| `iguanzhi://card?id={id}` / `iguanzhi://share-card?id={id}` | 카드 종류 |
| `iguanzhi://author?id={id}` | 작가 상세 |
| `iguanzhi://recite` / `iguanzhi://recite?id={id}` | 낭독 흐름 |

## 디스커버리 & 연습

| URL | 열리는 화면 |
|-----|-------|
| `iguanzhi://home` | 홈 |
| `iguanzhi://daily` | 오늘의 에세이 |
| `iguanzhi://random` | 무작위 구절 |
| `iguanzhi://favorites` | 즐겨찾기 |
| `iguanzhi://famous` | 명구 목록 |
| `iguanzhi://search` / `iguanzhi://search?q={query}` | 검색 |
| `iguanzhi://study` / `iguanzhi://study?id={id}` | Classics 학습 |
| `iguanzhi://hunt` | 에세이 사냥 (`keyword-hunt`/`flyflower`) |
| `iguanzhi://handwriting` | Handwriting search (`handwrite`; iOS) |
| `iguanzhi://mastered` | 마스터 (`progress`) |
| `iguanzhi://categories` / `iguanzhi://categories?section=` | 둘러보기 |
| `iguanzhi://collection?id=` | 컬렉션 / 책 |
| `iguanzhi://corpus` | 모든 통행 (`all`) |
| `iguanzhi://last-read` | 마지막으로 읽은 항목 |
| `iguanzhi://reading-history` | 읽기 기록 |
| `iguanzhi://notes` | 메모 |
| `iguanzhi://fables` / `iguanzhi://allegories` / `iguanzhi://concepts` | 사용할 때 특수 선반 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `iguanzhi://settings` | 설정 |
| `iguanzhi://usage-guide` | 사용 가이드 |
| `iguanzhi://widget-guide` | 위젯 가이드 |
| `iguanzhi://shortcuts-guide` | 단축어 가이드 |
| `iguanzhi://feature-guide` | 온보딩 다시 보기 |
| `iguanzhi://feedback` | 피드백 이메일 |
| `iguanzhi://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
iguanzhi://daily
iguanzhi://passage?id=1
iguanzhi://study
iguanzhi://hunt
```

</section>
<section lang="ru" markdown="1">

iGuanZhi поддерживает ярлыки ** `iguanzhi://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
iguanzhi://{host}?{params}
```


## Проходы и авторы

| URL | Открывает |
|-----|-------|
| `iguanzhi://passage?id={id}` | Страница отрывка |
| `iguanzhi://saying?id={id}` / `iguanzhi://couplet?id={id}` / `iguanzhi://poem?id={id}` | Совместимость (Compatibility) |
| `iguanzhi://passage?id={id}&card=1` | Детали проезда и карточный лист |
| `iguanzhi://card?id={id}` / `iguanzhi://share-card?id={id}` | карты |
| `iguanzhi://author?id={id}` | Страница автора |
| `iguanzhi://recite` / `iguanzhi://recite?id={id}` | Режим чтения вслух |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `iguanzhi://home` | Главная |
| `iguanzhi://daily` | Сегодняшнее эссе |
| `iguanzhi://random` | Случайный отрывок |
| `iguanzhi://favorites` | Избранное |
| `iguanzhi://famous` | Знаменитые строки |
| `iguanzhi://search` / `iguanzhi://search?q={query}` | Поиск |
| `iguanzhi://study` / `iguanzhi://study?id={id}` | Изучение классики |
| `iguanzhi://hunt` | Эссе Хант («охота за ключевыми словами» / «флайфлауэр») |
| `iguanzhi://handwriting` | Поиск почерка («handwrite»; iOS) |
| `iguanzhi://mastered` | Мастеринг («Прогресс») |
| `iguanzhi://categories` / `iguanzhi://categories?section=` | Обзор |
| `iguanzhi://collection?id=` | Коллекция / книга |
| `iguanzhi://corpus` | Все пассажи («All») |
| `iguanzhi://last-read` | Последнее прочитанное |
| `iguanzhi://reading-history` | История чтения |
| `iguanzhi://notes` | Заметки |
| `iguanzhi://fables` / `iguanzhi://allegories` / `iguanzhi://concepts` | Специальные полки, когда они доступны |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `iguanzhi://settings` | Настройки |
| `iguanzhi://usage-guide` | Руководство по использованию |
| `iguanzhi://widget-guide` | Руководство по виджетам |
| `iguanzhi://shortcuts-guide` | Руководство по «Командам» |
| `iguanzhi://feature-guide` | Повторное знакомство |
| `iguanzhi://feedback` | Письмо с отзывом |
| `iguanzhi://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
iguanzhi://daily
iguanzhi://passage?id=1
iguanzhi://study
iguanzhi://hunt
```

</section>
<section lang="th" markdown="1">

iguanZhi รองรับ~ `iguanzhi://` BAR * ลิงก์ลัด (URL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
iguanzhi://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `iguanzhi://passage?id={id}` | รายละเอียดข้อความ |
| `iguanzhi://saying?id={id}` / `iguanzhi://couplet?id={id}` / `iguanzhi://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `iguanzhi://passage?id={id}&card=1` | รายละเอียดและนามบัตร |
| `iguanzhi://card?id={id}` / `iguanzhi://share-card?id={id}` | ○ การ์ด |
| `iguanzhi://author?id={id}` | รายละเอียดผู้แต่ง |
| `iguanzhi://recite` / `iguanzhi://recite?id={id}` | โฟลว์การท่อง |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `iguanzhi://home` | หน้าแรก |
| `iguanzhi://daily` | คํา กล่าว ใน ปัจจุบัน |
| `iguanzhi://random` | ข้อความแบบสุ่ม |
| `iguanzhi://favorites` | รายการโปรด |
| `iguanzhi://famous` | บรรทัดขึ้นชื่อ |
| `iguanzhi://search` / `iguanzhi://search?q={query}` | ค้นหา |
| `iguanzhi://study` / `iguanzhi://study?id={id}` | การ ศึกษา แบบ คลาสสิก |
| `iguanzhi://hunt` | Esay Hunt ('คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน') |
| `iguanzhi://handwriting` | สืบค้นเมื่อเขียนด้วยมือ ('เขียนเอง'; OS) |
| `iguanzhi://mastered` | สําเร็จการศึกษาแล้ว ('รุก') |
| `iguanzhi://categories` / `iguanzhi://categories?section=` | เรียกดู |
| `iguanzhi://collection?id=` | ชุดสะสม / หนังสือ |
| `iguanzhi://corpus` | ทุกช่อง (ทั้งหมด) |
| `iguanzhi://last-read` | รายการที่อ่านล่าสุด |
| `iguanzhi://reading-history` | ประวัติการอ่าน |
| `iguanzhi://notes` | บันทึก |
| `iguanzhi://fables` / `iguanzhi://allegories` / `iguanzhi://concepts` | ชั้นวางพิเศษเมื่อมี |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `iguanzhi://settings` | การตั้งค่า |
| `iguanzhi://usage-guide` | คู่มือการใช้งาน |
| `iguanzhi://widget-guide` | คู่มือวิดเจ็ต |
| `iguanzhi://shortcuts-guide` | คู่มือทางลัด |
| `iguanzhi://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `iguanzhi://feedback` | อีเมลข้อเสนอแนะ |
| `iguanzhi://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
iguanzhi://daily
iguanzhi://passage?id=1
iguanzhi://study
iguanzhi://hunt
```

</section>
<section lang="de" markdown="1">

iGuanZhi unterstützt ** `iguanzhi://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
iguanzhi://{host}?{params}
```


## Passagen & Autoren

| URL | Öffnet |
|-----|-------|
| `iguanzhi://passage?id={id}` | Passagen-Detail |
| `iguanzhi://saying?id={id}` / `iguanzhi://couplet?id={id}` / `iguanzhi://poem?id={id}` | Wie Passage (Kompatibilität) |
| `iguanzhi://passage?id={id}&card=1` | Angaben zum Durchgang und Kartenblatt |
| `iguanzhi://card?id={id}` / `iguanzhi://share-card?id={id}` | 古 Karten |
| `iguanzhi://author?id={id}` | Autorendetail |
| `iguanzhi://recite` / `iguanzhi://recite?id={id}` | Rezitationsablauf |

## Entdeckung und Praxis

| URL | Öffnet |
|-----|-------|
| `iguanzhi://home` | Startseite |
| `iguanzhi://daily` | Der heutige Essay |
| `iguanzhi://random` | Zufällige Passage |
| `iguanzhi://favorites` | Favoriten |
| `iguanzhi://famous` | Berühmte Zeilen |
| `iguanzhi://search` / `iguanzhi://search?q={query}` | Suche |
| `iguanzhi://study` / `iguanzhi://study?id={id}` | Klassiker Studie |
| `iguanzhi://hunt` | Essay Hunt ('keyword-hunt' / 'flyflower') |
| `iguanzhi://handwriting` | Handschriftsuche (`handwrite`; iOS) |
| `iguanzhi://mastered` | gemeistert („Fortschritt) |
| `iguanzhi://categories` / `iguanzhi://categories?section=` | Durchsuchen |
| `iguanzhi://collection?id=` | Sammlung/Buch |
| `iguanzhi://corpus` | Alle Passagen (`all`) |
| `iguanzhi://last-read` | Zuletzt gelesen |
| `iguanzhi://reading-history` | Leseverlauf |
| `iguanzhi://notes` | Notizen |
| `iguanzhi://fables` / `iguanzhi://allegories` / `iguanzhi://concepts` | Spezialregale, wenn verfügbar |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `iguanzhi://settings` | Einstellungen |
| `iguanzhi://usage-guide` | Nutzungsanleitung |
| `iguanzhi://widget-guide` | Widget-Anleitung |
| `iguanzhi://shortcuts-guide` | Kurzbefehle-Anleitung |
| `iguanzhi://feature-guide` | Einführung erneut abspielen |
| `iguanzhi://feedback` | Feedback-E-Mail |
| `iguanzhi://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
iguanzhi://daily
iguanzhi://passage?id=1
iguanzhi://study
iguanzhi://hunt
```

</section>
<section lang="fr" markdown="1">

iGuanZhi prend en charge les liens de raccourci ** `iguanzhi://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
iguanzhi://{host}?{params}
```


## Passages et auteurs

| URL | Ouvre |
|-----|-------|
| `iguanzhi://passage?id={id}` | Détail du passage |
| `iguanzhi://saying?id={id}` / `iguanzhi://couplet?id={id}` / `iguanzhi://poem?id={id}` | Même chose que le passage (compatibilité) |
| `iguanzhi://passage?id={id}&card=1` | Détails du passage et feuille de carte |
| `iguanzhi://card?id={id}` / `iguanzhi://share-card?id={id}` | Cartes |
| `iguanzhi://author?id={id}` | Détail de l’auteur |
| `iguanzhi://recite` / `iguanzhi://recite?id={id}` | Flux de récitation |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `iguanzhi://home` | Accueil |
| `iguanzhi://daily` | Aujourd'hui Essay |
| `iguanzhi://random` | Passage aléatoire |
| `iguanzhi://favorites` | Favoris |
| `iguanzhi://famous` | Vers célèbres |
| `iguanzhi://search` / `iguanzhi://search?q={query}` | Recherche |
| `iguanzhi://study` / `iguanzhi://study?id={id}` | Études classiques |
| `iguanzhi://hunt` | Chasse aux mots clés / chasse aux fleurs volantes |
| `iguanzhi://handwriting` | Recherche d'écriture (`handwrite`; iOS) |
| `iguanzhi://mastered` | Maîtrise ('progrès') |
| `iguanzhi://categories` / `iguanzhi://categories?section=` | Parcourir |
| `iguanzhi://collection?id=` | Collection / livre |
| `iguanzhi://corpus` | Tous les passages |
| `iguanzhi://last-read` | Dernière lecture |
| `iguanzhi://reading-history` | Historique de lecture |
| `iguanzhi://notes` | Notes |
| `iguanzhi://fables` / `iguanzhi://allegories` / `iguanzhi://concepts` | Étagères spéciales lorsque disponibles |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `iguanzhi://settings` | Réglages |
| `iguanzhi://usage-guide` | Guide d'utilisation |
| `iguanzhi://widget-guide` | Guide des widgets |
| `iguanzhi://shortcuts-guide` | Guide Raccourcis |
| `iguanzhi://feature-guide` | Rejouer l’accueil |
| `iguanzhi://feedback` | E-mail de commentaires |
| `iguanzhi://in-app-review` | Avis in-app / App Store |

## Exemples


```
iguanzhi://daily
iguanzhi://passage?id=1
iguanzhi://study
iguanzhi://hunt
```

</section>
<section lang="tr" markdown="1">

iGuanZhi ** `iguanzhi://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
iguanzhi://{host}?{params}
```


## Geçişler ve yazarlar

| URL | Açar |
|-----|-------|
| `iguanzhi://passage?id={id}` | Pasaj ayrıntısı |
| `iguanzhi://saying?id={id}` / `iguanzhi://couplet?id={id}` / `iguanzhi://poem?id={id}` | Aynı geçiş (compatability) |
| `iguanzhi://passage?id={id}&card=1` | Pasaj detay ve kart sayfası |
| `iguanzhi://card?id={id}` / `iguanzhi://share-card?id={id}` | kartları |
| `iguanzhi://author?id={id}` | Yazar ayrıntısı |
| `iguanzhi://recite` / `iguanzhi://recite?id={id}` | Okuma akışı |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `iguanzhi://home` | Ana sayfa |
| `iguanzhi://daily` | Bugün Deneme |
| `iguanzhi://random` | Rastgele pasaj |
| `iguanzhi://favorites` | Favoriler |
| `iguanzhi://famous` | Ünlü dizeler |
| `iguanzhi://search` / `iguanzhi://search?q={query}` | Ara |
| `iguanzhi://study` / `iguanzhi://study?id={id}` | Classics Study |
| `iguanzhi://hunt` | Essay Hunt ('keyword-hunt' / 'flyflower') |
| `iguanzhi://handwriting` | Hand writing search ('handwrite'; iOS) |
| `iguanzhi://mastered` | Mastered ('progress') |
| `iguanzhi://categories` / `iguanzhi://categories?section=` | Gözat |
| `iguanzhi://collection?id=` | Koleksiyon / kitap |
| `iguanzhi://corpus` | Bütün geçitler ('all') |
| `iguanzhi://last-read` | Son okunan |
| `iguanzhi://reading-history` | Okuma geçmişi |
| `iguanzhi://notes` | Notlar |
| `iguanzhi://fables` / `iguanzhi://allegories` / `iguanzhi://concepts` | Mevcut özel raflar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `iguanzhi://settings` | Ayarlar |
| `iguanzhi://usage-guide` | Kullanım kılavuzu |
| `iguanzhi://widget-guide` | Widget kılavuzu |
| `iguanzhi://shortcuts-guide` | Kısayol kılavuzu |
| `iguanzhi://feature-guide` | Tanıtımı yeniden oynat |
| `iguanzhi://feedback` | Geri bildirim e-postası |
| `iguanzhi://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
iguanzhi://daily
iguanzhi://passage?id=1
iguanzhi://study
iguanzhi://hunt
```

</section>
