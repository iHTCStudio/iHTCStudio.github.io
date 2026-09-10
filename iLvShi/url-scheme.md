---
layout: doc
title: iLvShi — Shortcut Links
app_id: iLvShi
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: ilvshi:// deep links for iLvShi — passage, daily, recite, study, hunt, settings guides, and more.
---

<section lang="en" markdown="1">

iLvShi supports **`ilvshi://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
ilvshi://{host}?{params}
```

## Passages & authors

| URL | Opens |
|-----|-------|
| `ilvshi://passage?id={id}` | Passage detail |
| `ilvshi://saying?id={id}` / `ilvshi://couplet?id={id}` / `ilvshi://poem?id={id}` | Same as passage (compatibility) |
| `ilvshi://passage?id={id}&card=1` | Passage detail and card sheet |
| `ilvshi://card?id={id}` / `ilvshi://share-card?id={id}` | 秋 cards |
| `ilvshi://author?id={id}` | Author detail |
| `ilvshi://recite` / `ilvshi://recite?id={id}` | Recite flow |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `ilvshi://home` | Home |
| `ilvshi://daily` | Daily Passage |
| `ilvshi://random` | Random passage |
| `ilvshi://favorites` | Favorites |
| `ilvshi://famous` | Famous lines |
| `ilvshi://search` / `ilvshi://search?q={query}` | Search |
| `ilvshi://study` / `ilvshi://study?id={id}` | Spring–Autumn Study |
| `ilvshi://hunt` | Autumn Hunt (`keyword-hunt` / `flyflower`) |
| `ilvshi://handwriting` | Handwriting search (`handwrite`; iOS) |
| `ilvshi://mastered` | Mastered (`progress`) |
| `ilvshi://categories` / `ilvshi://categories?section=` | Browse |
| `ilvshi://collection?id=` | Collection / book |
| `ilvshi://corpus` | All passages (`all`) |
| `ilvshi://last-read` | Last read |
| `ilvshi://reading-history` | Reading history |
| `ilvshi://notes` | Notes |
| `ilvshi://fables` / `ilvshi://allegories` / `ilvshi://concepts` | Specialty shelves when available |

## Settings & guides

| URL | Opens |
|-----|-------|
| `ilvshi://settings` | Settings |
| `ilvshi://usage-guide` | Usage guide |
| `ilvshi://widget-guide` | Widget guide |
| `ilvshi://shortcuts-guide` | Shortcuts guide |
| `ilvshi://feature-guide` | Replay onboarding |
| `ilvshi://feedback` | Feedback email |
| `ilvshi://in-app-review` | In-app / Store review entry |

## Examples

```
ilvshi://daily
ilvshi://passage?id=1
ilvshi://study
ilvshi://hunt
```

</section>

<section lang="zh-CN" markdown="1">

爱吕氏春秋 支持 **`ilvshi://`** 快捷链接（URL Scheme）。冷启动与主屏幕快捷方式经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
ilvshi://{host}?{params}
```

## 篇目与作者

| URL | 打开 |
|-----|------|
| `ilvshi://passage?id={id}` | 篇目详情 |
| `ilvshi://saying?id={id}` / `ilvshi://couplet?id={id}` / `ilvshi://poem?id={id}` | 同 passage（兼容） |
| `ilvshi://passage?id={id}&card=1` | 篇目详情并打开分享卡 |
| `ilvshi://card?id={id}` / `ilvshi://share-card?id={id}` | 秋卡 |
| `ilvshi://author?id={id}` | 作者详情 |
| `ilvshi://recite` / `ilvshi://recite?id={id}` | 诵读 |

## 发现与练习

| URL | 打开 |
|-----|------|
| `ilvshi://home` | 首页 |
| `ilvshi://daily` | 每日一文 |
| `ilvshi://random` | 随机一篇 |
| `ilvshi://favorites` | 收藏 |
| `ilvshi://famous` | 名句 |
| `ilvshi://search` / `ilvshi://search?q={query}` | 搜索 |
| `ilvshi://study` / `ilvshi://study?id={id}` | 春秋学堂 |
| `ilvshi://hunt` | 寻秋（`keyword-hunt` / `flyflower`） |
| `ilvshi://handwriting` | 手写寻句（`handwrite`；iOS） |
| `ilvshi://mastered` | 已掌握（`progress`） |
| `ilvshi://categories` / `ilvshi://categories?section=` | 浏览 |
| `ilvshi://collection?id=` | 合集／分册 |
| `ilvshi://corpus` | 全部篇目（`all`） |
| `ilvshi://last-read` | 上次阅读 |
| `ilvshi://reading-history` | 阅读历史 |
| `ilvshi://notes` | 笔记 |
| `ilvshi://fables` / `ilvshi://allegories` / `ilvshi://concepts` | 专属书架（如有） |

## 设置与指南

| URL | 打开 |
|-----|------|
| `ilvshi://settings` | 设置 |
| `ilvshi://usage-guide` | 使用说明 |
| `ilvshi://widget-guide` | 小组件说明 |
| `ilvshi://shortcuts-guide` | 快捷指令说明 |
| `ilvshi://feature-guide` | 重看功能导览 |
| `ilvshi://feedback` | 反馈邮件 |
| `ilvshi://in-app-review` | 应用内／商店评价入口 |

## 示例

```
ilvshi://daily
ilvshi://passage?id=1
ilvshi://study
ilvshi://hunt
```

</section>

<section lang="zh-TW" markdown="1">

愛呂氏春秋 支援 **`ilvshi://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複打開。

## 連結格式

```
ilvshi://{host}?{params}
```

## 篇目與作者

| URL | 打開 |
|-----|------|
| `ilvshi://passage?id={id}` | 篇目詳情 |
| `ilvshi://saying?id={id}` / `ilvshi://couplet?id={id}` / `ilvshi://poem?id={id}` | 同 passage（相容） |
| `ilvshi://passage?id={id}&card=1` | 篇目詳情並打開分享卡 |
| `ilvshi://card?id={id}` / `ilvshi://share-card?id={id}` | 秋卡 |
| `ilvshi://author?id={id}` | 作者詳情 |
| `ilvshi://recite` / `ilvshi://recite?id={id}` | 誦讀 |

## 探索與練習

| URL | 打開 |
|-----|------|
| `ilvshi://home` | 首頁 |
| `ilvshi://daily` | 每日一文 |
| `ilvshi://random` | 隨機一篇 |
| `ilvshi://favorites` | 收藏 |
| `ilvshi://famous` | 名句 |
| `ilvshi://search` / `ilvshi://search?q={query}` | 搜尋 |
| `ilvshi://study` / `ilvshi://study?id={id}` | 春秋學堂 |
| `ilvshi://hunt` | 尋秋（`keyword-hunt` / `flyflower`） |
| `ilvshi://handwriting` | 手寫尋句（`handwrite`；iOS） |
| `ilvshi://mastered` | 已掌握（`progress`） |
| `ilvshi://categories` / `ilvshi://categories?section=` | 瀏覽 |
| `ilvshi://collection?id=` | 合集／分冊 |
| `ilvshi://corpus` | 全部篇目（`all`） |
| `ilvshi://last-read` | 上次閱讀 |
| `ilvshi://reading-history` | 閱讀歷史 |
| `ilvshi://notes` | 筆記 |
| `ilvshi://fables` / `ilvshi://allegories` / `ilvshi://concepts` | 專屬書架（如有） |

## 設定與指南

| URL | 打開 |
|-----|------|
| `ilvshi://settings` | 設定 |
| `ilvshi://usage-guide` | 使用說明 |
| `ilvshi://widget-guide` | 小工具說明 |
| `ilvshi://shortcuts-guide` | 捷徑說明 |
| `ilvshi://feature-guide` | 重看功能導覽 |
| `ilvshi://feedback` | 回饋郵件 |
| `ilvshi://in-app-review` | 應用內／商店評價入口 |

## 範例

```
ilvshi://daily
ilvshi://passage?id=1
ilvshi://study
ilvshi://hunt
```

</section>
