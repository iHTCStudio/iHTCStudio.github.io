---
layout: doc
title: iCangJie — Privacy Policy
app_id: iCangJie
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iCangJie.
---

<section lang="en" markdown="1">

iHTC Studio ("we", "us" or "our"; formerly iHTCTeam) built iCangJie (also known as "爱仓颉" / "愛倉頡"). This page describes our policies regarding data collection, use and disclosure when you use our app.

## Summary

**iCangJie does not collect, store or transmit any personal data.** All character lookups, quizzes, typing practice and learning progress are processed entirely on your device. No account is required, and no internet connection is needed for any core feature.

## Data Collection

We do not collect any data. Specifically:

- **No personal information** is collected (no name, email, phone number or account).
- **No usage data** or analytics are collected.
- **No third-party SDKs** for advertising, analytics or crash reporting are integrated.
- **No cookies or tracking** technologies are used.

## iCloud Sync

iCangJie offers an optional iCloud sync feature (toggleable in Settings). When enabled, the following data is synced via **iCloud Key-Value Storage (iCloud KVS)**, a service provided and managed entirely by Apple:

| Synced Data | Purpose |
|-------------|---------|
| Favorites | Your bookmarked characters |
| Learning status | Progress level for each character |
| Wrong question book | Incorrectly answered quiz questions |
| Quiz scores & streak | Your daily quiz performance |
| Typing statistics | Accuracy, streak, and session counts from typing practice |
| Daily typing records | Per-day character counts and code-length histograms (~120 days) |
| Built-in passage progress | Resume position in built-in typing passages |

This data is transmitted directly between your devices through Apple's iCloud infrastructure. iHTC Studio does not operate any server and has no access to your iCloud data. Apple's handling of iCloud data is governed by [Apple's Privacy Policy](https://www.apple.com/privacy/).

You can disable iCloud sync at any time in Settings. When disabled, all data stays local to each device.

Typing UI preferences (wrong-key retention, passage pinyin) are stored locally on each device and are **not** synced via iCloud.

## Data Stored Locally on Your Device

All data created by iCangJie stays on your device:

| Data | Storage | User Control |
|------|---------|--------------|
| Favorites | Local (UserDefaults / App Group) | Remove individual items or clear all in app |
| Learning status | Local (UserDefaults) | Reset in app settings |
| Wrong question book | Local (UserDefaults) | Clear in app |
| Quiz scores & streak | Local (UserDefaults) | Reset in app settings |
| Typing statistics & daily records | Local (UserDefaults / App Group); optional iCloud KVS | Cleared when learning data is reset |
| Passage progress | Local (UserDefaults / App Group); optional iCloud KVS | Cleared when learning data is reset |
| Typing UI preferences | Local (UserDefaults) | Change in Settings → Typing |
| Onboarding & newcomer path flags | Local (UserDefaults) | Shown again only if you reset app data |
| Quiz preferences | Local (UserDefaults) | Change in quiz settings |
| Spotlight indexing preference | Local (UserDefaults) | Toggle in Settings → Home shortcuts |
| App preferences & theme | Local (UserDefaults) | Reset by deleting the app |

Widgets use an **App Group** container to share data between the main app and widget extensions. This container stays on your device and is not accessible to any third party.

### JSON Backup (user-initiated)

You may **export** a JSON backup file (`.icangjie-backup`) containing learning data. The file is written to a location **you choose** (Files, AirDrop, etc.). **Import** reads a file you select. iHTC Studio does not upload, host, or access backup files.

### Spotlight Indexing (iOS, optional)

When enabled, iCangJie indexes up to **80** favorite and recent characters into the **on-device** iOS Spotlight index (domain `com.iHTCboy.iCangJie.words`). Entries expire after 30 days. This data never leaves your device except through Apple's Spotlight system on your iPhone/iPad. Disable anytime in Settings.

## Permissions

iCangJie requests **only one optional permission**:

| Permission | When requested | Purpose |
|------------|----------------|---------|
| **Photo Library (Add Only)** | When you tap **Save to Photos** on a radical chart image in a tutorial | Save the image to your photo library |

iCangJie does **not** read your existing photos. There is no access to your camera, microphone, contacts, location, or local network for core features.

Optional features that open external websites (Youdao online lookup, tutorial links) use the system browser and do not grant iCangJie access to your browsing history.

## Children's Privacy

iCangJie does not knowingly collect any personal data from anyone, including children under 13. Since no data is collected at all, no special provisions are required.

## Changes to This Policy

We may update this Privacy Policy from time to time. Any changes will be posted on this page with an updated date. We encourage you to review this page periodically.

## Contact Us

If you have any questions about this Privacy Policy, please contact us:

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>

<section lang="zh-CN" markdown="1">

爱火腿肠工作室（iHTC Studio）（「我们」；原 iHTCTeam）为爱仓颉（iCangJie，亦称「愛倉頡」）这款应用开发并维护本页面，以告知你在使用应用过程中，我们关于数据收集、使用与披露的政策。

## 概要

**爱仓颉不收集、存储或传输任何个人数据。** 所有查字、测验、打字练习与学习进度完全在你的设备上处理。无需账号，所有核心功能也无需联网。

## 数据收集

我们不收集任何数据。具体而言：

- **不收集任何个人信息**（无姓名、邮箱、电话或账号）。
- **不收集使用数据**或统计分析。
- **不集成任何第三方 SDK**用于广告、统计或崩溃上报。
- **不使用 Cookie 或追踪**技术。

## iCloud 同步

爱仓颉提供可选的 iCloud 同步功能（可在设置中开关）。启用后，以下数据通过 **iCloud 键值存储（iCloud KVS）** 同步，该服务完全由 Apple 提供和管理：

| 同步数据 | 用途 |
|-------------|---------|
| 收藏夹 | 你收藏的汉字 |
| 学习状态 | 每个汉字的学习进度等级 |
| 错题本 | 测验中答错的题目 |
| 测验成绩与连胜 | 每日测验表现 |
| 打字统计 | 打字练习的准确率、连胜与场次 |
| 按日打字记录 | 每日字数与码长直方图（约 120 天） |
| 内置文章进度 | 内置打字文章的续练位置 |

这些数据通过 Apple 的 iCloud 基础架构在你的设备之间直接传输。iHTC Studio 不运营任何服务器，也无法访问你的 iCloud 数据。Apple 对 iCloud 数据的处理受 [Apple 隐私政策](https://www.apple.com/privacy/) 约束。

你可以随时在设置中关闭 iCloud 同步。关闭后，所有数据仅保留在各设备本地。

打字界面偏好（错键保留、篇章拼音）仅保存在各设备本地，**不会**通过 iCloud 同步。

## 设备本地存储的数据

爱仓颉创建的所有数据都留在你的设备上：

| 数据 | 存储位置 | 用户控制 |
|------|---------|--------------|
| 收藏夹 | 本地（UserDefaults / App Group）| 在应用中移除单个项目或清空全部 |
| 学习状态 | 本地（UserDefaults）| 在应用设置中重置 |
| 错题本 | 本地（UserDefaults）| 在应用中清除 |
| 测验成绩与连胜 | 本地（UserDefaults）| 在应用设置中重置 |
| 打字统计与按日记录 | 本地（UserDefaults / App Group）；可选 iCloud KVS | 重置学习数据时清除 |
| 篇章进度 | 本地；可选 iCloud KVS | 重置学习数据时清除 |
| 打字界面偏好 | 本地（UserDefaults）| 在设置 → 打字练习中修改 |
| 引导与测验偏好 | 本地（UserDefaults）| 删除应用重置 |
| Spotlight 开关 | 本地（UserDefaults）| 设置 → 主屏快捷操作 |
| 应用偏好与主题 | 本地（UserDefaults）| 删除应用即可重置 |

小组件使用 **App Group** 容器在主应用与小组件扩展之间共享数据。该容器留在你的设备上，第三方无法访问。

### JSON 备份（用户主动操作）

你可 **导出** `.icangjie-backup` JSON 文件到自选位置（文件、隔空投送等），也可 **导入** 自选文件。我们不会上传或访问备份内容。

### Spotlight 索引（iOS，可选）

开启后，最多 **80** 个收藏与最近浏览汉字写入本机 Spotlight 索引，30 天过期。仅在本机 Spotlight 使用，可随时在设置中关闭。

## 权限

爱仓颉**仅请求一项可选权限**：

| 权限 | 何时请求 | 用途 |
|------|----------|------|
| **相册（仅添加）** | 在教程字根图点击 **保存到相册** 时 | 将图片保存到你的相册 |

爱仓颉**不会**读取你已有的照片。不访问相机、麦克风、通讯录、位置或本地网络（核心功能）。

可选的在线查词（有道）与教程外链通过系统浏览器打开，爱仓颉无法访问你的浏览记录。

## 儿童隐私

爱仓颉不会有意收集任何人（包括 13 岁以下儿童）的个人数据。因为我们完全不收集数据，所以无需特别条款。

## 政策变更

我们可能不时更新本隐私政策。任何变更都会更新本页并标注日期。建议你定期回访。

## 联系我们

如果你对本隐私政策有任何疑问，请联系：

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>

<section lang="zh-TW" markdown="1">

愛火腿腸工作室（iHTC Studio）（「我們」；原 iHTCTeam）為愛倉頡（iCangJie）這款應用開發並維護本頁面，以告知你在使用應用過程中，我們關於資料收集、使用與揭露的政策。

## 概要

**愛倉頡不收集、儲存或傳送任何個人資料。** 所有查字、測驗、打字練習與學習進度完全在你的裝置上處理。無需帳號，所有核心功能也無需連網。

## 資料收集

我們不收集任何資料。具體而言：

- **不收集任何個人資訊**（無姓名、電子郵件、電話或帳號）。
- **不收集使用資料**或統計分析。
- **不整合任何第三方 SDK**用於廣告、統計或當機回報。
- **不使用 Cookie 或追蹤**技術。

## iCloud 同步

愛倉頡提供可選的 iCloud 同步功能（可在設定中開關）。啟用後，以下資料透過 **iCloud 鍵值儲存（iCloud KVS）** 同步：

| 同步資料 | 用途 |
|-------------|---------|
| 收藏夾 | 你收藏的漢字 |
| 學習狀態 | 每個漢字的學習進度等級 |
| 錯題本 | 測驗中答錯的題目 |
| 測驗成績與連勝 | 每日測驗表現 |
| 打字統計 | 打字練習的準確率、連勝與場次 |
| 按日打字記錄 | 每日字數與碼長直方圖（約 120 天） |
| 內建文章進度 | 內建打字文章的續練位置 |

這些資料透過 Apple 的 iCloud 基礎架構在你的裝置之間直接傳輸。iHTC Studio 不營運任何伺服器，也無法存取你的 iCloud 資料。

## 裝置本地儲存的資料

愛倉頡建立的所有資料都留在你的裝置上，可透過應用內設定清除或重置。

### JSON 備份

由你主動匯出/匯入 `.icangjie-backup` 檔案；我們不會上傳或存取。

### Spotlight 索引（iOS）

可選；最多 80 字寫入本機 Spotlight，可隨時關閉。

## 權限

愛倉頡**僅請求一項可選權限**：

| 權限 | 何時請求 | 用途 |
|------|----------|------|
| **相簿（僅新增）** | 在教程字根圖點擊 **儲存到相簿** 時 | 將圖片儲存到你的相簿 |

愛倉頡**不會**讀取你已有的照片。不存取相機、麥克風、通訊錄、位置或區域網路（核心功能）。

## 兒童隱私

愛倉頡不會有意收集任何人（包括 13 歲以下兒童）的個人資料。

## 政策變更

我們可能不時更新本隱私政策。任何變更都會更新本頁並標註日期。

## 聯絡我們

如果你對本隱私政策有任何疑問，請聯絡：

- **電子郵件：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
