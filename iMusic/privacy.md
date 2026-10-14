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

iHTC Studio ("we", "us" or "our") built **iMusic** (also known as "爱音乐" / "愛音樂", Bundle ID `com.iHTCboy.iMusic`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on **this page** as the public privacy policy for the app. For App Store Connect, open this Privacy Policy in your browser and copy the address from the address bar (the public site domain may change over time).

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

爱火腿肠工作室（iHTC Studio）（「我们」）开发了 **爱音乐**（iMusic / 愛音樂，Bundle ID `com.iHTCboy.iMusic`）。本页说明使用本应用时数据如何被处理（以及**不会**如何被处理）。**App Store 审核**与用户可将本页作为公开隐私政策。在 App Store Connect 填写地址时：打开本站[隐私政策](../privacy)页，从浏览器地址栏复制当前网址（站点域名日后可能变更）。

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

愛火腿腸工作室（iHTC Studio）（「我們」）開發了 **愛音樂**（iMusic / 爱音乐，Bundle ID `com.iHTCboy.iMusic`）。本頁說明使用本應用時資料如何被處理（以及**不會**如何被處理）。**App Store 審核**與使用者可將本頁作為公開隱私政策。在 App Store Connect 填寫地址時：打開本站[隱私政策](../privacy)頁，從瀏覽器網址列複製目前網址（站點網域日後可能變更）。

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
<section lang="ja" markdown="1">

**最終更新:** 2026年9月9日

iHTC Studio（「当社」）は **iMusic**（「爱音乐」/「愛音樂」、Bundle ID `com.iHTCboy.iMusic`）を開発しました。本ページはアプリ利用時にデータがどう扱われるか（および扱われないか）を説明します。**Apple App Review** およびユーザーは本ページを公開プライバシーポリシーとして参照できます。App Store Connect では、ブラウザで本 Privacy Policy を開き、アドレスバーから URL をコピーしてください（公開ドメインは将来変更される場合があります）。

## 概要（Apple プライバシー表示ラベルとの整合）

| 項目 | 当社の方針 |
|-------|----------------|
| アカウント | **不要** — 登録、メールログイン、電話番号なし |
| iHTC Studio によるデータ収集 | **Data Not Collected** — 個人データを受け取る backend を**運用しません** |
| ネットワーク | **ガイド**はインストール後**オフライン**で閲覧可能。**再生**と**曲認識**は認可後に Apple サービスを使用 |
| 分析 / 広告 / 追跡 | **なし** — 第三者 analytics / 広告 / 追跡 SDK なし；App Tracking Transparency 不使用 |
| 任意の Apple サービス | **Apple Music / MusicKit**、**ShazamKit**、**iCloud**（私有 KVS）、シェアカード用 **Photo Library（追加のみ）**、任意チップ **StoreKit**、**ローカル通知**、任意 **Live Activities** |

## データ収集

広告や分析目的で個人情報を収集・販売・共有**しません**。

- **アカウントなし** — 当社アカウントなしで同梱ガイドをすべて閲覧できます。
- **分析・広告なし** — 当社へ電話する第三者 analytics / 広告 / クラッシュ SDK は同梱しません。
- **ガイドのアップロードなし** — お気に入り、リスンリスト、後で聴く、ノート、履歴、設定は端末（および任意で**あなたの** iCloud）に留まり、iHTC Studio サーバーへは送信されません（**当社は本アプリ用の such サーバーを運用しません**）。
- **楽曲ホスティングなし** — フルオーディオは同梱しません。マッチした再生は **Apple Music** が提供。未加入時は最大 **30 秒カタログプレビュー**を端末にキャッシュする場合があります。

## アプリの動作

- **同梱ライブラリ** — 曲索引、ガイド、歌手ノート、カテゴリ、コレクション、名句、日次カレンダーは App / Widget 同梱。ガイド閲覧にネットワーク不要。
- **Apple Music（MusicKit）** — 再生しアクセスを許可すると、精選カタログを照合（ISRC 優先、次にアーティスト + タイトル）し Apple プレイヤーで再生。加入状態は Apple に問い合わせ；タイムアウトは**不明**扱い（「未加入」とは断定しません）。カバー表示のため artwork URL を取得する場合があります。Apple ID や支払情報は当社に届きません。
- **30 秒プレビュー** — 未加入時、Apple プレビューが端末 `Caches` に保存される場合あり（LRU；フルトラックではありません）。セルラー / 低電力 / 低データモードでは次のプレビューを先読みしません。設定で artwork とプレビューキャッシュを個別に削除でき、お気に入りやリスンリストには触れません。
- **曲認識（ShazamKit）** — Recognize を開いたときのみ。マイク音声は **Apple** が処理；録音アーカイブは保持しません。カタログヒットで端末内ガイドを開きます。
- **端末内音声** — ガイド朗読は Apple **AVSpeechSynthesizer**。本文を iHTC Studio へ送りません。
- **Widget と App Group** — App と Widget は端末上 `group.com.iHTCboy.iMusic` で設定共有。Live Activity の artwork は小 JPEG + token（ペイロード全体にフル画像は入れません）。
- **毎日の通知** — ローカルスケジュール。タップで端末内曲 ID への deep link。
- **シェアカード** — 端末でレンダリング。保存タップ時のみ **Photo Library 追加のみ**。
- **任意チップ** — Apple **StoreKit** 消耗型。
- **任意 Spotlight** — **既定オフ**。有効時は端末上でシステムに索引送信。

## 端末に保存されるデータ

| データ | 場所 | 目的 |
|------|-------|---------|
| ガイドライブラリ（索引 + シャード） | App / Widget bundle | オフライン閲覧 |
| お気に入り、リスンリスト、後で聴く | App Group UserDefaults | あなたのリスト |
| ノート、履歴、朗読進捗 | App Group UserDefaults | 聴取 / 閲覧の継続 |
| ストリーク / チェックイン | App Group UserDefaults | 毎日の習慣 |
| 外観、言語、音声、タブ | App Group UserDefaults | 設定 |
| Daily Piece キャッシュと通知設定 | App Group UserDefaults | 今日の ID とスケジュール |
| シェアカード設定 | App Group UserDefaults | 前回のスタイル / キャンバス |
| Artwork URL とデコード画像 | App Group + メモリ / ディスクキャッシュ | カバー表示；MusicKit 認可後のみ静かに先読み |
| 30 秒プレビューファイル | App Caches | 初回ヒット後オフライン再生 |
| Live Activity サムネイル | App Group JPEG + token | ガイド**朗読**中の Lock Screen / Dynamic Island |
| MusicKit / Shazam 認可 | システム | 選択の記憶 |
| オンボーディングと評価プロンプト | 端末 UserDefaults | ウェルカム / レビュー |

アンインストールでサンドボックスと App Group を削除（iOS / macOS の規則に従う）。任意 iCloud コピーは**あなたの** iCloud に残ります。Apple Music ライブラリと加入は Apple 側に残ります。

## iCloud 同期（任意）

設定で **iCloud Sync** を有効にすると、**あなたの Apple ID** に紐づく **`NSUbiquitousKeyValueStore`** で以下をミラーします：

- お気に入り
- リスンリスト
- 後で聴く
- ノート
- 聴取 / 閲覧履歴
- 朗読進捗
- ストリーク

ガイド本文は既に App 同梱。Artwork ファイルとプレビュー音声は KVS 同期**しません**。トラフィックは **Apple iCloud** へ行き、iHTC Studio を経由しません。設定で無効化できます。当社はあなたの iCloud 内容を読めません。

## 権限

iMusic は機能に必要なときだけ権限を要求します：

| 権限 | タイミング | 理由 |
|------------|------|-----|
| **Apple Music / メディアライブラリ** | Music 説明で続行、または再生タップ | カタログ曲の照合と再生；カバー読込 |
| **マイク** | Song ID を開く | 周囲の音楽を認識 |
| **通知** | Daily Piece リマインダーを有効化 | ローカルスケジュール |
| **Photo Library（追加のみ）** | ミュージックカード保存 | レンダリング画像の書き込み；ライブラリ全体は読まない |
| **iCloud** | 同期を有効化 | リスト / ノート / 履歴 / ストリークのミラー |
| **Live Activities（iOS）** | Reading Live Activity をオン（既定オン） | **朗読**中のガイドを Lock Screen / Dynamic Island に表示 |
| **バックグラウンドオーディオ** | バックグラウンドオーディオをオン | 非前面時も MusicKit / プレビュー / TTS を継続 |

連絡先、精密位置、カメラ、Tracking は要求**しません**。Photo Library の読み取りも要求**しません**。

## 当社が行わないこと

- 個人データの販売や広告プロファイルの構築**をしない**
- アカウントやソーシャルログインを強制**しない**
- データ収集目的の第三者 ad / analytics / ソーシャル SDK を同梱**しない**
- 端末や当社サーバーにフル曲を保存**しない**
- 認識後 Shazam マイクバッファを保持**しない**
- **音楽再生**用のカスタム Dynamic Island を表示**しない** — ガイド朗読時のみ（設定でオンの場合）
- StoreKit のカード番号を受け取ら**ない**

## 児童のプライバシー

iMusic は 13 歳未満（または地域の同等年齢）を含め、故意に個人データを収集しません。データ収集 backend がないため、当社に児童プロファイルはありません。Apple Music と Shazam は Apple の規約と年齢ルールに従います。

## 第三者

- **Apple** — App Store、MusicKit / Apple Music、ShazamKit、任意 StoreKit、任意 iCloud KVS、システム TTS、あなたが選ぶ共有先、通知、Live Activities、Siri / Shortcuts
- データ収集目的の **他の第三者 SDK はありません**

## 国際的なユーザー

ガイドは端末でオフライン利用可能。Apple Music、Shazam、iCloud は Apple の規約と地域提供に従います。カタログ照合はサインイン中 Apple ID のストアフロントに依存します。

## データの保持と削除

- **端末** — **設定 → ストレージ**で artwork / プレビューキャッシュを削除。アンインストールでサンドボックスと App Group を削除。
- **iCloud（任意）** — **あなたの** iCloud に残り、同期をオフにするか Apple のツールで消すまで。
- **iHTC Studio** — 削除依頼のサーバー側アカウントデータセットはありません。

## 本ポリシーの変更

随時更新する場合があります。上部の「最終更新」日付が変わり、改訂版が本ページに掲載されます。

## お問い合わせ

- **メール:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

通常 48 時間以内に返信します。

</section>
<section lang="ko" markdown="1">

**최종 업데이트:** 2026년 9월 9일

iHTC Studio(「당사」)는 **iMusic**(「爱音乐」/「愛音樂」, Bundle ID `com.iHTCboy.iMusic`)을 개발했습니다. 이 페이지는 앱 및 위젯 확장 사용 시 어떤 데이터가 처리되는지(또는 처리되지 않는지) 설명합니다. **Apple App Review** 및 사용자는 본 페이지를 공개 개인정보 처리방침으로 참고할 수 있습니다. App Store Connect: 브라우저에서 본 [Privacy Policy](../privacy)를 열고 주소창 URL을 복사하세요(공개 도메인은 변경될 수 있음).

## 요약(Apple Privacy Nutrition Label 정렬)

| 항목 | 당사 방침 |
|-------|----------------|
| 계정 | **불필요** — 가입, 이메일, 전화번호 없음 |
| iHTC Studio 데이터 수집 | **Data Not Collected** — 개인 데이터를 받는 backend **미운영** |
| 네트워크 | **가이드**는 설치 후 **오프라인** 열람; **재생**·**곡 인식**은 허용 후 Apple 서비스 |
| 분석/광고/추적 | **없음** — 제3자 analytics/광고/추적 SDK 없음; ATT 미사용 |
| 선택 Apple 서비스 | **Apple Music/MusicKit**, **ShazamKit**, **iCloud**(private KVS), 공유 카드용 **사진(추가만)**, 선택 **StoreKit** 팁, **로컬 알림**, 선택 **Live Activities** |

## 데이터 수집

광고·분석 목적으로 개인정보를 수집·판매·공유**하지 않습니다**.

- **계정 없음** — iHTC Studio 계정 없이 동봉 가이드 전부 이용.
- **분석·광고 없음** — 당사로 전화하는 제3자 analytics/광고/크래시 SDK 없음.
- **가이드 업로드 없음** — 즐겨찾기, 리스트, 나중에 듣기, 메모, 기록, 설정은 기기(및 선택 시 **귀하의** iCloud)에만; iHTC Studio 서버로 전송 안 함(**본 앱용 such 서버 미운영**).
- **곡 호스팅 없음** — 전체 오디오 미포함. 매칭 재생은 **Apple Music**. 미가입 시 최대 **30초 카탈로그 미리듣기**가 기기에 캐시될 수 있음.

## 앱 동작

- **동봉 라이브러리** — 곡 색인, 가이드, 아티스트 노트, 카테고리, 컬렉션, 명구, 일일 달력 App/Widget 동봉; 가이드는 네트워크 불필요.
- **Apple Music(MusicKit)** — 재생 허용 시 큐레이션 카탈로그 매칭(ISRC 우선, 아티스트+제목) 후 Apple 플레이어. 구독 상태는 Apple 문의; 타임아웃은 **알 수 없음**. 커버용 artwork URL. Apple ID/결제 정보는 당사에 없음.
- **30초 미리듣기** — 미가입 시 Apple 미리듣기가 `Caches`에 저장될 수 있음(LRU; 전체 트랙 아님). 셀룰러/저전력/저데이터 모드에서 다음 미리듣기 선로드 안 함. 설정에서 artwork·미리듣기 캐시 개별 삭제, 즐겨찾기/리스트는 유지.
- **곡 인식(ShazamKit)** — Recognize 열 때만; 마이크는 **Apple** 처리; 녹음 아카이브 없음. 히트 시 기기 내 가이드.
- **기기 내 음성** — 가이드 낭독 **AVSpeechSynthesizer**; 본문 iHTC Studio 미전송.
- **Widget & App Group** — `group.com.iHTCboy.iMusic` 설정 공유; Live Activity artwork 소형 JPEG+토큰.
- **일일 알림** — 로컬 예약; 탭 시 곡 ID 딥링크.
- **공유 카드** — 기기 렌더링; 저장 시 **사진 추가만**.
- **선택 팁** — **StoreKit** 소모형.
- **선택 Spotlight** — **기본 꺼짐**; 켜면 기기에서 시스템 색인.

## 기기 저장 데이터

| 데이터 | 위치 | 목적 |
|------|-------|---------|
| 가이드 라이브러리 | App/Widget bundle | 오프라인 |
| 즐겨찾기·리스트·나중에 | App Group UserDefaults | 목록 |
| 메모·기록·낭독 진행 | App Group UserDefaults | 이어하기 |
| 스트릭/체크인 | App Group UserDefaults | 습관 |
| 외관·언어·탭 | App Group UserDefaults | 설정 |
| Daily Piece 캐시·알림 | App Group UserDefaults | 오늘 ID |
| 공유 카드 설정 | App Group UserDefaults | 스타일 |
| Artwork URL·이미지 | App Group+캐시 | 커버 |
| 30초 미리듣기 파일 | App Caches | 오프라인 |
| Live Activity 썸네일 | App Group JPEG+토큰 | **낭독** 중 잠금화면 |
| MusicKit/Shazam 허용 | 시스템 | 선택 기억 |
| 온보딩·리뷰 | UserDefaults | 환영/리뷰 |

삭제 시 sandbox·App Group 제거(iOS/macOS 규칙). 선택 iCloud는 **귀하의** iCloud에 잔류. Apple Music 라이브러리·구독은 Apple.

## iCloud 동기화(선택)

**iCloud Sync** 켜면 **Apple ID**의 **`NSUbiquitousKeyValueStore`**에 미러:

- 즐겨찾기, 리스트, 나중에, 메모, 청취/열람 기록, 낭독 진행, 스트릭

가이드 본문은 App 동봉. Artwork·미리듣기 오디오 KVS **미동기**. **Apple iCloud**로만; iHTC Studio 경유 없음. 끄기 가능; 당사는 iCloud 읽기 불가.

## 권한

| 권한 | 시점 | 이유 |
|------------|------|-----|
| **Apple Music/미디어** | MusicKit 또는 재생 | 매칭·재생·커버 |
| **마이크** | Song ID | 주변 음악 인식 |
| **알림** | Daily Piece | 로컬 |
| **사진(추가만)** | 뮤직 카드 저장 | 렌더 이미지 |
| **iCloud** | 동기화 | 목록/메모/기록 |
| **Live Activities** | Reading(기본 켜짐) | **낭독** 중 잠금화면 |
| **백그라운드 오디오** | 옵션 | MusicKit/미리듣기/TTS |

연락처·정밀 위치·카메라·추적 없음. 사진 라이브러리 **읽기** 없음.

## 하지 않는 일

- 개인정보 판매·광고 프로필 없음
- 계정·소셜 로그인 강제 없음
- 데이터 수집 목적 제3자 SDK 없음
- 전체 곡 당사 서버/기기 저장 없음
- Shazam 마이크 버퍼 인식 후 보관 없음
- **음악 재생**용 커스텀 Dynamic Island 없음 — 가이드 낭독만
- StoreKit 카드번호 미수신

## 아동

13세 미만(또는 지역 동등 연령) 포함 고의 수집 없음. 수집 backend 없음 → 아동 프로필 없음. Apple Music·Shazam은 Apple 규정.

## 제3자

- **Apple** — App Store, MusicKit, ShazamKit, StoreKit, iCloud KVS, TTS, 공유, 알림, Live Activities, Siri/Shortcuts
- 데이터 수집 **다른 SDK 없음**

## 국제 사용자

가이드 기기 오프라인. Apple Music·Shazam·iCloud Apple 약관. 카탈로그 매칭은 로그인 Apple ID 스토어프론트.

## 보관·삭제

- **기기** — **설정→저장장치**에서 캐시 삭제; 삭제 시 sandbox/App Group
- **iCloud** — **귀하의** iCloud에 잔류
- **iHTC Studio** — 서버 계정 데이터 없음

## 변경

정책 업데이트 가능; 상단 날짜 변경.

## 문의

- **이메일:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

보통 48시간 이내 답변.

</section>
<section lang="ru" markdown="1">

**Последнее обновление:** 9 сентября 2026 г.

iHTC Studio («мы») разработала **iMusic** («爱音乐» / «愛音樂», Bundle ID `com.iHTCboy.iMusic`). Эта страница объясняет, какие данные обрабатываются (и не обрабатываются) при использовании приложения и расширения виджета. **Apple App Review** и пользователи могут опираться на неё как на публичную политику конфиденциальности. Для App Store Connect откройте [Privacy Policy](../privacy) в браузере и скопируйте URL (публичный домен может измениться).

## Кратко (Apple Privacy Nutrition Label)

| Тема | Наша практика |
|-------|----------------|
| Учётная запись | **Не требуется** — без регистрации, e-mail и телефона |
| Сбор данных iHTC Studio | **Data Not Collected** — **не** эксплуатируем backend, принимающий персональные данные |
| Сеть | **Гиды** **офлайн** после установки; **воспроизведение** и **распознавание** — сервисы Apple после разрешения |
| Аналитика / реклама / трекинг | **Нет** — без сторонних analytics/рекламы/tracking SDK; без ATT |
| Опциональные сервисы Apple | **Apple Music / MusicKit**, **ShazamKit**, **iCloud** (private KVS), **Фото (только добавление)** для карточек, опциональный **StoreKit**, **локальные уведомления**, **Live Activities** |

## Сбор данных

Мы **не** собираем, продаём и не передаём персональные данные в рекламных или аналитических целях.

- **Без аккаунта** — все встроенные гиды доступны без учётной записи iHTC Studio.
- **Без аналитики и рекламы** — нет сторонних SDK, звонящих нам.
- **Без загрузки гидов** — избранное, списки, «позже», заметки, история и настройки остаются на устройстве (и опционально в **вашем** iCloud), не на серверах iHTC Studio (**мы не ведём такой backend для этого приложения**).
- **Без хостинга музыки** — полные аудиофайлы не встроены. Воспроизведение совпадений даёт **Apple Music**. Без подписки до **30 с превью каталога** может кэшироваться локально.

## Как работает приложение

- **Встроенная библиотека** — индекс, гиды, заметки об артистах, категории, коллекции, цитаты, календарь в bundle app/widget; гиды без сети.
- **Apple Music (MusicKit)** — после разрешения сопоставление с каталогом (ISRC, затем артист + название) и воспроизведение через Apple. Статус подписки у Apple; таймаут = **неизвестно**. URL обложек. Apple ID и оплата нам не передаются.
- **Превью 30 с** — без подписки превью Apple может сохраняться в `Caches` (LRU, не полный трек). Без предзагрузки следующего превью в сотовой / энергосбережении / экономии данных. Кэш artwork и превью можно очистить в настройках без избранного/списков.
- **Распознавание (ShazamKit)** — только при открытии Recognize; микрофон обрабатывает **Apple**; архивов записи нет. Совпадение открывает гид на устройстве.
- **Речь на устройстве** — озвучка гидов через **AVSpeechSynthesizer**; текст не отправляется в iHTC Studio.
- **Widget и App Group** — `group.com.iHTCboy.iMusic`; artwork Live Activity — малый JPEG + token.
- **Ежедневные уведомления** — локальное расписание; tap → deep link к ID трека.
- **Карточки шаринга** — рендер на устройстве; **Фото только добавление** при сохранении.
- **Опциональные чаевые** — consumable **StoreKit**.
- **Опциональный Spotlight** — **выключен по умолчанию**; при включении индексация системой на устройстве.

## Данные на устройстве

| Данные | Место | Назначение |
|------|-------|---------|
| Библиотека гидов | Bundle app/widget | Офлайн |
| Избранное, списки | App Group UserDefaults | Списки |
| Заметки, история, прогресс озвучки | App Group UserDefaults | Продолжение |
| Серии / check-in | App Group UserDefaults | Привычка |
| Оформление, язык | App Group UserDefaults | Настройки |
| Daily Piece и уведомления | App Group UserDefaults | ID дня |
| Настройки карточек | App Group UserDefaults | Стиль |
| URL artwork | App Group + cache | Обложки |
| Файлы превью 30 с | App Caches | Офлайн |
| Миниатюра Live Activity | App Group JPEG + token | Экран блокировки при **озвучке** |
| Разрешения MusicKit/Shazam | Система | Запоминание |
| Онбординг и отзыв | UserDefaults | Приветствие |

Удаление приложения удаляет sandbox и App Group. Опциональные копии iCloud остаются в **вашем** iCloud. Библиотека и подписка Apple Music — у Apple.

## Синхронизация iCloud (опционально)

При **iCloud Sync** **`NSUbiquitousKeyValueStore`** под **вашим Apple ID** зеркалит:

- Избранное, списки, «позже», заметки, историю прослушивания/чтения, прогресс озвучки, серии

Тексты гидов уже в bundle. Artwork и превью **не** синхронизируются KVS. Трафик только в **Apple iCloud**. Отключаемо; мы не читаем ваш iCloud.

## Разрешения

| Разрешение | Когда | Зачем |
|------------|------|-----|
| **Apple Music / медиатека** | MusicKit или воспроизведение | Сопоставление и play |
| **Микрофон** | Song ID | Распознавание |
| **Уведомления** | Daily Piece | Локально |
| **Фото (добавление)** | Сохранение карточки | Рендер |
| **iCloud** | Sync | Списки/история |
| **Live Activities** | Reading (по умолчанию вкл.) | **Озвучка** на экране блокировки |
| **Фоновое аудио** | Опция | MusicKit/превью/TTS |

Без контактов, точной геолокации, камеры и tracking. Без **чтения** фототеки.

## Чего мы не делаем

- Не продаём данные и не строим рекламные профили
- Не требуем аккаунт или social login
- Нет сторонних SDK для сбора данных
- Нет полных треков на наших серверах
- Не храним буферы микрофона Shazam после распознавания
- Нет custom Dynamic Island для **музыкального воспроизведения** — только озвучка гида
- Не получаем номера карт StoreKit

## Дети

Намеренно не собираем данные детей младше 13 лет (или местного возраста). Нет backend сбора → нет детских профилей у нас.

## Третьи стороны

- **Apple** — App Store, MusicKit, ShazamKit, StoreKit, iCloud KVS, TTS, шаринг, уведомления, Live Activities, Siri/Shortcuts
- **Других** SDK для сбора данных **нет**

## Международные пользователи

Гиды офлайн на устройстве. Apple Music, Shazam, iCloud — по правилам Apple. Сопоставление каталога зависит от storefront Apple ID.

## Хранение и удаление

- **Устройство** — кэш в **Настройки → Хранилище**; удаление app → sandbox/App Group
- **iCloud** — в **вашем** iCloud
- **iHTC Studio** — нет серверного аккаунта для удаления

## Изменения

Политика может обновляться; дата вверху изменится.

## Контакты

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Обычно ответ в течение 48 часов.

</section>
<section lang="th" markdown="1">

**อัปเดตล่าสุด:** 9 กันยายน 2026

iHTC Studio («เรา») พัฒนา **iMusic** («爱音乐» / «愛音樂», Bundle ID `com.iHTCboy.iMusic`) หน้านี้อธิบายว่าข้อมูลใดถูก (และไม่ถูก) จัดการเมื่อคุณใช้แอปและส่วนขยายวิดเจ็ต **Apple App Review** และผู้ใช้สามารถอ้างอิงหน้านี้เป็นนโยบายความเป็นส่วนตัวสาธารณะ สำหรับ App Store Connect: เปิด [Privacy Policy](../privacy) ในเบราว์เซอร์แล้วคัดลอก URL (โดเมนสาธารณะอาจเปลี่ยน)

## สรุป (สอดคล้อง Apple Privacy Nutrition Label)

| หัวข้อ | แนวทางของเรา |
|-------|----------------|
| บัญชี | **ไม่จำเป็น** — ไม่มีลงทะเบียน อีเมล หรือเบอร์โทร |
| การเก็บข้อมูลโดย iHTC Studio | **Data Not Collected** — **ไม่** มี backend รับข้อมูลส่วนบุคคล |
| เครือข่าย | **คู่มือ** อ่าน **ออฟไลน์** หลังติดตั้ง; **เล่น** และ **จดจำเพลง** ใช้บริการ Apple หลังอนุญาต |
| การวิเคราะห์/โฆษณา/ติดตาม | **ไม่มี** — ไม่มี SDK analytics/โฆษณา/ติดตามของบุคคลที่สาม; ไม่ใช้ ATT |
| บริการ Apple ทางเลือก | **Apple Music/MusicKit**, **ShazamKit**, **iCloud** (KVS ส่วนตัว), **คลังภาพ (เพิ่มเท่านั้น)** สำหรับการ์ดแชร์, **StoreKit** ทิป, **การแจ้งเตือนท้องถิ่น**, **Live Activities** |

## การเก็บข้อมูล

เรา**ไม่**เก็บ ขาย หรือแชร์ข้อมูลส่วนบุคคลเพื่อโฆษณาหรือการวิเคราะห์

- **ไม่มีบัญชี** — ใช้คู่มือในตัวได้โดยไม่มีบัญชี iHTC Studio
- **ไม่มี analytics/โฆษณา** — ไม่มี SDK ของบุคคลที่สามที่โทรหาเรา
- **ไม่อัปโหลดคู่มือ** — รายการโปรด ลิสต์ ฟังภายหลัง โน้ต ประวัติ การตั้งค่าอยู่บนอุปกรณ์ (และทางเลือก **iCloud ของคุณ**) ไม่ส่งไปเซิร์ฟเวอร์ iHTC Studio (**เราไม่มี backend แบบนั้นสำหรับแอปนี้**)
- **ไม่โฮสต์เพลง** — ไม่มีไฟล์เสียงเต็มในแอป การเล่นที่จับคู่มาจาก **Apple Music** ไม่สมัครอาจแคช **ตัวอย่าง 30 วิ** บนเครื่อง

## การทำงานของแอป

- **ไลบรารีในตัว** — ดัชนี คู่มือ โน้ตศิลปิน หมวด คอลเลกชัน คำคม ปฏิทินใน bundle; อ่านคู่มือไม่ต้องใช้เน็ต
- **Apple Music (MusicKit)** — หลังอนุญาต จับคู่แคตตalog (ISRC ก่อน แล้วศิลปิน+ชื่อ) เล่นผ่าน Apple สถานะสมัครถาม Apple; timeout = **ไม่ทราบ** URL ปก ไม่ได้รับ Apple ID/การชำระเงิน
- **ตัวอย่าง 30 วิ** — อาจเก็บใน `Caches` (LRU) ไม่ prefetch ถัดไปใน cellular/ประหยัดพลังงาน/ข้อมูล ล้าง cache ในการตั้งค่าได้
- **ShazamKit** — เมื่อเปิด Recognize เท่านั้น; ไมโครโฟนประมวลผลโดย **Apple** ไม่เก็บบันทึก
- **เสียงบนเครื่อง** — อ่านคู่มือด้วย **AVSpeechSynthesizer**
- **Widget & App Group** — `group.com.iHTCboy.iMusic`
- **การแจ้งเตือนรายวัน** — กำหนดการท้องถิ่น
- **การ์ดแชร์** — เรนเดอร์บนเครื่อง; **เพิ่มรูปเท่านั้น**
- **Spotlight** — **ปิดตามค่าเริ่มต้น**

## ข้อมูลบนอุปกรณ์

| ข้อมูล | ที่เก็บ | วัตถุประสงค์ |
|------|-------|---------|
| ไลบรารีคู่มือ | Bundle | ออฟไลน์ |
| รายการโปรด/ลิสต์ | App Group | รายการของคุณ |
| โน้ต/ประวัติ/ความคืบหน้า | App Group | ต่อเนื่อง |
| ส트รีค | App Group | นิสัย |
| การตั้งค่า | App Group | การตั้งค่า |
| Daily Piece | App Group | ID วันนี้ |
| Artwork/แคช | App Group+Cache | ปก |
| ไฟล์ตัวอย่าง 30 วิ | Caches | ออฟไลน์ |
| Live Activity | App Group | ขณะ**อ่านออกเสียง** |

ถอนการติดตั้งลบ sandbox/App Group สำเนา iCloud อยู่ใน **iCloud ของคุณ**

## iCloud (ทางเลือก)

**iCloud Sync** ใช้ **`NSUbiquitousKeyValueStore`** สะท้อนรายการโปรด ลิสต์ โน้ต ประวัติ สตรีค ไม่ sync ไฟล์ artwork/ตัวอย่าง ไป **Apple iCloud** เท่านั้น

## สิทธิ์

MusicKit, ไมโครโฟน, การแจ้งเตือน, รูป (เพิ่ม), iCloud, Live Activities, เสียงพื้นหลัง — ตามตารางในเวอร์ชัน EN/JA ไม่ขอ contacts/GPS/กล้อง/tracking

## สิ่งที่เราไม่ทำ

ไม่ขายข้อมูล ไม่บังคับบัญชี ไม่ SDK เก็บข้อมูล ไม่เก็บเพลงเต็ม ไม่ Dynamic Island สำหรับ**เล่นเพลง** — เฉพาะอ่านคู่มือ

## เด็ก / บุคคลที่สาม / ต่างประเทศ / การลบ

สอดคล้องนโยบาย EN: ไม่เก็บข้อมูลเด็จใจ มีเฉพาะ **Apple** เป็นบุคคลที่สามด้านบริการ ลบแคชในการตั้งค่า

## การเปลี่ยนแปลง

อาจอัปเดตนโยบาย; วันที่ด้านบนเปลี่ยน

## ติดต่อ

- **อีเมล:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

มักตอบภายใน 48 ชั่วโมง

</section>
<section lang="de" markdown="1">

**Zuletzt aktualisiert:** 9. September 2026

iHTC Studio („wir", „uns" oder „unser") hat **iMusic** (auch „爱音乐" / „愛音樂", Bundle ID `com.iHTCboy.iMusic`) entwickelt. Diese Seite erklärt, welche Daten bei der Nutzung der App (und der Widget-Erweiterung) verarbeitet werden — und welche nicht. **Apple App Review** und Nutzer können diese Seite als öffentliche Datenschutzerklärung heranziehen. Für App Store Connect: [Privacy Policy](../privacy) im Browser öffnen und die URL aus der Adressleiste kopieren (die öffentliche Domain kann sich ändern).

## Überblick (Apple Privacy Nutrition Label)

| Thema | Unser Vorgehen |
|-------|----------------|
| Konto | **Nicht erforderlich** — keine Registrierung, E-Mail oder Telefonnummer |
| Datenerfassung durch iHTC Studio | **Data Not Collected** — wir betreiben **kein** Backend, das personenbezogene Daten empfängt |
| Netzwerk | **Guides** nach Installation **offline** lesbar; **Wiedergabe** und **Song-ID** nutzen nach Freigabe Apple-Dienste |
| Analyse / Werbung / Tracking | **Keine** — keine Drittanbieter-Analytics, Werbung oder Tracking-SDKs; kein App Tracking Transparency |
| Optionale Apple-Dienste | **Apple Music / MusicKit**, **ShazamKit**, **iCloud** (private KVS), **Fotos (nur hinzufügen)** für Share Cards, optional **StoreKit**-Trinkgeld, **lokale Mitteilungen**, optionale **Live Activities** |

## Datenerfassung

Wir sammeln, verkaufen oder teilen **keine** personenbezogenen Daten zu Werbe- oder Analysezwecken.

- **Kein Konto** — alle mitgelieferten Guides ohne iHTC Studio-Konto nutzbar.
- **Keine Analyse oder Werbung** — keine Drittanbieter-Analytics-, Werbe- oder Crash-SDKs, die uns anrufen.
- **Kein Upload Ihrer Guides** — Favoriten, Listen, Später hören, Notizen, Verlauf und Einstellungen bleiben auf dem Gerät (optional **Ihre** iCloud); nichts geht an iHTC Studio-Server (**wir betreiben kein solches Backend für diese App**).
- **Kein Hosting von Musik** — keine Vollaudio-Dateien im Bundle. Abspielbare Treffer liefert **Apple Music**. Ohne Abo ggf. bis **30 s Katalog-Vorschau** lokal gecacht.

## Funktionsweise der App

- **Mitgelieferte Bibliothek** — Titelindex, Guides, Künstlernotizen, Kategorien, Sammlungen, Zitate, Tageskalender im App-/Widget-Bundle; Guides offline lesbar.
- **Apple Music (MusicKit)** — Nach Freigabe Abgleich mit kuratierter Katalogliste (ISRC zuerst, dann Künstler + Titel) und Wiedergabe über Apple Player. Abostatus bei Apple; Timeout = **unbekannt** (kein „nicht abonniert"-Hardcode). Artwork-URLs ggf. für Cover. Keine Apple-ID-/Zahlungsdaten bei uns.
- **30-Sekunden-Vorschau** — ohne Abo kann Apple-Vorschau in `Caches` landen (LRU, kein Volltrack). Kein Prefetch der nächsten Vorschau bei Mobilfunk/Niedrigenergie/Datensparmodus. Artwork- und Vorschau-Cache in Einstellungen löschbar, ohne Favoriten/Listen anzutasten.
- **Song-ID (ShazamKit)** — nur beim Öffnen von Recognize; Mikrofon verarbeitet **Apple**; keine Aufzeichnungsarchive. Treffer öffnet On-Device-Guide.
- **On-Device-Sprache** — Guide-Vorlesen via **AVSpeechSynthesizer**; Text nicht an iHTC Studio.
- **Widget & App Group** — `group.com.iHTCboy.iMusic` teilt Einstellungen; Live-Activity-Artwork kleines JPEG + Token.
- **Tägliche Mitteilungen** — lokal geplant; Tap → Deep Link zur Titel-ID.
- **Share Cards** — On-Device-Rendering; **Fotos nur hinzufügen** beim Speichern.
- **Optionales Trinkgeld** — **StoreKit**-Verbrauchsartikel.
- **Optionales Spotlight** — **standardmäßig aus**; wenn an, indexiert das System On-Device.

## Auf dem Gerät gespeicherte Daten

| Daten | Ort | Zweck |
|------|-------|---------|
| Guide-Bibliothek (Index + Shards) | App-/Widget-Bundle | Offline-Lesen |
| Favoriten, Listen, Später hören | App Group UserDefaults | Ihre Listen |
| Notizen, Verlauf, Vorlese-Fortschritt | App Group UserDefaults | Fortsetzen |
| Streak / Check-in | App Group UserDefaults | Tägliche Gewohnheit |
| Erscheinungsbild, Sprache, Tabs | App Group UserDefaults | Einstellungen |
| Daily Piece Cache & Mitteilungen | App Group UserDefaults | Heutige ID & Plan |
| Share-Card-Einstellungen | App Group UserDefaults | Letzter Stil |
| Artwork-URLs & decodierte Bilder | App Group + Cache | Cover; Prefetch nach MusicKit-Freigabe |
| 30-S-Vorschaudateien | App Caches | Offline nach erstem Treffer |
| Live-Activity-Thumbnail | App Group JPEG + Token | Lock Screen / Dynamic Island beim **Vorlesen** |
| MusicKit / Shazam-Freigabe | System | Merken Ihrer Wahl |
| Onboarding & Bewertungs-Prompt | Gerät UserDefaults | Willkommen / Review |

Deinstallation entfernt Sandbox und App Group (iOS/macOS-Regeln). Optionale iCloud-Kopien bleiben in **Ihrer** iCloud. Apple-Music-Bibliothek und Abo bleiben bei Apple.

## iCloud-Sync (optional)

Mit **iCloud Sync** in Einstellungen spiegelt **`NSUbiquitousKeyValueStore`** unter **Ihrer Apple-ID**:

- Favoriten, Listen, Später hören, Notizen, Hör-/Leseverlauf, Vorlese-Fortschritt, Streaks

Guide-Texte sind bereits im App-Bundle. Artwork-Dateien und Vorschau-Audio **nicht** per KVS. Traffic nur zu **Apple iCloud**, nicht über iHTC Studio. Abschaltbar; wir lesen Ihre iCloud nicht.

## Berechtigungen

| Berechtigung | Wann | Warum |
|------------|------|-----|
| **Apple Music / Mediathek** | MusicKit-Erklärung oder Wiedergabe-Tap | Abgleich & Play; Cover |
| **Mikrofon** | Song-ID öffnen | Umgebungsmusik erkennen |
| **Mitteilungen** | Daily-Piece-Erinnerung | Lokal geplant |
| **Fotos (nur hinzufügen)** | Musik-Karte speichern | Gerendertes Bild; keine Volllibrary-Lese |
| **iCloud** | Sync aktivieren | Listen/Notizen/Verlauf/Streaks |
| **Live Activities (iOS)** | Reading Live Activity (Standard an) | Guide beim **Vorlesen** auf Sperrbildschirm |
| **Hintergrundaudio** | Option an | MusicKit/Vorschau/TTS im Hintergrund |

Keine Kontakte, präzise Ortung, Kamera oder Tracking. Kein **Lesen** der Fotomediathek.

## Was wir nicht tun

- Kein Verkauf personenbezogener Daten oder Werbeprofile
- Kein erzwungenes Konto oder Social Login
- Keine werbe-/analyseorientierten Drittanbieter-SDKs
- Keine Volltracks auf Gerät oder unseren Servern
- Keine Speicherung von Shazam-Mikrofonpuffern nach Erkennung
- Keine Custom Dynamic Island für **Musikwiedergabe** — nur Guide-Vorlesen (wenn aktiv)
- Keine StoreKit-Kartennummern bei uns

## Datenschutz von Kindern

Keine absichtliche Erhebung bei Kindern unter 13 (oder lokalem Alter). Kein Datensammel-Backend → keine Kinderprofile bei uns. Apple Music & Shazam unterliegen Apples Regeln.

## Drittanbieter

- **Apple** — App Store, MusicKit, ShazamKit, StoreKit, iCloud KVS, TTS, Teilen, Mitteilungen, Live Activities, Siri/Shortcuts
- **Keine** weiteren datensammelnden Drittanbieter-SDKs

## Internationale Nutzer

Guides offline auf dem Gerät. Apple Music, Shazam, iCloud unterliegen Apples Bedingungen und Regionalverfügbarkeit. Katalog-Abgleich hängt von der Storefront der angemeldeten Apple-ID ab.

## Aufbewahrung & Löschung

- **Gerät** — Artwork/Vorschau-Cache unter **Einstellungen → Speicher**; Deinstallation löscht Sandbox/App Group.
- **iCloud (optional)** — bleibt in **Ihrer** iCloud bis Sie Sync aus oder Apple-Tools nutzen.
- **iHTC Studio** — kein serverseitiges Konto zum Löschen.

## Änderungen

Wir können diese Richtlinie aktualisieren; „Zuletzt aktualisiert" oben ändert sich.

## Kontakt

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Antwort in der Regel innerhalb von 48 Stunden.

</section>
<section lang="fr" markdown="1">

**Dernière mise à jour :** 9 septembre 2026

iHTC Studio (« nous ») a développé **iMusic** (« 爱音乐 » / « 愛音樂 », Bundle ID `com.iHTCboy.iMusic`). Cette page explique quelles données sont (ou ne sont pas) traitées lorsque vous utilisez l'app et son extension widget. **Apple App Review** et les utilisateurs peuvent s'y référer comme politique de confidentialité publique. Pour App Store Connect : ouvrez cette [Politique de confidentialité](../privacy) dans le navigateur et copiez l'URL (le domaine public peut changer).

## Résumé (alignement Apple Privacy Nutrition Label)

| Sujet | Notre pratique |
|-------|----------------|
| Compte | **Non requis** — pas d'inscription, e-mail ou téléphone |
| Collecte par iHTC Studio | **Data Not Collected** — nous n'exploitons **pas** de backend recevant des données personnelles |
| Réseau | **Guides** lisibles **hors ligne** après installation ; **lecture** et **identification** utilisent les services Apple après autorisation |
| Analyse / pub / suivi | **Aucun** — pas de SDK analytics, publicité ou tracking tiers ; pas d'App Tracking Transparency |
| Services Apple optionnels | **Apple Music / MusicKit**, **ShazamKit**, **iCloud** (KVS privé), **Photothèque (ajout uniquement)** pour cartes de partage, pourboire **StoreKit** optionnel, **notifications locales**, **Live Activities** optionnelles |

## Collecte de données

Nous ne collectons, vendons ni partageons de données personnelles à des fins publicitaires ou analytiques.

- **Sans compte** — tous les guides fournis sont utilisables sans compte iHTC Studio.
- **Sans analyse ni publicité** — pas de SDK analytics, pub ou crash tiers nous contactant.
- **Pas d'envoi de vos guides** — favoris, listes, « écouter plus tard », notes, historique et réglages restent sur l'appareil (et optionnellement **votre** iCloud), jamais vers nos serveurs (**nous n'exploitons pas un tel backend pour cette app**).
- **Pas d'hébergement musical** — pas de fichiers audio complets dans l'app. La lecture correspondante est fournie par **Apple Music**. Sans abonnement, jusqu'à **30 s d'aperçu catalogue** peuvent être mis en cache localement.

## Fonctionnement de l'app

- **Bibliothèque incluse** — index, guides, notes d'artistes, catégories, collections, citations, calendrier quotidien dans le bundle app/widget ; guides sans réseau.
- **Apple Music (MusicKit)** — après autorisation, correspondance avec le catalogue (ISRC d'abord, puis artiste + titre) et lecture via le lecteur Apple. Statut d'abonnement auprès d'Apple ; délai dépassé = **inconnu** (pas de « non abonné » forcé). URLs d'illustrations pour les pochettes. Pas d'Apple ID ni de paiement chez nous.
- **Aperçu 30 s** — sans abonnement, l'aperçu Apple peut être stocké dans `Caches` (LRU, pas la piste complète). Pas de préchargement de l'aperçu suivant en cellulaire / économie d'énergie / données réduites. Cache artwork et aperçu effaçable dans Réglages sans toucher favoris/listes.
- **Identification (ShazamKit)** — uniquement à l'ouverture de Recognize ; micro traité par **Apple** ; pas d'archives d'enregistrement. Un hit ouvre le guide sur l'appareil.
- **Synthèse vocale locale** — lecture des guides via **AVSpeechSynthesizer** ; texte non envoyé à iHTC Studio.
- **Widget & App Group** — `group.com.iHTCboy.iMusic` partage les réglages ; artwork Live Activity = petit JPEG + jeton.
- **Notifications quotidiennes** — planification locale ; toucher → deep link vers l'ID du morceau.
- **Cartes de partage** — rendu sur l'appareil ; **Photothèque ajout uniquement** à l'enregistrement.
- **Pourboire optionnel** — consommable **StoreKit**.
- **Spotlight optionnel** — **désactivé par défaut** ; si activé, indexation par le système sur l'appareil.

## Données stockées sur l'appareil

| Donnée | Emplacement | Objectif |
|------|-------|---------|
| Bibliothèque de guides | Bundle app/widget | Lecture hors ligne |
| Favoris, listes, plus tard | App Group UserDefaults | Vos listes |
| Notes, historique, progression lecture | App Group UserDefaults | Reprise |
| Séries / check-in | App Group UserDefaults | Habitude quotidienne |
| Apparence, langue, onglets | App Group UserDefaults | Réglages |
| Cache Daily Piece & notifications | App Group UserDefaults | ID du jour & planning |
| Réglages cartes de partage | App Group UserDefaults | Dernier style |
| URLs artwork & images décodées | App Group + cache | Pochettes ; prefetch après MusicKit |
| Fichiers aperçu 30 s | App Caches | Hors ligne après premier hit |
| Miniature Live Activity | App Group JPEG + jeton | Écran verrouillé / Dynamic Island pendant **lecture à voix haute** |
| Autorisations MusicKit / Shazam | Système | Mémorisation du choix |
| Onboarding & invite avis | UserDefaults appareil | Accueil / avis |

La désinstallation supprime sandbox et App Group (selon iOS/macOS). Les copies iCloud optionnelles restent dans **votre** iCloud. Bibliothèque et abonnement Apple Music restent chez Apple.

## Sync iCloud (optionnelle)

Avec **iCloud Sync** activé, **`NSUbiquitousKeyValueStore`** sous **votre Apple ID** reflète :

- Favoris, listes, plus tard, notes, historique d'écoute/lecture, progression de lecture à voix haute, séries

Le texte des guides est déjà dans le bundle. Pas de sync KVS pour fichiers artwork ni audio d'aperçu. Trafic vers **iCloud Apple** uniquement, pas via iHTC Studio. Désactivable ; nous ne lisons pas votre iCloud.

## Autorisations

| Autorisation | Quand | Pourquoi |
|------------|------|-----|
| **Apple Music / Médias** | Explication MusicKit ou lecture | Correspondance & lecture ; pochettes |
| **Microphone** | Ouvrir Song ID | Reconnaître la musique ambiante |
| **Notifications** | Rappel Daily Piece | Planification locale |
| **Photothèque (ajout)** | Enregistrer carte musique | Image rendue ; pas de lecture complète de la photothèque |
| **iCloud** | Activer la sync | Listes/notes/historique/séries |
| **Live Activities (iOS)** | Reading Live Activity (activé par défaut) | Guide à l'**écran verrouillé** pendant la lecture à voix haute |
| **Audio arrière-plan** | Option activée | MusicKit / aperçu / TTS en arrière-plan |

Pas de contacts, localisation précise, caméra ni tracking. Pas de **lecture** de photothèque.

## Ce que nous ne faisons pas

- Pas de vente de données ni de profils publicitaires
- Pas de compte imposé ni login social
- Pas de SDK tiers orientés collecte
- Pas de pistes complètes sur nos serveurs ou stockées pour nous
- Pas de conservation des tampons micro Shazam après reconnaissance
- Pas de Dynamic Island personnalisée pour **lecture musicale** — uniquement lecture de guide (si activée)
- Pas de numéros de carte StoreKit chez nous

## Enfants

Pas de collecte volontaire chez les moins de 13 ans (ou âge local). Pas de backend de collecte → pas de profils enfants chez nous. Apple Music et Shazam suivent les règles Apple.

## Tiers

- **Apple** — App Store, MusicKit, ShazamKit, StoreKit, iCloud KVS, TTS, partage, notifications, Live Activities, Siri/Raccourcis
- **Aucun** autre SDK tiers collectant des données

## Utilisateurs internationaux

Guides hors ligne sur l'appareil. Apple Music, Shazam, iCloud selon Apple. Correspondance catalogue selon la boutique de l'Apple ID connecté.

## Conservation & suppression

- **Appareil** — cache artwork/aperçu dans **Réglages → Stockage** ; désinstallation supprime sandbox/App Group.
- **iCloud (optionnel)** — reste dans **votre** iCloud jusqu'à désactivation ou outils Apple.
- **iHTC Studio** — aucun compte serveur à supprimer.

## Modifications

Nous pouvons mettre à jour cette politique ; la date « Dernière mise à jour » changera en tête de page.

## Contact

- **E-mail :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Réponse en général sous 48 h.

</section>
<section lang="tr" markdown="1">

**Son güncelleme:** 9 Eylül 2026

iHTC Studio («biz») **iMusic** («爱音乐» / «愛音樂», Bundle ID `com.iHTCboy.iMusic`) uygulamasını geliştirdi. Bu sayfa, uygulama ve widget uzantısı kullanılırken hangi verilerin işlendiğini (ve işlenmediğini) açıklar. **Apple App Review** ve kullanıcılar bunu herkese açık gizlilik politikası olarak kullanabilir. App Store Connect: [Privacy Policy](../privacy) sayfasını tarayıcıda açıp URL'yi kopyalayın (alan adı değişebilir).

## Özet (Apple Privacy Nutrition Label)

| Konu | Uygulamamız |
|-------|----------------|
| Hesap | **Gerekmez** — kayıt, e-posta, telefon yok |
| iHTC Studio veri toplama | **Data Not Collected** — kişisel veri alan backend **yok** |
| Ağ | **Rehberler** kurulumdan sonra **çevrimdışı**; **oynatma** ve **şarkı tanıma** izin sonrası Apple |
| Analitik/reklam/izleme | **Yok** — üçüncü taraf analytics/reklam/tracking SDK yok; ATT yok |
| İsteğe bağlı Apple | **Apple Music/MusicKit**, **ShazamKit**, **iCloud** (private KVS), paylaşım kartları için **Fotoğraflar (yalnızca ekleme)**, **StoreKit** bahşiş, **yerel bildirimler**, **Live Activities** |

## Veri toplama

Reklam veya analiz için kişisel veri **toplamıyor**, satmıyor veya paylaşmıyoruz.

- **Hesap yok** — iHTC Studio hesabı olmadan tüm rehberler.
- **Analitik/reklam yok** — bizi arayan üçüncü taraf SDK yok.
- **Rehber yükleme yok** — favoriler, listeler, notlar, geçmiş, ayarlar cihazda (isteğe bağlı **sizin** iCloud); iHTC Studio sunucularına gitmez (**böyle bir backend yok**).
- **Müzik barındırma yok** — tam ses dosyası yok; eşleşen oynatma **Apple Music**; abonelik yoksa **30 sn önizleme** önbelleği.

## Uygulama nasıl çalışır

- **Gömülü kütüphane** — dizin, rehberler, sanatçı notları, kategoriler, koleksiyonlar, bundle içinde; rehberler çevrimdışı.
- **Apple Music (MusicKit)** — ISRC öncelikli eşleme ve Apple oynatıcı; abonelik durumu Apple'a sorulur.
- **30 sn önizleme** — `Caches`; hücresel/düşük güç modunda sonraki önizleme önceden yüklenmez.
- **ShazamKit** — yalnızca Recognize açıkken; mikrofon **Apple** tarafından işlenir.
- **Cihaz içi konuşma** — **AVSpeechSynthesizer**; metin iHTC Studio'ya gitmez.
- **Widget & App Group** — `group.com.iHTCboy.iMusic`
- **Günlük bildirimler** — yerel zamanlama.
- **Paylaşım kartları** — cihazda render; **yalnızca ekleme**.

## Cihazda saklanan veriler

Favoriler, listeler, notlar, geçmiş, streak, ayarlar, Daily Piece önbelleği, artwork URL'leri, 30 sn dosyaları, Live Activity küçük resmi — App Group / bundle / Caches (JA/EN tablosuyla aynı kapsam).

Kaldırma sandbox ve App Group'u siler; isteğe bağlı iCloud **sizin** iCloud'unuzda kalır.

## iCloud (isteğe bağlı)

**iCloud Sync** açıkken **`NSUbiquitousKeyValueStore`** favoriler, listeler, notlar, geçmiş, streak yansıtır; rehber metni zaten bundle'da; artwork/önizleme KVS ile senkronize edilmez.

## İzinler

Apple Music, mikrofon, bildirimler, Fotoğraflar (ekleme), iCloud, Live Activities, arka plan sesi — yalnızca ilgili özellik açıkken. Kişiler, hassas konum, kamera, tracking **yok**.

## Yapmadıklarımız

Veri satışı yok; zorunlu hesap yok; veri toplama SDK'sı yok; tam parça sunucuda yok; Shazam tamponu saklanmaz; **müzik çalma** için özel Dynamic Island yok — yalnızca rehber okuma.

## Çocuklar / üçüncü taraflar / uluslararası / silme

Kasıtlı çocuk verisi yok; veri toplama backend'i yok. **Apple** hizmet sağlayıcı. Önbellek **Ayarlar → Depolama**'dan silinir.

## Değişiklikler

Politika güncellenebilir; üstteki tarih değişir.

## İletişim

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Genelde 48 saat içinde yanıt.

</section>
