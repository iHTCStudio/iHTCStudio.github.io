---
layout: doc
title: iPrimer — Privacy Policy
app_id: iPrimer
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iPrimer (爱小学) — fully offline Xiaoxue growth app, Data Not Collected, optional iCloud and Photo Library add-only.
---

<section lang="en" markdown="1">

**Last updated:** August 18, 2026

iHTC Studio ("we", "us" or "our"; formerly iHTCTeam) built **iPrimer** (also known as "爱小学" / "愛小學", Bundle ID `com.iHTCboy.iPrimer`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on **this page** as the public privacy policy for the app. For App Store Connect, open this Privacy Policy in your browser and copy the address from the address bar (the public site domain may change over time).

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration, email sign-in, or phone number |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your personal data |
| Network | Library, reading, recite, Character Study, meditation, Life Guidance, widgets, and daily notifications work **offline** after install |
| Analytics / ads / tracking | **None** — no third-party analytics, advertising, or tracking SDKs; no App Tracking Transparency use |
| Optional Apple services | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities** |

## Data Collection

We do **not** collect, sell, or share personal information for advertising or analytics.

- **No account** — You can use all core features without creating an account with us.
- **No analytics or ads** — The app binary does not integrate third-party analytics, advertising, or crash-reporting SDKs that phone home to us.
- **No content upload** — Your reading history, favorites, study lists, reflection journal entries, habit check-ins, meditation streaks, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## How the App Works

- **Bundled library** — Chapter JSON, vernacular/English text, collected notes, glosses, meditation scripts, and indexes ship inside the app / widget bundle (curated from public web sources). Browsing and study do not require a network request.
- **On-device speech** — Recitation uses Apple’s system **AVSpeechSynthesizer** (TTS). We do not send chapter text to iHTC Studio.
- **Widgets & App Group** — Widgets and the app share preferences and lightweight state via App Group `group.com.iHTCboy.iPrimer` on your device.
- **Daily notifications** — Scheduled locally with User Notifications. Tapping a notification opens a deep link to a chapter ID on device; no server fan-out.
- **Share cards** — Images are rendered on device. Saving uses **Photo Library add-only** only when you tap save. System Share Sheet may send the image to an app **you** choose; that destination’s privacy policy then applies.
- **Optional tip** — “Tip Developer” (`com.iHTCboy.iPrimer.6`) is a consumable **StoreKit** purchase processed by Apple. We do not receive your payment card details.
- **Siri / Shortcuts / Control Center** — Optional system integrations open on-device deep links; they do not send your library to us.
- **Optional Spotlight** — If you enable indexing, content is indexed by the system on device for local search; we do not operate a search backend.

## Data Stored on Your Device

| Data | Where | Purpose |
|------|-------|---------|
| Chapter database | App / Widget bundle | Offline reading & study |
| Favorites & study lists | App Group UserDefaults | Starred works and user lists |
| Reading history / last read | App Group UserDefaults | Continue reading, history UI |
| Study progress & mastery | App Group UserDefaults | Character Study state, quiz / Hunt progress |
| Study streak / check-in | App Group UserDefaults | Daily Study habit |
| Reflection journal entries | App Group UserDefaults | Life Guidance journal |
| Habit check-ins (洒扫应对) | App Group UserDefaults | Life Guidance daily habits |
| Meditation streak & session prefs | App Group UserDefaults | Meditation continuity |
| Appearance & reading prefs | App Group UserDefaults | Theme, accent, language, layout, TTS, tabs, widgets, font scale |
| Daily Study cache & notification prefs | App Group UserDefaults | Today’s ID, schedule time, contextual toggle |
| Share-card preferences | App Group UserDefaults | Last style / ratio choices |
| Onboarding & TipKit state | Standard UserDefaults (device) | Welcome guide / discovery tips |
| Home Screen quick actions | System + local prefs | Shortcuts you configure |
| Widget / Live Activity snapshots | App Group / ActivityKit | Display text you already opened |

Uninstalling the app removes sandbox and App Group data associated with the app (subject to iOS/macOS behavior). Optional iCloud copies remain in **your** iCloud until you clear them or turn sync off and delete elsewhere.

## iCloud Sync (Optional)

If you enable **iCloud Sync** in Settings, the app mirrors selected user data through Apple’s **`NSUbiquitousKeyValueStore`** tied to **your Apple ID**:

- Favorites
- Study lists
- Reading history
- Study progress / mastery
- Study streaks
- Reflection journal entries
- Habit check-in history

Sync traffic goes to **Apple iCloud**, not to iHTC Studio. You can disable sync in Settings. We cannot read your iCloud contents.

## Permissions

iPrimer requests permissions only when a feature needs them:

| Permission | When | Why |
|------------|------|-----|
| Notifications | You enable Daily Study or meditation reminders | Local scheduling |
| Photo Library (Add Only) | You save a share card | Write the rendered image |
| iCloud | You enable sync | Sync favorites / lists / history / progress / streaks / journal / habits |
| Live Activities (iOS) | You enable Reading or Meditation Live Activity | Lock Screen / Dynamic Island |
| Background audio | You enable background recitation | Continue TTS in background |

We do **not** request Contacts, precise Location, Camera, Microphone (beyond system TTS playback), or Tracking.

## Children’s Privacy

iPrimer is rated **12+** and is **not** in the Kids Category. We do not knowingly collect personal information from children. The app does not require an account.

## Third Parties

The only third-party services involved in normal use are **Apple** (App Store, iCloud, StoreKit, system TTS, notifications, Live Activities).

## Data Retention & Deletion

- **On device:** Delete the app to remove local sandbox and App Group data (subject to system behavior).
- **iCloud:** Disable sync in Settings; you may also manage iCloud storage in system Settings.
- **We do not retain copies** of your reading, journal, or habit data on iHTC Studio servers.

## Changes to This Policy

We may update this page for legal, product, or App Store compliance reasons. The “Last updated” date will change. Continued use after an update means you accept the revised policy.

## Contact

Questions about privacy: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>

<section lang="zh-CN" markdown="1">

**最近更新：** 2026 年 8 月 18 日

爱火腿肠工作室（iHTC Studio）（「我们」；原 iHTCTeam）开发了 **爱小学**（iPrimer / 愛小學，Bundle ID `com.iHTCboy.iPrimer`）。本隐私政策说明你在使用本应用时，数据如何被处理。本页可作为 **App Store 审核**与用户查阅的公开隐私政策地址。在 App Store Connect 填写隐私政策 URL 时，请在浏览器中打开本 [隐私政策](privacy) 页，从地址栏复制当前网址（公开站点域名日后可能变更）。

## 概要（对齐 App Store 隐私标签）

| 主题 | 我们的做法 |
|------|------------|
| 账号 | **不需要** — 无注册、邮箱登录或手机号 |
| 爱火腿肠工作室的数据收集 | **不收集数据** — 我们**不**运营接收你个人数据的后端 |
| 网络 | 安装后，语料、阅读、诵读、品格学堂、冥想、人生指导、小组件与每日通知可**离线** |
| 分析 / 广告 / 追踪 | **无** — 无第三方分析、广告或追踪 SDK；不使用 App 追踪透明度 |
| 可选 Apple 服务 | **iCloud**（你的私有 KVS）、分享卡的**相册（仅添加）**、**StoreKit** 打赏、**本地通知**、可选**实时活动** |

## 数据收集

我们**不**为广告或分析收集、出售或共享个人信息。

- **无账号** — 无需向我们注册即可使用全部核心功能。
- **无分析或广告** — 应用未集成会向我们家上报的第三方分析、广告或崩溃 SDK。
- **不上传内容** — 阅读记录、收藏、学单、反思日记、习惯打卡、冥想连续、学堂进度与偏好留在你的设备（以及可选的**你的** iCloud），不会上传到 iHTC Studio 服务器，因为**我们不为本应用运营此类服务器**。

## 应用如何工作

- **内置语料** — 篇章 JSON、白话/英文、集注、释义、冥想引导与索引随 App / 小组件安装（由网络公开资料梳理）。
- **本机朗读** — 使用系统 **AVSpeechSynthesizer**（TTS）；篇章正文不会发送给我们。
- **小组件与 App Group** — 通过 `group.com.iHTCboy.iPrimer` 在本机共享状态。
- **每日通知** — 仅本机调度；点击通过深链打开对应篇章 ID。
- **分享卡** — 本机渲染；仅在你点保存时使用**相册（仅添加）**。
- **可选打赏** — `com.iHTCboy.iPrimer.6` 消耗型内购由 **Apple StoreKit** 处理。
- **Siri / 快捷指令 / 控制中心** — 打开本机深链，不上传语料。
- **可选 Spotlight** — 在设置中开启后由系统本机索引；我们无搜索后端。

## 设备上存储的数据

| 数据 | 位置 | 用途 |
|------|------|------|
| 篇章语料库 | App / 小组件包 | 离线阅读与学堂 |
| 收藏与学单 | App Group UserDefaults | 星标与用户清单 |
| 阅读记录 / 上次阅读 | App Group UserDefaults | 继续阅读、历史界面 |
| 学堂进度与掌握度 | App Group UserDefaults | 品格学堂、测验/寻句 |
| 研习打卡连续 | App Group UserDefaults | 每日一学习惯 |
| 反思日记 | App Group UserDefaults | 人生指导日记 |
| 洒扫习惯打卡 | App Group UserDefaults | 人生指导微习惯 |
| 冥想连续与会话偏好 | App Group UserDefaults | 冥想统计 |
| 外观与阅读偏好 | App Group UserDefaults | 主题、强调色、语言、布局、TTS、Tab、小组件、字号 |
| 每日一学缓存与通知偏好 | App Group UserDefaults | 今日 ID、提醒时间 |
| 分享卡偏好 | App Group UserDefaults | 上次样式选择 |
| 引导与 TipKit 状态 | 标准 UserDefaults | 欢迎引导 |
| 主屏快捷操作 | 系统 + 本地偏好 | 你配置的快捷 |
| 小组件 / 实时活动快照 | App Group / ActivityKit | 你已打开内容的展示 |

卸载应用会移除与该应用关联的沙盒与 App Group 数据（以 iOS/macOS 行为为准）。可选 iCloud 副本留在**你的** iCloud 中，直至你关闭同步或在别处删除。

## iCloud 同步（可选）

在设置中开启 **iCloud 同步**后，应用通过 Apple **`NSUbiquitousKeyValueStore`**（绑定**你的 Apple ID**）镜像：

- 收藏
- 学单
- 阅读记录
- 学堂进度 / 掌握度
- 研习打卡连续
- 反思日记
- 习惯打卡历史

同步流量发往 **Apple iCloud**，而非 iHTC Studio。可在设置中关闭。我们无法读取你的 iCloud 内容。

## 权限

仅在功能需要时请求：

| 权限 | 何时 | 原因 |
|------|------|------|
| 通知 | 你开启每日一学或冥想提醒 | 本机调度 |
| 相册（仅添加） | 你保存分享卡 | 写入渲染图片 |
| iCloud | 你开启同步 | 同步收藏/学单/记录/进度/打卡/日记/习惯 |
| 实时活动（iOS） | 你开启品读或冥想实时活动 | 锁屏 / 灵动岛 |
| 后台音频 | 你开启后台诵读 | 后台继续 TTS |

我们**不**请求通讯录、精确位置、相机、麦克风（除系统 TTS 播放外）或追踪。

## 儿童隐私

本应用分级 **12+**，**非**儿童类别。我们不会有意收集儿童个人信息；应用无需账号。

## 第三方

正常使用中涉及的第三方仅为 **Apple**（App Store、iCloud、StoreKit、系统 TTS、通知、实时活动）。

## 保留与删除

- **本机：** 删除应用可移除本地数据。
- **iCloud：** 在设置中关闭同步，或在系统设置中管理 iCloud 存储。
- **我们不在服务器保留**你的阅读、日记或习惯数据副本。

## 政策变更

我们可能因法律、产品或 App Store 合规需要更新本页；「最近更新」日期会随之变更。继续使用即表示接受修订后的政策。

## 联系

隐私相关问题：[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>

<section lang="zh-TW" markdown="1">

**最近更新：** 2026 年 8 月 18 日

愛火腿腸工作室（iHTC Studio）（「我們」；原 iHTCTeam）開發了 **愛小學**（iPrimer，Bundle ID `com.iHTCboy.iPrimer`）。本隱私政策說明你在使用本應用時，資料如何被處理。本頁可作為 **App Store 審核**與使用者查閱的公開隱私政策地址。在 App Store Connect 填寫隱私政策 URL 時，請在瀏覽器中開啟本 [隱私政策](privacy) 頁，從網址列複製目前網址（公開站點網域日後可能變更）。

## 概要（對齊 App Store 隱私標籤）

| 主題 | 我們的做法 |
|------|------------|
| 帳號 | **不需要** |
| 愛火腿腸工作室的資料收集 | **不收集資料** |
| 網路 | 安裝後，語料、閱讀、誦讀、品格學堂、冥想、人生指導、小工具與每日通知可**離線** |
| 分析 / 廣告 / 追蹤 | **無** |
| 可選 Apple 服務 | **iCloud**、分享卡的**照片（僅加入）**、**StoreKit** 打賞、**本地通知**、可選**即時動態** |

## 資料收集

我們**不**為廣告或分析收集、出售或共享個人資訊。閱讀記錄、收藏、學單、反思日記、習慣打卡、冥想連續、學堂進度與偏好留在你的裝置（以及可選的**你的** iCloud），不會上傳到 iHTC Studio 伺服器。

## 應用如何工作

- **內建語料** — 篇章 JSON、白話/英文、集注、釋義、冥想引導與索引隨 App / 小工具安裝（由網絡公開資料梳理）。
- **本機朗讀** — 使用系統 TTS。
- **小工具與 App Group** — `group.com.iHTCboy.iPrimer` 本機共享。
- **每日通知** — 僅本機排程。
- **分享卡** — 本機渲染；**照片（僅加入）**。
- **可選打賞** — `com.iHTCboy.iPrimer.6` 由 Apple 處理。

## 裝置上儲存的資料

含篇章語料、收藏與學單、閱讀記錄、學堂進度、研習打卡、反思日記、灑掃習慣打卡、冥想連續、外觀與閱讀偏好、每日一學快取、分享卡偏好、引導狀態、主屏快捷與小工具/即時活動快照（詳見英文版表格）。

## iCloud 同步（可選）

可同步：收藏、學單、閱讀記錄、學堂進度/掌握度、研習打卡、反思日記、習慣打卡歷史。流量走 **Apple iCloud**。

## 權限

通知、照片（僅加入）、iCloud、即時活動、背景音訊——僅在對應功能開啟時使用。不請求通訊錄、精確位置、相機、麥克風（除系統 TTS）或追蹤。

## 兒童隱私

分級 **12+**，**非**兒童類別；無需帳號。

## 第三方

僅 **Apple** 系統服務。

## 保留與刪除

刪除應用可移除本機資料；iCloud 可在設定中關閉。我們不在伺服器保留你的資料副本。

## 政策變更

「最近更新」日期會隨修訂變更。

## 聯絡

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
