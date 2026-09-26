---
layout: doc
title: iZhuangZi — Shortcut Links
app_id: iZhuangZi
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: izhuangzi:// deep links for iZhuangZi — passage, daily, recite, study, hunt, collections, settings guides, and more.
---

<section lang="en" markdown="1">

iZhuangZi supports **`izhuangzi://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
izhuangzi://{host}?{params}
```

## Passages & authors

| URL | Opens |
|-----|-------|
| `izhuangzi://passage?id={id}` | Passage detail |
| `izhuangzi://saying?id={id}` / `izhuangzi://couplet?id={id}` / `izhuangzi://poem?id={id}` | Same as passage (compatibility) |
| `izhuangzi://passage?id={id}&card=1` | Passage detail and card sheet |
| `izhuangzi://card?id={id}` / `izhuangzi://share-card?id={id}` | 逍遥 cards |
| `izhuangzi://author?id={id}` | Author detail |
| `izhuangzi://recite` / `izhuangzi://recite?id={id}` | Recite flow |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `izhuangzi://home` | Home |
| `izhuangzi://daily` | Daily Zhuangzi |
| `izhuangzi://random` | Random passage |
| `izhuangzi://favorites` | Favorites |
| `izhuangzi://famous` | Famous lines |
| `izhuangzi://search` / `izhuangzi://search?q={query}` | Search |
| `izhuangzi://study` / `izhuangzi://study?id={id}` | Dao Study |
| `izhuangzi://hunt` | Zhuang Hunt (`keyword-hunt` / `flyflower`) |
| `izhuangzi://handwriting` | Handwriting search (`handwrite`; iOS) |
| `izhuangzi://mastered` | Mastered (`progress`) |
| `izhuangzi://categories` / `izhuangzi://categories?section=` | Browse |
| `izhuangzi://collection?id=` | Collection / book (`neipian` / `waipian` / `zapian`) |
| `izhuangzi://corpus` | All passages (`all`) |
| `izhuangzi://last-read` | Last read |
| `izhuangzi://reading-history` | Reading history |
| `izhuangzi://notes` | Notes |
| `izhuangzi://ask` | Ask Zhuangzi |
| `izhuangzi://allegories` | Parables |
| `izhuangzi://concepts` | Concepts |
| `izhuangzi://theme?id=neipian` | Inner / Outer / Miscellaneous |

## Settings & guides

| URL | Opens |
|-----|-------|
| `izhuangzi://settings` | Settings |
| `izhuangzi://usage-guide` | Usage guide |
| `izhuangzi://widget-guide` | Widget guide |
| `izhuangzi://shortcuts-guide` | Shortcuts guide |
| `izhuangzi://feature-guide` | Replay onboarding |
| `izhuangzi://feedback` | Feedback email |
| `izhuangzi://in-app-review` | In-app / Store review entry |

## Examples

```
izhuangzi://daily
izhuangzi://passage?id=1
izhuangzi://ask
izhuangzi://allegories
izhuangzi://collection?id=neipian
izhuangzi://study
izhuangzi://hunt
```

## Notes

- Parameters are case-sensitive where IDs are numeric.
- Siri, Shortcuts, widgets, and Control Center controls use the same deep-link routes.
- See the in-app **Settings → Help** guides for the latest list.

</section>

<section lang="zh-CN" markdown="1">

爱庄子支持 **`izhuangzi://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导页结束后重复打开。

## 链接格式

```
izhuangzi://{host}?{params}
```

## 篇目与作者

| URL | 打开 |
|-----|------|
| `izhuangzi://passage?id={id}` | 篇目详情 |
| `izhuangzi://saying?id={id}` / `izhuangzi://couplet?id={id}` / `izhuangzi://poem?id={id}` | 同详情（兼容别名） |
| `izhuangzi://passage?id={id}&card=1` | 详情并弹出逍遥卡 |
| `izhuangzi://card?id={id}` / `izhuangzi://share-card?id={id}` | 逍遥卡 |
| `izhuangzi://author?id={id}` | 作者详情 |
| `izhuangzi://recite` / `izhuangzi://recite?id={id}` | 诵读 |

## 发现与学堂

| URL | 打开 |
|-----|------|
| `izhuangzi://home` | 首页 |
| `izhuangzi://daily` | 今日一子 |
| `izhuangzi://random` | 随机篇目 |
| `izhuangzi://favorites` | 收藏 |
| `izhuangzi://famous` | 金句 |
| `izhuangzi://search` / `izhuangzi://search?q={query}` | 搜索 |
| `izhuangzi://study` / `izhuangzi://study?id={id}` | 庄学学堂 |
| `izhuangzi://hunt` | 寻庄（`keyword-hunt` / `flyflower`） |
| `izhuangzi://handwriting` | 手写搜索（`handwrite`；iOS） |
| `izhuangzi://mastered` | 已掌握（`progress`） |
| `izhuangzi://categories` / `izhuangzi://categories?section=` | 分类浏览 |
| `izhuangzi://collection?id=` | 合集 / 典籍（`neipian` / `waipian` / `zapian`） |
| `izhuangzi://corpus` | 全部篇目（`all`） |
| `izhuangzi://last-read` | 最近阅读 |
| `izhuangzi://reading-history` | 阅读历史 |
| `izhuangzi://notes` | 笔记 |
| `izhuangzi://ask` | 问庄子 |
| `izhuangzi://allegories` | 寓言 |
| `izhuangzi://concepts` | 概念 |
| `izhuangzi://theme?id=neipian` | 内篇 / 外篇 / 杂篇 |

## 设置与指南

| URL | 打开 |
|-----|------|
| `izhuangzi://settings` | 设置 |
| `izhuangzi://usage-guide` | 使用说明 |
| `izhuangzi://widget-guide` | 小组件指南 |
| `izhuangzi://shortcuts-guide` | 快捷指南 |
| `izhuangzi://feature-guide` | 重播功能引导 |
| `izhuangzi://feedback` | 反馈邮件 |
| `izhuangzi://in-app-review` | 应用内评价入口 |

## 示例

```
izhuangzi://daily
izhuangzi://passage?id=1
izhuangzi://ask
izhuangzi://allegories
izhuangzi://collection?id=neipian
izhuangzi://study
izhuangzi://hunt
```

## 说明

- 数字 ID 参数区分大小写。
- Siri、快捷指令、小组件与控制中心使用同一套深链。
- 最新列表见应用内 **设置 → 帮助**。

</section>

<section lang="zh-TW" markdown="1">

愛莊子支援 **`izhuangzi://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導頁結束後重複打開。

## 連結格式

```
izhuangzi://{host}?{params}
```

## 篇目與作者

| URL | 打開 |
|-----|------|
| `izhuangzi://passage?id={id}` | 篇目詳情 |
| `izhuangzi://saying?id={id}` / `izhuangzi://couplet?id={id}` / `izhuangzi://poem?id={id}` | 同詳情（相容別名） |
| `izhuangzi://passage?id={id}&card=1` | 詳情並彈出逍遙卡 |
| `izhuangzi://card?id={id}` / `izhuangzi://share-card?id={id}` | 逍遙卡 |
| `izhuangzi://author?id={id}` | 作者詳情 |
| `izhuangzi://recite` / `izhuangzi://recite?id={id}` | 誦讀 |

## 發現與學堂

| URL | 打開 |
|-----|------|
| `izhuangzi://home` | 首頁 |
| `izhuangzi://daily` | 今日一子 |
| `izhuangzi://random` | 隨機篇目 |
| `izhuangzi://favorites` | 收藏 |
| `izhuangzi://famous` | 金句 |
| `izhuangzi://search` / `izhuangzi://search?q={query}` | 搜尋 |
| `izhuangzi://study` / `izhuangzi://study?id={id}` | 莊學學堂 |
| `izhuangzi://hunt` | 尋莊（`keyword-hunt` / `flyflower`） |
| `izhuangzi://handwriting` | 手寫搜尋（`handwrite`；iOS） |
| `izhuangzi://mastered` | 已掌握（`progress`） |
| `izhuangzi://categories` / `izhuangzi://categories?section=` | 分類瀏覽 |
| `izhuangzi://collection?id=` | 合集 / 典籍（`neipian` / `waipian` / `zapian`） |
| `izhuangzi://corpus` | 全部篇目（`all`） |
| `izhuangzi://last-read` | 最近閱讀 |
| `izhuangzi://reading-history` | 閱讀歷史 |
| `izhuangzi://notes` | 筆記 |
| `izhuangzi://ask` | 問莊子 |
| `izhuangzi://allegories` | 寓言 |
| `izhuangzi://concepts` | 概念 |
| `izhuangzi://theme?id=neipian` | 內篇 / 外篇 / 雜篇 |

## 設定與指南

| URL | 打開 |
|-----|------|
| `izhuangzi://settings` | 設定 |
| `izhuangzi://usage-guide` | 使用說明 |
| `izhuangzi://widget-guide` | 小工具指南 |
| `izhuangzi://shortcuts-guide` | 捷徑指南 |
| `izhuangzi://feature-guide` | 重播功能引導 |
| `izhuangzi://feedback` | 回饋郵件 |
| `izhuangzi://in-app-review` | 應用內評價入口 |

## 範例

```
izhuangzi://daily
izhuangzi://passage?id=1
izhuangzi://ask
izhuangzi://allegories
izhuangzi://collection?id=neipian
izhuangzi://study
izhuangzi://hunt
```

## 說明

- 數字 ID 參數區分大小寫。
- Siri、捷徑、小工具與控制中心使用同一套深鏈。
- 最新列表見應用內 **設定 → 說明**。

</section>
