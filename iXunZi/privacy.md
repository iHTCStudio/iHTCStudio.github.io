---
layout: doc
title: iXunZi — Privacy Policy
app_id: iXunZi
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iXunZi (爱荀子) — fully offline, Data Not Collected, optional iCloud and Photo Library add-only.
---

<section lang="en" markdown="1">

**Last updated:** September 5, 2026

iHTC Studio ("we", "us" or "our"; formerly iHTCTeam) built **iXunZi** (also known as "爱荀子 / 愛荀子", Bundle ID `com.iHTCboy.iXunZi`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on **this page** as the public privacy policy for the app. For App Store Connect, open this Privacy Policy in your browser and copy the address from the address bar (the public site domain may change over time).

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration, email sign-in, or phone number |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your personal data |
| Network | Library, reading, recite, Encouraging Learning Academy, widgets, and daily notifications work **offline** after install |
| Analytics / ads / tracking | **None** — no third-party analytics, advertising, or tracking SDKs; no App Tracking Transparency use |
| Optional Apple services | **iCloud** (your private KVS), **Photo Library (Add Only)** for 荀 cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **on-device handwriting** (Vision), optional **Ask** (on-device Apple Intelligence when available) |

## Data Collection

We do **not** collect, sell, or share personal information for advertising or analytics.

- **No account** — You can use all core features without creating an account with us.
- **No analytics or ads** — The app binary does not integrate third-party analytics, advertising, or crash-reporting SDKs that phone home to us.
- **No content upload** — Your reading history, favorites, lists, notes, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## How the App Works

- **Bundled library** — Text JSON, vernacular/English, indexes, and study aids ship inside the app / widget bundle. Browsing and study do not require a network request.
- **On-device speech** — Recitation uses Apple’s system **AVSpeechSynthesizer** (TTS). We do not send passage text to iHTC Studio.
- **Widgets & App Group** — Widgets and the app share preferences and lightweight state via App Group `group.com.iHTCboy.iXunZi` on your device.
- **Daily notifications** — Scheduled locally with User Notifications. Tapping a notification opens a deep link to a passage ID on device; no server fan-out.
- **荀 cards** — Images are rendered on device. Saving uses **Photo Library add-only** only when you tap save. System Share Sheet may send the image to an app **you** choose; that destination’s privacy policy then applies.
- **Handwriting search (iOS)** — Optional character recognition uses Apple **Vision** on device. Strokes are not uploaded.
- **Optional tip** — “Tip Developer” is a consumable **StoreKit** purchase processed by Apple. We do not receive your payment card details.
- **Siri / Shortcuts / Control Center** — Optional system integrations open on-device deep links; they do not send your library to us.
- **Optional Spotlight** — If you enable indexing, content is indexed by the system on device for local search; we do not operate a search backend.

- **Ask Xunzi** — On supported devices (iOS 26+ / macOS 26+ with Apple Intelligence), the optional guide uses Apple **on-device Foundation Models**. Passage context and your question stay on the device; we do **not** upload them to iHTC Studio. If the model is unavailable, the app falls back to bundled commentary.

## Data Stored on Your Device

| Data | Where | Purpose |
|------|-------|---------|
| Xunzi database | App / Widget bundle | Offline reading & study |
| Favorites & lists (荀单 lists) | App Group UserDefaults | Starred passages and user lists |
| Reading history / last read | App Group UserDefaults | Continue reading, history UI |
| Notes | App Group UserDefaults | Reading notes you write |
| Study progress & mastery | App Group UserDefaults | Classroom state, quiz / Hunt progress |
| Practice streak / check-in | App Group UserDefaults | Daily habit |
| Appearance & reading prefs | App Group UserDefaults | Theme, accent, language, layout, TTS, tabs, widgets, font scale |
| Daily Xun cache & notification prefs | App Group UserDefaults | Today’s ID, schedule time, contextual toggle |
| Card preferences | App Group UserDefaults | Last style / ratio choices |
| Onboarding & TipKit state | Standard UserDefaults (device) | Welcome guide / discovery tips |
| Recent searches | Standard UserDefaults (device) | Search history you typed |
| Home Screen quick actions | System + local prefs | Shortcuts you configure |
| Widget / Live Activity snapshots | App Group / ActivityKit | Display text you already opened |

Uninstalling the app removes sandbox and App Group data associated with the app (subject to iOS/macOS behavior). Optional iCloud copies remain in **your** iCloud until you clear them or turn sync off and delete elsewhere.

## iCloud Sync (Optional)

If you enable **iCloud Sync** in Settings, the app mirrors selected user data through Apple’s **`NSUbiquitousKeyValueStore`** tied to **your Apple ID**:

- Favorites
- Lists (荀单 lists)
- Reading history
- Study progress / mastery
- Practice streaks
- Notes

Sync traffic goes to **Apple iCloud**, not to iHTC Studio. You can disable sync in Settings. We cannot read your iCloud contents.

## Permissions

iXunZi requests permissions only when a feature needs them:

| Permission | When | Why |
|------------|------|-----|
| Notifications | You enable Daily Xun reminders | Local scheduling of reminder notifications |
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
- We do **not** send Ask questions or passage context to iHTC Studio (on-device Apple Intelligence only, when available).

## Children’s Privacy

iXunZi is an educational literacy app for a general audience and is **not** in the Kids Category. We do not knowingly collect personal information from children. The app does not require an account. Families may use reading and study features offline on their own devices.

## Third Parties

- **Apple** — App Store distribution, optional StoreKit purchases, optional iCloud KVS, system TTS, Share Sheet destinations you pick, and OS-level notification / Live Activity / Siri / Shortcuts / Vision delivery, optional on-device Apple Intelligence for Ask.
- **No other third-party SDKs** for ads, analytics, or social login are included for data collection.

## International Users

The app is designed to function offline on your device. Optional Apple services follow Apple’s terms and regional availability.

## Data Retention & Deletion

- **On device** — Delete the app to remove local sandbox and App Group data (subject to OS behavior).
- **iCloud** — Turn off sync and clear related keys from your iCloud account / devices as needed; we cannot erase your iCloud for you.
- **We retain nothing** on iHTC Studio servers for this app because we do not collect it.

## Policy Changes

We may update this Privacy Policy. The “Last updated” date at the top will change. Continued use after an update means you accept the revised policy. Material changes may also be noted in the App Store “What’s New” text when appropriate.

## Contact

Questions about privacy: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>

<section lang="zh-CN" markdown="1">

**最近更新：** 2026 年 9 月 5 日

爱火腿肠工作室（iHTC Studio）（「我们」；原 iHTCTeam）开发了 **爱荀子**（iXunZi / 愛荀子，Bundle ID `com.iHTCboy.iXunZi`）。本隐私政策说明你在使用本应用时，数据如何被处理。本页可作为 **App Store 审核**与用户查阅的公开隐私政策地址。在 App Store Connect 填写时：打开本站[隐私政策](privacy)页，从浏览器地址栏复制当前网址（站点域名日后可能变更，请勿依赖写死的完整域名）。

## 摘要（对齐 Apple 隐私标签）

| 主题 | 我们的做法 |
|------|------------|
| 账号 | **不需要** — 无注册、邮箱登录或手机号 |
| iHTC Studio 数据采集 | **Data Not Collected** — 我们**不**运营接收你个人数据的后端 |
| 网络 | 语料、品读、诵读、劝学书院、小组件与每日通知安装后均可**离线** |
| 分析 / 广告 / 追踪 | **无** — 无第三方分析、广告或追踪 SDK；不使用 ATT |
| 可选 Apple 服务 | **iCloud**（你的私人 KVS）、保存 荀卡 时的**照片图库（仅添加）**、可选 **StoreKit** 打赏、**本地通知**、可选**实时活动**、可选本机**手写识别**（Vision）、可选本机 **问学**（Apple Intelligence 可用时） |

## 数据采集

我们**不**收集、出售或共享用于广告或分析的个人信息。

- **无账号** — 核心功能无需向我们注册。
- **无分析或广告** — 应用未集成会向我们回传的第三方分析、广告或崩溃 SDK。
- **无内容上传** — 阅读历史、收藏、清单、笔记、学习进度与偏好留在本机（并可选手动同步到**你的** iCloud）。它们不会上传到 iHTC Studio 服务器，因为**本应用不运行此类服务器**。

## 应用如何工作

- **内置语料** — 正文 JSON、白话／英译、索引与学习辅助随 App／小组件打包。浏览与学习无需联网请求。
- **本机语音** — 诵读使用系统 **AVSpeechSynthesizer**（TTS）。我们不会把正文发送到 iHTC Studio。
- **小组件与 App Group** — 通过本机 App Group `group.com.iHTCboy.iXunZi` 共享偏好与轻量状态。
- **每日通知** — 使用本地 User Notifications 调度。点按通知通过深链打开本机篇目 ID；无服务器推送。
- **荀卡** — 在设备上渲染。仅在你点保存时使用**照片图库（仅添加）**。系统分享表可能把图片发给**你选择**的 App，随后适用对方隐私政策。
- **手写寻句（iOS）** — 可选字符识别使用本机 Apple **Vision**。笔迹不会上传。
- **可选打赏** — 「打赏开发者」为 Apple 处理的消耗型 **StoreKit** 购买。我们收不到你的支付卡号。
- **Siri／快捷指令／控制中心** — 可选系统集成打开本机深链；不会把语料发给我们。
- **可选 Spotlight** — 若你开启索引，由系统在本机索引以供本地搜索；我们不运营搜索后端。

- **问荀子** — 在支援装置（iOS 26+ / macOS 26+ 且 Apple Intelligence 可用）上，可选导读使用 Apple **本机 Foundation Models**。篇目上下文与问题留在设备上；**不会**上传到 iHTC Studio。模型不可用时回退内置题解。

## 本机存储的数据

| 数据 | 位置 | 用途 |
|------|------|------|
| 《荀子》语料 | App／小组件 Bundle | 离线阅读与学习 |
| 收藏与清单（荀单） | App Group UserDefaults | 星标篇目与用户清单 |
| 阅读历史／上次阅读 | App Group UserDefaults | 继续阅读、历史界面 |
| 笔记 | App Group UserDefaults | 你写下的阅读笔记 |
| 学习进度与掌握度 | App Group UserDefaults | 学堂、测验／寻句进度 |
| 打卡／连续天数 | App Group UserDefaults | 每日习惯 |
| 外观与阅读偏好 | App Group UserDefaults | 主题、强调色、语言、版式、TTS、标签、小组件、字号 |
| 每日一荀 缓存与通知偏好 | App Group UserDefaults | 今日 ID、提醒时间、情境开关 |
| 分享卡偏好 | App Group UserDefaults | 上次风格／比例 |
| 引导与 TipKit 状态 | 标准 UserDefaults | 欢迎／发现提示 |
| 最近搜索 | 标准 UserDefaults | 你输入的搜索历史 |
| 主屏幕快捷操作 | 系统 + 本地偏好 | 你配置的快捷方式 |
| 小组件／实时活动快照 | App Group／ActivityKit | 展示你已打开的文本 |

卸载应用会移除与之关联的沙盒与 App Group 数据（取决于系统行为）。可选 iCloud 副本仍留在**你的** iCloud，直到你清除或在其他设备关闭同步并删除。

## iCloud 同步（可选）

若在设置中开启 **iCloud 同步**，应用通过绑定**你的 Apple ID** 的 **`NSUbiquitousKeyValueStore`** 镜像所选用户数据：

- 收藏
- 清单（荀单）
- 阅读历史
- 学习进度／掌握度
- 打卡连续天数
- 笔记

同步流量前往 **Apple iCloud**，而非 iHTC Studio。可在设置中关闭同步。我们无法读取你的 iCloud 内容。

## 权限

爱荀子 仅在功能需要时请求权限：

| 权限 | 时机 | 原因 |
|------|------|------|
| 通知 | 你开启 每日一荀 提醒 | 本地调度提醒 |
| 照片图库（仅添加） | 你保存分享卡 | 写入渲染图片；不需要读取完整图库 |
| iCloud | 你开启同步 | 同步收藏／清单／历史／进度／打卡／笔记 |
| 实时活动（iOS） | 你开启阅读实时活动 | 在锁定屏幕／灵动岛显示正在阅读的篇目 |
| 后台音频（能力） | 你开启后台诵读 | 应用不在前台时继续 TTS |

我们**不**请求通讯录、精确位置、相机、麦克风（系统 TTS 播放除外）或追踪。手写寻句使用本机 Vision，不需要联网权限提示。

## 我们不会做的事

- **不**出售个人数据。
- **不**建立广告画像。
- **不**要求账号或社交登录。
- **不**嵌入用于采集数据的第三方广告、分析或社交 SDK。
- **不**在你选择保存分享卡之外访问照片图库。
- **不**接收 StoreKit 支付卡号（由 Apple 处理付款）。
- **不**把手写笔迹或正文上传到 iHTC Studio。
- 我们**不会**把问学问题或篇目上下文上传到 iHTC Studio（仅在可用时使用本机 Apple Intelligence）。

## 儿童隐私

爱荀子 是面向大众的教育类读写应用，**不属于** Kids Category。我们不会有意收集儿童的个人信息。应用不要求账号。家庭可在自有设备上离线使用阅读与学习功能。

## 第三方

- **Apple** — App Store 分发、可选 StoreKit 购买、可选 iCloud KVS、系统 TTS、你选择的分享目标，以及系统级通知／实时活动／Siri／快捷指令／Vision 交付、可选本机 Apple Intelligence（问学）。
- **无其他**用于广告、分析或社交登录的第三方数据采集 SDK。

## 国际用户

应用设计为在你的设备上离线运行。可选 Apple 服务遵循 Apple 条款与地区可用性。

## 数据保留与删除

- **本机** — 删除应用即可移除本地沙盒与 App Group 数据（取决于系统行为）。
- **iCloud** — 关闭同步并按需在你的 iCloud 账户／设备上清除相关键；我们无法替你擦除 iCloud。
- **我们不保留**本应用在 iHTC Studio 服务器上的数据，因为我们根本不采集。

## 政策变更

我们可能更新本隐私政策。文首「最近更新」日期会随之变更。更新后继续使用即表示你接受修订政策。重大变更也可能酌情写在 App Store「新功能」说明中。

## 联系

隐私问题请邮件：[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>

<section lang="zh-TW" markdown="1">

**最近更新：** 2026 年 9 月 5 日

愛火腿腸工作室（iHTC Studio）（「我們」；原 iHTCTeam）開發了 **愛荀子**（iXunZi / 爱荀子，Bundle ID `com.iHTCboy.iXunZi`）。本隱私政策說明你在使用本應用時，資料如何被處理。本頁可作為 **App Store 審核**與使用者查閱的公開隱私政策地址。在 App Store Connect 填寫時：打開本站[隱私政策](privacy)頁，從瀏覽器網址列複製目前網址（站點網域日後可能變更，請勿依賴寫死的完整網域）。

## 摘要（對齊 Apple 隱私標籤）

| 主題 | 我們的做法 |
|------|------------|
| 帳號 | **不需要** — 無註冊、信箱登入或手機號碼 |
| iHTC Studio 資料蒐集 | **Data Not Collected** — 我們**不**營運接收你個人資料的後端 |
| 網路 | 語料、品讀、誦讀、勸學書院、小工具與每日通知安裝後均可**離線** |
| 分析 / 廣告 / 追蹤 | **無** — 無第三方分析、廣告或追蹤 SDK；不使用 ATT |
| 可選 Apple 服務 | **iCloud**（你的私人 KVS）、儲存 荀卡 時的**照片圖庫（僅加入）**、可選 **StoreKit** 打賞、**本機通知**、可選**即時動態**、可選本機**手寫辨識**（Vision）、可選本機 **問學**（Apple Intelligence 可用時） |

## 資料蒐集

我們**不**蒐集、出售或共享用於廣告或分析的個人資訊。

- **無帳號** — 核心功能無需向我們註冊。
- **無分析或廣告** — 應用未整合會向我們回傳的第三方分析、廣告或崩潰 SDK。
- **無內容上傳** — 閱讀歷史、收藏、清單、筆記、學習進度與偏好留在本機（並可選手動同步到**你的** iCloud）。它們不會上傳到 iHTC Studio 伺服器，因為**本應用不運行此類伺服器**。

## 應用如何運作

- **內建語料** — 正文 JSON、白話／英譯、索引與學習輔助隨 App／小工具打包。瀏覽與學習無需連網請求。
- **本機語音** — 誦讀使用系統 **AVSpeechSynthesizer**（TTS）。我們不會把正文傳送到 iHTC Studio。
- **小工具與 App Group** — 透過本機 App Group `group.com.iHTCboy.iXunZi` 共享偏好與輕量狀態。
- **每日通知** — 使用本機 User Notifications 排程。點按通知透過深鏈打開本機篇目 ID；無伺服器推播。
- **荀卡** — 在裝置上渲染。僅在你點儲存時使用**照片圖庫（僅加入）**。系統分享表可能把圖片傳給**你選擇**的 App，隨後適用對方隱私政策。
- **手寫尋句（iOS）** — 可選字元辨識使用本機 Apple **Vision**。筆跡不會上傳。
- **可選打賞** — 「打賞開發者」為 Apple 處理的消耗型 **StoreKit** 購買。我們收不到你的支付卡號。
- **Siri／捷徑／控制中心** — 可選系統整合打開本機深鏈；不會把語料傳給我們。
- **可選 Spotlight** — 若你開啟索引，由系統在本機索引以供本機搜尋；我們不營運搜尋後端。

- **問荀子** — 在支援裝置（iOS 26+ / macOS 26+ 且 Apple Intelligence 可用）上，可選導讀使用 Apple **本機 Foundation Models**。篇目上下文與問題留在裝置上；**不會**上傳到 iHTC Studio。模型不可用時回退內建題解。

## 本機儲存的資料

| 資料 | 位置 | 用途 |
|------|------|------|
| 《荀子》語料 | App／小工具 Bundle | 離線閱讀與學習 |
| 收藏與清單（荀單） | App Group UserDefaults | 星標篇目與使用者清單 |
| 閱讀歷史／上次閱讀 | App Group UserDefaults | 繼續閱讀、歷史介面 |
| 筆記 | App Group UserDefaults | 你寫下的閱讀筆記 |
| 學習進度與掌握度 | App Group UserDefaults | 學堂、測驗／尋句進度 |
| 打卡／連續天數 | App Group UserDefaults | 每日習慣 |
| 外觀與閱讀偏好 | App Group UserDefaults | 主題、強調色、語言、版式、TTS、標籤、小工具、字級 |
| 每日一荀 快取與通知偏好 | App Group UserDefaults | 今日 ID、提醒時間、情境開關 |
| 分享卡偏好 | App Group UserDefaults | 上次風格／比例 |
| 引導與 TipKit 狀態 | 標準 UserDefaults | 歡迎／探索提示 |
| 最近搜尋 | 標準 UserDefaults | 你輸入的搜尋歷史 |
| 主畫面快捷操作 | 系統 + 本機偏好 | 你設定的捷徑 |
| 小工具／即時動態快照 | App Group／ActivityKit | 展示你已打開的文字 |

解除安裝應用會移除與之關聯的沙盒與 App Group 資料（取決於系統行為）。可選 iCloud 副本仍留在**你的** iCloud，直到你清除或在其他裝置關閉同步並刪除。

## iCloud 同步（可選）

若在設定中開啟 **iCloud 同步**，應用透過綁定**你的 Apple ID** 的 **`NSUbiquitousKeyValueStore`** 鏡像所選使用者資料：

- 收藏
- 清單（荀單）
- 閱讀歷史
- 學習進度／掌握度
- 打卡連續天數
- 筆記

同步流量前往 **Apple iCloud**，而非 iHTC Studio。可在設定中關閉同步。我們無法讀取你的 iCloud 內容。

## 權限

愛荀子 僅在功能需要時請求權限：

| 權限 | 時機 | 原因 |
|------|------|------|
| 通知 | 你開啟 每日一荀 提醒 | 本機排程提醒 |
| 照片圖庫（僅加入） | 你儲存分享卡 | 寫入渲染圖片；不需要讀取完整圖庫 |
| iCloud | 你開啟同步 | 同步收藏／清單／歷史／進度／打卡／筆記 |
| 即時動態（iOS） | 你開啟閱讀即時動態 | 在鎖定畫面／動態島顯示正在閱讀的篇目 |
| 背景音訊（能力） | 你開啟背景誦讀 | 應用不在前景時繼續 TTS |

我們**不**請求通訊錄、精確位置、相機、麥克風（系統 TTS 播放除外）或追蹤。手寫尋句使用本機 Vision，不需要連網權限提示。

## 我們不會做的事

- **不**出售個人資料。
- **不**建立廣告畫像。
- **不**要求帳號或社交登入。
- **不**嵌入用於蒐集資料的第三方廣告、分析或社交 SDK。
- **不**在你選擇儲存分享卡之外存取照片圖庫。
- **不**接收 StoreKit 支付卡號（由 Apple 處理付款）。
- **不**把手寫筆跡或正文上傳到 iHTC Studio。
- 我們**不會**把問學問題或篇目上下文上傳到 iHTC Studio（僅在可用時使用本機 Apple Intelligence）。

## 兒童隱私

愛荀子 是面向大眾的教育類讀寫應用，**不屬於** Kids Category。我們不會有意蒐集兒童的個人資訊。應用不要求帳號。家庭可在自有裝置上離線使用閱讀與學習功能。

## 第三方

- **Apple** — App Store 發佈、可選 StoreKit 購買、可選 iCloud KVS、系統 TTS、你選擇的分享目標，以及系統級通知／即時動態／Siri／捷徑／Vision 交付、可選本機 Apple Intelligence（問學）。
- **無其他**用於廣告、分析或社交登入的第三方資料蒐集 SDK。

## 國際使用者

應用設計為在你的裝置上離線運行。可選 Apple 服務遵循 Apple 條款與地區可用性。

## 資料保留與刪除

- **本機** — 刪除應用即可移除本機沙盒與 App Group 資料（取決於系統行為）。
- **iCloud** — 關閉同步並按需在你的 iCloud 帳戶／裝置上清除相關鍵；我們無法替你擦除 iCloud。
- **我們不保留**本應用在 iHTC Studio 伺服器上的資料，因為我們根本不蒐集。

## 政策變更

我們可能更新本隱私政策。文首「最近更新」日期會隨之變更。更新後繼續使用即表示你接受修訂政策。重大變更也可能酌情寫在 App Store「新功能」說明中。

## 聯絡

隱私問題請寄信：[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
