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

iHTC Studio ("we", "us" or "our") built **iSutra** (also known as "爱佛经" / "愛佛經", Bundle ID `com.iHTCboy.iSutra`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on **this page** as the public privacy policy for the app. For App Store Connect, open this Privacy Policy in your browser and copy the address from the address bar (the public site domain may change over time).

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

爱火腿肠工作室（iHTC Studio）（「我们」）开发了 **爱佛经**（iSutra / 愛佛經，Bundle ID `com.iHTCboy.iSutra`）。本隐私政策说明你在使用本应用时，数据如何被处理（以及**不会**如何被处理）。本页可作为 **App Store 审核**与用户查阅的公开隐私政策。填写 App Store Connect 时，请在浏览器打开本隐私政策页，从地址栏复制当前网址（站点域名日后可能变更，请勿依赖文档中的固定域名）。

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

愛火腿腸工作室（iHTC Studio）（「我們」）開發了 **愛佛經**（iSutra / 爱佛经，Bundle ID `com.iHTCboy.iSutra`）。本隱私政策說明你在使用本應用時，資料如何被處理（以及**不會**如何被處理）。本頁可作為 **App Store 審核**與使用者查閱的公開隱私政策。填寫 App Store Connect 時，請在瀏覽器開啟本隱私政策頁，從網址列複製目前網址（網站網域日後可能變更，請勿依賴文件中的固定網域）。

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
<section lang="ja" markdown="1">

**最終更新日:** 2026年8月18日

iHTC Studio（「当社」）は **iSutra**（「爱佛经」／「爱佛经」、Bundle ID `com.iHTCboy.iSutra`）を開発しました。本プライバシーポリシーは、本アプリの利用時にどのデータが取り扱われ、取り扱われないかを説明します。**Apple App Review** とユーザーは、**本ページ**を公開のプライバシーポリシーとして参照できます。App Store Connect では、ブラウザで本プライバシーポリシーを開き、アドレスバーから URL をコピーしてください（公開サイトのドメインは将来変更される場合があります）。

## 概要（Apple プライバシー栄養表示との整合性）

| トピック | 当社の方針 |
|-------|----------------|
| アカウント | **不要** — 登録、メールサインイン、電話番号は必要ありません |
| iHTC Studioによるデータ収集 | **データは収集しません** — 個人データを受け取るバックエンドは運営していません |
| ネットワーク | ライブラリ、reading, recite, Study Hall, Hunt, chant, practice, widgets, and daily notifications work **offline** after installは、インストール後 **オフライン** で動作します |
| 分析 / 広告 / トラッキング | **なし** — サードパーティの分析、広告、トラッキングSDKは使用しておらず、App Tracking Transparencyも使用していません |
| 任意の Apple サービス | **iCloud** (your private KVS), **Photo Library (Add Only)** for Dharma cards / exports, **StoreKit** for 任意チップ, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default) |

## データの収集

当社は、広告や分析のために個人情報を収集、販売、共有することは**ありません**。

- **アカウント不要** — アカウントを作成せずに、すべての基本機能を使用できます。
- **分析や広告なし** — アプリのバイナリには、サードパーティの分析、広告、クラッシュレポートSDKは統合されておらず、データが当社に送信されることはありません。
- **コンテンツのアップロードなし** — お客様のreading history, favorites, lists, notes, mastery, streaks, chant counts, practice checklists, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## アプリの仕組み

- **同梱ライブラリ** — テキスト JSON、白話／英語、索引、学習補助はアプリ／ウィジェット バンドル内に同梱されます。閲覧と学習にネットワークは不要です。
- **端末内音声** — 朗誦は Apple **AVSpeechSynthesizer**（TTS）。経典テキストは iHTC Studio へ送りません。
- **ウィジェットと App Group** — ウィジェットとアプリは、端末上の App Group `group.com.iHTCboy.iSutra` を通じて設定と軽量な状態を共有します。
- **毎日の通知** - ユーザー通知を使用してローカルにスケジュールされます。 通知をタップすると、デバイス上のパッセージ ID へのディープ リンクが開きます。 サーバーのファンアウトはありません。
- **法カード / 書き出し** — 画像と PDF は端末で生成。保存時のみ **写真ライブラリ（追加のみ）**。**共有シート**は**お客様が選んだ**アプリへ送る場合があり、そのプライバシーポリシーが適用されます。
- **写経（iOS）** — PencilKit のストロークは Application Support（`CopySutra/…`）に保存されます。**App Group には入れず**、**iCloud 同期もされません**。
- **オプションのチップ** - 「チップ開発者」は、Apple によって処理される消耗品 **StoreKit** の購入です。 私たちはあなたの支払いカードの詳細を受け取りません。
- **Siri / ショートカット / コントロール センター** — オプションのシステム統合により、デバイス上のディープ リンクが開きます。 彼らはあなたのライブラリを私たちに送ることはありません。
- **オプションのスポットライト** — デフォルトではオフです。 インデックス作成を有効にすると、ローカル検索のためにデバイス上のシステムによってコンテンツのインデックスが作成されます。 当社は検索バックエンドを運用していません。

## 端末に保存されるデータ

 | データ | どこ | 目的 |
 |------|-------|-----------|
| 経典 DB（索引・シャード・大容量） | App / Widget バンドル | オフライン閲読と学習 |
| お気に入りとリスト（经单） | App Group UserDefaults | 星付きの篇目とユーザーリスト |
 | 読書履歴 / 最後に読んだ | アプリグループのUserDefaults | 続きを読む、履歴 UI |
| 学習進捗と習熟 | App Group UserDefaults | Study Hall state, quiz / Hunt progress |
| メモ | App Group UserDefaults | 篇についてのメモ |
 | 連続練習 / チェックイン | アプリグループのUserDefaults | 日々の習慣 |
| 唱和回数と音設定 | App Group UserDefaults | 木魚の合計・目標・音色 |
| 朝夕の修行と回向 | App Group UserDefaults | 日課チェックリスト |
 | 外観と読み取り設定 | アプリグループのUserDefaults | テーマ、アクセント、言語、レイアウト、TTS、タブ、ウィジェット |
| Daily Sutra cache & notification prefs | App Group UserDefaults | 今日の ID, 時刻 |
 | 共有カードの設定 | アプリグループのUserDefaults | 最後のスタイル/比率の選択 |
| 写経データ (iOS) | Application Support（`CopySutra/`） | 行ごとのなぞり書き草稿 |
 | オンボーディングと TipKit の状態 | 標準 UserDefaults (デバイス) | ウェルカムガイド / 発見のヒント |
 | ホーム画面のクイックアクション | システム + ローカル設定 | 設定するショートカット |
| Widget / Live Activity スナップショット | App Group / ActivityKit | 既に開いたテキスト / chant 状態を表示 |

アプリをアンインストールすると、アプリに関連するサンドボックスおよびApp Groupデータが削除されます（iOS/macOSの動作に依存します）。任意のiCloudコピーは、あなたが削除するか、同期をオフにして他の場所で削除するまで、**あなたの**iCloudに残ります。

## iCloud同期（オプション）

設定で **iCloud 同期**を有効にすると、**Apple ID** に紐づく **`NSUbiquitousKeyValueStore`** 経由でデータをミラーします（お気に入り、リスト、履歴、習熟、メモ、唱和設定など）。通信は **Apple iCloud** へ。写経データは**含まれません**。設定でオフ可能。当社は iCloud 内容を読めません。

## 権限

 iLiezi は、機能が必要な場合にのみアクセス許可を要求します。

| 権限 | タイミング | 理由 |
|------------|------|-----|
| 通知 | Daily Sutra reminders を有効にする | ローカルスケジュール of reminder notifications |
| 写真ライブラリ（追加のみ） | 法カード保存または書き出し | 描画画像/PDF を書き込み（ライブラリ読取は不要） |
| iCloud | 同期を有効にする | お気に入り/リスト/履歴/習熟/メモ/唱和・修行設定を同期 |
| Live Activities (iOS) | Reading / Chant Live Activity | 閲読 / 唱和進捗をロック画面 / Dynamic Island に |
 | バックグラウンドオーディオ (機能) | バックグラウンド朗読を有効にします | アプリがフォアグラウンドでないときに TTS を続行する |

 当社は、連絡先、正確な位置情報、カメラ、マイク (システムの TTS 再生を超える)、または追跡を要求しません**。

## 私たちがやらないこと

 - 当社は個人データを**販売しません**。
- 当社は広告プロフィールを構築しません**。
- アカウントやソーシャル ログインは**必要ありません**。
- データ収集のためにサードパーティの広告、分析、ソーシャル SDK を埋め込むことは**ありません**。
- 保存を選んだとき以外、**追加のみ**を超えて写真ライブラリにアクセスしません。
- 当社は StoreKit 支払いカード番号を**受け取りません** (Apple は支払いを処理します)。
- 宗教コンテンツを占いや有料祈福商取引に**しません**。

## 子供のプライバシー

iSutra は 13 歳未満を含め故意に個人データを収集しません。収集 backend がないため児童プロフィールはありません。家族は各自の端末でオフライン利用できます。

## 第三者

- **Apple** — App Storeでの配信、オプションのStoreKit購入、オプションのiCloud KVS、システムTTS、選択したShare Sheetの宛先、OSレベルの通知／ライブアクティビティ／Siri／ショートカットの配信。
- 広告、分析、ソーシャルログインのデータ収集のために**他のサードパーティSDKは含まれていません**。

## 国際ユーザー

このアプリは、お使いのデバイス上でオフラインで機能するように設計されています。オプションのAppleサービスは、Appleの利用規約および地域での利用可能性に従います。

## データ保持と削除

- **デバイス上** — 利用可能な場合、アプリ内で削除する、デバイスをリセットする、またはアプリをアンインストールするまで、ローカルの設定や進行状況は保持されます。
- **iCloud（任意）** — 同期したデータは、同期を無効にするかAppleのツールを使って削除するまで、Appleのポリシーに従って**あなたの**iCloudアカウント内に保持されます。
- **iHTC Studio** — 当社のサーバーでは個人データを収集していないため、メールでの質問に回答する以外に削除できるアカウントデータセットはありません。

## このポリシーの変更

当社はこのプライバシーポリシーを随時更新することがあります。ページ上部の「最終更新日」が変更され、改訂されたポリシーがこのプライバシーポリシーページに掲載されます。

## お問い合わせ

このプライバシーポリシーやプライバシーの取り扱いについて質問がある場合：

- **メール:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

通常48時間以内に回答いたします。

</section>
<section lang="ko" markdown="1">

**마지막 업데이트:** 2026년 8월 18일

iHTC Studio("당사")는 **iSutra**("爱佛经" / "爱佛经", Bundle ID `com.iHTCboy.iSutra`)을(를) 개발했습니다. 본 개인정보 처리방침은 앱 사용 시 어떤 데이터가 처리되고 처리되지 않는지 설명합니다. **Apple App Review**와 사용자는 **이 페이지**를 공개 개인정보 처리방침으로 사용할 수 있습니다. App Store Connect에는 브라우저에서 본 개인정보 처리방침을 열고 주소창의 URL을 복사하세요(공개 사이트 도메인은 변경될 수 있습니다).

## 요약 (Apple 개인정보 영양성분표 정렬)

| 주제 | 당사의 정책 |
|-------|----------------|
| 계정 | **필요 없음** — 등록, 이메일 로그인, 전화번호 필요 없음 |
| iHTC 스튜디오의 데이터 수집 | **데이터 수집 없음** — 개인 데이터를 받는 백엔드를 운영하지 않습니다 |
| 네트워크 | 라이브러리, reading, recite, Study Hall, Hunt, chant, practice, widgets, and daily notifications work **offline** after install는 설치 후 **오프라인**으로 동작합니다 |
| 분석 / 광고 / 추적 | **없음** — 타사 분석, 광고, 추적 SDK 없음; 앱 추적 투명성(App Tracking Transparency) 사용 없음 |
| 선택 Apple 서비스 | **iCloud** (your private KVS), **Photo Library (Add Only)** for Dharma cards / exports, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default) |

## 데이터 수집

개인 정보를 광고나 분석 목적으로 **수집, 판매, 공유하지 않습니다**.

- **계정 불필요** — 계정을 만들지 않아도 모든 핵심 기능을 사용할 수 있습니다.
- **분석 및 광고 없음** — 앱 바이너리는 당사로 데이터를 전송하는 타사 분석, 광고, 크래시 리포트 SDK를 통합하지 않습니다.
- **콘텐츠 업로드 없음** — 사용자의 reading history, favorites, lists, notes, mastery, streaks, chant counts, practice checklists, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## 앱 작동 방식

- **번들 라이브러리** — 텍스트 JSON, vernacular/English, 색인, 학습 보조 자료가 앱/위젯 번들에 포함됩니다. 탐색과 학습에 네트워크가 필요하지 않습니다.
- **기기 내 음성** — **AVSpeechSynthesizer**로 낭송. 경전 텍스트 미전송.
- **위젯 및 App Group** — 위젯과 앱은 기기의 App Group `group.com.iHTCboy.iSutra`을 통해 설정과 가벼운 상태를 공유합니다.
- **일일 알림** — 사용자 알림을 통해 로컬로 예약됩니다. 알림을 탭하면 기기의 통로 ID에 대한 딥 링크가 열립니다. 서버 팬아웃이 없습니다.
- **법 카드 / 내보내기** — 이미지·PDF는 기기에서 생성. 저장 시 **사진 보관함(추가 전용)**. **공유 시트**는 **사용자가 선택한** 앱으로 보낼 수 있습니다.
- **필경(iOS)** — PencilKit 획은 Application Support(`CopySutra/…`)에 저장됩니다. **App Group에 두지 않으며** **iCloud 동기화되지 않습니다**.
- **선택적 팁** — "팁 개발자"는 Apple에서 처리하는 소모품 **StoreKit** 구매입니다. 귀하의 결제 카드 정보는 수신되지 않습니다.
- **Siri / 바로가기 / 제어 센터** — 선택적 시스템 통합으로 기기 내 딥 링크가 열립니다. 그들은 귀하의 라이브러리를 우리에게 보내지 않습니다.
- **선택적 스포트라이트** — 기본적으로 꺼져 있습니다. 인덱싱을 활성화하면 로컬 검색을 위해 장치의 시스템이 콘텐츠를 인덱싱합니다. 우리는 검색 백엔드를 운영하지 않습니다.

## 귀하의 장치에 저장된 데이터

| 데이터 | 어디 | 목적 |
|------|-------|---------|
| 불경 DB(색인·샤드) | App / Widget 번들 | 오프라인 읽기·학습 |
| 즐겨찾기 및 목록(经单) | App Group UserDefaults | 별표 표시한 구절과 사용자 목록 |
| 읽은 이력/마지막 읽은 내용 | 앱 그룹 UserDefaults | 계속 읽기, 기록 UI |
| 학습 진행 및 숙달 | App Group UserDefaults | Study Hall state, quiz / Hunt progress |
| 메모 | App Group UserDefaults | 구절 메모 |
| 연속연습/체크인 | 앱 그룹 UserDefaults | 일상습관 |
| 염불 횟수·음향 설정 | App Group UserDefaults | 목어 합계·목표·음색 |
| 아침·저녁 수행 | App Group UserDefaults | 일과 체크리스트 |
| 모양 및 읽기 기본 설정 | 앱 그룹 UserDefaults | 테마, 악센트, 언어, 레이아웃, TTS, 탭, 위젯 |
| Daily Sutra cache & notification prefs | App Group UserDefaults | 오늘 ID, 시간 |
| 공유 카드 환경 설정 | 앱 그룹 UserDefaults | 마지막 스타일/비율 선택 |
| 필경 데이터(iOS) | Application Support(`CopySutra/`) | 줄별 따라쓰기 초안 |
| 온보딩 및 TipKit 상태 | 표준 UserDefaults(장치) | 환영 가이드/탐색 팁 |
| 홈 화면 빠른 작업 | 시스템 + 로컬 환경설정 | 구성한 바로가기 |
| Widget / Live Activity 스냅샷 | App Group / ActivityKit | 연 텍스트/chant 상태 표시 |

앱을 삭제하면 앱과 연관된 샌드박스 및 앱 그룹 데이터가 제거됩니다(iOS/macOS 동작에 따라 다름). 선택적으로 iCloud에 저장된 복사본은 사용자가 삭제하거나 동기화를 끄고 다른 곳에서 삭제할 때까지 **귀하의** iCloud에 남아 있습니다.

## iCloud 동기화 (선택 사항)

설정에서 **iCloud Sync** 사용 시 **Apple ID**의 **`NSUbiquitousKeyValueStore`**로 미러(즐겨찾기·목록·기록 등). **Apple iCloud**로만. 필경 그림 **미포함**. iCloud 내용 읽을 수 없음.

## 권한

iLiezi는 기능에 필요한 경우에만 권한을 요청합니다.

| 허가 | 언제 | 왜? |
|------------|------|-----|
| 알림 | Daily Sutra reminders 사용 | 로컬 예약 of reminder notifications |
| 사진 보관함(추가 전용) | 법 카드 저장/내보내기 | 렌더 이미지/PDF 기록(전체 읽기 불필요) |
| iCloud | 동기화 사용 | 즐겨찾기/목록/기록/숙달/메모/chant·수행 설정 |
| Live Activities(iOS) | Reading/Chant Live Activity | 읽기/chant 진행 표시 |
| 배경 오디오(기능) | 배경 암송을 활성화합니다 | 앱이 포그라운드가 아닐 때 TTS 계속 |

우리는 연락처, 정확한 위치, 카메라, 마이크(시스템 TTS 재생 이외) 또는 추적을 요청하지 **않습니다**.

## 우리가 하지 않는 일

- 당사는 개인 데이터를 판매하지 **않습니다**.
- 우리는 광고 프로필을 작성하지 **않습니다**.
- 계정이나 소셜 로그인이 필요하지 **않습니다**.
- 당사는 데이터 수집을 위해 제3자 광고, 분석 또는 소셜 SDK를 삽입하지 **않습니다**.
- 저장 선택 시 **추가 전용** 외 사진 보관함 접근 없음.
- 저희는 StoreKit 결제 카드 번호를 받지 **않습니다**(Apple에서 결제를 처리함).
- 종교 콘텐츠를 점술·유료 축복 상업으로 **바꾸지 않습니다**.

## 아동 개인정보 보호

iSutra는 13세 미만 포함 고의 수집 없음. backend 없어 아동 프로필 없음. 가족 오프라인 이용 가능.

## 제3자

- **Apple** — App Store 배포, 선택적 StoreKit 구매, 선택적 iCloud KVS, 시스템 TTS, 사용자가 선택한 공유 시트 대상, OS 수준의 알림 / 라이브 액티비티 / Siri / 단축키 전달.
- 광고, 분석, 소셜 로그인 등을 위한 **기타 제3자 SDK**는 데이터 수집을 위해 포함되지 않았습니다.

## 국제 사용자

앱은 사용자의 장치에서 오프라인 기능이 가능하도록 설계되었습니다. 선택적 Apple 서비스는 Apple의 이용 약관 및 지역 가용성을 따릅니다.

## 데이터 보존 및 삭제

- **기기 내** — 로컬 환경설정 및 진행 상황은 앱 내에서 삭제하지 않거나, 기기를 초기화하거나, 앱을 제거하지 않는 한 그대로 남아 있습니다(해당 기능이 제공되는 경우).
- **iCloud (선택 사항)** — 동기화한 데이터는 동기화를 해제하거나 Apple의 도구를 통해 삭제할 때까지 Apple 정책에 따라 **귀하의** iCloud 계정에 남아 있습니다.
- **iHTC Studio** — 당사는 서버에 개인 데이터를 수집하지 않기 때문에 이메일 문의에 답변하는 것을 제외하고 요청 시 삭제할 계정 데이터셋이 없습니다.

## 이 정책의 변경

본 개인정보처리방침은 수시로 업데이트될 수 있습니다. 상단의 '마지막 업데이트' 날짜가 변경되며, 수정된 정책은 이 개인정보처리방침 페이지에 게시됩니다.

## 문의하기

본 개인정보처리방침이나 개인정보 처리 관행에 대해 질문이 있는 경우:

- **이메일:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

일반적으로 48시간 이내에 회신합니다.

</section>
<section lang="ru" markdown="1">

**Последнее обновление:** 18 августа 2026 г.

iHTC Studio («мы») создала **iSutra** («爱佛经» / «爱佛经», Bundle ID `com.iHTCboy.iSutra`). Настоящая Политика конфиденциальности объясняет, какие данные обрабатываются (и не обрабатываются) при использовании приложения. **Apple App Review** и пользователи могут использовать **эту страницу** как публичную политику конфиденциальности. Для App Store Connect откройте эту страницу в браузере и скопируйте URL из адресной строки (домен публичного сайта может измениться).

## Сводка (в соответствии с меткой Apple Privacy Nutrition)

| Тема | Наша практика |
|-------|----------------|
| Учетная запись | **Не требуется** — регистрация, вход по электронной почте или номеру телефона не нужны |
| Сбор данных iHTC Studio | **Данные не собираются** — мы **не** используем серверную часть, которая получает ваши личные данные |
| Сеть | Библиотека, reading, recite, Study Hall, Hunt, chant, practice, widgets, and daily notifications work **offline** after install работают **офлайн** после установки |
| Аналитика / реклама / отслеживание | **Отсутствует** — нет сторонней аналитики, рекламы или SDK для отслеживания; не используется App Tracking Transparency |
| Необязательные сервисы Apple | **iCloud** (your private KVS), **Photo Library (Add Only)** for Dharma cards / exports, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default) |

## Сбор данных

Мы **не** собираем, не продаем и не делимся личной информацией для рекламы или аналитики.

- **Без аккаунта** — Вы можете использовать все основные функции без создания аккаунта у нас.
- **Без аналитики и рекламы** — В приложении не интегрированы сторонние SDK для аналитики, рекламы или отчётов о сбоях, которые отправляли бы данные нам.
- **Без загрузки контента** — Ваши reading history, favorites, lists, notes, mastery, streaks, chant counts, practice checklists, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## Как работает приложение

- **Встроенная библиотека** — текстовый JSON, vernacular/English, указатели и учебные материалы входят в пакет app/widget. Для просмотра и обучения сеть не нужна.
- **Речь на устройстве** — **AVSpeechSynthesizer**. Текст сутр не отправляем.
- **Виджеты и App Group** — виджеты и приложение обмениваются настройками и лёгким состоянием через App Group `group.com.iHTCboy.iSutra` на вашем устройстве.
- **Ежедневные уведомления** — планируются локально с помощью уведомлений пользователя. При нажатии на уведомление открывается глубокая ссылка на идентификатор прохода на устройстве; нет разветвления сервера.
- **Dharma-карты / экспорт** — изображения и PDF на устройстве. **Фототека (только добавление)** при сохранении. Share Sheet — приложение **по вашему выбору**.
- **Копирование сутры (iOS)** — штрихи PencilKit хранятся в Application Support (`CopySutra/…`). **Не** в App Group и **не** синхронизируются с iCloud.
- **Необязательный совет**. «Tip Developer» — это расходный материал, приобретаемый **StoreKit** и обрабатываемый Apple. Мы не получаем данные вашей платежной карты.
- **Siri / Ярлыки / Центр управления** — дополнительные системные интеграции открывают глубокие ссылки на устройстве; они не отправляют нам вашу библиотеку.
- **Дополнительный прожектор** — отключен по умолчанию. Если вы включите индексирование, контент индексируется системой на устройстве для локального поиска; мы не используем поисковую систему.

## Данные, хранящиеся на вашем устройстве

| Данные | Где | Цель |
|------|-------|---------|
| База сутр (индексы, шарды) | Пакет App / Widget | Офлайн-чтение и обучение |
| Избранное и списки (经单) | UserDefaults App Group | Отмеченные фрагменты и пользовательские списки |
| История чтения / последнее чтение | Пользовательские настройки группы приложений | Продолжить чтение, история пользовательского интерфейса |
| Прогресс и mastery | UserDefaults App Group | Study Hall state, quiz / Hunt progress |
| Заметки | UserDefaults App Group | Заметки к фрагментам |
| Практика / регистрация | Пользовательские настройки группы приложений | Ежедневная привычка |
| Счётчики chant и звук | UserDefaults App Group | Wooden-fish, цели, тоны |
| Утро/вечер практика | UserDefaults App Group | Ежедневный чеклист |
| Настройки внешнего вида и чтения | Пользовательские настройки группы приложений | Тема, акцент, язык, макет, TTS, вкладки, виджеты |
| Daily Sutra cache & notification prefs | UserDefaults App Group | ID на сегодня, время, переключатели |
| Настройки карты обмена | Пользовательские настройки группы приложений | Последний выбор стиля/пропорции |
| Рисунки Copy-sutra (iOS) | Application Support (`CopySutra/`) | Черновики по строкам |
| Регистрация и состояние TipKit | Стандартные настройки пользователя (устройство) | Приветственное руководство / советы по открытию |
| Быстрые действия на главном экране | Система + локальные настройки | Ярлыки, которые вы настраиваете |
| Снимки Widget / Live Activity | App Group / ActivityKit | Отображение открытого текста/chant |

При удалении приложения удаляются данные песочницы и группы приложений, связанные с приложением (в зависимости от поведения iOS/macOS). Дополнительные копии iCloud остаются в **вашем** iCloud до тех пор, пока вы не очистите их или не отключите синхронизацию и не удалите их в другом месте.

## Синхронизация с iCloud (необязательно)

При **iCloud Sync** данные зеркалируются через **`NSUbiquitousKeyValueStore`** **Apple ID**. Трафик — **Apple iCloud**. Copy-sutra **не** включены. Мы не читаем ваш iCloud.

## Разрешения

iLiezi запрашивает разрешения только тогда, когда они нужны функции:

| Разрешение | Когда | Почему |
|------------|------|-----|
| Уведомления | Вы включаете Daily Sutra reminders | Локальное планирование of reminder notifications |
| Фототека (только добавление) | Сохранение Dharma-карты/экспорт | Запись изображения/PDF; без чтения библиотеки |
| iCloud | Включаете синхронизацию | Избранное/списки/история/mastery/заметки/chant |
| Live Activities (iOS) | Reading or Chant Live Activity | Прогресс чтения/chant на Lock Screen |
| Фоновый звук (возможность) | Вы включаете фоновое чтение | Продолжить TTS, когда приложение не на переднем плане |

Мы **не** запрашиваем контакты, точное местоположение, камеру, микрофон (кроме системного воспроизведения TTS) или отслеживание.

## Чего мы не делаем

- Мы **не** продаем персональные данные.
- Мы **не** создаем рекламные профили.
- Нам **не** требуется учетная запись или вход в социальную сеть.
– Мы **не** встраиваем сторонние рекламные, аналитические или социальные SDK для сбора данных.
- **Не** обращаемся к Фототеке сверх **только добавления** при сохранении.
- Мы **не** получаем номера платежных карт StoreKit (Apple обрабатывает платежи).
- **Не** превращаем релigious контент в гадание или платные «благословения».

## Конфиденциальность детей

iSutra сознательно не собирает данные, включая детей до 13 лет. Нет backend — нет детских профилей.

## Третьи стороны

- **Apple** — распространение через App Store, необязательные покупки через StoreKit, необязательный iCloud KVS, система TTS, выбранные вами пункты общего доступа (Share Sheet), а также уведомления на уровне ОС / Live Activity / Siri / Shortcuts.
- **Никакие другие сторонние SDK** для рекламы, аналитики или социальной авторизации не включены для сбора данных.

## Пользователи из других стран

Приложение предназначено для работы в автономном режиме на вашем устройстве. Необязательные сервисы Apple подчиняются условиям Apple и региональной доступности.

## Сроки хранения и удаление данных

- **На устройстве** — Локальные настройки и прогресс сохраняются до тех пор, пока вы не удалите их в приложении (если такая функция доступна), не сбросите устройство или не удалите приложение.
- **iCloud (по желанию)** — Данные, которые вы синхронизировали, остаются в **вашем** iCloud-аккаунте согласно политике Apple, до тех пор пока вы не отключите синхронизацию и/или не удалите их с помощью инструментов Apple.
- **iHTC Studio** — Поскольку мы не собираем персональные данные на наших серверах, у нас нет набора данных аккаунта, который мы могли бы удалить по запросу, кроме как ответа на ваши вопросы по электронной почте.

## Изменения в этой Политике

Мы можем время от времени обновлять настоящую Политику конфиденциальности. Дата «Последнее обновление» вверху будет изменяться, а пересмотренная политика будет размещена на этой странице.

## Свяжитесь с нами

Если у вас есть вопросы о настоящей Политике конфиденциальности или практиках конфиденциальности:

- **Электронная почта:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Обычно мы отвечаем в течение 48 часов.

</section>
<section lang="th" markdown="1">

**อัปเดตล่าสุด:** 18 สิงหาคม 2026

iHTC Studio ("เรา") พัฒนา **iSutra** ("爱佛经" / "爱佛经", Bundle ID `com.iHTCboy.iSutra`) นโยบายความเป็นส่วนตัวนี้อธิบายว่าข้อมูลใดถูกจัดการและไม่ถูกจัดการเมื่อคุณใช้แอป **Apple App Review** และผู้ใช้สามารถใช้**หน้านี้**เป็นนโยบายความเป็นส่วนตัวสาธารณะ สำหรับ App Store Connect ให้เปิดนโยบายนี้ในเบราว์เซอร์แล้วคัดลอก URL จากแถบที่อยู่ (โดเมนสาธารณะอาจเปลี่ยนได้)

## สรุป (การจัดตำแหน่งกับ Nutrition Label ความเป็นส่วนตัวของ Apple)

| หัวข้อ | การปฏิบัติของเรา |
|-------|----------------|
| บัญชี | **ไม่จำเป็น** — ไม่ต้องลงทะเบียน ลงชื่อเข้าใช้ด้วยอีเมล หรือหมายเลขโทรศัพท์ |
| การเก็บข้อมูลโดย iHTC Studio | **ไม่เก็บข้อมูล** — เรา **ไม่ได้**ดำเนินการแบ็กเอนด์ที่รับข้อมูลส่วนตัวของคุณ |
| เครือข่าย | คลังข้อมูล reading, recite, Study Hall, Hunt, chant, practice, widgets, and daily notifications work **offline** after install ทำงาน **แบบออฟไลน์** หลังติดตั้ง |
| การวิเคราะห์ / โฆษณา / การติดตาม | **ไม่มี** — ไม่มี SDK การวิเคราะห์ โฆษณา หรือการติดตามจากบุคคลที่สาม; ไม่ใช้ App Tracking Transparency |
| บริการ Apple เสริม | **iCloud** (your private KVS), **Photo Library (Add Only)** for Dharma cards / exports, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default) |

## การเก็บข้อมูล

เราจะ **ไม่**เก็บ ขาย หรือแชร์ข้อมูลส่วนบุคคลเพื่อโฆษณาหรือการวิเคราะห์

- **ไม่ต้องมีบัญชีผู้ใช้** — คุณสามารถใช้คุณสมบัติหลักทั้งหมดได้โดยไม่ต้องสร้างบัญชีกับเรา
- **ไม่มีการวิเคราะห์หรือโฆษณา** — ไฟล์แอปไม่ได้รวม SDK การวิเคราะห์ การโฆษณา หรือการรายงานข้อผิดพลาดจากบุคคลที่สามที่ติดต่อกลับไปยังเรา
- **ไม่อัปโหลดเนื้อหา** — reading history, favorites, lists, notes, mastery, streaks, chant counts, practice checklists, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**. ของคุณ

## วิธีการทำงานของแอป

- **ไลบรารีในชุดแอป** — JSON ข้อความ vernacular/English ดัชนี และตัวช่วยเรียนอยู่ในชุดแอป/วิดเจ็ต การเรียกดูและเรียนไม่ต้องใช้เครือข่าย
- **เสียงบนอุปกรณ์** — **AVSpeechSynthesizer** ไม่ส่งข้อความสutra
- **วิดเจ็ตและ App Group** — วิดเจ็ตและแอปใช้การตั้งค่าและสถานะขนาดเล็กร่วมกันผ่าน App Group `group.com.iHTCboy.iSutra` บนอุปกรณ์ของคุณ
- **การแจ้งเตือนรายวัน** — กำหนดเวลาภายในเครื่องด้วยการแจ้งเตือนผู้ใช้ การแตะการแจ้งเตือนจะเปิดลิงก์ในรายละเอียดไปยังรหัสข้อความบนอุปกรณ์ ไม่มีการปิดเซิร์ฟเวอร์
- **การ์ดธรรม / ส่งออก** — สร้างภาพและ PDF บนเครื่อง **คลังรูปภาพ (เพิ่มอย่างเดียว)** เมื่อบันทึก
- **คัดลอกสutra (iOS)** — เส้น PencilKit เก็บใน Application Support (`CopySutra/…`) **ไม่**ใส่ App Group **ไม่**ซิงค์ iCloud
- **เคล็ดลับเสริม** — “Tip Developer” เป็นการซื้อ **StoreKit** แบบบริโภคที่ดำเนินการโดย Apple เราไม่ได้รับรายละเอียดบัตรชำระเงินของคุณ
- **Siri / ทางลัด / ศูนย์ควบคุม** — การรวมระบบที่เป็นตัวเลือกจะเปิดลิงก์ในรายละเอียดบนอุปกรณ์ พวกเขาไม่ได้ส่งห้องสมุดของคุณมาให้เรา
- **สปอตไลท์เสริม** — ปิดตามค่าเริ่มต้น หากคุณเปิดใช้งานการจัดทำดัชนี เนื้อหาจะถูกจัดทำดัชนีโดยระบบบนอุปกรณ์สำหรับการค้นหาในท้องถิ่น เราไม่ได้ดำเนินการแบ็กเอนด์การค้นหา

## ข้อมูลที่เก็บบนอุปกรณ์

| ข้อมูล | ที่ไหน | วัตถุประสงค์ |
|------|-------|---------|
| ฐานสutra (ดัชนี·ชards) | App / Widget bundle | อ่านและเรียนออฟไลน์ |
| รายการโปรดและรายการ (经单) | UserDefaults ของ App Group | ข้อความที่ติดดาวและรายการผู้ใช้ |
| ประวัติการอ่าน / อ่านครั้งล่าสุด | ค่าเริ่มต้นของกลุ่มแอป | อ่านต่อ ประวัติ UI |
| ความคืบหน้าและความเชี่ยวชาญ | UserDefaults ของ App Group | Study Hall state, quiz / Hunt progress |
| บันทึก | UserDefaults ของ App Group | บันทึกข้อความ |
| ฝึกสตรีค/เช็คอิน | ค่าเริ่มต้นของกลุ่มแอป | นิสัยประจำวัน |
| จำนวน chant และเสียง | UserDefaults ของ App Group | ปลาไม้ เป้า เสียง |
| ปฏิบัติเช้า-ค่ำ | UserDefaults ของ App Group | รายการพิธีรายวัน |
| ลักษณะที่ปรากฏและการตั้งค่าการอ่าน | ค่าเริ่มต้นของกลุ่มแอป | ธีม, สำเนียง, ภาษา, เค้าโครง, TTS, แท็บ, วิดเจ็ต |
| Daily Sutra cache & notification prefs | UserDefaults ของ App Group | ID วันนี้, schedule time |
| การตั้งค่าการ์ดแชร์ | ค่าเริ่มต้นของกลุ่มแอป | ตัวเลือกสไตล์ / อัตราส่วนสุดท้าย |
| ภาพ Copy-sutra (iOS) | Application Support (`CopySutra/`) | ร่างลากตามบรรทัด |
| การเริ่มต้นใช้งานและสถานะ TipKit | Standard UserDefaults (อุปกรณ์) | คู่มือต้อนรับ / เคล็ดลับการค้นพบ |
| การดำเนินการด่วนบนหน้าจอหลัก | ระบบ + การตั้งค่าท้องถิ่น | ทางลัดที่คุณกำหนดค่า |
| สแนป Widget / Live Activity | App Group / ActivityKit | แสดงข้อความ/chant ที่เปิดแล้ว |

การถอนการติดตั้งแอปจะลบข้อมูล sandbox และ App Group ที่เกี่ยวข้องกับแอป (ขึ้นอยู่กับพฤติกรรมของ iOS/macOS) สำเนา iCloud แบบเลือกได้จะยังคงอยู่ใน **iCloud ของคุณ** จนกว่าคุณจะลบหรือปิดการซิงค์และลบจากที่อื่น

## การซิงค์ iCloud (ตัวเลือก)

เปิด **iCloud Sync** ข้อมูลสะท้อนผ่าน **`NSUbiquitousKeyValueStore`** ไป **Apple iCloud** ไม่รวม Copy-sutra อ่าน iCloud ของคุณไม่ได้

## สิทธิ์

iLiezi ร้องขอการอนุญาตเฉพาะเมื่อคุณสมบัติต้องการ:

| สิทธิ์ | เมื่อไหร่ | ทำไม |
|------------|------|-----|
| การแจ้งเตือน | คุณเปิด Daily Sutra reminders | กำหนดเวลาในเครื่อง of reminder notifications |
| คลังรูปภาพ (เพิ่มอย่างเดียว) | บันทึก Dharma/ส่งออก | เขียนภาพ/PDF ไม่ต้องอ่านคลังทั้งหมด |
| iCloud | เปิดซิงค์ | ซิงค์รายการโปรด/รายการ/ประวัติ/mastery/บันทึก/chant |
| Live Activities (iOS) | Reading/Chant Live Activity | ความคืบหน้าบนหน้าจอล็อก |
| เสียงพื้นหลัง (ความสามารถ) | คุณเปิดใช้งานการอ่านพื้นหลัง | ดำเนินการต่อ TTS เมื่อแอปไม่ได้อยู่เบื้องหน้า |

เราไม่ **ไม่** ขอข้อมูลผู้ติดต่อ ตำแหน่งที่แน่นอน กล้อง ไมโครโฟน (นอกเหนือจากการเล่น TTS ของระบบ) หรือการติดตาม

## สิ่งที่เราไม่ทำ

- เราไม่ **ไม่** ขายข้อมูลส่วนบุคคล
- เราไม่ **ไม่** สร้างโปรไฟล์การโฆษณา
- เรา **ไม่** จำเป็นต้องมีบัญชีหรือการเข้าสู่ระบบโซเชียล
- เราไม่ **ไม่** ฝังโฆษณา การวิเคราะห์ หรือ SDK โซเชียลของบุคคลที่สามสำหรับการรวบรวมข้อมูล
- **ไม่**เข้าคลังรูปภาพเกิน **เพิ่มอย่างเดียว** เมื่อคุณบันทึก
- เรา **ไม่** รับหมายเลขบัตรชำระเงิน StoreKit (Apple ดำเนินการชำระเงิน)
- **ไม่**เปลี่ยนเนื้อหาศาสนาเป็นดูดวงหรือพาณิชย์อวยพร

## ความเป็นส่วนตัวของเด็ก

iSutra ไม่เก็บข้อมูลเด็กโดยเจตนา ไม่มี backend โปรไฟล์เด็ก

## บุคคลที่สาม

- **Apple** — การจัดจำหน่ายผ่าน App Store, การซื้อผ่าน StoreKit ตามตัวเลือก, iCloud KVS ตามตัวเลือก, ระบบ TTS, ปลายทาง Share Sheet ที่คุณเลือก, และการแจ้งเตือน / Live Activity / Siri / Shortcuts ระดับ OS
- **ไม่มี SDK ของบุคคลที่สามอื่น ๆ** สำหรับโฆษณา, การวิเคราะห์, หรือการเข้าสู่ระบบโซเชียลรวมอยู่เพื่อการเก็บข้อมูล

## ผู้ใช้ระหว่างประเทศ

แอปออกแบบมาให้ทำงานแบบออฟไลน์บนอุปกรณ์ของคุณ บริการของ Apple ตามตัวเลือกจะเป็นไปตามข้อกำหนดของ Apple และความพร้อมใช้งานในภูมิภาค

## การเก็บรักษาและการลบข้อมูล

- **บนอุปกรณ์** — การตั้งค่าและความคืบหน้าในเครื่องจะยังคงอยู่จนกว่าคุณจะล้างข้อมูลในแอป (ถ้ามี), รีเซ็ตอุปกรณ์ หรือถอนการติดตั้งแอป
- **iCloud (ไม่บังคับ)** — ข้อมูลที่คุณซิงค์จะยังคงอยู่ในบัญชี iCloud ของคุณตามนโยบายของ Apple จนกว่าคุณจะปิดการซิงค์และ/หรือล้างข้อมูลผ่านเครื่องมือของ Apple
- **iHTC Studio** — เนื่องจากเราไม่เก็บข้อมูลส่วนตัวบนเซิร์ฟเวอร์ของเรา จึงไม่มีชุดข้อมูลบัญชีใดให้เราลบตามคำขอ นอกจากตอบคำถามทางอีเมลของคุณ

## การเปลี่ยนแปลงนโยบายนี้

เราอาจปรับปรุงนโยบายความเป็นส่วนตัวนี้เป็นครั้งคราว วันที่ "ปรับปรุงล่าสุด" ด้านบนจะเปลี่ยนไป และนโยบายที่แก้ไขแล้วจะถูกโพสต์บนหน้าของนโยบายความเป็นส่วนตัวนี้

## ติดต่อเรา

หากคุณมีคำถามเกี่ยวกับนโยบายความเป็นส่วนตัวนี้หรือการปฏิบัติด้านความเป็นส่วนตัว:

- **อีเมล:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

เราโดยทั่วไปจะตอบกลับภายใน 48 ชั่วโมง

</section>
<section lang="de" markdown="1">

**Zuletzt aktualisiert:** 18. August 2026

iHTC Studio („wir“) hat **iSutra** („爱佛经“ / „爱佛经“, Bundle-ID `com.iHTCboy.iSutra`) entwickelt. Diese Datenschutzerklärung erläutert, welche Daten bei der Nutzung verarbeitet werden (und welche nicht). **Apple App Review** und Nutzer können sich auf **diese Seite** als öffentliche Datenschutzerklärung stützen. Für App Store Connect öffnen Sie diese Seite im Browser und kopieren Sie die URL aus der Adressleiste (die Domain kann sich ändern).

## Zusammenfassung (Übereinstimmung mit dem Apple-Datenschutzetikett)

| Thema | Unsere Praxis |
|-------|----------------|
| Konto | **Nicht erforderlich** — keine Registrierung, kein E-Mail-Login oder Telefonnummer erforderlich |
| Datenerhebung durch iHTC Studio | **Keine Datenerhebung** — wir betreiben **keinen** Backend-Service, der Ihre persönlichen Daten empfängt |
| Netzwerk | Bibliothek, reading, recite, Study Hall, Hunt, chant, practice, widgets, and daily notifications work **offline** after install funktionieren nach der Installation **offline** |
| Analysen / Werbung / Tracking | **Keine** — keine Analysen von Drittanbietern, Werbung oder Tracking-SDKs; keine Nutzung von App Tracking Transparency |
| Optionale Apple-Dienste | **iCloud** (your private KVS), **Photo Library (Add Only)** for Dharma cards / exports, **StoreKit** for optionales Trinkgeld, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default) |

## Datenerfassung

Wir erheben, verkaufen oder teilen **keine** persönlichen Informationen für Werbung oder Analysen.

- **Kein Konto** — Sie können alle Kernfunktionen nutzen, ohne ein Konto bei uns zu erstellen.
- **Keine Analysen oder Werbung** — Die App-Binärdatei integriert keine Analysen, Werbung oder Crash-Reporting-SDKs von Drittanbietern, die Daten an uns senden.
- **Kein Hochladen von Inhalten** — Ihre reading history, favorites, lists, notes, mastery, streaks, chant counts, practice checklists, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## So funktioniert die App

- **Mitgelieferte Bibliothek** — Text-JSON, Umgangssprache/Englisch, Indizes und Lernhilfen liegen im App-/Widget-Bundle. Durchsuchen und Lernen erfordern kein Netzwerk.
- **Sprache auf dem Gerät** — **AVSpeechSynthesizer**. Kein Sutra-Text an iHTC Studio.
- **Widgets und App Group** — Widgets und App teilen Einstellungen und leichten Zustand über die App Group `group.com.iHTCboy.iSutra` auf Ihrem Gerät.
- **Tägliche Benachrichtigungen** – Lokal geplant mit Benutzerbenachrichtigungen. Durch Tippen auf eine Benachrichtigung wird ein Deep-Link zu einer Durchgangs-ID auf dem Gerät geöffnet. Kein Server-Fanout.
- **Dharma-Karten / Export** — Bilder/PDF auf dem Gerät. **Fotomediathek (nur Hinzufügen)** beim Speichern.
- **Sutra abschreiben (iOS)** — PencilKit-Striche in Application Support (`CopySutra/…`). **Nicht** in App Group, **keine** iCloud-Sync.
- **Optionaler Tipp** – „Tip Developer“ ist ein verbrauchbarer **StoreKit**-Kauf, der von Apple abgewickelt wird. Wir erhalten Ihre Zahlungskartendaten nicht.
- **Siri / Verknüpfungen / Kontrollzentrum** – Optionale Systemintegrationen öffnen Deep Links auf dem Gerät; Sie senden Ihre Bibliothek nicht an uns.
- **Optionales Spotlight** – standardmäßig deaktiviert. Wenn Sie die Indizierung aktivieren, wird der Inhalt vom System auf dem Gerät für die lokale Suche indiziert; Wir betreiben kein Such-Backend.

## Auf Ihrem Gerät gespeicherte Daten

| Daten | Wo | Zweck |
|------|-------|---------|
| Sutra-Datenbank (Indizes, Shards) | App-/Widget-Bundle | Offline-Lesen und -Lernen |
| Favoriten und Listen (经单) | UserDefaults der App Group | Markierte Abschnitte und Nutzerlisten |
| Leseverlauf / zuletzt gelesen | Benutzerstandards der App-Gruppe | Lesen Sie weiter, Verlauf der Benutzeroberfläche |
| Lernfortschritt und Beherrschung | UserDefaults der App Group | Study Hall state, quiz / Hunt progress |
| Notizen | UserDefaults der App Group | Passagen-Notizen |
| Übungssträhne / Check-in | Benutzerstandards der App-Gruppe | Tägliche Gewohnheit |
| Chant-Zähler & Ton | UserDefaults der App Group | Wooden-fish, Ziele, Töne |
| Morgen/Abend-Praxis | UserDefaults der App Group | Tägliche Liturgie-Checkliste |
| Aussehen & Lesepräferenzen | Benutzerstandards der App-Gruppe | Thema, Akzent, Sprache, Layout, TTS, Tabs, Widgets |
| Daily Sutra cache & notification prefs | UserDefaults der App Group | Heutige ID, schedule time |
| Share-Card-Einstellungen | Benutzerstandards der App-Gruppe | Letzte Stil-/Verhältnisauswahl |
| Copy-sutra-Zeichnungen (iOS) | Application Support (`CopySutra/`) | Entwürfe pro Zeile |
| Onboarding- und TipKit-Status | Standard UserDefaults (Gerät) | Willkommensführer / Entdeckungstipps |
| Schnellaktionen auf dem Startbildschirm | System + lokale Einstellungen | Von Ihnen konfigurierte Verknüpfungen |
| Widget-/Live-Activity-Schnappschüsse | App Group / ActivityKit | Anzeige geöffneter Text/Chant |

Die Deinstallation der App entfernt Sandbox- und App-Gruppendaten, die mit der App verbunden sind (abhängig vom Verhalten von iOS/macOS). Optionale iCloud-Kopien bleiben in **deiner** iCloud, bis du sie löschst oder die Synchronisierung ausschaltest und anderswo löschst.

## iCloud-Synchronisierung (optional)

Mit **iCloud Sync** Spiegelung über **`NSUbiquitousKeyValueStore`**. Traffic zu **Apple iCloud**. Copy-sutra **nicht** enthalten.

## Berechtigungen

iLiezi fordert Berechtigungen nur an, wenn eine Funktion diese benötigt:

| Erlaubnis | Wann | Warum |
|------------|------|-----|
| Benachrichtigungen | Sie aktivieren Daily Sutra reminders | Lokale Planung of reminder notifications |
| Fotomediathek (nur Hinzufügen) | Dharma-Karte speichern/exportieren | Gerendetes Bild/PDF; kein Vollzugriff |
| iCloud | Sync aktivieren | Favoriten/Listen/Verlauf/Mastery/Notizen/Chant |
| Live Activities (iOS) | Reading/Chant Live Activity | Lesen/Chant auf Sperrbildschirm |
| Hintergrundaudio (Fähigkeit) | Sie aktivieren die Hintergrundrezitation | TTS fortsetzen, wenn die App nicht im Vordergrund ist |

Wir fordern **keine** Kontakte, den genauen Standort, die Kamera, das Mikrofon (über die System-TTS-Wiedergabe hinaus) oder die Nachverfolgung an.

## Was wir nicht tun

- Wir verkaufen **keine** personenbezogene Daten.
- Wir erstellen **keine** Werbeprofile.
- Wir benötigen **kein** Konto oder Social-Login.
- Wir betten zur Datenerfassung **keine** Werbung, Analysen oder soziale SDKs von Drittanbietern ein.
- **Kein** Zugriff auf Fotomediathek über **nur Hinzufügen** hinaus beim Speichern.
- Wir erhalten **keine** Nummern von StoreKit-Zahlungskarten (Apple verarbeitet Zahlungen).
- **Keine** Wahrsagerei oder bezahlte Segens-Commerce aus religiösen Inhalten.

## Privatsphäre von Kindern

iSutra erhebt wissentlich keine Daten, auch nicht von Kindern unter 13. Kein Backend, kein Kinderprofil.

## Dritte Parteien

- **Apple** — App Store-Verteilung, optionale StoreKit-Käufe, optionales iCloud-KVS, System-TTS, von Ihnen ausgewählte Share Sheet-Ziele, und Betriebssystem-gestützte Zustellung für Benachrichtigungen / Live-Aktivitäten / Siri / Kurzbefehle.
- **Keine weiteren Drittanbieter-SDKs** für Werbung, Analysen oder Social-Login sind zur Datenerfassung enthalten.

## Internationale Nutzer

Die App ist darauf ausgelegt, offline auf Ihrem Gerät zu funktionieren. Optionale Apple-Dienste unterliegen den Bedingungen von Apple und der regionalen Verfügbarkeit.

## Datenaufbewahrung & Löschung

- **Auf dem Gerät** — Lokale Einstellungen und Fortschritte bleiben erhalten, bis Sie sie in der App löschen (falls verfügbar), das Gerät zurücksetzen oder die App deinstallieren.
- **iCloud (optional)** — Daten, die Sie synchronisiert haben, bleiben in **Ihrem** iCloud-Konto gemäß den Richtlinien von Apple, bis Sie die Synchronisation deaktivieren und/oder sie über Apples Tools löschen.
- **iHTC Studio** — Da wir keine persönlichen Daten auf unseren Servern sammeln, gibt es keinen Kontodatensatz, den wir auf Anfrage löschen könnten, abgesehen davon, Ihre E-Mail-Fragen zu beantworten.

## Änderungen an dieser Richtlinie

Wir können diese Datenschutzrichtlinie von Zeit zu Zeit aktualisieren. Das Datum „Zuletzt aktualisiert“ oben wird sich ändern, und die überarbeitete Richtlinie wird auf dieser Seite der Datenschutzrichtlinie veröffentlicht.

## Kontaktieren Sie uns

Wenn Sie Fragen zu dieser Datenschutzrichtlinie oder zu Datenschutzpraktiken haben:

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Wir antworten normalerweise innerhalb von 48 Stunden.

</section>
<section lang="fr" markdown="1">

**Dernière mise à jour :** 18 août 2026

iHTC Studio (« nous ») a développé **iSutra** (« 爱佛经 » / « 爱佛经 », Bundle ID `com.iHTCboy.iSutra`). Cette politique de confidentialité explique quelles données sont (ou ne sont pas) traitées lorsque vous utilisez l’app. **Apple App Review** et les utilisateurs peuvent s’appuyer sur **cette page** comme politique publique. Pour App Store Connect, ouvrez cette page dans le navigateur et copiez l’URL depuis la barre d’adresse (le domaine public peut changer).

## Résumé (alignement sur l'étiquette nutritionnelle de confidentialité Apple)

| Sujet | Notre pratique |
|-------|----------------|
| Compte | **Non requis** — pas d'inscription, de connexion par e-mail ou de numéro de téléphone |
| Collecte de données par iHTC Studio | **Données non collectées** — nous n'exploitons **pas** de backend qui reçoit vos données personnelles |
| Réseau | Bibliothèque, reading, recite, Study Hall, Hunt, chant, practice, widgets, and daily notifications work **offline** after install fonctionnent **hors ligne** après l’installation |
| Analyses / publicités / suivi | **Aucun** — pas de SDK tiers d'analyse, de publicité ou de suivi ; pas d'utilisation de la transparence du suivi des applications |
| Services Apple facultatifs | **iCloud** (your private KVS), **Photo Library (Add Only)** for Dharma cards / exports, **StoreKit** for pourboire facultatif, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default) |

## Collecte de données

Nous ne collectons, vendons ou partageons **pas** d'informations personnelles à des fins publicitaires ou analytiques.

- **Aucun compte** — Vous pouvez utiliser toutes les fonctionnalités principales sans créer de compte chez nous.
- **Aucune analyse ni publicité** — Le binaire de l'application n'intègre pas de SDK tiers d'analyse, de publicité ou de rapport d'erreur qui nous contactent.
- **Aucun envoi de contenu** — Vos reading history, favorites, lists, notes, mastery, streaks, chant counts, practice checklists, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## Comment fonctionne l'application

- **Bibliothèque incluse** — JSON texte, vernaculaire/anglais, index et aides d’étude sont dans le bundle app/widget. Parcourir et étudier ne nécessite pas le réseau.
- **Voix sur l’appareil** — **AVSpeechSynthesizer**. Pas de texte de sutra à iHTC Studio.
- **Widgets et App Group** — Les widgets et l’app partagent des préférences et un état léger via l’App Group `group.com.iHTCboy.iSutra` sur votre appareil.
- **Notifications quotidiennes** — Planifiées localement avec les notifications utilisateur. Appuyer sur une notification ouvre un lien profond vers un identifiant de passage sur l'appareil ; pas de distribution du serveur.
- **Cartes Dharma / export** — images et PDF sur l’appareil. **Photothèque (ajout uniquement)** à l’enregistrement.
- **Copie de sutra (iOS)** — traits PencilKit dans Application Support (`CopySutra/…`). **Pas** dans App Group, **pas** de sync iCloud.
- **Conseil facultatif** — « Tip Developer » est un achat de consommable **StoreKit** traité par Apple. Nous ne recevons pas les détails de votre carte de paiement.
- **Siri / Raccourcis / Centre de contrôle** — Les intégrations système facultatives ouvrent des liens profonds sur l'appareil ; ils ne nous envoient pas votre bibliothèque.
- **Spotlight facultatif** — Désactivé par défaut. Si vous activez l'indexation, le contenu est indexé par le système sur l'appareil pour la recherche locale ; nous n'exploitons pas de backend de recherche.

## Données stockées sur votre appareil

| Données | Où | Objectif |
|------|-------|--------------|
| Base sutras (index, shards) | Bundle App / Widget | Lecture et étude hors ligne |
| Favoris et listes (经单) | UserDefaults de l’App Group | Passages favoris et listes utilisateur |
| Historique de lecture / dernière lecture | Paramètres par défaut du groupe d'applications | Continuer la lecture, historique de l'interface utilisateur |
| Progression d’étude et maîtrise | UserDefaults de l’App Group | Study Hall state, quiz / Hunt progress |
| Notes | UserDefaults de l’App Group | Notes de passages |
| Séquence d'entraînement / enregistrement | Paramètres par défaut du groupe d'applications | Habitude quotidienne |
| Compteurs de chant et son | UserDefaults de l’App Group | Wooden-fish, objectifs, tons |
| Pratique matin/soir | UserDefaults de l’App Group | Checklist liturgie |
| Apparence et préférences de lecture | Paramètres par défaut du groupe d'applications | Thème, accent, langue, mise en page, TTS, onglets, widgets |
| Daily Sutra cache & notification prefs | UserDefaults de l’App Group | ID du jour, schedule time |
| Préférences de carte partagée | Paramètres par défaut du groupe d'applications | Derniers choix de style/ratio |
| Dessins Copy-sutra (iOS) | Application Support (`CopySutra/`) | Brouillons par ligne |
| État d’intégration et de TipKit | Paramètres utilisateur standard (appareil) | Guide d'accueil / conseils découverte |
| Actions rapides sur l'écran d'accueil | Système + préférences locales | Raccourcis que vous configurez |
| Instantanés Widget / Live Activity | App Group / ActivityKit | Texte/chant déjà ouverts |

La désinstallation de l'application supprime les données du bac à sable et du groupe d'applications associées à l'application (selon le comportement d'iOS/macOS). Les copies facultatives dans iCloud restent dans **votre** iCloud jusqu'à ce que vous les supprimiez ou que vous désactiviez la synchronisation et supprimiez ailleurs.

## Synchronisation iCloud (Facultative)

Avec **iCloud Sync**, miroir via **`NSUbiquitousKeyValueStore`**. Trafic vers **Apple iCloud**. Copy-sutra **non** inclus.

## Autorisations

iLiezi demande des autorisations uniquement lorsqu'une fonctionnalité en a besoin :

| Autorisation | Quand | Pourquoi |
|------------|------|-----|
| Notifications | Vous activez Daily Sutra reminders | Planification locale of reminder notifications |
| Photothèque (ajout uniquement) | Carte Dharma/enregistrement | Image/PDF rendu ; pas de lecture complète |
| iCloud | Activez la sync | Favoris/listes/historique/maîtrise/notes/chant |
| Live Activities (iOS) | Reading/Chant Live Activity | Lecture/chant sur écran verrouillé |
| Audio de fond (capacité) | Vous activez la récitation en arrière-plan | Continuer TTS lorsque l'application n'est pas au premier plan |

Nous ne demandons **pas** de contacts, de localisation précise, de caméra, de microphone (au-delà de la lecture TTS du système) ou de suivi.

## Ce que nous ne faisons pas

- Nous ne vendons **pas** de données personnelles.
- Nous ne créons **pas** de profils publicitaires.
- Nous n'exigeons **pas** de compte ou de connexion sociale.
- Nous n'intégrons **pas** de publicités tierces, d'analyses ou de SDK sociaux pour la collecte de données.
- **Pas** d’accès à Photothèque au-delà de **l’ajout uniquement** lors de l’enregistrement.
- Nous ne recevons **pas** de numéros de carte de paiement StoreKit (Apple traite les paiements).
- **Pas** de divination ni commerce de bénédictions payantes à partir du contenu religieux.

## Confidentialité des enfants

iSutra ne collecte pas sciemment de données, y compris enfants de moins de 13 ans.

## Tiers

- **Apple** — Distribution via l'App Store, achats facultatifs via StoreKit, KVS iCloud facultatif, synthèse vocale système, destinations du partage choisies par vous, et notifications / Live Activity / Siri / Raccourcis au niveau du système d'exploitation.
- **Aucun autre SDK tiers** pour la publicité, l'analyse ou la connexion sociale n'est inclus pour la collecte de données.

## Utilisateurs internationaux

L'application est conçue pour fonctionner hors ligne sur votre appareil. Les services Apple optionnels suivent les conditions et la disponibilité régionale d'Apple.

## Conservation et suppression des données

- **Sur l'appareil** — Les préférences locales et la progression restent jusqu'à ce que vous les effaciez dans l'application (lorsque disponible), que vous réinitialisiez l'appareil ou que vous désinstalliez l'application.
- **iCloud (facultatif)** — Les données que vous avez synchronisées restent dans **votre** compte iCloud selon les politiques d’Apple jusqu’à ce que vous désactiviez la synchronisation et/ou les effaciez via les outils d’Apple.
- **iHTC Studio** — Comme nous ne collectons pas de données personnelles sur nos serveurs, il n’existe aucun jeu de données de compte que nous puissions supprimer sur demande, hormis répondre à vos questions par email.

## Modifications de cette politique

Nous pouvons mettre à jour cette politique de confidentialité de temps à autre. La date « Dernière mise à jour » en haut changera, et la politique révisée sera publiée sur cette page de politique de confidentialité.

## Contactez-nous

Si vous avez des questions concernant cette politique de confidentialité ou nos pratiques en matière de confidentialité :

- **Email :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Nous répondons généralement sous 48 heures.

</section>
<section lang="tr" markdown="1">

**Son güncelleme:** 18 Ağustos 2026

iHTC Studio ("biz"), **iSutra** ("爱佛经" / "爱佛经", Bundle ID `com.iHTCboy.iSutra`) uygulamasını geliştirdi. Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlendiğini (ve işlenmediğini) açıklar. **Apple App Review** ve kullanıcılar **bu sayfayı** herkese açık gizlilik politikası olarak kullanabilir. App Store Connect için tarayıcıda bu sayfayı açın ve adres çubuğundan URL’yi kopyalayın (genel site alan adı zamanla değişebilir).

## Özet (Apple Gizlilik Beslenme Etiketi uyumu)

| Konu | Uygulamamızın uygulaması |
|-------|----------------|
| Hesap | **Gerekli değil** — kayıt, e-posta ile giriş veya telefon numarası yok |
| iHTC Studio tarafından veri toplama | **Veri Toplanmıyor** — kişisel verilerinizi alan bir arka uç işletmiyoruz |
| Ağ | Kütüphane, reading, recite, Study Hall, Hunt, chant, practice, widgets, and daily notifications work **offline** after install kurulumdan sonra **çevrimdışı** çalışır |
| Analitik / reklam / izleme | **Yok** — üçüncü taraf analitik, reklam veya izleme SDK'ları yok; Uygulama İzleme Şeffaflığı kullanılmaz |
| İsteğe bağlı Apple hizmetleri | **iCloud** (your private KVS), **Photo Library (Add Only)** for Dharma cards / exports, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default) |

## Veri Toplama

Kişisel bilgileri reklam veya analiz için **toplamıyoruz**, satmıyoruz veya paylaşmıyoruz.

- **Hesap gerekmez** — Tüm temel özellikleri bizde hesap oluşturmadan kullanabilirsiniz.
- **Analitik veya reklam yok** — Uygulama ikili dosyası üçüncü taraf analitik, reklam veya çökme bildirim SDK'larını içermez, telefonla bize veri göndermez.
- **İçerik yüklenmez** — reading history, favorites, lists, notes, mastery, streaks, chant counts, practice checklists, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## Uygulama Nasıl Çalışır

- **Paketlenmiş kitaplık** — Metin JSON, vernacular/English, dizinler ve çalışma yardımcıları uygulama/widget paketinin içindedir. Gezinme ve çalışma için ağ gerekmez.
- **Cihaz içi konuşma** — **AVSpeechSynthesizer**. Sutra metni gönderilmez.
- **Widget'lar ve App Group** — Widget'lar ve uygulama, cihazınızdaki `group.com.iHTCboy.iSutra` App Group'u üzerinden tercihleri ve hafif durumu paylaşır.
- **Günlük bildirimler** — Kullanıcı Bildirimleriyle yerel olarak planlanır. Bir bildirime dokunulduğunda cihazdaki pasaj kimliğine giden derin bağlantı açılır; sunucu çıkışı yok.
- **Dharma kartları / dışa aktarma** — görseller/PDF cihazda. Kayıtta **Fotoğraf Kitaplığı (yalnızca ekleme)**.
- **Sutra kopyalama (iOS)** — PencilKit konturları Application Support (`CopySutra/…`). **App Group’ta değil**, **iCloud senkronu yok**.
- **İsteğe bağlı ipucu** — "İpucu Geliştirici", Apple tarafından gerçekleştirilen bir **StoreKit** sarf malzemesidir. Ödeme kartı bilgilerinizi almıyoruz.
- **Siri / Kısayollar / Kontrol Merkezi** — İsteğe bağlı sistem entegrasyonları cihazdaki derin bağlantıları açar; kütüphanenizi bize göndermiyorlar.
- **İsteğe Bağlı Spot Işığı** — Varsayılan olarak kapalıdır. Dizin oluşturmayı etkinleştirirseniz içerik, yerel arama için cihazdaki sistem tarafından dizine eklenir; bir arama arka ucu kullanmıyoruz.

## Cihazınızda Saklanan Veriler

| Veri | Nerede | Amaç |
|------|-------|-------------|
| Sutra DB (indeks, parçalar) | App / Widget paketi | Çevrimdışı okuma ve çalışma |
| Favoriler ve listeler (经单) | App Group UserDefaults | Yıldızlı pasajlar ve kullanıcı listeleri |
| Okuma geçmişi / son okuma | Uygulama Grubu Kullanıcı Varsayılanları | Okumaya devam et, geçmiş kullanıcı arayüzü |
| Çalışma ilerlemesi ve ustalık | App Group UserDefaults | Study Hall state, quiz / Hunt progress |
| Notlar | App Group UserDefaults | Pasaj notları |
| Antrenman serisi / check-in | Uygulama Grubu Kullanıcı Varsayılanları | Günlük alışkanlık |
| Chant sayıları ve ses | App Group UserDefaults | Wooden-fish, hedefler, tonlar |
| Sabah/akşam uygulama | App Group UserDefaults | Günlük liturji listesi |
| Görünüm ve okuma tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Tema, aksan, dil, düzen, TTS, sekmeler, widget'lar |
| Daily Sutra cache & notification prefs | App Group UserDefaults | Bugünün ID’si, schedule time |
| Paylaşımlı kart tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Son stil/oran seçenekleri |
| Copy-sutra çizimleri (iOS) | Application Support (`CopySutra/`) | Satır başına taslak |
| İlk katılım ve TipKit durumu | Standart Kullanıcı Varsayılanları (cihaz) | Hoş geldiniz kılavuzu / keşif ipuçları |
| Ana Ekran hızlı eylemler | Sistem + yerel tercihler | Yapılandırdığınız kısayollar |
| Widget / Live Activity anlık görüntüleri | App Group / ActivityKit | Açılmış metin/chant durumu |

Uygulamayı kaldırmak, uygulamayla ilişkili sandbox ve Uygulama Grubu verilerini kaldırır (iOS/macOS davranışına tabidir). İsteğe bağlı iCloud kopyaları, siz temizleyene veya senkronizasyonu kapatıp başka yerde silene kadar **iCloud’unuzda** kalır.

## iCloud Senkronizasyonu (İsteğe Bağlı)

**iCloud Sync** ile **`NSUbiquitousKeyValueStore`**. **Apple iCloud**’a. Copy-sutra **dahil değil**.

## İzinler

iLiezi yalnızca bir özellik ihtiyaç duyduğunda izin ister:

| İzin | Ne zaman | neden |
|------------|------|-----|
| Bildirimler | Daily Sutra reminders etkinleştirirsiniz | Yerel zamanlama of reminder notifications |
| Fotoğraf Kitaplığı (yalnızca ekleme) | Dharma kartı/kaydet | İşlenmiş görsel/PDF; tam okuma yok |
| iCloud | Senkronizasyonu açarsınız | Favoriler/listeler/geçmiş/ustalık/notlar/chant |
| Live Activities (iOS) | Reading/Chant Live Activity | Okuma/chant Kilit Ekranı |
| Arka planda ses (yetenek) | Arka planda okumayı etkinleştirirsiniz | Uygulama ön planda olmadığında TTS'ye devam edin |

Kişiler, kesin Konum, Kamera, Mikrofon (sistem TTS oynatmanın ötesinde) veya İzleme **talebi etmeyiz**.

## Ne Yapmıyoruz

- Kişisel verileri **satmıyoruz**.
- Reklam profilleri **oluşturmuyoruz**.
- Bir hesaba veya sosyal girişe **gerek duymayız**.
- Veri toplama amacıyla üçüncü taraf reklamları, analizleri veya sosyal SDK'ları **yerleştirmeyiz**.
- Kaydetme dışında **yalnızca ekleme** ötesinde Fotoğraf Kitaplığı erişimi **yok**.
- StoreKit ödeme kartı numaralarını **almıyoruz** (ödemeleri Apple işler).
- Dini içeriği fal veya ücretli bereket ticaretine **dönüştürmeyiz**.

## Çocukların Gizliliği

iSutra bilerek veri toplamaz; 13 yaş altı dahil. Backend yok.

## Üçüncü Taraflar

- **Apple** — App Store dağıtımı, isteğe bağlı StoreKit satın alımları, isteğe bağlı iCloud KVS, sistem TTS, sizin seçtiğiniz Paylaşım Sayfası hedefleri ve işletim sistemi düzeyinde bildirim / Canlı Aktivite / Siri / Kestirmeler teslimi.
- Reklam, analiz veya sosyal giriş için başka hiçbir üçüncü taraf SDK’sı veri toplama amacıyla dahil edilmemiştir.

## Uluslararası Kullanıcılar

Uygulama, cihazınızda çevrimdışı çalışacak şekilde tasarlanmıştır. İsteğe bağlı Apple hizmetleri Apple’ın şartlarına ve bölgesel kullanılabilirliğe tabidir.

## Veri Saklama ve Silme

- **Cihazda** — Yerel tercih ve ilerleme, uygulama içinden (varsa) temizleyene, cihazı sıfırlayana veya uygulamayı kaldırana kadar kalır.
- **iCloud (isteğe bağlı)** — Senkronize ettiğiniz veriler, Apple’ın politikaları uyarınca, senkronizasyonu devre dışı bırakana ve/veya Apple’ın araçlarıyla temizleyene kadar **iCloud** hesabınızda kalır.
- **iHTC Studio** — Sunucularımızda kişisel veri toplamadığımız için, e-posta sorularınıza cevap vermenin ötesinde silinebilecek bir hesap veri setimiz yoktur.

## Bu Politika ile İlgili Değişiklikler

Bu Gizlilik Politikasını zaman zaman güncelleyebiliriz. En üstteki "Son güncelleme" tarihi değişecek ve revize edilmiş politika bu Gizlilik Politikası sayfasında yayınlanacaktır.

## İletişim

Bu Gizlilik Politikası veya gizlilik uygulamaları hakkında sorularınız varsa:

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Genellikle 48 saat içinde yanıt veririz.

</section>
