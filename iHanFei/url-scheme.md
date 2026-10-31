---
layout: doc
title: iHanFei — Shortcut Links
app_id: iHanFei
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: ihanfei:// deep links for iHanFei — passage, daily, recite, study, hunt, settings guides, and more.
---

<section lang="en" markdown="1">

iHanFei supports **`ihanfei://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
ihanfei://{host}?{params}
```

## Passages & authors

| URL | Opens |
|-----|-------|
| `ihanfei://passage?id={id}` | Passage detail |
| `ihanfei://saying?id={id}` / `ihanfei://couplet?id={id}` / `ihanfei://poem?id={id}` | Same as passage (compatibility) |
| `ihanfei://passage?id={id}&card=1` | Passage detail and card sheet |
| `ihanfei://card?id={id}` / `ihanfei://share-card?id={id}` | 法 cards |
| `ihanfei://author?id={id}` | Author detail |
| `ihanfei://recite` / `ihanfei://recite?id={id}` | Recite flow |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `ihanfei://home` | Home |
| `ihanfei://daily` | Daily Stratagem |
| `ihanfei://random` | Random passage |
| `ihanfei://favorites` | Favorites |
| `ihanfei://famous` | Famous lines |
| `ihanfei://search` / `ihanfei://search?q={query}` | Search |
| `ihanfei://study` / `ihanfei://study?id={id}` | Legalism Study |
| `ihanfei://hunt` | Law Hunt (`keyword-hunt` / `flyflower`) |
| `ihanfei://handwriting` | Handwriting search (`handwrite`; iOS) |
| `ihanfei://mastered` | Mastered (`progress`) |
| `ihanfei://categories` / `ihanfei://categories?section=` | Browse |
| `ihanfei://collection?id=` | Collection / book |
| `ihanfei://corpus` | All passages (`all`) |
| `ihanfei://last-read` | Last read |
| `ihanfei://reading-history` | Reading history |
| `ihanfei://notes` | Notes |
| `ihanfei://fables` / `ihanfei://allegories` / `ihanfei://concepts` | Specialty shelves when available |

## Settings & guides

| URL | Opens |
|-----|-------|
| `ihanfei://settings` | Settings |
| `ihanfei://usage-guide` | Usage guide |
| `ihanfei://widget-guide` | Widget guide |
| `ihanfei://shortcuts-guide` | Shortcuts guide |
| `ihanfei://feature-guide` | Replay onboarding |
| `ihanfei://feedback` | Feedback email |
| `ihanfei://in-app-review` | In-app / Store review entry |

## Examples

```
ihanfei://daily
ihanfei://passage?id=1
ihanfei://study
ihanfei://hunt
```

</section>
<section lang="zh-CN" markdown="1">

爱韩非子 支持 **`ihanfei://`** 快捷链接（URL Scheme）。冷启动与主屏幕快捷方式经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
ihanfei://{host}?{params}
```

## 篇目与作者

| URL | 打开 |
|-----|------|
| `ihanfei://passage?id={id}` | 篇目详情 |
| `ihanfei://saying?id={id}` / `ihanfei://couplet?id={id}` / `ihanfei://poem?id={id}` | 同 passage（兼容） |
| `ihanfei://passage?id={id}&card=1` | 篇目详情并打开分享卡 |
| `ihanfei://card?id={id}` / `ihanfei://share-card?id={id}` | 法卡 |
| `ihanfei://author?id={id}` | 作者详情 |
| `ihanfei://recite` / `ihanfei://recite?id={id}` | 诵读 |

## 发现与练习

| URL | 打开 |
|-----|------|
| `ihanfei://home` | 首页 |
| `ihanfei://daily` | 每日一法 |
| `ihanfei://random` | 随机一篇 |
| `ihanfei://favorites` | 收藏 |
| `ihanfei://famous` | 名句 |
| `ihanfei://search` / `ihanfei://search?q={query}` | 搜索 |
| `ihanfei://study` / `ihanfei://study?id={id}` | 法家学堂 |
| `ihanfei://hunt` | 寻法（`keyword-hunt` / `flyflower`） |
| `ihanfei://handwriting` | 手写寻句（`handwrite`；iOS） |
| `ihanfei://mastered` | 已掌握（`progress`） |
| `ihanfei://categories` / `ihanfei://categories?section=` | 浏览 |
| `ihanfei://collection?id=` | 合集／分册 |
| `ihanfei://corpus` | 全部篇目（`all`） |
| `ihanfei://last-read` | 上次阅读 |
| `ihanfei://reading-history` | 阅读历史 |
| `ihanfei://notes` | 笔记 |
| `ihanfei://fables` / `ihanfei://allegories` / `ihanfei://concepts` | 专属书架（如有） |

## 设置与指南

| URL | 打开 |
|-----|------|
| `ihanfei://settings` | 设置 |
| `ihanfei://usage-guide` | 使用说明 |
| `ihanfei://widget-guide` | 小组件说明 |
| `ihanfei://shortcuts-guide` | 快捷指令说明 |
| `ihanfei://feature-guide` | 重看功能导览 |
| `ihanfei://feedback` | 反馈邮件 |
| `ihanfei://in-app-review` | 应用内／商店评价入口 |

## 示例

```
ihanfei://daily
ihanfei://passage?id=1
ihanfei://study
ihanfei://hunt
```

</section>
<section lang="zh-TW" markdown="1">

愛韓非子 支援 **`ihanfei://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複打開。

## 連結格式

```
ihanfei://{host}?{params}
```

## 篇目與作者

| URL | 打開 |
|-----|------|
| `ihanfei://passage?id={id}` | 篇目詳情 |
| `ihanfei://saying?id={id}` / `ihanfei://couplet?id={id}` / `ihanfei://poem?id={id}` | 同 passage（相容） |
| `ihanfei://passage?id={id}&card=1` | 篇目詳情並打開分享卡 |
| `ihanfei://card?id={id}` / `ihanfei://share-card?id={id}` | 法卡 |
| `ihanfei://author?id={id}` | 作者詳情 |
| `ihanfei://recite` / `ihanfei://recite?id={id}` | 誦讀 |

## 探索與練習

| URL | 打開 |
|-----|------|
| `ihanfei://home` | 首頁 |
| `ihanfei://daily` | 每日一法 |
| `ihanfei://random` | 隨機一篇 |
| `ihanfei://favorites` | 收藏 |
| `ihanfei://famous` | 名句 |
| `ihanfei://search` / `ihanfei://search?q={query}` | 搜尋 |
| `ihanfei://study` / `ihanfei://study?id={id}` | 法家學堂 |
| `ihanfei://hunt` | 尋法（`keyword-hunt` / `flyflower`） |
| `ihanfei://handwriting` | 手寫尋句（`handwrite`；iOS） |
| `ihanfei://mastered` | 已掌握（`progress`） |
| `ihanfei://categories` / `ihanfei://categories?section=` | 瀏覽 |
| `ihanfei://collection?id=` | 合集／分冊 |
| `ihanfei://corpus` | 全部篇目（`all`） |
| `ihanfei://last-read` | 上次閱讀 |
| `ihanfei://reading-history` | 閱讀歷史 |
| `ihanfei://notes` | 筆記 |
| `ihanfei://fables` / `ihanfei://allegories` / `ihanfei://concepts` | 專屬書架（如有） |

## 設定與指南

| URL | 打開 |
|-----|------|
| `ihanfei://settings` | 設定 |
| `ihanfei://usage-guide` | 使用說明 |
| `ihanfei://widget-guide` | 小工具說明 |
| `ihanfei://shortcuts-guide` | 捷徑說明 |
| `ihanfei://feature-guide` | 重看功能導覽 |
| `ihanfei://feedback` | 回饋郵件 |
| `ihanfei://in-app-review` | 應用內／商店評價入口 |

## 範例

```
ihanfei://daily
ihanfei://passage?id=1
ihanfei://study
ihanfei://hunt
```

</section>
<section lang="ja" markdown="1">

iHanFeiは、** `ihanfei://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
ihanfei://{host}?{params}
```


## パスポートと著者

| URL | 開く画面 |
|-----|-------|
| `ihanfei://passage?id={id}` | 章句の詳細 |
| `ihanfei://saying?id={id}` / `ihanfei://couplet?id={id}` / `ihanfei://poem?id={id}` | 通路と同じ(互換性) |
| `ihanfei://passage?id={id}&card=1` | 通路の細部およびカード シート |
| `ihanfei://card?id={id}` / `ihanfei://share-card?id={id}` | 法カード |
| `ihanfei://author?id={id}` | 作者の詳細 |
| `ihanfei://recite` / `ihanfei://recite?id={id}` | 誦読フロー |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `ihanfei://home` | ホーム |
| `ihanfei://daily` | デイリー・ストラテジーム |
| `ihanfei://random` | ランダムな章句 |
| `ihanfei://favorites` | お気に入り |
| `ihanfei://famous` | 名句一覧 |
| `ihanfei://search` / `ihanfei://search?q={query}` | 検索 |
| `ihanfei://study` / `ihanfei://study?id={id}` | 法律学研究 |
| `ihanfei://hunt` | 法ハント (`keyword-hunt`/`flyflower`) |
| `ihanfei://handwriting` | 手書き検索 (`handwrite`; iOS) |
| `ihanfei://mastered` | マスタード (`progress`) |
| `ihanfei://categories` / `ihanfei://categories?section=` | ブラウズ |
| `ihanfei://collection?id=` | コレクション/書籍 |
| `ihanfei://corpus` | すべての通路 (`all`) |
| `ihanfei://last-read` | 最後に読んだ項目 |
| `ihanfei://reading-history` | 閲覧履歴 |
| `ihanfei://notes` | ノート |
| `ihanfei://fables` / `ihanfei://allegories` / `ihanfei://concepts` | 利用できる場合の特別な棚 |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `ihanfei://settings` | 設定 |
| `ihanfei://usage-guide` | 使い方ガイド |
| `ihanfei://widget-guide` | ウィジェットガイド |
| `ihanfei://shortcuts-guide` | ショートカットガイド |
| `ihanfei://feature-guide` | オンボーディングの再生 |
| `ihanfei://feedback` | フィードバックメール |
| `ihanfei://in-app-review` | アプリ内／App Store レビュー |

## 例


```
ihanfei://daily
ihanfei://passage?id=1
ihanfei://study
ihanfei://hunt
```

</section>
<section lang="ko" markdown="1">

iHanFei 지원 ** `ihanfei://` ** 단축키 링크 (URL 계획). 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
ihanfei://{host}?{params}
```


## 책임 & 저자

| URL | 열리는 화면 |
|-----|-------|
| `ihanfei://passage?id={id}` | 구절 상세 |
| `ihanfei://saying?id={id}` / `ihanfei://couplet?id={id}` / `ihanfei://poem?id={id}` | 통행과 같 ( 겸용성) |
| `ihanfei://passage?id={id}&card=1` | 통행 세부사항과 카드 장 |
| `ihanfei://card?id={id}` / `ihanfei://share-card?id={id}` | 카드 카드 |
| `ihanfei://author?id={id}` | 작가 상세 |
| `ihanfei://recite` / `ihanfei://recite?id={id}` | 낭독 흐름 |

## 디스커버리 & 연습

| URL | 열리는 화면 |
|-----|-------|
| `ihanfei://home` | 홈 |
| `ihanfei://daily` | 매일 Stratagem |
| `ihanfei://random` | 무작위 구절 |
| `ihanfei://favorites` | 즐겨찾기 |
| `ihanfei://famous` | 명구 목록 |
| `ihanfei://search` / `ihanfei://search?q={query}` | 검색 |
| `ihanfei://study` / `ihanfei://study?id={id}` | 법률 연구 |
| `ihanfei://hunt` | 헌트 (`keyword-hunt`/`flyflower`) |
| `ihanfei://handwriting` | Handwriting search (`handwrite`; iOS) |
| `ihanfei://mastered` | 마스터 (`progress`) |
| `ihanfei://categories` / `ihanfei://categories?section=` | 둘러보기 |
| `ihanfei://collection?id=` | 컬렉션 / 책 |
| `ihanfei://corpus` | 모든 통행 (`all`) |
| `ihanfei://last-read` | 마지막으로 읽은 항목 |
| `ihanfei://reading-history` | 읽기 기록 |
| `ihanfei://notes` | 메모 |
| `ihanfei://fables` / `ihanfei://allegories` / `ihanfei://concepts` | 사용할 때 특수 선반 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `ihanfei://settings` | 설정 |
| `ihanfei://usage-guide` | 사용 가이드 |
| `ihanfei://widget-guide` | 위젯 가이드 |
| `ihanfei://shortcuts-guide` | 단축어 가이드 |
| `ihanfei://feature-guide` | 온보딩 다시 보기 |
| `ihanfei://feedback` | 피드백 이메일 |
| `ihanfei://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
ihanfei://daily
ihanfei://passage?id=1
ihanfei://study
ihanfei://hunt
```

</section>
<section lang="ru" markdown="1">

iHanFei поддерживает ярлыки ** `ihanfei://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
ihanfei://{host}?{params}
```


## Проходы и авторы

| URL | Открывает |
|-----|-------|
| `ihanfei://passage?id={id}` | Страница отрывка |
| `ihanfei://saying?id={id}` / `ihanfei://couplet?id={id}` / `ihanfei://poem?id={id}` | Совместимость (Compatibility) |
| `ihanfei://passage?id={id}&card=1` | Детали проезда и карточный лист |
| `ihanfei://card?id={id}` / `ihanfei://share-card?id={id}` | карточки |
| `ihanfei://author?id={id}` | Страница автора |
| `ihanfei://recite` / `ihanfei://recite?id={id}` | Режим чтения вслух |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `ihanfei://home` | Главная |
| `ihanfei://daily` | Daily Stratagem |
| `ihanfei://random` | Случайный отрывок |
| `ihanfei://favorites` | Избранное |
| `ihanfei://famous` | Знаменитые строки |
| `ihanfei://search` / `ihanfei://search?q={query}` | Поиск |
| `ihanfei://study` / `ihanfei://study?id={id}` | Исследование легализма |
| `ihanfei://hunt` | «Охота за ключевыми словами» / «Flyflower» |
| `ihanfei://handwriting` | Поиск почерка («handwrite»; iOS) |
| `ihanfei://mastered` | Мастеринг («Прогресс») |
| `ihanfei://categories` / `ihanfei://categories?section=` | Обзор |
| `ihanfei://collection?id=` | Коллекция / книга |
| `ihanfei://corpus` | Все пассажи («All») |
| `ihanfei://last-read` | Последнее прочитанное |
| `ihanfei://reading-history` | История чтения |
| `ihanfei://notes` | Заметки |
| `ihanfei://fables` / `ihanfei://allegories` / `ihanfei://concepts` | Специальные полки, когда они доступны |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `ihanfei://settings` | Настройки |
| `ihanfei://usage-guide` | Руководство по использованию |
| `ihanfei://widget-guide` | Руководство по виджетам |
| `ihanfei://shortcuts-guide` | Руководство по «Командам» |
| `ihanfei://feature-guide` | Повторное знакомство |
| `ihanfei://feedback` | Письмо с отзывом |
| `ihanfei://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
ihanfei://daily
ihanfei://passage?id=1
ihanfei://study
ihanfei://hunt
```

</section>
<section lang="th" markdown="1">

iHanfai สนับสนุน~ `ihanfei://` BAR * ลิงก์ลัด (URL scheme). การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
ihanfei://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `ihanfei://passage?id={id}` | รายละเอียดข้อความ |
| `ihanfei://saying?id={id}` / `ihanfei://couplet?id={id}` / `ihanfei://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `ihanfei://passage?id={id}&card=1` | รายละเอียดและนามบัตร |
| `ihanfei://card?id={id}` / `ihanfei://share-card?id={id}` | ○ การ์ด |
| `ihanfei://author?id={id}` | รายละเอียดผู้แต่ง |
| `ihanfei://recite` / `ihanfei://recite?id={id}` | โฟลว์การท่อง |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `ihanfei://home` | หน้าแรก |
| `ihanfei://daily` | ตารางเวลาประจําวัน |
| `ihanfei://random` | ข้อความแบบสุ่ม |
| `ihanfei://favorites` | รายการโปรด |
| `ihanfei://famous` | บรรทัดขึ้นชื่อ |
| `ihanfei://search` / `ihanfei://search?q={query}` | ค้นหา |
| `ihanfei://study` / `ihanfei://study?id={id}` | การ ศึกษา ด้าน กฎหมาย |
| `ihanfei://hunt` | Law Hunt ('คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน') |
| `ihanfei://handwriting` | สืบค้นเมื่อเขียนด้วยมือ ('เขียนเอง'; OS) |
| `ihanfei://mastered` | สําเร็จการศึกษาแล้ว ('รุก') |
| `ihanfei://categories` / `ihanfei://categories?section=` | เรียกดู |
| `ihanfei://collection?id=` | ชุดสะสม / หนังสือ |
| `ihanfei://corpus` | ทุกช่อง (ทั้งหมด) |
| `ihanfei://last-read` | รายการที่อ่านล่าสุด |
| `ihanfei://reading-history` | ประวัติการอ่าน |
| `ihanfei://notes` | บันทึก |
| `ihanfei://fables` / `ihanfei://allegories` / `ihanfei://concepts` | ชั้นวางพิเศษเมื่อมี |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `ihanfei://settings` | การตั้งค่า |
| `ihanfei://usage-guide` | คู่มือการใช้งาน |
| `ihanfei://widget-guide` | คู่มือวิดเจ็ต |
| `ihanfei://shortcuts-guide` | คู่มือทางลัด |
| `ihanfei://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `ihanfei://feedback` | อีเมลข้อเสนอแนะ |
| `ihanfei://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
ihanfei://daily
ihanfei://passage?id=1
ihanfei://study
ihanfei://hunt
```

</section>
<section lang="de" markdown="1">

iHanFei unterstützt ** `ihanfei://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
ihanfei://{host}?{params}
```


## Passagen & Autoren

| URL | Öffnet |
|-----|-------|
| `ihanfei://passage?id={id}` | Passagen-Detail |
| `ihanfei://saying?id={id}` / `ihanfei://couplet?id={id}` / `ihanfei://poem?id={id}` | Wie Passage (Kompatibilität) |
| `ihanfei://passage?id={id}&card=1` | Angaben zum Durchgang und Kartenblatt |
| `ihanfei://card?id={id}` / `ihanfei://share-card?id={id}` | Σ Karten |
| `ihanfei://author?id={id}` | Autorendetail |
| `ihanfei://recite` / `ihanfei://recite?id={id}` | Rezitationsablauf |

## Entdeckung und Praxis

| URL | Öffnet |
|-----|-------|
| `ihanfei://home` | Startseite |
| `ihanfei://daily` | Tägliche Stratagem |
| `ihanfei://random` | Zufällige Passage |
| `ihanfei://favorites` | Favoriten |
| `ihanfei://famous` | Berühmte Zeilen |
| `ihanfei://search` / `ihanfei://search?q={query}` | Suche |
| `ihanfei://study` / `ihanfei://study?id={id}` | Legalismusstudie |
| `ihanfei://hunt` | Law Hunt (`keyword-hunt` / `flyflower`) |
| `ihanfei://handwriting` | Handschriftsuche (`handwrite`; iOS) |
| `ihanfei://mastered` | gemeistert („Fortschritt) |
| `ihanfei://categories` / `ihanfei://categories?section=` | Durchsuchen |
| `ihanfei://collection?id=` | Sammlung/Buch |
| `ihanfei://corpus` | Alle Passagen (`all`) |
| `ihanfei://last-read` | Zuletzt gelesen |
| `ihanfei://reading-history` | Leseverlauf |
| `ihanfei://notes` | Notizen |
| `ihanfei://fables` / `ihanfei://allegories` / `ihanfei://concepts` | Spezialregale, wenn verfügbar |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `ihanfei://settings` | Einstellungen |
| `ihanfei://usage-guide` | Nutzungsanleitung |
| `ihanfei://widget-guide` | Widget-Anleitung |
| `ihanfei://shortcuts-guide` | Kurzbefehle-Anleitung |
| `ihanfei://feature-guide` | Einführung erneut abspielen |
| `ihanfei://feedback` | Feedback-E-Mail |
| `ihanfei://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
ihanfei://daily
ihanfei://passage?id=1
ihanfei://study
ihanfei://hunt
```

</section>
<section lang="fr" markdown="1">

iHanFei prend en charge les liens de raccourci ** `ihanfei://` ** (système URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
ihanfei://{host}?{params}
```


## Passages et auteurs

| URL | Ouvre |
|-----|-------|
| `ihanfei://passage?id={id}` | Détail du passage |
| `ihanfei://saying?id={id}` / `ihanfei://couplet?id={id}` / `ihanfei://poem?id={id}` | Même chose que le passage (compatibilité) |
| `ihanfei://passage?id={id}&card=1` | Détails du passage et feuille de carte |
| `ihanfei://card?id={id}` / `ihanfei://share-card?id={id}` | Cartes |
| `ihanfei://author?id={id}` | Détail de l’auteur |
| `ihanfei://recite` / `ihanfei://recite?id={id}` | Flux de récitation |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `ihanfei://home` | Accueil |
| `ihanfei://daily` | Stratagème quotidien |
| `ihanfei://random` | Passage aléatoire |
| `ihanfei://favorites` | Favoris |
| `ihanfei://famous` | Vers célèbres |
| `ihanfei://search` / `ihanfei://search?q={query}` | Recherche |
| `ihanfei://study` / `ihanfei://study?id={id}` | Étude sur le légalisme |
| `ihanfei://hunt` | Chasse aux lois ( ' chasse aux mots clés ' / `flyflower ') |
| `ihanfei://handwriting` | Recherche d'écriture (`handwrite`; iOS) |
| `ihanfei://mastered` | Maîtrise ('progrès') |
| `ihanfei://categories` / `ihanfei://categories?section=` | Parcourir |
| `ihanfei://collection?id=` | Collection / livre |
| `ihanfei://corpus` | Tous les passages |
| `ihanfei://last-read` | Dernière lecture |
| `ihanfei://reading-history` | Historique de lecture |
| `ihanfei://notes` | Notes |
| `ihanfei://fables` / `ihanfei://allegories` / `ihanfei://concepts` | Étagères spéciales lorsque disponibles |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `ihanfei://settings` | Réglages |
| `ihanfei://usage-guide` | Guide d'utilisation |
| `ihanfei://widget-guide` | Guide des widgets |
| `ihanfei://shortcuts-guide` | Guide Raccourcis |
| `ihanfei://feature-guide` | Rejouer l’accueil |
| `ihanfei://feedback` | E-mail de commentaires |
| `ihanfei://in-app-review` | Avis in-app / App Store |

## Exemples


```
ihanfei://daily
ihanfei://passage?id=1
ihanfei://study
ihanfei://hunt
```

</section>
<section lang="tr" markdown="1">

iHanFei, ** `ihanfei://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
ihanfei://{host}?{params}
```


## Geçişler ve yazarlar

| URL | Açar |
|-----|-------|
| `ihanfei://passage?id={id}` | Pasaj ayrıntısı |
| `ihanfei://saying?id={id}` / `ihanfei://couplet?id={id}` / `ihanfei://poem?id={id}` | Aynı geçiş (compatability) |
| `ihanfei://passage?id={id}&card=1` | Pasaj detay ve kart sayfası |
| `ihanfei://card?id={id}` / `ihanfei://share-card?id={id}` | kartları |
| `ihanfei://author?id={id}` | Yazar ayrıntısı |
| `ihanfei://recite` / `ihanfei://recite?id={id}` | Okuma akışı |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `ihanfei://home` | Ana sayfa |
| `ihanfei://daily` | Daily Stratagem |
| `ihanfei://random` | Rastgele pasaj |
| `ihanfei://favorites` | Favoriler |
| `ihanfei://famous` | Ünlü dizeler |
| `ihanfei://search` / `ihanfei://search?q={query}` | Ara |
| `ihanfei://study` / `ihanfei://study?id={id}` | Yasallık Çalışması |
| `ihanfei://hunt` | Law Hunt ('keyword-hunt' / 'flyflower') |
| `ihanfei://handwriting` | Hand writing search ('handwrite'; iOS) |
| `ihanfei://mastered` | Mastered ('progress') |
| `ihanfei://categories` / `ihanfei://categories?section=` | Gözat |
| `ihanfei://collection?id=` | Koleksiyon / kitap |
| `ihanfei://corpus` | Bütün geçitler ('all') |
| `ihanfei://last-read` | Son okunan |
| `ihanfei://reading-history` | Okuma geçmişi |
| `ihanfei://notes` | Notlar |
| `ihanfei://fables` / `ihanfei://allegories` / `ihanfei://concepts` | Mevcut özel raflar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `ihanfei://settings` | Ayarlar |
| `ihanfei://usage-guide` | Kullanım kılavuzu |
| `ihanfei://widget-guide` | Widget kılavuzu |
| `ihanfei://shortcuts-guide` | Kısayol kılavuzu |
| `ihanfei://feature-guide` | Tanıtımı yeniden oynat |
| `ihanfei://feedback` | Geri bildirim e-postası |
| `ihanfei://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
ihanfei://daily
ihanfei://passage?id=1
ihanfei://study
ihanfei://hunt
```

</section>
