---
layout: doc
title: iWuBi — URL Scheme Reference
app_id: iWuBi
doc_title_en: URL Scheme Reference
doc_title_zh_cn: URL Scheme 深度链接文档
doc_title_zh_tw: URL Scheme 深度連結文件
description: Complete reference of iWuBi:// deep links, widget links and Home Screen Quick Actions supported by iWuBi.
---

<section lang="en" markdown="1">

iWuBi supports **`iWuBi://`** (case-insensitive scheme `iwubi`) deep links — open lookup, daily quiz, favourites, wrong book, code-length levels, learn hub or typing practice from Safari, Shortcuts, widgets, or another app.

## Protocol

```
iWuBi://<host>[?query]
iWuBi:///path-style   ← host empty; first path segment is the action
```

| Host / action | Opens | Query |
|---------------|-------|-------|
| `search` | Lookup tab, focus search | `q`, `word`, or `name` pre-fills |
| `word`, `char`, `character` | Word detail (or search if query empty) | `q` / `word` / `name` = character |
| `quiz`, `test` | Learn → Daily Quiz | — |
| `favorites`, `favorite` | Settings → Favourites | — |
| `wrong`, `mistakes`, `wrongbook` | Wrong book | `record=<UUID>` → one record |
| `levels`, `level`, `codes` | Levels tab | — |
| `learn`, `study` | Learn tab | — |
| `typing`, `type`, `practice` | Typing tab | — |

## Examples

```
iWuBi://search?q=你好
iWuBi://word?q=好
iWuBi://quiz
iWuBi://wrong?record=550E8400-E29B-41D4-A716-446655440000
iWuBi://levels
iWuBi://typing
```

## Home Screen Quick Actions

Up to **4** in **Settings → Home Screen shortcuts**: `search`, `quiz`, `favorites`, `wrong`, `levels`, `feedback`, `review`. **Feedback** and **review** are Quick Action only.

[Back to overview](..) · [FAQ](faq) · [Privacy](privacy)

</section>

<section lang="zh-CN" markdown="1">

爱五笔支持 **`iWuBi://`**（scheme 不区分大小写，注册为 `iwubi`）深度链接——从 Safari、快捷指令、小组件或其他 App 打开查字、每日测验、收藏、错题本、简码、学习或打字练习。

## 协议

| Host / 动作 | 打开 | 查询参数 |
|-------------|------|----------|
| `search` | 查字 Tab，聚焦搜索 | `q` / `word` / `name` 预填 |
| `word` / `char` / `character` | 字词详情（无参数则仅打开搜索） | `q` / `word` / `name` = 汉字 |
| `quiz` / `test` | 学习 → 每日测验 | — |
| `favorites` | 设置 → 收藏 | — |
| `wrong` / `mistakes` / `wrongbook` | 错题本 | `record=<UUID>` 打开单条 |
| `levels` / `level` / `codes` | 简码 Tab | — |
| `learn` / `study` | 学习 Tab | — |
| `typing` / `type` / `practice` | 打字 Tab | — |

## 示例

```
iWuBi://search?q=你好
iWuBi://word?q=好
iWuBi://quiz
iWuBi://wrong?record=550E8400-E29B-41D4-A716-446655440000
```

## 主屏快捷操作

**设置 → 主屏快捷操作** 最多 **4** 项：`search`、`quiz`、`favorites`、`wrong`、`levels`、`feedback`、`review`。

[返回概览](..) · [常见问题](faq) · [隐私政策](privacy)

</section>

<section lang="zh-TW" markdown="1">

愛五筆支援 **`iWuBi://`**（scheme 不區分大小寫，註冊為 `iwubi`）深度連結——從 Safari、捷徑、小工具或其他 App 開啟查字、每日測驗、收藏、錯題本、簡碼、學習或打字練習。

## 協定

| Host / 動作 | 開啟 | 查詢參數 |
|-------------|------|----------|
| `search` | 查字 Tab，聚焦搜尋 | `q` / `word` / `name` 預填 |
| `word` / `char` / `character` | 字詞詳情 | `q` / `word` / `name` = 漢字 |
| `quiz` / `test` | 學習 → 每日測驗 | — |
| `favorites` | 設定 → 收藏 | — |
| `wrong` / `mistakes` / `wrongbook` | 錯題本 | `record=<UUID>` 開啟單條 |
| `levels` / `level` / `codes` | 簡碼 Tab | — |
| `learn` / `study` | 學習 Tab | — |
| `typing` / `type` / `practice` | 打字 Tab | — |

## 範例

```
iWuBi://search?q=你好
iWuBi://word?q=好
iWuBi://quiz
```

## 主畫面快捷操作

**設定 → 主畫面快捷操作** 最多 **4** 項。

[返回概覽](..) · [常見問題](faq) · [隱私政策](privacy)

</section>
