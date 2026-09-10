---
layout: doc
title: iStore — FAQ
app_id: iStore
doc_title_en: Frequently Asked Questions
doc_title_zh_cn: 常见问题
doc_title_zh_tw: 常見問題
description: Frequently asked questions about iStore — App Store region switching, availability checks, favorites, widgets, and iCloud sync.
---

<section lang="en" markdown="1">

### How does region switching work?

iStore opens Apple's **official App Store redirect link** for the region you pick. The App Store then asks you to confirm the change on Apple's own screen. iStore never sees your Apple ID, password, or payment details.

### Do I need to sign in?

No. iStore requires **no account and no login**. You only interact with your existing Apple ID inside Apple's own App Store screen when you confirm a switch.

### Will switching region log me out or lose my apps?

No. Switching your storefront changes which region's App Store you browse and buy from. Your installed apps stay installed. Apple may require your billing region and payment method to match before you can purchase in a new region.

### Is iStore affiliated with Apple?

No. iStore is an independent tool built by iHTC Studio contributors. It is **not affiliated with Apple Inc.** It simply uses Apple's official redirect link to switch regions.

### How many regions are supported?

**175 regions** across 7 continents, each with its flag and a localized name (English / Simplified / Traditional Chinese).

### What is the App Availability check?

Paste an **App Store link or numeric App ID** and iStore checks (via Apple's public iTunes Lookup API) **which regions the app is available in**. Scope the check to **Popular**, **Favorites**, or **All** regions, then switch to any available region with one tap. It works in the app and from the **Share Extension**.

### How do I check availability from another app?

Use the **Share** sheet on any App Store link (Safari, Messages, App Store, etc.) and choose **iStore**. The Share Extension checks popular regions and lets you open the result in the app to switch.

### What is the difference between Favorites and Pinned?

**Favorites** are the regions you star. **Pinned** regions are a subset you want to keep at the very top everywhere (store, favorites, and widgets). Unfavoriting a region also removes it from pinned.

### What's the Map Picker?

A **full-screen map** with a pin for each region. Scope it to Popular, Favorites, or All, then tap a pin to switch. It's a visual way to explore stores by location.

### Which widgets are available?

- **Quick Regions** and **Recent** widgets (Home & Lock Screen)
- A **Custom** widget you configure with your own regions (iOS 17+)
- **Interactive widgets** (iOS 17+) — tap a region tile to switch directly

### What is the Control Center control?

On **iOS 18+**, add the **Switch Last** control to Control Center to re-switch to your most recent target region in one tap.

### Can I switch using Siri or Shortcuts?

Yes. iStore provides Siri & Shortcuts actions to **switch a region**, **switch your last region**, **switch a favorite**, **open the store**, or **check availability**. See [Shortcut Links](url-scheme).

### Does Spotlight search work?

Yes. All 175 regions are indexed in **Spotlight** — search a region from the Home Screen and tap the result to switch directly in iStore.

### What does iCloud Sync cover?

Optional iCloud sync keeps these in step across your devices: **favorites**, **pinned regions**, **quick regions**, **switch history**, **last switched region**, and appearance / layout / favorites preferences. Data syncs through **your private iCloud** — not iHTC Studio servers. Sync is on by default and can be turned off in Settings.

### Can I turn off the confirmation before switching?

Yes. **Confirm before switch** is on by default to prevent mistaps; you can disable it in Settings.

### What languages does iStore support?

**English, 简体中文, and 繁體中文.** You can also choose how region names are displayed (region name display mode).

### Which devices are supported?

- **iPhone / iPad** — iOS 16.2+ (main app)
- **Configurable / interactive widgets** — iOS 17.0+
- **Control Center control & iPhone Search tab** — iOS 18.0+
- **Shortcuts & Siri** — iOS 16.2+

### Does iStore work offline?

Browsing and switching links work offline, but the **App Availability** check needs a network connection (it queries Apple's public lookup API). Your favorites, pinned regions, and history are saved on your device.

### How do I get iStore?

### How do I get iStore?

Download from the [App Store](https://apps.apple.com/app/id6786123132).

### Still need help?

Contact [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com). We typically respond within 48 hours.

</section>

<section lang="zh-CN" markdown="1">

### 地区切换是怎么实现的？

爱商店会打开你所选地区的 **App Store 官方跳转链接**，随后由 App Store 在 Apple 自己的界面上请你确认更改。爱商店不会看到你的 Apple ID、密码或支付信息。

### 需要登录吗？

不需要。爱商店**无需账号、无需登录**。只有在你确认切换时，才会在 Apple 自己的 App Store 界面上与你现有的 Apple ID 交互。

### 切换地区会退出登录或丢失已装 App 吗？

不会。切换商店地区只改变你浏览与购买所用的地区 App Store，已安装的 App 仍然保留。Apple 可能要求你的账单地区与支付方式匹配后，才能在新地区购买。

### 爱商店与 Apple 有关联吗？

没有。爱商店是 iHTC Studio 贡献者开发的独立工具，**与 Apple Inc. 无关联**，仅使用 Apple 官方跳转链接进行地区切换。

### 支持多少个地区？

**175 个地区**，横跨 7 大洲，每个地区含旗帜与本地化名称（英文 / 简体 / 繁体）。

### 上架查询是什么？

粘贴 **App Store 链接或数字 App ID**，爱商店通过 Apple 公开的 iTunes Lookup API 查询该 **App 在哪些地区上架**。查询范围可选**常用**、**收藏**或**全部**地区，然后可一键切换到任意可用地区。App 内与**分享扩展**均可使用。

### 如何从其他 App 查询上架？

在任意 App Store 链接上使用**分享**面板（Safari、信息、App Store 等），选择 **iStore**。分享扩展会查询常用地区，并可在 App 内打开结果进行切换。

### 收藏与置顶有什么区别？

**收藏**是你加星标的地区；**置顶**是收藏中你希望始终排在最前（商店、收藏与小组件中）的子集。取消收藏某地区时也会从置顶中移除。

### 地图选区是什么？

一张**全屏地图**，每个地区带有定位标记。范围可选常用、收藏或全部，点按标记即可切换——用地理方式直观探索各地商店。

### 有哪些小组件？

- **常用地区**与**最近**小组件（主屏与锁屏）
- 可自定义地区的**自定义**小组件（iOS 17+）
- **交互式小组件**（iOS 17+）——点按地区磁贴直接切换

### 控制中心控件是什么？

在 **iOS 18+** 上，可将**切换上次**控件添加到控制中心，一键再次切换到最近的目标地区。

### 能用 Siri 或快捷指令切换吗？

可以。爱商店提供 Siri 与快捷指令操作：**切换地区**、**切换上次**、**切换收藏**、**打开商店**或**查询上架**。详见 [快捷链接说明](url-scheme)。

### 支持 Spotlight 搜索吗？

支持。全部 175 个地区都会被索引到 **Spotlight**——在主屏搜索地区并点按结果，即可在爱商店中直接切换。

### iCloud 同步包含什么？

可选 iCloud 同步会在各设备间同步：**收藏**、**置顶地区**、**常用地区**、**切换历史**、**上次切换地区**以及外观 / 布局 / 收藏偏好。数据通过**你的私有 iCloud** 同步，不经过 iHTC Studio 服务器。默认开启，可在设置中关闭。

### 可以关闭切换前的确认吗？

可以。**切换前确认**默认开启以防误触，你可以在设置中关闭。

### 爱商店支持哪些语言？

**English、简体中文、繁體中文。** 你还可以选择地区名的显示方式（地区名显示模式）。

### 支持哪些设备？

- **iPhone / iPad** — iOS 16.2+（主应用）
- **可配置 / 交互式小组件** — iOS 17.0+
- **控制中心控件与 iPhone 搜索 Tab** — iOS 18.0+
- **快捷指令与 Siri** — iOS 16.2+

### 爱商店能离线使用吗？

浏览与切换链接可离线使用，但**上架查询**需要联网（调用 Apple 公开的查询 API）。你的收藏、置顶地区与历史保存在本机。

### 如何获取爱商店？

在 [App Store](https://apps.apple.com/app/id6786123132) 下载。

### 仍有问题？

联系 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)，我们通常在 48 小时内回复。

</section>

<section lang="zh-TW" markdown="1">

### 地區切換是怎麼實現的？

愛商店會開啟你所選地區的 **App Store 官方跳轉連結**，隨後由 App Store 在 Apple 自己的介面上請你確認更改。愛商店不會看到你的 Apple ID、密碼或付款資訊。

### 需要登入嗎？

不需要。愛商店**無需帳號、無需登入**。只有在你確認切換時，才會在 Apple 自己的 App Store 介面上與你現有的 Apple ID 互動。

### 切換地區會登出或遺失已裝 App 嗎？

不會。切換商店地區只改變你瀏覽與購買所用的地區 App Store，已安裝的 App 仍然保留。Apple 可能要求你的帳單地區與付款方式相符後，才能在新地區購買。

### 愛商店與 Apple 有關聯嗎？

沒有。愛商店是 iHTC Studio 貢獻者開發的獨立工具，**與 Apple Inc. 無關聯**，僅使用 Apple 官方跳轉連結進行地區切換。

### 支援多少個地區？

**175 個地區**，橫跨 7 大洲，每個地區含旗幟與本地化名稱（英文 / 簡體 / 繁體）。

### 上架查詢是什麼？

貼上 **App Store 連結或數字 App ID**，愛商店透過 Apple 公開的 iTunes Lookup API 查詢該 **App 在哪些地區上架**。查詢範圍可選**常用**、**收藏**或**全部**地區，然後可一鍵切換到任意可用地區。App 內與**分享延伸功能**均可使用。

### 如何從其他 App 查詢上架？

在任意 App Store 連結上使用**分享**面板（Safari、訊息、App Store 等），選擇 **iStore**。分享延伸功能會查詢常用地區，並可在 App 內開啟結果進行切換。

### 收藏與置頂有什麼區別？

**收藏**是你加星號的地區；**置頂**是收藏中你希望始終排在最前（商店、收藏與小工具中）的子集。取消收藏某地區時也會從置頂中移除。

### 地圖選區是什麼？

一張**全螢幕地圖**，每個地區帶有定位標記。範圍可選常用、收藏或全部，點按標記即可切換——用地理方式直觀探索各地商店。

### 有哪些小工具？

- **常用地區**與**最近**小工具（主畫面與鎖定畫面）
- 可自訂地區的**自訂**小工具（iOS 17+）
- **互動式小工具**（iOS 17+）——點按地區磁貼直接切換

### 控制中心控制項是什麼？

在 **iOS 18+** 上，可將**切換上次**控制項加入控制中心，一鍵再次切換到最近的目標地區。

### 能用 Siri 或捷徑切換嗎？

可以。愛商店提供 Siri 與捷徑操作：**切換地區**、**切換上次**、**切換收藏**、**開啟商店**或**查詢上架**。詳見 [快捷連結說明](url-scheme)。

### 支援 Spotlight 搜尋嗎？

支援。全部 175 個地區都會被索引到 **Spotlight**——在主畫面搜尋地區並點按結果，即可在愛商店中直接切換。

### iCloud 同步包含什麼？

可選 iCloud 同步會在各裝置間同步：**收藏**、**置頂地區**、**常用地區**、**切換歷史**、**上次切換地區**以及外觀 / 版面 / 收藏偏好。資料透過**你的私有 iCloud** 同步，不經過 iHTC Studio 伺服器。預設開啟，可在設定中關閉。

### 可以關閉切換前的確認嗎？

可以。**切換前確認**預設開啟以防誤觸，你可以在設定中關閉。

### 愛商店支援哪些語言？

**English、简体中文、繁體中文。** 你還可以選擇地區名的顯示方式（地區名顯示模式）。

### 支援哪些裝置？

- **iPhone / iPad** — iOS 16.2+（主應用）
- **可配置 / 互動式小工具** — iOS 17.0+
- **控制中心控制項與 iPhone 搜尋 Tab** — iOS 18.0+
- **捷徑與 Siri** — iOS 16.2+

### 愛商店能離線使用嗎？

瀏覽與切換連結可離線使用，但**上架查詢**需要連網（呼叫 Apple 公開的查詢 API）。你的收藏、置頂地區與歷史保存在本機。

### 如何取得愛商店？

在 [App Store](https://apps.apple.com/app/id6786123132) 下載。

### 仍有問題？

聯絡 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)，我們通常在 48 小時內回覆。

</section>
