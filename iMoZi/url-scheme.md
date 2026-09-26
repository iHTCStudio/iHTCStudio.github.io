---
layout: doc
title: iMoZi — Shortcut Links
app_id: iMoZi
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: imozi:// deep links for iMoZi — passage, daily, recite, study, hunt, settings guides, and more.
---

<section lang="en" markdown="1">

iMoZi supports **`imozi://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
imozi://{host}?{params}
```

## Passages & authors

| URL | Opens |
|-----|-------|
| `imozi://passage?id={id}` | Passage detail |
| `imozi://saying?id={id}` / `imozi://couplet?id={id}` / `imozi://poem?id={id}` | Same as passage (compatibility) |
| `imozi://passage?id={id}&card=1` | Passage detail and card sheet |
| `imozi://card?id={id}` / `imozi://share-card?id={id}` | 墨 cards |
| `imozi://author?id={id}` | Author detail |
| `imozi://recite` / `imozi://recite?id={id}` | Recite flow |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `imozi://home` | Home |
| `imozi://daily` | Today’s Mo |
| `imozi://random` | Random passage |
| `imozi://favorites` | Favorites |
| `imozi://famous` | Famous lines |
| `imozi://search` / `imozi://search?q={query}` | Search |
| `imozi://study` / `imozi://study?id={id}` | Mohism Study |
| `imozi://hunt` | Sentence Hunt (`keyword-hunt` / `flyflower`) |
| `imozi://handwriting` | Handwriting search (`handwrite`; iOS) |
| `imozi://mastered` | Mastered (`progress`) |
| `imozi://categories` / `imozi://categories?section=` | Browse |
| `imozi://collection?id=` | Collection / book |
| `imozi://corpus` | All passages (`all`) |
| `imozi://last-read` | Last read |
| `imozi://reading-history` | Reading history |
| `imozi://notes` | Notes |
| `imozi://ask` | Ask Mozi |
| `imozi://fables` / `imozi://allegories` / `imozi://concepts` | Specialty shelves when available |

## Settings & guides

| URL | Opens |
|-----|-------|
| `imozi://settings` | Settings |
| `imozi://usage-guide` | Usage guide |
| `imozi://widget-guide` | Widget guide |
| `imozi://shortcuts-guide` | Shortcuts guide |
| `imozi://feature-guide` | Replay onboarding |
| `imozi://feedback` | Feedback email |
| `imozi://in-app-review` | In-app / Store review entry |

## Examples

```
imozi://daily
imozi://passage?id=1
imozi://ask
imozi://study
imozi://hunt
```

</section>

<section lang="zh-CN" markdown="1">

爱墨子 支持 **`imozi://`** 快捷链接（URL Scheme）。冷启动与主屏幕快捷方式经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
imozi://{host}?{params}
```

## 篇目与作者

| URL | 打开 |
|-----|------|
| `imozi://passage?id={id}` | 篇目详情 |
| `imozi://saying?id={id}` / `imozi://couplet?id={id}` / `imozi://poem?id={id}` | 同 passage（兼容） |
| `imozi://passage?id={id}&card=1` | 篇目详情并打开分享卡 |
| `imozi://card?id={id}` / `imozi://share-card?id={id}` | 墨卡 |
| `imozi://author?id={id}` | 作者详情 |
| `imozi://recite` / `imozi://recite?id={id}` | 诵读 |

## 发现与练习

| URL | 打开 |
|-----|------|
| `imozi://home` | 首页 |
| `imozi://daily` | 今日一墨 |
| `imozi://random` | 随机一篇 |
| `imozi://favorites` | 收藏 |
| `imozi://famous` | 名句 |
| `imozi://search` / `imozi://search?q={query}` | 搜索 |
| `imozi://study` / `imozi://study?id={id}` | 墨学学堂 |
| `imozi://hunt` | 寻句（`keyword-hunt` / `flyflower`） |
| `imozi://handwriting` | 手写寻句（`handwrite`；iOS） |
| `imozi://mastered` | 已掌握（`progress`） |
| `imozi://categories` / `imozi://categories?section=` | 浏览 |
| `imozi://collection?id=` | 合集／分册 |
| `imozi://corpus` | 全部篇目（`all`） |
| `imozi://last-read` | 上次阅读 |
| `imozi://reading-history` | 阅读历史 |
| `imozi://notes` | 笔记 |
| `imozi://ask` | 问墨子 |
| `imozi://fables` / `imozi://allegories` / `imozi://concepts` | 专属书架（如有） |

## 设置与指南

| URL | 打开 |
|-----|------|
| `imozi://settings` | 设置 |
| `imozi://usage-guide` | 使用说明 |
| `imozi://widget-guide` | 小组件说明 |
| `imozi://shortcuts-guide` | 快捷指令说明 |
| `imozi://feature-guide` | 重看功能导览 |
| `imozi://feedback` | 反馈邮件 |
| `imozi://in-app-review` | 应用内／商店评价入口 |

## 示例

```
imozi://daily
imozi://passage?id=1
imozi://ask
imozi://study
imozi://hunt
```

</section>

<section lang="zh-TW" markdown="1">

愛墨子 支援 **`imozi://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複打開。

## 連結格式

```
imozi://{host}?{params}
```

## 篇目與作者

| URL | 打開 |
|-----|------|
| `imozi://passage?id={id}` | 篇目詳情 |
| `imozi://saying?id={id}` / `imozi://couplet?id={id}` / `imozi://poem?id={id}` | 同 passage（相容） |
| `imozi://passage?id={id}&card=1` | 篇目詳情並打開分享卡 |
| `imozi://card?id={id}` / `imozi://share-card?id={id}` | 墨卡 |
| `imozi://author?id={id}` | 作者詳情 |
| `imozi://recite` / `imozi://recite?id={id}` | 誦讀 |

## 探索與練習

| URL | 打開 |
|-----|------|
| `imozi://home` | 首頁 |
| `imozi://daily` | 今日一墨 |
| `imozi://random` | 隨機一篇 |
| `imozi://favorites` | 收藏 |
| `imozi://famous` | 名句 |
| `imozi://search` / `imozi://search?q={query}` | 搜尋 |
| `imozi://study` / `imozi://study?id={id}` | 墨學學堂 |
| `imozi://hunt` | 尋句（`keyword-hunt` / `flyflower`） |
| `imozi://handwriting` | 手寫尋句（`handwrite`；iOS） |
| `imozi://mastered` | 已掌握（`progress`） |
| `imozi://categories` / `imozi://categories?section=` | 瀏覽 |
| `imozi://collection?id=` | 合集／分冊 |
| `imozi://corpus` | 全部篇目（`all`） |
| `imozi://last-read` | 上次閱讀 |
| `imozi://reading-history` | 閱讀歷史 |
| `imozi://notes` | 筆記 |
| `imozi://ask` | 問墨子 |
| `imozi://fables` / `imozi://allegories` / `imozi://concepts` | 專屬書架（如有） |

## 設定與指南

| URL | 打開 |
|-----|------|
| `imozi://settings` | 設定 |
| `imozi://usage-guide` | 使用說明 |
| `imozi://widget-guide` | 小工具說明 |
| `imozi://shortcuts-guide` | 捷徑說明 |
| `imozi://feature-guide` | 重看功能導覽 |
| `imozi://feedback` | 回饋郵件 |
| `imozi://in-app-review` | 應用內／商店評價入口 |

## 範例

```
imozi://daily
imozi://passage?id=1
imozi://ask
imozi://study
imozi://hunt
```

</section>
