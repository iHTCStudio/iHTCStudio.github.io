---
layout: doc
title: iMusic — Privacy Policy
app_id: iMusic
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iMusic (爱音乐) — curated listening guides offline, Apple Music playback and song ID by authorization, Data Not Collected, optional iCloud.
---

<section lang="en" markdown="1">

**Last updated:** September 9, 2026

iHTC Studio ("we", "us" or "our"; formerly iHTCTeam) built **iMusic** (also known as "爱音乐" / "愛音樂", Bundle ID `com.iHTCboy.iMusic`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on **this page** as the public privacy policy for the app. For App Store Connect, open this Privacy Policy in your browser and copy the address from the address bar (the public site domain may change over time).

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration, email sign-in, or phone number |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your personal data |
| Network | Listening **guides** work **offline** after install. **Playback** and **song ID** use Apple services after you authorize them |
| Analytics / ads / tracking | **None** — no third-party analytics, advertising, or tracking SDKs; no App Tracking Transparency use |
| Optional Apple services | **Apple Music / MusicKit**, **ShazamKit**, **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities** |

## Data Collection

We do **not** collect, sell, or share personal information for advertising or analytics.

- **No account** — You can browse every bundled guide without creating an account with us.
- **No analytics or ads** — The app binary does not integrate third-party analytics, advertising, or crash-reporting SDKs that phone home to us.
- **No guide upload** — Favorites, listen lists, later, notes, history, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.
- **No song hosting** — We do not ship full audio. Matched playback is delivered by **Apple Music**. We cache at most a **30-second catalog preview** on device when you are not subscribed.

## How the App Works

- **Bundled library** — Piece indexes, guides, artist notes, categories, collections, famous lines, and the daily calendar ship inside the app / widget bundle. Browsing guides does not require a network request.
- **Apple Music (MusicKit)** — When you play a piece and grant access, the app matches the curated catalog (ISRC first, then artist + title) and plays through Apple’s player. Subscription status is queried from Apple; a timeout is treated as **unknown**, not as “unsubscribed.” Artwork URLs may be fetched to show covers. We do not receive your Apple ID or payment details.
- **30-second previews** — If you are not subscribed, Apple’s preview may be stored under `Caches` on your device (LRU; not a full track). Cellular / Low Power / Low Data modes do not prefetch the next preview. Settings can clear artwork and preview caches separately without touching favorites or listen lists.
- **Song ID (ShazamKit)** — Used only when you open Recognize. Microphone audio is processed by **Apple’s** recognition; we do not keep a recording archive. A catalog hit opens the on-device guide.
- **On-device speech** — Reading a guide aloud uses Apple’s **AVSpeechSynthesizer**. We do not send guide text to iHTC Studio.
- **Widgets & App Group** — The app and widgets share preferences via App Group `group.com.iHTCboy.iMusic` on your device. Live Activity artwork is a small JPEG in that group plus a token — not the full image inside the activity payload.
- **Daily notifications** — Scheduled locally. Tapping opens a deep link to a piece ID on device.
- **Share cards** — Rendered on device. Saving uses **Photo Library add-only** only when you tap save.
- **Optional tip** — Consumable **StoreKit** purchase processed by Apple.
- **Optional Spotlight** — **Off by default.** If you enable it, indexes are submitted to the system on device.

## Data Stored on Your Device

| Data | Where | Purpose |
|------|-------|---------|
| Guide library (indexes + shards) | App / Widget bundle | Offline reading |
| Favorites, listen lists, later | App Group UserDefaults | Your lists |
| Notes, history, recitation progress | App Group UserDefaults | Continue listening / reading |
| Streak / check-in | App Group UserDefaults | Daily habit |
| Appearance, language, speech, tabs | App Group UserDefaults | Settings |
| Daily Piece cache & notification prefs | App Group UserDefaults | Today’s ID and schedule |
| Share-card preferences | App Group UserDefaults | Last style / canvas |
| Artwork URL map & decoded covers | App Group + memory / disk cache | Show covers; silent prefetch only after MusicKit is authorized |
| 30-second preview files | App Caches | Play previews offline after first hit |
| Live Activity thumbnail | App Group JPEG + token | Lock Screen / Dynamic Island while **reading** a guide |
| MusicKit / Shazam authorization | System | Remember your choice |
| Onboarding & rating prompts | Device UserDefaults | Welcome / review |

Uninstalling removes sandbox and App Group data (subject to iOS/macOS). Optional iCloud copies remain in **your** iCloud until you clear them. Apple Music library and subscriptions stay with Apple.

## iCloud Sync (Optional)

If you enable **iCloud Sync** in Settings, the app mirrors selected user data through Apple’s **`NSUbiquitousKeyValueStore`** tied to **your Apple ID**:

- Favorites
- Listen lists
- Later
- Notes
- Listening / reading history
- Recitation progress
- Streaks

Guides themselves already ship in the app. Artwork files and preview audio are **not** synced through KVS. Sync traffic goes to **Apple iCloud**, not to iHTC Studio. You can disable sync in Settings. We cannot read your iCloud contents.

## Permissions

iMusic requests permissions only when a feature needs them:

| Permission | When | Why |
|------------|------|-----|
| **Apple Music / Media Library** | You continue on the Music explanation, or you tap play | Match and play catalog tracks; load artwork |
| **Microphone** | You open Song ID | Recognize music playing around you |
| **Notifications** | You enable Daily Piece reminders | Local scheduling |
| **Photo Library (Add Only)** | You save a music card | Write the rendered image; no full-library read |
| **iCloud** | You enable sync | Mirror lists / notes / history / streaks |
| **Live Activities (iOS)** | You leave Reading Live Activity on (default on) | Show the guide you are **reading** on Lock Screen / Dynamic Island |
| **Background audio** | You leave background audio on | Continue MusicKit / preview / TTS when not in the foreground |

We do **not** request Contacts, precise Location, Camera, or Tracking. We do **not** request full Photo Library read access.

## What We Do Not Do

- We do **not** sell personal data or build advertising profiles.
- We do **not** require an account or social login.
- We do **not** embed third-party ad, analytics, or social SDKs for data collection.
- We do **not** store full songs on device or on our servers.
- We do **not** keep Shazam microphone buffers after recognition.
- We do **not** show a custom Dynamic Island for **music playback** — only for reading a guide, and only if you leave that setting on.
- We do **not** receive StoreKit payment card numbers.

## Children’s Privacy

iMusic does not knowingly collect personal data from anyone, including children under 13 (or the equivalent age in your region). Because we do not operate a data-collection backend, there is no child profile stored with us. Apple Music and Shazam follow Apple’s terms and age rules.

## Third Parties

- **Apple** — App Store, MusicKit / Apple Music, ShazamKit, optional StoreKit, optional iCloud KVS, system TTS, Share Sheet destinations you pick, notifications, Live Activities, Siri / Shortcuts.
- **No other third-party SDKs** for ads, analytics, or social login are included for data collection.

## International Users

Guides work offline on your device. Apple Music, Shazam, and iCloud follow Apple’s terms and regional availability. Catalog matching depends on the storefront of the signed-in Apple ID.

## Data Retention & Deletion

- **On device** — Clear artwork / preview caches in **Settings → Storage**. Uninstalling removes the sandbox and App Group data.
- **iCloud (optional)** — Remains in **your** iCloud until you disable sync and/or clear it through Apple’s tools.
- **iHTC Studio** — We have no server-side account dataset to delete.

## Changes to This Policy

We may update this Privacy Policy from time to time. The “Last updated” date at the top will change, and the revised policy will be posted on this page.

## Contact Us

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

We typically respond within 48 hours.

</section>

<section lang="zh-CN" markdown="1">

**最近更新：** 2026 年 9 月 9 日

爱火腿肠工作室（iHTC Studio）（「我们」；原 iHTCTeam）开发了 **爱音乐**（iMusic / 愛音樂，Bundle ID `com.iHTCboy.iMusic`）。本页说明使用本应用时数据如何被处理（以及**不会**如何被处理）。**App Store 审核**与用户可将本页作为公开隐私政策。在 App Store Connect 填写地址时：打开本站[隐私政策](privacy)页，从浏览器地址栏复制当前网址（站点域名日后可能变更）。

## 概要（对齐 App Store 隐私标签）

| 主题 | 我们的做法 |
|------|------------|
| 账号 | **不需要**——无需注册、邮箱登录或手机号 |
| iHTC Studio 收集数据 | **不收集数据（Data Not Collected）**——我们**不**运营接收你个人数据的后端 |
| 网络 | **导听**安装后可**离线**阅读。**播放**与**识曲**在你授权后走 Apple 服务 |
| 分析 / 广告 / 追踪 | **无**——无第三方分析、广告或追踪 SDK；不使用跨 App 追踪 |
| 可选的 Apple 服务 | **Apple Music / MusicKit**、**ShazamKit**、**iCloud**（你的私有键值存储）、乐卡**相册（仅添加）**、打赏 **StoreKit**、**本地通知**、可选**实时活动** |

## 数据收集

我们**不**出于广告或分析目的收集、出售或共享个人信息。

- **无账号** — 无需在我们这边创建账户即可阅读全部内置导听。
- **无分析与广告** — 应用未集成会向我们回传数据的第三方分析、广告或崩溃统计 SDK。
- **无导听上传** — 收藏、听单、稍后听、笔记、历史与偏好留在你的设备（以及可选的**你的** iCloud），不会上传到 iHTC Studio——因为**本应用不为此运营此类服务器**。
- **不托管歌曲** — 我们不打包完整音频。匹配后的播放由 **Apple Music** 提供。未订阅时最多在本机缓存 **30 秒目录试听**。

## 应用工作原理

- **内置语料** — 曲目索引、导听分片、歌手志、分类、合集、名句与年历随 App / 小组件安装。阅读导听不必联网。
- **Apple Music（MusicKit）** — 你点播放并授权后，应用按精编目录匹配（优先 ISRC，再艺人 + 曲名），经 Apple 播放器出声。订阅状态向 Apple 查询；超时视为**未知**，不会误判成未订阅。封面 URL 可能被取回用于展示。我们不会收到你的 Apple ID 或支付信息。
- **30 秒试听** — 未订阅时，Apple 的预览可落入本机 `Caches`（LRU，不是完整曲）。蜂窝 / 低电量 / 低数据模式不预拉下一首。设置可分列清理封面与试听，不碰收藏与听单。
- **听歌识曲（ShazamKit）** — 仅在打开识曲时使用。麦克风音频由 **Apple** 识别；我们不保存录音。命中精编库则打开本机赏析。
- **本机语音合成** — 朗读导听使用系统 **AVSpeechSynthesizer**，不会把正文发到 iHTC Studio。
- **小组件与 App Group** — App 与小组件通过本机 `group.com.iHTCboy.iMusic` 共享偏好。朗读实时活动的封面是该组里的小 JPEG + token，不会把整图塞进活动状态。
- **每日通知** — 仅本机调度；点按以深链打开本机曲目。
- **乐卡** — 设备上渲染。仅当你点保存时申请**相册仅添加**。
- **可选打赏** — Apple **StoreKit** 消耗型内购。
- **可选 Spotlight** — **默认关闭**。开启后由系统在本机建索引。

## 设备本地存储

| 数据 | 位置 | 用途 |
|------|------|------|
| 导听库（索引 + 分片） | App / Widget Bundle | 离线阅读 |
| 收藏、听单、稍后听 | App Group UserDefaults | 你的清单 |
| 笔记、历史、朗读进度 | App Group UserDefaults | 继续听 / 读 |
| 打卡 | App Group UserDefaults | 每日习惯 |
| 外观、语言、朗读、标签 | App Group UserDefaults | 设置 |
| 今日一乐缓存与通知 | App Group UserDefaults | 今日 ID 与提醒 |
| 乐卡偏好 | App Group UserDefaults | 上次风格 / 画布 |
| 封面 URL 与位图 | App Group + 内存 / 磁盘缓存 | 展示封面；仅在已授权后静默预取 |
| 30 秒试听文件 | App Caches | 命中后离线再听预览 |
| 实时活动缩略图 | App Group JPEG + token | **朗读**导听时的锁屏 / 灵动岛 |
| MusicKit / Shazam 授权 | 系统 | 记住你的选择 |
| 引导与评价提示 | 本机 UserDefaults | 欢迎 / 评价 |

卸载会按系统规则删除沙盒与 App Group。可选 iCloud 副本仍在**你的** iCloud。Apple Music 曲库与订阅留在 Apple。

## iCloud 同步（可选）

若在设置中开启 **iCloud 同步**，应用通过绑定**你的 Apple ID** 的 **`NSUbiquitousKeyValueStore`** 镜像：

- 收藏
- 听单
- 稍后听
- 笔记
- 聆听 / 阅读历史
- 朗读进度
- 打卡

导听正文已随应用安装。封面文件与试听音频**不会**经 KVS 同步。流量通往 **Apple iCloud**，不经过 iHTC Studio。可在设置中关闭。我们无法读取你的 iCloud 内容。

## 权限说明

仅在功能需要时请求：

| 权限 | 时机 | 原因 |
|------|------|------|
| **Apple Music / 媒体资料库** | 你在说明页继续，或点播放 | 匹配并播放目录曲；加载封面 |
| **麦克风** | 你打开听歌识曲 | 识别环境中正在播放的音乐 |
| **通知** | 你开启今日一乐提醒 | 本机调度 |
| **相册（仅添加）** | 你保存乐卡 | 写入渲染图；不读取全部相册 |
| **iCloud** | 你开启同步 | 镜像清单 / 笔记 / 历史 / 打卡 |
| **实时活动（iOS）** | 你保持「朗读实时活动」开启（默认开） | 在锁屏 / 灵动岛显示你正在**朗读**的导听 |
| **后台音频** | 你保持后台音频开启 | 离开前台时继续 MusicKit / 试听 / TTS |

我们**不**申请通讯录、精确位置、相机或追踪，也**不**申请相册读取。

## 我们不会做的事

- **不**出售个人数据，不建立广告画像
- **不**强制账号或社交登录
- **不**内置广告 / 分析 / 社交登录 SDK 用于收集数据
- **不**在设备或我们的服务器上保存完整歌曲
- **不**在识别结束后保留 Shazam 麦克风缓冲
- **不**为**播放音乐**另开自定义灵动岛——只在朗读导听且你未关闭该开关时出现
- **不**接收 StoreKit 银行卡号

## 儿童隐私

爱音乐不会有意收集任何人的个人数据，包括 13 岁以下（或你所在地区的同等年龄）儿童。我们没有数据收集后端，因此不存在儿童档案。Apple Music 与 Shazam 遵循 Apple 条款与年龄规则。

## 第三方

- **Apple** — App Store、MusicKit / Apple Music、ShazamKit、可选 StoreKit、可选 iCloud KVS、系统 TTS、你选择的分享目标、通知、实时活动、Siri / 快捷指令
- **无**其他用于广告、分析或社交登录的第三方 SDK

## 国际用户

导听可在设备上离线使用。Apple Music、Shazam 与 iCloud 遵循 Apple 条款与地区可用性。目录匹配取决于登录 Apple ID 的商店地区。

## 保留与删除

- **本机** — 可在 **设置 → 存储与缓存** 清理封面 / 试听。卸载会删除沙盒与 App Group 数据
- **iCloud（可选）** — 留在**你的** iCloud，直到你关闭同步并/或用 Apple 工具清理
- **iHTC Studio** — 我们没有可按请求删除的服务端账号库

## 政策变更

我们可能更新本政策。「最近更新」日期会改，修订稿发布在本页。

## 联系我们

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

我们通常在 48 小时内回复。

</section>

<section lang="zh-TW" markdown="1">

**最近更新：** 2026 年 9 月 9 日

愛火腿腸工作室（iHTC Studio）（「我們」；原 iHTCTeam）開發了 **愛音樂**（iMusic / 爱音乐，Bundle ID `com.iHTCboy.iMusic`）。本頁說明使用本應用時資料如何被處理（以及**不會**如何被處理）。**App Store 審核**與使用者可將本頁作為公開隱私政策。在 App Store Connect 填寫地址時：打開本站[隱私政策](privacy)頁，從瀏覽器網址列複製目前網址（站點網域日後可能變更）。

## 概要（對齊 App Store 隱私標籤）

| 主題 | 我們的做法 |
|------|------------|
| 帳號 | **不需要**——無需註冊、信箱登入或手機號 |
| iHTC Studio 收集資料 | **不收集資料（Data Not Collected）**——我們**不**營運接收你個人資料的後端 |
| 網路 | **導聽**安裝後可**離線**閱讀。**播放**與**識曲**在你授權後走 Apple 服務 |
| 分析 / 廣告 / 追蹤 | **無**——無第三方分析、廣告或追蹤 SDK；不使用跨 App 追蹤 |
| 可選的 Apple 服務 | **Apple Music / MusicKit**、**ShazamKit**、**iCloud**（你的私有鍵值儲存）、樂卡**相簿（僅加入）**、打賞 **StoreKit**、**本地通知**、可選**即時動態** |

## 資料收集

我們**不**出於廣告或分析目的收集、出售或共享個人資訊。

- **無帳號** — 無需在我們這邊建立帳戶即可閱讀全部內建導聽。
- **無分析與廣告** — 應用未整合會向我們回傳資料的第三方分析、廣告或崩潰統計 SDK。
- **無導聽上傳** — 收藏、聽單、稍後聽、筆記、歷史與偏好留在你的裝置（以及可選的**你的** iCloud），不會上傳到 iHTC Studio——因為**本應用不為此營運此類伺服器**。
- **不托管歌曲** — 我們不打包完整音訊。匹配後的播放由 **Apple Music** 提供。未訂閱時最多在本機快取 **30 秒目錄試聽**。

## 應用運作原理

- **內建語料** — 曲目索引、導聽分片、歌手誌、分類、合集、名句與年曆隨 App / 小工具安裝。閱讀導聽不必連網。
- **Apple Music（MusicKit）** — 你點播放並授權後，應用按精編目錄匹配（優先 ISRC，再藝人 + 曲名），經 Apple 播放器出聲。訂閱狀態向 Apple 查詢；逾時視為**未知**，不會誤判成未訂閱。封面 URL 可能被取回用於展示。我們不會收到你的 Apple ID 或支付資訊。
- **30 秒試聽** — 未訂閱時，Apple 的預覽可落入本機 `Caches`（LRU，不是完整曲）。行動網路 / 低電量 / 低資料模式不預拉下一首。設定可分列清理封面與試聽，不碰收藏與聽單。
- **聽歌識曲（ShazamKit）** — 僅在打開識曲時使用。麥克風音訊由 **Apple** 辨識；我們不保存錄音。命中精編庫則打開本機賞析。
- **本機語音合成** — 朗讀導聽使用系統 **AVSpeechSynthesizer**，不會把正文發到 iHTC Studio。
- **小工具與 App Group** — App 與小工具透過本機 `group.com.iHTCboy.iMusic` 共享偏好。朗讀即時動態的封面是該組裡的小 JPEG + token，不會把整圖塞進動態狀態。
- **每日通知** — 僅本機排程；點按以深鏈打開本機曲目。
- **樂卡** — 裝置上渲染。僅當你點儲存時申請**相簿僅加入**。
- **可選打賞** — Apple **StoreKit** 消耗型內購。
- **可選 Spotlight** — **預設關閉**。開啟後由系統在本機建索引。

## 裝置本地儲存

| 資料 | 位置 | 用途 |
|------|------|------|
| 導聽庫（索引 + 分片） | App / Widget Bundle | 離線閱讀 |
| 收藏、聽單、稍後聽 | App Group UserDefaults | 你的清單 |
| 筆記、歷史、朗讀進度 | App Group UserDefaults | 繼續聽 / 讀 |
| 打卡 | App Group UserDefaults | 每日習慣 |
| 外觀、語言、朗讀、標籤 | App Group UserDefaults | 設定 |
| 今日一樂快取與通知 | App Group UserDefaults | 今日 ID 與提醒 |
| 樂卡偏好 | App Group UserDefaults | 上次風格 / 畫布 |
| 封面 URL 與點陣圖 | App Group + 記憶體 / 磁碟快取 | 展示封面；僅在已授權後靜默預取 |
| 30 秒試聽檔 | App Caches | 命中後離線再聽預覽 |
| 即時動態縮圖 | App Group JPEG + token | **朗讀**導聽時的鎖定畫面 / 靈動島 |
| MusicKit / Shazam 授權 | 系統 | 記住你的選擇 |
| 引導與評價提示 | 本機 UserDefaults | 歡迎 / 評價 |

解除安裝會依系統規則刪除沙盒與 App Group。可選 iCloud 副本仍在**你的** iCloud。Apple Music 曲庫與訂閱留在 Apple。

## iCloud 同步（可選）

若在設定中開啟 **iCloud 同步**，應用透過綁定**你的 Apple ID** 的 **`NSUbiquitousKeyValueStore`** 鏡像：

- 收藏
- 聽單
- 稍後聽
- 筆記
- 聆聽 / 閱讀歷史
- 朗讀進度
- 打卡

導聽正文已隨應用安裝。封面檔與試聽音訊**不會**經 KVS 同步。流量通往 **Apple iCloud**，不經過 iHTC Studio。可在設定中關閉。我們無法讀取你的 iCloud 內容。

## 權限說明

僅在功能需要時請求：

| 權限 | 時機 | 原因 |
|------|------|------|
| **Apple Music / 媒體資料庫** | 你在說明頁繼續，或點播放 | 匹配並播放目錄曲；載入封面 |
| **麥克風** | 你打開聽歌識曲 | 辨識環境中正在播放的音樂 |
| **通知** | 你開啟今日一樂提醒 | 本機排程 |
| **相簿（僅加入）** | 你儲存樂卡 | 寫入渲染圖；不讀取全部相簿 |
| **iCloud** | 你開啟同步 | 鏡像清單 / 筆記 / 歷史 / 打卡 |
| **即時動態（iOS）** | 你保持「朗讀即時動態」開啟（預設開） | 在鎖定畫面 / 靈動島顯示你正在**朗讀**的導聽 |
| **背景音訊** | 你保持背景音訊開啟 | 離開前景時繼續 MusicKit / 試聽 / TTS |

我們**不**申請通訊錄、精確位置、相機或追蹤，也**不**申請相簿讀取。

## 我們不會做的事

- **不**出售個人資料，不建立廣告畫像
- **不**強制帳號或社交登入
- **不**內建廣告 / 分析 / 社交登入 SDK 用於收集資料
- **不**在裝置或我們的伺服器上保存完整歌曲
- **不**在辨識結束後保留 Shazam 麥克風緩衝
- **不**為**播放音樂**另開自訂靈動島——只在朗讀導聽且你未關閉該開關時出現
- **不**接收 StoreKit 銀行卡號

## 兒童隱私

愛音樂不會有意收集任何人的個人資料，包括 13 歲以下（或你所在地區的同等年齡）兒童。我們沒有資料收集後端，因此不存在兒童檔案。Apple Music 與 Shazam 遵循 Apple 條款與年齡規則。

## 第三方

- **Apple** — App Store、MusicKit / Apple Music、ShazamKit、可選 StoreKit、可選 iCloud KVS、系統 TTS、你選擇的分享目標、通知、即時動態、Siri / 捷徑
- **無**其他用於廣告、分析或社交登入的第三方 SDK

## 國際使用者

導聽可在裝置上離線使用。Apple Music、Shazam 與 iCloud 遵循 Apple 條款與地區可用性。目錄匹配取決於登入 Apple ID 的商店地區。

## 保留與刪除

- **本機** — 可在 **設定 → 儲存與快取** 清理封面 / 試聽。解除安裝會刪除沙盒與 App Group 資料
- **iCloud（可選）** — 留在**你的** iCloud，直到你關閉同步並/或用 Apple 工具清理
- **iHTC Studio** — 我們沒有可按請求刪除的服務端帳號庫

## 政策變更

我們可能更新本政策。「最近更新」日期會改，修訂稿發佈在本頁。

## 聯絡我們

- **電子郵件：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

我們通常在 48 小時內回覆。

</section>
