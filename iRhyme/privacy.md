---
layout: doc
title: iRhyme — Privacy Policy
app_id: iRhyme
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iRhyme (爱声律启蒙) — fully offline, Data Not Collected, optional iCloud and Photo Library add-only.
---

<section lang="en" markdown="1">

**Last updated:** September 3, 2026

iHTC Studio ("we", "us" or "our"; formerly iHTCTeam) built **iRhyme** (also known as "爱声律启蒙 / 愛聲律啟蒙", Bundle ID `com.iHTCboy.iRhyme`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on **this page** as the public privacy policy for the app. For App Store Connect, open this Privacy Policy in your browser and copy the address from the address bar (the public site domain may change over time).

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration, email sign-in, or phone number |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your personal data |
| Network | Library, reading, recite, Rhyme Academy, widgets, and daily notifications work **offline** after install |
| Analytics / ads / tracking | **None** — no third-party analytics, advertising, or tracking SDKs; no App Tracking Transparency use |
| Optional Apple services | **iCloud** (your private KVS), **Photo Library (Add Only)** for rhyme cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **on-device handwriting** (Vision) |

## Data Collection

We do **not** collect, sell, or share personal information for advertising or analytics.

- **No account** — You can use all core features without creating an account with us.
- **No analytics or ads** — The app binary does not integrate third-party analytics, advertising, or crash-reporting SDKs that phone home to us.
- **No content upload** — Your reading history, favorites, lists, notes, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## How the App Works

- **Bundled library** — Text JSON, vernacular/English, indexes, and study aids ship inside the app / widget bundle. Browsing and study do not require a network request.
- **On-device speech** — Recitation uses Apple’s system **AVSpeechSynthesizer** (TTS). We do not send passage text to iHTC Studio.
- **Widgets & App Group** — Widgets and the app share preferences and lightweight state via App Group `group.com.iHTCboy.iRhyme` on your device.
- **Daily notifications** — Scheduled locally with User Notifications. Tapping a notification opens a deep link to a passage ID on device; no server fan-out.
- **Rhyme cards** — Images are rendered on device. Saving uses **Photo Library add-only** only when you tap save. System Share Sheet may send the image to an app **you** choose; that destination’s privacy policy then applies.
- **Handwriting search (iOS)** — Optional character recognition uses Apple **Vision** on device. Strokes are not uploaded.
- **Optional tip** — “Tip Developer” is a consumable **StoreKit** purchase processed by Apple. We do not receive your payment card details.
- **Siri / Shortcuts / Control Center** — Optional system integrations open on-device deep links; they do not send your library to us.
- **Optional Spotlight** — If you enable indexing, content is indexed by the system on device for local search; we do not operate a search backend.

## Data Stored on Your Device

| Data | Where | Purpose |
|------|-------|---------|
| Rhyme database | App / Widget bundle | Offline reading & study |
| Favorites & lists (韵单) | App Group UserDefaults | Starred passages and user lists |
| Reading history / last read | App Group UserDefaults | Continue reading, history UI |
| Notes | App Group UserDefaults | Reading notes you write |
| Study progress & mastery | App Group UserDefaults | Rhyme Academy state, quiz / Hunt progress |
| Practice streak / check-in | App Group UserDefaults | Daily habit |
| Appearance & reading prefs | App Group UserDefaults | Theme, accent, language, layout, TTS, tabs, widgets, font scale |
| Today’s Rhyme cache & notification prefs | App Group UserDefaults | Today’s ID, schedule time, contextual toggle |
| Card preferences | App Group UserDefaults | Last style / ratio choices |
| Onboarding & TipKit state | Standard UserDefaults (device) | Welcome guide / discovery tips |
| Recent searches | Standard UserDefaults (device) | Search history you typed |
| Home Screen quick actions | System + local prefs | Shortcuts you configure |
| Widget / Live Activity snapshots | App Group / ActivityKit | Display text you already opened |

Uninstalling the app removes sandbox and App Group data associated with the app (subject to iOS/macOS behavior). Optional iCloud copies remain in **your** iCloud until you clear them or turn sync off and delete elsewhere.

## iCloud Sync (Optional)

If you enable **iCloud Sync** in Settings, the app mirrors selected user data through Apple’s **`NSUbiquitousKeyValueStore`** tied to **your Apple ID**:

- Favorites
- Lists (韵单)
- Reading history
- Study progress / mastery
- Practice streaks
- Notes

Sync traffic goes to **Apple iCloud**, not to iHTC Studio. You can disable sync in Settings. We cannot read your iCloud contents.

## Permissions

iRhyme requests permissions only when a feature needs them:

| Permission | When | Why |
|------------|------|-----|
| Notifications | You enable Today’s Rhyme reminders | Local scheduling of reminder notifications |
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

iRhyme is an educational literacy app for a general audience and is **not** in the Kids Category. We do not knowingly collect personal information from children. The app does not require an account. Families may use reading and study features offline on their own devices.

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

爱火腿肠工作室（iHTC Studio）（「我们」；原 iHTCTeam）开发了 **爱声律启蒙**（iRhyme / 愛聲律啟蒙，Bundle ID `com.iHTCboy.iRhyme`）。本隐私政策说明你在使用本应用时，数据如何被处理（以及**不会**如何被处理）。本页可作为 **App Store 审核**与用户查阅的公开隐私政策。填写 App Store Connect 时，请在浏览器打开本 [隐私政策](privacy) 页，从地址栏复制当前网址（站点域名日后可能变更，请勿依赖文档中的固定域名）。

## 概要（对齐 App Store 隐私标签）

| 主题 | 我们的做法 |
|------|------------|
| 账号 | **不需要**——无需注册、邮箱登录或手机号 |
| iHTC Studio 收集数据 | **不收集数据（Data Not Collected）**——我们**不**运营接收你个人数据的后端 |
| 网络 | 语料、阅读、诵读、声律学堂、小组件与每日通知在安装后可**离线**使用 |
| 分析 / 广告 / 追踪 | **无**——无第三方分析、广告或追踪 SDK；不使用跨 App 追踪 |
| 可选 Apple 服务 | **iCloud**（你的私有键值存储）、保存韵卡时的**相簿（仅加入）**、可选 **StoreKit** 打赏、**本地通知**、可选**实时活动**、可选本机**手写识别**（Vision） |

## 数据收集

我们**不**收集、出售或出于广告 / 分析目的共享个人信息。

- **无账号** — 核心功能无需向我们注册。
- **无分析或广告** — 应用未集成会向我们回传的第三方分析、广告或崩溃上报 SDK。
- **不上传内容** — 阅读历史、收藏、韵单、笔记、学堂进度与偏好留在本机（以及可选的**你的** iCloud）。它们不会上传到 iHTC Studio 服务器，因为**我们不为该 App 运营此类服务器**。

## 应用如何工作

- **内置语料** — 正文 JSON、白话 / 英译、索引与学习辅助随 App / 小组件包分发。浏览与学堂**无需**网络请求。
- **本机语音** — 诵读使用系统 **AVSpeechSynthesizer**（TTS）。我们不会把正文发到 iHTC Studio。
- **小组件与 App Group** — 小组件与主应用通过本机 App Group `group.com.iHTCboy.iRhyme` 共享偏好与轻量状态。
- **每日通知** — 使用 User Notifications **本机排程**。点按通知会打开指向本机篇目 ID 的深链，没有服务端推送名单。
- **韵卡** — 图片在本机渲染。仅在你点保存时使用**相簿仅加入**。系统分享表可能把图片发到**你选择**的 App，随后适用该目标的隐私政策。
- **手写搜索（iOS）** — 可选字形识别使用 Apple **Vision**，在本机完成。笔迹不上传。
- **可选打赏** — 「打赏开发者」为消耗型 **StoreKit** 购买，由 Apple 处理。我们收不到银行卡号。
- **Siri / 快捷指令 / 控制中心** — 可选系统集成打开本机深链，不会把语料发给我们。
- **可选 Spotlight** — 若开启索引，由系统在本机建立搜索索引；我们不运营搜索后端。

## 本机存储的数据

| 数据 | 位置 | 用途 |
|------|------|------|
| 声律语料 | App / Widget Bundle | 离线阅读与学堂 |
| 收藏与韵单 | App Group UserDefaults | 星标与自订列表 |
| 浏览纪录 / 最近阅读 | App Group UserDefaults | 继续阅读与历史 |
| 笔记 | App Group UserDefaults | 你写下的阅读心得 |
| 学堂进度与掌握度 | App Group UserDefaults | 声律学堂状态、测验 / 寻对进度 |
| 打卡 | App Group UserDefaults | 每日习惯 |
| 外观与阅读偏好 | App Group UserDefaults | 主题、强调色、语言、版面、朗读、Tab、小组件、字级 |
| 今日一律缓存与通知偏好 | App Group UserDefaults | 今日 ID、提醒时间、情境开关 |
| 韵卡偏好 | App Group UserDefaults | 上次风格 / 比例 |
| 引导与 TipKit 状态 | 标准 UserDefaults | 欢迎引导 / 发现提示 |
| 最近搜索 | 标准 UserDefaults | 你输入过的搜索词 |
| 主屏快捷 | 系统 + 本机偏好 | 你设定的快捷 |
| 小组件 / 实时活动快照 | App Group / ActivityKit | 展示你已打开的正文 |

解除安装会清除与该 App 相关的沙盒与 App Group 数据（以系统行为为准）。可选 iCloud 副本仍留在**你的** iCloud。

## iCloud 同步（可选）

若你在设置中开启 **iCloud 同步**，应用会通过绑定**你的 Apple ID** 的 Apple **`NSUbiquitousKeyValueStore`** 镜像：收藏、韵单、阅读历史、学堂进度／掌握度、打卡与笔记。同步流量走向 **Apple iCloud**，而不是 iHTC Studio。我们无法读取你的 iCloud 内容。

## 权限

仅在功能需要时请求：

| 权限 | 何时 | 原因 |
|------|------|------|
| 通知 | 你开启今日一律提醒 | 本地排程提醒 |
| 相簿（仅加入） | 你保存韵卡 | 写入渲染图片；无需读取全部照片 |
| iCloud | 你开启同步 | 同步收藏／韵单／历史／进度／打卡／笔记 |
| 实时活动（iOS） | 你开启品读实时活动 | 在锁定屏幕／灵动岛显示正在品读的篇目 |
| 背景音频能力 | 你开启背景诵读 | App 不在前台时继续 TTS |

我们**不**请求通讯录、精确位置、相机、麦克风（除系统 TTS 播放外）或追踪权限。手写搜索使用本机 Vision，不会弹出网络权限。

## 我们明确不做的事

- **不**出售个人数据。
- **不**建立广告画像。
- **不**要求账号或社交登录。
- **不**嵌入用于数据收集的第三方广告、分析或社交 SDK。
- **不**在你主动保存韵卡之外访问照片（且仅为「加入」）。
- **不**接收 StoreKit 银行卡号码（由 Apple 处理付款）。
- **不**把手写笔迹或正文上传到 iHTC Studio。

## 儿童隐私

爱声律启蒙是面向一般受众的语文学习应用，**不属于儿童类别**。我们不会故意收集包括 13 岁以下（或你所在地区同等年龄）儿童在内的任何人的个人信息。应用不需要账号。家庭可在自有设备上离线使用阅读与学堂功能。

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

愛火腿腸工作室（iHTC Studio）（「我們」；原 iHTCTeam）開發了 **愛聲律啟蒙**（iRhyme / 爱声律启蒙，Bundle ID `com.iHTCboy.iRhyme`）。本隱私政策說明你在使用本應用時，資料如何被處理（以及**不會**如何被處理）。本頁可作為 **App Store 審核**與使用者查閱的公開隱私政策。填寫 App Store Connect 時，請在瀏覽器打開本 [隱私政策](privacy) 頁，從網址列複製目前網址（站點網域日後可能變更，請勿依賴文件中的固定網域）。

## 概要（對齊 App Store 隱私標籤）

| 主題 | 我們的做法 |
|------|------------|
| 帳號 | **不需要**——無需註冊、郵箱登入或手機號 |
| iHTC Studio 收集資料 | **不收集資料（Data Not Collected）**——我們**不**營運接收你個人資料的後端 |
| 網路 | 語料、閱讀、誦讀、聲律學堂、小工具與每日通知在安裝後可**離線**使用 |
| 分析 / 廣告 / 追蹤 | **無**——無第三方分析、廣告或追蹤 SDK；不使用跨 App 追蹤 |
| 可選 Apple 服務 | **iCloud**（你的私有鍵值儲存）、儲存韻卡時的**相簿（僅加入）**、可選 **StoreKit** 打賞、**本地通知**、可選**即時動態**、可選本機**手寫辨識**（Vision） |

## 資料收集

我們**不**收集、出售或出於廣告／分析目的共享個人資訊。

- **無帳號** — 核心功能無需向我們註冊。
- **無分析或廣告** — 應用未整合會向我們回傳的第三方分析、廣告或當機回報 SDK。
- **不上傳內容** — 閱讀歷史、收藏、韻單、筆記、學堂進度與偏好留在本機（以及可選的**你的** iCloud）。它們不會上傳到 iHTC Studio 伺服器，因為**我們不為該 App 營運此類伺服器**。

## 應用如何工作

- **內建語料** — 正文 JSON、白話／英譯、索引與學習輔助隨 App／小工具包分發。瀏覽與學堂**無需**網路請求。
- **本機語音** — 誦讀使用系統 **AVSpeechSynthesizer**（TTS）。我們不會把正文發到 iHTC Studio。
- **小工具與 App Group** — 小工具與主應用透過本機 App Group `group.com.iHTCboy.iRhyme` 共享偏好與輕量狀態。
- **每日通知** — 使用 User Notifications **本機排程**。點按通知會打開指向本機篇目 ID 的深鏈，沒有伺服器推送名單。
- **韻卡** — 圖片在本機渲染。僅在你點儲存時使用**相簿僅加入**。系統分享表可能把圖片發到**你選擇**的 App，隨後適用該目標的隱私政策。
- **手寫搜尋（iOS）** — 可選字形辨識使用 Apple **Vision**，在本機完成。筆跡不上傳。
- **可選打賞** — 「打賞開發者」為消耗型 **StoreKit** 購買，由 Apple 處理。我們收不到銀行卡號。
- **Siri / 捷徑 / 控制中心** — 可選系統整合打開本機深鏈，不會把語料發給我們。
- **可選 Spotlight** — 若開啟索引，由系統在本機建立搜尋索引；我們不營運搜尋後端。

## 本機儲存的資料

| 資料 | 位置 | 用途 |
|------|------|------|
| 聲律語料 | App / Widget Bundle | 離線閱讀與學堂 |
| 收藏與韻單 | App Group UserDefaults | 星標與自訂列表 |
| 瀏覽紀錄 / 最近閱讀 | App Group UserDefaults | 繼續閱讀與歷史 |
| 筆記 | App Group UserDefaults | 你寫下的閱讀心得 |
| 學堂進度與掌握度 | App Group UserDefaults | 聲律學堂狀態、測驗 / 尋對進度 |
| 打卡 | App Group UserDefaults | 每日習慣 |
| 外觀與閱讀偏好 | App Group UserDefaults | 主題、強調色、語言、版面、朗讀、Tab、小工具、字級 |
| 今日一律快取與通知偏好 | App Group UserDefaults | 今日 ID、提醒時間、情境開關 |
| 韻卡偏好 | App Group UserDefaults | 上次風格 / 比例 |
| 引導與 TipKit 狀態 | 標準 UserDefaults | 歡迎引導 / 發現提示 |
| 最近搜尋 | 標準 UserDefaults | 你輸入過的搜尋詞 |
| 主畫面捷徑 | 系統 + 本機偏好 | 你設定的捷徑 |
| 小工具 / 即時動態快照 | App Group / ActivityKit | 展示你已開啟的正文 |

解除安裝會清除與該 App 相關的沙盒與 App Group 資料（以系統行為為準）。可選 iCloud 副本仍留在**你的** iCloud。

## iCloud 同步（可選）

若你在設定中開啟 **iCloud 同步**，應用會透過綁定**你的 Apple ID** 的 Apple **`NSUbiquitousKeyValueStore`** 鏡像：收藏、韻單、閱讀歷史、學堂進度／掌握度、打卡與筆記。同步流量走向 **Apple iCloud**，而不是 iHTC Studio。我們無法讀取你的 iCloud 內容。

## 權限

僅在功能需要時請求：

| 權限 | 何時 | 原因 |
|------|------|------|
| 通知 | 你開啟今日一律提醒 | 本地排程提醒 |
| 相簿（僅加入） | 你儲存韻卡 | 寫入渲染圖片；無需讀取全部照片 |
| iCloud | 你開啟同步 | 同步收藏／韻單／歷史／進度／打卡／筆記 |
| 即時動態（iOS） | 你開啟品讀即時動態 | 在鎖定畫面／動態島顯示正在品讀的篇目 |
| 背景音訊能力 | 你開啟背景誦讀 | App 不在前景時繼續 TTS |

我們**不**請求通訊錄、精確位置、相機、麥克風（除系統 TTS 播放外）或追蹤權限。手寫搜尋使用本機 Vision，不會彈出網路權限。

## 我們明確不做的事

- **不**出售個人資料。
- **不**建立廣告畫像。
- **不**要求帳號或社交登入。
- **不**嵌入用於資料收集的第三方廣告、分析或社交 SDK。
- **不**在你主動儲存韻卡之外存取照片（且僅為「加入」）。
- **不**接收 StoreKit 銀行卡號碼（由 Apple 處理付款）。
- **不**把手寫筆跡或正文上傳到 iHTC Studio。

## 兒童隱私

愛聲律啟蒙是面向一般受眾的語文學習應用，**不屬於兒童類別**。我們不會故意收集包括 13 歲以下（或你所在地區同等年齡）兒童在內的任何人的個人資訊。應用不需要帳號。家庭可在自有裝置上離線使用閱讀與學堂功能。

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
