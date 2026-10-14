---
layout: doc
title: iSage — Shortcut Links
app_id: iSage
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: isage:// deep links for iSage — passage, daily, recite, study, hunt, collections, themes, settings guides, and more.
---

<section lang="en" markdown="1">

iSage supports **`isage://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
isage://{host}?{params}
```

## Sayings & authors

| URL | Opens |
|-----|-------|
| `isage://passage?id={id}` | Saying detail |
| `isage://saying?id={id}` / `isage://couplet?id={id}` / `isage://poem?id={id}` | Same as passage (compatibility) |
| `isage://passage?id={id}&card=1` | Saying detail and sage-card sheet |
| `isage://card?id={id}` / `isage://share-card?id={id}` | Sage card |
| `isage://author?id={id}` | Author detail |
| `isage://recite` / `isage://recite?id={id}` | Recite flow |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `isage://home` | Home |
| `isage://daily` | Today’s Wisdom |
| `isage://random` | Random saying |
| `isage://favorites` | Favorites |
| `isage://famous` | Famous lines |
| `isage://search` / `isage://search?q={query}` | Search |
| `isage://study` / `isage://study?id={id}` | Sage Academy |
| `isage://hunt` | Sage Hunt (`keyword-hunt` / `flyflower`) |
| `isage://handwriting` | Handwriting search (`handwrite`; iOS) |
| `isage://mastered` | Mastered (`progress`) |
| `isage://categories` / `isage://categories?section=` | Browse |
| `isage://collection?id=guxun` | Classic recension (`zhou-shang` / `zhou-xia`; also `book` / `form`) |
| `isage://corpus` | All sayings (`all`) |
| `isage://theme?id=conduct` | Theme (e.g. `cultivation`, `learning`, `friendship`, `household`, `wealth`, `virtue`, `fortune`, `speech`, `loyalty`, `diligence`, `world`) |
| `isage://last-read` | Last read |
| `isage://reading-history` | Reading history |
| `isage://notes` | Notes |

## Settings & guides

| URL | Opens |
|-----|-------|
| `isage://settings` | Settings |
| `isage://usage-guide` | Usage guide |
| `isage://widget-guide` | Widget guide |
| `isage://shortcuts-guide` | Shortcuts guide |
| `isage://feature-guide` | Replay onboarding |
| `isage://feedback` | Feedback email |
| `isage://in-app-review` | In-app / Store review entry |

## Examples

```
isage://daily
isage://passage?id=1
isage://passage?id=1&card=1
isage://collection?id=guxun
isage://theme?id=conduct
isage://study
isage://hunt
isage://handwriting
```

## Notes

- Parameters are case-sensitive where IDs are numeric.
- Siri, Shortcuts, widgets, and Control Center controls use the same deep-link routes.
- See the in-app **Settings → Help** guides for the latest list.

</section>
<section lang="zh-CN" markdown="1">

爱增广贤文支持 **`isage://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导页结束后重复打开。

## 链接格式

```
isage://{host}?{params}
```

## 贤句与作者

| URL | 打开 |
|-----|------|
| `isage://passage?id={id}` | 贤句详情 |
| `isage://saying?id={id}` / `isage://couplet?id={id}` / `isage://poem?id={id}` | 同详情（兼容别名） |
| `isage://passage?id={id}&card=1` | 详情并弹出贤卡 |
| `isage://card?id={id}` / `isage://share-card?id={id}` | 贤卡 |
| `isage://author?id={id}` | 作者详情 |
| `isage://recite` / `isage://recite?id={id}` | 诵读 |

## 发现与学堂

| URL | 打开 |
|-----|------|
| `isage://home` | 首页 |
| `isage://daily` | 今日一智 |
| `isage://random` | 随机贤句 |
| `isage://favorites` | 收藏 |
| `isage://famous` | 金句 |
| `isage://search` / `isage://search?q={query}` | 搜索 |
| `isage://study` / `isage://study?id={id}` | 贤文学堂 |
| `isage://hunt` | 寻贤（`keyword-hunt` / `flyflower`） |
| `isage://handwriting` | 手写寻贤（`handwrite`；iOS） |
| `isage://mastered` | 已掌握（`progress`） |
| `isage://categories` / `isage://categories?section=` | 分类浏览 |
| `isage://collection?id=guxun` | 古训增广（`zhou-shang` / `zhou-xia`；亦可用 `book` / `form`） |
| `isage://corpus` | 全部贤句（`all`） |
| `isage://theme?id=conduct` | 主题（如 `cultivation`、`learning`、`friendship`、`household`、`wealth`、`virtue`、`fortune`、`speech`、`loyalty`、`diligence`、`world`） |
| `isage://last-read` | 最近阅读 |
| `isage://reading-history` | 阅读历史 |
| `isage://notes` | 笔记 |

## 设置与指南

| URL | 打开 |
|-----|------|
| `isage://settings` | 设置 |
| `isage://usage-guide` | 使用说明 |
| `isage://widget-guide` | 小组件指南 |
| `isage://shortcuts-guide` | 快捷指南 |
| `isage://feature-guide` | 重播功能引导 |
| `isage://feedback` | 反馈邮件 |
| `isage://in-app-review` | 应用内评价入口 |

## 示例

```
isage://daily
isage://passage?id=1
isage://passage?id=1&card=1
isage://collection?id=guxun
isage://theme?id=conduct
isage://study
isage://hunt
isage://handwriting
```

## 说明

- 数字 ID 参数区分大小写。
- Siri、快捷指令、小组件与控制中心使用同一套深链。
- 最新列表见应用内 **设置 → 帮助**。

</section>
<section lang="zh-TW" markdown="1">

愛增廣賢文支援 **`isage://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導頁結束後重複打開。

## 連結格式

```
isage://{host}?{params}
```

## 賢句與作者

| URL | 打開 |
|-----|------|
| `isage://passage?id={id}` | 賢句詳情 |
| `isage://saying?id={id}` / `isage://couplet?id={id}` / `isage://poem?id={id}` | 同詳情（相容別名） |
| `isage://passage?id={id}&card=1` | 詳情並彈出賢卡 |
| `isage://card?id={id}` / `isage://share-card?id={id}` | 賢卡 |
| `isage://author?id={id}` | 作者詳情 |
| `isage://recite` / `isage://recite?id={id}` | 誦讀 |

## 發現與學堂

| URL | 打開 |
|-----|------|
| `isage://home` | 首頁 |
| `isage://daily` | 今日一智 |
| `isage://random` | 隨機賢句 |
| `isage://favorites` | 收藏 |
| `isage://famous` | 金句 |
| `isage://search` / `isage://search?q={query}` | 搜尋 |
| `isage://study` / `isage://study?id={id}` | 賢文學堂 |
| `isage://hunt` | 尋賢（`keyword-hunt` / `flyflower`） |
| `isage://handwriting` | 手寫尋賢（`handwrite`；iOS） |
| `isage://mastered` | 已掌握（`progress`） |
| `isage://categories` / `isage://categories?section=` | 分類瀏覽 |
| `isage://collection?id=guxun` | 古訓增廣（`zhou-shang` / `zhou-xia`；亦可用 `book` / `form`） |
| `isage://corpus` | 全部賢句（`all`） |
| `isage://theme?id=conduct` | 主題（如 `cultivation`、`learning`、`friendship`、`household`、`wealth`、`virtue`、`fortune`、`speech`、`loyalty`、`diligence`、`world`） |
| `isage://last-read` | 最近閱讀 |
| `isage://reading-history` | 閱讀歷史 |
| `isage://notes` | 筆記 |

## 設定與指南

| URL | 打開 |
|-----|------|
| `isage://settings` | 設定 |
| `isage://usage-guide` | 使用說明 |
| `isage://widget-guide` | 小工具指南 |
| `isage://shortcuts-guide` | 捷徑指南 |
| `isage://feature-guide` | 重播功能引導 |
| `isage://feedback` | 回饋郵件 |
| `isage://in-app-review` | 應用內評價入口 |

## 範例

```
isage://daily
isage://passage?id=1
isage://passage?id=1&card=1
isage://collection?id=guxun
isage://theme?id=conduct
isage://study
isage://hunt
isage://handwriting
```

## 說明

- 數字 ID 參數區分大小寫。
- Siri、捷徑、小工具與控制中心使用同一套深鏈。
- 最新列表見應用內 **設定 → 說明**。

</section>
<section lang="ja" markdown="1">

iSageは** `isage://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
isage://{host}?{params}
```


## 言葉と著者

| URL | 開く画面 |
|-----|-------|
| `isage://passage?id={id}` | 詳しく見る |
| `isage://saying?id={id}` / `isage://couplet?id={id}` / `isage://poem?id={id}` | 通路と同じ(互換性) |
| `isage://passage?id={id}&card=1` | 細部およびsageカード シートを言うこと |
| `isage://card?id={id}` / `isage://share-card?id={id}` | セージカード |
| `isage://author?id={id}` | 作者の詳細 |
| `isage://recite` / `isage://recite?id={id}` | 誦読フロー |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `isage://home` | ホーム |
| `isage://daily` | 今日の知恵 |
| `isage://random` | ランダム 言う |
| `isage://favorites` | お気に入り |
| `isage://famous` | 名句一覧 |
| `isage://search` / `isage://search?q={query}` | 検索 |
| `isage://study` / `isage://study?id={id}` | セージアカデミー |
| `isage://hunt` | セージハント (`keyword-hunt`/`flyflower`) |
| `isage://handwriting` | 手書き検索 (`handwrite`; iOS) |
| `isage://mastered` | マスタード (`progress`) |
| `isage://categories` / `isage://categories?section=` | ブラウズ |
| `isage://collection?id=guxun` | クラシック・リセンション (`ZH-Shang`/`ZH-Xia`; また`book`/`form`) |
| `isage://corpus` | すべての言葉 (`all`) |
| `isage://theme?id=conduct` | テーマ(例:`cultivation`、`learning`、`friendship`、`household`、`wealth`、`virtue`、`fortune`、`speech`、`loyalty`、`diligence`、`world`) |
| `isage://last-read` | 最後に読んだ項目 |
| `isage://reading-history` | 閲覧履歴 |
| `isage://notes` | ノート |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `isage://settings` | 設定 |
| `isage://usage-guide` | 使い方ガイド |
| `isage://widget-guide` | ウィジェットガイド |
| `isage://shortcuts-guide` | ショートカットガイド |
| `isage://feature-guide` | オンボーディングの再生 |
| `isage://feedback` | フィードバックメール |
| `isage://in-app-review` | アプリ内／App Store レビュー |

## 例


```
isage://daily
isage://passage?id=1
isage://passage?id=1&card=1
isage://collection?id=guxun
isage://theme?id=conduct
isage://study
isage://hunt
isage://handwriting
```


## ノート

- パラメータはIDが数値である場合感度です。
- シリ、ショートカット、ウィジェット、およびコントロールセンターコントロールは、同じディープリンクルートを使用します。
- 最新リストのアプリ内設定 → Help** ガイドを参照してください。

</section>
<section lang="ko" markdown="1">

iSage는 ** `isage://` ** 단축키 링크 (URL 계획)를 지원합니다. 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
isage://{host}?{params}
```


## Sayings & 저자

| URL | 열리는 화면 |
|-----|-------|
| `isage://passage?id={id}` | 자주 묻는 질문 |
| `isage://saying?id={id}` / `isage://couplet?id={id}` / `isage://poem?id={id}` | 통행과 같 ( 겸용성) |
| `isage://passage?id={id}&card=1` | Saying 세부 사항 및 sage 카드 시트 |
| `isage://card?id={id}` / `isage://share-card?id={id}` | Sage 카드 |
| `isage://author?id={id}` | 작가 상세 |
| `isage://recite` / `isage://recite?id={id}` | 낭독 흐름 |

## 디스커버리 & 연습

| URL | 열리는 화면 |
|-----|-------|
| `isage://home` | 홈 |
| `isage://daily` | 오늘의 지혜 |
| `isage://random` | 무작위 말 |
| `isage://favorites` | 즐겨찾기 |
| `isage://famous` | 명구 목록 |
| `isage://search` / `isage://search?q={query}` | 검색 |
| `isage://study` / `isage://study?id={id}` | Sage 아카데미 |
| `isage://hunt` | Sage Hunt (`keyword-hunt`/`flyflower`) |
| `isage://handwriting` | Handwriting search (`handwrite`; iOS) |
| `isage://mastered` | 마스터 (`progress`) |
| `isage://categories` / `isage://categories?section=` | 둘러보기 |
| `isage://collection?id=guxun` | 클래식 recension (`zhou-shang`/`zhou-xia`; 또한 `book`/`form`) |
| `isage://corpus` | 모든 말 (`all`) |
| `isage://theme?id=conduct` | 테마 (예 : `cultivation`, `learning`, `friendship`, `household`, `wealth`, `virtue`, `fortune`, `speech`, `loyalty`, `diligence`, `world`) |
| `isage://last-read` | 마지막으로 읽은 항목 |
| `isage://reading-history` | 읽기 기록 |
| `isage://notes` | 메모 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `isage://settings` | 설정 |
| `isage://usage-guide` | 사용 가이드 |
| `isage://widget-guide` | 위젯 가이드 |
| `isage://shortcuts-guide` | 단축어 가이드 |
| `isage://feature-guide` | 온보딩 다시 보기 |
| `isage://feedback` | 피드백 이메일 |
| `isage://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
isage://daily
isage://passage?id=1
isage://passage?id=1&card=1
isage://collection?id=guxun
isage://theme?id=conduct
isage://study
isage://hunt
isage://handwriting
```


## 메모

- 매개 변수는 ID가 숫자인지 여부를 감지합니다.
- Siri, Shortcuts, 위젯 및 제어 센터 제어는 동일한 딥 링크 루트를 사용합니다.
- in-app**Settings → 도움말** 최신 목록 안내

</section>
<section lang="ru" markdown="1">

iSage поддерживает ярлыки ** `isage://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
isage://{host}?{params}
```


## Слова и авторы

| URL | Открывает |
|-----|-------|
| `isage://passage?id={id}` | Говорить детали |
| `isage://saying?id={id}` / `isage://couplet?id={id}` / `isage://poem?id={id}` | Совместимость (Compatibility) |
| `isage://passage?id={id}&card=1` | Сказать детали и лист шалфея |
| `isage://card?id={id}` / `isage://share-card?id={id}` | Мудрая карта |
| `isage://author?id={id}` | Страница автора |
| `isage://recite` / `isage://recite?id={id}` | Режим чтения вслух |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `isage://home` | Главная |
| `isage://daily` | Сегодняшняя мудрость |
| `isage://random` | Случайные слова |
| `isage://favorites` | Избранное |
| `isage://famous` | Знаменитые строки |
| `isage://search` / `isage://search?q={query}` | Поиск |
| `isage://study` / `isage://study?id={id}` | Академия Мудрецов |
| `isage://hunt` | «Охота на мудрецов» («keyword-hunt» / «flyflower») |
| `isage://handwriting` | Поиск почерка («handwrite»; iOS) |
| `isage://mastered` | Мастеринг («Прогресс») |
| `isage://categories` / `isage://categories?section=` | Обзор |
| `isage://collection?id=guxun` | Классическая рецензия ('zhou-shang' / 'zhou-xia'; также 'книга' / 'форма') |
| `isage://corpus` | Все слова («All») |
| `isage://theme?id=conduct` | Тема (например, "культивация", "обучение", "дружба", "домохозяйство", "богатство", "добродетель", "счастье", "речь", "лояльность", "усердие", "мир") |
| `isage://last-read` | Последнее прочитанное |
| `isage://reading-history` | История чтения |
| `isage://notes` | Заметки |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `isage://settings` | Настройки |
| `isage://usage-guide` | Руководство по использованию |
| `isage://widget-guide` | Руководство по виджетам |
| `isage://shortcuts-guide` | Руководство по «Командам» |
| `isage://feature-guide` | Повторное знакомство |
| `isage://feedback` | Письмо с отзывом |
| `isage://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
isage://daily
isage://passage?id=1
isage://passage?id=1&card=1
isage://collection?id=guxun
isage://theme?id=conduct
isage://study
isage://hunt
isage://handwriting
```


## Заметки

- Параметры чувствительны к регистру, где идентификаторы являются числовыми.
- Siri, ярлыки, виджеты и элементы управления Центра управления используют одни и те же маршруты глубокой связи.
- Смотрите в приложении ** Настройки → Справочные руководства ** для последнего списка.

</section>
<section lang="th" markdown="1">

ISSage รองรับ ** `isage://` BAR * ลิงก์ลัด (RUL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
isage://{host}?{params}
```


## คําพูดและผู้เขียน

| URL | เปิด |
|-----|-------|
| `isage://passage?id={id}` | บอกรายละเอียด |
| `isage://saying?id={id}` / `isage://couplet?id={id}` / `isage://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `isage://passage?id={id}&card=1` | พูดถึงเรื่องรายละเอียดและไพ่เซจ |
| `isage://card?id={id}` / `isage://share-card?id={id}` | ไพ่เซจ |
| `isage://author?id={id}` | รายละเอียดผู้แต่ง |
| `isage://recite` / `isage://recite?id={id}` | โฟลว์การท่อง |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `isage://home` | หน้าแรก |
| `isage://daily` | สติ ปัญญา ใน ปัจจุบัน |
| `isage://random` | สุ่มพูดว่า |
| `isage://favorites` | รายการโปรด |
| `isage://famous` | บรรทัดขึ้นชื่อ |
| `isage://search` / `isage://search?q={query}` | ค้นหา |
| `isage://study` / `isage://study?id={id}` | โรงเรียนเซจ |
| `isage://hunt` | เซจ ฮันท์ ('คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน') |
| `isage://handwriting` | สืบค้นเมื่อเขียนด้วยมือ ('เขียนเอง'; OS) |
| `isage://mastered` | สําเร็จการศึกษาแล้ว ('รุก') |
| `isage://categories` / `isage://categories?section=` | เรียกดู |
| `isage://collection?id=guxun` | Resension คลาสสิก ('Zo-sange' / woo-xia'; และยัง 'Book' / image') |
| `isage://corpus` | ทุกคําพูด (ทั้งหมด) |
| `isage://theme?id=conduct` | ธีม (e.g. สืบค้นเมื่อ: Urdin', attendin', oh House Hollowe', UNVRUMRURUMOUMRUMOUMRESCOUMRESCOUMRESCIORESEIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII ONTHCORESCIIIIIIIIIIIIIIIIIIIIIIIIII] |
| `isage://last-read` | รายการที่อ่านล่าสุด |
| `isage://reading-history` | ประวัติการอ่าน |
| `isage://notes` | บันทึก |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `isage://settings` | การตั้งค่า |
| `isage://usage-guide` | คู่มือการใช้งาน |
| `isage://widget-guide` | คู่มือวิดเจ็ต |
| `isage://shortcuts-guide` | คู่มือทางลัด |
| `isage://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `isage://feedback` | อีเมลข้อเสนอแนะ |
| `isage://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
isage://daily
isage://passage?id=1
isage://passage?id=1&card=1
isage://collection?id=guxun
isage://theme?id=conduct
isage://study
isage://hunt
isage://handwriting
```


## บันทึก

- พารามิเตอร์คือความไวของตัวเลข
- ไซรี, ทางลัด, วิดเจ็ต, และศูนย์ควบคุม ใช้เส้นทางลับเดียวกัน
- ดู In-appings-Cettings softs for the list ล่าสุด

</section>
<section lang="de" markdown="1">

iSage unterstützt ** `isage://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
isage://{host}?{params}
```


## Sprüche & Autoren

| URL | Öffnet |
|-----|-------|
| `isage://passage?id={id}` | Details sagen |
| `isage://saying?id={id}` / `isage://couplet?id={id}` / `isage://poem?id={id}` | Wie Passage (Kompatibilität) |
| `isage://passage?id={id}&card=1` | Details und Salbei-Kartenblatt |
| `isage://card?id={id}` / `isage://share-card?id={id}` | Salbeikarte |
| `isage://author?id={id}` | Autorendetail |
| `isage://recite` / `isage://recite?id={id}` | Rezitationsablauf |

## Entdeckung und Praxis

| URL | Öffnet |
|-----|-------|
| `isage://home` | Startseite |
| `isage://daily` | Die Weisheit von heute |
| `isage://random` | Zufälliges Sprichwort |
| `isage://favorites` | Favoriten |
| `isage://famous` | Berühmte Zeilen |
| `isage://search` / `isage://search?q={query}` | Suche |
| `isage://study` / `isage://study?id={id}` | Sage Akademie |
| `isage://hunt` | Sage Hunt (`keyword-hunt` / `flyflower`) |
| `isage://handwriting` | Handschriftsuche (`handwrite`; iOS) |
| `isage://mastered` | gemeistert („Fortschritt) |
| `isage://categories` / `isage://categories?section=` | Durchsuchen |
| `isage://collection?id=guxun` | Klassische Rezension (`zhou-shang` / `zhou-xia`; auch `book` / `form`) |
| `isage://corpus` | Alle Worte (`all`) |
| `isage://theme?id=conduct` | Thema (z.B. `Kultivierung`, `Lernen`, `Freundschaft`, `Haushalt`, `Wohlstand`, `Tugend`, `Geschick`, `Sprache`, `Loyalität`, `Fleiß`, `Welt`) |
| `isage://last-read` | Zuletzt gelesen |
| `isage://reading-history` | Leseverlauf |
| `isage://notes` | Notizen |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `isage://settings` | Einstellungen |
| `isage://usage-guide` | Nutzungsanleitung |
| `isage://widget-guide` | Widget-Anleitung |
| `isage://shortcuts-guide` | Kurzbefehle-Anleitung |
| `isage://feature-guide` | Einführung erneut abspielen |
| `isage://feedback` | Feedback-E-Mail |
| `isage://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
isage://daily
isage://passage?id=1
isage://passage?id=1&card=1
isage://collection?id=guxun
isage://theme?id=conduct
isage://study
isage://hunt
isage://handwriting
```


## Notizen

- Parameter sind fallsensibel, wo IDs numerisch sind.
- Siri, Shortcuts, Widgets und Control Center-Steuerelemente verwenden die gleichen Deep-Link-Routen.
- Sehen Sie sich die In-App **Einstellungen → Hilfe ** Anleitungen für die neueste Liste an.

</section>
<section lang="fr" markdown="1">

iSage supporte les liens de raccourci ** `isage://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
isage://{host}?{params}
```


## Sayings & auteurs

| URL | Ouvre |
|-----|-------|
| `isage://passage?id={id}` | Les détails |
| `isage://saying?id={id}` / `isage://couplet?id={id}` / `isage://poem?id={id}` | Même chose que le passage (compatibilité) |
| `isage://passage?id={id}&card=1` | Décrire les détails et la feuille de la fiche de sauge |
| `isage://card?id={id}` / `isage://share-card?id={id}` | Carte d'âge |
| `isage://author?id={id}` | Détail de l’auteur |
| `isage://recite` / `isage://recite?id={id}` | Flux de récitation |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `isage://home` | Accueil |
| `isage://daily` | Aujourd'hui la sagesse |
| `isage://random` | Aléatoire |
| `isage://favorites` | Favoris |
| `isage://famous` | Vers célèbres |
| `isage://search` / `isage://search?q={query}` | Recherche |
| `isage://study` / `isage://study?id={id}` | Académie des sages |
| `isage://hunt` | Chasse aux sages ( ' chasse aux mots clés ' / ' fleurs volantes ') |
| `isage://handwriting` | Recherche d'écriture (`handwrite`; iOS) |
| `isage://mastered` | Maîtrise ('progrès') |
| `isage://categories` / `isage://categories?section=` | Parcourir |
| `isage://collection?id=guxun` | Recension classique (`zhou-shang` / `zhou-xia`; aussi `book` / `form`) |
| `isage://corpus` | Toutes les paroles |
| `isage://theme?id=conduct` | Thème (par exemple: «culture», «apprentissage», «amitié», «ménage», «pauvreté», «virtue», «fortune», «discipline», «monde»), |
| `isage://last-read` | Dernière lecture |
| `isage://reading-history` | Historique de lecture |
| `isage://notes` | Notes |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `isage://settings` | Réglages |
| `isage://usage-guide` | Guide d'utilisation |
| `isage://widget-guide` | Guide des widgets |
| `isage://shortcuts-guide` | Guide Raccourcis |
| `isage://feature-guide` | Rejouer l’accueil |
| `isage://feedback` | E-mail de commentaires |
| `isage://in-app-review` | Avis in-app / App Store |

## Exemples


```
isage://daily
isage://passage?id=1
isage://passage?id=1&card=1
isage://collection?id=guxun
isage://theme?id=conduct
isage://study
isage://hunt
isage://handwriting
```


## Notes

- Les paramètres sont sensibles aux cas où les ID sont numériques.
- Les commandes Siri, Shortcuts, Widgets et Control Center utilisent les mêmes itinéraires de liaison profonde.
- Voir la page d'application **Paramètres → Aide** pour la dernière liste.

</section>
<section lang="tr" markdown="1">

ISage, ** `isage://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
isage://{host}?{params}
```


## Sayings & Yazarlar

| URL | Açar |
|-----|-------|
| `isage://passage?id={id}` | De ki: |
| `isage://saying?id={id}` / `isage://couplet?id={id}` / `isage://poem?id={id}` | Aynı geçiş (compatability) |
| `isage://passage?id={id}&card=1` | Detaylı ve sage-kart sayfası |
| `isage://card?id={id}` / `isage://share-card?id={id}` | Sage kartı |
| `isage://author?id={id}` | Yazar ayrıntısı |
| `isage://recite` / `isage://recite?id={id}` | Okuma akışı |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `isage://home` | Ana sayfa |
| `isage://daily` | Bugünün Bilgeliği |
| `isage://random` | Random diyor |
| `isage://favorites` | Favoriler |
| `isage://famous` | Ünlü dizeler |
| `isage://search` / `isage://search?q={query}` | Ara |
| `isage://study` / `isage://study?id={id}` | Sage Academy |
| `isage://hunt` | Sage Hunt ('keyword-hunt' / 'flyflower') |
| `isage://handwriting` | Hand writing search ('handwrite'; iOS) |
| `isage://mastered` | Mastered ('progress') |
| `isage://categories` / `isage://categories?section=` | Gözat |
| `isage://collection?id=guxun` | Klasik reension ('zhou-shang' / "zhou-xia"; Ayrıca "book' / "form") |
| `isage://corpus` | Bütün sözler ('all') |
| `isage://theme?id=conduct` | Tema (e.g. "cultivation", "öğrenme", "arkadaşlık", "evhold", "wealth", "virtue", "fortune", "speech", " |
| `isage://last-read` | Son okunan |
| `isage://reading-history` | Okuma geçmişi |
| `isage://notes` | Notlar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `isage://settings` | Ayarlar |
| `isage://usage-guide` | Kullanım kılavuzu |
| `isage://widget-guide` | Widget kılavuzu |
| `isage://shortcuts-guide` | Kısayol kılavuzu |
| `isage://feature-guide` | Tanıtımı yeniden oynat |
| `isage://feedback` | Geri bildirim e-postası |
| `isage://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
isage://daily
isage://passage?id=1
isage://passage?id=1&card=1
isage://collection?id=guxun
isage://theme?id=conduct
isage://study
isage://hunt
isage://handwriting
```


## Notlar

- Parametreler, kimliklerin sayısal olduğu durumlarda hassastır.
- Siri, Shortcuts, widgets ve Control Center kontrolleri aynı derin bağlantı yollarını kullanır.
- In-app **Settings → Yardım** en son liste için kılavuzlar.

</section>
