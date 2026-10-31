---
layout: doc
title: iGuanZhi — Privacy Policy
app_id: iGuanZhi
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iGuanZhi (爱古文观止) — fully offline, Data Not Collected, optional iCloud and Photo Library add-only.
---

<section lang="en" markdown="1">

**Last updated:** September 5, 2026

iHTC Studio ("we", "us" or "our") built **iGuanZhi** (also known as "爱古文观止 / 愛古文觀止", Bundle ID `com.iHTCboy.iGuanZhi`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on **this page** as the public privacy policy for the app. For App Store Connect, open this Privacy Policy in your browser and copy the address from the address bar (the public site domain may change over time).

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration, email sign-in, or phone number |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your personal data |
| Network | Library, reading, recite, Classics Study, widgets, and daily notifications work **offline** after install |
| Analytics / ads / tracking | **None** — no third-party analytics, advertising, or tracking SDKs; no App Tracking Transparency use |
| Optional Apple services | **iCloud** (your private KVS), **Photo Library (Add Only)** for 古 cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **on-device handwriting** (Vision) |

## Data Collection

We do **not** collect, sell, or share personal information for advertising or analytics.

- **No account** — You can use all core features without creating an account with us.
- **No analytics or ads** — The app binary does not integrate third-party analytics, advertising, or crash-reporting SDKs that phone home to us.
- **No content upload** — Your reading history, favorites, lists, notes, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## How the App Works

- **Bundled library** — Text JSON, vernacular/English, indexes, and study aids ship inside the app / widget bundle. Browsing and study do not require a network request.
- **On-device speech** — Recitation uses Apple’s system **AVSpeechSynthesizer** (TTS). We do not send passage text to iHTC Studio.
- **Widgets & App Group** — Widgets and the app share preferences and lightweight state via App Group `group.com.iHTCboy.iGuanZhi` on your device.
- **Daily notifications** — Scheduled locally with User Notifications. Tapping a notification opens a deep link to a passage ID on device; no server fan-out.
- **古 cards** — Images are rendered on device. Saving uses **Photo Library add-only** only when you tap save. System Share Sheet may send the image to an app **you** choose; that destination’s privacy policy then applies.
- **Handwriting search (iOS)** — Optional character recognition uses Apple **Vision** on device. Strokes are not uploaded.
- **Optional tip** — “Tip Developer” is a consumable **StoreKit** purchase processed by Apple. We do not receive your payment card details.
- **Siri / Shortcuts / Control Center** — Optional system integrations open on-device deep links; they do not send your library to us.
- **Optional Spotlight** — If you enable indexing, content is indexed by the system on device for local search; we do not operate a search backend.

## Data Stored on Your Device

| Data | Where | Purpose |
|------|-------|---------|
| Guwen Guanzhi database | App / Widget bundle | Offline reading & study |
| Favorites & lists (essay lists) | App Group UserDefaults | Starred passages and user lists |
| Reading history / last read | App Group UserDefaults | Continue reading, history UI |
| Notes | App Group UserDefaults | Reading notes you write |
| Study progress & mastery | App Group UserDefaults | Classroom state, quiz / Hunt progress |
| Practice streak / check-in | App Group UserDefaults | Daily habit |
| Appearance & reading prefs | App Group UserDefaults | Theme, accent, language, layout, TTS, tabs, widgets, font scale |
| Today’s Essay cache & notification prefs | App Group UserDefaults | Today’s ID, schedule time, contextual toggle |
| Card preferences | App Group UserDefaults | Last style / ratio choices |
| Onboarding & TipKit state | Standard UserDefaults (device) | Welcome guide / discovery tips |
| Recent searches | Standard UserDefaults (device) | Search history you typed |
| Home Screen quick actions | System + local prefs | Shortcuts you configure |
| Widget / Live Activity snapshots | App Group / ActivityKit | Display text you already opened |

Uninstalling the app removes sandbox and App Group data associated with the app (subject to iOS/macOS behavior). Optional iCloud copies remain in **your** iCloud until you clear them or turn sync off and delete elsewhere.

## iCloud Sync (Optional)

If you enable **iCloud Sync** in Settings, the app mirrors selected user data through Apple’s **`NSUbiquitousKeyValueStore`** tied to **your Apple ID**:

- Favorites
- Lists (essay lists)
- Reading history
- Study progress / mastery
- Practice streaks
- Notes

Sync traffic goes to **Apple iCloud**, not to iHTC Studio. You can disable sync in Settings. We cannot read your iCloud contents.

## Permissions

iGuanZhi requests permissions only when a feature needs them:

| Permission | When | Why |
|------------|------|-----|
| Notifications | You enable Today’s Essay reminders | Local scheduling of reminder notifications |
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

iGuanZhi is an educational literacy app for a general audience and is **not** in the Kids Category. We do not knowingly collect personal information from children. The app does not require an account. Families may use reading and study features offline on their own devices.

## Third Parties

- **Apple** — App Store distribution, optional StoreKit purchases, optional iCloud KVS, system TTS, Share Sheet destinations you pick, and OS-level notification / Live Activity / Siri / Shortcuts / Vision delivery.
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

爱火腿肠工作室（iHTC Studio）（「我们」）开发了 **爱古文观止**（iGuanZhi / 愛古文觀止，Bundle ID `com.iHTCboy.iGuanZhi`）。本隐私政策说明你在使用本应用时，数据如何被处理。本页可作为 **App Store 审核**与用户查阅的公开隐私政策地址。在 App Store Connect 填写时：打开本站[隐私政策](../privacy)页，从浏览器地址栏复制当前网址（站点域名日后可能变更，请勿依赖写死的完整域名）。

## 摘要（对齐 Apple 隐私标签）

| 主题 | 我们的做法 |
|------|------------|
| 账号 | **不需要** — 无注册、邮箱登录或手机号 |
| iHTC Studio 数据采集 | **Data Not Collected** — 我们**不**运营接收你个人数据的后端 |
| 网络 | 语料、品读、诵读、古文学堂、小组件与每日通知安装后均可**离线** |
| 分析 / 广告 / 追踪 | **无** — 无第三方分析、广告或追踪 SDK；不使用 ATT |
| 可选 Apple 服务 | **iCloud**（你的私人 KVS）、保存 古卡 时的**照片图库（仅添加）**、可选 **StoreKit** 打赏、**本地通知**、可选**实时活动**、可选本机**手写识别**（Vision） |

## 数据采集

我们**不**收集、出售或共享用于广告或分析的个人信息。

- **无账号** — 核心功能无需向我们注册。
- **无分析或广告** — 应用未集成会向我们回传的第三方分析、广告或崩溃 SDK。
- **无内容上传** — 阅读历史、收藏、清单、笔记、学习进度与偏好留在本机（并可选手动同步到**你的** iCloud）。它们不会上传到 iHTC Studio 服务器，因为**本应用不运行此类服务器**。

## 应用如何工作

- **内置语料** — 正文 JSON、白话／英译、索引与学习辅助随 App／小组件打包。浏览与学习无需联网请求。
- **本机语音** — 诵读使用系统 **AVSpeechSynthesizer**（TTS）。我们不会把正文发送到 iHTC Studio。
- **小组件与 App Group** — 通过本机 App Group `group.com.iHTCboy.iGuanZhi` 共享偏好与轻量状态。
- **每日通知** — 使用本地 User Notifications 调度。点按通知通过深链打开本机篇目 ID；无服务器推送。
- **古卡** — 在设备上渲染。仅在你点保存时使用**照片图库（仅添加）**。系统分享表可能把图片发给**你选择**的 App，随后适用对方隐私政策。
- **手写寻句（iOS）** — 可选字符识别使用本机 Apple **Vision**。笔迹不会上传。
- **可选打赏** — 「打赏开发者」为 Apple 处理的消耗型 **StoreKit** 购买。我们收不到你的支付卡号。
- **Siri／快捷指令／控制中心** — 可选系统集成打开本机深链；不会把语料发给我们。
- **可选 Spotlight** — 若你开启索引，由系统在本机索引以供本地搜索；我们不运营搜索后端。

## 本机存储的数据

| 数据 | 位置 | 用途 |
|------|------|------|
| 《古文观止》语料 | App／小组件 Bundle | 离线阅读与学习 |
| 收藏与清单（篇单） | App Group UserDefaults | 星标篇目与用户清单 |
| 阅读历史／上次阅读 | App Group UserDefaults | 继续阅读、历史界面 |
| 笔记 | App Group UserDefaults | 你写下的阅读笔记 |
| 学习进度与掌握度 | App Group UserDefaults | 学堂、测验／寻句进度 |
| 打卡／连续天数 | App Group UserDefaults | 每日习惯 |
| 外观与阅读偏好 | App Group UserDefaults | 主题、强调色、语言、版式、TTS、标签、小组件、字号 |
| 今日一文 缓存与通知偏好 | App Group UserDefaults | 今日 ID、提醒时间、情境开关 |
| 分享卡偏好 | App Group UserDefaults | 上次风格／比例 |
| 引导与 TipKit 状态 | 标准 UserDefaults | 欢迎／发现提示 |
| 最近搜索 | 标准 UserDefaults | 你输入的搜索历史 |
| 主屏幕快捷操作 | 系统 + 本地偏好 | 你配置的快捷方式 |
| 小组件／实时活动快照 | App Group／ActivityKit | 展示你已打开的文本 |

卸载应用会移除与之关联的沙盒与 App Group 数据（取决于系统行为）。可选 iCloud 副本仍留在**你的** iCloud，直到你清除或在其他设备关闭同步并删除。

## iCloud 同步（可选）

若在设置中开启 **iCloud 同步**，应用通过绑定**你的 Apple ID** 的 **`NSUbiquitousKeyValueStore`** 镜像所选用户数据：

- 收藏
- 清单（篇单）
- 阅读历史
- 学习进度／掌握度
- 打卡连续天数
- 笔记

同步流量前往 **Apple iCloud**，而非 iHTC Studio。可在设置中关闭同步。我们无法读取你的 iCloud 内容。

## 权限

爱古文观止 仅在功能需要时请求权限：

| 权限 | 时机 | 原因 |
|------|------|------|
| 通知 | 你开启 今日一文 提醒 | 本地调度提醒 |
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

## 儿童隐私

爱古文观止 是面向大众的教育类读写应用，**不属于** Kids Category。我们不会有意收集儿童的个人信息。应用不要求账号。家庭可在自有设备上离线使用阅读与学习功能。

## 第三方

- **Apple** — App Store 分发、可选 StoreKit 购买、可选 iCloud KVS、系统 TTS、你选择的分享目标，以及系统级通知／实时活动／Siri／快捷指令／Vision 交付。
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

愛火腿腸工作室（iHTC Studio）（「我們」）開發了 **愛古文觀止**（iGuanZhi / 爱古文观止，Bundle ID `com.iHTCboy.iGuanZhi`）。本隱私政策說明你在使用本應用時，資料如何被處理。本頁可作為 **App Store 審核**與使用者查閱的公開隱私政策地址。在 App Store Connect 填寫時：打開本站[隱私政策](../privacy)頁，從瀏覽器網址列複製目前網址（站點網域日後可能變更，請勿依賴寫死的完整網域）。

## 摘要（對齊 Apple 隱私標籤）

| 主題 | 我們的做法 |
|------|------------|
| 帳號 | **不需要** — 無註冊、信箱登入或手機號碼 |
| iHTC Studio 資料蒐集 | **Data Not Collected** — 我們**不**營運接收你個人資料的後端 |
| 網路 | 語料、品讀、誦讀、古文學堂、小工具與每日通知安裝後均可**離線** |
| 分析 / 廣告 / 追蹤 | **無** — 無第三方分析、廣告或追蹤 SDK；不使用 ATT |
| 可選 Apple 服務 | **iCloud**（你的私人 KVS）、儲存 古卡 時的**照片圖庫（僅加入）**、可選 **StoreKit** 打賞、**本機通知**、可選**即時動態**、可選本機**手寫辨識**（Vision） |

## 資料蒐集

我們**不**蒐集、出售或共享用於廣告或分析的個人資訊。

- **無帳號** — 核心功能無需向我們註冊。
- **無分析或廣告** — 應用未整合會向我們回傳的第三方分析、廣告或崩潰 SDK。
- **無內容上傳** — 閱讀歷史、收藏、清單、筆記、學習進度與偏好留在本機（並可選手動同步到**你的** iCloud）。它們不會上傳到 iHTC Studio 伺服器，因為**本應用不運行此類伺服器**。

## 應用如何運作

- **內建語料** — 正文 JSON、白話／英譯、索引與學習輔助隨 App／小工具打包。瀏覽與學習無需連網請求。
- **本機語音** — 誦讀使用系統 **AVSpeechSynthesizer**（TTS）。我們不會把正文傳送到 iHTC Studio。
- **小工具與 App Group** — 透過本機 App Group `group.com.iHTCboy.iGuanZhi` 共享偏好與輕量狀態。
- **每日通知** — 使用本機 User Notifications 排程。點按通知透過深鏈打開本機篇目 ID；無伺服器推播。
- **古卡** — 在裝置上渲染。僅在你點儲存時使用**照片圖庫（僅加入）**。系統分享表可能把圖片傳給**你選擇**的 App，隨後適用對方隱私政策。
- **手寫尋句（iOS）** — 可選字元辨識使用本機 Apple **Vision**。筆跡不會上傳。
- **可選打賞** — 「打賞開發者」為 Apple 處理的消耗型 **StoreKit** 購買。我們收不到你的支付卡號。
- **Siri／捷徑／控制中心** — 可選系統整合打開本機深鏈；不會把語料傳給我們。
- **可選 Spotlight** — 若你開啟索引，由系統在本機索引以供本機搜尋；我們不營運搜尋後端。

## 本機儲存的資料

| 資料 | 位置 | 用途 |
|------|------|------|
| 《古文觀止》語料 | App／小工具 Bundle | 離線閱讀與學習 |
| 收藏與清單（篇單） | App Group UserDefaults | 星標篇目與使用者清單 |
| 閱讀歷史／上次閱讀 | App Group UserDefaults | 繼續閱讀、歷史介面 |
| 筆記 | App Group UserDefaults | 你寫下的閱讀筆記 |
| 學習進度與掌握度 | App Group UserDefaults | 學堂、測驗／尋句進度 |
| 打卡／連續天數 | App Group UserDefaults | 每日習慣 |
| 外觀與閱讀偏好 | App Group UserDefaults | 主題、強調色、語言、版式、TTS、標籤、小工具、字級 |
| 今日一文 快取與通知偏好 | App Group UserDefaults | 今日 ID、提醒時間、情境開關 |
| 分享卡偏好 | App Group UserDefaults | 上次風格／比例 |
| 引導與 TipKit 狀態 | 標準 UserDefaults | 歡迎／探索提示 |
| 最近搜尋 | 標準 UserDefaults | 你輸入的搜尋歷史 |
| 主畫面快捷操作 | 系統 + 本機偏好 | 你設定的捷徑 |
| 小工具／即時動態快照 | App Group／ActivityKit | 展示你已打開的文字 |

解除安裝應用會移除與之關聯的沙盒與 App Group 資料（取決於系統行為）。可選 iCloud 副本仍留在**你的** iCloud，直到你清除或在其他裝置關閉同步並刪除。

## iCloud 同步（可選）

若在設定中開啟 **iCloud 同步**，應用透過綁定**你的 Apple ID** 的 **`NSUbiquitousKeyValueStore`** 鏡像所選使用者資料：

- 收藏
- 清單（篇單）
- 閱讀歷史
- 學習進度／掌握度
- 打卡連續天數
- 筆記

同步流量前往 **Apple iCloud**，而非 iHTC Studio。可在設定中關閉同步。我們無法讀取你的 iCloud 內容。

## 權限

愛古文觀止 僅在功能需要時請求權限：

| 權限 | 時機 | 原因 |
|------|------|------|
| 通知 | 你開啟 今日一文 提醒 | 本機排程提醒 |
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

## 兒童隱私

愛古文觀止 是面向大眾的教育類讀寫應用，**不屬於** Kids Category。我們不會有意蒐集兒童的個人資訊。應用不要求帳號。家庭可在自有裝置上離線使用閱讀與學習功能。

## 第三方

- **Apple** — App Store 發佈、可選 StoreKit 購買、可選 iCloud KVS、系統 TTS、你選擇的分享目標，以及系統級通知／即時動態／Siri／捷徑／Vision 交付。
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
<section lang="ja" markdown="1">

**最終更新日：** 2026年9月5日

iHTC Studio（「当社」）は **iGuanZhi**（「爱古文观止 / 愛古文觀止」、Bundle ID `com.iHTCboy.iGuanZhi`）を開発しました。本プライバシーポリシーは、本アプリの利用時にどのデータが取り扱われ、取り扱われないかを説明します。**Apple App Review** とユーザーは、**本ページ**を公開のプライバシーポリシーとして参照できます。App Store Connect では、ブラウザで本プライバシーポリシーを開き、アドレスバーから URL をコピーしてください（公開サイトのドomainは将来変更される場合があります）。

## 概要（Apple プライバシー栄養表示との整合性）

| トピック | 当社の方針 |
|-------|----------------|
| アカウント | **不要** — 登録、メールサインイン、電話番号は必要ありません |
| iHTC Studioによるデータ収集 | **データは収集しません** — 個人データを受け取るバックエンドは運営していません |
| ネットワーク | ライブラリ、読書、暗唱、学習、Hunt、ウィジェット、日次通知はインストール後**オフライン**で動作します |
| 分析 / 広告 / トラッキング | **なし** — サードパーティの分析、広告、トラッキングSDKは使用しておらず、App Tracking Transparencyも使用していません |
| 任意の Apple サービス | **iCloud**（プライベート KVS）、**孟カード**用 **写真ライブラリ（追加のみ）**、任意の **StoreKit** 投げ銭、**ローカル通知**、任意の **ライブアクティビティ**、任意の端末内 **手書き**（Vision） |

## データの収集

当社は、広告や分析のために個人情報を収集、販売、共有することは**ありません**。

- **アカウント不要** — アカウントを作成せずに、すべての基本機能を使用できます。
- **分析や広告なし** — アプリのバイナリには、サードパーティの分析、広告、クラッシュレポートSDKは統合されておらず、データが当社に送信されることはありません。
- **コンテンツのアップロードなし** — 閲読履歴、お気に入り、リスト、メモ、学習進捗、設定は端末内（および任意で**お客様の** iCloud）に留まります。**当社は本アプリ向けにそのようなサーバーを運用していない**ため、iHTC Studio のサーバーにアップロードされることはありません。

## アプリの仕組み

- **同梱ライブラリ** — テキスト JSON、白話／英語、索引、学習補助はアプリ／ウィジェット バンドル内に同梱されます。閲覧と学習にネットワークは不要です。
- **オンデバイス音声** - 朗読には Apple のシステム **AVSpeechSynthesizer** (TTS) が使用されます。 iHTC Studio には文章テキストは送信されません。
- **ウィジェットと App Group** — ウィジェットとアプリは、端末上の App Group `group.com.iHTCboy.iGuanZhi` を通じて設定と軽量な状態を共有します。
- **毎日の通知** - ユーザー通知を使用してローカルにスケジュールされます。 通知をタップすると、デバイス上のパッセージ ID へのディープ リンクが開きます。 サーバーのファンアウトはありません。
- **古カード** — 画像は端末上で生成されます。保存は「保存」をタップしたときのみ **写真ライブラリ（追加のみ）** を使用します。共有シートは**お客様が選んだ**アプリに画像を送ることがあり、その場合は送信先のプライバシーポリシーが適用されます。
- **手書き検索 (iOS)** - オプションの文字認識では、デバイス上の Apple **Vision** を使用します。 ストロークはアップロードされません。
- **オプションのチップ** - 「チップ開発者」は、Apple によって処理される消耗品 **StoreKit** の購入です。 私たちはあなたの支払いカードの詳細を受け取りません。
- **Siri / ショートカット / コントロール センター** — オプションのシステム統合により、デバイス上のディープ リンクが開きます。 彼らはあなたのライブラリを私たちに送ることはありません。
- **オプションのスポットライト** — インデックス作成を有効にすると、ローカル検索のためにデバイス上のシステムによってコンテンツのインデックスが作成されます。 当社は検索バックエンドを運用していません。

## 端末に保存されるデータ

 | データ | どこ | 目的 |
 |------|-------|-----------|
| Guwen Guanzhi データベース | App / Widget バンドル | オフライン閲読と学習 |
| お気に入りとリスト（essay lists） | App Group UserDefaults | 星付きの篇とユーザーリスト |
 | 読書履歴 / 最後に読んだ | アプリグループのUserDefaults | 続きを読む、履歴 UI |
 | メモ | アプリグループのUserDefaults | あなたが書いた読書メモ |
 | 学習の進捗と習熟度 | アプリグループのUserDefaults | 教室の様子、クイズ・ハントの進行状況 |
 | 連続練習 / チェックイン | アプリグループのUserDefaults | 日々の習慣 |
| 共有カードの設定 | App Group の UserDefaults | 最後に選んだスタイルや比率 |
| Today’s Essay cache & notification prefs | App Group UserDefaults | 今日の ID, 時刻, 文脈トグル |
| カード設定 | App Group UserDefaults | 最後のスタイル / 比率 |
 | オンボーディングと TipKit の状態 | 標準 UserDefaults (デバイス) | ウェルカムガイド / 発見のヒント |
| 最近の検索 | Standard UserDefaults (device) | 入力した検索履歴 |
 | ホーム画面のクイックアクション | システム + ローカル設定 | 設定するショートカット |
 | ウィジェット / ライブ アクティビティのスナップショット | アプリグループ / ActivityKit | すでに開いているテキストを表示 |

アプリをアンインストールすると、アプリに関連するサンドボックスおよびApp Groupデータが削除されます（iOS/macOSの動作に依存します）。任意のiCloudコピーは、あなたが削除するか、同期をオフにして他の場所で削除するまで、**あなたの**iCloudに残ります。

## iCloud同期（オプション）

設定で**iCloud同期**を有効にすると、アプリは選択したユーザーデータをAppleの**`NSUbiquitousKeyValueStore`**を通じてあなたのApple IDに関連付けて同期します：

- お気に入り
- リスト（随园诗话リスト）
- 読書履歴
- 学習進捗 / 習熟度
- 練習の連続日数
 - 注意事項

同期トラフィックは**Apple iCloud**にのみ送信され、iHTC Studioには送信されません。設定で同期を無効にできます。私たちはあなたのiCloudの内容を読むことはできません。

## 権限

 iLiezi は、機能が必要な場合にのみアクセス許可を要求します。

| 権限 | タイミング | 理由 |
|------------|------|-----|
| 通知 | Today’s Essay reminders を有効にする | ローカルスケジュール of reminder notifications |
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

iGuanZhi は一般向けの教育・読書アプリであり、**Kids Category には属しません**。当社は児童から故意に個人情報を収集しません。アカウントは不要です。家族は各自の端末で、オフラインの読書・学習機能をご利用いただけます。

## 第三者

- **Apple** — App Store 配信、任意の StoreKit 購入、任意の iCloud KVS、システム TTS、お客様が選ぶ共有シートの送信先、OS レベルの通知／ライブアクティビティ／Siri／ショートカット／Vision の提供。
- 広告、分析、ソーシャルログインのデータ収集のために**他のサードパーティSDKは含まれていません**。

## 国際ユーザー

このアプリは、お使いのデバイス上でオフラインで機能するように設計されています。オプションのAppleサービスは、Appleの利用規約および地域での利用可能性に従います。

## データ保持と削除

- **デバイス上** — アプリを削除すると、ローカルのサンドボックスおよびApp Groupデータが削除されます（OSの動作によります）。
- **iCloud** — 同期をオフにし、必要に応じて iCloud アカウント／端末から関連キーを削除してください。当社がお客様の iCloud を代わりに消去することはできません。
- **当社は何も保持しません** — このアプリに関してiHTC Studioのサーバー上にデータを収集していません。

## ポリシーの変更

本プライバシーポリシーは更新される場合があります。上部の「最終更新日」が変更されます。更新後も利用を続ける場合、改訂版に同意したものとみなされます。重要な変更は、適宜 App Store の「新機能」にも記載されることがあります。

## お問い合わせ

プライバシーに関するご質問: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ko" markdown="1">

**최종 업데이트:** 2026년 9월 5일

iHTC Studio("당사")는 **iGuanZhi**("爱古文观止 / 愛古文觀止", Bundle ID `com.iHTCboy.iGuanZhi`)을(를) 개발했습니다. 본 개인정보 처리방침은 앱 사용 시 어떤 데이터가 처리되고 처리되지 않는지 설명합니다. **Apple App Review**와 사용자는 **이 페이지**를 공개 개인정보 처리방침으로 사용할 수 있습니다. App Store Connect에는 브라우저에서 본 개인정보 처리방침을 열고 주소창의 URL을 복사하세요(공개 사이트 도메인은 변경될 수 있습니다).

## 요약 (Apple 개인정보 영양성분표 정렬)

| 주제 | 당사의 정책 |
|-------|----------------|
| 계정 | **필요 없음** — 등록, 이메일 로그인, 전화번호 필요 없음 |
| iHTC 스튜디오의 데이터 수집 | **데이터 수집 없음** — 개인 데이터를 받는 백엔드를 운영하지 않습니다 |
| 네트워크 | 라이브러리, 읽기, 암기, 학습, Hunt, 위젯, 일일 알림은 설치 후 **오프라인**에서도 작동 |
| 분석 / 광고 / 추적 | **없음** — 타사 분석, 광고, 추적 SDK 없음; 앱 추적 투명성(App Tracking Transparency) 사용 없음 |
| 선택적 Apple 서비스 | **iCloud**(개인 KVS), **孟 카드**용 **사진 보관함(추가 전용)**, 선택 **StoreKit** 후원, **로컬 알림**, 선택 **Live Activities**, 선택 기기 내 **손글씨**(Vision) |

## 데이터 수집

개인 정보를 광고나 분석 목적으로 **수집, 판매, 공유하지 않습니다**.

- **계정 불필요** — 계정을 만들지 않아도 모든 핵심 기능을 사용할 수 있습니다.
- **분석 및 광고 없음** — 앱 바이너리는 당사로 데이터를 전송하는 타사 분석, 광고, 크래시 리포트 SDK를 통합하지 않습니다.
- **콘텐츠 업로드 없음** — 읽기 기록, 즐겨찾기, 목록, 메모, 학습 진행, 설정은 기기(및 선택적으로 **사용자의** iCloud)에만 남습니다. **이 앱용 서버를 운영하지 않으므로** iHTC Studio 서버로 업로드되지 않습니다.

## 앱 작동 방식

- **번들 라이브러리** — 텍스트 JSON, vernacular/English, 색인, 학습 보조 자료가 앱/위젯 번들에 포함됩니다. 탐색과 학습에 네트워크가 필요하지 않습니다.
- **기기 내 음성** — 암송은 Apple 시스템 **AVSpeechSynthesizer**(TTS)를 사용합니다. iHTC Studio에는 문구 텍스트를 보내지 않습니다.
- **위젯 및 App Group** — 위젯과 앱은 기기의 App Group `group.com.iHTCboy.iGuanZhi`을 통해 설정과 가벼운 상태를 공유합니다.
- **일일 알림** — 사용자 알림을 통해 로컬로 예약됩니다. 알림을 탭하면 기기의 통로 ID에 대한 딥 링크가 열립니다. 서버 팬아웃이 없습니다.
- **古 카드** — 이미지는 기기에서 생성됩니다. 저장은 저장을 탭할 때만 **사진 보관함(추가 전용)** 을 사용합니다. 시스템 공유 시트는 **사용자가 선택한** 앱으로 이미지를 보낼 수 있으며, 해당 앱의 개인정보 처리방침이 적용됩니다.
- **필기 검색(iOS)** — 선택적 문자 인식은 장치에서 Apple **Vision**을 사용합니다. 스트로크는 업로드되지 않습니다.
- **선택적 팁** — "팁 개발자"는 Apple에서 처리하는 소모품 **StoreKit** 구매입니다. 귀하의 결제 카드 정보는 수신되지 않습니다.
- **Siri / 바로가기 / 제어 센터** — 선택적 시스템 통합으로 기기 내 딥 링크가 열립니다. 그들은 귀하의 라이브러리를 우리에게 보내지 않습니다.
- **선택적 스포트라이트** — 인덱싱을 활성화하면 로컬 검색을 위해 장치의 시스템에서 콘텐츠를 인덱싱합니다. 우리는 검색 백엔드를 운영하지 않습니다.

## 귀하의 장치에 저장된 데이터

| 데이터 | 어디 | 목적 |
|------|-------|---------|
| Guwen Guanzhi 데이터베이스 | App / Widget 번들 | 오프라인 읽기 및 학습 |
| 즐겨찾기·목록(essay lists) | App Group UserDefaults | 별표 구절·목록 |
| 읽은 이력/마지막 읽은 내용 | 앱 그룹 UserDefaults | 계속 읽기, 기록 UI |
| 메모 | 앱 그룹 UserDefaults | 당신이 쓴 메모 읽기 |
| 학습 진행 및 숙달 | 앱 그룹 UserDefaults | 교실상태, 퀴즈/사냥 진행 |
| 연속연습/체크인 | 앱 그룹 UserDefaults | 일상습관 |
| 공유 카드 설정 | App Group UserDefaults | 마지막으로 선택한 스타일 / 비율 |
| Today’s Essay cache & notification prefs | App Group UserDefaults | 오늘 ID, 시간, contextual toggle |
| 카드 설정 | App Group UserDefaults | 마지막 스타일/비율 |
| 온보딩 및 TipKit 상태 | 표준 UserDefaults(장치) | 환영 가이드/탐색 팁 |
| 최근 검색 | Standard UserDefaults (device) | 입력 검색 기록 |
| 홈 화면 빠른 작업 | 시스템 + 로컬 환경설정 | 구성한 바로가기 |
| 위젯/실시간 활동 스냅샷 | 앱 그룹/ActivityKit | 이미 열어본 텍스트 표시 |

앱을 삭제하면 앱과 연관된 샌드박스 및 앱 그룹 데이터가 제거됩니다(iOS/macOS 동작에 따라 다름). 선택적으로 iCloud에 저장된 복사본은 사용자가 삭제하거나 동기화를 끄고 다른 곳에서 삭제할 때까지 **귀하의** iCloud에 남아 있습니다.

## iCloud 동기화 (선택 사항)

설정에서 **iCloud 동기화**를 활성화하면, 앱은 **귀하의 Apple ID**와 연결된 Apple의 **`NSUbiquitousKeyValueStore`**를 통해 선택한 사용자 데이터를 미러링합니다:

- 즐겨찾기
- 목록(essay lists)
- 읽기 기록
- 학습 진행/숙련도
- 연습 연속 기록
- 메모

동기화 트래픽은 iHTC Studio가 아닌 **Apple iCloud**로 전송됩니다. 설정에서 동기화를 비활성화할 수 있습니다. 우리는 귀하의 iCloud 내용을 읽을 수 없습니다.

## 권한

iLiezi는 기능에 필요한 경우에만 권한을 요청합니다.

| 허가 | 언제 | 왜? |
|------------|------|-----|
| 알림 | Today’s Essay reminders 사용 | 로컬 예약 of reminder notifications |
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

iGuanZhi은(는) 일반 대중을 위한 교육용 독서 앱이며 **Kids Category에 해당하지 않습니다**. 당사는 아동으로부터 고의로 개인정보를 수집하지 않습니다. 계정이 필요하지 않습니다. 가족은 각자의 기기에서 오프라인으로 읽기·학습 기능을 사용할 수 있습니다.

## 제3자

- **Apple** — App Store 배포, 선택적 StoreKit 구매, 선택적 iCloud KVS, 시스템 TTS, 사용자가 선택하는 공유 시트 대상, OS 수준 알림/Live Activities/Siri/Shortcuts/Vision 제공.
- 광고, 분석, 소셜 로그인 등을 위한 **기타 제3자 SDK**는 데이터 수집을 위해 포함되지 않았습니다.

## 국제 사용자

앱은 사용자의 장치에서 오프라인 기능이 가능하도록 설계되었습니다. 선택적 Apple 서비스는 Apple의 이용 약관 및 지역 가용성을 따릅니다.

## 데이터 보존 및 삭제

- **기기 내** — 앱을 삭제하여 로컬 샌드박스 및 앱 그룹 데이터를 제거합니다(운영 체제 동작에 따라 다를 수 있음).
- **iCloud** — 동기화를 끄고 필요 시 iCloud 계정/기기에서 관련 키를 삭제하세요. iCloud를 대신 지울 수 없습니다.
- **저희는 아무것도 보관하지 않습니다** — iHTC Studio 서버에는 이 앱과 관련된 데이터를 수집하지 않기 때문에 저장하지 않습니다.

## 정책 변경

본 개인정보 처리방침은 업데이트될 수 있습니다. 상단의 「최종 업데이트」 날짜가 변경됩니다. 업데이트 후 계속 사용하면 개정된 정책에 동의하는 것입니다. 중요한 변경은 App Store 「새로운 기능」에도 적절히 안내될 수 있습니다.

## 연락처

개인정보 관련 문의: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ru" markdown="1">

**Дата последнего обновления:** 5 сентября 2026 г.

iHTC Studio («мы») создала **iGuanZhi** («爱古文观止 / 愛古文觀止», Bundle ID `com.iHTCboy.iGuanZhi`). Настоящая Политика конфиденциальности объясняет, какие данные обрабатываются (и не обрабатываются) при использовании приложения. **Apple App Review** и пользователи могут использовать **эту страницу** как публичную политику конфиденциальности. Для App Store Connect откройте эту страницу в браузере и скопируйте URL из адресной строки (домен публичного сайта может измениться).

## Сводка (в соответствии с меткой Apple Privacy Nutrition)

| Тема | Наша практика |
|-------|----------------|
| Учетная запись | **Не требуется** — регистрация, вход по электронной почте или номеру телефона не нужны |
| Сбор данных iHTC Studio | **Данные не собираются** — мы **не** используем серверную часть, которая получает ваши личные данные |
| Сеть | Библиотека, чтение, повторение, учеба, Охота, виджеты и ежедневные уведомления работают **оффлайн** после установки |
| Аналитика / реклама / отслеживание | **Отсутствует** — нет сторонней аналитики, рекламы или SDK для отслеживания; не используется App Tracking Transparency |
| Необязательные сервисы Apple | **iCloud** (личный KVS), **Фототека (только добавление)** для карточек 孟, **StoreKit** для необязательных чаевых, **локальные уведомления**, необязательные **Live Activities**, необязательное **рукописное ввод** на устройстве (Vision) |

## Сбор данных

Мы **не** собираем, не продаем и не делимся личной информацией для рекламы или аналитики.

- **Без аккаунта** — Вы можете использовать все основные функции без создания аккаунта у нас.
- **Без аналитики и рекламы** — В приложении не интегрированы сторонние SDK для аналитики, рекламы или отчётов о сбоях, которые отправляли бы данные нам.
- **Без загрузки контента** — история чтения, избранное, списки, заметки, прогресс обучения и настройки остаются на устройстве (и, по желанию, в **вашем** iCloud). Они не загружаются на серверы iHTC Studio, потому что **мы не эксплуатируем такие серверы для этого приложения**.

## Как работает приложение

- **Встроенная библиотека** — текстовый JSON, vernacular/English, указатели и учебные материалы входят в пакет app/widget. Для просмотра и обучения сеть не нужна.
- **Речь на устройстве** — при декламации используется система Apple **AVSpeechSynthesizer** (TTS). Мы не отправляем текст прохождения в iHTC Studio.
- **Виджеты и App Group** — виджеты и приложение обмениваются настройками и лёгким состоянием через App Group `group.com.iHTCboy.iGuanZhi` на вашем устройстве.
- **Ежедневные уведомления** — планируются локально с помощью уведомлений пользователя. При нажатии на уведомление открывается глубокая ссылка на идентификатор прохода на устройстве; нет разветвления сервера.
- **Карточки 古** — изображения создаются на устройстве. Сохранение использует **Фототеку (только добавление)** лишь при нажатии «Сохранить». Меню «Поделиться» может передать изображение приложению, **которое вы выберете**; тогда действует политика конфиденциальности получателя.
- **Поиск по рукописному вводу (iOS)** — дополнительное распознавание символов использует Apple **Vision** на устройстве. Штрихи не загружаются.
- **Необязательный совет**. «Tip Developer» — это расходный материал, приобретаемый **StoreKit** и обрабатываемый Apple. Мы не получаем данные вашей платежной карты.
- **Siri / Ярлыки / Центр управления** — дополнительные системные интеграции открывают глубокие ссылки на устройстве; они не отправляют нам вашу библиотеку.
- **Дополнительный Spotlight** — если вы включите индексирование, контент индексируется системой на устройстве для локального поиска; мы не используем поисковую систему.

## Данные, хранящиеся на вашем устройстве

| Данные | Где | Цель |
|------|-------|---------|
| База Guwen Guanzhi | Пакет App / Widget | Офлайн-чтение и обучение |
| Избранное (essay lists) | UserDefaults App Group | Отмеченные фрагменты и списки |
| История чтения / последнее чтение | Пользовательские настройки группы приложений | Продолжить чтение, история пользовательского интерфейса |
| Заметки | Пользовательские настройки группы приложений | Чтение заметок, которые вы пишете |
| Ход учебы и мастерство | Пользовательские настройки группы приложений | Состояние класса, викторина / Ход охоты |
| Практика / регистрация | Пользовательские настройки группы приложений | Ежедневная привычка |
| Настройки карточек для обмена | UserDefaults App Group | Последний выбранный стиль / соотношение сторон |
| Today’s Essay cache & notification prefs | UserDefaults App Group | ID на сегодня, время, переключатели |
| Настройки карточек | UserDefaults App Group | Последний стиль/ratio |
| Регистрация и состояние TipKit | Стандартные настройки пользователя (устройство) | Приветственное руководство / советы по открытию |
| Недавние запросы | Standard UserDefaults (device) | История введённого поиска |
| Быстрые действия на главном экране | Система + локальные настройки | Ярлыки, которые вы настраиваете |
| Виджет / Снимки активности в реальном времени | Группа приложений / ActivityKit | Показать текст, который вы уже открыли |

При удалении приложения удаляются данные песочницы и группы приложений, связанные с приложением (в зависимости от поведения iOS/macOS). Дополнительные копии iCloud остаются в **вашем** iCloud до тех пор, пока вы не очистите их или не отключите синхронизацию и не удалите их в другом месте.

## Синхронизация с iCloud (необязательно)

Если вы включите **iCloud Sync** в настройках, приложение зеркально отображает выбранные пользовательские данные через **`NSUbiquitousKeyValueStore`** Apple, привязанный к **вашему Apple ID**:

- Избранное
- Списки (essay lists)
- Чтение истории
- Прогресс в учебе/мастерстве
- Практика полос
- Примечания

Трафик синхронизации поступает в **Apple iCloud**, а не в iHTC Studio. Вы можете отключить синхронизацию в настройках. Мы не можем прочитать ваше содержимое iCloud.

## Разрешения

iLiezi запрашивает разрешения только тогда, когда они нужны функции:

| Разрешение | Когда | Почему |
|------------|------|-----|
| Уведомления | Вы включаете Today’s Essay reminders | Локальное планирование of reminder notifications |
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

iGuanZhi — образовательное приложение для широкой аудитории и **не относится к Kids Category**. Мы сознательно не собираем персональные данные детей. Приложение не требует учётной записи. Семьи могут пользоваться чтением и обучением офлайн на своих устройствах.

## Третьи стороны

- **Apple** — распространение в App Store, необязательные покупки StoreKit, необязательный iCloud KVS, системный TTS, выбранные вами пункты «Поделиться», а также уведомления на уровне ОС / Live Activities / Siri / Shortcuts / Vision.
- **Никакие другие сторонние SDK** для рекламы, аналитики или социальной авторизации не включены для сбора данных.

## Пользователи из других стран

Приложение предназначено для работы в автономном режиме на вашем устройстве. Необязательные сервисы Apple подчиняются условиям Apple и региональной доступности.

## Сроки хранения и удаление данных

- **На устройстве** — Удалите приложение, чтобы удалить локальные данные песочницы и группы приложений (в зависимости от поведения ОС).
- **iCloud** — Отключите синхронизацию и при необходимости удалите связанные ключи из учётной записи iCloud / устройств; мы не можем стереть ваш iCloud за вас.
- **Мы ничего не сохраняем** на серверах iHTC Studio для этого приложения, так как мы не собираем эти данные.

## Изменения политики

Мы можем обновлять эту Политику конфиденциальности. Дата «Последнего обновления» вверху изменится. Продолжение использования после обновления означает принятие пересмотренной политики. Существенные изменения также могут быть указаны в разделе App Store «Что нового», когда это уместно.

## Контакт

Вопросы о конфиденциальности: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="th" markdown="1">

**อัปเดตล่าสุด:** 5 กันยายน 2026

iHTC Studio ("เรา") พัฒนา **iGuanZhi** ("爱古文观止 / 愛古文觀止", Bundle ID `com.iHTCboy.iGuanZhi`) นโยบายความเป็นส่วนตัวนี้อธิบายว่าข้อมูลใดถูกจัดการและไม่ถูกจัดการเมื่อคุณใช้แอป **Apple App Review** และผู้ใช้สามารถใช้**หน้านี้**เป็นนโยบายความเป็นส่วนตัวสาธารณะ สำหรับ App Store Connect ให้เปิดนโยบายนี้ในเบราว์เซอร์แล้วคัดลอก URL จากแถบที่อยู่ (โดเมนสาธารณะอาจเปลี่ยนได้)

## สรุป (การจัดตำแหน่งกับ Nutrition Label ความเป็นส่วนตัวของ Apple)

| หัวข้อ | การปฏิบัติของเรา |
|-------|----------------|
| บัญชี | **ไม่จำเป็น** — ไม่ต้องลงทะเบียน ลงชื่อเข้าใช้ด้วยอีเมล หรือหมายเลขโทรศัพท์ |
| การเก็บข้อมูลโดย iHTC Studio | **ไม่เก็บข้อมูล** — เรา **ไม่ได้**ดำเนินการแบ็กเอนด์ที่รับข้อมูลส่วนตัวของคุณ |
| เครือข่าย | ห้องสมุด การอ่าน การท่องจำ การศึกษา การล่า วิดเจ็ต และการแจ้งเตือนประจำวันทำงาน **ออฟไลน์** หลังการติดตั้ง |
| การวิเคราะห์ / โฆษณา / การติดตาม | **ไม่มี** — ไม่มี SDK การวิเคราะห์ โฆษณา หรือการติดตามจากบุคคลที่สาม; ไม่ใช้ App Tracking Transparency |
| บริการ Apple เสริม | **iCloud** (KVS ส่วนตัว), **คลังรูปภาพ (เพิ่มอย่างเดียว)** สำหรับการ์ด 孟, **StoreKit** สำหรับทิปแบบเลือกได้, **การแจ้งเตือนในเครื่อง**, **Live Activities** แบบเลือกใช้, **ลายมือบนอุปกรณ์** (Vision) แบบเลือกใช้ |

## การเก็บข้อมูล

เราจะ **ไม่**เก็บ ขาย หรือแชร์ข้อมูลส่วนบุคคลเพื่อโฆษณาหรือการวิเคราะห์

- **ไม่ต้องมีบัญชีผู้ใช้** — คุณสามารถใช้คุณสมบัติหลักทั้งหมดได้โดยไม่ต้องสร้างบัญชีกับเรา
- **ไม่มีการวิเคราะห์หรือโฆษณา** — ไฟล์แอปไม่ได้รวม SDK การวิเคราะห์ การโฆษณา หรือการรายงานข้อผิดพลาดจากบุคคลที่สามที่ติดต่อกลับไปยังเรา
- **ไม่อัปโหลดเนื้อหา** — ประวัติการอ่าน รายการโปรด รายการ บันทึก ความคืบหน้าการเรียน และการตั้งค่าอยู่บนอุปกรณ์ (และอาจอยู่ใน iCloud **ของคุณ**) จะไม่ถูกอัปโหลดไปยังเซิร์ฟเวอร์ iHTC Studio เพราะ **เราไม่ได้ดำเนินการเซิร์ฟเวอร์เช่นนั้นสำหรับแอปนี้**

## วิธีการทำงานของแอป

- **ไลบรารีในชุดแอป** — JSON ข้อความ vernacular/English ดัชนี และตัวช่วยเรียนอยู่ในชุดแอป/วิดเจ็ต การเรียกดูและเรียนไม่ต้องใช้เครือข่าย
- **คำพูดบนอุปกรณ์** — การบรรยายใช้ระบบของ Apple **AVSpeechSynthesizer** (TTS) เราไม่ส่งข้อความข้อความไปที่ iHTC Studio
- **วิดเจ็ตและ App Group** — วิดเจ็ตและแอปใช้การตั้งค่าและสถานะขนาดเล็กร่วมกันผ่าน App Group `group.com.iHTCboy.iGuanZhi` บนอุปกรณ์ของคุณ
- **การแจ้งเตือนรายวัน** — กำหนดเวลาภายในเครื่องด้วยการแจ้งเตือนผู้ใช้ การแตะการแจ้งเตือนจะเปิดลิงก์ในรายละเอียดไปยังรหัสข้อความบนอุปกรณ์ ไม่มีการปิดเซิร์ฟเวอร์
- **การ์ด古** — รูปภาพสร้างบนอุปกรณ์ การบันทึกใช้ **คลังรูปภาพ (เพิ่มอย่างเดียว)** เฉพาะเมื่อแตะบันทึก ชีตแชร์ของระบบอาจส่งรูปไปยังแอปที่**คุณเลือก** ซึ่งจะใช้นโยบายความเป็นส่วนตัวของปลายทางนั้น
- **การค้นหาด้วยลายมือ (iOS)** — ตัวเลือกการรู้จำอักขระใช้ Apple **Vision** บนอุปกรณ์ จังหวะไม่ได้อัปโหลด
- **เคล็ดลับเสริม** — “Tip Developer” เป็นการซื้อ **StoreKit** แบบบริโภคที่ดำเนินการโดย Apple เราไม่ได้รับรายละเอียดบัตรชำระเงินของคุณ
- **Siri / ทางลัด / ศูนย์ควบคุม** — การรวมระบบที่เป็นตัวเลือกจะเปิดลิงก์ในรายละเอียดบนอุปกรณ์ พวกเขาไม่ได้ส่งห้องสมุดของคุณมาให้เรา
- **สปอตไลท์เสริม** — หากคุณเปิดใช้งานการจัดทำดัชนี เนื้อหาจะถูกจัดทำดัชนีโดยระบบบนอุปกรณ์สำหรับการค้นหาในท้องถิ่น เราไม่ได้ดำเนินการแบ็กเอนด์การค้นหา

## ข้อมูลที่เก็บบนอุปกรณ์

| ข้อมูล | ที่ไหน | วัตถุประสงค์ |
|------|-------|---------|
| ฐานข้อมูล Guwen Guanzhi | App / Widget bundle | การอ่านและเรียนแบบออฟไลน์ |
| รายการโปรด (essay lists) | UserDefaults ของ App Group | ข้อความติดดาวและรายการ |
| ประวัติการอ่าน / อ่านครั้งล่าสุด | ค่าเริ่มต้นของกลุ่มแอป | อ่านต่อ ประวัติ UI |
| หมายเหตุ | ค่าเริ่มต้นของกลุ่มแอป | อ่านบันทึกที่คุณเขียน |
| ความก้าวหน้าและความเชี่ยวชาญด้านการศึกษา | ค่าเริ่มต้นของกลุ่มแอป | สภาพห้องเรียน แบบทดสอบ / ล่าความคืบหน้า |
| ฝึกสตรีค/เช็คอิน | ค่าเริ่มต้นของกลุ่มแอป | นิสัยประจำวัน |
| การตั้งค่าการ์ดแชร์ | UserDefaults ของ App Group | สไตล์ / อัตราส่วนที่เลือกล่าสุด |
| Today’s Essay cache & notification prefs | UserDefaults ของ App Group | ID วันนี้, schedule time, contextual toggle |
| การตั้งค่าการ์ด | UserDefaults ของ App Group | สไตล์/อัตราส่วนล่าสุด |
| การเริ่มต้นใช้งานและสถานะ TipKit | Standard UserDefaults (อุปกรณ์) | คู่มือต้อนรับ / เคล็ดลับการค้นพบ |
| การค้นหาล่าสุด | Standard UserDefaults (device) | ประวัติที่พิมพ์ |
| การดำเนินการด่วนบนหน้าจอหลัก | ระบบ + การตั้งค่าท้องถิ่น | ทางลัดที่คุณกำหนดค่า |
| วิดเจ็ต / ภาพรวมกิจกรรมสด | กลุ่มแอป / ActivityKit | แสดงข้อความที่คุณเปิดแล้ว |

การถอนการติดตั้งแอปจะลบข้อมูล sandbox และ App Group ที่เกี่ยวข้องกับแอป (ขึ้นอยู่กับพฤติกรรมของ iOS/macOS) สำเนา iCloud แบบเลือกได้จะยังคงอยู่ใน **iCloud ของคุณ** จนกว่าคุณจะลบหรือปิดการซิงค์และลบจากที่อื่น

## การซิงค์ iCloud (ตัวเลือก)

หากคุณเปิดใช้งาน **การซิงค์ iCloud** ในการตั้งค่า แอปจะสะท้อนข้อมูลผู้ใช้ที่เลือกผ่าน **`NSUbiquitousKeyValueStore`** ของ Apple ที่เชื่อมโยงกับ **Apple ID ของคุณ**:

- รายการโปรด
- รายการ (essay lists)
- ประวัติการอ่าน
- ความคืบหน้า/ความชำนาญในการศึกษา
- สถิติการฝึกต่อเนื่อง
- หมายเหตุ

การจราจรการซิงค์จะไปยัง **Apple iCloud** ไม่ใช่ iHTC Studio คุณสามารถปิดการซิงค์ได้ใน การตั้งค่า เราไม่สามารถอ่านเนื้อหา iCloud ของคุณได้

## สิทธิ์

iLiezi ร้องขอการอนุญาตเฉพาะเมื่อคุณสมบัติต้องการ:

| สิทธิ์ | เมื่อไหร่ | ทำไม |
|------------|------|-----|
| การแจ้งเตือน | คุณเปิด Today’s Essay reminders | กำหนดเวลาในเครื่อง of reminder notifications |
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

iGuanZhi เป็นแอปการอ่านเชิงการศึกษาสำหรับผู้ใช้ทั่วไป และ**ไม่ได้**อยู่ใน Kids Category เราไม่เก็บข้อมูลส่วนบุคคลจากเด็กโดยเจตนา แอปไม่ต้องมีบัญชี ครอบครัวสามารถใช้การอ่านและการเรียนแบบออฟไลน์บนอุปกรณ์ของตนเอง

## บุคคลที่สาม

- **Apple** — การจำหน่าย App Store, การซื้อ StoreKit แบบเลือกได้, iCloud KVS แบบเลือกได้, TTS ของระบบ, ปลายทาง Share Sheet ที่คุณเลือก และการส่งมอบการแจ้งเตือน/Live Activity/Siri/Shortcuts/Vision ระดับ OS
- **ไม่มี SDK ของบุคคลที่สามอื่น ๆ** สำหรับโฆษณา, การวิเคราะห์, หรือการเข้าสู่ระบบโซเชียลรวมอยู่เพื่อการเก็บข้อมูล

## ผู้ใช้ระหว่างประเทศ

แอปออกแบบมาให้ทำงานแบบออฟไลน์บนอุปกรณ์ของคุณ บริการของ Apple ตามตัวเลือกจะเป็นไปตามข้อกำหนดของ Apple และความพร้อมใช้งานในภูมิภาค

## การเก็บรักษาและการลบข้อมูล

- **บนอุปกรณ์** — ลบแอปเพื่อเอาข้อมูล sandbox และ App Group ที่อยู่ในเครื่องออก (ขึ้นอยู่กับพฤติกรรมของระบบปฏิบัติการ)
- **iCloud** — ปิดการซิงค์และลบคีย์ที่เกี่ยวข้องจากบัญชี iCloud / อุปกรณ์ตามต้องการ เราไม่สามารถลบ iCloud ของคุณแทนคุณได้
- **เราไม่เก็บอะไรเลย** บนเซิร์ฟเวอร์ iHTC Studio สำหรับแอปนี้เพราะเราไม่ได้เก็บข้อมูลนั้น

## การเปลี่ยนแปลงนโยบาย

เราอาจปรับปรุงนโยบายความเป็นส่วนตัวนี้ วันที่ 「อัปเดตล่าสุด」 ด้านบนจะเปลี่ยน การใช้งานต่อหลังอัปเดตถือว่าคุณยอมรับนโยบายที่แก้ไข การเปลี่ยนแปลงสำคัญอาจระบุในข้อความ App Store 「มีอะไรใหม่」 เมื่อเหมาะสม

## ติดต่อ

คำถามเกี่ยวกับความเป็นส่วนตัว: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="de" markdown="1">

**Zuletzt aktualisiert:** 5. September 2026

iHTC Studio („wir“) hat **iGuanZhi** („爱古文观止 / 愛古文觀止“, Bundle-ID `com.iHTCboy.iGuanZhi`) entwickelt. Diese Datenschutzerklärung erläutert, welche Daten bei der Nutzung verarbeitet werden (und welche nicht). **Apple App Review** und Nutzer können sich auf **diese Seite** als öffentliche Datenschutzerklärung stützen. Für App Store Connect öffnen Sie diese Seite im Browser und kopieren Sie die URL aus der Adressleiste (die Domain kann sich ändern).

## Zusammenfassung (Übereinstimmung mit dem Apple-Datenschutzetikett)

| Thema | Unsere Praxis |
|-------|----------------|
| Konto | **Nicht erforderlich** — keine Registrierung, kein E-Mail-Login oder Telefonnummer erforderlich |
| Datenerhebung durch iHTC Studio | **Keine Datenerhebung** — wir betreiben **keinen** Backend-Service, der Ihre persönlichen Daten empfängt |
| Netzwerk | Bibliothek, Lesen, Rezitieren, Lernen, Hunt, Widgets und tägliche Benachrichtigungen funktionieren **offline** nach der Installation |
| Analysen / Werbung / Tracking | **Keine** — keine Analysen von Drittanbietern, Werbung oder Tracking-SDKs; keine Nutzung von App Tracking Transparency |
| Optionale Apple-Dienste | **iCloud** (privater KVS), **Fotomediathek (nur Hinzufügen)** für 孟-Karten, **StoreKit** für optionales Trinkgeld, **lokale Benachrichtigungen**, optionale **Live-Aktivitäten**, optionale **Handschrift** auf dem Gerät (Vision) |

## Datenerfassung

Wir erheben, verkaufen oder teilen **keine** persönlichen Informationen für Werbung oder Analysen.

- **Kein Konto** — Sie können alle Kernfunktionen nutzen, ohne ein Konto bei uns zu erstellen.
- **Keine Analysen oder Werbung** — Die App-Binärdatei integriert keine Analysen, Werbung oder Crash-Reporting-SDKs von Drittanbietern, die Daten an uns senden.
- **Kein Hochladen von Inhalten** — Leseverlauf, Favoriten, Listen, Notizen, Lernfortschritt und Einstellungen bleiben auf dem Gerät (optional in **Ihrem** iCloud). Sie werden nicht auf iHTC Studio-Server hochgeladen, da **wir für diese App keine solchen Server betreiben**.

## So funktioniert die App

- **Mitgelieferte Bibliothek** — Text-JSON, Umgangssprache/Englisch, Indizes und Lernhilfen liegen im App-/Widget-Bundle. Durchsuchen und Lernen erfordern kein Netzwerk.
- **Sprache auf dem Gerät** – Die Rezitation nutzt Apples System **AVSpeechSynthesizer** (TTS). Wir senden keine Passagentexte an iHTC Studio.
- **Widgets und App Group** — Widgets und App teilen Einstellungen und leichten Zustand über die App Group `group.com.iHTCboy.iGuanZhi` auf Ihrem Gerät.
- **Tägliche Benachrichtigungen** – Lokal geplant mit Benutzerbenachrichtigungen. Durch Tippen auf eine Benachrichtigung wird ein Deep-Link zu einer Durchgangs-ID auf dem Gerät geöffnet. Kein Server-Fanout.
- **古-Karten** — Bilder werden auf dem Gerät erzeugt. Speichern nutzt **Fotomediathek (nur Hinzufügen)** nur beim Tippen auf Speichern. Das Share Sheet kann das Bild an eine App senden, **die Sie wählen**; dann gilt deren Datenschutzerklärung.
- **Handschriftsuche (iOS)** – Die optionale Zeichenerkennung verwendet Apple **Vision** auf dem Gerät. Striche werden nicht hochgeladen.
- **Optionaler Tipp** – „Tip Developer“ ist ein verbrauchbarer **StoreKit**-Kauf, der von Apple abgewickelt wird. Wir erhalten Ihre Zahlungskartendaten nicht.
- **Siri / Verknüpfungen / Kontrollzentrum** – Optionale Systemintegrationen öffnen Deep Links auf dem Gerät; Sie senden Ihre Bibliothek nicht an uns.
- **Optionales Spotlight** – Wenn Sie die Indizierung aktivieren, werden Inhalte vom System auf dem Gerät für die lokale Suche indiziert; Wir betreiben kein Such-Backend.

## Auf Ihrem Gerät gespeicherte Daten

| Daten | Wo | Zweck |
|------|-------|---------|
| Guwen Guanzhi-Datenbank | App-/Widget-Bundle | Offline-Lesen und -Lernen |
| Favoriten (essay lists) | UserDefaults der App Group | Markierte Passagen & Listen |
| Leseverlauf / zuletzt gelesen | Benutzerstandards der App-Gruppe | Lesen Sie weiter, Verlauf der Benutzeroberfläche |
| Notizen | Benutzerstandards der App-Gruppe | Lesen von Notizen, die Sie schreiben |
| Studienfortschritt & Beherrschung | Benutzerstandards der App-Gruppe | Unterrichtszustand, Quiz/Jagdfortschritt |
| Übungssträhne / Check-in | Benutzerstandards der App-Gruppe | Tägliche Gewohnheit |
| Einstellungen der Teilen-Karten | UserDefaults der App Group | Zuletzt gewählter Stil / zuletzt gewähltes Seitenverhältnis |
| Today’s Essay cache & notification prefs | UserDefaults der App Group | Heutige ID, schedule time, contextual toggle |
| Karten-Einstellungen | UserDefaults der App Group | Letzter Stil/Verhältnis |
| Onboarding- und TipKit-Status | Standard UserDefaults (Gerät) | Willkommensführer / Entdeckungstipps |
| Letzte Suchen | Standard UserDefaults (device) | Suchverlauf Ihrer Eingaben |
| Schnellaktionen auf dem Startbildschirm | System + lokale Einstellungen | Von Ihnen konfigurierte Verknüpfungen |
| Widget-/Live-Aktivitäts-Schnappschüsse | App-Gruppe / ActivityKit | Text anzeigen, den Sie bereits geöffnet haben |

Die Deinstallation der App entfernt Sandbox- und App-Gruppendaten, die mit der App verbunden sind (abhängig vom Verhalten von iOS/macOS). Optionale iCloud-Kopien bleiben in **deiner** iCloud, bis du sie löschst oder die Synchronisierung ausschaltest und anderswo löschst.

## iCloud-Synchronisierung (optional)

Wenn du **iCloud-Synchronisierung** in den Einstellungen aktivierst, spiegelt die App ausgewählte Benutzerdaten über Apples **`NSUbiquitousKeyValueStore`**, die mit **deiner Apple-ID** verknüpft ist:

- Favoriten
- Listen (essay lists)
- Leseverlauf
- Lernfortschritt / Kenntnisse
- Übungsserien
- Notizen

Der Synchronisationsverkehr geht an **Apple iCloud**, nicht an iHTC Studio. Du kannst die Synchronisierung in den Einstellungen deaktivieren. Wir können deine iCloud-Inhalte nicht lesen.

## Berechtigungen

iLiezi fordert Berechtigungen nur an, wenn eine Funktion diese benötigt:

| Erlaubnis | Wann | Warum |
|------------|------|-----|
| Benachrichtigungen | Sie aktivieren Today’s Essay reminders | Lokale Planung of reminder notifications |
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

iGuanZhi ist eine Bildungs- und Lese-App für ein allgemeines Publikum und **nicht** in der Kids Category. Wir erheben wissentlich keine personenbezogenen Daten von Kindern. Die App erfordert kein Konto. Familien können Lese- und Lernfunktionen offline auf eigenen Geräten nutzen.

## Dritte Parteien

- **Apple** — App Store-Vertrieb, optionale StoreKit-Käufe, optionales iCloud-KVS, System-TTS, von Ihnen gewählte Share-Sheet-Ziele sowie Benachrichtigungen/Live-Aktivitäten/Siri/Kurzbefehle/Vision auf OS-Ebene.
- **Keine weiteren Drittanbieter-SDKs** für Werbung, Analysen oder Social-Login sind zur Datenerfassung enthalten.

## Internationale Nutzer

Die App ist darauf ausgelegt, offline auf Ihrem Gerät zu funktionieren. Optionale Apple-Dienste unterliegen den Bedingungen von Apple und der regionalen Verfügbarkeit.

## Datenaufbewahrung & Löschung

- **Auf dem Gerät** — Löschen Sie die App, um lokale Sandbox- und App-Gruppendaten zu entfernen (abhängig vom Verhalten des Betriebssystems).
- **iCloud** — Deaktivieren Sie die Synchronisierung und löschen Sie bei Bedarf zugehörige Schlüssel aus Ihrem iCloud-Konto / Ihren Geräten; wir können Ihr iCloud nicht für Sie löschen.
- **Wir speichern nichts** auf den iHTC Studio-Servern für diese App, da wir keine Daten sammeln.

## Richtlinienänderungen

Wir können diese Datenschutzerklärung aktualisieren. Das Datum „Zuletzt aktualisiert“ oben ändert sich. Fortgesetzte Nutzung nach einer Aktualisierung gilt als Zustimmung zur überarbeiteten Richtlinie. Wesentliche Änderungen können gegebenenfalls auch im App Store unter „Was ist neu“ vermerkt werden.

## Kontakt

Fragen zum Datenschutz: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="fr" markdown="1">

**Dernière mise à jour :** 5 septembre 2026

iHTC Studio (« nous ») a développé **iGuanZhi** (« 爱古文观止 / 愛古文觀止 », Bundle ID `com.iHTCboy.iGuanZhi`). Cette politique de confidentialité explique quelles données sont (ou ne sont pas) traitées lorsque vous utilisez l’app. **Apple App Review** et les utilisateurs peuvent s’appuyer sur **cette page** comme politique publique. Pour App Store Connect, ouvrez cette page dans le navigateur et copiez l’URL depuis la barre d’adresse (le domaine public peut changer).

## Résumé (alignement sur l'étiquette nutritionnelle de confidentialité Apple)

| Sujet | Notre pratique |
|-------|----------------|
| Compte | **Non requis** — pas d'inscription, de connexion par e-mail ou de numéro de téléphone |
| Collecte de données par iHTC Studio | **Données non collectées** — nous n'exploitons **pas** de backend qui reçoit vos données personnelles |
| Réseau | La bibliothèque, la lecture, la récitation, l'étude, la chasse, les widgets et les notifications quotidiennes fonctionnent **hors ligne** après l'installation |
| Analyses / publicités / suivi | **Aucun** — pas de SDK tiers d'analyse, de publicité ou de suivi ; pas d'utilisation de la transparence du suivi des applications |
| Services Apple facultatifs | **iCloud** (KVS privé), **Photothèque (ajout uniquement)** pour cartes 孟, **StoreKit** pour pourboire facultatif, **notifications locales**, **activités en direct** facultatives, **écriture manuscrite** sur l’appareil (Vision) facultative |

## Collecte de données

Nous ne collectons, vendons ou partageons **pas** d'informations personnelles à des fins publicitaires ou analytiques.

- **Aucun compte** — Vous pouvez utiliser toutes les fonctionnalités principales sans créer de compte chez nous.
- **Aucune analyse ni publicité** — Le binaire de l'application n'intègre pas de SDK tiers d'analyse, de publicité ou de rapport d'erreur qui nous contactent.
- **Aucun envoi de contenu** — historique, favoris, listes, notes, progression d’étude et préférences restent sur l’appareil (et, en option, dans **votre** iCloud). Ils ne sont jamais envoyés aux serveurs iHTC Studio car **nous n’exploitons pas de tels serveurs pour cette app**.

## Comment fonctionne l'application

- **Bibliothèque incluse** — JSON texte, vernaculaire/anglais, index et aides d’étude sont dans le bundle app/widget. Parcourir et étudier ne nécessite pas le réseau.
- **Discours sur l'appareil** — La récitation utilise le système **AVSpeechSynthesizer** (TTS) d'Apple. Nous n'envoyons pas de texte de passage à iHTC Studio.
- **Widgets et App Group** — Les widgets et l’app partagent des préférences et un état léger via l’App Group `group.com.iHTCboy.iGuanZhi` sur votre appareil.
- **Notifications quotidiennes** — Planifiées localement avec les notifications utilisateur. Appuyer sur une notification ouvre un lien profond vers un identifiant de passage sur l'appareil ; pas de distribution du serveur.
- **Cartes 古** — Les images sont générées sur l’appareil. L’enregistrement utilise **Photothèque (ajout uniquement)** seulement lorsque vous touchez Enregistrer. La feuille de partage peut envoyer l’image à une app **que vous choisissez** ; la politique de confidentialité de cette destination s’applique alors.
- **Recherche d'écriture manuscrite (iOS)** : la reconnaissance de caractères facultative utilise Apple **Vision** sur l'appareil. Les traits ne sont pas téléchargés.
- **Conseil facultatif** — « Tip Developer » est un achat de consommable **StoreKit** traité par Apple. Nous ne recevons pas les détails de votre carte de paiement.
- **Siri / Raccourcis / Centre de contrôle** — Les intégrations système facultatives ouvrent des liens profonds sur l'appareil ; ils ne nous envoient pas votre bibliothèque.
- **Spotlight facultatif** — Si vous activez l'indexation, le contenu est indexé par le système sur l'appareil pour la recherche locale ; nous n'exploitons pas de backend de recherche.

## Données stockées sur votre appareil

| Données | Où | Objectif |
|------|-------|--------------|
| Base Guwen Guanzhi | Bundle App / Widget | Lecture et étude hors ligne |
| Favoris (essay lists) | UserDefaults de l’App Group | Passages favoris et listes |
| Historique de lecture / dernière lecture | Paramètres par défaut du groupe d'applications | Continuer la lecture, historique de l'interface utilisateur |
| Remarques | Paramètres par défaut du groupe d'applications | Notes de lecture que vous écrivez |
| Avancement et maîtrise des études | Paramètres par défaut du groupe d'applications | Etat de la classe, quiz / Progression de la chasse |
| Séquence d'entraînement / enregistrement | Paramètres par défaut du groupe d'applications | Habitude quotidienne |
| Préférences des cartes de partage | UserDefaults de l'App Group | Derniers choix de style / de format |
| Today’s Essay cache & notification prefs | UserDefaults de l’App Group | ID du jour, schedule time, contextual toggle |
| Préférences de cartes | UserDefaults de l’App Group | Dernier style/ratio |
| État d’intégration et de TipKit | Paramètres utilisateur standard (appareil) | Guide d'accueil / conseils découverte |
| Recherches récentes | Standard UserDefaults (device) | Historique saisi |
| Actions rapides sur l'écran d'accueil | Système + préférences locales | Raccourcis que vous configurez |
| Widget / Instantanés d'activité en direct | Groupe d'applications / ActivityKit | Afficher le texte que vous avez déjà ouvert |

La désinstallation de l'application supprime les données du bac à sable et du groupe d'applications associées à l'application (selon le comportement d'iOS/macOS). Les copies facultatives dans iCloud restent dans **votre** iCloud jusqu'à ce que vous les supprimiez ou que vous désactiviez la synchronisation et supprimiez ailleurs.

## Synchronisation iCloud (Facultative)

Si vous activez **la synchronisation iCloud** dans les Réglages, l'application reflète les données utilisateur sélectionnées via le **`NSUbiquitousKeyValueStore`** d'Apple lié à **votre identifiant Apple** :

- Favoris
- Listes (essay lists)
- Historique de lecture
- Progression / maîtrise des études
- Séries de pratique
- Remarques

Le trafic de synchronisation passe par **Apple iCloud**, et non par iHTC Studio. Vous pouvez désactiver la synchronisation dans les Réglages. Nous ne pouvons pas lire le contenu de votre iCloud.

## Autorisations

iLiezi demande des autorisations uniquement lorsqu'une fonctionnalité en a besoin :

| Autorisation | Quand | Pourquoi |
|------------|------|-----|
| Notifications | Vous activez Today’s Essay reminders | Planification locale of reminder notifications |
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

iGuanZhi est une application éducative de lecture pour le grand public et **n’est pas** dans la Kids Category. Nous ne collectons pas sciemment d’informations personnelles auprès d’enfants. L’app ne nécessite pas de compte. Les familles peuvent utiliser lecture et étude hors ligne sur leurs propres appareils.

## Tiers

- **Apple** — Distribution App Store, achats StoreKit facultatifs, KVS iCloud facultatif, TTS système, destinations de partage que vous choisissez, et notifications/activités en direct/Siri/raccourcis/Vision au niveau du système.
- **Aucun autre SDK tiers** pour la publicité, l'analyse ou la connexion sociale n'est inclus pour la collecte de données.

## Utilisateurs internationaux

L'application est conçue pour fonctionner hors ligne sur votre appareil. Les services Apple optionnels suivent les conditions et la disponibilité régionale d'Apple.

## Conservation et suppression des données

- **Sur l'appareil** — Supprimez l'application pour retirer les données locales du bac à sable et du groupe d'applications (sous réserve du comportement du système d'exploitation).
- **iCloud** — Désactivez la synchronisation et effacez les clés associées de votre compte iCloud / appareils si nécessaire ; nous ne pouvons pas effacer votre iCloud à votre place.
- **Nous ne conservons rien** sur les serveurs iHTC Studio pour cette application car nous ne collectons pas ces données.

## Modifications de la politique

Nous pouvons mettre à jour cette politique de confidentialité. La date « Dernière mise à jour » en haut changera. L’utilisation continue après une mise à jour vaut acceptation de la politique révisée. Les changements importants peuvent aussi figurer dans « Nouveautés » de l’App Store le cas échéant.

## Nous contacter

Questions sur la vie privée : [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="tr" markdown="1">

**Son güncelleme:** 5 Eylül 2026

iHTC Studio ("biz"), **iGuanZhi** ("爱古文观止 / 愛古文觀止", Bundle ID `com.iHTCboy.iGuanZhi`) uygulamasını geliştirdi. Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlendiğini (ve işlenmediğini) açıklar. **Apple App Review** ve kullanıcılar **bu sayfayı** herkese açık gizlilik politikası olarak kullanabilir. App Store Connect için tarayıcıda bu sayfayı açın ve adres çubuğundan URL’yi kopyalayın (genel site alan adı zamanla değişebilir).

## Özet (Apple Gizlilik Beslenme Etiketi uyumu)

| Konu | Uygulamamızın uygulaması |
|-------|----------------|
| Hesap | **Gerekli değil** — kayıt, e-posta ile giriş veya telefon numarası yok |
| iHTC Studio tarafından veri toplama | **Veri Toplanmıyor** — kişisel verilerinizi alan bir arka uç işletmiyoruz |
| Ağ | Kütüphane, okuma, ezberleme, çalışma, avlanma, widgetlar ve günlük bildirimler kurulumdan sonra **çevrimdışı** çalışır |
| Analitik / reklam / izleme | **Yok** — üçüncü taraf analitik, reklam veya izleme SDK'ları yok; Uygulama İzleme Şeffaflığı kullanılmaz |
| İsteğe bağlı Apple hizmetleri | **iCloud** (özel KVS), 孟 kartları için **Fotoğraf Kitaplığı (yalnızca ekleme)**, isteğe bağlı **StoreKit** bahşiş, **yerel bildirimler**, isteğe bağlı **Canlı Etkinlikler**, isteğe bağlı cihaz içi **el yazısı** (Vision) |

## Veri Toplama

Kişisel bilgileri reklam veya analiz için **toplamıyoruz**, satmıyoruz veya paylaşmıyoruz.

- **Hesap gerekmez** — Tüm temel özellikleri bizde hesap oluşturmadan kullanabilirsiniz.
- **Analitik veya reklam yok** — Uygulama ikili dosyası üçüncü taraf analitik, reklam veya çökme bildirim SDK'larını içermez, telefonla bize veri göndermez.
- **İçerik yüklenmez** — Okuma geçmişi, favoriler, listeler, notlar, çalışma ilerlemesi ve tercihler cihazınızda (ve isteğe bağlı **iCloud’unuzda**) kalır. **Bu uygulama için böyle sunucular işletmediğimizden** iHTC Studio sunucularına yüklenmez.

## Uygulama Nasıl Çalışır

- **Paketlenmiş kitaplık** — Metin JSON, vernacular/English, dizinler ve çalışma yardımcıları uygulama/widget paketinin içindedir. Gezinme ve çalışma için ağ gerekmez.
- **Cihaz içi konuşma** — Okuma, Apple'ın **AVSpeechSynthesizer** (TTS) sistemini kullanır. iHTC Studio'ya pasaj metni göndermiyoruz.
- **Widget'lar ve App Group** — Widget'lar ve uygulama, cihazınızdaki `group.com.iHTCboy.iGuanZhi` App Group'u üzerinden tercihleri ve hafif durumu paylaşır.
- **Günlük bildirimler** — Kullanıcı Bildirimleriyle yerel olarak planlanır. Bir bildirime dokunulduğunda cihazdaki pasaj kimliğine giden derin bağlantı açılır; sunucu çıkışı yok.
- **古 kartları** — Görseller cihazda oluşturulur. Kaydetme yalnızca kaydet’e dokunduğunuzda **Fotoğraf Kitaplığı (yalnızca ekleme)** kullanır. Paylaşım Sayfası görseli **sizin seçtiğiniz** bir uygulamaya gönderebilir; o hedefin gizlilik politikası geçerli olur.
- **El yazısı araması (iOS)** — İsteğe bağlı karakter tanıma, cihazda Apple **Vision**'ı kullanır. Konturlar yüklenmedi.
- **İsteğe bağlı ipucu** — "İpucu Geliştirici", Apple tarafından gerçekleştirilen bir **StoreKit** sarf malzemesidir. Ödeme kartı bilgilerinizi almıyoruz.
- **Siri / Kısayollar / Kontrol Merkezi** — İsteğe bağlı sistem entegrasyonları cihazdaki derin bağlantıları açar; kütüphanenizi bize göndermiyorlar.
- **İsteğe Bağlı Spotlight** — Dizin oluşturmayı etkinleştirirseniz içerik, yerel arama için cihazdaki sistem tarafından dizine eklenir; bir arama arka ucu kullanmıyoruz.

## Cihazınızda Saklanan Veriler

| Veri | Nerede | Amaç |
|------|-------|-------------|
| Guwen Guanzhi veritabanı | App / Widget paketi | Çevrimdışı okuma ve çalışma |
| Favoriler (essay lists) | App Group UserDefaults | Yıldızlı pasajlar ve listeler |
| Okuma geçmişi / son okuma | Uygulama Grubu Kullanıcı Varsayılanları | Okumaya devam et, geçmiş kullanıcı arayüzü |
| Notlar | Uygulama Grubu Kullanıcı Varsayılanları | Yazdığınız notları okuma |
| Çalışma ilerlemesi ve ustalık | Uygulama Grubu Kullanıcı Varsayılanları | Sınıf durumu, sınav / Arama ilerlemesi |
| Antrenman serisi / check-in | Uygulama Grubu Kullanıcı Varsayılanları | Günlük alışkanlık |
| Paylaşım kartı tercihleri | App Group UserDefaults | Son stil / oran seçimleri |
| Today’s Essay cache & notification prefs | App Group UserDefaults | Bugünün ID’si, schedule time, contextual toggle |
| Kart tercihleri | App Group UserDefaults | Son stil/oran |
| İlk katılım ve TipKit durumu | Standart Kullanıcı Varsayılanları (cihaz) | Hoş geldiniz kılavuzu / keşif ipuçları |
| Son aramalar | Standard UserDefaults (device) | Yazdığınız arama geçmişi |
| Ana Ekran hızlı eylemler | Sistem + yerel tercihler | Yapılandırdığınız kısayollar |
| Widget / Canlı Etkinlik anlık görüntüleri | Uygulama Grubu / ActivityKit | Daha önce açmış olduğunuz metni görüntüleyin |

Uygulamayı kaldırmak, uygulamayla ilişkili sandbox ve Uygulama Grubu verilerini kaldırır (iOS/macOS davranışına tabidir). İsteğe bağlı iCloud kopyaları, siz temizleyene veya senkronizasyonu kapatıp başka yerde silene kadar **iCloud’unuzda** kalır.

## iCloud Senkronizasyonu (İsteğe Bağlı)

Eğer Ayarlar’dan **iCloud Senkronizasyonu**’nu etkinleştirirseniz, uygulama seçili kullanıcı verilerini Apple’ın **`NSUbiquitousKeyValueStore`** aracılığıyla **Apple Kimliğinizle** eşler:

- Favoriler
- Listeler (essay lists)
- Okuma geçmişi
- Çalışma ilerlemesi / ustalık
- Pratik serileri
- Notlar

Senkronizasyon trafiği **Apple iCloud**’a gider, iHTC Studio’ya değil. Ayarlardan senkronizasyonu devre dışı bırakabilirsiniz. iCloud içeriğinizi okuyamayız.

## İzinler

iLiezi yalnızca bir özellik ihtiyaç duyduğunda izin ister:

| İzin | Ne zaman | neden |
|------------|------|-----|
| Bildirimler | Today’s Essay reminders etkinleştirirsiniz | Yerel zamanlama of reminder notifications |
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

iGuanZhi, genel kitleye yönelik bir eğitim/okuma uygulamasıdır ve **Kids Category**’de değildir. Çocuklardan bilerek kişisel bilgi toplamayız. Uygulama hesap gerektirmez. Aileler kendi cihazlarında okuma ve çalışma özelliklerini çevrimdışı kullanabilir.

## Üçüncü Taraflar

- **Apple** — App Store dağıtımı, isteğe bağlı StoreKit satın alımları, isteğe bağlı iCloud KVS, sistem TTS, seçtiğiniz Paylaşım Sayfası hedefleri ve işletim sistemi düzeyinde bildirim/Canlı Etkinlik/Siri/Kestirmeler/Vision.
- Reklam, analiz veya sosyal giriş için başka hiçbir üçüncü taraf SDK’sı veri toplama amacıyla dahil edilmemiştir.

## Uluslararası Kullanıcılar

Uygulama, cihazınızda çevrimdışı çalışacak şekilde tasarlanmıştır. İsteğe bağlı Apple hizmetleri Apple’ın şartlarına ve bölgesel kullanılabilirliğe tabidir.

## Veri Saklama ve Silme

- **Cihazda** — Yerel sandbox ve App Group verilerini kaldırmak için uygulamayı silin (işletim sistemi davranışına bağlıdır).
- **iCloud** — Senkronizasyonu kapatın ve gerektiğinde iCloud hesabınızdan / cihazlarınızdan ilgili anahtarları temizleyin; iCloud’unuzu sizin adınıza silemeyiz.
- **Hiçbir şeyi** iHTC Studio sunucularında bu uygulama için saklamıyoruz çünkü bunu toplamıyoruz.

## Politika Değişiklikleri

Bu Gizlilik Politikasını güncelleyebiliriz. Üstteki 「Son güncelleme」 tarihi değişir. Güncellemeden sonra kullanıma devam etmek, revize edilmiş politikayı kabul ettiğiniz anlamına gelir. Önemli değişiklikler uygun olduğunda App Store 「Yenilikler」 metninde de belirtilebilir.

## İletişim

Gizlilik ile ilgili sorular: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
