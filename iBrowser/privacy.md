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

iHTC Studio ("we", "us" or "our") built **iBrowser** (also known as "全屏浏览器" / "全螢幕瀏覽器", Bundle ID `full.screen.browser`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on this page as the public privacy URL. For App Store Connect, open this [Privacy Policy](../privacy) page and copy the address from the browser address bar.

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

Open this [Privacy Policy](../privacy) page in a browser and copy the address bar URL if you need the public link for App Store Connect.

</section>
<section lang="zh-CN" markdown="1">

**最近更新：** 2026 年 9 月 6 日

爱火腿肠工作室（iHTC Studio）（「我们」）开发了 **全屏浏览器**（iBrowser / 全螢幕瀏覽器，Bundle ID `full.screen.browser`）。本政策说明使用本应用时数据如何处理。可供 **Apple 审核**与用户作为公开隐私政策链接。如需向 App Store Connect 提供地址：打开本站 [隐私政策](../privacy) 页，从浏览器地址栏复制当前网址。

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

如需向 App Store Connect 提供隐私政策地址：打开本站 [隐私政策](../privacy) 页，从浏览器地址栏复制当前网址。

</section>
<section lang="zh-TW" markdown="1">

**最近更新：** 2026 年 9 月 6 日

愛火腿腸工作室（iHTC Studio）（「我們」）開發了 **全螢幕瀏覽器**（iBrowser / 全屏浏览器，Bundle ID `full.screen.browser`）。本政策說明使用本應用時資料如何處理。可供 **Apple 審核**與使用者作為公開隱私政策連結。如需向 App Store Connect 提供地址：打開本站 [隱私政策](../privacy) 頁，從瀏覽器地址欄複製當前網址。

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

如需向 App Store Connect 提供隱私政策地址：打開本站 [隱私政策](../privacy) 頁，從瀏覽器地址欄複製當前網址。

</section>
<section lang="ja" markdown="1">

**最終更新日:** 2026 年 9 月 6 日

 iHTC Studio (「当社」、「当社」、または「当社の」) は **iBrowser** (「全屏浏览器」 / 「全螢幕瀏覽器」、バンドル ID `full.screen.browser` とも呼ばれます) をビルドしました。 このプライバシー ポリシーでは、アプリを使用するときにどのようなデータが処理される (および扱われない) かについて説明します。 **Apple App Review** およびユーザーは、このページをパブリック プライバシー URL として利用できます。 App Store Connect の場合は、この [プライバシー ポリシー](../privacy) ページを開き、ブラウザのアドレス バーからアドレスをコピーします。 

## 概要 (Apple プライバシー栄養ラベルの調整)

 | トピック | 私たちの実践 |
 |------|----------------|
 | アカウント | **不要** — iHTC Studio への登録やサインインは必要ありません |
 | iHTC Studioによるデータ収集 | **データは収集されません** - 当社はあなたのブックマークや設定を受信するバックエンドを**操作しません** |
 | 広告 | **なし** - 広告なし、広告 SDK なし、広告の App Tracking Transparency プロンプトなし |
 | コンテンツの閲覧 | 開いたページは、**WebKit によってこれらのサイトから直接**読み込まれます。 私たちはブラウジングプロキシを運用していません。 
| オプションの Apple 同期 | **iCloud Key-Value ストレージ** — デフォルトではオフです。 設定 | で有効にした場合のみ。 

## データ収集

- **アカウントなし** — アカウントを作成しなくてもアプリを使用できます。 
- **広告や分析 SDK はありません** - アプリは、iHTC Studio に広告やテレホン ホーム分析を表示しません。 
- **ブックマーク用の iHTC Studio バックエンドはありません** - 設定はデバイス (およびオプションで **あなたの** Apple iCloud) に残ります。 当社は、ブックマーク リストを受信するサーバーをホストしていません。 

### Web ブラウジング

 Web サイトに移動するとき、または検索エンジンを使用するとき:

 - 他のブラウザと同様に、デバイスはネットワーク経由で **そのサイト** (または検索プロバイダー) に接続します。 
- これらの第三者は、標準のリクエスト メタデータ (IP アドレス、ユーザー エージェント、設定した Cookie、ユーザーがリクエストしたページ コンテンツ) を参照する可能性があります。 プライバシー ポリシーが適用されます。 
- 組み込みまたはカスタム **検索エンジン**を選択すると、デバイスに検索 URL プレフィックスが設定されるだけです。 

### ウィジェット、ショートカット、ディープリンク

 ホーム画面/ロック画面ウィジェット、Siri、ショートカット、ホーム画面のクイック アクション、`ibrowser://` リンクにより、**デバイス上**の目的地が開きます。 閲覧履歴は iHTC Studio に送信されません。 

## デバイスに保存されているデータ

| データ | どこ | 目的 |
 |------|-------|-----------|
 | ホームページの URL | UserDefaults (+ アプリ グループのスナップショット) | スタートページ; ウィジェット表示 |
 | 検索エンジンのプレフィックス | ユーザーデフォルト | アドレスバー検索 |
 | ブックマーク | UserDefaults (JSON) (+ アプリ グループのスナップショット) | 地元のお気に入り。 ブックマークウィジェット |
 | チャイルドロック / 強制非表示クロム | UserDefaults (+ アプリグループ) | イマーシブ & キッズ / キオスク モード |
 | フロートボールのオン/オフとメニューの注文 | ユーザーデフォルト | ショートカット アフォーダンス |
 | フロートボール **位置** | UserDefaults (デバイスのみ) | ボールを置いた場所 — **未同期** iCloud |
 | 最後に正常にロードされたページ | UserDefaults (+ アプリグループ) | 「最後に続行」 — **デバイスのみ**、iCloud ではありません |
 | 設定パスワード | **キーホルダー** (`WhenUnlockedThisDeviceOnly`) | オプションの設定ロック — UserDefaults、App Group、または iCloud では**ではありません** |
 | ブラウザの余白 | ユーザーデフォルト | コンテンツのインセット |
 | 容姿・言語 | UserDefaults (デバイスのみ) | テーマと UI 言語 — **非対応** iCloud |
 | ホーム画面のクイックアクションの順序 | UserDefaults (デバイスのみ) | 長押しメニュー — **非対応** iCloud |
 | 初回版ガイドと規約フラグ | UserDefaults (デバイスのみ) | オンボーディング |
 | ウィジェットのスナップショット | アプリグループ `group.full.screen.browser` | ウィジェット拡張機能の読み取り専用表示 |

アプリをアンインストールすると、そのサンドボックスとアプリ グループのデータが削除されます (iOS の動作の影響を受けます)。 オプションの iCloud コピーは、クリアするか他の場所で同期をオフにするまで、**あなたの** iCloud に残ります。 

## オプションの iCloud 同期

 設定で**iCloud同期**を有効にすると（デフォルトは**オフ**）、選択した設定は**Apple ID**に関連付けられたAppleの**`NSUbiquitousKeyValueStore`**を介してミラーリングされます。 

**同期する可能性があるもの:** ブックマーク、ホームページ、検索エンジン、余白、アドレス バー/ツールバーの表示ロック、フロート ボールのオン/オフ、フロート ボールのメニュー順序。 

**同期しません:** 設定パスワード、最後のページ (「最後に続ける」)、フロート ボールの位置、外観、言語、ホーム画面のクイック アクションの順序、ガイド/用語フラグ。 

同期トラフィックは iHTC Studio ではなく **Apple iCloud** に送信されます。 同期を無効にするか、[設定] で [**今すぐ同期**] をタップすることができます。 iCloud のコンテンツを読み取ることができません。 

## 権限

 Web ページは、サイトによっては WebKit を通じてデバイス機能 (カメラ、マイク、位置情報など) を要求する場合があります。 システム プロンプトは、ページで要求された場合にのみ表示されます。 アプリは、Web コンテンツに必要な可能性のある機能文字列も宣言します。 これらの権限を別のネイティブ ソーシャル機能または広告機能に使用することはありません。

| 項目 | 注意事項 |
|------|--------|
| ネットワーク | ウェブサイトの読み込みや検索に必要 |
| モーション（振動） | **iPhone** ではフロートボール / Chrome を復元するために使用 — 処理はローカルで行われます；**iPad** では代わりに画面上部近くのタップを使用 |
| iCloud | 同期を有効にした場合のみ |
| メール / 共有シート | フィードバックや共有アクションを実行したい場合にオプション |
| StoreKit（任意のチップ） | Apple によって処理される消費型チップ；機能はアンロックされません |

## 子どものプライバシー

チャイルドロックは**ローカルのUI制限**です（アドレスバーを非表示 / 設定のパスワードは任意）。オンになっている間、ウィジェット、ショートカット、およびホーム以外のブックマークは**ホーム**を開きます。これは当社で子ども用アカウントを作成するものではありません。マーケティング目的で子どもから個人情報を意図的に取得することはありません。親はどのサイトが開かれるか監督する必要があります。

## 私たちが行わないこと

- iHTC Studio アカウントは**必要ありません**。 
- アプリ内広告やインタースティシャル プロモーション ポップアップは**表示されません** (必須の初回実行条件を除く)。 
- 当社は、このアプリ用に独自のクラウド同期サーバーを運用しません** (オプションの同期では、**お客様の** Apple iCloud のみを使用します)。 
- 私たちはあなたのデータを**販売しません**。 
- 設定パスワードをプレーンな UserDefaults に保存しません** (デバイス上のキーチェーンを使用します)。 

## サードパーティ

 | パーティー | 役割 |
 |------|------|
 | **アップル** | App Storeでの配布。 オプションの iCloud KVS; ウィジェット / Siri / ショートカット; メール、シート共有、Safari View コントローラー; オプションの StoreKit ヒント |
 | **あなたが開いているウェブサイトと検索エンジン** | アクセスしたページの通常のブラウザ トラフィックを受信する |

 ## 保持と削除

 ローカル設定とブックマークは、変更またはクリアするか、アプリをアンインストールするまで残ります。 オプションの iCloud データは、Apple のツールを通じて同期を無効にするかクリアするまで、Apple のポリシーに従って残ります。 当社はサーバー上で個人データを収集しないため、メールに返信する以外に削除できるアカウント データセットはありません。 

## このポリシーの変更

このページは随時更新されることがあります。上記の「最終更新日」は、更新が行われると変更されます。変更後も継続して使用する場合は、更新されたポリシーに同意したものとみなされます。

## お問い合わせ

- **メール:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

App Store Connect 用の公開リンクが必要な場合は、この [プライバシーポリシー](../privacy) ページをブラウザで開き、アドレスバーの URL をコピーしてください。

</section>
<section lang="ko" markdown="1">

**최종 업데이트:** 2026년 9월 6일 

iHTC Studio("당사", "당사" 또는 "당사")는 **iBrowser**("전체屏浏览器" / "전체螢幕瀏覽器", 번들 ID `full.screen.browser`라고도 함)를 구축했습니다. 본 개인정보 보호정책은 귀하가 앱을 사용할 때 처리되는 데이터와 처리되지 않는 데이터에 대해 설명합니다. **Apple App Review** 및 사용자는 이 페이지를 공개 개인 정보 보호 URL로 사용할 수 있습니다. App Store Connect의 경우 이 [개인정보 보호정책](../privacy) 페이지를 열고 브라우저 주소 표시줄에서 주소를 복사하세요. 

## 요약(Apple 개인 정보 보호 영양 라벨 정렬) 

| 주제 | 우리의 실천 | 
|-------|---| 
| 계정 | **필요하지 않음** — iHTC Studio에 등록하거나 로그인할 필요가 없습니다 | 
| iHTC Studio를 통한 데이터 수집 | **데이터가 수집되지 않음** — 당사는 귀하의 북마크나 설정을 수신하는 백엔드를 운영하지 **않습니다** | 
| 광고 | **없음** — 광고 없음, 광고 SDK 없음, 광고에 대한 앱 추적 투명성 메시지 없음 | 
| 콘텐츠 탐색 | 귀하가 여는 페이지는 해당 사이트에서 **WebKit에 의해 직접** 로드됩니다. 우리는 브라우징 프록시를 운영하지 않습니다 | 
| 선택적 Apple 동기화 | **iCloud 키-값 저장소** — 기본적으로 꺼져 있습니다. 설정 | 

## 데이터 수집

- **계정 없음** — 계정을 만들지 않고도 앱을 사용할 수 있습니다. 
- **광고 또는 분석 SDK 없음** — 앱은 iHTC Studio에 광고 또는 Phone Home 분석을 표시하지 않습니다. 
- **북마크용 iHTC Studio 백엔드 없음** — 기본 설정은 기기에 유지됩니다(선택적으로 **귀하의** Apple iCloud에도 있음). 우리는 귀하의 북마크 목록을 수신하는 서버를 호스팅하지 않습니다. 

### 웹 탐색 

웹사이트를 탐색하거나 검색 엔진을 사용할 때: 

- 귀하의 장치는 다른 브라우저와 마찬가지로 네트워크를 통해 **해당 사이트**(또는 검색 공급자)에 접속합니다. 
- 해당 제3자는 표준 요청 메타데이터(IP 주소, 사용자 에이전트, 그들이 설정한 쿠키, 귀하가 요청한 페이지 콘텐츠)를 볼 수 있습니다. 해당 개인정보 보호정책이 적용됩니다. 
- 내장 또는 맞춤 **검색 엔진**을 선택하면 기기에 검색 URL 접두어만 설정됩니다. 

### 위젯, 바로가기 및 딥 링크 

홈 화면/잠금 화면 위젯, Siri, 바로가기, 홈 화면 빠른 동작 및 `ibrowser://` 링크는 **기기**에서 대상을 엽니다. 그들은 귀하의 검색 기록을 iHTC Studio로 보내지 않습니다. 

## 귀하의 기기에 저장된 데이터

| 데이터 | 어디 | 목적 | 
|------|-------|---------| 
| 홈페이지 URL | UserDefaults(+ 앱 그룹 스냅샷) | 시작 페이지; 위젯 표시 | 
| 검색 엔진 접두사 | 사용자 기본값 | 주소 표시줄 검색 | 
| 북마크 | UserDefaults(JSON)(+ 앱 그룹 스냅샷) | 지역 즐겨찾기; 북마크 위젯 | 
| 어린이 잠금/강제 숨기기 크롬 | UserDefaults(+ 앱 그룹) | 몰입형 및 어린이/키오스크 모드 | 
| 플로트볼 온/오프 및 메뉴 순서 | 사용자 기본값 | 바로가기 어포던스 | 
| 플로트 볼 **위치** | UserDefaults(장치에만 해당) | 공을 떠난 곳 — iCloud와 동기화되지 **않음** | 
| 마지막으로 성공적으로 로드된 페이지 | UserDefaults(+ 앱 그룹) | "마지막에 계속" — iCloud가 아닌 **기기에만 해당** | 
| 설정 비밀번호 | **키체인** (`WhenUnlockedThisDeviceOnly`) | 선택적 설정 잠금 - UserDefaults, 앱 그룹 또는 iCloud | 
| 브라우저 여백 | 사용자 기본값 | 콘텐츠 삽입 | 
| 외관 / 언어 | UserDefaults(장치에만 해당) | 테마 및 UI 언어 — **iCloud 아님** | 
| 홈 화면 빠른 작업 순서 | UserDefaults(장치에만 해당) | 길게 누르기 메뉴 - **아님** iCloud | 
| 첫 실행 가이드 및 용어 플래그 | UserDefaults(장치에만 해당) | 온보딩 | 
| 위젯 스냅샷 | 앱 그룹 `group.full.screen.browser` | 위젯 확장에 대한 읽기 전용 표시 |

앱을 제거하면 해당 샌드박스 및 앱 그룹 데이터가 제거됩니다(iOS 동작에 따라 다름). 선택적인 iCloud 사본은 귀하가 이를 지우거나 다른 곳에서 동기화를 끌 때까지 **귀하의** iCloud에 남아 있습니다. 

## iCloud 동기화 옵션 

설정에서 **iCloud 동기화**를 활성화하면(기본값은 **꺼짐**) 선택한 환경설정이 **Apple ID**에 연결된 Apple의 **`NSUbiquitousKeyValueStore`**를 통해 미러링됩니다. 

**동기화 가능:** 북마크, 홈 페이지, 검색 엔진, 여백, 주소 표시줄/도구 모음 표시 잠금, 플로트 볼 켜기/끄기, 플로트 볼 메뉴 순서. 

**동기화되지 않음:** 비밀번호, 마지막 페이지(“마지막에 계속”), 플로트 볼 위치, 모양, 언어, 홈 화면 빠른 작업 순서, 가이드/용어 플래그를 설정합니다. 

동기화 트래픽은 iHTC Studio가 아닌 **Apple iCloud**로 이동합니다. 동기화를 비활성화하거나 설정에서 **지금 동기화**를 탭할 수 있습니다. 귀하의 iCloud 콘텐츠를 읽을 수 없습니다. 

## 권한 

웹 페이지는 사이트에 따라 WebKit(예: 카메라, 마이크 또는 위치)을 통해 장치 기능을 요청할 수 있습니다. 시스템 프롬프트는 페이지에서 요청할 때만 나타납니다. 또한 앱은 웹 콘텐츠에 필요할 수 있는 기능 문자열을 선언합니다. 당사는 별도의 기본 소셜 또는 광고 기능에 이러한 권한을 사용하지 않습니다.

| 영역 | 설명 |
|------|--------|
| 네트워크 | 웹사이트 로드 및 검색에 필요 |
| 모션 (흔들기) | **iPhone**에서 플로팅 볼 / 크롬 복구에 사용 — 처리는 기기 내에서 이루어짐; **iPad**는 대신 상단 근처 탭 사용 |
| iCloud | 동기화를 활성화한 경우에만 |
| 메일 / 공유 시트 | 사용자가 시작한 피드백 또는 공유 작업 선택 사항 |
| StoreKit (선택적 팁) | Apple에서 처리하는 사용 가능한 팁; 기능 잠금 해제는 아님 |

## 아동 개인정보 보호

어린이 잠금은 **로컬 UI 제한**입니다 (주소 표시줄 숨기기 / 선택적 설정 비밀번호). 활성화된 동안, 위젯, 단축어, 홈이 아닌 즐겨찾기들은 대신 **홈**을 엽니다. 이는 저희와 함께 어린이 계정을 만들지 않습니다. 저희는 마케팅 목적을 위해 아동의 개인 정보를 고의로 수집하지 않습니다. 부모는 어떤 사이트가 열리는지 감독해야 합니다.

## 저희가 하지 않는 것

- iHTC Studio 계정은 **필요하지** 않습니다. 
- 우리는 인앱 광고나 삽입 프로모션 팝업을 표시하지 **않습니다**(필수 첫 실행 조건 제외). 
- 우리는 이 앱에 대해 자체 클라우드 동기화 서버를 운영하지 **않습니다**(선택적 동기화는 **귀하의** Apple iCloud만 사용합니다). 
- 우리는 귀하의 데이터를 판매하지 **않습니다**. 
- 일반 UserDefaults에 설정 비밀번호를 저장하지 **않습니다**(장치의 키체인을 사용함). 

## 제3자 

| 파티 | 역할 | 
|-------|------| 
| **애플** | 앱스토어 배포; 선택적인 iCloud KVS; 위젯 / Siri / 바로가기; 메일, 공유 시트, Safari 보기 컨트롤러; 선택적 StoreKit 팁 | 
| **사용자가 여는 웹사이트 및 검색 엔진** | 귀하가 방문하는 페이지에 대한 정상적인 브라우저 트래픽 수신 | 

## 보관 및 삭제 

로컬 기본 설정 및 북마크는 변경 또는 삭제하거나 앱을 제거할 때까지 유지됩니다. 선택적 iCloud 데이터는 동기화를 비활성화하거나 Apple 도구를 통해 삭제할 때까지 Apple 정책에 따라 유지됩니다. 당사는 서버에서 개인 데이터를 수집하지 않기 때문에 귀하의 이메일에 응답하는 것 외에 삭제할 계정 데이터세트가 없습니다. 

## 본 정책의 변경 사항

우리는 이 페이지를 때때로 업데이트할 수 있습니다. 위의 “마지막 업데이트” 날짜는 업데이트할 때 변경됩니다. 변경 후 계속 사용하는 것은 업데이트된 정책에 동의함을 의미합니다.

## 문의하기

- **이메일:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

이 [개인정보 처리방침](../privacy) 페이지를 브라우저에서 열고 App Store Connect용 공개 링크가 필요하면 주소 표시줄 URL을 복사하세요.

</section>
<section lang="ru" markdown="1">

**Последнее обновление:** 6 сентября 2026 г. 

iHTC Studio («мы», «нас» или «наш») создал **iBrowser** (также известный как «全屏浏览器» / «全螢幕瀏覽器», идентификатор пакета `full.screen.browser`). В настоящей Политике конфиденциальности объясняется, какие данные обрабатываются (а какие нет) при использовании вами приложения. **Обзор приложения Apple**, и пользователи могут использовать эту страницу как общедоступный URL-адрес конфиденциальности. Для App Store Connect откройте эту страницу [Политика конфиденциальности](../privacy) и скопируйте адрес из адресной строки браузера. 

## Резюме (согласование этикетки Apple Privacy Nutrition) 

| Тема | Наша практика | 
|-------|----------------| 
| Аккаунт | **Не требуется** — без регистрации или входа в систему с помощью iHTC Studio | 
| Сбор данных с помощью iHTC Studio | **Данные не собираются** — мы **не** используем серверную часть, которая получает ваши закладки или настройки | 
| Реклама | **Нет** — нет рекламы, нет рекламного SDK, нет запроса прозрачности отслеживания приложений для рекламы | 
| Просмотр контента | Страницы, которые вы открываете, загружаются **напрямую WebKit** с этих сайтов; мы не используем прокси-сервер для просмотра | 
| Дополнительная синхронизация Apple | **Хранилище ключей и значений iCloud** — отключено по умолчанию; только если вы включите его в Настройках | 

## Сбор данных

- **Нет учетной записи** — вы можете использовать приложение, не создавая у нас учетную запись. 
- **Нет рекламного или аналитического SDK** — приложение не показывает рекламу или домашнюю аналитику телефона в iHTC Studio. 
- **Нет серверной части iHTC Studio для ваших закладок** — настройки остаются на вашем устройстве (и, при необходимости, в **вашем** Apple iCloud). У нас нет сервера, который получает ваш список закладок. 

### Просмотр веб-страниц 

Когда вы переходите на веб-сайт или используете поисковую систему: 

- Ваше устройство связывается с **этим сайтом** (или поисковой системой) по сети, как и в любом браузере. 
- Эти третьи лица могут видеть стандартные метаданные запроса (IP-адрес, пользовательский агент, установленные ими файлы cookie, запрашиваемое вами содержимое страницы). Применяются их политики конфиденциальности. 
– При выборе встроенной или настраиваемой **поисковой системы** на устройстве устанавливается только префикс URL-адреса поиска. 

### Виджеты, ярлыки и глубокие ссылки 

Виджеты главного экрана/экрана блокировки, Siri, ярлыки, быстрые действия на главном экране и ссылки `ibrowser://` открывают пункты назначения **на вашем устройстве**. Они не отправляют вашу историю просмотров в iHTC Studio. 

## Данные, хранящиеся на вашем устройстве

| Данные | Где | Цель | 
|------|-------|---------| 
| URL-адрес домашней страницы | UserDefaults (+ снимок группы приложений) | Стартовая страница; отображение виджетов | 
| Префикс поисковой системы | Пользовательские настройки по умолчанию | Поиск в адресной строке | 
| Закладки | UserDefaults (JSON) (+ снимок группы приложений) | Местные фавориты; виджеты закладок | 
| Замок от детей / принудительное скрытие хром | UserDefaults (+ Группа приложений) | Режимы погружения и детский/киоск | 
| Включение/выключение плавающего шара и порядок меню | Пользовательские настройки по умолчанию | Доступность ярлыков | 
| Плавающий шар **позиция** | UserDefaults (только для устройства) | Место, где вы оставили мяч — **не** синхронизируется с iCloud | 
| Последняя успешно загруженная страница | UserDefaults (+ Группа приложений) | «Продолжить последним» — **только устройство**, а не iCloud | 
| Пароль настроек | **Брелок** (`WhenUnlockedThisDeviceOnly`) | Дополнительная блокировка настроек — **нет** в UserDefaults, группе приложений или iCloud | 
| Поля браузера | Пользовательские настройки по умолчанию | Вставки контента | 
| Внешний вид/язык | UserDefaults (только для устройства) | Язык тем и пользовательского интерфейса — **не** iCloud | 
| Главный экран быстрого заказа | UserDefaults (только для устройства) | Меню при длительном нажатии — **не** iCloud | 
| Руководство по первому запуску и флаги условий | UserDefaults (только для устройства) | Регистрация | 
| Виджеты снимков | Группа приложений `group.full.screen.browser` | Отображение расширения виджета только для чтения |

При удалении приложения удаляются данные его песочницы и группы приложений (в зависимости от поведения iOS). Дополнительные копии iCloud остаются в **вашем** iCloud, пока вы не очистите их или не отключите синхронизацию в другом месте. 

## Дополнительная синхронизация с iCloud 

Если вы включите **iCloud Sync** в настройках (по умолчанию **выключено**), выбранные настройки отражаются через **`NSUbiquitousKeyValueStore`** Apple, привязанный к **вашему Apple ID**: 

**Можно синхронизировать** закладки, домашнюю страницу, поисковую систему, поля, блокировку отображения адресной строки и панели инструментов, включение/выключение плавающего шарика, порядок меню с плавающим шариком. 

**Не синхронизируется**: пароль настроек, последняя страница («продолжить последней»), положение плавающего шарика, внешний вид, язык, порядок быстрых действий на главном экране, флажки руководства/терминов. 

Трафик синхронизации поступает в **Apple iCloud**, а не в iHTC Studio. Вы можете отключить синхронизацию или нажать **Синхронизировать сейчас** в настройках. Мы не можем прочитать ваше содержимое iCloud. 

## Разрешения 

Веб-страницы могут запрашивать возможности устройства через WebKit (например, камеру, микрофон или местоположение) в зависимости от сайта. Системные подсказки появляются только тогда, когда страница запрашивает. Приложение также объявляет строки возможностей, которые могут потребоваться веб-контенту; мы не используем эти разрешения для отдельной социальной или рекламной функции.

| Область | Примечания |
|------|--------|
| Сеть | Требуется для загрузки веб-сайтов и поиска |
| Движение (трясение) | Используется на **iPhone** для восстановления плавающей кнопки / Chrome — обработка остаётся локальной; **iPad** использует нажатие возле верхней части вместо этого |
| iCloud | Только если вы включите синхронизацию |
| Почта / Панель совместного использования | Дополнительные действия обратной связи или обмена, которые вы инициируете |
| StoreKit (необязательный совет) | Расходуемый совет обрабатывается Apple; не разблокирует функции |

## Конфиденциальность детей

Детский замок — это **локальное ограничение интерфейса** (скрывает адресную строку / необязательный пароль Настроек). Пока он включен, виджеты, Быстрые команды и закладки, не относящиеся к домашним, открываются на **главной странице**. Он **не** создаёт детскую учётную запись у нас. Мы сознательно не собираем личную информацию детей для маркетинга. Родители должны контролировать, какие сайты открываются.

## Чего мы не делаем

- Нам **не** требуется учетная запись iHTC Studio. 
– Мы **не** показываем рекламу в приложении или всплывающие рекламные объявления (за исключением обязательных условий первого запуска). 
- Мы **не** используем собственные серверы облачной синхронизации для этого приложения (дополнительная синхронизация использует только **ваш** Apple iCloud). 
- Мы **не** продаем ваши данные. 
- Мы **не** храним пароль настроек в простом файле UserDefaults (он использует связку ключей на устройстве). 

## Третьи стороны 

| Вечеринка | Роль | 
|-------|------| 
| **Яблоко** | Распространение в App Store; дополнительный iCloud KVS; виджеты/Siri/Ярлыки; Почта, общий лист, контроллер представления Safari; дополнительный совет StoreKit | 
| **Сайты и поисковые системы, которые вы открываете** | Получайте нормальный трафик браузера для страниц, которые вы посещаете | 

## Хранение и удаление 

Локальные настройки и закладки остаются до тех пор, пока вы не измените, не очистите их или не удалите приложение. Дополнительные данные iCloud остаются под политикой Apple до тех пор, пока вы не отключите синхронизацию и/или не очистите их с помощью инструментов Apple. Поскольку мы не собираем персональные данные на наших серверах, мы не можем удалить набор данных учетной записи, кроме ответа на ваше электронное письмо. 

## Изменения в этой политике

Мы можем время от времени обновлять эту страницу. Дата «Последнее обновление» выше изменится, когда мы это сделаем. Продолжение использования после изменений означает, что вы принимаете обновленную политику.

## Свяжитесь с нами

- **Электронная почта:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Откройте эту страницу [Политика конфиденциальности](../privacy) в браузере и скопируйте URL из адресной строки, если вам нужна публичная ссылка для App Store Connect.

</section>
<section lang="th" markdown="1">

**อัปเดตล่าสุด:** 6 กันยายน 2026 

iHTC Studio ("เรา", "พวกเรา" หรือ "ของเรา") สร้างขึ้น **iBrowser** (หรือที่เรียกว่า "全屏浏览器" / "全螢幕瀏覽器", Bundle ID `full.screen.browser`) นโยบายความเป็นส่วนตัวนี้อธิบายว่าข้อมูลใดบ้างที่ได้รับ (และไม่ใช่) จัดการเมื่อคุณใช้แอป **รีวิวแอป Apple** และผู้ใช้อาจใช้หน้านี้เป็น URL ความเป็นส่วนตัวสาธารณะ สำหรับ App Store Connect ให้เปิดหน้า [นโยบายความเป็นส่วนตัว](../privacy) และคัดลอกที่อยู่จากแถบที่อยู่ของเบราว์เซอร์ 

## สรุป (การจัดแนวฉลากโภชนาการความเป็นส่วนตัวของ Apple) 

| หัวข้อ | แนวปฏิบัติของเรา | 
|----------------------|----------------| 
| บัญชี | **ไม่จำเป็น** — ไม่ต้องลงทะเบียนหรือลงชื่อเข้าใช้ด้วย iHTC Studio | 
| การรวบรวมข้อมูลโดย iHTC Studio | **ข้อมูลไม่ถูกเก็บรวบรวม** — เราไม่ **ไม่** ดำเนินการแบ็กเอนด์ที่ได้รับบุ๊กมาร์กหรือการตั้งค่าของคุณ | 
| การโฆษณา | **ไม่มี** — ไม่มีโฆษณา ไม่มี SDK โฆษณา ไม่มีข้อความแจ้งความโปร่งใสในการติดตามแอปสำหรับโฆษณา | 
| กำลังเปิดดูเนื้อหา | หน้าที่คุณเปิดจะถูกโหลด **โดยตรงจาก WebKit** จากไซต์เหล่านั้น เราไม่ได้ใช้งานพรอกซีการเรียกดู | 
| ตัวเลือก Apple Sync | **ที่เก็บข้อมูลคีย์-ค่า iCloud** — ปิดตามค่าเริ่มต้น เฉพาะในกรณีที่คุณเปิดใช้งานในการตั้งค่า | 

## การรวบรวมข้อมูล

- **ไม่มีบัญชี** — คุณสามารถใช้แอปได้โดยไม่ต้องสร้างบัญชีกับเรา 
- **ไม่มีการโฆษณาหรือ SDK การวิเคราะห์** — แอปไม่แสดงโฆษณาหรือการวิเคราะห์บ้านทางโทรศัพท์ไปยัง iHTC Studio 
- **ไม่มีแบ็กเอนด์ iHTC Studio สำหรับบุ๊กมาร์กของคุณ** — การตั้งค่าจะยังคงอยู่บนอุปกรณ์ของคุณ (และเป็นทางเลือกใน **ของคุณ** Apple iCloud) เราไม่ได้โฮสต์เซิร์ฟเวอร์ที่ได้รับรายการบุ๊กมาร์กของคุณ 

### การท่องเว็บ 

เมื่อคุณนำทางไปยังเว็บไซต์หรือใช้เครื่องมือค้นหา: 

- อุปกรณ์ของคุณติดต่อกับ **ไซต์นั้น** (หรือผู้ให้บริการค้นหา) ผ่านเครือข่าย เช่นเดียวกับเบราว์เซอร์ใดๆ 
- บุคคลที่สามเหล่านั้นอาจเห็นข้อมูลเมตาคำขอมาตรฐาน (ที่อยู่ IP, ตัวแทนผู้ใช้, คุกกี้ที่พวกเขาตั้งค่า, เนื้อหาหน้าที่คุณร้องขอ) นโยบายความเป็นส่วนตัวมีผลบังคับใช้ 
- การเลือก **เครื่องมือค้นหา** ในตัวหรือแบบกำหนดเอง จะตั้งค่าคำนำหน้า URL การค้นหาบนอุปกรณ์เท่านั้น 

### วิดเจ็ต ทางลัด และลิงก์ในรายละเอียด 

วิดเจ็ตหน้าจอหลัก / หน้าจอล็อค, Siri, ทางลัด, การดำเนินการด่วนบนหน้าจอหลัก และลิงก์ `ibrowser://` ปลายทางที่เปิดอยู่ **บนอุปกรณ์ของคุณ** พวกเขาจะไม่ส่งประวัติการเข้าชมของคุณไปที่ iHTC Studio 

## ข้อมูลที่จัดเก็บไว้ในอุปกรณ์ของคุณ

| ข้อมูล | ที่ไหน | วัตถุประสงค์ | 
|------|-------|---------| 
| URL หน้าแรก | UserDefaults (+ สแนปชอตกลุ่มแอป) | หน้าเริ่มต้น; การแสดงวิดเจ็ต | 
| คำนำหน้าเครื่องมือค้นหา | ค่าเริ่มต้นของผู้ใช้ | ค้นหาแถบที่อยู่ | 
| บุ๊กมาร์ก | UserDefaults (JSON) (+ สแนปช็อตกลุ่มแอป) | รายการโปรดในท้องถิ่น วิดเจ็ตบุ๊กมาร์ก | 
| ล็อคป้องกันเด็ก / บังคับซ่อนโครเมียม | UserDefaults (+ กลุ่มแอป) | โหมดดื่มด่ำ & เด็ก / คีออสก์ | 
| เปิด/ปิดลูกลอย & ลำดับเมนู | ค่าเริ่มต้นของผู้ใช้ | ทางลัดที่จ่ายได้ | 
| ลูกลอย **ตำแหน่ง** | UserDefaults (อุปกรณ์เท่านั้น) | ตำแหน่งที่คุณทิ้งลูกบอล — **ไม่** ซิงค์กับ iCloud | 
| โหลดหน้าสำเร็จครั้งล่าสุด | UserDefaults (+ กลุ่มแอป) | “ดำเนินการต่อล่าสุด” — **อุปกรณ์เท่านั้น** ไม่ใช่ iCloud | 
| การตั้งค่ารหัสผ่าน | **พวงกุญแจ** (`WhenUnlockedThisDeviceOnly`) | การล็อคการตั้งค่าเสริม — **ไม่ใช่** ใน UserDefaults, App Group หรือ iCloud | 
| ขอบเบราว์เซอร์ | ค่าเริ่มต้นของผู้ใช้ | แทรกเนื้อหา | 
| ลักษณะ/ภาษา | UserDefaults (อุปกรณ์เท่านั้น) | ภาษาของธีมและ UI — **ไม่ใช่** iCloud | 
| คำสั่งดำเนินการด่วนบนหน้าจอหลัก | UserDefaults (อุปกรณ์เท่านั้น) | เมนูกดแบบยาว — **ไม่ใช่** iCloud | 
| คู่มือการเรียกใช้ครั้งแรกและแฟล็กข้อกำหนด | UserDefaults (อุปกรณ์เท่านั้น) | การเริ่มต้นใช้งาน | 
| สแนปชอตวิดเจ็ต | กลุ่มแอป `group.full.screen.browser` | การแสดงผลแบบอ่านอย่างเดียวสำหรับส่วนขยายวิดเจ็ต |

การถอนการติดตั้งแอปจะลบข้อมูลแซนด์บ็อกซ์และกลุ่มแอป (ขึ้นอยู่กับพฤติกรรมของ iOS) สำเนา iCloud ที่เป็นตัวเลือกจะยังคงอยู่ใน **ของคุณ** iCloud จนกว่าคุณจะล้างหรือปิดการซิงค์ที่อื่น 

## ตัวเลือกการซิงค์ iCloud 

หากคุณเปิดใช้งาน **iCloud Sync** ในการตั้งค่า (ค่าเริ่มต้น **ปิด**) การตั้งค่าที่เลือกจะสะท้อนผ่าน **`NSUbiquitousKeyValueStore`** ของ Apple ที่เชื่อมโยงกับ **Apple ID ของคุณ**: 

**อาจซิงค์:** บุ๊กมาร์ก หน้าแรก เครื่องมือค้นหา ระยะขอบ การล็อคการแสดงแถบที่อยู่ / แถบเครื่องมือ เปิด/ปิดลูกลอย ลำดับเมนูลูกลอย 

**ไม่ซิงค์:** รหัสผ่านการตั้งค่า, หน้าสุดท้าย (“ไปต่อหน้าสุดท้าย”), ตำแหน่งลูกลอย, ลักษณะที่ปรากฏ, ภาษา, ลำดับการดำเนินการด่วนของหน้าจอหลัก, คำแนะนำ / ธงข้อกำหนด 

การรับส่งข้อมูลการซิงค์ไปที่ **Apple iCloud** ไม่ใช่ไปที่ iHTC Studio คุณสามารถปิดการซิงค์หรือแตะ **ซิงค์ทันที** ในการตั้งค่า เราไม่สามารถอ่านเนื้อหา iCloud ของคุณได้ 

## สิทธิ์ 

เว็บเพจอาจร้องขอความสามารถของอุปกรณ์ผ่าน WebKit (เช่น กล้อง ไมโครโฟน หรือตำแหน่ง) ขึ้นอยู่กับไซต์ ข้อความแจ้งของระบบจะปรากฏเฉพาะเมื่อเพจถามเท่านั้น แอพนี้ยังประกาศสตริงความสามารถที่เนื้อหาเว็บอาจต้องการ เราไม่ใช้การอนุญาตเหล่านั้นสำหรับคุณลักษณะโซเชียลหรือการโฆษณาที่แยกจากกัน

| พื้นที่ | หมายเหตุ |
|------|--------|
| เครือข่าย | จำเป็นสำหรับการโหลดเว็บไซต์และค้นหา |
| การเคลื่อนไหว (เขย่า) | ใช้บน **iPhone** เพื่อเรียกบอลลอย / Chrome — การประมวลผลอยู่ในเครื่อง; **iPad** ใช้การแตะใกล้ด้านบนแทน |
| iCloud | ใช้เฉพาะหากคุณเปิดใช้งานการซิงค์ |
| เมล / แผ่นแชร์ | ฟีดแบ็กหรือการแชร์ที่คุณเริ่มต้นเอง (ไม่บังคับ) |
| StoreKit (ทิปเสริม) | ทิปแบบใช้ครั้งเดียวประมวลผลโดย Apple; ไม่ปลดล็อกฟีเจอร์ |

## ความเป็นส่วนตัวของเด็ก

การล็อกเด็กเป็น **ข้อจำกัดใน UI ภายในเครื่อง** (ซ่อนแถบที่อยู่ / รหัสผ่านการตั้งค่าเป็นทางเลือก) ขณะเปิดใช้งาน วิดเจ็ต, ทางลัด, และบุ๊กมาร์กที่ไม่ใช่หน้าหลักจะเปิด **หน้าแรก** แทน ไม่สร้างบัญชีเด็กกับเรา เราไม่ได้ขอข้อมูลส่วนบุคคลจากเด็กเพื่อการตลาดโดยทราบ ผู้ปกครองควรสอดส่องว่าเว็บไซต์ใดถูกเปิด

## สิ่งที่เราไม่ทำ

- เรา **ไม่** จำเป็นต้องมีบัญชี iHTC Studio 
- เราไม่ **ไม่** แสดงโฆษณาในแอปหรือป๊อปอัปโปรโมตโฆษณาคั่นระหว่างหน้า (นอกเหนือจากเงื่อนไขการเรียกใช้ครั้งแรกที่จำเป็น) 
- เรา **ไม่** ดำเนินการเซิร์ฟเวอร์ซิงค์บนคลาวด์ของเราเองสำหรับแอปนี้ (การซิงค์เสริมจะใช้ **Apple iCloud ของคุณ** เท่านั้น) 
- เราไม่ **ไม่** ขายข้อมูลของคุณ 
- เราไม่ ** ไม่ ** เก็บรหัสผ่านการตั้งค่าไว้ใน UserDefaults ธรรมดา (ใช้พวงกุญแจบนอุปกรณ์) 

## บุคคลที่สาม 

| ปาร์ตี้ | บทบาท | 
|-------|-| 
| **แอปเปิ้ล** | การจำหน่ายแอพสโตร์ ตัวเลือกเสริม iCloud KVS; วิดเจ็ต / Siri / ทางลัด; เมล, แผ่นแบ่งปัน, ตัวควบคุมมุมมอง Safari; เคล็ดลับ StoreKit เสริม | 
| **เว็บไซต์และเครื่องมือค้นหาที่คุณเปิด** | รับการเข้าชมเบราว์เซอร์ปกติสำหรับหน้าที่คุณเยี่ยมชม | 

## การเก็บรักษาและการลบ 

ค่ากำหนดและบุ๊กมาร์กในเครื่องจะยังคงอยู่จนกว่าคุณจะเปลี่ยนหรือล้างข้อมูลหรือถอนการติดตั้งแอป ข้อมูลเสริม iCloud จะอยู่ภายใต้นโยบายของ Apple จนกว่าคุณจะปิดใช้งานการซิงค์และ/หรือล้างข้อมูลผ่านเครื่องมือของ Apple เนื่องจากเราไม่ได้เก็บรวบรวมข้อมูลส่วนบุคคลบนเซิร์ฟเวอร์ของเรา จึงไม่มีชุดข้อมูลบัญชีให้เราลบได้ นอกเหนือจากการตอบอีเมลของคุณ 

## การเปลี่ยนแปลงนโยบายนี้

เราอาจปรับปรุงหน้านี้เป็นครั้งคราว วันที่ “อัปเดตล่าสุด” ข้างต้นจะเปลี่ยนเมื่อเราทำการอัปเดต การใช้งานอย่างต่อเนื่องหลังจากมีการเปลี่ยนแปลงหมายความว่าคุณยอมรับนโยบายที่อัปเดตแล้ว

## ติดต่อเรา

- **อีเมล:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

เปิดหน้ [นโยบายความเป็นส่วนตัว](../privacy) นี้ในเว็บเบราว์เซอร์และคัดลอก URL จากแถบที่อยู่หากคุณต้องการลิงก์สาธารณะสำหรับ App Store Connect.

</section>
<section lang="de" markdown="1">

**Letzte Aktualisierung:** 6. September 2026 

iHTC Studio („wir“, „uns“ oder „unser“) hat **iBrowser** erstellt (auch bekannt als „全屏浏览器“ / „全螢幕瀏覽器“, Bundle-ID `full.screen.browser`). Diese Datenschutzrichtlinie erläutert, welche Daten bei der Nutzung der App verarbeitet werden (und welche nicht). **Apple App Review** und Benutzer können sich auf diese Seite als öffentliche Datenschutz-URL verlassen. Öffnen Sie für App Store Connect diese Seite mit den Datenschutzbestimmungen (../privacy) und kopieren Sie die Adresse aus der Adressleiste des Browsers. 

## Zusammenfassung (Ausrichtung des Apple Privacy Nutrition Label) 

| Thema | Unsere Praxis | 
|-------|----------------| 
| Konto | **Nicht erforderlich** – keine Registrierung oder Anmeldung bei iHTC Studio | 
| Datenerfassung durch iHTC Studio | **Daten werden nicht erfasst** – wir betreiben **kein** Backend, das Ihre Lesezeichen oder Einstellungen empfängt | 
| Werbung | **Keine** – keine Werbung, kein Anzeigen-SDK, keine Aufforderung zur App-Tracking-Transparenz für Anzeigen | 
| Inhalte durchsuchen | Von Ihnen geöffnete Seiten werden **direkt von WebKit** von diesen Websites geladen; Wir betreiben keinen Browsing-Proxy | 
| Optionale Apple-Synchronisierung | **iCloud Key-Value Storage** – standardmäßig deaktiviert; nur, wenn Sie es unter Einstellungen | aktivieren 

## Datenerfassung

- **Kein Konto** – Sie können die App nutzen, ohne ein Konto bei uns zu erstellen. 
- **Keine Werbung oder Analyse-SDK** – Die App zeigt iHTC Studio keine Werbung oder Phone-Home-Analysen an. 
- **Kein iHTC Studio-Backend für Ihre Lesezeichen** – Einstellungen bleiben auf Ihrem Gerät (und optional in **Ihrer** Apple iCloud). Wir hosten keinen Server, der Ihre Lesezeichenliste empfängt. 

### Surfen im Internet 

Wenn Sie zu einer Website navigieren oder eine Suchmaschine verwenden: 

- Ihr Gerät kontaktiert **diese Website** (oder diesen Suchanbieter) über das Netzwerk, wie bei jedem Browser. 
- Diese Dritten sehen möglicherweise Standardanfrage-Metadaten (IP-Adresse, Benutzeragent, von ihnen gesetzte Cookies, von Ihnen angeforderte Seiteninhalte). Es gelten deren Datenschutzrichtlinien. 
– Durch die Auswahl einer integrierten oder benutzerdefinierten **Suchmaschine** wird nur ein Such-URL-Präfix auf dem Gerät festgelegt. 

### Widgets, Verknüpfungen und Deep Links 

Startbildschirm-/Sperrbildschirm-Widgets, Siri, Verknüpfungen, Schnellaktionen auf dem Startbildschirm und `ibrowser://`-Links öffnen Ziele **auf Ihrem Gerät**. Sie senden Ihren Browserverlauf nicht an iHTC Studio. 

## Auf Ihrem Gerät gespeicherte Daten

| Daten | Wo | Zweck | 
|------|-------|---------| 
| Homepage-URL | UserDefaults (+ App-Gruppen-Snapshot) | Startseite; Widget-Anzeige | 
| Suchmaschinenpräfix | Benutzerstandards | Suche in der Adressleiste | 
| Lesezeichen | UserDefaults (JSON) (+ App-Gruppen-Snapshot) | Lokale Favoriten; Lesezeichen-Widgets | 
| Kindersicherung / Force-Hide-Chrom | UserDefaults (+ App-Gruppe) | Immersive & Kinder-/Kiosk-Modi | 
| Floatball ein/aus & Menüreihenfolge | Benutzerstandards | Abkürzungsangebot | 
| Schwimmerball **Position** | UserDefaults (nur Gerät) | Wo Sie den Ball gelassen haben – **nicht** mit iCloud synchronisiert | 
| Letzte erfolgreich geladene Seite | UserDefaults (+ App-Gruppe) | „Zuletzt fortfahren“ – **nur Gerät**, nicht iCloud | 
| Einstellungen Passwort | **Schlüsselanhänger** (`WhenUnlockedThisDeviceOnly`) | Optionale Einstellungssperre – **nicht** in UserDefaults, App Group oder iCloud | 
| Browserränder | Benutzerstandards | Inhaltseinfügungen | 
| Aussehen / Sprache | UserDefaults (nur Gerät) | Design und UI-Sprache – **nicht** iCloud | 
| Schnellauftrag auf dem Startbildschirm | UserDefaults (nur Gerät) | Menü lange drücken – **nicht** iCloud | 
| Erstausgabe-Leitfaden und Begriffsflaggen | UserDefaults (nur Gerät) | Onboarding | 
| Widget-Schnappschüsse | App-Gruppe `group.full.screen.browser` | Schreibgeschützte Anzeige für die Widget-Erweiterung |

Durch die Deinstallation der App werden ihre Sandbox- und App-Gruppendaten entfernt (abhängig vom iOS-Verhalten). Optionale iCloud-Kopien bleiben in **Ihrer** iCloud, bis Sie sie löschen oder die Synchronisierung an anderer Stelle deaktivieren. 

## Optionale iCloud-Synchronisierung 

Wenn Sie **iCloud Sync** in den Einstellungen aktivieren (standardmäßig **aus**), werden ausgewählte Einstellungen über Apples **`NSUbiquitousKeyValueStore`** gespiegelt, das an **Ihre Apple-ID** gebunden ist: 

**Kann synchronisiert werden:** Lesezeichen, Startseite, Suchmaschine, Ränder, Adressleisten-/Symbolleisten-Anzeigesperren, Float-Ball ein/aus, Float-Ball-Menüreihenfolge. 

**Wird nicht synchronisiert:** Einstellungen Passwort, letzte Seite („Letzte Seite fortsetzen“), Float-Ball-Position, Aussehen, Sprache, Schnellaktionsreihenfolge auf dem Startbildschirm, Markierungen für Anleitungen/Begriffe. 

Der Synchronisierungsverkehr geht an **Apple iCloud**, nicht an iHTC Studio. Sie können die Synchronisierung deaktivieren oder in den Einstellungen auf **Jetzt synchronisieren** tippen. Wir können Ihre iCloud-Inhalte nicht lesen. 

## Berechtigungen 

Abhängig von der Website können Webseiten über WebKit Gerätefunktionen anfordern (z. B. Kamera, Mikrofon oder Standort). Systemaufforderungen werden nur angezeigt, wenn eine Seite danach fragt. Die App deklariert außerdem Funktionszeichenfolgen, die Webinhalte möglicherweise benötigen. Wir verwenden diese Berechtigungen nicht für eine separate native soziale oder Werbefunktion.

| Bereich | Hinweise |
|--------|---------|
| Netzwerk | Wird benötigt, um Websites zu laden und zu suchen |
| Bewegung (Schütteln) | Wird auf dem **iPhone** verwendet, um den Float-Ball/Chrome wiederherzustellen – die Verarbeitung erfolgt lokal; **iPad** verwendet stattdessen Tippen-nahe-oben |
| iCloud | Nur, wenn Sie die Synchronisierung aktivieren |
| Mail / Teilen-Menü | Optionale Rückmeldungen oder Freigabeaktionen, die Sie initiieren |
| StoreKit (optionales Trinkgeld) | Verbrauchbares Trinkgeld, das von Apple verarbeitet wird; schaltet keine Funktionen frei |

## Datenschutz von Kindern

Die Kindersicherung ist eine **lokale UI-Beschränkung** (Adressleiste ausblenden / optionales Einstellungs-Passwort). Solange sie aktiviert ist, öffnen Widgets, Kurzbefehle und nicht-Haupt-Lesezeichen stattdessen **Startseite**. Sie erstellt **kein** Kinderkonto bei uns. Wir fordern wissentlich keine persönlichen Informationen von Kindern für Marketingzwecke an. Eltern sollten überwachen, welche Websites geöffnet werden.

## Was wir nicht tun

- Wir benötigen **kein** ein iHTC Studio-Konto. 
- Wir zeigen **keine** In-App-Werbung oder Interstitial-Werbe-Popups an (abgesehen von den erforderlichen Erstauflagen). 
- Wir betreiben **keine** eigenen Cloud-Synchronisierungsserver für diese App (für die optionale Synchronisierung wird nur **Ihre** Apple iCloud verwendet). 
- Wir verkaufen Ihre Daten **nicht**. 
- Wir speichern das Einstellungskennwort **nicht** in einfachen Benutzerstandards (es verwendet den Schlüsselbund auf dem Gerät). 

## Dritte 

| Party | Rolle | 
|-------|------| 
| **Apfel** | App-Store-Vertrieb; optionales iCloud KVS; Widgets / Siri / Verknüpfungen; Mail, Share Sheet, Safari View Controller; optionaler StoreKit-Tipp | 
| **Websites und Suchmaschinen, die Sie öffnen** | Erhalten Sie normalen Browserverkehr für die von Ihnen besuchten Seiten | 

## Aufbewahrung und Löschung 

Lokale Einstellungen und Lesezeichen bleiben erhalten, bis Sie sie ändern oder löschen oder die App deinstallieren. Optionale iCloud-Daten unterliegen weiterhin den Richtlinien von Apple, bis Sie die Synchronisierung deaktivieren und/oder sie über die Tools von Apple löschen. Da wir auf unseren Servern keine personenbezogenen Daten erfassen, gibt es keinen Kontodatensatz, den wir über die Beantwortung Ihrer E-Mail hinaus löschen könnten. 

## Änderungen an dieser Richtlinie

Wir können diese Seite von Zeit zu Zeit aktualisieren. Das oben angezeigte Datum „Zuletzt aktualisiert“ wird sich ändern, wenn wir dies tun. Die fortgesetzte Nutzung nach Änderungen bedeutet, dass Sie die aktualisierte Richtlinie akzeptieren.

## Kontaktieren Sie uns

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Öffnen Sie diese [Datenschutzerklärung](../privacy) Seite in einem Browser und kopieren Sie die Adressleiste-URL, wenn Sie den öffentlichen Link für App Store Connect benötigen.

</section>
<section lang="fr" markdown="1">

**Dernière mise à jour :** 6 septembre 2026 

iHTC Studio ("nous", "notre" ou "notre") a créé **iBrowser** (également connu sous le nom de "全屏浏览器" / "全螢幕瀏覽器", ID de bundle `full.screen.browser`). Cette politique de confidentialité explique quelles données sont (et ne sont pas) traitées lorsque vous utilisez l'application. **Apple App Review** et les utilisateurs peuvent se fier à cette page comme URL de confidentialité publique. Pour App Store Connect, ouvrez cette page [Politique de confidentialité](../privacy) et copiez l'adresse de la barre d'adresse du navigateur. 

## Résumé (alignement sur l'étiquette nutritionnelle de confidentialité Apple) 

| Sujet | Notre pratique | 
|-------|----------------| 
| Compte | **Non requis** — pas d'inscription ni de connexion avec iHTC Studio | 
| Collecte de données par iHTC Studio | **Données non collectées** — nous n'exploitons **pas** de backend qui reçoit vos favoris ou vos paramètres | 
| Publicité | **Aucun** — pas de publicité, pas de SDK publicitaire, pas d'invite de transparence du suivi des applications pour les publicités | 
| Navigation dans le contenu | Les pages que vous ouvrez sont chargées **directement par WebKit** à partir de ces sites ; nous n'exploitons pas de proxy de navigation | 
| Synchronisation Apple en option | **Stockage de valeurs-clés iCloud** — désactivé par défaut ; seulement si vous l'activez dans Paramètres | 

## Collecte de données

- **Aucun compte** — Vous pouvez utiliser l'application sans créer de compte chez nous. 
- **Pas de SDK de publicité ou d'analyse** — L'application ne diffuse pas de publicités ni d'analyses téléphoniques sur iHTC Studio. 
- **Pas de backend iHTC Studio pour vos favoris** — Les préférences restent sur votre appareil (et éventuellement dans **votre** Apple iCloud). Nous n'hébergeons pas de serveur qui reçoit votre liste de favoris. 

### Navigation sur le Web 

Lorsque vous naviguez sur un site Web ou utilisez un moteur de recherche : 

- Votre appareil contacte **ce site** (ou ce fournisseur de recherche) via le réseau, comme avec n'importe quel navigateur. 
- Ces tiers peuvent voir les métadonnées de demande standard (adresse IP, agent utilisateur, cookies qu'ils définissent, contenu de la page que vous demandez). Leurs politiques de confidentialité s’appliquent. 
- Le choix d'un **moteur de recherche** intégré ou personnalisé définit uniquement un préfixe d'URL de recherche sur l'appareil. 

### Widgets, raccourcis et liens profonds 

Les widgets de l'écran d'accueil/de l'écran de verrouillage, Siri, les raccourcis, les actions rapides de l'écran d'accueil et les liens `ibrowser://` ouvrent des destinations **sur votre appareil**. Ils n'envoient pas votre historique de navigation à iHTC Studio. 

## Données stockées sur votre appareil

| Données | Où | Objectif | 
|------|-------|--------------| 
| URL de la page d'accueil | UserDefaults (+ instantané du groupe d'applications) | Page de démarrage ; affichage des widgets | 
| Préfixe du moteur de recherche | Paramètres par défaut de l'utilisateur | Recherche dans la barre d'adresse | 
| Signets | UserDefaults (JSON) (+ instantané du groupe d'applications) | Favoris locaux ; widgets de favoris | 
| Sécurité enfant / masquage forcé chrome | Paramètres par défaut (+ groupe d'applications) | Modes immersif & enfant / kiosque | 
| Boule flottante marche/arrêt et commande de menu | Paramètres par défaut de l'utilisateur | Possibilité de raccourci | 
| Ballon flottant **position** | UserDefaults (appareil uniquement) | Où vous avez laissé le ballon – **non** synchronisé avec iCloud | 
| Dernière page chargée avec succès | Paramètres par défaut (+ groupe d'applications) | « Continuer en dernier » – **appareil uniquement**, pas iCloud | 
| Mot de passe des paramètres | **Porte-clés** (`WhenUnlockedThisDeviceOnly`) | Verrouillage des paramètres facultatif – **pas** dans UserDefaults, App Group ou iCloud | 
| Marges du navigateur | Paramètres par défaut de l'utilisateur | Encarts de contenu | 
| Apparence / langage | UserDefaults (appareil uniquement) | Langue du thème et de l'interface utilisateur – **pas** iCloud | 
| Commande d'action rapide sur l'écran d'accueil | UserDefaults (appareil uniquement) | Menu à pression longue — **pas** iCloud | 
| Guide de première diffusion et indicateurs de termes | UserDefaults (appareil uniquement) | Intégration | 
| Instantanés de widgets | Groupe d'applications `group.full.screen.browser` | Affichage en lecture seule pour l'extension du widget |

La désinstallation de l'application supprime ses données sandbox et App Group (sous réserve du comportement d'iOS). Les copies iCloud facultatives restent dans **votre** iCloud jusqu'à ce que vous les effaciez ou désactiviez la synchronisation ailleurs. 

## Synchronisation iCloud en option 

Si vous activez **iCloud Sync** dans Paramètres (**désactivé** par défaut), les préférences sélectionnées sont reflétées via le **`NSUbiquitousKeyValueStore`_** d'Apple lié à **votre identifiant Apple** : 

**Peut synchroniser :** signets, page d'accueil, moteur de recherche, marges, verrouillages d'affichage de la barre d'adresse/barre d'outils, activation/désactivation de la boule flottante, ordre du menu de la boule flottante. 

**Ne synchronise pas :** Mot de passe des paramètres, dernière page (« continuer en dernier »), position de la boule flottante, apparence, langue, ordre d'action rapide sur l'écran d'accueil, indicateurs de guide/termes. 

Le trafic de synchronisation va vers **Apple iCloud**, pas vers iHTC Studio. Vous pouvez désactiver la synchronisation ou appuyer sur **Synchroniser maintenant** dans Paramètres. Nous ne pouvons pas lire votre contenu iCloud. 

## Autorisations 

Les pages Web peuvent demander des fonctionnalités de périphérique via WebKit (par exemple une caméra, un microphone ou un emplacement) en fonction du site. Les invites du système apparaissent uniquement lorsqu'une page le demande. L'application déclare également les chaînes de capacités dont le contenu Web peut avoir besoin ; nous n'utilisons pas ces autorisations pour une fonctionnalité sociale ou publicitaire native distincte.

| Zone | Remarques |
|------|--------|
| Réseau | Nécessaire pour charger les sites web et effectuer des recherches |
| Mouvement (secouer) | Utilisé sur **iPhone** pour récupérer la boule flottante / Chrome — le traitement reste local ; **iPad** utilise plutôt un tapotement près du haut |
| iCloud | Seulement si vous activez la synchronisation |
| Mail / Feuille de partage | Retour facultatif ou actions de partage que vous initiez |
| StoreKit (pourboire optionnel) | Pourboire consommable traité par Apple ; ne déverrouille pas de fonctionnalités |

## Confidentialité des enfants

Le verrouillage pour enfant est une **restriction UI locale** (cacher la barre d’adresse / mot de passe facultatif dans les Réglages). Tant qu’il est activé, les widgets, Raccourcis et favoris non domestiques s’ouvrent **à la page d’accueil**. Il ne crée **pas** de compte enfant chez nous. Nous ne sollicitons pas sciemment d’informations personnelles auprès des enfants à des fins de marketing. Les parents doivent superviser les sites qui sont ouverts.

## Ce que nous ne faisons pas

- Nous n'avons **pas** besoin d'un compte iHTC Studio. 
- Nous ne diffusons **pas** de publicités dans l'application ni de pop-ups promotionnels interstitiels (en dehors des conditions de première diffusion requises). 
- Nous n'exploitons **pas** nos propres serveurs de synchronisation cloud pour cette application (la synchronisation facultative utilise **votre** Apple iCloud uniquement). 
- Nous ne vendons **pas** vos données. 
- Nous ne stockons **pas** le mot de passe des paramètres dans UserDefaults (il utilise le trousseau sur l'appareil). 

## Tiers 

| Fête | Rôle | 
|-------|------| 
| **Pomme** | Distribution sur l'App Store ; iCloud KVS en option ; widgets / Siri / Raccourcis ; Courrier, feuille de partage, contrôleur Safari View ; Astuce StoreKit en option | 
| **Sites Web et moteurs de recherche que vous ouvrez** | Recevez le trafic normal du navigateur pour les pages que vous visitez | 

## Conservation et suppression 

Les préférences locales et les favoris restent jusqu'à ce que vous les modifiiez ou les supprimiez, ou que vous désinstalliez l'application. Les données iCloud facultatives restent soumises aux politiques d'Apple jusqu'à ce que vous désactiviez la synchronisation et/ou les effaciez via les outils d'Apple. Étant donné que nous ne collectons pas de données personnelles sur nos serveurs, nous ne pouvons supprimer aucun ensemble de données de compte au-delà de la réponse à votre courrier électronique. 

## Modifications apportées à cette politique

Nous pouvons mettre à jour cette page de temps en temps. La date « Dernière mise à jour » ci-dessus changera lorsque nous le ferons. L'utilisation continue après les modifications signifie que vous acceptez la politique mise à jour.

## Contactez-nous

- **Email :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Ouvrez cette page [Politique de confidentialité](../privacy) dans un navigateur et copiez l'URL de la barre d'adresse si vous avez besoin du lien public pour App Store Connect.

</section>
<section lang="tr" markdown="1">

**Son güncelleme:** 6 Eylül 2026 

iHTC Studio ("biz", "bize" veya "bizim") **iBrowser**'ı oluşturdu ("全屏浏览器" / "全螢幕瀏覽器", Paket Kimliği `full.screen.browser` olarak da bilinir). Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlendiğini (ve işlenmediğini) açıklar. **Apple Uygulama İncelemesi** ve kullanıcılar, genel gizlilik URL'si olarak bu sayfaya güvenebilirler. App Store Connect için bu [Gizlilik Politikası](../privacy) sayfasını açın ve tarayıcının adres çubuğundan adresi kopyalayın. 

## Özet (Apple Gizlilik Beslenme Etiketi uyumu) 

| Konu | Uygulamamız | 
|----------|----------------| 
| Hesap | **Gerekli değil** — iHTC Studio'ya kaydolmak veya oturum açmak gerekmez | 
| iHTC Studio tarafından veri toplama | **Veri Toplanmadı** — yer işaretlerinizi veya ayarlarınızı alan bir arka uç **işletmiyoruz** | 
| Reklam | **Yok** — reklam yok, reklam SDK'sı yok, reklamlar için Uygulama İzleme Şeffaflığı istemi yok | 
| İçeriğe göz atılıyor | Açtığınız sayfalar **doğrudan WebKit** tarafından bu sitelerden yüklenir; bir tarama proxy'si kullanmıyoruz | 
| İsteğe bağlı Apple senkronizasyonu | **iCloud Anahtar-Değer Depolaması** — varsayılan olarak kapalıdır; yalnızca Ayarlar | 

## Veri Toplama

- **Hesap yok** — Uygulamayı bizde bir hesap oluşturmadan kullanabilirsiniz. 
- **Reklam veya analiz SDK'sı yok** — Uygulama, iHTC Studio'ya reklam veya telefonla ev analizi göstermez. 
- **Yer işaretleriniz için iHTC Studio arka ucu yok** — Tercihler cihazınızda kalır (ve isteğe bağlı olarak **Apple iCloud'unuzda** kalır). Yer imi listenizi alan bir sunucuyu barındırmıyoruz. 

### Web'de gezinme 

Bir web sitesine gittiğinizde veya bir arama motorunu kullandığınızda: 

- Cihazınız herhangi bir tarayıcıda olduğu gibi ağ üzerinden **o siteyle** (veya arama sağlayıcısıyla) iletişim kurar. 
- Bu üçüncü taraflar standart istek meta verilerini (IP adresi, kullanıcı aracısı, ayarladıkları çerezler, talep ettiğiniz sayfa içeriği) görebilir. Gizlilik politikaları geçerlidir. 
- Yerleşik veya özel bir **arama motoru** seçildiğinde yalnızca cihazda bir arama URL'si öneki ayarlanır. 

### Widget'lar, Kısayollar ve derin bağlantılar 

Ana Ekran / Kilit Ekranı widget'ları, Siri, Kısayollar, Ana Ekran hızlı eylemleri ve `ibrowser://` bağlantıları **cihazınızda** hedefleri açar. Tarama geçmişinizi iHTC Studio'ya göndermezler. 

## Cihazınızda Saklanan Veriler

| Veri | Nerede | Amaç | 
|------|-------|-------------| 
| Ana sayfa URL'si | UserDefaults (+ Uygulama Grubu anlık görüntüsü) | Başlangıç ​​sayfası; widget ekranı | 
| Arama motoru öneki | Kullanıcı Varsayılanları | Adres çubuğu araması | 
| Yer İmleri | UserDefaults (JSON) (+ Uygulama Grubu anlık görüntüsü) | Yerel favoriler; yer imi widget'ları | 
| Çocuk kilidi / kromu zorla gizleme | Kullanıcı Varsayılanları (+ Uygulama Grubu) | Sürükleyici ve çocuk / kiosk modları | 
| Şamandıra topu açma/kapama ve menü sırası | Kullanıcı Varsayılanları | Kısayol olanağı | 
| Yüzen top **konumu** | Kullanıcı Varsayılanları (yalnızca cihaz) | Topu bıraktığınız yer — iCloud ile **senkronize edilmedi** | 
| Başarıyla yüklenen son sayfa | Kullanıcı Varsayılanları (+ Uygulama Grubu) | “Sonuncuya devam et” — **yalnızca cihaz**, iCloud değil | 
| Ayarlar şifresi | **Anahtarlık** (`WhenUnlockedThisDeviceOnly`) | İsteğe Bağlı Ayarlar kilidi — UserDefaults, Uygulama Grubu veya iCloud'da **değil** | 
| Tarayıcı kenar boşlukları | Kullanıcı Varsayılanları | İçerik ekleri | 
| Görünüm / dil | Kullanıcı Varsayılanları (yalnızca cihaz) | Tema ve kullanıcı arayüzü dili — iCloud **değil** | 
| Ana Ekran hızlı işlem sırası | Kullanıcı Varsayılanları (yalnızca cihaz) | Menüye uzun basın — **değil** iCloud | 
| İlk çalıştırma kılavuzu ve şartlar bayrakları | Kullanıcı Varsayılanları (yalnızca cihaz) | İlk Katılım | 
| Widget anlık görüntüleri | Uygulama Grubu `group.full.screen.browser` | Widget uzantısı için salt okunur ekran |

Uygulamanın kaldırılması, uygulamanın korumalı alanını ve Uygulama Grubu verilerini kaldırır (iOS davranışına bağlıdır). İsteğe bağlı iCloud kopyaları, siz bunları temizleyene veya senkronizasyonu başka bir yerde kapatana kadar **iCloud'unuzda** kalır. 

## İsteğe Bağlı iCloud Senkronizasyonu 

Ayarlar'da **iCloud Senkronizasyonu**'nu etkinleştirirseniz (varsayılan **kapalı**), seçilen tercihler, **Apple Kimliğinize** bağlı olan Apple'ın **`NSUbiquitousKeyValueStore`_** aracılığıyla yansıtılır: 

**Senkronize edilebilecekler:** yer işaretleri, ana sayfa, arama motoru, kenar boşlukları, adres çubuğu/araç çubuğu ekran kilitleri, kayan top açma/kapama, kayan top menü sırası. 

**Senkronize edilmiyor:** Ayarlar şifresi, son sayfa (“sonuncuya devam et”), kayan top konumu, görünüm, dil, Ana Ekran hızlı işlem sırası, kılavuz / terimler bayrakları. 

Senkronizasyon trafiği iHTC Studio'ya değil **Apple iCloud**'a gider. Senkronizasyonu devre dışı bırakabilir veya Ayarlar'da **Şimdi Senkronize Et**'e dokunabilirsiniz. iCloud içeriklerinizi okuyamıyoruz. 

## İzinler 

Web sayfaları, siteye bağlı olarak WebKit aracılığıyla cihaz özellikleri (örneğin kamera, mikrofon veya konum) talep edebilir. Sistem istemleri yalnızca bir sayfa sorduğunda görünür. Uygulama ayrıca web içeriğinin ihtiyaç duyabileceği yetenek dizelerini de bildirir; bu izinleri ayrı bir yerel sosyal veya reklam özelliği için kullanmayız.

| Alan | Notlar |
|------|--------|
| Ağ | Web sitelerini yüklemek ve arama yapmak için gereklidir |
| Hareket (sallama) | **iPhone** üzerinde float ball / chrome'u geri almak için kullanılır — işlem yerel olarak gerçekleşir; **iPad** bunun yerine üst yakına dokunma kullanır |
| iCloud | Sadece senkronizasyonu etkinleştirirseniz |
| Mail / Paylaşım Menüsü | Başlattığınız isteğe bağlı geri bildirim veya paylaşım eylemleri |
| StoreKit (isteğe bağlı ipucu) | Apple tarafından işlenen tüketilebilir ipucu; özelliklerin kilidini açmaz |

## Çocukların Gizliliği

Çocuk kilidi bir **yerel kullanıcı arayüzü kısıtlamasıdır** (adres çubuğunu gizler / isteğe bağlı Ayarlar şifresi). Açıkken, widget'lar, Kestirmeler ve ana sayfa olmayan yer imleri yerine **ana sayfa** açılır. Bu, bizimle bir çocuk hesabı oluşturmaz. Pazarlama amacıyla bilinçli olarak çocuklardan kişisel bilgi talep etmiyoruz. Ebeveynler açılan siteleri denetlemelidir.

## Yapmadıklarımız

- Bir iHTC Studio hesabına **gerek duymayız**. 
- Uygulama içi reklamları veya geçiş reklamı promosyon açılır pencerelerini **göstermiyoruz** (gerekli ilk çalıştırma koşulları dışında). 
- Bu uygulama için kendi bulut senkronizasyon sunucularımızı **işletmiyoruz** (isteğe bağlı senkronizasyon yalnızca **sizin** Apple iCloud'unuzu kullanır). 
- Verilerinizi **satmıyoruz**. 
- Ayarlar şifresini düz UserDefaults'ta **depolamayız** (cihazda Anahtar Zinciri kullanır). 

## Üçüncü Taraflar 

| Parti | Rol | 
|----------|------| 
| **Elma** | App Store dağıtımı; isteğe bağlı iCloud KVS; widget'lar / Siri / Kısayollar; Posta, Paylaşım Sayfası, Safari Görünüm Denetleyicisi; isteğe bağlı StoreKit ipucu | 
| **Açtığınız web siteleri ve arama motorları** | Ziyaret ettiğiniz sayfalar için normal tarayıcı trafiği alın | 

## Saklama ve Silme 

Yerel tercihler ve yer işaretleri, siz onları değiştirene, temizleyene ya da uygulamayı kaldırana kadar kalır. İsteğe bağlı iCloud verileri, siz senkronizasyonu devre dışı bırakana ve/veya Apple'ın araçları aracılığıyla temizleyene kadar Apple'ın politikaları kapsamında kalır. Sunucularımızda kişisel veri toplamadığımız için e-postanıza yanıt vermenin ötesinde silebileceğimiz bir hesap veri kümesi yoktur. 

## Bu Politikadaki Değişiklikler

Bu sayfayı zaman zaman güncelleyebiliriz. Yukarıdaki “Son güncelleme” tarihi, yaptığımız değişikliklerle birlikte değişecektir. Değişikliklerden sonra devam eden kullanım, güncellenmiş politikayı kabul ettiğiniz anlamına gelir.

## Bizimle İletişime Geçin

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Uygulama Mağazası Bağlantısı için genel bağlantıya ihtiyacınız varsa, bu [Gizlilik Politikası](../privacy) sayfasını tarayıcıda açın ve adres çubuğundaki URL’yi kopyalayın.

</section>
