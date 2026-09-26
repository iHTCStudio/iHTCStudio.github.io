---
layout: doc
title: iBrowser — Shortcut Links
app_id: iBrowser
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接
doc_title_zh_tw: 快捷連結
description: ibrowser:// deep links for Shortcuts, Siri, widgets and Home Screen quick actions.
---

<section lang="en" markdown="1">

iBrowser supports **`ibrowser://`** deep links — open from Apple **Shortcuts**, **Siri**, Home Screen widgets, or the app icon long-press menu.

> **Child lock:** When **Force-hide address bar** is on, destinations other than **home** / **settings** / **guide** open the **home page** instead (bookmarks list only allows the home URL). Settings still asks for the password if enabled.

## Destinations

| URL | Opens |
|-----|--------|
| `ibrowser://home` | Home page from Settings |
| `ibrowser://search` | Focus the address bar |
| `ibrowser://search?q=keyword` | Search with the configured engine |
| `ibrowser://last` | Last successfully loaded page on this device (falls back to home) |
| `ibrowser://bookmarks` | Bookmark list |
| `ibrowser://settings` | Settings (password if enabled) |
| `ibrowser://guide` | Feature tour |
| `ibrowser://open?url=` | Open a specific `http`/`https` URL (percent-encoded) |

`http` / `https` links handed to the app by the system are **not** deep links — they load as external pages as-is.

## Siri & Shortcuts (iOS 16+)

Ask Siri or build a Shortcut to: open home, search, continue last page, bookmarks, Settings, feature tour, or open a URL.

## Home Screen quick actions

Long-press the app icon (up to **4** items). Defaults: home · continue last · search · bookmarks. Customize order / visibility in **Settings → Home Screen Quick Actions**; you can also add Settings or the feature tour. With child lock on, only **Open Home** remains.

[Support](../) · [FAQ](faq) · [Privacy Policy](privacy)

</section>

<section lang="zh-CN" markdown="1">

全屏浏览器支持 **`ibrowser://`** 深链 — 可用于苹果**快捷指令**、**Siri**、主屏小组件或长按图标。

> **儿童锁：** 开启**强制隐藏地址栏**时，除主页 / 设置 / 功能导览外，其他入口会改开**主页**（书签列表也只放行主页 URL）。设置若有密码仍会校验。

## 目标

| URL | 打开 |
|-----|------|
| `ibrowser://home` | 设置中的主页 |
| `ibrowser://search` | 唤出地址栏 |
| `ibrowser://search?q=关键词` | 用当前搜索引擎搜索 |
| `ibrowser://last` | 本机上次成功加载的页面（没有则回主页） |
| `ibrowser://bookmarks` | 书签列表 |
| `ibrowser://settings` | 设置（有密码先校验） |
| `ibrowser://guide` | 功能导览 |
| `ibrowser://open?url=` | 打开指定 `http`/`https` 网址（需编码） |

系统交给应用的 `http` / `https` **不是**深链，会按外来网页原样加载。

## Siri 与快捷指令（iOS 16+）

可打开主页、搜索、继续上次、书签、设置、功能导览，或打开指定网址。

## 主屏幕快捷操作

长按图标最多 **4** 项。默认：主页 · 继续上次 · 搜索 · 书签。在 **设置 → 主屏幕快捷操作** 中排序 / 隐藏，也可换成设置或功能导览。儿童锁开启时无论怎么配置只留「打开主页」。

[支持页](../) · [常见问题](faq) · [隐私政策](privacy)

</section>

<section lang="zh-TW" markdown="1">

全螢幕瀏覽器支援 **`ibrowser://`** 深鏈 — 可用於蘋果**捷徑**、**Siri**、主畫面小工具或長按圖示。

> **兒童鎖：** 開啟**強制隱藏網址列**時，除主頁 / 設定 / 功能導覽外，其他入口會改開**主頁**（書籤列表也只放行主頁 URL）。設定若有密碼仍會校驗。

## 目標

| URL | 打開 |
|-----|------|
| `ibrowser://home` | 設定中的主頁 |
| `ibrowser://search` | 喚出網址列 |
| `ibrowser://search?q=關鍵詞` | 用當前搜尋引擎搜尋 |
| `ibrowser://last` | 本機上次成功載入的頁面（沒有則回主頁） |
| `ibrowser://bookmarks` | 書籤列表 |
| `ibrowser://settings` | 設定（有密碼先校驗） |
| `ibrowser://guide` | 功能導覽 |
| `ibrowser://open?url=` | 打開指定 `http`/`https` 網址（需編碼） |

系統交給應用的 `http` / `https` **不是**深鏈，會按外來網頁原樣載入。

## Siri 與捷徑（iOS 16+）

可打開主頁、搜尋、繼續上次、書籤、設定、功能導覽，或打開指定網址。

## 主畫面快捷操作

長按圖示最多 **4** 項。預設：主頁 · 繼續上次 · 搜尋 · 書籤。在 **設定 → 主畫面快捷操作** 中排序 / 隱藏，也可換成設定或功能導覽。兒童鎖開啟時無論怎麼配置只留「打開主頁」。

[支援頁](../) · [常見問題](faq) · [隱私政策](privacy)

</section>
