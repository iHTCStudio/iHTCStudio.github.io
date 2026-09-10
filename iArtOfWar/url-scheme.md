---
layout: doc
title: iArtOfWar — Shortcut Links
app_id: iArtOfWar
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: iartofwar:// deep links for iArtOfWar — passage, daily, recite, study, hunt, collections, themes, settings guides, and more.
---

<section lang="en" markdown="1">

iArtOfWar supports **`iartofwar://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
iartofwar://{host}?{params}
```

## Passages & authors

| URL | Opens |
|-----|-------|
| `iartofwar://passage?id={id}` | Passage detail |
| `iartofwar://couplet?id={id}` / `iartofwar://poem?id={id}` | Same as passage (compatibility) |
| `iartofwar://author?id={id}` | Author detail |
| `iartofwar://recite` / `iartofwar://recite?id={id}` | Recite flow |

## Discovery

| URL | Opens |
|-----|-------|
| `iartofwar://home` | Home |
| `iartofwar://daily` | Today’s Daily Stratagem |
| `iartofwar://random` | Random passage |
| `iartofwar://favorites` | Favorites |
| `iartofwar://famous` | Famous lines / stratagems |
| `iartofwar://search` / `iartofwar://search?q={query}` | Search |
| `iartofwar://study` | Strategy classroom |
| `iartofwar://hunt` | Hunt (寻谋); aliases `keyword-hunt` / `flyflower` |
| `iartofwar://mastered` | Mastered |
| `iartofwar://categories` / `iartofwar://categories?section=` | Browse (`theme`, `volume`, …) |
| `iartofwar://collection?id=` | Book collection (e.g. `sunzi`, `wujing`, `wuzi`; also `name=` / `theme=`) |
| `iartofwar://theme?id=` | Stratagem suite or volume (e.g. `wen-tao`, `winning`, `sunbin-a`) |
| `iartofwar://last-read` | Last read |
| `iartofwar://reading-history` | Reading history |
| `iartofwar://notes` | Notes |

## Settings & guides

| URL | Opens |
|-----|-------|
| `iartofwar://settings` | Settings |
| `iartofwar://usage-guide` | Usage guide |
| `iartofwar://widget-guide` | Widget guide |
| `iartofwar://shortcuts-guide` | Shortcuts guide |
| `iartofwar://feature-guide` | Replay onboarding |
| `iartofwar://feedback` | Feedback email |
| `iartofwar://in-app-review` | In-app / Store review entry |

## Examples

```
iartofwar://daily
iartofwar://passage?id=1
iartofwar://collection?id=wuzi
iartofwar://theme?id=wen-tao
iartofwar://study
iartofwar://hunt
```

Use these in the Shortcuts app, Home Screen quick actions, widgets, or Safari. See also in-app **Settings → Shortcuts Guide**.

</section>

<section lang="zh-CN" markdown="1">

爱兵法支持 **`iartofwar://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
iartofwar://{host}?{params}
```

## 篇目与作者

| URL | 打开 |
|-----|------|
| `iartofwar://passage?id={id}` | 篇目详情 |
| `iartofwar://couplet?id={id}` / `iartofwar://poem?id={id}` | 同上（兼容别名） |
| `iartofwar://author?id={id}` | 作者详情 |
| `iartofwar://recite` / `iartofwar://recite?id={id}` | 诵读 |

## 发现与学习

| URL | 打开 |
|-----|------|
| `iartofwar://home` | 首页 |
| `iartofwar://daily` | 每日一计 |
| `iartofwar://random` | 随机 |
| `iartofwar://favorites` | 收藏 |
| `iartofwar://famous` | 名句 / 名计 |
| `iartofwar://search` / `iartofwar://search?q={query}` | 搜索 |
| `iartofwar://study` | 谋略学堂 |
| `iartofwar://hunt` | 寻谋 |
| `iartofwar://mastered` | 已掌握 |
| `iartofwar://categories` / `iartofwar://categories?section=` | 分类 |
| `iartofwar://collection?id=` | 书目合集（如 `sunzi`、`wujing`、`wuzi`） |
| `iartofwar://theme?id=` | 计套或卷编（如 `wen-tao`、`winning`、`sunbin-a`） |
| `iartofwar://last-read` | 上次阅读 |
| `iartofwar://reading-history` | 浏览记录 |
| `iartofwar://notes` | 笔记 |

## 设置与教程

| URL | 打开 |
|-----|------|
| `iartofwar://settings` | 设置 |
| `iartofwar://usage-guide` | 使用说明 |
| `iartofwar://widget-guide` | 小组件指南 |
| `iartofwar://shortcuts-guide` | 快捷指南 |
| `iartofwar://feature-guide` | 重播功能引导 |
| `iartofwar://feedback` | 反馈邮件 |
| `iartofwar://in-app-review` | 评分入口 |

## 示例

```
iartofwar://daily
iartofwar://passage?id=1
iartofwar://collection?id=wuzi
iartofwar://theme?id=wen-tao
iartofwar://study
iartofwar://hunt
```

可在「快捷指令」、主屏快捷、小组件或 Safari 中使用。详见应用内 **设置 → 快捷指南**。

</section>

<section lang="zh-TW" markdown="1">

愛兵法支援 **`iartofwar://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複開啟。

## 連結格式

```
iartofwar://{host}?{params}
```

## 篇目與作者

| URL | 開啟 |
|-----|------|
| `iartofwar://passage?id={id}` | 篇目詳情 |
| `iartofwar://couplet?id={id}` / `iartofwar://poem?id={id}` | 同上（相容別名） |
| `iartofwar://author?id={id}` | 作者詳情 |
| `iartofwar://recite` / `iartofwar://recite?id={id}` | 誦讀 |

## 發現與學習

| URL | 開啟 |
|-----|------|
| `iartofwar://home` | 首頁 |
| `iartofwar://daily` | 每日一計 |
| `iartofwar://random` | 隨機 |
| `iartofwar://favorites` | 收藏 |
| `iartofwar://famous` | 名句 / 名計 |
| `iartofwar://search` / `iartofwar://search?q={query}` | 搜尋 |
| `iartofwar://study` | 謀略學堂 |
| `iartofwar://hunt` | 尋謀 |
| `iartofwar://mastered` | 已掌握 |
| `iartofwar://categories` / `iartofwar://categories?section=` | 分類 |
| `iartofwar://collection?id=` | 書目合集（如 `sunzi`、`wujing`、`wuzi`） |
| `iartofwar://theme?id=` | 計套或卷編（如 `wen-tao`、`winning`、`sunbin-a`） |
| `iartofwar://last-read` | 上次閱讀 |
| `iartofwar://reading-history` | 瀏覽記錄 |
| `iartofwar://notes` | 筆記 |

## 設定與教學

| URL | 開啟 |
|-----|------|
| `iartofwar://settings` | 設定 |
| `iartofwar://usage-guide` | 使用說明 |
| `iartofwar://widget-guide` | 小工具指南 |
| `iartofwar://shortcuts-guide` | 捷徑指南 |
| `iartofwar://feature-guide` | 重播功能引導 |
| `iartofwar://feedback` | 回饋郵件 |
| `iartofwar://in-app-review` | 評分入口 |

## 範例

```
iartofwar://daily
iartofwar://passage?id=1
iartofwar://collection?id=wuzi
iartofwar://theme?id=wen-tao
iartofwar://study
iartofwar://hunt
```

可在「捷徑」、主畫面捷徑、小工具或 Safari 中使用。詳見應用內 **設定 → 捷徑指南**。

</section>
