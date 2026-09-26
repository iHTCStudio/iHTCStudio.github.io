---
layout: doc
title: iZiSi — Privacy Policy
app_id: iZiSi
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iZiSi — offline Zisi workshop, Data Not Collected, watchfulness notes stay on device.
---

<section lang="en" markdown="1">

**Last updated:** September 19, 2026

iHTC Studio ("we", "us" or "our"; formerly iHTCTeam) built **iZiSi** (also known as "爱子思 / 愛子思", Bundle ID `com.iHTCboy.iZiSi`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on **this page** as the public privacy policy. For App Store Connect, open this Privacy Policy in your browser and copy the address from the address bar (the public site domain may change over time).

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration, email sign-in, or phone number |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your personal data |
| Network | Library, reading, recite, Zisi Study, widgets, and daily notifications work **offline** after install |
| Analytics / ads / tracking | **None** — no third-party analytics, advertising, or tracking SDKs; no App Tracking Transparency use |
| Optional Apple services | **iCloud** (your private KVS), **Photo Library (Add Only)** for study cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional on-device **handwriting** (Vision) |

## Data Collection

We do **not** collect, sell, or share personal information for advertising or analytics.

- **No account** — You can use all core features without creating an account with us.
- **No analytics or ads** — The app binary does not integrate third-party analytics, advertising, or crash-reporting SDKs that phone home to us.
- **No content upload** — Your reading history, favorites, lists, notes, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

**Watchfulness studio** is an inner reading ritual (stillness timer, notes on the unissued and the issued). It is **not** a meditation-tracker product and **not** a camera on other people. The Guodian Five Conducts gallery is an academic parallel with *Zhongyong*, **not** fortune-telling.

## How the App Works

- **Bundled library** — Text JSON, vernacular/English, indexes, and study aids ship inside the app / widget bundle.
- **On-device speech** — Recitation uses Apple’s system **AVSpeechSynthesizer** (TTS). We do not send passage text to iHTC Studio.
- **Widgets & App Group** — Widgets and the app share preferences via App Group `group.com.iHTCboy.iZiSi` on your device.
- **Daily notifications** — Scheduled locally. Tapping a notification opens a deep link on device.
- **Study cards** — Images are rendered on device. Saving uses **Photo Library add-only** only when you tap save.
- **Handwriting search (iOS)** — Optional character recognition uses Apple **Vision** on device. Strokes are not uploaded.
- **Optional tip** — “Tip Developer” is a consumable **StoreKit** purchase processed by Apple.
- **Siri / Shortcuts / Control Center** — Optional system integrations open on-device deep links.
- **Optional Spotlight** — If you enable indexing, the system indexes content on device.

## Data Stored on Your Device

| Data | Where | Purpose |
|------|-------|---------|
| Zisi-line library | App / Widget bundle | Offline reading & study |
| Favorites & lists | App Group UserDefaults | Starred items and user lists |
| Reading history / last read | App Group UserDefaults | Continue reading |
| Notes | App Group UserDefaults | Reading notes you write |
| Study progress & mastery | App Group UserDefaults | Classroom / Hunt progress |
| Streak / check-in | App Group UserDefaults | Daily habit |
| Appearance & reading prefs | App Group UserDefaults | Theme, language, TTS, widgets |
| Today’s Thought cache & notification prefs | App Group UserDefaults | Today’s ID and schedule |
| Card preferences | App Group UserDefaults | Last style / ratio |
| Onboarding & TipKit state | Standard UserDefaults | Welcome guide |
| Widget / Live Activity snapshots | App Group / ActivityKit | Display text you already opened |

Uninstalling the app removes sandbox and App Group data (subject to OS behavior). Optional iCloud copies remain in **your** iCloud until you clear them.

## iCloud Sync (Optional)

If you enable **iCloud Sync** in Settings, the app mirrors selected user data through Apple’s **`NSUbiquitousKeyValueStore`** tied to **your Apple ID**:

- Favorites
- Lists
- Reading history
- Study progress / mastery
- Practice streaks
- Notes
- Watchfulness reflections
- Five-steps completion marks

Sync traffic goes to **Apple iCloud**, not to iHTC Studio. We cannot read your iCloud contents.

## Permissions

iZiSi requests permissions only when a feature needs them:

| Permission | When | Why |
|------------|------|-----|
| Notifications | You enable Today’s Thought reminders | Local scheduling |
| Photo Library (Add Only) | You save a card | Write the rendered image |
| iCloud | You enable sync | Sync favorites / lists / history / progress / notes |
| Live Activities (iOS) | You enable Reading Live Activity | Show the passage on Lock Screen / Dynamic Island |
| Background audio (capability) | You enable background recitation | Continue TTS in background |

We do **not** request Contacts, precise Location, Camera, Microphone (beyond system TTS playback), or Tracking.

## What We Do Not Do

- We do **not** sell personal data.
- We do **not** build advertising profiles.
- We do **not** require an account or social login.
- We do **not** embed third-party ad, analytics, or social SDKs for data collection.
- We do **not** access your Photo Library beyond **add-only** when you choose to save a card.
- We do **not** receive StoreKit payment card numbers (Apple processes payments).

## Children’s Privacy

iZiSi is an educational literacy app for a general audience and is **not** in the Kids Category. We do not knowingly collect personal information from children. Families may use reading and study features offline on their own devices.

## Third Parties

- **Apple** — App Store distribution, optional StoreKit, optional iCloud KVS, system TTS, Share Sheet destinations you pick, and OS-level notification / Live Activity / Siri / Shortcuts / Vision delivery.
- **No other third-party SDKs** for ads, analytics, or social login are included for data collection.

## International Users

The app is designed to function offline on your device. Optional Apple services follow Apple’s terms and regional availability.

## Data Retention & Deletion

- **On device** — Delete the app to remove local sandbox and App Group data (subject to OS behavior).
- **iCloud** — Turn off sync and clear related keys from your iCloud account as needed; we cannot erase your iCloud for you.
- **We retain nothing** on iHTC Studio servers for this app because we do not collect it.

## Policy Changes

We may update this Privacy Policy. The “Last updated” date at the top will change. Continued use after an update means you accept the revised policy.

## Contact

Questions about privacy: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>

<section lang="zh-CN" markdown="1">

**最近更新：** 2026 年 9 月 19 日

爱火腿肠工作室（iHTC Studio）（「我们」；原 iHTCTeam）开发了 **爱子思**（iZiSi / 愛子思，Bundle ID `com.iHTCboy.iZiSi`）。本隐私政策说明你在使用本应用时，数据如何被处理。本页可作为 **App Store 审核**与用户查阅的公开隐私政策。填写 App Store Connect 时：打开本站[隐私政策](privacy)页，从浏览器地址栏复制当前网址（站点域名日后可能变更，请勿依赖写死的完整域名）。

## 摘要（对齐 Apple 隐私标签）

| 主题 | 我们的做法 |
|------|------------|
| 账号 | **不需要** — 无注册、邮箱登录或手机号 |
| iHTC Studio 数据采集 | **Data Not Collected** — 我们**不**运营接收你个人数据的后端 |
| 网络 | 语料、品读、诵读、子思学堂、小组件与每日通知安装后均可**离线** |
| 分析 / 广告 / 追踪 | **无** — 无第三方分析、广告或追踪 SDK；不使用 ATT |
| 可选 Apple 服务 | **iCloud**（你的私人 KVS）、保存研读卡时的**照片图库（仅添加）**、可选 **StoreKit** 打赏、**本地通知**、可选**实时活动**、可选本机**手写识别** |

## 数据采集

我们**不**收集、出售或共享用于广告或分析的个人信息。

- **无账号** — 核心功能无需向我们注册。
- **无分析或广告** — 应用未集成会向我们回传的第三方分析、广告或崩溃 SDK。
- **无内容上传** — 阅读历史、收藏、清单、笔记、学习进度与偏好留在本机（并可选手动同步到**你的** iCloud）。

**慎独工坊**是内省功课（静心倒计时、未发 / 已发笔记）。它**不是**冥想打卡产品，也**不是**去监视别人。郭店《五行》馆是与《中庸》的学术对读，**不是**算命。

## 应用如何工作

- **内置语料** — 正文 JSON、白话／英译、索引与学习辅助随 App／小组件打包。
- **本机语音** — 诵读使用系统 **AVSpeechSynthesizer**。我们不会把正文发送到 iHTC Studio。
- **小组件与 App Group** — 通过本机 App Group `group.com.iHTCboy.iZiSi` 共享偏好。
- **每日通知** — 本地调度；点按后经深链打开本机篇目。
- **研读卡** — 在设备上渲染。仅在你点保存时使用**照片图库（仅添加）**。
- **手写寻句（iOS）** — 使用本机 Apple **Vision**。笔迹不会上传。
- **可选打赏** — Apple 处理的消耗型 **StoreKit** 购买。
- **Siri／快捷指令／控制中心** — 打开本机深链。
- **可选 Spotlight** — 由系统在本机索引。

## 本机存储的数据

| 数据 | 位置 | 用途 |
|------|------|------|
| 子思一线语料 | App／小组件 Bundle | 离线阅读与学习 |
| 收藏与清单 | App Group UserDefaults | 星标与用户清单 |
| 阅读历史／上次阅读 | App Group UserDefaults | 继续阅读 |
| 笔记 | App Group UserDefaults | 你写下的笔记 |
| 学习进度与掌握度 | App Group UserDefaults | 学堂／寻句进度 |
| 打卡／连续天数 | App Group UserDefaults | 每日习惯 |
| 外观与阅读偏好 | App Group UserDefaults | 主题、语言、TTS、小组件 |
| 今日一思缓存与通知偏好 | App Group UserDefaults | 今日 ID 与提醒 |
| 分享卡偏好 | App Group UserDefaults | 上次风格／比例 |
| 引导与 TipKit 状态 | 标准 UserDefaults | 欢迎引导 |
| 小组件／实时活动快照 | App Group／ActivityKit | 展示已打开的文本 |

卸载应用会移除沙盒与相关 App Group 数据（取决于系统）。可选 iCloud 副本仍留在**你的** iCloud。

## iCloud 同步（可选）

若在设置中开启 **iCloud 同步**，应用通过绑定**你的 Apple ID** 的 **`NSUbiquitousKeyValueStore`** 镜像：

- 收藏
- 清单
- 阅读历史
- 学习进度／掌握度
- 打卡
- 笔记
- 慎独反思
- 为学五步完成记录

同步流量前往 **Apple iCloud**，而非 iHTC Studio。我们无法读取你的 iCloud 内容。

## 权限

仅在功能需要时请求：

| 权限 | 时机 | 原因 |
|------|------|------|
| 通知 | 你开启今日一思提醒 | 本地调度 |
| 照片图库（仅添加） | 你保存分享卡 | 写入渲染图片 |
| iCloud | 你开启同步 | 同步收藏／清单／历史／进度／笔记 |
| 实时活动（iOS） | 你开启阅读实时活动 | 在锁定屏幕／灵动岛显示篇目 |
| 后台音频（能力） | 你开启后台诵读 | 后台继续 TTS |


我们**不**请求通讯录、精确位置、相机、麦克风（系统 TTS 除外）或追踪。

## 我们不会做的事

- **不**出售个人数据。
- **不**建立广告画像。
- **不**要求账号或社交登录。
- **不**嵌入用于数据收集的第三方广告、分析或社交 SDK。
- **不**在你主动保存分享卡之外访问相册。
- **不**接收 StoreKit 银行卡号。

## 儿童隐私

爱子思是面向一般读者的教育类语文应用，**不属于** Kids Category。我们不会故意收集儿童个人信息。家庭可在自有设备上离线使用阅读与学习功能。

## 第三方

- **Apple** — App Store 分发、可选 StoreKit、可选 iCloud、系统 TTS、你选择的分享目标，以及系统通知／实时活动／Siri／快捷指令／Vision。
- **无其他**用于广告、分析或社交登录的第三方数据收集 SDK。

## 国际用户

应用设计为在你的设备上离线运行。可选 Apple 服务遵循 Apple 条款与地区可用性。

## 数据保留与删除

- **本机** — 删除应用以移除沙盒与 App Group 数据（取决于系统）。
- **iCloud** — 关闭同步并按需清理你的 iCloud；我们无法代你删除。
- **iHTC Studio** — 本应用不在自有服务器收集个人数据。

## 政策变更

我们可能更新本政策。页首「最近更新」日期会随之变化。

## 联系

隐私疑问：[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>

<section lang="zh-TW" markdown="1">

**最近更新：** 2026 年 9 月 19 日

愛火腿腸工作室（iHTC Studio）（「我們」；原 iHTCTeam）開發了 **愛子思**（iZiSi / 爱子思，Bundle ID `com.iHTCboy.iZiSi`）。本隱私政策說明你在使用本應用時，資料如何被處理。本頁可作為 **App Store 審核**與使用者查閱的公開隱私政策。填寫 App Store Connect 時：打開本站[隱私政策](privacy)頁，從瀏覽器網址列複製目前網址（網站網域日後可能變更，請勿依賴寫死的完整網域）。

## 摘要（對齊 Apple 隱私標籤）

| 主題 | 我們的做法 |
|------|------------|
| 帳號 | **不需要** — 無註冊、電子郵件登入或手機號碼 |
| iHTC Studio 資料蒐集 | **Data Not Collected** — 我們**不**營運接收你個人資料的後端 |
| 網路 | 語料、品讀、誦讀、子思學堂、小工具與每日通知安裝後均可**離線** |
| 分析 / 廣告 / 追蹤 | **無** — 無第三方分析、廣告或追蹤 SDK；不使用 ATT |
| 可選 Apple 服務 | **iCloud**（你的私人 KVS）、儲存研讀卡時的**照片（僅加入）**、可選 **StoreKit** 打賞、**本機通知**、可選**即時動態**、可選本機**手寫辨識** |

## 資料蒐集

我們**不**蒐集、出售或共享用於廣告或分析的個人資訊。

- **無帳號** — 核心功能無需向我們註冊。
- **無分析或廣告** — 應用未整合會向我們回傳的第三方分析、廣告或當機 SDK。
- **無內容上傳** — 閱讀歷史、收藏、清單、筆記、學習進度與偏好留在本機（並可選手動同步到**你的** iCloud）。

**慎獨工坊**是內省功課（靜心倒數、未發 / 已發筆記）。它**不是**冥想打卡產品，也**不是**去監視別人。郭店《五行》館是與《中庸》的學術對讀，**不是**算命。

## 應用如何工作

- **內建語料** — 正文 JSON、白話／英譯、索引與學習輔助隨 App／小工具打包。
- **本機語音** — 誦讀使用系統 **AVSpeechSynthesizer**。我們不會把正文傳送到 iHTC Studio。
- **小工具與 App Group** — 透過本機 App Group `group.com.iHTCboy.iZiSi` 共享偏好。
- **每日通知** — 本機排程；點按後經深鏈打開本機篇目。
- **研讀卡** — 在裝置上渲染。僅在你點儲存時使用**照片（僅加入）**。
- **手寫尋句（iOS）** — 使用本機 Apple **Vision**。筆跡不會上傳。
- **可選打賞** — Apple 處理的消耗型 **StoreKit** 購買。
- **Siri／捷徑／控制中心** — 打開本機深鏈。
- **可選 Spotlight** — 由系統在本機建立索引。

## 本機儲存的資料

| 資料 | 位置 | 用途 |
|------|------|------|
| 子思一線語料 | App／小工具 Bundle | 離線閱讀與學習 |
| 收藏與清單 | App Group UserDefaults | 星號與使用者清單 |
| 閱讀歷史／上次閱讀 | App Group UserDefaults | 繼續閱讀 |
| 筆記 | App Group UserDefaults | 你寫下的筆記 |
| 學習進度與掌握度 | App Group UserDefaults | 學堂／尋句進度 |
| 打卡／連續天數 | App Group UserDefaults | 每日習慣 |
| 外觀與閱讀偏好 | App Group UserDefaults | 主題、語言、TTS、小工具 |
| 今日一思快取與通知偏好 | App Group UserDefaults | 今日 ID 與提醒 |
| 分享卡偏好 | App Group UserDefaults | 上次風格／比例 |
| 引導與 TipKit 狀態 | 標準 UserDefaults | 歡迎引導 |
| 小工具／即時動態快照 | App Group／ActivityKit | 展示已打開的文本 |

解除安裝應用會移除沙盒與相關 App Group 資料（取決於系統）。可選 iCloud 副本仍留在**你的** iCloud。

## iCloud 同步（可選）

若在設定中開啟 **iCloud 同步**，應用透過綁定**你的 Apple ID** 的 **`NSUbiquitousKeyValueStore`** 鏡像：

- 收藏
- 清單
- 閱讀歷史
- 學習進度／掌握度
- 打卡
- 筆記
- 慎獨反思
- 為學五步完成紀錄

同步流量前往 **Apple iCloud**，而非 iHTC Studio。我們無法讀取你的 iCloud 內容。

## 權限

僅在功能需要時請求：

| 權限 | 時機 | 原因 |
|------|------|------|
| 通知 | 你開啟今日一思提醒 | 本機排程 |
| 照片（僅加入） | 你儲存分享卡 | 寫入渲染圖片 |
| iCloud | 你開啟同步 | 同步收藏／清單／歷史／進度／筆記 |
| 即時動態（iOS） | 你開啟閱讀即時動態 | 在鎖定畫面／動態島顯示篇目 |
| 背景音訊（能力） | 你開啟背景誦讀 | 背景繼續 TTS |


我們**不**請求通訊錄、精確位置、相機、麥克風（系統 TTS 除外）或追蹤。

## 我們不會做的事

- **不**出售個人資料。
- **不**建立廣告畫像。
- **不**要求帳號或社交登入。
- **不**嵌入用於資料蒐集的第三方廣告、分析或社交 SDK。
- **不**在你主動儲存分享卡之外存取照片。
- **不**接收 StoreKit 銀行卡號。

## 兒童隱私

愛子思是面向一般讀者的教育類語文應用，**不屬於** Kids Category。我們不會故意蒐集兒童個人資訊。家庭可在自有裝置上離線使用閱讀與學習功能。

## 第三方

- **Apple** — App Store 分發、可選 StoreKit、可選 iCloud、系統 TTS、你選擇的分享目標，以及系統通知／即時動態／Siri／捷徑／Vision。
- **無其他**用於廣告、分析或社交登入的第三方資料蒐集 SDK。

## 國際使用者

應用設計為在你的裝置上離線運行。可選 Apple 服務遵循 Apple 條款與地區可用性。

## 資料保留與刪除

- **本機** — 刪除應用以移除沙盒與 App Group 資料（取決於系統）。
- **iCloud** — 關閉同步並按需清理你的 iCloud；我們無法代你刪除。
- **iHTC Studio** — 本應用不在自有伺服器蒐集個人資料。

## 政策變更

我們可能更新本政策。頁首「最近更新」日期會隨之變化。

## 聯絡

隱私疑問：[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
