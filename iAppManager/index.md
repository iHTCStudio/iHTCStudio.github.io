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
- **Reports** — sales / finance / Analytics with scenario shortcuts, custom presets, TSV preview & summaries; guide `iappmanager://reports-guide`
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
- **报表** — 销售 / 财务 / Analytics，场景快捷与自定义预设，TSV 预览与摘要；指南 `iappmanager://reports-guide`
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
- **報表** — 銷售 / 財務 / Analytics，場景快捷與自訂預設，TSV 預覽與摘要；指南 `iappmanager://reports-guide`
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
