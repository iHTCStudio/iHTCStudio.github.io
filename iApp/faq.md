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

Yes. **`iapp://`** links can **open an app detail page**, **return to a filtered Rankings view**, **switch tabs**, or **open secondary pages** (developer favorites, browse history, rank tracking, Live Activity settings, and more). Choose up to **4** from **15** Home Screen Quick Actions in Settings. Widgets and Live Activity generate these links when you tap. See [Shortcut Links](../url-scheme).

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

iOS 16+ 可搜索应用、打开榜单、添加收藏。**18 种语言完整本地化**——切换应用语言后 Siri 短语同步变化。`iapp://` 链接可打开详情、榜单筛选、Tab 或 **8 个二级页面**；主屏快捷指令可从 **15 项**中选 **4 项**。详见 [快捷链接说明](../url-scheme)。

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

**18 種語言完整本地化**——切換應用語言後 Siri 短語同步變化。`iapp://` 連結可開啟詳情、榜單篩選、Tab 或 **8 個二級頁面**；主畫面捷徑可從 **15 項**中選 **4 項**。詳見 [快捷連結說明](../url-scheme)。

### 仍有問題？

**設定 → 幫助 → 使用說明**（含 14 條 FAQ），或聯絡 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)。

</section>
<section lang="ja" markdown="1">

### Apple IDは必要ですか、またはサインインは必要ですか？

いいえ。iAppは登録やログインを必要としません。デバイス上でApple IDを切り替えなくても、サポートされている地域のランキングを閲覧したり、アプリを検索したりできます。

### データはどこから取得されますか？

ストアのリスト、検索結果、アプリの詳細、およびアプリ内購入リストは**公開されているApp Storeデータ**から取得されます。ユーザーレビューは地域ごとに表示されます。iAppはサードパーティのブラウザであり、公式のApp Storeクライアントではありません。

### iAppからアプリをダウンロードまたはインストールできますか？

いいえ。iAppは公開されているストア情報のみを表示します。ダウンロードや購入を行うには、詳細画面の**App Storeで開く**または**アプリ内のApp Store商品ページ**を使用してください。

### iAppはAppleと提携していますか？

いいえ。iAppはiHTC Studioの貢献者によって作られた独立したツールです。**Apple Inc.とは提携していません。**

### 主なタブは何ですか？

デフォルトでは：**ランキング**、**検索**、**サブスクリプション**、**設定**です。オプションとして、**お気に入り**や**開発者のお気に入り**を独自のタブとして表示したり、**設定 → アプリ設定**でタブバーから**サブスクリプション**を非表示にすることができます。お気に入りは常に**設定 → データ → アプリのお気に入り**から利用できます。開発者のお気に入りは**設定 → データ → 開発者のお気に入り**から利用できます。

### アプリプレビュー動画とは？

アプリ詳細ページで、iAppは公式の**App Storeプレビュー予告編**（ストリーミング動画）を再生できます。画質の切り替え、ミュート/ミュート解除、リンクのコピー、または**音声付きで写真に保存**が可能です。保存には写真ライブラリの許可が必要です。プレビュー動画にはネットワーク接続が必要です。

### 地域コンテンツ比較とは？

「**全地域ストア情報**」では、アプリの**説明**、**リリースノート**、**スクリーンショット**、**プレビュービデオ**を基準地域と比較するために、**コンテンツ比較**に切り替えます。差異のある地域をタップすると、オレンジでハイライトされたサイドバイサイド表示が可能です。追加フィルターを使うと、説明、スクリーンショット、ビデオの差異を見つけやすくなります。このモードはデータを多く使用するため、デフォルトでモバイル回線での確認が表示されます。**コンテンツ比較では画像のエクスポートはできません**。エクスポートする場合は、リストまたはグリッドに戻してください。

### アプリ閲覧履歴とは何ですか？

iAppは、詳細ページで開いたアプリ（アプリ + 地域、最大**100**件、最新順）を自動的に記録します。**設定 → データ → アプリ閲覧履歴**で閲覧、再開、スワイプで削除、またはすべてクリアできます。これは**ローカルのみ**で、iCloud、ウィジェット、その他のデバイスで同期されません。**検索履歴**とは別です。

### なぜ地域ピッカーで香港・台湾・マカオは異なる表示になるのですか？

地域 **リスト** と **検索** では、より明確な名前が表示されます (例: 簡体字中国語のフルネーム、他の言語のショートネーム + 「(中国)」)。 **フィルター チップ** と保存領域 **コード** (`hk`、`tw`、`mo`) は変更されていません。ディープ リンクとお気に入りは引き続き同じコードを使用します。 

### レビューが読み込まれない、または切り捨てられますか?

 レビュー全文ページで、**レビューをタップ**して全文を展開または折りたたむことができます。 iApp はデフォルトで **開発者の返信を含む顧客レビュー** を読み込みます (星の完全な内訳が含まれます)。 そのソースが空であるか失敗した場合は、RSS フィードにフォールバックします。プルして更新するか、詳細ページで手動更新を使用します。 

### レビューにおける開発者の返信とは何ですか?

 開発者が App Store のユーザー レビューに返信すると、iApp は完全なレビュー ページのレビューの下に **開発者の返信をインラインで**表示します。 返信は、主要な顧客レビュー ソースと一緒に読み込まれます。 

### アプリのバージョン履歴とは何ですか?

 アプリの詳細ページで **バージョン履歴** を開くと、現在の地域の公開 App Store カタログから取得した過去のリリース (バージョン番号、リリース日、リリース ノート) が表示されます。 

### 詳細ページの同じ開発者のカルーセルとは何ですか?

iApp では、主要な詳細コンテンツの下に、同じ開発者による他のアプリの **水平プレビュー** が表示されます (App Store スタイルのカルーセル)。 セクションのタイトルをタップすると、同一開発者の完全なリストが表示され、並べ替えやランキング順のビューが表示されます。 

### 単一のアプリ ID を検索できますか?

 はい。 [検索] に、数値のアプリ ID (**6 ～ 12 桁**、カンマなし) を 1 つ入力します。 複数の ID の場合は、カンマ区切りのバッチ検索を使用します (最大 50)。 

### [開発者のお気に入り] タブはどこにありますか?

 **[設定] → [アプリ設定] → [タブ バーに開発者のお気に入りを表示]** (デフォルトは **オフ**)。 有効にすると、タブはお気に入りと設定の間に配置されます。 開発者のお気に入りは、タブが非表示のときでも **[設定] → [データ]** からいつでも開くことができます。 

### 長押しメニューの開発者サブメニューとは何ですか?

 開発者のホームページ、同じ開発者のアプリ、開発者のお気に入りの保存/削除は、乱雑さを減らすために長押しメニューの **開発者** の下にグループ化されています。 

### モバイル データ使用量アラートとは何ですか?

 **セルラー**では、iApp はトラフィックの多い検索 (全地域比較、**コンテンツ比較**、お気に入り/開発者によるランキング表示) の前に確認を求めます。 デフォルトは**オン**です。 **[設定] → [アプリ設定]** で無効にします。 シートで「今後通知しない」を選択できます。

### アプリ内リージョンと App Store リージョンの違いは何ですか?

 - **アプリ内地域フィルター** (ランキング、検索、詳細地域切り替え) を使用すると、デバイスを変更せずにストアのチャートやリストを閲覧できます。 
- **App Store 地域** (**設定 → サードパーティ**) は、Apple の公式リダイレクト リンクを使用してデバイスの実際の App Store ストアフロントを切り替えるのに役立ちます。 これらは独立した設定です。 

### iCloud 同期の対象範囲は何ですか?

 **[設定] → [データ]** で個別に切り替えます:

 - **お気に入り** — 保存されたアプリ (地域ごと)、グループ、メモ、およびピンの状態。 タイムスタンプベースのマージ
 - **開発者のお気に入り** — 保存された開発者 (アーティスト + 地域ごと)。 **個別のトグル、デフォルトはオフ**
 - **サブスクリプション** — ウォッチリスト (オプション)
 - **フィルター プリセット** — ランク追跡プリセット (オプション)
 - **検索領域とクイック領域** — 検索デフォルトとクイック領域チップ (オプション)

 すべての同期は、iHTC Studio サーバーではなく、プライベート Apple アカウントの **iCloud** を通じて行われます。 

### どのようなサブスクリプション タイプがサポートされていますか?

 リージョンごとに 4 つのモニター:

| タイプ | の時計 |
 |------|---------------|
 | バージョン | 新しい App Store バージョン |
 | リスト | アプリがストアに登場 |
 | 上場廃止 | アプリがストアから削除されました |
 | **値下げ** | 価格がベースラインを下回ります。 オプションの目標価格および/またはドロップ率。 有料→無料は常にカウントされます |

 同じアプリ + リージョンに、異なるタイプの **複数のモニター**を含めることができます。 無料アプリでは価格下落監視を使用できません。 

### 価格下落の監視はどのように機能しますか?

 価格下落モニターを追加すると、iApp は**ベースライン価格**を記録します。 必要に応じて、**目標価格** および/または **最小ドロップ率** を設定できます (どちらの条件でもトリガー可能)。 両方が空のままの場合は、ベースラインからの減少によって監視が完了します。 サブスクリプション リストと **ライブ アクティビティ** には、ベースラインと現在の価格が表示されます。 

### サブスクリプションを一時停止できますか?

 はい。 アクティブなサブスクリプションのコンテキスト メニューを使用して **一時停止** します。つまり、ポーリングが停止し、ライブ アクティビティが終了します。 **再開** は即時チェックを実行し、ライブ アクティビティを再開できます。 一時停止された項目は、プルツーリフレッシュではチェックされません。 

### サブスクリプションをすぐに追加するにはどうすればよいですか?

**ランキング、検索、またはお気に入りでアプリの行を**長押し** → **サブスクリプションを追加**。 詳細ページまたは [サブスクリプション] タブから追加することもできます (バージョンのキーワード検索/モニターのリストから削除)。 

### 開発者のお気に入りは何ですか?

 **[設定] → [データ] → [開発者のお気に入り]** で開発者 (**アーティスト + 地域**別) を保存します。 アプリを開き、**ランキング別**のチャートの位置を表示し、エントリをピン留めし、必要に応じて **別の iCloud トグル** (デフォルトはオフ) を介して同期します。 詳細 **詳細** メニューまたは長押しコンテキスト メニューから追加します。 

### アプリ内購入の詳細リストには何が含まれていますか?

 折りたたみ可能な **アプリ内購入** セクションには、**現在の詳細リージョン** (名前、価格、サブスクリプション バッジ) の注目の IAP が表示されます。 これは、App Store の公開ページから読み込まれるため、App Store アプリの完全なカタログとは異なる場合があります。 読み込みに失敗した場合は、「更新」をタップします。 

### ファイル サイズが設定と異なるのはなぜですか?

 iApp では、バイナリ GiB ではなく、**App Store の小数単位** (1 GB = 1,000,000,000 バイト) を使用してアプリのサイズが表示され、App Store で表示されるものと一致します。 

### 同じアプリを複数の地域でお気に入りに登録できますか?

はい。 お気に入りは **アプリ ID および地域ごとに**保持されます。 中国と米国の同じアプリは、地域ラベルが付いた 2 つの別個のエントリとして表示されます。 

### お気に入りのアプリがリストから削除されたらどうなりますか?

 エントリは、**除外** ラベルとプレースホルダー アイコンとともにお気に入りに残ります。 詳細ページを開くことはできませんが、スワイプまたはコンテキスト メニューを使用してお気に入りを解除できます。 

### ランク追跡とは何ですか?

 **[設定] → [詳細設定]** のオプション機能。 有効にすると、iApp は **ドロップオフ レコード**を含むランク履歴をデバイスに保存します (チャート ビューごとに最大 90 エントリ)。 **トラッキング プリセット**を作成し、トラッキング ページで監視対象のアプリを管理し、**インタラクティブなランク チャート**を表示し (ドラッグしてスクラブします)、オプションで **ライブ アクティビティ**を表示します (iOS 16.2 以降)。 

### お気に入りの固定とランキングによる表示はどのように機能しますか?

 コンテキスト メニューまたはバッチ アクションからアプリを**ピン留め**します。 統合された並べ替えテーブル (コレクションの順序、名前、全体/カテゴリのランク、評価、価格) を表示するには、お気に入りフィルター メニューで **ランキング順** に切り替えます。 **他のリージョンを検索** を使用して、お気に入りのストア リージョンを再配置します。 

### アプリの言語を変更するにはどうすればよいですか?

**設定 → 外観 → 言語** — システムデフォルトまたは**18言語**のいずれか。UIは即座に更新され、ウィジェットや**Siri & ショートカット**のタイトル、説明、フレーズも同じ言語で**完全にローカライズ**されます。

### アプリアイコンを変更するには？

iPhone/iPadの場合: **設定 → 外観 → アプリアイコン** — **9種類の代替アイコン**から選択可能で、サムネイルプレビューとフルスクリーンプレビューが表示されます。Macは代替アイコンに対応していません。

### ウィジェットやライブアクティビティは自分のデバイスで使用できますか？

- **ホーム画面ウィジェット** — iOS 17.0以降（ランキング + マイフェイバリット; ピン留めされたフェイバリットが先に表示されます）
- **ライブアクティビティ — ランキング** — iOS 16.2以降（ランキング追跡のプリセット）
- **ライブアクティビティ — サブスクリプション** — iOS 16.2以降（個別のマスタートグル; サブスクリプションごと; 値下げ情報行を含む）
- ウィジェットはMacでは利用できません

### リンクやショートカットからiAppを開くことはできますか？

はい。 **`iapp://`** リンクでは、**アプリの詳細ページを開く**、**フィルタリングされたランキング ビューに戻る**、**タブを切り替える**、または**二次ページを開く** (開発者のお気に入り、閲覧履歴、ランク追跡、ライブ アクティビティ設定など) を行うことができます。 設定の**15**ホーム画面クイックアクションから最大**4**を選択します。 ウィジェットとライブ アクティビティは、タップするとこれらのリンクを生成します。 [ショートカット リンク](../url-scheme) を参照してください。 

### Siri とショートカットはどのように機能しますか?

 iOS 16 以降では、**ショートカット** アプリまたは **Siri** を使用して、アプリを検索したり、グラフを開いたり、お気に入りを追加したりできます。 アクション名と Siri フレーズは **18 のアプリ言語すべてにローカライズされています**。 日本語 *「iApp でアプリを検索」*; **設定 → 外観 → 言語** を切り替えるとフレーズが変わります。 

### iApp はオフラインでも動作しますか?

 ランキング、検索、レビュー、全地域チェック、IAP リストにはネットワーク アクセスが必要です。 最近閲覧したアプリには、保存された画像が引き続き表示される場合があります。 お気に入り、登録、ランキング履歴、検索履歴は **デバイスに保存されます**。 

### どのデバイスがサポートされていますか?

- **iPhone / iPad** — iOS 15.0以降（メインアプリ）；iOS 10.3以降（代替アイコン）；iOS 17.0以降（ウィジェット）；iOS 16.2以降（ライブアクティビティ）；iOS 16.0以降（Siri & ショートカット）；iOS 18.0以降（翻訳）
- **Mac** — macOS 11.0以降；**⌘1–⌘N** は表示されているタブに応じてタブを動的に切り替え（オプションでお気に入りタブや開発者お気に入りタブも含む）

### iAppはどうやって入手しますか？

[App Store](https://apps.apple.com/app/id6446581591) からダウンロードしてください。

### まだサポートが必要ですか？

**設定 → ヘルプ → 使い方の説明**（価格下落の方法を含む14件のFAQ）を開くか、[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) に連絡してください。通常、48時間以内に返信します。

</section>
<section lang="ko" markdown="1">

### Apple ID가 필요하거나 로그인해야 하나요?

아니요. iApp은 회원가입이나 로그인이 필요하지 않습니다. 기기에서 Apple ID를 변경하지 않고도 지원되는 모든 지역에서 순위를 살펴보고 앱을 검색할 수 있습니다.

### 데이터는 어디서 가져오나요?

스토어 목록, 검색 결과, 앱 상세 정보, 인앱 구매 목록은 **공개 App Store 데이터**에서 가져옵니다. 사용자 리뷰는 지역별로 표시됩니다. iApp은 공식 App Store 클라이언트가 아닌 서드파티 브라우저입니다.

### iApp에서 앱을 다운로드하거나 설치할 수 있나요?

아니요. iApp은 공개 스토어 정보만 표시합니다. 다운로드하거나 구매하려면 상세 화면에서 **App Store에서 열기** 또는 **앱 내 App Store 상품 페이지**를 사용하세요.

### iApp은 Apple과 관련이 있나요?

아니요. iApp은 iHTC Studio 기여자들이 만든 독립 도구입니다. Apple Inc.와 **관련이 없습니다.**

### 주요 탭은 무엇인가요?

기본값: **랭킹**, **검색**, **구독**, 그리고 **설정**. 선택적으로 **즐겨찾기**와 **개발자 즐겨찾기**를 별도의 탭으로 표시할 수 있으며, **설정 → 앱 설정**에서 탭 바에서 **구독**을 숨길 수 있습니다. 즐겨찾기는 항상 **설정 → 데이터 → 앱 즐겨찾기**에서 사용할 수 있으며, 개발자 즐겨찾기는 **설정 → 데이터 → 개발자 즐겨찾기**에서 사용할 수 있습니다.

### 앱 미리보기 비디오란?

앱 상세 페이지에서 iApp은 공식 **앱 스토어 미리보기 트레일러**(스트리밍 비디오)를 재생할 수 있습니다. 품질 변경, 음소거/음소거 해제, 링크 복사, 또는 **오디오와 함께 사진에 저장**할 수 있습니다. 저장하려면 사진 라이브러리 권한이 필요합니다. 미리보기 비디오는 네트워크 연결이 필요합니다.

### 지역 콘텐츠 비교란 무엇인가요?

**모든 지역 스토어 정보(All-region store info)**에서, 앱의 **설명(description)**, **업데이트 내역(release notes)**, **스크린샷(screenshots)**, **미리보기 동영상(preview videos)**을 기준 지역과 비교(diff)하려면 **콘텐츠 비교(Content compare)**로 전환하세요. 서로 다른 지역을 탭하면 오렌지색 하이라이트와 함께 나란히 보기(side-by-side view)가 나타납니다. 추가 필터를 사용하면 설명, 스크린샷, 또는 동영상의 차이를 쉽게 찾을 수 있습니다. 이 모드는 데이터를 더 많이 사용하므로 기본적으로 셀룰러 확인이 나타납니다. **콘텐츠 비교에서는 이미지 내보내기(image export)는 불가**하며, 내보내려면 리스트(list)나 그리드(grid)로 다시 전환하세요.

### 앱 탐색 기록(App Browse History)이란?

iApp은 사용자가 상세 페이지에서 연 앱(app + region, 최대 **100**개, 최신순)을 자동으로 기록합니다. **설정(Settings) → 데이터(Data) → 앱 탐색 기록(App Browse History)**에서 보기, 다시 열기, 스와이프하여 삭제, 또는 모두 지우기가 가능합니다. 이 기능은 **로컬 전용**이며 iCloud, 위젯, 다른 기기와 동기화되지 않습니다. **검색 기록(search history)**과는 별도입니다.

### 왜 홍콩(Hong Kong) / 대만(Taiwan) / 마카오(Macau)는 지역 선택기(region picker)에서 다르게 보이나요?

지역 **목록** 및 **검색**에는 더 명확한 이름이 표시됩니다(예: 중국어 간체의 전체 이름, 짧은 이름 + 다른 언어의 '(중국)'). **필터 칩** 및 저장된 지역 **코드**(`hk`, `tw`, `mo`)는 변경되지 않습니다. 딥 링크와 즐겨찾기는 여전히 동일한 코드를 사용합니다. 

### 리뷰가 로드되지 않거나 잘리지 않나요? 

전체 리뷰 페이지에서 **리뷰를 탭**하여 전체 텍스트를 펼치거나 접을 수 있습니다. iApp은 기본적으로 **개발자 답변과 함께 고객 리뷰**를 로드합니다(전체 별표 분석 포함). 해당 소스가 비어 있거나 실패하면 RSS 피드로 대체됩니다. 당겨서 새로 고치거나 세부 정보 페이지에서 수동 새로 고침을 사용하세요. 

### 리뷰의 개발자 답변이란 무엇인가요? 

개발자가 App Store의 사용자 리뷰에 응답하면 iApp은 전체 리뷰 페이지에서 해당 리뷰 아래에 **개발자 응답 인라인**을 표시합니다. 답변은 기본 고객 리뷰 소스와 함께 로드됩니다. 

### 앱 버전 기록이란 무엇인가요? 

앱 세부정보 페이지에서 **버전 기록**을 열어 현재 지역의 공개 App Store 카탈로그에서 가져온 이전 릴리스(버전 번호, 릴리스 날짜, 릴리스 노트)를 확인하세요. 

### 상세 페이지에 있는 동일 개발자 캐러셀은 무엇인가요?

기본 세부 콘텐츠 아래에 iApp은 동일한 개발자가 만든 다른 앱의 **수평 미리보기**를 표시합니다(App Store 스타일 캐러셀). 섹션 제목을 탭하면 정렬 및 순위별 보기가 포함된 전체 동일 개발자 목록이 열립니다. 

### 단일 앱 ID로 검색할 수 있나요? 

예. 검색에 하나의 숫자로 된 앱 ID(**6~12자리**, 쉼표 없음)를 입력하세요. ID가 여러 개인 경우 쉼표로 구분된 일괄 조회(최대 50개)를 사용하세요. 

### 개발자 즐겨찾기 탭은 어디에 있나요? 

**설정 → 앱 설정 → 탭 표시줄에 개발자 즐겨찾기 표시** (기본값 **꺼짐**) 활성화되면 탭이 즐겨찾기와 설정 사이에 위치합니다. 탭이 숨겨져 있으면 언제든지 **설정 → 데이터**에서 개발자 즐겨찾기를 열 수 있습니다. 

### 길게 누르기 메뉴의 개발자 하위 메뉴는 무엇인가요? 

개발자 홈페이지, 동일 개발자 앱, 개발자 즐겨찾기 저장/제거는 길게 누르기 메뉴의 **개발자** 아래에 그룹화되어 복잡해지지 않습니다. 

### 모바일 데이터 사용량 알림이란 무엇인가요? 

**셀룰러**에서 iApp은 트래픽이 많은 조회(모든 지역 비교, **콘텐츠 비교**, 즐겨찾기/개발자 순위별 보기) 전에 확인을 요청합니다. 기본값은 **켜짐**입니다. **설정 → 앱 설정**에서 비활성화하세요. 시트에서 '다시 알림 안 함'을 선택할 수 있습니다.

### 인앱 지역과 앱스토어 지역의 차이점은 무엇인가요? 

- **인앱 지역 필터**(순위, 검색, 세부 지역 전환기)를 사용하면 기기를 바꾸지 않고도 모든 매장의 차트와 목록을 탐색할 수 있습니다. 
- **App Store 지역**(**설정 → 타사**)은 Apple의 공식 리디렉션 링크를 사용하여 기기의 실제 App Store 스토어를 전환하는 데 도움이 됩니다. 이는 독립적인 설정입니다. 

### iCloud 동기화에는 어떤 내용이 포함되나요? 

**설정 → 데이터**에서 별도의 토글: 

- **즐겨찾기** — 저장된 앱(지역별), 그룹, 메모 및 핀 상태 타임스탬프 기반 병합 
- **개발자 즐겨찾기** — 저장된 개발자(아티스트별 + 지역별) **별도의 토글, 기본적으로 꺼짐** 
- **구독** — 관심 목록(선택 사항) 
- **필터 사전 설정** — 순위 추적 사전 설정(선택 사항) 
- **검색 지역 및 빠른 지역** — 검색 기본값 및 빠른 지역 칩(선택 사항) 

모든 동기화는 iHTC Studio 서버가 아닌 개인 Apple 계정의 **iCloud**를 통해 이루어집니다. 

### 어떤 구독 유형이 지원되나요? 

지역당 4개의 모니터:

| 유형 | 시계 | 
|------|-------------| 
| 버전 | 새로운 앱스토어 버전 | 
| 목록 | 앱이 스토어에 나타납니다 | 
| 상장폐지 | 앱이 스토어에서 제거됨 | 
| **가격인하** | 가격이 기준선 아래로 떨어집니다. 선택적 목표 가격 및/또는 하락율(%); 유료 → 무료는 항상 중요합니다 | 

동일한 앱 + 지역에는 다양한 유형의 **여러 모니터**가 있을 수 있습니다. 무료 앱은 가격 인하 모니터링을 사용할 수 없습니다. 

### 가격 하락 모니터링은 어떻게 작동하나요? 

가격 인하 모니터를 추가하면 iApp은 **기준 가격**을 기록합니다. 선택적으로 **목표 가격** 및/또는 **최소 하락 비율**을 설정할 수 있습니다(두 가지 조건 중 하나가 트리거될 수 있음). 둘 다 비어 있는 경우 기준선에서 감소하면 모니터가 완료됩니다. 구독 목록과 **실시간 활동**에는 기준 가격과 현재 가격이 표시됩니다. 

### 구독을 일시중지할 수 있나요? 

예. **일시 중지**에 대한 활성 구독의 상황에 맞는 메뉴를 사용하면 폴링이 중지되고 라이브 활동이 종료됩니다. **재개**는 즉시 확인을 실행하고 라이브 활동을 다시 시작할 수 있습니다. 일시 중지된 항목은 당겨서 새로 고칠 때 확인되지 않습니다. 

### 구독을 빠르게 추가하려면 어떻게 해야 하나요?

순위, 검색, 즐겨찾기에서 앱 행을 **길게 누르기** → **구독 추가**. 세부 정보 페이지 또는 구독 탭(버전/모니터 목록 삭제에 대한 키워드 검색)에서 추가할 수도 있습니다. 

### 개발자가 가장 좋아하는 것은 무엇입니까? 

**설정 → 데이터 → 개발자 즐겨찾기**에 개발자(**아티스트 + 지역별**)를 저장하세요. 앱을 열고 **순위별** 차트 위치를 확인하고 항목을 고정하고 선택적으로 **별도의 iCloud 토글**(기본값은 꺼짐)을 통해 동기화합니다. 세부 정보 **더보기** 메뉴 또는 길게 누르는 상황에 맞는 메뉴에서 추가하세요. 

### 세부 인앱 구매 목록에는 무엇이 있나요? 

축소 가능한 **인앱 구매** 섹션에는 **현재 세부 정보 영역**(이름, 가격, 구독 배지)에 대한 추천 IAP가 표시됩니다. 공개 App Store 페이지에서 로드되며 App Store 앱의 전체 카탈로그와 다를 수 있습니다. 로딩에 실패하면 새로고침을 탭하세요. 

### 파일 크기가 설정과 다르게 보이는 이유는 무엇인가요? 

iApp은 바이너리 GiB가 아닌 App Store에 표시되는 것과 일치하는 **App Store 십진 단위**(1GB = 1,000,000,000바이트)를 사용하여 앱 크기를 표시합니다. 

### 동일한 앱을 여러 지역에서 즐겨찾기에 추가할 수 있나요?

예. 즐겨찾기는 **앱 ID 및 지역**별로 보관됩니다. 중국과 미국의 동일한 앱은 지역 라벨이 있는 두 개의 별도 항목으로 표시됩니다. 

### 즐겨찾는 앱이 삭제되면 어떻게 되나요? 

항목은 **삭제됨** 라벨과 자리 표시자 아이콘과 함께 즐겨찾기에 유지됩니다. 세부정보 페이지를 열 수는 없지만 스와이프나 컨텍스트 메뉴를 통해 즐겨찾기를 취소할 수 있습니다. 

### 순위 추적이란 무엇입니까? 

**설정 → 고급**의 선택 기능입니다. 활성화되면 iApp은 **탈락 기록**을 포함하여 순위 기록을 기기에 저장합니다(차트 보기당 최대 90개 항목). **추적 사전 설정** 생성, 추적 페이지에서 시청 중인 앱 관리, **대화형 순위 차트** 보기(드래그하여 스크러빙), 선택적으로 **실시간 활동** 표시(iOS 16.2+). 

### 즐겨찾기 고정 및 순위별 보기는 어떻게 작동하나요? 

컨텍스트 메뉴 또는 일괄 작업에서 앱을 **고정**하세요. 통일된 정렬표(컬렉션 순서, 이름, 전체/카테고리 순위, 평점, 가격)를 보려면 즐겨찾기 필터 메뉴에서 **순위별**으로 전환하세요. 즐겨찾는 매장 지역을 재배치하려면 **다른 지역 찾기**를 사용하세요. 

### 앱 언어는 어떻게 변경하나요?

**설정 → 외관 → 언어** — 시스템 기본값 또는 **18개 언어** 중 선택. UI가 즉시 새로 고쳐지며, 위젯과 **시리 & 단축어**의 제목, 설명, 문구가 같은 언어로 **완전히 현지화**됩니다.

### 앱 아이콘을 어떻게 변경하나요?

iPhone/iPad에서: **설정 → 외관 → 앱 아이콘** — **9개의 대체 아이콘** 중에서 축소판 미리보기와 전체 화면 미리보기를 통해 선택. Mac에서는 대체 아이콘을 지원하지 않습니다.

### 내 기기에서 위젯과 실시간 활동이 작동하나요?

- **홈 화면 위젯** — iOS 17.0 이상 (랭킹 + 즐겨찾기; 고정한 즐겨찾기 우선)
- **실시간 활동 — 랭킹** — iOS 16.2 이상 (랭킹 추적 사전 설정)
- **실시간 활동 — 구독** — iOS 16.2 이상 (별도의 마스터 토글; 구독별; 가격 하락 표시 포함)
- Mac에서는 위젯을 사용할 수 없습니다

### 링크나 단축어를 통해 iApp을 열 수 있나요?

예. **_`iapp://`** 링크는 **앱 세부정보 페이지 열기**, **필터링된 순위 보기로 돌아가기**, **탭 전환** 또는 **보조 페이지 열기**(개발자 즐겨찾기, 검색 기록, 순위 추적, 실시간 활동 설정 등)를 수행할 수 있습니다. 설정의 홈 화면 빠른 작업 **15**개 중 최대 **4**개를 선택하세요. 위젯과 실시간 활동은 탭할 때 이러한 링크를 생성합니다. [바로가기 링크](../url-scheme)를 참조하세요. 

### Siri와 단축어는 어떻게 작동하나요? 

iOS 16 이상에서는 **단축키** 앱 또는 **Siri**를 통해 앱을 검색하고 차트를 열거나 즐겨찾기를 추가할 수 있습니다. 작업 이름과 Siri 문구는 **18개 앱 언어로 모두 현지화**됩니다. 영어 *"iApp에서 앱 검색"*; **설정 → 모양 → 언어**를 전환하면 문구가 변경됩니다. 

### iApp은 오프라인에서도 작동하나요? 

순위, 검색, 리뷰, 전체 지역 확인, IAP 목록에는 네트워크 액세스가 필요합니다. 최근에 본 앱에는 저장된 이미지가 계속 표시될 수 있습니다. 즐겨찾기, 구독, 순위 기록, 검색 기록이 **기기에 저장됩니다**. 

### 어떤 기기가 지원되나요?

- **iPhone / iPad** — iOS 15.0 이상 (메인 앱); iOS 10.3 이상 (대체 아이콘); iOS 17.0 이상 (위젯); iOS 16.2 이상 (라이브 액티비티); iOS 16.0 이상 (시리 & 단축어); iOS 18.0 이상 (번역)
- **Mac** — macOS 11.0 이상; **⌘1–⌘N** 현재 보이는 탭에 따라 동적으로 탭 전환 (선택적 즐겨찾기 및 개발자 즐겨찾기 탭 포함)

### iApp을 어떻게 얻나요?

[앱 스토어](https://apps.apple.com/app/id6446581591)에서 다운로드하세요.

### 여전히 도움이 필요하신가요?

**설정 → 도움말 → 사용 방법**을 열어보세요 (가격 인하 방법을 포함한 FAQ 14개 항목) 또는 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)로 연락하세요. 일반적으로 48시간 이내에 답변 드립니다.

</section>
<section lang="ru" markdown="1">

### Мне нужен Apple ID или вход в систему?

Нет. iApp не требует регистрации или входа. Вы можете просматривать рейтинги и искать приложения в любом поддерживаемом регионе без смены Apple ID на устройстве.

### Откуда берутся данные?

Списки магазинов, результаты поиска, сведения о приложениях и списки покупок внутри приложений берутся из **публичных данных App Store**. Пользовательские отзывы отображаются по регионам. iApp является сторонним браузером, а не официальным клиентом App Store.

### Могу ли я загружать или устанавливать приложения через iApp?

Нет. iApp отображает только публичную информацию магазина. Для загрузки или покупки используйте **Открыть в App Store** или страницу продукта App Store внутри приложения на экране сведений.

### Является ли iApp аффилированным с Apple?

Нет. iApp — это независимый инструмент, созданный участниками iHTC Studio. Он **не аффилирован с Apple Inc.**

### Какие основные вкладки?

По умолчанию: **Рейтинги**, **Поиск**, **Подписки** и **Настройки**. По желанию вы можете показывать **Избранное** и **Избранное разработчика** как отдельные вкладки, а **Подписки** скрывать с панели вкладок в **Настройки → Настройки приложения**. Избранное всегда доступно через **Настройки → Данные → Избранное приложения**; избранное разработчика — через **Настройки → Данные → Избранное разработчика**.

### Что такое видео-превью приложений?

На странице с деталями приложения iApp может воспроизводить официальные **трейлеры-превью App Store** (стриминговое видео). Вы можете переключать качество, включать/выключать звук, копировать ссылку или **сохранять в Фото с аудио**. Для сохранения требуется разрешение на доступ к фототеке. Для просмотра превью видео требуется подключение к сети.

### Что такое сравнение регионального контента?

В **Информации о магазине для всех регионов** переключитесь на **Сравнение контента**, чтобы сравнить **описание** приложения, **примечания к выпуску**, **скриншоты** и **видео-превью** с эталонным регионом. Нажмите на регион с отличиями для просмотра бок о бок с оранжевыми выделениями. Дополнительные фильтры помогут найти различия в описании, скриншотах или видео. Этот режим использует больше данных — по умолчанию появляется подтверждение при использовании мобильной сети. **Экспорт изображений недоступен** в режиме сравнения контента; чтобы экспортировать, переключитесь обратно на список или сетку.

### Что такое история просмотра приложений?

iApp автоматически записывает приложения, которые вы открываете на странице с деталями (приложение + регион, до **100** записей, сначала самые новые). Просматривайте, повторно открывайте, смахивайте для удаления или очищайте все в **Настройки → Данные → История просмотра приложений**. Это **только локально** — не синхронизируется через iCloud, виджеты или другие устройства. Она отделена от **истории поиска**.

### Почему Гонконг / Тайвань / Макао выглядят иначе в выборе региона?

В **списках** и **поиске** регионов отображаются более понятные названия (например, полное имя на упрощенном китайском языке, короткое имя + «(Китай)» на других языках). **Чипы фильтров** и **коды хранимых регионов** (`hk`, `tw`, `mo`) не изменились — глубокие ссылки и избранное по-прежнему используют одни и те же коды. 

### Отзывы не загружаются или обрезаны? 

На странице полных отзывов **нажмите на отзыв**, чтобы развернуть или свернуть полный текст. iApp по умолчанию загружает **отзывы клиентов с ответами разработчиков** (включая разбивку по всем звездам); если этот источник пуст или не работает, он возвращается к каналу RSS — потяните, чтобы обновить, или используйте обновление вручную на странице сведений. 

### Что такое ответы разработчиков в обзорах? 

Когда разработчик отвечает на отзыв пользователя в App Store, iApp отображает **встроенный ответ разработчика** под этим отзывом на странице полных отзывов. Ответы загружаются вместе с основным источником отзывов клиентов. 

### Что такое история версий приложения? 

На странице сведений о приложении откройте **История версий**, чтобы просмотреть предыдущие выпуски (номер версии, дату выпуска и примечания к выпуску), полученные из общедоступного каталога App Store для текущего региона. 

### Что такое карусель разработчиков на странице сведений?

Под основной информацией iApp показывает **горизонтальный предварительный просмотр** других приложений того же разработчика (карусель в стиле App Store). Коснитесь заголовка раздела, чтобы открыть полный список разработчиков с сортировкой и ранжированием. 

### Могу ли я выполнить поиск по одному идентификатору приложения? 

Да. В поле «Поиск» введите один цифровой идентификатор приложения (**6–12 цифр** без запятой). Для нескольких идентификаторов используйте пакетный поиск, разделенный запятыми (до 50). 

### Где находится вкладка «Избранное разработчика»? 

**Настройки → Настройки приложения → Показывать избранное разработчика на панели вкладок** (по умолчанию **выключено**). Если эта опция включена, вкладка находится между «Избранным» и «Настройки». Вы всегда можете открыть избранное разработчика в меню **Настройки → Данные**, когда вкладка скрыта. 

### Что такое подменю «Разработчик» в меню длительного нажатия? 

Домашняя страница разработчика, приложения того же разработчика и сохранение/удаление избранного разработчика сгруппированы в разделе **Разработчик** в меню длительного нажатия, чтобы уменьшить беспорядок. 

### Что такое оповещение об использовании мобильных данных? 

На **сотовой связи** iApp запрашивает подтверждение перед поиском с высоким трафиком (сравнение всех регионов, **сравнение контента**, просмотры избранного/разработчика по рейтингу). По умолчанию **включено**; отключить в **Настройки → Настройки приложения**. Вы можете выбрать «Больше не напоминать» на листе.

### В чем разница между регионом приложения и регионом App Store? 

- **Фильтры регионов в приложении** (рейтинги, поиск, подробный переключатель региона) позволяют просматривать диаграммы и списки любых магазинов, не меняя устройство. 
- **Регион App Store** (**Настройки → Сторонние**) позволяет переключить фактическую витрину App Store вашего устройства с помощью официальной ссылки перенаправления Apple. Это независимые настройки. 

### Что включает в себя синхронизация iCloud? 

Отдельные переключатели в **Настройки → Данные**: 

- **Избранное** — сохраненные приложения (для каждого региона), группы, заметки и состояние закрепления; слияние на основе временных меток 
- **Избранное разработчика** — сохраненные разработчики (для каждого исполнителя + регион); **отдельный переключатель, по умолчанию выключен** 
- **Подписки** — ваш список наблюдения (необязательно). 
- **Наборы фильтров** — настройки отслеживания рангов (необязательно). 
- **Регион поиска и быстрые регионы** — параметры поиска по умолчанию и чипы быстрого региона (необязательно). 

Все синхронизируется через **iCloud** в вашей личной учетной записи Apple, а не на серверах iHTC Studio. 

### Какие типы подписок поддерживаются? 

Четыре монитора на регион:

| Тип | Часы для | 
|------|-------------| 
| Версия | Новая версия App Store | 
| Листинг | Приложение появляется в магазине | 
| Исключение из листинга | Приложение удалено из магазина | 
| **Снижение цен** | Цена падает ниже базовой линии; необязательная целевая цена и/или процент падения; платно → бесплатно всегда имеет значение | 

В одном и том же приложении и регионе может быть **несколько мониторов** разных типов. Бесплатные приложения не могут использовать мониторинг падения цен. 

### Как работает мониторинг падения цен? 

Когда вы добавляете монитор падения цен, iApp записывает **базовую цену**. При желании вы можете установить **целевую цену** и/или **минимальный процент падения** (любое условие может сработать). Если оба значения оставлены пустыми, любое снижение по сравнению с базовым уровнем завершает мониторинг. Список подписок и **Активность в реальном времени** отображают базовую цену и текущую цену. 

### Могу ли я приостановить подписку? 

Да. Используйте контекстное меню любой активной подписки, чтобы **Пауза** — опрос останавливается, и его активная активность завершается. **Возобновить** запускает немедленную проверку и может перезапустить Live Activity. Приостановленные элементы не проверяются при обновлении. 

### Как быстро добавить подписку?

**Длительное нажатие** любой строки приложения в разделе «Рейтинги», «Поиск» или «Избранное» → **Добавить подписку**. Вы также можете добавить информацию со страницы сведений или на вкладке «Подписки» (поиск по ключевым словам для версии/исключение мониторов). 

### Что нравится разработчикам? 

Сохраните разработчика (по **исполнителю + региону**) в **Настройки → Данные → Избранное разработчика**. Открывайте их приложения, просматривайте позиции в диаграммах **по рейтингу**, закрепляйте записи и при необходимости синхронизируйте их с помощью **отдельного переключателя iCloud** (по умолчанию отключено). Добавьте из подробного меню **Дополнительно** или контекстного меню при длительном нажатии. 

### Что находится в подробном списке покупок в приложении? 

В сворачиваемом разделе **Покупки в приложении** показаны избранные IAP для **текущего подробного региона** (название, цена, значок подписки). Он загружается с общедоступных страниц App Store и может отличаться от полного каталога в приложении App Store. Нажмите «Обновить», если загрузка не удалась. 

### Почему размер файла отличается от настроек? 

iApp отображает размер приложения в **десятичных единицах App Store** (1 ГБ = 1 000 000 000 байт), что соответствует тому, что вы видите в App Store, а не в двоичных ГиБ. 

### Может ли одно и то же приложение быть добавлено в избранное в нескольких регионах?

Да. Избранное сохраняется **по идентификатору приложения и региону**. Одно и то же приложение в Китае и США отображается как две отдельные записи с метками регионов. 

### Что произойдет, если избранное приложение будет исключено из списка? 

Запись останется в избранном с пометкой **Исключено** и значком-заполнителем. Вы не можете открыть страницу сведений о нем, но можете удалить его из избранного, проведя пальцем по экрану или контекстное меню. 

### Что такое отслеживание рейтинга? 

Дополнительная функция в **Настройки → Дополнительно**. Если эта функция включена, iApp сохраняет историю рейтингов на вашем устройстве (до 90 записей в каждом представлении диаграммы), включая **записи выпадения**. Создавайте **настройки отслеживания**, управляйте просмотренными приложениями на странице отслеживания, просматривайте **интерактивные диаграммы рейтингов** (перетаскивайте их для пролистывания) и при необходимости отображайте **Активность в реальном времени** (iOS 16.2+). 

### Как работает закрепление избранного и просмотр по рейтингу? 

**Закрепляйте** приложения из контекстного меню или пакетных действий. Переключитесь на **По рейтингу** в меню фильтра избранного, чтобы получить единую таблицу сортировки (порядок сбора, имя, общий рейтинг/категория, рейтинг, цена). Используйте **Найти другой регион**, чтобы переместить регион избранного магазина. 

### Как изменить язык приложения?

**Настройки → Внешний вид → Язык** — Системный по умолчанию или любой из **18 языков**. Интерфейс обновляется мгновенно; виджеты и названия, описания и фразы **Siri & Shortcuts** полностью локализованы на этом языке.

### Как изменить иконку приложения?

На iPhone/iPad: **Настройки → Внешний вид → Иконка приложения** — выберите из **9 альтернативных иконок** с миниатюрным и полноэкранным предпросмотром. Mac не поддерживает альтернативные иконки.

### Работают ли виджеты и Live Activity на моем устройстве?

- **Виджеты на главном экране** — iOS 17.0+ (Рейтинги + Мои любимые; закрепленные избранные отображаются первыми)
- **Live Activity — Рейтинги** — iOS 16.2+ (предустановки отслеживания рейтинга)
- **Live Activity — Подписки** — iOS 16.2+ (отдельный общий переключатель; для каждой подписки; включает строку с изменением цены)
- Виджеты недоступны на Mac

### Могу ли я открыть iApp по ссылке или ярлыку?

Да. Ссылки **`iapp://`** позволяют **открыть страницу сведений о приложении**, **возвратиться к отфильтрованному представлению рейтингов**, **переключить вкладки** или **открыть дополнительные страницы** (избранное разработчиков, историю просмотров, отслеживание рейтингов, настройки активности в реальном времени и т. д.). Выберите до **4** из **15** быстрых действий на главном экране в настройках. Виджеты и интерактивная активность генерируют эти ссылки при нажатии. См. [Быстрые ссылки](../url-scheme). 

### Как работают Siri и ярлыки? 

На iOS 16+ ищите приложения, открывайте диаграммы или добавляйте их в избранное с помощью приложения **Ярлыки** или **Siri**. Названия действий и фразы Siri **локализованы на все 18 языков приложения** — например. Английский *"Поиск приложений в iApp"*; фразы меняются при переключении **Настройки → Внешний вид → Язык**. 

### Работает ли iApp в автономном режиме? 

Рейтинги, поиск, обзоры, проверки по всем регионам и списки IAP требуют доступа к сети. Недавно просмотренные приложения могут по-прежнему отображать сохраненные изображения. Избранное, подписки, история рейтингов и история поиска **сохраняются на вашем устройстве**. 

### Какие устройства поддерживаются?

- **iPhone / iPad** — iOS 15.0+ (основное приложение); iOS 10.3+ (альтернативные иконки); iOS 17.0+ (виджеты); iOS 16.2+ (Live Activity); iOS 16.0+ (Siri и ярлыки); iOS 18.0+ (перевод)
- **Mac** — macOS 11.0+; **⌘1–⌘N** переключение вкладок динамически в зависимости от видимых вкладок (включая опциональные вкладки «Избранное» и «Избранное разработчика»)

### Как получить iApp?

Скачайте из [App Store](https://apps.apple.com/app/id6446581591).

### Всё ещё нужна помощь?

Откройте **Настройки → Помощь → Инструкции по использованию** (14 часто задаваемых вопросов, включая инструкции по снижению цены) или свяжитесь с [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com). Обычно мы отвечаем в течение 48 часов.

</section>
<section lang="th" markdown="1">

### ฉันจำเป็นต้องมี Apple ID หรือเข้าสู่ระบบหรือไม่?

ไม่จำเป็น iApp ไม่ต้องการการลงทะเบียนหรือล็อกอิน คุณสามารถเรียกดูอันดับและค้นหาแอปในทุกภูมิภาคที่สนับสนุนได้โดยไม่ต้องเปลี่ยน Apple ID บนอุปกรณ์

### ข้อมูลมาจากที่ไหน?

รายการในร้านค้า ผลการค้นหา รายละเอียดแอป และรายการการซื้อภายในแอปมาจาก **ข้อมูล App Store สาธารณะ** รีวิวของผู้ใช้จะแสดงตามภูมิภาค iApp เป็นเบราว์เซอร์ของบุคคลที่สาม — ไม่ใช่ลูกค้า App Store อย่างเป็นทางการ

### ฉันสามารถดาวน์โหลดหรือติดตั้งแอปจาก iApp ได้หรือไม่?

ไม่ได้ iApp จะแสดงเฉพาะข้อมูลสาธารณะของร้านค้าเท่านั้น หากต้องการดาวน์โหลดหรือซื้อ ให้ใช้ **เปิดใน App Store** หรือ **หน้าผลิตภัณฑ์ใน App Store ภายในแอป** บนหน้ารายละเอียด

### iApp มีความเกี่ยวข้องกับ Apple หรือไม่?

ไม่ iApp เป็นเครื่องมืออิสระที่สร้างโดยผู้ร่วมงานจาก iHTC Studio และ **ไม่เกี่ยวข้องกับ Apple Inc.**

### แท็บหลักมีอะไรบ้าง?

โดยค่าเริ่มต้น: **อันดับ**, **ค้นหา**, **การสมัครสมาชิก**, และ **การตั้งค่า** คุณสามารถเลือกที่จะแสดง **รายการโปรด** และ **รายการโปรดของนักพัฒนา** เป็นแท็บของตัวเอง และซ่อน **การสมัครสมาชิก** จากแถบแท็บใน **การตั้งค่า → การตั้งค่าแอป** รายการโปรดสามารถเข้าถึงได้ตลอดเวลาจาก **การตั้งค่า → ข้อมูล → รายการโปรดของแอป**; รายการโปรดของนักพัฒนาจาก **การตั้งค่า → ข้อมูล → รายการโปรดของนักพัฒนา**

### วิดีโอตัวอย่างแอปคืออะไร?

ในหน้ารายละเอียดแอป, iApp สามารถเล่น **ตัวอย่างเทรลเลอร์อย่างเป็นทางการของ App Store** (วิดีโอสตรีม) คุณสามารถสลับคุณภาพ, ปิด/เปิดเสียง, คัดลอกลิงก์, หรือ **บันทึกลงในรูปภาพพร้อมเสียง** การบันทึกต้องมีสิทธิ์การเข้าถึงคลังรูปภาพ วิดีโอตัวอย่างต้องการการเชื่อมต่อเครือข่าย

### การเปรียบเทียบเนื้อหาในภูมิภาคคืออะไร?

ใน **ข้อมูลร้านค้าแบบทุกภูมิภาค** ให้สลับไปที่ **เปรียบเทียบเนื้อหา** เพื่อเปรียบเทียบ **คำอธิบาย**, **บันทึกการอัปเดต**, **สกรีนช็อต**, และ **วิดีโอพรีวิว** ของแอปกับภูมิภาคมาตรฐาน แตะภูมิภาคที่แตกต่างเพื่อดูแบบข้างเคียงพร้อมไฮไลท์สีส้ม ตัวกรองเพิ่มเติมช่วยให้คุณค้นหาความแตกต่างของคำอธิบาย, สกรีนช็อต, หรือวิดีโอ โหมดนี้ใช้ข้อมูลมากขึ้น — โดยค่าเริ่มต้นจะมีการยืนยันผ่านเครือข่ายมือถือ **การส่งออกภาพไม่สามารถใช้ได้** ในการเปรียบเทียบเนื้อหา; ให้สลับกลับไปที่รายการหรือตารางเพื่อส่งออก

### ประวัติการเรียกดูแอปคืออะไร?

iApp จะบันทึกแอปที่คุณเปิดในหน้ารายละเอียดโดยอัตโนมัติ (แอป + ภูมิภาค สูงสุด **100** รายการ เรียงลำดับจากล่าสุดไปก่อน) ดู, เปิดซ้ำ, ปัดเพื่อลบ, หรือเคลียร์ทั้งหมดได้ที่ **การตั้งค่า → ข้อมูล → ประวัติการเรียกดูแอป** ซึ่งจะ **จำกัดเฉพาะเครื่องเท่านั้น** — ไม่ซิงค์ผ่าน iCloud, วิดเจ็ต, หรืออุปกรณ์อื่น เป็นข้อมูลแยกจาก **ประวัติการค้นหา**

### ทำไมฮ่องกง / ไต้หวัน / มาเก๊าถึงดูแตกต่างในตัวเลือกภูมิภาค?

ภูมิภาค **รายการ** และ **การค้นหา** แสดงชื่อที่ชัดเจนยิ่งขึ้น (เช่น ชื่อเต็มในภาษาจีนตัวย่อ ชื่อสั้น + “(จีน)” ในภาษาอื่น) **ชิปตัวกรอง** และภูมิภาคที่เก็บไว้ **รหัส** (`hk`, `tw`, `mo`) ไม่มีการเปลี่ยนแปลง — ลิงก์ในรายละเอียดและรายการโปรดยังคงใช้รหัสเดียวกัน 

### บทวิจารณ์ไม่โหลดหรือถูกตัดทอน? 

ในหน้าบทวิจารณ์ฉบับเต็ม **แตะบทวิจารณ์** เพื่อขยายหรือยุบข้อความทั้งหมด iApp โหลด **บทวิจารณ์ของลูกค้าพร้อมการตอบกลับของนักพัฒนา** โดยค่าเริ่มต้น (รวมการแบ่งดาวทั้งหมดด้วย) หากแหล่งข้อมูลนั้นว่างเปล่าหรือล้มเหลว แหล่งข้อมูลนั้นจะกลับไปที่ฟีด RSS — ดึงเพื่อรีเฟรชหรือใช้การรีเฟรชด้วยตนเองในหน้ารายละเอียด 

### นักพัฒนาซอฟต์แวร์ตอบกลับในรีวิวอย่างไร 

เมื่อนักพัฒนาตอบรีวิวของผู้ใช้บน App Store iApp จะแสดง **การตอบกลับของนักพัฒนาในบรรทัด** ใต้รีวิวนั้นในหน้ารีวิวฉบับเต็ม โหลดคำตอบพร้อมกับแหล่งรีวิวจากลูกค้าหลัก 

### ประวัติเวอร์ชันของแอปคืออะไร? 

ในหน้ารายละเอียดแอป ให้เปิด **ประวัติเวอร์ชัน** เพื่อดูรุ่นที่ผ่านมา — หมายเลขเวอร์ชัน วันที่วางจำหน่าย และบันทึกประจำรุ่น — ที่ดึงมาจากแค็ตตาล็อก App Store สาธารณะสำหรับภูมิภาคปัจจุบัน 

### ภาพหมุนของนักพัฒนาคนเดียวกันในหน้ารายละเอียดคืออะไร

ด้านล่างเนื้อหารายละเอียดหลัก iApp จะแสดง **ตัวอย่างแนวนอน** ของแอพอื่นๆ โดยนักพัฒนาคนเดียวกัน (แบบหมุนสไตล์ App Store) แตะชื่อส่วนเพื่อเปิดรายชื่อนักพัฒนารายเดียวกันทั้งหมดพร้อมมุมมองการเรียงลำดับและตามอันดับ 

### ฉันสามารถค้นหา App ID เดียวได้หรือไม่ 

ใช่. ในการค้นหา ให้ป้อนรหัสแอปที่เป็นตัวเลขหนึ่งตัว (**6–12 หลัก** โดยไม่มีเครื่องหมายจุลภาค) สำหรับหลาย ID ให้ใช้การค้นหาแบบกลุ่มโดยคั่นด้วยเครื่องหมายจุลภาค (สูงสุด 50) 

### แท็บรายการโปรดของนักพัฒนาอยู่ที่ไหน 

**การตั้งค่า → การตั้งค่าแอพ → แสดงรายการโปรดของนักพัฒนาในแถบแท็บ** (ค่าเริ่มต้น **ปิด**) เมื่อเปิดใช้งาน แท็บจะอยู่ระหว่างรายการโปรดและการตั้งค่า คุณสามารถเปิดรายการโปรดของนักพัฒนาได้ตลอดเวลาจาก **การตั้งค่า → ข้อมูล** เมื่อแท็บถูกซ่อนอยู่ 

### เมนูย่อยของนักพัฒนาในเมนูแบบกดยาวคืออะไร? 

หน้าแรกของนักพัฒนา แอปของนักพัฒนาคนเดียวกัน และบันทึก/ลบรายการโปรดของนักพัฒนาจะถูกจัดกลุ่มไว้ภายใต้ **นักพัฒนา** ในเมนูกดแบบยาวเพื่อลดความยุ่งเหยิง 

### การแจ้งเตือนการใช้ข้อมูลมือถือคืออะไร? 

บน **มือถือ** iApp จะขอการยืนยันก่อนการค้นหาที่มีการเข้าชมสูง (การเปรียบเทียบทุกภูมิภาค **การเปรียบเทียบเนื้อหา** การดูรายการโปรด/นักพัฒนาตามอันดับ) ค่าเริ่มต้นคือ **เปิด**; ปิดการใช้งานใน **การตั้งค่า → การตั้งค่าแอพ** คุณสามารถเลือก "ไม่ต้องเตือนอีกครั้ง" ในชีตได้

### ภูมิภาคในแอปและภูมิภาค App Store แตกต่างกันอย่างไร 

- **ตัวกรองภูมิภาคในแอป** (อันดับ การค้นหา ตัวสลับขอบเขตรายละเอียด) ช่วยให้คุณสามารถเรียกดูแผนภูมิและรายการของร้านค้าโดยไม่ต้องเปลี่ยนอุปกรณ์ของคุณ 
- **ภูมิภาค App Store** (**การตั้งค่า → บุคคลที่สาม**) ช่วยสลับหน้าร้าน App Store ที่แท้จริงของอุปกรณ์ของคุณโดยใช้ลิงก์เปลี่ยนเส้นทางอย่างเป็นทางการของ Apple สิ่งเหล่านี้เป็นการตั้งค่าที่เป็นอิสระ 

### iCloud Sync ครอบคลุมอะไรบ้าง? 

แยกการสลับใน **การตั้งค่า → ข้อมูล**: 

- **รายการโปรด** — แอปที่บันทึกไว้ (ตามภูมิภาค) กลุ่ม โน้ต และสถานะหมุด การผสานตามการประทับเวลา 
- **รายการโปรดของนักพัฒนา** — นักพัฒนาที่บันทึกไว้ (ต่อศิลปิน + ภูมิภาค) **สลับแยก ปิดค่าเริ่มต้น** 
- **การสมัครสมาชิก** — รายการเฝ้าดูของคุณ (ไม่บังคับ) 
- **ค่าที่ตั้งไว้ล่วงหน้าของตัวกรอง** — ค่าที่ตั้งล่วงหน้าสำหรับการติดตามอันดับ (ไม่บังคับ) 
- **ค้นหาภูมิภาคและภูมิภาคด่วน** — ค่าเริ่มต้นการค้นหาและชิปภูมิภาคด่วน (ไม่บังคับ) 

ซิงค์ทั้งหมดผ่าน **iCloud** บนบัญชี Apple ส่วนตัวของคุณ ไม่ใช่เซิร์ฟเวอร์ iHTC Studio 

### รองรับการสมัครสมาชิกประเภทใด? 

สี่จอภาพต่อภูมิภาค:

| พิมพ์ | นาฬิกาสำหรับ | 
|-|-------------| 
| เวอร์ชั่น | ใหม่ App Store เวอร์ชัน | 
| รายการ | แอพปรากฏในร้านค้า | 
| การเพิกถอน | แอพถูกลบออกจากร้านค้า | 
| **ลดราคา** | ราคาตกลงต่ำกว่าเส้นพื้นฐาน ราคาเป้าหมายเพิ่มเติมและ/หรือลดลง %; จ่าย → ฟรี นับ | เสมอ 

แอป + ภูมิภาคเดียวกันสามารถมี **หลายจอภาพ** ในประเภทที่แตกต่างกันได้ แอปฟรีไม่สามารถใช้การตรวจสอบการลดราคาได้ 

### การตรวจสอบการลดราคาทำงานอย่างไร? 

เมื่อคุณเพิ่มตัวตรวจสอบการลดราคา iApp จะบันทึก **ราคาพื้นฐาน** คุณสามารถเลือกกำหนด **ราคาเป้าหมาย** และ/หรือ **เปอร์เซ็นต์การลดลงขั้นต่ำ** ได้ (เงื่อนไขใดเงื่อนไขหนึ่งก็สามารถทริกเกอร์ได้) หากปล่อยว่างทั้งสองรายการ การลดลงจากพื้นฐานจะทำให้จอภาพสมบูรณ์ รายการสมัครรับข้อมูลและ **กิจกรรมสด** แสดงข้อมูลพื้นฐานเทียบกับราคาปัจจุบัน 

### ฉันสามารถหยุดการสมัครชั่วคราวได้หรือไม่? 

ใช่. ใช้เมนูบริบทในการสมัครรับข้อมูลที่ใช้งานอยู่เพื่อ **หยุดชั่วคราว** — การโพลหยุดและกิจกรรมสดสิ้นสุดลง **ดำเนินการต่อ** จะทำการตรวจสอบทันทีและสามารถรีสตาร์ท Live Activity ได้ รายการที่หยุดชั่วคราวจะไม่ถูกตรวจสอบเมื่อดึงเพื่อรีเฟรช 

### ฉันจะเพิ่มการสมัครสมาชิกอย่างรวดเร็วได้อย่างไร?

**กดค้างไว้** แถวแอปใดก็ได้ในการจัดอันดับ การค้นหา หรือรายการโปรด → **เพิ่มการสมัครรับข้อมูล** คุณยังสามารถเพิ่มจากหน้ารายละเอียดหรือแท็บการสมัครสมาชิก (การค้นหาคำสำคัญสำหรับการตรวจสอบเวอร์ชัน/การลบออก) 

### รายการโปรดของนักพัฒนาคืออะไร? 

บันทึกนักพัฒนา (โดย **ศิลปิน + ภูมิภาค**) ใน **การตั้งค่า → ข้อมูล → รายการโปรดของนักพัฒนา** เปิดแอป ดูตำแหน่งแผนภูมิ **ตามอันดับ** ปักหมุดรายการ และเลือกซิงค์ผ่าน **สลับ iCloud แยกต่างหาก** (ปิดค่าเริ่มต้น) เพิ่มจากเมนูรายละเอียด **เพิ่มเติม** หรือเมนูบริบทแบบกดค้าง 

### รายการซื้อในรายละเอียดในแอปมีรายละเอียดอะไรบ้าง? 

ส่วน **การซื้อในแอป** ที่ยุบได้จะแสดง IAP ที่แนะนำสำหรับ **ภูมิภาครายละเอียดปัจจุบัน** (ชื่อ ราคา ป้ายสถานะการสมัครสมาชิก) โหลดจากหน้า App Store สาธารณะ และอาจแตกต่างจากแค็ตตาล็อกทั้งหมดในแอพ App Store แตะรีเฟรชหากการโหลดล้มเหลว 

### ทำไมขนาดไฟล์จึงดูแตกต่างจากการตั้งค่า? 

iApp แสดงขนาดแอพโดยใช้ **หน่วยทศนิยมของ App Store** (1 GB = 1,000,000,000 ไบต์) ซึ่งตรงกับสิ่งที่คุณเห็นใน App Store ไม่ใช่ GiB ไบนารี 

### แอปเดียวกันสามารถเป็นรายการโปรดในหลายภูมิภาคได้หรือไม่

ใช่. รายการโปรดจะถูกเก็บไว้ **ตามรหัสแอปและภูมิภาค** แอพเดียวกันในจีนและสหรัฐอเมริกาปรากฏเป็นสองรายการแยกกันพร้อมป้ายกำกับภูมิภาค 

### จะเกิดอะไรขึ้นหากแอปโปรดถูกเพิกถอน 

รายการจะยังคงอยู่ในรายการโปรดของคุณโดยมีป้ายกำกับ **ถูกเพิกถอน** และไอคอนตัวยึด คุณไม่สามารถเปิดหน้ารายละเอียดได้ แต่คุณสามารถยกเลิกรายการโปรดได้ด้วยการปัดหรือเมนูตามบริบท 

### การติดตามอันดับคืออะไร? 

คุณสมบัติเสริมใน **การตั้งค่า → ขั้นสูง** เมื่อเปิดใช้งาน iApp จะบันทึกประวัติอันดับบนอุปกรณ์ของคุณ (สูงสุด 90 รายการต่อการดูแผนภูมิ) รวมถึง **บันทึกการดรอปดาวน์** สร้าง **การตั้งค่าการติดตามล่วงหน้า** จัดการแอปที่ดูบนหน้าการติดตาม ดู **แผนภูมิอันดับเชิงโต้ตอบ** (ลากเพื่อสครับ) และเลือกแสดง **กิจกรรมสด** (iOS 16.2+) 

### การปักหมุดรายการโปรดและมุมมองตามอันดับทำงานอย่างไร 

**ปักหมุด** แอปจากเมนูตามบริบทหรือการดำเนินการแบบกลุ่ม สลับไปที่ **ตามการจัดอันดับ** ในเมนูตัวกรองรายการโปรดสำหรับตารางการจัดเรียงแบบรวม (ลำดับคอลเลกชัน ชื่อ อันดับโดยรวม/หมวดหมู่ คะแนน ราคา) ใช้ **ค้นหาภูมิภาคอื่น** เพื่อย้ายภูมิภาคร้านค้าของรายการโปรด 

### ฉันจะเปลี่ยนภาษาของแอปได้อย่างไร

**การตั้งค่า → ลักษณะ → ภาษา** — ใช้ค่าเริ่มต้นของระบบหรือเลือกจาก **18 ภาษา** UI จะรีเฟรชทันที; ชื่อวิดเจ็ตและ **Siri & คำสั่งลัด** คำอธิบาย และวลีทั้งหมดจะ **แปลเป็นภาษานั้นอย่างสมบูรณ์**

### ฉันจะเปลี่ยนไอคอนแอปได้อย่างไร?

บน iPhone/iPad: **การตั้งค่า → ลักษณะ → ไอคอนแอป** — เลือกจาก **9 ไอคอนสำรอง** พร้อมตัวอย่างขนาดเล็กและตัวอย่างเต็มหน้าจอ Mac ไม่รองรับไอคอนสำรอง

### วิดเจ็ตและกิจกรรมสดทำงานบนอุปกรณ์ของฉันหรือไม่?

- **วิดเจ็ตหน้าจอโฮม** — iOS 17.0+ (อันดับ + รายการโปรดของฉัน; รายการโปรดที่ปักหมุดอยู่ด้านบน)
- **กิจกรรมสด — อันดับ** — iOS 16.2+ (ตั้งค่าติดตามอันดับล่วงหน้า)
- **กิจกรรมสด — การสมัคร** — iOS 16.2+ (สวิตช์หลักแยกต่างหาก; แยกตามการสมัคร; รวมแถวลดราคา)
- วิดเจ็ตไม่สามารถใช้ได้บน Mac

### ฉันสามารถเปิด iApp ผ่านลิงก์หรือคำสั่งลัดได้หรือไม่?

ใช่. ลิงก์ **`iapp://`** สามารถ **เปิดหน้ารายละเอียดแอป**, **กลับไปยังมุมมองอันดับที่ถูกกรอง**, **สลับแท็บ** หรือ **เปิดหน้ารอง** (รายการโปรดของนักพัฒนา ประวัติการเรียกดู การติดตามอันดับ การตั้งค่ากิจกรรมสด และอื่นๆ) Choose up to **4** from **15** Home Screen Quick Actions in Settings. Widgets and Live Activity generate these links when you tap. ดู [ลิงก์ทางลัด](../url-scheme) 

### Siri และคำสั่งลัดทำงานอย่างไร 

On iOS 16+, search apps, open charts, or add a favorite via the **Shortcuts** app or **Siri**. Action names and Siri phrases are **localized in all 18 app languages** — e.g. อังกฤษ *"ค้นหาแอปใน iApp"*; phrases change when you switch **Settings → Appearance → Language**.

 ### iApp ทำงานแบบออฟไลน์หรือไม่? 

Rankings, search, reviews, all-region checks, and IAP lists require network access. Recently viewed apps may still show saved images. Favorites, subscriptions, rank history, and search history are **saved on your device**.

 ### อุปกรณ์ใดบ้างที่รองรับ?

- **iPhone / iPad** — iOS 15.0 ขึ้นไป (แอปหลัก); iOS 10.3 ขึ้นไป (ไอคอนสำรอง); iOS 17.0 ขึ้นไป (วิดเจ็ต); iOS 16.2 ขึ้นไป (กิจกรรมสด); iOS 16.0 ขึ้นไป (Siri & คำสั่งลัด); iOS 18.0 ขึ้นไป (การแปล)
- **Mac** — macOS 11.0 ขึ้นไป; **⌘1–⌘N** สลับแท็บแบบไดนามิกตามแท็บที่มองเห็น (รวมถึงแท็บโปรดและแท็บโปรดสำหรับนักพัฒนาแบบเลือกได้)

### ฉันจะดาวน์โหลด iApp ได้อย่างไร?

ดาวน์โหลดจาก [App Store](https://apps.apple.com/app/id6446581591)

### ยังต้องการความช่วยเหลืออยู่หรือไม่?

เปิด **การตั้งค่า → ความช่วยเหลือ → คำแนะนำการใช้งาน** (มี 14 คำถามที่พบบ่อย รวมถึงวิธีลดราคา) หรือ ติดต่อ [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) โดยปกติเราจะตอบกลับภายใน 48 ชั่วโมง

</section>
<section lang="de" markdown="1">

### Benötige ich eine Apple-ID oder muss ich mich anmelden? 

Nein. Für iApp ist keine Registrierung oder Anmeldung erforderlich. Sie können Rankings durchsuchen und Apps in jeder unterstützten Region suchen, ohne Ihre Apple-ID auf dem Gerät zu wechseln. 

### Woher kommen die Daten? 

Store-Einträge, Suchergebnisse, App-Details und In-App-Kauflisten stammen aus **öffentlichen App Store-Daten**. Benutzerbewertungen werden nach Region angezeigt. iApp ist ein Browser eines Drittanbieters – kein offizieller App Store-Client. 

### Kann ich Apps von iApp herunterladen oder installieren? 

Nein. iApp zeigt nur öffentliche Store-Informationen an. Zum Herunterladen oder Kaufen verwenden Sie **Im App Store öffnen** oder die **In-App-App-Store-Produktseite** auf dem Detailbildschirm. 

### Ist iApp mit Apple verbunden? 

Nein. iApp ist ein unabhängiges Tool, das von iHTC Studio-Mitarbeitern entwickelt wurde. Es ist **nicht mit Apple Inc. verbunden** 

### Was sind die Hauptregisterkarten?

Standardmäßig: **Rankings**, **Suche**, **Abonnements** und **Einstellungen**. Optional können Sie **Favoriten** und **Entwicklerfavoriten** als eigene Tabs anzeigen und **Abonnements** in der **Einstellungen → App-Einstellungen**-Leiste ausblenden. Favoriten sind immer über **Einstellungen → Daten → App-Favoriten** verfügbar; Entwicklerfavoriten über **Einstellungen → Daten → Entwicklerfavoriten**.

### Was sind App-Vorschauvideos?

Auf der App-Detailseite kann iApp offizielle **App Store-Vorschautrailer** (Streaming-Video) abspielen. Sie können die Qualität wechseln, stummschalten/entsperren, den Link kopieren oder **mit Ton in Fotos speichern**. Das Speichern erfordert die Berechtigung für die Fotobibliothek. Vorschauvideos benötigen eine Netzwerkverbindung.

### Was ist der Vergleich von Inhalten nach Region?

In **All-Region Store-Info** wechseln Sie zu **Content Compare**, um die **Beschreibung**, **Release Notes**, **Screenshots** und **Vorschauvideos** einer App mit einer Basisregion zu vergleichen. Tippen Sie auf eine abweichende Region, um eine Seitenansicht mit orangefarbenen Hervorhebungen zu erhalten. Zusätzliche Filter helfen Ihnen, Unterschiede in Beschreibung, Screenshot oder Video zu finden. Dieser Modus verbraucht mehr Daten — eine Mobilfunkbestätigung wird standardmäßig angezeigt. **Bildexport ist im Content Compare nicht verfügbar**; wechseln Sie zurück zur Listen- oder Rasteransicht, um zu exportieren.  

### Was ist App-Browse-Verlauf?

iApp zeichnet automatisch auf, welche Apps Sie auf der Detailseite öffnen (App + Region, bis zu **100** Einträge, neueste zuerst). Anzeigen, erneut öffnen, nach links wischen zum Löschen oder alle löschen in **Einstellungen → Daten → App-Browse-Verlauf**. Dies ist **nur lokal** — wird nicht über iCloud, Widgets oder andere Geräte synchronisiert. Es ist getrennt vom **Suchverlauf**.  

### Warum sehen Hongkong / Taiwan / Macau im Regionauswahlmenü anders aus?

Regions-**Listen** und **Suche** zeigen klarere Namen an (z. B. vollständige Namen in vereinfachtem Chinesisch, Kurzname + „(China)“ in anderen Sprachen). **Filterchips** und gespeicherte Regionscodes** (`hk`, `tw`, `mo`) bleiben unverändert – Deep Links und Favoriten verwenden weiterhin dieselben Codes. 

### Bewertungen werden nicht geladen oder abgeschnitten? 

**Tippen Sie auf der Seite mit den vollständigen Rezensionen auf eine Rezension**, um den vollständigen Text zu erweitern oder zu reduzieren. iApp lädt standardmäßig **Kundenrezensionen mit Entwicklerantworten** (vollständige Sterneaufschlüsselung inbegriffen); Wenn diese Quelle leer ist oder ausfällt, greift sie auf den RSS-Feed zurück – ziehen Sie ihn zum Aktualisieren oder verwenden Sie die manuelle Aktualisierung auf der Detailseite. 

### Was sind Entwicklerantworten in Rezensionen? 

Wenn ein Entwickler auf eine Benutzerrezension im App Store antwortet, zeigt iApp die **Inline-Antwort des Entwicklers** unter dieser Rezension auf der Seite mit den vollständigen Rezensionen an. Antworten werden zusammen mit der primären Kundenrezensionsquelle geladen. 

### Was ist der App-Versionsverlauf? 

Öffnen Sie auf der Detailseite der App den **Versionsverlauf**, um frühere Versionen anzuzeigen – Versionsnummer, Veröffentlichungsdatum und Versionshinweise –, die aus dem öffentlichen App Store-Katalog für die aktuelle Region abgerufen wurden. 

### Was ist das gleiche Entwicklerkarussell auf der Detailseite?

Unter dem Hauptdetailinhalt zeigt iApp eine **horizontale Vorschau** anderer Apps desselben Entwicklers (Karussell im App Store-Stil). Tippen Sie auf den Abschnittstitel, um die vollständige Liste der gleichen Entwickler mit Sortier- und Rangfolgeansichten zu öffnen. 

### Kann ich eine einzelne App-ID durchsuchen? 

Ja. Geben Sie in der Suche eine numerische App-ID ein (**6–12 Ziffern**, kein Komma). Verwenden Sie für mehrere IDs die durch Kommas getrennte Batch-Suche (bis zu 50). 

### Wo ist die Registerkarte „Entwicklerfavoriten“? 

**Einstellungen → App-Einstellungen → Entwicklerfavoriten in der Tab-Leiste anzeigen** (standardmäßig **aus**). Wenn diese Option aktiviert ist, befindet sich die Registerkarte zwischen Favoriten und Einstellungen. Sie können Entwicklerfavoriten jederzeit über **Einstellungen → Daten** öffnen, wenn die Registerkarte ausgeblendet ist. 

### Was ist das Entwickler-Untermenü in Menüs mit langem Drücken? 

Die Entwickler-Homepage, die Apps des gleichen Entwicklers und die Option „Entwicklerfavorit speichern/entfernen“ sind zur Vermeidung von Unordnung unter **Entwickler** im Menü für langes Drücken gruppiert. 

### Was ist die Warnung zur mobilen Datennutzung? 

Auf **Mobilfunk** bittet die iApp vor Suchvorgängen mit hohem Datenverkehr um eine Bestätigung (Vergleich aller Regionen, **Inhaltsvergleich**, Favoriten/Entwickler-Ranking-Ansichten). Der Standardwert ist **ein**; Deaktivieren Sie die Option unter **Einstellungen → App-Einstellungen**. Sie können im Blatt „Nicht mehr erinnern“ auswählen.

### Was ist der Unterschied zwischen der In-App-Region und der App Store-Region? 

- **In-App-Regionsfilter** (Rankings, Suche, detaillierter Regionsumschalter) ermöglichen Ihnen das Durchsuchen der Diagramme und Einträge jedes Stores, ohne Ihr Gerät wechseln zu müssen. 
- **App Store-Region** (**Einstellungen → Drittanbieter**) hilft dabei, die tatsächliche App Store-Storefront Ihres Geräts über den offiziellen Weiterleitungslink von Apple zu wechseln. Dies sind unabhängige Einstellungen. 

### Was deckt iCloud Sync ab? 

Separate Schalter in **Einstellungen → Daten**: 

- **Favoriten** – gespeicherte Apps (pro Region), Gruppen, Notizen und Pin-Status; zeitstempelbasierte Zusammenführung 
- **Entwicklerfavoriten** – gespeicherte Entwickler (pro Künstler + Region); **separater Schalter, standardmäßig deaktiviert** 
- **Abonnements** – Ihre Merkliste (optional) 
- **Filtervoreinstellungen** – Rangverfolgungsvoreinstellungen (optional) 
- **Suchregion und Schnellregionen** – Suchvorgaben und Schnellregion-Chips (optional) 

Alles wird über **iCloud** auf Ihrem privaten Apple-Konto synchronisiert – nicht über iHTC Studio-Server. 

### Welche Abonnementtypen werden unterstützt? 

Vier Monitore pro Region:

| Geben Sie | ein Uhren für | 
|------|-------------| 
| Version | Neue App Store-Version | 
| Auflistung | App erscheint im Store | 
| Delisting | App aus dem Store entfernt | 
| **Preissenkung** | Der Preis fällt unter den Basiswert; optionaler Zielpreis und/oder Rückgang %; kostenpflichtig → kostenlos zählt immer | 

Dieselbe App + Region kann **mehrere Monitore** verschiedener Typen haben. Kostenlose Apps können die Überwachung von Preissenkungen nicht nutzen. 

### Wie funktioniert die Überwachung von Preissenkungen? 

Wenn Sie einen Preissenkungsmonitor hinzufügen, zeichnet iApp den **Grundpreis** auf. Sie können optional einen **Zielpreis** und/oder einen **minimalen Drop-Prozentsatz** festlegen (beide Bedingungen können ausgelöst werden). Wenn beide leer bleiben, vervollständigt jede Verringerung gegenüber dem Ausgangswert den Monitor. Die Abonnementliste und **Live-Aktivität** zeigen den Basispreis im Vergleich zum aktuellen Preis. 

### Kann ich ein Abonnement pausieren? 

Ja. Verwenden Sie das Kontextmenü für jedes aktive Abonnement, um **Pause** zu aktivieren – die Umfrage wird beendet und die Live-Aktivität endet. **Resume** führt eine sofortige Prüfung durch und kann die Live-Aktivität neu starten. Angehaltene Elemente werden beim Pull-to-Refresh nicht überprüft. 

### Wie füge ich schnell ein Abonnement hinzu?

**Drücken Sie lange** auf eine beliebige App-Zeile in Rankings, Suche oder Favoriten → **Abonnement hinzufügen**. Sie können auch über die Detailseite oder die Registerkarte „Abonnements“ hinzufügen (Stichwortsuche für Versions-/Delisting-Monitore). 

### Was sind Entwicklerfavoriten? 

Speichern Sie einen Entwickler (nach **Künstler + Region**) unter **Einstellungen → Daten → Entwicklerfavoriten**. Öffnen Sie ihre Apps, zeigen Sie Diagrammpositionen **nach Rangfolge** an, markieren Sie Einträge und synchronisieren Sie sie optional über einen **separaten iCloud-Schalter** (standardmäßig deaktiviert). Fügen Sie es über das Detailmenü **Mehr** oder durch langes Drücken des Kontextmenüs hinzu. 

### Was steht auf der detaillierten In-App-Kaufliste? 

Ein einklappbarer Abschnitt **In-App-Käufe** zeigt die vorgestellten IAPs für die **aktuelle Detailregion** (Name, Preis, Abonnementabzeichen). Es wird von öffentlichen App Store-Seiten geladen und kann vom vollständigen Katalog in der App Store-App abweichen. Tippen Sie auf „Aktualisieren“, wenn der Ladevorgang fehlschlägt. 

### Warum unterscheidet sich die Dateigröße von den Einstellungen? 

iApp zeigt die App-Größe in **App Store-Dezimaleinheiten** (1 GB = 1.000.000.000 Byte) an und entspricht dem, was Sie im App Store sehen – nicht binären GiB. 

### Kann dieselbe App in mehreren Regionen als Favorit markiert werden?

Ja. Favoriten werden **pro App-ID und Region** gespeichert. Dieselbe App erscheint in China und den USA als zwei separate Einträge mit Regionsbezeichnungen. 

### Was passiert, wenn eine Lieblings-App aus der Liste entfernt wird? 

Der Eintrag bleibt in Ihren Favoriten mit der Bezeichnung **Delisted** und einem Platzhaltersymbol. Sie können die Detailseite nicht öffnen, aber Sie können die Favoriten per Wisch oder Kontextmenü entfernen. 

### Was ist Rangverfolgung? 

Optionale Funktion in **Einstellungen → Erweitert**. Wenn diese Option aktiviert ist, speichert die iApp den Rangverlauf auf Ihrem Gerät (bis zu 90 Einträge pro Diagrammansicht), einschließlich **Abgabeaufzeichnungen**. Erstellen Sie **Tracking-Voreinstellungen**, verwalten Sie beobachtete Apps auf der Tracking-Seite, zeigen Sie **interaktive Rangdiagramme** an (zum Scrollen ziehen) und zeigen Sie optional eine **Live-Aktivität** an (iOS 16.2+). 

### Wie funktionieren das Anheften von Favoriten und die Ansicht nach Rangfolge? 

**Anheften** Apps über das Kontextmenü oder Batch-Aktionen. Wechseln Sie im Favoriten-Filtermenü zu **Nach Rangfolge**, um eine einheitliche Sortiertabelle (Sammlungsreihenfolge, Name, Gesamt-/Kategorierang, Bewertung, Preis) zu erhalten. Verwenden Sie **Andere Region suchen**, um die Store-Region eines Favoriten zu verschieben. 

### Wie ändere ich die App-Sprache?

**Einstellungen → Darstellung → Sprache** — Systemstandard oder eine der **18 Sprachen**. Die Benutzeroberfläche wird sofort aktualisiert; Widgets sowie **Siri & Kurzbefehle** Titel, Beschreibungen und Phrasen sind in derselben Sprache **vollständig lokalisiert**.

### Wie ändere ich das App-Symbol?

Auf iPhone/iPad: **Einstellungen → Darstellung → App-Symbol** — wählen Sie aus **9 alternativen Symbolen** mit Miniaturansicht und Vollbildvorschau. Auf dem Mac werden keine alternativen Symbole unterstützt.

### Funktionieren Widgets und Live-Aktivität auf meinem Gerät?

- **Home-Bildschirm-Widgets** — iOS 17.0+ (Ranglisten + Meine Favoriten; angepinnte Favoriten zuerst)
- **Live-Aktivität — Ranglisten** — iOS 16.2+ (Rank-Tracking-Voreinstellungen)
- **Live-Aktivität — Abonnements** — iOS 16.2+ (separater Hauptschalter; pro Abonnement; inklusive Preisreduktionszeile)
- Widgets sind auf dem Mac nicht verfügbar

### Kann ich iApp über einen Link oder Kurzbefehl öffnen?

Ja. **`iapp://`** Links können **eine App-Detailseite öffnen**, **zu einer gefilterten Ranglistenansicht zurückkehren**, **Tabs wechseln** oder **sekundäre Seiten öffnen** (Entwicklerfavoriten, Browserverlauf, Rangverfolgung, Live-Aktivitätseinstellungen und mehr). Wählen Sie in den Einstellungen bis zu **4** von **15** Schnellaktionen für den Startbildschirm aus. Widgets und Live-Aktivitäten generieren diese Links, wenn Sie darauf tippen. Siehe [Shortcut-Links](../url-scheme). 

### Wie funktionieren Siri und Verknüpfungen? 

Unter iOS 16+ können Sie über die **Shortcuts**-App oder **Siri** Apps durchsuchen, Diagramme öffnen oder einen Favoriten hinzufügen. Aktionsnamen und Siri-Sätze sind **in allen 18 App-Sprachen lokalisiert** – z.B. Englisch *"Apps in iApp suchen"*; Phrasen ändern sich, wenn Sie zwischen **Einstellungen → Darstellung → Sprache** wechseln. 

### Funktioniert iApp offline? 

Für Rankings, Suche, Rezensionen, Überprüfungen aller Regionen und IAP-Listen ist ein Netzwerkzugriff erforderlich. Kürzlich angesehene Apps zeigen möglicherweise weiterhin gespeicherte Bilder an. Favoriten, Abonnements, Rangverlauf und Suchverlauf werden **auf Ihrem Gerät gespeichert**. 

### Welche Geräte werden unterstützt?

- **iPhone / iPad** — iOS 15.0+ (Haupt-App); iOS 10.3+ (alternative Symbole); iOS 17.0+ (Widgets); iOS 16.2+ (Live-Aktivität); iOS 16.0+ (Siri & Kurzbefehle); iOS 18.0+ (Übersetzung)
- **Mac** — macOS 11.0+; **⌘1–⌘N** wechselt Tabs dynamisch je nach sichtbaren Tabs (einschließlich optionaler Favoriten- und Entwickler-Favoriten-Tabs)

### Wie bekomme ich iApp?

Herunterladen aus dem [App Store](https://apps.apple.com/app/id6446581591).

### Brauchen Sie noch Hilfe?

Öffnen Sie **Einstellungen → Hilfe → Gebrauchsanweisungen** (14 FAQ-Artikel einschließlich Preisreduktions-Anleitung) oder kontaktieren Sie [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com). Wir antworten normalerweise innerhalb von 48 Stunden.

</section>
<section lang="fr" markdown="1">

### Ai-je besoin d'un identifiant Apple ou de me connecter ?

Non. iApp ne nécessite pas d'inscription ni de connexion. Vous pouvez consulter les classements et rechercher des applications dans n'importe quelle région prise en charge sans changer votre identifiant Apple sur l'appareil.

### D'où proviennent les données ?

Les listes du store, les résultats de recherche, les détails des applications et les listes d'achats intégrés proviennent des **données publiques de l'App Store**. Les avis des utilisateurs sont affichés par région. iApp est un navigateur tiers — et non un client officiel de l'App Store.

### Puis-je télécharger ou installer des applications depuis iApp ?

Non. iApp affiche uniquement les informations publiques du store. Pour télécharger ou acheter, utilisez **Ouvrir dans l'App Store** ou la **page produit de l'App Store intégrée à l'application** sur l'écran de détail.

### iApp est-il affilié à Apple ?

Non. iApp est un outil indépendant créé par les contributeurs d'iHTC Studio. Il **n'est pas affilié à Apple Inc.**

### Quels sont les onglets principaux ?

Par défaut : **Classements**, **Recherche**, **Abonnements** et **Paramètres**. Vous pouvez éventuellement afficher **Favoris** et **Favoris des développeurs** comme onglets séparés, et masquer **Abonnements** de la barre d'onglets dans **Paramètres → Paramètres de l'application**. Les favoris sont toujours disponibles depuis **Paramètres → Données → Favoris de l'application** ; les favoris des développeurs depuis **Paramètres → Données → Favoris des développeurs**.

### Quelles sont les vidéos de prévisualisation d'application ?

Sur la page de détail de l'application, iApp peut lire les **bandes-annonces de prévisualisation officielles de l'App Store** (vidéo en streaming). Vous pouvez changer la qualité, couper/activer le son, copier le lien ou **enregistrer dans Photos avec audio**. L'enregistrement nécessite l'autorisation de la bibliothèque de photos. Les vidéos de prévisualisation nécessitent une connexion réseau.

### Qu'est-ce que la comparaison de contenu par région ?

Dans **Informations sur le magasin toutes régions**, passez à **Comparer le contenu** pour comparer la **description**, les **notes de version**, les **captures d'écran** et les **vidéos de prévisualisation** d'une application par rapport à une région de référence. Appuyez sur une région différente pour une vue côte à côte avec les différences en surbrillance orange. Des filtres supplémentaires vous aident à trouver les différences dans la description, les captures d'écran ou les vidéos. Ce mode utilise plus de données — une confirmation sur réseau cellulaire apparaît par défaut. **L'exportation d'images n'est pas disponible** dans la comparaison de contenu ; revenez à la vue liste ou grille pour exporter.

### Qu'est-ce que l'historique de navigation des applications ?

iApp enregistre automatiquement les applications que vous ouvrez sur la page de détail (application + région, jusqu'à **100** entrées, de la plus récente à la plus ancienne). Consultez-les, rouvrez-les, faites glisser pour supprimer, ou effacez tout dans **Paramètres → Données → Historique de navigation des apps**. Ceci est **strictement local** — non synchronisé via iCloud, widgets ou autres appareils. Il est séparé de **l'historique de recherche**.

### Pourquoi Hong Kong / Taïwan / Macao apparaissent-ils différemment dans le sélecteur de région ?

Les **listes** et **recherches** de régions affichent des noms plus clairs (par exemple, noms complets en chinois simplifié, nom court + « (Chine) » dans d'autres langues). Les **puces de filtre** et les **codes** de région stockés (`hk`, `tw`, `mo`) sont inchangés : les liens profonds et les favoris utilisent toujours les mêmes codes. 

### Les avis ne se chargent pas ou sont tronqués ? 

Sur la page des avis complets, **appuyez sur un avis** pour développer ou réduire le texte intégral. iApp charge **les avis des clients avec les réponses des développeurs** par défaut (répartition complète des étoiles incluse) ; si cette source est vide ou échoue, elle revient au flux RSS : tirez pour actualiser ou utilisez l'actualisation manuelle sur la page de détail. 

### Que sont les réponses des développeurs dans les avis ? 

Lorsqu'un développeur répond à un avis d'utilisateur sur l'App Store, iApp affiche la **réponse du développeur en ligne** sous cet avis sur la page des avis complets. Les réponses se chargent avec la source principale des avis clients. 

### Qu'est-ce que l'historique des versions de l'application ? 

Sur la page de détails de l'application, ouvrez **Historique des versions** pour voir les versions précédentes (numéro de version, date de sortie et notes de version) extraites du catalogue public de l'App Store pour la région actuelle. 

### Qu'est-ce que le carrousel du même développeur sur la page de détails ?

Sous le contenu détaillé principal, iApp affiche un **aperçu horizontal** d'autres applications du même développeur (carrousel de style App Store). Appuyez sur le titre de la section pour ouvrir la liste complète des mêmes développeurs avec des vues de tri et de classement. 

### Puis-je rechercher un seul identifiant d'application ? 

Oui. Dans Rechercher, saisissez un identifiant d'application numérique (**6 à 12 chiffres**, sans virgule). Pour plusieurs ID, utilisez la recherche par lots séparés par des virgules (jusqu'à 50). 

### Où se trouve l'onglet Favoris des développeurs ? 

**Paramètres → Paramètres de l'application → Afficher les favoris du développeur dans la barre d'onglets** (**désactivé** par défaut). Lorsqu'il est activé, l'onglet se situe entre Favoris et Paramètres. Vous pouvez toujours ouvrir les favoris des développeurs depuis **Paramètres → Données** lorsque l'onglet est masqué. 

### Qu'est-ce que le sous-menu Développeur dans les menus à pression longue ? 

La page d'accueil du développeur, les applications du même développeur et l'enregistrement/suppression des favoris du développeur sont regroupés sous **Développeur** dans le menu d'appui long pour réduire l'encombrement. 

### Qu'est-ce que l'alerte d'utilisation des données mobiles ? 

Sur **cellulaire**, iApp demande une confirmation avant les recherches à fort trafic (comparaison de toutes les régions, **comparaison de contenu**, vues des favoris/développeurs par classement). La valeur par défaut est **on** ; désactiver dans **Paramètres → Paramètres de l'application**. Vous pouvez choisir « Ne plus rappeler » dans la feuille.

### Quelle est la différence entre la région intégrée à l'application et la région App Store ? 

- **Filtres de région intégrés à l'application** (Classements, recherche, sélecteur de région détaillée) vous permettent de parcourir les graphiques et les listes de n'importe quel magasin sans changer d'appareil. 
- **Région App Store** (**Paramètres → Tiers**) permet de changer la vitrine App Store réelle de votre appareil à l'aide du lien de redirection officiel d'Apple. Ce sont des paramètres indépendants. 

### Que couvre iCloud Sync ? 

Séparez les boutons dans **Paramètres → Données** : 

- **Favoris** : applications enregistrées (par région), groupes, notes et état du code PIN ; fusion basée sur l'horodatage 
- **Favoris des développeurs** — développeurs enregistrés (par artiste + région) ; **bascule séparée, désactivée par défaut** 
- **Abonnements** — votre liste de surveillance (facultatif) 
- **Préréglages de filtre** — préréglages de suivi de classement (facultatif) 
- **Région de recherche et régions rapides** — valeurs par défaut de recherche et puces de région rapide (facultatif) 

Tout se synchronise via **iCloud** sur votre compte Apple privé – et non sur les serveurs iHTC Studio. 

### Quels types d'abonnement sont pris en charge ? 

Quatre moniteurs par région :

| Tapez | Montres pour | 
|------|-------------| 
| Version | Nouvelle version de l'App Store | 
| Inscription | L'application apparaît dans la boutique | 
| Radiation | Application supprimée du magasin | 
| **Baisse de prix** | Le prix tombe en dessous du niveau de référence ; prix cible facultatif et/ou % de baisse ; payant → gratuit compte toujours | 

La même application + région peut avoir **plusieurs moniteurs** de types différents. Les applications gratuites ne peuvent pas utiliser la surveillance des baisses de prix. 

### Comment fonctionne le suivi des baisses de prix ? 

Lorsque vous ajoutez un moniteur de baisse de prix, iApp enregistre le **prix de référence**. Vous pouvez éventuellement définir un **prix cible** et/ou un **pourcentage de baisse minimum** (l'une ou l'autre condition peut se déclencher). Si les deux restent vides, toute diminution par rapport à la ligne de base complète le suivi. La liste d'abonnements et **Live Activity** affichent le prix de référence par rapport au prix actuel. 

### Puis-je suspendre un abonnement ? 

Oui. Utilisez le menu contextuel de tout abonnement actif à **Pause** : l'interrogation s'arrête et son activité en direct se termine. **Resume** exécute une vérification immédiate et peut redémarrer l'activité en direct. Les éléments en pause ne sont pas vérifiés lors de l'extraction pour actualiser. 

### Comment ajouter un abonnement rapidement ?

**Appuyez longuement** sur n'importe quelle ligne d'application dans les classements, la recherche ou les favoris → **Ajouter un abonnement**. Vous pouvez également ajouter à partir de la page de détails ou de l'onglet Abonnements (recherche par mot-clé pour les moniteurs de version/suppression). 

### Quels sont les favoris des développeurs ? 

Enregistrez un développeur (par **artiste + région**) dans **Paramètres → Données → Favoris du développeur**. Ouvrez leurs applications, affichez les positions du graphique **par classement**, les entrées d'épingles et éventuellement synchronisez via une **bascule iCloud séparée** (désactivée par défaut). Ajoutez à partir du menu détaillé **Plus** ou du menu contextuel en appuyant longuement. 

### Que trouve-t-on dans la liste détaillée des achats intégrés ? 

Une section **Achats intégrés** pliable affiche les IAP présentés pour la **région détaillée actuelle** (nom, prix, badge d'abonnement). Il se charge à partir des pages publiques de l'App Store et peut différer du catalogue complet de l'application App Store. Appuyez sur Actualiser si le chargement échoue. 

### Pourquoi la taille du fichier est-elle différente de celle des paramètres ? 

iApp affiche la taille de l'application en utilisant **unités décimales de l'App Store** (1 Go = 1 000 000 000 d'octets), correspondant à ce que vous voyez dans l'App Store — et non en GiB binaire. 

### La même application peut-elle être favorite dans plusieurs régions ?

Oui. Les favoris sont conservés **par identifiant d'application et par région**. La même application en Chine et aux États-Unis apparaît sous la forme de deux entrées distinctes avec des étiquettes de région. 

### Que se passe-t-il si une application favorite est supprimée de la liste ? 

L'entrée reste dans vos favoris avec une étiquette **Supprimé** et une icône d'espace réservé. Vous ne pouvez pas ouvrir sa page de détails, mais vous pouvez la supprimer des favoris via un balayage ou un menu contextuel. 

### Qu'est-ce que le suivi des classements ? 

Fonctionnalité facultative dans **Paramètres → Avancé**. Lorsqu'elle est activée, iApp enregistre l'historique des classements sur votre appareil (jusqu'à 90 entrées par vue graphique), y compris les **enregistrements de dépôt**. Créez des **préréglages de suivi**, gérez les applications surveillées sur la page de suivi, affichez des **graphiques de classement interactifs** (faites glisser pour parcourir) et affichez éventuellement une **activité en direct** (iOS 16.2+). 

### Comment fonctionnent l'épinglage des favoris et l'affichage par classement ? 

**Épinglez** des applications à partir du menu contextuel ou des actions par lots. Passez à **Par classement** dans le menu de filtrage des favoris pour un tableau de tri unifié (ordre de collecte, nom, classement global/catégorie, note, prix). Utilisez **Rechercher une autre région** pour déplacer la région du magasin d'un favori. 

### Comment changer la langue de l'application ?

**Paramètres → Apparence → Langue** — Par défaut du système ou l'une des **18 langues**. L'interface se met à jour immédiatement ; les widgets ainsi que les titres, descriptions et phrases de **Siri & Raccourcis** sont **entièrement localisés** dans la même langue.

### Comment puis-je changer l'icône de l'application ?

Sur iPhone/iPad : **Paramètres → Apparence → Icône de l'application** — choisissez parmi **9 icônes alternatives** avec aperçu miniature et aperçu en plein écran. Mac ne prend pas en charge les icônes alternatives.

### Les widgets et Live Activity fonctionnent-ils sur mon appareil ?

- **Widgets de l'Écran d'accueil** — iOS 17.0+ (Classements + Mes Favoris ; favoris épinglés en premier)
- **Live Activity — Classements** — iOS 16.2+ (préréglages de suivi des classements)
- **Live Activity — Abonnements** — iOS 16.2+ (interrupteur principal séparé ; par abonnement ; inclut la ligne de baisse de prix)
- Les widgets ne sont pas disponibles sur Mac

### Puis-je ouvrir iApp depuis un lien ou un raccourci ?

Oui. Les liens **`iapp://`** peuvent **ouvrir une page de détails d'application**, **revenir à une vue de classement filtrée**, **changer d'onglet** ou **ouvrir des pages secondaires** (favoris des développeurs, historique de navigation, suivi des classements, paramètres d'activité en direct, etc.). Choisissez jusqu'à **4** parmi **15** Actions rapides sur l'écran d'accueil dans les paramètres. Les widgets et l'activité en direct génèrent ces liens lorsque vous appuyez sur. Voir [Liens de raccourci] (../url-scheme). 

### Comment fonctionnent Siri et les raccourcis ? 

Sur iOS 16+, recherchez des applications, ouvrez des graphiques ou ajoutez un favori via l'application **Raccourcis** ou **Siri**. Les noms d'action et les phrases Siri sont **localisés dans les 18 langues de l'application** - par ex. Anglais *« Rechercher des applications dans iApp »* ; les phrases changent lorsque vous basculez sur **Paramètres → Apparence → Langue**. 

### L'iApp fonctionne-t-il hors ligne ? 

Les classements, les recherches, les avis, les vérifications dans toutes les régions et les listes IAP nécessitent un accès au réseau. Les applications récemment consultées peuvent toujours afficher des images enregistrées. Les favoris, les abonnements, l'historique des classements et l'historique des recherches sont **enregistrés sur votre appareil**. 

### Quels appareils sont pris en charge ?

- **iPhone / iPad** — iOS 15.0+ (application principale) ; iOS 10.3+ (icônes alternatives) ; iOS 17.0+ (widgets) ; iOS 16.2+ (Activité en direct) ; iOS 16.0+ (Siri et Raccourcis) ; iOS 18.0+ (traduction)
- **Mac** — macOS 11.0+ ; **⌘1–⌘N** changer d'onglets dynamiquement en fonction des onglets visibles (y compris les onglets Favoris et Favoris Développeur optionnels)

### Comment obtenir iApp ?

Téléchargez depuis l’[App Store](https://apps.apple.com/app/id6446581591).

### Toujours besoin d’aide ?

Ouvrez **Réglages → Aide → Instructions d’utilisation** (14 FAQ incluant comment procéder pour les baisses de prix) ou contactez [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com). Nous répondons généralement sous 48 heures.

</section>
<section lang="tr" markdown="1">

### Apple ID'ye ihtiyacım var mı veya oturum açmam gerekiyor mu?

Hayır. iApp kayıt veya giriş gerektirmez. Desteklenen herhangi bir bölgede Apple ID'nizi değiştirmeden sıralamaları göz atabilir ve uygulama arayabilirsiniz.

### Veriler nereden geliyor?

Mağaza listeleri, arama sonuçları, uygulama detayları ve uygulama içi satın alma listeleri **kamuya açık App Store verilerinden** gelmektedir. Kullanıcı yorumları bölgeye göre gösterilir. iApp üçüncü taraf bir tarayıcıdır — resmi bir App Store istemcisi değildir.

### iApp üzerinden uygulama indirebilir veya yükleyebilir miyim?

Hayır. iApp yalnızca kamuya açık mağaza bilgilerini gösterir. İndirmek veya satın almak için, detay ekranındaki **App Store'da Aç** veya **uygulama içi App Store ürün sayfasını** kullanın.

### iApp Apple ile bağlantılı mı?

Hayır. iApp, iHTC Studio katkıcıları tarafından geliştirilen bağımsız bir araçtır. Apple Inc. ile **bağlantılı değildir**.

### Ana sekmeler nelerdir?

Varsayılan olarak: **Sıralamalar**, **Arama**, **Abonelikler** ve **Ayarlar**. İsteğe bağlı olarak **Favoriler** ve **Geliştirici Favorileri** sekmelerini kendi ayrı sekmeleri olarak gösterebilir ve **Ayarlar → Uygulama Ayarları** üzerinden sekme çubuğundan **Abonelikler**i gizleyebilirsiniz. Favoriler her zaman **Ayarlar → Veriler → Uygulama Favorileri** üzerinden erişilebilir; geliştirici favorileri ise **Ayarlar → Veriler → Geliştirici Favorileri** üzerinden erişilebilir.

### Uygulama Önizleme videoları nedir?

Uygulama detay sayfasında, iApp resmi **App Store önizleme fragmanlarını** (akış videosu) oynatabilir. Kaliteyi değiştirebilir, sessize alabilir/sesi açabilir, bağlantıyı kopyalayabilir veya **sesle birlikte Fotoğraflara kaydedebilirsiniz**. Kaydetme işlemi fotoğraf kütüphanesi izni gerektirir. Önizleme videoları bir ağ bağlantısı gerektirir.

### Bölge içeriği karşılaştırması nedir?

**Tüm bölge mağaza bilgileri**nde, bir uygulamanın **açıklamasını**, **sürüm notlarını**, **ekran görüntülerini** ve **önizleme videolarını** bir temel bölge ile karşılaştırmak için **İçerik karşılaştır**a geçin. Farklı bir bölgeye dokunarak turuncu vurgularla yan yana görünüm elde edebilirsiniz. Ek filtreler, açıklama, ekran görüntüsü veya video farklarını bulmanıza yardımcı olur. Bu mod daha fazla veri kullanır — varsayılan olarak bir hücresel onay görünür. **Görüntü dışa aktarma**, içerik karşılaştırmada **mevcut değildir**; dışa aktarmak için liste veya ızgaraya geri dönün.

### Uygulama Tarama Geçmişi Nedir?

iApp, detay sayfasında açtığınız uygulamaları otomatik olarak kaydeder (uygulama + bölge, en fazla **100** giriş, en yenisi ilk sırada). Görüntüleyin, tekrar açın, silmek için kaydırın veya tümünü **Ayarlar → Veriler → Uygulama Tarama Geçmişi**nden temizleyin. Bu **yalnızca yerel**dir — iCloud, widgetlar veya diğer cihazlarla senkronize edilmez. **Arama geçmişinden** ayrıdır.

### Neden Hong Kong / Tayvan / Makao bölge seçiciye farklı görünüyor?

Bölge **listeleri** ve **arama** daha net adlar gösterir (ör. Basitleştirilmiş Çince'de tam adlar, diğer dillerde kısa ad + "(Çin)"). **Filtre çipleri** ve depolanan bölge **kodları** (`hk`, `tw`, `mo`) değiştirilmedi; derin bağlantılar ve favoriler hâlâ aynı kodları kullanıyor. 

### İncelemeler yüklenmiyor veya kısaltılmıyor mu? 

Tam incelemeler sayfasında, tam metni genişletmek veya daraltmak için **bir incelemeye dokunun**. iApp varsayılan olarak **geliştirici yanıtlarıyla birlikte müşteri incelemelerini** yükler (tam yıldız dökümü dahildir); kaynak boşsa veya arızalanırsa RSS beslemesine geri döner; yenilemek için çekin veya ayrıntı sayfasında manuel yenilemeyi kullanın. 

### İncelemelerdeki geliştirici yanıtları nelerdir? 

Bir geliştirici, App Store'daki bir kullanıcı incelemesine yanıt verdiğinde, iApp, tam incelemeler sayfasında bu incelemenin altında **geliştirici yanıtını satır içi** gösterir. Yanıtlar birincil müşteri yorumları kaynağıyla birlikte yüklenir. 

### Uygulama sürüm geçmişi nedir? 

Geçerli bölge için genel App Store kataloğundan alınan geçmiş sürümleri (sürüm numarası, yayın tarihi ve sürüm notları) görmek için uygulama ayrıntıları sayfasında **Sürüm Geçmişi**'ni açın. 

### Ayrıntı sayfasındaki aynı geliştirici karusel nedir?

Ana ayrıntı içeriğinin altında iApp, aynı geliştiricinin (App Store tarzı atlıkarınca) diğer uygulamalarının **yatay önizlemesini** gösterir. Sıralama ve sıralamaya göre görünümlerle aynı geliştirici listesinin tamamını açmak için bölüm başlığına dokunun. 

### Tek bir Uygulama Kimliğini arayabilir miyim? 

Evet. Arama'ya bir sayısal Uygulama Kimliği girin (**6–12 rakam**, virgülsüz). Birden fazla kimlik için virgülle ayrılmış toplu aramayı kullanın (50'ye kadar). 

### Geliştirici Favorileri sekmesi nerede? 

**Ayarlar → Uygulama Ayarları → Sekme çubuğunda Geliştirici Favorilerini Göster** (varsayılan **kapalı**). Etkinleştirildiğinde sekme, Sık Kullanılanlar ve Ayarlar arasında yer alır. Sekme gizlendiğinde, geliştiricilerin favorilerini istediğiniz zaman **Ayarlar → Veri**'den açabilirsiniz. 

### Uzun basılan menülerdeki Geliştirici alt menüsü nedir? 

Karışıklığı azaltmak için geliştirici ana sayfası, aynı geliştiricinin uygulamaları ve geliştiricinin favorilerini kaydet/kaldır, uzun basılan menüde **Geliştirici** altında gruplandırılmıştır. 

### Mobil veri kullanımı uyarısı nedir? 

**hücresel** üzerinde, iApp yüksek trafikli aramalardan (tüm bölge karşılaştırması, **içerik karşılaştırması**, favoriler/geliştirici sıralamasına göre görünümler) önce onay ister. Varsayılan **açık**'tır; **Ayarlar → Uygulama Ayarları** bölümünden devre dışı bırakın. Sayfada "Bir daha hatırlatma"yı seçebilirsiniz.

### Uygulama içi bölge ile App Store bölgesi arasındaki fark nedir? 

- **Uygulama içi bölge filtreleri** (Sıralamalar, Arama, ayrıntılı bölge değiştirici), cihazınızı değiştirmeden herhangi bir mağazanın grafiklerine ve listelerine göz atmanıza olanak tanır. 
- **App Store Bölgesi** (**Ayarlar → Üçüncü Taraf**), Apple'ın resmi yönlendirme bağlantısını kullanarak cihazınızın gerçek App Store vitrinini değiştirmenize yardımcı olur. Bunlar bağımsız ayarlardır. 

### iCloud Senkronizasyonu neleri kapsar? 

**Ayarlar → Veri**'de ayrı geçişler: 

- **Favoriler** — kayıtlı uygulamalar (bölgeye göre), gruplar, notlar ve pin durumu; zaman damgası tabanlı birleştirme 
- **Geliştiricilerin Favorileri** — kaydedilen geliştiriciler (sanatçı + bölge başına); **ayrı geçiş, varsayılan olarak kapalı** 
- **Abonelikler** — izleme listeniz (isteğe bağlı) 
- **Filtre ön ayarları** — sıralama izleme ön ayarları (isteğe bağlı) 
- **Bölgeyi ve hızlı bölgeleri arayın** — varsayılanları ve hızlı bölge çiplerini arayın (isteğe bağlı) 

Tüm senkronizasyonlar iHTC Studio sunucularında değil, özel Apple hesabınızda **iCloud** üzerinden yapılır. 

### Hangi abonelik türleri destekleniyor? 

Bölge başına dört monitör:

| Tür | Saatler | 
|------|-----------------| 
| Sürüm | Yeni App Store sürümü | 
| Listeleme | Uygulama mağazada görünüyor | 
| Listeden kaldırılıyor | Uygulama mağazadan kaldırıldı | 
| **Fiyat düşüşü** | Fiyat taban çizgisinin altına düşer; isteğe bağlı hedef fiyat ve/veya düşüş yüzdesi; ücretli → ücretsiz her zaman önemlidir | 

Aynı uygulama + bölgede farklı türlerde **birden fazla monitör** bulunabilir. Ücretsiz uygulamalar fiyat düşüşü izlemeyi kullanamaz. 

### Fiyat düşüşünü izleme nasıl çalışır? 

Bir fiyat düşüşü monitörü eklediğinizde, iApp **temel fiyatı** kaydeder. İsteğe bağlı olarak bir **hedef fiyat** ve/veya **minimum düşüş yüzdesi** belirleyebilirsiniz (her iki koşul da tetiklenebilir). Her ikisi de boş bırakılırsa taban çizgisinden herhangi bir azalma monitörü tamamlar. Abonelik listesi ve **Canlı Etkinlik** temel ve geçerli fiyatı gösterir. 

### Bir aboneliği duraklatabilir miyim? 

Evet. **Duraklatma** için herhangi bir etkin aboneliğin içerik menüsünü kullanın; oylama durdurulur ve Canlı Etkinliği sona erer. **Devam Et** anında bir kontrol gerçekleştirir ve Canlı Etkinliği yeniden başlatabilir. Duraklatılan öğeler yenilemek için çekmede kontrol edilmez. 

### Aboneliği hızlı bir şekilde nasıl eklerim?

Sıralamalar, Arama veya Favoriler'deki herhangi bir uygulama satırına **uzun basın** → **Abonelik Ekle**. Ayrıntı sayfasından veya Abonelikler sekmesinden de ekleyebilirsiniz (sürüm için anahtar kelime araması/monitörlerin listeden çıkarılması). 

### Geliştiricilerin favorileri nelerdir? 

**Ayarlar → Veri → Geliştirici Favorileri**'ne giderek bir geliştiriciyi kaydedin (**sanatçı + bölgeye** göre). Uygulamalarını açın, **sıralamaya göre** grafik konumlarını görüntüleyin, pin girişlerini görüntüleyin ve isteğe bağlı olarak **ayrı bir iCloud açma/kapama düğmesi** (varsayılan olarak kapalı) aracılığıyla senkronizasyon yapın. Ayrıntı **Diğer** menüsünden veya uzun basılan içerik menüsünden ekleyin. 

### Ayrıntılı uygulama içi satın alma listesinde neler var? 

Daraltılabilir bir **Uygulama İçi Satın Alımlar** bölümü, **mevcut ayrıntılı bölge** için öne çıkan IAP'leri (ad, fiyat, abonelik rozeti) gösterir. Herkese açık App Store sayfalarından yüklenir ve App Store uygulamasındaki kataloğun tamamından farklı olabilir. Yükleme başarısız olursa yenile'ye dokunun. 

### Dosya boyutu neden Ayarlar'dan farklı görünüyor? 

iApp, uygulama boyutunu **App Store ondalık birimleri** (1 GB = 1.000.000.000 bayt) kullanarak görüntüler; ikili GiB ile değil, App Store'da gördüklerinizle eşleşir. 

### Aynı uygulama birden fazla bölgede favorilere eklenebilir mi?

Evet. Favoriler **Uygulama Kimliği ve bölgeye göre** tutulur. Çin ve ABD'de aynı uygulama, bölge etiketleriyle iki ayrı giriş olarak görünüyor. 

### Favorilere eklenen bir uygulama listeden çıkarılırsa ne olur? 

Giriş, **Listeden Çıkarıldı** etiketi ve yer tutucu simgesiyle favorilerinizde kalır. Ayrıntı sayfasını açamazsınız ancak kaydırma veya içerik menüsü aracılığıyla favorilerden kaldırabilirsiniz. 

### Sıralama takibi nedir? 

**Ayarlar → Gelişmiş**'deki isteğe bağlı özellik. Etkinleştirildiğinde, iApp, **bırakma kayıtları** da dahil olmak üzere sıralama geçmişini cihazınıza kaydeder (harita görünümü başına en fazla 90 giriş). **İzleme ön ayarları** oluşturun, izleme sayfasında izlenen uygulamaları yönetin, **etkileşimli sıralama grafiklerini** görüntüleyin (silme için sürükleyin) ve isteğe bağlı olarak bir **Canlı Etkinlik** (iOS 16.2+) gösterin. 

### Favorileri sabitleme ve sıralamaya göre görünüm nasıl çalışır? 

İçerik menüsünden veya toplu işlemlerden **Uygulamaları sabitleyin**. Birleşik bir sıralama tablosu (koleksiyon sırası, ad, genel/kategori sıralaması, derecelendirme, fiyat) için favoriler filtre menüsünde **Sıralamaya göre** seçeneğine geçin. Favori mağaza bölgesinin yerini değiştirmek için **Başka bir bölge bul**'u kullanın. 

### Uygulama dilini nasıl değiştiririm?

**Ayarlar → Görünüm → Dil** — Sistem varsayılanı veya **18 dilden** herhangi biri. Kullanıcı arayüzü hemen yenilenir; widget'lar ve **Siri & Kestirmeler** başlıkları, açıklamaları ve ifadeleri aynı dilde **tamamen yerelleştirilmiştir**.

### Uygulama simgesini nasıl değiştiririm?

iPhone/iPad: **Ayarlar → Görünüm → Uygulama Simgesi** — küçük önizleme ve tam ekran önizlemesi ile **9 alternatif simgeden** birini seçin. Mac alternatif simgeleri desteklemez.

### Widget'lar ve Canlı Etkinlik cihazımda çalışıyor mu?

- **Ana Ekran widget'ları** — iOS 17.0+ (Sıralamalar + Favorilerim; sabitlenmiş favoriler önce)
- **Canlı Etkinlik — Sıralamalar** — iOS 16.2+ (sıra takip ön ayarları)
- **Canlı Etkinlik — Abonelikler** — iOS 16.2+ (ayrı ana anahtar; her abonelik için; fiyat düşüşü satırı dahil)
- Widget'lar Mac'te kullanılamaz

### iApp'i bir bağlantı veya kestirmeden açabilir miyim?

Evet. **`iapp://`_** bağlantılar **bir uygulama ayrıntı sayfasını açabilir**, **filtrelenmiş bir Sıralama görünümüne dönebilir**, **sekmeler arasında geçiş yapabilir** veya **ikincil sayfaları açabilir** (geliştirici favorileri, göz atma geçmişi, sıralama takibi, Canlı Etkinlik ayarları ve daha fazlası). Ayarlar'da **15** Ana Ekran Hızlı Eylemleri arasından **4**'e kadar seçim yapın. Widget'lar ve Canlı Etkinlik, dokunduğunuzda bu bağlantıları oluşturur. Bkz. [Kısayol Bağlantıları](../url-scheme). 

### Siri ve Kısayollar nasıl çalışır? 

iOS 16 ve sonraki sürümlerde **Kısayollar** uygulaması veya **Siri** aracılığıyla uygulamaları arayın, grafikleri açın veya favorilerinizi ekleyin. Eylem adları ve Siri ifadeleri **18 uygulama dilinin tamamında yerelleştirilmiştir** - ör. İngilizce *"iApp'te uygulamaları arayın"*; **Ayarlar → Görünüm → Dil** seçeneğini değiştirdiğinizde ifadeler değişir. 

### iApp çevrimdışı çalışıyor mu? 

Sıralamalar, arama, incelemeler, tüm bölgeleri kapsayan kontroller ve IAP listeleri ağ erişimi gerektirir. Son görüntülenen uygulamalar hâlâ kayıtlı resimleri gösterebilir. Favoriler, abonelikler, sıralama geçmişi ve arama geçmişi **cihazınıza kaydedilir**. 

### Hangi cihazlar destekleniyor?

- **iPhone / iPad** — iOS 15.0+ (ana uygulama); iOS 10.3+ (alternatif simgeler); iOS 17.0+ (widget'lar); iOS 16.2+ (Canlı Aktivite); iOS 16.0+ (Siri & Kestirmeler); iOS 18.0+ (çeviri)
- **Mac** — macOS 11.0+; **⌘1–⌘N** görünür sekmelere bağlı olarak sekmeler arasında dinamik geçiş (isteğe bağlı Favoriler ve Geliştirici Favorileri sekmeleri dahil)

### iApp'i nasıl alabilirim?

[App Store](https://apps.apple.com/app/id6446581591) üzerinden indirin.

### Hala yardıma mı ihtiyacınız var?

**Ayarlar → Yardım → Kullanım Talimatları**nı açın (fiyat düşüşü nasıl yapılır dahil 14 SSS öğesi) ya da [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) adresinden iletişime geçin. Genellikle 48 saat içinde yanıt veriyoruz.

</section>
