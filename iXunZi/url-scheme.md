---
layout: doc
title: iXunZi — Shortcut Links
app_id: iXunZi
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: ixunzi:// deep links for iXunZi — passage, daily, recite, study, hunt, settings guides, and more.
---

<section lang="en" markdown="1">

iXunZi supports **`ixunzi://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
ixunzi://{host}?{params}
```

## Passages & authors

| URL | Opens |
|-----|-------|
| `ixunzi://passage?id={id}` | Passage detail |
| `ixunzi://saying?id={id}` / `ixunzi://couplet?id={id}` / `ixunzi://poem?id={id}` | Same as passage (compatibility) |
| `ixunzi://passage?id={id}&card=1` | Passage detail and card sheet |
| `ixunzi://card?id={id}` / `ixunzi://share-card?id={id}` | 荀 cards |
| `ixunzi://author?id={id}` | Author detail |
| `ixunzi://recite` / `ixunzi://recite?id={id}` | Recite flow |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `ixunzi://home` | Home |
| `ixunzi://daily` | Daily Xun |
| `ixunzi://random` | Random passage |
| `ixunzi://favorites` | Favorites |
| `ixunzi://famous` | Famous lines |
| `ixunzi://search` / `ixunzi://search?q={query}` | Search |
| `ixunzi://study` / `ixunzi://study?id={id}` | Encouraging Learning Academy |
| `ixunzi://hunt` | Xun Hunt (`keyword-hunt` / `flyflower`) |
| `ixunzi://handwriting` | Handwriting search (`handwrite`; iOS) |
| `ixunzi://mastered` | Mastered (`progress`) |
| `ixunzi://categories` / `ixunzi://categories?section=` | Browse |
| `ixunzi://collection?id=` | Collection / book |
| `ixunzi://corpus` | All passages (`all`) |
| `ixunzi://last-read` | Last read |
| `ixunzi://reading-history` | Reading history |
| `ixunzi://notes` | Notes |
| `ixunzi://ask` | Ask Xunzi |
| `ixunzi://fables` / `ixunzi://allegories` / `ixunzi://concepts` | Specialty shelves when available |

## Settings & guides

| URL | Opens |
|-----|-------|
| `ixunzi://settings` | Settings |
| `ixunzi://usage-guide` | Usage guide |
| `ixunzi://widget-guide` | Widget guide |
| `ixunzi://shortcuts-guide` | Shortcuts guide |
| `ixunzi://feature-guide` | Replay onboarding |
| `ixunzi://feedback` | Feedback email |
| `ixunzi://in-app-review` | In-app / Store review entry |

## Examples

```
ixunzi://daily
ixunzi://passage?id=1
ixunzi://ask
ixunzi://study
ixunzi://hunt
```

</section>
<section lang="zh-CN" markdown="1">

爱荀子 支持 **`ixunzi://`** 快捷链接（URL Scheme）。冷启动与主屏幕快捷方式经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
ixunzi://{host}?{params}
```

## 篇目与作者

| URL | 打开 |
|-----|------|
| `ixunzi://passage?id={id}` | 篇目详情 |
| `ixunzi://saying?id={id}` / `ixunzi://couplet?id={id}` / `ixunzi://poem?id={id}` | 同 passage（兼容） |
| `ixunzi://passage?id={id}&card=1` | 篇目详情并打开分享卡 |
| `ixunzi://card?id={id}` / `ixunzi://share-card?id={id}` | 荀卡 |
| `ixunzi://author?id={id}` | 作者详情 |
| `ixunzi://recite` / `ixunzi://recite?id={id}` | 诵读 |

## 发现与练习

| URL | 打开 |
|-----|------|
| `ixunzi://home` | 首页 |
| `ixunzi://daily` | 每日一荀 |
| `ixunzi://random` | 随机一篇 |
| `ixunzi://favorites` | 收藏 |
| `ixunzi://famous` | 名句 |
| `ixunzi://search` / `ixunzi://search?q={query}` | 搜索 |
| `ixunzi://study` / `ixunzi://study?id={id}` | 劝学书院 |
| `ixunzi://hunt` | 寻荀（`keyword-hunt` / `flyflower`） |
| `ixunzi://handwriting` | 手写寻句（`handwrite`；iOS） |
| `ixunzi://mastered` | 已掌握（`progress`） |
| `ixunzi://categories` / `ixunzi://categories?section=` | 浏览 |
| `ixunzi://collection?id=` | 合集／分册 |
| `ixunzi://corpus` | 全部篇目（`all`） |
| `ixunzi://last-read` | 上次阅读 |
| `ixunzi://reading-history` | 阅读历史 |
| `ixunzi://notes` | 笔记 |
| `ixunzi://ask` | 问荀子 |
| `ixunzi://fables` / `ixunzi://allegories` / `ixunzi://concepts` | 专属书架（如有） |

## 设置与指南

| URL | 打开 |
|-----|------|
| `ixunzi://settings` | 设置 |
| `ixunzi://usage-guide` | 使用说明 |
| `ixunzi://widget-guide` | 小组件说明 |
| `ixunzi://shortcuts-guide` | 快捷指令说明 |
| `ixunzi://feature-guide` | 重看功能导览 |
| `ixunzi://feedback` | 反馈邮件 |
| `ixunzi://in-app-review` | 应用内／商店评价入口 |

## 示例

```
ixunzi://daily
ixunzi://passage?id=1
ixunzi://ask
ixunzi://study
ixunzi://hunt
```

</section>
<section lang="zh-TW" markdown="1">

愛荀子 支援 **`ixunzi://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複打開。

## 連結格式

```
ixunzi://{host}?{params}
```

## 篇目與作者

| URL | 打開 |
|-----|------|
| `ixunzi://passage?id={id}` | 篇目詳情 |
| `ixunzi://saying?id={id}` / `ixunzi://couplet?id={id}` / `ixunzi://poem?id={id}` | 同 passage（相容） |
| `ixunzi://passage?id={id}&card=1` | 篇目詳情並打開分享卡 |
| `ixunzi://card?id={id}` / `ixunzi://share-card?id={id}` | 荀卡 |
| `ixunzi://author?id={id}` | 作者詳情 |
| `ixunzi://recite` / `ixunzi://recite?id={id}` | 誦讀 |

## 探索與練習

| URL | 打開 |
|-----|------|
| `ixunzi://home` | 首頁 |
| `ixunzi://daily` | 每日一荀 |
| `ixunzi://random` | 隨機一篇 |
| `ixunzi://favorites` | 收藏 |
| `ixunzi://famous` | 名句 |
| `ixunzi://search` / `ixunzi://search?q={query}` | 搜尋 |
| `ixunzi://study` / `ixunzi://study?id={id}` | 勸學書院 |
| `ixunzi://hunt` | 尋荀（`keyword-hunt` / `flyflower`） |
| `ixunzi://handwriting` | 手寫尋句（`handwrite`；iOS） |
| `ixunzi://mastered` | 已掌握（`progress`） |
| `ixunzi://categories` / `ixunzi://categories?section=` | 瀏覽 |
| `ixunzi://collection?id=` | 合集／分冊 |
| `ixunzi://corpus` | 全部篇目（`all`） |
| `ixunzi://last-read` | 上次閱讀 |
| `ixunzi://reading-history` | 閱讀歷史 |
| `ixunzi://notes` | 筆記 |
| `ixunzi://ask` | 問荀子 |
| `ixunzi://fables` / `ixunzi://allegories` / `ixunzi://concepts` | 專屬書架（如有） |

## 設定與指南

| URL | 打開 |
|-----|------|
| `ixunzi://settings` | 設定 |
| `ixunzi://usage-guide` | 使用說明 |
| `ixunzi://widget-guide` | 小工具說明 |
| `ixunzi://shortcuts-guide` | 捷徑說明 |
| `ixunzi://feature-guide` | 重看功能導覽 |
| `ixunzi://feedback` | 回饋郵件 |
| `ixunzi://in-app-review` | 應用內／商店評價入口 |

## 範例

```
ixunzi://daily
ixunzi://passage?id=1
ixunzi://ask
ixunzi://study
ixunzi://hunt
```

</section>
<section lang="ja" markdown="1">

iXunZiは** `ixunzi://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
ixunzi://{host}?{params}
```


## パスポートと著者

| URL | 開く画面 |
|-----|-------|
| `ixunzi://passage?id={id}` | 章句の詳細 |
| `ixunzi://saying?id={id}` / `ixunzi://couplet?id={id}` / `ixunzi://poem?id={id}` | 通路と同じ(互換性) |
| `ixunzi://passage?id={id}&card=1` | 通路の細部およびカード シート |
| `ixunzi://card?id={id}` / `ixunzi://share-card?id={id}` | カード |
| `ixunzi://author?id={id}` | 作者の詳細 |
| `ixunzi://recite` / `ixunzi://recite?id={id}` | 誦読フロー |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `ixunzi://home` | ホーム |
| `ixunzi://daily` | デイリー・クーン |
| `ixunzi://random` | ランダムな章句 |
| `ixunzi://favorites` | お気に入り |
| `ixunzi://famous` | 名句一覧 |
| `ixunzi://search` / `ixunzi://search?q={query}` | 検索 |
| `ixunzi://study` / `ixunzi://study?id={id}` | 学習アカデミーの奨励 |
| `ixunzi://hunt` | Xun ハント (`keyword-hunt`/`flyflower`) |
| `ixunzi://handwriting` | 手書き検索 (`handwrite`; iOS) |
| `ixunzi://mastered` | マスタード (`progress`) |
| `ixunzi://categories` / `ixunzi://categories?section=` | ブラウズ |
| `ixunzi://collection?id=` | コレクション/書籍 |
| `ixunzi://corpus` | すべての通路 (`all`) |
| `ixunzi://last-read` | 最後に読んだ項目 |
| `ixunzi://reading-history` | 閲覧履歴 |
| `ixunzi://notes` | ノート |
| `ixunzi://ask` | Xunziを尋ねる |
| `ixunzi://fables` / `ixunzi://allegories` / `ixunzi://concepts` | 利用できる場合の特別な棚 |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `ixunzi://settings` | 設定 |
| `ixunzi://usage-guide` | 使い方ガイド |
| `ixunzi://widget-guide` | ウィジェットガイド |
| `ixunzi://shortcuts-guide` | ショートカットガイド |
| `ixunzi://feature-guide` | オンボーディングの再生 |
| `ixunzi://feedback` | フィードバックメール |
| `ixunzi://in-app-review` | アプリ内／App Store レビュー |

## 例


```
ixunzi://daily
ixunzi://passage?id=1
ixunzi://ask
ixunzi://study
ixunzi://hunt
```

</section>
<section lang="ko" markdown="1">

iXunZi 지원 ** `ixunzi://` ** 단축키 링크 (URL 계획). 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
ixunzi://{host}?{params}
```


## 책임 & 저자

| URL | 열리는 화면 |
|-----|-------|
| `ixunzi://passage?id={id}` | 구절 상세 |
| `ixunzi://saying?id={id}` / `ixunzi://couplet?id={id}` / `ixunzi://poem?id={id}` | 통행과 같 ( 겸용성) |
| `ixunzi://passage?id={id}&card=1` | 통행 세부사항과 카드 장 |
| `ixunzi://card?id={id}` / `ixunzi://share-card?id={id}` | 카드 |
| `ixunzi://author?id={id}` | 작가 상세 |
| `ixunzi://recite` / `ixunzi://recite?id={id}` | 낭독 흐름 |

## 디스커버리 & 연습

| URL | 열리는 화면 |
|-----|-------|
| `ixunzi://home` | 홈 |
| `ixunzi://daily` | 매일 Xun |
| `ixunzi://random` | 무작위 구절 |
| `ixunzi://favorites` | 즐겨찾기 |
| `ixunzi://famous` | 명구 목록 |
| `ixunzi://search` / `ixunzi://search?q={query}` | 검색 |
| `ixunzi://study` / `ixunzi://study?id={id}` | 학습 아카데미 |
| `ixunzi://hunt` | Xun Hunt (`keyword-hunt`/`flyflower`) |
| `ixunzi://handwriting` | Handwriting search (`handwrite`; iOS) |
| `ixunzi://mastered` | 마스터 (`progress`) |
| `ixunzi://categories` / `ixunzi://categories?section=` | 둘러보기 |
| `ixunzi://collection?id=` | 컬렉션 / 책 |
| `ixunzi://corpus` | 모든 통행 (`all`) |
| `ixunzi://last-read` | 마지막으로 읽은 항목 |
| `ixunzi://reading-history` | 읽기 기록 |
| `ixunzi://notes` | 메모 |
| `ixunzi://ask` | Xunzi 소개 |
| `ixunzi://fables` / `ixunzi://allegories` / `ixunzi://concepts` | 사용할 때 특수 선반 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `ixunzi://settings` | 설정 |
| `ixunzi://usage-guide` | 사용 가이드 |
| `ixunzi://widget-guide` | 위젯 가이드 |
| `ixunzi://shortcuts-guide` | 단축어 가이드 |
| `ixunzi://feature-guide` | 온보딩 다시 보기 |
| `ixunzi://feedback` | 피드백 이메일 |
| `ixunzi://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
ixunzi://daily
ixunzi://passage?id=1
ixunzi://ask
ixunzi://study
ixunzi://hunt
```

</section>
<section lang="ru" markdown="1">

iXunZi поддерживает ярлыки ** `ixunzi://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
ixunzi://{host}?{params}
```


## Проходы и авторы

| URL | Открывает |
|-----|-------|
| `ixunzi://passage?id={id}` | Страница отрывка |
| `ixunzi://saying?id={id}` / `ixunzi://couplet?id={id}` / `ixunzi://poem?id={id}` | Совместимость (Compatibility) |
| `ixunzi://passage?id={id}&card=1` | Детали проезда и карточный лист |
| `ixunzi://card?id={id}` / `ixunzi://share-card?id={id}` | карты |
| `ixunzi://author?id={id}` | Страница автора |
| `ixunzi://recite` / `ixunzi://recite?id={id}` | Режим чтения вслух |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `ixunzi://home` | Главная |
| `ixunzi://daily` | Ежедневный Сун |
| `ixunzi://random` | Случайный отрывок |
| `ixunzi://favorites` | Избранное |
| `ixunzi://famous` | Знаменитые строки |
| `ixunzi://search` / `ixunzi://search?q={query}` | Поиск |
| `ixunzi://study` / `ixunzi://study?id={id}` | Поощрение Академии обучения |
| `ixunzi://hunt` | Xun Hunt («охота за ключевыми словами» / «флайфлауэр») |
| `ixunzi://handwriting` | Поиск почерка («handwrite»; iOS) |
| `ixunzi://mastered` | Мастеринг («Прогресс») |
| `ixunzi://categories` / `ixunzi://categories?section=` | Обзор |
| `ixunzi://collection?id=` | Коллекция / книга |
| `ixunzi://corpus` | Все пассажи («All») |
| `ixunzi://last-read` | Последнее прочитанное |
| `ixunzi://reading-history` | История чтения |
| `ixunzi://notes` | Заметки |
| `ixunzi://ask` | Спроси у Ксунзи. |
| `ixunzi://fables` / `ixunzi://allegories` / `ixunzi://concepts` | Специальные полки, когда они доступны |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `ixunzi://settings` | Настройки |
| `ixunzi://usage-guide` | Руководство по использованию |
| `ixunzi://widget-guide` | Руководство по виджетам |
| `ixunzi://shortcuts-guide` | Руководство по «Командам» |
| `ixunzi://feature-guide` | Повторное знакомство |
| `ixunzi://feedback` | Письмо с отзывом |
| `ixunzi://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
ixunzi://daily
ixunzi://passage?id=1
ixunzi://ask
ixunzi://study
ixunzi://hunt
```

</section>
<section lang="th" markdown="1">

IXunZi รองรับ~ `ixunzi://` BAR * ลิงก์ลัด (URL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
ixunzi://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `ixunzi://passage?id={id}` | รายละเอียดข้อความ |
| `ixunzi://saying?id={id}` / `ixunzi://couplet?id={id}` / `ixunzi://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `ixunzi://passage?id={id}&card=1` | รายละเอียดและนามบัตร |
| `ixunzi://card?id={id}` / `ixunzi://share-card?id={id}` | ○ การ์ด |
| `ixunzi://author?id={id}` | รายละเอียดผู้แต่ง |
| `ixunzi://recite` / `ixunzi://recite?id={id}` | โฟลว์การท่อง |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `ixunzi://home` | หน้าแรก |
| `ixunzi://daily` | Name=หน้าต่างComment |
| `ixunzi://random` | ข้อความแบบสุ่ม |
| `ixunzi://favorites` | รายการโปรด |
| `ixunzi://famous` | บรรทัดขึ้นชื่อ |
| `ixunzi://search` / `ixunzi://search?q={query}` | ค้นหา |
| `ixunzi://study` / `ixunzi://study?id={id}` | โรงเรียนเพื่อส่งเสริมการเรียนรู้ |
| `ixunzi://hunt` | Sun Hunt ('คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน') |
| `ixunzi://handwriting` | สืบค้นเมื่อเขียนด้วยมือ ('เขียนเอง'; OS) |
| `ixunzi://mastered` | สําเร็จการศึกษาแล้ว ('รุก') |
| `ixunzi://categories` / `ixunzi://categories?section=` | เรียกดู |
| `ixunzi://collection?id=` | ชุดสะสม / หนังสือ |
| `ixunzi://corpus` | ทุกช่อง (ทั้งหมด) |
| `ixunzi://last-read` | รายการที่อ่านล่าสุด |
| `ixunzi://reading-history` | ประวัติการอ่าน |
| `ixunzi://notes` | บันทึก |
| `ixunzi://ask` | ถาม Xunzi |
| `ixunzi://fables` / `ixunzi://allegories` / `ixunzi://concepts` | ชั้นวางพิเศษเมื่อมี |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `ixunzi://settings` | การตั้งค่า |
| `ixunzi://usage-guide` | คู่มือการใช้งาน |
| `ixunzi://widget-guide` | คู่มือวิดเจ็ต |
| `ixunzi://shortcuts-guide` | คู่มือทางลัด |
| `ixunzi://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `ixunzi://feedback` | อีเมลข้อเสนอแนะ |
| `ixunzi://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
ixunzi://daily
ixunzi://passage?id=1
ixunzi://ask
ixunzi://study
ixunzi://hunt
```

</section>
<section lang="de" markdown="1">

iXunZi unterstützt ** `ixunzi://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
ixunzi://{host}?{params}
```


## Passagen & Autoren

| URL | Öffnet |
|-----|-------|
| `ixunzi://passage?id={id}` | Passagen-Detail |
| `ixunzi://saying?id={id}` / `ixunzi://couplet?id={id}` / `ixunzi://poem?id={id}` | Wie Passage (Kompatibilität) |
| `ixunzi://passage?id={id}&card=1` | Angaben zum Durchgang und Kartenblatt |
| `ixunzi://card?id={id}` / `ixunzi://share-card?id={id}` | 荀 Karten |
| `ixunzi://author?id={id}` | Autorendetail |
| `ixunzi://recite` / `ixunzi://recite?id={id}` | Rezitationsablauf |

## Entdeckung und Praxis

| URL | Öffnet |
|-----|-------|
| `ixunzi://home` | Startseite |
| `ixunzi://daily` | Tägliche Xun |
| `ixunzi://random` | Zufällige Passage |
| `ixunzi://favorites` | Favoriten |
| `ixunzi://famous` | Berühmte Zeilen |
| `ixunzi://search` / `ixunzi://search?q={query}` | Suche |
| `ixunzi://study` / `ixunzi://study?id={id}` | Lernakademie fördern |
| `ixunzi://hunt` | Xun Hunt (`keyword-hunt` / `flyflower`) |
| `ixunzi://handwriting` | Handschriftsuche (`handwrite`; iOS) |
| `ixunzi://mastered` | gemeistert („Fortschritt) |
| `ixunzi://categories` / `ixunzi://categories?section=` | Durchsuchen |
| `ixunzi://collection?id=` | Sammlung/Buch |
| `ixunzi://corpus` | Alle Passagen (`all`) |
| `ixunzi://last-read` | Zuletzt gelesen |
| `ixunzi://reading-history` | Leseverlauf |
| `ixunzi://notes` | Notizen |
| `ixunzi://ask` | Fragen Sie Xunzi |
| `ixunzi://fables` / `ixunzi://allegories` / `ixunzi://concepts` | Spezialregale, wenn verfügbar |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `ixunzi://settings` | Einstellungen |
| `ixunzi://usage-guide` | Nutzungsanleitung |
| `ixunzi://widget-guide` | Widget-Anleitung |
| `ixunzi://shortcuts-guide` | Kurzbefehle-Anleitung |
| `ixunzi://feature-guide` | Einführung erneut abspielen |
| `ixunzi://feedback` | Feedback-E-Mail |
| `ixunzi://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
ixunzi://daily
ixunzi://passage?id=1
ixunzi://ask
ixunzi://study
ixunzi://hunt
```

</section>
<section lang="fr" markdown="1">

iXunZi prend en charge les liens de raccourci ** `ixunzi://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
ixunzi://{host}?{params}
```


## Passages et auteurs

| URL | Ouvre |
|-----|-------|
| `ixunzi://passage?id={id}` | Détail du passage |
| `ixunzi://saying?id={id}` / `ixunzi://couplet?id={id}` / `ixunzi://poem?id={id}` | Même chose que le passage (compatibilité) |
| `ixunzi://passage?id={id}&card=1` | Détails du passage et feuille de carte |
| `ixunzi://card?id={id}` / `ixunzi://share-card?id={id}` | Cartes |
| `ixunzi://author?id={id}` | Détail de l’auteur |
| `ixunzi://recite` / `ixunzi://recite?id={id}` | Flux de récitation |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `ixunzi://home` | Accueil |
| `ixunzi://daily` | Xun quotidien |
| `ixunzi://random` | Passage aléatoire |
| `ixunzi://favorites` | Favoris |
| `ixunzi://famous` | Vers célèbres |
| `ixunzi://search` / `ixunzi://search?q={query}` | Recherche |
| `ixunzi://study` / `ixunzi://study?id={id}` | Encourager l'Académie d'apprentissage |
| `ixunzi://hunt` | Xun Hunt ( ' chasse aux mots clés ' / ' flyflower ') |
| `ixunzi://handwriting` | Recherche d'écriture (`handwrite`; iOS) |
| `ixunzi://mastered` | Maîtrise ('progrès') |
| `ixunzi://categories` / `ixunzi://categories?section=` | Parcourir |
| `ixunzi://collection?id=` | Collection / livre |
| `ixunzi://corpus` | Tous les passages |
| `ixunzi://last-read` | Dernière lecture |
| `ixunzi://reading-history` | Historique de lecture |
| `ixunzi://notes` | Notes |
| `ixunzi://ask` | Demandez à Xunzi |
| `ixunzi://fables` / `ixunzi://allegories` / `ixunzi://concepts` | Étagères spéciales lorsque disponibles |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `ixunzi://settings` | Réglages |
| `ixunzi://usage-guide` | Guide d'utilisation |
| `ixunzi://widget-guide` | Guide des widgets |
| `ixunzi://shortcuts-guide` | Guide Raccourcis |
| `ixunzi://feature-guide` | Rejouer l’accueil |
| `ixunzi://feedback` | E-mail de commentaires |
| `ixunzi://in-app-review` | Avis in-app / App Store |

## Exemples


```
ixunzi://daily
ixunzi://passage?id=1
ixunzi://ask
ixunzi://study
ixunzi://hunt
```

</section>
<section lang="tr" markdown="1">

iXunZi, ** `ixunzi://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
ixunzi://{host}?{params}
```


## Geçişler ve yazarlar

| URL | Açar |
|-----|-------|
| `ixunzi://passage?id={id}` | Pasaj ayrıntısı |
| `ixunzi://saying?id={id}` / `ixunzi://couplet?id={id}` / `ixunzi://poem?id={id}` | Aynı geçiş (compatability) |
| `ixunzi://passage?id={id}&card=1` | Pasaj detay ve kart sayfası |
| `ixunzi://card?id={id}` / `ixunzi://share-card?id={id}` | kartları |
| `ixunzi://author?id={id}` | Yazar ayrıntısı |
| `ixunzi://recite` / `ixunzi://recite?id={id}` | Okuma akışı |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `ixunzi://home` | Ana sayfa |
| `ixunzi://daily` | Daily Xun |
| `ixunzi://random` | Rastgele pasaj |
| `ixunzi://favorites` | Favoriler |
| `ixunzi://famous` | Ünlü dizeler |
| `ixunzi://search` / `ixunzi://search?q={query}` | Ara |
| `ixunzi://study` / `ixunzi://study?id={id}` | Öğrenme Akademisi |
| `ixunzi://hunt` | Xun Hunt ('keyword-hunt' / 'flyflower') |
| `ixunzi://handwriting` | Hand writing search ('handwrite'; iOS) |
| `ixunzi://mastered` | Mastered ('progress') |
| `ixunzi://categories` / `ixunzi://categories?section=` | Gözat |
| `ixunzi://collection?id=` | Koleksiyon / kitap |
| `ixunzi://corpus` | Bütün geçitler ('all') |
| `ixunzi://last-read` | Son okunan |
| `ixunzi://reading-history` | Okuma geçmişi |
| `ixunzi://notes` | Notlar |
| `ixunzi://ask` | Xunzi |
| `ixunzi://fables` / `ixunzi://allegories` / `ixunzi://concepts` | Mevcut özel raflar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `ixunzi://settings` | Ayarlar |
| `ixunzi://usage-guide` | Kullanım kılavuzu |
| `ixunzi://widget-guide` | Widget kılavuzu |
| `ixunzi://shortcuts-guide` | Kısayol kılavuzu |
| `ixunzi://feature-guide` | Tanıtımı yeniden oynat |
| `ixunzi://feedback` | Geri bildirim e-postası |
| `ixunzi://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
ixunzi://daily
ixunzi://passage?id=1
ixunzi://ask
ixunzi://study
ixunzi://hunt
```

</section>
