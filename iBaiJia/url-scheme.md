---
layout: doc
title: iBaiJia — Shortcut Links
app_id: iBaiJia
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: ibaijia:// deep links for iBaiJia — surname, daily, recite, study, search, naming, categories, settings guides, and more.
---

<section lang="en" markdown="1">

iBaiJia supports **`ibaijia://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
ibaijia://{host}?{params}
```

## Core navigation

| URL | Opens |
|-----|-------|
| `ibaijia://home` | Home tab |
| `ibaijia://categories` | Browse / categories |
| `ibaijia://surname?id={id}` | Surname detail |
| `ibaijia://daily` | Today's Daily Surname |
| `ibaijia://random` | Random surname |
| `ibaijia://mySurname` | My Surname |
| `ibaijia://recite` | Recitation studio |
| `ibaijia://favorites` | Favorites |
| `ibaijia://search` / `ibaijia://search?q={query}` | Search |
| `ibaijia://study` | Study Hall |
| `ibaijia://stats` | Statistics |
| `ibaijia://naming` | Naming inspiration |
| `ibaijia://settings` | Settings |

## History & notes

| URL | Opens |
|-----|-------|
| `ibaijia://last-read` | Last read surname |
| `ibaijia://reading-history` | Reading history |
| `ibaijia://notes` | Notes list |
| `ibaijia://mastered` | Mastered / study progress |

## Help & feedback

| URL | Opens |
|-----|-------|
| `ibaijia://feature-guide` | Feature guide (onboarding replay) |
| `ibaijia://usage-guide` | Usage guide |
| `ibaijia://widget-guide` | Widget guide |
| `ibaijia://shortcuts-guide` | Shortcuts guide |
| `ibaijia://feedback` | Feedback mail compose |
| `ibaijia://in-app-review` | In-app review prompt |

## Notes

- Parameters are case-sensitive where IDs are numeric.
- Siri, Shortcuts, widgets, and Control Center controls use the same deep-link routes.
- See the in-app **Settings → Help** guides for the latest list.

</section>

<section lang="zh-CN" markdown="1">

爱百家姓支持 **`ibaijia://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导页结束后重复打开。

## 链接格式

```
ibaijia://{host}?{params}
```

## 核心导航

| URL | 打开 |
|-----|------|
| `ibaijia://home` | 首页 |
| `ibaijia://categories` | 分类浏览 |
| `ibaijia://surname?id={id}` | 姓氏详情 |
| `ibaijia://daily` | 今日一姓 |
| `ibaijia://random` | 随机姓氏 |
| `ibaijia://mySurname` | 我的姓氏 |
| `ibaijia://recite` | 四言诵读 |
| `ibaijia://favorites` | 收藏 |
| `ibaijia://search` / `ibaijia://search?q={query}` | 搜索 |
| `ibaijia://study` | 姓氏学堂 |
| `ibaijia://stats` | 统计 |
| `ibaijia://naming` | 取名灵感 |
| `ibaijia://settings` | 设置 |

## 历史与笔记

| URL | 打开 |
|-----|------|
| `ibaijia://last-read` | 上次阅读 |
| `ibaijia://reading-history` | 阅读历史 |
| `ibaijia://notes` | 笔记列表 |
| `ibaijia://mastered` | 已掌握 / 学堂进度 |

## 帮助与反馈

| URL | 打开 |
|-----|------|
| `ibaijia://feature-guide` | 功能引导（重播引导） |
| `ibaijia://usage-guide` | 使用说明 |
| `ibaijia://widget-guide` | 小组件指南 |
| `ibaijia://shortcuts-guide` | 快捷指令指南 |
| `ibaijia://feedback` | 反馈邮件 |
| `ibaijia://in-app-review` | 应用内好评 |

## 说明

- ID 类参数为数字时请保持正确格式。
- Siri、快捷指令、小组件与控制中心控件使用相同深链路由。
- 最新列表见应用内 **设置 → 帮助**。

</section>

<section lang="zh-TW" markdown="1">

愛百家姓支援 **`ibaijia://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導頁結束後重複開啟。

## 連結格式

```
ibaijia://{host}?{params}
```

## 核心導覽

| URL | 開啟 |
|-----|------|
| `ibaijia://home` | 首頁 |
| `ibaijia://categories` | 分類瀏覽 |
| `ibaijia://surname?id={id}` | 姓氏詳情 |
| `ibaijia://daily` | 今日一姓 |
| `ibaijia://random` | 隨機姓氏 |
| `ibaijia://mySurname` | 我的姓氏 |
| `ibaijia://recite` | 四言誦讀 |
| `ibaijia://favorites` | 收藏 |
| `ibaijia://search` / `ibaijia://search?q={query}` | 搜尋 |
| `ibaijia://study` | 姓氏學堂 |
| `ibaijia://stats` | 統計 |
| `ibaijia://naming` | 取名靈感 |
| `ibaijia://settings` | 設定 |

## 歷史與筆記

| URL | 開啟 |
|-----|------|
| `ibaijia://last-read` | 上次閱讀 |
| `ibaijia://reading-history` | 閱讀歷史 |
| `ibaijia://notes` | 筆記列表 |
| `ibaijia://mastered` | 已掌握 / 學堂進度 |

## 說明

- Siri、捷徑、小工具與控制中心控件使用相同深鏈路由。
- 最新列表見應用內 **設定 → 幫助**。

</section>
