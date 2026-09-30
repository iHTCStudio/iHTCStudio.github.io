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
