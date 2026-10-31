---
layout: doc
title: iCangJie — URL Scheme Reference
app_id: iCangJie
doc_title_en: URL Scheme Reference
doc_title_zh_cn: URL Scheme 深度链接文档
doc_title_zh_tw: URL Scheme 深度連結文件
description: Complete reference of iCangJie:// deep links and Home Screen Quick Actions.
---

<section lang="en" markdown="1">

iCangJie supports **`iCangJie://`** URL scheme deep links — open Lookup search, word detail, Daily Quiz, Typing, Favorites, Wrong Book, Levels, or Learn from Safari, another app, a QR code, a widget tap, or Apple Shortcuts.

A parallel set of **Home Screen Quick Actions** (long-press the app icon) covers additional destinations such as Search, Feedback, and Rate. Configure up to 4 shortcuts in **Settings → App Settings → Home Screen shortcuts**.

## Protocol Specification

```
iCangJie://<host>[?query]
```

| Rule | Detail |
|------|--------|
| **Scheme** | `icangjie` / `iCangJie` — compared case-insensitively |
| **Host routing** | Primary router is the URL **host** |
| **Query aliases** | `q`, `word`, and `name` are interchangeable for search/word hosts |
| **Parser** | `ICangJieDeepLink.parse(_:)` — consumed via `onOpenURL` → `AppRouter.pendingDeepLink` |

**Three delivery channels**

| Channel | Handled by | Examples |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ICangJieDeepLink.parse` → `RootTabView` | `search`, `word`, `quiz`, `typing`, `favorites`, `wrong`, `levels`, `learn` |
| **Home Screen Quick Action** | `ShortcutObserver.dispatch` | `search`, `quiz`, `favorites`, `wrong`, `levels`, `feedback`, `review` |
| **App Intents / Siri / Widget pending URL** | Writes `AppGroup.pendingDeepLinkURL` → `RootTabView.consumePendingDeepLinkFromAppGroup()` | Lookup code, start quiz, open search |

Quick-action types use **`contains`** matching on the type string, so both `iCangJie://feedback` and legacy variants still route correctly.

---

## 1. Lookup Search

Open the **Lookup** tab. Optionally pre-fill the search field.

| Parameter | Required | Description |
|-----------|----------|-------------|
| `q` | No | Search query (code prefix, character, pinyin, or Jyutping) |
| `word` | No | Synonym for `q` |
| `name` | No | Synonym for `q` |

**Open Lookup (empty search)**

```
iCangJie://search
```

**Search for code prefix `ab`**

```
iCangJie://search?q=ab
```

**Search for character 颉**

```
iCangJie://search?q=颉
```

---

## 2. Word Detail

Open the detail page for a single character. Requires a non-empty query.

| Parameter | Required | Description |
|-----------|----------|-------------|
| `q` | One of `q` / `word` / `name` | Target Han character |
| `word` | One of `q` / `word` / `name` | Synonym for `q` |
| `name` | One of `q` / `word` / `name` | Synonym for `q` |

**Hosts accepted:** `word`, `char`, `character`

**Open detail for 倉**

```
iCangJie://word?q=倉
```

Alternate host:

```
iCangJie://character?word=颉
```

If the query is **empty or the character is not in the dictionary**, the link is **silently ignored**.

---

## 3. Daily Quiz

Jump directly to the **Daily Quiz**. Does not auto-start or skip questions.

```
iCangJie://quiz
```

Aliases: `test`

---

## 4. Typing Practice

Open the **Typing** tab hub.

```
iCangJie://typing
```

Aliases: `type`, `practice`

---

## 5. Favorites

Open the **Favorites** list.

```
iCangJie://favorites
```

Alias: `favorite`

---

## 6. Wrong Answer Book

### 6.1 List

Open the **Wrong Answer Book** list.

```
iCangJie://wrong
```

Aliases: `mistakes`, `wrongbook`

### 6.2 Single record

When `record` is a valid UUID of a saved wrong-answer entry, the app opens that record's word detail (if the record still exists).

| Parameter | Required | Format |
|-----------|----------|--------|
| `record` | Yes | UUID string |
| `id` | Yes | Synonym for `record` |

```
iCangJie://wrong?record=550e8400-e29b-41d4-a716-446655440000
```

---

## 7. Levels (Code Length)

Open the **Levels** tab.

```
iCangJie://levels
```

Aliases: `level`, `codes`

---

## 8. Learn (Tutorials)

Open the **Learn** hub.

```
iCangJie://learn
```

Aliases: `study`

---

## 9. Feedback (Quick Action only)

Open the pre-filled feedback email composer (or `mailto:` fallback).

```
iCangJie://feedback
```

Handled by **Home Screen Quick Action** / `ShortcutObserver`, not `ICangJieDeepLink.parse`.

---

## 10. App Store Review (Quick Action only)

Request an in-app App Store review prompt.

```
iCangJie://review
```

Alias matching also accepts `star` in the quick-action type string.

---

## 11. App Intents & Siri (iOS 16+)

Built-in **App Shortcuts** appear in the Shortcuts app and Siri. Each intent sets `pendingDeepLinkURL` in the App Group; the app consumes it on launch.

| Intent | Action | Pending URL |
|--------|--------|-------------|
| **Look up Cangjie code** | Opens word detail for the given character | `iCangJie://word?q=<char>` |
| **Start daily quiz** | Opens Daily Quiz | `iCangJie://quiz` |
| **Open lookup search** | Opens Lookup tab | `iCangJie://search` |

**Example Siri phrases (English)**

- *"Look up Cangjie code for 颉 in iCangJie"*
- *"Start daily quiz in iCangJie"*
- *"Search Cangjie in iCangJie"*

In **Shortcuts**, add the action from the iCangJie app section. The **Look up** intent requires a **Chinese character** parameter (`ChineseCharacterEntity`).

> App Intents are **iOS only**. macOS relies on `iCangJie://` URLs and menu navigation.

---

## Widget Deep Links

Widgets tap through the same `iCangJie://` URLs. Examples:

| Widget | Typical URL |
|--------|-------------|
| Daily Character | `iCangJie://word?q=<char>` |
| Code Length | `iCangJie://levels` |
| Daily Quiz | `iCangJie://quiz` |
| Typing Glance | `iCangJie://typing` |
| Favorites | `iCangJie://favorites` |
| Wrong Book | `iCangJie://wrong` |
| Recent | `iCangJie://search` |
| Learning Progress | `iCangJie://learn` |

---

## Shortcuts Examples

**Open today's quiz**

```
iCangJie://quiz
```

**Look up a character from clipboard**

Use a Shortcuts **Get Clipboard** action, then **Open URL** with:

```
iCangJie://word?q=[Clipboard]
```

**Start typing practice**

```
iCangJie://typing
```

---

## Home Screen Quick Actions

Long-press the iCangJie app icon. Default options (pick up to 4 in Settings):

| Action | URL |
|--------|-----|
| Search | `iCangJie://search` |
| Daily Quiz | `iCangJie://quiz` |
| Favorites | `iCangJie://favorites` |
| Wrong Book | `iCangJie://wrong` |
| Code Length | `iCangJie://levels` |
| Feedback | `iCangJie://feedback` |
| Rate App | `iCangJie://review` |

</section>
<section lang="zh-CN" markdown="1">

爱仓颉支持 **`iCangJie://`** 深度链接——从 Safari、其他应用、二维码、小组件点击或快捷指令打开查字、字词详情、每日测验、打字、收藏、错题本、码长或学习等页面。

**主屏快捷操作**（长按应用图标）还可打开搜索、反馈、评分等入口。在 **设置 → 应用设置 → 主屏快捷操作** 中自选最多 4 项。

## 协议规范

```
iCangJie://<host>[?query]
```

| 规则 | 说明 |
|------|------|
| **Scheme** | `icangjie` / `iCangJie`，大小写不敏感 |
| **路由** | 以 URL **host** 为主 |
| **查询别名** | `q`、`word`、`name` 可互换 |
| **解析器** | `ICangJieDeepLink.parse` → `AppRouter.pendingDeepLink` |

**三种投递渠道**

| 渠道 | 处理方 | 示例 |
|------|--------|------|
| **通用深链**（`onOpenURL`） | `ICangJieDeepLink.parse` | `search`、`word`、`quiz`、`typing` 等 |
| **主屏快捷操作** | `ShortcutObserver.dispatch` | `search`、`feedback`、`review` 等 |
| **App Intents / Siri** | 写入 App Group → `RootTabView` 消费 | 查码、开测验、打开查字 |

---

## 1. 查字搜索

打开 **查字** Tab，可选预填搜索词。

| 参数 | 必填 | 说明 |
|------|------|------|
| `q` | 否 | 搜索内容（码前缀、汉字、拼音或粤拼） |
| `word` / `name` | 否 | `q` 的同义词 |

```
iCangJie://search
iCangJie://search?q=ab
iCangJie://search?q=颉
```

---

## 2. 字词详情

打开单个汉字的详情页，查询参数不可为空。

| 参数 | 必填 | 说明 |
|------|------|------|
| `q` / `word` / `name` | 其一必填 | 目标汉字 |

**Host：** `word`、`char`、`character`

```
iCangJie://word?q=倉
iCangJie://character?word=颉
```

查询为空或字不在字典中时，链接会被**静默忽略**。

---

## 3. 每日测验

```
iCangJie://quiz
```

别名：`test`

---

## 4. 打字练习

```
iCangJie://typing
```

别名：`type`、`practice`

---

## 5. 收藏

```
iCangJie://favorites
```

---

## 6. 错题本

### 列表

```
iCangJie://wrong
```

别名：`mistakes`、`wrongbook`

### 单条记录

```
iCangJie://wrong?record=<UUID>
```

参数 `id` 为 `record` 的同义词。

---

## 7. 码长

```
iCangJie://levels
```

---

## 8. 学习（教程）

```
iCangJie://learn
```

---

## 9. 反馈（仅快捷操作）

```
iCangJie://feedback
```

打开预填反馈邮件（或 `mailto:` 回退）。

---

## 10. App Store 评分（仅快捷操作）

```
iCangJie://review
```

---

## 11. App Intents 与 Siri（iOS 16+）

| 意图 | 作用 | 待处理 URL |
|------|------|------------|
| **查仓颉码** | 打开字词详情 | `iCangJie://word?q=<字>` |
| **开始每日测验** | 打开测验 | `iCangJie://quiz` |
| **打开查字** | 打开查字 Tab | `iCangJie://search` |

可对 Siri 说：「在爱仓颉查 颉 的仓颉码」「在爱仓颉开始每日测验」。仅 **iOS** 支持。

---

## 小组件深链

| 小组件 | 典型 URL |
|--------|----------|
| 今日一字 | `iCangJie://word?q=<字>` |
| 码长精选 | `iCangJie://levels` |
| 每日测验 | `iCangJie://quiz` |
| 打字一览 | `iCangJie://typing` |
| 收藏 | `iCangJie://favorites` |
| 错题 | `iCangJie://wrong` |
| 最近浏览 | `iCangJie://search` |
| 学习进度 | `iCangJie://learn` |

---

## 快捷指令示例

**打开今日测验**

```
iCangJie://quiz
```

**查剪贴板中的字**

获取剪贴板 → 打开 URL：`iCangJie://word?q=[剪贴板]`

**开始打字练习**

```
iCangJie://typing
```

---

## 主屏快捷操作

长按爱仓颉图标，可在设置中自选最多 4 项：

| 操作 | URL |
|------|-----|
| 搜索 | `iCangJie://search` |
| 每日测验 | `iCangJie://quiz` |
| 收藏 | `iCangJie://favorites` |
| 错题本 | `iCangJie://wrong` |
| 码长 | `iCangJie://levels` |
| 反馈 | `iCangJie://feedback` |
| 评分 | `iCangJie://review` |

</section>
<section lang="zh-TW" markdown="1">

愛倉頡支援 **`iCangJie://`** 深度連結——從 Safari、其他應用、QR Code、小工具點擊或捷徑開啟查字、字詞詳情、每日測驗、打字、收藏、錯題本、碼長或學習等頁面。

**主畫面快速操作**（長按應用圖示）還可開啟搜尋、回饋、評分等入口。在 **設定 → 應用設定 → 主畫面快捷操作** 中自選最多 4 項。

## 協議規範

```
iCangJie://<host>[?query]
```

| 規則 | 說明 |
|------|------|
| **Scheme** | `icangjie` / `iCangJie`，大小寫不敏感 |
| **路由** | 以 URL **host** 為主 |
| **查詢別名** | `q`、`word`、`name` 可互換 |

---

## 常用路徑

| 功能 | URL |
|------|-----|
| 查字 | `iCangJie://search` 或 `?q=...` |
| 字詞詳情 | `iCangJie://word?q=倉` |
| 每日測驗 | `iCangJie://quiz` |
| 打字練習 | `iCangJie://typing` |
| 收藏 | `iCangJie://favorites` |
| 錯題本 | `iCangJie://wrong` |
| 錯題記錄 | `iCangJie://wrong?record=<UUID>` |
| 碼長 | `iCangJie://levels` |
| 學習 | `iCangJie://learn` |
| 回饋 | `iCangJie://feedback` |
| 評分 | `iCangJie://review` |

---

## 小工具深鏈

| 小工具 | 典型 URL |
|--------|----------|
| 每日一字 | `iCangJie://word?q=<字>` |
| 碼長精選 | `iCangJie://levels` |
| 每日測驗 | `iCangJie://quiz` |
| 打字一覽 | `iCangJie://typing` |
| 收藏 | `iCangJie://favorites` |
| 錯題 | `iCangJie://wrong` |
| 最近瀏覽 | `iCangJie://search` |
| 學習進度 | `iCangJie://learn` |

---

## 主畫面快速操作

| 操作 | URL |
|------|-----|
| 搜尋 | `iCangJie://search` |
| 每日測驗 | `iCangJie://quiz` |
| 收藏 | `iCangJie://favorites` |
| 錯題本 | `iCangJie://wrong` |
| 碼長 | `iCangJie://levels` |
| 回饋 | `iCangJie://feedback` |
| 評分 | `iCangJie://review` |

---

## App Intents 與 Siri（iOS 16+）

| 意圖 | 作用 |
|------|------|
| 查倉頡碼 | `iCangJie://word?q=<字>` |
| 開始每日測驗 | `iCangJie://quiz` |
| 開啟查字 | `iCangJie://search` |

僅 **iOS** 支援；macOS 請用 `iCangJie://` URL。

</section>
<section lang="ja" markdown="1">

iCangJieは** `iCangJie://` **をサポートしています URLスキームの深いリンク — 参照検索、単語詳細、毎日のクイズ、タイピング、お気に入り、間違ったブック、レベル、またはSafari、別のアプリ、QRコード、ウィジェットタップ、またはAppleショートカットから学びます。

**ホーム画面クイックアクション**(アプリのアイコンを長押し)の並列セットは、検索、フィードバック、およびレートなどの追加の目的地をカバーしています。 *Settings → App Settings → Home Screen Shortcuts**で最大4つのショートカットを設定します。

## プロトコル仕様


```
iCangJie://<host>[?query]
```


| Rule | 詳細を見る |
|------|--------|
| **Scheme** | `icangjie`/`iCangJie` — ケースを無感覚に比較 |
| **Host routing** | プライマリルータはURL **ホスト**です。 |
| **Query aliases** | `q`, `word`, `name` は、検索/単語のホストに交換可能 |
| **Parser** | `ICangJieDeepLink.parse( :)` — を `onOpenURL` → `AppRouter.pendingDeepLink` 経由で消費 |

**3つの配達チャネル**

| Channel | Handled by | 例 |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ICangJieDeepLink.parse` → `RootTabView` | `search`、`word`、`quiz`、`typing`、`favorites`、`wrong`、`levels`、`learn` |
| **Home Screen Quick Action** | `ShortcutObserver.dispatch` | `search`、`quiz`、`favorites`、`wrong`、`levels`、`feedback`、`review` |
| **App Intents / Siri / Widget pending URL** | Writes `AppGroup.pendingDeepLinkURL` → `RootTabView.consumePendingDeepLinkFromAppGroup()` | ルックアップコード、クイズ、オープン検索を開始 |

クイックアクションタイプは、タイプ文字列にマッチする** `iCangJie://` **を使うので、 `icangjie` とレガシーのバリアントも正しくルーティングします。

---

## 1. 探査検索

**Lookup**タブを開きます。 オプションで、検索フィールドを事前に入力します。

| Parameter | Required | コンテンツ |
|-----------|----------|-------------|
| `q` | No | 検索クエリ(コードプレフィックス、文字、ピンイン、またはJyutping) |
| `word` | No | `q` の同義語 |
| `name` | No | `q` の同義語 |

**Lookup(空検索)を開く**


```
iCangJie://search
```


**コード接頭辞の検索 `iCangJie://` **


```
iCangJie://search?q=ab
```


**キャラクター検索**


```
iCangJie://search?q=颉
```


---

## 2. 単語の細部

1つの文字の詳細はページを開きます。 非空のクエリが必要です。

| Parameter | Required | コンテンツ |
|-----------|----------|-------------|
| `q` | One of `q` / `word` / `name` | ターゲットハンキャラ |
| `word` | One of `q` / `word` / `name` | `q` の同義語 |
| `name` | One of `q` / `word` / `name` | `q` の同義語 |

**主催:** `iCangJie://` , `icangjie` , `iCangJie` ** KURA のオープンディテール**


```
iCangJie://word?q=倉
```


代替ホスト:


```
iCangJie://character?word=颉
```


クエリが **empty または文字が辞書にない場合**、リンクは無視されます**。

---

## 3. 毎日のクイズ

**デイリークイズ**に直接ジャンプします。 質問を自動起動またはスキップしません。


```
iCangJie://quiz
```


別名で: `iCangJie://` ---

## 4. タイピング練習

**Typing**タブハブを開きます。


```
iCangJie://typing
```


別名で: `iCangJie://` 、 `icangjie` ---

## 5.お気に入り

**お気に入り**リストを開きます。


```
iCangJie://favorites
```


別名で: `iCangJie://` ---

## 6. 間違った答えの本

### 6.1 リスト

**間違った回答ブック**リストを開きます。


```
iCangJie://wrong
```


別名で: `iCangJie://` 、 `icangjie` ### 6.2 シングルレコード `iCangJie://` が保存された不備なエントリの有効な UUID である場合、このアプリはレコードの単語の詳細(レコードがまだ存在する場合)を開きます。

| Parameter | Required | フォーマット |
|-----------|----------|--------|
| `record` | Yes | UUID 文字列 |
| `id` | Yes | `record` の同義語 |


```
iCangJie://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


---

## 7. レベル(コードの長さ)

**Levels**タブを開きます。


```
iCangJie://levels
```


別名で: `iCangJie://` 、 `icangjie` ---

## 8. 学習(チュートリアル)

**Learn** ハブを開きます。


```
iCangJie://learn
```


別名で: `iCangJie://` ---

## 9. フィードバック(クイックアクションのみ)

プレフィルドフィードバックメールコンポーザー(または `iCangJie://` フォールバック)を開きます。


```
iCangJie://feedback
```


**ホーム画面クイックアクション** / `iCangJie://` , `icangjie` ではなく、処理

---

## 10. アプリストアレビュー(クイックアクションのみ)

アプリ内 App Store レビュー プロンプトをリクエストします。


```
iCangJie://review
```


Alias マッチングは、クイックアクション型の文字列で `iCangJie://` も受け付けます。

---

## 11. アプリの意図とシリ (iOS 16 +)

内蔵**Appショートカット**はショートカットアプリとシリに表示されます。 各インテントは、App Group で `iCangJie://` をセットします。アプリは起動時に消費します。

| Intent | Action | 送信URL |
|--------|--------|-------------|
| **Look up Cangjie code** | Opens word detail for the given character | iCangJie://word?q=<char>` |
| **Start daily quiz** | Opens Daily Quiz | 「iCangJie://quiz」 |
| **Open lookup search** | Opens Lookup tab | 「iCangJie://search」 |

**シリフレーズ例(英語)**

- *「Cangjieコードを調べる」*
- *「iCangJieで日々のクイズを始める」*
- *「iCangJieでカンジエを検索」*

**ショートカット**で、iCangJieアプリセクションからアクションを追加します。 **Look up** は、** 中国語文字** パラメータ ( `iCangJie://` ) が必要です。

> App Intents は、**iOS のみです。 macOS は `iCangJie://` の URL とメニューのナビゲーションに依存しています。

---

## ウィジェットディープリンク

ウィジェットは同じ `iCangJie://` の URL をタップします。 例:

| Widget | 典型的な URL |
|--------|-------------|
| Daily Character | iCangJie://word?q=<char>` |
| Code Length | 「iCangJie://levels」 |
| Daily Quiz | 「iCangJie://quiz」 |
| Typing Glance | iCangJie://タイピング |
| Favorites | 「iCangJie」 http://favorites」 |
| Wrong Book | 「iCangJie://wrong」 |
| Recent | 「iCangJie://search」 |
| Learning Progress | 「iCangJie」 http://learn` |

---

## ショートカット例

**今日のクイズを開く**


```
iCangJie://quiz
```


**クリップボードからキャラクターを見る**

Shortcuts **Get Clipboard** アクションを使用して、** URL** を以下で開きます。


```
iCangJie://word?q=[Clipboard]
```


**タイピング練習を開始**


```
iCangJie://typing
```


---

## ホーム スクリーンの速い行為

iCangJieアプリアイコンを長押しします。 デフォルトオプション(設定で最大4つを選択):

| Action | サイトマップ |
|--------|-----|
| Search | 「iCangJie://search」 |
| Daily Quiz | 「iCangJie://quiz」 |
| Favorites | 「iCangJie」 http://favorites」 |
| Wrong Book | 「iCangJie://wrong」 |
| Code Length | 「iCangJie://levels」 |
| Feedback | 「iCangJie://feedback」 |
| Rate App | 「iCangJie://review」 |

</section>
<section lang="ko" markdown="1">

iCangJie 지원 ** `iCangJie://` ** URL 계획 딥 링크 — 오픈 검색, 워드 세부 사항, 매일 퀴즈, 타이핑, 즐겨찾기, 잘못된 책, 레벨, 또는 사파리에서 배울, 또 다른 응용 프로그램, QR 코드, 위젯 탭, 또는 애플 단축키.

홈 화면 Quick Actions** (앱 아이콘을 길게 누르십시오)의 병렬 세트는 검색, 피드백 및 비율과 같은 추가 목적지를 포함합니다. **Settings → App Settings → Home Screen Shortcuts**에서 최대 4개의 단축키 구성

## 프로토콜


```
iCangJie://<host>[?query]
```


| Rule | 제품 정보 |
|------|--------|
| **Scheme** | `icangjie`/`iCangJie` — case-insensitively 비교 |
| **Host routing** | 기본 라우터는 URL ** 호스팅 ** |
| **Query aliases** | `q`, `word`, `name`는 검색/word 호스트의 교환이 가능합니다. |
| **Parser** | `ICangJieDeepLink.parse( :)` - `onOpenURL` → `AppRouter.pendingDeepLink`를 통해 소모 |

** 3 배달 채널 **

| Channel | Handled by | 예시 |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ICangJieDeepLink.parse` → `RootTabView` | `search`, `word`, `quiz`, `typing`, `favorites`, `wrong`, `level`, `learn` |
| **Home Screen Quick Action** | `ShortcutObserver.dispatch` | `search`, `quiz`, `favorites`, `wrong`, `level`, `feedback`, `review` |
| **App Intents / Siri / Widget pending URL** | Writes `AppGroup.pendingDeepLinkURL` → `RootTabView.consumePendingDeepLinkFromAppGroup()` | 조회 코드, 시작 퀴즈, 열린 검색 |

Quick-action type use ** `iCangJie://` ** type string에 매칭하므로, `icangjie` 와 레거시 변형은 여전히 올바르게 변형됩니다.

---

## 1. 조회 수

**Lookup** 탭을 엽니다. 선택적으로 사전 채우기 검색 필드.

| Parameter | Required | 이름 * |
|-----------|----------|-------------|
| `q` | No | 검색 쿼리 (코드 접두사, 문자, pinyin, 또는 Jyutping) |
| `word` | No | `q`를 위한 동의어 |
| `name` | No | `q`를 위한 동의어 |

**Open Lookup (비어 있는 검색)**


```
iCangJie://search
```


**코드 접두사 검색 `iCangJie://` **


```
iCangJie://search?q=ab
```


** 캐릭터 검색 **


```
iCangJie://search?q=颉
```


---

## 2. Word 세부사항

단일 문자에 대한 세부 페이지를 엽니다. 비empty 쿼리가 필요합니다.

| Parameter | Required | 이름 * |
|-----------|----------|-------------|
| `q` | One of `q` / `word` / `name` | 대상 Han 캐릭터 |
| `word` | One of `q` / `word` / `name` | `q`를 위한 동의어 |
| `name` | One of `q` / `word` / `name` | `q`를 위한 동의어 |

** 허용 호스트 : ** `iCangJie://` , `icangjie` , `iCangJie` **에 대한 세부 정보 **


```
iCangJie://word?q=倉
```


Alternate 호스트:


```
iCangJie://character?word=颉
```


쿼리가 **empty 또는 문자가 사전 **에 있지 않은 경우, 링크는 ** 분명히 무시 **.

---

## 3. 매일 퀴즈

**Daily Quiz**에 직접 점프하십시오. 자동 시작 또는 건너뛰기 질문은 없습니다.


```
iCangJie://quiz
```


Aliases : `iCangJie://` ---

## 4. 타이핑 연습

** 타이핑** 탭 허브를 엽니다.


```
iCangJie://typing
```


Aliases : `iCangJie://` , `icangjie` ---

## 5. 즐겨찾기

** 즐겨 찾기 ** 목록.


```
iCangJie://favorites
```


별명으로: `iCangJie://` ---

## 6. 잘못된 대답 책

### 6.1 목록

** 잘못된 답변 책 ** 목록.


```
iCangJie://wrong
```


Aliases : `iCangJie://` , `icangjie` ### 6.2 단 하나 기록

언제 `iCangJie://` 는 저장 된 잘못 answer 항목의 유효 UUID, 응용 프로그램은 기록의 단어 세부 사항 (기록이 여전히 존재하는 경우)를 엽니 다.

| Parameter | Required | 지원하다 |
|-----------|----------|--------|
| `record` | Yes | UUID 문자열 |
| `id` | Yes | `record`를 위한 동의어 |


```
iCangJie://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


---

## 7. 수준 (코드 길이)

**Levels** 탭을 엽니다.


```
iCangJie://levels
```


Aliases : `iCangJie://` , `icangjie` ---

## 8. 알아보기 (Tutorials)

**Learn** 허브를 엽니다.


```
iCangJie://learn
```


Aliases : `iCangJie://` ---

## 9. 의견 (빠른 행동 전용)

사전 채워진 피드백 이메일 작곡가 (또는 `iCangJie://` fallback)를 엽니다.


```
iCangJie://feedback
```


으로 처리 **홈 화면 빠른 행동** / `iCangJie://` , 아니 `icangjie` .

---

## 10. App Store Review (빠른 행동 만)

in-app App Store 검토를 취소하십시오.


```
iCangJie://review
```


Alias matching also accepts `iCangJie://` 빠른 액션 타입 문자열.

---

## 11. 앱 의도 및 Siri (iOS 16+)

Built-in **App Shortcuts**는 Shortcuts 앱과 Siri에 나타났습니다. App Group의 각 intent set `iCangJie://` ; 앱은 출시에 소비합니다.

| Intent | Action | URL을 종료 |
|--------|--------|-------------|
| **Look up Cangjie code** | Opens word detail for the given character | `iCangJie://word?q=<char>```` |
| **Start daily quiz** | Opens Daily Quiz | `iCangJie://quiz``````` |
| **Open lookup search** | Opens Lookup tab | `iCangJie://search``````` |

**Example Siri 구문 (영어) **

- * "iCangJie"*에서  for에 대한 Cangjie 코드를 봐
- * "iCangJie에서 매일 퀴즈 시작"*
- * "iCangJie에서 검색 Cangjie"*

**Shortcuts**에서 iCangJie 앱 섹션에서 동작을 추가합니다. **Look up** intent는 **중국어 문자** 매개변수( `iCangJie://` )를 요구합니다.

> App Intents는 **iOS 만 **입니다. macOS는 `iCangJie://` URL 및 메뉴 네비게이션에 의존합니다.

---

## Widget 딥 링크

같은 `iCangJie://` URL을 탭합니다. 예제:

| Widget | 일반적인 URL |
|--------|-------------|
| Daily Character | `iCangJie://word?q=<char>```` |
| Code Length | `iCangJie://levels`````` |
| Daily Quiz | `iCangJie://quiz``````` |
| Typing Glance | `iCangJie://typing`````` |
| Favorites | `iCangJie://favorites`````` |
| Wrong Book | `iCangJie://wrong```````` |
| Recent | `iCangJie://search``````` |
| Learning Progress | `iCangJie://learn``````` |

---

## 단축키 예제

**오늘의 퀴즈 열기 **


```
iCangJie://quiz
```


** 클립보드에서 문자를 찾습니다 **

Shortcuts**Get Clipboard** 동작을 사용하여 **Open URL**:


```
iCangJie://word?q=[Clipboard]
```


**시작 태핑 연습**


```
iCangJie://typing
```


---

## 홈 화면 빠른 행동

iCangJie 앱 아이콘을 오래 누르십시오. 기본 옵션 (설정에서 최대 4까지):

| Action | 사이트 맵 |
|--------|-----|
| Search | `iCangJie://search``````` |
| Daily Quiz | `iCangJie://quiz``````` |
| Favorites | `iCangJie://favorites`````` |
| Wrong Book | `iCangJie://wrong```````` |
| Code Length | `iCangJie://levels`````` |
| Feedback | `iCangJie://feedback````` |
| Rate App | 숙박 플랜 |

</section>
<section lang="ru" markdown="1">

iCangJie поддерживает ** `iCangJie://` ** URL-схема глубоких ссылок — открытый поиск в поиске, детали текста, Daily Quiz, Typing, Favorites, Wrong Book, Levels или Learn from Safari, другое приложение, QR-код, кран виджета или ярлыки Apple.

Параллельный набор **Home Screen Quick Actions** (иконка приложения с длинным нажатием) охватывает дополнительные направления, такие как поиск, обратная связь и скорость. Настройка до 4 ярлыков в ** Настройки → Настройки приложений → Настройки домашнего экрана **.

## Спецификация протокола


```
iCangJie://<host>[?query]
```


| Rule | Подробнее |
|------|--------|
| **Scheme** | «icangjie» / «iCangJie» — сравнительный случай |
| **Host routing** | Основным маршрутизатором является URL **host** |
| **Query aliases** | «q», «word» и «name» являются взаимозаменяемыми для хостов поиска/слова. |
| **Parser** | «ICangJieDeepLink.parse( :)» — потребляется через «onOpenURL» → «AppRouter.pendingDeepLink» |

** Три канала доставки**

| Channel | Handled by | Примеры |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ICangJieDeepLink.parse` → `RootTabView` | «поиск», «слово», «викторина», «типирование», «любимые», «неправильные», «уровни», «учиться» |
| **Home Screen Quick Action** | `ShortcutObserver.dispatch` | «поиск», «викторина», «любимые», «неправильные», «уровни», «обратная связь», «обзор» |
| **App Intents / Siri / Widget pending URL** | Writes `AppGroup.pendingDeepLinkURL` → `RootTabView.consumePendingDeepLinkFromAppGroup()` | Код поиска, начало викторины, открытый поиск |

Типы быстрого действия используют ** `iCangJie://` **, совпадающие по строке типа, поэтому как `icangjie` , так и унаследованные варианты все еще маршрутизируются правильно.

---

## 1.В поисках.

Откройте вкладку **Lookup**. Опционально заполните поле поиска.

| Parameter | Required | Описание |
|-----------|----------|-------------|
| `q` | No | Поисковый запрос (префикс кода, символ, пиньинь или Jyutping) |
| `word` | No | Синонимы к «q» |
| `name` | No | Синонимы к «q» |

Открытый поиск (Open Lookup)


```
iCangJie://search
```


**Поиск префикса кода `iCangJie://` **


```
iCangJie://search?q=ab
```


**Поиск персонажа **


```
iCangJie://search?q=颉
```


---

## 2. Подробнее

Откройте страницу деталей для одного персонажа. Требуется не пустой запрос.

| Parameter | Required | Описание |
|-----------|----------|-------------|
| `q` | One of `q` / `word` / `name` | Персонаж Target Han |
| `word` | One of `q` / `word` / `name` | Синонимы к «q» |
| `name` | One of `q` / `word` / `name` | Синонимы к «q» |

** Принимаемые хосты: ** `iCangJie://` , `icangjie` , `iCangJie` **Открытая деталь для  **


```
iCangJie://word?q=倉
```


Альтернативный хост:


```
iCangJie://character?word=颉
```


Если запрос ** пуст или символ не в словаре **, ссылка ** молча игнорируется **.

---

## 3. Daily Quiz

Прыгайте прямо в ежедневный квиз. Не запускает и не пропускает вопросы.


```
iCangJie://quiz
```


Алиасы: `iCangJie://` ---

## 4.Типирование

Откройте **Typing** tab hub.


```
iCangJie://typing
```


Алиасы: `iCangJie://` , `icangjie` ---

## 5. Любимые

Откройте список **Любимые **.


```
iCangJie://favorites
```


Алиас: `iCangJie://` ---

## 6.Неправильный ответ

### 6.1 Список

Откройте список «Книга неправильных ответов».


```
iCangJie://wrong
```


Алиасы: `iCangJie://` , `icangjie` ### 6.2 Единый рекорд

Когда `iCangJie://` является действительным UUID сохраненной записи с неверным ответом, приложение открывает детали слова записи (если запись все еще существует).

| Parameter | Required | Формат |
|-----------|----------|--------|
| `record` | Yes | струна UUID |
| `id` | Yes | Синонимы к «Record» |


```
iCangJie://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


---

## 7. Уровни (длина кода)

Откройте вкладку **Levels**.


```
iCangJie://levels
```


Алиасы: `iCangJie://` , `icangjie` ---

## 8.Учитесь (курсивы)

Откройте центр **Learn**.


```
iCangJie://learn
```


Алиасы: `iCangJie://` ---

## 9. Обратная связь (только быстрое действие)

Откройте предварительно заполненный почтовый композитор обратной связи (или `iCangJie://` fallback).


```
iCangJie://feedback
```


Обрабатывается **Home Screen Quick Action** / `iCangJie://` , а не `icangjie` .

---

## 10. Обзор App Store (только для быстрого действия)

Запросить отзыв в App Store.


```
iCangJie://review
```


Alias matching также принимает `iCangJie://` в строке типа быстрого действия.

---

## 11. App Intents & Siri (iOS 16+)

Встроенные ярлыки **App появляются в приложении Shortcuts и Siri. Каждое намерение устанавливает `iCangJie://` в группе приложений; приложение потребляет его при запуске.

| Intent | Action | В ожидании URL |
|--------|--------|-------------|
| **Look up Cangjie code** | Opens word detail for the given character | iCangJie://word?q=<char> |
| **Start daily quiz** | Opens Daily Quiz | "iCangJie://quiz" |
| **Open lookup search** | Opens Lookup tab | "iCangJie://поиск" |

** Примеры фраз Siri (английский)**

- *"Поищите код Cangjie для   в iCangJie"*
- «Начать ежедневную викторину в iCangJie»
- «Поиск Канджи в iCangJie»

В **Shortcuts** добавьте действие из раздела приложения iCangJie. Намерение **Look up** требует параметра **Chinese character** ( `iCangJie://` ).

> Намерения приложений **iOS только **. macOS полагается на `iCangJie://` URL и навигацию по меню.

---

## Виджет Deep Links

Виджеты нажимают на те же `iCangJie://` URL. Примеры:

| Widget | Типичный URL |
|--------|-------------|
| Daily Character | iCangJie://word?q=<char> |
| Code Length | "iCangJie://levels" |
| Daily Quiz | "iCangJie://quiz" |
| Typing Glance | "iCangJie://typing" |
| Favorites | "iCangJie://favorites" |
| Wrong Book | "iCangJie://wrong" |
| Recent | "iCangJie://поиск" |
| Learning Progress | "iCangJie://learn" |

---

## Короткие примеры

** Открытая сегодня викторина**


```
iCangJie://quiz
```


**Посмотрите на персонажа из клипборда**

Используйте ярлыки **Get Clipboard** action, затем **Open URL** с:


```
iCangJie://word?q=[Clipboard]
```


**Практика набора текста**


```
iCangJie://typing
```


---

## Домой Экран Быстрые действия

Нажмите на иконку приложения iCangJie. Варианты по умолчанию (выберите до 4 в настройках):

| Action | URL |
|--------|-----|
| Search | "iCangJie://поиск" |
| Daily Quiz | "iCangJie://quiz" |
| Favorites | "iCangJie://favorites" |
| Wrong Book | "iCangJie://wrong" |
| Code Length | "iCangJie://levels" |
| Feedback | "iCangJie://feedback" |
| Rate App | "iCangJie://review" |

</section>
<section lang="th" markdown="1">

iCangjie รองรับ~ `iCangJie://` BAR ~ เว็บไซต์ ที่ อยู่ อาศัย วาง แบบ อย่าง ที่ ลึก ซึ้ง — เปิด การ ค้น หา, ราย ละเอียด เกี่ยว กับ คํา, เดลี ควินซ์, ไท ติง, รายการ โปรด, ผิด เล่ม, ระดับ, หรือ เรียน รู้ จาก ซา ฟารี, แอพ อีก แบบ หนึ่ง, คิว อาร์ รหัส, แอปเปิล แท็บ, หรือ แอปเปิล.

ชุดที่คล้ายกันของ ~Home screen secure appoction ~ (ยาว-ดันไอคอนแอพ) ครอบคลุมไปยังปลายทางอื่น ๆ เช่น สืบค้น, แหล่งป้อนและอัตรา ตั้งค่าปุ่มพิมพ์ลัดขึ้นถึง 4 ปุ่มพิมพ์ลัดใน~. ตั้งโปรแกรม Apps ettings → หน้าจอส่วนตัว ~.

## การกําหนดโพรโทคอล


```
iCangJie://<host>[?query]
```


| Rule | รายละเอียด |
|------|--------|
| **Scheme** | 'Cykangjie' / 'icangjie' — เปรียบเทียบกรณีที่อ่อนไหว |
| **Host routing** | ตัวนําร่องหลักคือที่อยู่ URL ~! ~ |
| **Query aliases** | 'c', 'คํา' และ 'ชื่อ' สามารถสลับกันสําหรับการค้นหา/โฮสต์คํา |
| **Parser** | 'Changjie deeplink.parse(help:)' — ถูกบริโภคผ่านทาง 'On OpenURL' 'HAHHHHHHHA AppRouter.pending Deeplidge' |

~ช่องส่ง 3 ~

| Channel | Handled by | ตัวอย่าง |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ICangJieDeepLink.parse` → `RootTabView` | และจงเฝ้าคอยดูเถิด ผลสุดท้ายจะเกิดขึ้นอย่างแน่นอน |
| **Home Screen Quick Action** | `ShortcutObserver.dispatch` | และจงเฝ้าคอยดูเถิด ผลสุดท้ายจะเกิดขึ้นอย่างแน่นอน |
| **App Intents / Siri / Widget pending URL** | Writes `AppGroup.pendingDeepLinkURL` → `RootTabView.consumePendingDeepLinkFromAppGroup()` | ค้นหารหัส, เริ่มทดสอบ, เปิดการค้นหา |

ประเภทการกระทําด่วนใช้} BAR `iCangJie://` BAR  } ตรงกันกับข้อความชนิด ดังนั้นทั้ง   c1   BAR ข้อมูลมรดกยังคงพาธที่ถูกต้อง

---

## 1. สืบค้น

เปิด... ตัวเลือกก่อนเติมสนามค้นหา

| Parameter | Required | คําอธิบาย |
|-----------|----------|-------------|
| `q` | No | สืบค้น (นําหน้ารหัส, อักขระ, pinyin, หรือ juitping) |
| `word` | No | Synonym สําหรับ 'q' |
| `name` | No | Synonym สําหรับ 'q' |

** เปิดค้นหา (การค้นหาเปล่า) ~


```
iCangJie://search
```


** ตรวจหารหัสนําหน้า `iCangJie://` BAR ~


```
iCangJie://search?q=ab
```


~มองหาตัวละคร ~


```
iCangJie://search?q=颉
```


---

## 2. รายละเอียดคํา

เปิดหน้ารายละเอียดสําหรับอักขระเดียว ต้องการการสอบถามที่ไม่ว่างเปล่า

| Parameter | Required | คําอธิบาย |
|-----------|----------|-------------|
| `q` | One of `q` / `word` / `name` | อักขระเป้าหมาย ฮัน |
| `word` | One of `q` / `word` / `name` | Synonym สําหรับ 'q' |
| `name` | One of `q` / `word` / `name` | Synonym สําหรับ 'q' |

~ฮูสยอมรับ: ~ BAR `iCangJie://` BAR `icangjie` BAR   BAR    BAR `iCangJie` BAR

~รายละเอียดเปิดให้บริการ~


```
iCangJie://word?q=倉
```


โฮสต์อื่น:


```
iCangJie://character?word=颉
```


หากการค้นหาไม่อยู่ใน~ หรือไม่มีอักขระอยู่ในพจนานุกรม ~ ลิงก์จะถูกละทิ้ง~

---

## 3. เดลี ควิซ

กระโดดตรงไปที่ เดลี่ เควซ ไม่ได้เริ่มต้นอัตโนมัติหรือข้ามคําถาม


```
iCangJie://quiz
``` `iCangJie://` BAR

---

## 4. การฝึกซ้อม

เปิดช่องแท็บ


```
iCangJie://typing
``` `iCangJie://` BAR `icangjie` BAR

---

## 5 รายการโปรด

เปิดรายการ


```
iCangJie://favorites
```


อาลี: `iCangJie://` BAR

---

## 6. หนังสือคําตอบผิด

### รายการ 6.1

เปิดรายการคําตอบของ Wrong Book


```
iCangJie://wrong
``` `iCangJie://` BAR `icangjie` BAR

### 6.2 สถิติซิงเกิล

เมื่อ  c0   BAR เป็น UUID ที่ถูกต้องของรายการที่บันทึกข้อมูลผิดพลาด App จะเปิดรายละเอียดคําของการบันทึก (หากบันทึกยังคงมีอยู่)

| Parameter | Required | รูปแบบ |
|-----------|----------|--------|
| `record` | Yes | ข้อความ UUID |
| `id` | Yes | Synonym สําหรับ 'บันทึก' |


```
iCangJie://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


---

## 7. ระดับ (ความยาวสี)

เปิดแท็บ


```
iCangJie://levels
``` `iCangJie://` BAR `icangjie` BAR

---

## 8. เรียน รู้ (ภาษา อังกฤษ)

เปิดหมวก


```
iCangJie://learn
``` `iCangJie://` BAR

---

## 9. แหล่งป้อนกลับ (เฉพาะการกระทําของ Quick เท่านั้น)

เปิดโปรแกรมเขียนจดหมายตอบกลับแบบเติมข้อมูล (หรือ `iCangJie://` packed)


```
iCangJie://feedback
```


จัดการโดย ~Home screen exacting ~ / c0         r ไม่ใช่ `icangjie` .

---

## 10 App street Review (Kick Action) เท่านั้น

ขอข้อมูลด่วนจากร้านเอป


```
iCangJie://review
```


จับคู่ Alias ยังยอมรับ  c0    ในข้อความชนิดการกระทําอย่างรวดเร็ว

---

## 11. App Inspents & Siri (inOS 16+).

มีทางลัดของเอปป์ ปรากฏในแอพทางลัดและเซอร์ริ แต่ละเซต `iCangJie://` BAR ใน App Group; app จะบริโภคเมื่อเปิดตัว

| Intent | Action | ที่อยู่ URL ที่หยุดการทํางาน |
|--------|--------|-------------|
| **Look up Cangjie code** | Opens word detail for the given character | """"'"'""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" |
| **Start daily quiz** | Opens Daily Quiz | ยงเจ๋อย |
| **Open lookup search** | Opens Lookup tab | สืบค้นเมื่อ ค.ศ. |

~Example Seri words (อังกฤษ) ~

- ♪"มองหารหัส Cangjie สําหรับ 颉 in iKang Jie"*
- ♪เริ่มทดสอบทุกวันใน iKangJie ♪
- *"ค้นหากวางเจียงเจี้ยง"*

ในโปรแกรม ~เพิ่มการกระทําจากภาคไอแคงจี้ ~ มองขึ้นไป~ ~ วัตถุประสงค์ต้องการค่าอักขระ~~~~ ~พารามิเตอร์ ( `iCangJie://` )

> ส่วนเชื่อมโยงของ App มี < iOS เท่านั้น *. MacOS พึ่งพาที่อยู่ที่  c0 ที่อยู่ URL และที่นําทางเมนู

---

## วิดเจ็ตที่อยู่เชื่อมโยงแบบลึก

วิดเจ็ตสามารถเคาะผ่านที่อยู่ URL แบบเดียวกัน `iCangJie://` ตัวอย่าง:

| Widget | ที่อยู่ URL ปกติ |
|--------|-------------|
| Daily Character | """"'"'""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" |
| Code Length | 'อุงเจ๋อ' |
| Daily Quiz | ยงเจ๋อย |
| Typing Glance | ยงจี้ |
| Favorites | ยงเจ๋อย |
| Wrong Book | ยงเจ๋อ |
| Recent | สืบค้นเมื่อ ค.ศ. |
| Learning Progress | ยงเจี่ย |

---

## ตัวอย่างปุ่มพิมพ์ลัด

~เปิดข้อสอบในวันนี้~


```
iCangJie://quiz
```


** หาตัวละครจากคลิปบอร์ด~

ใช้ปุ่มพิมพ์ลัด # รับค่าการกระทําจากคลิปบอร์ด ~ เปิดที่อยู่ URL ด้วย:


```
iCangJie://word?q=[Clipboard]
```


~เริ่มฝึกพิมพ์ใหม่~


```
iCangJie://typing
```


---

## การกระทําด่วนของจอส่วนตัว

กดปุ่มไอแคงจี้ ตัวเลือกปริยาย (เลือกที่ 4 ในการตั้งค่า):

| Action | ที่อยู่ URL |
|--------|-----|
| Search | สืบค้นเมื่อ ค.ศ. |
| Daily Quiz | ยงเจ๋อย |
| Favorites | ยงเจ๋อย |
| Wrong Book | ยงเจ๋อ |
| Code Length | 'อุงเจ๋อ' |
| Feedback | 'Oi Cang Jie Acttitive' |
| Rate App | 'Oi Cang Jie Augustview' |

</section>
<section lang="de" markdown="1">

iCangJie unterstützt ** `iCangJie://` ** URL-Schema Deep Links - offene Lookup-Suche, Wortdetails, tägliches Quiz, Tippen, Favoriten, falsches Buch, Levels oder Lernen von Safari, einer anderen App, einem QR-Code, einem Widget-Tipp oder Apple Shortcuts.

Ein paralleler Satz von **Home Screen Quick Actions** (langes Drücken des App-Symbols) deckt zusätzliche Ziele wie Suche, Feedback und Rate ab. Konfigurieren Sie bis zu 4 Verknüpfungen in **Settings → App Settings → Home Screen Shortcuts**.

## Protokollspezifikation


```
iCangJie://<host>[?query]
```


| Rule | Einzelheiten |
|------|--------|
| **Scheme** | `icangjie` / `iCangJie` — Fall-unempfindlich verglichen |
| **Host routing** | Primärer Router ist die URL **host** |
| **Query aliases** | `q`, `word` und `name` sind austauschbar für Such-/Wort-Hosts. |
| **Parser** | `ICangJieDeepLink.parse( :):` — verbraucht über `onOpenURL` → `AppRouter.pendingDeepLink` |

**Drei Lieferkanäle **

| Channel | Handled by | Beispiele |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ICangJieDeepLink.parse` → `RootTabView` | `search`, `word`, `quiz`, `type`, `favorites`, `falsch`, `levels`, `learn` |
| **Home Screen Quick Action** | `ShortcutObserver.dispatch` | `search`, `quiz`, `favorites`, `falsch`, `levels`, `feedback`, `review` |
| **App Intents / Siri / Widget pending URL** | Writes `AppGroup.pendingDeepLinkURL` → `RootTabView.consumePendingDeepLinkFromAppGroup()` | Lookup-Code, Start Quiz, offene Suche |

Quick-Action-Typen verwenden ** `iCangJie://` ** Matching auf der Typzeichenfolge, so dass sowohl `icangjie` als auch Legacy-Varianten immer noch korrekt routen.

---

## 1. Lookup Suche

Öffnen Sie den Tab **Lookup**. Optional das Suchfeld vorfüllen.

| Parameter | Required | Beschreibung |
|-----------|----------|-------------|
| `q` | No | Suchanfrage (Codepräfix, Zeichen, Pinyin oder Jyutping) |
| `word` | No | Synonym für `q` |
| `name` | No | Synonym für `q` |

**Open Lookup (leere Suche)**


```
iCangJie://search
```


**Suche nach Codepräfix `iCangJie://` **


```
iCangJie://search?q=ab
```


**Suche nach Charakter 颉**


```
iCangJie://search?q=颉
```


---

## 2. Word Detail

Öffnen Sie die Detailseite für ein einzelnes Zeichen. Erfordert eine nicht-leere Abfrage.

| Parameter | Required | Beschreibung |
|-----------|----------|-------------|
| `q` | One of `q` / `word` / `name` | Ziel-Han-Charakter |
| `word` | One of `q` / `word` / `name` | Synonym für `q` |
| `name` | One of `q` / `word` / `name` | Synonym für `q` |

** Hosts akzeptiert:** `iCangJie://` , `icangjie` , `iCangJie` **Offenes Detail für 倉**


```
iCangJie://word?q=倉
```


Alternativer Host:


```
iCangJie://character?word=颉
```


Wenn die Abfrage **leer ist oder das Zeichen nicht im Wörterbuch ** ist, wird der Link **stillschweigend ignoriert **.

---

## 3. Tägliches Quiz

Springen Sie direkt zum **Daily Quiz**. Startet oder überspringt keine Fragen automatisch.


```
iCangJie://quiz
```


Aliasnamen: `iCangJie://` ---

## 4. Schreibpraxis

Öffnen Sie den **Typing** Tab Hub.


```
iCangJie://typing
```


Aliasnamen: `iCangJie://` , `icangjie` ---

## 5. Favoriten

Öffnen Sie die **Favoriten**-Liste.


```
iCangJie://favorites
```


Aliasname: `iCangJie://` ---

## 6. Falsches Antwortbuch

### 6.1 Liste

Öffnen Sie die **Wrong Answer Book** Liste.


```
iCangJie://wrong
```


Aliasnamen: `iCangJie://` , `icangjie` ### 6.2 Einzeldatensatz

Wenn `iCangJie://` eine gültige UUID eines gespeicherten Falschantworteintrags ist, öffnet die App das Wortdetail dieses Datensatzes (falls der Datensatz noch existiert).

| Parameter | Required | Format |
|-----------|----------|--------|
| `record` | Yes | UUID-Strecke |
| `id` | Yes | Synonym für `record` |


```
iCangJie://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


---

## 7. Stufen (Codelänge)

Öffnen Sie den Tab **Levels **.


```
iCangJie://levels
```


Aliasnamen: `iCangJie://` , `icangjie` ---

## 8. Lernen (Tutorials)

Öffnen Sie den **Learn** Hub.


```
iCangJie://learn
```


Aliasnamen: `iCangJie://` ---

## 9. Feedback (nur schnelle Maßnahmen)

Öffnen Sie den vorgefüllten Feedback-E-Mail-Komponisten (oder `iCangJie://` Fallback).


```
iCangJie://feedback
```


Handled by **Home Screen Quick Action** / `iCangJie://` , nicht `icangjie` .

---

## 10. App Store Review (nur Quick Action)

Fordern Sie eine In-App App Store Überprüfungsaufforderung an.


```
iCangJie://review
```


Alias-Matching akzeptiert auch `iCangJie://` in der Schnellaktionszeichenfolge.

---

## 11. App Intents & Siri (iOS 16+)

**App Shortcuts** werden in der Shortcuts App und Siri angezeigt. Jede Absicht setzt `iCangJie://` in der App-Gruppe; die App verbraucht sie beim Start.

| Intent | Action | Ausstehende URL |
|--------|--------|-------------|
| **Look up Cangjie code** | Opens word detail for the given character | `iCangJie://word?q=<char>` |
| **Start daily quiz** | Opens Daily Quiz | „iCangJie://quiz |
| **Open lookup search** | Opens Lookup tab | „iCangJie://search |

**Beispiel Siri Phrasen (Englisch)**

- *"Schauen Sie Cangjie-Code für 颉 in iCangJie"*
- *"Tägliches Quiz in iCangJie starten"*
- *"Search Cangjie in iCangJie"*

Fügen Sie in **Shortcuts** die Aktion aus dem iCangJie-App-Bereich hinzu. Die **Look up**-Intention erfordert einen **chinesischen Zeichen**-Parameter ( `iCangJie://` ).

> App Intents sind **iOS only**. macOS setzt auf `iCangJie://` URLs und Menünavigation.

---

## Widget Deep Links

Widgets tippen durch die gleichen `iCangJie://` URLs. Beispiele:

| Widget | Typische URL |
|--------|-------------|
| Daily Character | `iCangJie://word?q=<char>` |
| Code Length | „iCangJie://levels |
| Daily Quiz | „iCangJie://quiz |
| Typing Glance | „iCangJie://typing |
| Favorites | „iCangJie://favorites |
| Wrong Book | „iCangJie://wrong |
| Recent | „iCangJie://search |
| Learning Progress | „iCangJie://learn |

---

## Abkürzungen Beispiele

**Öffne das heutige Quiz **


```
iCangJie://quiz
```


**Schauen Sie einen Charakter aus dem Clipboard nach **

Verwenden Sie eine Shortcuts **Get Clipboard ** Aktion, dann **Open URL ** mit:


```
iCangJie://word?q=[Clipboard]
```


**Beginn der Schreibpraxis**


```
iCangJie://typing
```


---

## Home Bildschirm Schnelle Aktionen

Langes Drücken des iCangJie App-Symbols. Standardoptionen (wählen Sie bis zu 4 in Einstellungen):

| Action | URL |
|--------|-----|
| Search | „iCangJie://search |
| Daily Quiz | „iCangJie://quiz |
| Favorites | „iCangJie://favorites |
| Wrong Book | „iCangJie://wrong |
| Code Length | „iCangJie://levels |
| Feedback | „iCangJie://feedback |
| Rate App | „iCangJie://review |

</section>
<section lang="fr" markdown="1">

iCangJie supporte ** `iCangJie://` ** URL schéma de liens profonds — ouvert Recherche de recherche, de détail de mots, Daily Quiz, Typing, Favoris, mauvais livre, niveaux, ou apprendre de Safari, une autre application, un code QR, un widget tap, ou Apple Raccourcis.

Un ensemble parallèle de **Actions rapides d'écran d'accueil** (appuyer sur l'icône de l'application) couvre d'autres destinations telles que Search, Feedback et Rate. Configurez jusqu'à 4 raccourcis dans **Paramètres → Paramètres de l'application → Raccourcis d'écran d'accueil**.

## Spécification du protocole


```
iCangJie://<host>[?query]
```


| Rule | Détail |
|------|--------|
| **Scheme** | `icangjie` / `iCangJie` — comparaison insensible aux cas |
| **Host routing** | Le routeur principal est l'URL **host** |
| **Query aliases** | `q`, `word` et `name` sont interchangeables pour les hôtes de recherche/mot |
| **Parser** | `ICangJieDeepLink.parse( :)` — consommé via `onOpenURL` → `AppRouter.pendingDeepLink` |

**Trois canaux de livraison**

| Channel | Handled by | Exemples |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ICangJieDeepLink.parse` → `RootTabView` | `recherche`, `mot`, `quiz`, `typing`, `favorites`, `mauvais`, `niveaux`, `apprendre` |
| **Home Screen Quick Action** | `ShortcutObserver.dispatch` | `recherche`, `quiz`, `favorites`, `mauvais`, `niveaux`, `feedback`, `examen` |
| **App Intents / Siri / Widget pending URL** | Writes `AppGroup.pendingDeepLinkURL` → `RootTabView.consumePendingDeepLinkFromAppGroup()` | Code de recherche, quiz de démarrage, recherche ouverte |

Les types d'action rapide utilisent ** `iCangJie://` ** correspondant sur la chaîne de type, de sorte que les variantes `icangjie` et les variantes héritées suivent toujours correctement.

---

## 1. Recherche de recherche

Ouvrez l'onglet **Lookup**. En option, préremplissez le champ de recherche.

| Parameter | Required | Désignation des marchandises |
|-----------|----------|-------------|
| `q` | No | Requête de recherche (préfixe de code, caractère, pinyin, ou Jyutping) |
| `word` | No | Synonyme de `q` |
| `name` | No | Synonyme de `q` |

**Open Lookup (recherche vide)**


```
iCangJie://search
```


**Rechercher le préfixe de code `iCangJie://` **


```
iCangJie://search?q=ab
```


**Rechercher un personnage


```
iCangJie://search?q=颉
```


---

## 2. Détail des mots

Ouvrez la page de détails pour un seul caractère. Nécessite une requête non vide.

| Parameter | Required | Désignation des marchandises |
|-----------|----------|-------------|
| `q` | One of `q` / `word` / `name` | Caractère Han cible |
| `word` | One of `q` / `word` / `name` | Synonyme de `q` |
| `name` | One of `q` / `word` / `name` | Synonyme de `q` |

**Hosts acceptés :** `iCangJie://` , `icangjie` , `iCangJie` **Détails ouverts pour :**


```
iCangJie://word?q=倉
```


Autre hôte :


```
iCangJie://character?word=颉
```


Si la requête est **vide ou si le caractère n'est pas dans le dictionnaire**, le lien est ** silencieusement ignoré**.

---

## 3. Quiz quotidien

Sautez directement au Quiz quotidien**. Ne démarre pas automatiquement ou ne saute pas les questions.


```
iCangJie://quiz
```


Alias: `iCangJie://` ---

## 4. Pratique dactyloscopique

Ouvrez le centre d'onglet **Typing**.


```
iCangJie://typing
```


Alias : `iCangJie://` , `icangjie` ---

## 5. Favoris

Ouvrez la liste **Favorites**.


```
iCangJie://favorites
```


Étrangères :

---

## 6. Livre de mauvaise réponse

### 6.1 Liste

Ouvrez la liste **Wrong Answer Book**.


```
iCangJie://wrong
```


Alias : `iCangJie://` , `icangjie` ### 6.2 Enregistrement unique

Lorsque `iCangJie://` | Parameter | Required | Format |
|-----------|----------|--------|
| `record` | Yes | Chaîne UUID |
| `id` | Yes | Synonyme de `record` |


```
iCangJie://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


---

## 7. Niveaux (longueur du code)

Ouvrez l'onglet **Nivaux**.


```
iCangJie://levels
```


Alias : `iCangJie://` , `icangjie` ---

## 8. Apprendre (tutoriels)

Ouvrez le centre **Learn**.


```
iCangJie://learn
```


Alias: `iCangJie://` ---

## 9. Rétroaction (action rapide seulement)

Ouvrez l'éditeur de courriels de rétroaction prérempli (ou `iCangJie://` ```
iCangJie://feedback
```


Géré par **Action rapide de l'écran d'accueil** / `iCangJie://` , pas `icangjie` .

---

## 10. App Store Review (action rapide seulement)

Demander un avis App Store in-app rapide.


```
iCangJie://review
```


Alias matching accepte également `iCangJie://` dans la chaîne de type action rapide.

---

## 11. App Intents & Siri (iOS 16+)

Les raccourcis de l'application** apparaissent dans l'application Raccourcis et Siri. Chaque intention définit `iCangJie://` dans le groupe App; l'application la consomme au lancement.

| Intent | Action | URL en attente |
|--------|--------|-------------|
| **Look up Cangjie code** | Opens word detail for the given character | `iCangJie://word?q=<char>` |
| **Start daily quiz** | Opens Daily Quiz | 'iCangJie://quiz' |
| **Open lookup search** | Opens Lookup tab | "iCangJie://search" |

**Exemple de phrases Siri (anglais)**

- *"Regardez le code Cangjie pour "" dans iCangJie"*
- *"Démarrer le quiz quotidien en iCangJie"*
- *"Rechercher Cangjie en iCangJie"*

Dans **Shortcuts**, ajoutez l'action de la section application iCangJie. L'intention **Look up** nécessite un paramètre **Chinois** ( `iCangJie://` ).

> App Intents sont **iOS seulement**. macOS compte sur `iCangJie://` URLs et la navigation de menu.

---

## Widget Liens profonds

Widgets tapez sur les mêmes URLs. Exemples:

| Widget | URL typique |
|--------|-------------|
| Daily Character | `iCangJie://word?q=<char>` |
| Code Length | «iCangJie://niveaux» |
| Daily Quiz | 'iCangJie://quiz' |
| Typing Glance | "iCangJie://typing" |
| Favorites | `iCangJie://favorites` |
| Wrong Book | 'iCangJie://wrong' |
| Recent | "iCangJie://search" |
| Learning Progress | <iCangJie://learn> |

---

## Exemples de raccourcis

**Ouvrir le questionnaire d'aujourd'hui**


```
iCangJie://quiz
```


**Regardez un personnage du presse-papiers**

Utilisez un raccourci **Obtenez l'action Clipboard**, puis **Ouvrir l'URL** avec :


```
iCangJie://word?q=[Clipboard]
```


**Démarrer la pratique de dactylographie**


```
iCangJie://typing
```


---

## Actions rapides de l'écran d'accueil

Appuyez sur l'icône iCangJie. Options par défaut (cochez jusqu'à 4 dans Paramètres) :

| Action | URL |
|--------|-----|
| Search | "iCangJie://search" |
| Daily Quiz | 'iCangJie://quiz' |
| Favorites | `iCangJie://favorites` |
| Wrong Book | 'iCangJie://wrong' |
| Code Length | «iCangJie://niveaux» |
| Feedback | «iCangJie://feedback» |
| Rate App | 'iCangJie://review' |

</section>
<section lang="tr" markdown="1">

iCangJie ** `iCangJie://` ** URL planı derin bağlantıları - açık arama, kelime detayı, Daily Quiz, Typing, Favorites, Wrong Book, Levels, or Learn from Safari, another app, a QR code, a item, or Apple Shortcuts.

Paralel bir dizi **Home Ekran Hızlı Eylemler ** (Uygulama ikonunu uzun süreli baskı) Arama, geri bildirim ve Puan gibi ek destinasyonları kapsar. 2018'de 4 kısayolu yapılandırın **Settings → App Ayarları → Ev Ekran kısayolları**.

## Protokol Doğrulaması


```
iCangJie://<host>[?query]
```


| Rule | Detaylı Bilgi |
|------|--------|
| **Scheme** | "icangjie" / "iCangJie" - vakaya duyarlı olarak karşılaştırıldığında |
| **Host routing** | Birincil yönlendirici URL **host** |
| **Query aliases** | "q", "word" ve "name" arama / kelime ev sahipliği için değiştirilebilir |
| **Parser** | "ICangJie DeepLink.parse ( :)" - "onOpenURL" → "AppRouter.pending DeepLink" |

** Üç teslimat kanalı**

| Channel | Handled by | Örnekler |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ICangJieDeepLink.parse` → `RootTabView` | "Arapça", "quiz", "favorites", "wrong", " seviyeler", " |
| **Home Screen Quick Action** | `ShortcutObserver.dispatch` | "Arapçalar", "wrong", " seviyeler", "feedback", " |
| **App Intents / Siri / Widget pending URL** | Writes `AppGroup.pendingDeepLinkURL` → `RootTabView.consumePendingDeepLinkFromAppGroup()` | Lookup kodu, başlangıç testi, açık arama |

Hızlı aksiyon türleri ** `iCangJie://` ** tipi dizede eşleşen, bu yüzden hem de `icangjie` ve mirası seçenekleri hala doğru rotayı doğru şekilde rotalar.

---

## 1. Lookup Search

**Bakup** sekmesi açın. Seçmeli olarak arama alanını önceden doldur.

| Parameter | Required | Açıklama |
|-----------|----------|-------------|
| `q` | No | Arama sorgusu (Ek olarak, karakter, pinyin veya Jyutping) |
| `word` | No | "q" için eş anlamlı |
| `name` | No | "q" için eş anlamlı |

**Open Lookup (boş arama)**


```
iCangJie://search
```


** Kodu önceden ek olarak arayın `iCangJie://` **


```
iCangJie://search?q=ab
```


** Karakter için ara


```
iCangJie://search?q=颉
```


---

## 2. Word Detayları

Tek bir karakter için detay sayfasını açın. Boş olmayan bir sorgu gerektirir.

| Parameter | Required | Açıklama |
|-----------|----------|-------------|
| `q` | One of `q` / `word` / `name` | Hedef Han karakteri |
| `word` | One of `q` / `word` / `name` | "q" için eş anlamlı |
| `name` | One of `q` / `word` / `name` | "q" için eş anlamlı |

**Hosts kabul etti: ** `iCangJie://` , `icangjie` , `iCangJie` **  for** için açık detay


```
iCangJie://word?q=倉
```


Alternatif ev sahibi:


```
iCangJie://character?word=颉
```


Soru ** Eksik veya karakter sözlükte değilse, bağlantı ** olarak göz ardı edilir**.

---

## 3. Günlük Quiz

Doğrudan **Daily Quiz**'e gidin. Auto-start veya soruları atlamayın.


```
iCangJie://quiz
```


Aliases: `iCangJie://` ---

## 4. Typing Practice

**Typing ** sekme merkezi açın.


```
iCangJie://typing
```


Aliases: `iCangJie://` , `icangjie` ---

## 5. Favoriler

**Favorites ** listesi açın.


```
iCangJie://favorites
```


Alias: `iCangJie://` ---

## 6. Yanlış Cevap Kitabı

### 6.1 Listesi

**Wrong Cevap Kitabı** listesi açın.


```
iCangJie://wrong
```


Aliases: `iCangJie://` , `icangjie` ### 6.2 Tek kayıt `iCangJie://` , kurtarılmış bir yanlış cevap girişinin geçerli bir UUID'si olduğunda, uygulama bu rekorun kelime detayını açar (eğer kayıt hala varsa).

| Parameter | Required | Format |
|-----------|----------|--------|
| `record` | Yes | UUID string |
| `id` | Yes | "record" için Synonym |


```
iCangJie://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


---

## 7. Seviyeler (Kolay uzunluğu)

**Levels ** sekmesi açın.


```
iCangJie://levels
```


Aliases: `iCangJie://` , `icangjie` ---

## 8. Öğrenme (yardım)

**Learn ** merkezi açın.


```
iCangJie://learn
```


Aliases: `iCangJie://` ---

## 9. Geri bildirim (Quick Action sadece)

Tamamlanmış geri bildirimler e-posta bestecisi açın (veya `iCangJie://` geri dönüş).


```
iCangJie://feedback
```


**Home Ekran Hızlı Aksiyon ** / `iCangJie://` , `icangjie` .

---

## 10. App Store Review (Quick Action sadece)

Bir in-app App Store incelemesini talep edin.


```
iCangJie://review
```


Alias eşleştirme ayrıca hızlı tepki türü dizesinde `iCangJie://` 'i kabul eder.

---

## 11. App niyetleri ve Siri (iOS 16+)

Yerleşik **App Kısa kesimler ** Kısa kesimler uygulamasında ve Siri'de görünür. Her niyet, App Grubu'nda `iCangJie://` ayarlar; uygulama bunu başlatıyor.

| Intent | Action | Pending URL |
|--------|--------|-------------|
| **Look up Cangjie code** | Opens word detail for the given character | "iCangJie httpword?q=<char>" |
| **Start daily quiz** | Opens Daily Quiz | "iCangJie httpquiz" |
| **Open lookup search** | Opens Lookup tab | "iCangJie httpsearch" |

**Example Siri cümleleri (İngilizce)**

- * "Bak up Cangjie code for 颉 in iCangJie"*
- *"ICangJie'de günlük sınava başlayın"*
- *"Ara Cangjie in iCangJie"*

**Shortcuts **, iCangJie uygulama bölümünden eylem ekleyin. **Bakın** niyeti ** Çin karakteri ** parametresi ( `iCangJie://` ).

> App niyetleri **iOS sadece**.OS, `iCangJie://` URL'lere ve menü navigasyona dayanmaktadır.

---

## Widget Deep Links

Widgets aynı `iCangJie://` URL'leri ele alır. Örnekler:

| Widget | Tipik URL URL URL |
|--------|-------------|
| Daily Character | "iCangJie httpword?q=<char>" |
| Code Length | “iCangJie: |
| Daily Quiz | "iCangJie httpquiz" |
| Typing Glance | "iCangJie #typing" |
| Favorites | "iCangJie httpfavorites" |
| Wrong Book | "iCangJie httpwrong" |
| Recent | "iCangJie httpsearch" |
| Learning Progress | “iCangJie: |

---

## Kısaltmalar Örnekler

**Bugünün sınavı**


```
iCangJie://quiz
```


**Singboard'dan bir karaktere bakın**

Kısa bir kesim kullanın ** Clipboard ** aksiyon alın, sonra **Open URL** ile:


```
iCangJie://word?q=[Clipboard]
```


** Uygulamayı yazmaya başlayın**


```
iCangJie://typing
```


---

## Home Screen Quick Actions

ICangJie app i. Varsayılan seçenekler ( Ayarları 4'e kadar):

| Action | URL URL URL URL |
|--------|-----|
| Search | "iCangJie httpsearch" |
| Daily Quiz | "iCangJie httpquiz" |
| Favorites | "iCangJie httpfavorites" |
| Wrong Book | "iCangJie httpwrong" |
| Code Length | “iCangJie: |
| Feedback | "iCangJie https |
| Rate App | "iCangJie http |

</section>
