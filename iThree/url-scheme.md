---
layout: doc
title: iThree — Shortcut Links
app_id: iThree
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: ithree:// deep links for iThree — passage, daily, recite, study, hunt, stories, books, dynasties, settings guides, and more.
---

<section lang="en" markdown="1">

iThree supports **`ithree://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
ithree://{host}?{params}
```

## Passages & discovery

| URL | Opens |
|-----|-------|
| `ithree://home` | Home |
| `ithree://daily` | Today’s Daily Line |
| `ithree://random` | Random passage |
| `ithree://passage?id={id}` | Passage detail |
| `ithree://recite` / `ithree://recite?id={id}` | Recite flow |
| `ithree://favorites` | Favorites |
| `ithree://famous` | Famous lines |
| `ithree://search` / `ithree://search?q={query}` | Search |
| `ithree://study` | Study classroom |
| `ithree://quiz` | Today’s quiz |
| `ithree://hunt` | Hunt (寻句) |
| `ithree://mastered` | Mastered |
| `ithree://categories` | Browse |
| `ithree://chapter?id={id}` | Chapter |
| `ithree://stories` / `ithree://story?id={id}` | Stories / story detail |
| `ithree://books` / `ithree://book?id={id}` | Classic indexes / book |
| `ithree://dynasties` / `ithree://dynasty?id={id}` | Dynasties / dynasty |
| `ithree://collection?id=` / `?name=` | Collection (or books if empty) |
| `ithree://last-read` | Last read |
| `ithree://reading-history` | Reading history |
| `ithree://notes` | Notes |

> Note: `ithree://author?id=` is a compatibility alias and opens the matching **chapter**.

## Settings & guides

| URL | Opens |
|-----|-------|
| `ithree://settings` | Settings |
| `ithree://usage-guide` | Usage guide |
| `ithree://widget-guide` | Widget guide |
| `ithree://shortcuts-guide` | Shortcuts guide |
| `ithree://feature-guide` | Replay onboarding |
| `ithree://feedback` | Feedback email |
| `ithree://in-app-review` | In-app / Store review entry |
| `ithree://privacy` | In-app privacy |

## Examples

```
ithree://daily
ithree://passage?id=1
ithree://recite?id=1
ithree://study
ithree://hunt
ithree://quiz
ithree://stories
ithree://search?q=人之初
```

Use these in the Shortcuts app, Home Screen quick actions, widgets, Control Center, or Safari. See also in-app **Settings → Shortcuts Guide**.

</section>

<section lang="zh-CN" markdown="1">

爱三字经支持 **`ithree://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
ithree://{host}?{params}
```

## 段落与发现

| URL | 打开 |
|-----|------|
| `ithree://home` | 首页 |
| `ithree://daily` | 每日一句 |
| `ithree://random` | 随机 |
| `ithree://passage?id={id}` | 段落详情 |
| `ithree://recite` / `ithree://recite?id={id}` | 诵读 |
| `ithree://favorites` | 收藏 |
| `ithree://famous` | 名句 |
| `ithree://search` / `ithree://search?q={query}` | 搜索 |
| `ithree://study` | 蒙学学堂 |
| `ithree://quiz` | 今日测验 |
| `ithree://hunt` | 寻句 |
| `ithree://mastered` | 已掌握 |
| `ithree://categories` | 分类 |
| `ithree://chapter?id={id}` | 章节 |
| `ithree://stories` / `ithree://story?id={id}` | 典故 / 典故详情 |
| `ithree://books` / `ithree://book?id={id}` | 典籍 / 典籍详情 |
| `ithree://dynasties` / `ithree://dynasty?id={id}` | 朝代 / 朝代详情 |
| `ithree://collection?id=` / `?name=` | 合集（空参则进典籍） |
| `ithree://last-read` | 上次阅读 |
| `ithree://reading-history` | 浏览记录 |
| `ithree://notes` | 笔记 |

> 说明：`ithree://author?id=` 为兼容别名，会打开对应**章节**。

## 设置与教程

| URL | 打开 |
|-----|------|
| `ithree://settings` | 设置 |
| `ithree://usage-guide` | 使用说明 |
| `ithree://widget-guide` | 小组件指南 |
| `ithree://shortcuts-guide` | 快捷指南 |
| `ithree://feature-guide` | 重播引导 |
| `ithree://feedback` | 反馈邮件 |
| `ithree://in-app-review` | 应用内 / 商店评价入口 |
| `ithree://privacy` | 应用内隐私说明 |

## 示例

```
ithree://daily
ithree://passage?id=1
ithree://recite?id=1
ithree://study
ithree://hunt
ithree://quiz
ithree://stories
ithree://search?q=人之初
```

可在「快捷指令」、主屏快捷、小组件、控制中心或 Safari 中使用。也可查看应用内 **设置 → 快捷指南**。

</section>

<section lang="zh-TW" markdown="1">

愛三字經支援 **`ithree://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複開啟。

## 連結格式

```
ithree://{host}?{params}
```

## 段落與發現

| URL | 開啟 |
|-----|------|
| `ithree://home` | 首頁 |
| `ithree://daily` | 每日一句 |
| `ithree://random` | 隨機 |
| `ithree://passage?id={id}` | 段落詳情 |
| `ithree://recite` / `ithree://recite?id={id}` | 誦讀 |
| `ithree://favorites` | 收藏 |
| `ithree://famous` | 名句 |
| `ithree://search` / `ithree://search?q={query}` | 搜尋 |
| `ithree://study` | 蒙學學堂 |
| `ithree://quiz` | 今日測驗 |
| `ithree://hunt` | 尋句 |
| `ithree://mastered` | 已掌握 |
| `ithree://categories` | 分類 |
| `ithree://chapter?id={id}` | 章節 |
| `ithree://stories` / `ithree://story?id={id}` | 典故 / 典故詳情 |
| `ithree://books` / `ithree://book?id={id}` | 典籍 / 典籍詳情 |
| `ithree://dynasties` / `ithree://dynasty?id={id}` | 朝代 / 朝代詳情 |
| `ithree://collection?id=` / `?name=` | 合集（空參則進典籍） |
| `ithree://last-read` | 上次閱讀 |
| `ithree://reading-history` | 瀏覽記錄 |
| `ithree://notes` | 筆記 |

> 說明：`ithree://author?id=` 為相容別名，會開啟對應**章節**。

## 設定與教學

| URL | 開啟 |
|-----|------|
| `ithree://settings` | 設定 |
| `ithree://usage-guide` | 使用說明 |
| `ithree://widget-guide` | 小工具指南 |
| `ithree://shortcuts-guide` | 捷徑指南 |
| `ithree://feature-guide` | 重播引導 |
| `ithree://feedback` | 回饋郵件 |
| `ithree://in-app-review` | App 內 / 商店評價入口 |
| `ithree://privacy` | App 內隱私說明 |

## 範例

```
ithree://daily
ithree://passage?id=1
ithree://recite?id=1
ithree://study
ithree://hunt
ithree://quiz
ithree://stories
ithree://search?q=人之初
```

可在「捷徑」、主畫面捷徑、小工具、控制中心或 Safari 中使用。也可查看應用內 **設定 → 捷徑指南**。

</section>
