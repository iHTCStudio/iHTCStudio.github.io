---
layout: doc
title: iTer — URL Scheme Reference
app_id: iTer
doc_title_en: URL Scheme Reference
doc_title_zh_cn: URL Scheme 深度链接文档
doc_title_zh_tw: URL Scheme 深度連結文件
description: Complete reference for iTer:// deep links, widget links, and Home Screen Quick Actions on iPhone and iPad.
---

<section lang="en" markdown="1">

iTer supports the **`iTer://`** URL scheme on **iPhone and iPad**. Use it in Shortcuts, Safari, widgets, or other apps to open a question, the daily quiz, favourites, or the wrong-answer book.

**Home Screen Quick Actions** (long-press the app icon) reuse the same `type` strings. Choose up to **4** from **7** options in **Settings → Home Screen shortcuts**.

> **Note:** Deep links **navigate** inside the app. They do not change quiz settings or mark questions remotely. **Mac** does not register Home Screen Quick Actions; widgets and in-app navigation still work on Mac.

## Protocol

```
iTer://<host>[?query]
```

| Rule | Detail |
|------|--------|
| **Scheme** | `iTer` (case-insensitive) |
| **Question detail** | Host `question` — query **`id=<questionID>`** or **`q=<questionID>`** (required) |
| **Daily Quiz** | Host `quiz` |
| **Favourites** | Host `favorites` → Settings → Favourites list |
| **Wrong book** | Host `wrong`, `mistakes`, or `wrongquestions` — optional **`record=<UUID>`** opens one mistake |
| **Search** | Host `search` — Quick Action / shortcut only (opens global search tab) |
| **Categories** | Host `categories` — Quick Action / shortcut only (opens Categories tab) |
| **Feedback** | Host `feedback` — Quick Action only (mail compose or `mailto:` fallback) |
| **Rate app** | Host `review` — Quick Action only (StoreKit in-app review). Legacy types containing `star` also work. |

Paths such as `iTer://quiz` are accepted when the host is empty and the path segment matches.

## Examples

```
iTer://question?id=94c34bb2bdef11e6a0e100163e0021c8
iTer://quiz
iTer://favorites
iTer://wrong
iTer://wrong?record=550E8400-E29B-41D4-A716-446655440000
```

## Home Screen Quick Actions

| Type | Typical use |
|------|-------------|
| `iTer://search` | Global search |
| `iTer://quiz` | Daily Quiz tab |
| `iTer://favorites` | Favourites list |
| `iTer://wrong` | Wrong-answer book |
| `iTer://categories` | Categories tab |
| `iTer://feedback` | Send feedback |
| `iTer://review` | Rate the app (StoreKit) |

Default selection: Search, Quiz, Favourites, Feedback. Reorder or replace in **Settings → Home Screen shortcuts** (max 4). The app matches shortcut `type` strings with **contains**, so legacy variants that include these paths still route correctly.

## Widget deep links

| Widget | Typical URL |
|--------|-------------|
| Daily Question | `iTer://question?id=…` |
| Quiz Glance | `iTer://quiz` |
| Favourites Glance | `iTer://favorites` |
| Wrong Book Glance | `iTer://wrong` or `iTer://wrong?record=<UUID>` |

---

[Back to iTer Support](./) · [FAQ](faq) · [Privacy Policy](privacy)

</section>

<section lang="zh-CN" markdown="1">

爱技术支持 **`iTer://`** URL Scheme（**iPhone / iPad**）。可在快捷指令、Safari、小组件或其他 App 中打开题目、每日测验、收藏或错题本。

**主屏快捷指令**（长按图标）使用相同的 `type` 字符串。在 **设置 → 主屏快捷方式** 中从 **7 项**里最多选 **4 项**。

> **说明：** 深度链接仅用于**应用内跳转**，不会远程修改测验设置或题目标记。**Mac** 无主屏快捷指令；小组件与应用内导航在 Mac 上仍可用。

## 协议

```
iTer://<host>[?query]
```

| 规则 | 说明 |
|------|------|
| **Scheme** | `iTer`（大小写不敏感） |
| **题目详情** | Host `question` — 查询参数 **`id=<题目ID>`** 或 **`q=<题目ID>`**（必填） |
| **每日测验** | Host `quiz` |
| **收藏** | Host `favorites` → 设置 → 收藏列表 |
| **错题本** | Host `wrong` / `mistakes` / `wrongquestions` — 可选 **`record=<UUID>`** 打开单条错题 |
| **搜索** | Host `search` — 仅快捷指令（打开全局搜索 Tab） |
| **分类** | Host `categories` — 仅快捷指令（打开分类 Tab） |
| **反馈** | Host `feedback` — 仅快捷指令（邮件撰写或 `mailto:` 回退） |
| **评分** | Host `review` — 仅快捷指令（StoreKit 应用内评分）。含 `star` 的旧 type 仍兼容 |

## 示例

```
iTer://question?id=94c34bb2bdef11e6a0e100163e0021c8
iTer://quiz
iTer://favorites
iTer://wrong
iTer://wrong?record=550E8400-E29B-41D4-A716-446655440000
```

## 主屏快捷指令

| Type | 用途 |
|------|------|
| `iTer://search` | 全局搜索 |
| `iTer://quiz` | 每日测验 Tab |
| `iTer://favorites` | 收藏列表 |
| `iTer://wrong` | 错题本 |
| `iTer://categories` | 分类 Tab |
| `iTer://feedback` | 发送反馈 |
| `iTer://review` | 应用评分（StoreKit） |

默认：搜索、测验、收藏、反馈。可在 **设置 → 主屏快捷方式** 中排序或替换（最多 4 项）。应用以 **contains** 匹配 type，兼容包含上述路径的历史变体。

## 小组件深度链接

| 小组件 | 典型 URL |
|--------|----------|
| 每日一题 | `iTer://question?id=…` |
| 测验一览 | `iTer://quiz` |
| 收藏速览 | `iTer://favorites` |
| 错题速览 | `iTer://wrong` 或 `iTer://wrong?record=<UUID>` |

---

[返回爱技术支持页](./) · [常见问题](faq) · [隐私政策](privacy)

</section>

<section lang="zh-TW" markdown="1">

愛技術支援 **`iTer://`** URL Scheme（**iPhone / iPad**）。可在捷徑、Safari、小工具或其他 App 中開啟題目、每日測驗、收藏或錯題本。

**主畫面捷徑**（長按圖示）使用相同的 `type` 字串。在 **設定 → 主畫面捷徑** 中從 **7 項**裡最多選 **4 項**。

> **說明：** 深度連結僅用於**應用內跳轉**，不會遠端修改測驗設定或題目標記。**Mac** 無主畫面捷徑；小工具與應用內導覽在 Mac 上仍可用。

## 協定

```
iTer://<host>[?query]
```

| 規則 | 說明 |
|------|------|
| **Scheme** | `iTer`（大小寫不敏感） |
| **題目詳情** | Host `question` — 查詢參數 **`id=<題目ID>`** 或 **`q=<題目ID>`**（必填） |
| **每日測驗** | Host `quiz` |
| **收藏** | Host `favorites` → 設定 → 收藏列表 |
| **錯題本** | Host `wrong` / `mistakes` / `wrongquestions` — 可選 **`record=<UUID>`** 開啟單條錯題 |
| **搜尋** | Host `search` — 僅捷徑（開啟全域搜尋 Tab） |
| **分類** | Host `categories` — 僅捷徑（開啟分類 Tab） |
| **回饋** | Host `feedback` — 僅捷徑（郵件撰寫或 `mailto:` 回退） |
| **評分** | Host `review` — 僅捷徑（StoreKit 應用內評分）。含 `star` 的舊 type 仍相容 |

## 範例

```
iTer://question?id=94c34bb2bdef11e6a0e100163e0021c8
iTer://quiz
iTer://favorites
iTer://wrong
iTer://wrong?record=550E8400-E29B-41D4-A716-446655440000
```

## 主畫面捷徑

| Type | 用途 |
|------|------|
| `iTer://search` | 全域搜尋 |
| `iTer://quiz` | 每日測驗 Tab |
| `iTer://favorites` | 收藏列表 |
| `iTer://wrong` | 錯題本 |
| `iTer://categories` | 分類 Tab |
| `iTer://feedback` | 傳送回饋 |
| `iTer://review` | 應用評分（StoreKit） |

預設：搜尋、測驗、收藏、回饋。可在 **設定 → 主畫面捷徑** 中排序或替換（最多 4 項）。應用以 **contains** 匹配 type，相容包含上述路徑的歷史變體。

## 小工具深度連結

| 小工具 | 典型 URL |
|--------|----------|
| 每日一題 | `iTer://question?id=…` |
| 測驗一覽 | `iTer://quiz` |
| 收藏速覽 | `iTer://favorites` |
| 錯題速覽 | `iTer://wrong` 或 `iTer://wrong?record=<UUID>` |

---

[返回愛技術支援頁](./) · [常見問題](faq) · [隱私政策](privacy)

</section>
