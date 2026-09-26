---
layout: doc
title: iPrecepts — Shortcut Links
app_id: iPrecepts
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: iprecepts:// deep links for iPrecepts — passage, daily, recite, study, hunt, collections, settings guides, and more.
---

<section lang="en" markdown="1">

iPrecepts supports **`iprecepts://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
iprecepts://{host}?{params}
```

## Passages & authors

| URL | Opens |
|-----|-------|
| `iprecepts://passage?id={id}` | Passage detail |
| `iprecepts://saying?id={id}` / `iprecepts://couplet?id={id}` / `iprecepts://poem?id={id}` | Same as passage (compatibility) |
| `iprecepts://passage?id={id}&card=1` | Passage detail and card sheet |
| `iprecepts://card?id={id}` / `iprecepts://share-card?id={id}` | Precept cards |
| `iprecepts://author?id={id}` | Author detail |
| `iprecepts://recite` / `iprecepts://recite?id={id}` | Recite flow |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `iprecepts://home` | Home |
| `iprecepts://daily` | Daily Precept |
| `iprecepts://random` | Random passage |
| `iprecepts://favorites` | Favorites |
| `iprecepts://famous` | Famous lines |
| `iprecepts://search` / `iprecepts://search?q={query}` | Search |
| `iprecepts://study` / `iprecepts://study?id={id}` | Family Study |
| `iprecepts://hunt` | Precept Hunt (`keyword-hunt` / `flyflower`) |
| `iprecepts://handwriting` | Handwriting search (`handwrite`; iOS) |
| `iprecepts://mastered` | Mastered (`progress`) |
| `iprecepts://categories` / `iprecepts://categories?section=` | Browse |
| `iprecepts://collection?id=` | Collection / book (zhuxi / zhubailu / yanshi / zhuge / zeng / yuanshi / qian / tingxun / shortworks) |
| `iprecepts://corpus` | All passages (`all`) |
| `iprecepts://last-read` | Last read |
| `iprecepts://reading-history` | Reading history |
| `iprecepts://notes` | Notes |
| `iprecepts://compare` | Parallel compare |
| `iprecepts://theme?id=` | Theme |
| `iprecepts://authors` | Authors |

## Settings & guides

| URL | Opens |
|-----|-------|
| `iprecepts://settings` | Settings |
| `iprecepts://usage-guide` | Usage guide |
| `iprecepts://widget-guide` | Widget guide |
| `iprecepts://shortcuts-guide` | Shortcuts guide |
| `iprecepts://feature-guide` | Replay onboarding |
| `iprecepts://feedback` | Feedback email |
| `iprecepts://in-app-review` | In-app / Store review entry |

## Examples

```
iprecepts://daily
iprecepts://passage?id=1
iprecepts://passage?id=1&card=1
iprecepts://compare
iprecepts://collection?id=yanshi
iprecepts://study
iprecepts://hunt
```

## Notes

- Parameters are case-sensitive where IDs are numeric.
- Siri, Shortcuts, widgets, and Control Center controls use the same deep-link routes.
- See the in-app **Settings → Help** guides for the latest list.

</section>

<section lang="zh-CN" markdown="1">

爱家训支持 **`iprecepts://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导页结束后重复打开。

## 链接格式

```
iprecepts://{host}?{params}
```

## 篇目与作者

| URL | 打开 |
|-----|------|
| `iprecepts://passage?id={id}` | 篇目详情 |
| `iprecepts://saying?id={id}` / `iprecepts://couplet?id={id}` / `iprecepts://poem?id={id}` | 同详情（兼容别名） |
| `iprecepts://passage?id={id}&card=1` | 详情并弹出训卡 |
| `iprecepts://card?id={id}` / `iprecepts://share-card?id={id}` | 训卡 |
| `iprecepts://author?id={id}` | 作者详情 |
| `iprecepts://recite` / `iprecepts://recite?id={id}` | 诵读 |

## 发现与学堂

| URL | 打开 |
|-----|------|
| `iprecepts://home` | 首页 |
| `iprecepts://daily` | 今日一训 |
| `iprecepts://random` | 随机篇目 |
| `iprecepts://favorites` | 收藏 |
| `iprecepts://famous` | 金句 |
| `iprecepts://search` / `iprecepts://search?q={query}` | 搜索 |
| `iprecepts://study` / `iprecepts://study?id={id}` | 家训学堂 |
| `iprecepts://hunt` | 寻训（`keyword-hunt` / `flyflower`） |
| `iprecepts://handwriting` | 手写搜索（`handwrite`；iOS） |
| `iprecepts://mastered` | 已掌握（`progress`） |
| `iprecepts://categories` / `iprecepts://categories?section=` | 分类浏览 |
| `iprecepts://collection?id=` | 合集 / 典籍（zhuxi / zhubailu / yanshi / zhuge / zeng / yuanshi / qian / tingxun / shortworks） |
| `iprecepts://corpus` | 全部篇目（`all`） |
| `iprecepts://last-read` | 最近阅读 |
| `iprecepts://reading-history` | 阅读历史 |
| `iprecepts://notes` | 笔记 |
| `iprecepts://compare` | 跨代对照 |
| `iprecepts://theme?id=` | 主题 |
| `iprecepts://authors` | 作者 |

## 设置与指南

| URL | 打开 |
|-----|------|
| `iprecepts://settings` | 设置 |
| `iprecepts://usage-guide` | 使用说明 |
| `iprecepts://widget-guide` | 小组件指南 |
| `iprecepts://shortcuts-guide` | 快捷指南 |
| `iprecepts://feature-guide` | 重播功能引导 |
| `iprecepts://feedback` | 反馈邮件 |
| `iprecepts://in-app-review` | 应用内评价入口 |

## 示例

```
iprecepts://daily
iprecepts://passage?id=1
iprecepts://passage?id=1&card=1
iprecepts://compare
iprecepts://collection?id=yanshi
iprecepts://study
iprecepts://hunt
```

## 说明

- 数字 ID 参数区分大小写。
- Siri、快捷指令、小组件与控制中心使用同一套深链。
- 最新列表见应用内 **设置 → 帮助**。

</section>

<section lang="zh-TW" markdown="1">

愛家訓支援 **`iprecepts://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導頁結束後重複打開。

## 連結格式

```
iprecepts://{host}?{params}
```

## 篇目與作者

| URL | 打開 |
|-----|------|
| `iprecepts://passage?id={id}` | 篇目詳情 |
| `iprecepts://saying?id={id}` / `iprecepts://couplet?id={id}` / `iprecepts://poem?id={id}` | 同詳情（相容別名） |
| `iprecepts://passage?id={id}&card=1` | 詳情並彈出訓卡 |
| `iprecepts://card?id={id}` / `iprecepts://share-card?id={id}` | 訓卡 |
| `iprecepts://author?id={id}` | 作者詳情 |
| `iprecepts://recite` / `iprecepts://recite?id={id}` | 誦讀 |

## 發現與學堂

| URL | 打開 |
|-----|------|
| `iprecepts://home` | 首頁 |
| `iprecepts://daily` | 今日一訓 |
| `iprecepts://random` | 隨機篇目 |
| `iprecepts://favorites` | 收藏 |
| `iprecepts://famous` | 金句 |
| `iprecepts://search` / `iprecepts://search?q={query}` | 搜尋 |
| `iprecepts://study` / `iprecepts://study?id={id}` | 家訓學堂 |
| `iprecepts://hunt` | 尋訓（`keyword-hunt` / `flyflower`） |
| `iprecepts://handwriting` | 手寫搜尋（`handwrite`；iOS） |
| `iprecepts://mastered` | 已掌握（`progress`） |
| `iprecepts://categories` / `iprecepts://categories?section=` | 分類瀏覽 |
| `iprecepts://collection?id=` | 合集 / 典籍（zhuxi / zhubailu / yanshi / zhuge / zeng / yuanshi / qian / tingxun / shortworks） |
| `iprecepts://corpus` | 全部篇目（`all`） |
| `iprecepts://last-read` | 最近閱讀 |
| `iprecepts://reading-history` | 閱讀歷史 |
| `iprecepts://notes` | 筆記 |
| `iprecepts://compare` | 跨代對照 |
| `iprecepts://theme?id=` | 主題 |
| `iprecepts://authors` | 作者 |

## 設定與指南

| URL | 打開 |
|-----|------|
| `iprecepts://settings` | 設定 |
| `iprecepts://usage-guide` | 使用說明 |
| `iprecepts://widget-guide` | 小工具指南 |
| `iprecepts://shortcuts-guide` | 捷徑指南 |
| `iprecepts://feature-guide` | 重播功能引導 |
| `iprecepts://feedback` | 回饋郵件 |
| `iprecepts://in-app-review` | 應用內評價入口 |

## 範例

```
iprecepts://daily
iprecepts://passage?id=1
iprecepts://passage?id=1&card=1
iprecepts://compare
iprecepts://collection?id=yanshi
iprecepts://study
iprecepts://hunt
```

## 說明

- 數字 ID 參數區分大小寫。
- Siri、捷徑、小工具與控制中心使用同一套深鏈。
- 最新列表見應用內 **設定 → 說明**。

</section>
