---
layout: doc
title: iAppManager — FAQ
app_id: iAppManager
doc_title_en: Frequently Asked Questions
doc_title_zh_cn: 常见问题
doc_title_zh_tw: 常見問題
description: FAQ for iAppManager — API Key login, ASC features, IPA upload, TestFlight, widgets, and privacy.
---

<section lang="en" markdown="1">

### What is iAppManager?

A **native App Store Connect workstation** for iPhone, iPad and Mac. Sign in with an **API Key**, manage versions, screenshots, IAP, TestFlight, certificates, reports and reviews — traffic goes **straight to Apple**. No iHTC Studio account.

### How do I get an API Key?

1. Open [App Store Connect](https://appstoreconnect.apple.com) → **Users and Access** → **Integrations** → **App Store Connect API**
2. Create a key (Admin or App Manager recommended)
3. Download the `.p8` **once**, note **Issuer ID** and **Key ID**
4. Paste them in iAppManager (or pick the file). The in-app guide walks you through screenshots.

### Is my `.p8` uploaded to iHTC Studio?

**No.** The private key stays in **device Keychain**. Requests are signed locally and sent to `api.appstoreconnect.apple.com`. Removing an account deletes the local key.

### Do I need an Apple ID password inside the app?

**No.** Authentication is **API Key only** (Issuer ID + Key ID + `.p8`). You still use your Apple ID in Safari/ASC when a feature has no public API (e.g. privacy nutrition labels, free-app promo codes) — the app opens Apple’s site for those cases.

### Can I upload IPA / PKG without Transporter?

**Yes.** iAppManager uses Apple’s **Build Upload REST** (WWDC25). Prefer **Mac** for large files; iOS supports the same API but is less comfortable for big uploads.

### What does “on sale” mean in filters / widgets?

**Available in at least one App Store territory.** Pipeline buckets (waiting / in review / rejected / pending developer release) are tracked separately. Widget **Needs attention** = waiting + in review + rejected + pending release (local sum, not an ASC field).

### Hard vs soft checks before submit?

**Hard blockers** stop submit (e.g. build not ready, demo account required but missing). **Soft checks** warn (primary screenshot size, copyright, age rating, etc.) and you can confirm to continue. See Overview / Versions / Submissions `?` or `iappmanager://release-guide`.

### Which languages are supported?

**English · 简体中文 · 繁體中文**, follow system or force in Settings. Language hot-swap refreshes copy **without** remounting the root (navigation and drafts stay).

### Widgets don’t show live ASC numbers?

Widgets **do not call ASC**. The main app scans and writes a snapshot (~10‑minute TTL, same buckets as My Apps). Open the app and refresh the list (or force status refresh) to update.

### macOS vs iOS differences?

Both cover store, monetization, TestFlight, Game Center, users, reports, reviews and Webhooks. **Prefer Mac** for large IPA uploads and installing certificates into the system Keychain. Alternate app icons are **iOS only**.

### Where is the privacy policy URL for App Store Connect?

Open this site’s [Privacy Policy](privacy) page and copy the URL from your browser’s address bar.

### System requirements?

iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+**.

### How do I contact support?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — typically within 48 hours.

</section>

<section lang="zh-CN" markdown="1">

### 爱应用者是什么？

面向 iPhone、iPad 与 Mac 的 **原生 App Store Connect 工作台**。用 **API Key** 登录，管理版本、截图、内购、TestFlight、证书、报表与评价——流量 **直连 Apple**。无需 iHTC Studio 账号。

### 如何获取 API Key？

1. 打开 [App Store Connect](https://appstoreconnect.apple.com) → **用户和访问** → **集成** → **App Store Connect API**
2. 创建密钥（建议 Admin 或 App Manager）
3. **仅一次**下载 `.p8`，记下 **Issuer ID** 与 **密钥 ID**
4. 在爱应用者粘贴（或选择文件）。应用内图文引导逐步说明。

### 我的 `.p8` 会上传到 iHTC Studio 吗？

**不会。** 私钥只存本机 **钥匙串**。请求在本地签名后发往 `api.appstoreconnect.apple.com`。移除账号会删除本机密钥。

### 应用内需要输入 Apple ID 密码吗？

**不需要。** 鉴权 **仅 API Key**（Issuer ID + 密钥 ID + `.p8`）。若某功能暂无公开 API（如隐私营养标签、免费 App 推广码），应用会打开 Apple 网页，由你在 Safari/ASC 侧使用 Apple ID。

### 不用 Transporter 能上传 IPA / PKG 吗？

**可以。** 爱应用者使用 Apple **Build Upload REST**（WWDC25）。大文件建议用 **Mac**；iOS 支持同 API，但大文件体验较弱。

### 筛选 / 小组件里的「已上架」是什么意思？

**至少一地区可用。** 流水线分桶（送审中 / 审核中 / 被拒 / 待开发者发布）单独统计。小组件 **需关注** = 送审中 + 审核中 + 被拒 + 待发布（本地合计，非 ASC 字段）。

### 提审前的硬拦截与软检查？

**硬拦截**会阻止送审（如构建未就绪、需要演示账号却缺失）。**软检查**会提示（主尺寸截图、版权、年龄分级等），可确认后继续。见 Overview / 版本 / 审核提交的 `?`，或 `iappmanager://release-guide`。

### 支持哪些语言？

**English · 简体中文 · 繁體中文**，可跟随系统或在设置强制。热切换文案时 **不会** 重挂根视图（导航与草稿保留）。

### 小组件为什么不是实时 ASC 数字？

小组件 **不直连 ASC**。由主应用扫描后写入快照（约 10 分钟 TTL，与「我的 App」同口径）。打开应用并刷新列表（或强制重扫状态）即可更新。

### macOS 与 iOS 有何差异？

两端均覆盖商店、变现、TestFlight、Game Center、用户、报表、评价与 Webhooks。**大体积 IPA** 与把证书装进系统钥匙串建议用 **Mac**。备用图标仅 **iOS**。

### App Store Connect 隐私政策网址？

打开本站的 [隐私政策](privacy) 页面，从浏览器地址栏复制当前网址即可。

### 系统要求？

iPhone / iPad **iOS 17.0+**，Mac **macOS 14.0+**。

### 如何联系支持？

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)——通常 48 小时内回复。

</section>

<section lang="zh-TW" markdown="1">

### 愛應用者是什麼？

面向 iPhone、iPad 與 Mac 的 **原生 App Store Connect 工作台**。用 **API Key** 登入，管理版本、截圖、內購、TestFlight、憑證、報表與評價——流量 **直連 Apple**。無需 iHTC Studio 帳號。

### 如何取得 API Key？

1. 打開 [App Store Connect](https://appstoreconnect.apple.com) → **使用者和存取權限** → **整合** → **App Store Connect API**
2. 建立金鑰（建議 Admin 或 App Manager）
3. **僅一次**下載 `.p8`，記下 **Issuer ID** 與 **金鑰 ID**
4. 在愛應用者貼上（或選擇檔案）。應用內圖文引導逐步說明。

### 我的 `.p8` 會上傳到 iHTC Studio 嗎？

**不會。** 私鑰只存本機 **鑰匙圈**。請求在本地簽名後送往 `api.appstoreconnect.apple.com`。移除帳號會刪除本機金鑰。

### 應用內需要輸入 Apple ID 密碼嗎？

**不需要。** 鑑權 **僅 API Key**（Issuer ID + 金鑰 ID + `.p8`）。若某功能暫無公開 API（如隱私營養標籤、免費 App 推廣碼），應用會打開 Apple 網頁，由你在 Safari/ASC 側使用 Apple ID。

### 不用 Transporter 能上傳 IPA / PKG 嗎？

**可以。** 愛應用者使用 Apple **Build Upload REST**（WWDC25）。大檔建議用 **Mac**；iOS 支援同 API，但大檔體驗較弱。

### 篩選 / 小工具裡的「已上架」是什麼意思？

**至少一地區可用。** 流水線分桶（送審中 / 審核中 / 被拒 / 待開發者發佈）單獨統計。小工具 **需關注** = 送審中 + 審核中 + 被拒 + 待發佈（本地合計，非 ASC 欄位）。

### 送審前的硬攔截與軟檢查？

**硬攔截**會阻止送審（如建置未就緒、需要示範帳號卻缺失）。**軟檢查**會提示（主尺寸截圖、版權、年齡分級等），可確認後繼續。見 Overview / 版本 / 審核提交的 `?`，或 `iappmanager://release-guide`。

### 支援哪些語言？

**English · 簡體中文 · 繁體中文**，可跟隨系統或在設定強制。熱切換文案時 **不會** 重掛根檢視（導覽與草稿保留）。

### 小工具為什麼不是即時 ASC 數字？

小工具 **不直連 ASC**。由主應用掃描後寫入快照（約 10 分鐘 TTL，與「我的 App」同口徑）。打開應用並重新整理列表（或強制重掃狀態）即可更新。

### macOS 與 iOS 有何差異？

兩端均涵蓋商店、變現、TestFlight、Game Center、使用者、報表、評價與 Webhooks。**大體積 IPA** 與把憑證裝進系統鑰匙圈建議用 **Mac**。備用圖示僅 **iOS**。

### App Store Connect 隱私權政策網址？

打開本站的 [隱私權政策](privacy) 頁面，從瀏覽器網址列複製目前網址即可。

### 系統需求？

iPhone / iPad **iOS 17.0+**，Mac **macOS 14.0+**。

### 如何聯絡支援？

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)——通常 48 小時內回覆。

</section>
