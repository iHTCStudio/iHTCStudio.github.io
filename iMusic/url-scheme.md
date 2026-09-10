---
layout: doc
title: iMusic — Shortcut Links
app_id: iMusic
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: imusic:// deep links for iMusic — piece, daily, play, recognize, artists, collections, mood, settings guides, and more.
---

<section lang="en" markdown="1">

iMusic supports **`imusic://`** shortcut links. Cold start and Home Screen shortcuts go through a unified buffer so a link is not opened twice after onboarding.

## Link format

```
imusic://{host}?{params}
```

Scheme is **`imusic`** only.

## Home & today

| URL | Opens |
|-----|-------|
| `imusic://` / `imusic://home` | Home |
| `imusic://daily` / `imusic://today` | Daily Piece (queue is this track only) |
| `imusic://random` | Roam (whole-library shuffle) |
| `imusic://play` | Play |
| `imusic://last` / `imusic://lastheard` | Last heard |

## Pieces & artists

| URL | Opens |
|-----|-------|
| `imusic://piece?id={id}` | Piece guide (`passage` / `song` also accepted) |
| `imusic://artist?id={id}` / `imusic://artist?name={name}` | Artist desk |
| `imusic://artists` / `imusic://singers` | Artist directory |
| `imusic://famous` / `imusic://lines` | Famous lines |

A share-card footer may add `name=` (title · artist) for humans. Matching still uses **`id` only**.

## Browse, search & listen

| URL | Opens |
|-----|-------|
| `imusic://categories` / `imusic://browse` | Browse (`section=catalog` / `all` / `allpieces` → All Pieces) |
| `imusic://collection?id={id}` | Collection (`id=col-all` is the virtual All Pieces list) |
| `imusic://search` / `imusic://search?q={query}` | Search |
| `imusic://favorites` | Favorites |
| `imusic://later` | Favorites, scrolled to Later |
| `imusic://lists` / `imusic://listenlists` | Listen lists |
| `imusic://history` | History |
| `imusic://notes` | Notes |
| `imusic://mastered` | Finished |
| `imusic://streak` / `imusic://footprint` | Streak |

Opening a single piece, the mini bar, or Song ID **resets** the reading queue to that piece. Opening from a collection, search, or artist keeps that list so Next / Previous stay available.

## Song ID, school & mood

| URL | Opens |
|-----|-------|
| `imusic://recognize` / `imusic://shazam` | Song ID |
| `imusic://school` / `imusic://earschool` | Ear school |
| `imusic://timeline` / `imusic://corridor` | Era corridor |
| `imusic://compare` | Compare listening |
| `imusic://mood?id={id}` | Start that mood (`piece=` / `pieceId=` is the starting track only; the mood still matches `id`) |

## Settings & guides

| URL | Opens |
|-----|-------|
| `imusic://settings` | Settings |
| `imusic://usageguide` / `imusic://featureguide` | Usage / feature guide |
| `imusic://widgetguide` | Widget guide |
| `imusic://shortcutsguide` | Shortcuts guide |
| `imusic://feedback` | Feedback |
| `imusic://review` / `imusic://in-app-review` | In-app review (when the store listing is live) |

## Siri & Home Screen

Ask Siri for today’s piece, roam, search, or favorites after you add shortcuts. Configure Home Screen quick actions in **Settings → Shortcuts**. Full examples live in the in-app Shortcuts guide.

[FAQ](faq) · [Privacy Policy](privacy) · [Support](./)

</section>

<section lang="zh-CN" markdown="1">

爱音乐支持 **`imusic://`** 快捷链接。冷启动与主屏快捷会走统一缓冲，避免引导结束后同一条链接打开两次。

## 链接格式

```
imusic://{host}?{params}
```

Scheme **只接受** `imusic`。

## 首页与今日

| URL | 打开 |
|-----|------|
| `imusic://` / `imusic://home` | 首页 |
| `imusic://daily` / `imusic://today` | 今日一乐（阅读队列只含这一首） |
| `imusic://random` | 漫游（整库随机） |
| `imusic://play` | 播放 |
| `imusic://last` / `imusic://lastheard` | 最近在听 |

## 曲目与歌手

| URL | 打开 |
|-----|------|
| `imusic://piece?id={id}` | 赏析（也接受 `passage` / `song`） |
| `imusic://artist?id={id}` / `imusic://artist?name={name}` | 歌手志 |
| `imusic://artists` / `imusic://singers` | 歌手目录 |
| `imusic://famous` / `imusic://lines` | 名句 |

乐卡脚注可带 `name=`（曲名 · 艺人）给人读。匹配**只认 `id`**。

## 浏览、搜索与听单

| URL | 打开 |
|-----|------|
| `imusic://categories` / `imusic://browse` | 分类（`section=catalog` / `all` / `allpieces` → 全部曲目） |
| `imusic://collection?id={id}` | 合集（`id=col-all` 为虚拟全部曲目） |
| `imusic://search` / `imusic://search?q={query}` | 搜索 |
| `imusic://favorites` | 收藏 |
| `imusic://later` | 收藏并滚到稍后听 |
| `imusic://lists` / `imusic://listenlists` | 听单 |
| `imusic://history` | 历史 |
| `imusic://notes` | 笔记 |
| `imusic://mastered` | 已听完 |
| `imusic://streak` / `imusic://footprint` | 打卡 |

打开单曲、迷你条或识曲时，阅读队列会**重置**为这一首。从合集、搜索或歌手作品进入则保留该列表，赏析页可上一首 / 下一首。

## 识曲、小学与心情

| URL | 打开 |
|-----|------|
| `imusic://recognize` / `imusic://shazam` | 听歌识曲 |
| `imusic://school` / `imusic://earschool` | 听音小学 |
| `imusic://timeline` / `imusic://corridor` | 年代走廊 |
| `imusic://compare` | 对比听 |
| `imusic://mood?id={id}` | 从该心情起播（`piece=` 只作起点，匹配心情仍只读 `id`） |

## 设置与教程

| URL | 打开 |
|-----|------|
| `imusic://settings` | 设置 |
| `imusic://usageguide` / `imusic://featureguide` | 使用 / 功能引导 |
| `imusic://widgetguide` | 小组件指南 |
| `imusic://shortcutsguide` | 快捷指南 |
| `imusic://feedback` | 反馈 |
| `imusic://review` / `imusic://in-app-review` | 应用内评价（商店上架后） |

## Siri 与主屏

添加快捷指令后，可对 Siri 说今日一乐、漫游、搜索或收藏。主屏长按快捷在 **设置 → 快捷** 配置。完整示例见应用内快捷指南。

[常见问题](faq) · [隐私政策](privacy) · [支持页](./)

</section>

<section lang="zh-TW" markdown="1">

愛音樂支援 **`imusic://`** 快捷連結。冷啟動與主畫面捷徑會走統一緩衝，避免引導結束後同一條連結打開兩次。

## 連結格式

```
imusic://{host}?{params}
```

Scheme **只接受** `imusic`。

## 首頁與今日

| URL | 打開 |
|-----|------|
| `imusic://` / `imusic://home` | 首頁 |
| `imusic://daily` / `imusic://today` | 今日一樂（閱讀佇列只含這一首） |
| `imusic://random` | 漫遊（整庫隨機） |
| `imusic://play` | 播放 |
| `imusic://last` / `imusic://lastheard` | 最近在聽 |

## 曲目與歌手

| URL | 打開 |
|-----|------|
| `imusic://piece?id={id}` | 賞析（也接受 `passage` / `song`） |
| `imusic://artist?id={id}` / `imusic://artist?name={name}` | 歌手誌 |
| `imusic://artists` / `imusic://singers` | 歌手目錄 |
| `imusic://famous` / `imusic://lines` | 名句 |

樂卡腳註可帶 `name=`（曲名 · 藝人）給人讀。匹配**只認 `id`**。

## 瀏覽、搜尋與聽單

| URL | 打開 |
|-----|------|
| `imusic://categories` / `imusic://browse` | 分類（`section=catalog` / `all` / `allpieces` → 全部曲目） |
| `imusic://collection?id={id}` | 合集（`id=col-all` 為虛擬全部曲目） |
| `imusic://search` / `imusic://search?q={query}` | 搜尋 |
| `imusic://favorites` | 收藏 |
| `imusic://later` | 收藏並滾到稍後聽 |
| `imusic://lists` / `imusic://listenlists` | 聽單 |
| `imusic://history` | 歷史 |
| `imusic://notes` | 筆記 |
| `imusic://mastered` | 已聽完 |
| `imusic://streak` / `imusic://footprint` | 打卡 |

打開單曲、迷你條或識曲時，閱讀佇列會**重置**為這一首。從合集、搜尋或歌手作品進入則保留該列表，賞析頁可上一首 / 下一首。

## 識曲、小學與心情

| URL | 打開 |
|-----|------|
| `imusic://recognize` / `imusic://shazam` | 聽歌識曲 |
| `imusic://school` / `imusic://earschool` | 聽音小學 |
| `imusic://timeline` / `imusic://corridor` | 年代走廊 |
| `imusic://compare` | 對比聽 |
| `imusic://mood?id={id}` | 從該心情起播（`piece=` 只作起點，匹配心情仍只讀 `id`） |

## 設定與教學

| URL | 打開 |
|-----|------|
| `imusic://settings` | 設定 |
| `imusic://usageguide` / `imusic://featureguide` | 使用 / 功能引導 |
| `imusic://widgetguide` | 小工具指南 |
| `imusic://shortcutsguide` | 捷徑指南 |
| `imusic://feedback` | 回饋 |
| `imusic://review` / `imusic://in-app-review` | 應用內評價（商店上架後） |

## Siri 與主畫面

加入捷徑後，可對 Siri 說今日一樂、漫遊、搜尋或收藏。主畫面長按捷徑在 **設定 → 快捷** 設定。完整示例見應用內捷徑指南。

[常見問題](faq) · [隱私政策](privacy) · [支援頁](./)

</section>
