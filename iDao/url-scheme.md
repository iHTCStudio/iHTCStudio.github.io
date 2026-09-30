---
layout: doc
title: iDao — Shortcut Links
app_id: iDao
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: idao:// deep links for iDao — chapter, daily, recite, study, hunt, famous lines, books, settings guides, and more.
---

<section lang="en" markdown="1">

iDao supports **`idao://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
idao://{host}?{params}
```

## Chapters & discovery

| URL | Opens |
|-----|-------|
| `idao://home` | Home |
| `idao://daily` | Today’s Daily Chapter |
| `idao://random` | Random chapter |
| `idao://chapter?id={id}` | Chapter detail |
| `idao://recite` / `idao://recite?id={id}` | Recite flow |
| `idao://favorites` | Favorites |
| `idao://famous` | Famous lines |
| `idao://search` / `idao://search?q={query}` | Search |
| `idao://study` | Study Hall |
| `idao://hunt` | Seek the Tao (寻道) |
| `idao://mastered` | Mastered |
| `idao://categories` / `?section=` | Browse (optional section) |
| `idao://book?id=` | Book collection (`ddj` / `qingjing` / `yinfu`) |
| `idao://author` | Laozi intro |
| `idao://last-read` | Last read |
| `idao://reading-history` | Reading history |
| `idao://notes` | Notes |

> Compatibility aliases: `passage` / `poem` → chapter; `learn` → study; `seek` → hunt; `laozi` → author; `theme?id=` → categories section; `browse` → categories.

## Settings & guides

| URL | Opens |
|-----|-------|
| `idao://settings` | Settings |
| `idao://usage-guide` | Usage guide |
| `idao://widget-guide` | Widget guide |
| `idao://shortcuts-guide` | Shortcuts guide |
| `idao://feature-guide` | Replay onboarding |
| `idao://feedback` | Feedback email |
| `idao://in-app-review` | In-app / Store review entry |

## Examples

```
idao://daily
idao://chapter?id=1
idao://recite?id=1
idao://study
idao://hunt
idao://famous
idao://book?id=ddj
idao://author
idao://search?q=上善若水
```

Use these in the Shortcuts app, Home Screen quick actions, widgets, Control Center, or Safari. See also in-app **Settings → Shortcuts Guide**.

</section>

<section lang="zh-CN" markdown="1">

爱道德经支持 **`idao://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
idao://{host}?{params}
```

## 章节与发现

| URL | 打开 |
|-----|------|
| `idao://home` | 首页 |
| `idao://daily` | 每日一章 |
| `idao://random` | 随机 |
| `idao://chapter?id={id}` | 章节详情 |
| `idao://recite` / `idao://recite?id={id}` | 诵读 |
| `idao://favorites` | 收藏 |
| `idao://famous` | 名句 |
| `idao://search` / `idao://search?q={query}` | 搜索 |
| `idao://study` | 道学堂 |
| `idao://hunt` | 寻道 |
| `idao://mastered` | 已掌握 |
| `idao://categories` / `?section=` | 分类（可选分区） |
| `idao://book?id=` | 书目合集（`ddj` / `qingjing` / `yinfu`） |
| `idao://author` | 老子简介 |
| `idao://last-read` | 上次阅读 |
| `idao://reading-history` | 浏览记录 |
| `idao://notes` | 笔记 |

> 兼容别名：`passage` / `poem` → chapter；`learn` → study；`seek` → hunt；`laozi` → author；`theme?id=` → 分类分区；`browse` → categories。

## 设置与教程

| URL | 打开 |
|-----|------|
| `idao://settings` | 设置 |
| `idao://usage-guide` | 使用说明 |
| `idao://widget-guide` | 小组件指南 |
| `idao://shortcuts-guide` | 快捷指南 |
| `idao://feature-guide` | 重播引导 |
| `idao://feedback` | 反馈邮件 |
| `idao://in-app-review` | 应用内 / 商店评价入口 |

## 示例

```
idao://daily
idao://chapter?id=1
idao://recite?id=1
idao://study
idao://hunt
idao://famous
idao://book?id=ddj
idao://author
idao://search?q=上善若水
```

可在「快捷指令」、主屏快捷、小组件、控制中心或 Safari 中使用。也可查看应用内 **设置 → 快捷指南**。

</section>

<section lang="zh-TW" markdown="1">

愛道德經支援 **`idao://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複開啟。

## 連結格式

```
idao://{host}?{params}
```

## 章節與發現

| URL | 開啟 |
|-----|------|
| `idao://home` | 首頁 |
| `idao://daily` | 每日一章 |
| `idao://random` | 隨機 |
| `idao://chapter?id={id}` | 章節詳情 |
| `idao://recite` / `idao://recite?id={id}` | 誦讀 |
| `idao://favorites` | 收藏 |
| `idao://famous` | 名句 |
| `idao://search` / `idao://search?q={query}` | 搜尋 |
| `idao://study` | 道學堂 |
| `idao://hunt` | 尋道 |
| `idao://mastered` | 已掌握 |
| `idao://categories` / `?section=` | 分類（可選分區） |
| `idao://book?id=` | 書目合集（`ddj` / `qingjing` / `yinfu`） |
| `idao://author` | 老子簡介 |
| `idao://last-read` | 上次閱讀 |
| `idao://reading-history` | 瀏覽記錄 |
| `idao://notes` | 筆記 |

> 相容別名：`passage` / `poem` → chapter；`learn` → study；`seek` → hunt；`laozi` → author；`theme?id=` → 分類分區；`browse` → categories。

## 設定與教學

| URL | 開啟 |
|-----|------|
| `idao://settings` | 設定 |
| `idao://usage-guide` | 使用說明 |
| `idao://widget-guide` | 小工具指南 |
| `idao://shortcuts-guide` | 捷徑指南 |
| `idao://feature-guide` | 重播引導 |
| `idao://feedback` | 回饋郵件 |
| `idao://in-app-review` | App 內 / 商店評價入口 |

## 範例

```
idao://daily
idao://chapter?id=1
idao://recite?id=1
idao://study
idao://hunt
idao://famous
idao://book?id=ddj
idao://author
idao://search?q=上善若水
```

可在「捷徑」、主畫面捷徑、小工具、控制中心或 Safari 中使用。也可查看應用內 **設定 → 捷徑指南**。

</section>
