---
layout: doc
title: iPrecepts — Privacy Policy
app_id: iPrecepts
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iPrecepts (爱家训) — fully offline, Data Not Collected, optional iCloud and Photo Library add-only.
---

<section lang="en" markdown="1">

**Last updated:** September 3, 2026

iHTC Studio ("we", "us" or "our") built **iPrecepts** (also known as "爱家训 / 愛家訓", Bundle ID `com.iHTCboy.iPrecepts`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on **this page** as the public privacy policy for the app. For App Store Connect, open this Privacy Policy in your browser and copy the address from the address bar (the public site domain may change over time).

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration, email sign-in, or phone number |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your personal data |
| Network | Library, reading, recite, Family Study, widgets, and daily notifications work **offline** after install |
| Analytics / ads / tracking | **None** — no third-party analytics, advertising, or tracking SDKs; no App Tracking Transparency use |
| Optional Apple services | **iCloud** (your private KVS), **Photo Library (Add Only)** for precept cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **on-device handwriting** (Vision) |

## Data Collection

We do **not** collect, sell, or share personal information for advertising or analytics.

- **No account** — You can use all core features without creating an account with us.
- **No analytics or ads** — The app binary does not integrate third-party analytics, advertising, or crash-reporting SDKs that phone home to us.
- **No content upload** — Your reading history, favorites, lists, notes, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## How the App Works

- **Bundled library** — Text JSON, vernacular/English, indexes, and study aids ship inside the app / widget bundle. Browsing and study do not require a network request.
- **On-device speech** — Recitation uses Apple’s system **AVSpeechSynthesizer** (TTS). We do not send passage text to iHTC Studio.
- **Widgets & App Group** — Widgets and the app share preferences and lightweight state via App Group `group.com.iHTCboy.iPrecepts` on your device.
- **Daily notifications** — Scheduled locally with User Notifications. Tapping a notification opens a deep link to a passage ID on device; no server fan-out.
- **Precept cards** — Images are rendered on device. Saving uses **Photo Library add-only** only when you tap save. System Share Sheet may send the image to an app **you** choose; that destination’s privacy policy then applies.
- **Handwriting search (iOS)** — Optional character recognition uses Apple **Vision** on device. Strokes are not uploaded.
- **Optional tip** — “Tip Developer” is a consumable **StoreKit** purchase processed by Apple. We do not receive your payment card details.
- **Siri / Shortcuts / Control Center** — Optional system integrations open on-device deep links; they do not send your library to us.
- **Optional Spotlight** — If you enable indexing, content is indexed by the system on device for local search; we do not operate a search backend.

## Data Stored on Your Device

| Data | Where | Purpose |
|------|-------|---------|
| Precept database | App / Widget bundle | Offline reading & study |
| Favorites & lists (训单) | App Group UserDefaults | Starred passages and user lists |
| Reading history / last read | App Group UserDefaults | Continue reading, history UI |
| Notes | App Group UserDefaults | Reading notes you write |
| Study progress & mastery | App Group UserDefaults | Family Study state, quiz / Hunt progress |
| Practice streak / check-in | App Group UserDefaults | Daily habit |
| Appearance & reading prefs | App Group UserDefaults | Theme, accent, language, layout, TTS, tabs, widgets, font scale |
| Daily Precept cache & notification prefs | App Group UserDefaults | Today’s ID, schedule time, contextual toggle |
| Card preferences | App Group UserDefaults | Last style / ratio choices |
| Onboarding & TipKit state | Standard UserDefaults (device) | Welcome guide / discovery tips |
| Recent searches | Standard UserDefaults (device) | Search history you typed |
| Home Screen quick actions | System + local prefs | Shortcuts you configure |
| Widget / Live Activity snapshots | App Group / ActivityKit | Display text you already opened |

Uninstalling the app removes sandbox and App Group data associated with the app (subject to iOS/macOS behavior). Optional iCloud copies remain in **your** iCloud until you clear them or turn sync off and delete elsewhere.

## iCloud Sync (Optional)

If you enable **iCloud Sync** in Settings, the app mirrors selected user data through Apple’s **`NSUbiquitousKeyValueStore`** tied to **your Apple ID**:

- Favorites
- Lists (训单)
- Reading history
- Study progress / mastery
- Practice streaks
- Notes

Sync traffic goes to **Apple iCloud**, not to iHTC Studio. You can disable sync in Settings. We cannot read your iCloud contents.

## Permissions

iPrecepts requests permissions only when a feature needs them:

| Permission | When | Why |
|------------|------|-----|
| Notifications | You enable Daily Precept reminders | Local scheduling of reminder notifications |
| Photo Library (Add Only) | You save a card | Write the rendered image; we do not need full library read access |
| iCloud | You enable sync | Sync favorites / lists / history / progress / streaks / notes |
| Live Activities (iOS) | You enable Reading Live Activity | Show the passage you are reading on Lock Screen / Dynamic Island |
| Background audio (capability) | You enable background recitation | Continue TTS when the app is not foreground |

We do **not** request Contacts, precise Location, Camera, Microphone (beyond system TTS playback), or Tracking. Handwriting search uses on-device Vision and does not require a network permission prompt.

## What We Do Not Do

- We do **not** sell personal data.
- We do **not** build advertising profiles.
- We do **not** require an account or social login.
- We do **not** embed third-party ad, analytics, or social SDKs for data collection.
- We do **not** access your Photo Library beyond **add-only** when you choose to save a card.
- We do **not** receive StoreKit payment card numbers (Apple processes payments).
- We do **not** upload handwriting strokes or passage text to iHTC Studio.

## Children’s Privacy

iPrecepts is an educational literacy app for a general audience and is **not** in the Kids Category. We do not knowingly collect personal information from children. The app does not require an account. Families may use reading and study features offline on their own devices.

## Third Parties

- **Apple** — App Store distribution, optional StoreKit purchases, optional iCloud KVS, system TTS, Share Sheet destinations you pick, and OS-level notification / Live Activity / Siri / Shortcuts / Vision delivery.
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

**最近更新：** 2026 年 9 月 3 日

爱火腿肠工作室（iHTC Studio）（「我们」）开发了 **爱家训**（iPrecepts / 愛家訓，Bundle ID `com.iHTCboy.iPrecepts`）。本隐私政策说明你在使用本应用时，数据如何被处理（以及**不会**如何被处理）。本页可作为 **App Store 审核**与用户查阅的公开隐私政策。填写 App Store Connect 时，请在浏览器打开本 [隐私政策](../privacy) 页，从地址栏复制当前网址（站点域名日后可能变更，请勿依赖文档中的固定域名）。

## 概要（对齐 App Store 隐私标签）

| 主题 | 我们的做法 |
|------|------------|
| 账号 | **不需要**——无需注册、邮箱登录或手机号 |
| iHTC Studio 收集数据 | **不收集数据（Data Not Collected）**——我们**不**运营接收你个人数据的后端 |
| 网络 | 语料、阅读、诵读、家训学堂、小组件与每日通知在安装后可**离线**使用 |
| 分析 / 广告 / 追踪 | **无**——无第三方分析、广告或追踪 SDK；不使用跨 App 追踪 |
| 可选 Apple 服务 | **iCloud**（你的私有键值存储）、保存训卡时的**相簿（仅加入）**、可选 **StoreKit** 打赏、**本地通知**、可选**实时活动**、可选本机**手写识别**（Vision） |

## 数据收集

我们**不**收集、出售或出于广告 / 分析目的共享个人信息。

- **无账号** — 核心功能无需向我们注册。
- **无分析或广告** — 应用未集成会向我们回传的第三方分析、广告或崩溃上报 SDK。
- **不上传内容** — 阅读历史、收藏、训单、笔记、学堂进度与偏好留在本机（以及可选的**你的** iCloud）。它们不会上传到 iHTC Studio 服务器，因为**我们不为该 App 运营此类服务器**。

## 应用如何工作

- **内置语料** — 正文 JSON、白话 / 英译、索引与学习辅助随 App / 小组件包分发。浏览与学堂**无需**网络请求。
- **本机语音** — 诵读使用系统 **AVSpeechSynthesizer**（TTS）。我们不会把正文发到 iHTC Studio。
- **小组件与 App Group** — 小组件与主应用通过本机 App Group `group.com.iHTCboy.iPrecepts` 共享偏好与轻量状态。
- **每日通知** — 使用 User Notifications **本机排程**。点按通知会打开指向本机篇目 ID 的深链，没有服务端推送名单。
- **训卡** — 图片在本机渲染。仅在你点保存时使用**相簿仅加入**。系统分享表可能把图片发到**你选择**的 App，随后适用该目标的隐私政策。
- **手写搜索（iOS）** — 可选字形识别使用 Apple **Vision**，在本机完成。笔迹不上传。
- **可选打赏** — 「打赏开发者」为消耗型 **StoreKit** 购买，由 Apple 处理。我们收不到银行卡号。
- **Siri / 快捷指令 / 控制中心** — 可选系统集成打开本机深链，不会把语料发给我们。
- **可选 Spotlight** — 若开启索引，由系统在本机建立搜索索引；我们不运营搜索后端。

## 本机存储的数据

| 数据 | 位置 | 用途 |
|------|------|------|
| 家训语料 | App / Widget Bundle | 离线阅读与学堂 |
| 收藏与训单 | App Group UserDefaults | 星标与自订列表 |
| 浏览纪录 / 最近阅读 | App Group UserDefaults | 继续阅读与历史 |
| 笔记 | App Group UserDefaults | 你写下的阅读心得 |
| 学堂进度与掌握度 | App Group UserDefaults | 家训学堂状态、测验 / 寻训进度 |
| 打卡 | App Group UserDefaults | 每日习惯 |
| 外观与阅读偏好 | App Group UserDefaults | 主题、强调色、语言、版面、朗读、Tab、小组件、字级 |
| 今日一训缓存与通知偏好 | App Group UserDefaults | 今日 ID、提醒时间、情境开关 |
| 训卡偏好 | App Group UserDefaults | 上次风格 / 比例 |
| 引导与 TipKit 状态 | 标准 UserDefaults | 欢迎引导 / 发现提示 |
| 最近搜索 | 标准 UserDefaults | 你输入过的搜索词 |
| 主屏快捷 | 系统 + 本机偏好 | 你设定的快捷 |
| 小组件 / 实时活动快照 | App Group / ActivityKit | 展示你已打开的正文 |

解除安装会清除与该 App 相关的沙盒与 App Group 数据（以系统行为为准）。可选 iCloud 副本仍留在**你的** iCloud。

## iCloud 同步（可选）

若你在设置中开启 **iCloud 同步**，应用会通过绑定**你的 Apple ID** 的 Apple **`NSUbiquitousKeyValueStore`** 镜像：收藏、训单、阅读历史、学堂进度／掌握度、打卡与笔记。同步流量走向 **Apple iCloud**，而不是 iHTC Studio。我们无法读取你的 iCloud 内容。

## 权限

仅在功能需要时请求：

| 权限 | 何时 | 原因 |
|------|------|------|
| 通知 | 你开启今日一训提醒 | 本地排程提醒 |
| 相簿（仅加入） | 你保存训卡 | 写入渲染图片；无需读取全部照片 |
| iCloud | 你开启同步 | 同步收藏／训单／历史／进度／打卡／笔记 |
| 实时活动（iOS） | 你开启品读实时活动 | 在锁定屏幕／灵动岛显示正在品读的篇目 |
| 背景音频能力 | 你开启背景诵读 | App 不在前台时继续 TTS |

我们**不**请求通讯录、精确位置、相机、麦克风（除系统 TTS 播放外）或追踪权限。手写搜索使用本机 Vision，不会弹出网络权限。

## 我们明确不做的事

- **不**出售个人数据。
- **不**建立广告画像。
- **不**要求账号或社交登录。
- **不**嵌入用于数据收集的第三方广告、分析或社交 SDK。
- **不**在你主动保存训卡之外访问照片（且仅为「加入」）。
- **不**接收 StoreKit 银行卡号码（由 Apple 处理付款）。
- **不**把手写笔迹或正文上传到 iHTC Studio。

## 儿童隐私

爱家训是面向一般受众的语文学习应用，**不属于儿童类别**。我们不会故意收集包括 13 岁以下（或你所在地区同等年龄）儿童在内的任何人的个人信息。应用不需要账号。家庭可在自有设备上离线使用阅读与学堂功能。

## 第三方

- **Apple** — App Store 分发、可选 StoreKit 购买、可选 iCloud、系统 TTS、你选择的分享目标，以及系统通知／实时活动／Siri／快捷指令／Vision。
- **无其他**用于广告、分析或社交登录的第三方数据收集 SDK。

## 国际使用者

应用设计为在你的设备上离线运行。可选 Apple 服务遵循 Apple 条款与地区可用性。

## 数据保留与删除

- **本机** — 偏好与进度保留至你在应用内清除（如有入口）、重置设备或卸载应用。
- **iCloud（可选）** — 你同步的数据按 Apple 政策留在**你的** iCloud，直到关闭同步并／或通过 Apple 工具清理。
- **iHTC Studio** — 我们不在自有服务器收集个人数据，因此没有可供删除的账号数据集；隐私疑问可通过邮件联络。

## 政策变更

我们可能不时更新本政策。页首「最近更新」日期会随之变化，修订版将发布于本隐私政策页面。

## 联系我们

如对本隐私政策或隐私实务有疑问：

- **电子邮件：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

通常 48 小时内回复。

</section>
<section lang="zh-TW" markdown="1">

**最近更新：** 2026 年 9 月 3 日

愛火腿腸工作室（iHTC Studio）（「我們」）開發了 **愛家訓**（iPrecepts / 爱家训，Bundle ID `com.iHTCboy.iPrecepts`）。本隱私政策說明你在使用本應用時，資料如何被處理（以及**不會**如何被處理）。本頁可作為 **App Store 審核**與使用者查閱的公開隱私政策。填寫 App Store Connect 時，請在瀏覽器打開本 [隱私政策](../privacy) 頁，從網址列複製目前網址（站點網域日後可能變更，請勿依賴文件中的固定網域）。

## 概要（對齊 App Store 隱私標籤）

| 主題 | 我們的做法 |
|------|------------|
| 帳號 | **不需要**——無需註冊、郵箱登入或手機號 |
| iHTC Studio 收集資料 | **不收集資料（Data Not Collected）**——我們**不**營運接收你個人資料的後端 |
| 網路 | 語料、閱讀、誦讀、家訓學堂、小工具與每日通知在安裝後可**離線**使用 |
| 分析 / 廣告 / 追蹤 | **無**——無第三方分析、廣告或追蹤 SDK；不使用跨 App 追蹤 |
| 可選 Apple 服務 | **iCloud**（你的私有鍵值儲存）、儲存訓卡時的**相簿（僅加入）**、可選 **StoreKit** 打賞、**本地通知**、可選**即時動態**、可選本機**手寫辨識**（Vision） |

## 資料收集

我們**不**收集、出售或出於廣告／分析目的共享個人資訊。

- **無帳號** — 核心功能無需向我們註冊。
- **無分析或廣告** — 應用未整合會向我們回傳的第三方分析、廣告或當機回報 SDK。
- **不上傳內容** — 閱讀歷史、收藏、訓單、筆記、學堂進度與偏好留在本機（以及可選的**你的** iCloud）。它們不會上傳到 iHTC Studio 伺服器，因為**我們不為該 App 營運此類伺服器**。

## 應用如何工作

- **內建語料** — 正文 JSON、白話／英譯、索引與學習輔助隨 App／小工具包分發。瀏覽與學堂**無需**網路請求。
- **本機語音** — 誦讀使用系統 **AVSpeechSynthesizer**（TTS）。我們不會把正文發到 iHTC Studio。
- **小工具與 App Group** — 小工具與主應用透過本機 App Group `group.com.iHTCboy.iPrecepts` 共享偏好與輕量狀態。
- **每日通知** — 使用 User Notifications **本機排程**。點按通知會打開指向本機篇目 ID 的深鏈，沒有伺服器推送名單。
- **訓卡** — 圖片在本機渲染。僅在你點儲存時使用**相簿僅加入**。系統分享表可能把圖片發到**你選擇**的 App，隨後適用該目標的隱私政策。
- **手寫搜尋（iOS）** — 可選字形辨識使用 Apple **Vision**，在本機完成。筆跡不上傳。
- **可選打賞** — 「打賞開發者」為消耗型 **StoreKit** 購買，由 Apple 處理。我們收不到銀行卡號。
- **Siri / 捷徑 / 控制中心** — 可選系統整合打開本機深鏈，不會把語料發給我們。
- **可選 Spotlight** — 若開啟索引，由系統在本機建立搜尋索引；我們不營運搜尋後端。

## 本機儲存的資料

| 資料 | 位置 | 用途 |
|------|------|------|
| 家訓語料 | App / Widget Bundle | 離線閱讀與學堂 |
| 收藏與訓單 | App Group UserDefaults | 星標與自訂列表 |
| 瀏覽紀錄 / 最近閱讀 | App Group UserDefaults | 繼續閱讀與歷史 |
| 筆記 | App Group UserDefaults | 你寫下的閱讀心得 |
| 學堂進度與掌握度 | App Group UserDefaults | 家訓學堂狀態、測驗 / 尋訓進度 |
| 打卡 | App Group UserDefaults | 每日習慣 |
| 外觀與閱讀偏好 | App Group UserDefaults | 主題、強調色、語言、版面、朗讀、Tab、小工具、字級 |
| 今日一訓快取與通知偏好 | App Group UserDefaults | 今日 ID、提醒時間、情境開關 |
| 訓卡偏好 | App Group UserDefaults | 上次風格 / 比例 |
| 引導與 TipKit 狀態 | 標準 UserDefaults | 歡迎引導 / 發現提示 |
| 最近搜尋 | 標準 UserDefaults | 你輸入過的搜尋詞 |
| 主畫面捷徑 | 系統 + 本機偏好 | 你設定的捷徑 |
| 小工具 / 即時動態快照 | App Group / ActivityKit | 展示你已開啟的正文 |

解除安裝會清除與該 App 相關的沙盒與 App Group 資料（以系統行為為準）。可選 iCloud 副本仍留在**你的** iCloud。

## iCloud 同步（可選）

若你在設定中開啟 **iCloud 同步**，應用會透過綁定**你的 Apple ID** 的 Apple **`NSUbiquitousKeyValueStore`** 鏡像：收藏、訓單、閱讀歷史、學堂進度／掌握度、打卡與筆記。同步流量走向 **Apple iCloud**，而不是 iHTC Studio。我們無法讀取你的 iCloud 內容。

## 權限

僅在功能需要時請求：

| 權限 | 何時 | 原因 |
|------|------|------|
| 通知 | 你開啟今日一訓提醒 | 本地排程提醒 |
| 相簿（僅加入） | 你儲存訓卡 | 寫入渲染圖片；無需讀取全部照片 |
| iCloud | 你開啟同步 | 同步收藏／訓單／歷史／進度／打卡／筆記 |
| 即時動態（iOS） | 你開啟品讀即時動態 | 在鎖定畫面／動態島顯示正在品讀的篇目 |
| 背景音訊能力 | 你開啟背景誦讀 | App 不在前景時繼續 TTS |

我們**不**請求通訊錄、精確位置、相機、麥克風（除系統 TTS 播放外）或追蹤權限。手寫搜尋使用本機 Vision，不會彈出網路權限。

## 我們明確不做的事

- **不**出售個人資料。
- **不**建立廣告畫像。
- **不**要求帳號或社交登入。
- **不**嵌入用於資料收集的第三方廣告、分析或社交 SDK。
- **不**在你主動儲存訓卡之外存取照片（且僅為「加入」）。
- **不**接收 StoreKit 銀行卡號碼（由 Apple 處理付款）。
- **不**把手寫筆跡或正文上傳到 iHTC Studio。

## 兒童隱私

愛家訓是面向一般受眾的語文學習應用，**不屬於兒童類別**。我們不會故意收集包括 13 歲以下（或你所在地區同等年齡）兒童在內的任何人的個人資訊。應用不需要帳號。家庭可在自有裝置上離線使用閱讀與學堂功能。

## 第三方

- **Apple** — App Store 分發、可選 StoreKit 購買、可選 iCloud、系統 TTS、你選擇的分享目標，以及系統通知／即時動態／Siri／捷徑／Vision。
- **無其他**用於廣告、分析或社交登入的第三方資料收集 SDK。

## 國際使用者

應用設計為在你的裝置上離線運行。可選 Apple 服務遵循 Apple 條款與地區可用性。

## 資料保留與刪除

- **本機** — 偏好與進度保留至你在應用內清除（如有入口）、重置裝置或解除安裝應用。
- **iCloud（可選）** — 你同步的資料按 Apple 政策留在**你的** iCloud，直到關閉同步並／或透過 Apple 工具清理。
- **iHTC Studio** — 我們不在自有伺服器收集個人資料，因此沒有可供刪除的帳號資料集；隱私疑問可透過郵件聯絡。

## 政策變更

我們可能不時更新本政策。頁首「最近更新」日期會隨之變化，修訂版將發佈於本隱私政策頁面。

## 聯絡我們

如對本隱私政策或隱私實務有疑問：

- **電子郵件：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

通常 48 小時內回覆。

</section>
<section lang="ja" markdown="1">

**最終更新日:** 2026年9月3日

iHTC Studio（「当社」）は **iPrecepts**（「爱家训 / 愛家訓」、Bundle ID `com.iHTCboy.iPrecepts`）を開発しました。本プライバシーポリシーは、本アプリの利用時にどのデータが取り扱われ、取り扱われないかを説明します。**Apple App Review** とユーザーは、**本ページ**を公開のプライバシーポリシーとして参照できます。App Store Connect では、ブラウザで本プライバシーポリシーを開き、アドレスバーから URL をコピーしてください（公開サイトのドomainは将来変更される場合があります）。

## 概要（Apple プライバシー栄養表示との整合性）

| トピック | 当社の方針 |
|-------|----------------|
| アカウント | **不要** — 登録、メールサインイン、電話番号は必要ありません |
| iHTC Studioによるデータ収集 | **データは収集しません** — 個人データを受け取るバックエンドは運営していません |
| ネットワーク | ライブラリ、読書、暗唱、学習、Hunt、ウィジェット、日次通知はインストール後**オフライン**で動作します |
| 分析 / 広告 / トラッキング | **なし** — サードパーティの分析、広告、トラッキングSDKは使用しておらず、App Tracking Transparencyも使用していません |
| 任意の Apple サービス | **iCloud** (your private KVS), **Photo Library (Add Only)** for precept cards, **StoreKit** for 任意チップ, **local notifications**, optional **Live Activities**, optional **on-device handwriting** (Vision) |

## データの収集

当社は、広告や分析のために個人情報を収集、販売、共有することは**ありません**。

- **アカウント不要** — アカウントを作成せずに、すべての基本機能を使用できます。
- **分析や広告なし** — アプリのバイナリには、サードパーティの分析、広告、クラッシュレポートSDKは統合されておらず、データが当社に送信されることはありません。
- **コンテンツのアップロードなし** — 閲読履歴、お気に入り、リスト、メモ、学習進捗、設定は端末内（および任意で**お客様の** iCloud）に留まります。**当社は本アプリ向けにそのようなサーバーを運用していない**ため、iHTC Studio のサーバーにアップロードされることはありません。

## アプリの仕組み

- **同梱ライブラリ** — テキスト JSON、白話／英語、索引、学習補助はアプリ／ウィジェット バンドル内に同梱されます。閲覧と学習にネットワークは不要です。
- **オンデバイス音声** - 朗読には Apple のシステム **AVSpeechSynthesizer** (TTS) が使用されます。 iHTC Studio には文章テキストは送信されません。
- **ウィジェットと App Group** — ウィジェットとアプリは、端末上の App Group `group.com.iHTCboy.iPrecepts` を通じて設定と軽量な状態を共有します。
- **毎日の通知** - ユーザー通知を使用してローカルにスケジュールされます。 通知をタップすると、デバイス上のパッセージ ID へのディープ リンクが開きます。 サーバーのファンアウトはありません。
- **Preceptカード** — 画像は端末上で生成されます。保存は「保存」をタップしたときのみ **写真ライブラリ（追加のみ）** を使用します。共有シートは**お客様が選んだ**アプリに画像を送ることがあり、その場合は送信先のプライバシーポリシーが適用されます。
- **手書き検索 (iOS)** - オプションの文字認識では、デバイス上の Apple **Vision** を使用します。 ストロークはアップロードされません。
- **オプションのチップ** - 「チップ開発者」は、Apple によって処理される消耗品 **StoreKit** の購入です。 私たちはあなたの支払いカードの詳細を受け取りません。
- **Siri / ショートカット / コントロール センター** — オプションのシステム統合により、デバイス上のディープ リンクが開きます。 彼らはあなたのライブラリを私たちに送ることはありません。
- **オプションのスポットライト** — インデックス作成を有効にすると、ローカル検索のためにデバイス上のシステムによってコンテンツのインデックスが作成されます。 当社は検索バックエンドを運用していません。

## 端末に保存されるデータ

 | データ | どこ | 目的 |
 |------|-------|-----------|
| Precept データベース | App / Widget バンドル | オフライン閲読と学習 |
| お気に入りとリスト（训单） | App Group UserDefaults | 星付きの篇目とユーザーリスト |
 | 読書履歴 / 最後に読んだ | アプリグループのUserDefaults | 続きを読む、履歴 UI |
 | メモ | アプリグループのUserDefaults | あなたが書いた読書メモ |
| 学習進捗と習熟 | App Group UserDefaults | Family Study state, quiz / Hunt progress |
 | 連続練習 / チェックイン | アプリグループのUserDefaults | 日々の習慣 |
| 共有カードの設定 | App Group の UserDefaults | 最後に選んだスタイルや比率 |
| Daily Precept cache & notification prefs | App Group UserDefaults | 今日の ID, 時刻, 文脈トグル |
| カード設定 | App Group UserDefaults | 最後のスタイル / 比率 |
 | オンボーディングと TipKit の状態 | 標準 UserDefaults (デバイス) | ウェルカムガイド / 発見のヒント |
| 最近の検索 | Standard UserDefaults (device) | 入力した検索履歴 |
 | ホーム画面のクイックアクション | システム + ローカル設定 | 設定するショートカット |
 | ウィジェット / ライブ アクティビティのスナップショット | アプリグループ / ActivityKit | すでに開いているテキストを表示 |

アプリをアンインストールすると、アプリに関連するサンドボックスおよびApp Groupデータが削除されます（iOS/macOSの動作に依存します）。任意のiCloudコピーは、あなたが削除するか、同期をオフにして他の場所で削除するまで、**あなたの**iCloudに残ります。

## iCloud同期（オプション）

設定で**iCloud同期**を有効にすると、アプリは選択したユーザーデータをAppleの**`NSUbiquitousKeyValueStore`**を通じてあなたのApple IDに関連付けて同期します：

- お気に入り
- リスト（训单）
- 読書履歴
- 学習進捗 / 習熟度
- 練習の連続日数
 - 注意事項

同期トラフィックは**Apple iCloud**にのみ送信され、iHTC Studioには送信されません。設定で同期を無効にできます。私たちはあなたのiCloudの内容を読むことはできません。

## 権限

 iLiezi は、機能が必要な場合にのみアクセス許可を要求します。

| 権限 | タイミング | 理由 |
|------------|------|-----|
| 通知 | Daily Precept reminders を有効にする | ローカルスケジュール of reminder notifications |
| 写真ライブラリ（追加のみ） | カードを保存 | 描画画像を書き込み（読取不要） |
| iCloud | 同期を有効にする | お気に入り/リスト/履歴/進捗/連続/メモを同期 |
 | ライブアクティビティ (iOS) | ライブ アクティビティの読み取りを有効にします | 読んでいる文章をロック画面に表示 / ダイナミックアイランド |
 | バックグラウンドオーディオ (機能) | バックグラウンド朗読を有効にします | アプリがフォアグラウンドでないときに TTS を続行する |

連絡先・正確な位置・カメラ・マイク（TTS 再生除く）・トラッキングは**要求しません**。手書き検索は端末 Vision で、ネットワーク権限プロンプトは不要です。

## 私たちがやらないこと

 - 当社は個人データを**販売しません**。
- 当社は広告プロフィールを構築しません**。
- アカウントやソーシャル ログインは**必要ありません**。
- データ収集のためにサードパーティの広告、分析、ソーシャル SDK を埋め込むことは**ありません**。
- カードの保存を選択した場合、**追加のみ**を超えてフォト ライブラリにアクセスすることは**ありません**。
- 当社は StoreKit 支払いカード番号を**受け取りません** (Apple は支払いを処理します)。
- 手書きストrokesや篇テキストを iHTC Studio へ**アップロードしません**。

## 子供のプライバシー

iPrecepts は一般向けの教育・読書アプリであり、**Kids Category には属しません**。当社は児童から故意に個人情報を収集しません。アカウントは不要です。家族は各自の端末で、オフラインの読書・学習機能をご利用いただけます。

## 第三者

- **Apple** — App Store 配信、任意の StoreKit 購入、任意の iCloud KVS、システム TTS、お客様が選ぶ共有シートの送信先、OS レベルの通知／ライブアクティビティ／Siri／ショートカット／Vision の提供。
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

**마지막 업데이트:** 2026년 9월 3일

iHTC Studio("당사")는 **iPrecepts**("爱家训 / 愛家訓", Bundle ID `com.iHTCboy.iPrecepts`)을(를) 개발했습니다. 본 개인정보 처리방침은 앱 사용 시 어떤 데이터가 처리되고 처리되지 않는지 설명합니다. **Apple App Review**와 사용자는 **이 페이지**를 공개 개인정보 처리방침으로 사용할 수 있습니다. App Store Connect에는 브라우저에서 본 개인정보 처리방침을 열고 주소창의 URL을 복사하세요(공개 사이트 도메인은 변경될 수 있습니다).

## 요약 (Apple 개인정보 영양성분표 정렬)

| 주제 | 당사의 정책 |
|-------|----------------|
| 계정 | **필요 없음** — 등록, 이메일 로그인, 전화번호 필요 없음 |
| iHTC 스튜디오의 데이터 수집 | **데이터 수집 없음** — 개인 데이터를 받는 백엔드를 운영하지 않습니다 |
| 네트워크 | 라이브러리, 읽기, 암기, 학습, Hunt, 위젯, 일일 알림은 설치 후 **오프라인**에서도 작동 |
| 분석 / 광고 / 추적 | **없음** — 타사 분석, 광고, 추적 SDK 없음; 앱 추적 투명성(App Tracking Transparency) 사용 없음 |
| 선택 Apple 서비스 | **iCloud** (your private KVS), **Photo Library (Add Only)** for precept cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **on-device handwriting** (Vision) |

## 데이터 수집

개인 정보를 광고나 분석 목적으로 **수집, 판매, 공유하지 않습니다**.

- **계정 불필요** — 계정을 만들지 않아도 모든 핵심 기능을 사용할 수 있습니다.
- **분석 및 광고 없음** — 앱 바이너리는 당사로 데이터를 전송하는 타사 분석, 광고, 크래시 리포트 SDK를 통합하지 않습니다.
- **콘텐츠 업로드 없음** — 읽기 기록, 즐겨찾기, 목록, 메모, 학습 진행, 설정은 기기(및 선택적으로 **사용자의** iCloud)에만 남습니다. **이 앱용 서버를 운영하지 않으므로** iHTC Studio 서버로 업로드되지 않습니다.

## 앱 작동 방식

- **번들 라이브러리** — 텍스트 JSON, vernacular/English, 색인, 학습 보조 자료가 앱/위젯 번들에 포함됩니다. 탐색과 학습에 네트워크가 필요하지 않습니다.
- **기기 내 음성** — 암송은 Apple 시스템 **AVSpeechSynthesizer**(TTS)를 사용합니다. iHTC Studio에는 문구 텍스트를 보내지 않습니다.
- **위젯 및 App Group** — 위젯과 앱은 기기의 App Group `group.com.iHTCboy.iPrecepts`을 통해 설정과 가벼운 상태를 공유합니다.
- **일일 알림** — 사용자 알림을 통해 로컬로 예약됩니다. 알림을 탭하면 기기의 통로 ID에 대한 딥 링크가 열립니다. 서버 팬아웃이 없습니다.
- **Precept 카드** — 이미지는 기기에서 생성됩니다. 저장은 저장을 탭할 때만 **사진 보관함(추가 전용)** 을 사용합니다. 시스템 공유 시트는 **사용자가 선택한** 앱으로 이미지를 보낼 수 있으며, 해당 앱의 개인정보 처리방침이 적용됩니다.
- **필기 검색(iOS)** — 선택적 문자 인식은 장치에서 Apple **Vision**을 사용합니다. 스트로크는 업로드되지 않습니다.
- **선택적 팁** — "팁 개발자"는 Apple에서 처리하는 소모품 **StoreKit** 구매입니다. 귀하의 결제 카드 정보는 수신되지 않습니다.
- **Siri / 바로가기 / 제어 센터** — 선택적 시스템 통합으로 기기 내 딥 링크가 열립니다. 그들은 귀하의 라이브러리를 우리에게 보내지 않습니다.
- **선택적 스포트라이트** — 인덱싱을 활성화하면 로컬 검색을 위해 장치의 시스템에서 콘텐츠를 인덱싱합니다. 우리는 검색 백엔드를 운영하지 않습니다.

## 귀하의 장치에 저장된 데이터

| 데이터 | 어디 | 목적 |
|------|-------|---------|
| Precept 데이터베이스 | App / Widget 번들 | 오프라인 읽기 및 학습 |
| 즐겨찾기 및 목록(训单) | App Group UserDefaults | 별표 표시한 구절과 사용자 목록 |
| 읽은 이력/마지막 읽은 내용 | 앱 그룹 UserDefaults | 계속 읽기, 기록 UI |
| 메모 | 앱 그룹 UserDefaults | 당신이 쓴 메모 읽기 |
| 학습 진행 및 숙달 | App Group UserDefaults | Family Study state, quiz / Hunt progress |
| 연속연습/체크인 | 앱 그룹 UserDefaults | 일상습관 |
| 공유 카드 설정 | App Group UserDefaults | 마지막으로 선택한 스타일 / 비율 |
| Daily Precept cache & notification prefs | App Group UserDefaults | 오늘 ID, 시간, contextual toggle |
| 카드 설정 | App Group UserDefaults | 마지막 스타일/비율 |
| 온보딩 및 TipKit 상태 | 표준 UserDefaults(장치) | 환영 가이드/탐색 팁 |
| 최근 검색 | Standard UserDefaults (device) | 입력 검색 기록 |
| 홈 화면 빠른 작업 | 시스템 + 로컬 환경설정 | 구성한 바로가기 |
| 위젯/실시간 활동 스냅샷 | 앱 그룹/ActivityKit | 이미 열어본 텍스트 표시 |

앱을 삭제하면 앱과 연관된 샌드박스 및 앱 그룹 데이터가 제거됩니다(iOS/macOS 동작에 따라 다름). 선택적으로 iCloud에 저장된 복사본은 사용자가 삭제하거나 동기화를 끄고 다른 곳에서 삭제할 때까지 **귀하의** iCloud에 남아 있습니다.

## iCloud 동기화 (선택 사항)

설정에서 **iCloud 동기화**를 활성화하면, 앱은 **귀하의 Apple ID**와 연결된 Apple의 **`NSUbiquitousKeyValueStore`**를 통해 선택한 사용자 데이터를 미러링합니다:

- 즐겨찾기
- 목록(训单)
- 읽기 기록
- 학습 진행/숙련도
- 연습 연속 기록
- 메모

동기화 트래픽은 iHTC Studio가 아닌 **Apple iCloud**로 전송됩니다. 설정에서 동기화를 비활성화할 수 있습니다. 우리는 귀하의 iCloud 내용을 읽을 수 없습니다.

## 권한

iLiezi는 기능에 필요한 경우에만 권한을 요청합니다.

| 허가 | 언제 | 왜? |
|------------|------|-----|
| 알림 | Daily Precept reminders 사용 | 로컬 예약 of reminder notifications |
| 사진 보관함(추가 전용) | 카드 저장 | 렌더 이미지 기록 |
| iCloud | 동기화 사용 | 즐겨찾기/목록/기록/진행/연속/메모 |
| 라이브 활동(iOS) | 실시간 활동 읽기 | 잠금화면/다이내믹 아일랜드 | 읽고 있는 구절을 보여주세요 |
| 배경 오디오(기능) | 배경 암송을 활성화합니다 | 앱이 포그라운드가 아닐 때 TTS 계속 |

연락처·정확한 위치·카메라·마이크(TTS 제외)·추적 **요청 안 함**. 필기 검색은 기기 Vision.

## 우리가 하지 않는 일

- 당사는 개인 데이터를 판매하지 **않습니다**.
- 우리는 광고 프로필을 작성하지 **않습니다**.
- 계정이나 소셜 로그인이 필요하지 **않습니다**.
- 당사는 데이터 수집을 위해 제3자 광고, 분석 또는 소셜 SDK를 삽입하지 **않습니다**.
- 귀하가 카드를 저장하기로 선택한 경우 **추가 전용** 이외의 사진 라이브러리에는 액세스하지 **않습니다**.
- 저희는 StoreKit 결제 카드 번호를 받지 **않습니다**(Apple에서 결제를 처리함).
- 필기 획·구절 텍스트 iHTC Studio **업로드 안 함**.

## 아동 개인정보 보호

iPrecepts은(는) 일반 대중을 위한 교육용 독서 앱이며 **Kids Category에 해당하지 않습니다**. 당사는 아동으로부터 고의로 개인정보를 수집하지 않습니다. 계정이 필요하지 않습니다. 가족은 각자의 기기에서 오프라인으로 읽기·학습 기능을 사용할 수 있습니다.

## 제3자

- **Apple** — App Store 배포, 선택적 StoreKit 구매, 선택적 iCloud KVS, 시스템 TTS, 사용자가 선택하는 공유 시트 대상, OS 수준 알림/Live Activities/Siri/Shortcuts/Vision 제공.
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

**Последнее обновление:** 3 сентября 2026 г.

iHTC Studio («мы») создала **iPrecepts** («爱家训 / 愛家訓», Bundle ID `com.iHTCboy.iPrecepts`). Настоящая Политика конфиденциальности объясняет, какие данные обрабатываются (и не обрабатываются) при использовании приложения. **Apple App Review** и пользователи могут использовать **эту страницу** как публичную политику конфиденциальности. Для App Store Connect откройте эту страницу в браузере и скопируйте URL из адресной строки (домен публичного сайта может измениться).

## Сводка (в соответствии с меткой Apple Privacy Nutrition)

| Тема | Наша практика |
|-------|----------------|
| Учетная запись | **Не требуется** — регистрация, вход по электронной почте или номеру телефона не нужны |
| Сбор данных iHTC Studio | **Данные не собираются** — мы **не** используем серверную часть, которая получает ваши личные данные |
| Сеть | Библиотека, чтение, повторение, учеба, Охота, виджеты и ежедневные уведомления работают **оффлайн** после установки |
| Аналитика / реклама / отслеживание | **Отсутствует** — нет сторонней аналитики, рекламы или SDK для отслеживания; не используется App Tracking Transparency |
| Необязательные сервисы Apple | **iCloud** (your private KVS), **Photo Library (Add Only)** for precept cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **on-device handwriting** (Vision) |

## Сбор данных

Мы **не** собираем, не продаем и не делимся личной информацией для рекламы или аналитики.

- **Без аккаунта** — Вы можете использовать все основные функции без создания аккаунта у нас.
- **Без аналитики и рекламы** — В приложении не интегрированы сторонние SDK для аналитики, рекламы или отчётов о сбоях, которые отправляли бы данные нам.
- **Без загрузки контента** — история чтения, избранное, списки, заметки, прогресс обучения и настройки остаются на устройстве (и, по желанию, в **вашем** iCloud). Они не загружаются на серверы iHTC Studio, потому что **мы не эксплуатируем такие серверы для этого приложения**.

## Как работает приложение

- **Встроенная библиотека** — текстовый JSON, vernacular/English, указатели и учебные материалы входят в пакет app/widget. Для просмотра и обучения сеть не нужна.
- **Речь на устройстве** — при декламации используется система Apple **AVSpeechSynthesizer** (TTS). Мы не отправляем текст прохождения в iHTC Studio.
- **Виджеты и App Group** — виджеты и приложение обмениваются настройками и лёгким состоянием через App Group `group.com.iHTCboy.iPrecepts` на вашем устройстве.
- **Ежедневные уведомления** — планируются локально с помощью уведомлений пользователя. При нажатии на уведомление открывается глубокая ссылка на идентификатор прохода на устройстве; нет разветвления сервера.
- **Карточки Precept** — изображения создаются на устройстве. Сохранение использует **Фототеку (только добавление)** лишь при нажатии «Сохранить». «Поделиться» может передать изображение приложению, **которое вы выберете**; тогда действует политика получателя.
- **Поиск по рукописному вводу (iOS)** — дополнительное распознавание символов использует Apple **Vision** на устройстве. Штрихи не загружаются.
- **Необязательный совет**. «Tip Developer» — это расходный материал, приобретаемый **StoreKit** и обрабатываемый Apple. Мы не получаем данные вашей платежной карты.
- **Siri / Ярлыки / Центр управления** — дополнительные системные интеграции открывают глубокие ссылки на устройстве; они не отправляют нам вашу библиотеку.
- **Дополнительный Spotlight** — если вы включите индексирование, контент индексируется системой на устройстве для локального поиска; мы не используем поисковую систему.

## Данные, хранящиеся на вашем устройстве

| Данные | Где | Цель |
|------|-------|---------|
| База Precept | Пакет App / Widget | Офлайн-чтение и обучение |
| Избранное и списки (训单) | UserDefaults App Group | Отмеченные фрагменты и пользовательские списки |
| История чтения / последнее чтение | Пользовательские настройки группы приложений | Продолжить чтение, история пользовательского интерфейса |
| Заметки | Пользовательские настройки группы приложений | Чтение заметок, которые вы пишете |
| Прогресс и mastery | UserDefaults App Group | Family Study state, quiz / Hunt progress |
| Практика / регистрация | Пользовательские настройки группы приложений | Ежедневная привычка |
| Настройки карточек для обмена | UserDefaults App Group | Последний выбранный стиль / соотношение сторон |
| Daily Precept cache & notification prefs | UserDefaults App Group | ID на сегодня, время, переключатели |
| Настройки карточек | UserDefaults App Group | Последний стиль/ratio |
| Регистрация и состояние TipKit | Стандартные настройки пользователя (устройство) | Приветственное руководство / советы по открытию |
| Недавние запросы | Standard UserDefaults (device) | История введённого поиска |
| Быстрые действия на главном экране | Система + локальные настройки | Ярлыки, которые вы настраиваете |
| Виджет / Снимки активности в реальном времени | Группа приложений / ActivityKit | Показать текст, который вы уже открыли |

При удалении приложения удаляются данные песочницы и группы приложений, связанные с приложением (в зависимости от поведения iOS/macOS). Дополнительные копии iCloud остаются в **вашем** iCloud до тех пор, пока вы не очистите их или не отключите синхронизацию и не удалите их в другом месте.

## Синхронизация с iCloud (необязательно)

Если вы включите **iCloud Sync** в настройках, приложение зеркально отображает выбранные пользовательские данные через **`NSUbiquitousKeyValueStore`** Apple, привязанный к **вашему Apple ID**:

- Избранное
- Списки (训单)
- Чтение истории
- Прогресс в учебе/мастерстве
- Практика полос
- Примечания

Трафик синхронизации поступает в **Apple iCloud**, а не в iHTC Studio. Вы можете отключить синхронизацию в настройках. Мы не можем прочитать ваше содержимое iCloud.

## Разрешения

iLiezi запрашивает разрешения только тогда, когда они нужны функции:

| Разрешение | Когда | Почему |
|------------|------|-----|
| Уведомления | Вы включаете Daily Precept reminders | Локальное планирование of reminder notifications |
| Фототека (только добавление) | Сохраняете карту | Запись изображения; без чтения |
| iCloud | Включаете синхронизацию | Избранное/списки/история/прогресс/серии/заметки |
| Живые мероприятия (iOS) | Вы включаете чтение активности в реальном времени | Покажите отрывок, который вы читаете, на экране блокировки / Dynamic Island |
| Фоновый звук (возможность) | Вы включаете фоновое чтение | Продолжить TTS, когда приложение не на переднем плане |

**Не** запрашиваем контакты, точную геолокацию, камеру, микрофон (кроме TTS), tracking. Поиск почерка — Vision на устройстве.

## Чего мы не делаем

- Мы **не** продаем персональные данные.
- Мы **не** создаем рекламные профили.
- Нам **не** требуется учетная запись или вход в социальную сеть.
– Мы **не** встраиваем сторонние рекламные, аналитические или социальные SDK для сбора данных.
- Мы **не** получаем доступ к вашей библиотеке фотографий, кроме **только добавления**, когда вы решаете сохранить карту.
- Мы **не** получаем номера платежных карт StoreKit (Apple обрабатывает платежи).
- **Не** загружаем штрихи почерка и текст фрагментов в iHTC Studio.

## Конфиденциальность детей

iPrecepts — образовательное приложение для широкой аудитории и **не относится к Kids Category**. Мы сознательно не собираем персональные данные детей. Приложение не требует учётной записи. Семьи могут пользоваться чтением и обучением офлайн на своих устройствах.

## Третьи стороны

- **Apple** — распространение в App Store, необязательные покупки StoreKit, необязательный iCloud KVS, системный TTS, выбранные вами пункты «Поделиться», а также уведомления на уровне ОС / Live Activities / Siri / Shortcuts / Vision.
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

**อัปเดตล่าสุด:** 3 กันยายน 2026

iHTC Studio ("เรา") พัฒนา **iPrecepts** ("爱家训 / 愛家訓", Bundle ID `com.iHTCboy.iPrecepts`) นโยบายความเป็นส่วนตัวนี้อธิบายว่าข้อมูลใดถูกจัดการและไม่ถูกจัดการเมื่อคุณใช้แอป **Apple App Review** และผู้ใช้สามารถใช้**หน้านี้**เป็นนโยบายความเป็นส่วนตัวสาธารณะ สำหรับ App Store Connect ให้เปิดนโยบายนี้ในเบราว์เซอร์แล้วคัดลอก URL จากแถบที่อยู่ (โดเมนสาธารณะอาจเปลี่ยนได้)

## สรุป (การจัดตำแหน่งกับ Nutrition Label ความเป็นส่วนตัวของ Apple)

| หัวข้อ | การปฏิบัติของเรา |
|-------|----------------|
| บัญชี | **ไม่จำเป็น** — ไม่ต้องลงทะเบียน ลงชื่อเข้าใช้ด้วยอีเมล หรือหมายเลขโทรศัพท์ |
| การเก็บข้อมูลโดย iHTC Studio | **ไม่เก็บข้อมูล** — เรา **ไม่ได้**ดำเนินการแบ็กเอนด์ที่รับข้อมูลส่วนตัวของคุณ |
| เครือข่าย | ห้องสมุด การอ่าน การท่องจำ การศึกษา การล่า วิดเจ็ต และการแจ้งเตือนประจำวันทำงาน **ออฟไลน์** หลังการติดตั้ง |
| การวิเคราะห์ / โฆษณา / การติดตาม | **ไม่มี** — ไม่มี SDK การวิเคราะห์ โฆษณา หรือการติดตามจากบุคคลที่สาม; ไม่ใช้ App Tracking Transparency |
| บริการ Apple เสริม | **iCloud** (your private KVS), **Photo Library (Add Only)** for precept cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **on-device handwriting** (Vision) |

## การเก็บข้อมูล

เราจะ **ไม่**เก็บ ขาย หรือแชร์ข้อมูลส่วนบุคคลเพื่อโฆษณาหรือการวิเคราะห์

- **ไม่ต้องมีบัญชีผู้ใช้** — คุณสามารถใช้คุณสมบัติหลักทั้งหมดได้โดยไม่ต้องสร้างบัญชีกับเรา
- **ไม่มีการวิเคราะห์หรือโฆษณา** — ไฟล์แอปไม่ได้รวม SDK การวิเคราะห์ การโฆษณา หรือการรายงานข้อผิดพลาดจากบุคคลที่สามที่ติดต่อกลับไปยังเรา
- **ไม่อัปโหลดเนื้อหา** — ประวัติการอ่าน รายการโปรด รายการ บันทึก ความคืบหน้าการเรียน และการตั้งค่าอยู่บนอุปกรณ์ (และอาจอยู่ใน iCloud **ของคุณ**) จะไม่ถูกอัปโหลดไปยังเซิร์ฟเวอร์ iHTC Studio เพราะ **เราไม่ได้ดำเนินการเซิร์ฟเวอร์เช่นนั้นสำหรับแอปนี้**

## วิธีการทำงานของแอป

- **ไลบรารีในชุดแอป** — JSON ข้อความ vernacular/English ดัชนี และตัวช่วยเรียนอยู่ในชุดแอป/วิดเจ็ต การเรียกดูและเรียนไม่ต้องใช้เครือข่าย
- **คำพูดบนอุปกรณ์** — การบรรยายใช้ระบบของ Apple **AVSpeechSynthesizer** (TTS) เราไม่ส่งข้อความข้อความไปที่ iHTC Studio
- **วิดเจ็ตและ App Group** — วิดเจ็ตและแอปใช้การตั้งค่าและสถานะขนาดเล็กร่วมกันผ่าน App Group `group.com.iHTCboy.iPrecepts` บนอุปกรณ์ของคุณ
- **การแจ้งเตือนรายวัน** — กำหนดเวลาภายในเครื่องด้วยการแจ้งเตือนผู้ใช้ การแตะการแจ้งเตือนจะเปิดลิงก์ในรายละเอียดไปยังรหัสข้อความบนอุปกรณ์ ไม่มีการปิดเซิร์ฟเวอร์
- **การ์ด Precept** — สร้างภาพบนอุปกรณ์ การบันทึกใช้ **คลังรูปภาพ (เพิ่มอย่างเดียว)** เมื่อแตะบันทึกเท่านั้น ชีตแชร์อาจส่งภาพไปแอปที่**คุณเลือก** ซึ่งใช้นโยบายความเป็นส่วนตัวของปลายทาง
- **การค้นหาด้วยลายมือ (iOS)** — ตัวเลือกการรู้จำอักขระใช้ Apple **Vision** บนอุปกรณ์ จังหวะไม่ได้อัปโหลด
- **เคล็ดลับเสริม** — “Tip Developer” เป็นการซื้อ **StoreKit** แบบบริโภคที่ดำเนินการโดย Apple เราไม่ได้รับรายละเอียดบัตรชำระเงินของคุณ
- **Siri / ทางลัด / ศูนย์ควบคุม** — การรวมระบบที่เป็นตัวเลือกจะเปิดลิงก์ในรายละเอียดบนอุปกรณ์ พวกเขาไม่ได้ส่งห้องสมุดของคุณมาให้เรา
- **สปอตไลท์เสริม** — หากคุณเปิดใช้งานการจัดทำดัชนี เนื้อหาจะถูกจัดทำดัชนีโดยระบบบนอุปกรณ์สำหรับการค้นหาในท้องถิ่น เราไม่ได้ดำเนินการแบ็กเอนด์การค้นหา

## ข้อมูลที่เก็บบนอุปกรณ์

| ข้อมูล | ที่ไหน | วัตถุประสงค์ |
|------|-------|---------|
| ฐานข้อมูล Precept | App / Widget bundle | การอ่านและเรียนแบบออฟไลน์ |
| รายการโปรดและรายการ (训单) | UserDefaults ของ App Group | ข้อความที่ติดดาวและรายการผู้ใช้ |
| ประวัติการอ่าน / อ่านครั้งล่าสุด | ค่าเริ่มต้นของกลุ่มแอป | อ่านต่อ ประวัติ UI |
| หมายเหตุ | ค่าเริ่มต้นของกลุ่มแอป | อ่านบันทึกที่คุณเขียน |
| ความคืบหน้าและความเชี่ยวชาญ | UserDefaults ของ App Group | Family Study state, quiz / Hunt progress |
| ฝึกสตรีค/เช็คอิน | ค่าเริ่มต้นของกลุ่มแอป | นิสัยประจำวัน |
| การตั้งค่าการ์ดแชร์ | UserDefaults ของ App Group | สไตล์ / อัตราส่วนที่เลือกล่าสุด |
| Daily Precept cache & notification prefs | UserDefaults ของ App Group | ID วันนี้, schedule time, contextual toggle |
| การตั้งค่าการ์ด | UserDefaults ของ App Group | สไตล์/อัตราส่วนล่าสุด |
| การเริ่มต้นใช้งานและสถานะ TipKit | Standard UserDefaults (อุปกรณ์) | คู่มือต้อนรับ / เคล็ดลับการค้นพบ |
| การค้นหาล่าสุด | Standard UserDefaults (device) | ประวัติที่พิมพ์ |
| การดำเนินการด่วนบนหน้าจอหลัก | ระบบ + การตั้งค่าท้องถิ่น | ทางลัดที่คุณกำหนดค่า |
| วิดเจ็ต / ภาพรวมกิจกรรมสด | กลุ่มแอป / ActivityKit | แสดงข้อความที่คุณเปิดแล้ว |

การถอนการติดตั้งแอปจะลบข้อมูล sandbox และ App Group ที่เกี่ยวข้องกับแอป (ขึ้นอยู่กับพฤติกรรมของ iOS/macOS) สำเนา iCloud แบบเลือกได้จะยังคงอยู่ใน **iCloud ของคุณ** จนกว่าคุณจะลบหรือปิดการซิงค์และลบจากที่อื่น

## การซิงค์ iCloud (ตัวเลือก)

หากคุณเปิดใช้งาน **การซิงค์ iCloud** ในการตั้งค่า แอปจะสะท้อนข้อมูลผู้ใช้ที่เลือกผ่าน **`NSUbiquitousKeyValueStore`** ของ Apple ที่เชื่อมโยงกับ **Apple ID ของคุณ**:

- รายการโปรด
- รายการ (训单)
- ประวัติการอ่าน
- ความคืบหน้า/ความชำนาญในการศึกษา
- สถิติการฝึกต่อเนื่อง
- หมายเหตุ

การจราจรการซิงค์จะไปยัง **Apple iCloud** ไม่ใช่ iHTC Studio คุณสามารถปิดการซิงค์ได้ใน การตั้งค่า เราไม่สามารถอ่านเนื้อหา iCloud ของคุณได้

## สิทธิ์

iLiezi ร้องขอการอนุญาตเฉพาะเมื่อคุณสมบัติต้องการ:

| สิทธิ์ | เมื่อไหร่ | ทำไม |
|------------|------|-----|
| การแจ้งเตือน | คุณเปิด Daily Precept reminders | กำหนดเวลาในเครื่อง of reminder notifications |
| คลังรูปภาพ (เพิ่มอย่างเดียว) | บันทึกการ์ด | เขียนภาพที่เรนเดอร์ |
| iCloud | เปิดซิงค์ | ซิงค์รายการโปรด/รายการ/ประวัติ/ความคืบหน้า/สตรีค/บันทึก |
| กิจกรรมสด (iOS) | คุณเปิดใช้งานการอ่านกิจกรรมสด | แสดงข้อความที่คุณกำลังอ่านบนหน้าจอล็อค / Dynamic Island |
| เสียงพื้นหลัง (ความสามารถ) | คุณเปิดใช้งานการอ่านพื้นหลัง | ดำเนินการต่อ TTS เมื่อแอปไม่ได้อยู่เบื้องหน้า |

**ไม่**ขอ Contacts/ตำแหน่ง/กล้อง/ไมค์/ติดตาม ค้นหาลายมือใช้ Vision บนเครื่อง

## สิ่งที่เราไม่ทำ

- เราไม่ **ไม่** ขายข้อมูลส่วนบุคคล
- เราไม่ **ไม่** สร้างโปรไฟล์การโฆษณา
- เรา **ไม่** จำเป็นต้องมีบัญชีหรือการเข้าสู่ระบบโซเชียล
- เราไม่ **ไม่** ฝังโฆษณา การวิเคราะห์ หรือ SDK โซเชียลของบุคคลที่สามสำหรับการรวบรวมข้อมูล
- เราไม่ **ไม่** เข้าถึงคลังภาพของคุณเกินกว่า **เพิ่มเท่านั้น** เมื่อคุณเลือกที่จะบันทึกการ์ด
- เรา **ไม่** รับหมายเลขบัตรชำระเงิน StoreKit (Apple ดำเนินการชำระเงิน)
- **ไม่**อัปโหลดลายมือ/ข้อความไป iHTC Studio

## ความเป็นส่วนตัวของเด็ก

iPrecepts เป็นแอปการอ่านเชิงการศึกษาสำหรับผู้ใช้ทั่วไป และ**ไม่ได้**อยู่ใน Kids Category เราไม่เก็บข้อมูลส่วนบุคคลจากเด็กโดยเจตนา แอปไม่ต้องมีบัญชี ครอบครัวสามารถใช้การอ่านและการเรียนแบบออฟไลน์บนอุปกรณ์ของตนเอง

## บุคคลที่สาม

- **Apple** — การจำหน่าย App Store, การซื้อ StoreKit แบบเลือกได้, iCloud KVS แบบเลือกได้, TTS ของระบบ, ปลายทาง Share Sheet ที่คุณเลือก และการส่งมอบการแจ้งเตือน/Live Activity/Siri/Shortcuts/Vision ระดับ OS
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

**Zuletzt aktualisiert:** 3. September 2026

iHTC Studio („wir“) hat **iPrecepts** („爱家训 / 愛家訓“, Bundle-ID `com.iHTCboy.iPrecepts`) entwickelt. Diese Datenschutzerklärung erläutert, welche Daten bei der Nutzung verarbeitet werden (und welche nicht). **Apple App Review** und Nutzer können sich auf **diese Seite** als öffentliche Datenschutzerklärung stützen. Für App Store Connect öffnen Sie diese Seite im Browser und kopieren Sie die URL aus der Adressleiste (die Domain kann sich ändern).

## Zusammenfassung (Übereinstimmung mit dem Apple-Datenschutzetikett)

| Thema | Unsere Praxis |
|-------|----------------|
| Konto | **Nicht erforderlich** — keine Registrierung, kein E-Mail-Login oder Telefonnummer erforderlich |
| Datenerhebung durch iHTC Studio | **Keine Datenerhebung** — wir betreiben **keinen** Backend-Service, der Ihre persönlichen Daten empfängt |
| Netzwerk | Bibliothek, Lesen, Rezitieren, Lernen, Hunt, Widgets und tägliche Benachrichtigungen funktionieren **offline** nach der Installation |
| Analysen / Werbung / Tracking | **Keine** — keine Analysen von Drittanbietern, Werbung oder Tracking-SDKs; keine Nutzung von App Tracking Transparency |
| Optionale Apple-Dienste | **iCloud** (your private KVS), **Photo Library (Add Only)** for precept cards, **StoreKit** for optionales Trinkgeld, **local notifications**, optional **Live Activities**, optional **on-device handwriting** (Vision) |

## Datenerfassung

Wir erheben, verkaufen oder teilen **keine** persönlichen Informationen für Werbung oder Analysen.

- **Kein Konto** — Sie können alle Kernfunktionen nutzen, ohne ein Konto bei uns zu erstellen.
- **Keine Analysen oder Werbung** — Die App-Binärdatei integriert keine Analysen, Werbung oder Crash-Reporting-SDKs von Drittanbietern, die Daten an uns senden.
- **Kein Hochladen von Inhalten** — Leseverlauf, Favoriten, Listen, Notizen, Lernfortschritt und Einstellungen bleiben auf dem Gerät (optional in **Ihrem** iCloud). Sie werden nicht auf iHTC Studio-Server hochgeladen, da **wir für diese App keine solchen Server betreiben**.

## So funktioniert die App

- **Mitgelieferte Bibliothek** — Text-JSON, Umgangssprache/Englisch, Indizes und Lernhilfen liegen im App-/Widget-Bundle. Durchsuchen und Lernen erfordern kein Netzwerk.
- **Sprache auf dem Gerät** – Die Rezitation nutzt Apples System **AVSpeechSynthesizer** (TTS). Wir senden keine Passagentexte an iHTC Studio.
- **Widgets und App Group** — Widgets und App teilen Einstellungen und leichten Zustand über die App Group `group.com.iHTCboy.iPrecepts` auf Ihrem Gerät.
- **Tägliche Benachrichtigungen** – Lokal geplant mit Benutzerbenachrichtigungen. Durch Tippen auf eine Benachrichtigung wird ein Deep-Link zu einer Durchgangs-ID auf dem Gerät geöffnet. Kein Server-Fanout.
- **Precept-Karten** — Bilder werden auf dem Gerät erzeugt. Speichern nutzt **Fotomediathek (nur Hinzufügen)** nur beim Tippen auf Speichern. Das Teilen-Blatt kann das Bild an eine App senden, **die Sie wählen**; dann gilt deren Datenschutzerklärung.
- **Handschriftsuche (iOS)** – Die optionale Zeichenerkennung verwendet Apple **Vision** auf dem Gerät. Striche werden nicht hochgeladen.
- **Optionaler Tipp** – „Tip Developer“ ist ein verbrauchbarer **StoreKit**-Kauf, der von Apple abgewickelt wird. Wir erhalten Ihre Zahlungskartendaten nicht.
- **Siri / Verknüpfungen / Kontrollzentrum** – Optionale Systemintegrationen öffnen Deep Links auf dem Gerät; Sie senden Ihre Bibliothek nicht an uns.
- **Optionales Spotlight** – Wenn Sie die Indizierung aktivieren, werden Inhalte vom System auf dem Gerät für die lokale Suche indiziert; Wir betreiben kein Such-Backend.

## Auf Ihrem Gerät gespeicherte Daten

| Daten | Wo | Zweck |
|------|-------|---------|
| Precept-Datenbank | App-/Widget-Bundle | Offline-Lesen und -Lernen |
| Favoriten und Listen (训单) | UserDefaults der App Group | Markierte Abschnitte und Nutzerlisten |
| Leseverlauf / zuletzt gelesen | Benutzerstandards der App-Gruppe | Lesen Sie weiter, Verlauf der Benutzeroberfläche |
| Notizen | Benutzerstandards der App-Gruppe | Lesen von Notizen, die Sie schreiben |
| Lernfortschritt und Beherrschung | UserDefaults der App Group | Family Study state, quiz / Hunt progress |
| Übungssträhne / Check-in | Benutzerstandards der App-Gruppe | Tägliche Gewohnheit |
| Einstellungen der Teilen-Karten | UserDefaults der App Group | Zuletzt gewählter Stil / zuletzt gewähltes Seitenverhältnis |
| Daily Precept cache & notification prefs | UserDefaults der App Group | Heutige ID, schedule time, contextual toggle |
| Karten-Einstellungen | UserDefaults der App Group | Letzter Stil/Verhältnis |
| Onboarding- und TipKit-Status | Standard UserDefaults (Gerät) | Willkommensführer / Entdeckungstipps |
| Letzte Suchen | Standard UserDefaults (device) | Suchverlauf Ihrer Eingaben |
| Schnellaktionen auf dem Startbildschirm | System + lokale Einstellungen | Von Ihnen konfigurierte Verknüpfungen |
| Widget-/Live-Aktivitäts-Schnappschüsse | App-Gruppe / ActivityKit | Text anzeigen, den Sie bereits geöffnet haben |

Die Deinstallation der App entfernt Sandbox- und App-Gruppendaten, die mit der App verbunden sind (abhängig vom Verhalten von iOS/macOS). Optionale iCloud-Kopien bleiben in **deiner** iCloud, bis du sie löschst oder die Synchronisierung ausschaltest und anderswo löschst.

## iCloud-Synchronisierung (optional)

Wenn du **iCloud-Synchronisierung** in den Einstellungen aktivierst, spiegelt die App ausgewählte Benutzerdaten über Apples **`NSUbiquitousKeyValueStore`**, die mit **deiner Apple-ID** verknüpft ist:

- Favoriten
- Listen (训单)
- Leseverlauf
- Lernfortschritt / Kenntnisse
- Übungsserien
- Notizen

Der Synchronisationsverkehr geht an **Apple iCloud**, nicht an iHTC Studio. Du kannst die Synchronisierung in den Einstellungen deaktivieren. Wir können deine iCloud-Inhalte nicht lesen.

## Berechtigungen

iLiezi fordert Berechtigungen nur an, wenn eine Funktion diese benötigt:

| Erlaubnis | Wann | Warum |
|------------|------|-----|
| Benachrichtigungen | Sie aktivieren Daily Precept reminders | Lokale Planung of reminder notifications |
| Fotomediathek (nur Hinzufügen) | Karte speichern | Gerendetes Bild schreiben |
| iCloud | Sync aktivieren | Favoriten/Listen/Verlauf/Fortschritt/Serien/Notizen |
| Live-Aktivitäten (iOS) | Sie aktivieren die Lese-Live-Aktivität | Zeigen Sie die Passage, die Sie gerade lesen, auf dem Sperrbildschirm/Dynamic Island | an
| Hintergrundaudio (Fähigkeit) | Sie aktivieren die Hintergrundrezitation | TTS fortsetzen, wenn die App nicht im Vordergrund ist |

**Keine** Kontakte, Standort, Kamera, Mikrofon (außer TTS), Tracking. Handschrift — Vision auf dem Gerät.

## Was wir nicht tun

- Wir verkaufen **keine** personenbezogene Daten.
- Wir erstellen **keine** Werbeprofile.
- Wir benötigen **kein** Konto oder Social-Login.
- Wir betten zur Datenerfassung **keine** Werbung, Analysen oder soziale SDKs von Drittanbietern ein.
- Wir greifen über die Option „Nur hinzufügen“ hinaus **nicht** auf Ihre Fotobibliothek zu, wenn Sie sich für das Speichern einer Karte entscheiden.
- Wir erhalten **keine** Nummern von StoreKit-Zahlungskarten (Apple verarbeitet Zahlungen).
- **Kein** Upload von Handschrift/Passagentext an iHTC Studio.

## Privatsphäre von Kindern

iPrecepts ist eine Bildungs- und Lese-App für ein allgemeines Publikum und **nicht** in der Kids Category. Wir erheben wissentlich keine personenbezogenen Daten von Kindern. Die App erfordert kein Konto. Familien können Lese- und Lernfunktionen offline auf eigenen Geräten nutzen.

## Dritte Parteien

- **Apple** — App Store-Vertrieb, optionale StoreKit-Käufe, optionales iCloud-KVS, System-TTS, von Ihnen gewählte Share-Sheet-Ziele sowie Benachrichtigungen/Live-Aktivitäten/Siri/Kurzbefehle/Vision auf OS-Ebene.
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

**Dernière mise à jour :** 3 septembre 2026

iHTC Studio (« nous ») a développé **iPrecepts** (« 爱家训 / 愛家訓 », Bundle ID `com.iHTCboy.iPrecepts`). Cette politique de confidentialité explique quelles données sont (ou ne sont pas) traitées lorsque vous utilisez l’app. **Apple App Review** et les utilisateurs peuvent s’appuyer sur **cette page** comme politique publique. Pour App Store Connect, ouvrez cette page dans le navigateur et copiez l’URL depuis la barre d’adresse (le domaine public peut changer).

## Résumé (alignement sur l'étiquette nutritionnelle de confidentialité Apple)

| Sujet | Notre pratique |
|-------|----------------|
| Compte | **Non requis** — pas d'inscription, de connexion par e-mail ou de numéro de téléphone |
| Collecte de données par iHTC Studio | **Données non collectées** — nous n'exploitons **pas** de backend qui reçoit vos données personnelles |
| Réseau | La bibliothèque, la lecture, la récitation, l'étude, la chasse, les widgets et les notifications quotidiennes fonctionnent **hors ligne** après l'installation |
| Analyses / publicités / suivi | **Aucun** — pas de SDK tiers d'analyse, de publicité ou de suivi ; pas d'utilisation de la transparence du suivi des applications |
| Services Apple facultatifs | **iCloud** (your private KVS), **Photo Library (Add Only)** for precept cards, **StoreKit** for pourboire facultatif, **local notifications**, optional **Live Activities**, optional **on-device handwriting** (Vision) |

## Collecte de données

Nous ne collectons, vendons ou partageons **pas** d'informations personnelles à des fins publicitaires ou analytiques.

- **Aucun compte** — Vous pouvez utiliser toutes les fonctionnalités principales sans créer de compte chez nous.
- **Aucune analyse ni publicité** — Le binaire de l'application n'intègre pas de SDK tiers d'analyse, de publicité ou de rapport d'erreur qui nous contactent.
- **Aucun envoi de contenu** — historique, favoris, listes, notes, progression d’étude et préférences restent sur l’appareil (et, en option, dans **votre** iCloud). Ils ne sont jamais envoyés aux serveurs iHTC Studio car **nous n’exploitons pas de tels serveurs pour cette app**.

## Comment fonctionne l'application

- **Bibliothèque incluse** — JSON texte, vernaculaire/anglais, index et aides d’étude sont dans le bundle app/widget. Parcourir et étudier ne nécessite pas le réseau.
- **Discours sur l'appareil** — La récitation utilise le système **AVSpeechSynthesizer** (TTS) d'Apple. Nous n'envoyons pas de texte de passage à iHTC Studio.
- **Widgets et App Group** — Les widgets et l’app partagent des préférences et un état léger via l’App Group `group.com.iHTCboy.iPrecepts` sur votre appareil.
- **Notifications quotidiennes** — Planifiées localement avec les notifications utilisateur. Appuyer sur une notification ouvre un lien profond vers un identifiant de passage sur l'appareil ; pas de distribution du serveur.
- **Cartes Precept** — Les images sont générées sur l’appareil. L’enregistrement utilise **Photothèque (ajout uniquement)** seulement lorsque vous touchez Enregistrer. Le partage peut envoyer l’image à une app **que vous choisissez** ; la politique de cette destination s’applique.
- **Recherche d'écriture manuscrite (iOS)** : la reconnaissance de caractères facultative utilise Apple **Vision** sur l'appareil. Les traits ne sont pas téléchargés.
- **Conseil facultatif** — « Tip Developer » est un achat de consommable **StoreKit** traité par Apple. Nous ne recevons pas les détails de votre carte de paiement.
- **Siri / Raccourcis / Centre de contrôle** — Les intégrations système facultatives ouvrent des liens profonds sur l'appareil ; ils ne nous envoient pas votre bibliothèque.
- **Spotlight facultatif** — Si vous activez l'indexation, le contenu est indexé par le système sur l'appareil pour la recherche locale ; nous n'exploitons pas de backend de recherche.

## Données stockées sur votre appareil

| Données | Où | Objectif |
|------|-------|--------------|
| Base Precept | Bundle App / Widget | Lecture et étude hors ligne |
| Favoris et listes (训单) | UserDefaults de l’App Group | Passages favoris et listes utilisateur |
| Historique de lecture / dernière lecture | Paramètres par défaut du groupe d'applications | Continuer la lecture, historique de l'interface utilisateur |
| Remarques | Paramètres par défaut du groupe d'applications | Notes de lecture que vous écrivez |
| Progression d’étude et maîtrise | UserDefaults de l’App Group | Family Study state, quiz / Hunt progress |
| Séquence d'entraînement / enregistrement | Paramètres par défaut du groupe d'applications | Habitude quotidienne |
| Préférences des cartes de partage | UserDefaults de l'App Group | Derniers choix de style / de format |
| Daily Precept cache & notification prefs | UserDefaults de l’App Group | ID du jour, schedule time, contextual toggle |
| Préférences de cartes | UserDefaults de l’App Group | Dernier style/ratio |
| État d’intégration et de TipKit | Paramètres utilisateur standard (appareil) | Guide d'accueil / conseils découverte |
| Recherches récentes | Standard UserDefaults (device) | Historique saisi |
| Actions rapides sur l'écran d'accueil | Système + préférences locales | Raccourcis que vous configurez |
| Widget / Instantanés d'activité en direct | Groupe d'applications / ActivityKit | Afficher le texte que vous avez déjà ouvert |

La désinstallation de l'application supprime les données du bac à sable et du groupe d'applications associées à l'application (selon le comportement d'iOS/macOS). Les copies facultatives dans iCloud restent dans **votre** iCloud jusqu'à ce que vous les supprimiez ou que vous désactiviez la synchronisation et supprimiez ailleurs.

## Synchronisation iCloud (Facultative)

Si vous activez **la synchronisation iCloud** dans les Réglages, l'application reflète les données utilisateur sélectionnées via le **`NSUbiquitousKeyValueStore`** d'Apple lié à **votre identifiant Apple** :

- Favoris
- Listes (训单)
- Historique de lecture
- Progression / maîtrise des études
- Séries de pratique
- Remarques

Le trafic de synchronisation passe par **Apple iCloud**, et non par iHTC Studio. Vous pouvez désactiver la synchronisation dans les Réglages. Nous ne pouvons pas lire le contenu de votre iCloud.

## Autorisations

iLiezi demande des autorisations uniquement lorsqu'une fonctionnalité en a besoin :

| Autorisation | Quand | Pourquoi |
|------------|------|-----|
| Notifications | Vous activez Daily Precept reminders | Planification locale of reminder notifications |
| Photothèque (ajout uniquement) | Enregistrer une carte | Image rendu |
| iCloud | Activez la sync | Favoris/listes/historique/progression/séries/notes |
| Activités en direct (iOS) | Vous activez l'activité de lecture en direct | Affichez le passage que vous lisez sur l'écran de verrouillage / Dynamic Island |
| Audio de fond (capacité) | Vous activez la récitation en arrière-plan | Continuer TTS lorsque l'application n'est pas au premier plan |

**Pas** de contacts, localisation précise, caméra, micro (hors TTS), suivi. Écriture — Vision sur l’appareil.

## Ce que nous ne faisons pas

- Nous ne vendons **pas** de données personnelles.
- Nous ne créons **pas** de profils publicitaires.
- Nous n'exigeons **pas** de compte ou de connexion sociale.
- Nous n'intégrons **pas** de publicités tierces, d'analyses ou de SDK sociaux pour la collecte de données.
- Nous n'accédons **pas** à votre photothèque au-delà du **ajout uniquement** lorsque vous choisissez d'enregistrer une carte.
- Nous ne recevons **pas** de numéros de carte de paiement StoreKit (Apple traite les paiements).
- **Pas** d’envoi d’écriture manuscrite ou de passages à iHTC Studio.

## Confidentialité des enfants

iPrecepts est une application éducative de lecture pour le grand public et **n’est pas** dans la Kids Category. Nous ne collectons pas sciemment d’informations personnelles auprès d’enfants. L’app ne nécessite pas de compte. Les familles peuvent utiliser lecture et étude hors ligne sur leurs propres appareils.

## Tiers

- **Apple** — Distribution App Store, achats StoreKit facultatifs, KVS iCloud facultatif, TTS système, destinations de partage que vous choisissez, et notifications/activités en direct/Siri/raccourcis/Vision au niveau du système.
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

**Son güncelleme:** 3 Eylül 2026

iHTC Studio ("biz"), **iPrecepts** ("爱家训 / 愛家訓", Bundle ID `com.iHTCboy.iPrecepts`) uygulamasını geliştirdi. Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlendiğini (ve işlenmediğini) açıklar. **Apple App Review** ve kullanıcılar **bu sayfayı** herkese açık gizlilik politikası olarak kullanabilir. App Store Connect için tarayıcıda bu sayfayı açın ve adres çubuğundan URL’yi kopyalayın (genel site alan adı zamanla değişebilir).

## Özet (Apple Gizlilik Beslenme Etiketi uyumu)

| Konu | Uygulamamızın uygulaması |
|-------|----------------|
| Hesap | **Gerekli değil** — kayıt, e-posta ile giriş veya telefon numarası yok |
| iHTC Studio tarafından veri toplama | **Veri Toplanmıyor** — kişisel verilerinizi alan bir arka uç işletmiyoruz |
| Ağ | Kütüphane, okuma, ezberleme, çalışma, avlanma, widgetlar ve günlük bildirimler kurulumdan sonra **çevrimdışı** çalışır |
| Analitik / reklam / izleme | **Yok** — üçüncü taraf analitik, reklam veya izleme SDK'ları yok; Uygulama İzleme Şeffaflığı kullanılmaz |
| İsteğe bağlı Apple hizmetleri | **iCloud** (your private KVS), **Photo Library (Add Only)** for precept cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **on-device handwriting** (Vision) |

## Veri Toplama

Kişisel bilgileri reklam veya analiz için **toplamıyoruz**, satmıyoruz veya paylaşmıyoruz.

- **Hesap gerekmez** — Tüm temel özellikleri bizde hesap oluşturmadan kullanabilirsiniz.
- **Analitik veya reklam yok** — Uygulama ikili dosyası üçüncü taraf analitik, reklam veya çökme bildirim SDK'larını içermez, telefonla bize veri göndermez.
- **İçerik yüklenmez** — Okuma geçmişi, favoriler, listeler, notlar, çalışma ilerlemesi ve tercihler cihazınızda (ve isteğe bağlı **iCloud’unuzda**) kalır. **Bu uygulama için böyle sunucular işletmediğimizden** iHTC Studio sunucularına yüklenmez.

## Uygulama Nasıl Çalışır

- **Paketlenmiş kitaplık** — Metin JSON, vernacular/English, dizinler ve çalışma yardımcıları uygulama/widget paketinin içindedir. Gezinme ve çalışma için ağ gerekmez.
- **Cihaz içi konuşma** — Okuma, Apple'ın **AVSpeechSynthesizer** (TTS) sistemini kullanır. iHTC Studio'ya pasaj metni göndermiyoruz.
- **Widget'lar ve App Group** — Widget'lar ve uygulama, cihazınızdaki `group.com.iHTCboy.iPrecepts` App Group'u üzerinden tercihleri ve hafif durumu paylaşır.
- **Günlük bildirimler** — Kullanıcı Bildirimleriyle yerel olarak planlanır. Bir bildirime dokunulduğunda cihazdaki pasaj kimliğine giden derin bağlantı açılır; sunucu çıkışı yok.
- **Precept kartları** — Görseller cihazda oluşturulur. Kaydetme yalnızca kaydet’e dokunduğunuzda **Fotoğraf Kitaplığı (yalnızca ekleme)** kullanır. Paylaşım Sayfası görseli **sizin seçtiğiniz** bir uygulamaya gönderebilir; o hedefin gizlilik politikası geçerli olur.
- **El yazısı araması (iOS)** — İsteğe bağlı karakter tanıma, cihazda Apple **Vision**'ı kullanır. Konturlar yüklenmedi.
- **İsteğe bağlı ipucu** — "İpucu Geliştirici", Apple tarafından gerçekleştirilen bir **StoreKit** sarf malzemesidir. Ödeme kartı bilgilerinizi almıyoruz.
- **Siri / Kısayollar / Kontrol Merkezi** — İsteğe bağlı sistem entegrasyonları cihazdaki derin bağlantıları açar; kütüphanenizi bize göndermiyorlar.
- **İsteğe Bağlı Spotlight** — Dizin oluşturmayı etkinleştirirseniz içerik, yerel arama için cihazdaki sistem tarafından dizine eklenir; bir arama arka ucu kullanmıyoruz.

## Cihazınızda Saklanan Veriler

| Veri | Nerede | Amaç |
|------|-------|-------------|
| Precept veritabanı | App / Widget paketi | Çevrimdışı okuma ve çalışma |
| Favoriler ve listeler (训单) | App Group UserDefaults | Yıldızlı pasajlar ve kullanıcı listeleri |
| Okuma geçmişi / son okuma | Uygulama Grubu Kullanıcı Varsayılanları | Okumaya devam et, geçmiş kullanıcı arayüzü |
| Notlar | Uygulama Grubu Kullanıcı Varsayılanları | Yazdığınız notları okuma |
| Çalışma ilerlemesi ve ustalık | App Group UserDefaults | Family Study state, quiz / Hunt progress |
| Antrenman serisi / check-in | Uygulama Grubu Kullanıcı Varsayılanları | Günlük alışkanlık |
| Paylaşım kartı tercihleri | App Group UserDefaults | Son stil / oran seçimleri |
| Daily Precept cache & notification prefs | App Group UserDefaults | Bugünün ID’si, schedule time, contextual toggle |
| Kart tercihleri | App Group UserDefaults | Son stil/oran |
| İlk katılım ve TipKit durumu | Standart Kullanıcı Varsayılanları (cihaz) | Hoş geldiniz kılavuzu / keşif ipuçları |
| Son aramalar | Standard UserDefaults (device) | Yazdığınız arama geçmişi |
| Ana Ekran hızlı eylemler | Sistem + yerel tercihler | Yapılandırdığınız kısayollar |
| Widget / Canlı Etkinlik anlık görüntüleri | Uygulama Grubu / ActivityKit | Daha önce açmış olduğunuz metni görüntüleyin |

Uygulamayı kaldırmak, uygulamayla ilişkili sandbox ve Uygulama Grubu verilerini kaldırır (iOS/macOS davranışına tabidir). İsteğe bağlı iCloud kopyaları, siz temizleyene veya senkronizasyonu kapatıp başka yerde silene kadar **iCloud’unuzda** kalır.

## iCloud Senkronizasyonu (İsteğe Bağlı)

Eğer Ayarlar’dan **iCloud Senkronizasyonu**’nu etkinleştirirseniz, uygulama seçili kullanıcı verilerini Apple’ın **`NSUbiquitousKeyValueStore`** aracılığıyla **Apple Kimliğinizle** eşler:

- Favoriler
- Listeler (训单)
- Okuma geçmişi
- Çalışma ilerlemesi / ustalık
- Pratik serileri
- Notlar

Senkronizasyon trafiği **Apple iCloud**’a gider, iHTC Studio’ya değil. Ayarlardan senkronizasyonu devre dışı bırakabilirsiniz. iCloud içeriğinizi okuyamayız.

## İzinler

iLiezi yalnızca bir özellik ihtiyaç duyduğunda izin ister:

| İzin | Ne zaman | neden |
|------------|------|-----|
| Bildirimler | Daily Precept reminders etkinleştirirsiniz | Yerel zamanlama of reminder notifications |
| Fotoğraf Kitaplığı (yalnızca ekleme) | Kart kaydetme | İşlenmiş görsel yaz |
| iCloud | Senkronizasyonu açarsınız | Favoriler/listeler/geçmiş/ilerleme/seriler/notlar |
| Canlı Etkinlikler (iOS) | Canlı Okuma Etkinliğini etkinleştirirsiniz | Okuduğunuz pasajı Kilit Ekranında / Dinamik Ada'da gösterin |
| Arka planda ses (yetenek) | Arka planda okumayı etkinleştirirsiniz | Uygulama ön planda olmadığında TTS'ye devam edin |

Kişiler, konum, kamera, mikrofon (TTS hariç), izleme **istenmez**. El yazısı — cihaz Vision.

## Ne Yapmıyoruz

- Kişisel verileri **satmıyoruz**.
- Reklam profilleri **oluşturmuyoruz**.
- Bir hesaba veya sosyal girişe **gerek duymayız**.
- Veri toplama amacıyla üçüncü taraf reklamları, analizleri veya sosyal SDK'ları **yerleştirmeyiz**.
- Bir kartı kaydetmeyi seçtiğinizde **yalnızca eklenti** dışında Fotoğraf Kitaplığınıza **erişmeyiz**.
- StoreKit ödeme kartı numaralarını **almıyoruz** (ödemeleri Apple işler).
- El yazısı/pasaj metni iHTC Studio’ya **yüklenmez**.

## Çocukların Gizliliği

iPrecepts, genel kitleye yönelik bir eğitim/okuma uygulamasıdır ve **Kids Category**’de değildir. Çocuklardan bilerek kişisel bilgi toplamayız. Uygulama hesap gerektirmez. Aileler kendi cihazlarında okuma ve çalışma özelliklerini çevrimdışı kullanabilir.

## Üçüncü Taraflar

- **Apple** — App Store dağıtımı, isteğe bağlı StoreKit satın alımları, isteğe bağlı iCloud KVS, sistem TTS, seçtiğiniz Paylaşım Sayfası hedefleri ve işletim sistemi düzeyinde bildirim/Canlı Etkinlik/Siri/Kestirmeler/Vision.
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
