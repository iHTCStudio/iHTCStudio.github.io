---
layout: doc
title: iHanFei — Shortcut Links
app_id: iHanFei
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: ihanfei:// deep links for iHanFei — passage, daily, recite, study, hunt, settings guides, and more.
---

<section lang="en" markdown="1">

iHanFei supports **`ihanfei://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
ihanfei://{host}?{params}
```

## Passages & authors

| URL | Opens |
|-----|-------|
| `ihanfei://passage?id={id}` | Passage detail |
| `ihanfei://saying?id={id}` / `ihanfei://couplet?id={id}` / `ihanfei://poem?id={id}` | Same as passage (compatibility) |
| `ihanfei://passage?id={id}&card=1` | Passage detail and card sheet |
| `ihanfei://card?id={id}` / `ihanfei://share-card?id={id}` | 法 cards |
| `ihanfei://author?id={id}` | Author detail |
| `ihanfei://recite` / `ihanfei://recite?id={id}` | Recite flow |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `ihanfei://home` | Home |
| `ihanfei://daily` | Daily Stratagem |
| `ihanfei://random` | Random passage |
| `ihanfei://favorites` | Favorites |
| `ihanfei://famous` | Famous lines |
| `ihanfei://search` / `ihanfei://search?q={query}` | Search |
| `ihanfei://study` / `ihanfei://study?id={id}` | Legalism Study |
| `ihanfei://hunt` | Law Hunt (`keyword-hunt` / `flyflower`) |
| `ihanfei://handwriting` | Handwriting search (`handwrite`; iOS) |
| `ihanfei://mastered` | Mastered (`progress`) |
| `ihanfei://categories` / `ihanfei://categories?section=` | Browse |
| `ihanfei://collection?id=` | Collection / book |
| `ihanfei://corpus` | All passages (`all`) |
| `ihanfei://last-read` | Last read |
| `ihanfei://reading-history` | Reading history |
| `ihanfei://notes` | Notes |
| `ihanfei://fables` / `ihanfei://allegories` / `ihanfei://concepts` | Specialty shelves when available |

## Settings & guides

| URL | Opens |
|-----|-------|
| `ihanfei://settings` | Settings |
| `ihanfei://usage-guide` | Usage guide |
| `ihanfei://widget-guide` | Widget guide |
| `ihanfei://shortcuts-guide` | Shortcuts guide |
| `ihanfei://feature-guide` | Replay onboarding |
| `ihanfei://feedback` | Feedback email |
| `ihanfei://in-app-review` | In-app / Store review entry |

## Examples

```
ihanfei://daily
ihanfei://passage?id=1
ihanfei://study
ihanfei://hunt
```

</section>

<section lang="zh-CN" markdown="1">

爱韩非子 支持 **`ihanfei://`** 快捷链接（URL Scheme）。冷启动与主屏幕快捷方式经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
ihanfei://{host}?{params}
```

## 篇目与作者

| URL | 打开 |
|-----|------|
| `ihanfei://passage?id={id}` | 篇目详情 |
| `ihanfei://saying?id={id}` / `ihanfei://couplet?id={id}` / `ihanfei://poem?id={id}` | 同 passage（兼容） |
| `ihanfei://passage?id={id}&card=1` | 篇目详情并打开分享卡 |
| `ihanfei://card?id={id}` / `ihanfei://share-card?id={id}` | 法卡 |
| `ihanfei://author?id={id}` | 作者详情 |
| `ihanfei://recite` / `ihanfei://recite?id={id}` | 诵读 |

## 发现与练习

| URL | 打开 |
|-----|------|
| `ihanfei://home` | 首页 |
| `ihanfei://daily` | 每日一法 |
| `ihanfei://random` | 随机一篇 |
| `ihanfei://favorites` | 收藏 |
| `ihanfei://famous` | 名句 |
| `ihanfei://search` / `ihanfei://search?q={query}` | 搜索 |
| `ihanfei://study` / `ihanfei://study?id={id}` | 法家学堂 |
| `ihanfei://hunt` | 寻法（`keyword-hunt` / `flyflower`） |
| `ihanfei://handwriting` | 手写寻句（`handwrite`；iOS） |
| `ihanfei://mastered` | 已掌握（`progress`） |
| `ihanfei://categories` / `ihanfei://categories?section=` | 浏览 |
| `ihanfei://collection?id=` | 合集／分册 |
| `ihanfei://corpus` | 全部篇目（`all`） |
| `ihanfei://last-read` | 上次阅读 |
| `ihanfei://reading-history` | 阅读历史 |
| `ihanfei://notes` | 笔记 |
| `ihanfei://fables` / `ihanfei://allegories` / `ihanfei://concepts` | 专属书架（如有） |

## 设置与指南

| URL | 打开 |
|-----|------|
| `ihanfei://settings` | 设置 |
| `ihanfei://usage-guide` | 使用说明 |
| `ihanfei://widget-guide` | 小组件说明 |
| `ihanfei://shortcuts-guide` | 快捷指令说明 |
| `ihanfei://feature-guide` | 重看功能导览 |
| `ihanfei://feedback` | 反馈邮件 |
| `ihanfei://in-app-review` | 应用内／商店评价入口 |

## 示例

```
ihanfei://daily
ihanfei://passage?id=1
ihanfei://study
ihanfei://hunt
```

</section>

<section lang="zh-TW" markdown="1">

愛韓非子 支援 **`ihanfei://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複打開。

## 連結格式

```
ihanfei://{host}?{params}
```

## 篇目與作者

| URL | 打開 |
|-----|------|
| `ihanfei://passage?id={id}` | 篇目詳情 |
| `ihanfei://saying?id={id}` / `ihanfei://couplet?id={id}` / `ihanfei://poem?id={id}` | 同 passage（相容） |
| `ihanfei://passage?id={id}&card=1` | 篇目詳情並打開分享卡 |
| `ihanfei://card?id={id}` / `ihanfei://share-card?id={id}` | 法卡 |
| `ihanfei://author?id={id}` | 作者詳情 |
| `ihanfei://recite` / `ihanfei://recite?id={id}` | 誦讀 |

## 探索與練習

| URL | 打開 |
|-----|------|
| `ihanfei://home` | 首頁 |
| `ihanfei://daily` | 每日一法 |
| `ihanfei://random` | 隨機一篇 |
| `ihanfei://favorites` | 收藏 |
| `ihanfei://famous` | 名句 |
| `ihanfei://search` / `ihanfei://search?q={query}` | 搜尋 |
| `ihanfei://study` / `ihanfei://study?id={id}` | 法家學堂 |
| `ihanfei://hunt` | 尋法（`keyword-hunt` / `flyflower`） |
| `ihanfei://handwriting` | 手寫尋句（`handwrite`；iOS） |
| `ihanfei://mastered` | 已掌握（`progress`） |
| `ihanfei://categories` / `ihanfei://categories?section=` | 瀏覽 |
| `ihanfei://collection?id=` | 合集／分冊 |
| `ihanfei://corpus` | 全部篇目（`all`） |
| `ihanfei://last-read` | 上次閱讀 |
| `ihanfei://reading-history` | 閱讀歷史 |
| `ihanfei://notes` | 筆記 |
| `ihanfei://fables` / `ihanfei://allegories` / `ihanfei://concepts` | 專屬書架（如有） |

## 設定與指南

| URL | 打開 |
|-----|------|
| `ihanfei://settings` | 設定 |
| `ihanfei://usage-guide` | 使用說明 |
| `ihanfei://widget-guide` | 小工具說明 |
| `ihanfei://shortcuts-guide` | 捷徑說明 |
| `ihanfei://feature-guide` | 重看功能導覽 |
| `ihanfei://feedback` | 回饋郵件 |
| `ihanfei://in-app-review` | 應用內／商店評價入口 |

## 範例

```
ihanfei://daily
ihanfei://passage?id=1
ihanfei://study
ihanfei://hunt
```

</section>
