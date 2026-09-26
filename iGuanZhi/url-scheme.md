---
layout: doc
title: iGuanZhi — Shortcut Links
app_id: iGuanZhi
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: iguanzhi:// deep links for iGuanZhi — passage, daily, recite, study, hunt, settings guides, and more.
---

<section lang="en" markdown="1">

iGuanZhi supports **`iguanzhi://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
iguanzhi://{host}?{params}
```

## Passages & authors

| URL | Opens |
|-----|-------|
| `iguanzhi://passage?id={id}` | Passage detail |
| `iguanzhi://saying?id={id}` / `iguanzhi://couplet?id={id}` / `iguanzhi://poem?id={id}` | Same as passage (compatibility) |
| `iguanzhi://passage?id={id}&card=1` | Passage detail and card sheet |
| `iguanzhi://card?id={id}` / `iguanzhi://share-card?id={id}` | 古 cards |
| `iguanzhi://author?id={id}` | Author detail |
| `iguanzhi://recite` / `iguanzhi://recite?id={id}` | Recite flow |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `iguanzhi://home` | Home |
| `iguanzhi://daily` | Today’s Essay |
| `iguanzhi://random` | Random passage |
| `iguanzhi://favorites` | Favorites |
| `iguanzhi://famous` | Famous lines |
| `iguanzhi://search` / `iguanzhi://search?q={query}` | Search |
| `iguanzhi://study` / `iguanzhi://study?id={id}` | Classics Study |
| `iguanzhi://hunt` | Essay Hunt (`keyword-hunt` / `flyflower`) |
| `iguanzhi://handwriting` | Handwriting search (`handwrite`; iOS) |
| `iguanzhi://mastered` | Mastered (`progress`) |
| `iguanzhi://categories` / `iguanzhi://categories?section=` | Browse |
| `iguanzhi://collection?id=` | Collection / book |
| `iguanzhi://corpus` | All passages (`all`) |
| `iguanzhi://last-read` | Last read |
| `iguanzhi://reading-history` | Reading history |
| `iguanzhi://notes` | Notes |
| `iguanzhi://fables` / `iguanzhi://allegories` / `iguanzhi://concepts` | Specialty shelves when available |

## Settings & guides

| URL | Opens |
|-----|-------|
| `iguanzhi://settings` | Settings |
| `iguanzhi://usage-guide` | Usage guide |
| `iguanzhi://widget-guide` | Widget guide |
| `iguanzhi://shortcuts-guide` | Shortcuts guide |
| `iguanzhi://feature-guide` | Replay onboarding |
| `iguanzhi://feedback` | Feedback email |
| `iguanzhi://in-app-review` | In-app / Store review entry |

## Examples

```
iguanzhi://daily
iguanzhi://passage?id=1
iguanzhi://study
iguanzhi://hunt
```

</section>

<section lang="zh-CN" markdown="1">

爱古文观止 支持 **`iguanzhi://`** 快捷链接（URL Scheme）。冷启动与主屏幕快捷方式经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
iguanzhi://{host}?{params}
```

## 篇目与作者

| URL | 打开 |
|-----|------|
| `iguanzhi://passage?id={id}` | 篇目详情 |
| `iguanzhi://saying?id={id}` / `iguanzhi://couplet?id={id}` / `iguanzhi://poem?id={id}` | 同 passage（兼容） |
| `iguanzhi://passage?id={id}&card=1` | 篇目详情并打开分享卡 |
| `iguanzhi://card?id={id}` / `iguanzhi://share-card?id={id}` | 古卡 |
| `iguanzhi://author?id={id}` | 作者详情 |
| `iguanzhi://recite` / `iguanzhi://recite?id={id}` | 诵读 |

## 发现与练习

| URL | 打开 |
|-----|------|
| `iguanzhi://home` | 首页 |
| `iguanzhi://daily` | 今日一文 |
| `iguanzhi://random` | 随机一篇 |
| `iguanzhi://favorites` | 收藏 |
| `iguanzhi://famous` | 名句 |
| `iguanzhi://search` / `iguanzhi://search?q={query}` | 搜索 |
| `iguanzhi://study` / `iguanzhi://study?id={id}` | 古文学堂 |
| `iguanzhi://hunt` | 寻章（`keyword-hunt` / `flyflower`） |
| `iguanzhi://handwriting` | 手写寻句（`handwrite`；iOS） |
| `iguanzhi://mastered` | 已掌握（`progress`） |
| `iguanzhi://categories` / `iguanzhi://categories?section=` | 浏览 |
| `iguanzhi://collection?id=` | 合集／分册 |
| `iguanzhi://corpus` | 全部篇目（`all`） |
| `iguanzhi://last-read` | 上次阅读 |
| `iguanzhi://reading-history` | 阅读历史 |
| `iguanzhi://notes` | 笔记 |
| `iguanzhi://fables` / `iguanzhi://allegories` / `iguanzhi://concepts` | 专属书架（如有） |

## 设置与指南

| URL | 打开 |
|-----|------|
| `iguanzhi://settings` | 设置 |
| `iguanzhi://usage-guide` | 使用说明 |
| `iguanzhi://widget-guide` | 小组件说明 |
| `iguanzhi://shortcuts-guide` | 快捷指令说明 |
| `iguanzhi://feature-guide` | 重看功能导览 |
| `iguanzhi://feedback` | 反馈邮件 |
| `iguanzhi://in-app-review` | 应用内／商店评价入口 |

## 示例

```
iguanzhi://daily
iguanzhi://passage?id=1
iguanzhi://study
iguanzhi://hunt
```

</section>

<section lang="zh-TW" markdown="1">

愛古文觀止 支援 **`iguanzhi://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複打開。

## 連結格式

```
iguanzhi://{host}?{params}
```

## 篇目與作者

| URL | 打開 |
|-----|------|
| `iguanzhi://passage?id={id}` | 篇目詳情 |
| `iguanzhi://saying?id={id}` / `iguanzhi://couplet?id={id}` / `iguanzhi://poem?id={id}` | 同 passage（相容） |
| `iguanzhi://passage?id={id}&card=1` | 篇目詳情並打開分享卡 |
| `iguanzhi://card?id={id}` / `iguanzhi://share-card?id={id}` | 古卡 |
| `iguanzhi://author?id={id}` | 作者詳情 |
| `iguanzhi://recite` / `iguanzhi://recite?id={id}` | 誦讀 |

## 探索與練習

| URL | 打開 |
|-----|------|
| `iguanzhi://home` | 首頁 |
| `iguanzhi://daily` | 今日一文 |
| `iguanzhi://random` | 隨機一篇 |
| `iguanzhi://favorites` | 收藏 |
| `iguanzhi://famous` | 名句 |
| `iguanzhi://search` / `iguanzhi://search?q={query}` | 搜尋 |
| `iguanzhi://study` / `iguanzhi://study?id={id}` | 古文學堂 |
| `iguanzhi://hunt` | 尋章（`keyword-hunt` / `flyflower`） |
| `iguanzhi://handwriting` | 手寫尋句（`handwrite`；iOS） |
| `iguanzhi://mastered` | 已掌握（`progress`） |
| `iguanzhi://categories` / `iguanzhi://categories?section=` | 瀏覽 |
| `iguanzhi://collection?id=` | 合集／分冊 |
| `iguanzhi://corpus` | 全部篇目（`all`） |
| `iguanzhi://last-read` | 上次閱讀 |
| `iguanzhi://reading-history` | 閱讀歷史 |
| `iguanzhi://notes` | 筆記 |
| `iguanzhi://fables` / `iguanzhi://allegories` / `iguanzhi://concepts` | 專屬書架（如有） |

## 設定與指南

| URL | 打開 |
|-----|------|
| `iguanzhi://settings` | 設定 |
| `iguanzhi://usage-guide` | 使用說明 |
| `iguanzhi://widget-guide` | 小工具說明 |
| `iguanzhi://shortcuts-guide` | 捷徑說明 |
| `iguanzhi://feature-guide` | 重看功能導覽 |
| `iguanzhi://feedback` | 回饋郵件 |
| `iguanzhi://in-app-review` | 應用內／商店評價入口 |

## 範例

```
iguanzhi://daily
iguanzhi://passage?id=1
iguanzhi://study
iguanzhi://hunt
```

</section>
