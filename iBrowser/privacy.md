---
layout: doc
title: iBrowser — Privacy Policy
app_id: iBrowser
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iBrowser (全屏浏览器) — no account, on-device storage, optional Apple iCloud KVS, widgets via App Group.
---

<section lang="en" markdown="1">

**Last updated:** September 6, 2026

iHTC Studio ("we", "us" or "our"; formerly iHTCTeam) built **iBrowser** (also known as "全屏浏览器" / "全螢幕瀏覽器", Bundle ID `full.screen.browser`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on this page as the public privacy URL. For App Store Connect, open this [Privacy Policy](privacy) page and copy the address from the browser address bar.

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration or sign-in with iHTC Studio |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your bookmarks or settings |
| Advertising | **None** — no ads, no ad SDK, no App Tracking Transparency prompt for ads |
| Browsing content | Pages you open are loaded **directly by WebKit** from those sites; we do not operate a browsing proxy |
| Optional Apple sync | **iCloud Key-Value Storage** — off by default; only if you enable it in Settings |

## Data Collection

- **No account** — You can use the app without creating an account with us.
- **No advertising or analytics SDK** — The app does not show ads or phone home analytics to iHTC Studio.
- **No iHTC Studio backend for your bookmarks** — Preferences stay on your device (and optionally in **your** Apple iCloud). We do not host a server that receives your bookmark list.

### Web browsing

When you navigate to a website or use a search engine:

- Your device contacts **that site** (or search provider) over the network, as with any browser.
- Those third parties may see standard request metadata (IP address, user agent, cookies they set, page content you request). Their privacy policies apply.
- Choosing a built-in or custom **search engine** only sets a search URL prefix on device.

### Widgets, Shortcuts & deep links

Home Screen / Lock Screen widgets, Siri, Shortcuts, Home Screen quick actions, and `ibrowser://` links open destinations **on your device**. They do not send your browsing history to iHTC Studio.

## Data Stored on Your Device

| Data | Where | Purpose |
|------|-------|---------|
| Home page URL | UserDefaults (+ App Group snapshot) | Start page; widget display |
| Search engine prefix | UserDefaults | Address-bar search |
| Bookmarks | UserDefaults (JSON) (+ App Group snapshot) | Local favorites; bookmark widgets |
| Child lock / force-hide chrome | UserDefaults (+ App Group) | Immersive & kid / kiosk modes |
| Float ball on/off & menu order | UserDefaults | Shortcut affordance |
| Float ball **position** | UserDefaults (device only) | Where you left the ball — **not** synced to iCloud |
| Last successfully loaded page | UserDefaults (+ App Group) | “Continue last” — **device only**, not iCloud |
| Settings password | **Keychain** (`WhenUnlockedThisDeviceOnly`) | Optional Settings lock — **not** in UserDefaults, App Group, or iCloud |
| Browser margins | UserDefaults | Content insets |
| Appearance / language | UserDefaults (device only) | Theme & UI language — **not** iCloud |
| Home Screen quick-action order | UserDefaults (device only) | Long-press menu — **not** iCloud |
| First-run guide & terms flags | UserDefaults (device only) | Onboarding |
| Widget snapshots | App Group `group.full.screen.browser` | Read-only display for the widget extension |

Uninstalling the app removes its sandbox and App Group data (subject to iOS behavior). Optional iCloud copies remain in **your** iCloud until you clear them or turn sync off elsewhere.

## Optional iCloud Sync

If you enable **iCloud Sync** in Settings (default **off**), selected preferences mirror through Apple’s **`NSUbiquitousKeyValueStore`** tied to **your Apple ID**:

**May sync:** bookmarks, home page, search engine, margins, address-bar / toolbar display locks, float-ball on/off, float-ball menu order.

**Does not sync:** Settings password, last page (“continue last”), float-ball position, appearance, language, Home Screen quick-action order, guide / terms flags.

Sync traffic goes to **Apple iCloud**, not to iHTC Studio. You can disable sync or tap **Sync Now** in Settings. We cannot read your iCloud contents.

## Permissions

Web pages may request device capabilities through WebKit (for example camera, microphone, or location) depending on the site. System prompts appear only when a page asks. The app also declares capability strings that web content may need; we do not use those permissions for a separate native social or advertising feature.

| Area | Notes |
|------|--------|
| Network | Required to load websites and search |
| Motion (shake) | Used on **iPhone** to recover the float ball / chrome — processing stays local; **iPad** uses tap-near-top instead |
| iCloud | Only if you enable sync |
| Mail / Share Sheet | Optional feedback or share actions you initiate |
| StoreKit (optional tip) | Consumable tip processed by Apple; does not unlock features |

## Children’s Privacy

Child lock is a **local UI restriction** (hide address bar / optional Settings password). While it is on, widgets, Shortcuts, and non-home bookmarks open **home** instead. It does **not** create a child account with us. We do not knowingly solicit personal information from children for marketing. Parents should supervise which sites are opened.

## What We Do Not Do

- We do **not** require an iHTC Studio account.
- We do **not** show in-app advertisements or interstitial promo pop-ups (aside from the required first-run terms).
- We do **not** operate our own cloud sync servers for this app (optional sync uses **your** Apple iCloud only).
- We do **not** sell your data.
- We do **not** store the Settings password in plain UserDefaults (it uses Keychain on device).

## Third Parties

| Party | Role |
|-------|------|
| **Apple** | App Store distribution; optional iCloud KVS; widgets / Siri / Shortcuts; Mail, Share Sheet, Safari View Controller; optional StoreKit tip |
| **Websites & search engines you open** | Receive normal browser traffic for pages you visit |

## Retention & Deletion

Local preferences and bookmarks remain until you change or clear them, or uninstall the app. Optional iCloud data remains under Apple’s policies until you disable sync and/or clear it through Apple’s tools. Because we do not collect personal data on our servers, there is no account dataset for us to delete beyond answering your email.

## Changes to This Policy

We may update this page from time to time. The “Last updated” date above will change when we do. Continued use after changes means you accept the updated policy.

## Contact Us

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Open this [Privacy Policy](privacy) page in a browser and copy the address bar URL if you need the public link for App Store Connect.

</section>

<section lang="zh-CN" markdown="1">

**最近更新：** 2026 年 9 月 6 日

爱火腿肠工作室（iHTC Studio）（「我们」；原 iHTCTeam）开发了 **全屏浏览器**（iBrowser / 全螢幕瀏覽器，Bundle ID `full.screen.browser`）。本政策说明使用本应用时数据如何处理。可供 **Apple 审核**与用户作为公开隐私政策链接。如需向 App Store Connect 提供地址：打开本站 [隐私政策](privacy) 页，从浏览器地址栏复制当前网址。

## 摘要（对齐 Apple 隐私标签口径）

| 主题 | 做法 |
|------|------|
| 账号 | **不需要** — 无需向 iHTC Studio 注册或登录 |
| iHTC Studio 侧收集 | **Data Not Collected** — 我们**不**运营接收书签 / 设置的后端 |
| 广告 | **无** — 无广告、无广告 SDK、不为广告弹出 ATT |
| 浏览内容 | 你打开的网页由 **WebKit 直连**对应站点；我们不运行浏览代理 |
| 可选 Apple 同步 | **iCloud 键值存储** — 默认关闭；仅在你于设置中开启后生效 |

## 数据收集

- **无账号** — 无需注册即可使用。
- **无广告 / 分析 SDK** — 应用内不展示广告，也不向 iHTC Studio 回传分析数据。
- **书签不上传到 iHTC Studio 服务器** — 偏好保存在本机（以及可选的 **你的** Apple iCloud）。我们不为该书签列表运营回传服务器。

### 网页浏览

当你打开网站或使用搜索引擎时：

- 设备会像普通浏览器一样**直连该站点**（或搜索服务）。
- 对方可能看到常规请求元数据（IP、UA、其 Cookie、你请求的页面）。适用对方隐私政策。
- 选择内置或自定义**搜索引擎**，只是在本机设置搜索 URL 前缀。

### 小组件、快捷指令与深链

主屏 / 锁屏小组件、Siri、快捷指令、主屏长按与 `ibrowser://` 均在**本机**打开目标，不会把浏览历史发给 iHTC Studio。

## 本机存储

| 数据 | 位置 | 用途 |
|------|------|------|
| 主页 URL | UserDefaults（+ App Group 快照） | 启动页；小组件展示 |
| 搜索引擎前缀 | UserDefaults | 地址栏搜索 |
| 书签 | UserDefaults（JSON）（+ App Group 快照） | 本机收藏；书签小组件 |
| 儿童锁 / 强制隐藏控件 | UserDefaults（+ App Group） | 沉浸与看管场景 |
| 悬浮球开关与菜单顺序 | UserDefaults | 快捷入口 |
| 悬浮球**位置** | UserDefaults（仅本机） | 拖放位置 — **不同步** iCloud |
| 上次成功加载的页面 | UserDefaults（+ App Group） | 「继续上次」— **仅本机**，不同步 iCloud |
| 设置密码 | **钥匙串**（`WhenUnlockedThisDeviceOnly`） | 可选设置锁 — **不进** UserDefaults / App Group / iCloud |
| 浏览器边距 | UserDefaults | 内容内边距 |
| 外观 / 语言 | UserDefaults（仅本机） | 主题与界面语言 — **不同步** iCloud |
| 主屏长按顺序 | UserDefaults（仅本机） | 长按菜单 — **不同步** iCloud |
| 首次导览与条款标记 | UserDefaults（仅本机） | 引导 |
| 小组件快照 | App Group `group.full.screen.browser` | 供小组件扩展只读展示 |

卸载应用会按系统规则清除沙盒与 App Group 数据。可选 iCloud 副本仍保留在**你的** iCloud，直至你清除或关闭同步。

## 可选 iCloud 同步

若在设置中开启 **iCloud 同步**（默认**关闭**），部分偏好通过绑定 **你的 Apple ID** 的 Apple **`NSUbiquitousKeyValueStore`** 镜像：

**可同步：** 书签、主页、搜索引擎、边距、地址栏 / 底栏显示锁、悬浮球开关、悬浮球菜单顺序。

**不同步：** 设置密码、上次页面（「继续上次」）、悬浮球位置、外观、语言、主屏长按顺序、导览 / 条款标记。

同步流量走向 **Apple iCloud**，而非 iHTC Studio。可在设置中关闭同步或点「立即同步」。我们无法读取你的 iCloud 内容。

## 权限

网页可能通过 WebKit 请求相机、麦克风或定位等能力，仅在页面需要时由系统弹窗。应用声明了网页可能用到的用途说明；我们不用这些权限做独立的原生社交或广告功能。

| 范围 | 说明 |
|------|------|
| 网络 | 加载网页与搜索所必需 |
| 运动（摇一摇） | **iPhone** 上本机用于找回悬浮球 / 控件；**iPad** 改用点到顶 |
| iCloud | 仅在你开启同步时 |
| 邮件 / 分享 | 你主动发起的反馈或分享 |
| StoreKit（可选打赏） | Apple 处理的消耗型打赏；不解锁功能 |

## 儿童隐私

儿童锁是**本机界面限制**（隐藏地址栏 / 可选设置密码）。开启时，小组件、快捷指令与非主页书签会改开**主页**。它**不会**在我们这边创建儿童账号。我们不会为营销目的故意向儿童索取个人信息。家长应留意打开了哪些网站。

## 我们明确不做的事

- **不**要求 iHTC Studio 账号。
- **不**展示应用内广告或运营插屏（首次条款除外）。
- **不**为本应用运营自有云同步服务器（可选同步仅使用**你的** Apple iCloud）。
- **不**出售你的数据。
- **不**将设置密码明文存在 UserDefaults（本机钥匙串保存）。

## 第三方

| 主体 | 角色 |
|------|------|
| **Apple** | App Store 分发；可选 iCloud KVS；小组件 / Siri / 快捷指令；邮件、分享、Safari 视图；可选 StoreKit 打赏 |
| **你打开的网站与搜索引擎** | 接收正常浏览流量 |

## 保留与删除

本地偏好与书签保留至你修改、清除或卸载。可选 iCloud 数据按 Apple 政策保留，直至你关闭同步并/或通过 Apple 工具清除。因我们不在自有服务器收集个人数据，除回复邮件外没有可删除的账号数据集。

## 政策变更

我们可能不时更新本页，并修改上方「最近更新」日期。变更后继续使用即表示接受更新后的政策。

## 联系我们

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

如需向 App Store Connect 提供隐私政策地址：打开本站 [隐私政策](privacy) 页，从浏览器地址栏复制当前网址。

</section>

<section lang="zh-TW" markdown="1">

**最近更新：** 2026 年 9 月 6 日

愛火腿腸工作室（iHTC Studio）（「我們」；原 iHTCTeam）開發了 **全螢幕瀏覽器**（iBrowser / 全屏浏览器，Bundle ID `full.screen.browser`）。本政策說明使用本應用時資料如何處理。可供 **Apple 審核**與使用者作為公開隱私政策連結。如需向 App Store Connect 提供地址：打開本站 [隱私政策](privacy) 頁，從瀏覽器地址欄複製當前網址。

## 摘要（對齊 Apple 隱私標籤口徑）

| 主題 | 做法 |
|------|------|
| 帳號 | **不需要** — 無需向 iHTC Studio 註冊或登入 |
| iHTC Studio 側收集 | **Data Not Collected** — 我們**不**營運接收書籤 / 設定的後端 |
| 廣告 | **無** — 無廣告、無廣告 SDK、不為廣告彈出 ATT |
| 瀏覽內容 | 你打開的網頁由 **WebKit 直連**對應站點；我們不運行瀏覽代理 |
| 可選 Apple 同步 | **iCloud 鍵值儲存** — 預設關閉；僅在你於設定中開啟後生效 |

## 資料收集

- **無帳號** — 無需註冊即可使用。
- **無廣告 / 分析 SDK** — 應用內不展示廣告，也不向 iHTC Studio 回傳分析資料。
- **書籤不上傳到 iHTC Studio 伺服器** — 偏好保存在本機（以及可選的 **你的** Apple iCloud）。我們不為該書籤列表營運回傳伺服器。

### 網頁瀏覽

當你打開網站或使用搜尋引擎時：

- 裝置會像普通瀏覽器一樣**直連該站點**（或搜尋服務）。
- 對方可能看到常規請求中繼資料（IP、UA、其 Cookie、你請求的頁面）。適用對方隱私政策。
- 選擇內建或自訂**搜尋引擎**，只是在本機設定搜尋 URL 前綴。

### 小工具、捷徑與深鏈

主畫面 / 鎖定畫面小工具、Siri、捷徑、主畫面長按與 `ibrowser://` 均在**本機**打開目標，不會把瀏覽歷史發給 iHTC Studio。

## 本機儲存

| 資料 | 位置 | 用途 |
|------|------|------|
| 主頁 URL | UserDefaults（+ App Group 快照） | 啟動頁；小工具展示 |
| 搜尋引擎前綴 | UserDefaults | 網址列搜尋 |
| 書籤 | UserDefaults（JSON）（+ App Group 快照） | 本機收藏；書籤小工具 |
| 兒童鎖 / 強制隱藏控制項 | UserDefaults（+ App Group） | 沉浸與看管場景 |
| 懸浮球開關與選單順序 | UserDefaults | 快捷入口 |
| 懸浮球**位置** | UserDefaults（僅本機） | 拖放位置 — **不同步** iCloud |
| 上次成功載入的頁面 | UserDefaults（+ App Group） | 「繼續上次」— **僅本機**，不同步 iCloud |
| 設定密碼 | **鑰匙圈**（`WhenUnlockedThisDeviceOnly`） | 可選設定鎖 — **不進** UserDefaults / App Group / iCloud |
| 瀏覽器邊距 | UserDefaults | 內容內邊距 |
| 外觀 / 語言 | UserDefaults（僅本機） | 主題與介面語言 — **不同步** iCloud |
| 主畫面長按順序 | UserDefaults（僅本機） | 長按選單 — **不同步** iCloud |
| 首次導覽與條款標記 | UserDefaults（僅本機） | 引導 |
| 小工具快照 | App Group `group.full.screen.browser` | 供小工具擴充功能唯讀展示 |

解除安裝應用會依系統規則清除沙盒與 App Group 資料。可選 iCloud 副本仍保留在**你的** iCloud，直至你清除或關閉同步。

## 可選 iCloud 同步

若在設定中開啟 **iCloud 同步**（預設**關閉**），部分偏好透過綁定 **你的 Apple ID** 的 Apple **`NSUbiquitousKeyValueStore`** 鏡像：

**可同步：** 書籤、主頁、搜尋引擎、邊距、網址列 / 底欄顯示鎖、懸浮球開關、懸浮球選單順序。

**不同步：** 設定密碼、上次頁面（「繼續上次」）、懸浮球位置、外觀、語言、主畫面長按順序、導覽 / 條款標記。

同步流量走向 **Apple iCloud**，而非 iHTC Studio。可在設定中關閉同步或點「立即同步」。我們無法讀取你的 iCloud 內容。

## 權限

網頁可能透過 WebKit 請求相機、麥克風或定位等能力，僅在頁面需要時由系統彈窗。應用宣告了網頁可能用到的用途說明；我們不用這些權限做獨立的原生社交或廣告功能。

| 範圍 | 說明 |
|------|------|
| 網路 | 載入網頁與搜尋所必需 |
| 運動（搖一搖） | **iPhone** 上本機用於找回懸浮球 / 控制項；**iPad** 改用點到頂 |
| iCloud | 僅在你開啟同步時 |
| 郵件 / 分享 | 你主動發起的回饋或分享 |
| StoreKit（可選打賞） | Apple 處理的消耗型打賞；不解鎖功能 |

## 兒童隱私

兒童鎖是**本機介面限制**（隱藏網址列 / 可選設定密碼）。開啟時，小工具、捷徑與非主頁書籤會改開**主頁**。它**不會**在我們這邊建立兒童帳號。我們不會為行銷目的故意向兒童索取個人資訊。家長應留意打開了哪些網站。

## 我們明確不做的事

- **不**要求 iHTC Studio 帳號。
- **不**展示應用內廣告或營運插屏（首次條款除外）。
- **不**為本應用營運自有雲同步伺服器（可選同步僅使用**你的** Apple iCloud）。
- **不**出售你的資料。
- **不**將設定密碼明文存在 UserDefaults（本機鑰匙圈保存）。

## 第三方

| 主體 | 角色 |
|------|------|
| **Apple** | App Store 分發；可選 iCloud KVS；小工具 / Siri / 捷徑；郵件、分享、Safari 檢視；可選 StoreKit 打賞 |
| **你打開的網站與搜尋引擎** | 接收正常瀏覽流量 |

## 保留與刪除

本地偏好與書籤保留至你修改、清除或解除安裝。可選 iCloud 資料按 Apple 政策保留，直至你關閉同步並/或透過 Apple 工具清除。因我們不在自有伺服器收集個人資料，除回覆郵件外沒有可刪除的帳號資料集。

## 政策變更

我們可能不時更新本頁，並修改上方「最近更新」日期。變更後繼續使用即表示接受更新後的政策。

## 聯絡我們

- **電子郵件：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

如需向 App Store Connect 提供隱私政策地址：打開本站 [隱私政策](privacy) 頁，從瀏覽器地址欄複製當前網址。

</section>
