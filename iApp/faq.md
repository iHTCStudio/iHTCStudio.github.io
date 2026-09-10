---
layout: doc
title: iApp — FAQ
app_id: iApp
doc_title_en: Frequently Asked Questions
doc_title_zh_cn: 常见问题
doc_title_zh_tw: 常見問題
description: Frequently asked questions about iApp.
---

<section lang="en" markdown="1">

### Do I need an Apple ID or sign in?

No. iApp does not require registration or login. You can browse rankings and search apps in any supported region without switching your Apple ID on the device.

### Where does the data come from?

Store listings, search results, app details, and in-app purchase lists come from **public App Store data**. User reviews are shown by region. iApp is a third-party browser — not an official App Store client.

### Can I download or install apps from iApp?

No. iApp only displays public store information. To download or purchase, use **Open in App Store** or the **in-app App Store product page** on the detail screen.

### Is iApp affiliated with Apple?

No. iApp is an independent tool built by iHTC Studio contributors. It is **not affiliated with Apple Inc.**

### What are the main tabs?

By default: **Rankings**, **Search**, **Subscriptions**, and **Settings**. You can optionally show **Favorites** and **Developer Favorites** as their own tabs, and hide **Subscriptions** from the tab bar in **Settings → App Settings**. Favorites are always available from **Settings → Data → App Favorites**; developer favorites from **Settings → Data → Developer Favorites**.

### What are App Preview videos?

On the app detail page, iApp can play official **App Store preview trailers** (streaming video). You can switch quality, mute/unmute, copy the link, or **save to Photos with audio**. Saving requires photo library permission. Preview videos need a network connection.

### What is region content compare?

In **All-region store info**, switch to **Content compare** to diff an app's **description**, **release notes**, **screenshots**, and **preview videos** against a baseline region. Tap a differing region for a side-by-side view with orange highlights. Extra filters help you find description, screenshot, or video differences. This mode uses more data — a cellular confirmation appears by default. **Image export is not available** in content compare; switch back to list or grid to export.

### What is App Browse History?

iApp automatically records apps you open on the detail page (app + region, up to **100** entries, most recent first). View, reopen, swipe to delete, or clear all in **Settings → Data → App Browse History**. This is **local only** — not synced via iCloud, widgets, or other devices. It is separate from **search history**.

### Why do Hong Kong / Taiwan / Macau look different in the region picker?

Region **lists** and **search** show clearer names (e.g. full names in Simplified Chinese, short name + “(China)” in other languages). **Filter chips** and stored region **codes** (`hk`, `tw`, `mo`) are unchanged — deep links and favorites still use the same codes.

### Reviews not loading or truncated?

On the full reviews page, **tap a review** to expand or collapse the full text. iApp loads **customer reviews with developer replies** by default (full star breakdown included); if that source is empty or fails, it falls back to the RSS feed — pull to refresh or use manual refresh on the detail page.

### What are developer replies in reviews?

When a developer responds to a user review on the App Store, iApp shows the **developer reply inline** beneath that review on the full reviews page. Replies load together with the primary customer-reviews source.

### What is App version history?

On the app detail page, open **Version History** to see past releases — version number, release date, and release notes — fetched from the public App Store catalog for the current region.

### What is the same-developer carousel on the detail page?

Below the main detail content, iApp shows a **horizontal preview** of other apps by the same developer (App Store–style carousel). Tap the section title to open the full same-developer list with sorting and by-ranking views.

### Can I search a single App ID?

Yes. In Search, enter one numeric App ID (**6–12 digits**, no comma). For multiple IDs, use comma-separated batch lookup (up to 50).

### Where is the Developer Favorites tab?

**Settings → App Settings → Show Developer Favorites in Tab bar** (default **off**). When enabled, the tab sits between Favorites and Settings. You can always open developer favorites from **Settings → Data** when the tab is hidden.

### What is the Developer submenu in long-press menus?

Developer homepage, same-developer apps, and save/remove developer favorite are grouped under **Developer** in the long-press menu to reduce clutter.

### What is the mobile data usage alert?

On **cellular**, iApp asks for confirmation before high-traffic lookups (all-region comparison, **content compare**, favorites/developer by-ranking views). Default is **on**; disable in **Settings → App Settings**. You can choose "Don't remind again" in the sheet.

### What is the difference between in-app region and App Store region?

- **In-app region filters** (Rankings, Search, detail region switcher) let you browse any store's charts and listings without changing your device.
- **App Store Region** (**Settings → Third-party**) helps switch your device's actual App Store storefront using Apple's official redirect link. These are independent settings.

### What does iCloud Sync cover?

Separate toggles in **Settings → Data**:

- **Favorites** — saved apps (per region), groups, notes, and pin state; timestamp-based merge
- **Developer Favorites** — saved developers (per artist + region); **separate toggle, default off**
- **Subscriptions** — your watch list (optional)
- **Filter presets** — rank-tracking presets (optional)
- **Search region & quick regions** — search defaults and quick-region chips (optional)

All sync through **iCloud** on your private Apple account — not iHTC Studio servers.

### What subscription types are supported?

Four monitors per region:

| Type | Watches for |
|------|-------------|
| Version | New App Store version |
| Listing | App appears in the store |
| Delisting | App removed from the store |
| **Price drop** | Price falls below baseline; optional target price and/or drop %; paid → free always counts |

The same app + region can have **multiple monitors** of different types. Free apps cannot use price-drop monitoring.

### How does price-drop monitoring work?

When you add a price-drop monitor, iApp records the **baseline price**. You can optionally set a **target price** and/or **minimum drop percentage** (either condition can trigger). If both are left empty, any decrease from baseline completes the monitor. The subscription list and **Live Activity** show baseline vs current price.

### Can I pause a subscription?

Yes. Use the context menu on any active subscription to **Pause** — polling stops and its Live Activity ends. **Resume** runs an immediate check and can restart Live Activity. Paused items are not checked on pull-to-refresh.

### How do I add a subscription quickly?

**Long-press** any app row in Rankings, Search, or Favorites → **Add Subscription**. You can also add from the detail page or Subscriptions tab (keyword search for version/delisting monitors).

### What are developer favorites?

Save a developer (by **artist + region**) in **Settings → Data → Developer Favorites**. Open their apps, view **by-ranking** chart positions, pin entries, and optionally sync via a **separate iCloud toggle** (default off). Add from the detail **More** menu or long-press context menu.

### What is on the detail in-app purchase list?

A collapsible **In-App Purchases** section shows featured IAPs for the **current detail region** (name, price, subscription badge). It loads from public App Store pages and may differ from the full catalog in the App Store app. Tap refresh if loading fails.

### Why does file size look different from Settings?

iApp displays app size using **App Store decimal units** (1 GB = 1,000,000,000 bytes), matching what you see in the App Store — not binary GiB.

### Can the same app be favorited in multiple regions?

Yes. Favorites are kept **per App ID and region**. The same app in China and the US appears as two separate entries with region labels.

### What happens if a favorited app is delisted?

The entry stays in your favorites with a **Delisted** label and placeholder icon. You cannot open its detail page, but you can unfavorite it via swipe or context menu.

### What is rank tracking?

Optional feature in **Settings → Advanced**. When enabled, iApp saves rank history on your device (up to 90 entries per chart view), including **drop-off records**. Create **tracking presets**, manage watched apps on the tracking page, view **interactive rank charts** (drag to scrub), and optionally show a **Live Activity** (iOS 16.2+).

### How do favorites pinning and by-ranking view work?

**Pin** apps from the context menu or batch actions. Switch to **By ranking** in the favorites filter menu for a unified sort table (collection order, name, overall/category rank, rating, price). Use **Find other region** to relocate a favorite's store region.

### How do I change the app language?

**Settings → Appearance → Language** — System default or any of **18 languages**. The UI refreshes immediately; widgets and **Siri & Shortcuts** titles, descriptions, and phrases are **fully localized** in the same language.

### How do I change the app icon?

On iPhone/iPad: **Settings → Appearance → App Icon** — pick from **9 alternate icons** with thumbnail preview and full-screen preview. Mac does not support alternate icons.

### Do widgets and Live Activity work on my device?

- **Home Screen widgets** — iOS 17.0+ (Rankings + My Favorites; pinned favorites first)
- **Live Activity — Rankings** — iOS 16.2+ (rank-tracking presets)
- **Live Activity — Subscriptions** — iOS 16.2+ (separate master toggle; per subscription; includes price-drop line)
- Widgets are not available on Mac

### Can I open iApp from a link or shortcut?

Yes. **`iapp://`** links can **open an app detail page**, **return to a filtered Rankings view**, **switch tabs**, or **open secondary pages** (developer favorites, browse history, rank tracking, Live Activity settings, and more). Choose up to **4** from **15** Home Screen Quick Actions in Settings. Widgets and Live Activity generate these links when you tap. See [Shortcut Links](url-scheme).

### How do Siri and Shortcuts work?

On iOS 16+, search apps, open charts, or add a favorite via the **Shortcuts** app or **Siri**. Action names and Siri phrases are **localized in all 18 app languages** — e.g. English *"Search apps in iApp"*; phrases change when you switch **Settings → Appearance → Language**.

### Does iApp work offline?

Rankings, search, reviews, all-region checks, and IAP lists require network access. Recently viewed apps may still show saved images. Favorites, subscriptions, rank history, and search history are **saved on your device**.

### Which devices are supported?

- **iPhone / iPad** — iOS 15.0+ (main app); iOS 10.3+ (alternate icons); iOS 17.0+ (widgets); iOS 16.2+ (Live Activity); iOS 16.0+ (Siri & Shortcuts); iOS 18.0+ (translation)
- **Mac** — macOS 11.0+; **⌘1–⌘N** switch tabs dynamically depending on visible tabs (including optional Favorites and Developer Favorites tabs)

### How do I get iApp?

Download from the [App Store](https://apps.apple.com/app/id6446581591).

### Still need help?

Open **Settings → Help → Usage Instructions** (14 FAQ items including price-drop how-to) or contact [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com). We typically respond within 48 hours.

</section>

<section lang="zh-CN" markdown="1">

### 需要 Apple ID 或登录吗？

不需要。爱应用无需注册或登录，可直接切换地区浏览榜单与搜索。

### 数据从哪里来？

榜单、搜索、详情与应用内购买列表来自 **App Store 公开数据**；用户评论按地区展示。爱应用是第三方浏览工具，非官方 App Store 客户端。

### 能在爱应用里下载或安装 App 吗？

不能。仅展示商店公开信息，下载或购买请使用详情页的 **在 App Store 中打开** 或 **App 内产品页**。

### 主要 Tab 有哪些？

默认：**榜单**、**搜索**、**订阅**、**设置**。可在 **设置 → 应用设置** 中可选显示**收藏 Tab**、**开发者收藏 Tab**，或隐藏**订阅 Tab**。收藏夹始终可从 **设置 → 数据 → App 收藏夹** 进入；开发者收藏可从 **设置 → 数据 → 开发者收藏** 进入。

### App 预览视频是什么？

详情页可播放官方 **App Store 预览片**（流媒体）。可切换清晰度、静音、复制链接，或**含音轨保存到相册**（需相册写入权限）。需联网播放。

### 什么是全地区内容对比？

在**全地区商店信息**中切换到**内容对比**，可对比**简介**、**更新说明**、**截图**与**预览视频**相对基准地区的差异；点按差异地区可双栏查看，变更行橙色高亮。支持内容 / 简介 / 更新 / 截图 / 视频等筛选。**此模式不可导出图片**；蜂窝网络下进入前默认确认。流量消耗较大。

### 什么是 App 浏览记录？

打开应用详情时自动记录（App + 地区，最多 **100** 条，最近优先）。在 **设置 → 数据 → App 浏览记录** 查看、重新打开、左滑删除或清空。**仅保存在本机**，不同步 iCloud，与**搜索历史**相互独立。

### 港 / 台 / 澳在地区列表里名称变了？

**选择列表**与**搜索**显示更清晰名称（简体中文用全称，其他语言短名 +「(China)」等）。**筛选 Chip** 与存储的**地区代码**（`hk` / `tw` / `mo`）不变。

### 评论加载失败或显示不全？

评论页**点按一条评论**可展开 / 收起全文。默认加载**含开发者回复**的 customer-reviews 数据（含完整星级分布）；若为空或失败则退回 RSS——可下拉刷新或详情页手动刷新。

### 评论里的开发者回复是什么？

当开发者在 App Store 回复用户评论时，爱应用在评论全文页**内联显示开发者回复**，与主评论数据源一并加载。

### 什么是应用版本历史？

在应用详情页打开**版本历史**，可查看该地区过往发布记录——版本号、发布日期与更新说明，来自 App Store 公开 catalog。

### 详情页的同开发者横滑预览是什么？

详情页下方以 **App Store 风格横滑卡片**展示同开发者的其他 App；点按区块标题进入完整列表，支持排序与按榜单视图。

### 能只搜索一个 App ID 吗？

可以。搜索框输入单个数字 App ID（**6–12 位**，无逗号）。多个 ID 请用逗号分隔（最多 50 个）。

### 开发者收藏 Tab 在哪里？

**设置 → 应用设置 → 在 Tab 栏显示开发者收藏**（默认**关闭**）。开启后位于收藏与设置之间。关闭 Tab 时仍可从 **设置 → 数据 → 开发者收藏** 进入。

### 如何切换界面语言？

**设置 → 外观 → 语言** — 跟随系统或 **18 种语言**。界面、小组件与 **Siri / 快捷指令** 的标题、描述与短语**完整本地化**。

### iCloud 同步包含什么？

**设置 → 数据** 中各有独立开关：

- **收藏夹** — 已收藏应用（按地区）、分组、备注与置顶；时间戳合并
- **开发者收藏** — 已收藏开发者（按开发者 + 地区）；**独立开关，默认关闭**
- **订阅列表**、**筛选预设**、**搜索地区与常用地区**（均可选）

### 支持哪些订阅类型？

按地区四种监控：

| 类型 | 监控内容 |
|------|----------|
| 版本 | 新版本发布 |
| 上架 | App 出现在商店 |
| 下架 | App 从商店移除 |
| **降价** | 价格低于基准；可设目标价和 / 或降幅；付费转免费视为达标 |

同一 App + 地区可有**多种类型**并存。免费 App 无法使用降价监控。

### 降价监控怎么用？

添加时记录**基准价**；可设**目标价**和 / 或**最低降幅百分比**（满足其一即触发）；两者均留空则任意降价即达标。列表与**实时活动**显示基准价与现价。

### 能暂停订阅吗？

可以。长按菜单选择**暂停**——停止轮询并结束实时活动；**恢复**时立即检查并可重启实时活动。暂停项不会在下拉刷新时检查。

### 如何快速添加订阅？

**长按**榜单 / 搜索 / 收藏中的任意行 → **加入订阅**。也可在详情页或订阅 Tab 添加。

### 什么是开发者收藏？

在 **设置 → 数据 → 开发者收藏** 按**开发者 + 地区**保存。可查看其 App、**按榜单排名**视图、置顶，并可选**独立 iCloud 同步**（默认关闭）。

### 详情页的应用内购买列表是什么？

按**当前详情地区**折叠展示精选 IAP（名称、价格、订阅标识），来自 App Store 公开页面，可能与 App Store App 内完整目录不同。加载失败可手动刷新。

### 为什么容量显示与系统设置不同？

爱应用按 **App Store 十进制单位**显示（1 GB = 10 亿字节），与 App Store 一致，而非二进制 GiB。

### 什么是榜单追踪？

**设置 → 高级** 可选功能。开启后在本机记录排名历史（含掉榜），可创建追踪预设、查看**交互式排名曲线**，并可选**实时活动**（iOS 16.2+）。

### 移动数据提醒是什么？

**蜂窝网络**下，全地区对比、**内容对比**、收藏 / 开发者按榜单查询等高流量操作前会弹出确认。**设置 → 应用设置** 中可关闭（默认开启）。

### 如何更换应用图标？

iPhone / iPad：**设置 → 外观 → 应用图标** — 从 **9 款备用图标**中选择，支持缩略图与全屏预览。Mac 不支持备用图标。

### 小组件和实时活动能用吗？

- **主屏小组件** — iOS 17.0+
- **实时活动 — 榜单 / 订阅** — iOS 16.2+（订阅有**独立总开关**；降价显示价格行）

### Siri 与快捷指令怎么用？

iOS 16+ 可搜索应用、打开榜单、添加收藏。**18 种语言完整本地化**——切换应用语言后 Siri 短语同步变化。`iapp://` 链接可打开详情、榜单筛选、Tab 或 **8 个二级页面**；主屏快捷指令可从 **15 项**中选 **4 项**。详见 [快捷链接说明](url-scheme)。

### 仍有问题？

打开 **设置 → 帮助 → 使用说明**（含 14 条 FAQ，含降价说明），或联系 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)。

</section>

<section lang="zh-TW" markdown="1">

### 需要 Apple ID 或登入嗎？

不需要。愛應用無需註冊或登入。

### 資料從哪裡來？

榜單、搜尋、詳情與應用內購買列表來自 **App Store 公開資料**。

### 主要 Tab 有哪些？

預設：**榜單**、**搜尋**、**訂閱**、**設定**。可在 **設定 → 應用設定** 中可選顯示**收藏 Tab**、**開發者收藏 Tab**，或隱藏**訂閱 Tab**。

### App 預覽影片是什麼？

詳情頁可播放官方 **App Store 預覽片**；可**含音軌保存到相簿**（需相簿寫入權限）。

### 什麼是全地區內容對比？

**全地區商店資訊**中的**內容對比**可對比簡介、更新說明、截圖與預覽影片；雙欄 diff 橙色高亮。**此模式不可匯出圖片**。

### 什麼是 App 瀏覽記錄？

**設定 → 資料 → App 瀏覽記錄** — 最多 **100** 條，**僅本機**，不同步 iCloud。

### 使用者評論載入失敗？

**點按一則評論**可展開 / 收起全文。預設載入**含開發者回覆**的 customer-reviews 資料；若為空或失敗則退回 RSS。

### 什麼是版本歷史？

詳情頁的**版本歷史**列出該地區過往發布記錄（版本號、日期、更新說明）。

### 同開發者橫滑預覽？

詳情頁下方以橫滑卡片展示同開發者的其他 App；點標題進入完整列表。

### 能只搜尋一個 App ID 嗎？

可以。輸入單個數字 App ID（**6–12 位**，無逗號）。多個 ID 請用逗號分隔（最多 50 個）。

### 開發者收藏 Tab 在哪裡？

**設定 → 應用設定 → 在 Tab 欄顯示開發者收藏**（預設**關閉**）。

### iCloud 同步包含什麼？

**設定 → 資料** 中各有獨立開關：收藏夾、**開發者收藏**（獨立開關，預設關閉）、訂閱、篩選預設、搜尋地區等。

### 支援哪些訂閱類型？

**版本更新**、**上架**、**下架**、**降價**四種。同 App + 地區可**多類型並存**。免費 App 無法使用降價監控。

### 降價監控怎麼用？

記錄**基準價**；可設**目標價**和 / 或**降幅**；付費轉免費視為達標。列表與**即時動態**顯示價格變化。

### 能暫停訂閱嗎？

可以。長按選單**暫停**後停止輪詢並結束即時動態；**恢復**時立即檢查。

### 什麼是開發者收藏？

**設定 → 資料 → 開發者收藏** — 依**開發者 + 地區**保存；可檢視**依榜單排名**；可選**獨立 iCloud 同步**（預設關閉）。

### 詳情頁的應用內購買列表？

依**目前詳情地區**折疊展示精選 IAP，來自 App Store 公開頁面。

### 如何更換應用圖示？

**設定 → 外觀 → 應用圖示** — **9 款備用圖示**（僅 iOS）。

### 行動數據提醒？

**行動網路**下全地區對比、**內容對比**、依榜單查詢等高流量操作前確認；**設定 → 應用設定** 可關閉（預設開啟）。

### Siri 與捷徑？

**18 種語言完整本地化**——切換應用語言後 Siri 短語同步變化。`iapp://` 連結可開啟詳情、榜單篩選、Tab 或 **8 個二級頁面**；主畫面捷徑可從 **15 項**中選 **4 項**。詳見 [快捷連結說明](url-scheme)。

### 仍有問題？

**設定 → 幫助 → 使用說明**（含 14 條 FAQ），或聯絡 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)。

</section>
