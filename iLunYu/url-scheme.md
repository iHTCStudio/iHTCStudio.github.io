---
layout: doc
title: iLunYu — Shortcut Links
app_id: iLunYu
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: ilunyu:// deep links for iLunYu — passage, daily, recite, study, hunt, themes, settings guides, and more.
---

<section lang="en" markdown="1">

iLunYu supports **`ilunyu://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
ilunyu://{host}?{params}
```

## Chapters & authors

| URL | Opens |
|-----|-------|
| `ilunyu://passage?id={id}` | Chapter detail |
| `ilunyu://couplet?id={id}` / `ilunyu://poem?id={id}` | Same as passage (compatibility) |
| `ilunyu://author?id={id}` | Author detail |
| `ilunyu://recite` | Recite flow |
| `ilunyu://recite?id={id}` | Open chapter and auto-recite |

## Discovery

| URL | Opens |
|-----|-------|
| `ilunyu://home` | Home tab |
| `ilunyu://daily` | Today’s Daily Verse |
| `ilunyu://random` | Random chapter |
| `ilunyu://favorites` | Favorites |
| `ilunyu://famous` | Famous lines |
| `ilunyu://search` / `ilunyu://search?q={query}` | Search |
| `ilunyu://study` | Study classroom |
| `ilunyu://hunt` | Hunt (寻章); aliases `keyword-hunt` / `flyflower` |
| `ilunyu://mastered` / `ilunyu://progress` | Mastered / progress |
| `ilunyu://categories` / `ilunyu://categories?section=` | Browse |
| `ilunyu://collection?id=lunyu` | Book collection (aliases `book` / `form`; also `name=`) |
| `ilunyu://theme?id=` | Theme or volume (e.g. `junzi`, `xue-er`; aliases `suite` / `volume`) |
| `ilunyu://last-read` | Last read |
| `ilunyu://reading-history` | Reading history |
| `ilunyu://notes` | Notes |

## Settings & guides

| URL | Opens |
|-----|-------|
| `ilunyu://settings` | Settings |
| `ilunyu://usage-guide` | Usage guide |
| `ilunyu://widget-guide` | Widget guide |
| `ilunyu://shortcuts-guide` | Shortcuts guide |
| `ilunyu://feature-guide` | Replay onboarding |
| `ilunyu://feedback` | Feedback email |
| `ilunyu://in-app-review` | In-app / Store review entry |

## Examples

```
ilunyu://daily
ilunyu://passage?id=1
ilunyu://recite?id=20
ilunyu://theme?id=junzi
ilunyu://study
ilunyu://hunt
```

Use these in the Shortcuts app, Home Screen quick actions, widgets, or Safari. See also in-app **Settings → Shortcuts Guide**.

</section>

<section lang="zh-CN" markdown="1">

爱论语支持 **`ilunyu://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
ilunyu://{host}?{params}
```

## 章句与作者

| URL | 打开 |
|-----|------|
| `ilunyu://passage?id={id}` | 章句详情 |
| `ilunyu://couplet?id={id}` / `ilunyu://poem?id={id}` | 同上（兼容别名） |
| `ilunyu://author?id={id}` | 作者详情 |
| `ilunyu://recite` | 诵读 |
| `ilunyu://recite?id={id}` | 打开章句并自动诵读 |

## 发现与学习

| URL | 打开 |
|-----|------|
| `ilunyu://home` | 首页 |
| `ilunyu://daily` | 每日一则 |
| `ilunyu://random` | 随机 |
| `ilunyu://favorites` | 收藏 |
| `ilunyu://famous` | 名句 |
| `ilunyu://search` / `ilunyu://search?q={query}` | 搜索 |
| `ilunyu://study` | 习礼学堂 |
| `ilunyu://hunt` | 寻章（别名 `keyword-hunt` / `flyflower`） |
| `ilunyu://mastered` / `ilunyu://progress` | 已掌握 / 进度 |
| `ilunyu://categories` / `ilunyu://categories?section=` | 分类 |
| `ilunyu://collection?id=lunyu` | 书目合集 |
| `ilunyu://theme?id=` | 主题或篇目（如 `junzi`、`xue-er`） |
| `ilunyu://last-read` | 上次阅读 |
| `ilunyu://reading-history` | 浏览记录 |
| `ilunyu://notes` | 笔记 |

## 设置与教程

| URL | 打开 |
|-----|------|
| `ilunyu://settings` | 设置 |
| `ilunyu://usage-guide` | 使用说明 |
| `ilunyu://widget-guide` | 小组件指南 |
| `ilunyu://shortcuts-guide` | 快捷指南 |
| `ilunyu://feature-guide` | 重播功能引导 |
| `ilunyu://feedback` | 反馈邮件 |
| `ilunyu://in-app-review` | 评分入口 |

## 示例

```
ilunyu://daily
ilunyu://passage?id=1
ilunyu://recite?id=20
ilunyu://theme?id=junzi
ilunyu://study
ilunyu://hunt
```

可在「快捷指令」、主屏快捷、小组件或 Safari 中使用。详见应用内 **设置 → 快捷指南**。

</section>

<section lang="zh-TW" markdown="1">

愛論語支援 **`ilunyu://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複開啟。

## 連結格式

```
ilunyu://{host}?{params}
```

## 章句與作者

| URL | 開啟 |
|-----|------|
| `ilunyu://passage?id={id}` | 章句詳情 |
| `ilunyu://couplet?id={id}` / `ilunyu://poem?id={id}` | 同上（相容別名） |
| `ilunyu://author?id={id}` | 作者詳情 |
| `ilunyu://recite` | 誦讀 |
| `ilunyu://recite?id={id}` | 打開章句並自動誦讀 |

## 發現與學習

| URL | 開啟 |
|-----|------|
| `ilunyu://home` | 首頁 |
| `ilunyu://daily` | 每日一則 |
| `ilunyu://random` | 隨機 |
| `ilunyu://favorites` | 收藏 |
| `ilunyu://famous` | 名句 |
| `ilunyu://search` / `ilunyu://search?q={query}` | 搜尋 |
| `ilunyu://study` | 習禮學堂 |
| `ilunyu://hunt` | 尋章（別名 `keyword-hunt` / `flyflower`） |
| `ilunyu://mastered` / `ilunyu://progress` | 已掌握 / 進度 |
| `ilunyu://categories` / `ilunyu://categories?section=` | 分類 |
| `ilunyu://collection?id=lunyu` | 書目合集 |
| `ilunyu://theme?id=` | 主題或篇目（如 `junzi`、`xue-er`） |
| `ilunyu://last-read` | 上次閱讀 |
| `ilunyu://reading-history` | 瀏覽記錄 |
| `ilunyu://notes` | 筆記 |

## 設定與教學

| URL | 開啟 |
|-----|------|
| `ilunyu://settings` | 設定 |
| `ilunyu://usage-guide` | 使用說明 |
| `ilunyu://widget-guide` | 小工具指南 |
| `ilunyu://shortcuts-guide` | 捷徑指南 |
| `ilunyu://feature-guide` | 重播功能引導 |
| `ilunyu://feedback` | 回饋郵件 |
| `ilunyu://in-app-review` | 評分入口 |

## 範例

```
ilunyu://daily
ilunyu://passage?id=1
ilunyu://recite?id=20
ilunyu://theme?id=junzi
ilunyu://study
ilunyu://hunt
```

可在「捷徑」、主畫面捷徑、小工具或 Safari 中使用。詳見應用內 **設定 → 捷徑指南**。

</section>
