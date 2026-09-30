---
layout: doc
title: iWidget — Privacy Policy
app_id: iWidget
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iWidget (爱组件) — widget designer, on-device designs, optional iCloud, WeatherKit & HealthKit when enabled.
---

<section lang="en" markdown="1">

**Last updated:** September 30, 2026

iHTC Studio ("we", "us" or "our"; formerly iHTCTeam) built **iWidget** (also known as "爱组件" / "愛組件", Bundle ID `com.iHTCboy.iWidget`). This Privacy Policy explains what data is (and is not) handled when you use the app and its widget extension. **Apple App Review** and users may rely on this page as the public privacy policy. For App Store Connect, open this [Privacy Policy](../privacy) page in your browser and copy the address from the address bar (the public site domain may change over time).

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration or sign-in with iHTC Studio |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your widget designs, wallpapers, or calendar data |
| Advertising / analytics | **None** — no ads, no third-party analytics or tracking SDKs |
| Core calendar & almanac | Computed **on device** from bundled tables; optional holiday JSON may be fetched from a public GitHub mirror (see below) |
| Weather | **Apple WeatherKit** when you enable weather blocks or Today weather — requests go to **Apple**, not iHTC Studio |
| Optional Apple services | **iCloud (CloudKit)** for design sync, **HealthKit** (read steps/distance), **Location When In Use** (or manual city), **local notifications**, **Background App Refresh** task |

## Data Collection

- **No account** — You can use the app without creating an account with us.
- **No advertising or analytics SDK** — The app does not show ads or send usage analytics to iHTC Studio.
- **No iHTC Studio cloud for your designs** — Widget layouts, cropped wallpapers, countdowns, and caches live in the **App Group** on your device (and optionally in **your** iCloud container). We do not host a server that stores your boards.

## Network Use

| Feature | What happens |
|---------|----------------|
| **WeatherKit** | Your device asks Apple for forecast data for your chosen location or city. Weather UI shows **Apple Weather** attribution where required. |
| **Statutory holiday updates** | The app may download public holiday JSON (e.g. from the open **holiday-cn** project) roughly every few days to refresh work/rest marks. No personal identifiers are sent by us. |
| **Optional open-source fonts** | Smiley Sans / LXGW WenKai may be downloaded to App Group storage when you pick those typefaces. |
| **Tip Developer** | Optional **StoreKit** consumable processed by Apple. We do not receive payment card numbers. |
| **Feedback email** | If you choose **Send feedback**, Mail compose may attach non-secret diagnostics (version, device model). You control sending. |

All other features — lunar calendar, almanac, editor, previews, widgets (except live weather fetch), notifications scheduling — work **offline** after install.

## Data Stored on Your Device (App Group)

Design files, caches, and preferences are stored under App Group `group.com.iHTCboy.iWidget`, for example:

| Data | Purpose |
|------|---------|
| `designs/*.json` | Saved widget board layouts |
| `images/*`, `wallpaper/*` | Cropped wallpaper slots (light/dark) |
| `countdowns/items.json` | Countdown list |
| `cache/weather.json` | Weather snapshot cache |
| `cache/battery.json`, `cache/storage.json`, `cache/music.json`, `cache/steps.json` | Device block snapshots (iOS) |
| `cache/holidays/{year}.json` | Downloaded statutory holiday tables |
| UserDefaults keys | Language, theme, festival filters, widget session cursors, stale design IDs, etc. |

Uninstalling the app removes sandbox and App Group data subject to iOS/macOS behavior.

## iCloud Sync (Optional, Off by Default)

When you enable **iCloud** in Settings, the app uses **CloudKit** private database `iCloud.com.iHTCboy.iWidget` (zone **Designs**) via `CKSyncEngine` to sync:

- Design JSON summaries and full documents
- Cropped wallpaper assets associated with designs

Traffic goes to **Apple iCloud** under **your Apple ID**. We cannot read your iCloud contents. Turning iCloud off stops sync; local copies remain on device until you delete them.

## Permissions

| Permission | When | Why |
|------------|------|-----|
| **Location When In Use** | You enable location-based weather | Resolve city for WeatherKit; you may use **manual city** instead |
| **HealthKit (read)** | You enable step blocks | Read today’s steps / walking distance for widget display |
| **Apple Music / Media** | Now Playing block | Read currently playing title & artwork (Info.plist usage strings) |
| **Notifications** | You enable reminder categories | Schedule local holiday / countdown / workday reminders |
| **Background App Refresh** | System allows | Periodic refresh of weather/device caches (~6 h) |
| **iCloud** | You toggle sync | Design backup across your devices |

We do **not** request Contacts, Camera, Microphone recording, or App Tracking Transparency for ads.

## Widget Extension

The widget extension reads the **same App Group** as the app. It renders the design you selected in the widget configuration UI. Interactive intents (refresh weather, cycle countdown, shift month) run on device. Weather fetches in widgets are time-limited (e.g. ~8 s) and may use cached data on failure.

## Privacy Manifest

The app ships `PrivacyInfo.xcprivacy` declaring **UserDefaults** access for reason **CA92.1** (app functionality).

## Children’s Privacy

We do not knowingly collect personal information from children. Because we do not operate a data collection backend for this app, no special child account is required.

## Changes

We may update this policy. Material changes will be reflected on this page with an updated date.

## Contact

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>

<section lang="zh-CN" markdown="1">

**最后更新：** 2026 年 9 月 30 日

爱火腿肠工作室（iHTC Studio）（「我们」；原 iHTCTeam）开发了 **爱组件**（iWidget / 愛組件，Bundle ID `com.iHTCboy.iWidget`）。本隐私政策说明你在使用主 App 与小组件扩展时，数据如何被处理。本页可供 **App Store 审核**与用户查阅。填写 App Store Connect 时：打开本站 [隐私政策](../privacy) 页，从浏览器地址栏复制当前网址（站点域名日后可能变更）。

## 概要（与 Apple 隐私标签对齐）

| 主题 | 做法 |
|------|------|
| 账号 | **不需要** — 无需向爱火腿肠工作室注册或登录 |
| 我们侧数据收集 | **Data Not Collected** — **不**运营接收你的设计、壁纸或日历内容的后端 |
| 广告 / 统计 | **无** — 无广告、无第三方分析或追踪 SDK |
| 日历与黄历 | **本机离线**计算；法定调休数据可能从公开 GitHub 镜像按需下载 |
| 天气 | 启用天气相关能力时使用 **Apple WeatherKit**，请求发往 **Apple** |
| 可选 Apple 服务 | **iCloud（CloudKit）** 同步设计、**HealthKit**（读步数/距离）、**使用期间定位**（或手动城市）、**本地通知**、**后台刷新**任务 |

## 数据收集

- **无账号** — 无需创建我们侧账号即可使用。
- **无广告或分析 SDK** — 不向爱火腿肠工作室上报使用统计。
- **无设计云备份（我们侧）** — 看板布局、裁切壁纸、倒数与缓存保存在 **App Group**（及可选 **你的 iCloud**）。

## 网络使用

| 功能 | 说明 |
|------|------|
| **WeatherKit** | 设备向 Apple 请求所选位置/城市的预报；界面按要求展示 **Apple Weather** 标识。 |
| **法定假日更新** | 可能每隔数日下载公开 holiday JSON（如 holiday-cn 项目），用于刷新休/班标记；我们不附带个人标识。 |
| **开源字体** | 选择特定字体时可能下载到 App Group（如得意黑、霞鹜文楷）。 |
| **开发者赞赏** | 可选 **StoreKit** 消耗型，由 Apple 处理支付。 |
| **反馈邮件** | 你选择发送时，邮件可能附带版本、机型等非敏感诊断信息。 |

除上述外，农历、黄历、编辑器、预览、小组件渲染（除实时天气拉取）、通知调度等均在安装后 **可离线** 使用。

## 本机存储（App Group）

数据位于 App Group `group.com.iHTCboy.iWidget`，例如：

| 数据 | 用途 |
|------|------|
| `designs/*.json` | 已保存的小组件看板 |
| `images/*`、`wallpaper/*` | 深浅色壁纸槽位裁切图 |
| `countdowns/items.json` | 倒数日列表 |
| `cache/weather.json` 等 | 天气与设备积木缓存 |
| `cache/holidays/{year}.json` | 下载的法定调休表 |
| UserDefaults | 语言、主题、节日筛选、小组件会话游标等 |

卸载 App 将按系统规则删除沙盒与 App Group 数据。

## iCloud 同步（可选，默认关）

在设置中开启 **iCloud** 后，通过 **CloudKit** 私有库 `iCloud.com.iHTCboy.iWidget`（**Designs** 区域）同步设计 JSON 与关联裁切壁纸。流量走 **你的 Apple ID** 的 iCloud；我们无法读取你的 iCloud 内容。关闭后停止同步，本机副本仍保留直至你删除。

## 权限

| 权限 | 触发时机 | 用途 |
|------|----------|------|
| **使用期间定位** | 启用定位天气 | WeatherKit 解析城市；可改用手动选城市 |
| **HealthKit（读）** | 启用步数积木 | 读取今日步数/步行距离 |
| **媒体与 Apple Music** | 正在播放积木 | 读取当前播放信息与封面 |
| **通知** | 开启提醒类别 | 本地调度调休/节日/节气/倒数提醒 |
| **后台 App 刷新** | 系统允许 | 约 6 小时刷新天气/设备等缓存 |
| **iCloud** | 你打开同步开关 | 跨设备备份设计 |

**不**请求通讯录、相机、麦克风录音或用于广告的 ATT。

## 小组件扩展

扩展与主 App 共用 **App Group**，渲染你在系统小组件配置里选择的设计。交互 Intent（刷新天气、切换倒数、翻月等）在本机执行；扩展内拉天气有时间上限，失败时可回退缓存。

## 隐私清单

App 内置 `PrivacyInfo.xcprivacy`，声明因 **CA92.1**（App 功能）访问 **UserDefaults**。

## 儿童隐私

我们不会有意收集儿童个人信息；本 App 不运营用户数据后端。

## 政策变更

我们可能更新本页，并在文首更新日期。

## 联系

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>

<section lang="zh-TW" markdown="1">

**最後更新：** 2026 年 9 月 30 日

愛火腿腸工作室（iHTC Studio）（「我們」；原 iHTCTeam）開發了 **愛組件**（iWidget / 爱组件，Bundle ID `com.iHTCboy.iWidget`）。本隱私政策說明你在使用主 App 與小工具延伸功能時，資料如何被處理。本頁可供 **App Store 審核**與使用者查閱。填寫 App Store Connect 時：打開本站 [隱私政策](../privacy) 頁，從瀏覽器網址列複製目前網址（站點網域日後可能變更）。

## 概要（與 Apple 隱私標籤對齊）

| 主題 | 做法 |
|------|------|
| 帳號 | **不需要** — 無需向愛火腿腸工作室註冊或登入 |
| 我們側資料收集 | **Data Not Collected** — **不**營運接收你的設計、桌布或日曆內容的後端 |
| 廣告 / 統計 | **無** — 無廣告、無第三方分析或追蹤 SDK |
| 日曆與黃曆 | **本機離線**計算；法定調休資料可能從公開 GitHub 鏡像按需下載 |
| 天氣 | 啟用天氣相關能力時使用 **Apple WeatherKit**，請求送往 **Apple** |
| 可選 Apple 服務 | **iCloud（CloudKit）** 同步設計、**HealthKit**（讀步數/距離）、**使用期間定位**（或手動城市）、**本地通知**、**背景重新整理**任務 |

## 資料收集

- **無帳號** — 無需建立我們側帳號即可使用。
- **無廣告或分析 SDK** — 不向愛火腿腸工作室上報使用統計。
- **無設計雲備份（我們側）** — 看板版面、裁切桌布、倒數與快取保存在 **App Group**（及可選 **你的 iCloud**）。

## 網路使用

| 功能 | 說明 |
|------|------|
| **WeatherKit** | 裝置向 Apple 請求所選位置/城市的預報；介面按要求展示 **Apple Weather** 標示。 |
| **法定假日更新** | 可能每隔數日下載公開 holiday JSON（如 holiday-cn 專案），用於更新休/班標記。 |
| **開源字體** | 選擇特定字體時可能下載到 App Group。 |
| **開發者打賞** | 可選 **StoreKit** 消耗型，由 Apple 處理付款。 |
| **反馈郵件** | 你選擇傳送時，郵件可能附版本、機型等非敏感診斷資訊。 |

除上述外，農曆、黃曆、編輯器、預覽、小工具渲染（除即時天氣拉取）、通知排程等均在安裝後 **可離線** 使用。

## 本機儲存（App Group）

資料位於 App Group `group.com.iHTCboy.iWidget`，例如：`designs/*.json`、裁切桌布、倒數列表、天氣/裝置快取、調休表與 UserDefaults 偏好。

卸載 App 將依系統規則刪除沙盒與 App Group 資料。

## iCloud 同步（可選，預設關）

開啟 **iCloud** 後，透過 **CloudKit** 私有庫同步設計 JSON 與裁切桌布；流量走 **你的 Apple ID** 的 iCloud。關閉後停止同步。

## 權限

定位（使用期間）或手動城市、HealthKit 讀取步數、媒體/Apple Music（正在播放）、通知、背景重新整理、iCloud — 均仅在对应功能开启时使用。**不**請求通訊錄、相機、麥克風錄音或用于廣告的 ATT。

## 小工具延伸功能

與主 App 共用 **App Group**；互動 Intent 在本機執行；拉取天氣有時間上限並可回退快取。

## 隱私清單

App 內含 `PrivacyInfo.xcprivacy`，声明因 **CA92.1** 存取 **UserDefaults**。

## 兒童隱私

我們不會有意收集兒童個人資訊。

## 政策變更

我們可能更新本頁並調整日期。

## 聯絡

- **信箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
