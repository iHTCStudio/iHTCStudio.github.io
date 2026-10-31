---
layout: doc
title: iRhyme — Shortcut Links
app_id: iRhyme
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: irhyme:// deep links for iRhyme — passage, daily, recite, study, hunt, collections, settings guides, and more.
---

<section lang="en" markdown="1">

iRhyme supports **`irhyme://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
irhyme://{host}?{params}
```

## Passages & authors

| URL | Opens |
|-----|-------|
| `irhyme://passage?id={id}` | Passage detail |
| `irhyme://saying?id={id}` / `irhyme://couplet?id={id}` / `irhyme://poem?id={id}` | Same as passage (compatibility) |
| `irhyme://passage?id={id}&card=1` | Passage detail and card sheet |
| `irhyme://card?id={id}` / `irhyme://share-card?id={id}` | Rhyme cards |
| `irhyme://author?id={id}` | Author detail |
| `irhyme://recite` / `irhyme://recite?id={id}` | Recite flow |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `irhyme://home` | Home |
| `irhyme://daily` | Today’s Rhyme |
| `irhyme://random` | Random passage |
| `irhyme://favorites` | Favorites |
| `irhyme://famous` | Famous lines |
| `irhyme://search` / `irhyme://search?q={query}` | Search |
| `irhyme://study` / `irhyme://study?id={id}` | Rhyme Academy |
| `irhyme://hunt` | Rhyme Hunt (`keyword-hunt` / `flyflower`) |
| `irhyme://handwriting` | Handwriting search (`handwrite`; iOS) |
| `irhyme://mastered` | Mastered (`progress`) |
| `irhyme://categories` / `irhyme://categories?section=` | Browse |
| `irhyme://collection?id=` | Collection / book (`shenglv` / `liweng` / `qianjia` / `youxue`) |
| `irhyme://corpus` | All passages (`all`) |
| `irhyme://last-read` | Last read |
| `irhyme://reading-history` | Reading history |
| `irhyme://notes` | Notes |
| `irhyme://pair` | Parallelism practice |
| `irhyme://prosody` | Prosody desk |
| `irhyme://rhyme?id=dong` | One rhyme class |
| `irhyme://compare?rhyme=dong` | Same-rhyme compare |
| `irhyme://glossary?id=` | Glossary |

## Settings & guides

| URL | Opens |
|-----|-------|
| `irhyme://settings` | Settings |
| `irhyme://usage-guide` | Usage guide |
| `irhyme://widget-guide` | Widget guide |
| `irhyme://shortcuts-guide` | Shortcuts guide |
| `irhyme://feature-guide` | Replay onboarding |
| `irhyme://feedback` | Feedback email |
| `irhyme://in-app-review` | In-app / Store review entry |

## Examples

```
irhyme://daily
irhyme://passage?id=1001
irhyme://pair
irhyme://compare?rhyme=dong
irhyme://collection?id=shenglv
irhyme://study
irhyme://hunt
```

## Notes

- Parameters are case-sensitive where IDs are numeric.
- Siri, Shortcuts, widgets, and Control Center controls use the same deep-link routes.
- See the in-app **Settings → Help** guides for the latest list.

</section>
<section lang="zh-CN" markdown="1">

爱声律启蒙支持 **`irhyme://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导页结束后重复打开。

## 链接格式

```
irhyme://{host}?{params}
```

## 篇目与作者

| URL | 打开 |
|-----|------|
| `irhyme://passage?id={id}` | 篇目详情 |
| `irhyme://saying?id={id}` / `irhyme://couplet?id={id}` / `irhyme://poem?id={id}` | 同详情（兼容别名） |
| `irhyme://passage?id={id}&card=1` | 详情并弹出韵卡 |
| `irhyme://card?id={id}` / `irhyme://share-card?id={id}` | 韵卡 |
| `irhyme://author?id={id}` | 作者详情 |
| `irhyme://recite` / `irhyme://recite?id={id}` | 诵读 |

## 发现与学堂

| URL | 打开 |
|-----|------|
| `irhyme://home` | 首页 |
| `irhyme://daily` | 今日一律 |
| `irhyme://random` | 随机篇目 |
| `irhyme://favorites` | 收藏 |
| `irhyme://famous` | 金句 |
| `irhyme://search` / `irhyme://search?q={query}` | 搜索 |
| `irhyme://study` / `irhyme://study?id={id}` | 声律学堂 |
| `irhyme://hunt` | 寻对（`keyword-hunt` / `flyflower`） |
| `irhyme://handwriting` | 手写搜索（`handwrite`；iOS） |
| `irhyme://mastered` | 已掌握（`progress`） |
| `irhyme://categories` / `irhyme://categories?section=` | 分类浏览 |
| `irhyme://collection?id=` | 合集 / 典籍（`shenglv` / `liweng` / `qianjia` / `youxue`） |
| `irhyme://corpus` | 全部篇目（`all`） |
| `irhyme://last-read` | 最近阅读 |
| `irhyme://reading-history` | 阅读历史 |
| `irhyme://notes` | 笔记 |
| `irhyme://pair` | 对仗练习 |
| `irhyme://prosody` | 声律工作台 |
| `irhyme://rhyme?id=dong` | 单一韵部 |
| `irhyme://compare?rhyme=dong` | 同韵对照 |
| `irhyme://glossary?id=` | 术语表 |

## 设置与指南

| URL | 打开 |
|-----|------|
| `irhyme://settings` | 设置 |
| `irhyme://usage-guide` | 使用说明 |
| `irhyme://widget-guide` | 小组件指南 |
| `irhyme://shortcuts-guide` | 快捷指南 |
| `irhyme://feature-guide` | 重播功能引导 |
| `irhyme://feedback` | 反馈邮件 |
| `irhyme://in-app-review` | 应用内评价入口 |

## 示例

```
irhyme://daily
irhyme://passage?id=1001
irhyme://pair
irhyme://compare?rhyme=dong
irhyme://collection?id=shenglv
irhyme://study
irhyme://hunt
```

## 说明

- 数字 ID 参数区分大小写。
- Siri、快捷指令、小组件与控制中心使用同一套深链。
- 最新列表见应用内 **设置 → 帮助**。

</section>
<section lang="zh-TW" markdown="1">

愛聲律啟蒙支援 **`irhyme://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導頁結束後重複打開。

## 連結格式

```
irhyme://{host}?{params}
```

## 篇目與作者

| URL | 打開 |
|-----|------|
| `irhyme://passage?id={id}` | 篇目詳情 |
| `irhyme://saying?id={id}` / `irhyme://couplet?id={id}` / `irhyme://poem?id={id}` | 同詳情（相容別名） |
| `irhyme://passage?id={id}&card=1` | 詳情並彈出韻卡 |
| `irhyme://card?id={id}` / `irhyme://share-card?id={id}` | 韻卡 |
| `irhyme://author?id={id}` | 作者詳情 |
| `irhyme://recite` / `irhyme://recite?id={id}` | 誦讀 |

## 發現與學堂

| URL | 打開 |
|-----|------|
| `irhyme://home` | 首頁 |
| `irhyme://daily` | 今日一律 |
| `irhyme://random` | 隨機篇目 |
| `irhyme://favorites` | 收藏 |
| `irhyme://famous` | 金句 |
| `irhyme://search` / `irhyme://search?q={query}` | 搜尋 |
| `irhyme://study` / `irhyme://study?id={id}` | 聲律學堂 |
| `irhyme://hunt` | 尋對（`keyword-hunt` / `flyflower`） |
| `irhyme://handwriting` | 手寫搜尋（`handwrite`；iOS） |
| `irhyme://mastered` | 已掌握（`progress`） |
| `irhyme://categories` / `irhyme://categories?section=` | 分類瀏覽 |
| `irhyme://collection?id=` | 合集 / 典籍（`shenglv` / `liweng` / `qianjia` / `youxue`） |
| `irhyme://corpus` | 全部篇目（`all`） |
| `irhyme://last-read` | 最近閱讀 |
| `irhyme://reading-history` | 閱讀歷史 |
| `irhyme://notes` | 筆記 |
| `irhyme://pair` | 對仗練習 |
| `irhyme://prosody` | 聲律工作臺 |
| `irhyme://rhyme?id=dong` | 單一韻部 |
| `irhyme://compare?rhyme=dong` | 同韻對照 |
| `irhyme://glossary?id=` | 術語表 |

## 設定與指南

| URL | 打開 |
|-----|------|
| `irhyme://settings` | 設定 |
| `irhyme://usage-guide` | 使用說明 |
| `irhyme://widget-guide` | 小工具指南 |
| `irhyme://shortcuts-guide` | 捷徑指南 |
| `irhyme://feature-guide` | 重播功能引導 |
| `irhyme://feedback` | 回饋郵件 |
| `irhyme://in-app-review` | 應用內評價入口 |

## 範例

```
irhyme://daily
irhyme://passage?id=1001
irhyme://pair
irhyme://compare?rhyme=dong
irhyme://collection?id=shenglv
irhyme://study
irhyme://hunt
```

## 說明

- 數字 ID 參數區分大小寫。
- Siri、捷徑、小工具與控制中心使用同一套深鏈。
- 最新列表見應用內 **設定 → 說明**。

</section>
<section lang="ja" markdown="1">

iRhymeは** `irhyme://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
irhyme://{host}?{params}
```


## パスポートと著者

| URL | 開く画面 |
|-----|-------|
| `irhyme://passage?id={id}` | 章句の詳細 |
| `irhyme://saying?id={id}` / `irhyme://couplet?id={id}` / `irhyme://poem?id={id}` | 通路と同じ(互換性) |
| `irhyme://passage?id={id}&card=1` | 通路の細部およびカード シート |
| `irhyme://card?id={id}` / `irhyme://share-card?id={id}` | ライムカード |
| `irhyme://author?id={id}` | 作者の詳細 |
| `irhyme://recite` / `irhyme://recite?id={id}` | 誦読フロー |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `irhyme://home` | ホーム |
| `irhyme://daily` | 今日のライム |
| `irhyme://random` | ランダムな章句 |
| `irhyme://favorites` | お気に入り |
| `irhyme://famous` | 名句一覧 |
| `irhyme://search` / `irhyme://search?q={query}` | 検索 |
| `irhyme://study` / `irhyme://study?id={id}` | ライムアカデミー |
| `irhyme://hunt` | ライムハント (`keyword-hunt`/`flyflower`) |
| `irhyme://handwriting` | 手書き検索 (`handwrite`; iOS) |
| `irhyme://mastered` | マスタード (`progress`) |
| `irhyme://categories` / `irhyme://categories?section=` | ブラウズ |
| `irhyme://collection?id=` | コレクション / book (`shenglv` / `liweng` / `qianjia` /`youxue`) |
| `irhyme://corpus` | すべての通路 (`all`) |
| `irhyme://last-read` | 最後に読んだ項目 |
| `irhyme://reading-history` | 閲覧履歴 |
| `irhyme://notes` | ノート |
| `irhyme://pair` | 並列練習 |
| `irhyme://prosody` | プロソディデスク |
| `irhyme://rhyme?id=dong` | 1つの韻のクラス |
| `irhyme://compare?rhyme=dong` | 同じ韻比較 |
| `irhyme://glossary?id=` | 用語集 |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `irhyme://settings` | 設定 |
| `irhyme://usage-guide` | 使い方ガイド |
| `irhyme://widget-guide` | ウィジェットガイド |
| `irhyme://shortcuts-guide` | ショートカットガイド |
| `irhyme://feature-guide` | オンボーディングの再生 |
| `irhyme://feedback` | フィードバックメール |
| `irhyme://in-app-review` | アプリ内／App Store レビュー |

## 例


```
irhyme://daily
irhyme://passage?id=1001
irhyme://pair
irhyme://compare?rhyme=dong
irhyme://collection?id=shenglv
irhyme://study
irhyme://hunt
```


## ノート

- パラメータはIDが数値である場合感度です。
- シリ、ショートカット、ウィジェット、およびコントロールセンターコントロールは、同じディープリンクルートを使用します。
- 最新リストのアプリ内設定 → Help** ガイドを参照してください。

</section>
<section lang="ko" markdown="1">

iRhyme 지원 ** `irhyme://` ** 단축키 링크 (URL 계획). 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
irhyme://{host}?{params}
```


## 책임 & 저자

| URL | 열리는 화면 |
|-----|-------|
| `irhyme://passage?id={id}` | 구절 상세 |
| `irhyme://saying?id={id}` / `irhyme://couplet?id={id}` / `irhyme://poem?id={id}` | 통행과 같 ( 겸용성) |
| `irhyme://passage?id={id}&card=1` | 통행 세부사항과 카드 장 |
| `irhyme://card?id={id}` / `irhyme://share-card?id={id}` | Rhyme 카드 |
| `irhyme://author?id={id}` | 작가 상세 |
| `irhyme://recite` / `irhyme://recite?id={id}` | 낭독 흐름 |

## 디스커버리 & 연습

| URL | 열리는 화면 |
|-----|-------|
| `irhyme://home` | 홈 |
| `irhyme://daily` | 오늘의 Rhyme |
| `irhyme://random` | 무작위 구절 |
| `irhyme://favorites` | 즐겨찾기 |
| `irhyme://famous` | 명구 목록 |
| `irhyme://search` / `irhyme://search?q={query}` | 검색 |
| `irhyme://study` / `irhyme://study?id={id}` | Rhyme 아카데미 |
| `irhyme://hunt` | Rhyme Hunt (`keyword-hunt`/`flyflower`) |
| `irhyme://handwriting` | Handwriting search (`handwrite`; iOS) |
| `irhyme://mastered` | 마스터 (`progress`) |
| `irhyme://categories` / `irhyme://categories?section=` | 둘러보기 |
| `irhyme://collection?id=` | 컬렉션 / 책 (`shenglv`/`liweng`/`qianjia`/`youxue`) |
| `irhyme://corpus` | 모든 통행 (`all`) |
| `irhyme://last-read` | 마지막으로 읽은 항목 |
| `irhyme://reading-history` | 읽기 기록 |
| `irhyme://notes` | 메모 |
| `irhyme://pair` | 병렬 연습 |
| `irhyme://prosody` | Prosody 책상 |
| `irhyme://rhyme?id=dong` | 1개의 rhyme 종류 |
| `irhyme://compare?rhyme=dong` | Same-rhyme 비교 |
| `irhyme://glossary?id=` | 회사 소개 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `irhyme://settings` | 설정 |
| `irhyme://usage-guide` | 사용 가이드 |
| `irhyme://widget-guide` | 위젯 가이드 |
| `irhyme://shortcuts-guide` | 단축어 가이드 |
| `irhyme://feature-guide` | 온보딩 다시 보기 |
| `irhyme://feedback` | 피드백 이메일 |
| `irhyme://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
irhyme://daily
irhyme://passage?id=1001
irhyme://pair
irhyme://compare?rhyme=dong
irhyme://collection?id=shenglv
irhyme://study
irhyme://hunt
```


## 메모

- 매개 변수는 ID가 숫자인지 여부를 감지합니다.
- Siri, Shortcuts, 위젯 및 제어 센터 제어는 동일한 딥 링크 루트를 사용합니다.
- in-app**Settings → 도움말** 최신 목록 안내

</section>
<section lang="ru" markdown="1">

iRhyme поддерживает ярлыки ** `irhyme://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
irhyme://{host}?{params}
```


## Проходы и авторы

| URL | Открывает |
|-----|-------|
| `irhyme://passage?id={id}` | Страница отрывка |
| `irhyme://saying?id={id}` / `irhyme://couplet?id={id}` / `irhyme://poem?id={id}` | Совместимость (Compatibility) |
| `irhyme://passage?id={id}&card=1` | Детали проезда и карточный лист |
| `irhyme://card?id={id}` / `irhyme://share-card?id={id}` | Карты ритма |
| `irhyme://author?id={id}` | Страница автора |
| `irhyme://recite` / `irhyme://recite?id={id}` | Режим чтения вслух |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `irhyme://home` | Главная |
| `irhyme://daily` | Сегодняшний ритм |
| `irhyme://random` | Случайный отрывок |
| `irhyme://favorites` | Избранное |
| `irhyme://famous` | Знаменитые строки |
| `irhyme://search` / `irhyme://search?q={query}` | Поиск |
| `irhyme://study` / `irhyme://study?id={id}` | Академия Rhyme |
| `irhyme://hunt` | Rhyme Hunt («охота за ключевыми словами» / «флайфлауэр») |
| `irhyme://handwriting` | Поиск почерка («handwrite»; iOS) |
| `irhyme://mastered` | Мастеринг («Прогресс») |
| `irhyme://categories` / `irhyme://categories?section=` | Обзор |
| `irhyme://collection?id=` | Коллекция/книга ('shenglv'/'liweng'/'qianjia'/'youxue') |
| `irhyme://corpus` | Все пассажи («All») |
| `irhyme://last-read` | Последнее прочитанное |
| `irhyme://reading-history` | История чтения |
| `irhyme://notes` | Заметки |
| `irhyme://pair` | Практика параллелизма |
| `irhyme://prosody` | Стол для просодия |
| `irhyme://rhyme?id=dong` | Один класс рифмы |
| `irhyme://compare?rhyme=dong` | Сравнение одной и той же рифмы |
| `irhyme://glossary?id=` | Глоссарий |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `irhyme://settings` | Настройки |
| `irhyme://usage-guide` | Руководство по использованию |
| `irhyme://widget-guide` | Руководство по виджетам |
| `irhyme://shortcuts-guide` | Руководство по «Командам» |
| `irhyme://feature-guide` | Повторное знакомство |
| `irhyme://feedback` | Письмо с отзывом |
| `irhyme://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
irhyme://daily
irhyme://passage?id=1001
irhyme://pair
irhyme://compare?rhyme=dong
irhyme://collection?id=shenglv
irhyme://study
irhyme://hunt
```


## Заметки

- Параметры чувствительны к регистру, где идентификаторы являются числовыми.
- Siri, ярлыки, виджеты и элементы управления Центра управления используют одни и те же маршруты глубокой связи.
- Смотрите в приложении ** Настройки → Справочные руководства ** для последнего списка.

</section>
<section lang="th" markdown="1">

iRhyme รองรับ~ `irhyme://` BAR * ลิงก์ลัด (URL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
irhyme://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `irhyme://passage?id={id}` | รายละเอียดข้อความ |
| `irhyme://saying?id={id}` / `irhyme://couplet?id={id}` / `irhyme://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `irhyme://passage?id={id}&card=1` | รายละเอียดและนามบัตร |
| `irhyme://card?id={id}` / `irhyme://share-card?id={id}` | ไพ่ Ryme |
| `irhyme://author?id={id}` | รายละเอียดผู้แต่ง |
| `irhyme://recite` / `irhyme://recite?id={id}` | โฟลว์การท่อง |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `irhyme://home` | หน้าแรก |
| `irhyme://daily` | ไรม์ ใน ปัจจุบัน |
| `irhyme://random` | ข้อความแบบสุ่ม |
| `irhyme://favorites` | รายการโปรด |
| `irhyme://famous` | บรรทัดขึ้นชื่อ |
| `irhyme://search` / `irhyme://search?q={query}` | ค้นหา |
| `irhyme://study` / `irhyme://study?id={id}` | โรงเรียน Rayme |
| `irhyme://hunt` | Rayme Hunt ('คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน') |
| `irhyme://handwriting` | สืบค้นเมื่อเขียนด้วยมือ ('เขียนเอง'; OS) |
| `irhyme://mastered` | สําเร็จการศึกษาแล้ว ('รุก') |
| `irhyme://categories` / `irhyme://categories?section=` | เรียกดู |
| `irhyme://collection?id=` | คอลเลกชัน / หนังสือ (อังกฤษ) |
| `irhyme://corpus` | ทุกช่อง (ทั้งหมด) |
| `irhyme://last-read` | รายการที่อ่านล่าสุด |
| `irhyme://reading-history` | ประวัติการอ่าน |
| `irhyme://notes` | บันทึก |
| `irhyme://pair` | ฝึกความเหลื่อมล้ํา |
| `irhyme://prosody` | โต๊ะพรอโซดี้ |
| `irhyme://rhyme?id=dong` | คลาสกลอนหนึ่ง |
| `irhyme://compare?rhyme=dong` | เปรียบเทียบขนาดเท่าเดิม |
| `irhyme://glossary?id=` | อภิธานศัพท์ |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `irhyme://settings` | การตั้งค่า |
| `irhyme://usage-guide` | คู่มือการใช้งาน |
| `irhyme://widget-guide` | คู่มือวิดเจ็ต |
| `irhyme://shortcuts-guide` | คู่มือทางลัด |
| `irhyme://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `irhyme://feedback` | อีเมลข้อเสนอแนะ |
| `irhyme://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
irhyme://daily
irhyme://passage?id=1001
irhyme://pair
irhyme://compare?rhyme=dong
irhyme://collection?id=shenglv
irhyme://study
irhyme://hunt
```


## บันทึก

- พารามิเตอร์คือความไวของตัวเลข
- ไซรี, ทางลัด, วิดเจ็ต, และศูนย์ควบคุม ใช้เส้นทางลับเดียวกัน
- ดู In-appings-Cettings softs for the list ล่าสุด

</section>
<section lang="de" markdown="1">

iRhyme unterstützt ** `irhyme://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
irhyme://{host}?{params}
```


## Passagen & Autoren

| URL | Öffnet |
|-----|-------|
| `irhyme://passage?id={id}` | Passagen-Detail |
| `irhyme://saying?id={id}` / `irhyme://couplet?id={id}` / `irhyme://poem?id={id}` | Wie Passage (Kompatibilität) |
| `irhyme://passage?id={id}&card=1` | Angaben zum Durchgang und Kartenblatt |
| `irhyme://card?id={id}` / `irhyme://share-card?id={id}` | Reimkarten |
| `irhyme://author?id={id}` | Autorendetail |
| `irhyme://recite` / `irhyme://recite?id={id}` | Rezitationsablauf |

## Entdeckung und Praxis

| URL | Öffnet |
|-----|-------|
| `irhyme://home` | Startseite |
| `irhyme://daily` | Der heutige Reim |
| `irhyme://random` | Zufällige Passage |
| `irhyme://favorites` | Favoriten |
| `irhyme://famous` | Berühmte Zeilen |
| `irhyme://search` / `irhyme://search?q={query}` | Suche |
| `irhyme://study` / `irhyme://study?id={id}` | Rhyme Akademie |
| `irhyme://hunt` | Rhyme Hunt (`keyword-hunt` / `flyflower`) |
| `irhyme://handwriting` | Handschriftsuche (`handwrite`; iOS) |
| `irhyme://mastered` | gemeistert („Fortschritt) |
| `irhyme://categories` / `irhyme://categories?section=` | Durchsuchen |
| `irhyme://collection?id=` | Sammlung/Buch (`shenglv`/`liweng`/`qianjia`/`youxue`) |
| `irhyme://corpus` | Alle Passagen (`all`) |
| `irhyme://last-read` | Zuletzt gelesen |
| `irhyme://reading-history` | Leseverlauf |
| `irhyme://notes` | Notizen |
| `irhyme://pair` | Parallelitätspraxis |
| `irhyme://prosody` | Prosodie Schreibtisch |
| `irhyme://rhyme?id=dong` | Eine Reimklasse |
| `irhyme://compare?rhyme=dong` | Gleicher Reim Vergleich |
| `irhyme://glossary?id=` | Glossar |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `irhyme://settings` | Einstellungen |
| `irhyme://usage-guide` | Nutzungsanleitung |
| `irhyme://widget-guide` | Widget-Anleitung |
| `irhyme://shortcuts-guide` | Kurzbefehle-Anleitung |
| `irhyme://feature-guide` | Einführung erneut abspielen |
| `irhyme://feedback` | Feedback-E-Mail |
| `irhyme://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
irhyme://daily
irhyme://passage?id=1001
irhyme://pair
irhyme://compare?rhyme=dong
irhyme://collection?id=shenglv
irhyme://study
irhyme://hunt
```


## Notizen

- Parameter sind fallsensibel, wo IDs numerisch sind.
- Siri, Shortcuts, Widgets und Control Center-Steuerelemente verwenden die gleichen Deep-Link-Routen.
- Sehen Sie sich die In-App **Einstellungen → Hilfe ** Anleitungen für die neueste Liste an.

</section>
<section lang="fr" markdown="1">

iRhyme prend en charge les liens de raccourci ** `irhyme://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
irhyme://{host}?{params}
```


## Passages et auteurs

| URL | Ouvre |
|-----|-------|
| `irhyme://passage?id={id}` | Détail du passage |
| `irhyme://saying?id={id}` / `irhyme://couplet?id={id}` / `irhyme://poem?id={id}` | Même chose que le passage (compatibilité) |
| `irhyme://passage?id={id}&card=1` | Détails du passage et feuille de carte |
| `irhyme://card?id={id}` / `irhyme://share-card?id={id}` | Cartes de rythme |
| `irhyme://author?id={id}` | Détail de l’auteur |
| `irhyme://recite` / `irhyme://recite?id={id}` | Flux de récitation |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `irhyme://home` | Accueil |
| `irhyme://daily` | Aujourd'hui |
| `irhyme://random` | Passage aléatoire |
| `irhyme://favorites` | Favoris |
| `irhyme://famous` | Vers célèbres |
| `irhyme://search` / `irhyme://search?q={query}` | Recherche |
| `irhyme://study` / `irhyme://study?id={id}` | Académie de rythme |
| `irhyme://hunt` | Chasse aux rimes ( ' chasse aux mots clés ' / ' fleurs volantes ') |
| `irhyme://handwriting` | Recherche d'écriture (`handwrite`; iOS) |
| `irhyme://mastered` | Maîtrise ('progrès') |
| `irhyme://categories` / `irhyme://categories?section=` | Parcourir |
| `irhyme://collection?id=` | Collection / livre (`shenglv` / `liweng` / `qianjia` / `youxue`) |
| `irhyme://corpus` | Tous les passages |
| `irhyme://last-read` | Dernière lecture |
| `irhyme://reading-history` | Historique de lecture |
| `irhyme://notes` | Notes |
| `irhyme://pair` | La pratique du parallélisme |
| `irhyme://prosody` | Bureau de prosodie |
| `irhyme://rhyme?id=dong` | Une classe de rimes |
| `irhyme://compare?rhyme=dong` | Comparaison des mêmes rythmes |
| `irhyme://glossary?id=` | Glossaire |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `irhyme://settings` | Réglages |
| `irhyme://usage-guide` | Guide d'utilisation |
| `irhyme://widget-guide` | Guide des widgets |
| `irhyme://shortcuts-guide` | Guide Raccourcis |
| `irhyme://feature-guide` | Rejouer l’accueil |
| `irhyme://feedback` | E-mail de commentaires |
| `irhyme://in-app-review` | Avis in-app / App Store |

## Exemples


```
irhyme://daily
irhyme://passage?id=1001
irhyme://pair
irhyme://compare?rhyme=dong
irhyme://collection?id=shenglv
irhyme://study
irhyme://hunt
```


## Notes

- Les paramètres sont sensibles aux cas où les ID sont numériques.
- Les commandes Siri, Shortcuts, Widgets et Control Center utilisent les mêmes itinéraires de liaison profonde.
- Voir la page d'application **Paramètres → Aide** pour la dernière liste.

</section>
<section lang="tr" markdown="1">

iRhyme ** `irhyme://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
irhyme://{host}?{params}
```


## Geçişler ve yazarlar

| URL | Açar |
|-----|-------|
| `irhyme://passage?id={id}` | Pasaj ayrıntısı |
| `irhyme://saying?id={id}` / `irhyme://couplet?id={id}` / `irhyme://poem?id={id}` | Aynı geçiş (compatability) |
| `irhyme://passage?id={id}&card=1` | Pasaj detay ve kart sayfası |
| `irhyme://card?id={id}` / `irhyme://share-card?id={id}` | Rhyme kartları |
| `irhyme://author?id={id}` | Yazar ayrıntısı |
| `irhyme://recite` / `irhyme://recite?id={id}` | Okuma akışı |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `irhyme://home` | Ana sayfa |
| `irhyme://daily` | Bugünün Rhyme |
| `irhyme://random` | Rastgele pasaj |
| `irhyme://favorites` | Favoriler |
| `irhyme://famous` | Ünlü dizeler |
| `irhyme://search` / `irhyme://search?q={query}` | Ara |
| `irhyme://study` / `irhyme://study?id={id}` | Rhyme Akademi |
| `irhyme://hunt` | Rhyme Hunt ('keyword-hunt' / 'flyflower') |
| `irhyme://handwriting` | Hand writing search ('handwrite'; iOS) |
| `irhyme://mastered` | Mastered ('progress') |
| `irhyme://categories` / `irhyme://categories?section=` | Gözat |
| `irhyme://collection?id=` | Collection / book ('shenglv' / "liweng" / "qianjia" / "youxue") |
| `irhyme://corpus` | Bütün geçitler ('all') |
| `irhyme://last-read` | Son okunan |
| `irhyme://reading-history` | Okuma geçmişi |
| `irhyme://notes` | Notlar |
| `irhyme://pair` | Paralellik uygulamaları |
| `irhyme://prosody` | Prosody desk |
| `irhyme://rhyme?id=dong` | Bir rhyme sınıfı |
| `irhyme://compare?rhyme=dong` | Aynı-rhyme Karşılaştırma |
| `irhyme://glossary?id=` | Parlak |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `irhyme://settings` | Ayarlar |
| `irhyme://usage-guide` | Kullanım kılavuzu |
| `irhyme://widget-guide` | Widget kılavuzu |
| `irhyme://shortcuts-guide` | Kısayol kılavuzu |
| `irhyme://feature-guide` | Tanıtımı yeniden oynat |
| `irhyme://feedback` | Geri bildirim e-postası |
| `irhyme://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
irhyme://daily
irhyme://passage?id=1001
irhyme://pair
irhyme://compare?rhyme=dong
irhyme://collection?id=shenglv
irhyme://study
irhyme://hunt
```


## Notlar

- Parametreler, kimliklerin sayısal olduğu durumlarda hassastır.
- Siri, Shortcuts, widgets ve Control Center kontrolleri aynı derin bağlantı yollarını kullanır.
- In-app **Settings → Yardım** en son liste için kılavuzlar.

</section>
