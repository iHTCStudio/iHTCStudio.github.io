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
