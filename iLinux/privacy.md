---
layout: doc
title: iLinux — Privacy Policy
app_id: iLinux
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iLinux.
---

<section lang="en" markdown="1">

iHTC Studio ("we", "us" or "our"; formerly iHTCTeam) built iLinux (also known as "爱 Linux"). This page informs you of our policies regarding the collection, use and disclosure of personal data when you use our app.

## Summary

**iLinux does not collect analytics or sell personal data.** Command libraries run fully offline on your device. Optional **iCloud sync** (when enabled and signed into iCloud) stores favourites, quiz progress, theme and display preferences in **your** iCloud Key-Value Storage under your Apple ID — iHTC Studio does not operate a backend server for this data.

## Data Collection

We do not operate analytics, advertising or tracking. Specifically:

- **No personal information** is collected by iHTC Studio (no name, email, phone number or iHTC Studio account).
- **No usage analytics** or crash-reporting SDKs are integrated.
- **Your learning data** (favourites, quiz scores, wrong answers) stays on your devices and, if you enable sync, in **Apple iCloud** — not on iHTC Studio servers.
- **No cookies or third-party trackers** in the app.

## How the App Works

iLinux stores all user-generated data — favourites, recent views, quiz session results, wrong answer records, shell platform preference, favourites scope, widget command library and app preferences — locally on your device:

- All command data (JSON summaries and Markdown documentation for **Linux, CMD and PowerShell**) is bundled inside the app and never fetched from any external server.
- No internet connection is required to browse commands or take quizzes.
- Optional **iCloud sync** uses Apple's **NSUbiquitousKeyValueStore** when you are signed into iCloud and leave sync enabled. You can turn it off per device in Settings.
- Opening external links from within the app (e.g., tapping a URL in the Feedback section) uses standard iOS networking behaviour; the linked page is loaded by your device directly from its host, not through any iHTC Studio server.
- The optional **App Store version check** (`AppStoreVersionChecker`) makes a single read-only request to the public iTunes Lookup API to compare the installed version with the latest release. No personal data is sent in this request.

## Permissions

iLinux requests **Photo Library** access only when you choose to **save a share card or command screenshot** to Photos. No camera, microphone, location or contacts access is required.

## Data Storage

| Data | Storage Location |
|------|-----------------|
| Favourites, recent views, wrong answer records, learning status (per platform) | Local UserDefaults / App Group on your device |
| Quiz progress and daily session results (keyed by date and shell platform) | Local app sandbox on your device |
| Theme, language, list/grid layout, shell platform, favourites scope, widget library | Local UserDefaults / App Group on your device |
| iCloud sync mirror (optional) | Apple iCloud Key-Value Storage (`crossSync.*` keys) — favourites, quiz progress, theme, app preferences |
| Widget snapshot (iOS/iPad only) | App Group container (`group.com.iHTCboy.iLinuxs`) |

No data is stored on any iHTC Studio-operated server. Optional iCloud data is governed by Apple's iCloud terms.

## iCloud Sync (Optional)

When **iCloud Sync** is enabled and you are signed into iCloud:

- Data synced: **learning progress** (favourites, recents, learning status, quiz scores, wrong-answer records), **theme**, and **app preferences** (language, shell platform, favourites scope, list/grid settings).
- Storage: Apple **iCloud Key-Value Storage**, associated with your Apple ID.
- Merge: conflicting updates are merged on device (e.g. favourites union, latest timestamps).
- Opt-out: disable in **Settings → iCloud Sync** on any device; that device stops uploading and merging but keeps local data.
- iHTC Studio cannot read your iCloud container.

## App Group (Widget Extension — iOS/iPad only)

iLinux uses an App Group (`group.com.iHTCboy.iLinuxs`) to share a small amount of data with its Home Screen widget extension. This data includes:

- The selected content language code (e.g. `en`, `zh-Hans`)
- A theme colour snapshot (accent hex and gradient values)
- A summary of your learning progress (favourites count, quiz stats) for widget display
- The selected **widget command library** (Linux / CMD / PowerShell)
- The Daily Command widget shuffle counter (a simple integer used to pick the next featured command)

This data is written to a shared container on your device only, and is never transmitted anywhere.

## What iLinux Is Not

iLinux does not execute shell commands, open SSH sessions or access remote systems. No command-line input you might type elsewhere is collected by this app.

## In-App Purchase

iLinux includes an optional tip/purchase option. All payment transactions are handled exclusively by **Apple's StoreKit framework**. iHTC Studio does not receive, process or store any payment card information or billing details.

## Children's Privacy

iLinux does not knowingly collect any personal data from anyone, including children under 13. Since we do not collect any data at all, no special provisions are needed.

## Changes to This Policy

We may update this Privacy Policy from time to time. Any changes will be posted on this page with an updated date. We encourage you to review this page periodically.

## Contact Us

If you have any questions about this Privacy Policy, please contact us:

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>

<section lang="zh-CN" markdown="1">

爱火腿肠工作室（iHTC Studio）（「我们」；原 iHTCTeam）为 iLinux（亦称"爱 Linux"）这款应用开发并维护本页面，以告知你在使用应用过程中，我们关于个人数据收集、使用与披露的政策。

## 概要

**爱 Linux 不收集统计分析或出售个人数据。** 命令库完全离线。可选 **iCloud 同步**（登录 iCloud 并开启后）将收藏、测验进度、主题与显示偏好存入 **您 Apple ID 下的 iCloud 键值存储**——iHTC Studio 不运营后端服务器。

## 数据收集

iHTC Studio 不运营统计、广告或追踪。您的学习数据留在设备上，启用同步时由 **Apple iCloud** 托管，我们无法访问。

## 应用工作原理

爱 Linux 将所有用户生成的数据——收藏、最近浏览、测验结果、错题记录、Shell 平台偏好、收藏范围、小组件命令库与应用偏好——存储在设备本地：

- 所有命令数据（**Linux、CMD 与 PowerShell** 的 JSON 摘要与 Markdown 文档）都打包在应用内，绝不从任何外部服务器获取。
- 浏览命令与做测验无需联网。
- 可选 **iCloud 同步**使用 Apple **NSUbiquitousKeyValueStore**；可在设置中按设备关闭。
- 应用内打开外部链接（如点按反馈区的 URL）使用标准 iOS 网络行为；链接的页面由你的设备直接从其主机加载，不经过任何 iHTC Studio 服务器。
- 可选的 **App Store 版本检查**（`AppStoreVersionChecker`）会向公开的 iTunes Lookup API 发起一次只读请求，比较已安装版本与最新版本。该请求不发送任何个人数据。

## 权限

仅在您选择将**分享卡片或命令截图保存到相册**时，爱 Linux 会请求**相册**访问权限。无需相机、麦克风、位置或通讯录权限。

## 数据存储

| 数据 | 存储位置 |
|------|-----------------|
| 收藏、最近浏览、错题、学习状态（按平台） | 设备本地 UserDefaults / App Group |
| 测验进度（按日期与 Shell 平台） | 设备本地应用沙盒 |
| 主题、语言、布局、Shell 平台、收藏范围、小组件库 | 设备本地 UserDefaults / App Group |
| iCloud 同步镜像（可选） | Apple iCloud 键值存储 |
| 小组件快照（仅 iOS/iPad） | App Group 容器 |

不在 iHTC Studio 服务器存储数据。

## iCloud 同步（可选）

开启 **iCloud 同步** 且已登录 iCloud 时，同步**学习进度**、**主题**与**应用偏好**；冲突自动合并；可单设备关闭。

## App Group（小组件扩展 — 仅 iOS/iPad）

爱 Linux 使用 App Group（`group.com.iHTCboy.iLinuxs`）与其主屏小组件扩展共享少量数据。包括：

- 当前内容语言代码（如 `en`、`zh-Hans`）
- 主题色快照（主色 hex 与渐变值）
- 学习进度摘要（收藏数、测验统计）用于小组件显示
- 当前**小组件命令库**（Linux / CMD / PowerShell）
- 「每日命令」小组件的随机刷新计数

这些数据仅写入设备本地的共享容器，从不传输到任何地方。

## 应用不是什么

爱 Linux 不执行 Shell 命令、不建立 SSH 连接、不访问远程系统。你在其它环境输入的命令行内容不会被本应用收集。

## 应用内购

爱 Linux 包含可选的打赏 / 购买选项。所有支付交易完全由 **Apple StoreKit 框架** 处理。iHTC Studio 不接收、不处理、也不存储任何支付卡信息或账单细节。

## 儿童隐私

爱 Linux 不会有意收集任何人（包括 13 岁以下儿童）的个人数据。因为我们完全不收集数据，所以无需特别条款。

## 政策变更

我们可能不时更新本隐私政策。任何变更都会更新本页并标注日期。建议你定期回访。

## 联系我们

如果你对本隐私政策有任何疑问，请联系：

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>

<section lang="zh-TW" markdown="1">

愛火腿腸工作室（iHTC Studio）（「我們」；原 iHTCTeam）為 iLinux（亦稱「愛 Linux」）這款應用開發並維護本頁面，以告知你在使用應用過程中，我們關於個人資料收集、使用與揭露的政策。

## 摘要

**愛 Linux 不收集統計分析或出售個人資料。** 指令庫完全離線。可選 **iCloud 同步**將收藏、測驗進度、主題與顯示偏好存入 **您 Apple ID 下的 iCloud 鍵值儲存**。

## 資料收集

iHTC Studio 不營運統計、廣告或追蹤。您的學習資料留在裝置上，啟用同步時由 **Apple iCloud** 託管。

## 應用運作原理

愛 Linux 將所有使用者產生的資料——收藏、最近瀏覽、測驗結果、錯題紀錄、Shell 平台偏好、收藏範圍、小工具指令庫與應用偏好——儲存在裝置本地：

- 所有指令資料（**Linux、CMD 與 PowerShell** 的 JSON 摘要與 Markdown 文件）都打包在應用內，絕不從任何外部伺服器取得。
- 瀏覽指令與做測驗無需連網。
- 可選 **iCloud 同步**使用 Apple **NSUbiquitousKeyValueStore**；可在設定中按裝置關閉。
- 應用內開啟外部連結（如點按回饋區的 URL）使用標準 iOS 網路行為；連結的頁面由你的裝置直接從其主機載入，不經過任何 iHTC Studio 伺服器。
- 可選的 **App Store 版本檢查**（`AppStoreVersionChecker`）會向公開的 iTunes Lookup API 發起一次只讀請求，比較已安裝版本與最新版本。該請求不傳送任何個人資料。

## 權限

僅在您選擇將**分享卡片或指令截圖儲存到相簿**時，愛 Linux 會請求**相簿**存取權限。無需相機、麥克風、位置或通訊錄權限。

## 資料儲存

| 資料 | 儲存位置 |
|------|-----------------|
| 收藏、最近瀏覽、錯題、學習狀態（依平台） | 裝置本地 UserDefaults / App Group |
| 測驗進度（依日期與 Shell 平台） | 裝置本地應用沙盒 |
| 主題、語言、佈局、Shell 平台、收藏範圍、小工具庫 | 裝置本地 UserDefaults / App Group |
| iCloud 同步鏡像（可選） | Apple iCloud 鍵值儲存 |
| 小工具快照（僅 iOS/iPad） | App Group 容器 |

不在 iHTC Studio 伺服器儲存資料。

## iCloud 同步（可選）

開啟 **iCloud 同步** 且已登入 iCloud 時，同步**學習進度**、**主題**與**應用偏好**；可單裝置關閉。

## App Group（小工具擴充套件 — 僅 iOS/iPad）

愛 Linux 使用 App Group（`group.com.iHTCboy.iLinuxs`）與其主畫面小工具擴充套件共享少量資料。包括：

- 目前內容語言代碼（如 `en`、`zh-Hans`）
- 主題色快照（主色 hex 與漸層值）
- 學習進度摘要（收藏數、測驗統計）用於小工具顯示
- 目前**小工具指令庫**（Linux / CMD / PowerShell）
- 「每日指令」小工具的隨機刷新計數

這些資料僅寫入裝置本地的共享容器，從不傳送到任何地方。

## 應用不是什麼

愛 Linux 不執行 Shell 指令、不建立 SSH 連線、不存取遠端系統。你在其它環境輸入的指令列內容不會被本應用收集。

## 應用內購

愛 Linux 包含可選的打賞 / 購買選項。所有支付交易完全由 **Apple StoreKit 框架** 處理。iHTC Studio 不接收、不處理、也不儲存任何支付卡資訊或帳單細節。

## 兒童隱私

愛 Linux 不會有意收集任何人（包括 13 歲以下兒童）的個人資料。因為我們完全不收集資料，所以無需特別條款。

## 政策變更

我們可能不時更新本隱私政策。任何變更都會更新本頁並標註日期。建議你定期回訪。

## 聯絡我們

如果你對本隱私政策有任何疑問，請聯絡：

- **電子郵件：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
