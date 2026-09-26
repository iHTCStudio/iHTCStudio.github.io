---
layout: doc
title: iBaiJia — Privacy Policy
app_id: iBaiJia
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iBaiJia (爱百家姓) — fully offline surname-culture app, Data Not Collected, optional iCloud and Photo Library add-only.
---

<section lang="en" markdown="1">

**Last updated:** August 18, 2026

iHTC Studio ("we", "us" or "our"; formerly iHTCTeam) built **iBaiJia** (also known as "爱百家姓" / "愛百家姓", Bundle ID `com.iHTCboy.iBaiJia`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on **this page** as the public privacy policy for the app. For App Store Connect, open this Privacy Policy in your browser and copy the address from the address bar (the public site domain may change over time).

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration, email sign-in, or phone number |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your personal data |
| Network | Surname library, detail reading, recite, Study Hall, naming inspiration, widgets, and daily notifications work **offline** after install |
| Analytics / ads / tracking | **None** — no third-party analytics, advertising, or tracking SDKs; no App Tracking Transparency use |
| Optional Apple services | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default), optional **system speech / translation** |

## Data Collection

We do **not** collect, sell, or share personal information for advertising or analytics.

- **No account** — You can use all core features without creating an account with us.
- **No analytics or ads** — The app binary does not integrate third-party analytics, advertising, or crash-reporting SDKs that phone home to us.
- **No content upload** — Your favorites, surname lists, notes, reading history, study progress, streaks, naming preferences, and settings stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## How the App Works

- **Bundled library** — Surname JSON, English glosses, stroke-order glyphs, and indexes ship inside the app / widget bundle. Browsing and study do not require a network request.
- **On-device speech** — Reading and recitation use Apple’s system **AVSpeechSynthesizer** (TTS). We do not send surname text to iHTC Studio.
- **Optional system translation** — If you long-press detail text and use Apple’s system Translation (iOS 17.4 / macOS 14.4+), processing stays with Apple’s OS. We do not operate a translation backend.
- **Naming inspiration** — Generated entirely on device from bundled data. No names or preferences are uploaded.
- **Widgets & App Group** — Widgets and the app share preferences and lightweight state via App Group `group.com.iHTCboy.iBaiJia` on your device.
- **Daily notifications** — Scheduled locally with User Notifications. Tapping a notification opens a deep link on device; no server fan-out.
- **Share cards** — Images are rendered on device. Saving uses **Photo Library add-only** only when you tap save. System Share Sheet may send the image to an app **you** choose; that destination’s privacy policy then applies.
- **Optional tip** — “Tip Developer” (`com.iHTCboy.iBaiJia.6`) is a consumable **StoreKit** purchase processed by Apple. We do not receive your payment card details.
- **Siri / Shortcuts / Control Center** — Optional system integrations open on-device deep links; they do not send your library to us.
- **Optional Spotlight** — Off by default. If you enable indexing, surnames are indexed by the system on device for local search; we do not operate a search backend.
- **Feedback email** — If you send Feedback, the message may include text you write plus device / app diagnostics (version, OS, language) solely for troubleshooting.

## Data Stored on Your Device

| Data | Where | Purpose |
|------|-------|---------|
| Surname database & stroke glyphs | App bundle | Offline reading, tracing & study |
| Favorites & surname lists | App Group UserDefaults | Starred surnames and user lists |
| Notes | App Group UserDefaults | Surname notes you write |
| My Surname | App Group UserDefaults | Personalized home & widgets |
| Reading history / last read | App Group UserDefaults | Continue browsing, history UI |
| Study progress & high scores | App Group UserDefaults | Study Hall state |
| Check-in streak | App Group UserDefaults | Daily habit |
| Appearance & reading prefs | App Group UserDefaults | Theme, accent, language, layout, TTS, tabs, widgets |
| Daily Surname cache & notification prefs | App Group UserDefaults | Today’s ID, schedule time |
| Share-card preferences | App Group UserDefaults | Last style choices |
| Onboarding & TipKit state | Standard UserDefaults (device) | Welcome guide / discovery tips |
| Home Screen quick actions | System + local prefs | Shortcuts you configure |
| Widget / Live Activity snapshots | App Group / ActivityKit | Display text you already opened |

Uninstalling the app removes sandbox and App Group data associated with the app (subject to iOS/macOS behavior). Optional iCloud copies remain in **your** iCloud until you clear them or turn sync off and delete elsewhere.

## iCloud Sync (Optional)

If you enable **iCloud Sync** in Settings, the app mirrors selected user data through Apple’s **`NSUbiquitousKeyValueStore`** tied to **your Apple ID**:

- Favorites
- Surname lists
- Notes
- Reading history
- Study progress / high scores
- Check-in streaks
- Related preferences

Sync traffic goes to **Apple iCloud**, not to iHTC Studio. You can disable sync in Settings. We cannot read your iCloud contents.

## Permissions

iBaiJia requests permissions only when a feature needs them:

| Permission | When | Why |
|------------|------|-----|
| Notifications | You enable Daily Surname reminders | Local scheduling |
| Photo Library (Add Only) | You save a share card | Write the rendered image |
| iCloud | You enable sync | Sync favorites / lists / history / progress / streaks / notes |
| Live Activities (iOS) | You enable Reading Live Activity | Lock Screen / Dynamic Island |
| Background audio (iOS) | You enable background recitation | Continue TTS in background |

We do **not** request Contacts, precise Location, Camera, Microphone (beyond system TTS playback), or Tracking.

## Children’s Privacy

iBaiJia is a cultural learning app for a general audience and is **not** in the Kids Category. We do not knowingly collect personal information from children. The app does not require an account. Families may use reading and study features offline on their own devices.

## Third Parties

The only third-party services involved in normal use are **Apple** (App Store, iCloud, StoreKit, system TTS, optional system translation, notifications, Live Activities, Spotlight). Surname datasets include open-licensed English glosses (CC BY 4.0) and stroke-order glyphs (LGPL / Arphic Public License) — see the in-app About page for attribution. Cultural commentary in the app is original study material marked for reference.

## Data Retention & Deletion

- **On device:** You can clear study progress, history, or notes in the app. Settings supports export/import for backup. Delete the app to remove local sandbox and App Group data (subject to system behavior).
- **iCloud:** Disable sync in Settings; you may also manage iCloud storage in system Settings.
- **We do not retain copies** of your reading, notes, or favorites on iHTC Studio servers.

## Changes to This Policy

We may update this page for legal, product, or App Store compliance reasons. The “Last updated” date will change. Continued use after an update means you accept the revised policy.

## Contact

Questions about privacy: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>

<section lang="zh-CN" markdown="1">

**最近更新：** 2026 年 8 月 18 日

爱火腿肠工作室（iHTC Studio）（「我们」；原 iHTCTeam）开发了 **爱百家姓**（iBaiJia / 愛百家姓，Bundle ID `com.iHTCboy.iBaiJia`）。本隐私政策说明你在使用本应用时，数据如何被处理。本页可作为 **App Store 审核**与用户查阅的公开隐私政策地址。在 App Store Connect 填写隐私政策 URL 时，请在浏览器中打开本 [隐私政策](privacy) 页，从地址栏复制当前网址（公开站点域名日后可能变更）。

## 概要（对齐 App Store 隐私标签）

| 主题 | 我们的做法 |
|------|------------|
| 账号 | **不需要** — 无注册、邮箱登录或手机号 |
| 爱火腿肠工作室的数据收集 | **不收集数据** — 我们**不**运营接收你个人数据的后端 |
| 网络 | 安装后，姓氏语料、阅读、诵读、学堂、取名、小组件与每日通知可**离线** |
| 分析 / 广告 / 追踪 | **无** — 无第三方分析、广告或追踪 SDK；不使用 App 追踪透明度 |
| 可选 Apple 服务 | **iCloud**（你的私有 KVS）、分享卡的**相册（仅添加）**、**StoreKit** 打赏、**本地通知**、可选**实时活动**、可选 **Spotlight**（默认关）、可选**系统朗读 / 翻译** |

## 数据收集

我们**不**为广告或分析收集、出售或共享个人信息。

- **无账号** — 无需向我们注册即可使用全部核心功能。
- **无分析或广告** — 应用未集成会向我们家上报的第三方分析、广告或崩溃 SDK。
- **不上传内容** — 收藏、姓氏册、笔记、阅读记录、学堂进度、打卡与取名偏好留在你的设备（以及可选的**你的** iCloud），不会上传到 iHTC Studio 服务器，因为**我们不为本应用运营此类服务器**。

## 应用如何工作

- **内置语料** — 姓氏 JSON、英文释义、笔顺字形与索引随 App / 小组件安装。
- **本机朗读** — 使用系统 **AVSpeechSynthesizer**（TTS）；正文不会发送给我们。
- **可选系统翻译** — 详情长按调用 Apple 系统翻译（iOS 17.4 / macOS 14.4+）；处理留在系统侧。
- **取名灵感** — 纯本机从内置数据生成，不上传姓名或偏好。
- **小组件与 App Group** — 通过 `group.com.iHTCboy.iBaiJia` 在本机共享状态。
- **每日通知** — 仅本机调度；点击通过深链打开对应内容。
- **分享卡** — 本机渲染；仅在你点保存时使用**相册（仅添加）**。
- **可选打赏** — `com.iHTCboy.iBaiJia.6` 消耗型内购由 **Apple StoreKit** 处理。
- **Siri / 快捷指令 / 控制中心** — 打开本机深链，不上传语料。
- **可选 Spotlight** — 默认关闭；开启后由系统本机索引姓氏。
- **反馈邮件** — 你主动发送时可能包含自愿填写内容与设备/应用诊断信息，仅用于排查。

## 设备上存储的数据

| 数据 | 位置 | 用途 |
|------|------|------|
| 姓氏语料与笔顺 | App 包 | 离线阅读、描红与学堂 |
| 收藏与姓氏册 | App Group UserDefaults | 星标与用户清单 |
| 笔记 | App Group UserDefaults | 你写下的姓氏笔记 |
| 我的姓氏 | App Group UserDefaults | 个性化首页与小组件 |
| 阅读记录 / 上次浏览 | App Group UserDefaults | 继续浏览、历史界面 |
| 学堂进度与最高分 | App Group UserDefaults | 姓氏学堂 |
| 打卡连续 | App Group UserDefaults | 今日一姓习惯 |
| 外观与阅读偏好 | App Group UserDefaults | 主题、强调色、语言、布局、TTS、Tab、小组件 |
| 今日一姓缓存与通知偏好 | App Group UserDefaults | 今日 ID、提醒时间 |
| 分享卡偏好 | App Group UserDefaults | 上次样式选择 |
| 引导与 TipKit 状态 | 标准 UserDefaults | 欢迎引导 |
| 主屏快捷操作 | 系统 + 本地偏好 | 你配置的快捷 |
| 小组件 / 实时活动快照 | App Group / ActivityKit | 你已打开内容的展示 |

卸载应用会移除与该应用关联的沙盒与 App Group 数据（以 iOS/macOS 行为为准）。可选 iCloud 副本留在**你的** iCloud 中，直至你关闭同步或在别处删除。

## iCloud 同步（可选）

在设置中开启 **iCloud 同步**后，应用通过 Apple **`NSUbiquitousKeyValueStore`**（绑定**你的 Apple ID**）镜像：

- 收藏
- 姓氏册
- 笔记
- 阅读记录
- 学堂进度 / 最高分
- 打卡连续
- 相关偏好

同步流量发往 **Apple iCloud**，而非 iHTC Studio。可在设置中关闭。我们无法读取你的 iCloud 内容。

## 权限

仅在功能需要时请求：

| 权限 | 何时 | 原因 |
|------|------|------|
| 通知 | 你开启今日一姓提醒 | 本机调度 |
| 相册（仅添加） | 你保存分享卡 | 写入渲染图片 |
| iCloud | 你开启同步 | 同步收藏/姓氏册/记录/进度/打卡/笔记 |
| 实时活动（iOS） | 你开启朗读实时活动 | 锁屏 / 灵动岛 |
| 后台音频（iOS） | 你开启后台诵读 | 后台继续 TTS |

我们**不**请求通讯录、精确位置、相机、麦克风（除系统 TTS 播放外）或追踪。

## 儿童隐私

本应用面向一般公众的文化学习，**非**儿童类别。我们不会有意收集儿童个人信息；应用无需账号。家庭可在自有设备上离线使用阅读与学堂功能。

## 第三方

正常使用中涉及的第三方仅为 **Apple**（App Store、iCloud、StoreKit、系统 TTS、可选系统翻译、通知、实时活动、Spotlight）。英文姓氏数据集遵循 CC BY 4.0；笔顺字形子集来自 makemeahanzi（LGPL / Arphic Public License）——详见应用内关于页署名。文化白话字段为原创学习参考材料。

## 保留与删除

- **本机：** 可在应用内清除进度、历史或笔记；设置支持导出/导入备份；删除应用可移除本地数据。
- **iCloud：** 在设置中关闭同步，或在系统设置中管理 iCloud 存储。
- **我们不在服务器保留**你的阅读、笔记或收藏数据副本。

## 政策变更

我们可能因法律、产品或 App Store 合规原因更新本页。「最近更新」日期会随之变更。更新后继续使用即表示接受修订后的政策。

## 联系

隐私相关问题：[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>

<section lang="zh-TW" markdown="1">

**最近更新：** 2026 年 8 月 18 日

愛火腿腸工作室（iHTC Studio）（「我們」；原 iHTCTeam）開發了 **愛百家姓**（iBaiJia，Bundle ID `com.iHTCboy.iBaiJia`）。本隱私政策說明你在使用本應用時，資料如何被處理。本頁可作為 **App Store 審核**與使用者查閱的公開隱私政策地址。在 App Store Connect 填寫隱私政策 URL 時，請在瀏覽器中開啟本 [隱私政策](privacy) 頁，從網址列複製目前網址（公開站點網域日後可能變更）。

## 概要（對齊 App Store 隱私標籤）

| 主題 | 我們的做法 |
|------|------------|
| 帳號 | **不需要** — 無註冊、信箱登入或手機號 |
| 愛火腿腸工作室的資料收集 | **不收集資料** — 我們**不**營運接收你個人資料的後端 |
| 網路 | 安裝後，姓氏語料、閱讀、誦讀、學堂、取名、小工具與每日通知可**離線** |
| 分析 / 廣告 / 追蹤 | **無** — 無第三方分析、廣告或追蹤 SDK |
| 可選 Apple 服務 | **iCloud**、分享卡的**照片（僅加入）**、**StoreKit** 打賞、**本地通知**、可選**即時動態**、可選 **Spotlight**（預設關） |

## 資料收集

我們**不**為廣告或分析收集、出售或共享個人資訊。收藏、姓氏冊、筆記、閱讀記錄、學堂進度、打卡與取名偏好留在你的裝置（以及可選的**你的** iCloud），不會上傳至 iHTC Studio 伺服器。

## 應用如何工作

- **內建語料** — 姓氏 JSON、英文釋義、筆順字形與索引隨 App 安裝。
- **本機朗讀** — 使用系統 TTS；正文不會傳送給我們。
- **取名靈感** — 純本機生成，不上傳姓名或偏好。
- **分享卡** — 本機渲染；僅在你點儲存時使用**照片（僅加入）**。
- **可選打賞** — `com.iHTCboy.iBaiJia.6` 由 **Apple StoreKit** 處理。

## iCloud 同步（可選）

可選同步**收藏**、**姓氏冊**、**筆記**、**閱讀記錄**、**學堂進度**、**打卡**等，經你的私有 iCloud KVS。

## 權限

| 權限 | 何時 | 原因 |
|------|------|------|
| 通知 | 你開啟今日一姓提醒 | 本機排程 |
| 照片（僅加入） | 你儲存分享卡 | 寫入渲染圖片 |
| iCloud | 你開啟同步 | 同步使用者資料 |
| 即時動態（iOS） | 你開啟朗讀即時動態 | 鎖定畫面 / 動態島 |
| 背景音訊（iOS） | 你開啟背景誦讀 | 背景繼續 TTS |

## 兒童隱私

本應用面向一般大眾的文化學習，**非**兒童類別；無需帳號。

## 第三方

正常使用中涉及的第三方僅為 **Apple**。英文姓氏資料集遵循 CC BY 4.0；筆順字形子集來自 makemeahanzi（LGPL / Arphic Public License）。

## 保留與刪除

- **本機：** 可在應用內清除進度、歷史或筆記；刪除應用可移除本地資料。
- **iCloud：** 在設定中關閉同步，或在系統設定中管理 iCloud 儲存空間。
- **我們不在伺服器保留**你的閱讀、筆記或收藏資料副本。

## 政策變更

我們可能因法律、產品或 App Store 合規原因更新本頁。

## 聯絡

隱私相關問題：[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
