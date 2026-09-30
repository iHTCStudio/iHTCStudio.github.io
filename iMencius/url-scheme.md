---
layout: doc
title: iMencius — Shortcut Links
app_id: iMencius
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: imencius:// deep links for iMencius — passage, daily, recite, study, hunt, settings guides, and more.
---

<section lang="en" markdown="1">

iMencius supports **`imencius://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
imencius://{host}?{params}
```

## Passages & authors

| URL | Opens |
|-----|-------|
| `imencius://passage?id={id}` | Passage detail |
| `imencius://saying?id={id}` / `imencius://couplet?id={id}` / `imencius://poem?id={id}` | Same as passage (compatibility) |
| `imencius://passage?id={id}&card=1` | Passage detail and card sheet |
| `imencius://card?id={id}` / `imencius://share-card?id={id}` | 孟 cards |
| `imencius://author?id={id}` | Author detail |
| `imencius://recite` / `imencius://recite?id={id}` | Recite flow |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `imencius://home` | Home |
| `imencius://daily` | Daily Saying |
| `imencius://random` | Random passage |
| `imencius://favorites` | Favorites |
| `imencius://famous` | Famous lines |
| `imencius://search` / `imencius://search?q={query}` | Search |
| `imencius://study` / `imencius://study?id={id}` | Nurturing Qi Study |
| `imencius://hunt` | Yi Hunt (`keyword-hunt` / `flyflower`) |
| `imencius://handwriting` | Handwriting search (`handwrite`; iOS) |
| `imencius://mastered` | Mastered (`progress`) |
| `imencius://categories` / `imencius://categories?section=` | Browse |
| `imencius://collection?id=` | Collection / book |
| `imencius://corpus` | All passages (`all`) |
| `imencius://last-read` | Last read |
| `imencius://reading-history` | Reading history |
| `imencius://notes` | Notes |
| `imencius://fables` / `imencius://allegories` / `imencius://concepts` | Specialty shelves when available |

## Settings & guides

| URL | Opens |
|-----|-------|
| `imencius://settings` | Settings |
| `imencius://usage-guide` | Usage guide |
| `imencius://widget-guide` | Widget guide |
| `imencius://shortcuts-guide` | Shortcuts guide |
| `imencius://feature-guide` | Replay onboarding |
| `imencius://feedback` | Feedback email |
| `imencius://in-app-review` | In-app / Store review entry |

## Examples

```
imencius://daily
imencius://passage?id=1
imencius://study
imencius://hunt
```

</section>

<section lang="zh-CN" markdown="1">

爱孟子 支持 **`imencius://`** 快捷链接（URL Scheme）。冷启动与主屏幕快捷方式经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
imencius://{host}?{params}
```

## 篇目与作者

| URL | 打开 |
|-----|------|
| `imencius://passage?id={id}` | 篇目详情 |
| `imencius://saying?id={id}` / `imencius://couplet?id={id}` / `imencius://poem?id={id}` | 同 passage（兼容） |
| `imencius://passage?id={id}&card=1` | 篇目详情并打开分享卡 |
| `imencius://card?id={id}` / `imencius://share-card?id={id}` | 孟卡 |
| `imencius://author?id={id}` | 作者详情 |
| `imencius://recite` / `imencius://recite?id={id}` | 诵读 |

## 发现与练习

| URL | 打开 |
|-----|------|
| `imencius://home` | 首页 |
| `imencius://daily` | 每日一语 |
| `imencius://random` | 随机一篇 |
| `imencius://favorites` | 收藏 |
| `imencius://famous` | 名句 |
| `imencius://search` / `imencius://search?q={query}` | 搜索 |
| `imencius://study` / `imencius://study?id={id}` | 养气学堂 |
| `imencius://hunt` | 寻义（`keyword-hunt` / `flyflower`） |
| `imencius://handwriting` | 手写寻句（`handwrite`；iOS） |
| `imencius://mastered` | 已掌握（`progress`） |
| `imencius://categories` / `imencius://categories?section=` | 浏览 |
| `imencius://collection?id=` | 合集／分册 |
| `imencius://corpus` | 全部篇目（`all`） |
| `imencius://last-read` | 上次阅读 |
| `imencius://reading-history` | 阅读历史 |
| `imencius://notes` | 笔记 |
| `imencius://fables` / `imencius://allegories` / `imencius://concepts` | 专属书架（如有） |

## 设置与指南

| URL | 打开 |
|-----|------|
| `imencius://settings` | 设置 |
| `imencius://usage-guide` | 使用说明 |
| `imencius://widget-guide` | 小组件说明 |
| `imencius://shortcuts-guide` | 快捷指令说明 |
| `imencius://feature-guide` | 重看功能导览 |
| `imencius://feedback` | 反馈邮件 |
| `imencius://in-app-review` | 应用内／商店评价入口 |

## 示例

```
imencius://daily
imencius://passage?id=1
imencius://study
imencius://hunt
```

</section>

<section lang="zh-TW" markdown="1">

愛孟子 支援 **`imencius://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複打開。

## 連結格式

```
imencius://{host}?{params}
```

## 篇目與作者

| URL | 打開 |
|-----|------|
| `imencius://passage?id={id}` | 篇目詳情 |
| `imencius://saying?id={id}` / `imencius://couplet?id={id}` / `imencius://poem?id={id}` | 同 passage（相容） |
| `imencius://passage?id={id}&card=1` | 篇目詳情並打開分享卡 |
| `imencius://card?id={id}` / `imencius://share-card?id={id}` | 孟卡 |
| `imencius://author?id={id}` | 作者詳情 |
| `imencius://recite` / `imencius://recite?id={id}` | 誦讀 |

## 探索與練習

| URL | 打開 |
|-----|------|
| `imencius://home` | 首頁 |
| `imencius://daily` | 每日一語 |
| `imencius://random` | 隨機一篇 |
| `imencius://favorites` | 收藏 |
| `imencius://famous` | 名句 |
| `imencius://search` / `imencius://search?q={query}` | 搜尋 |
| `imencius://study` / `imencius://study?id={id}` | 養氣學堂 |
| `imencius://hunt` | 尋義（`keyword-hunt` / `flyflower`） |
| `imencius://handwriting` | 手寫尋句（`handwrite`；iOS） |
| `imencius://mastered` | 已掌握（`progress`） |
| `imencius://categories` / `imencius://categories?section=` | 瀏覽 |
| `imencius://collection?id=` | 合集／分冊 |
| `imencius://corpus` | 全部篇目（`all`） |
| `imencius://last-read` | 上次閱讀 |
| `imencius://reading-history` | 閱讀歷史 |
| `imencius://notes` | 筆記 |
| `imencius://fables` / `imencius://allegories` / `imencius://concepts` | 專屬書架（如有） |

## 設定與指南

| URL | 打開 |
|-----|------|
| `imencius://settings` | 設定 |
| `imencius://usage-guide` | 使用說明 |
| `imencius://widget-guide` | 小工具說明 |
| `imencius://shortcuts-guide` | 捷徑說明 |
| `imencius://feature-guide` | 重看功能導覽 |
| `imencius://feedback` | 回饋郵件 |
| `imencius://in-app-review` | 應用內／商店評價入口 |

## 範例

```
imencius://daily
imencius://passage?id=1
imencius://study
imencius://hunt
```

</section>
