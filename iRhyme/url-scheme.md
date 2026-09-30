---
layout: doc
title: iRhyme — Shortcut Links
app_id: iRhyme
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: irhyme:// deep links for iRhyme — passage, daily, recite, study, hunt, collections, settings guides, and more.
---

<section lang="en" markdown="1">

iRhyme supports **`irhyme://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
irhyme://{host}?{params}
```

## Passages & authors

| URL | Opens |
|-----|-------|
| `irhyme://passage?id={id}` | Passage detail |
| `irhyme://saying?id={id}` / `irhyme://couplet?id={id}` / `irhyme://poem?id={id}` | Same as passage (compatibility) |
| `irhyme://passage?id={id}&card=1` | Passage detail and card sheet |
| `irhyme://card?id={id}` / `irhyme://share-card?id={id}` | Rhyme cards |
| `irhyme://author?id={id}` | Author detail |
| `irhyme://recite` / `irhyme://recite?id={id}` | Recite flow |

## Discovery & practice

| URL | Opens |
|-----|-------|
| `irhyme://home` | Home |
| `irhyme://daily` | Today’s Rhyme |
| `irhyme://random` | Random passage |
| `irhyme://favorites` | Favorites |
| `irhyme://famous` | Famous lines |
| `irhyme://search` / `irhyme://search?q={query}` | Search |
| `irhyme://study` / `irhyme://study?id={id}` | Rhyme Academy |
| `irhyme://hunt` | Rhyme Hunt (`keyword-hunt` / `flyflower`) |
| `irhyme://handwriting` | Handwriting search (`handwrite`; iOS) |
| `irhyme://mastered` | Mastered (`progress`) |
| `irhyme://categories` / `irhyme://categories?section=` | Browse |
| `irhyme://collection?id=` | Collection / book (`shenglv` / `liweng` / `qianjia` / `youxue`) |
| `irhyme://corpus` | All passages (`all`) |
| `irhyme://last-read` | Last read |
| `irhyme://reading-history` | Reading history |
| `irhyme://notes` | Notes |
| `irhyme://pair` | Parallelism practice |
| `irhyme://prosody` | Prosody desk |
| `irhyme://rhyme?id=dong` | One rhyme class |
| `irhyme://compare?rhyme=dong` | Same-rhyme compare |
| `irhyme://glossary?id=` | Glossary |

## Settings & guides

| URL | Opens |
|-----|-------|
| `irhyme://settings` | Settings |
| `irhyme://usage-guide` | Usage guide |
| `irhyme://widget-guide` | Widget guide |
| `irhyme://shortcuts-guide` | Shortcuts guide |
| `irhyme://feature-guide` | Replay onboarding |
| `irhyme://feedback` | Feedback email |
| `irhyme://in-app-review` | In-app / Store review entry |

## Examples

```
irhyme://daily
irhyme://passage?id=1001
irhyme://pair
irhyme://compare?rhyme=dong
irhyme://collection?id=shenglv
irhyme://study
irhyme://hunt
```

## Notes

- Parameters are case-sensitive where IDs are numeric.
- Siri, Shortcuts, widgets, and Control Center controls use the same deep-link routes.
- See the in-app **Settings → Help** guides for the latest list.

</section>

<section lang="zh-CN" markdown="1">

爱声律启蒙支持 **`irhyme://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导页结束后重复打开。

## 链接格式

```
irhyme://{host}?{params}
```

## 篇目与作者

| URL | 打开 |
|-----|------|
| `irhyme://passage?id={id}` | 篇目详情 |
| `irhyme://saying?id={id}` / `irhyme://couplet?id={id}` / `irhyme://poem?id={id}` | 同详情（兼容别名） |
| `irhyme://passage?id={id}&card=1` | 详情并弹出韵卡 |
| `irhyme://card?id={id}` / `irhyme://share-card?id={id}` | 韵卡 |
| `irhyme://author?id={id}` | 作者详情 |
| `irhyme://recite` / `irhyme://recite?id={id}` | 诵读 |

## 发现与学堂

| URL | 打开 |
|-----|------|
| `irhyme://home` | 首页 |
| `irhyme://daily` | 今日一律 |
| `irhyme://random` | 随机篇目 |
| `irhyme://favorites` | 收藏 |
| `irhyme://famous` | 金句 |
| `irhyme://search` / `irhyme://search?q={query}` | 搜索 |
| `irhyme://study` / `irhyme://study?id={id}` | 声律学堂 |
| `irhyme://hunt` | 寻对（`keyword-hunt` / `flyflower`） |
| `irhyme://handwriting` | 手写搜索（`handwrite`；iOS） |
| `irhyme://mastered` | 已掌握（`progress`） |
| `irhyme://categories` / `irhyme://categories?section=` | 分类浏览 |
| `irhyme://collection?id=` | 合集 / 典籍（`shenglv` / `liweng` / `qianjia` / `youxue`） |
| `irhyme://corpus` | 全部篇目（`all`） |
| `irhyme://last-read` | 最近阅读 |
| `irhyme://reading-history` | 阅读历史 |
| `irhyme://notes` | 笔记 |
| `irhyme://pair` | 对仗练习 |
| `irhyme://prosody` | 声律工作台 |
| `irhyme://rhyme?id=dong` | 单一韵部 |
| `irhyme://compare?rhyme=dong` | 同韵对照 |
| `irhyme://glossary?id=` | 术语表 |

## 设置与指南

| URL | 打开 |
|-----|------|
| `irhyme://settings` | 设置 |
| `irhyme://usage-guide` | 使用说明 |
| `irhyme://widget-guide` | 小组件指南 |
| `irhyme://shortcuts-guide` | 快捷指南 |
| `irhyme://feature-guide` | 重播功能引导 |
| `irhyme://feedback` | 反馈邮件 |
| `irhyme://in-app-review` | 应用内评价入口 |

## 示例

```
irhyme://daily
irhyme://passage?id=1001
irhyme://pair
irhyme://compare?rhyme=dong
irhyme://collection?id=shenglv
irhyme://study
irhyme://hunt
```

## 说明

- 数字 ID 参数区分大小写。
- Siri、快捷指令、小组件与控制中心使用同一套深链。
- 最新列表见应用内 **设置 → 帮助**。

</section>

<section lang="zh-TW" markdown="1">

愛聲律啟蒙支援 **`irhyme://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導頁結束後重複打開。

## 連結格式

```
irhyme://{host}?{params}
```

## 篇目與作者

| URL | 打開 |
|-----|------|
| `irhyme://passage?id={id}` | 篇目詳情 |
| `irhyme://saying?id={id}` / `irhyme://couplet?id={id}` / `irhyme://poem?id={id}` | 同詳情（相容別名） |
| `irhyme://passage?id={id}&card=1` | 詳情並彈出韻卡 |
| `irhyme://card?id={id}` / `irhyme://share-card?id={id}` | 韻卡 |
| `irhyme://author?id={id}` | 作者詳情 |
| `irhyme://recite` / `irhyme://recite?id={id}` | 誦讀 |

## 發現與學堂

| URL | 打開 |
|-----|------|
| `irhyme://home` | 首頁 |
| `irhyme://daily` | 今日一律 |
| `irhyme://random` | 隨機篇目 |
| `irhyme://favorites` | 收藏 |
| `irhyme://famous` | 金句 |
| `irhyme://search` / `irhyme://search?q={query}` | 搜尋 |
| `irhyme://study` / `irhyme://study?id={id}` | 聲律學堂 |
| `irhyme://hunt` | 尋對（`keyword-hunt` / `flyflower`） |
| `irhyme://handwriting` | 手寫搜尋（`handwrite`；iOS） |
| `irhyme://mastered` | 已掌握（`progress`） |
| `irhyme://categories` / `irhyme://categories?section=` | 分類瀏覽 |
| `irhyme://collection?id=` | 合集 / 典籍（`shenglv` / `liweng` / `qianjia` / `youxue`） |
| `irhyme://corpus` | 全部篇目（`all`） |
| `irhyme://last-read` | 最近閱讀 |
| `irhyme://reading-history` | 閱讀歷史 |
| `irhyme://notes` | 筆記 |
| `irhyme://pair` | 對仗練習 |
| `irhyme://prosody` | 聲律工作臺 |
| `irhyme://rhyme?id=dong` | 單一韻部 |
| `irhyme://compare?rhyme=dong` | 同韻對照 |
| `irhyme://glossary?id=` | 術語表 |

## 設定與指南

| URL | 打開 |
|-----|------|
| `irhyme://settings` | 設定 |
| `irhyme://usage-guide` | 使用說明 |
| `irhyme://widget-guide` | 小工具指南 |
| `irhyme://shortcuts-guide` | 捷徑指南 |
| `irhyme://feature-guide` | 重播功能引導 |
| `irhyme://feedback` | 回饋郵件 |
| `irhyme://in-app-review` | 應用內評價入口 |

## 範例

```
irhyme://daily
irhyme://passage?id=1001
irhyme://pair
irhyme://compare?rhyme=dong
irhyme://collection?id=shenglv
irhyme://study
irhyme://hunt
```

## 說明

- 數字 ID 參數區分大小寫。
- Siri、捷徑、小工具與控制中心使用同一套深鏈。
- 最新列表見應用內 **設定 → 說明**。

</section>
