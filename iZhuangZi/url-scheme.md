---
layout: doc
title: iZhuangZi — Shortcut Links
app_id: iZhuangZi
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: izhuangzi:// deep links for iZhuangZi — passage, daily, recite, study, hunt, collections, settings guides, and more.
---

<section lang="en" markdown="1">

iZhuangZi supports **`izhuangzi://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
izhuangzi://{host}?{params}
```

## Passages & authors

| URL | Opens |
|-----|-------|
| `izhuangzi://passage?id={id}` | Passage detail |
| `izhuangzi://saying?id={id}` / `izhuangzi://couplet?id={id}` / `izhuangzi://poem?id={id}` | Same as passage (compatibility) |
| `izhuangzi://passage?id={id}&card=1` | Passage detail and card sheet |
| `izhuangzi://card?id={id}` / `izhuangzi://share-card?id={id}` | 逍遥 cards |
| `izhuangzi://author?id={id}` | Author detail |
| `izhuangzi://recite` / `izhuangzi://recite?id={id}` | Recite flow |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `izhuangzi://home` | Home |
| `izhuangzi://daily` | Daily Zhuangzi |
| `izhuangzi://random` | Random passage |
| `izhuangzi://favorites` | Favorites |
| `izhuangzi://famous` | Famous lines |
| `izhuangzi://search` / `izhuangzi://search?q={query}` | Search |
| `izhuangzi://study` / `izhuangzi://study?id={id}` | Dao Study |
| `izhuangzi://hunt` | Zhuang Hunt (`keyword-hunt` / `flyflower`) |
| `izhuangzi://handwriting` | Handwriting search (`handwrite`; iOS) |
| `izhuangzi://mastered` | Mastered (`progress`) |
| `izhuangzi://categories` / `izhuangzi://categories?section=` | Browse |
| `izhuangzi://collection?id=` | Collection / book (`neipian` / `waipian` / `zapian`) |
| `izhuangzi://corpus` | All passages (`all`) |
| `izhuangzi://last-read` | Last read |
| `izhuangzi://reading-history` | Reading history |
| `izhuangzi://notes` | Notes |
| `izhuangzi://ask` | Ask Zhuangzi |
| `izhuangzi://allegories` | Parables |
| `izhuangzi://concepts` | Concepts |
| `izhuangzi://theme?id=neipian` | Inner / Outer / Miscellaneous |

## Settings & guides

| URL | Opens |
|-----|-------|
| `izhuangzi://settings` | Settings |
| `izhuangzi://usage-guide` | Usage guide |
| `izhuangzi://widget-guide` | Widget guide |
| `izhuangzi://shortcuts-guide` | Shortcuts guide |
| `izhuangzi://feature-guide` | Replay onboarding |
| `izhuangzi://feedback` | Feedback email |
| `izhuangzi://in-app-review` | In-app / Store review entry |

## Examples

```
izhuangzi://daily
izhuangzi://passage?id=1
izhuangzi://ask
izhuangzi://allegories
izhuangzi://collection?id=neipian
izhuangzi://study
izhuangzi://hunt
```

## Notes

- Parameters are case-sensitive where IDs are numeric.
- Siri, Shortcuts, widgets, and Control Center controls use the same deep-link routes.
- See the in-app **Settings → Help** guides for the latest list.

</section>
<section lang="zh-CN" markdown="1">

爱庄子支持 **`izhuangzi://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导页结束后重复打开。

## 链接格式

```
izhuangzi://{host}?{params}
```

## 篇目与作者

| URL | 打开 |
|-----|------|
| `izhuangzi://passage?id={id}` | 篇目详情 |
| `izhuangzi://saying?id={id}` / `izhuangzi://couplet?id={id}` / `izhuangzi://poem?id={id}` | 同详情（兼容别名） |
| `izhuangzi://passage?id={id}&card=1` | 详情并弹出逍遥卡 |
| `izhuangzi://card?id={id}` / `izhuangzi://share-card?id={id}` | 逍遥卡 |
| `izhuangzi://author?id={id}` | 作者详情 |
| `izhuangzi://recite` / `izhuangzi://recite?id={id}` | 诵读 |

## 发现与学堂

| URL | 打开 |
|-----|------|
| `izhuangzi://home` | 首页 |
| `izhuangzi://daily` | 今日一子 |
| `izhuangzi://random` | 随机篇目 |
| `izhuangzi://favorites` | 收藏 |
| `izhuangzi://famous` | 金句 |
| `izhuangzi://search` / `izhuangzi://search?q={query}` | 搜索 |
| `izhuangzi://study` / `izhuangzi://study?id={id}` | 庄学学堂 |
| `izhuangzi://hunt` | 寻庄（`keyword-hunt` / `flyflower`） |
| `izhuangzi://handwriting` | 手写搜索（`handwrite`；iOS） |
| `izhuangzi://mastered` | 已掌握（`progress`） |
| `izhuangzi://categories` / `izhuangzi://categories?section=` | 分类浏览 |
| `izhuangzi://collection?id=` | 合集 / 典籍（`neipian` / `waipian` / `zapian`） |
| `izhuangzi://corpus` | 全部篇目（`all`） |
| `izhuangzi://last-read` | 最近阅读 |
| `izhuangzi://reading-history` | 阅读历史 |
| `izhuangzi://notes` | 笔记 |
| `izhuangzi://ask` | 问庄子 |
| `izhuangzi://allegories` | 寓言 |
| `izhuangzi://concepts` | 概念 |
| `izhuangzi://theme?id=neipian` | 内篇 / 外篇 / 杂篇 |

## 设置与指南

| URL | 打开 |
|-----|------|
| `izhuangzi://settings` | 设置 |
| `izhuangzi://usage-guide` | 使用说明 |
| `izhuangzi://widget-guide` | 小组件指南 |
| `izhuangzi://shortcuts-guide` | 快捷指南 |
| `izhuangzi://feature-guide` | 重播功能引导 |
| `izhuangzi://feedback` | 反馈邮件 |
| `izhuangzi://in-app-review` | 应用内评价入口 |

## 示例

```
izhuangzi://daily
izhuangzi://passage?id=1
izhuangzi://ask
izhuangzi://allegories
izhuangzi://collection?id=neipian
izhuangzi://study
izhuangzi://hunt
```

## 说明

- 数字 ID 参数区分大小写。
- Siri、快捷指令、小组件与控制中心使用同一套深链。
- 最新列表见应用内 **设置 → 帮助**。

</section>
<section lang="zh-TW" markdown="1">

愛莊子支援 **`izhuangzi://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導頁結束後重複打開。

## 連結格式

```
izhuangzi://{host}?{params}
```

## 篇目與作者

| URL | 打開 |
|-----|------|
| `izhuangzi://passage?id={id}` | 篇目詳情 |
| `izhuangzi://saying?id={id}` / `izhuangzi://couplet?id={id}` / `izhuangzi://poem?id={id}` | 同詳情（相容別名） |
| `izhuangzi://passage?id={id}&card=1` | 詳情並彈出逍遙卡 |
| `izhuangzi://card?id={id}` / `izhuangzi://share-card?id={id}` | 逍遙卡 |
| `izhuangzi://author?id={id}` | 作者詳情 |
| `izhuangzi://recite` / `izhuangzi://recite?id={id}` | 誦讀 |

## 發現與學堂

| URL | 打開 |
|-----|------|
| `izhuangzi://home` | 首頁 |
| `izhuangzi://daily` | 今日一子 |
| `izhuangzi://random` | 隨機篇目 |
| `izhuangzi://favorites` | 收藏 |
| `izhuangzi://famous` | 金句 |
| `izhuangzi://search` / `izhuangzi://search?q={query}` | 搜尋 |
| `izhuangzi://study` / `izhuangzi://study?id={id}` | 莊學學堂 |
| `izhuangzi://hunt` | 尋莊（`keyword-hunt` / `flyflower`） |
| `izhuangzi://handwriting` | 手寫搜尋（`handwrite`；iOS） |
| `izhuangzi://mastered` | 已掌握（`progress`） |
| `izhuangzi://categories` / `izhuangzi://categories?section=` | 分類瀏覽 |
| `izhuangzi://collection?id=` | 合集 / 典籍（`neipian` / `waipian` / `zapian`） |
| `izhuangzi://corpus` | 全部篇目（`all`） |
| `izhuangzi://last-read` | 最近閱讀 |
| `izhuangzi://reading-history` | 閱讀歷史 |
| `izhuangzi://notes` | 筆記 |
| `izhuangzi://ask` | 問莊子 |
| `izhuangzi://allegories` | 寓言 |
| `izhuangzi://concepts` | 概念 |
| `izhuangzi://theme?id=neipian` | 內篇 / 外篇 / 雜篇 |

## 設定與指南

| URL | 打開 |
|-----|------|
| `izhuangzi://settings` | 設定 |
| `izhuangzi://usage-guide` | 使用說明 |
| `izhuangzi://widget-guide` | 小工具指南 |
| `izhuangzi://shortcuts-guide` | 捷徑指南 |
| `izhuangzi://feature-guide` | 重播功能引導 |
| `izhuangzi://feedback` | 回饋郵件 |
| `izhuangzi://in-app-review` | 應用內評價入口 |

## 範例

```
izhuangzi://daily
izhuangzi://passage?id=1
izhuangzi://ask
izhuangzi://allegories
izhuangzi://collection?id=neipian
izhuangzi://study
izhuangzi://hunt
```

## 說明

- 數字 ID 參數區分大小寫。
- Siri、捷徑、小工具與控制中心使用同一套深鏈。
- 最新列表見應用內 **設定 → 說明**。

</section>
<section lang="ja" markdown="1">

iZhuangZiは** `izhuangzi://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
izhuangzi://{host}?{params}
```


## パスポートと著者

| URL | 開く画面 |
|-----|-------|
| `izhuangzi://passage?id={id}` | 章句の詳細 |
| `izhuangzi://saying?id={id}` / `izhuangzi://couplet?id={id}` / `izhuangzi://poem?id={id}` | 通路と同じ(互換性) |
| `izhuangzi://passage?id={id}&card=1` | 通路の細部およびカード シート |
| `izhuangzi://card?id={id}` / `izhuangzi://share-card?id={id}` | クレジットカード |
| `izhuangzi://author?id={id}` | 作者の詳細 |
| `izhuangzi://recite` / `izhuangzi://recite?id={id}` | 誦読フロー |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `izhuangzi://home` | ホーム |
| `izhuangzi://daily` | 毎日のZhuangzi |
| `izhuangzi://random` | ランダムな章句 |
| `izhuangzi://favorites` | お気に入り |
| `izhuangzi://famous` | 名句一覧 |
| `izhuangzi://search` / `izhuangzi://search?q={query}` | 検索 |
| `izhuangzi://study` / `izhuangzi://study?id={id}` | 大夫研究 |
| `izhuangzi://hunt` | チュアン・ハント (`keyword-hunt`/`flyflower`) |
| `izhuangzi://handwriting` | 手書き検索 (`handwrite`; iOS) |
| `izhuangzi://mastered` | マスタード (`progress`) |
| `izhuangzi://categories` / `izhuangzi://categories?section=` | ブラウズ |
| `izhuangzi://collection?id=` | コレクション / ブック (`neipian`/`waipian`/`zapian`) |
| `izhuangzi://corpus` | すべての通路 (`all`) |
| `izhuangzi://last-read` | 最後に読んだ項目 |
| `izhuangzi://reading-history` | 閲覧履歴 |
| `izhuangzi://notes` | ノート |
| `izhuangzi://ask` | お問い合わせ |
| `izhuangzi://allegories` | パナブル |
| `izhuangzi://concepts` | コンセプト |
| `izhuangzi://theme?id=neipian` | インナー・アウター・その他 |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `izhuangzi://settings` | 設定 |
| `izhuangzi://usage-guide` | 使い方ガイド |
| `izhuangzi://widget-guide` | ウィジェットガイド |
| `izhuangzi://shortcuts-guide` | ショートカットガイド |
| `izhuangzi://feature-guide` | オンボーディングの再生 |
| `izhuangzi://feedback` | フィードバックメール |
| `izhuangzi://in-app-review` | アプリ内／App Store レビュー |

## 例


```
izhuangzi://daily
izhuangzi://passage?id=1
izhuangzi://ask
izhuangzi://allegories
izhuangzi://collection?id=neipian
izhuangzi://study
izhuangzi://hunt
```


## ノート

- パラメータはIDが数値である場合感度です。
- シリ、ショートカット、ウィジェット、およびコントロールセンターコントロールは、同じディープリンクルートを使用します。
- 最新リストのアプリ内設定 → Help** ガイドを参照してください。

</section>
<section lang="ko" markdown="1">

iZhuangZi 지원 ** `izhuangzi://` ** 단축키 링크 (URL 계획). 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
izhuangzi://{host}?{params}
```


## 책임 & 저자

| URL | 열리는 화면 |
|-----|-------|
| `izhuangzi://passage?id={id}` | 구절 상세 |
| `izhuangzi://saying?id={id}` / `izhuangzi://couplet?id={id}` / `izhuangzi://poem?id={id}` | 통행과 같 ( 겸용성) |
| `izhuangzi://passage?id={id}&card=1` | 통행 세부사항과 카드 장 |
| `izhuangzi://card?id={id}` / `izhuangzi://share-card?id={id}` | 카드 |
| `izhuangzi://author?id={id}` | 작가 상세 |
| `izhuangzi://recite` / `izhuangzi://recite?id={id}` | 낭독 흐름 |

## 디스커버리 & 연습

| URL | 열리는 화면 |
|-----|-------|
| `izhuangzi://home` | 홈 |
| `izhuangzi://daily` | 매일 Zhuangzi |
| `izhuangzi://random` | 무작위 구절 |
| `izhuangzi://favorites` | 즐겨찾기 |
| `izhuangzi://famous` | 명구 목록 |
| `izhuangzi://search` / `izhuangzi://search?q={query}` | 검색 |
| `izhuangzi://study` / `izhuangzi://study?id={id}` | Dao 연구 |
| `izhuangzi://hunt` | 주앙 헌트 (`keyword-hunt`/`flyflower`) |
| `izhuangzi://handwriting` | Handwriting search (`handwrite`; iOS) |
| `izhuangzi://mastered` | 마스터 (`progress`) |
| `izhuangzi://categories` / `izhuangzi://categories?section=` | 둘러보기 |
| `izhuangzi://collection?id=` | 컬렉션/책 (`neipian`/`waipian`/`zapian`) |
| `izhuangzi://corpus` | 모든 통행 (`all`) |
| `izhuangzi://last-read` | 마지막으로 읽은 항목 |
| `izhuangzi://reading-history` | 읽기 기록 |
| `izhuangzi://notes` | 메모 |
| `izhuangzi://ask` | Zhuangzi 소개 |
| `izhuangzi://allegories` | 옵션 정보 |
| `izhuangzi://concepts` | 회사 소개 |
| `izhuangzi://theme?id=neipian` | 내부 / 외부 / 기타 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `izhuangzi://settings` | 설정 |
| `izhuangzi://usage-guide` | 사용 가이드 |
| `izhuangzi://widget-guide` | 위젯 가이드 |
| `izhuangzi://shortcuts-guide` | 단축어 가이드 |
| `izhuangzi://feature-guide` | 온보딩 다시 보기 |
| `izhuangzi://feedback` | 피드백 이메일 |
| `izhuangzi://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
izhuangzi://daily
izhuangzi://passage?id=1
izhuangzi://ask
izhuangzi://allegories
izhuangzi://collection?id=neipian
izhuangzi://study
izhuangzi://hunt
```


## 메모

- 매개 변수는 ID가 숫자인지 여부를 감지합니다.
- Siri, Shortcuts, 위젯 및 제어 센터 제어는 동일한 딥 링크 루트를 사용합니다.
- in-app**Settings → 도움말** 최신 목록 안내

</section>
<section lang="ru" markdown="1">

iZhuangZi поддерживает ярлыки ** `izhuangzi://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
izhuangzi://{host}?{params}
```


## Проходы и авторы

| URL | Открывает |
|-----|-------|
| `izhuangzi://passage?id={id}` | Страница отрывка |
| `izhuangzi://saying?id={id}` / `izhuangzi://couplet?id={id}` / `izhuangzi://poem?id={id}` | Совместимость (Compatibility) |
| `izhuangzi://passage?id={id}&card=1` | Детали проезда и карточный лист |
| `izhuangzi://card?id={id}` / `izhuangzi://share-card?id={id}` | карты |
| `izhuangzi://author?id={id}` | Страница автора |
| `izhuangzi://recite` / `izhuangzi://recite?id={id}` | Режим чтения вслух |

## Discovery & Practice

| URL | Открывает |
|-----|-------|
| `izhuangzi://home` | Главная |
| `izhuangzi://daily` | Daily Zhuangzi |
| `izhuangzi://random` | Случайный отрывок |
| `izhuangzi://favorites` | Избранное |
| `izhuangzi://famous` | Знаменитые строки |
| `izhuangzi://search` / `izhuangzi://search?q={query}` | Поиск |
| `izhuangzi://study` / `izhuangzi://study?id={id}` | Исследование Дао |
| `izhuangzi://hunt` | Чжуан Хант («охота за ключевыми словами» / «флайфлауэр») |
| `izhuangzi://handwriting` | Поиск почерка («handwrite»; iOS) |
| `izhuangzi://mastered` | Мастеринг («Прогресс») |
| `izhuangzi://categories` / `izhuangzi://categories?section=` | Обзор |
| `izhuangzi://collection?id=` | Коллекция/книга ('neipian'/ 'waipian'/'zapian') |
| `izhuangzi://corpus` | Все пассажи («All») |
| `izhuangzi://last-read` | Последнее прочитанное |
| `izhuangzi://reading-history` | История чтения |
| `izhuangzi://notes` | Заметки |
| `izhuangzi://ask` | Спроси у Чжуанци. |
| `izhuangzi://allegories` | Притчи |
| `izhuangzi://concepts` | Концепции |
| `izhuangzi://theme?id=neipian` | Внутренний / Внешний / Разное |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `izhuangzi://settings` | Настройки |
| `izhuangzi://usage-guide` | Руководство по использованию |
| `izhuangzi://widget-guide` | Руководство по виджетам |
| `izhuangzi://shortcuts-guide` | Руководство по «Командам» |
| `izhuangzi://feature-guide` | Повторное знакомство |
| `izhuangzi://feedback` | Письмо с отзывом |
| `izhuangzi://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
izhuangzi://daily
izhuangzi://passage?id=1
izhuangzi://ask
izhuangzi://allegories
izhuangzi://collection?id=neipian
izhuangzi://study
izhuangzi://hunt
```


## Заметки

- Параметры чувствительны к регистру, где идентификаторы являются числовыми.
- Siri, ярлыки, виджеты и элементы управления Центра управления используют одни и те же маршруты глубокой связи.
- Смотрите в приложении ** Настройки → Справочные руководства ** для последнего списка.

</section>
<section lang="th" markdown="1">

i Zhuang Zi รองรับ~ `izhuangzi://` BAR * ลิงก์ลัด (URL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
izhuangzi://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `izhuangzi://passage?id={id}` | รายละเอียดข้อความ |
| `izhuangzi://saying?id={id}` / `izhuangzi://couplet?id={id}` / `izhuangzi://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `izhuangzi://passage?id={id}&card=1` | รายละเอียดและนามบัตร |
| `izhuangzi://card?id={id}` / `izhuangzi://share-card?id={id}` | ○ การ์ด |
| `izhuangzi://author?id={id}` | รายละเอียดผู้แต่ง |
| `izhuangzi://recite` / `izhuangzi://recite?id={id}` | โฟลว์การท่อง |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `izhuangzi://home` | หน้าแรก |
| `izhuangzi://daily` | เดลีซ็องซี |
| `izhuangzi://random` | ข้อความแบบสุ่ม |
| `izhuangzi://favorites` | รายการโปรด |
| `izhuangzi://famous` | บรรทัดขึ้นชื่อ |
| `izhuangzi://search` / `izhuangzi://search?q={query}` | ค้นหา |
| `izhuangzi://study` / `izhuangzi://study?id={id}` | การ ศึกษา |
| `izhuangzi://hunt` | Zhuung Hunt ('คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน') |
| `izhuangzi://handwriting` | สืบค้นเมื่อเขียนด้วยมือ ('เขียนเอง'; OS) |
| `izhuangzi://mastered` | สําเร็จการศึกษาแล้ว ('รุก') |
| `izhuangzi://categories` / `izhuangzi://categories?section=` | เรียกดู |
| `izhuangzi://collection?id=` | คอลเลคชั่น / หนังสือ (อังกฤษ) |
| `izhuangzi://corpus` | ทุกช่อง (ทั้งหมด) |
| `izhuangzi://last-read` | รายการที่อ่านล่าสุด |
| `izhuangzi://reading-history` | ประวัติการอ่าน |
| `izhuangzi://notes` | บันทึก |
| `izhuangzi://ask` | ถามซ็องซี |
| `izhuangzi://allegories` | สี่เหลี่ยม |
| `izhuangzi://concepts` | จับภาพ |
| `izhuangzi://theme?id=neipian` | ภายใน / ภายนอก / เบ็ดเตล็ด |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `izhuangzi://settings` | การตั้งค่า |
| `izhuangzi://usage-guide` | คู่มือการใช้งาน |
| `izhuangzi://widget-guide` | คู่มือวิดเจ็ต |
| `izhuangzi://shortcuts-guide` | คู่มือทางลัด |
| `izhuangzi://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `izhuangzi://feedback` | อีเมลข้อเสนอแนะ |
| `izhuangzi://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
izhuangzi://daily
izhuangzi://passage?id=1
izhuangzi://ask
izhuangzi://allegories
izhuangzi://collection?id=neipian
izhuangzi://study
izhuangzi://hunt
```


## บันทึก

- พารามิเตอร์คือความไวของตัวเลข
- ไซรี, ทางลัด, วิดเจ็ต, และศูนย์ควบคุม ใช้เส้นทางลับเดียวกัน
- ดู In-appings-Cettings softs for the list ล่าสุด

</section>
<section lang="de" markdown="1">

iZhuangZi unterstützt ** `izhuangzi://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
izhuangzi://{host}?{params}
```


## Passagen & Autoren

| URL | Öffnet |
|-----|-------|
| `izhuangzi://passage?id={id}` | Passagen-Detail |
| `izhuangzi://saying?id={id}` / `izhuangzi://couplet?id={id}` / `izhuangzi://poem?id={id}` | Wie Passage (Kompatibilität) |
| `izhuangzi://passage?id={id}&card=1` | Angaben zum Durchgang und Kartenblatt |
| `izhuangzi://card?id={id}` / `izhuangzi://share-card?id={id}` | 逍遥 Karten |
| `izhuangzi://author?id={id}` | Autorendetail |
| `izhuangzi://recite` / `izhuangzi://recite?id={id}` | Rezitationsablauf |

## Entdeckung und Praxis

| URL | Öffnet |
|-----|-------|
| `izhuangzi://home` | Startseite |
| `izhuangzi://daily` | Tägliche Zhuangzi |
| `izhuangzi://random` | Zufällige Passage |
| `izhuangzi://favorites` | Favoriten |
| `izhuangzi://famous` | Berühmte Zeilen |
| `izhuangzi://search` / `izhuangzi://search?q={query}` | Suche |
| `izhuangzi://study` / `izhuangzi://study?id={id}` | Dao-Studie |
| `izhuangzi://hunt` | Zhuang Hunt (`keyword-hunt` / `flyflower`) |
| `izhuangzi://handwriting` | Handschriftsuche (`handwrite`; iOS) |
| `izhuangzi://mastered` | gemeistert („Fortschritt) |
| `izhuangzi://categories` / `izhuangzi://categories?section=` | Durchsuchen |
| `izhuangzi://collection?id=` | Sammlung/Buch (`neipian`/`waipian`/`zapian`) |
| `izhuangzi://corpus` | Alle Passagen (`all`) |
| `izhuangzi://last-read` | Zuletzt gelesen |
| `izhuangzi://reading-history` | Leseverlauf |
| `izhuangzi://notes` | Notizen |
| `izhuangzi://ask` | Fragen Sie Zhuangzi |
| `izhuangzi://allegories` | Gleichnisse |
| `izhuangzi://concepts` | Konzepte |
| `izhuangzi://theme?id=neipian` | Innerer / Äußerer / Verschiedenes |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `izhuangzi://settings` | Einstellungen |
| `izhuangzi://usage-guide` | Nutzungsanleitung |
| `izhuangzi://widget-guide` | Widget-Anleitung |
| `izhuangzi://shortcuts-guide` | Kurzbefehle-Anleitung |
| `izhuangzi://feature-guide` | Einführung erneut abspielen |
| `izhuangzi://feedback` | Feedback-E-Mail |
| `izhuangzi://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
izhuangzi://daily
izhuangzi://passage?id=1
izhuangzi://ask
izhuangzi://allegories
izhuangzi://collection?id=neipian
izhuangzi://study
izhuangzi://hunt
```


## Notizen

- Parameter sind fallsensibel, wo IDs numerisch sind.
- Siri, Shortcuts, Widgets und Control Center-Steuerelemente verwenden die gleichen Deep-Link-Routen.
- Sehen Sie sich die In-App **Einstellungen → Hilfe ** Anleitungen für die neueste Liste an.

</section>
<section lang="fr" markdown="1">

iZhuangZi prend en charge les liens de raccourci **   C   ** (système URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
izhuangzi://{host}?{params}
```


## Passages et auteurs

| URL | Ouvre |
|-----|-------|
| `izhuangzi://passage?id={id}` | Détail du passage |
| `izhuangzi://saying?id={id}` / `izhuangzi://couplet?id={id}` / `izhuangzi://poem?id={id}` | Même chose que le passage (compatibilité) |
| `izhuangzi://passage?id={id}&card=1` | Détails du passage et feuille de carte |
| `izhuangzi://card?id={id}` / `izhuangzi://share-card?id={id}` | Cartes |
| `izhuangzi://author?id={id}` | Détail de l’auteur |
| `izhuangzi://recite` / `izhuangzi://recite?id={id}` | Flux de récitation |

## Découverte et pratique

| URL | Ouvre |
|-----|-------|
| `izhuangzi://home` | Accueil |
| `izhuangzi://daily` | Zhuangzi quotidien |
| `izhuangzi://random` | Passage aléatoire |
| `izhuangzi://favorites` | Favoris |
| `izhuangzi://famous` | Vers célèbres |
| `izhuangzi://search` / `izhuangzi://search?q={query}` | Recherche |
| `izhuangzi://study` / `izhuangzi://study?id={id}` | Étude Dao |
| `izhuangzi://hunt` | Zhuang Hunt ( ' chasse aux mots clés ' / `flyflower ') |
| `izhuangzi://handwriting` | Recherche d'écriture (`handwrite`; iOS) |
| `izhuangzi://mastered` | Maîtrise ('progrès') |
| `izhuangzi://categories` / `izhuangzi://categories?section=` | Parcourir |
| `izhuangzi://collection?id=` | Collection / livre (`neipian` / `waipian` / `zapian`) |
| `izhuangzi://corpus` | Tous les passages |
| `izhuangzi://last-read` | Dernière lecture |
| `izhuangzi://reading-history` | Historique de lecture |
| `izhuangzi://notes` | Notes |
| `izhuangzi://ask` | Demandez à Zhuangzi |
| `izhuangzi://allegories` | Paraboles |
| `izhuangzi://concepts` | Concepts |
| `izhuangzi://theme?id=neipian` | Intérieur / Extérieur / Divers |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `izhuangzi://settings` | Réglages |
| `izhuangzi://usage-guide` | Guide d'utilisation |
| `izhuangzi://widget-guide` | Guide des widgets |
| `izhuangzi://shortcuts-guide` | Guide Raccourcis |
| `izhuangzi://feature-guide` | Rejouer l’accueil |
| `izhuangzi://feedback` | E-mail de commentaires |
| `izhuangzi://in-app-review` | Avis in-app / App Store |

## Exemples


```
izhuangzi://daily
izhuangzi://passage?id=1
izhuangzi://ask
izhuangzi://allegories
izhuangzi://collection?id=neipian
izhuangzi://study
izhuangzi://hunt
```


## Notes

- Les paramètres sont sensibles aux cas où les ID sont numériques.
- Les commandes Siri, Shortcuts, Widgets et Control Center utilisent les mêmes itinéraires de liaison profonde.
- Voir la page d'application **Paramètres → Aide** pour la dernière liste.

</section>
<section lang="tr" markdown="1">

iZhuangZi, ** `izhuangzi://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
izhuangzi://{host}?{params}
```


## Geçişler ve yazarlar

| URL | Açar |
|-----|-------|
| `izhuangzi://passage?id={id}` | Pasaj ayrıntısı |
| `izhuangzi://saying?id={id}` / `izhuangzi://couplet?id={id}` / `izhuangzi://poem?id={id}` | Aynı geçiş (compatability) |
| `izhuangzi://passage?id={id}&card=1` | Pasaj detay ve kart sayfası |
| `izhuangzi://card?id={id}` / `izhuangzi://share-card?id={id}` | kartları |
| `izhuangzi://author?id={id}` | Yazar ayrıntısı |
| `izhuangzi://recite` / `izhuangzi://recite?id={id}` | Okuma akışı |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `izhuangzi://home` | Ana sayfa |
| `izhuangzi://daily` | Daily Zhuangzi |
| `izhuangzi://random` | Rastgele pasaj |
| `izhuangzi://favorites` | Favoriler |
| `izhuangzi://famous` | Ünlü dizeler |
| `izhuangzi://search` / `izhuangzi://search?q={query}` | Ara |
| `izhuangzi://study` / `izhuangzi://study?id={id}` | Dao Study |
| `izhuangzi://hunt` | Zhuang Hunt ('keyword-hunt' / 'flyflower') |
| `izhuangzi://handwriting` | Hand writing search ('handwrite'; iOS) |
| `izhuangzi://mastered` | Mastered ('progress') |
| `izhuangzi://categories` / `izhuangzi://categories?section=` | Gözat |
| `izhuangzi://collection?id=` | Collection / book ('neipian' / "waipian' / "zapian") |
| `izhuangzi://corpus` | Bütün geçitler ('all') |
| `izhuangzi://last-read` | Son okunan |
| `izhuangzi://reading-history` | Okuma geçmişi |
| `izhuangzi://notes` | Notlar |
| `izhuangzi://ask` | Zhuangzi |
| `izhuangzi://allegories` | Parables |
| `izhuangzi://concepts` | Kavramlar |
| `izhuangzi://theme?id=neipian` | İç / Dış / Miscellane |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `izhuangzi://settings` | Ayarlar |
| `izhuangzi://usage-guide` | Kullanım kılavuzu |
| `izhuangzi://widget-guide` | Widget kılavuzu |
| `izhuangzi://shortcuts-guide` | Kısayol kılavuzu |
| `izhuangzi://feature-guide` | Tanıtımı yeniden oynat |
| `izhuangzi://feedback` | Geri bildirim e-postası |
| `izhuangzi://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
izhuangzi://daily
izhuangzi://passage?id=1
izhuangzi://ask
izhuangzi://allegories
izhuangzi://collection?id=neipian
izhuangzi://study
izhuangzi://hunt
```


## Notlar

- Parametreler, kimliklerin sayısal olduğu durumlarda hassastır.
- Siri, Shortcuts, widgets ve Control Center kontrolleri aynı derin bağlantı yollarını kullanır.
- In-app **Settings → Yardım** en son liste için kılavuzlar.

</section>
