---
layout: doc
title: iCouplet — Privacy Policy
app_id: iCouplet
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iCouplet (爱对联) — fully offline couplet app, Data Not Collected, optional iCloud and Photo Library add-only.
---

<section lang="en" markdown="1">

**Last updated:** July 23, 2026

iHTC Studio ("we", "us" or "our"; formerly iHTCTeam) built **iCouplet** (also known as "爱对联" / "愛對聯", Bundle ID `com.iHTCboy.iCouplet`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on this page as the public privacy URL.

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration, email sign-in, or phone number |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your personal data |
| Network | Couplet library, reading, recite, study, widgets, and daily notifications work **offline** after install |
| Analytics / ads / tracking | **None** — no third-party analytics, advertising, or tracking SDKs; no App Tracking Transparency use |
| Optional Apple services | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities** |

## Data Collection

We do **not** collect, sell, or share personal information for advertising or analytics.

- **No account** — You can use all core features without creating an account with us.
- **No analytics or ads** — The app binary does not integrate third-party analytics, advertising, or crash-reporting SDKs that phone home to us.
- **No couplet content upload** — Your reading history, favorites, notes-like progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## How the App Works

- **Bundled library** — Couplet JSON and indexes ship inside the app / widget bundle. Browsing and study do not require a network request.
- **On-device speech** — Recitation uses Apple’s on-device / system **AVSpeechSynthesizer** (TTS). We do not send couplet text to iHTC Studio.
- **Widgets & App Group** — Widgets and the app share preferences and lightweight state via App Group `group.com.iHTCboy.iCouplet` on your device.
- **Daily notifications** — Scheduled locally with User Notifications. Tapping a notification opens a deep link to a couplet ID on device; no server fan-out.
- **Share cards** — Images are rendered on device. Saving uses **Photo Library add-only** only when you tap save. System Share Sheet may send the image to an app **you** choose; that destination’s privacy policy then applies.
- **Optional tip** — “Tip Developer” is a consumable **StoreKit** purchase processed by Apple. We do not receive your payment card details.

## Data Stored on Your Device

| Data | Where | Purpose |
|------|-------|---------|
| Couplet database | App / Widget bundle | Offline reading & study |
| Favorites & couplet lists | App Group UserDefaults | Starred works and user lists |
| Reading history / last read | App Group UserDefaults | Continue reading, history UI |
| Study progress & mastery | App Group UserDefaults | 4-level mastery, quiz state |
| Streak / check-in | App Group UserDefaults | Learning streaks |
| Appearance & reading prefs | App Group UserDefaults | Theme, accent, language, layout, TTS, tabs, widgets |
| Daily couplet cache & notification prefs | App Group UserDefaults | Today’s ID, schedule time, contextual toggle |
| Share-card preferences | App Group UserDefaults | Last style / ratio choices |
| Onboarding & TipKit state | Standard UserDefaults (device) | Welcome guide / discovery tips |
| Home Screen quick actions | System + local prefs | Up to 4 shortcuts you configure |
| Widget / Live Activity snapshots | App Group / ActivityKit | Display text you already opened |

Uninstalling the app removes sandbox and App Group data associated with the app (subject to iOS/macOS behavior). Optional iCloud copies remain in **your** iCloud until you clear them or turn sync off and delete elsewhere.

## iCloud Sync (Optional)

If you enable **iCloud Sync** in Settings, the app mirrors selected user data through Apple’s **`NSUbiquitousKeyValueStore`** tied to **your Apple ID**:

- Favorites
- Couplet lists
- Reading history
- Study progress / mastery
- Streak days

Sync traffic goes to **Apple iCloud**, not to iHTC Studio. You can disable sync in Settings. We cannot read your iCloud contents.

## Permissions

iCouplet requests permissions only when a feature needs them:

| Permission | When | Why |
|------------|------|-----|
| Notifications | You enable Daily Couplet reminders | Local scheduling of reminder notifications |
| Photo Library (Add Only) | You save a share card | Write the rendered image; we do not need full library read access |
| iCloud | You enable sync | Sync favorites / lists / history / progress / streaks |
| Live Activities (iOS) | You enable Reading Live Activity | Show the couplet you are reading on Lock Screen / Dynamic Island |
| Background audio (capability) | You enable background recitation | Continue TTS when the app is not foreground |

We do **not** request Contacts, precise Location, Camera, Microphone (beyond system TTS playback), or Tracking.

## Children’s Privacy

iCouplet does not knowingly collect personal data from anyone, including children under 13 (or the equivalent age in your region). Because we do not operate a data-collection backend, there is no child profile stored with us.

## Third Parties

- **Apple** — App Store distribution, optional StoreKit purchases, optional iCloud KVS, system TTS, Share Sheet destinations you pick, and OS-level notification / Live Activity delivery.
- **No other third-party SDKs** for ads, analytics, or social login are included for data collection.

## International Users

The app is designed to function offline on your device. Optional Apple services follow Apple’s terms and regional availability.

## Changes to This Policy

We may update this Privacy Policy from time to time. The “Last updated” date at the top will change, and the revised policy will be posted on this Privacy Policy page.

## Contact Us

If you have questions about this Privacy Policy or privacy practices:

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

We typically respond within 48 hours.

</section>

<section lang="zh-CN" markdown="1">

**最近更新：** 2026 年 7 月 23 日

爱火腿肠工作室（iHTC Studio）（「我们」；原 iHTCTeam）开发了 **爱对联**（iCouplet / 愛對聯，Bundle ID `com.iHTCboy.iCouplet`）。本隐私政策说明你在使用本应用时，数据如何被处理（以及**不会**如何被处理）。本页可作为 **App Store 审核**与用户查阅的公开隐私政策地址。

## 概要（对齐 App Store 隐私标签）

| 主题 | 我们的做法 |
|------|------------|
| 账号 | **不需要**——无需注册、邮箱登录或手机号 |
| iHTC Studio 收集数据 | **不收集数据（Data Not Collected）**——我们**不**运营接收你个人数据的后端 |
| 网络 | 对联库、阅读、诵联、对课、小组件与每日通知在安装后可**离线**使用 |
| 分析 / 广告 / 追踪 | **无**——无第三方分析、广告或追踪 SDK；不使用跨 App 追踪 |
| 可选的 Apple 服务 | **iCloud**（你的私有键值存储）、联卡**相册（仅添加）**、打赏用的 **StoreKit**、**本地通知**、可选**实时活动** |

## 数据收集

我们**不**出于广告或分析目的收集、出售或共享个人信息。

- **无账号** — 无需在我们这边创建账户即可使用核心功能。
- **无分析与广告** — 应用未集成会向我们回传数据的第三方分析、广告或崩溃统计 SDK。
- **无对联内容上传** — 浏览记录、收藏、学习进度与偏好保存在你的设备（以及可选的**你的** iCloud）。它们不会上传到 iHTC Studio 服务器——因为**本应用不为此运营此类服务器**。

## 应用工作原理

- **内置语料** — 对联 JSON 与索引随 App / Widget 安装包提供，浏览与对课无需联网。
- **本机语音合成** — 诵联使用系统 **AVSpeechSynthesizer**，我们不会把联句发送到 iHTC Studio。
- **小组件与 App Group** — App 与小组件通过本机 App Group `group.com.iHTCboy.iCouplet` 共享偏好与轻量状态。
- **每日通知** — 使用本地用户通知调度；点击后通过深链打开本机对联，无服务器推送内容库。
- **联卡分享** — 图片在设备上渲染。仅当你点「保存」时请求**相册仅添加**权限。系统分享会把图片交给**你选择**的目标 App，此后适用该目标的隐私政策。
- **可选打赏** — 「打赏开发者」为 Apple **StoreKit** 消耗型内购，由 Apple 处理支付；我们不会收到你的银行卡信息。

## 设备本地存储

| 数据 | 位置 | 用途 |
|------|------|------|
| 对联数据库 | App / Widget Bundle | 离线阅读与对课 |
| 收藏与联单 | App Group UserDefaults | 星标与自定义联单 |
| 浏览记录 / 最近阅读 | App Group UserDefaults | 继续阅读与历史 |
| 学习进度与掌握度 | App Group UserDefaults | 四级掌握度与测验状态 |
| 打卡连续 | App Group UserDefaults | 学习连续天数 |
| 外观与阅读偏好 | App Group UserDefaults | 主题、强调色、语言、布局、诵联、Tab、小组件 |
| 每日一联缓存与通知偏好 | App Group UserDefaults | 今日 ID、提醒时间、情境开关 |
| 联卡偏好 | App Group UserDefaults | 上次风格 / 比例 |
| 引导与 TipKit 状态 | 标准 UserDefaults | 欢迎引导 / 发现提示 |
| 主屏快捷 | 系统 + 本机偏好 | 你配置的最多 4 项 |
| 小组件 / 实时活动快照 | App Group / ActivityKit | 展示你正在阅读的内容 |

卸载应用会按系统规则删除沙盒与相关 App Group 数据。可选 iCloud 副本仍留在**你的** iCloud，直到你清理或关闭同步。

## iCloud 同步（可选）

若在设置中开启 **iCloud 同步**，应用通过绑定**你的 Apple ID** 的 **`NSUbiquitousKeyValueStore`** 镜像下列用户数据：

- 收藏
- 联单
- 浏览记录
- 学习进度 / 掌握度
- 打卡天数

同步流量通往 **Apple iCloud**，不经过 iHTC Studio。可在设置中关闭。我们无法读取你的 iCloud 内容。

## 权限说明

仅在功能需要时请求：

| 权限 | 时机 | 原因 |
|------|------|------|
| 通知 | 你开启每日一联提醒 | 本地调度提醒 |
| 相册（仅添加） | 你保存联卡 | 写入渲染图片；无需读取全部相册 |
| iCloud | 你开启同步 | 同步收藏 / 联单 / 历史 / 进度 / 打卡 |
| 实时活动（iOS） | 你开启品联实时活动 | 在锁屏 / 灵动岛显示正在品读的联 |
| 后台音频能力 | 你开启后台诵联 | App 不在前台时继续 TTS |

我们**不**请求通讯录、精确位置、相机、麦克风（除系统 TTS 播放外）或追踪权限。

## 儿童隐私

爱对联不会故意收集包括 13 岁以下（或你所在地区同等年龄）儿童在内的任何人的个人数据。由于我们不运营数据收集后端，我们这边不会保存儿童档案。

## 第三方

- **Apple** — App Store 分发、可选 StoreKit 购买、可选 iCloud、系统 TTS、你选择的分享目标，以及系统通知 / 实时活动投递。
- **无其他**用于广告、分析或社交登录的第三方数据收集 SDK。

## 政策变更

我们可能不时更新本政策。页首「最近更新」日期会随之变化，修订版将发布于本隐私政策页面。

## 联系我们

如对隐私政策有疑问：

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

我们通常在 48 小时内回复。

</section>

<section lang="zh-TW" markdown="1">

**最近更新：** 2026 年 7 月 23 日

愛火腿腸工作室（iHTC Studio）（「我們」；原 iHTCTeam）開發了 **愛對聯**（iCouplet / 爱对联，Bundle ID `com.iHTCboy.iCouplet`）。本隱私政策說明你在使用本應用時，資料如何被處理（以及**不會**如何被處理）。本頁可作為 **App Store 審核**與使用者查閱的公開隱私政策地址。

## 概要（對齊 App Store 隱私標籤）

| 主題 | 我們的做法 |
|------|------------|
| 帳號 | **不需要**——無需註冊、電子郵件登入或手機號碼 |
| iHTC Studio 收集資料 | **不收集資料（Data Not Collected）**——我們**不**營運接收你個人資料的後端 |
| 網路 | 對聯庫、閱讀、誦聯、對課、小工具與每日通知在安裝後可**離線**使用 |
| 分析 / 廣告 / 追蹤 | **無**——無第三方分析、廣告或追蹤 SDK；不使用跨 App 追蹤 |
| 可選的 Apple 服務 | **iCloud**（你的私有鍵值儲存）、聯卡**照片（僅加入）**、打賞用的 **StoreKit**、**本地通知**、可選**即時動態** |

## 資料收集

我們**不**出於廣告或分析目的收集、出售或共享個人資訊。

- **無帳號** — 無需在我們這邊建立帳戶即可使用核心功能。
- **無分析與廣告** — 應用未整合會向我們回傳資料的第三方分析、廣告或當機統計 SDK。
- **無對聯內容上傳** — 瀏覽紀錄、收藏、學習進度與偏好保存在你的裝置（以及可選的**你的** iCloud）。它們不會上傳到 iHTC Studio 伺服器——因為**本應用不為此營運此類伺服器**。

## 應用工作原理

- **內建語料** — 對聯 JSON 與索引隨 App / Widget 安裝包提供，瀏覽與對課無需連網。
- **本機語音合成** — 誦聯使用系統 **AVSpeechSynthesizer**，我們不會把聯句傳送到 iHTC Studio。
- **小工具與 App Group** — App 與小工具透過本機 App Group `group.com.iHTCboy.iCouplet` 共享偏好與輕量狀態。
- **每日通知** — 使用本地使用者通知排程；點擊後透過深鏈開啟本機對聯，無伺服器推播內容庫。
- **聯卡分享** — 圖片在裝置上渲染。僅當你點「儲存」時請求**照片僅加入**權限。系統分享會把圖片交給**你選擇**的目標 App，此後適用該目標的隱私政策。
- **可選打賞** — 「打賞開發者」為 Apple **StoreKit** 消耗型內購，由 Apple 處理付款；我們不會收到你的银行卡／信用卡資訊。

## 裝置本機儲存

| 資料 | 位置 | 用途 |
|------|------|------|
| 對聯資料庫 | App / Widget Bundle | 離線閱讀與對課 |
| 收藏與聯單 | App Group UserDefaults | 星號與自訂聯單 |
| 瀏覽紀錄 / 最近閱讀 | App Group UserDefaults | 繼續閱讀與歷史 |
| 學習進度與掌握度 | App Group UserDefaults | 四級掌握度與測驗狀態 |
| 打卡連續 | App Group UserDefaults | 學習連續天數 |
| 外觀與閱讀偏好 | App Group UserDefaults | 主題、強調色、語言、版面、誦聯、Tab、小工具 |
| 每日一聯快取與通知偏好 | App Group UserDefaults | 今日 ID、提醒時間、情境開關 |
| 聯卡偏好 | App Group UserDefaults | 上次風格 / 比例 |
| 引導與 TipKit 狀態 | 標準 UserDefaults | 歡迎引導 / 發現提示 |
| 主畫面捷徑 | 系統 + 本機偏好 | 你設定的最多 4 項 |
| 小工具 / 即時動態快照 | App Group / ActivityKit | 展示你正在閱讀的內容 |

解除安裝應用會依系統規則刪除沙盒與相關 App Group 資料。可選 iCloud 副本仍留在**你的** iCloud，直到你清理或關閉同步。

## iCloud 同步（可選）

若在設定中開啟 **iCloud 同步**，應用透過綁定**你的 Apple ID** 的 **`NSUbiquitousKeyValueStore`** 鏡像下列使用者資料：

- 收藏
- 聯單
- 瀏覽紀錄
- 學習進度 / 掌握度
- 打卡天數

同步流量通往 **Apple iCloud**，不經過 iHTC Studio。可在設定中關閉。我們無法讀取你的 iCloud 內容。

## 權限說明

僅在功能需要時請求：

| 權限 | 時機 | 原因 |
|------|------|------|
| 通知 | 你開啟每日一聯提醒 | 本地排程提醒 |
| 照片（僅加入） | 你儲存聯卡 | 寫入渲染圖片；無需讀取全部照片 |
| iCloud | 你開啟同步 | 同步收藏 / 聯單 / 歷史 / 進度 / 打卡 |
| 即時動態（iOS） | 你開啟品聯即時動態 | 在鎖定畫面 / 動態島顯示正在品讀的聯 |
| 背景音訊能力 | 你開啟背景誦聯 | App 不在前景時繼續 TTS |

我們**不**請求通訊錄、精確位置、相機、麥克風（除系統 TTS 播放外）或追蹤權限。

## 兒童隱私

愛對聯不會故意收集包括 13 歲以下（或你所在地區同等年齡）兒童在內的任何人的個人資料。由於我們不營運資料收集後端，我們這邊不會保存兒童檔案。

## 第三方

- **Apple** — App Store 分發、可選 StoreKit 購買、可選 iCloud、系統 TTS、你選擇的分享目標，以及系統通知 / 即時動態投遞。
- **無其他**用於廣告、分析或社交登入的第三方資料收集 SDK。

## 政策變更

我們可能不時更新本政策。頁首「最近更新」日期會隨之變化，修訂版將發佈於本隱私政策頁面。

## 聯絡我們

如對隱私政策有疑問：

- **電子郵件：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

我們通常在 48 小時內回覆。

</section>
