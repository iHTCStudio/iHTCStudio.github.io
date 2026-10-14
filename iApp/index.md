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
<section lang="ja" markdown="1">

iApp（爱应用）は、開発者、プロダクトマネージャー、アプリ愛好者向けの**サードパーティのAppストアブラウザ**です。**サインイン不要**で、**175地域**の**12種類のライブチャート**を閲覧したり、プラットフォームフィルターで検索したり、**アプリプレビュービデオ**を視聴したり、**地域ごとのストアコンテンツを比較**したり、レビューやアプリ内購入リストを確認したり、インタラクティブなチャートでランキングを追跡したり、バージョン／掲載／削除／**価格変更**イベントを監視したり、**開発者お気に入り**を保存したり、**閲覧履歴**からアプリを再訪したり、設定可能なQRカードを共有したり、**ウィジェット**や**ライブアクティビティ**、**ショートカットリンク**からチャートにアクセスしたりできます。UIは**18言語**以上に対応しており、システムのデフォルト言語も使用可能です。**Siri & Shortcuts**のフレーズは選んだ言語に従います。

> **注意:** 本アプリはApple Inc.とは提携しておらず、アプリのダウンロードやインストールは提供していません。ストア情報は**公開されているApp Storeデータ**から取得しています。購入やダウンロードについては公式App Storeをご参照ください。

## はじめに

1. 初回起動時に **5 ページの機能ガイド**を完了します (**[設定] → [ヘルプ] → [機能ガイド]**でいつでも再度開きます)。 
2. **ランキング**で、*地域**、*グラフの種類**、および**カテゴリ**を選択します。検索可能な地域ピッカーまたは**クイック地域チップ**を使用します（香港/台湾/MOではピッカーでより明確な名前が表示されます。地域コードは同じままです）。 
3. **ゲーム** を選択すると、**18 ゲームのサブカテゴリ** (アクション、パズル、ストラテジーなど) にドリルダウンします。 
4. いずれかのアプリをタップして詳細を確認します。ヘッダーで **地域** を切り替え、**アプリ プレビュー ビデオ**を視聴し、**ユーザー レビュー**を読み (タップして全文を展開します)、**アプリ内購入リスト**を参照し、**全地域のストア情報**を確認し (**コンテンツの比較**を含む)、ズーム可能な **スクリーンショット ギャラリー**を表示します。 
5. ランキングで **左にスワイプ**するか、**お気に入り**を検索します。 **サブスクリプションの追加** または **開発者** アクション (ホームページ、同じ開発者アプリ、開発者の保存) を行うには、任意の行を **長押しします。 
6. オプションの **[お気に入り] タブ** または **[設定] → [データ] → [アプリのお気に入り]** でお気に入りを管理します。固定、並べ替え、グループ化、ランキングによる表示、バッチ編集、またはエクスポートを行います。 
7. **サブスクリプション**を使用して、**バージョン更新**、**リスト**、**削除**、または**値下げ**を監視します。 モニターを削除せずに一時停止します。 グローバルまたはアプリごとのチェック間隔を調整します (デフォルト **30 秒**)。 
8. **[設定] → [データ] → [開発者のお気に入り]** またはオプションの [**開発者のお気に入り] タブ** (オプションで別の **iCloud** 同期) に開発者を保存します。 
9. **[設定] → [データ] → [アプリの閲覧履歴]** で、最近表示したアプリを再表示します (ローカルのみ、最大 100 エントリ)。 
10. [**設定] → [詳細設定]** で **ランク トラッキング**を有効にして、ランク履歴 (**ドロップオフ レコード**を含む) を保存し、トラッキング プリセットを作成し、必要に応じて **ライブ アクティビティ** を表示します (iOS 16.2 以降)。 
11. **ランキング** または **お気に入り** ウィジェットを追加します (iOS 17 以降)。 **9 つの代替アプリ アイコン** から選択します。 アプリアイコンを長押ししてクイックアクションを実行するか、**Siri** に尋ねます。

## 機能

### ランキング

- **12 種類のライブ チャート** — iPhone、iPad、および **Mac** 無料 / 有料 / 収益の上位、および新しいアプリのチャート
 - **26 のメイン カテゴリ** + **18 のゲーム サブカテゴリ** (ゲームが選択されている場合)
 - **175 の国と地域** — Apple ID を変更せずにどのストアでも閲覧できます。 キーワード検索 + 構成可能な **クイック領域チップ**
 - **永続フィルター** および **リスト/グリッド レイアウト** (iPhone では 2 ～ 4 列、iPad では 3 ～ 6 列)。 同じ高さのグリッド行
 - Mac および iPad のグラフ行の **プラットフォーム バッジ**; 無料アプリではグリッドビューに灰色の価格が表示される
 - **インライン エラー状態**、チャートの読み込みに失敗した場合の再試行
 - **ランク履歴追跡** (オプション) — デバイスに保存されます。**チャート外のドロップオフ** イベントを含む、チャート ビューごとに最大 90 エントリ
 - **トラッキング プリセット** - 専用のトラッキング ページで特定のアプリを監視し、**インタラクティブなランク チャート**を表示し (ドラッグしてスクラブします)、プリセットごとに **ライブ アクティビティ**を有効にします
 - **チャートの共有** — 地域ラベル、フィルターの概要、およびアプリのアイコン (エクスポート前にプリフェッチ) を含むブランド画像スナップショット (最大 30 個のアプリ) をエクスポートします。 
- **長押しメニュー** — サブスクリプションの追加、全地域情報、同じ開発者のアプリ、**開発者** サブメニューなどを開きます。 
- **ランキングによるビューの高速化** — お気に入り、同じ開発者、および全地域のランキング テーブルのバッチ チャート プリフェッチ (Wi‑Fi で最適)

### 検索

- **iPhone / iPad / Mac プラットフォームフィルター**付きキーワード検索（訪問間で記憶されます）
- **検索履歴** — 最近の検索クエリを最大50件まで保存; タップで再検索可能; 検索バーを閉じても結果は保持されます
- **一括App ID検索** — 最大50個のカンマ区切りIDを貼り付け可能; **単一の数値App ID**（6〜12桁、カンマなし）でも対応
- **App Storeリンクの貼り付け** — 検索とサブスクリプションでストアURLを解析可能
- **設定可能なリスト項目** — ランキング、検索、お気に入り、同一開発者リストでサイズ / 評価 / 日付などを表示
- **開発者ランキングのクイックアクション** — ホーム画面のアイコンメニューに開発者チャートを固定; チャートごとの同一開発者リンク
- 上部に**クイック地域チップバー**（ランキングと検索で共通または個別で使用可能）
- リスト/グリッドのレイアウトを保持; 読み込み失敗時に再試行オプションを表示
- ランク追跡使用時、フォアグラウンドに戻るとデバイス上のランク履歴を静かに更新・追加可能

### アプリ詳細

- ページを離れることなく、詳細ヘッダーから **地域** を切り替えます。 利用できない地域では役立つ代替手段が表示されます
 - バージョン、評価、価格、説明、リリースノート、バンドル ID、互換性、言語。 **ファイル サイズ**は App Store の小数単位で表示されます (1000 ベースの MB/GB)
 - **アプリ プレビュー ビデオ** — 公式 App Store プレビュー トレーラー (HLS) を再生します。 品質の切り替え、ミュート/ミュート解除、リンクのコピー、**音声付き写真に保存** (写真ライブラリの許可が必要)
 - **アプリ内購入** — 現在の地域の注目の IAP の折りたたみ可能なリスト (名前、価格、サブスクリプション バッジ)。 失敗時の手動更新
 - **ユーザー レビュー** — プレビュー カルーセル、評価の内訳とフィルター (最大 500) を含むページ全体。 **レビューをタップして展開または折りたたむ** 全文。 **開発者の返信**はインラインで表示されます。 デフォルトでは顧客レビュー API、空または失敗した場合は RSS フォールバック
 - **バージョン履歴** — App Store カタログの過去のリリース (バージョン、日付、リリース ノート) をリストした専用ページ
 - **全地域の店舗情報** — 170 以上の地域で在庫状況を確認します。 **すべて**、**ランキング順**、または **コンテンツ比較** ビュー
 - **コンテンツの比較** — ベースライン リージョンとの差分説明、リリース ノート、スクリーンショット、プレビュー ビデオ。 別の領域をタップすると、オレンジ色のハイライトで並べて表示されます。 追加フィルター (コンテンツ / 説明 / リリースノート / スクリーンショット / ビデオの差分); **このモードでは画像のエクスポートは利用できません**。 入国前の携帯電話確認
 - **スクリーンショット ギャラリー** — iPhone ではポップアップ、iPad では全画面。 ピンチズーム。 現在/すべてを保存; 品質ピッカー (標準/HD/オリジナル); **公式 App Store HD スクリーンショット** を好みます (複数のプラットフォームが存在する場合は iPhone → iPad → Mac の順)
 - アプリアイコンをタップすると、フルサイズで表示、保存、共有できます
 - **アプリ内 App Store ページ** — iApp 内で公式製品ページをプレビューするか、App Store アプリで開きます
 - **リッチ コンテキスト メニュー** — すべての地域、アプリ内ストア ページ、**開発者** サブメニュー (ホームページ、同じ開発者のアプリ、開発者のお気に入りの保存/削除)、**サブスクリプションの追加**、コピー サブメニュー、表示オプション
 - **同じ開発者のアプリ** — 詳細ページの水平 **カルーセル プレビュー** (タイトルをタップすると完全なリストが表示されます)。 **8 つの並べ替えオプション** (ストアのデフォルト、最近更新、リリース日、名前、評価、価格など)。 **ランキング別** エクスポート付きテーブル
 - トラッキングが有効な場合の **インタラクティブなランク履歴** グラフ — ランクの変更、ドロップオフ、およびリターンラベル
 - 長押しまたはタップすると、**コピー**され、画面上に簡単な確認が表示されます。 iOS 18 外国語テキストの **翻訳**
 - **閲覧履歴** — 各訪問の詳細がローカルに記録されます (アプリ + 地域、最大 100)。 **[設定] → [データ] → [アプリの閲覧履歴]** で管理します

### サブスクリプションの監視

 - **4 つのモニター タイプ** (地域ごと): **バージョン更新**、**新規リスト**、**削除**、**値下げ**
 - **値下げ** — 追加時にベースラインを設定します。 オプションの目標価格および/または下落率。 有料→無料は常にカウントされます。 同じアプリ + リージョンは、異なるタイプの **複数のモニター**を保持できます
 - **プラットフォーム フィルターを使用した **キーワード検索による追加**; または **リストの行を長押し** → サブスクリプションを追加
 - **削除せずにアクティブなモニターを **一時停止/再開** - 一時停止するとポーリングが停止し、ライブ アクティビティが終了します。 再開すると即時チェックがトリガーされます
 - **グローバル チェック間隔** - デフォルト **30 秒**、最小 10 秒、最大約 24 時間。 **サブスクリプションごとの間隔** オーバーライド
 - 項目ごとに **強制チェック**; スワイプして削除します。 pull-to-refresh はアクティブなモニターを即座に実行します
 - サブスクリプションごとのオプションの **ライブ アクティビティ** (iOS 16.2 以降) — ランクのライブ アクティビティとは独立しています。 バージョン、リスト、リスト廃止、または価格ステータスを表示します。 タップするとアプリの詳細が開きます
 - サブスクリプション リストのオプション **iCloud 同期** (お気に入りとは別に)
 - **オプションのサブスクリプション タブ** — **[設定] → [アプリ設定]** のタブ バーから非表示にします (引き続き [設定] からアクセスできます)

 ### お気に入り

- タブバーにオプションで **お気に入りタブ**（**設定 → アプリ設定 → タブバーにお気に入りを表示**；デフォルトはオフ）  
- 詳細画面で左にスワイプまたはお気に入り登録；ランキングや検索でスター付き行を表示  
- **地域別** — 中国と米国の同じアプリは別エントリ  
- 重要なアプリを **ピン留め** — ピン留めしたアイテムはリスト、グリッド、**マイお気に入り**ウィジェットで先頭に表示  
- リスト／グリッド用 **9種類の並べ替えモード**；統一された並べ替えの **ランキング順** テーブル（コレクション順、名前、総合／カテゴリランキング、評価、価格）  
- **配信終了アプリ** は削除するまで明確なラベル付きで表示  
- **グループ** — デフォルトは「競合／自社アプリ」；グループや開発者でフィルタ  
- **一括管理** — 複数選択、ピン留め／解除、グループ割り当て、一括お気に入り解除、メモ編集  
- **エクスポート** — テキストサマリー、**CSVファイル**（Excel対応）、またはブランド付き画像を共有  
- オプションの **iCloud同期**（タイムスタンプベースの統合）；**マイお気に入り**ウィジェットで使用可能  

### 開発者のお気に入り

- **設定 → データ → デベロッパーのお気に入り**で**アーティスト＋地域**ごとにデベロッパーを保存  
- お気に入りと設定の間に任意で**デベロッパーのお気に入りタブ**を表示可能（**設定 → アプリ設定 → タブバーにデベロッパーのお気に入りを表示**; デフォルトはオフ）  
- リスト／グリッドレイアウト、ピン留め、全てまたは地域別でフィルタ、コレクション順／名前／地域でソート  
- 詳細の**その他**メニューまたは長押し**デベロッパー**サブメニューから追加可能；デベロッパーのアプリを開くか、**ランキング順**チャート表示  
- 任意で**iCloud別同期**トグル（デフォルトオフ；タイムスタンプベースのマージ）

### 共有カード

- **4つのテンプレート** — クラシック、エンシェント、クリーン、ストーリー  
- **エクスポート品質** — 標準、高、高精細（すべての段階でよりシャープなベクターレンダリング）  
- 表示する項目を選択可能（デベロッパー、カテゴリ、バージョン、価格、説明、ウォーターマークなど）  
- ストーリーテンプレートは縦型のSNSフォーマット向けに最適化  
- ランク／お気に入り／全地域の共有画像には**共有日時**を含む；縦長画像は安全なスティッチング使用

### ウィジェット & ライブアクティビティ

- **ランキング · iApp** (iOS 17+) — ウィジェットごとにチャート、カテゴリー、地域を選択可能; テーマと言語はアプリ設定に従う
- **マイお気に入り · iApp** — 地域ごとのお気に入りリスト; **固定アプリを最初に表示**
- **サイズ** — スモールからエクストララージまで、ロック画面の円形および長方形
- **ライブアクティビティ — ランキング** (iOS 16.2+) — ロック画面+ダイナミックアイランドでトップ6表示; ランク追跡のプリセットに連動; タップでフィルタリングされたランキングを開く
- **ライブアクティビティ — サブスクリプション** (iOS 16.2+) — 個別のマスタートグル; サブスクリプションごとのステータス（価格含む）; タップでアプリ詳細を開く
- 設定ガイドは **設定 → ウィジェット** および **設定 → 詳細 → ライブアクティビティ** にあり

### ショートカットリンク、クイックアクション & Siri

- **`iapp://` リンク** - アプリの詳細ページを開いたり、フィルターされたランキング ビューにジャンプしたり、**8 つの二次ページ** (開発者のお気に入り、閲覧履歴、ランク追跡など) にディープリンクしたりできます。 [ショートカット リンク](url-scheme) を参照してください。 
- **ホーム画面のクイック アクション** — **15** オプションから最大 **4** を選択します (開発者のお気に入り、閲覧履歴、ランク追跡、ライブ アクティビティ設定などを含む)
 - **Siri とショートカット** (iOS 16 以降) - アプリを検索したり、グラフを開いたり、お気に入りを追加したりできます。 **完全にローカライズ** 18 のアプリ言語すべてに対応
 - **Mac キーボード ショートカット** — **⌘1–⌘N** 表示されているタブ (ランキング、検索、サブスクリプション、お気に入り、開発者のお気に入り、設定) に基づいてタブを動的に切り替えます

 ### 言語とヘルプ

 - **設定 → 外観 → 言語** — システムのデフォルトまたは **18 言語**のいずれか: 英語、简体中文、繁體中文、日本語、한국어、Русский、Français、Deutsch、Español、Português、Italiano、العربية、 हिन्दी、インドネシア語、Türkçe、Tiếng Việt、ไทย、Polski
 - ウィジェットと **Siri** フレーズは同じ言語設定に従います
 - **使用ガイド** — **設定 → ヘルプ → 使用説明** (値下げ方法を含む拡張 FAQ)
 - ランク追跡ガイド、ウィジェット ガイド、および 5 ページのオンボーディング

### 設定 & ツール

- ライト、ダーク、システムの外観; **プレビュー付きの 9 つの代替アプリ アイコン** (**[設定] → [外観] → [アプリ アイコン]**、iOS のみ)
 - オプションのウィジェットテーマの同期
 - **アプリ設定** (**データ**の後、サードパーティリンクの前) - モバイルデータ使用量アラート (デフォルトでオン)、サブスクリプション / お気に入り / **開発者のお気に入り** タブの表示設定
 - **データ** — お気に入り、開発者のお気に入り、サブスクリプション、**アプリの閲覧履歴** (ローカル、最大 100)、iCloud 切り替え、キャッシュ管理
 - **App Store 地域** — Apple の公式リンク (**[設定] → [サードパーティ]**) 経由でデバイスの App Store ストアフロントを切り替えます。 アプリ内のチャート領域フィルターから独立
 - **Apple サービス** — 56 の Apple 開発者およびストアのリソースへの厳選されたリンク (複数言語のローカライズされた表示)
 - **iCloud 同期** (オプション、個別の切り替え) — アプリのお気に入り、**開発者のお気に入り**、サブスクリプション、フィルター プリセット、検索/クイック リージョン
 - インラインキャッシュ管理 — 保存された画像、ウィジェットアイコン、ランク履歴ストレージをクリアします
 - 高トラフィック検索前の **セルラー データ確認** (全地域比較、開発者/お気に入りビューのランキングによる); アプリ設定で無効にできます
 - アプリ内評価、フィードバックメール、アプリの共有、アプリの更新プロンプト

## アプリを入手する

| チャンネル | リンク |
|------------|------|
| App Store | [App Storeでダウンロード](https://apps.apple.com/app/id6446581591) |

## システム要件

| コンポーネント | 最低バージョン |
|----------------|----------------|
| iPhone / iPad（メインアプリ） | iOS 15.0以上 |
| 代替アプリアイコン | iOS 10.3以上 |
| ホーム画面ウィジェット | iOS 17.0以上 |
| ライブアクティビティ（ランキング＋サブスクリプション） | iOS 16.2以上 |
| Siri & ショートカット | iOS 16.0以上 |
| アプリ内翻訳 | iOS 18.0以上 |
| Mac | macOS 11.0以上 |

## お問い合わせ

質問、フィードバック、サポートが必要な場合：

- **メール:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

通常、48時間以内に返信いたします。

[FAQ](faq) · [ショートカットリンク](url-scheme) · [プライバシーポリシー](privacy)

</section>
<section lang="ko" markdown="1">

iApp (爱应用)은 개발자, 제품 관리자, 앱 애호가를 위한 **서드파티 앱 스토어 브라우저**입니다. **로그인 불필요** — **175개 지역**에서 **12가지 실시간 차트 유형**을 탐색하고, 플랫폼 필터로 검색하며, **앱 미리보기 영상**을 보고, **지역별 스토어 콘텐츠를 비교**하고, 리뷰와 앱 내 구매 목록을 읽고, 상호 작용형 차트로 순위를 추적하며, 버전 / 등록 / 삭제 / **가격 인하** 이벤트를 모니터링하고, **개발자 즐겨찾기**를 저장하고, **탐색 기록**의 앱을 다시 방문하며, 구성 가능한 QR 카드를 공유하고, **위젯**, **실시간 활동(Live Activity)**, **바로가기 링크**에서 차트에 머물 수 있습니다. 전체 UI는 **18개 언어** 및 시스템 기본 언어로 제공되며; **Siri & 단축어** 문구는 선택한 언어를 따릅니다.

> **참고:** 이 앱은 Apple Inc.와 관련이 없으며 앱 다운로드나 설치를 제공하지 않습니다. 스토어 정보는 **공개 앱 스토어 데이터**에서 가져옵니다. 구매 및 다운로드는 공식 앱 스토어를 참조하시기 바랍니다.

## 시작하기

1. 처음 실행 시 **5페이지 분량의 기능 가이드**를 완료합니다(**설정 → 도움말 → 기능 가이드**에서 언제든지 다시 열 수 있음). 
2. **순위**에서 **지역**, **차트 유형** 및 **카테고리**를 선택합니다. 검색 가능한 지역 선택기 또는 **빠른 지역 칩**을 사용합니다(HK/TW/MO는 선택기에서 더 명확한 이름을 표시하고 지역 코드는 동일하게 유지됨). 
3. **게임**을 선택한 경우 **18개의 게임 하위 카테고리**(액션, 퍼즐, 전략 등)를 살펴보세요. 
4. 세부 정보를 보려면 아무 앱이나 탭하세요. 헤더에서 **지역**을 전환하고, **앱 미리보기 동영상**을 시청하고, **사용자 리뷰**를 읽고(전체 텍스트를 확장하려면 탭하세요), **인앱 구매 목록**을 찾아보고, **모든 지역 스토어 정보**(**콘텐츠 비교** 포함)를 확인하고, 확대/축소 가능한 **스크린샷 갤러리**를 확인하세요. 
5. 순위에서 **왼쪽으로 스와이프**하거나 **즐겨찾기**를 검색하세요. **구독 추가** 또는 **개발자** 작업(홈페이지, 동일한 개발자 앱, 개발자 저장)에 대한 행을 **길게 누르세요**. 
6. 선택 사항인 **즐겨찾기 탭** 또는 **설정 → 데이터 → 앱 즐겨찾기**에서 즐겨찾기를 관리하세요. 고정, 정렬, 그룹화, 순위별로 보기, 일괄 편집 또는 내보내기가 가능합니다. 
7. **구독**을 사용하여 **버전 업데이트**, **목록**, **제거** 또는 **가격 인하**를 시청하세요. 모니터를 삭제하지 않고 일시 중지합니다. 전역 또는 앱별 확인 간격을 조정합니다(기본값 **30초**). 
8. 개발자를 **설정 → 데이터 → 개발자 즐겨찾기** 또는 선택적 **개발자 즐겨찾기 탭**(별도의 **iCloud** 동기화 옵션)에 저장하세요. 
9. **설정 → 데이터 → 앱 검색 기록**에서 최근 본 앱을 다시 방문하세요(로컬 전용, 최대 100개 항목). 
10. **설정 → 고급**에서 **순위 추적**을 활성화하여 순위 기록(**탈퇴 기록** 포함)을 저장하고 추적 사전 설정을 생성하며 선택적으로 **실시간 활동**을 표시합니다(iOS 16.2+). 
11. **순위** 또는 **즐겨찾기** 위젯을 추가하세요(iOS 17+). **9개의 대체 앱 아이콘** 중에서 선택하세요. 빠른 작업을 수행하려면 앱 아이콘을 길게 누르거나 **Siri**에게 물어보세요.

## 기능

### 랭킹

- **12가지 라이브 차트 유형** — iPhone, iPad, **Mac** 인기 무료/유료/총수익 및 신규 앱 차트 
- **26개 주요 카테고리** + **18개 게임 하위 카테고리**(게임 선택 시) 
- **175개 국가 및 지역** — Apple ID를 변경하지 않고도 모든 매장을 탐색할 수 있습니다. 키워드 검색 + 구성 가능 **빠른 지역 칩** 
- **영구 필터** 및 **목록/그리드 레이아웃**(iPhone에서는 2~4열, iPad에서는 3~6열) 동일한 높이의 그리드 행 
- Mac 및 iPad 차트 행의 **플랫폼 배지**; 무료 앱은 그리드 보기에 회색 가격을 표시합니다. 
- 차트 로드 실패 시 재시도와 관련된 **인라인 오류 상태** 
- **순위 내역 추적**(선택 사항) — **차트에서 벗어난 드롭오프** 이벤트를 포함하여 차트 보기당 최대 90개의 항목이 장치에 저장됩니다. 
- **추적 사전 설정** — 전용 추적 페이지에서 특정 앱 보기, **대화형 순위 차트** 보기(드래그하여 스크러빙), 사전 설정별로 **실시간 활동** 활성화 
- **차트 공유** — 지역 라벨, 필터 요약 및 앱 아이콘(내보내기 전에 미리 가져옴)이 포함된 브랜드 이미지 스냅샷(최대 30개 앱) 내보내기 
- **길게 누르기 메뉴** — 구독 추가, 모든 지역 정보 열기, 동일한 개발자 앱, **개발자** 하위 메뉴 등 
- **더 빠른 순위별 보기** — 즐겨찾기, 동일 개발자 및 전체 지역 순위표에 대한 일괄 차트 미리 가져오기(Wi-Fi에서 최고)

### 검색

- **iPhone / iPad / Mac 플랫폼 필터**를 사용한 키워드 검색 (방문 간 기억됨)
- **검색 기록** — 최근 50개의 쿼리 저장; 탭하여 다시 검색 가능; 검색바를 닫아도 결과 유지
- **일괄 App ID 검색** — 최대 50개의 쉼표로 구분된 ID 붙여넣기; **단일 숫자 App ID**(6~12자리, 쉼표 없음)도 가능
- **App Store 링크 붙여넣기** — 검색 및 구독에서 스토어 URL 파싱 가능
- **구성 가능한 목록 필드** — 순위, 검색, 즐겨찾기 및 동일 개발자 목록에서 용량 / 평점 / 날짜 등 표시 가능
- **개발자 순위 빠른 액션** — 홈 화면 아이콘 메뉴에 개발자 차트 고정; 차트별 동일 개발자 딥 링크
- 상단의 **빠른 지역 칩 바** (순위와 검색에 대해 공유 또는 별도 가능)
- 지속적인 목록/그리드 레이아웃; 로딩 실패 시 재시도 옵션 표시
- 랭크 추적 활성화 시, 앱 전경 복귀 시 조용히 새로고침하고 기기 내 순위 기록 추가

### 앱 상세 정보

- 페이지를 떠나지 않고 세부 헤더에서 **지역**을 전환합니다. 사용할 수 없는 지역에는 유용한 대안이 표시됩니다. 
- 버전, 등급, 가격, 설명, 릴리스 노트, 번들 ID, 호환성, 언어 **파일 크기** App Store 소수점 단위로 표시됨(1000 기준 MB/GB) 
- **앱 미리보기 동영상** — 공식 App Store 미리보기 예고편(HLS)을 재생합니다. 품질 전환, 음소거/음소거 해제, 링크 복사, **오디오가 포함된 사진에 저장**(사진 라이브러리 권한 필요) 
- **인앱 구매** — 현재 지역의 추천 IAP 목록(이름, 가격, 구독 배지) 실패 시 수동 새로 고침 
- **사용자 리뷰** — 미리보기 캐러셀, 평점 분석 및 필터(최대 500개)가 포함된 전체 페이지 **리뷰를 탭하여 펼치거나 접으세요** 전체 텍스트; **개발자 답변**이 인라인으로 표시됩니다. 기본적으로 고객 리뷰 API, 비어 있거나 실패한 경우 RSS 대체 
- **버전 기록** — App Store 카탈로그의 이전 릴리스(버전, 날짜, 릴리스 노트)를 나열하는 전용 페이지 
- **전지역 매장 정보** — 170개 이상의 지역에서 구매 가능 여부를 확인하세요. **전체**, **순위별** 또는 **콘텐츠 비교** 보기 
- **콘텐츠 비교** — 차이점 설명, 출시 노트, 스크린샷, 미리보기 비디오와 기준 지역 비교 주황색 하이라이트로 나란히 보려면 ​​다른 영역을 탭하세요. 추가 필터(콘텐츠/설명/릴리스 노트/스크린샷/비디오 차이점); 이 모드에서는 **이미지 내보내기를 사용할 수 없습니다**; 입장 전 휴대폰 인증 
- **스크린샷 갤러리** — iPhone에서는 팝업, iPad에서는 전체 화면으로 표시됩니다. 핀치 줌; 현재/모두 저장; 품질 선택기(표준/HD/원본); **공식 App Store HD 스크린샷**을 선호합니다(여러 플랫폼이 존재할 경우 iPhone → iPad → Mac 순서) 
- 전체 화면으로 보기, 저장 또는 공유하려면 앱 아이콘을 탭하세요. 
- **인앱 App Store 페이지** — iApp 내에서 공식 제품 페이지를 미리 보거나 App Store 앱에서 엽니다. 
- **풍부한 상황에 맞는 메뉴** — 모든 지역, 인앱 스토어 페이지, **개발자** 하위 메뉴(홈페이지, 동일한 개발자 앱, 개발자 즐겨찾기 저장/제거), **구독 추가**, 하위 메뉴 복사, 표시 옵션 
- **동일 개발자 앱** — 세부정보 페이지의 수평 **캐러셀 미리보기**(전체 목록을 보려면 제목을 탭하세요) **8가지 정렬 옵션**(스토어 기본, 최근 업데이트, 출시 날짜, 이름, 평점, 가격 등) 내보내기가 포함된 **순위별** 테이블 
- 추적이 활성화된 경우 **상호작용 순위 내역** 차트 — 순위 변경, 하락 및 반품 라벨 
- 화면에서 간략한 확인과 함께 **복사**하려면 길게 누르거나 탭하세요. iOS 18 **외국어 텍스트 **번역** 
- **탐색 기록** — 각 세부 방문이 로컬로 기록됩니다(앱 + 지역, 최대 100개). **설정 → 데이터 → 앱 검색 기록**에서 관리하세요

### 구독 모니터링 

- **4가지 모니터 유형**(지역별): **버전 업데이트**, **새 목록**, **제거**, **가격 인하** 
- **가격 인하** — 추가 시 기준선을 설정합니다. 선택적 목표 가격 및/또는 하락율; 유료 → 무료는 항상 중요합니다. 동일한 앱 + 지역은 다양한 유형의 **여러 모니터**를 보유할 수 있습니다. 
- 플랫폼 필터를 사용하여 **키워드 검색으로 추가**; 또는 **목록 행을 길게 누르기** → 구독 추가 
- 삭제하지 않고 모든 활성 모니터를 **일시 중지/재개** - 일시 중지하면 폴링이 중지되고 라이브 활동이 종료됩니다. 이력서는 즉시 확인을 트리거합니다. 
- **전역 확인 간격** — 기본값 **30초**, 최소 10초, 최대 약 24시간 **구독별 간격** 재정의 
- 항목별 **강제 확인**; 삭제하려면 스와이프하세요. 당겨서 새로 고침하면 활성 모니터가 즉시 실행됩니다. 
- 구독당 선택 사항인 **라이브 활동**(iOS 16.2+) - 순위 라이브 활동과 별개입니다. 버전, 목록, 목록 삭제 또는 가격 상태를 표시합니다. 탭하면 앱 세부정보가 열립니다. 
- 구독 목록에 대한 선택적인 **iCloud 동기화**(즐겨찾기와는 별개) 
- **선택적 구독 탭** — **설정 → 앱 설정**의 탭 표시줄에서 숨깁니다(여전히 설정에서 액세스 가능). 

### 즐겨찾기

- 탭 바에서 선택 가능한 **즐겨찾기 탭** (**설정 → 앱 설정 → 탭 바에 즐겨찾기 표시**; 기본값 꺼짐)  
- 세부 정보에서 왼쪽으로 스와이프하거나 즐겨찾기; 순위 및 검색에서 별표 표시된 항목  
- **지역별** — 중국과 미국의 동일한 앱은 별도 항목으로 표시  
- **중요 앱 고정** — 고정한 항목은 리스트, 그리드, **내 즐겨찾기** 위젯에서 맨 앞에 표시  
- 리스트/그리드의 **9가지 정렬 모드**; 통합 정렬이 가능한 **순위별** 테이블 (컬렉션 순서, 이름, 전체/카테고리 순위, 평가, 가격)  
- **삭제된 앱**은 제거할 때까지 명확한 라벨과 함께 계속 표시  
- **그룹** — 기본 경쟁사 / 본인 앱; 그룹 또는 개발자별로 필터링 가능  
- **일괄 관리** — 다중 선택, 고정/고정 해제, 그룹 지정, 즐겨찾기 일괄 해제, 메모 편집  
- **내보내기** — 텍스트 요약 공유, **CSV 파일** (Excel 친화적), 또는 브랜딩 이미지  
- 선택적 **iCloud 동기화** (타임스탬프 기반 병합); **내 즐겨찾기** 위젯 지원  

### 개발자 즐겨찾기

- **설정 → 데이터 → 개발자 즐겨찾기**에서 **작가 + 지역**별로 개발자 저장  
- 즐겨찾기와 설정 사이에 선택적 **개발자 즐겨찾기 탭** (**설정 → 앱 설정 → 탭 바에 개발자 즐겨찾기 표시**; 기본값 꺼짐)  
- 목록/그리드 레이아웃, 고정, 전체 또는 지역별 필터, 컬렉션 순서/이름/지역별 정렬  
- 세부 정보 **더보기** 메뉴나 길게 누르기 **개발자** 서브메뉴에서 추가; 개발자의 앱 열기 또는 **랭킹별** 차트 보기  
- 선택적 **iCloud 별도 동기화** 토글 (기본값 꺼짐; 타임스탬프 기반 병합)  

### 카드 공유

- **4가지 템플릿** — 클래식, 고대, 클린, 스토리  
- **내보내기 품질** — 표준, 높음, 울트라 (모든 단계에서 더 선명한 벡터 렌더링)  
- 표시할 필드 선택 (개발자, 카테고리, 버전, 가격, 설명, 워터마크 등)  
- 세로 소셜 포맷에 최적화된 스토리 템플릿  
- 순위/즐겨찾기/전체 지역 공유 이미지에는 **공유 시각** 타임스탬프 포함; 긴 이미지는 안전한 이어붙이기 사용  

### 위젯 & 라이브 액티비티

- **랭킹 · iApp** (iOS 17 이상) — 위젯별 차트, 카테고리, 지역 선택 가능; 테마와 언어는 앱 설정을 따릅니다
- **내 즐겨찾기 · iApp** — 지역별 즐겨찾기 목록; **고정된 앱 우선 표시**
- **크기** — 소형부터 매우 큰형, 잠금화면 원형 및 직사각형
- **라이브 액티비티 — 랭킹** (iOS 16.2 이상) — 잠금화면 + 다이내믹 아일랜드 상위 6개; 순위 추적 프리셋과 연동; 탭하면 필터링된 랭킹 열기
- **라이브 액티비티 — 구독** (iOS 16.2 이상) — 별도 마스터 토글; 가격 포함 구독별 상태 확인; 탭하면 앱 상세 열기
- 설정 가이드: **설정 → 위젯** 및 **설정 → 고급 → 라이브 액티비티**

### 바로가기 링크, 빠른 동작 & 시리

- **`iapp://` 링크** — 앱 세부정보 페이지를 열고 필터링된 순위 보기로 이동하거나 **8개의 보조 페이지**(개발자 즐겨찾기, 검색 기록, 순위 추적 등)로 딥 링크합니다. [바로가기 링크](url-scheme)를 참조하세요. 
- **홈 화면 빠른 작업** — **15** 옵션 중 최대 **4** 선택(개발자 즐겨찾기, 검색 기록, 순위 추적, 실시간 활동 설정 등 포함) 
- **Siri 및 단축키**(iOS 16+) — 앱을 검색하고 차트를 열거나 즐겨찾기를 추가합니다. **완전히 현지화됨** 18개 앱 언어 모두 
- **Mac 키보드 단축키** — **⌘1–⌘N** 표시되는 탭에 따라 탭을 동적으로 전환합니다(순위, 검색, 구독, 즐겨찾기, 개발자 즐겨찾기, 설정). 

### 언어 및 도움말 

- **설정 → 모양 → 언어** — 시스템 기본값 또는 **18개 언어**: English, 简体中文, 繁體中文, 日本語, English, Русский, Français, Deutsch, Español, Português, Italiano, العربية, اندي, Bahasa Indonesia, Türkçe, Tiếng 비엣, ไท้, 폴스키 
- 위젯과 **Siri** 문구는 동일한 언어 설정을 따릅니다. 
- **사용 가이드** — **설정 → 도움말 → 사용 지침** (가격 인하 방법을 포함한 확장된 FAQ) 
- 순위 추적 가이드, 위젯 가이드, 5페이지 온보딩

### 설정 및 도구

- 밝음, 어두움 및 시스템 모양; 미리보기가 포함된 **9개의 대체 앱 아이콘**(**설정 → 모양 → 앱 아이콘**, iOS에만 해당) 
- 옵션 위젯 테마 동기화 
- **앱 설정**(**데이터** 뒤, 타사 링크 앞) — 모바일 데이터 사용량 알림(기본적으로 켜져 있음), 구독/즐겨찾기/ **개발자 즐겨찾기** 탭 표시 
- **데이터** — 즐겨찾기, 개발자 즐겨찾기, 구독, **앱 검색 기록**(로컬, 최대 100개), iCloud 토글, 캐시 관리 
- **App Store 지역** — Apple의 공식 링크(**설정 → 타사**)를 통해 기기의 App Store 스토어를 전환하세요. 인앱 차트 영역 필터와 독립적 
- **Apple 서비스** — 56개의 Apple 개발자 및 스토어 리소스에 대한 엄선된 링크(다국어로 현지화된 표시) 
- **iCloud 동기화**(선택 사항, 별도 토글) — 앱 즐겨찾기, **개발자 즐겨찾기**, 구독, 필터 사전 설정, 검색/빠른 영역 
- 인라인 캐시 관리 - 저장된 이미지, 위젯 아이콘, 순위 기록 저장 공간 지우기 
- 트래픽이 많은 조회 전 **셀룰러 데이터 확인**(모든 지역 비교, 순위별 개발자/즐겨찾기 보기) 앱 설정에서 비활성화할 수 있습니다 
- 인앱 평가, 피드백 이메일, 앱 공유, 앱 업데이트 프롬프트

## 앱 다운로드

| 채널 | 링크 |
|---------|------|
| 앱 스토어 | [앱 스토어에서 다운로드](https://apps.apple.com/app/id6446581591) |

## 시스템 요구 사항

| 구성 요소 | 최소 버전 |
|-----------|-----------------|
| iPhone / iPad (메인 앱) | iOS 15.0 이상 |
| 대체 앱 아이콘 | iOS 10.3 이상 |
| 홈 화면 위젯 | iOS 17.0 이상 |
| 실시간 활동 (순위 + 구독) | iOS 16.2 이상 |
| Siri 및 단축어 | iOS 16.0 이상 |
| 인앱 번역 | iOS 18.0 이상 |
| Mac | macOS 11.0 이상 |

## 문의하기

질문, 피드백 또는 도움이 필요하시면:

- **이메일:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

보통 48시간 이내에 답변드립니다.

[FAQ](faq) · [단축 링크](url-scheme) · [개인정보 처리방침](privacy)

</section>
<section lang="ru" markdown="1">

iApp (爱应用) — это **браузер стороннего App Store** для разработчиков, продакт-менеджеров и любителей приложений. **Вход не требуется** — просматривайте **12 типов живых чартов** в **175 регионах**, ищите с фильтрами по платформе, смотрите **предварительные видеоролики приложений**, сравнивайте **контент магазина между регионами**, читайте обзоры и списки внутриигровых покупок, отслеживайте рейтинги с интерактивными графиками, контролируйте события версий / размещения / снятия с публикации / **снижения цены**, сохраняйте **избранных разработчиков**, возвращайтесь к приложениям из **истории просмотра**, делитесь настраиваемыми QR-картами и оставайтесь в чартах с помощью **виджетов**, **Live Activity** и **ссылок-ярлыков**. Полный интерфейс на **18 языках** плюс системный по умолчанию; фразы **Siri & Shortcuts** соответствуют выбранному языку.

> **Примечание:** Это приложение не связано с Apple Inc. и не предоставляет возможность скачивания или установки приложений. Информация о магазине берется из **публичных данных App Store**. Для покупок и загрузок обращайтесь к официальному App Store.

## Начало работы

1. Заполните **5-страничное руководство по функциям** при первом запуске (откройте его в любое время в **Настройки → Справка → Руководство по функциям**). 
2. В разделе **Рейтинги** выберите **регион**, **тип диаграммы** и **категорию** — используйте средство выбора региона с возможностью поиска или **быстрые чипы региона** (HK/TW/MO отображают более понятные названия в средстве выбора; коды регионов остаются прежними). 
3. Если выбран вариант **Игры**, перейдите к **18 подкатегориям игр** (боевики, головоломки, стратегии и т. д.). 
4. Для получения подробной информации коснитесь любого приложения — переключите **регион** в заголовке, посмотрите **видео с предварительным просмотром приложений**, прочитайте **отзывы пользователей** (нажмите, чтобы развернуть полный текст), просмотрите **список покупок в приложении**, проверьте **информацию о магазине для всех регионов** (включая **сравнение контента**) и просмотрите масштабируемую **галерею скриншотов**. 
5. **Проведите пальцем влево** в рейтингах или найдите **избранное**; **Длительное нажатие** любой строки для действий **Добавить подписку** или **Разработчика** (домашняя страница, приложения того же разработчика, сохранение разработчика). 
6. Управляйте избранным на дополнительной вкладке **Избранное** или **Настройки → Данные → Избранное приложений** — закрепляйте, сортируйте, группируйте, просматривайте по рейтингу, пакетное редактирование или экспорт. 
7. Используйте **Подписки**, чтобы смотреть **обновления версий**, **списки**, **удаления** или **снижения цен**; приостановить любой монитор, не удаляя его; настроить интервалы проверки для всего приложения или для каждого приложения (по умолчанию **30 секунд**). 
8. Сохраните разработчиков в **Настройки → Данные → Избранное разработчика** или на дополнительной вкладке **Избранное разработчика** (дополнительная отдельная синхронизация **iCloud**). 
9. Вернитесь к недавно просмотренным приложениям в разделе **Настройки → Данные → История просмотра приложений** (только локально, до 100 записей). 
10. Включите **Отслеживание рейтинга** в **Настройки → Дополнительно**, чтобы сохранять историю рейтингов (включая **записи выпадения**), создавать настройки отслеживания и при необходимости отображать **Активность в реальном времени** (iOS 16.2+). 
11. Добавьте виджеты **Рейтинги** или **Мое избранное** (iOS 17+); выберите один из **9 альтернативных значков приложений**; нажмите и удерживайте значок приложения, чтобы выполнить быстрые действия, или спросите **Siri**.

# Особенности

### Рейтинги

- **12 типов динамических диаграмм** — топ бесплатных/платных/прибыльных iPhone, iPad и **Mac**, а также диаграммы новых приложений. 
- **26 основных категорий** + **18 подкатегорий игр** при выборе «Игры». 
- **175 стран и регионов** — заходите в любой магазин, не меняя Apple ID; поиск по ключевым словам + настраиваемый **быстрые чипы регионов** 
- **Постоянные фильтры** и **список/сетка** (2–4 столбца на iPhone, 3–6 на iPad); строки сетки одинаковой высоты 
- **Значки платформы** в строках диаграмм Mac и iPad; бесплатные приложения показывают серые цены в виде сетки 
- **Встроенные состояния ошибок** с повторной попыткой, если диаграмма не загружается. 
- **Отслеживание истории рейтингов** (необязательно) — сохраняется на вашем устройстве, до 90 записей для каждого представления диаграммы, включая события **выпадания из диаграммы**. 
- **Наборы настроек отслеживания** — смотрите определенные приложения на специальной странице отслеживания, просматривайте **интерактивные диаграммы рейтингов** (перетаскивайте их для прокрутки), включите **Активность в режиме реального времени** для каждого набора настроек. 
- **Поделиться диаграммой** — экспортируйте снимок фирменного изображения (до 30 приложений) с меткой региона, сводкой фильтров и значками приложений (предварительно загруженными перед экспортом). 
- **Меню при длительном нажатии** — добавление подписки, открытие информации обо всем регионе, приложения того же разработчика, подменю **Разработчик** и многое другое. 
- **Более быстрый просмотр по рейтингу** — пакетная предварительная выборка диаграмм для избранных, рейтинговых таблиц одного разработчика и всех регионов (лучше всего при использовании Wi-Fi).

### Поиск

- Поиск по ключевым словам с **фильтром платформ iPhone / iPad / Mac** (сохраняется между визитами)
- **История поиска** — до 50 последних запросов; нажмите, чтобы искать снова; закрытие панели поиска сохраняет результаты
- **Пакетный поиск по ID приложений** — вставьте до 50 ID, разделённых запятыми; **отдельный числовой ID приложения** (6–12 цифр, без запятой) также работает
- **Вставка ссылок App Store** — поиск и подписки могут обрабатывать URL магазина
- **Настраиваемые поля списка** — показывать размер / рейтинг / дату и другое в Рейтингах, Поиске, Избранном и списках одного разработчика
- **Быстрое действие для Рейтингов разработчиков** — закрепите график разработчика в меню иконки на Главном экране; глубокие ссылки по одному разработчику через график
- **Быстрая панель выбора региона** вверху (общая или отдельная для Рейтингов и Поиска)
- Сохраняемая компоновка списка/сетки; показывается опция повторной попытки при ошибке загрузки
- С включённым Отслеживанием рейтинга возврат в фоновый режим может тихо обновлять и добавлять локальную историю рейтингов

### Детали приложения

- Переключить **регион** из шапки подробностей, не покидая страницу; недоступные регионы показывают полезные альтернативы 
- Версия, рейтинг, цена, описание, примечания к выпуску, идентификатор пакета, совместимость, языки; **размер файла** указан в десятичных единицах App Store (МБ/ГБ в расчете на 1000). 
- **Видео предварительного просмотра приложений** — воспроизводите официальные трейлеры предварительного просмотра App Store (HLS); переключить качество, отключить/включить звук, скопировать ссылку, **сохранить в фотографиях со звуком** (требуется разрешение библиотеки фотографий) 
- **Встроенные покупки** — свертываемый список рекомендуемых покупок в приложении для текущего региона (название, цена, значок подписки); ручное обновление в случае сбоя 
- **Отзывы пользователей** — карусель предварительного просмотра, полная страница с разбивкой рейтингов и фильтрами (до 500); **нажмите на отзыв, чтобы развернуть или свернуть** полный текст; **ответы разработчиков** отображаются внутри; API отзывов клиентов по умолчанию, резервный RSS, если он пуст или не работает 
- **История версий** — отдельная страница со списком прошлых выпусков (версия, дата, примечания к выпуску) из каталога App Store. 
- **Информация о магазине во всех регионах** — проверьте доступность в более чем 170 регионах; Просмотр **Все**, **По рейтингу** или **Сравнение контента**. 
– **Сравнение контента** – описание различий, примечания к выпуску, снимки экрана и видео для предварительного просмотра по сравнению с базовым регионом; коснитесь другого региона для просмотра рядом с оранжевыми бликами; дополнительные фильтры (контент/описание/примечания к выпуску/скриншот/разница видео); **экспорт изображений недоступен** в этом режиме; подтверждение сотового телефона перед входом 
- **Галерея скриншотов** — всплывающее окно на iPhone и полноэкранный режим на iPad; масштабирование щипком; сохранить текущий/все; подборщик качества (стандартное/HD/оригинальное); предпочитает **официальные скриншоты App Store HD** (при наличии нескольких платформ порядок iPhone → iPad → Mac) 
- Коснитесь значка приложения, чтобы просмотреть его в полном размере, сохранить или поделиться. 
- **Страница App Store в приложении** — просмотр официальной страницы продукта внутри iApp или открытие в приложении App Store. 
- **Расширенное контекстное меню** — все регионы, страница магазина приложений, подменю **Разработчик** (домашняя страница, приложения того же разработчика, сохранение/удаление избранного разработчика), **добавить подписку**, копировать подменю, параметры отображения. 
- **Приложения одного разработчика** — горизонтальный **предварительный просмотр карусели** на странице сведений (нажмите заголовок, чтобы увидеть полный список); **8 вариантов сортировки** (по умолчанию, последнее обновление, дата выпуска, название, рейтинг, цена и т. д.); Таблица **по ранжированию** с экспортом 
- Диаграмма **Интерактивная история рейтингов** при включенном отслеживании — изменения рейтинга, метки выпадения и возврата. 
- Нажмите и удерживайте или коснитесь, чтобы **скопировать** с кратким подтверждением на экране; iOS 18 **перевод** иностранного текста 
- **История просмотров** — каждая деталь посещения записывается локально (приложение + регион, до 100); управлять в **Настройки → Данные → История просмотра приложений**.

### Мониторинг подписки 

- **Четыре типа мониторов** (для каждого региона): **обновление версии**, **новое объявление**, **удаление** и **снижение цены**. 
- **Снижение цены** — установите базовый уровень при добавлении; необязательная целевая цена и/или процент падения; платное → бесплатное всегда имеет значение; одно и то же приложение и регион могут содержать **несколько мониторов** разных типов. 
- **Добавить поиск по ключевым словам** с фильтром по платформам; или **нажмите и удерживайте любую строку списка** → Добавить подписку. 
- **Пауза/возобновление** любого активного монитора без удаления — приостановка останавливает опрос и завершает его живую активность; резюме запускает немедленную проверку 
- **Глобальный интервал проверки** — по умолчанию **30 секунд**, минимум 10 секунд, примерно до 24 часов; **интервал каждой подписки** переопределить 
- **Принудительная проверка** для каждого элемента; проведите пальцем, чтобы удалить; pull-to-refresh немедленно запускает активные мониторы 
- Опциональная **Активность в реальном времени** (iOS 16.2+) для каждой подписки — независимо от ранга Активность в реальном времени; показывает версию, листинг, исключение из списка или статус цены; нажмите, чтобы открыть подробную информацию о приложении 
- Дополнительная **синхронизация с iCloud** для списка подписок (отдельно от избранного) 
- **Вкладка «Дополнительная подписка»** — скрывается с панели вкладок в **Настройки → Настройки приложения** (все еще доступно из настроек). 

### Избранное

- Необязательная **вкладка Избранное** на панели вкладок (**Настройки → Настройки приложения → Показать Избранное на панели вкладок**; по умолчанию отключено)
- Проведите влево или добавьте в избранное из деталей; отмеченные звёздочкой строки в рейтингах и поиске
- **По регионам** — одно и то же приложение в Китае и США отображается как отдельные записи
- **Закрепление** важных приложений — закреплённые элементы отображаются первыми в списке, сетке и виджете **Мои Избранные**
- **9 режимов сортировки** для списка/сетки; таблица **По рейтингу** с единой сортировкой (по последовательности коллекции, названию, общему/категориальному рейтингу, оценке, цене)
- **Снятые с публикации приложения** остаются видимыми с ясной пометкой, пока вы их не удалите
- **Группы** — стандартные Конкуренты / Собственные приложения; фильтровать по группе или разработчику
- **Пакетное управление** — мультивыбор, закрепление/открепление, назначение группы, массовое удаление из избранного, редактирование заметок
- **Экспорт** — поделиться текстовым сводным отчётом, **CSV-файлом** (совместимым с Excel) или фирменным изображением
- Необязательная **синхронизация iCloud** с объединением по временной метке; обеспечивает работу виджета **Мои Избранные**

### Избранное разработчика

- Сохраняйте разработчиков по **художнику + региону** в **Настройки → Данные → Избранные разработчики**
- Дополнительно **Вкладка Избранные разработчики** между Избранным и Настройками (**Настройки → Настройки приложения → Показать Избранных разработчиков на панели вкладок**; по умолчанию выключено)
- Список/сетка, закрепление, фильтр всех или по региону, сортировка по порядку коллекции / имени / региону
- Добавление из деталей через меню **Подробнее** или долгим нажатием на подменю **Разработчик**; открыть приложения разработчика или просмотр по **рейтингу**
- Дополнительно **отдельный переключатель синхронизации iCloud** (по умолчанию выключено; слияние по отметке времени)

### Поделиться карточками

- **4 шаблона** — Классический, Древний, Чистый, История
- **Качество экспорта** — Стандарт, Высокое, Ультра (более четкий векторный рендер на всех уровнях)
- Выбор полей для отображения (разработчик, категория, версия, цена, описание, водяной знак и другое)
- Шаблон История оптимизирован для вертикальных социальных форматов
- Рейтинги / избранное / изображения для всех регионов содержат отметку **поделено в**; длинные изображения используют более безопасное сшивание

### Виджеты и Живая активность

- **Рейтинги · iApp** (iOS 17+) — выберите график, категорию и регион для каждого виджета; тема и язык следуют настройкам приложения
- **Мои избранные · iApp** — список избранного по регионам; **сначала закреплённые приложения**
- **Размеры** — от Малого до Очень Большого, для экранной блокировки Круглые и Прямоугольные
- **Живая активность — Рейтинги** (iOS 16.2+) — Топ-6 на экране блокировки + Dynamic Island; привязка к пресетам отслеживания рейтинга; тап открывает отфильтрованные Рейтинги
- **Живая активность — Подписки** (iOS 16.2+) — отдельный главный переключатель; статус каждой подписки включая цену; тап открывает сведения о приложении
- Руководства по настройке в **Настройки → Виджеты** и **Настройки → Дополнительно → Живая активность**

### Ссылки на ярлыки, быстрые действия и Siri

- **`iapp://` ссылки** — откройте страницу сведений о приложении, перейдите к отфильтрованному представлению рейтингов или создайте глубокие ссылки на **8 второстепенных страниц** (избранное разработчиков, история просмотров, отслеживание рейтингов и т. д.). См. [Быстрые ссылки] (url-схема). 
- **Быстрые действия на главном экране** — выберите до **4** из **15** вариантов (включая избранное разработчика, историю просмотров, отслеживание рейтинга, настройки активности в реальном времени и т. д.) 
- **Siri и ярлыки** (iOS 16+) — поиск приложений, открытие графиков или добавление в избранное; **полностью локализовано** на всех 18 языках приложения. 
- **Сочетания клавиш Mac** — **⌘1–⌘N** динамически переключают вкладки в зависимости от того, какие вкладки видимы (Рейтинги, Поиск, Подписки, Избранное, Избранное разработчика, Настройки). 

### Язык и помощь 

- **Настройки → Внешний вид → Язык** — система по умолчанию или любой из **18 языков**: английский, 简体中文, 繁體中文, 日本語, 한국어, русский, французский, немецкий, испанский, португальский, итальянский, العربية, हिन्दी, Bahasa Indonesia, Türkçe, Tiếng Việt, ไทย, Polski 
- Виджеты и фразы **Siri** используют одни и те же языковые настройки. 
- **Руководство по использованию** — **Настройки → Справка → Инструкции по использованию** (расширенные часто задаваемые вопросы, включая инструкции по снижению цен) 
- Руководство по отслеживанию рейтингов, руководство по виджетам и 5-страничная регистрация.

### Параметры & Инструменты

- Светлый, Темный и Системный внешний вид; **9 альтернативных значков приложений** с предварительным просмотром (**Настройки → Внешний вид → Значок приложения**, только для iOS) 
- Дополнительная синхронизация темы виджета 
- **Настройки приложения** (после **Данные**, перед сторонними ссылками) — оповещение об использовании мобильных данных (по умолчанию включено), видимость вкладки «Подписка / Избранное / **Избранное разработчика**». 
- **Данные** — избранное, избранное разработчика, подписки, **История просмотра приложений** (локальная, до 100), переключатели iCloud, управление кешем. 
- **Регион App Store** — переключите витрину App Store вашего устройства по официальной ссылке Apple (**Настройки → Сторонние**); независимо от фильтров регионов диаграммы в приложении 
- **Сервисы Apple** — кураторские ссылки на 56 ресурсов для разработчиков и магазинов Apple (локализованное отображение на нескольких языках). 
- **Синхронизация с iCloud** (необязательно, отдельные переключатели) — избранное приложений, **избранное разработчика**, подписки, настройки фильтров, регионы поиска и быстрого доступа. 
- Встроенное управление кэшем — очистка сохраненных изображений, значков виджетов и сохранение истории рейтингов. 
- **Подтверждение сотовых данных** перед поиском с высоким трафиком (сравнение по всем регионам, просмотры по рейтингу разработчиков/избранного); можно отключить в настройках приложения 
- Рейтинг в приложении, электронная почта с отзывами, возможность поделиться приложением, приглашение на обновление приложения.

## Скачайте приложение

| Канал | Ссылка |
|-------|------|
| App Store | [Скачать в App Store](https://apps.apple.com/app/id6446581591) |

## Системные требования

| Компонент | Минимальная версия |
|-----------|-----------------|
| iPhone / iPad (основное приложение) | iOS 15.0+ |
| Альтернативные иконки приложения | iOS 10.3+ |
| Виджеты на домашнем экране | iOS 17.0+ |
| Live Activity (рейтинг + подписка) | iOS 16.2+ |
| Siri и ярлыки | iOS 16.0+ |
| Встроенный перевод | iOS 18.0+ |
| Mac | macOS 11.0+ |

## Свяжитесь с нами

Если у вас есть вопросы, отзывы или нужна помощь:

- **Электронная почта:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Обычно мы отвечаем в течение 48 часов.

[FAQ](faq) · [Ссылки на ярлыки](url-scheme) · [Политика конфиденциальности](privacy)

</section>
<section lang="th" markdown="1">

iApp (爱应用) เป็น **เบราว์เซอร์ของ App Store ของบุคคลที่สาม** สำหรับนักพัฒนา ผู้จัดการผลิตภัณฑ์ และผู้ที่ชื่นชอบแอป **ไม่ต้องลงชื่อเข้าใช้** — เรียกดู **12 ประเภทชาร์ตสด** ใน **175 ภูมิภาค**, ค้นหาด้วยตัวกรองแพลตฟอร์ม, ดู **วิดีโอตัวอย่างแอป**, เปรียบเทียบ **เนื้อหาร้านค้าตามภูมิภาค**, อ่านรีวิวและรายการการซื้อในแอป, ติดตามอันดับด้วยชาร์ตแบบโต้ตอบ, ตรวจสอบเวอร์ชัน / การขึ้นรายการ / การลบรายการ / **เหตุการณ์ลดราคา**, บันทึก **รายชื่อโปรดของนักพัฒนา**, กลับไปยังแอปจาก **ประวัติการเรียกดู**, แชร์การ์ด QR ที่ปรับแต่งได้, และติดตามชาร์ตจาก **วิดเจ็ต**, **กิจกรรมสด**, และ **ลิงก์ทางลัด** ส่วนติดต่อผู้ใช้ครบใน **18 ภาษา** บวกค่ามาตรฐานของระบบ; วลีของ **Siri & Shortcuts** จะเป็นไปตามภาษาที่คุณเลือก

> **หมายเหตุ:** แอปนี้ไม่เกี่ยวข้องกับ Apple Inc. และไม่ให้บริการดาวน์โหลดหรือการติดตั้งแอป ข้อมูลในร้านค้ามาจาก **ข้อมูล App Store สาธารณะ** โปรดดู App Store อย่างเป็นทางการสำหรับการซื้อและดาวน์โหลด

## การเริ่มต้นใช้งาน

1. ทำตาม **คำแนะนำคุณสมบัติ 5 หน้า** ในการเปิดตัวครั้งแรก (เปิดใหม่ได้ทุกเมื่อใน **การตั้งค่า → ช่วยเหลือ → คู่มือคุณสมบัติ**) 
2. ใน **อันดับ** ให้เลือก **ภูมิภาค** **ประเภทแผนภูมิ** และ **หมวดหมู่** — ใช้ตัวเลือกภูมิภาคที่ค้นหาได้หรือ **ชิปภูมิภาคด่วน** (HK / TW / MO แสดงชื่อที่ชัดเจนในเครื่องมือเลือก รหัสภูมิภาคจะยังคงเหมือนเดิม) 
3. เมื่อเลือก **เกม** ให้เจาะลึก **หมวดหมู่ย่อยของเกม 18 หมวดหมู่** (แอคชั่น ปริศนา กลยุทธ์ และอื่นๆ) 
4. แตะแอปใดก็ได้เพื่อดูรายละเอียด — สลับ **ภูมิภาค** ในส่วนหัว ดู **วิดีโอตัวอย่างแอป** อ่าน **บทวิจารณ์ของผู้ใช้** (แตะเพื่อขยายข้อความทั้งหมด) เลือกดู **รายการซื้อในแอป** ตรวจสอบ **ข้อมูลร้านค้าทุกภูมิภาค** (รวมถึง **การเปรียบเทียบเนื้อหา**) และดู **แกลเลอรีภาพหน้าจอ** ที่ซูมได้ 
5. **ปัดไปทางซ้าย** ในการจัดอันดับหรือค้นหาเป็น **รายการโปรด**; **กดค้าง** แถวใดก็ได้เพื่อดำเนินการ **เพิ่มการสมัครสมาชิก** หรือ **นักพัฒนา** (หน้าแรก แอปของนักพัฒนาคนเดียวกัน บันทึกนักพัฒนา) 
6. จัดการรายการโปรดใน **แท็บรายการโปรด** หรือ **การตั้งค่า → ข้อมูล → รายการโปรดของแอป** — ปักหมุด จัดเรียง จัดกลุ่ม ดูตามการจัดอันดับ แก้ไขเป็นชุด หรือส่งออก 
7. ใช้ **การสมัครรับข้อมูล** เพื่อรับชม **การอัปเดตเวอร์ชัน**, **รายการ**, **การลบออก** หรือ **ราคาลดลง**; หยุดจอภาพใด ๆ ชั่วคราวโดยไม่ลบออก ปรับช่วงเวลาการตรวจสอบทั่วโลกหรือต่อแอป (ค่าเริ่มต้น **30 วินาที**) 
8. บันทึกนักพัฒนาใน **การตั้งค่า → ข้อมูล → รายการโปรดของนักพัฒนา** หรือแท็บเสริม **รายการโปรดของนักพัฒนา** (ตัวเลือกการซิงค์ **iCloud** แยกต่างหาก) 
9. เยี่ยมชมแอปที่ดูล่าสุดอีกครั้งใน **การตั้งค่า → ข้อมูล → ประวัติการเรียกดูแอป** (เฉพาะในเครื่องเท่านั้น สูงสุด 100 รายการ) 
10. เปิดใช้งาน **การติดตามอันดับ** ใน **การตั้งค่า → ขั้นสูง** เพื่อบันทึกประวัติอันดับ (รวมถึง **บันทึกการเลื่อนออก**) สร้างการตั้งค่าการติดตามล่วงหน้า และเลือกแสดง **กิจกรรมสด** (iOS 16.2+) 
11. เพิ่มวิดเจ็ต **อันดับ** หรือ **รายการโปรดของฉัน** (iOS 17+) เลือกจาก **ไอคอนแอปสำรอง 9 รายการ**; กดไอคอนแอปค้างไว้เพื่อดำเนินการอย่างรวดเร็ว หรือถาม **Siri**

## คุณสมบัติ

### อับดับ

- **แผนภูมิสด 12 ประเภท** — iPhone, iPad และ **Mac** ฟรียอดนิยม / ชำระเงิน / รายได้รวม รวมถึงแผนภูมิแอพใหม่ 
- **26 หมวดหมู่หลัก** + **18 หมวดหมู่ย่อยของเกม** เมื่อเลือกเกม 
- **175 ประเทศและภูมิภาค** — เรียกดูร้านค้าใดก็ได้โดยไม่ต้องเปลี่ยน Apple ID ของคุณ ค้นหาคำหลัก + กำหนดค่าได้ **ชิปภูมิภาคด่วน** 
- **ตัวกรองถาวร** และ **รายการ/เค้าโครงตาราง** (2–4 คอลัมน์บน iPhone, 3–6 คอลัมน์บน iPad) แถวตารางที่มีความสูงเท่ากัน 
- **ป้ายแพลตฟอร์ม** บนแถวแผนภูมิ Mac และ iPad แอพฟรีแสดงราคาสีเทาในมุมมองตาราง 
- **สถานะข้อผิดพลาดแบบอินไลน์** พร้อมลองอีกครั้งเมื่อโหลดแผนภูมิไม่สำเร็จ 
- **การติดตามประวัติอันดับ** (ไม่บังคับ) — บันทึกลงในอุปกรณ์ของคุณ สูงสุด 90 รายการต่อการดูแผนภูมิ รวมถึงกิจกรรม **การออกจากแผนภูมิ** 
- **การตั้งค่าการติดตามล่วงหน้า** — ดูแอปเฉพาะบนหน้าติดตามเฉพาะ ดู **แผนภูมิอันดับเชิงโต้ตอบ** (ลากเพื่อขัด) เปิดใช้งาน **กิจกรรมสด** ต่อการตั้งค่าล่วงหน้า 
- **แชร์แผนภูมิ** — ส่งออกสแนปชอตรูปภาพของแบรนด์ (สูงสุด 30 แอป) พร้อมป้ายกำกับภูมิภาค สรุปตัวกรอง และไอคอนแอป (ดึงข้อมูลไว้ล่วงหน้าก่อนส่งออก) 
- **เมนูกดแบบยาว** — เพิ่มการสมัครสมาชิก เปิดข้อมูลทุกภูมิภาค แอพสำหรับนักพัฒนาเดียวกัน เมนูย่อย **นักพัฒนา** และอีกมากมาย 
- **การดูตามอันดับเร็วขึ้น** — การดึงข้อมูลแผนภูมิเป็นกลุ่มล่วงหน้าสำหรับรายการโปรด ผู้พัฒนาเดียวกัน และตารางจัดอันดับทุกภูมิภาค (ดีที่สุดบน Wi-Fi)

### ค้นหา

- ค้นหาคำสำคัญพร้อม **ตัวกรองแพลตฟอร์ม iPhone / iPad / Mac** (จำระหว่างการเข้าชม)
- **ประวัติการค้นหา** — เก็บได้สูงสุด 50 คำค้นล่าสุด; แตะเพื่อค้นหาอีกครั้ง; การปิดแถบค้นหาจะคงผลลัพธ์ไว้
- **ค้นหา App ID แบบชุด** — วาง ID สูงสุด 50 รายการที่คั่นด้วยเครื่องหมายจุลภาค; **App ID ตัวเลขเดียว** (6–12 หลัก ไม่มีจุลภาค) ก็ใช้ได้
- **วางลิงก์ App Store** — การค้นหาและการสมัครสมาชิกสามารถแยกวิเคราะห์ URL ของร้านค้าได้
- **ฟิลด์รายการปรับแต่งได้** — แสดงขนาด / คะแนน / วันที่ และอื่นๆ ใน Rankings, Search, Favorites และรายการของนักพัฒนาคนเดียวกัน
- **การกระทำด่วนใน Developer Rankings** — ปักหมุดแผนภูมินักพัฒนาบนเมนูไอคอนหน้าจอหลัก; ลิงก์เชิงลึกของนักพัฒนาคนเดียวกันตามแผนภูมิ
- **แถบชิปภูมิภาคด่วน** ที่ด้านบน (แชร์ร่วมกันหรือแยกสำหรับ Rankings กับ Search)
- การจัดวางรายการ/กริดคงที่; แสดงตัวเลือกลองใหม่เมื่อโหลดล้มเหลว
- เมื่อเปิด Rank Tracking การกลับไปสู่หน้าจอหลักสามารถรีเฟรชเงียบ ๆ และเพิ่มประวัติอันดับบนอุปกรณ์

### รายละเอียดแอป

- สลับ **ภูมิภาค** จากส่วนหัวรายละเอียดโดยไม่ต้องออกจากหน้า ภูมิภาคที่ไม่พร้อมใช้งานแสดงทางเลือกที่เป็นประโยชน์ 
- เวอร์ชัน, การให้คะแนน, ราคา, คำอธิบาย, บันทึกประจำรุ่น, Bundle ID, ความเข้ากันได้, ภาษา; **ขนาดไฟล์** แสดงในหน่วยทศนิยมของ App Store (1,000 MB/GB) 
- **วิดีโอตัวอย่างแอพ** — เล่นตัวอย่างอย่างเป็นทางการของ App Store (HLS) สลับคุณภาพ, ปิดเสียง/เปิดเสียง, คัดลอกลิงก์, **บันทึกลงในรูปภาพพร้อมเสียง** (ต้องได้รับอนุญาตจากคลังภาพ) 
- **การซื้อในแอป** — รายการ IAP เด่นที่ยุบได้สำหรับภูมิภาคปัจจุบัน (ชื่อ ราคา ป้ายการสมัครสมาชิก) รีเฟรชด้วยตนเองเมื่อเกิดความล้มเหลว 
- **บทวิจารณ์ของผู้ใช้** — ภาพตัวอย่างแบบหมุน เต็มหน้าพร้อมรายละเอียดคะแนนและตัวกรอง (สูงสุด 500 รายการ) **แตะบทวิจารณ์เพื่อขยายหรือยุบ** ข้อความเต็ม **การตอบกลับของนักพัฒนา** แสดงอยู่ในบรรทัด API บทวิจารณ์ลูกค้าตามค่าเริ่มต้น RSS สำรองเมื่อว่างเปล่าหรือล้มเหลว 
- **ประวัติเวอร์ชัน** — หน้าเฉพาะที่แสดงรายการรุ่นที่ผ่านมา (เวอร์ชัน วันที่ บันทึกประจำรุ่น) จากแค็ตตาล็อก App Store 
- **ข้อมูลร้านค้าทุกภูมิภาค** — ตรวจสอบความพร้อมในกว่า 170 ภูมิภาค **ทั้งหมด**, **ตามการจัดอันดับ** หรือ **เปรียบเทียบเนื้อหา** ดู 
- **การเปรียบเทียบเนื้อหา** — คำอธิบายที่แตกต่าง บันทึกประจำรุ่น ภาพหน้าจอ และวิดีโอตัวอย่างเทียบกับภูมิภาคพื้นฐาน แตะภูมิภาคอื่นเพื่อดูแบบเคียงข้างกันพร้อมไฮไลต์สีส้ม ตัวกรองพิเศษ (เนื้อหา / คำอธิบาย / บันทึกประจำรุ่น / ภาพหน้าจอ / ส่วนต่างของวิดีโอ); **ไม่สามารถส่งออกรูปภาพได้** ในโหมดนี้ การยืนยันโทรศัพท์มือถือก่อนเข้า 
- **แกลเลอรีภาพหน้าจอ** — ป็อปอัพบน iPhone, เต็มหน้าจอบน iPad; ซูมหยิก; บันทึกปัจจุบัน/ทั้งหมด; ตัวเลือกคุณภาพ (มาตรฐาน / HD / ดั้งเดิม); ชอบ **ภาพหน้าจอ HD อย่างเป็นทางการของ App Store** (iPhone → iPad → Mac สั่งซื้อเมื่อมีหลายแพลตฟอร์ม) 
- แตะไอคอนแอปเพื่อดูขนาดเต็ม บันทึก หรือแชร์ 
- **หน้า App Store ในแอพ** — ดูตัวอย่างหน้าผลิตภัณฑ์อย่างเป็นทางการภายใน iApp หรือเปิดในแอพ App Store 
- **เมนูบริบทที่หลากหลาย** — ทุกภูมิภาค, หน้าร้านค้าในแอป, เมนูย่อย **นักพัฒนา** (หน้าแรก, แอพสำหรับนักพัฒนาเดียวกัน, บันทึก/ลบรายการโปรดของนักพัฒนา), **เพิ่มการสมัครสมาชิก**, คัดลอกเมนูย่อย, ตัวเลือกการแสดงผล 
- **แอปสำหรับนักพัฒนาคนเดียวกัน** — **ภาพตัวอย่างแบบหมุน** แนวนอนในหน้ารายละเอียด (แตะชื่อเพื่อดูรายการทั้งหมด) **8 ตัวเลือกการจัดเรียง** (ค่าเริ่มต้นของร้านค้า อัปเดตล่าสุด วันที่วางจำหน่าย ชื่อ การจัดอันดับ ราคา และอื่นๆ) **ตามอันดับ** ตารางที่มีการส่งออก 
- **แผนภูมิประวัติอันดับเชิงโต้ตอบ** เมื่อเปิดใช้งานการติดตาม — การเปลี่ยนแปลงอันดับ ป้ายกำกับการดรอปออฟและการส่งคืน 
- กดหรือแตะค้างไว้เพื่อ **คัดลอก** พร้อมการยืนยันบนหน้าจอสั้นๆ iOS 18 **การแปล** สำหรับข้อความภาษาต่างประเทศ 
- **ประวัติการเรียกดู** — การเยี่ยมชมรายละเอียดแต่ละครั้งจะถูกบันทึกในเครื่อง (แอป + ภูมิภาค สูงสุด 100 รายการ) จัดการใน **การตั้งค่า → ข้อมูล → ประวัติการเรียกดูแอป**

### การตรวจสอบการสมัครสมาชิก 

- **จอภาพสี่ประเภท** (ต่อภูมิภาค): **การอัปเดตเวอร์ชัน**, **รายการใหม่**, **การลบออก** และ **การลดราคา** 
- **ราคาลดลง** — ตั้งค่าพื้นฐานเมื่อเพิ่มเวลา ราคาเป้าหมายเพิ่มเติมและ/หรือเปอร์เซ็นต์การลดลง; จ่าย → ฟรี นับเสมอ แอป + ภูมิภาคเดียวกันสามารถเก็บ **จอภาพหลายจอ** ประเภทต่างๆ ได้ 
- **เพิ่มด้วยการค้นหาคำหลัก** พร้อมตัวกรองแพลตฟอร์ม หรือ **กดแถวรายการใดก็ได้ค้างไว้** → เพิ่มการสมัครสมาชิก 
- **หยุดชั่วคราว / ดำเนินการต่อ** จอภาพที่ใช้งานอยู่โดยไม่ต้องลบ — การหยุดชั่วคราวจะหยุดการสำรวจและสิ้นสุดกิจกรรมสด ดำเนินการต่อจะทำให้เกิดการตรวจสอบทันที 
- **ช่วงเวลาตรวจสอบทั่วโลก** — ค่าเริ่มต้น **30 วินาที** ขั้นต่ำ 10 วินาที สูงสุดประมาณ 24 ชั่วโมง ** ช่วงเวลาต่อการสมัครสมาชิก ** แทนที่ 
- **บังคับตรวจสอบ** ต่อรายการ ปัดเพื่อลบ; pull-to-refresh จะรันจอภาพที่ใช้งานอยู่ทันที 
- ตัวเลือก **กิจกรรมสด** (iOS 16.2+) ต่อการสมัครสมาชิก — เป็นอิสระจากอันดับกิจกรรมสด แสดงเวอร์ชัน รายการ การเพิกถอน หรือสถานะราคา แตะเปิดรายละเอียดแอป 
- ตัวเลือก **การซิงค์ iCloud** สำหรับรายการสมัครสมาชิก (แยกจากรายการโปรด) 
- **แท็บการสมัครสมาชิกเพิ่มเติม** — ซ่อนจากแถบแท็บใน **การตั้งค่า → การตั้งค่าแอพ** (ยังสามารถเข้าถึงได้จากการตั้งค่า) 

### รายการโปรด

- แท็บ **รายการโปรด** เป็นทางเลือกในแถบแท็บ (**การตั้งค่า → การตั้งค่าแอป → แสดงรายการโปรดในแถบแท็บ**; ปิดเป็นค่าเริ่มต้น)  
- ปัดซ้ายหรือเพิ่มรายการโปรดจากรายละเอียด; แถวที่มีดาวในอันดับและการค้นหา  
- **ตามภูมิภาค** — แอปเดียวกันในจีนและสหรัฐอเมริกาจะอยู่เป็นรายการแยก  
- **ปักหมุด** แอปสำคัญ — รายการที่ปักหมุดจะปรากฏก่อนในรายการ, ตาราง, และวิดเจ็ต **รายการโปรดของฉัน**  
- **โหมดการจัดเรียง 9 แบบ** สำหรับรายการ/ตาราง; **การจัดเรียงตามอันดับ** ตารางที่จัดเรียงร่วม (ลำดับคอลเลกชัน, ชื่อ, อันดับรวม/ตามหมวดหมู่, คะแนน, ราคา)  
- **แอปที่ถูกลบออกจากลิสต์** ยังคงมองเห็นได้พร้อมป้ายชัดเจนจนกว่าคุณจะลบออก  
- **กลุ่ม** — เริ่มต้นด้วย Competitors / Own Apps; กรองตามกลุ่มหรือผู้พัฒนา  
- **การจัดการเป็นกลุ่ม** — เลือกหลายรายการ, ปัก/ยกเลิกปัก, กำหนดกลุ่ม, ยกเลิกรายการโปรดจำนวนมาก, แก้ไขโน้ต  
- **ส่งออก** — แชร์สรุปเป็นข้อความ, **ไฟล์ CSV** (ใช้งานกับ Excel ได้), หรือภาพมีแบรนด์  
- **iCloud Sync** เป็นทางเลือกพร้อมการรวมตามเวลาตราประทับ; สนับสนุนวิดเจ็ต **รายการโปรดของฉัน**  

### รายการโปรดของนักพัฒนา

- บันทึกนักพัฒนาโดย **ศิลปิน + ภูมิภาค** ใน **การตั้งค่า → ข้อมูล → นักพัฒนาที่ชื่นชอบ**
- **แท็บนักพัฒนาที่ชื่นชอบ** แบบเลือกได้ ระหว่าง รายการโปรด และ การตั้งค่า (**การตั้งค่า → การตั้งค่าแอป → แสดงนักพัฒนาที่ชื่นชอบในแถบแท็บ**; ปิดเป็นค่าเริ่มต้น)
- เลย์เอาต์แบบรายการ/กริด, ปักหมุด, กรองทั้งหมดหรือแยกตามภูมิภาค, จัดเรียงตามลำดับคอลเล็กชัน / ชื่อ / ภูมิภาค
- เพิ่มจากเมนูรายละเอียด **เพิ่มเติม** หรือกดค้างที่เมนูย่อย **นักพัฒนา**; เปิดแอปของนักพัฒนาหรือดู **ตามอันดับ**
- ตัวเลือก **ซิงค์ iCloud แยกต่างหาก** (ปิดเป็นค่าเริ่มต้น; ผสานตามเวลาที่บันทึก)

### การแชร์การ์ด

- **4 แบบ** — คลาสสิค, โบราณ, สะอาด, เรื่องราว
- **คุณภาพการส่งออก** — มาตรฐาน, สูง, อัลตร้า (การเรนเดอร์เวกเตอร์คมชัดในทุกระดับ)
- เลือกฟิลด์ที่จะแสดง (นักพัฒนา, หมวดหมู่, เวอร์ชัน, ราคา, คำอธิบาย, ลายน้ำ และอื่น ๆ)
- แบบเรื่องราวเหมาะสำหรับฟอร์แมตโซเชียลแนวตั้ง
- การจัดอันดับ / รายการโปรด / ภาพแชร์ทุกภูมิภาครวม **เวลาที่แชร์**; ภาพยาวใช้การต่อภาพแบบปลอดภัย

### วิดเจ็ต & กิจกรรมสด

- **การจัดอันดับ · iApp** (iOS 17+) — เลือกชาร์ต ประเภท และภูมิภาคตามวิดเจ็ต; ธีมและภาษาตามการตั้งค่าแอป  
- **รายการโปรดของฉัน · iApp** — รายการโปรดตามภูมิภาค; **แอปที่ปักหมุดอยู่ด้านบน**  
- **ขนาด** — เล็กถึงใหญ่มาก, วงกลมและสี่เหลี่ยมบนหน้าจอล็อก  
- **กิจกรรมสด — การจัดอันดับ** (iOS 16.2+) — 6 อันดับแรกบนหน้าจอล็อก + Dynamic Island; เชื่อมโยงกับการติดตามอันดับ; แตะเพื่อเปิดการจัดอันดับที่กรองแล้ว  
- **กิจกรรมสด — การสมัครรับข้อมูล** (iOS 16.2+) — สวิตช์หลักแยกต่างหาก; สถานะต่อการสมัครรวมถึงราคา; แตะเพื่อเปิดรายละเอียดแอป  
- คู่มือการตั้งค่าอยู่ที่ **การตั้งค่า → วิดเจ็ต** และ **การตั้งค่า → ขั้นสูง → กิจกรรมสด**  

### ลิงก์ลัด, การกระทำด่วน & Siri

- ลิงก์ **`iapp://`** — เปิดหน้ารายละเอียดแอป ข้ามไปยังมุมมองการจัดอันดับที่กรองแล้ว หรือลิงก์ในรายละเอียดไปยัง **หน้ารอง 8 หน้า** (รายการโปรดของนักพัฒนา ประวัติการเรียกดู การติดตามอันดับ และอื่นๆ) ดู [ลิงก์ทางลัด](url-scheme) 
- **การดำเนินการด่วนบนหน้าจอหลัก** — เลือกได้สูงสุด **4** จากตัวเลือก **15** (รวมถึงรายการโปรดของนักพัฒนา ประวัติการเรียกดู การติดตามอันดับ การตั้งค่ากิจกรรมสด และอื่นๆ) 
- **Siri และคำสั่งลัด** (iOS 16+) — ค้นหาแอพ เปิดแผนภูมิ หรือเพิ่มรายการโปรด **แปลเป็นภาษาท้องถิ่นทั้งหมด** ในแอปทั้งหมด 18 ภาษา 
- **แป้นพิมพ์ลัดสำหรับ Mac** — **⌘1–⌘N** สลับแท็บแบบไดนามิกโดยขึ้นอยู่กับแท็บที่มองเห็นได้ (อันดับ การค้นหา การสมัครรับข้อมูล รายการโปรด รายการโปรดของนักพัฒนา การตั้งค่า) 

### ภาษาและความช่วยเหลือ 

- **การตั้งค่า → ลักษณะที่ปรากฏ → ภาษา** — ค่าเริ่มต้นของระบบหรือภาษาใด ๆ ใน **18 ภาษา**: อังกฤษ, 简体中文, 繁體中文, 日本語, เกาหลี어, Русский, Français, Deutsch, Español, Português, Italiano, العربية, हिन्दी, Bahasa Indonesia, Türkçe, Tiếng เวียต, ไทย, โปแลนด์ 
- วิดเจ็ตและวลี **Siri** ใช้การตั้งค่าภาษาเดียวกัน 
- **คู่มือการใช้งาน** — **การตั้งค่า → ช่วยเหลือ → คำแนะนำการใช้งาน** (ขยายคำถามที่พบบ่อย รวมถึงวิธีลดราคา) 
- คู่มือการติดตามอันดับ คู่มือวิดเจ็ต และการเริ่มต้นใช้งาน 5 หน้า

### การตั้งค่าและเครื่องมือ

- รูปลักษณ์แสง ความมืด และระบบ; **ไอคอนแอปสำรอง 9 ไอคอน** พร้อมการแสดงตัวอย่าง (**การตั้งค่า → ลักษณะ → ไอคอนแอป**, iOS เท่านั้น) 
- การซิงค์ธีมวิดเจ็ตเสริม 
- **การตั้งค่าแอป** (หลัง **ข้อมูล** ก่อนลิงก์บุคคลที่สาม) — การแจ้งเตือนการใช้ข้อมูลมือถือ (เปิดตามค่าเริ่มต้น) การสมัครสมาชิก / รายการโปรด / **รายการโปรดของนักพัฒนา** การมองเห็นแท็บ 
- **ข้อมูล** — รายการโปรด รายการโปรดของนักพัฒนา การสมัครรับ **ประวัติการเรียกดูแอพ** (ในเครื่อง สูงสุด 100 รายการ) การสลับ iCloud การจัดการแคช 
- **ภูมิภาค App Store** — สลับหน้าร้าน App Store ของอุปกรณ์ผ่านลิงก์อย่างเป็นทางการของ Apple (**การตั้งค่า → บุคคลที่สาม**) เป็นอิสระจากตัวกรองขอบเขตแผนภูมิในแอป 
- **บริการของ Apple** — ลิงก์ที่รวบรวมไว้ไปยังนักพัฒนา Apple และทรัพยากรร้านค้า 56 ราย (การแสดงผลเป็นภาษาท้องถิ่นสำหรับหลายภาษา) 
- **การซิงค์ iCloud** (เป็นทางเลือก การสลับแบบแยก) — รายการโปรดของแอป **รายการโปรดของนักพัฒนา** การสมัครสมาชิก การตั้งค่าตัวกรองล่วงหน้า การค้นหา/ภูมิภาคด่วน 
- การจัดการแคชแบบอินไลน์ — ล้างภาพที่บันทึกไว้ ไอคอนวิดเจ็ต และการจัดเก็บประวัติอันดับ 
- **การยืนยันข้อมูลมือถือ** ก่อนการค้นหาที่มีการเข้าชมสูง (การเปรียบเทียบทุกภูมิภาค ตามการจัดอันดับของนักพัฒนา/มุมมองรายการโปรด) สามารถปิดการใช้งานได้ในการตั้งค่าแอพ 
- การให้คะแนนในแอป อีเมลตอบรับ แชร์แอป ข้อความแจ้งการอัปเดตแอป

## ดาวน์โหลดแอป

| ช่องทาง | ลิงก์ |
|---------|------|
| App Store | [ดาวน์โหลดบน App Store](https://apps.apple.com/app/id6446581591) |

## ความต้องการของระบบ

| ส่วนประกอบ | เวอร์ชันขั้นต่ำ |
|-----------|-----------------|
| iPhone / iPad (แอปหลัก) | iOS 15.0+ |
| ไอคอนแอปทางเลือก | iOS 10.3+ |
| วิดเจ็ตหน้าจอโฮม | iOS 17.0+ |
| กิจกรรมสด (อันดับ + การสมัครสมาชิก) | iOS 16.2+ |
| Siri & ช็อตคัต | iOS 16.0+ |
| การแปลในแอป | iOS 18.0+ |
| Mac | macOS 11.0+ |

## ติดต่อเรา

หากคุณมีคำถาม ข้อเสนอแนะ หรือความช่วยเหลือ:

- **อีเมล:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

ปกติเราจะตอบกลับภายใน 48 ชั่วโมง

[คำถามที่พบบ่อย](faq) · [ลิงก์ช็อตคัต](url-scheme) · [นโยบายความเป็นส่วนตัว](privacy)

</section>
<section lang="de" markdown="1">

iApp (Liebes-App) ist ein **Drittanbieter App Store-Browser** für Entwickler, Produktmanager und App-Enthusiasten. **Keine Anmeldung erforderlich** – durchsuchen Sie **12 Live-Chart-Typen** über **175 Regionen**, suchen Sie mit Plattformfiltern, schauen Sie sich **App-Vorschau-Videos** an, vergleichen Sie **Store-Inhalte über Regionen**, lesen Sie Bewertungen und In-App-Kauflisten, verfolgen Sie Rankings mit interaktiven Diagrammen, überwachen Sie Version / Auflisten / Löschen / **Preis-Rückverkauf**-Ereignisse, speichern Sie **Entwicklerfavoriten**, besuchen Sie Apps aus **Browsing-Verlauf**, teilen Sie konfigurierbare QR-Karten, und bleiben Sie auf Diagrammen aus **Widgets**, **Live-Aktivität** und **Shortcut-Links**. Vollständige Benutzeroberfläche in **18 Sprachen** plus Systemstandard; **Siri & Kurzbefehle** Phrasen folgen Ihrer Sprachwahl.

> **Hinweis: **Diese App ist nicht mit Apple Inc. verbunden und bietet keinen App-Download oder -Installation an. Store-Informationen stammen aus den öffentlichen App StoreDaten**. Bitte wenden Sie sich für Käufe und Downloads an die offizielle App Store.

## Erste Schritte

1. Vervollständigen Sie das 5-Seiten-Feature-Handbuch** beim ersten Start (öffnen Sie es jederzeit wieder in den Einstellungen → Hilfe → Feature-Handbuch**).
2. Wählen Sie unter **Rankings** eine **Region**, **Charttyp** und **Kategorie** aus – verwenden Sie den durchsuchbaren Regionsauswahlprofil oder die schnellen Regionschips** (HK / TW / MO zeigen im Auswahlprofil deutlichere Namen an; die Regionscodes bleiben gleich).
3. Wenn **Games** ausgewählt ist, dringen Sie in **18 Spielunterkategorien** ein (Action, Puzzle, Strategie und mehr).
4. Tippen Sie auf eine beliebige App für Details – schalten Sie **region** im Header um,  schauen Sie sich **App Preview-Videos** an,  lesen Sie **benutzerbewertungen** (tippen Sie,  um den vollständigen Text zu erweitern),  durchsuchen Sie die Liste der In-App-Käufe**,  überprüfen Sie **alle regionalen Store-Informationen** (einschließlich **Inhaltsvergleich**),  und zeigen Sie eine zoombare **Screenshot-Galerie** an.
5. Wischen Sie in den Rankings nach links oder suchen Sie nach Favoriten; drücken Sie lange auf jede Zeile für Abonnement hinzufügen oder Entwickleraktionen (Homepage, Apps desselben Entwicklers, Entwickler speichern).
6. Verwalten Sie Favoriten auf der optionalen Registerkarte Favoriten oder Einstellungen → Daten → App-Favoriten – Anheften, Sortieren, Gruppieren, Anzeigen nach Rang, Batch-Bearbeitung oder Exportieren.
7. Verwenden Sie **Subscriptions**,  um **version-Updates**,  **listings**,  **removals** oder **preiskürzungen** zu überwachen; unterbrechen Sie jeden Monitor,  ohne ihn zu löschen; passen Sie globale oder pro App-Prüfintervalle an (standardmäßig **30 Sekunden**).
8. Speichern Sie Entwickler in den **Einstellungen → Daten → Entwicklerfavoriten** oder der optionalen **Entwicklerfavoriten-Registerkarte** (optional separate **iCloud** Synchronisierung).
9. Überprüfen Sie kürzlich angezeigte Apps unter **Einstellungen → Daten → App-Browsing-Verlauf** (nur lokal, bis zu 100 Einträge).
10. Aktivieren Sie **Rank Tracking** in den **Einstellungen → Advanced**, um den Rangverlauf zu speichern (einschließlich **Drop-off-Datensätze**), Tracking-Presets zu erstellen und optional **Live Activity** (iOS 16.2+) anzuzeigen.
11. Fügen Sie die Widgets „Rankings" oder „Meine Favoriten" hinzu (iOS 17+); wählen Sie aus 9 alternativen App-Symbolen aus; halten Sie das App-Symbol für schnelle Aktionen gedrückt oder fragen Sie Siri.

## Features

### Rankings

- **12 Live-Charttypen** – iPhone, iPad und **Mac** Top Free / Paid / Grossing, plus Neue Apps-Charts
- **26 Hauptkategorien** + **18 Spielunterkategorien** bei Auswahl von Spielen
- **175 Länder und Regionen** - Durchsuchen Sie jeden Store, ohne Ihre Apple-ID zu ändern; Schlüsselwortsuche + konfigurierbare **schnelle Regionchips**
- **Persistente Filter** und **Liste/Rasterlayout** (2–4 Spalten auf iPhone, 3–6 auf iPad); gleich hohe Rasterzeilen
- **Plattform-Badges** auf den Diagrammzeilen Mac und iPad; kostenlose Apps zeigen graue Preise in der Rasteransicht an
- **Inline-Fehlerzustände** mit Wiederholungsversuchen, wenn ein Diagramm nicht geladen werden kann
- **Rankverlaufverfolgung** (optional) – auf Ihrem Gerät gespeichert, bis zu 90 Einträge pro Chartansicht, einschließlich **off-Chart-Drop-off**-Ereignisse
– **Tracking-Voreinstellungen** – Anzeigen bestimmter Apps auf einer dedizierten Tracking-Seite, Anzeigen interaktiver Rangdiagramme** (Ziehen zum Scrubben), Aktivieren von Live-Aktivitäten** pro Voreinstellung
- **Share chart** – exportieren Sie einen markierten Bildsnapshot (bis zu 30 Apps) mit Regionsbezeichnung, Filterzusammenfassung und App-Symbolen (vor dem Export vorab abgerufen)
- Long-press-Menü** – Hinzufügen eines Abonnements, Öffnen aller Regionsinformationen, Apps desselben Entwicklers, Untermenü „Entwickler**" und mehr
- **Schnelleres Anzeigen nach Rangfolge** – Batch-Diagramm vorab abrufen für Favoriten, dieselben Entwickler und Ranglisten in allen Regionen (bestmöglich über WLAN)

### Suche

- Schlüsselwortsuche mit **iPhone / _iPad / _Mac Plattformfilter** (zwischen Besuchen gespeichert)
– **Suchverlauf** – bis zu 50 aktuelle Abfragen; tippen, um erneut zu suchen; das Löschen der Suchleiste behält die Ergebnisse bei
- Batch-App-ID-Suche** – Fügen Sie bis zu 50 durch Kommas getrennte IDs ein; eine einzelne numerische App-ID** (6–12 Ziffern, kein Komma) funktioniert auch
- **Verkleben von App Store Links** – Suche und Abonnements können Speicher-URLs analysieren
- **Konfigurierbare Listenfelder** – Zeigen Sie Größe / Bewertung / Datum und mehr auf Rankings, Search, Favoriten und gleichentwickelten Listen an
- **Schnellaktion Developer Rankings** – Anheften eines Entwicklerdiagramms im Symbolmenü des Home-Bildschirms; tiefe Links desselben Entwicklers nach Diagramm
- **Schnellregions-Chip-Leiste** oben (gemeinsam oder separat für Rankings vs. Search)
- Persistentes Listen-/Rasterlayout; zeigt eine Wiederholungsoption an, wenn das Laden fehlschlägt
- Bei aktivierter Rangverfolgung kann die Rückkehr in den Vordergrund den Rangverlauf auf dem Gerät leise aktualisieren und hinzufügen

### App-Details

- Wechseln Sie **region** aus der Detailüberschrift, ohne die Seite zu verlassen; nicht verfügbare Regionen zeigen hilfreiche Alternativen
- Version,  Bewertung,  Preis,  Beschreibung,  Versionshinweise,  Paket-ID,  Kompatibilität,  Sprachen; **Dateigröße** in __APP_STORE__ Dezimaleinheiten (basierend auf 1000 MB/GB)
- **App Preview-Videos** – Wiedergabe offizieller App Store Preview-Trailer (HLS); Qualität umschalten, Stummschalten/Stummschalten aufheben, Link kopieren, **auf Fotos mit Audio speichern** (Fotobibliotheksberechtigung erforderlich)
- **In-App-Käufe** – zusammenklappbare Liste der vorgestellten IAPs für die aktuelle Region (Name, Preis, Abonnement-Badge); manuelle Aktualisierung bei Ausfall
- **Benutzerbewertungen** – Vorschaukarussell, vollständige Seite mit Bewertungsauflösung und Filtern (bis zu 500); **Tippen Sie auf eine Bewertung, um den vollständigen Text zu erweitern oder zu reduzieren**; **Entwicklerantworten**, die inline angezeigt werden; Kundenbewertungs-API standardmäßig, RSS-Fallback, wenn leer oder fehlgeschlagen
- **Versionsverlauf** – dedizierte Seite mit einer Liste früherer Versionen (Version, Datum, Versionshinweise) aus dem App Store-Katalog
- **Speicherinformationen für alle Regionen** – Verfügbarkeit über mehr als 170 Regionen überprüfen; **Alle**, **Nach Bewertung** oder **Ansicht zum Inhaltsvergleich**
- **Inhalt vergleichen** – Differenz in Beschreibung, Versionshinweisen, Screenshots und Vorschauvideos im Vergleich zu einer Baseline-Region; tippen Sie auf eine andere Region für die Seite-an-Seite-Ansicht mit orangefarbenen Highlights; zusätzliche Filter (Inhalt / Beschreibung / Versionshinweise / Screenshot / Video Differenz); **Image-Export ist in diesem Modus nicht verfügbar**; Mobilfunkbestätigung vor der Eingabe
- **Screenshot-Galerie** – Pop-up auf iPhone, Vollbild auf iPad; Zoom durch Zupfen; aktuell/alle speichern; Qualitätsauswahl (Standard/HD/Original); bevorzugt **offizielle App Store HD-Screenshots** (iPhone → iPad → Mac Reihenfolge, wenn mehrere Plattformen vorhanden sind)
- Tippen Sie auf das App-Symbol, um es in voller Größe anzuzeigen, zu speichern oder zu teilen
- **In-App App Store Seite** – Vorschau der offiziellen Produktseite innerhalb von iApp oder Öffnen in der App Store App
- **Rich Kontextmenü** – alle Regionen, In-App-Store-Seite, **Developer-Untermenü** (Startseite, Apps desselben Entwicklers, Entwicklerfavorit speichern/entfernen), **Abonnement hinzufügen**, Untermenü kopieren, Anzeigeoptionen
- **Apps desselben Entwicklers** – horizontale **Carousel-Vorschau** auf der Detailseite (tippen Sie auf den Titel, um die vollständige Liste anzuzeigen); **8 Sortieroptionen** (Store-Standard, kürzlich aktualisiert, Veröffentlichungsdatum, Name, Bewertung, Preis und mehr); **Tabellen nach Rang** mit Export
- Interaktives Rangverlaufsdiagramm**, wenn die Nachverfolgung aktiviert ist – Rangänderungen, Drop-off- und Return-Beschriftungen
- Drücken Sie lange oder tippen Sie auf **kopieren** mit einer kurzen Onscreen-Bestätigung; iOS 18 **Übersetzung** für ausländischen Text
- **Browsing-Verlauf** – Jeder detaillierte Besuch wird lokal aufgezeichnet (App + Region, bis zu 100); verwalten Sie in **Einstellungen → Daten → App-Browsing-Verlauf**

### Abonnementüberwachung

- **Vier Monitortypen** (pro Region): **Versionsupdate**, **neue Auflistung**, **Entfernung** und **Preisreduzierung**
- **Preisabfall** – Baseline bei Ergänzungszeit festlegen; optionaler Zielpreis und/oder Drop-Prozent; bezahlt → kostenlos zählt immer; dieselbe App + Region kann **mehrere Monitore** unterschiedlicher Typen enthalten
- **Nach Schlüsselwort suchen** mit Plattformfilter hinzufügen; oder **eine beliebige Listenzeile lang drücken** → Abonnement hinzufügen
- **Pause/Fortsetzung** eines aktiven Monitors ohne Löschen – Pausieren stoppt die Abfrage und beendet ihre Live-Aktivität; Fortsetzung löst eine sofortige Überprüfung aus
- **Globales Überprüfungsintervall** – Standardmäßig **30 Sekunden**, Minimum 10 Sekunden, bis zu etwa 24 Stunden; **Abonnementintervall** Überschreibung
- **Erzwingen der Überprüfung** pro Element; Streichen zum Löschen; Pull-to-Refresh führt aktive Monitore sofort aus
- Optional **Live Activity** (iOS 16.2+) pro Abonnement – unabhängig von der Live Activity-Rangierung; zeigt Version, Auflistung, Löschung oder Preisstatus an; Tippen öffnet App-Details
- Optional **iCloud sync** für die Abonnementliste (getrennt von Favoriten)
- **Optionaler Abonnement-Tab** – ausblenden von der Tableiste in **Einstellungen → App-Einstellungen** (immer noch über die Einstellungen zugänglich)

### Favoriten

- Optional **Favoriten-Tab** in der Tableiste (**Einstellungen → App-Einstellungen → Favoriten in der Tableiste anzeigen**; standardmäßig deaktiviert)
- Streichen nach links oder Favorit aus den Details; Sternzeilen in Ranglisten und Suchen
- **Nach Region** – dieselbe App in China und den USA sind separate Einträge
- **Wichtige Apps anheften** – Angeheftete Elemente werden zuerst in der Liste, im Raster und im Widget **Meine Favoriten** angezeigt
- **9 Sortiermodi** für Liste/Raster; **Nach Rang**-Tabelle mit einheitlicher Sortierung (Sammlungsreihenfolge, Name, Gesamt-/Kategorienrang, Bewertung, Preis)
- **Entfernte Apps** bleiben mit einem klaren Etikett sichtbar, bis Sie sie entfernen
- **Gruppen** – Standardkonkurrenten/Eigene Apps; nach Gruppe oder Entwickler filtern
- **Batch-Verwaltung** – Mehrfachauswahl, Anheften/Entheften, Zuweisen von Gruppen, Massenunfavoriten, Bearbeiten von Notizen
- **Export** – Textzusammenfassung, CSV-Datei (Excel-freundlich) oder markiertes Bild teilen
- Optional **iCloud Sync** mit zeitstampbasiertem Merge; unterstützt das Widget **Meine Favoriten**

### Entwicklerfavoriten

- Entwickler nach **künstler + Region** in **Einstellungen → Daten → Entwicklerfavoriten** speichern
- Optionale Registerkarte Entwicklerfavoriten** zwischen Favoriten und Einstellungen (**Einstellungen → App-Einstellungen → Entwicklerfavoriten in der Registerkartenleiste anzeigen**; standardmäßig deaktiviert)
- Listen-/Rasterlayout, Pin, Alle oder nach Region filtern, nach Sammlungsreihenfolge sortieren / Name / Region
- Hinzufügen aus dem Detail-Menü *Mehr* oder dem Untermenü *Entwickler* durch langes Drücken; Öffnen von Entwickler-Apps oder Diagrammansicht nach Rang*
- Optionale **separate iCloud sync**-Umschaltung (standardmäßig deaktiviert; timestamp-basierte Zusammenführung)

### Freigabekarten

- **4 Vorlagen** – Klassisch, Alt, Sauber, Geschichte
– **Exportqualität** – Standard, Hoch, Ultra (schärferes Vektor-Rendering auf allen Ebenen)
- Wählen Sie aus, welche Felder angezeigt werden sollen (Entwickler, Kategorie, Version, Preis, Beschreibung, Wasserzeichen und mehr)
- Story-Vorlage optimiert für vertikale soziale Formate
- Rang/Favoriten/all-region-Share-Bilder enthalten einen **geteilten Zeitstempel**; lange Bilder verwenden sicherere Stitching

### Widgets & Live-Aktivität

- **Rankings · iApp** (iOS 17+) – wählen Sie Diagramm, Kategorie und Region nach Widget aus; Thema und Sprache folgen den App-Einstellungen
- **Meine Favoriten · iApp** – Favoritenliste nach Region; **angeheftete Apps zuerst**
- **Größen** – Klein bis extra groß, Sperrbildschirm kreisförmig und rechteckig
- **Live-Aktivität – Rankings** (iOS 16.2+) – Top 6 auf Sperrbildschirm + Dynamic Island; an Rangverfolgungseinstellungen gebunden; durch Tippen werden gefilterte Rankings geöffnet
- **Live-Aktivität – Abonnements** (iOS 16.2+) – separater Master-Umschalter; Status pro Abonnement einschließlich Preis; Tippen öffnet App-Details
- Einrichtungsanleitungen unter **Einstellungen → Widgets** und **Einstellungen → Erweiterte → Live-Aktivität**

### Kurzbefehle, Schnellaktionen und Siri

– **`iapp://` Links** – Öffnen Sie eine App-Detailseite, springen Sie zu einer gefilterten Rankings-Ansicht oder verlinken Sie tief zu **8 sekundären Seiten** (Entwicklerfavoriten, Browserverlauf, Rangverfolgung und mehr). Siehe [Shortcut Links](url-schema).
- Home-Bildschirm-Schnellaktionen** – bis zu 4** aus den Optionen von 15** auswählen (einschließlich Entwicklerfavoriten, Browserverlauf, Rangverfolgung, Live-Aktivitätseinstellungen und mehr)
- Siri & Kurzbefehle** (iOS 16+) – Apps suchen, Charts öffnen oder einen Favoriten hinzufügen; **vollständig lokalisiert** in allen 18 App-Sprachen
– **Mac-Tastaturkurzbefehle** – **⌘1–⌘N** wechselt dynamisch zwischen den Tabs, basierend darauf, welche Tabs sichtbar sind (Rankings, Suche, Abonnements, Favoriten, Entwicklerfavoriten, Einstellungen)

### Sprache & Hilfe

– **Einstellungen → Erscheinungsbild → Sprache** – Systemstandard oder eine der **18 Sprachen**: Englisch,  vereinfachtes Chinesisch,  traditionelles Chinesisch,  Japanisch,  Koreanisch,  Russisch,  Französisch,  Deutsch,  Spanisch,  Portugiesisch,  Italienisch,  Arabisch,  Hindi,  Bahasa Indonesisch,  Türkisch,  Vietnamesisch,  Thailändisch,  Polnisch
- Widgets und **Siri**-Sätze folgen derselben Spracheinstellung
– **Benutzerhandbuch** – **Einstellungen → Hilfe → Gebrauchsanweisungen** (erweiterte FAQs, einschließlich Preisabnahme-Anleitungen)
- Rank-Tracking-Leitfaden, Widget-Leitfaden und 5-Seiten-Onboarding

### Einstellungen und Tools

- Hell, Dunkel und System-Erscheinungsbild; **9 alternative App-Symbole** mit Vorschau (**Einstellungen → Erscheinungsbild → App-Symbol**, iOS nur)
- Optionale Widget-Thema-Synchronisierung
– **App-Einstellungen** (nach **Daten**, vor Links von Drittanbietern) – mobile Datenverwendungswarnung (standardmäßig aktiviert), Tabsichtbarkeit für Abonnement / Favoriten / Entwicklerfavoriten**
- **Data** – Favoriten,  Entwicklerfavoriten,  Abonnements,  **App-Browsing-Verlauf** (lokal,  bis zu 100),  iCloud-Umschaltungen,  Cache-Verwaltung
- **App Store Region** - Wechseln Sie die App Store-Frontseite Ihres Geräts über den offiziellen Link von Apple (**Einstellungen → Drittanbieter**); unabhängig von In-App-Diagrammregionsfiltern
- Apple Services** – Kuratierte Links zu 56 Apple Entwickler- und Speicherressourcen (lokale Anzeige für mehrere Sprachen)
- **iCloud** sync** (optional, separate Umschaltungen) – App-Favoriten, Entwicklerfavoriten, Abonnements, Filtervoreinstellungen, Such-/Schnellregionen
- Inline-Cache-Verwaltung – Klares Speichern von gespeicherten Bildern, Widget-Symbolen und Rangverlaufspeicher
- **Mobilfunkdatenbestätigung** vor Suchvorgängen mit hohem Datenverkehr (All-Region-Vergleich, Ansicht nach Entwickler-/Favoriten-Ranking); kann in App-Einstellungen deaktiviert werden
- In-App-Bewertung, Feedback-E-Mail, App-Freigabe, App-Update-Anfrage

## App abrufen

Kanal Link
|----------|------|
| App Store | [Download on the App Store](https://apps.apple.com/app/id6446581591) |

## Systemanforderungen

| Komponente | Mindestversion |
|------------------------|
| iPhone / iPad (Haupt-App) | iOS 15.0+ |
| Alternative App-Symbole | iOS 10.3+ |
| Home-Bildschirm-Widgets | iOS 17.0+ |
| Live-Aktivität (Rank + Abonnement) | iOS 16.2+ |
| Siri & Kurzbefehle | iOS 16.0+ |
| In-App-Übersetzung | iOS 18.0+ |
| Mac | macOS 11.0+ |

## Kontakt

Wenn Sie Fragen, Feedback oder Hilfe benötigen:

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Wir antworten in der Regel innerhalb von 48 Stunden.

[FAQ](faq) · [Shortcut Links](url-schema) · [Privacy Policy](privacy)

</section>
<section lang="fr" markdown="1">

iApp (爱应用) est un **navigateur de l'App Store tiers** pour les développeurs, les chefs de produit et les passionnés d'applications. **Aucune inscription requise** — parcourez **12 types de classements en direct** dans **175 régions**, recherchez avec des filtres de plateforme, regardez des **vidéos de prévisualisation d'apps**, comparez le **contenu des stores selon les régions**, lisez les avis et les listes d'achats intégrés, suivez les classements avec des graphiques interactifs, surveillez les événements de version / publication / suppression / **baisse de prix**, sauvegardez les **favoris des développeurs**, revisitez les applications depuis l'**historique de navigation**, partagez des cartes QR configurables, et restez informé des classements grâce aux **widgets**, **Live Activity**, et **liens de raccourci**. Interface complète en **18 langues** plus le choix par défaut du système ; les phrases **Siri & Raccourcis** suivent votre choix de langue.

> **Remarque :** Cette application n'est pas affiliée à Apple Inc. et ne fournit pas le téléchargement ni l'installation des applications. Les informations du store proviennent de **données publiques de l'App Store**. Veuillez vous référer à l'App Store officiel pour les achats et les téléchargements.

## Pour commencer

1. Complétez le **guide des fonctionnalités de 5 pages** lors du premier lancement (rouvrez-le à tout moment dans **Paramètres → Aide → Guide des fonctionnalités**). 
2. Dans **Classements**, choisissez une **région**, un **type de graphique** et une **catégorie** — utilisez le sélecteur de région consultable ou des **puces de région rapides** (HK/TW/MO affichent des noms plus clairs dans le sélecteur ; les codes de région restent les mêmes). 
3. Lorsque **Jeux** est sélectionné, explorez **18 sous-catégories de jeux** (Action, Puzzle, Stratégie, etc.). 
4. Appuyez sur n'importe quelle application pour plus de détails : changez de **région** dans l'en-tête, regardez les **vidéos d'aperçu de l'application**, lisez les **avis d'utilisateurs** (appuyez pour développer le texte intégral), parcourez la **liste d'achats intégrée à l'application**, vérifiez les **informations sur la boutique dans toutes les régions** (y compris la **comparaison de contenu**) et affichez une **galerie de captures d'écran** zoomable. 
5. **Faites glisser votre doigt vers la gauche** dans les classements ou recherchez **favori** ; **Appuyez longuement** sur n'importe quelle ligne pour les actions **Ajouter un abonnement** ou **Développeur** (page d'accueil, applications du même développeur, enregistrer le développeur). 
6. Gérez les favoris dans l'onglet **Favoris** ou **Paramètres → Données → Favoris de l'application** en option : épingler, trier, regrouper, afficher par classement, modifier par lots ou exporter. 
7. Utilisez les **Abonnements** pour regarder les **mises à jour de version**, les **annonces**, les **suppressions** ou les **baisses de prix** ; mettre n'importe quel moniteur en pause sans le supprimer ; ajustez les intervalles de vérification globaux ou par application (par défaut **30 secondes**). 
8. Enregistrez les développeurs dans **Paramètres → Données → Favoris des développeurs** ou dans l'onglet **Favoris des développeurs** facultatif (synchronisation **iCloud** séparée facultative). 
9. Revenez sur les applications récemment consultées dans **Paramètres → Données → Historique de navigation des applications** (local uniquement, jusqu'à 100 entrées). 
10. Activez le **Suivi des classements** dans **Paramètres → Avancé** pour enregistrer l'historique des classements (y compris les **enregistrements de dépôt**), créer des préréglages de suivi et éventuellement afficher **Activité en direct** (iOS 16.2+). 
11. Ajoutez les widgets **Classements** ou **Mes favoris** (iOS 17+) ; choisissez parmi **9 icônes d'application alternatives** ; appuyez longuement sur l'icône de l'application pour des actions rapides ou demandez à **Siri**.

## Caractéristiques

### Classements

- **12 types de graphiques en direct** — iPhone, iPad et **Mac** Meilleurs graphiques gratuits/payants/grossifs, ainsi que de nouvelles applications 
- **26 catégories principales** + **18 sous-catégories de jeux** lorsque Jeux est sélectionné 
- **175 pays et régions** — parcourez n'importe quel magasin sans modifier votre identifiant Apple ; recherche par mot-clé + **puces de région rapides configurables** 
- **Filtres persistants** et **disposition en liste/grille** (2 à 4 colonnes sur iPhone, 3 à 6 sur iPad) ; lignes de grille de même hauteur 
- **Badges de plateforme** sur les lignes des graphiques Mac et iPad ; les applications gratuites affichent les prix gris sous forme de grille 
- **États d'erreur en ligne** avec nouvelle tentative lorsqu'un graphique ne parvient pas à se charger 
- **Suivi de l'historique des classements** (facultatif) — enregistré sur votre appareil, jusqu'à 90 entrées par vue graphique, y compris les événements **de dépôt hors graphique** 
- **Préréglages de suivi** : regardez des applications spécifiques sur une page de suivi dédiée, affichez des **graphiques de classement interactifs** (faites glisser pour parcourir), activez **Activité en direct** par préréglage 
- **Partager le graphique** : exportez un instantané d'image de marque (jusqu'à 30 applications) avec l'étiquette de région, le résumé du filtre et les icônes d'application (préchargées avant l'exportation) 
- **Menu en appuyant longuement** : ajoutez un abonnement, ouvrez les informations sur toutes les régions, les applications du même développeur, le sous-menu **Développeur**, et bien plus encore. 
- **Vues plus rapides par classement** : prélecture des graphiques par lots pour les tableaux de classement des favoris, du même développeur et de toutes les régions (meilleur sur Wi-Fi)

### Recherche

- Recherche par mot-clé avec **filtre de plateforme iPhone / iPad / Mac** (mémorisé entre les visites)
- **Historique des recherches** — jusqu'à 50 requêtes récentes ; appuyez pour rechercher à nouveau ; fermer la barre de recherche conserve les résultats
- **Recherche par lot d'ID d'applications** — collez jusqu'à 50 ID séparés par des virgules ; un **ID d'application numérique unique** (6 à 12 chiffres, sans virgule) fonctionne également
- **Coller des liens App Store** — la recherche et les abonnements peuvent analyser les URL de l’App Store
- **Champs de liste configurables** — afficher la taille / la note / la date et plus sur les classements, la recherche, les favoris et les listes de mêmes développeurs
- **Action rapide des classements de développeurs** — épingler un graphique de développeur dans le menu de l'icône de l'écran d'accueil ; liens profonds des mêmes développeurs par graphique
- **Barre de puces rapide pour la région** en haut (partagée ou séparée pour les classements et la recherche)
- Disposition liste/grille persistante ; affiche une option de réessai lorsque le chargement échoue
- Avec le suivi du classement activé, revenir au premier plan peut rafraîchir discrètement et ajouter l’historique des classements sur l’appareil

### Détails de l’application

- Changer de **région** depuis l'en-tête de détail sans quitter la page ; les régions indisponibles affichent des alternatives utiles 
- Version, note, prix, description, notes de version, ID du bundle, compatibilité, langues ; **taille du fichier** affichée en unités décimales de l'App Store (1 000 Mo/Go) 
- **Vidéos d'aperçu de l'application** : lisez les bandes-annonces officielles de l'App Store (HLS) ; changer de qualité, activer/désactiver le son, copier le lien, **enregistrer dans Photos avec audio** (autorisation de la photothèque requise) 
- **Achats intégrés** : liste pliable des IAP présentés pour la région actuelle (nom, prix, badge d'abonnement) ; actualisation manuelle en cas d'échec 
- **Avis d'utilisateurs** — carrousel d'aperçu, page complète avec répartition des notes et filtres (jusqu'à 500) ; **appuyez sur un avis pour développer ou réduire** le texte intégral ; **réponses du développeur** affichées en ligne ; API d'avis clients par défaut, secours RSS en cas de vide ou d'échec 
- **Historique des versions** — page dédiée répertoriant les versions précédentes (version, date, notes de version) du catalogue App Store 
- **Informations sur le magasin dans toutes les régions** : vérifiez la disponibilité dans plus de 170 régions ; Vue **Tous**, **Par classement** ou **Comparaison de contenu** 
- **Comparaison de contenu** : description des différences, notes de version, captures d'écran et aperçus de vidéos par rapport à une région de référence ; appuyez sur une région différente pour une vue côte à côte avec des reflets orange ; filtres supplémentaires (contenu/description/notes de version/capture d'écran/différence vidéo) ; **exportation d'images non disponible** dans ce mode ; confirmation cellulaire avant l'entrée 
- **Galerie de captures d'écran** : fenêtre contextuelle sur iPhone, plein écran sur iPad ; pincer le zoom ; enregistrer le courant/tout ; sélecteur de qualité (standard / HD / original) ; préfère les **captures d'écran HD officielles de l'App Store** (ordre iPhone → iPad → Mac lorsque plusieurs plates-formes existent) 
- Appuyez sur l'icône de l'application pour l'afficher en taille réelle, l'enregistrer ou la partager. 
- **Page App Store intégrée à l'application** : prévisualisez la page produit officielle dans iApp ou ouvrez-la dans l'application App Store 
- **Menu contextuel riche** — toutes les régions, page de la boutique d'applications, sous-menu **Développeur** (page d'accueil, applications du même développeur, enregistrer/supprimer le favori du développeur), **ajouter un abonnement**, copier le sous-menu, options d'affichage 
- **Applications du même développeur** — **aperçu carrousel** horizontal sur la page de détails (appuyez sur le titre pour la liste complète) ; **8 options de tri** (par défaut du magasin, récemment mis à jour, date de sortie, nom, note, prix, etc.) ; Tableau **par classement** avec export 
- **Graphique interactif de l'historique des classements** lorsque le suivi est activé : changements de classement, étiquettes de dépôt et de retour 
- Appuyez longuement ou appuyez sur pour **copier** avec une brève confirmation à l'écran ; iOS 18 **traduction** pour le texte étranger 
- **Historique de navigation** — chaque visite détaillée est enregistrée localement (application + région, jusqu'à 100) ; gérer dans **Paramètres → Données → Historique de navigation des applications**

### Surveillance des abonnements 

- **Quatre types de moniteurs** (par région) : **mise à jour de version**, **nouvelle annonce**, **suppression** et **baisse de prix** 
- ** Baisse de prix ** : définissez la référence au moment de l'ajout ; prix cible facultatif et/ou pourcentage de baisse ; payant → gratuit compte toujours ; la même application + la même région peuvent contenir **plusieurs moniteurs** de différents types 
- **Ajouter par recherche par mot-clé** avec filtre de plateforme ; ou **appuyez longuement sur n'importe quelle ligne de la liste** → Ajouter un abonnement 
- **Pause/reprise** de tout moniteur actif sans le supprimer — la pause arrête l'interrogation et met fin à son activité en direct ; la reprise déclenche une vérification immédiate 
- **Intervalle de vérification global** — par défaut **30 secondes**, minimum 10 secondes, jusqu'à environ 24 heures ; **Remplacement de l'intervalle par abonnement** 
- **Forcer le contrôle** par article ; faites glisser pour supprimer ; pull-to-refresh exécute immédiatement les moniteurs actifs 
- **Activité en direct** facultative (iOS 16.2+) par abonnement — indépendamment du classement de l'activité en direct ; affiche l'état de la version, de la liste, de la radiation ou du prix ; appuyez pour ouvrir les détails de l'application 
- **Synchronisation iCloud** facultative pour la liste d'abonnements (séparée des favoris) 
- **Onglet Abonnement facultatif** : masquez-le dans la barre d'onglets dans **Paramètres → Paramètres de l'application** (toujours accessible depuis Paramètres) 

### Favoris

- **Onglet Favoris** optionnel dans la barre d'onglets (**Paramètres → Paramètres de l'application → Afficher les favoris dans la barre d'onglets** ; désactivé par défaut)
- Glisser vers la gauche ou ajouter aux favoris depuis le détail ; lignes étoilées dans les classements et la recherche
- **Par région** — la même application en Chine et aux États-Unis apparaît en entrées séparées
- **Épingler** les applications importantes — les éléments épinglés apparaissent en premier dans la liste, la grille et le **widget Mes Favoris**
- **9 modes de tri** pour liste/grille ; tableau **Par classement** avec tri unifié (ordre de collection, nom, rang global/par catégorie, note, prix)
- **Applications retirées** restent visibles avec un label clair jusqu'à ce que vous les supprimiez
- **Groupes** — par défaut Concurrents / Applications personnelles ; filtrer par groupe ou développeur
- **Gestion en lot** — sélection multiple, épingler/désépingler, assigner un groupe, retirer en masse des favoris, éditer des notes
- **Exporter** — partager un résumé texte, **fichier CSV** (compatible Excel) ou image personnalisée
- **Synchronisation iCloud** optionnelle avec fusion basée sur l'horodatage ; alimente le **widget Mes Favoris**

### Favoris Développeur

- Sauvegarder les développeurs par **artiste + région** dans **Paramètres → Données → Favoris des développeurs**  
- **Onglet Favoris des développeurs** optionnel entre Favoris et Paramètres (**Paramètres → Paramètres de l’application → Montrer Favoris des développeurs dans la barre d’onglets** ; par défaut désactivé)  
- Présentation en liste/grille, épingler, filtrer tout ou par région, trier par ordre de collection / nom / région  
- Ajouter depuis le menu Détail **Plus** ou sous-menu **Développeur** par appui long ; ouvrir les applications du développeur ou vue du classement **par rang**  
- Option de **synchronisation iCloud séparée** (par défaut désactivée ; fusion basée sur les horodatages)  

### Partager des cartes

- **4 modèles** — Classique, Ancien, Propre, Histoire  
- **Qualité d’exportation** — Standard, Haute, Ultra (rendu vectoriel plus net pour tous les niveaux)  
- Choisir les champs à afficher (développeur, catégorie, version, prix, description, filigrane, et plus)  
- Modèle Histoire optimisé pour les formats sociaux verticaux  
- Les images de classement / favoris / toutes-régions incluent un horodatage **partagé à** ; les images longues utilisent un assemblage plus sûr  

### Widgets & Activité en direct

- **Classements · iApp** (iOS 17+) — choisir le classement, la catégorie et la région par widget ; le thème et la langue suivent les paramètres de l'application
- **Mes Favoris · iApp** — liste des favoris par région ; **applications épinglées en premier**
- **Tailles** — Petit à Très Grand, Écran de verrouillage Circulaire et Rectangulaire
- **Activité en direct — Classements** (iOS 16.2+) — Top 6 sur l’écran de verrouillage + Dynamic Island ; lié aux préréglages de suivi de classement ; appuyer ouvre les Classements filtrés
- **Activité en direct — Abonnements** (iOS 16.2+) — activation principale séparée ; statut par abonnement incluant le prix ; appuyer ouvre le détail de l’application
- Guides d’installation dans **Paramètres → Widgets** et **Paramètres → Avancé → Activité en direct**

### Liens rapides, Actions rapides & Siri

- Liens **`iapp://`** : ouvrez une page de détails d'application, accédez à une vue de classement filtrée ou créez un lien profond vers **8 pages secondaires** (favoris des développeurs, historique de navigation, suivi des classements, etc.). Voir [Liens de raccourci] (schéma d'url). 
- **Actions rapides sur l'écran d'accueil** : choisissez jusqu'à **4** parmi **15** options (y compris les favoris des développeurs, l'historique de navigation, le suivi des classements, les paramètres d'activité en direct, etc.) 
- **Siri et raccourcis** (iOS 16+) : recherchez des applications, ouvrez des graphiques ou ajoutez un favori ; **entièrement localisé** dans les 18 langues de l'application 
- **Raccourcis clavier Mac** — **⌘1–⌘N** change d'onglet de manière dynamique en fonction des onglets visibles (Classements, Recherche, Abonnements, Favoris, Favoris des développeurs, Paramètres) 

### Langue et aide 

- **Paramètres → Apparence → Langue** — Système par défaut ou l'une des **18 langues** : English, 简体中文, 繁體中文, 日本語, 한국어, Русский, Français, Deutsch, Español, Português, Italiano, العربية, हिन्दी, Bahasa Indonesia, Türkçe, Tiếng Việt, ไทย, Polski 
- Les widgets et les phrases **Siri** suivent le même paramètre de langue 
- **Guide d'utilisation** — **Paramètres → Aide → Instructions d'utilisation** (FAQ étendue, y compris comment faire pour baisser les prix) 
- Guide de suivi des classements, guide des widgets et intégration de 5 pages

### Paramètres et outils

- Apparence claire, sombre et système ; **9 alternate app icons** with preview (**Settings → Appearance → App Icon**, iOS only)
 - Synchronisation facultative du thème du widget 
- **Paramètres de l'application** (après **Données**, avant les liens tiers) — alerte d'utilisation des données mobiles (activée par défaut), visibilité de l'onglet Abonnement/Favoris/**Favoris des développeurs** 
- **Data** — favorites, developer favorites, subscriptions, **App Browse History** (local, up to 100), iCloud toggles, cache management
 - **App Store Region** — switch your device's App Store storefront via Apple's official link (**Settings → Third-party**); indépendant des filtres de région de graphique intégrés à l'application 
- **Apple Services** — curated links to 56 Apple developer and store resources (localized display for multiple languages)
 - **iCloud sync** (optional, separate toggles) — app favorites, **developer favorites**, subscriptions, filter presets, search/quick regions
 - Inline cache management — clear saved images, widget icons, and rank history storage
 - **Cellular data confirmation** before high-traffic lookups (all-region comparison, by-ranking developer/favorites views); peut désactiver dans les paramètres de l'application 
- In-app rating, feedback email, share app, app update prompt

## Obtenez l'application

| Canal | Lien |
|-------|------|
| App Store | [Télécharger sur l'App Store](https://apps.apple.com/app/id6446581591) |

## Configuration requise

| Composant | Version minimale |
|-----------|-----------------|
| iPhone / iPad (application principale) | iOS 15.0+ |
| Icônes d'application alternatives | iOS 10.3+ |
| Widgets pour l'écran d'accueil | iOS 17.0+ |
| Activité en direct (classement + abonnement) | iOS 16.2+ |
| Siri et Raccourcis | iOS 16.0+ |
| Traduction intégrée | iOS 18.0+ |
| Mac | macOS 11.0+ |

## Contactez-nous

Si vous avez des questions, des commentaires ou besoin d'aide :

- **Email :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Nous répondons généralement sous 48 heures.

[FAQ](faq) · [Liens de raccourci](url-scheme) · [Politique de confidentialité](privacy)

</section>
<section lang="tr" markdown="1">

iApp (爱应用), geliştiriciler, ürün yöneticileri ve uygulama meraklıları için bir **üçüncü taraf Uygulama Mağazası tarayıcısıdır**. **Giriş yapmaya gerek yok** — **175 bölge**deki **12 canlı grafik türünü** göz atın, platform filtreleriyle arama yapın, **Uygulama Önizleme videolarını** izleyin, **bölgelerdeki mağaza içeriğini karşılaştırın**, yorumları ve uygulama içi satın alma listelerini okuyun, etkileşimli grafiklerle sıralamaları takip edin, sürüm / listeleme / listeden kaldırma / **fiyat düşüşü** olaylarını izleyin, **geliştirici favorilerini** kaydedin, **geçmişten uygulamalara** yeniden göz atın, yapılandırılabilir QR kartlarını paylaşın ve **widget’lar**, **Canlı Aktivite** ve **kısayol linkleri** ile sıralamalarda kalın. Tüm arayüz **18 dilde** ve Sistem varsayılanı; **Siri ve Kısayollar** ifadeleri dil seçiminize göre değişir.

> **Not:** Bu uygulama Apple Inc. ile ilişkili değildir ve uygulama indirimi veya kurulumu sağlamaz. Mağaza bilgileri **kamuya açık Uygulama Mağazası verilerinden** gelmektedir. Lütfen satın alımlar ve indirmeler için resmi Uygulama Mağazası’na başvurun.

## Başlarken

1. İlk başlatmada **5 sayfalık özellik kılavuzunu** doldurun (**Ayarlar → Yardım → Özellik Kılavuzu**'ndan istediğiniz zaman yeniden açabilirsiniz). 
2. **Sıralamalar**'da bir **bölge**, **grafik türü** ve **kategori** seçin; aranabilir bölge seçiciyi veya **hızlı bölge çiplerini** kullanın (HK / TW / MO seçicide daha net adlar gösterir; bölge kodları aynı kalır). 
3. **Oyunlar** seçildiğinde **18 oyun alt kategorisine** (Aksiyon, Bulmaca, Strateji ve daha fazlası) ayrıntılı olarak bakın. 
4. Ayrıntılar için herhangi bir uygulamaya dokunun — başlıkta **bölgeyi** değiştirin, **Uygulama Önizleme videolarını** izleyin, **kullanıcı yorumlarını** okuyun (tam metni genişletmek için dokunun), **uygulama içi satın alma listesine** göz atın, **tüm bölge mağaza bilgilerini** kontrol edin (**içerik karşılaştırması** dahil) ve yakınlaştırılabilir **ekran görüntüsü galerisini** görüntüleyin. 
5. Sıralamada **sola kaydırın** veya **favori** olarak arama yapın; **Abonelik Ekle** veya **Geliştirici** işlemleri (ana sayfa, aynı geliştiricinin uygulamaları, geliştiriciyi kaydetme) için herhangi bir satıra **uzun basın**. 
6. İsteğe bağlı **Favoriler sekmesinde** veya **Ayarlar → Veri → Uygulama Favorileri**'nde favorileri yönetin — sabitleyin, sıralayın, gruplandırın, sıralamaya göre görüntüleyin, toplu olarak düzenleyin veya dışa aktarın. 
7. **Sürüm güncellemelerini**, **listeleri**, **kaldırmaları** veya **fiyat düşüşlerini** izlemek için **Abonelikler**'i kullanın; herhangi bir monitörü silmeden duraklatın; genel veya uygulama başına kontrol aralıklarını ayarlayın (varsayılan **30 saniye**). 
8. Geliştiricileri **Ayarlar → Veri → Geliştirici Favorileri**'ne veya isteğe bağlı **Geliştirici Favorileri sekmesine** (isteğe bağlı ayrı **iCloud** senkronizasyonu) kaydedin. 
9. **Ayarlar → Veri → Uygulamaya Göz Atma Geçmişi**'nde son görüntülenen uygulamaları tekrar ziyaret edin (yalnızca yerel, 100 girişe kadar). 
10. Sıralama geçmişini kaydetmek (**bırakma kayıtları** dahil), izleme ön ayarları oluşturmak ve isteğe bağlı olarak **Canlı Etkinlik** (iOS 16.2+) göstermek için **Ayarlar → Gelişmiş** bölümünde **Sıralama İzleme**'yi etkinleştirin. 
11. **Sıralamalar** veya **Favorilerim** widget'larını ekleyin (iOS 17+); **9 alternatif uygulama simgesi** arasından seçim yapın; Hızlı işlemler için uygulama simgesine uzun basın veya **Siri**'ye sorun.

## Özellikleri

### Sıralaması

- **12 canlı grafik türü** — iPhone, iPad ve **Mac** En Popüler Ücretsiz / Ücretli / Hasılat ve Yeni Uygulama listeleri 
- **26 ana kategori** + **18 oyun alt kategorisi** Oyunlar seçildiğinde 
- **175 ülke ve bölge** — Apple Kimliğinizi değiştirmeden herhangi bir mağazaya göz atın; anahtar kelime arama + yapılandırılabilir **hızlı bölge çipleri** 
- **Kalıcı filtreler** ve **liste/tablo düzeni** (iPhone'da 2-4 sütun, iPad'de 3-6 sütun); eşit yükseklikte ızgara satırları 
- Mac ve iPad grafik satırlarında **Platform rozetleri**; ücretsiz uygulamalar ızgara görünümünde gri fiyatları gösterir 
- Grafik yüklenemediğinde yeniden deneme ile **satır içi hata durumları** 
- **Sıralama geçmişi takibi** (isteğe bağlı) — **grafik dışı düşüş** olayları dahil olmak üzere, harita görünümü başına en fazla 90 giriş olmak üzere cihazınıza kaydedilir 
- **İzleme ön ayarları** — özel bir izleme sayfasında belirli uygulamaları izleyin, **etkileşimli sıralama tablolarını** görüntüleyin (ovmak için sürükleyin), ön ayar başına **Canlı Etkinlik**'i etkinleştirin 
- **Grafiği paylaş** — markalı görselin anlık görüntüsünü (30 uygulamaya kadar) bölge etiketi, filtre özeti ve uygulama simgeleriyle (dışa aktarmadan önce önceden getirilir) dışa aktarın 
- **Uzun basma menüsü** — abonelik ekleyin, tüm bölge bilgilerini açın, aynı geliştirici uygulamalarını, **Geliştirici** alt menüsünü ve daha fazlasını açın 
- **Sıralamaya göre daha hızlı görünümler** — favoriler, aynı geliştirici ve tüm bölgelerin sıralama tabloları için toplu grafik önceden getirme (Wi-Fi'de en iyisi)

### Arama

- **iPhone / iPad / Mac platform filtreli** anahtar kelime araması (ziyaretler arasında hatırlanır)
- **Arama geçmişi** — en son 50 sorguya kadar; tekrar aramak için dokunun; arama çubuğunu kapatmak sonuçları korur
- **Toplu Uygulama Kimliği araması** — virgülle ayrılmış en fazla 50 kimlik yapıştırabilirsiniz; **tek bir sayısal Uygulama Kimliği** (6–12 rakam, virgül yok) de çalışır
- **App Store bağlantılarını yapıştırın** — arama ve abonelikler mağaza URL'lerini çözebilir
- **Yapılandırılabilir liste alanları** — Rankings, Arama, Favoriler ve aynı geliştirici listelerinde boyut / derecelendirme / tarih ve daha fazlasını göster
- **Geliştirici Rangları hızlı işlemi** — bir geliştirici grafiğini Ana Ekran simge menüsüne sabitleyin; aynı geliştirici derin bağlantıları grafiğe göre
- Üstte **Hızlı bölge çipi çubuğu** (Rankings ile Arama için ayrı veya paylaşımlı)
- Kalıcı liste/grid düzeni; yükleme başarısız olduğunda yeniden deneme seçeneği gösterir
- Sıralama Takibi açık olduğunda, uygulama öne döndüğünde sessizce yenileyebilir ve cihaz üzerindeki sıralama geçmişine ekleyebilir

### Uygulama Detayları

- Sayfadan ayrılmadan ayrıntı başlığından **bölgeyi** değiştirin; kullanılamayan bölgeler yararlı alternatifleri gösterir 
- Sürüm, derecelendirme, fiyat, açıklama, sürüm notları, Paket Kimliği, uyumluluk, diller; **dosya boyutu** App Store ondalık birimleriyle gösterilir (1000 tabanlı MB/GB) 
- **Uygulama Önizleme videoları** — resmi App Store önizleme fragmanlarını (HLS) oynatın; kaliteyi değiştir, sesi kapat/aç, bağlantıyı kopyala, **sesli Fotoğraflar'a kaydet** (fotoğraf kitaplığı izni gerekli) 
- **Uygulama içi satın almalar** — mevcut bölge için öne çıkan IAP'lerin daraltılabilir listesi (ad, fiyat, abonelik rozeti); arıza durumunda manuel yenileme 
- **Kullanıcı yorumları** — önizleme karuseli, derecelendirme dökümü ve filtreleri içeren tam sayfa (500'e kadar); **genişletmek veya daraltmak için bir incelemeye dokunun** tam metni; **geliştirici yanıtları** satır içi gösterilir; varsayılan olarak müşteri incelemeleri API'si, boş veya başarısız olduğunda RSS geri dönüşü 
- **Sürüm geçmişi** — App Store kataloğundaki geçmiş sürümlerin (sürüm, tarih, sürüm notları) listelendiği özel sayfa 
- **Tüm bölge mağaza bilgileri** — 170'den fazla bölgedeki stok durumunu kontrol edin; **Tümü**, **Sıralamaya göre** veya **İçerik karşılaştırma** görünümü 
- **İçerik karşılaştırması** — temel bölgeye göre fark açıklamaları, sürüm notları, ekran görüntüleri ve ön izleme videoları; turuncu vurgularla yan yana görünüm için farklı bir bölgeye dokunun; ekstra filtreler (içerik / açıklama / sürüm notları / ekran görüntüsü / video farkı); **görüntü dışa aktarımı bu modda kullanılamaz**; girişten önce hücresel onay 
- **Ekran görüntüsü galerisi** — iPhone'da açılır pencere, iPad'de tam ekran; kıstırma yakınlaştırma; mevcut/tümünü kaydet; kalite seçici (standart / HD / orijinal); **resmi App Store HD ekran görüntülerini** tercih eder (birden fazla platform mevcut olduğunda iPhone → iPad → Mac sırası) 
- Tam boyutlu görüntülemek, kaydetmek veya paylaşmak için uygulama simgesine dokunun 
- **Uygulama içi App Store sayfası** — iApp içindeki resmi ürün sayfasını önizleyin veya App Store uygulamasında açın 
- **Zengin içerik menüsü** — tüm bölgeler, uygulama içi mağaza sayfası, **Geliştirici** alt menüsü (ana sayfa, aynı geliştirici uygulamaları, geliştiricinin favorisini kaydet/kaldır), **abonelik ekle**, alt menüyü kopyala, görüntüleme seçenekleri 
- **Aynı geliştirici uygulamaları** — ayrıntı sayfasında yatay **atlıkarınca önizlemesi** (tam liste için başlığa dokunun); **8 sıralama seçeneği** (mağaza varsayılanı, yakın zamanda güncellenen, yayın tarihi, ad, derecelendirme, fiyat ve daha fazlası); **sıralamaya göre** dışa aktarma tablosu 
- İzleme etkinleştirildiğinde **Etkileşimli sıralama geçmişi** grafiği - sıralama değişiklikleri, ayrılma ve dönüş etiketleri 
- Ekranda kısa bir onayla **kopyalamak** için uzun basın veya dokunun; iOS 18 yabancı metin için **çeviri** 
- **Geçmişe göz at** — her ayrıntılı ziyaret yerel olarak kaydedilir (uygulama + bölge, en fazla 100); **Ayarlar → Veri → Uygulamaya Göz Atma Geçmişi**'nde yönetin

### Abonelik İzleme 

- **Dört monitör türü** (bölge başına): **sürüm güncellemesi**, **yeni listeleme**, **kaldırma** ve **fiyat düşüşü** 
- **Fiyat düşüşü** — ekleme sırasında temel çizgiyi ayarlayın; isteğe bağlı hedef fiyat ve/veya düşüş yüzdesi; ücretli → ücretsiz her zaman önemlidir; aynı uygulama + bölgede farklı türlerde **birden fazla monitör** bulunabilir 
- **Platform filtreli anahtar kelime aramasıyla ekle**; veya **herhangi bir liste satırına uzun basın** → Abonelik Ekle 
- Herhangi bir etkin monitörü silmeden **duraklatın/devam ettirin** — duraklatma, yoklamayı durdurur ve Canlı Etkinliğini sonlandırır; özgeçmiş anında kontrolü tetikler 
- **Genel kontrol aralığı** — varsayılan **30 saniye**, minimum 10 saniye, yaklaşık 24 saate kadar; **abonelik aralığı başına** geçersiz kılma 
- **Öğe başına kontrolü zorla**; silmek için kaydırın; yenilemek için çek, aktif monitörleri anında çalıştırır 
- Abonelik başına isteğe bağlı **Canlı Etkinlik** (iOS 16.2+) — Canlı Etkinlik sıralamasından bağımsız; sürümü, listelemeyi, listeden çıkmayı veya fiyat durumunu gösterir; dokunun uygulama detayını açar 
- Abonelik listesi için isteğe bağlı **iCloud senkronizasyonu** (favorilerden ayrı) 
- **İsteğe Bağlı Abonelik sekmesi** — **Ayarlar → Uygulama Ayarları** bölümündeki sekme çubuğundan gizleyin (yine de Ayarlar'dan erişilebilir) 

### Favoriler

- İsteğe bağlı **Favoriler sekmesi** sekme çubuğunda (**Ayarlar → Uygulama Ayarları → Sekme Çubuğunda Favorileri Göster**; varsayılan kapalı)
- Detaydan sola kaydır veya favorile; sıralamalarda ve aramada yıldızlı satırlar
- **Bölgeye göre** — Çin ve ABD’de aynı uygulama ayrı girdiler
- Önemli uygulamaları **Sabitle** — sabitlenen öğeler liste, ızgara ve **Favorilerim** widget’ında ilk sırada görünür
- Liste/ızgara için **9 sıralama modu**; birleşik sıralama ile **Sıralamaya göre** tablo (koleksiyon sırası, ad, genel/kategori sırası, puan, fiyat)
- **Listeden kaldırılmış uygulamalar**, siz kaldırana kadar net bir etiketle görünür
- **Gruplar** — varsayılan Rakipler / Kendi Uygulamalar; grup veya geliştiriciye göre filtrele
- **Toplu yönetim** — çoklu seçim, sabitle/kaldır, grup ata, toplu favoriden çıkar, notları düzenle
- **Dışa aktar** — metin özetini paylaş, **CSV dosyası** (Excel uyumlu) veya markalı görsel
- İsteğe bağlı **iCloud Senkronizasyonu** zaman damgasına dayalı birleştirme ile; **Favorilerim** widget’ını destekler

### Geliştirici Favorileri

- **Ayarlar → Veri → Geliştirici Favorileri** bölümünde geliştiricileri **sanatçı + bölge** bazında kaydedin  
- Favoriler ve Ayarlar arasında isteğe bağlı **Geliştirici Favorileri sekmesi** (**Ayarlar → Uygulama Ayarları → Sekme çubuğunda Geliştirici Favorilerini Göster**; varsayılan kapalı)  
- Liste/grid görünümü, sabitleme, tümünü veya bölgeye göre filtreleme, koleksiyon sırasına / isme / bölgeye göre sıralama  
- Detay **Daha Fazla** menüsünden veya uzun basma ile **Geliştirici** alt menüsünden ekleyin; geliştiricinin uygulamalarını veya **sıralamaya göre** grafik görünümünü açın  
- İsteğe bağlı **ayrı iCloud senkronizasyonu** anahtarı (varsayılan kapalı; zaman damgasına dayalı birleştirme)

### Kartları Paylaş

- **4 şablon** — Klasik, Antik, Temiz, Hikaye  
- **Dışa aktarım kalitesi** — Standart, Yüksek, Ultra (tüm seviyelerde daha keskin vektör render)  
- Hangi alanların gösterileceğini seçin (geliştirici, kategori, sürüm, fiyat, açıklama, filigran ve daha fazlası)  
- Hikaye şablonu dikey sosyal formatlar için optimize edilmiştir  
- Sıralama / favoriler / tüm bölge paylaşım görselleri **paylaşım zamanı** içerir; uzun görsellerde daha güvenli birleştirme kullanılır

### Widget’lar & Canlı Aktivite

- **Sıralamalar · iApp** (iOS 17+) — widget başına grafik, kategori ve bölge seçin; tema ve dil uygulama ayarlarını takip eder
- **Favorilerim · iApp** — bölgeye göre favori listesi; **sabitlenmiş uygulamalar önce**
- **Boyutlar** — Küçük'den Ekstra Büyük'e, Kilit Ekranı Dairesel ve Dikdörtgen
- **Canlı Aktivite — Sıralamalar** (iOS 16.2+) — Kilit Ekranında + Dinamik Adada İlk 6; sıra takibi ön ayarlarına bağlı; dokunulduğunda filtrelenmiş Sıralamalar açılır
- **Canlı Aktivite — Abonelikler** (iOS 16.2+) — ayrı ana anahtar; fiyat dahil her abonelik durumu; dokunulduğunda uygulama detayını açar
- Kurulum rehberleri **Ayarlar → Widget'lar** ve **Ayarlar → Gelişmiş → Canlı Aktivite** bölümünde

### Kısayol Bağlantıları, Hızlı Eylemler ve Siri

- **_`iapp://` bağlantılar** — bir uygulama ayrıntı sayfasını açın, filtrelenmiş bir Sıralama görünümüne geçin veya **8 ikincil sayfaya** (geliştirici favorileri, göz atma geçmişi, sıralama takibi ve daha fazlası) derin bağlantı verin. Bkz. [Kısayol Bağlantıları](url şeması). 
- **Ana Ekran Hızlı Eylemleri** — **15** seçenek arasından **4**'e kadar seçim yapın (geliştiricilerin favorileri, göz atma geçmişi, sıralama takibi, Canlı Etkinlik ayarları ve daha fazlası dahil) 
- **Siri ve Kısayollar** (iOS 16+) — uygulamaları arayın, grafikleri açın veya favorilerinizi ekleyin; 18 uygulama dilinin tamamında **tamamen yerelleştirilmiştir** 
- **Mac klavye kısayolları** — **⌘1–⌘N** hangi sekmelerin görünür olduğuna bağlı olarak sekmeleri dinamik olarak değiştirir (Sıralamalar, Arama, Abonelikler, Favoriler, Geliştirici Favorileri, Ayarlar) 

### Dil ve Yardım 

- **Ayarlar → Görünüm → Dil** — Sistem varsayılanı veya **18 dilden herhangi biri**: İngilizce, 简体中文, 繁體中文, 日本語, 한국어, Русский, Français, Deutsch, Español, Português, Italiano, العربية, हिन्दी, Bahasa Endonezya, Türkçe, Tiếng Việt, ไทย, Polski 
- Widget'lar ve **Siri** ifadeleri aynı dil ayarını takip eder 
- **Kullanım kılavuzu** — **Ayarlar → Yardım → Kullanım Talimatları** (fiyat indirimi nasıl yapılır dahil genişletilmiş SSS) 
- Sıralama izleme kılavuzu, widget kılavuzu ve 5 sayfalık katılım kılavuzu

### Ayarlar ve araçlar

- Açık, Koyu ve Sistem görünümü; **9 alternatif uygulama simgesi** önizlemeli (**Ayarlar → Görünüm → Uygulama Simgesi**, yalnızca iOS) 
- İsteğe bağlı widget teması senkronizasyonu 
- **Uygulama Ayarları** (**Veri**'den sonra, üçüncü taraf bağlantılarından önce) — mobil veri kullanımı uyarısı (varsayılan açık), Abonelik / Favoriler / **Geliştirici Favorileri** sekme görünürlüğü 
- **Veri** — favoriler, geliştiricilerin favorileri, abonelikler, **Uygulamaya Göz Atma Geçmişi** (yerel, 100'e kadar), iCloud geçişleri, önbellek yönetimi 
- **App Store Bölgesi** — Apple'ın resmi bağlantısı (**Ayarlar → Üçüncü taraf**) aracılığıyla cihazınızın App Store mağazasını değiştirin; uygulama içi grafik bölgesi filtrelerinden bağımsız 
- **Apple Hizmetleri** — 56 Apple geliştirici ve mağaza kaynağına özel olarak hazırlanmış bağlantılar (birden fazla dil için yerelleştirilmiş ekran) 
- **iCloud senkronizasyonu** (isteğe bağlı, ayrı geçişler) — uygulama favorileri, **geliştirici favorileri**, abonelikler, filtre ön ayarları, arama/hızlı bölgeler 
- Satır içi önbellek yönetimi — kayıtlı görüntüleri, widget simgelerini ve sıralama geçmişi deposunu temizleyin 
- Yüksek trafikli aramalardan önce **hücresel veri onayı** (tüm bölge karşılaştırması, geliştirici/favori görünümlerine göre sıralama); Uygulama Ayarlarında devre dışı bırakabilirsiniz 
- Uygulama içi derecelendirme, geri bildirim e-postası, uygulamayı paylaşma, uygulama güncelleme istemi

## Uygulamayı Edinin

| Kanal | Bağlantı |
|-------|---------|
| App Store | [App Store'dan İndirin](https://apps.apple.com/app/id6446581591) |

## Sistem Gereksinimleri

| Bileşen | Minimum Sürüm |
|---------|----------------|
| iPhone / iPad (ana uygulama) | iOS 15.0+ |
| Alternatif uygulama ikonları | iOS 10.3+ |
| Ana Ekran widget'ları | iOS 17.0+ |
| Canlı Aktivite (sıralama + abonelik) | iOS 16.2+ |
| Siri & Kısayollar | iOS 16.0+ |
| Uygulama içi çeviri | iOS 18.0+ |
| Mac | macOS 11.0+ |

## Bize Ulaşın

Sorularınız, geri bildirimleriniz veya yardıma ihtiyacınız varsa:

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Genellikle 48 saat içinde yanıt veriyoruz.

[SSS](faq) · [Kısayol Bağlantıları](url-scheme) · [Gizlilik Politikası](privacy)

</section>
