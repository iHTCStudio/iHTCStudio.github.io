---
layout: doc
title: iEnglish — URL Scheme Reference
app_id: iEnglish
doc_title_en: URL Scheme Reference
doc_title_zh_cn: URL Scheme 深度链接文档
doc_title_zh_tw: URL Scheme 深度連結文件
description: Complete reference of ienglish:// deep links, widget links and Home Screen Quick Actions supported by iEnglish.
---

<section lang="en" markdown="1">

iEnglish supports **`ienglish://`** URL scheme deep links — open a word, the Daily Quiz, Favourites, Wrong Book, playlist or categories from Safari, Shortcuts, widgets, or another app.

**Home Screen Quick Actions** (long-press the app icon) add Search, Feedback and Rate — those types are **not** parsed by `IEnglishDeepLink` but still open the app via the shortcut observer.

> **Note:** Links only **navigate** inside the app. They do not start pronunciation or change study settings remotely.

## Protocol

```
ienglish://<host>[?query]
```

| Rule | Detail |
|------|--------|
| **Scheme** | `ienglish` (case-insensitive) |
| **Word detail** | Host `word` — query **`id=<wordID>`** (required, non-empty) |
| **Quiz** | Host `quiz` |
| **Favourites** | Host `favorites` |
| **Wrong book** | Host `wrong` or `mistakes` — optional `record=<UUID>` opens one mistake |
| **Playlist** | Host `playlist` |
| **Categories** | Host `categories` |

## Examples

```
ienglish://word?id=apple
ienglish://quiz
ienglish://favorites
ienglish://wrong
ienglish://wrong?record=550E8400-E29B-41D4-A716-446655440000
ienglish://playlist
ienglish://categories
```

## Home Screen Quick Actions

Configure up to **4** in **Settings → Home Screen shortcuts**. Types include `ienglish://search`, `quiz`, `favorites`, `wrong`, `categories`, `feedback`, `review` — Search / Feedback / Review are delivered as Quick Actions only.

## Widget deep links

Widget taps use the same `ienglish://` hosts (e.g. Daily Quiz → `quiz`, Favourites glance → `favorites`).

[Back to overview](..) · [FAQ](faq) · [Privacy](privacy)

</section>

<section lang="zh-CN" markdown="1">

爱英语支持 **`ienglish://`** 深度链接——从 Safari、快捷指令、小组件或其他 App 打开单词详情、每日测验、收藏、错题本、播放列表或分类。

**主屏快捷操作**（长按图标）另提供搜索、反馈、评分等入口；其中 **搜索 / 反馈 / 评分** 仅通过 Quick Action 分发，不经 `IEnglishDeepLink.parse`。

> **说明：** 链接仅用于 **App 内导航**，不会远程播放发音或修改学习设置。

## 协议

```
ienglish://<host>[?query]
```

| 规则 | 说明 |
|------|------|
| **Scheme** | `ienglish`（不区分大小写） |
| **单词详情** | Host `word` — 查询参数 **`id=<wordID>`**（必填） |
| **每日测验** | Host `quiz` |
| **收藏** | Host `favorites` |
| **错题本** | Host `wrong` 或 `mistakes` — 可选 `record=<UUID>` 打开单条错题 |
| **播放列表** | Host `playlist` |
| **分类** | Host `categories` |

## 示例

```
ienglish://word?id=apple
ienglish://quiz
ienglish://favorites
ienglish://wrong
ienglish://wrong?record=550E8400-E29B-41D4-A716-446655440000
ienglish://playlist
ienglish://categories
```

## 主屏快捷操作

在 **设置 → 主屏快捷操作** 中最多选 **4** 项，类型含 `ienglish://search`、`quiz`、`favorites`、`wrong`、`categories`、`feedback`、`review`。

## 小组件深度链接

小组件点击使用相同 `ienglish://` 路径（如每日测验 → `quiz`）。

[返回概览](..) · [常见问题](faq) · [隐私政策](privacy)

</section>

<section lang="zh-TW" markdown="1">

愛英語支援 **`ienglish://`** 深度連結——從 Safari、捷徑、小工具或其他 App 開啟單字詳情、每日測驗、收藏、錯題本、播放清單或分類。

**主畫面快捷操作**（長按圖示）另提供搜尋、回饋、評分等入口；其中 **搜尋 / 回饋 / 評分** 僅透過 Quick Action 分發，不經 `IEnglishDeepLink.parse`。

> **說明：** 連結僅用於 **App 內導覽**，不會遠端播放發音或修改學習設定。

## 協定

```
ienglish://<host>[?query]
```

| 規則 | 說明 |
|------|------|
| **Scheme** | `ienglish`（不區分大小寫） |
| **單字詳情** | Host `word` — 查詢參數 **`id=<wordID>`**（必填） |
| **每日測驗** | Host `quiz` |
| **收藏** | Host `favorites` |
| **錯題本** | Host `wrong` 或 `mistakes` — 可選 `record=<UUID>` 開啟單條錯題 |
| **播放清單** | Host `playlist` |
| **分類** | Host `categories` |

## 範例

```
ienglish://word?id=apple
ienglish://quiz
ienglish://favorites
ienglish://wrong
ienglish://wrong?record=550E8400-E29B-41D4-A716-446655440000
ienglish://playlist
ienglish://categories
```

## 主畫面快捷操作

在 **設定 → 主畫面快捷操作** 中最多選 **4** 項，類型含 `ienglish://search`、`quiz`、`favorites`、`wrong`、`categories`、`feedback`、`review`。

## 小工具深度連結

小工具點擊使用相同 `ienglish://` 路徑（如每日測驗 → `quiz`）。

[返回概覽](..) · [常見問題](faq) · [隱私政策](privacy)

</section>
