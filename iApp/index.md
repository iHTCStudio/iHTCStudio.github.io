---
layout: app
title: iApp — Support
app_id: iApp
description: Third-party App Store browser with preview videos, region content compare, version history, developer replies, browse history, expanded iapp:// links, price-drop monitoring, developer favorites, rank tracking, Live Activity, widgets, and 18-language UI.
---

<section lang="en" markdown="1">

iApp (爱应用) is a **third-party App Store browser** for developers, product managers, and App enthusiasts. **No sign-in required** — browse **12 live chart types** across **175 regions**, search with platform filters, watch **App Preview videos**, compare **store content across regions**, read reviews and in-app purchase lists, track rankings with interactive charts, monitor version / listing / delisting / **price-drop** events, save **developer favorites**, revisit apps from **browse history**, share configurable QR cards, and stay on charts from **widgets**, **Live Activity**, and **shortcut links**. Full UI in **18 languages** plus System default; **Siri & Shortcuts** phrases follow your language choice.

> **Note:** This app is not affiliated with Apple Inc. and does not provide app download or installation. Store information comes from **public App Store data**. Please refer to the official App Store for purchases and downloads.

## Getting Started

1. Complete the **5-page feature guide** on first launch (re-open anytime in **Settings → Help → Feature Guide**).
2. On **Rankings**, pick a **region**, **chart type**, and **category** — use the searchable region picker or **quick region chips** (HK / TW / MO show clearer names in the picker; region codes stay the same).
3. When **Games** is selected, drill into **18 game subcategories** (Action, Puzzle, Strategy, and more).
4. Tap any app for details — switch **region** in the header, watch **App Preview videos**, read **user reviews** (tap to expand full text), browse the **in-app purchase list**, check **all-region store info** (including **content compare**), and view a zoomable **screenshot gallery**.
5. **Swipe left** in rankings or search to **favorite**; **long-press** any row for **Add Subscription** or **Developer** actions (homepage, same-developer apps, save developer).
6. Manage favorites in the optional **Favorites tab** or **Settings → Data → App Favorites** — pin, sort, group, view by ranking, batch-edit, or export.
7. Use **Subscriptions** to watch **version updates**, **listings**, **removals**, or **price drops**; pause any monitor without deleting it; adjust global or per-app check intervals (default **30 seconds**).
8. Save developers in **Settings → Data → Developer Favorites** or the optional **Developer Favorites tab** (optional separate **iCloud** sync).
9. Revisit recently viewed apps in **Settings → Data → App Browse History** (local only, up to 100 entries).
10. Enable **Rank Tracking** in **Settings → Advanced** to save rank history (including **drop-off records**), create tracking presets, and optionally show **Live Activity** (iOS 16.2+).
11. Add **Rankings** or **My Favorites** widgets (iOS 17+); pick from **9 alternate app icons**; long-press the app icon for quick actions, or ask **Siri**.

## Features

### Rankings

- **12 live chart types** — iPhone, iPad, and **Mac** Top Free / Paid / Grossing, plus New Apps charts
- **26 main categories** + **18 game subcategories** when Games is selected
- **175 countries and regions** — browse any store without changing your Apple ID; keyword search + configurable **quick region chips**
- **Persistent filters** and **list/grid layout** (2–4 columns on iPhone, 3–6 on iPad); equal-height grid rows
- **Platform badges** on Mac and iPad chart rows; free apps show gray prices in grid view
- **Inline error states** with retry when a chart fails to load
- **Rank history tracking** (optional) — saved on your device, up to 90 entries per chart view, including **off-chart drop-off** events
- **Tracking presets** — watch specific apps on a dedicated tracking page, view **interactive rank charts** (drag to scrub), enable **Live Activity** per preset
- **Share chart** — export a branded image snapshot (up to 30 apps) with region label, filter summary, and app icons (prefetched before export)
- **Long-press menu** — add subscription, open all-region info, same-developer apps, **Developer** submenu, and more
- **Faster by-ranking views** — batch chart prefetch for favorites, same-developer, and all-region ranking tables (best on Wi‑Fi)

### Search

- Keyword search with **iPhone / iPad / Mac platform filter** (remembered between visits)
- **Search history** — up to 50 recent queries; tap to search again; dismissing the search bar keeps results
- **Batch App ID search** — paste up to 50 comma-separated IDs; a **single numeric App ID** (6–12 digits, no comma) also works
- **Paste App Store links** — search and subscriptions can parse store URLs
- **Configurable list fields** — show size / rating / date and more on Rankings, Search, Favorites, and same-developer lists
- **Developer Rankings quick action** — pin a developer chart on the Home Screen icon menu; same-developer deep links by chart
- **Quick region chip bar** at the top (shared or separate for Rankings vs Search)
- Persistent list/grid layout; shows a retry option when loading fails
- With Rank Tracking on, returning to the foreground can quietly refresh and append on-device rank history

### App Details

- Switch **region** from the detail header without leaving the page; unavailable regions show helpful alternatives
- Version, rating, price, description, release notes, Bundle ID, compatibility, languages; **file size** shown in App Store decimal units (1000-based MB/GB)
- **App Preview videos** — play official App Store preview trailers (HLS); switch quality, mute/unmute, copy link, **save to Photos with audio** (photo library permission required)
- **In-app purchases** — collapsible list of featured IAPs for the current region (name, price, subscription badge); manual refresh on failure
- **User reviews** — preview carousel, full page with rating breakdown and filters (up to 500); **tap a review to expand or collapse** full text; **developer replies** shown inline; customer-reviews API by default, RSS fallback when empty or failed
- **Version history** — dedicated page listing past releases (version, date, release notes) from the App Store catalog
- **All-region store info** — check availability across 170+ regions; **All**, **By ranking**, or **Content compare** view
  - **Content compare** — diff description, release notes, screenshots, and preview videos vs a baseline region; tap a differing region for side-by-side view with orange highlights; extra filters (content / description / release notes / screenshot / video diff); **image export not available** in this mode; cellular confirmation before entry
- **Screenshot gallery** — pop-up on iPhone, full-screen on iPad; pinch zoom; save current/all; quality picker (standard / HD / original); prefers **official App Store HD screenshots** (iPhone → iPad → Mac order when multiple platforms exist)
- Tap the app icon for full-size view, save, or share
- **In-app App Store page** — preview the official product page inside iApp, or open in the App Store app
- **Rich context menu** — all regions, in-app store page, **Developer** submenu (homepage, same-developer apps, save/remove developer favorite), **add subscription**, copy submenu, display options
- **Same-developer apps** — horizontal **carousel preview** on the detail page (tap title for full list); **8 sort options** (store default, recently updated, release date, name, rating, price, and more); **by-ranking** table with export
- **Interactive rank history** chart when tracking is enabled — rank changes, drop-off and return labels
- Long-press or tap to **copy** with a brief on-screen confirmation; iOS 18 **translation** for foreign text
- **Browse history** — each detail visit is recorded locally (app + region, up to 100); manage in **Settings → Data → App Browse History**

### Subscription Monitoring

- **Four monitor types** (per region): **version update**, **new listing**, **removal**, and **price drop**
- **Price drop** — set baseline at add time; optional target price and/or drop percentage; paid → free always counts; same app + region can hold **multiple monitors** of different types
- **Add by keyword search** with platform filter; or **long-press any list row** → Add Subscription
- **Pause / resume** any active monitor without deleting — pausing stops polling and ends its Live Activity; resume triggers an immediate check
- **Global check interval** — default **30 seconds**, minimum 10 seconds, up to about 24 hours; **per-subscription interval** override
- **Force check** per item; swipe to delete; pull-to-refresh runs active monitors immediately
- Optional **Live Activity** (iOS 16.2+) per subscription — independent from rank Live Activity; shows version, listing, delisting, or price status; tap opens app detail
- Optional **iCloud sync** for the subscription list (separate from favorites)
- **Optional Subscription tab** — hide from the tab bar in **Settings → App Settings** (still accessible from Settings)

### Favorites

- Optional **Favorites tab** in the tab bar (**Settings → App Settings → Show Favorites in Tab Bar**; default off)
- Swipe left or favorite from detail; starred rows in rankings and search
- **Per-region** — the same app in China and the US are separate entries
- **Pin** important apps — pinned items appear first in list, grid, and the **My Favorites** widget
- **9 sort modes** for list/grid; **By ranking** table with unified sort (collection order, name, overall/category rank, rating, price)
- **Delisted apps** stay visible with a clear label until you remove them
- **Groups** — default Competitors / Own Apps; filter by group or developer
- **Batch management** — multi-select, pin/unpin, assign group, bulk unfavorite, edit notes
- **Export** — share text summary, **CSV file** (Excel-friendly), or branded image
- Optional **iCloud Sync** with timestamp-based merge; powers the **My Favorites** widget

### Developer Favorites

- Save developers by **artist + region** in **Settings → Data → Developer Favorites**
- Optional **Developer Favorites tab** between Favorites and Settings (**Settings → App Settings → Show Developer Favorites in Tab bar**; default off)
- List/grid layout, pin, filter all or by region, sort by collection order / name / region
- Add from detail **More** menu or long-press **Developer** submenu; open developer's apps or **by-ranking** chart view
- Optional **separate iCloud sync** toggle (default off; timestamp-based merge)

### Share Cards

- **4 templates** — Classic, Ancient, Clean, Story
- **Export quality** — Standard, High, Ultra (sharper vector render at all tiers)
- Choose which fields to show (developer, category, version, price, description, watermark, and more)
- Story template optimized for vertical social formats
- Rank / favorites / all-region share images include a **shared at** timestamp; long images use safer stitching

### Widgets & Live Activity

- **Rankings · iApp** (iOS 17+) — pick chart, category, and region per widget; theme and language follow app settings
- **My Favorites · iApp** — favorites list by region; **pinned apps first**
- **Sizes** — Small through Extra Large, Lock Screen Circular and Rectangular
- **Live Activity — Rankings** (iOS 16.2+) — Top 6 on Lock Screen + Dynamic Island; tied to rank-tracking presets; tap opens filtered Rankings
- **Live Activity — Subscriptions** (iOS 16.2+) — separate master toggle; per-subscription status including price; tap opens app detail
- Setup guides at **Settings → Widgets** and **Settings → Advanced → Live Activity**

### Shortcut Links, Quick Actions & Siri

- **`iapp://` links** — open an app detail page, jump to a filtered Rankings view, or deep-link into **8 secondary pages** (developer favorites, browse history, rank tracking, and more). See [Shortcut Links](url-scheme).
- **Home Screen Quick Actions** — pick up to **4** from **15** options (including developer favorites, browse history, rank tracking, Live Activity settings, and more)
- **Siri & Shortcuts** (iOS 16+) — search apps, open charts, or add a favorite; **fully localized** in all 18 app languages
- **Mac keyboard shortcuts** — **⌘1–⌘N** switch tabs dynamically based on which tabs are visible (Rankings, Search, Subscriptions, Favorites, Developer Favorites, Settings)

### Language & Help

- **Settings → Appearance → Language** — System default or any of **18 languages**: English, 简体中文, 繁體中文, 日本語, 한국어, Русский, Français, Deutsch, Español, Português, Italiano, العربية, हिन्दी, Bahasa Indonesia, Türkçe, Tiếng Việt, ไทย, Polski
- Widgets and **Siri** phrases follow the same language setting
- **Usage guide** — **Settings → Help → Usage Instructions** (expanded FAQ, including price-drop how-to)
- Rank tracking guide, widget guide, and 5-page onboarding

### Settings & Tools

- Light, Dark, and System appearance; **9 alternate app icons** with preview (**Settings → Appearance → App Icon**, iOS only)
- Optional widget theme sync
- **App Settings** (after **Data**, before third-party links) — mobile data usage alert (default on), Subscription / Favorites / **Developer Favorites** tab visibility
- **Data** — favorites, developer favorites, subscriptions, **App Browse History** (local, up to 100), iCloud toggles, cache management
- **App Store Region** — switch your device's App Store storefront via Apple's official link (**Settings → Third-party**); independent from in-app chart region filters
- **Apple Services** — curated links to 56 Apple developer and store resources (localized display for multiple languages)
- **iCloud sync** (optional, separate toggles) — app favorites, **developer favorites**, subscriptions, filter presets, search/quick regions
- Inline cache management — clear saved images, widget icons, and rank history storage
- **Cellular data confirmation** before high-traffic lookups (all-region comparison, by-ranking developer/favorites views); can disable in App Settings
- In-app rating, feedback email, share app, app update prompt

## Get the App

| Channel | Link |
|---------|------|
| App Store | [Download on the App Store](https://apps.apple.com/app/id6446581591) |

## System Requirements

| Component | Minimum Version |
|-----------|-----------------|
| iPhone / iPad (main app) | iOS 15.0+ |
| Alternate app icons | iOS 10.3+ |
| Home Screen widgets | iOS 17.0+ |
| Live Activity (rank + subscription) | iOS 16.2+ |
| Siri & Shortcuts | iOS 16.0+ |
| In-app translation | iOS 18.0+ |
| Mac | macOS 11.0+ |

## Contact Us

If you have questions, feedback, or need help:

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

We typically respond within 48 hours.

[FAQ](faq) · [Shortcut Links](url-scheme) · [Privacy Policy](privacy)

</section>

<section lang="zh-CN" markdown="1">

爱应用（iApp）是一款面向开发者、产品经理与 App 爱好者的 **第三方 App Store 浏览工具**。**无需注册登录**——即可查看 **12 种实时榜单**、**175 个地区**商店数据，按平台筛选搜索，观看 **App 预览视频**，**跨地区对比商店内容**，阅读用户评论与**应用内购买列表**，用交互式图表追踪排名变化，监控版本 / 上架 / 下架 / **降价**事件，收藏**开发者**，通过**浏览记录**快速回访，生成可配置分享卡片，并通过 **小组件**、**实时活动** 与 **快捷链接** 快速直达。界面支持 **18 种语言**；**Siri 与快捷指令**短语同步跟随所选语言。

> **注：** 本应用与 Apple Inc. 无关联，也不提供应用下载安装服务。商店信息来自 **App Store 公开数据**。购买与下载请以官方 App Store 为准。

## 快速上手

1. 首次启动完成 **5 页功能引导**（可在 **设置 → 帮助 → 功能引导** 再次查看）。
2. 在**榜单** Tab 选择**地区**、**榜单类型**与**分类**；地区选择器支持搜索（港 / 台 / 澳在列表中显示更清晰名称，地区代码不变）。
3. 选择**游戏**分类时，可进一步筛选 **18 个游戏子分类**。
4. 点按应用查看详情——页头**切换地区**，观看 **App 预览视频**，阅读**用户评论**（点按展开全文），浏览**应用内购买**、**全地区商店信息**（含**内容对比**）与**截图画廊**。
5. 榜单或搜索中**左滑收藏**；**长按任意行**可**加入订阅**或使用**开发者**子菜单（主页、同开发者 App、收藏开发者）。
6. 在可选的**收藏** Tab 或 **设置 → 数据 → App 收藏夹** 管理收藏。
7. 使用**订阅**监控**版本更新**、**上架**、**下架**或**降价**；可**暂停**监控而不删除。
8. 在 **设置 → 数据 → 开发者收藏** 或可选的**开发者收藏 Tab** 保存开发者（可选独立 **iCloud** 同步）。
9. 在 **设置 → 数据 → App 浏览记录** 查看最近访问的详情页（本机保存，最多 100 条）。
10. 在 **设置 → 高级** 开启**榜单历史追踪**并可选启用**实时活动**（iOS 16.2+）。
11. 添加小组件（需 iOS 17+）；选择 **9 款备用图标**；长按图标或使用 **Siri**。

## 功能特性

### 榜单浏览

- **12 种实时榜单** — iPhone / iPad / **Mac** 热门免费、付费、畅销及新上架榜
- **26 个主分类** + 游戏下 **18 个子分类**；**175 个地区**
- **筛选记忆**；列表 / 网格布局；网格行等高；免费应用价格为灰色
- **榜单历史追踪**（可选）— 含**掉榜**记录；**交互式排名曲线**；按预设启用**实时活动**
- **分享榜单**长图（含地区标签、筛选摘要与应用图标）；**按榜单**视图加载更快
- **长按菜单** — 加入订阅、全地区信息、**开发者**子菜单等

### 搜索

- 关键词搜索 + **平台筛选**；**搜索历史**（最多 50 条）
- **批量 App ID** 查询；**单个数字 App ID**（6–12 位、无逗号）同样有效
- **粘贴 App Store 链接** — 搜索与订阅支持解析商店 URL
- **列表多字段显示** — 榜单 / 搜索 / 收藏 / 同开发者可配置大小、评分、日期等
- **开发者排行快捷** — 主屏图标菜单可钉开发者榜；同开发者按榜单深链直达
- 开启榜单追踪后，回前台可静默刷新并写入本机排名历史

### 应用详情

- 页头**切换地区**；**容量**按 App Store 十进制 MB/GB 显示
- **App 预览视频** — 播放官方预览片（HLS）；切换清晰度、静音、复制链接、**含音轨保存到相册**
- **应用内购买列表** — 按当前地区折叠展示；失败可手动刷新
- **用户评论**（最多 500 条）— **点按展开 / 收起**全文；**开发者回复**内联显示；默认 customer-reviews API，空结果或失败时退回 RSS
- **版本历史** — 独立页面列出过往版本（版本号、日期、更新说明），来自 App Store catalog
- **全地区商店信息** — 全部 / **按榜单** / **内容对比**三种视图
  - **内容对比** — 对比简介、更新说明、截图与预览视频；双栏 diff 橙色高亮；支持内容 / 简介 / 更新 / 截图 / 视频差异筛选；此模式**不可导出图片**；蜂窝网络下进入前确认
- **截图画廊** — 优先 **App Store 官方 HD 截图**（多平台时按 iPhone → iPad → Mac 顺序）；**App 内产品页**；**交互式排名历史**
- **丰富长按菜单** — **开发者**子菜单、加入订阅等；详情页**同开发者 App 横滑预览**（点标题进入完整列表）；完整列表 **8 种排序**
- **浏览记录** — 访问详情自动记录（App + 地区，最多 100 条）；**设置 → 数据 → App 浏览记录** 管理

### 订阅监控

- **四种监控**：**版本更新**、**上架**、**下架**、**降价**（暂停 / 恢复；实时活动独立开关）

### 收藏夹

- 可选**收藏 Tab**；**置顶**；**9 种排序**；**按榜单**表格；CSV / 长图导出

### 开发者收藏

- **设置 → 数据 → 开发者收藏**；可选**开发者收藏 Tab**（**设置 → 应用设置**；默认关闭）
- 可选**独立 iCloud 同步**（默认关闭）

### 分享卡片

- **4 套模板**；标准 / 高清 / 超清（矢量渲染更清晰）；榜单 / 收藏 / 全地区分享图含**分享时间**

### 小组件与实时活动

- **榜单 · iApp** / **我的收藏 · iApp**（需 iOS 17+）
- **实时活动 — 榜单** / **实时活动 — 订阅**（iOS 16.2+）

### 快捷链接、主屏快捷指令与 Siri

- **`iapp://` 链接** — 可打开详情、带筛选榜单，或直达 **8 个二级页面**（开发者收藏、浏览记录、榜单追踪等）。详见 [快捷链接说明](url-scheme)
- **主屏快捷指令** — 从 **15 项**中最多选 **4 项**（含开发者收藏、浏览记录、榜单追踪、实时活动设置等）
- **Mac 键盘快捷键** — **⌘1–⌘N** 随可见 Tab 动态编号（含开发者收藏 Tab）

### 多语言与帮助

- **18 种语言** + 跟随系统；**使用说明**含扩展 FAQ

### 设置与工具

- **9 款备用应用图标**（仅 iOS）
- **应用设置**（位于**数据**之后）— 移动数据提醒、订阅 / 收藏 / **开发者收藏** Tab 开关
- **数据** — 收藏、开发者收藏、订阅、**App 浏览记录**、iCloud 各自独立
- **蜂窝网络**下高流量操作前确认；**App Store 地区**、**苹果常用网站**（支持多语言显示）

## 获取应用

| 渠道 | 链接 |
|------|------|
| App Store | [在 App Store 下载](https://apps.apple.com/app/id6446581591) |

## 系统要求

| 组件 | 最低版本 |
|------|----------|
| iPhone / iPad（主应用） | iOS 15.0+ |
| 备用应用图标 | iOS 10.3+ |
| 主屏小组件 | iOS 17.0+ |
| 实时活动（榜单 + 订阅） | iOS 16.2+ |
| Siri 与快捷指令 | iOS 16.0+ |
| 应用内翻译 | iOS 18.0+ |
| Mac | macOS 11.0+ |

## 联系我们

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

[常见问题](faq) · [快捷链接](url-scheme) · [隐私政策](privacy)

</section>

<section lang="zh-TW" markdown="1">

愛應用（iApp）是一款面向開發者、產品經理與 App 愛好者的 **第三方 App Store 瀏覽工具**。**無需註冊登入**——即可查看 **12 種即時榜單**、**175 個地區**商店資料，依平台篩選搜尋，觀看 **App 預覽影片**，**跨地區對比商店內容**，閱讀使用者評論與**應用內購買列表**，用互動式圖表追蹤排名變化，監控版本 / 上架 / 下架 / **降價**事件，收藏**開發者**，透過**瀏覽記錄**快速回訪，產生可設定分享卡片，並透過 **小工具**、**即時動態** 與 **快捷連結** 快速直達。介面支援 **18 種語言**；**Siri 與捷徑**短語同步跟隨所選語言。

> **註：** 本應用與 Apple Inc. 無關聯，也不提供應用下載安裝服務。商店資訊來自 **App Store 公開資料**。購買與下載請以官方 App Store 為準。

## 快速上手

1. 首次啟動完成 **5 頁功能引導**（可在 **設定 → 幫助 → 功能引導** 再次查看）。
2. 在**榜單** Tab 選擇**地區**、**榜單類型**與**分類**；地區選擇器支援搜尋（港 / 台 / 澳在列表中顯示更清晰名稱，地區代碼不變）。
3. 選擇**遊戲**分類時，可進一步篩選 **18 個遊戲子分類**。
4. 點按應用查看詳情——頁首**切換地區**，觀看 **App 預覽影片**，閱讀**使用者評論**（點按展開全文），瀏覽**應用內購買**、**全地區商店資訊**（含**內容對比**）與**截圖畫廊**。
5. 榜單或搜尋中**左滑收藏**；**長按任意列**可**加入訂閱**或使用**開發者**子選單。
6. 在可選的**收藏** Tab 或 **設定 → 資料 → App 收藏夾** 管理收藏。
7. 使用**訂閱**監控**版本更新**、**上架**、**下架**或**降價**；可**暫停**監控而不刪除。
8. 在 **設定 → 資料 → 開發者收藏** 或可選的**開發者收藏 Tab** 保存開發者（可選獨立 **iCloud** 同步）。
9. 在 **設定 → 資料 → App 瀏覽記錄** 查看最近造訪的詳情頁（本機保存，最多 100 條）。
10. 在 **設定 → 進階** 開啟**榜單歷史追蹤**並可選啟用**即時動態**（iOS 16.2+）。
11. 新增小工具（需 iOS 17+）；選擇 **9 款備用圖示**；長按圖示或使用 **Siri**。

## 功能特色

### 榜單瀏覽

- **12 種即時榜單**；**26 個主分類** + **18 個遊戲子分類**；**175 個地區**
- **榜單歷史追蹤**（含掉榜）；**互動式排名曲線**；**分享榜單**長圖（含篩選摘要）
- **長按選單** — 加入訂閱、全地區資訊、**開發者**子選單等

### 搜尋

- 關鍵字 + **平台篩選**；搜尋歷史；批次 App ID；**單個數字 App ID**（6–12 位）同樣有效
- **貼上 App Store 連結** — 搜尋與訂閱支援解析商店 URL
- **列表多欄位顯示** — 榜單 / 搜尋 / 收藏 / 同開發者可設定大小、評分、日期等
- **開發者排行快捷** — 主畫面圖示選單可釘開發者榜；同開發者按榜單深鏈直達
- 開啟榜單追蹤後，回前景可靜默刷新並寫入本機排名歷史

### 應用詳情

- **App 預覽影片** — 播放官方預覽片；切換清晰度、**含音軌保存到相簿**
- **使用者評論** — **點按展開 / 收起**全文；**開發者回覆**內聯顯示；預設 customer-reviews API，空結果或失敗時退回 RSS
- **版本歷史** — 獨立頁面列出過往版本（版本號、日期、更新說明）
- **全地區商店資訊** — 全部 / **依榜單** / **內容對比**；雙欄 diff 橙色高亮；此模式**不可匯出圖片**
- **開發者**子選單；詳情頁**同開發者 App 橫滑預覽**（點標題進入完整列表）；完整列表 **8 種排序**
- **瀏覽記錄** — **設定 → 資料 → App 瀏覽記錄**（本機，最多 100 條）

### 訂閱監控

- **四種監控**；**暫停 / 恢復**；**即時動態**獨立開關

### 開發者收藏

- 可選**開發者收藏 Tab**（**設定 → 應用設定**；預設關閉）；可選**獨立 iCloud 同步**

### 小工具與即時動態

- **榜單 · iApp** / **我的收藏 · iApp**（iOS 17+）
- **即時動態 — 榜單** / **即時動態 — 訂閱**（iOS 16.2+）

### 快捷連結、主畫面捷徑與 Siri

- **`iapp://` 連結** — 可開啟詳情、帶篩選榜單，或直達 **8 個二級頁面**（開發者收藏、瀏覽記錄、榜單追蹤等）。詳見 [快捷連結說明](url-scheme)
- **主畫面捷徑** — 從 **15 項**中最多選 **4 項**（含開發者收藏、瀏覽記錄、榜單追蹤、即時動態設定等）
- **Mac 鍵盤快捷鍵** — **⌘1–⌘N** 隨可見 Tab 動態編號

### 設定與工具

- **應用設定**（位於**資料**之後）— 行動數據提醒、訂閱 / 收藏 / **開發者收藏** Tab 開關
- **9 款備用應用圖示**（僅 iOS）；**iCloud 同步**各自獨立

## 取得應用

| 管道 | 連結 |
|------|------|
| App Store | [在 App Store 下載](https://apps.apple.com/app/id6446581591) |

## 系統需求

| 元件 | 最低版本 |
|------|----------|
| iPhone / iPad（主應用） | iOS 15.0+ |
| 備用應用圖示 | iOS 10.3+ |
| 主畫面小工具 | iOS 17.0+ |
| 即時動態（榜單 + 訂閱） | iOS 16.2+ |
| Siri 與捷徑 | iOS 16.0+ |
| Mac | macOS 11.0+ |

## 聯絡我們

- **電子郵件：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

[常見問題](faq) · [快捷連結](url-scheme) · [隱私政策](privacy)

</section>
