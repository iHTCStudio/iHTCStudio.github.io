---
layout: doc
title: iAppManager — Privacy Policy
app_id: iAppManager
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iAppManager (爱应用者) — API Key in Keychain; ASC traffic to Apple only; no analytics SDK.
---

<section lang="en" markdown="1">

iHTC Studio (formerly iHTCTeam) built iAppManager (爱应用者 / 愛應用者).

## Summary

**iHTC Studio does not operate a backend for your App Store Connect data.** You sign in with an **API Key** stored in **device Keychain**. Business requests go **directly to Apple** (`api.appstoreconnect.apple.com`). **No iHTC Studio account. No ads. No analytics / crash SDK.** Optional StoreKit tip purchases are processed by **Apple**.

## Data Stored on Your Device

| Data | Purpose |
|------|---------|
| API Key accounts (Issuer ID, Key ID, `.p8` PEM) | Authenticate to App Store Connect API — Keychain |
| Account index / current account / preferences | Multi-account switch, appearance, language, accent |
| Remote image cache | App icons & media thumbnails (clearable in Settings) |
| Review reply templates, report presets / stars | Local productivity helpers per account |
| App Group widget snapshot | Pipeline counts, theme/language for widgets — **on device only** |

## Network

| Destination | Why |
|-------------|-----|
| `api.appstoreconnect.apple.com` | All ASC management (JWT signed on device) |
| Apple iTunes Lookup (multi-region) | Optional App icon enrichment |
| Apple CDN / pre-signed upload URLs | Screenshots, previews, IPA/PKG chunk uploads (no Bearer on PUT) |
| `apps.apple.com` / App Store | Open product pages (system / external) |
| Mail client | Feedback you choose to send |

iHTC Studio does **not** receive your API private key, app metadata, IPA contents, sales reports or customer reviews.

## Permissions & platform notes

| Capability | When | Why |
|------------|------|-----|
| Outgoing network | Always while using ASC features | Talk to Apple APIs |
| User-selected files | Upload IPA/screenshots, export reports | You pick the files |
| Keychain | Save / remove API keys | Secure local storage |
| App Group | Widgets | Share local summaries only |
| Photos / share sheet (as offered by OS) | Export / save when you act | User-initiated |

Certificate **install into system Keychain** is intended for **macOS**. iOS focuses on list / download / share.

## What we do not do

- No iHTC Studio cloud account for ASC data
- No advertising or third-party trackers
- No sale of personal data
- Widgets never call ASC by themselves

## Contact

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>

<section lang="zh-CN" markdown="1">

爱火腿肠工作室（iHTC Studio；原 iHTCTeam）开发了爱应用者。

## 摘要

**iHTC Studio 不为你的 App Store Connect 数据运营后端。** 你使用 **API Key** 登录，密钥保存在本机 **钥匙串**。业务请求 **直连 Apple**（`api.appstoreconnect.apple.com`）。**无 iHTC Studio 账号。无广告。无分析 / 崩溃 SDK。** 可选 StoreKit 赞赏由 **Apple** 处理。

## 设备本地存储

| 数据 | 用途 |
|------|------|
| API Key 账号（Issuer ID、密钥 ID、`.p8` PEM） | 鉴权 App Store Connect API — 钥匙串 |
| 账号索引 / 当前账号 / 偏好 | 多账号、外观、语言、强调色 |
| 远程图片缓存 | App 图标与素材缩略图（设置可清空） |
| 评价回复模板、报表预设 / 星标 | 按账号的本机效率工具 |
| App Group 小组件快照 | 流水线计数、主题/语言 — **仅本机** |

## 网络

| 目标 | 原因 |
|------|------|
| `api.appstoreconnect.apple.com` | 全部 ASC 管理（JWT 在本机签名） |
| Apple iTunes Lookup（多区） | 可选补全 App 图标 |
| Apple CDN / 预签名上传 URL | 截图、预览、IPA/PKG 分片上传（PUT 不带 Bearer） |
| `apps.apple.com` / App Store | 打开产品页（系统 / 外开） |
| 邮件客户端 | 你主动发送的反馈 |

iHTC Studio **不会**收到你的 API 私钥、App 元数据、IPA 内容、销售报表或顾客评价。

## 权限与平台说明

| 能力 | 时机 | 原因 |
|------|------|------|
| 出站网络 | 使用 ASC 功能时 | 连接 Apple API |
| 用户所选文件 | 上传 IPA/截图、导出报表 | 由你选择文件 |
| 钥匙串 | 保存 / 移除 API Key | 安全本地存储 |
| App Group | 小组件 | 仅共享本机摘要 |
| 照片 / 分享表（系统提供时） | 你主动导出 / 保存 | 用户发起 |

证书 **安装到系统钥匙串** 面向 **macOS**。iOS 以列表 / 下载 / 分享为主。

## 我们不会做的事

- 不为 ASC 数据提供 iHTC Studio 云账号
- 无广告或第三方追踪
- 不出售个人数据
- 小组件不会自行请求 ASC

## 联系

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>

<section lang="zh-TW" markdown="1">

愛火腿腸工作室（iHTC Studio；原 iHTCTeam）開發了愛應用者。

## 摘要

**iHTC Studio 不為你的 App Store Connect 資料營運後端。** 你使用 **API Key** 登入，金鑰保存在本機 **鑰匙圈**。業務請求 **直連 Apple**（`api.appstoreconnect.apple.com`）。**無 iHTC Studio 帳號。無廣告。無分析 / 當機 SDK。** 可選 StoreKit 打賞由 **Apple** 處理。

## 裝置本機儲存

| 資料 | 用途 |
|------|------|
| API Key 帳號（Issuer ID、金鑰 ID、`.p8` PEM） | 鑑權 App Store Connect API — 鑰匙圈 |
| 帳號索引 / 目前帳號 / 偏好 | 多帳號、外觀、語言、強調色 |
| 遠端圖片快取 | App 圖示與素材縮圖（設定可清空） |
| 評價回覆範本、報表預設 / 星標 | 按帳號的本機效率工具 |
| App Group 小工具快照 | 流水線計數、主題/語言 — **僅本機** |

## 網路

| 目標 | 原因 |
|------|------|
| `api.appstoreconnect.apple.com` | 全部 ASC 管理（JWT 在本機簽名） |
| Apple iTunes Lookup（多區） | 可選補全 App 圖示 |
| Apple CDN / 預簽名上傳 URL | 截圖、預覽、IPA/PKG 分片上傳（PUT 不帶 Bearer） |
| `apps.apple.com` / App Store | 打開產品頁（系統 / 外開） |
| 郵件用戶端 | 你主動傳送的回饋 |

iHTC Studio **不會**收到你的 API 私鑰、App 中繼資料、IPA 內容、銷售報表或顧客評價。

## 權限與平台說明

| 能力 | 時機 | 原因 |
|------|------|------|
| 出站網路 | 使用 ASC 功能時 | 連線 Apple API |
| 使用者所選檔案 | 上傳 IPA/截圖、匯出報表 | 由你選擇檔案 |
| 鑰匙圈 | 儲存 / 移除 API Key | 安全本機儲存 |
| App Group | 小工具 | 僅共享本機摘要 |
| 照片 / 分享表（系統提供時） | 你主動匯出 / 儲存 | 使用者發起 |

憑證 **安裝到系統鑰匙圈** 面向 **macOS**。iOS 以列表 / 下載 / 分享為主。

## 我們不會做的事

- 不為 ASC 資料提供 iHTC Studio 雲帳號
- 無廣告或第三方追蹤
- 不出售個人資料
- 小工具不會自行請求 ASC

## 聯絡

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
