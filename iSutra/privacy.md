---
layout: doc
title: iSutra — Privacy Policy
app_id: iSutra
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iSutra (爱佛经) — fully offline Buddhist sutra app, Data Not Collected, optional iCloud and Photo Library add-only.
---

<section lang="en" markdown="1">

**Last updated:** August 18, 2026

iHTC Studio ("we", "us" or "our"; formerly iHTCTeam) built **iSutra** (also known as "爱佛经" / "愛佛經", Bundle ID `com.iHTCboy.iSutra`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on **this page** as the public privacy policy for the app. For App Store Connect, open this Privacy Policy in your browser and copy the address from the address bar (the public site domain may change over time).

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration, email sign-in, or phone number |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your personal data |
| Network | Library, reading, recite, Study Hall, Hunt, chant, practice, widgets, and daily notifications work **offline** after install |
| Analytics / ads / tracking | **None** — no third-party analytics, advertising, or tracking SDKs; no App Tracking Transparency use |
| Optional Apple services | **iCloud** (your private KVS), **Photo Library (Add Only)** for Dharma cards / exports, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default) |

## Data Collection

We do **not** collect, sell, or share personal information for advertising or analytics.

- **No account** — You can use all core features without creating an account with us.
- **No analytics or ads** — The app binary does not integrate third-party analytics, advertising, or crash-reporting SDKs that phone home to us.
- **No content upload** — Your reading history, favorites, lists, notes, mastery, streaks, chant counts, practice checklists, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## How the App Works

- **Bundled library** — Sutra JSON indexes, shards, large volumes, vernacular, English, famous lines, and indexes ship inside the app / widget bundle. Browsing and study do not require a network request.
- **On-device speech** — Recitation uses Apple’s system **AVSpeechSynthesizer** (TTS). We do not send sutra text to iHTC Studio.
- **Widgets & App Group** — Widgets and the app share preferences and lightweight state via App Group `group.com.iHTCboy.iSutra` on your device.
- **Daily notifications** — Scheduled locally with User Notifications. Tapping a notification opens a deep link to a passage ID on device; no server fan-out.
- **Dharma cards / exports** — Images and PDFs are rendered on device. Saving uses **Photo Library add-only** only when you tap save. System Share Sheet may send the file to an app **you** choose; that destination’s privacy policy then applies.
- **Copy-sutra (iOS)** — PencilKit strokes are stored under Application Support on the device (`CopySutra/…`) for drafts and export. They are **not** placed in the App Group and are **not** synced to iCloud.
- **Optional tip** — “Tip Developer” is a consumable **StoreKit** purchase processed by Apple. We do not receive your payment card details.
- **Siri / Shortcuts / Control Center** — Optional system integrations open on-device deep links; they do not send your library to us.
- **Optional Spotlight** — Off by default. If you enable indexing, content is indexed by the system on device for local search; we do not operate a search backend.

## Data Stored on Your Device

| Data | Where | Purpose |
|------|-------|---------|
| Sutra database (indexes, shards, large volumes) | App / Widget bundle | Offline reading & study |
| Favorites & lists (经单) | App Group UserDefaults | Starred passages and user lists |
| Reading history / last read | App Group UserDefaults | Continue reading, history UI |
| Study progress & mastery | App Group UserDefaults | Study Hall state, quiz / Hunt progress |
| Notes | App Group UserDefaults | Passage notes you write |
| Practice streak / check-in | App Group UserDefaults | Daily habit |
| Chant counts & sound prefs | App Group UserDefaults | Wooden-fish totals, goals, tones |
| Morning / evening practice & dedication | App Group UserDefaults | Daily liturgy checklist |
| Appearance & reading prefs | App Group UserDefaults | Theme, accent, language, layout, TTS, tabs, widgets |
| Daily Sutra cache & notification prefs | App Group UserDefaults | Today’s ID, schedule time |
| Share-card preferences | App Group UserDefaults | Last style / ratio choices |
| Copy-sutra drawings (iOS) | Application Support (`CopySutra/`) | Per-line tracing drafts |
| Onboarding & TipKit state | Standard UserDefaults (device) | Welcome guide / discovery tips |
| Home Screen quick actions | System + local prefs | Shortcuts you configure |
| Widget / Live Activity snapshots | App Group / ActivityKit | Display text / chant state you already opened |

Uninstalling the app removes sandbox and App Group data associated with the app (subject to iOS/macOS behavior). Optional iCloud copies remain in **your** iCloud until you clear them or turn sync off and delete elsewhere.

## iCloud Sync (Optional)

If you enable **iCloud Sync** in Settings, the app mirrors selected user data through Apple’s **`NSUbiquitousKeyValueStore`** tied to **your Apple ID** (favorites, lists, history, mastery, notes, chant preferences, practice configuration, and related progress). Sync traffic goes to **Apple iCloud**, not to iHTC Studio. Copy-sutra drawings are **not** included. You can disable sync in Settings. We cannot read your iCloud contents.

## Permissions

iSutra requests permissions only when a feature needs them:

| Permission | When | Why |
|------------|------|-----|
| Notifications | You enable Daily Sutra reminders | Local scheduling of reminder notifications |
| Photo Library (Add Only) | You save a Dharma card or export | Write the rendered image / PDF; we do not need full library read access |
| iCloud | You enable sync | Sync favorites / lists / history / mastery / notes / chant & practice prefs |
| Live Activities (iOS) | You enable Reading or Chant Live Activity | Show reading / chant progress on Lock Screen / Dynamic Island |
| Background audio (capability) | You enable background recitation | Continue TTS when the app is not foreground |

We do **not** request Contacts, precise Location, Camera, Microphone (beyond system TTS playback), or Tracking.

## What We Do Not Do

- We do **not** sell personal data.
- We do **not** build advertising profiles.
- We do **not** require an account or social login.
- We do **not** embed third-party ad, analytics, or social SDKs for data collection.
- We do **not** access your Photo Library beyond **add-only** when you choose to save.
- We do **not** receive StoreKit payment card numbers (Apple processes payments).
- We do **not** turn religious content into fortune-telling or paid blessing commerce.

## Children’s Privacy

iSutra does not knowingly collect personal data from anyone, including children under 13 (or the equivalent age in your region). Because we do not operate a data-collection backend, there is no child profile stored with us. Families may use the reading and practice features offline on their own devices.

## Third Parties

- **Apple** — App Store distribution, optional StoreKit purchases, optional iCloud KVS, system TTS, Share Sheet destinations you pick, and OS-level notification / Live Activity / Siri / Shortcuts delivery.
- **No other third-party SDKs** for ads, analytics, or social login are included for data collection.

## International Users

The app is designed to function offline on your device. Optional Apple services follow Apple’s terms and regional availability.

## Data Retention & Deletion

- **On device** — Local preferences and progress remain until you clear them in-app (where available), reset the device, or uninstall the app.
- **iCloud (optional)** — Data you synced remains in **your** iCloud account under Apple’s policies until you disable sync and/or clear it through Apple’s tools.
- **iHTC Studio** — Because we do not collect personal data on our servers, there is no account dataset for us to delete on request beyond answering your email questions.

## Changes to This Policy

We may update this Privacy Policy from time to time. The “Last updated” date at the top will change, and the revised policy will be posted on this Privacy Policy page.

## Contact Us

If you have questions about this Privacy Policy or privacy practices:

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

We typically respond within 48 hours.

</section>

<section lang="zh-CN" markdown="1">

**最近更新：** 2026 年 8 月 18 日

爱火腿肠工作室（iHTC Studio）（「我们」；原 iHTCTeam）开发了 **爱佛经**（iSutra / 愛佛經，Bundle ID `com.iHTCboy.iSutra`）。本隐私政策说明你在使用本应用时，数据如何被处理（以及**不会**如何被处理）。本页可作为 **App Store 审核**与用户查阅的公开隐私政策。填写 App Store Connect 时，请在浏览器打开本隐私政策页，从地址栏复制当前网址（站点域名日后可能变更，请勿依赖文档中的固定域名）。

## 概要（对齐 App Store 隐私标签）

| 主题 | 我们的做法 |
|------|------------|
| 账号 | **不需要**——无需注册、邮箱登录或手机号 |
| iHTC Studio 收集数据 | **不收集数据（Data Not Collected）**——我们**不**运营接收你个人数据的后端 |
| 网络 | 语料、阅读、诵经、持诵学堂、寻经、念诵、功课、小组件与每日通知在安装后可**离线**使用 |
| 分析 / 广告 / 追踪 | **无**——无第三方分析、广告或追踪 SDK；不使用跨 App 追踪 |
| 可选的 Apple 服务 | **iCloud**（你的私有键值存储）、法卡 / 导出的**相册（仅添加）**、打赏用的 **StoreKit**、**本地通知**、可选**实时活动**、可选 **Spotlight**（默认关闭） |

## 数据收集

我们**不**出于广告或分析目的收集、出售或共享个人信息。

- **无账号** — 无需在我们这边创建账户即可使用核心功能。
- **无分析与广告** — 应用未集成会向我们回传数据的第三方分析、广告或崩溃统计 SDK。
- **无内容上传** — 浏览记录、收藏、经单、笔记、掌握度、打卡、念诵计数、功课清单与偏好保存在你的设备（以及可选的**你的** iCloud）。它们不会上传到 iHTC Studio 服务器——因为**本应用不为此运营此类服务器**。

## 应用工作原理

- **内置语料** — 经文索引、分片、大部头、白话、英译、法语与索引随 App / Widget 安装包提供，浏览与学堂无需联网。
- **本机语音合成** — 诵经使用系统 **AVSpeechSynthesizer**，我们不会把正文发送到 iHTC Studio。
- **小组件与 App Group** — App 与小组件通过本机 App Group `group.com.iHTCboy.iSutra` 共享偏好与轻量状态。
- **每日通知** — 使用本地用户通知调度；点击后通过深链打开本机经目，无服务器推送内容库。
- **法卡 / 导出** — 图片与 PDF 在设备上渲染。仅当你点「保存」时请求**相册仅添加**权限。系统分享会把文件交给**你选择**的目标 App。
- **抄经（iOS）** — PencilKit 笔迹保存在本机 Application Support（`CopySutra/…`），用于存稿与导出；**不**进入 App Group，也**不**同步到 iCloud。
- **可选打赏** — 「打赏开发者」为 Apple **StoreKit** 消耗型内购，由 Apple 处理支付；我们不会收到你的银行卡信息。
- **Siri / 快捷指令 / 控制中心** — 可选系统能力通过本机深链打开功能，不会把语料库发送给我们。
- **可选 Spotlight** — **默认关闭**。若你开启索引，由系统在本机建立搜索索引；我们不运营搜索后端。

## 设备本地存储

| 数据 | 位置 | 用途 |
|------|------|------|
| 经文语料（索引 / 分片 / 大部） | App / Widget Bundle | 离线阅读与学堂 |
| 收藏与经单 | App Group UserDefaults | 星标与自定义经单 |
| 浏览记录 / 最近阅读 | App Group UserDefaults | 继续阅读与历史 |
| 学堂进度与掌握度 | App Group UserDefaults | 持诵学堂状态、测验 / 寻经进度 |
| 笔记 | App Group UserDefaults | 你写下的经文笔记 |
| 打卡 / 连续天数 | App Group UserDefaults | 每日习惯 |
| 念诵计数与音色偏好 | App Group UserDefaults | 木鱼累计、目标、音色 |
| 早 / 晚功课与回向 | App Group UserDefaults | 功课清单 |
| 外观与阅读偏好 | App Group UserDefaults | 主题、强调色、语言、布局、TTS、Tab、小组件 |
| 今日一经缓存与通知偏好 | App Group UserDefaults | 今日 ID、提醒时间 |
| 法卡偏好 | App Group UserDefaults | 上次风格 / 比例 |
| 抄经笔迹（iOS） | Application Support（`CopySutra/`） | 按句描红存稿 |
| 引导与 TipKit 状态 | 标准 UserDefaults | 欢迎引导 / 发现提示 |
| 主屏快捷 | 系统 + 本机偏好 | 你配置的快捷项 |
| 小组件 / 实时活动快照 | App Group / ActivityKit | 展示你正在阅读 / 念诵的内容 |

卸载应用会按系统规则删除沙盒与相关 App Group 数据。可选 iCloud 副本仍留在**你的** iCloud，直到你清理或关闭同步。

## iCloud 同步（可选）

若在设置中开启 **iCloud 同步**，应用通过绑定**你的 Apple ID** 的 **`NSUbiquitousKeyValueStore`** 镜像收藏、经单、浏览记录、掌握度、笔记、念诵偏好、功课配置及相关进度。同步流量通往 **Apple iCloud**，不经过 iHTC Studio。**抄经笔迹不同步**。可在设置中关闭。我们无法读取你的 iCloud 内容。

## 权限说明

仅在功能需要时请求：

| 权限 | 时机 | 原因 |
|------|------|------|
| 通知 | 你开启今日一经提醒 | 本地调度提醒 |
| 相册（仅添加） | 你保存法卡或导出 | 写入渲染图片 / PDF；无需读取全部相册 |
| iCloud | 你开启同步 | 同步收藏 / 经单 / 历史 / 掌握度 / 笔记 / 念诵与功课偏好 |
| 实时活动（iOS） | 你开启品读或念诵实时活动 | 在锁屏 / 灵动岛显示进度 |
| 后台音频能力 | 你开启后台诵经 | App 不在前台时继续 TTS |

我们**不**请求通讯录、精确位置、相机、麦克风（除系统 TTS 播放外）或追踪权限。

## 我们明确不做的事

- **不**出售个人数据。
- **不**构建广告画像。
- **不**要求账号或社交登录。
- **不**嵌入用于数据收集的第三方广告、分析或社交 SDK。
- **不**在你主动保存之外访问相册（且仅为「添加」）。
- **不**接收 StoreKit 银行卡号（由 Apple 处理支付）。
- **不**把宗教内容做成算命 / 祈福求财的商业化产品。

## 儿童隐私

爱佛经不会故意收集包括 13 岁以下（或你所在地区同等年龄）儿童在内的任何人的个人数据。由于我们不运营数据收集后端，我们这边不会保存儿童档案。家庭可在自有设备上离线使用阅读与修习功能。

## 第三方

- **Apple** — App Store 分发、可选 StoreKit 购买、可选 iCloud、系统 TTS、你选择的分享目标，以及系统通知 / 实时活动 / Siri / 快捷指令投递。
- **无其他**用于广告、分析或社交登录的第三方数据收集 SDK。

## 国际用户

应用设计为在你的设备上离线运行。可选 Apple 服务遵循 Apple 条款与地区可用性。

## 数据保留与删除

- **本机** — 偏好与进度保留至你在应用内清除（如有入口）、重置设备或卸载应用。
- **iCloud（可选）** — 你同步的数据按 Apple 政策留在**你的** iCloud，直到关闭同步并/或通过 Apple 工具清理。
- **iHTC Studio** — 我们不在自有服务器收集个人数据，因此没有可供删除的账号数据集；隐私疑问可通过邮件联系。

## 政策变更

我们可能不时更新本政策。页首「最近更新」日期会随之变化，修订版将发布于本隐私政策页面。

## 联系我们

如对隐私政策有疑问：

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

我们通常在 48 小时内回复。

</section>

<section lang="zh-TW" markdown="1">

**最近更新：** 2026 年 8 月 18 日

愛火腿腸工作室（iHTC Studio）（「我們」；原 iHTCTeam）開發了 **愛佛經**（iSutra / 爱佛经，Bundle ID `com.iHTCboy.iSutra`）。本隱私政策說明你在使用本應用時，資料如何被處理（以及**不會**如何被處理）。本頁可作為 **App Store 審核**與使用者查閱的公開隱私政策。填寫 App Store Connect 時，請在瀏覽器開啟本隱私政策頁，從網址列複製目前網址（網站網域日後可能變更，請勿依賴文件中的固定網域）。

## 概要（對齊 App Store 隱私標籤）

| 主題 | 我們的做法 |
|------|------------|
| 帳號 | **不需要**——無需註冊、電子郵件登入或手機號碼 |
| iHTC Studio 收集資料 | **不收集資料（Data Not Collected）**——我們**不**營運接收你個人資料的後端 |
| 網路 | 語料、閱讀、誦經、持誦學堂、尋經、念誦、功課、小工具與每日通知在安裝後可**離線**使用 |
| 分析 / 廣告 / 追蹤 | **無**——無第三方分析、廣告或追蹤 SDK；不使用跨 App 追蹤 |
| 可選的 Apple 服務 | **iCloud**（你的私有鍵值儲存）、法卡 / 匯出的**照片（僅加入）**、打賞用的 **StoreKit**、**本地通知**、可選**即時動態**、可選 **Spotlight**（預設關閉） |

## 資料收集

我們**不**出於廣告或分析目的收集、出售或共享個人資訊。

- **無帳號** — 無需在我們這邊建立帳戶即可使用核心功能。
- **無分析與廣告** — 應用未整合會向我們回傳資料的第三方分析、廣告或當機統計 SDK。
- **無內容上傳** — 瀏覽記錄、收藏、經單、筆記、掌握度、打卡、念誦計數、功課清單與偏好保存在你的裝置（以及可選的**你的** iCloud）。它們不會上傳到 iHTC Studio 伺服器——因為**本應用不為此營運此類伺服器**。

## 應用工作原理

- **內建語料** — 經文索引、分片、大部頭、白話、英譯、法語與索引隨 App / Widget 安裝包提供，瀏覽與學堂無需連網。
- **本機語音合成** — 誦經使用系統 **AVSpeechSynthesizer**，我們不會把正文傳送到 iHTC Studio。
- **小工具與 App Group** — App 與小工具透過本機 App Group `group.com.iHTCboy.iSutra` 共享偏好與輕量狀態。
- **每日通知** — 使用本地使用者通知排程；點擊後透過深鏈開啟本機經目，無伺服器推播內容庫。
- **法卡 / 匯出** — 圖片與 PDF 在裝置上渲染。僅當你點「儲存」時請求**照片僅加入**權限。系統分享會把檔案交給**你選擇**的目標 App。
- **抄經（iOS）** — PencilKit 筆跡保存在本機 Application Support（`CopySutra/…`），用於存稿與匯出；**不**進入 App Group，也**不**同步到 iCloud。
- **可選打賞** — 「打賞開發者」為 Apple **StoreKit** 消耗型內購，由 Apple 處理付款；我們不會收到你的銀行卡／信用卡資訊。
- **Siri / 捷徑 / 控制中心** — 可選系統能力透過本機深鏈開啟功能，不會把語料庫傳送給我們。
- **可選 Spotlight** — **預設關閉**。若你開啟索引，由系統在本機建立搜尋索引；我們不營運搜尋後端。

## 裝置本機儲存

| 資料 | 位置 | 用途 |
|------|------|------|
| 經文語料（索引 / 分片 / 大部） | App / Widget Bundle | 離線閱讀與學堂 |
| 收藏與經單 | App Group UserDefaults | 星號與自訂經單 |
| 瀏覽記錄 / 最近閱讀 | App Group UserDefaults | 繼續閱讀與歷史 |
| 學堂進度與掌握度 | App Group UserDefaults | 持誦學堂狀態、測驗 / 尋經進度 |
| 筆記 | App Group UserDefaults | 你寫下的經文筆記 |
| 打卡 / 連續天數 | App Group UserDefaults | 每日習慣 |
| 念誦計數與音色偏好 | App Group UserDefaults | 木魚累計、目標、音色 |
| 早 / 晚功課與回向 | App Group UserDefaults | 功課清單 |
| 外觀與閱讀偏好 | App Group UserDefaults | 主題、強調色、語言、版面、TTS、Tab、小工具 |
| 今日一經快取與通知偏好 | App Group UserDefaults | 今日 ID、提醒時間 |
| 法卡偏好 | App Group UserDefaults | 上次風格 / 比例 |
| 抄經筆跡（iOS） | Application Support（`CopySutra/`） | 按句描紅存稿 |
| 引導與 TipKit 狀態 | 標準 UserDefaults | 歡迎引導 / 發現提示 |
| 主畫面捷徑 | 系統 + 本機偏好 | 你設定的捷徑 |
| 小工具 / 即時動態快照 | App Group / ActivityKit | 展示你正在閱讀 / 念誦的內容 |

解除安裝應用會依系統規則刪除沙盒與相關 App Group 資料。可選 iCloud 副本仍留在**你的** iCloud，直到你清理或關閉同步。

## iCloud 同步（可選）

若在設定中開啟 **iCloud 同步**，應用透過綁定**你的 Apple ID** 的 **`NSUbiquitousKeyValueStore`** 鏡像收藏、經單、瀏覽記錄、掌握度、筆記、念誦偏好、功課設定及相關進度。同步流量通往 **Apple iCloud**，不經過 iHTC Studio。**抄經筆跡不同步**。可在設定中關閉。我們無法讀取你的 iCloud 內容。

## 權限說明

僅在功能需要時請求：

| 權限 | 時機 | 原因 |
|------|------|------|
| 通知 | 你開啟今日一經提醒 | 本地排程提醒 |
| 照片（僅加入） | 你儲存法卡或匯出 | 寫入渲染圖片 / PDF；無需讀取全部照片 |
| iCloud | 你開啟同步 | 同步收藏 / 經單 / 歷史 / 掌握度 / 筆記 / 念誦與功課偏好 |
| 即時動態（iOS） | 你開啟品讀或念誦即時動態 | 在鎖定畫面 / 動態島顯示進度 |
| 背景音訊能力 | 你開啟背景誦經 | App 不在前景時繼續 TTS |

我們**不**請求通訊錄、精確位置、相機、麥克風（除系統 TTS 播放外）或追蹤權限。

## 我們明確不做的事

- **不**出售個人資料。
- **不**建立廣告畫像。
- **不**要求帳號或社交登入。
- **不**嵌入用於資料收集的第三方廣告、分析或社交 SDK。
- **不**在你主動儲存之外存取照片（且僅為「加入」）。
- **不**接收 StoreKit 銀行卡／信用卡號碼（由 Apple 處理付款）。
- **不**把宗教內容做成算命 / 祈福求財的商業化產品。

## 兒童隱私

愛佛經不會故意收集包括 13 歲以下（或你所在地區同等年齡）兒童在內的任何人的個人資料。由於我們不營運資料收集後端，我們這邊不會保存兒童檔案。家庭可在自有裝置上離線使用閱讀與修習功能。

## 第三方

- **Apple** — App Store 分發、可選 StoreKit 購買、可選 iCloud、系統 TTS、你選擇的分享目標，以及系統通知 / 即時動態 / Siri / 捷徑投遞。
- **無其他**用於廣告、分析或社交登入的第三方資料收集 SDK。

## 國際使用者

應用設計為在你的裝置上離線運行。可選 Apple 服務遵循 Apple 條款與地區可用性。

## 資料保留與刪除

- **本機** — 偏好與進度保留至你在應用內清除（如有入口）、重置裝置或解除安裝應用。
- **iCloud（可選）** — 你同步的資料按 Apple 政策留在**你的** iCloud，直到關閉同步並/或透過 Apple 工具清理。
- **iHTC Studio** — 我們不在自有伺服器收集個人資料，因此沒有可供刪除的帳號資料集；隱私疑問可透過郵件聯絡。

## 政策變更

我們可能不時更新本政策。頁首「最近更新」日期會隨之變化，修訂版將發佈於本隱私政策頁面。

## 聯絡我們

如對隱私政策有疑問：

- **電子郵件：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

我們通常在 48 小時內回覆。

</section>
