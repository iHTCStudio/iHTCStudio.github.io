---
layout: app
title: iAppManager — Support
app_id: iAppManager
description: Native App Store Connect desk for iPhone, iPad and Mac — API Key login, versions & IPA upload, metadata & screenshots, IAP, TestFlight, certificates, reports, reviews and widgets.
---

<section lang="en" markdown="1">

**Ship faster. Leave the browser maze behind.**

iAppManager (爱应用者) is a **native App Store Connect workstation** for iPhone, iPad and Mac. Sign in with an **API Key**, keep credentials in **Keychain**, and talk **directly to Apple** — versions, screenshots, IAP, TestFlight, certificates, sales reports and customer reviews in one place. **No iHTC Studio account. No ads. No analytics SDK. No third-party backend for your ASC data.**

**At a glance:** multi-account API Key login · App list with platform & pipeline filters · Overview readiness checklist · versions & review submissions · Build Upload REST (IPA/PKG) · metadata & media with cross-locale copy · Custom Product Pages · In-App Events · App Clips · store experiments · featuring nominations · availability & pricing · age rating · accessibility · App Tags · IAP & subscriptions · Game Center · TestFlight · customer reviews · certificates & devices · users & roles · sales / finance / Analytics reports · Webhooks · widgets & `iappmanager://` deep links · English / 简体 / 繁體.

> Built for indie developers and small teams who live in App Store Connect every week — and want a desk that feels like a Mac app, not a tab farm.

## Getting Started

1. Create an **App Store Connect API Key** (Admin or App Manager recommended): App Store Connect → **Users and Access** → **Integrations** → **App Store Connect API** → create a key, download the **`.p8` once**, and note **Issuer ID** + **Key ID**.
2. Open iAppManager → paste Issuer ID / Key ID / PEM (or pick the `.p8`) → verify (calls `GET /v1/apps`). Keys are stored in **Keychain** on this device.
3. Finish the short **onboarding** (certificates · reports · widgets · privacy notes). Replay guides anytime under **Settings → Help**.
4. On **My Apps**, pick **list / grid / cards**, pin favorites, filter by **platform** (iOS / macOS / tvOS / visionOS) or **status** (on sale · off sale · waiting · in review · rejected · pending developer release).
5. Open an app → start from **Overview** (latest version/build, shortcuts, soft readiness checklist, recent submissions).
6. Walk the release path: **Versions** → attach a **Build** → fill **Metadata / Media** → **Review Detail** → submit via **Review Submissions** (or “send now”).
7. Add **Home Screen widgets** (Account Hub, Apps Pulse, Review Desk, Quick Actions) and try `iappmanager://` from Shortcuts.

> In-app **Release / IAP / TestFlight / Reports** guides are one tap away (also via deep links below).

## Why you’ll want to download

- **One native desk for the whole ship** — stop bouncing between ASC web tabs for versions, assets, IAP, TestFlight, certs and reports.
- **API Key, not another password dance** — Issuer ID + Key ID + `.p8` in Keychain; multi-account switch; remove account deletes the local key.
- **Upload builds without Transporter** — WWDC25 **Build Upload REST** for IPA/PKG; same pipeline on iOS (large files still prefer Mac).
- **Babysitter-level guides inside the app** — release readiness, IAP, TestFlight and reports explain hard vs soft checks before you burn a review cycle.
- **See your pipeline on the Lock Screen** — widgets mirror on-sale / waiting / in-review / rejected / pending-release counts (same buckets as My Apps filters).
- **Privacy by architecture** — ASC traffic goes to `api.appstoreconnect.apple.com`; iHTC Studio does not host your apps, keys or reports.

## Features

### Sign-in & accounts

- **API Key only** (Issuer ID / Key ID / `.p8`) — no Apple ID OAuth inside the app
- Keychain storage; **multi-account**; sign-out / remove deletes the local secret
- In-app **“How to get an API Key”** illustrated guide

### My Apps

- **List / grid / cards** layouts (list by default) with column controls
- Per-account **pinning**; **platform** and **status** filters with ~10‑minute catalog cache (force refresh rescans with progress)
- **On sale = available in at least one territory**; pipeline buckets independent of storefront presence
- Context menu: pin, jump to modules, copy name / Bundle ID / Apple ID / SKU / store · ASC · deep links / summary; open App Store or ASC
- Icons: ASC build artwork → iTunes Lookup → monogram, disk-cached

### Overview & release readiness

- Latest version / build summary, module shortcuts, recent review submissions
- **Soft checklist** (primary screenshot size, copyright, age rating, and more)
- Versions / Submissions apply **hard blockers** (build state, demo credentials when required)
- Guide: `iappmanager://release-guide`

### Versions, builds & submissions

- Create versions, attach builds, submit / cancel, release modes (manual / auto / scheduled), phased release, **Release Now** when pending developer release
- **Build Upload REST** for IPA/PKG; build size; diagnostics; Beta App Clip; export compliance
- **Background Assets** (`.aar`) create / chunked upload / External Beta & App Store review paths
- **Encryption declarations** with document upload; soft-checked from Overview
- **Review Submissions** draft / add items / submit; “send now” or “add to draft”
- **Review Detail** — contact, demo account, notes, attachments, Routing App Coverage

### Store listing & growth

- **Metadata** — App Info vs Version Listing; categories, copyright, EULA, primary locale; Android mapping; multi-locale with ★ primary; **cross-locale copy**
- **Screenshots & previews** — by version / locale / device size; reservation upload; cross-locale copy; poster frame timecode; coverage by real assets
- **Batch assets workstation** — upload screenshots / previews across locales × sizes in one desk
- **Download-size workbench** — inspect build download sizes with soft limit hints
- **SKU search** on My Apps; narrow-screen adaptive action bars for dense row actions
- **Custom Product Pages** — visibility, deep links, promo text, Search Keywords, media, submit
- **In-App Events**, **App Clips** (default + advanced experiences), **store experiments** (traffic separate from review), **featuring nominations** — galleries with load-more where lists truncate
- **Availability**, **pricing** (pick a price point, then apply — including equalization preview), **age rating**, **accessibility declarations**, **App Tags**
- Frequent forms support **⌘S** save on Mac

### Monetization & Game Center

- IAP / subscription groups, localizations, review screenshots/notes, territorial availability, price points
- Introductory / promotional / win-back offers; **Offer Codes**; promotional images; grace period; server notification URLs; CSV import/export; submit (including subscription groups)
- Guide: `iappmanager://iap-guide`
- **Game Center** — achievements, leaderboards / sets, challenges / activities, multiplayer, matchmaking

### TestFlight

- Groups, public links, recruitment criteria, metrics, invitations, individual testers, builds, What to Test, Beta license / review
- Feedback inbox with CSV + **bulk export** of full-size screenshots / crash logs (Mac folder / iOS zip + manifest)
- Guide: `iappmanager://testflight-guide`

### Certificates, users, reports & reviews

- Certificates (in-app CSR / import) · profiles · Bundle IDs & Capabilities · Merchant / Pass Type · devices (Keychain install on **macOS**)
- Invite users, roles, app visibility, supply permissions; Sandbox testers
- **Reports** — sales / finance / Analytics with scenario shortcuts, custom presets, **wide-table TSV preview** (column toggle, search, fullscreen landscape) & **lightweight summary charts**; guide `iappmanager://reports-guide`
- Customer reviews — filter, search, reply / delete reply, **reply templates** (up to 20 per account)
- **Webhooks** — create / edit / ping / deliveries (does not host your public callback)

### Widgets, shortcuts & polish

- Widgets: **Account Hub**, **Apps Pulse** (S/M/L), **Review Desk**, configurable **Quick Actions**
- `iappmanager://` deep links + App Intents (open a managed app + optional module) — see [Shortcut Links](url-scheme)
- Appearance, accent color, EN / 简 / 繁 (hot-swap without losing navigation)
- iOS **alternate icons** (IconStyle1–7); optional StoreKit tip; feedback mail

### Privacy

- API private keys stay in **device Keychain**; business calls go to **Apple** only
- Optional icon enrichment via Apple iTunes Lookup; thumbnail cache clearable in Settings
- App Group shares **local** widget snapshots only — never uploaded to iHTC Studio
- Full details: [Privacy Policy](privacy)

## Get the App

| Channel | Link |
|---------|------|
| App Store | [Download on the App Store](https://apps.apple.com/app/id6794497110) |

## System Requirements

| Component | Minimum |
|-----------|---------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |
| Widgets | iOS 17.0+ |
| Large IPA upload | Prefer Mac |

## Contact Us

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

We typically respond within 48 hours.

[FAQ](faq) · [Shortcut Links](url-scheme) · [Privacy Policy](privacy)

</section>
<section lang="zh-CN" markdown="1">

**更快上架。少在网页标签页里打转。**

爱应用者（iAppManager）是面向 iPhone、iPad 与 Mac 的 **原生 App Store Connect 工作台**。用 **API Key** 登录，密钥存 **钥匙串**，请求 **直连 Apple**——版本、截图、内购、TestFlight、证书、销售报表与顾客评价，一处完成。**无需 iHTC Studio 账号。无广告。无分析 SDK。不上架你的 ASC 数据到第三方服务器。**

**一眼看懂：** 多账号 API Key 登录 · 平台与流水线筛选 · Overview 提审就绪清单 · 版本与审核提交 · Build Upload REST（IPA/PKG）· 元数据与素材跨语言复制 · 自定义产品页 · App 内活动 · App Clips · 商店实验 · 推荐提名 · 上架地区与定价 · 年龄分级 · 辅助功能 · App Tags · 内购与订阅 · Game Center · TestFlight · 顾客评价 · 证书与设备 · 用户与角色 · 销售 / 财务 / Analytics 报表 · Webhooks · 小组件与 `iappmanager://` 深链 · English / 简体 / 繁體。

> 为每周都要泡在 App Store Connect 的独立开发者与小团队而做——桌面感像 Mac App，而不是浏览器标签农场。

## 快速上手

1. 创建 **App Store Connect API 密钥**（建议 Admin 或 App Manager）：App Store Connect → **用户和访问** → **集成** → **App Store Connect API** → 创建密钥，**仅一次**下载 `.p8`，记下 **Issuer ID** 与 **密钥 ID**。
2. 打开爱应用者 → 填写 Issuer ID / 密钥 ID / PEM（或选择 `.p8`）→ 验证（请求 `GET /v1/apps`）。密钥保存在本机 **钥匙串**。
3. 完成简短 **首启引导**（证书 · 报表 · 小组件 · 隐私要点）。可随时在 **设置 → 帮助** 重看指南。
4. 在 **我的 App** 选择 **列表 / 网格 / 卡片**，置顶常用项，按 **平台**（iOS / macOS / tvOS / visionOS）或 **状态**（已上架 · 已下架 · 送审中 · 审核中 · 被拒 · 待开发者发布）筛选。
5. 进入某个 App → 从 **Overview** 开始（最新版本/构建、快捷入口、提审软清单、最近提交）。
6. 走完发布路径：**版本** → 关联 **构建** → 填写 **元数据 / 素材** → **审核备注** → 通过 **审核提交** 送审（或「立刻送审」）。
7. 添加 **主屏小组件**（账号中心、Apps Pulse、审核台、快捷四入口），并用快捷指令试试 `iappmanager://`。

> 应用内 **提审就绪 / 内购 / TestFlight / 报表** 保姆指南一键可达（亦可用下方深链）。

## 为什么值得下载

- **上架全流程一张原生桌面** — 不必再在 ASC 网页标签之间来回跳：版本、素材、内购、TestFlight、证书与报表。
- **API Key，而不是反复输密码** — Issuer ID + 密钥 ID + `.p8` 存钥匙串；多账号切换；移除账号即删本地密钥。
- **不用 Transporter 也能传包** — WWDC25 **Build Upload REST** 上传 IPA/PKG；iOS 同管线（大文件仍建议 Mac）。
- **应用内保姆级指南** — 提审就绪、内购、TestFlight、报表讲清硬拦截与软检查，少浪费一次审核轮次。
- **流水线状态上锁屏** — 小组件与「我的 App」同口径展示已上架 / 送审 / 审核中 / 被拒 / 待发布。
- **架构即隐私** — ASC 流量只到 `api.appstoreconnect.apple.com`；iHTC Studio 不托管你的 App、密钥或报表。

## 功能特性

### 登录与账号

- **仅 API Key**（Issuer ID / 密钥 ID / `.p8`）——应用内不做 Apple ID OAuth
- 钥匙串存储；**多账号**；退出/移除会删除本机密钥
- 应用内 **「如何获取 API Key」** 图文引导

### 我的 App

- **列表 / 网格 / 卡片**（默认列表）与列数控制
- 按账号 **置顶**；**平台**与**状态**筛选，全目录约 10 分钟缓存（强制刷新可重扫并显示进度）
- **已上架 = 至少一地区可用**；流水线分桶与店面在售相互独立
- 右键/长按：置顶、直达模块、复制名称 / Bundle ID / Apple ID / SKU / 商店·ASC·深链 / 摘要；外开 App Store 或 ASC
- 图标：ASC 构建图标 → iTunes Lookup → 字母占位，磁盘缓存

### Overview 与提审就绪

- 最新版本/构建摘要、模块快捷入口、最近审核提交
- **软清单**（主尺寸截图、版权、年龄分级等）
- 版本 / 审核提交有 **硬拦截**（构建状态、需要演示账号时缺凭据等）
- 指南：`iappmanager://release-guide`

### 版本、构建与审核提交

- 创建版本、关联构建、提审/取消、发布方式（手动/自动/定时）、分阶段发布、待开发者发布时 **立即发布**
- **Build Upload REST** 上传 IPA/PKG；构建体积；诊断；Beta App Clip；出口合规
- **后台资源**（`.aar`）创建 / 分片上传 / External Beta 与 App Store 提审
- **加密声明**与证明文档；Overview 软检查
- **审核提交**草稿 / 加项 / 提交；「立刻送审」或「加入草稿」
- **审核备注** — 联系人、演示账号、备注、附件、Routing App Coverage

### 商店上架与增长

- **元数据** — App Info 与 Version Listing；类别、版权、EULA、主语言；Android 映射；多语言 ★；**跨语言复制**
- **截图与预览** — 按版本 / 语言 / 尺寸；reservation 上传；跨语言复制；海报帧时间码；覆盖率按真实素材计
- **批量素材工作台** — 按语言 × 尺寸批量上传截图 / 预览
- **下载体积工作台** — 查看构建下载体积与软限额提示
- **我的 App 按 SKU 搜索**；窄屏自适应操作条（主操作 + 溢出菜单）
- **自定义产品页** — 可见性、深链、宣传文案、Search Keywords、素材、提审
- **App 内活动**、**App Clips**（默认 + 高级体验）、**商店实验**（启停流量与提审分开）、**推荐提名** — 图库浏览，列表截断处可续载
- **上架地区**、**定价**（先选价格点再应用，含等化预览）、**年龄分级**、**辅助功能声明**、**App Tags**
- Mac 高频表单支持 **⌘S** 保存

### 变现与 Game Center

- 内购 / 订阅组、本地化、审核截图/备注、地区可用性、价格点
- 推介 / 促销 / 赢回；**Offer Codes**；推广图；宽限期；服务器通知 URL；CSV；提审（含订阅组）
- 指南：`iappmanager://iap-guide`
- **Game Center** — 成就、排行榜/集、挑战/活动、多人、匹配

### TestFlight

- 测试组、公开链接、招募条件、指标、邀测、单独测试员、组内构建、What to Test、Beta 许可/审核
- Feedback 收件箱：CSV + **批量导出**全尺寸截图/崩溃日志（Mac 选文件夹 / iOS zip + manifest）
- 指南：`iappmanager://testflight-guide`

### 证书、用户、报表与评价

- 证书（应用内 CSR / 导入）· 描述文件 · Bundle ID 与 Capabilities · Merchant / Pass Type · 设备（钥匙串安装面向 **macOS**）
- 邀请用户、角色、App 可见性、供应权限；Sandbox 测试员
- **报表** — 销售 / 财务 / Analytics，场景快捷与自定义预设，**宽表 TSV 预览**（列显隐、搜索、全屏横屏）与**轻量摘要图**；指南 `iappmanager://reports-guide`
- 顾客评价 — 筛选、搜索、回复/删回复、**回复模板**（每账号最多 20 条）
- **Webhooks** — 创建/编辑/Ping/投递记录（不托管你的公网回调）

### 小组件、快捷与体验

- 小组件：**账号中心**、**Apps Pulse**（小/中/大）、**审核台**、可配置 **快捷四入口**
- `iappmanager://` 深链 + App Intents（打开指定 App + 可选模块）——见 [快捷链接](url-scheme)
- 外观、强调色、英 / 简 / 繁（热切换不丢导航）
- iOS **备用图标**（IconStyle1–7）；可选 StoreKit 赞赏；反馈邮件

### 隐私

- API 私钥仅存 **本机钥匙串**；业务请求只到 **Apple**
- 可选经 Apple iTunes Lookup 补全图标；缩略图缓存可在设置清空
- App Group 仅共享 **本地** 小组件摘要——不会上传到 iHTC Studio
- 详见 [隐私政策](privacy)

## 获取应用

| 渠道 | 链接 |
|------|------|
| App Store | [在 App Store 下载](https://apps.apple.com/app/id6794497110) |

## 系统要求

| 组件 | 最低版本 |
|------|----------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |
| 小组件 | iOS 17.0+ |
| 大体积 IPA 上传 | 建议使用 Mac |

## 联系我们

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

通常 48 小时内回复。

[常见问题](faq) · [快捷链接](url-scheme) · [隐私政策](privacy)

</section>
<section lang="zh-TW" markdown="1">

**更快上架。少在網頁分頁裡打轉。**

愛應用者（iAppManager）是面向 iPhone、iPad 與 Mac 的 **原生 App Store Connect 工作台**。用 **API Key** 登入，金鑰存 **鑰匙圈**，請求 **直連 Apple**——版本、截圖、內購、TestFlight、憑證、銷售報表與顧客評價，一處完成。**無需 iHTC Studio 帳號。無廣告。無分析 SDK。不上架你的 ASC 資料到第三方伺服器。**

**一眼看懂：** 多帳號 API Key 登入 · 平台與流水線篩選 · Overview 送審就緒清單 · 版本與審核提交 · Build Upload REST（IPA/PKG）· 中繼資料與素材跨語言複製 · 自訂產品頁 · App 內活動 · App Clips · 商店實驗 · 推薦提名 · 上架地區與定價 · 年齡分級 · 輔助功能 · App Tags · 內購與訂閱 · Game Center · TestFlight · 顧客評價 · 憑證與裝置 · 使用者與角色 · 銷售 / 財務 / Analytics 報表 · Webhooks · 小工具與 `iappmanager://` 深鏈 · English / 簡體 / 繁體。

> 為每週都要泡在 App Store Connect 的獨立開發者與小團隊而做——桌面感像 Mac App，而不是瀏覽器分頁農場。

## 快速上手

1. 建立 **App Store Connect API 金鑰**（建議 Admin 或 App Manager）：App Store Connect → **使用者和存取權限** → **整合** → **App Store Connect API** → 建立金鑰，**僅一次**下載 `.p8`，記下 **Issuer ID** 與 **金鑰 ID**。
2. 打開愛應用者 → 填寫 Issuer ID / 金鑰 ID / PEM（或選擇 `.p8`）→ 驗證（請求 `GET /v1/apps`）。金鑰保存在本機 **鑰匙圈**。
3. 完成簡短 **首啟引導**（憑證 · 報表 · 小工具 · 隱私要點）。可隨時在 **設定 → 說明** 重看指南。
4. 在 **我的 App** 選擇 **列表 / 網格 / 卡片**，置頂常用項，按 **平台**（iOS / macOS / tvOS / visionOS）或 **狀態**（已上架 · 已下架 · 送審中 · 審核中 · 被拒 · 待開發者發佈）篩選。
5. 進入某個 App → 從 **Overview** 開始（最新版本/建置、快捷入口、送審軟清單、最近提交）。
6. 走完發佈路徑：**版本** → 關聯 **建置** → 填寫 **中繼資料 / 素材** → **審核備註** → 透過 **審核提交** 送審（或「立刻送審」）。
7. 加入 **主畫面小工具**（帳號中心、Apps Pulse、審核台、快捷四入口），並用捷徑試試 `iappmanager://`。

> 應用內 **送審就緒 / 內購 / TestFlight / 報表** 保姆指南一鍵可達（亦可用下方深鏈）。

## 為什麼值得下載

- **上架全流程一張原生桌面** — 不必再在 ASC 網頁分頁之間來回跳：版本、素材、內購、TestFlight、憑證與報表。
- **API Key，而不是反覆輸密碼** — Issuer ID + 金鑰 ID + `.p8` 存鑰匙圈；多帳號切換；移除帳號即刪本機金鑰。
- **不用 Transporter 也能傳包** — WWDC25 **Build Upload REST** 上傳 IPA/PKG；iOS 同管線（大檔仍建議 Mac）。
- **應用內保姆級指南** — 送審就緒、內購、TestFlight、報表講清硬攔截與軟檢查，少浪費一次審核輪次。
- **流水線狀態上鎖定畫面** — 小工具與「我的 App」同口徑展示已上架 / 送審 / 審核中 / 被拒 / 待發佈。
- **架構即隱私** — ASC 流量只到 `api.appstoreconnect.apple.com`；iHTC Studio 不託管你的 App、金鑰或報表。

## 功能特性

### 登入與帳號

- **僅 API Key**（Issuer ID / 金鑰 ID / `.p8`）——應用內不做 Apple ID OAuth
- 鑰匙圈儲存；**多帳號**；退出/移除會刪除本機金鑰
- 應用內 **「如何取得 API Key」** 圖文引導

### 我的 App

- **列表 / 網格 / 卡片**（預設列表）與欄數控制
- 按帳號 **置頂**；**平台**與**狀態**篩選，全目錄約 10 分鐘快取（強制重新整理可重掃並顯示進度）
- **已上架 = 至少一地區可用**；流水線分桶與店面在售相互獨立
- 右鍵/長按：置頂、直達模組、複製名稱 / Bundle ID / Apple ID / SKU / 商店·ASC·深鏈 / 摘要；外開 App Store 或 ASC
- 圖示：ASC 建置圖示 → iTunes Lookup → 字母佔位，磁碟快取

### Overview 與送審就緒

- 最新版本/建置摘要、模組快捷入口、最近審核提交
- **軟清單**（主尺寸截圖、版權、年齡分級等）
- 版本 / 審核提交有 **硬攔截**（建置狀態、需要示範帳號時缺憑據等）
- 指南：`iappmanager://release-guide`

### 版本、建置與審核提交

- 建立版本、關聯建置、送審/取消、發佈方式（手動/自動/定時）、分階段發佈、待開發者發佈時 **立即發佈**
- **Build Upload REST** 上傳 IPA/PKG；建置體積；診斷；Beta App Clip；出口合規
- **背景資源**（`.aar`）建立 / 分片上傳 / External Beta 與 App Store 送審
- **加密聲明**與證明文件；Overview 軟檢查
- **審核提交**草稿 / 加項 / 提交；「立刻送審」或「加入草稿」
- **審核備註** — 聯絡人、示範帳號、備註、附件、Routing App Coverage

### 商店上架與成長

- **中繼資料** — App Info 與 Version Listing；類別、版權、EULA、主語言；Android 對應；多語言 ★；**跨語言複製**
- **截圖與預覽** — 按版本 / 語言 / 尺寸；reservation 上傳；跨語言複製；海報幀時間碼；覆蓋率按真實素材計
- **批次素材工作台** — 按語言 × 尺寸批次上傳截圖 / 預覽
- **下載體積工作台** — 查看建置下載體積與軟限額提示
- **我的 App 按 SKU 搜尋**；窄屏自適應操作列（主操作 + 溢出選單）
- **自訂產品頁** — 可見性、深鏈、宣傳文案、Search Keywords、素材、送審
- **App 內活動**、**App Clips**（預設 + 進階體驗）、**商店實驗**（啟停流量與送審分開）、**推薦提名** — 圖庫瀏覽，列表截斷處可續載
- **上架地區**、**定價**（先選價格點再套用，含等化預覽）、**年齡分級**、**輔助功能聲明**、**App Tags**
- Mac 高頻表單支援 **⌘S** 儲存

### 變現與 Game Center

- 內購 / 訂閱群組、本地化、審核截圖/備註、地區可用性、價格點
- 推介 / 促銷 / 贏回；**Offer Codes**；推廣圖；寬限期；伺服器通知 URL；CSV；送審（含訂閱群組）
- 指南：`iappmanager://iap-guide`
- **Game Center** — 成就、排行榜/集、挑戰/活動、多人、配對

### TestFlight

- 測試群組、公開連結、招募條件、指標、邀測、單獨測試員、組內建置、What to Test、Beta 授權/審核
- Feedback 收件匣：CSV + **批次匯出**全尺寸截圖/當機紀錄（Mac 選資料夾 / iOS zip + manifest）
- 指南：`iappmanager://testflight-guide`

### 憑證、使用者、報表與評價

- 憑證（應用內 CSR / 匯入）· 描述檔 · Bundle ID 與 Capabilities · Merchant / Pass Type · 裝置（鑰匙圈安裝面向 **macOS**）
- 邀請使用者、角色、App 可見性、供應權限；Sandbox 測試員
- **報表** — 銷售 / 財務 / Analytics，場景快捷與自訂預設，**寬表 TSV 預覽**（欄顯隱、搜尋、全螢幕橫向）與**輕量摘要圖**；指南 `iappmanager://reports-guide`
- 顧客評價 — 篩選、搜尋、回覆/刪回覆、**回覆範本**（每帳號最多 20 條）
- **Webhooks** — 建立/編輯/Ping/投遞紀錄（不託管你的公網回呼）

### 小工具、快捷與體驗

- 小工具：**帳號中心**、**Apps Pulse**（小/中/大）、**審核台**、可設定 **快捷四入口**
- `iappmanager://` 深鏈 + App Intents（打開指定 App + 可選模組）——見 [快捷連結](url-scheme)
- 外觀、強調色、英 / 簡 / 繁（熱切換不丟導覽）
- iOS **備用圖示**（IconStyle1–7）；可選 StoreKit 打賞；回饋郵件

### 隱私

- API 私鑰僅存 **本機鑰匙圈**；業務請求只到 **Apple**
- 可選經 Apple iTunes Lookup 補全圖示；縮圖快取可在設定清空
- App Group 僅共享 **本機** 小工具摘要——不會上傳到 iHTC Studio
- 詳見 [隱私權政策](privacy)

## 取得應用程式

| 管道 | 連結 |
|------|------|
| App Store | [在 App Store 下載](https://apps.apple.com/app/id6794497110) |

## 系統需求

| 元件 | 最低版本 |
|------|----------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |
| 小工具 | iOS 17.0+ |
| 大體積 IPA 上傳 | 建議使用 Mac |

## 聯絡我們

- **電子郵件：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

通常 48 小時內回覆。

[常見問題](faq) · [快捷連結](url-scheme) · [隱私權政策](privacy)

</section>
<section lang="ja" markdown="1">

**出荷を速く。ブラウザの迷路から抜け出す。**

iAppManager（爱应用者）は、iPhone、iPad、Mac 向けの **ネイティブ App Store Connect ワークステーション**です。**API Key** でサインインし、資格情報は **Keychain** に保存。Apple と **直接**通信 — バージョン、スクリーンショット、IAP、TestFlight、証明書、売上レポート、カスタマーレビューを一括管理。**iHTC Studio アカウント不要。広告なし。分析 SDK なし。ASC データ用の第三者 backend なし。**

**一覧：** マルチアカウント API Key ログイン · プラットフォーム／パイプライン filter のアプリ一覧 · Overview 準備チェックリスト · バージョンとレビュー提出 · Build Upload REST（IPA/PKG）· クロスロケールコピー付きメタデータ／メディア · Custom Product Pages · In-App Events · App Clips · ストア実験 · フィーチャー提名 · 提供状況と価格 · 年齢制限 · アクセシビリティ · App Tags · IAP／サブスクリプション · Game Center · TestFlight · カスタマーレビュー · 証明書とデバイス · ユーザーとロール · 売上／財務／Analytics レポート · Webhooks · ウィジェットと `iappmanager://` ディープリンク · English／简体／繁體

> 毎週 App Store Connect に住むインディー開発者と小規模チーム向け — タブだらけの Web ではなく、Mac アプリのようなデスク。

## はじめに

1. **App Store Connect API Key** を作成（Admin または App Manager 推奨）：App Store Connect → **Users and Access** → **Integrations** → **App Store Connect API** → キー作成、**`.p8` を一度だけ** ダウンロード、**Issuer ID** + **Key ID** を控える。
2. iAppManager を開く → Issuer ID／Key ID／PEM を貼付（または `.p8` を選択）→ 検証（`GET /v1/apps`）。キーは **このデバイスの Keychain** に保存。
3. 短い **オンボーディング**（証明書 · レポート · ウィジェット · プライバシー）。**設定 → ヘルプ** でいつでも再生。
4. **My Apps** で **リスト／グリッド／カード**、お気に入りピン、**プラットフォーム**（iOS／macOS／tvOS／visionOS）または **ステータス**（販売中 · 非販売 · 待機 · 審査中 · 却下 · 開発者リリース待ち）でフィルタ。
5. アプリを開く → **Overview** から（最新バージョン／ビルド、ショートカット、ソフト準備チェックリスト、最近の提出）。
6. リリース経路：**Versions** → **Build** 添付 → **Metadata／Media** → **Review Detail** → **Review Submissions** で提出（または「今すぐ送信」）。
7. **ホーム画面ウィジェット**（Account Hub、Apps Pulse、Review Desk、Quick Actions）と Shortcuts から `iappmanager://` を試す。

> アプリ内 **Release／IAP／TestFlight／Reports** ガイドはワンタップ（下記ディープリンクも可）。

## ダウンロードする理由

- **出荷全体を一つのネイティブデスク** — バージョン、素材、IAP、TestFlight、証明書、レポートの ASC Web タブ往復をやめる。
- **API Key — 別のパスワード踊りではない** — Issuer ID + Key ID + `.p8` を Keychain；マルチアカウント；アカウント削除でローカルキー削除。
- **Transporter なしでビルドアップロード** — WWDC25 **Build Upload REST**（IPA/PKG）；iOS も同じ API（大容量は **Mac** 推奨）。
- **アプリ内の手厚いガイド** — リリース準備、IAP、TestFlight、レポートで hard／soft チェックを説明。
- **ロック画面でパイプライン** — ウィジェットが My Apps と同じ区分で on-sale／waiting／in-review／rejected／pending-release を表示。
- **アーキテクチャによるプライバシー** — ASC 通信は `api.appstoreconnect.apple.com`；iHTC Studio はアプリ・キー・レポートをホストしない。

## 機能

### サインインとアカウント

- **API Key のみ**（Issuer ID／Key ID／`.p8`）— アプリ内 Apple ID OAuth なし
- Keychain；**マルチアカウント**；サインアウト／削除でローカル秘密鍵削除
- アプリ内 **「API Key の取得方法」** 図解ガイド

### My Apps

- **リスト／グリッド／カード**（既定リスト）と列コントロール
- アカウントごと **ピン**；**プラットフォーム**・**ステータス** filt（約 10 分キャッシュ、強制更新で再スキャン）
- **On sale = 少なくとも 1 地域で提供**；パイプライン区分は storefront とは独立
- コンテキストメニュー：ピン、モジュールへ、名前／Bundle ID／Apple ID／SKU／ストア · ASC · ディープリンク／概要のコピー；App Store または ASC を開く
- アイコン：ASC ビルド artwork → iTunes Lookup → モノグラム、ディスクキャッシュ

### Overview とリリース準備

- 最新バージョン／ビルド、モジュールショートカット、最近のレビュー提出
- **ソフトチェックリスト**（主スクリーンショットサイズ、著作権、年齢制限など）
- Versions／Submissions の **hard blocker**（ビルド状態、必要時デモ資格情報）
- ガイド：`iappmanager://release-guide`

### バージョン、ビルド、提出

- バージョン作成、ビルド添付、提出／キャンセル、リリースモード（手動／自動／スケジュール）、段階的リリース、**Release Now**（開発者リリース待ち時）
- **Build Upload REST**（IPA/PKG）；サイズ；診断；Beta App Clip；輸出コンプライアンス
- **Background Assets**（`.aar`）作成／チャンクアップロード／External Beta と App Store 審査経路
- **暗号化申告**とドキュメントアップロード；Overview からソフトチェック
- **Review Submissions** 下書き／項目追加／提出；「今すぐ」または下書きへ
- **Review Detail** — 連絡先、デモアカウント、メモ、添付、Routing App Coverage

### ストア掲載と成長

- **Metadata** — App Info と Version Listing；カテゴリ、著作権、EULA、プライマリロケール；Android マッピング；★ プライマリのマルチロケール；**クロスロケールコピー**
- **スクリーンショットとプレビュー** — バージョン／ロケール／デバイスサイズ；予約アップロード；クロスロケール；ポスターフレームタイムコード；実アセットによるカバレッジ
- **バッチアセットワークステーション** — ロケール×サイズ一括アップロード
- **ダウンロードサイズワークベンチ** — ソフト上限ヒント付きサイズ確認
- My Apps の **SKU 検索**；狭い画面の適応型アクションバー
- **Custom Product Pages** — 可視性、ディープリンク、プロモ、Search Keywords、メディア、提出
- **In-App Events**、**App Clips**、**ストア実験**（トラフィックは審査と分離）、**フィーチャー提名**
- **Availability**、**pricing**（価格ポイント選択と適用、均等化プレビュー含む）、**年齢制限**、**アクセシビリティ**、**App Tags**
- Mac では **⌘S** 保存

### 収益化と Game Center

- IAP／サブスクリプショングループ、ローカライズ、レビュー用スクショ／メモ、地域提供、価格ポイント
- 紹介／プロモ／ウィンバック；**Offer Codes**；プロモ画像；猶予期間；サーバー通知 URL；CSV 入出力；提出（サブスクリプショングループ含む）
- ガイド：`iappmanager://iap-guide`
- **Game Center** — 実績、リーダーボード／セット、チャレンジ／アクティビティ、マルチプレイ、マッチメイキング

### TestFlight

- グループ、公開リンク、募集条件、メトリクス、招待、個人テスター、ビルド、What to Test、ベータライセンス／レビュー
- フィードバック受信箱と CSV + **フルサイズスクショ／クラッシュログ一括エクスポート**（Mac フォルダ／iOS zip + manifest）
- ガイド：`iappmanager://testflight-guide`

### 証明書、ユーザー、レポート、レビュー

- 証明書（アプリ内 CSR／インポート）· プロファイル · Bundle ID と Capabilities · Merchant／Pass Type · デバイス（**macOS** で Keychain インストール）
- ユーザー招待、ロール、アプリ可視性、プロビジョニング；Sandbox テスター
- **Reports** — 売上／財務／Analytics、シナリオ、カスタムプリセット、**ワイド TSV プレビュー**（列切替、検索、全画面横向き）と**軽量サマリーチャート**；`iappmanager://reports-guide`
- カスタマーレビュー — filt、検索、返信／削除、**返信テンプレート**（アカウント最大 20）
- **Webhooks** — 作成／編集／ping／配信（公開コールバックはホストしない）

### ウィジェット、ショートカット、仕上げ

- ウィジェット：**Account Hub**、**Apps Pulse**（S/M/L）、**Review Desk**、**Quick Actions**
- `iappmanager://` + App Intents — [Shortcut Links](url-scheme)
- 外観、アクセント、EN／简／繁（ナビを失わずホットスワップ）
- iOS **代替アイコン**（IconStyle1–7）；StoreKit チップ；フィードバックメール

### プライバシー

- API 秘密鍵は **デバイス Keychain**；業務 API は **Apple** のみ
- iTunes Lookup による任意アイコン；Settings でサムネキャッシュ削除
- App Group は **ローカル** ウィジェットスナップショットのみ — iHTC Studio にアップロードしない
- 詳細：[Privacy Policy](privacy)

## アプリを入手

| チャンネル | リンク |
|---------|------|
| App Store | [Download on the App Store](https://apps.apple.com/app/id6794497110) |

## システム要件

| コンポーネント | 最小 |
|-----------|---------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |
| ウィジェット | iOS 17.0+ |
| 大容量 IPA | **Mac** 推奨 |

## お問い合わせ

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

通常 48 時間以内に返信します。

[FAQ](faq) · [Shortcut Links](url-scheme) · [Privacy Policy](privacy)

</section>
<section lang="ko" markdown="1">

**더 빠르게 출시하세요. 브라우저 미로에서 벗어나세요.**

iAppManager(爱应用者)는 iPhone, iPad, Mac용 **네이티브 App Store Connect 워크스테이션**입니다. **API Key**로 로그인하고 자격 증명은 **Keychain**에 보관하며 Apple과 **직접** 통신합니다 — 버전, 스크린샷, IAP, TestFlight, 인증서, 판매 보고서, 고객 리뷰를 한곳에서.**iHTC Studio 계정 없음. 광고 없음. analytics SDK 없음. ASC 데이터용 제3자 backend 없음.**

**한눈에:** 다중 계정 API Key · 플랫폼/파이프라인 filt 앱 목록 · Overview 준비 체크리스트 · 버전 및 리뷰 제출 · Build Upload REST(IPA/PKG) · cross-locale 메타데이터/미디어 · Custom Product Pages · In-App Events · App Clips · 스토어 실험 · featuring · 가용성/가격 · 연령 · 접근성 · App Tags · IAP/구독 · Game Center · TestFlight · 리뷰 · 인증서/기기 · 사용자/역할 · sales/finance/Analytics · Webhooks · 위젯 및 `iappmanager://` · EN/简体/繁體

> 매주 App Store Connect에 사는 인디 개발자와 소규모 팀 — 탭 농장이 아닌 Mac 앱 같은 책상.

## 시작하기

1. **App Store Connect API Key** 생성(Admin/App Manager 권장) → `.p8` **한 번** 다운로드, **Issuer ID** + **Key ID**
2. iAppManager → 붙여넣기 → 검증(`GET /v1/apps`). **Keychain** 저장
3. **온보딩** 완료. **설정 → 도움말**에서 가이드 재생
4. **My Apps** — list/grid/cards, pin, platform/status filt
5. **Overview**에서 시작
6. **Versions** → Build → Metadata/Media → Review Detail → **Review Submissions**
7. 홈 화면 **위젯** 및 `iappmanager://`

## 다운로드 이유

- **하나의 네이티브 책상** — ASC 웹 탭 전환 중단
- **API Key** — Keychain의 Issuer/Key/`.p8`; 다중 계정
- **Transporter 없이 업로드** — WWDC25 Build Upload REST
- **앱 내 가이드** — hard/soft 체크
- **잠금 화면 파이프라인** — 위젯
- **아키텍처 프라이버시** — `api.appstoreconnect.apple.com`

## 기능

(Sign-in, My Apps, Overview, Versions, Store listing, Monetization, TestFlight, Certificates/Reports, Widgets, Privacy — EN index와 동일 범위; deep links: `iappmanager://release-guide`, `iappmanager://iap-guide`, `iappmanager://testflight-guide`, `iappmanager://reports-guide`)

### 개인정보

키는 **Keychain**; 호출은 **Apple**만. [Privacy Policy](privacy)

## 앱 받기

| App Store | [Download](https://apps.apple.com/app/id6794497110) |

## 시스템 요구 사항

iOS 17.0+, macOS 14.0+, 위젯 iOS 17.0+, 대용량 IPA는 Mac 권장.

## 문의

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 보통 48시간 이내.

[FAQ](faq) · [Shortcut Links](url-scheme) · [Privacy Policy](privacy)

</section>
<section lang="ru" markdown="1">

**Публикуйте быстрее. Выйдите из лабиринта браузера.**

iAppManager (爱应用者) — **нативная рабочая станция App Store Connect** для iPhone, iPad и Mac. Вход по **API Key**, учётные данные в **Keychain**, общение **напрямую с Apple** — версии, скриншоты, IAP, TestFlight, сертификаты, отчёты о продажах и отзывы клиентов в одном месте. **Без аккаунта iHTC Studio. Без рекламы. Без analytics SDK. Без стороннего backend для данных ASC.**

**Кратко:** мультиаккаунт API Key · список приложений с фильтрами платформы и pipeline · чеклист готовности Overview · версии и review submissions · Build Upload REST (IPA/PKG) · метаданные и медиа с копированием между локалями · Custom Product Pages · In-App Events · App Clips · store experiments · featuring nominations · availability и pricing · возрастной рейтинг · accessibility · App Tags · IAP и подписки · Game Center · TestFlight · отзывы · сертификаты и устройства · пользователи и роли · sales / finance / Analytics · Webhooks · виджеты и deep links `iappmanager://` · English / 简体 / 繁體

> Для инди-разработчиков и небольших команд, которые каждую неделю живут в App Store Connect — стол, похожий на Mac-приложение, а не на ферму вкладок.

## Начало работы

1. Создайте **API Key App Store Connect** (рекомендуется Admin или App Manager): App Store Connect → **Users and Access** → **Integrations** → **App Store Connect API** → создайте ключ, скачайте **`.p8` один раз**, запишите **Issuer ID** + **Key ID**.
2. Откройте iAppManager → вставьте Issuer ID / Key ID / PEM (или выберите `.p8`) → проверка (`GET /v1/apps`). Ключи хранятся в **Keychain** этого устройства.
3. Пройдите короткий **onboarding** (сертификаты · отчёты · виджеты · конфиденциальность). Повтор гайдов в **Настройки → Справка**.
4. В **My Apps** выберите **list / grid / cards**, закрепите избранное, фильтруйте по **платформе** (iOS / macOS / tvOS / visionOS) или **статусу** (в продаже · не в продаже · ожидание · на review · отклонено · ожидает release разработчика).
5. Откройте приложение → начните с **Overview** (последняя версия/build, shortcuts, мягкий чеклист, недавние submissions).
6. Путь релиза: **Versions** → прикрепить **Build** → **Metadata / Media** → **Review Detail** → отправить через **Review Submissions** (или «отправить сейчас»).
7. Добавьте **виджеты Home Screen** (Account Hub, Apps Pulse, Review Desk, Quick Actions) и попробуйте `iappmanager://` из Shortcuts.

> Встроенные гайды **Release / IAP / TestFlight / Reports** — один tap (также deep links ниже).

## Зачем скачать

- **Один нативный стол для всего релиза** — без прыжков между вкладками ASC для версий, assets, IAP, TestFlight, certs и отчётов.
- **API Key, а не ещё один пароль** — Issuer ID + Key ID + `.p8` в Keychain; мультиаккаунт; удаление аккаунта удаляет локальный ключ.
- **Загрузка builds без Transporter** — WWDC25 **Build Upload REST** для IPA/PKG; тот же pipeline на iOS (большие файлы лучше на Mac).
- **Подробные гайды в приложении** — release readiness, IAP, TestFlight и reports объясняют hard vs soft checks до сжигания review cycle.
- **Pipeline на Lock Screen** — виджеты отражают в продаже / ожидание / review / отклонено / pending release (те же buckets, что My Apps).
- **Конфиденциальность архитектурой** — ASC traffic на `api.appstoreconnect.apple.com`; iHTC Studio не хостит ваши apps, keys или reports.

## Возможности

### Вход и аккаунты

- **Только API Key** (Issuer ID / Key ID / `.p8`) — без Apple ID OAuth в приложении
- Keychain; **мультиаккаунт**; sign-out / remove удаляет локальный secret
- In-app **«Как получить API Key»** с иллюстрациями

### My Apps

- **List / grid / cards** (list по умолчанию) с управлением колонками
- **Pin** по аккаунту; фильтры **platform** и **status** с ~10‑минутным cache каталога (force refresh с progress)
- **On sale = доступно хотя бы в одной territory**; pipeline buckets независимы от storefront
- Context menu: pin, jump to modules, copy name / Bundle ID / Apple ID / SKU / store · ASC · deep links / summary; open App Store или ASC
- Icons: ASC build artwork → iTunes Lookup → monogram, disk cache

### Overview и готовность к релизу

- Latest version/build, module shortcuts, recent review submissions
- **Soft checklist** (primary screenshot size, copyright, age rating и др.)
- Versions / Submissions — **hard blockers** (build state, demo credentials при необходимости)
- Guide: `iappmanager://release-guide`

### Versions, builds и submissions

- Create versions, attach builds, submit / cancel, release modes (manual / auto / scheduled), phased release, **Release Now** при pending developer release
- **Build Upload REST** IPA/PKG; build size; diagnostics; Beta App Clip; export compliance
- **Background Assets** (`.aar`) create / chunked upload / External Beta & App Store review paths
- **Encryption declarations** с upload документов; soft check из Overview
- **Review Submissions** draft / add items / submit; «now» или «add to draft»
- **Review Detail** — contact, demo account, notes, attachments, Routing App Coverage

### Store listing и рост

- **Metadata** — App Info vs Version Listing; categories, copyright, EULA, primary locale; Android mapping; multi-locale с ★ primary; **cross-locale copy**
- **Screenshots & previews** — by version / locale / device size; reservation upload; cross-locale; poster frame timecode; coverage real assets
- **Batch assets workstation** — upload across locales × sizes
- **Download-size workbench** — inspect sizes с soft limit hints
- **SKU search** в My Apps; adaptive action bars на узких экранах
- **Custom Product Pages**, **In-App Events**, **App Clips**, **store experiments**, **featuring nominations**
- **Availability**, **pricing** (price point + apply — equalization preview), **age rating**, **accessibility**, **App Tags**
- **⌘S** save на Mac

### Монетизация и Game Center

- IAP / subscription groups, localizations, review screenshots/notes, territorial availability, price points
- Intro / promo / win-back; **Offer Codes**; promotional images; grace period; server notification URLs; CSV import/export; submit
- Guide: `iappmanager://iap-guide`
- **Game Center** — achievements, leaderboards / sets, challenges / activities, multiplayer, matchmaking

### TestFlight

- Groups, public links, recruitment criteria, metrics, invites, individual testers, builds, What to Test, beta license / review
- Feedback inbox и CSV + **bulk export full-size screenshots / crash logs** (Mac folder / iOS zip + manifest)
- Guide: `iappmanager://testflight-guide`

### Сертификаты, пользователи, отчёты, отзывы

- Certificates (in-app CSR / import) · profiles · Bundle IDs & capabilities · Merchant / Pass Type · devices (**macOS**: Keychain install)
- User invites, roles, app visibility, provisioning; Sandbox testers
- **Reports** — sales / finance / Analytics, scenarios, custom presets, **wide TSV preview** и **summary charts**; `iappmanager://reports-guide`
- Customer reviews — filter, search, reply / delete, **reply templates** (max 20 per account)
- **Webhooks** — create / edit / ping / delivery

### Виджеты, shortcuts, polish

- Widgets: **Account Hub**, **Apps Pulse** (S/M/L), **Review Desk**, **Quick Actions**
- `iappmanager://` + App Intents — [Shortcut Links](url-scheme)
- Appearance, accent, EN / 简 / 繁 (hot swap)
- iOS **alternate icons** (IconStyle1–7); StoreKit tip; feedback email

### Конфиденциальность

- API secrets в **Keychain** устройства; business API только **Apple**
- Optional icons via iTunes Lookup; clear thumbnail cache в Settings
- App Group — только **local** widget snapshots; no upload iHTC Studio
- Details: [Privacy Policy](privacy)

## Скачать

| Канал | Ссылка |
|-------|--------|
| App Store | [Download on the App Store](https://apps.apple.com/app/id6794497110) |

## Системные требования

| Компонент | Минимум |
|-----------|---------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |
| Widgets | iOS 17.0+ |
| Большие IPA | **Mac** рекомендуется |

## Контакты

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Обычно отвечаем в течение 48 часов.

[FAQ](faq) · [Shortcut Links](url-scheme) · [Privacy Policy](privacy)

</section>
<section lang="th" markdown="1">

**ปล่อยแอปเร็วขึ้น ออกจากเขาวงกตเบราว์เซอร์**

iAppManager (爱应用者) คือ **สถานีงาน App Store Connect แบบ native** สำหรับ iPhone, iPad และ Mac ลงชื่อด้วย **API Key** เก็บข้อมูลใน **Keychain** และคุย **ตรงกับ Apple** — เวอร์ชัน สกรีนช็อต IAP TestFlight ใบรับรอง รายงานยอดขาย และรีวิวลูกค้าในที่เดียว **ไม่ต้องมีบัญชี iHTC Studio ไม่มีโฆษณา ไม่มี analytics SDK ไม่มี backend บุคคลที่สามสำหรับข้อมูล ASC**

**สรุป:** ล็อกอิน API Key หลายบัญชี · รายการแอปพร้อม filt แพลตฟอร์มและ pipeline · checklist ความพร้อม Overview · เวอร์ชันและ review submissions · Build Upload REST (IPA/PKG) · metadata และสื่อพร้อมคัดลอกข้าม locale · Custom Product Pages · In-App Events · App Clips · store experiments · featuring · availability และราคา · เรตติ้งอายุ · accessibility · App Tags · IAP และสมาชิก · Game Center · TestFlight · รีวิว · ใบรับรองและอุปกรณ์ · ผู้ใช้และบทบาท · รายงาน sales/finance/Analytics · Webhooks · วิดเจ็ตและ deep link `iappmanager://` · English / 简体 / 繁體

> สำหรับนักพัฒนาอินดีและทีมเล็กที่อยู่ใน App Store Connectทุกสัปดาห์ — โต๊ะทำงานที่รู้สึกเหมือนแอป Mac ไม่ใช่ฟาร์มแท็บ

## เริ่มต้น

1. สร้าง **App Store Connect API Key** (แนะนำ Admin หรือ App Manager): App Store Connect → **Users and Access** → **Integrations** → **App Store Connect API** → สร้างคีย์ ดาวน์โหลด **`.p8` ครั้งเดียว** จด **Issuer ID** + **Key ID**
2. เปิด iAppManager → วาง Issuer ID / Key ID / PEM (หรือเลือก `.p8`) → ตรวจสอบ (`GET /v1/apps`) คีย์อยู่ใน **Keychain** ของเครื่องนี้
3. ทำ **onboarding** สั้น (ใบรับรอง · รายงาน · วิดเจ็ต · ความเป็นส่วนตัว) ดู guide ซ้ำที่ **Settings → Help**
4. ใน **My Apps** เลือก **list / grid / cards** ปักหมุดรายการโปรด filt **แพลตฟอร์ม** (iOS / macOS / tvOS / visionOS) หรือ **สถานะ** (on sale · off sale · waiting · in review · rejected · pending developer release)
5. เปิดแอป → เริ่มที่ **Overview** (เวอร์ชัน/build ล่าสุด shortcuts checklist แบบ soft submissions ล่าสุด)
6. เส้นทาง release: **Versions** → แนบ **Build** → **Metadata / Media** → **Review Detail** → ส่งผ่าน **Review Submissions** (หรือ "send now")
7. เพิ่ม **วิดเจ็ต Home Screen** (Account Hub, Apps Pulse, Review Desk, Quick Actions) และลอง `iappmanager://` จาก Shortcuts

> คู่มือ **Release / IAP / TestFlight / Reports** ในแอปแตะครั้งเดียว (deep link ด้านล่าง)

## ทำไมควรดาวน์โหลด

- **โต๊ะ native เดียวสำหรับการปล่อยทั้งหมด** — หยุดสลับแท็บ ASC สำหรับเวอร์ชัน assets IAP TestFlight certs และรายงาน
- **API Key ไม่ใช่รำแ dance รหัสผ่าน** — Issuer ID + Key ID + `.p8` ใน Keychain หลายบัญชี ลบบัญชีลบคีย์ local
- **อัปโหลด build โดยไม่ใช้ Transporter** — WWDC25 **Build Upload REST** สำหรับ IPA/PKG pipeline เดียวกันบน iOS (ไฟล์ใหญ่ยังแนะนำ Mac)
- **คู่มือละเอียดในแอป** — release readiness IAP TestFlight และ reports อธิบาย hard vs soft checks
- **เห็น pipeline บน Lock Screen** — วิดเจ็ตสะท้อน on sale / waiting / in review / rejected / pending release
- **ความเป็นส่วนตัวโดยสถาปัตยกรรม** — ASC ไปที่ `api.appstoreconnect.apple.com` iHTC Studio ไม่โฮสต์แอป คีย์ หรือรายงานของคุณ

## ฟีเจอร์

### ล็อกอินและบัญชี

- **API Key เท่านั้น** (Issuer ID / Key ID / `.p8`) — ไม่มี Apple ID OAuth ในแอป
- Keychain **หลายบัญชี** sign-out / remove ลบ secret local
- คู่มือ **"วิธีรับ API Key"** ในแอป

### My Apps

- **List / grid / cards** (ค่าเริ่ม list) ควบคุมคอลัมน์
- **Pin** ต่อบัญชี filt **platform** และ **status** cache ~10 นาที (force refresh)
- **On sale = มีอย่างน้อยหนึ่ง territory** pipeline buckets แยกจาก storefront
- Context menu: pin ไปโมดูล คัดลอก name / Bundle ID / Apple ID / SKU เปิด App Store หรือ ASC
- ไอคอน: ASC build artwork → iTunes Lookup → monogram cache

### Overview และความพร้อม release

- สรุปเวอร์ชัน/build shortcuts submissions ล่าสุด
- **Soft checklist** (ขนาด screenshot หลัก copyright age rating ฯลฯ)
- **Hard blockers** ใน Versions / Submissions
- Guide: `iappmanager://release-guide`

### เวอร์ชัน builds และ submissions

- สร้างเวอร์ชัน แนบ build submit / cancel โหมด release phased **Release Now**
- **Build Upload REST** IPA/PKG Background Assets encryption declarations
- **Review Submissions** และ **Review Detail**

### Store listing และการเติบโต

- **Metadata** screenshots previews batch assets download-size workbench
- **Custom Product Pages** In-App Events App Clips store experiments featuring
- **Availability** **pricing** age rating accessibility App Tags
- **⌘S** บันทึกบน Mac

### การสร้างรายได้และ Game Center

- IAP / subscription groups offers CSV
- Guide: `iappmanager://iap-guide`
- **Game Center**

### TestFlight

- กลุ่ม ลิงก์สาธารณะ metrics feedback export
- Guide: `iappmanager://testflight-guide`

### ใบรับรอง ผู้ใช้ รายงาน รีวิว

- Certificates profiles devices users reports customer reviews webhooks
- Guide: `iappmanager://reports-guide`

### วิดเจ็ต shortcuts

- Account Hub Apps Pulse Review Desk Quick Actions
- `iappmanager://` — [Shortcut Links](url-scheme)

### ความเป็นส่วนตัว

- API secrets ใน **Keychain** เรียก **Apple** เท่านั้น
- รายละเอียด: [Privacy Policy](privacy)

## ดาวน์โหลด

| ช่องทาง | ลิงก์ |
|---------|------|
| App Store | [Download on the App Store](https://apps.apple.com/app/id6794497110) |

## ความต้องการระบบ

| ส่วน | ขั้นต่ำ |
|------|---------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |
| Widgets | iOS 17.0+ |
| IPA ใหญ่ | แนะนำ **Mac** |

## ติดต่อ

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

มักตอบภายใน 48 ชั่วโมง

[FAQ](faq) · [Shortcut Links](url-scheme) · [Privacy Policy](privacy)

</section>
<section lang="de" markdown="1">

**Schneller veröffentlichen. Raus aus dem Browser-Labyrinth.**

iAppManager (爱应用者) ist eine **native App-Store-Connect-Arbeitsstation** für iPhone, iPad und Mac. Melden Sie sich mit einem **API Key** an, speichern Sie Zugangsdaten in der **Keychain** und sprechen Sie **direkt mit Apple** — Versionen, Screenshots, IAP, TestFlight, Zertifikate, Umsatzberichte und Kundenrezensionen an einem Ort. **Kein iHTC-Studio-Konto. Keine Werbung. Kein Analytics-SDK. Kein Drittanbieter-Backend für Ihre ASC-Daten.**

**Auf einen Blick:** Multi-Account-API-Key-Login · App-Liste mit Plattform- und Pipeline-Filtern · Overview-Bereitschafts-Checkliste · Versionen & Review-Einreichungen · Build Upload REST (IPA/PKG) · Metadaten & Medien mit Cross-Locale-Kopie · Custom Product Pages · In-App Events · App Clips · Store-Experimente · Featuring-Nominierungen · Verfügbarkeit & Preise · Altersfreigabe · Barrierefreiheit · App Tags · IAP & Abos · Game Center · TestFlight · Kundenrezensionen · Zertifikate & Geräte · Benutzer & Rollen · Sales-/Finance-/Analytics-Berichte · Webhooks · Widgets & `iappmanager://`-Deep-Links · English / 简体 / 繁體

> Für Indie-Entwickler und kleine Teams, die jede Woche in App Store Connect leben — und einen Schreibtisch wollen, der sich wie eine Mac-App anfühlt, nicht wie ein Tab-Chaos.

## Erste Schritte

1. Erstellen Sie einen **App Store Connect API Key** (Admin oder App Manager empfohlen): App Store Connect → **Users and Access** → **Integrations** → **App Store Connect API** → Key anlegen, **`.p8` einmal** herunterladen, **Issuer ID** + **Key ID** notieren.
2. iAppManager öffnen → Issuer ID / Key ID / PEM einfügen (oder `.p8` wählen) → verifizieren (`GET /v1/apps`). Keys werden in der **Keychain** dieses Geräts gespeichert.
3. Kurzes **Onboarding** abschließen (Zertifikate · Berichte · Widgets · Datenschutz). Guides jederzeit unter **Einstellungen → Hilfe** wiederholen.
4. Unter **My Apps**: **Liste / Raster / Karten**, Favoriten anheften, nach **Plattform** (iOS / macOS / tvOS / visionOS) oder **Status** filtern (im Verkauf · nicht im Verkauf · wartend · in Review · abgelehnt · ausstehende Entwicklerfreigabe).
5. App öffnen → starten in **Overview** (neueste Version/Build, Shortcuts, weiche Checkliste, kürzliche Einreichungen).
6. Release-Pfad: **Versions** → **Build** anhängen → **Metadata / Media** → **Review Detail** → über **Review Submissions** einreichen (oder „sofort senden").
7. **Home-Screen-Widgets** hinzufügen (Account Hub, Apps Pulse, Review Desk, Quick Actions) und `iappmanager://` aus Kurzbefehlen testen.

> In-App-Guides **Release / IAP / TestFlight / Reports** sind einen Tipp entfernt (auch per Deep Link unten).

## Warum Sie es herunterladen sollten

- **Ein nativer Schreibtisch für den gesamten Release** — kein Hin und Her zwischen ASC-Web-Tabs für Versionen, Assets, IAP, TestFlight, Zerts und Berichte.
- **API Key, kein weiteres Passwort-Ritual** — Issuer ID + Key ID + `.p8` in der Keychain; Multi-Account; Konto entfernen löscht den lokalen Key.
- **Builds ohne Transporter hochladen** — WWDC25 **Build Upload REST** für IPA/PKG; dieselbe Pipeline auf iOS (große Dateien weiterhin am liebsten am Mac).
- **Ausführliche Guides in der App** — Release-Bereitschaft, IAP, TestFlight und Berichte erklären harte vs. weiche Checks, bevor Sie einen Review-Zyklus verbrennen.
- **Pipeline auf dem Sperrbildschirm** — Widgets spiegeln im Verkauf / wartend / in Review / abgelehnt / ausstehende Freigabe (gleiche Buckets wie My Apps).
- **Datenschutz durch Architektur** — ASC-Traffic geht an `api.appstoreconnect.apple.com`; iHTC Studio hostet Ihre Apps, Keys oder Berichte nicht.

## Funktionen

### Anmeldung & Konten

- **Nur API Key** (Issuer ID / Key ID / `.p8`) — kein Apple-ID-OAuth in der App
- Keychain-Speicher; **Multi-Account**; Abmelden / Entfernen löscht das lokale Geheimnis
- In-App-Guide **„So erhalten Sie einen API Key"** mit Abbildungen

### My Apps

- **Liste / Raster / Karten** (Standard Liste) mit Spaltensteuerung
- **Anheften** pro Konto; **Plattform-** und **Status-**Filter mit ~10‑Minuten-Katalog-Cache (Force Refresh mit Fortschritt)
- **Im Verkauf = in mindestens einem Territory verfügbar**; Pipeline-Buckets unabhängig vom Storefront
- Kontextmenü: anheften, zu Modulen springen, Name / Bundle ID / Apple ID / SKU / Store · ASC · Deep Links / Zusammenfassung kopieren; App Store oder ASC öffnen
- Icons: ASC-Build-Artwork → iTunes Lookup → Monogramm, disk-cached

### Overview & Release-Bereitschaft

- Neueste Version/Build, Modul-Shortcuts, kürzliche Review-Einreichungen
- **Weiche Checkliste** (primäre Screenshot-Größe, Copyright, Altersfreigabe u. a.)
- Versions / Submissions wenden **harte Blocker** an (Build-Status, Demo-Zugangsdaten wenn nötig)
- Guide: `iappmanager://release-guide`

### Versionen, Builds & Einreichungen

- Versionen anlegen, Builds anhängen, einreichen / abbrechen, Release-Modi (manuell / auto / geplant), gestaffeltes Release, **Release Now** bei ausstehender Entwicklerfreigabe
- **Build Upload REST** für IPA/PKG; Build-Größe; Diagnose; Beta App Clip; Export-Compliance
- **Background Assets** (`.aar`) erstellen / Chunk-Upload / External Beta & App-Store-Review-Pfade
- **Verschlüsselungserklärungen** mit Dokument-Upload; aus Overview weich geprüft
- **Review Submissions** Entwurf / Items hinzufügen / einreichen; „sofort" oder „zum Entwurf"
- **Review Detail** — Kontakt, Demo-Konto, Notizen, Anhänge, Routing App Coverage

### Store-Eintrag & Wachstum

- **Metadata** — App Info vs. Version Listing; Kategorien, Copyright, EULA, Primärlocale; Android-Mapping; Multi-Locale mit ★ Primary; **Cross-Locale-Kopie**
- **Screenshots & Previews** — nach Version / Locale / Gerätegröße; Reservierungs-Upload; Cross-Locale; Poster-Frame-Zeitcode; Abdeckung durch echte Assets
- **Batch-Assets-Workstation** — Screenshots/Previews über Locales × Größen in einem Desk
- **Download-Size-Workbench** — Build-Downloadgrößen mit weichen Limit-Hinweisen
- **SKU-Suche** in My Apps; adaptive Aktionsleisten auf schmalen Screens
- **Custom Product Pages** — Sichtbarkeit, Deep Links, Promo-Text, Search Keywords, Medien, einreichen
- **In-App Events**, **App Clips**, **Store-Experimente** (Traffic getrennt von Review), **Featuring-Nominierungen**
- **Availability**, **Pricing** (Preispunkt wählen und anwenden — inkl. Equalization-Vorschau), **Altersfreigabe**, **Barrierefreiheit**, **App Tags**
- Häufige Formulare: **⌘S** speichern am Mac

### Monetarisierung & Game Center

- IAP / Abo-Gruppen, Lokalisierungen, Review-Screenshots/Notizen, territoriale Verfügbarkeit, Preispunkte
- Intro / Promo / Win-back; **Offer Codes**; Promo-Bilder; Grace Period; Server-Notification-URLs; CSV Import/Export; einreichen (inkl. Abo-Gruppen)
- Guide: `iappmanager://iap-guide`
- **Game Center** — Achievements, Leaderboards / Sets, Challenges / Activities, Multiplayer, Matchmaking

### TestFlight

- Gruppen, öffentliche Links, Rekrutierungskriterien, Metriken, Einladungen, individuelle Tester, Builds, What to Test, Beta-Lizenz / Review
- Feedback-Posteingang und CSV + **Vollgrößen-Screenshots / Crash-Logs Bulk-Export** (Mac-Ordner / iOS-Zip + Manifest)
- Guide: `iappmanager://testflight-guide`

### Zertifikate, Benutzer, Berichte, Rezensionen

- Zertifikate (CSR in der App / Import) · Profile · Bundle IDs & Capabilities · Merchant / Pass Type · Geräte (**macOS**: Keychain-Installation)
- Benutzereinladungen, Rollen, App-Sichtbarkeit, Provisioning; Sandbox-Tester
- **Reports** — Sales / Finance / Analytics, Szenarien, Custom Presets, **breite TSV-Vorschau** (Spalten, Suche, Vollbild quer) und **leichte Summary-Charts**; `iappmanager://reports-guide`
- Kundenrezensionen — Filter, Suche, antworten / löschen, **Antwort-Vorlagen** (max. 20 pro Konto)
- **Webhooks** — anlegen / bearbeiten / ping / Zustellung (wir hosten keine öffentlichen Callbacks)

### Widgets, Shortcuts, Feinschliff

- Widgets: **Account Hub**, **Apps Pulse** (S/M/L), **Review Desk**, **Quick Actions**
- `iappmanager://` + App Intents — [Shortcut Links](url-scheme)
- Erscheinungsbild, Akzent, EN / 简 / 繁 (Hot-Swap ohne Navigationsverlust)
- iOS **Alternative App-Icons** (IconStyle1–7); StoreKit-Trinkgeld; Feedback-E-Mail

### Datenschutz

- API-Geheimnisse in der **Geräte-Keychain**; Business-API nur an **Apple**
- Optionale Icons via iTunes Lookup; Thumbnail-Cache in Einstellungen löschen
- App Group nur **lokale** Widget-Snapshots — kein Upload an iHTC Studio
- Details: [Privacy Policy](privacy)

## App beziehen

| Kanal | Link |
|-------|------|
| App Store | [Download on the App Store](https://apps.apple.com/app/id6794497110) |

## Systemanforderungen

| Komponente | Minimum |
|------------|---------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |
| Widgets | iOS 17.0+ |
| Große IPAs | **Mac** empfohlen |

## Kontakt

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Wir antworten in der Regel innerhalb von 48 Stunden.

[FAQ](faq) · [Shortcut Links](url-scheme) · [Privacy Policy](privacy)

</section>
<section lang="fr" markdown="1">

**Publiez plus vite. Quittez le labyrinthe du navigateur.**

iAppManager (爱应用者) est un **poste de travail natif App Store Connect** pour iPhone, iPad et Mac. Connectez-vous avec une **clé API**, conservez les identifiants dans le **Trousseau**, et communiquez **directement avec Apple** — versions, captures, IAP, TestFlight, certificats, rapports de ventes et avis clients au même endroit. **Pas de compte iHTC Studio. Pas de pub. Pas de SDK analytics. Pas de backend tiers pour vos données ASC.**

**En bref :** connexion multi-comptes par clé API · liste d'apps avec filtres plateforme et pipeline · checklist de préparation Overview · versions et soumissions review · Build Upload REST (IPA/PKG) · métadonnées et médias avec copie inter-locales · Custom Product Pages · In-App Events · App Clips · expériences store · nominations featuring · disponibilité et prix · classification · accessibilité · App Tags · IAP et abonnements · Game Center · TestFlight · avis clients · certificats et appareils · utilisateurs et rôles · rapports sales / finance / Analytics · Webhooks · widgets et deep links `iappmanager://` · English / 简体 / 繁體

> Conçu pour les indés et petites équipes qui vivent dans App Store Connect chaque semaine — un bureau qui ressemble à une app Mac, pas à une ferme d'onglets.

## Premiers pas

1. Créez une **clé API App Store Connect** (Admin ou App Manager recommandé) : App Store Connect → **Users and Access** → **Integrations** → **App Store Connect API** → créez une clé, téléchargez le **`.p8` une seule fois**, notez **Issuer ID** + **Key ID**.
2. Ouvrez iAppManager → collez Issuer ID / Key ID / PEM (ou choisissez le `.p8`) → vérifiez (`GET /v1/apps`). Les clés sont stockées dans le **Trousseau** de cet appareil.
3. Terminez l'**onboarding** court (certificats · rapports · widgets · confidentialité). Relisez les guides dans **Réglages → Aide**.
4. Dans **My Apps**, choisissez **liste / grille / cartes**, épinglez les favoris, filtrez par **plateforme** (iOS / macOS / tvOS / visionOS) ou **statut** (en vente · hors vente · en attente · en review · refusé · release développeur en attente).
5. Ouvrez une app → commencez par **Overview** (dernière version/build, raccourcis, checklist souple, soumissions récentes).
6. Parcours release : **Versions** → attacher un **Build** → **Metadata / Media** → **Review Detail** → soumettre via **Review Submissions** (ou « envoyer maintenant »).
7. Ajoutez des **widgets d'écran d'accueil** (Account Hub, Apps Pulse, Review Desk, Quick Actions) et testez `iappmanager://` depuis Raccourcis.

> Les guides **Release / IAP / TestFlight / Reports** intégrés sont à un tap (aussi via deep links).

## Pourquoi télécharger

- **Un bureau natif pour toute la publication** — fini les allers-retours entre onglets ASC pour versions, assets, IAP, TestFlight, certs et rapports.
- **Clé API, pas une danse de mots de passe** — Issuer ID + Key ID + `.p8` dans le Trousseau ; multi-comptes ; retirer un compte supprime la clé locale.
- **Envoyer des builds sans Transporter** — **Build Upload REST** WWDC25 pour IPA/PKG ; même pipeline sur iOS (gros fichiers de préférence sur Mac).
- **Guides détaillés dans l'app** — préparation release, IAP, TestFlight et rapports expliquent checks durs vs souples avant de brûler un cycle review.
- **Pipeline sur l'écran verrouillé** — les widgets reflètent en vente / attente / review / refusé / release en attente (mêmes seaux que My Apps).
- **Confidentialité par architecture** — le trafic ASC va vers `api.appstoreconnect.apple.com` ; iHTC Studio n'héberge pas vos apps, clés ou rapports.

## Fonctionnalités

### Connexion et comptes

- **Clé API uniquement** (Issuer ID / Key ID / `.p8`) — pas d'OAuth Apple ID dans l'app
- Stockage Trousseau ; **multi-comptes** ; déconnexion / suppression efface le secret local
- Guide illustré **« Obtenir une clé API »** dans l'app

### My Apps

- **Liste / grille / cartes** (liste par défaut) avec contrôle des colonnes
- **Épinglage** par compte ; filtres **plateforme** et **statut** avec cache catalogue ~10 min (rafraîchissement forcé avec progression)
- **En vente = disponible dans au moins un territoire** ; seaux pipeline indépendants de la présence storefront
- Menu contextuel : épingler, sauter aux modules, copier nom / Bundle ID / Apple ID / SKU / store · ASC · deep links / résumé ; ouvrir App Store ou ASC
- Icônes : artwork build ASC → iTunes Lookup → monogramme, cache disque

### Overview et préparation release

- Résumé dernière version/build, raccourcis modules, soumissions review récentes
- **Checklist souple** (taille capture principale, copyright, classification, etc.)
- Versions / Submissions appliquent des **bloqueurs durs** (état build, identifiants démo si requis)
- Guide : `iappmanager://release-guide`

### Versions, builds et soumissions

- Créer versions, attacher builds, soumettre / annuler, modes release (manuel / auto / planifié), release progressive, **Release Now** en attente développeur
- **Build Upload REST** IPA/PKG ; taille build ; diagnostics ; Beta App Clip ; conformité export
- **Background Assets** (`.aar`) créer / upload par morceaux / chemins External Beta et review App Store
- **Déclarations chiffrement** avec upload document ; vérification souple depuis Overview
- **Review Submissions** brouillon / ajouter items / soumettre ; « maintenant » ou « ajouter au brouillon »
- **Review Detail** — contact, compte démo, notes, pièces jointes, Routing App Coverage

### Fiche store et croissance

- **Metadata** — App Info vs Version Listing ; catégories, copyright, EULA, locale primaire ; mapping Android ; multi-locale avec ★ primaire ; **copie inter-locales**
- **Captures et previews** — par version / locale / taille appareil ; upload réservation ; copie inter-locales ; timecode poster ; couverture par assets réels
- **Poste batch assets** — upload captures/previews sur locales × tailles en un desk
- **Workbench taille de téléchargement** — inspecter tailles avec hints limites souples
- **Recherche SKU** dans My Apps ; barres d'action adaptatives sur écrans étroits
- **Custom Product Pages** — visibilité, deep links, promo, Search Keywords, médias, soumettre
- **In-App Events**, **App Clips**, **expériences store** (trafic séparé du review), **nominations featuring**
- **Disponibilité**, **prix** (choisir un price point puis appliquer — preview equalization incluse), **classification**, **accessibilité**, **App Tags**
- Formulaires fréquents : **⌘S** enregistrer sur Mac

### Monétisation et Game Center

- IAP / groupes d'abonnement, localisations, captures/notes review, disponibilité territoriale, price points
- Offres intro / promo / win-back ; **Offer Codes** ; images promo ; grace period ; URLs notifications serveur ; import/export CSV ; soumettre (y compris groupes abo)
- Guide : `iappmanager://iap-guide`
- **Game Center** — succès, leaderboards / sets, défis / activités, multijoueur, matchmaking

### TestFlight

- Groupes, liens publics, critères recrutement, métriques, invitations, testeurs individuels, builds, What to Test, licence bêta / review
- Boîte feedback et CSV + **export bulk captures pleine taille / crash logs** (dossier Mac / zip iOS + manifest)
- Guide : `iappmanager://testflight-guide`

### Certificats, utilisateurs, rapports, avis

- Certificats (CSR in-app / import) · profils · Bundle ID et capabilities · Merchant / Pass Type · appareils (**macOS** : installation Keychain)
- Invitations utilisateurs, rôles, visibilité app, provisioning ; testeurs Sandbox
- **Reports** — sales / finance / Analytics, scénarios, presets custom, **aperçu TSV large** (colonnes, recherche, plein écran paysage) et **graphiques résumé légers** ; `iappmanager://reports-guide`
- Avis clients — filtres, recherche, répondre / supprimer, **modèles de réponse** (max 20 par compte)
- **Webhooks** — créer / modifier / ping / livraison (nous n'hébergeons pas de callbacks publics)

### Widgets, raccourcis, finitions

- Widgets : **Account Hub**, **Apps Pulse** (S/M/L), **Review Desk**, **Quick Actions**
- `iappmanager://` + App Intents — [Shortcut Links](url-scheme)
- Apparence, accent, EN / 简 / 繁 (changement à chaud sans perdre la nav)
- **Icônes alternatives** iOS (IconStyle1–7) ; pourboire StoreKit ; e-mail feedback

### Confidentialité

- Secrets API dans le **Trousseau** de l'appareil ; API métier uniquement vers **Apple**
- Icônes optionnelles via iTunes Lookup ; vider le cache miniatures dans Réglages
- App Group pour snapshots **locaux** widgets uniquement — pas d'upload iHTC Studio
- Détails : [Privacy Policy](privacy)

## Obtenir l'app

| Canal | Lien |
|-------|------|
| App Store | [Download on the App Store](https://apps.apple.com/app/id6794497110) |

## Configuration requise

| Composant | Minimum |
|-----------|---------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |
| Widgets | iOS 17.0+ |
| Grosses IPAs | **Mac** recommandé |

## Contact

- **E-mail :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Réponse habituelle sous 48 heures.

[FAQ](faq) · [Shortcut Links](url-scheme) · [Privacy Policy](privacy)

</section>
<section lang="tr" markdown="1">

**Daha hızlı yayınlayın. Tarayıcı labirentinden çıkın.**

iAppManager (爱应用者), iPhone, iPad ve Mac için **yerel bir App Store Connect istasyonudur**. **API Key** ile oturum açın, kimlik bilgilerini **Keychain**'de tutun ve **doğrudan Apple** ile konuşun — sürümler, ekran görüntüleri, IAP, TestFlight, sertifikalar, satış raporları ve müşteri yorumları tek yerde. **iHTC Studio hesabı yok. Reklam yok. Analytics SDK yok. ASC verileriniz için üçüncü taraf backend yok.**

**Özet:** çoklu hesap API Key · platform ve pipeline filtreli uygulama listesi · Overview hazırlık kontrol listesi · sürümler ve review gönderimleri · Build Upload REST (IPA/PKG) · cross-locale kopyalı metadata ve medya · Custom Product Pages · In-App Events · App Clips · store deneyleri · featuring adaylıkları · availability ve fiyatlandırma · yaş derecelendirmesi · erişilebilirlik · App Tags · IAP ve abonelikler · Game Center · TestFlight · müşteri yorumları · sertifikalar ve cihazlar · kullanıcılar ve roller · sales / finance / Analytics raporları · Webhooks · widget'lar ve `iappmanager://` deep link'leri · English / 简体 / 繁體

> Her hafta App Store Connect'te yaşayan indie geliştiriciler ve küçük ekipler için — sekme çiftliği değil, Mac uygulaması gibi bir masa.

## Başlarken

1. **App Store Connect API Key** oluşturun (Admin veya App Manager önerilir): App Store Connect → **Users and Access** → **Integrations** → **App Store Connect API** → anahtar oluşturun, **`.p8`'i bir kez** indirin, **Issuer ID** + **Key ID** not edin.
2. iAppManager'ı açın → Issuer ID / Key ID / PEM yapıştırın (veya `.p8` seçin) → doğrulayın (`GET /v1/apps`). Anahtarlar bu cihazın **Keychain**'inde saklanır.
3. Kısa **onboarding**'i bitirin (sertifikalar · raporlar · widget'lar · gizlilik). **Ayarlar → Yardım**'dan rehberleri tekrarlayın.
4. **My Apps**'te **liste / ızgara / kartlar**, favorileri sabitleyin, **platform** (iOS / macOS / tvOS / visionOS) veya **durum** (satışta · satış dışı · bekliyor · incelemede · reddedildi · geliştirici release bekliyor) filtreleyin.
5. Uygulamayı açın → **Overview**'dan başlayın (son sürüm/build, kısayollar, yumuşak kontrol listesi, son gönderimler).
6. Release yolu: **Versions** → **Build** ekle → **Metadata / Media** → **Review Detail** → **Review Submissions** ile gönderin (veya "hemen gönder").
7. **Ana Ekran widget'ları** ekleyin (Account Hub, Apps Pulse, Review Desk, Quick Actions) ve Shortcuts'tan `iappmanager://` deneyin.

> Uygulama içi **Release / IAP / TestFlight / Reports** rehberleri bir dokunuşta (deep link'ler de).

## Neden indirmelisiniz

- **Tüm yayın için tek yerel masa** — sürümler, varlıklar, IAP, TestFlight, sertifikalar ve raporlar için ASC web sekmeleri arasında zıplamayı bırakın.
- **API Key, başka bir parola dansı değil** — Issuer ID + Key ID + `.p8` Keychain'de; çoklu hesap; hesap kaldırma yerel anahtarı siler.
- **Transporter olmadan build yükleme** — WWDC25 **Build Upload REST** IPA/PKG için; iOS'ta aynı pipeline (büyük dosyalar Mac'te).
- **Uygulama içi ayrıntılı rehberler** — release hazırlığı, IAP, TestFlight ve raporlar hard vs soft kontrolleri açıklar.
- **Kilit Ekranı'nda pipeline** — widget'lar satışta / bekliyor / incelemede / reddedildi / release bekliyor sayılarını yansıtır.
- **Mimariyle gizlilik** — ASC trafiği `api.appstoreconnect.apple.com`; iHTC Studio uygulamalarınızı, anahtarlarınızı veya raporlarınızı barındırmaz.

## Özellikler

### Oturum ve hesaplar

- **Yalnızca API Key** (Issuer ID / Key ID / `.p8`) — uygulama içi Apple ID OAuth yok
- Keychain; **çoklu hesap**; çıkış / kaldırma yerel gizli anahtarı siler
- Uygulama içi **"API Key nasıl alınır"** rehberi

### My Apps

- **Liste / ızgara / kartlar** (varsayılan liste) sütun kontrolleri
- Hesap başına **sabitleme**; **platform** ve **durum** filtreleri ~10 dk önbellek
- **Satışta = en az bir bölgede kullanılabilir**
- Bağlam menüsü: sabitle, modüllere atla, kopyala; App Store veya ASC aç
- İkonlar: ASC build artwork → iTunes Lookup → monogram

### Overview ve release hazırlığı

- Son sürüm/build özeti, modül kısayolları, son review gönderimleri
- **Yumuşak kontrol listesi**
- **Sert blockers** Versions / Submissions'ta
- Rehber: `iappmanager://release-guide`

### Sürümler, build'ler ve gönderimler

- Sürüm oluşturma, build ekleme, gönder / iptal, release modları, **Release Now**
- **Build Upload REST**, Background Assets, encryption declarations
- **Review Submissions** ve **Review Detail**

### Store listesi ve büyüme

- **Metadata**, screenshots, batch assets, download-size workbench
- **Custom Product Pages**, In-App Events, App Clips, store experiments, featuring
- **Availability**, **pricing**, age rating, accessibility, App Tags
- Mac'te **⌘S** kaydet

### Monetizasyon ve Game Center

- IAP / abonelik grupları, teklifler, CSV
- Rehber: `iappmanager://iap-guide`
- **Game Center**

### TestFlight

- Gruplar, public link'ler, metrikler, feedback export
- Rehber: `iappmanager://testflight-guide`

### Sertifikalar, kullanıcılar, raporlar, yorumlar

- Certificates, profiles, devices, reports, customer reviews, webhooks
- Rehber: `iappmanager://reports-guide`

### Widget'lar ve kısayollar

- Account Hub, Apps Pulse, Review Desk, Quick Actions
- `iappmanager://` — [Shortcut Links](url-scheme)

### Gizlilik

- API sırları **Keychain**'de; yalnızca **Apple**'a çağrılar
- Ayrıntılar: [Privacy Policy](privacy)

## Uygulamayı edinin

| Kanal | Bağlantı |
|-------|----------|
| App Store | [Download on the App Store](https://apps.apple.com/app/id6794497110) |

## Sistem gereksinimleri

| Bileşen | Minimum |
|---------|---------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |
| Widget'lar | iOS 17.0+ |
| Büyük IPA | **Mac** önerilir |

## İletişim

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Genelde 48 saat içinde yanıt veririz.

[FAQ](faq) · [Shortcut Links](url-scheme) · [Privacy Policy](privacy)

</section>
