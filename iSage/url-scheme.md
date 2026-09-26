---
layout: doc
title: iSage — Shortcut Links
app_id: iSage
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: isage:// deep links for iSage — passage, daily, recite, study, hunt, collections, themes, settings guides, and more.
---

<section lang="en" markdown="1">

iSage supports **`isage://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
isage://{host}?{params}
```

## Sayings & authors

| URL | Opens |
|-----|-------|
| `isage://passage?id={id}` | Saying detail |
| `isage://saying?id={id}` / `isage://couplet?id={id}` / `isage://poem?id={id}` | Same as passage (compatibility) |
| `isage://passage?id={id}&card=1` | Saying detail and sage-card sheet |
| `isage://card?id={id}` / `isage://share-card?id={id}` | Sage card |
| `isage://author?id={id}` | Author detail |
| `isage://recite` / `isage://recite?id={id}` | Recite flow |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `isage://home` | Home |
| `isage://daily` | Today’s Wisdom |
| `isage://random` | Random saying |
| `isage://favorites` | Favorites |
| `isage://famous` | Famous lines |
| `isage://search` / `isage://search?q={query}` | Search |
| `isage://study` / `isage://study?id={id}` | Sage Academy |
| `isage://hunt` | Sage Hunt (`keyword-hunt` / `flyflower`) |
| `isage://handwriting` | Handwriting search (`handwrite`; iOS) |
| `isage://mastered` | Mastered (`progress`) |
| `isage://categories` / `isage://categories?section=` | Browse |
| `isage://collection?id=guxun` | Classic recension (`zhou-shang` / `zhou-xia`; also `book` / `form`) |
| `isage://corpus` | All sayings (`all`) |
| `isage://theme?id=conduct` | Theme (e.g. `cultivation`, `learning`, `friendship`, `household`, `wealth`, `virtue`, `fortune`, `speech`, `loyalty`, `diligence`, `world`) |
| `isage://last-read` | Last read |
| `isage://reading-history` | Reading history |
| `isage://notes` | Notes |

## Settings & guides

| URL | Opens |
|-----|-------|
| `isage://settings` | Settings |
| `isage://usage-guide` | Usage guide |
| `isage://widget-guide` | Widget guide |
| `isage://shortcuts-guide` | Shortcuts guide |
| `isage://feature-guide` | Replay onboarding |
| `isage://feedback` | Feedback email |
| `isage://in-app-review` | In-app / Store review entry |

## Examples

```
isage://daily
isage://passage?id=1
isage://passage?id=1&card=1
isage://collection?id=guxun
isage://theme?id=conduct
isage://study
isage://hunt
isage://handwriting
```

## Notes

- Parameters are case-sensitive where IDs are numeric.
- Siri, Shortcuts, widgets, and Control Center controls use the same deep-link routes.
- See the in-app **Settings → Help** guides for the latest list.

</section>

<section lang="zh-CN" markdown="1">

爱增广贤文支持 **`isage://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导页结束后重复打开。

## 链接格式

```
isage://{host}?{params}
```

## 贤句与作者

| URL | 打开 |
|-----|------|
| `isage://passage?id={id}` | 贤句详情 |
| `isage://saying?id={id}` / `isage://couplet?id={id}` / `isage://poem?id={id}` | 同详情（兼容别名） |
| `isage://passage?id={id}&card=1` | 详情并弹出贤卡 |
| `isage://card?id={id}` / `isage://share-card?id={id}` | 贤卡 |
| `isage://author?id={id}` | 作者详情 |
| `isage://recite` / `isage://recite?id={id}` | 诵读 |

## 发现与学堂

| URL | 打开 |
|-----|------|
| `isage://home` | 首页 |
| `isage://daily` | 今日一智 |
| `isage://random` | 随机贤句 |
| `isage://favorites` | 收藏 |
| `isage://famous` | 金句 |
| `isage://search` / `isage://search?q={query}` | 搜索 |
| `isage://study` / `isage://study?id={id}` | 贤文学堂 |
| `isage://hunt` | 寻贤（`keyword-hunt` / `flyflower`） |
| `isage://handwriting` | 手写寻贤（`handwrite`；iOS） |
| `isage://mastered` | 已掌握（`progress`） |
| `isage://categories` / `isage://categories?section=` | 分类浏览 |
| `isage://collection?id=guxun` | 古训增广（`zhou-shang` / `zhou-xia`；亦可用 `book` / `form`） |
| `isage://corpus` | 全部贤句（`all`） |
| `isage://theme?id=conduct` | 主题（如 `cultivation`、`learning`、`friendship`、`household`、`wealth`、`virtue`、`fortune`、`speech`、`loyalty`、`diligence`、`world`） |
| `isage://last-read` | 最近阅读 |
| `isage://reading-history` | 阅读历史 |
| `isage://notes` | 笔记 |

## 设置与指南

| URL | 打开 |
|-----|------|
| `isage://settings` | 设置 |
| `isage://usage-guide` | 使用说明 |
| `isage://widget-guide` | 小组件指南 |
| `isage://shortcuts-guide` | 快捷指南 |
| `isage://feature-guide` | 重播功能引导 |
| `isage://feedback` | 反馈邮件 |
| `isage://in-app-review` | 应用内评价入口 |

## 示例

```
isage://daily
isage://passage?id=1
isage://passage?id=1&card=1
isage://collection?id=guxun
isage://theme?id=conduct
isage://study
isage://hunt
isage://handwriting
```

## 说明

- 数字 ID 参数区分大小写。
- Siri、快捷指令、小组件与控制中心使用同一套深链。
- 最新列表见应用内 **设置 → 帮助**。

</section>

<section lang="zh-TW" markdown="1">

愛增廣賢文支援 **`isage://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導頁結束後重複打開。

## 連結格式

```
isage://{host}?{params}
```

## 賢句與作者

| URL | 打開 |
|-----|------|
| `isage://passage?id={id}` | 賢句詳情 |
| `isage://saying?id={id}` / `isage://couplet?id={id}` / `isage://poem?id={id}` | 同詳情（相容別名） |
| `isage://passage?id={id}&card=1` | 詳情並彈出賢卡 |
| `isage://card?id={id}` / `isage://share-card?id={id}` | 賢卡 |
| `isage://author?id={id}` | 作者詳情 |
| `isage://recite` / `isage://recite?id={id}` | 誦讀 |

## 發現與學堂

| URL | 打開 |
|-----|------|
| `isage://home` | 首頁 |
| `isage://daily` | 今日一智 |
| `isage://random` | 隨機賢句 |
| `isage://favorites` | 收藏 |
| `isage://famous` | 金句 |
| `isage://search` / `isage://search?q={query}` | 搜尋 |
| `isage://study` / `isage://study?id={id}` | 賢文學堂 |
| `isage://hunt` | 尋賢（`keyword-hunt` / `flyflower`） |
| `isage://handwriting` | 手寫尋賢（`handwrite`；iOS） |
| `isage://mastered` | 已掌握（`progress`） |
| `isage://categories` / `isage://categories?section=` | 分類瀏覽 |
| `isage://collection?id=guxun` | 古訓增廣（`zhou-shang` / `zhou-xia`；亦可用 `book` / `form`） |
| `isage://corpus` | 全部賢句（`all`） |
| `isage://theme?id=conduct` | 主題（如 `cultivation`、`learning`、`friendship`、`household`、`wealth`、`virtue`、`fortune`、`speech`、`loyalty`、`diligence`、`world`） |
| `isage://last-read` | 最近閱讀 |
| `isage://reading-history` | 閱讀歷史 |
| `isage://notes` | 筆記 |

## 設定與指南

| URL | 打開 |
|-----|------|
| `isage://settings` | 設定 |
| `isage://usage-guide` | 使用說明 |
| `isage://widget-guide` | 小工具指南 |
| `isage://shortcuts-guide` | 捷徑指南 |
| `isage://feature-guide` | 重播功能引導 |
| `isage://feedback` | 回饋郵件 |
| `isage://in-app-review` | 應用內評價入口 |

## 範例

```
isage://daily
isage://passage?id=1
isage://passage?id=1&card=1
isage://collection?id=guxun
isage://theme?id=conduct
isage://study
isage://hunt
isage://handwriting
```

## 說明

- 數字 ID 參數區分大小寫。
- Siri、捷徑、小工具與控制中心使用同一套深鏈。
- 最新列表見應用內 **設定 → 說明**。

</section>
