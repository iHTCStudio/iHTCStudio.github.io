---
layout: doc
title: iDeveloper — Shortcut Links
app_id: iDeveloper
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: ideveloper:// deep links for iDeveloper — tools, categories, search, references, focus, share, settings guides, and more.
---

<section lang="en" markdown="1">

iDeveloper supports **`ideveloper://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
ideveloper://{host}?{params}
```

## Tools & browse

| URL | Opens |
|-----|-------|
| `ideveloper://home` | Home |
| `ideveloper://tool?id={id}` | Tool detail (e.g. `json`, `base64`, `timestamp`) |
| `ideveloper://category?id={id}` | Category (e.g. `encoding`) |
| `ideveloper://search` / `ideveloper://search?q={query}` | Search |
| `ideveloper://favorites` | Favorites |
| `ideveloper://history` | Operation history |
| `ideveloper://reference` / `ideveloper://reference?id={id}` | Reference center / entry |
| `ideveloper://new-snippet` | New snippet |
| `ideveloper://focus` | Focus timer / Live Activity entry |
| `ideveloper://share?tool={id}` | Open Share handoff into a tool (works with the Share extension + App Group payload) |

## Settings & guides

| URL | Opens |
|-----|-------|
| `ideveloper://settings` | Settings |
| `ideveloper://usage-guide` | Usage guide |
| `ideveloper://widget-guide` | Widget guide |
| `ideveloper://shortcuts-guide` | Shortcuts guide |
| `ideveloper://feature-guide` | Replay onboarding |
| `ideveloper://feedback` | Feedback email |
| `ideveloper://in-app-review` | In-app / Store review entry |

## Examples

```
ideveloper://tool?id=json
ideveloper://search?q=base64
ideveloper://reference?id=http-200
ideveloper://favorites
ideveloper://focus
ideveloper://share?tool=json
ideveloper://category?id=encoding
```

Use these in the Shortcuts app, Home Screen quick actions, widgets, Control Center, or Safari. See also in-app **Settings → Shortcuts Guide**.

</section>

<section lang="zh-CN" markdown="1">

爱开发者支持 **`ideveloper://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
ideveloper://{host}?{params}
```

## 工具与浏览

| URL | 打开 |
|-----|------|
| `ideveloper://home` | 首页 |
| `ideveloper://tool?id={id}` | 工具详情（如 `json`、`base64`、`timestamp`） |
| `ideveloper://category?id={id}` | 分类（如 `encoding`） |
| `ideveloper://search` / `ideveloper://search?q={query}` | 搜索 |
| `ideveloper://favorites` | 收藏 |
| `ideveloper://history` | 操作历史 |
| `ideveloper://reference` / `ideveloper://reference?id={id}` | 速查中心 / 条目 |
| `ideveloper://new-snippet` | 新建代码片段 |
| `ideveloper://focus` | 专注计时 / 实时活动 |
| `ideveloper://share?tool={id}` | 分享投递到指定工具（配合分享扩展与 App Group） |

## 设置与教程

| URL | 打开 |
|-----|------|
| `ideveloper://settings` | 设置 |
| `ideveloper://usage-guide` | 使用说明 |
| `ideveloper://widget-guide` | 小组件指南 |
| `ideveloper://shortcuts-guide` | 快捷指南 |
| `ideveloper://feature-guide` | 重播功能引导 |
| `ideveloper://feedback` | 反馈邮件 |
| `ideveloper://in-app-review` | 评分入口 |

## 示例

```
ideveloper://tool?id=json
ideveloper://search?q=base64
ideveloper://reference?id=http-200
ideveloper://favorites
ideveloper://focus
ideveloper://share?tool=json
ideveloper://category?id=encoding
```

可在「快捷指令」、主屏快捷、小组件、控制中心或 Safari 中使用。详见应用内 **设置 → 快捷指南**。

</section>

<section lang="zh-TW" markdown="1">

愛開發者支援 **`ideveloper://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複開啟。

## 連結格式

```
ideveloper://{host}?{params}
```

## 工具與瀏覽

| URL | 開啟 |
|-----|------|
| `ideveloper://home` | 首頁 |
| `ideveloper://tool?id={id}` | 工具詳情（如 `json`、`base64`、`timestamp`） |
| `ideveloper://category?id={id}` | 分類（如 `encoding`） |
| `ideveloper://search` / `ideveloper://search?q={query}` | 搜尋 |
| `ideveloper://favorites` | 收藏 |
| `ideveloper://history` | 操作歷史 |
| `ideveloper://reference` / `ideveloper://reference?id={id}` | 速查中心 / 條目 |
| `ideveloper://new-snippet` | 新建程式碼片段 |
| `ideveloper://focus` | 專注計時 / 即時動態 |
| `ideveloper://share?tool={id}` | 分享投遞到指定工具（配合分享延伸功能與 App Group） |

## 設定與教學

| URL | 開啟 |
|-----|------|
| `ideveloper://settings` | 設定 |
| `ideveloper://usage-guide` | 使用說明 |
| `ideveloper://widget-guide` | 小工具指南 |
| `ideveloper://shortcuts-guide` | 捷徑指南 |
| `ideveloper://feature-guide` | 重播功能引導 |
| `ideveloper://feedback` | 回饋郵件 |
| `ideveloper://in-app-review` | 評分入口 |

## 範例

```
ideveloper://tool?id=json
ideveloper://search?q=base64
ideveloper://reference?id=http-200
ideveloper://favorites
ideveloper://focus
ideveloper://share?tool=json
ideveloper://category?id=encoding
```

可在「捷徑」、主畫面捷徑、小工具、控制中心或 Safari 中使用。詳見應用內 **設定 → 捷徑指南**。

</section>
