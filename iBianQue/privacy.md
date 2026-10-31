---
layout: doc
title: iBianQue — Privacy Policy
app_id: iBianQue
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iBianQue — offline Bian Que cultural workshop, Data Not Collected, cultural study not medical advice.
---

<section lang="en" markdown="1">

**Last updated:** September 19, 2026

iHTC Studio ("we", "us" or "our") built **iBianQue** (also known as "爱扁鹊 / 愛扁鵲", Bundle ID `com.iHTCboy.iBianQue`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on **this page** as the public privacy policy. For App Store Connect, open this Privacy Policy in your browser and copy the address from the address bar (the public site domain may change over time).

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration, email sign-in, or phone number |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your personal data |
| Network | Library, reading, recite, Que Study, widgets, and daily notifications work **offline** after install |
| Analytics / ads / tracking | **None** — no third-party analytics, advertising, or tracking SDKs; no App Tracking Transparency use |
| Optional Apple services | **iCloud** (your private KVS), **Photo Library (Add Only)** for study cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional on-device **handwriting** (Vision) |

## Data Collection

We do **not** collect, sell, or share personal information for advertising or analytics.

- **No account** — You can use all core features without creating an account with us.
- **No analytics or ads** — The app binary does not integrate third-party analytics, advertising, or crash-reporting SDKs that phone home to us.
- **No content upload** — Your reading history, favorites, lists, notes, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

Four Examinations scenes, meridian atlas taps, and the on-device tongue color sketch stay local. They are cultural diagrams. They are **not** a diagnosis, prescription, or HealthKit integration.

## How the App Works

- **Bundled library** — Text JSON, vernacular/English, indexes, and study aids ship inside the app / widget bundle.
- **On-device speech** — Recitation uses Apple’s system **AVSpeechSynthesizer** (TTS). We do not send passage text to iHTC Studio.
- **Widgets & App Group** — Widgets and the app share preferences via App Group `group.com.iHTCboy.iBianQue` on your device.
- **Daily notifications** — Scheduled locally. Tapping a notification opens a deep link on device.
- **Study cards** — Images are rendered on device. Saving uses **Photo Library add-only** only when you tap save.
- **Handwriting search (iOS)** — Optional character recognition uses Apple **Vision** on device. Strokes are not uploaded.
- **Optional tip** — “Tip Developer” is a consumable **StoreKit** purchase processed by Apple.
- **Siri / Shortcuts / Control Center** — Optional system integrations open on-device deep links.
- **Optional Spotlight** — If you enable indexing, the system indexes content on device.

## Data Stored on Your Device

| Data | Where | Purpose |
|------|-------|---------|
| Bian Que / Nan Jing library | App / Widget bundle | Offline reading & study |
| Favorites & lists | App Group UserDefaults | Starred items and user lists |
| Reading history / last read | App Group UserDefaults | Continue reading |
| Notes | App Group UserDefaults | Reading notes you write |
| Study progress & mastery | App Group UserDefaults | Classroom / Hunt progress |
| Streak / check-in | App Group UserDefaults | Daily habit |
| Appearance & reading prefs | App Group UserDefaults | Theme, language, TTS, widgets |
| Daily Art cache & notification prefs | App Group UserDefaults | Today’s ID and schedule |
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

Sync traffic goes to **Apple iCloud**, not to iHTC Studio. We cannot read your iCloud contents.

## Permissions

iBianQue requests permissions only when a feature needs them:

| Permission | When | Why |
|------------|------|-----|
| Notifications | You enable Daily Art reminders | Local scheduling |
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

iBianQue is an educational literacy app for a general audience and is **not** in the Kids Category. We do not knowingly collect personal information from children. Families may use reading and study features offline on their own devices.

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

爱火腿肠工作室（iHTC Studio）（「我们」）开发了 **爱扁鹊**（iBianQue / 愛扁鵲，Bundle ID `com.iHTCboy.iBianQue`）。本隐私政策说明你在使用本应用时，数据如何被处理。本页可作为 **App Store 审核**与用户查阅的公开隐私政策。填写 App Store Connect 时：打开本站[隐私政策](../privacy)页，从浏览器地址栏复制当前网址（站点域名日后可能变更，请勿依赖写死的完整域名）。

## 摘要（对齐 Apple 隐私标签）

| 主题 | 我们的做法 |
|------|------------|
| 账号 | **不需要** — 无注册、邮箱登录或手机号 |
| iHTC Studio 数据采集 | **Data Not Collected** — 我们**不**运营接收你个人数据的后端 |
| 网络 | 语料、品读、诵读、鹊学堂、小组件与每日通知安装后均可**离线** |
| 分析 / 广告 / 追踪 | **无** — 无第三方分析、广告或追踪 SDK；不使用 ATT |
| 可选 Apple 服务 | **iCloud**（你的私人 KVS）、保存研读卡时的**照片图库（仅添加）**、可选 **StoreKit** 打赏、**本地通知**、可选**实时活动**、可选本机**手写识别** |

## 数据采集

我们**不**收集、出售或共享用于广告或分析的个人信息。

- **无账号** — 核心功能无需向我们注册。
- **无分析或广告** — 应用未集成会向我们回传的第三方分析、广告或崩溃 SDK。
- **无内容上传** — 阅读历史、收藏、清单、笔记、学习进度与偏好留在本机（并可选手动同步到**你的** iCloud）。

四诊馆情景、经络图谱点穴与舌象颜色示意均留在本机。它们是文化示意，**不是**诊断、处方，也不接入 HealthKit。

## 应用如何工作

- **内置语料** — 正文 JSON、白话／英译、索引与学习辅助随 App／小组件打包。
- **本机语音** — 诵读使用系统 **AVSpeechSynthesizer**。我们不会把正文发送到 iHTC Studio。
- **小组件与 App Group** — 通过本机 App Group `group.com.iHTCboy.iBianQue` 共享偏好。
- **每日通知** — 本地调度；点按后经深链打开本机篇目。
- **研读卡** — 在设备上渲染。仅在你点保存时使用**照片图库（仅添加）**。
- **手写寻句（iOS）** — 使用本机 Apple **Vision**。笔迹不会上传。
- **可选打赏** — Apple 处理的消耗型 **StoreKit** 购买。
- **Siri／快捷指令／控制中心** — 打开本机深链。
- **可选 Spotlight** — 由系统在本机索引。

## 本机存储的数据

| 数据 | 位置 | 用途 |
|------|------|------|
| 扁鹊与难经语料 | App／小组件 Bundle | 离线阅读与学习 |
| 收藏与清单 | App Group UserDefaults | 星标与用户清单 |
| 阅读历史／上次阅读 | App Group UserDefaults | 继续阅读 |
| 笔记 | App Group UserDefaults | 你写下的笔记 |
| 学习进度与掌握度 | App Group UserDefaults | 学堂／寻句进度 |
| 打卡／连续天数 | App Group UserDefaults | 每日习惯 |
| 外观与阅读偏好 | App Group UserDefaults | 主题、语言、TTS、小组件 |
| 今日一术缓存与通知偏好 | App Group UserDefaults | 今日 ID 与提醒 |
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

同步流量前往 **Apple iCloud**，而非 iHTC Studio。我们无法读取你的 iCloud 内容。

## 权限

仅在功能需要时请求：

| 权限 | 时机 | 原因 |
|------|------|------|
| 通知 | 你开启今日一术提醒 | 本地调度 |
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

爱扁鹊是面向一般读者的教育类语文应用，**不属于** Kids Category。我们不会故意收集儿童个人信息。家庭可在自有设备上离线使用阅读与学习功能。

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

愛火腿腸工作室（iHTC Studio）（「我們」）開發了 **愛扁鵲**（iBianQue / 爱扁鹊，Bundle ID `com.iHTCboy.iBianQue`）。本隱私政策說明你在使用本應用時，資料如何被處理。本頁可作為 **App Store 審核**與使用者查閱的公開隱私政策。填寫 App Store Connect 時：打開本站[隱私政策](../privacy)頁，從瀏覽器網址列複製目前網址（網站網域日後可能變更，請勿依賴寫死的完整網域）。

## 摘要（對齊 Apple 隱私標籤）

| 主題 | 我們的做法 |
|------|------------|
| 帳號 | **不需要** — 無註冊、電子郵件登入或手機號碼 |
| iHTC Studio 資料蒐集 | **Data Not Collected** — 我們**不**營運接收你個人資料的後端 |
| 網路 | 語料、品讀、誦讀、鵲學堂、小工具與每日通知安裝後均可**離線** |
| 分析 / 廣告 / 追蹤 | **無** — 無第三方分析、廣告或追蹤 SDK；不使用 ATT |
| 可選 Apple 服務 | **iCloud**（你的私人 KVS）、儲存研讀卡時的**照片（僅加入）**、可選 **StoreKit** 打賞、**本機通知**、可選**即時動態**、可選本機**手寫辨識** |

## 資料蒐集

我們**不**蒐集、出售或共享用於廣告或分析的個人資訊。

- **無帳號** — 核心功能無需向我們註冊。
- **無分析或廣告** — 應用未整合會向我們回傳的第三方分析、廣告或當機 SDK。
- **無內容上傳** — 閱讀歷史、收藏、清單、筆記、學習進度與偏好留在本機（並可選手動同步到**你的** iCloud）。

四診館情景、經絡圖譜點穴與舌象顏色示意均留在本機。它們是文化示意，**不是**診斷、處方，也不接入 HealthKit。

## 應用如何工作

- **內建語料** — 正文 JSON、白話／英譯、索引與學習輔助隨 App／小工具打包。
- **本機語音** — 誦讀使用系統 **AVSpeechSynthesizer**。我們不會把正文傳送到 iHTC Studio。
- **小工具與 App Group** — 透過本機 App Group `group.com.iHTCboy.iBianQue` 共享偏好。
- **每日通知** — 本機排程；點按後經深鏈打開本機篇目。
- **研讀卡** — 在裝置上渲染。僅在你點儲存時使用**照片（僅加入）**。
- **手寫尋句（iOS）** — 使用本機 Apple **Vision**。筆跡不會上傳。
- **可選打賞** — Apple 處理的消耗型 **StoreKit** 購買。
- **Siri／捷徑／控制中心** — 打開本機深鏈。
- **可選 Spotlight** — 由系統在本機建立索引。

## 本機儲存的資料

| 資料 | 位置 | 用途 |
|------|------|------|
| 扁鵲與難經語料 | App／小工具 Bundle | 離線閱讀與學習 |
| 收藏與清單 | App Group UserDefaults | 星號與使用者清單 |
| 閱讀歷史／上次閱讀 | App Group UserDefaults | 繼續閱讀 |
| 筆記 | App Group UserDefaults | 你寫下的筆記 |
| 學習進度與掌握度 | App Group UserDefaults | 學堂／尋句進度 |
| 打卡／連續天數 | App Group UserDefaults | 每日習慣 |
| 外觀與閱讀偏好 | App Group UserDefaults | 主題、語言、TTS、小工具 |
| 今日一術快取與通知偏好 | App Group UserDefaults | 今日 ID 與提醒 |
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

同步流量前往 **Apple iCloud**，而非 iHTC Studio。我們無法讀取你的 iCloud 內容。

## 權限

僅在功能需要時請求：

| 權限 | 時機 | 原因 |
|------|------|------|
| 通知 | 你開啟今日一術提醒 | 本機排程 |
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

愛扁鵲是面向一般讀者的教育類語文應用，**不屬於** Kids Category。我們不會故意蒐集兒童個人資訊。家庭可在自有裝置上離線使用閱讀與學習功能。

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
<section lang="ja" markdown="1">

**最終更新日:** 2026年9月19日

iHTC Studio（「当社」、「私たち」または「私たちの」）は **iBianQue**（「爱扁鹊 / 愛扁鵲」とも呼ばれる、バンドルID `com.iHTCboy.iBianQue`）を開発しました。このプライバシーポリシーは、アプリを使用する際にどのデータが取り扱われるか（および取り扱われないか）を説明します。**Apple App Review**やユーザーは、**このページ**を公開されているプライバシーポリシーとして参照することができます。App Store Connect用には、このプライバシーポリシーをブラウザで開き、アドレスバーからアドレスをコピーしてください（公開サイトのドメインは時間とともに変更される場合があります）。

## 概要（Appleプライバシー栄養ラベルとの整合性）

| トピック | 当社の実践 |
|-------|----------------|
| アカウント | **不要** — 登録、メールサインイン、電話番号は必要ありません |
| iHTC Studioによるデータ収集 | **データは収集されません** — 当社はあなたの個人データを受信するバックエンドを**運営していません** |
| ネットワーク | ライブラリ、読書、暗唱、Que Study、ウィジェット、毎日の通知はインストール後**オフライン**で動作します |
| 分析 / 広告 / トラッキング | **なし** — サードパーティの分析、広告、トラッキングSDKはありません; App Tracking Transparencyは使用しません |
| 任意のAppleサービス | **iCloud**（あなたのプライベートKVS）、**写真ライブラリ（追加のみ）**（学習カード用）、**StoreKit**（任意のチップ用）、**ローカル通知**、任意の**ライブアクティビティ**、任意のデバイス上での**手書き入力**（Vision） |

## データ収集

当社は個人情報を広告や分析のために**収集、販売、共有**しません。

- **アカウント不要** — アカウントを作成しなくても、すべての基本機能を使用できます。
- **分析や広告なし** — アプリのバイナリには、第三者の分析、広告、クラッシュレポートSDKは統合されておらず、データが私たちに送信されることはありません。
- **コンテンツアップロードなし** — あなたの閲覧履歴、お気に入り、リスト、メモ、学習進捗、設定はデバイス上（必要に応じて**あなたの**iCloudにも）に留まります。これらはiHTC Studioのサーバーにアップロードされることはありません。**このアプリのためにサーバーを運用していないからです。**

四検査のシーン、経絡アトラスのタップ、そしてデバイス上の舌の色スケッチはローカルに保持されます。これらは文化的な図であり、**診断、処方、HealthKit統合ではありません**。

## アプリの使い方

- **バンドルされたライブラリ** — テキスト JSON、現地語/英語、インデックス、および学習支援機能がアプリ / ウィジェット バンドル内に同梱されています。 
- **オンデバイス音声** - 朗読には Apple のシステム **AVSpeechSynthesizer** (TTS) が使用されます。 iHTC Studio には文章テキストは送信されません。 
- **ウィジェットとアプリ グループ** - ウィジェットとアプリは、デバイス上のアプリ グループ `group.com.iHTCboy.iBianQue` を介して設定を共有します。 
- **毎日の通知** — ローカルでスケジュールされます。 通知をタップすると、デバイス上でディープリンクが開きます。 
- **学習カード** — 画像はデバイス上でレンダリングされます。 保存すると、[保存] をタップした場合にのみ **フォト ライブラリの追加のみ**が使用されます。 
- **手書き検索 (iOS)** - オプションの文字認識では、デバイス上の Apple **Vision** を使用します。 ストロークはアップロードされません。 
- **オプションのチップ** - 「チップ開発者」は、Apple によって処理される消耗品 **StoreKit** の購入です。 
- **Siri / ショートカット / コントロール センター** — オプションのシステム統合により、デバイス上のディープ リンクが開きます。 
- **オプションのスポットライト** — インデックス作成を有効にすると、システムはデバイス上のコンテンツにインデックスを付けます。 

## デバイスに保存されているデータ

| データ | どこ | 目的 |
 |------|-------|-----------|
 | Bian Que / Nan Jing 図書館 | アプリ/ウィジェットバンドル | オフラインでの読書と学習 |
 | お気に入りとリスト | アプリグループのUserDefaults | スター付きアイテムとユーザーリスト |
 | 読書履歴 / 最後に読んだ | アプリグループのUserDefaults | 続きを読む |
 | メモ | アプリグループのUserDefaults | あなたが書いた読書メモ |
 | 学習の進捗と習熟度 | アプリグループのUserDefaults | 教室/狩りの進行状況 |
 | 連続記録 / チェックイン | アプリグループのUserDefaults | 日々の習慣 |
 | 外観と読み取り設定 | アプリグループのUserDefaults | テーマ、言語、TTS、ウィジェット |
 | Daily Art のキャッシュと通知の設定 | アプリグループのUserDefaults | 今日のIDとスケジュール |
 | カードの好み | アプリグループのUserDefaults | 最後のスタイル/比率 |
 | オンボーディングと TipKit の状態 | 標準の UserDefaults | ウェルカムガイド |
 | ウィジェット / ライブ アクティビティのスナップショット | アプリグループ / ActivityKit | すでに開いているテキストを表示 |

 アプリをアンインストールすると、サンドボックスとアプリ グループのデータが削除されます (OS の動作に依存します)。 オプションの iCloud コピーは、クリアするまで **あなたの** iCloud に残ります。 

## iCloud 同期 (オプション)

設定で **iCloud 同期**を有効にすると、アプリは **Apple ID** に関連付けられた Apple の **`NSUbiquitousKeyValueStore`** を通じて選択したユーザー データをミラーリングします。 

- お気に入り
 - リスト
 - 読書履歴
 - 学習の進捗/習熟度
 - 連続記録を練習する
 - 注意事項

 同期トラフィックは iHTC Studio ではなく **Apple iCloud** に送信されます。 iCloud のコンテンツを読み取ることができません。 

## 権限

 iBianQue は、機能が必要な場合にのみアクセス許可を要求します。 

| 許可 | いつ | なぜ |
 |-----------|------|-----|
 | お知らせ | Daily Art リマインダーを有効にします | ローカルスケジュール |
 | フォトライブラリ（追加のみ） | カードを保存します | レンダリングされたイメージを書き込む |
 | iCloud | 同期を有効にする | お気に入り/リスト/履歴/進行状況/メモを同期 |
 | ライブアクティビティ (iOS) | ライブ アクティビティの読み取りを有効にします | ロック画面にパッセージを表示 / ダイナミックアイランド |
 | バックグラウンドオーディオ (機能) | バックグラウンド朗読を有効にします | バックグラウンドで TTS を続行 |

 当社は、連絡先、正確な位置情報、カメラ、マイク (システムの TTS 再生を超える)、または追跡を要求しません**。 

## 私たちがやらないこと

- 当社は個人データを**販売しません**。 
- 当社は広告プロフィールを構築しません**。 
- アカウントやソーシャル ログインは**必要ありません**。 
- データ収集のためにサードパーティの広告、分析、ソーシャル SDK を埋め込むことは**ありません**。 
- カードの保存を選択した場合、**追加のみ**を超えてフォト ライブラリにアクセスすることは**ありません**。 
- 当社は StoreKit 支払いカード番号を**受け取りません** (Apple は支払いを処理します)。 

## 子供のプライバシー

 iBianQue は一般向けの読み書き教育アプリであり、キッズ カテゴリには含まれません**。 当社は故意に子供から個人情報を収集しません。 家族は各自のデバイスでオフラインで読書および学習機能を使用できます。 

## サードパーティ

 - **Apple** — App Store ディストリビューション、オプションの StoreKit、オプションの iCloud KVS、システム TTS、選択した共有シートの宛先、および OS レベルの通知 / ライブ アクティビティ / Siri / ショートカット / ビジョン配信。 
- **広告、分析、ソーシャル ログイン用の他のサードパーティ SDK** はデータ収集には含まれません。 

## 海外ユーザー

 アプリはデバイス上でオフラインで機能するように設計されています。 オプションの Apple サービスは、Apple の規約と利用可能な地域に従います。 

## データの保持と削除

- **デバイス上** — アプリを削除すると、ローカルのサンドボックスおよびApp Groupデータが削除されます（OSの動作によります）。
- **iCloud** — 同期をオフにし、必要に応じてiCloudアカウントから関連するキーを削除してください。iCloudの内容をこちらで消去することはできません。
- **当社は何も保持しません** — このアプリに関してiHTC Studioのサーバー上にデータを収集していません。

## ポリシーの変更

本プライバシーポリシーは更新される場合があります。上部の「最終更新日」が変更されます。更新後も継続して利用する場合、改訂されたポリシーに同意したものとみなされます。

## お問い合わせ

プライバシーに関するご質問: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ko" markdown="1">

**마지막 업데이트:** 2026년 9월 19일

iHTC Studio(“우리”, “저희” 또는 “당사”)는 **iBianQue**(또는 “爱扁鹊 / 愛扁鵲”, 번들 ID `com.iHTCboy.iBianQue`)를 개발했습니다. 이 개인정보 보호정책은 앱 사용 시 처리되는(또는 처리되지 않는) 데이터에 대해 설명합니다. **Apple 앱 심사** 및 사용자는 **이 페이지**를 공개 개인정보 보호정책으로 참고할 수 있습니다. App Store Connect에서는 브라우저에서 이 개인정보 보호정책을 열고 주소 표시줄에서 주소를 복사하세요(공개 사이트 도메인은 시간이 지남에 따라 변경될 수 있습니다).

## 요약(Apple 개인정보 영양 라벨 정렬)

| 주제 | 우리의 실천 |
|-------|----------------|
| 계정 | **필요 없음** — 등록, 이메일 로그인, 전화번호 불필요 |
| iHTC 스튜디오의 데이터 수집 | **데이터 수집 없음** — 개인 데이터를 받는 백엔드를 운영하지 않습니다 |
| 네트워크 | 라이브러리, 읽기, 암기, Que Study, 위젯, 일일 알림은 설치 후 **오프라인**에서 작동 |
| 분석 / 광고 / 추적 | **없음** — 타사 분석, 광고, 추적 SDK 없음; 앱 추적 투명성(App Tracking Transparency) 사용 없음 |
| 선택적 Apple 서비스 | **iCloud** (개인 KVS), 학습 카드용 **사진 라이브러리(추가만 가능)**, 선택적 팁용 **StoreKit**, **로컬 알림**, 선택적 **Live Activities**, 선택적 기기 내 **손글씨**(Vision) |

## 데이터 수집

저희는 광고나 분석을 위해 개인 정보를 **수집, 판매, 공유하지 않습니다**.

- **계정 필요 없음** — 계정을 만들지 않고도 모든 기본 기능을 사용할 수 있습니다.
- **분석 및 광고 없음** — 앱 바이너리는 타사 분석, 광고 또는 크래시 리포트 SDK를 통합하지 않으며, 우리에게 데이터를 전송하지 않습니다.
- **콘텐츠 업로드 없음** — 읽기 기록, 즐겨찾기, 목록, 노트, 학습 진행 상황 및 설정은 기기 내에만 저장되며(선택적으로 **본인의** iCloud에 저장 가능), iHTC Studio 서버로 절대 업로드되지 않습니다. **이 앱을 위해 서버를 운영하지 않기 때문입니다.**

네 가지 검사 장면, 경락 지도 탭, 기기 내 혀 색상 스케치는 로컬에 남아 있습니다. 이는 문화적 다이어그램일 뿐, 진단, 처방, HealthKit 통합이 아닙니다.

## 앱 작동 방식

- **번들 라이브러리** — 텍스트 JSON, 모국어/영어, 색인 및 학습 보조 자료가 앱/위젯 번들 내에 포함되어 있습니다. 
- **기기 내 음성** — 암송은 Apple 시스템 **AVSpeechSynthesizer**(TTS)를 사용합니다. iHTC Studio에는 문구 텍스트를 보내지 않습니다. 
- **위젯 및 앱 그룹** — 위젯과 앱은 기기의 앱 그룹 `group.com.iHTCboy.iBianQue`을(를) 통해 기본 설정을 공유합니다. 
- **매일 알림** — 로컬로 예약됩니다. 알림을 탭하면 기기에서 딥 링크가 열립니다. 
- **학습 카드** — 이미지가 장치에서 렌더링됩니다. 저장은 저장을 탭한 경우에만 **사진 라이브러리 추가 전용**을 사용합니다. 
- **필기 검색(iOS)** — 선택적 문자 인식은 장치에서 Apple **Vision**을 사용합니다. 스트로크는 업로드되지 않습니다. 
- **선택적 팁** — "팁 개발자"는 Apple에서 처리하는 소모품 **StoreKit** 구매입니다. 
- **Siri / 바로가기 / 제어 센터** — 선택적 시스템 통합으로 기기 내 딥 링크가 열립니다. 
- **선택적 스포트라이트** — 인덱싱을 활성화하면 시스템이 장치의 콘텐츠를 인덱싱합니다. 

## 귀하의 기기에 저장된 데이터

| 데이터 | 어디 | 목적 | 
|------|-------|---------| 
| Bian Que / Nan Jing 도서관 | 앱/위젯 번들 | 오프라인 독서 및 학습 | 
| 즐겨찾기 및 목록 | 앱 그룹 UserDefaults | 별표 표시된 항목 및 사용자 목록 | 
| 읽은 이력/마지막 읽은 내용 | 앱 그룹 UserDefaults | 계속 읽기 | 
| 메모 | 앱 그룹 UserDefaults | 당신이 쓴 메모 읽기 | 
| 학습 진행 및 숙달 | 앱 그룹 UserDefaults | 교실/사냥 진행 | 
| 연속/체크인 | 앱 그룹 UserDefaults | 일상습관 | 
| 모양 및 읽기 기본 설정 | 앱 그룹 UserDefaults | 테마, 언어, TTS, 위젯 | 
| 일일 아트 캐시 및 알림 환경설정 | 앱 그룹 UserDefaults | 오늘의 아이디와 일정 | 
| 카드 환경설정 | 앱 그룹 UserDefaults | 마지막 스타일/비율 | 
| 온보딩 및 TipKit 상태 | 표준 사용자 기본값 | 환영 가이드 | 
| 위젯/실시간 활동 스냅샷 | 앱 그룹/ActivityKit | 이미 열어본 텍스트 표시 | 

앱을 제거하면 샌드박스 및 앱 그룹 데이터가 제거됩니다(OS 동작에 따라 다름). 선택적인 iCloud 사본은 귀하가 삭제할 때까지 **귀하의** iCloud에 남아 있습니다. 

## iCloud 동기화(선택사항)

설정에서 **iCloud 동기화**를 활성화하면 앱은 **Apple ID**에 연결된 Apple의 **`NSUbiquitousKeyValueStore`**를 통해 선택한 사용자 데이터를 미러링합니다. 

- 즐겨찾기 
- 목록 
- 독서 이력 
- 학습 진행/숙달 
- 연습 연속 
- 메모 

동기화 트래픽은 iHTC Studio가 아닌 **Apple iCloud**로 이동합니다. 귀하의 iCloud 콘텐츠를 읽을 수 없습니다. 

## 권한 

iBianQue는 기능에 필요한 경우에만 권한을 요청합니다. 

| 허가 | 언제 | 왜 | 
|------------|------|----| 
| 알림 | Daily Art 알림을 활성화합니다 | 지역 일정 | 
| 사진 라이브러리(추가 전용) | 당신은 카드를 저장 | 렌더링된 이미지 쓰기 | 
| 아이클라우드 | 동기화를 활성화 | 즐겨찾기/목록/기록/진행상황/메모 동기화 | 
| 라이브 활동(iOS) | 실시간 활동 읽기 | 잠금화면 / 다이내믹 아일랜드 | 
| 배경 오디오(기능) | 배경 암송을 활성화합니다 | 백그라운드에서 TTS 계속 | 

우리는 연락처, 정확한 위치, 카메라, 마이크(시스템 TTS 재생 이외) 또는 추적을 요청하지 **않습니다**. 

## 우리가 하지 않는 일

- 당사는 개인 데이터를 판매하지 **않습니다**. 
- 우리는 광고 프로필을 작성하지 **않습니다**. 
- 계정이나 소셜 로그인이 필요하지 **않습니다**. 
- 당사는 데이터 수집을 위해 제3자 광고, 분석 또는 소셜 SDK를 삽입하지 **않습니다**. 
- 귀하가 카드를 저장하기로 선택한 경우 **추가 전용** 이외의 사진 라이브러리에는 액세스하지 **않습니다**. 
- 저희는 StoreKit 결제 카드 번호를 받지 **않습니다**(Apple에서 결제를 처리함). 

## 아동 개인정보 보호 

iBianQue는 일반 청중을 위한 교육용 읽기 쓰기 앱이며 어린이 카테고리에 **아닙니다**. 우리는 어린이로부터 고의로 개인정보를 수집하지 않습니다. 가족은 자신의 기기에서 오프라인으로 독서 및 학습 기능을 사용할 수 있습니다. 

## 제3자 

- **Apple** — App Store 배포, 선택적 StoreKit, 선택적 iCloud KVS, 시스템 TTS, 선택한 공유 시트 대상 및 OS 수준 알림/실시간 활동/Siri/바로가기/비전 전달. 
- 광고, 분석 또는 소셜 로그인을 위한 **다른 타사 SDK**는 데이터 수집에 포함되지 않습니다. 

## 해외 사용자 

이 앱은 귀하의 기기에서 오프라인으로 작동하도록 설계되었습니다. 선택적 Apple 서비스는 Apple의 약관 및 지역별 이용 가능 여부를 따릅니다. 

## 데이터 보관 및 삭제

- **기기 내** — 앱을 삭제하여 로컬 샌드박스 및 앱 그룹 데이터를 제거합니다(운영 체제 동작에 따라 다를 수 있음).  
- **iCloud** — 동기화를 끄고 필요에 따라 iCloud 계정에서 관련 키를 삭제합니다. iCloud 데이터를 직접 삭제할 수는 없습니다.  
- **저희는 아무것도 보관하지 않습니다** — iHTC Studio 서버에는 이 앱과 관련된 데이터를 수집하지 않기 때문에 저장하지 않습니다.

## 정책 변경

저희는 이 개인정보 처리방침을 업데이트할 수 있습니다. 상단에 있는 “마지막 업데이트” 날짜가 변경됩니다. 업데이트 이후에도 계속 사용하면 수정된 정책에 동의하는 것으로 간주됩니다.

## 연락처

개인정보 관련 문의: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ru" markdown="1">

**Последнее обновление:** 19 сентября 2026 года

iHTC Studio («мы», «нас» или «наш») создало **iBianQue** (также известное как «爱扁鹊 / 愛扁鵲», Bundle ID `com.iHTCboy.iBianQue`). Настоящая Политика конфиденциальности объясняет, какие данные обрабатываются (и не обрабатываются) при использовании приложения. **Apple App Review** и пользователи могут полагаться на **эту страницу** в качестве публичной политики конфиденциальности. Для App Store Connect откройте эту Политику конфиденциальности в браузере и скопируйте адрес из адресной строки (домен публичного сайта может со временем изменяться).

## Краткое содержание (соответствие меткам конфиденциальности Apple)

| Тема | Наша практика |
|-------|----------------|
| Учетная запись | **Не требуется** — регистрация, вход по электронной почте или номеру телефона не нужны |
| Сбор данных iHTC Studio | **Данные не собираются** — мы **не** управляем серверной частью, которая получает ваши персональные данные |
| Сеть | Библиотека, чтение, заучивание, Que Study, виджеты и ежедневные уведомления работают **офлайн** после установки |
| Аналитика / реклама / отслеживание | **Нет** — нет сторонней аналитики, рекламы или SDK для отслеживания; не используется App Tracking Transparency |
| Опциональные сервисы Apple | **iCloud** (ваш личный KVS), **Фототека (только добавление)** для учебных карточек, **StoreKit** для опциональных чаевых, **локальные уведомления**, опционально **Live Activities**, опционально на устройстве **ручное письмо** (Vision) |

## Сбор данных

Мы **не** собираем, не продаем и не передаем персональную информацию для рекламы или аналитики.

- **Нет аккаунта** — Вы можете использовать все основные функции без создания аккаунта у нас.
- **Без аналитики и рекламы** — Бинарный файл приложения не интегрирует сторонние SDK для аналитики, рекламы или отчётов о сбоях, которые отправляют данные нам.
- **Без загрузки контента** — Ваша история чтения, избранное, списки, заметки, прогресс обучения и настройки остаются на вашем устройстве (и, при желании, в **вашем** iCloud). Они никогда не загружаются на серверы iHTC Studio, потому что **мы не используем такие серверы для этого приложения**.

Сцены «Четырех обследований», нажатия на атлас меридианов и эскиз цвета языка на устройстве остаются локальными. Это культурные диаграммы. Они **не** являются диагнозом, рецептом или интеграцией с HealthKit.

## Как работает приложение

- **Встроенная библиотека**. Текст в формате JSON, на местном/английском языке, указатели и учебные пособия поставляются в комплекте приложения/виджета. 
- **Речь на устройстве** — при декламации используется система Apple **AVSpeechSynthesizer** (TTS). Мы не отправляем текст прохождения в iHTC Studio. 
- **Виджеты и группа приложений** — виджеты и настройки приложения делятся через группу приложений `group.com.iHTCboy.iBianQue` на вашем устройстве. 
- **Ежедневные уведомления** — по расписанию. При нажатии на уведомление открывается глубокая ссылка на устройстве. 
- **Обучающие карточки** — изображения обрабатываются на устройстве. При сохранении используется **Дополнение «Библиотека фотографий»** только при нажатии «Сохранить». 
- **Поиск по рукописному вводу (iOS)** — дополнительное распознавание символов использует Apple **Vision** на устройстве. Штрихи не загружаются. 
- **Необязательный совет**. «Tip Developer» — это расходный материал, приобретаемый **StoreKit** и обрабатываемый Apple. 
- **Siri / Ярлыки / Центр управления** — дополнительные системные интеграции открывают глубокие ссылки на устройстве. 
- **Дополнительный Spotlight** — если вы включите индексирование, система будет индексировать контент на устройстве. 

## Данные, хранящиеся на вашем устройстве

| Данные | Где | Цель | 
|------|-------|---------| 
| Библиотека Бянь Цюэ / Нань Цзин | Пакет приложений и виджетов | Офлайн-чтение и изучение | 
| Избранное и списки | Пользовательские настройки группы приложений | Избранные элементы и списки пользователей | 
| История чтения / последнее чтение | Пользовательские настройки группы приложений | Продолжить чтение | 
| Заметки | Пользовательские настройки группы приложений | Чтение заметок, которые вы пишете | 
| Ход учебы и мастерство | Пользовательские настройки группы приложений | Прогресс в классе/охоте | 
| Полоса / регистрация | Пользовательские настройки группы приложений | Ежедневная привычка | 
| Настройки внешнего вида и чтения | Пользовательские настройки группы приложений | Тема, язык, TTS, виджеты | 
| Кэш ежедневных произведений искусства и настройки уведомлений | Пользовательские настройки группы приложений | Сегодняшний идентификатор и расписание | 
| Настройки карты | Пользовательские настройки группы приложений | Последний стиль/соотношение | 
| Регистрация и состояние TipKit | Стандартные пользовательские настройки | Приветственное руководство | 
| Виджет / Снимки активности в реальном времени | Группа приложений / ActivityKit | Показать текст, который вы уже открыли | 

При удалении приложения удаляются данные песочницы и группы приложений (в зависимости от поведения ОС). Дополнительные копии iCloud остаются в **вашем** iCloud, пока вы их не очистите. 

## Синхронизация с iCloud (необязательно)

Если вы включите **iCloud Sync** в настройках, приложение зеркально отображает выбранные пользовательские данные через **`NSUbiquitousKeyValueStore`** Apple, привязанный к **вашему Apple ID**: 

- Избранное 
- Списки 
- Чтение истории 
- Прогресс в учебе/мастерстве 
- Практика полос 
- Примечания 

Трафик синхронизации поступает в **Apple iCloud**, а не в iHTC Studio. Мы не можем прочитать ваше содержимое iCloud. 

## Разрешения 

iBianQue запрашивает разрешения только тогда, когда они нужны функции: 

| Разрешение | Когда | Почему | 
|------------|------|-----| 
| Уведомления | Вы включаете напоминания Daily Art | Локальное планирование | 
| Библиотека фотографий (только добавление) | Вы сохраняете карту | Запишите визуализированное изображение | 
| iCloud | Вы включаете синхронизацию | Синхронизировать избранное/списки/историю/прогресс/заметки | 
| Живые мероприятия (iOS) | Вы включаете чтение активности в реальном времени | Показать прохождение на экране блокировки/Динамический остров | 
| Фоновый звук (возможность) | Вы включаете фоновое чтение | Продолжить TTS в фоновом режиме | 

Мы **не** запрашиваем контакты, точное местоположение, камеру, микрофон (кроме системного воспроизведения TTS) или отслеживание. 

## Чего мы не делаем

- Мы **не** продаем персональные данные. 
- Мы **не** создаем рекламные профили. 
- Нам **не** требуется учетная запись или вход в социальную сеть. 
– Мы **не** встраиваем сторонние рекламные, аналитические или социальные SDK для сбора данных. 
- Мы **не** получаем доступ к вашей библиотеке фотографий, кроме **только добавления**, когда вы решаете сохранить карту. 
- Мы **не** получаем номера платежных карт StoreKit (Apple обрабатывает платежи). 

## Конфиденциальность детей 

iBianQue — это образовательное приложение для широкой аудитории, которое **не** входит в категорию «Дети». Мы сознательно не собираем личную информацию от детей. Семьи могут использовать функции чтения и обучения в автономном режиме на своих устройствах. 

## Третьи стороны 

- **Apple** — распространение в App Store, дополнительный StoreKit, дополнительный iCloud KVS, системный TTS, выбранные вами места назначения Share Sheet, а также уведомления на уровне ОС / Live Activity / Siri / Ярлыки / Доставка Vision. 
- **Для сбора данных не включены никакие другие сторонние SDK** для рекламы, аналитики или входа в социальные сети. 

## Международные пользователи 

Приложение предназначено для работы в автономном режиме на вашем устройстве. Дополнительные услуги Apple соответствуют условиям Apple и региональной доступности. 

## Хранение и удаление данных

- **На устройстве** — Удалите приложение, чтобы удалить локальные данные песочницы и группы приложений (в зависимости от поведения ОС).  
- **iCloud** — Отключите синхронизацию и при необходимости удалите соответствующие ключи из вашей учетной записи iCloud; мы не можем стереть ваш iCloud за вас.  
- **Мы ничего не сохраняем** на серверах iHTC Studio для этого приложения, так как мы не собираем эти данные.

## Изменения политики

Мы можем обновлять эту Политику конфиденциальности. Дата «Последнего обновления» вверху будет изменяться. Продолжение использования после обновления означает, что вы принимаете обновленную политику.

## Контакт

Вопросы о конфиденциальности: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="th" markdown="1">

**อัปเดตล่าสุด:** 19 กันยายน 2026

iHTC Studio ("เรา", "พวกเรา" หรือ "ของเรา") สร้าง **iBianQue** (หรือที่รู้จักในชื่อ "爱扁鹊 / 愛扁鵲", Bundle ID `com.iHTCboy.iBianQue`) นโยบายความเป็นส่วนตัวนี้อธิบายว่าข้อมูลใดบ้างที่ถูก (และไม่ได้) จัดการเมื่อคุณใช้แอป **Apple App Review** และผู้ใช้สามารถพึ่งพา **หน้าหน้าเว็บนี้** เป็นนโยบายความเป็นส่วนตัวสาธารณะ สำหรับ App Store Connect ให้เปิดนโยบายความเป็นส่วนตัวนี้ในเว็บเบราว์เซอร์ของคุณและคัดลอกที่อยู่จากแถบที่อยู่ (โดเมนเว็บไซต์สาธารณะอาจมีการเปลี่ยนแปลงเมื่อเวลาผ่านไป)

## สรุป (การจัดแนวตามฉลากโภชนาการความเป็นส่วนตัวของ Apple)

| หัวข้อ | นโยบายการปฏิบัติของเรา |
|-------|----------------|
| บัญชี | **ไม่จำเป็น** — ไม่ต้องลงทะเบียน, เข้าสู่ระบบด้วยอีเมล หรือหมายเลขโทรศัพท์ |
| การเก็บข้อมูลโดย iHTC Studio | **ไม่ได้เก็บข้อมูล** — เรา **ไม่** ดำเนินการระบบหลังบ้านที่รับข้อมูลส่วนตัวของคุณ |
| เครือข่าย | หนังสือห้องสมุด, การอ่าน, การท่อง, Que Study, วิดเจ็ต, และการแจ้งเตือนประจำวันทำงานได้ **ออฟไลน์** หลังติดตั้ง |
| การวิเคราะห์ / โฆษณา / การติดตาม | **ไม่มี** — ไม่มีการวิเคราะห์โดยบุคคลที่สาม, โฆษณา, หรือ SDK การติดตาม; ไม่ใช้ App Tracking Transparency |
| บริการของ Apple ที่เลือกใช้ได้ | **iCloud** (KVS ส่วนตัวของคุณ), **คลังรูปภาพ (เพิ่มได้เท่านั้น)** สำหรับการ์ดศึกษา, **StoreKit** สำหรับการให้ทิปที่เลือกได้, **การแจ้งเตือนภายในเครื่อง**, **กิจกรรมสด (Live Activities)** ที่เลือกได้, **การเขียนด้วยมือบนอุปกรณ์ (Vision)** ที่เลือกได้ |

## การเก็บข้อมูล

เรามีข้อกำหนดว่า **ไม่** เก็บ, ขาย หรือแบ่งปันข้อมูลส่วนตัวเพื่อโฆษณาหรือการวิเคราะห์

- **ไม่ต้องมีบัญชี** — คุณสามารถใช้ฟีเจอร์หลักทั้งหมดได้โดยไม่ต้องสร้างบัญชีกับเรา
- **ไม่มีการวิเคราะห์หรือโฆษณา** — แอปพลิเคชันไม่รวม SDK ของบุคคลที่สามสำหรับการวิเคราะห์ โฆษณา หรือรายงานข้อผิดพลาดที่ส่งข้อมูลกลับมายังเรา
- **ไม่มีการอัปโหลดเนื้อหา** — ประวัติการอ่าน รายการโปรด รายการบันทึก โน้ต ความก้าวหน้าการศึกษา และการตั้งค่าของคุณจะอยู่บนอุปกรณ์ของคุณ (และสามารถเลือกเก็บไว้ใน **iCloud ของคุณ** ได้) ข้อมูลเหล่านี้จะไม่ถูกอัปโหลดไปยังเซิร์ฟเวอร์ของ iHTC Studio เพราะ **เราไม่ได้ดำเนินการเซิร์ฟเวอร์สำหรับแอปนี้**

ฉากสี่การสอบ การแตะแผนภาพเส้นลมปราณ และการร่างสีลิ้นบนอุปกรณ์ทั้งหมดอยู่ในเครื่อง พวกมันเป็นแผนภาพเชิงวัฒนธรรม ไม่ใช่การวินิจฉัย การสั่งยา หรือการรวมกับ HealthKit

## วิธีการทำงานของแอป

- **ไลบรารีที่รวมกลุ่ม** — ข้อความ JSON ภาษาพื้นถิ่น/อังกฤษ ดัชนี และตัวช่วยในการเรียนจะจัดส่งภายในชุดแอป/วิดเจ็ต 
- **คำพูดบนอุปกรณ์** — การบรรยายใช้ระบบของ Apple **AVSpeechSynthesizer** (TTS) เราไม่ส่งข้อความข้อความไปที่ iHTC Studio 
- **วิดเจ็ตและกลุ่มแอป** — วิดเจ็ตและแอปแชร์การตั้งค่าผ่านกลุ่มแอป `group.com.iHTCboy.iBianQue` บนอุปกรณ์ของคุณ 
- **การแจ้งเตือนรายวัน** — กำหนดเวลาในเครื่อง การแตะการแจ้งเตือนจะเปิดลิงก์ในรายละเอียดบนอุปกรณ์ 
- **การ์ดการศึกษา** — รูปภาพถูกเรนเดอร์บนอุปกรณ์ การบันทึกจะใช้ **เฉพาะส่วนเสริมคลังรูปภาพ** เฉพาะเมื่อคุณแตะบันทึก 
- **การค้นหาด้วยลายมือ (iOS)** — ตัวเลือกการรู้จำอักขระใช้ Apple **Vision** บนอุปกรณ์ จังหวะไม่ได้อัปโหลด 
- **เคล็ดลับเสริม** — “Tip Developer” เป็นการซื้อ **StoreKit** แบบบริโภคที่ดำเนินการโดย Apple 
- **Siri / ทางลัด / ศูนย์ควบคุม** — การบูรณาการระบบที่เป็นตัวเลือกจะเปิดลิงก์ในรายละเอียดบนอุปกรณ์ 
- **สปอตไลท์เสริม** — หากคุณเปิดใช้งานการจัดทำดัชนี ระบบจะจัดทำดัชนีเนื้อหาบนอุปกรณ์ 

## ข้อมูลที่จัดเก็บไว้ในอุปกรณ์ของคุณ

| ข้อมูล | ที่ไหน | วัตถุประสงค์ | 
|------|-------|---------| 
| ห้องสมุด Bian Que / Nan Jing | ชุดแอพ / วิดเจ็ต | การอ่านและการศึกษาแบบออฟไลน์ | 
| รายการโปรดและรายการ | ค่าเริ่มต้นของกลุ่มแอป | รายการที่ติดดาวและรายชื่อผู้ใช้ | 
| ประวัติการอ่าน / อ่านครั้งล่าสุด | ค่าเริ่มต้นของกลุ่มแอป | อ่านต่อ | 
| หมายเหตุ | ค่าเริ่มต้นของกลุ่มแอป | อ่านบันทึกที่คุณเขียน | 
| ความก้าวหน้าและความเชี่ยวชาญด้านการศึกษา | ค่าเริ่มต้นของกลุ่มแอป | ห้องเรียน / ล่าความคืบหน้า | 
| สตรีค/เช็คอิน | ค่าเริ่มต้นของกลุ่มแอป | นิสัยประจำวัน | 
| ลักษณะที่ปรากฏและการตั้งค่าการอ่าน | ค่าเริ่มต้นของกลุ่มแอป | ธีม, ภาษา, TTS, วิดเจ็ต | 
| การตั้งค่าแคชศิลปะรายวันและการแจ้งเตือน | ค่าเริ่มต้นของกลุ่มแอป | ID และกำหนดการของวันนี้ | 
| การตั้งค่าการ์ด | ค่าเริ่มต้นของกลุ่มแอป | รูปแบบสุดท้าย / อัตราส่วน | 
| การเริ่มต้นใช้งานและสถานะ TipKit | ค่าเริ่มต้นของผู้ใช้มาตรฐาน | คู่มือต้อนรับ | 
| วิดเจ็ต / ภาพรวมกิจกรรมสด | กลุ่มแอป / ActivityKit | แสดงข้อความที่คุณเปิดแล้ว | 

การถอนการติดตั้งแอปจะลบข้อมูลแซนด์บ็อกซ์และกลุ่มแอป (ขึ้นอยู่กับพฤติกรรมของระบบปฏิบัติการ) สำเนา iCloud ที่เป็นตัวเลือกจะยังคงอยู่ใน iCloud **ของคุณ** จนกว่าคุณจะล้างข้อมูลเหล่านั้น 

## iCloud ซิงค์ (ไม่จำเป็น)

หากคุณเปิดใช้งาน **iCloud Sync** ในการตั้งค่า แอปจะสะท้อนข้อมูลผู้ใช้ที่เลือกผ่าน **`NSUbiquitousKeyValueStore`** ของ Apple ที่เชื่อมโยงกับ **Apple ID ของคุณ**: 

- รายการโปรด 
- รายการ 
- การอ่านประวัติศาสตร์ 
- ความก้าวหน้าในการศึกษา / การเรียนรู้ 
- ฝึกลายเส้น 
- หมายเหตุ 

การรับส่งข้อมูลการซิงค์ไปที่ **Apple iCloud** ไม่ใช่ไปที่ iHTC Studio เราไม่สามารถอ่านเนื้อหา iCloud ของคุณได้ 

## สิทธิ์ 

iBianQue ร้องขอการอนุญาตเมื่อคุณสมบัติต้องการเท่านั้น: 

| การอนุญาต | เมื่อ | ทำไม | 
|------------|------|-----| 
| การแจ้งเตือน | คุณเปิดใช้งานการแจ้งเตือนศิลปะรายวัน | การกำหนดเวลาท้องถิ่น | 
| คลังรูปภาพ (เพิ่มเท่านั้น) | คุณบันทึกการ์ด | เขียนภาพที่แสดงผล | 
| ไอคลาวด์ | คุณเปิดใช้งานการซิงค์ | ซิงค์รายการโปรด / รายการ / ประวัติ / ความคืบหน้า / บันทึก | 
| กิจกรรมสด (iOS) | คุณเปิดใช้งานการอ่านกิจกรรมสด | แสดงข้อความบนหน้าจอล็อค / Dynamic Island | 
| เสียงพื้นหลัง (ความสามารถ) | คุณเปิดใช้งานการอ่านพื้นหลัง | ดำเนินการต่อ TTS ในพื้นหลัง | 

เราไม่ **ไม่** ขอข้อมูลผู้ติดต่อ ตำแหน่งที่แน่นอน กล้อง ไมโครโฟน (นอกเหนือจากการเล่น TTS ของระบบ) หรือการติดตาม 

## สิ่งที่เราไม่ทำ

- เราไม่ **ไม่** ขายข้อมูลส่วนบุคคล 
- เราไม่ **ไม่** สร้างโปรไฟล์การโฆษณา 
- เรา **ไม่** จำเป็นต้องมีบัญชีหรือการเข้าสู่ระบบโซเชียล 
- เราไม่ **ไม่** ฝังโฆษณา การวิเคราะห์ หรือ SDK โซเชียลของบุคคลที่สามสำหรับการรวบรวมข้อมูล 
- เราไม่ **ไม่** เข้าถึงคลังภาพของคุณเกินกว่า **เพิ่มเท่านั้น** เมื่อคุณเลือกที่จะบันทึกการ์ด 
- เรา **ไม่** รับหมายเลขบัตรชำระเงิน StoreKit (Apple ดำเนินการชำระเงิน) 

## ความเป็นส่วนตัวของเด็ก 

iBianQue เป็นแอปความรู้ด้านการศึกษาสำหรับผู้ชมทั่วไป และ **ไม่** อยู่ในหมวดหมู่เด็ก เราไม่รวบรวมข้อมูลส่วนบุคคลจากเด็กโดยเจตนา ครอบครัวอาจใช้คุณสมบัติการอ่านและการศึกษาแบบออฟไลน์บนอุปกรณ์ของตนเอง 

## บุคคลที่สาม 

- **Apple** — การจำหน่าย App Store, StoreKit ที่เป็นตัวเลือก, iCloud KVS ที่เป็นตัวเลือก, TTS ระบบ, ปลายทาง Share Sheet ที่คุณเลือก และการแจ้งเตือนระดับระบบปฏิบัติการ / กิจกรรมสด / Siri / ทางลัด / การส่งมอบวิสัยทัศน์ 
- **ไม่มี SDK บุคคลที่สามอื่นๆ** สำหรับโฆษณา การวิเคราะห์ หรือการเข้าสู่ระบบโซเชียลรวมอยู่ในการรวบรวมข้อมูล 

## ผู้ใช้ต่างประเทศ 

แอปได้รับการออกแบบมาให้ทำงานแบบออฟไลน์บนอุปกรณ์ของคุณ บริการเสริมของ Apple เป็นไปตามข้อกำหนดของ Apple และความพร้อมให้บริการในภูมิภาค 

## การเก็บรักษาและการลบข้อมูล

- **บนอุปกรณ์** — ลบแอปเพื่อเอาข้อมูล sandbox และ App Group ที่อยู่ในเครื่องออก (ขึ้นอยู่กับพฤติกรรมของระบบปฏิบัติการ)
- **iCloud** — ปิดการซิงค์และลบคีย์ที่เกี่ยวข้องจากบัญชี iCloud ของคุณตามความจำเป็น; เราไม่สามารถลบ iCloud ของคุณให้ได้
- **เราไม่เก็บอะไรเลย** บนเซิร์ฟเวอร์ iHTC Studio สำหรับแอปนี้เพราะเราไม่ได้เก็บข้อมูลนั้น

## การเปลี่ยนแปลงนโยบาย

เราอาจอัปเดตนโยบายความเป็นส่วนตัวนี้ วันที่ “อัปเดตล่าสุด” ที่ด้านบนจะมีการเปลี่ยนแปลง การใช้งานต่อหลังจากมีการอัปเดต หมายความว่าคุณยอมรับนโยบายที่แก้ไขแล้ว

## ติดต่อ

คำถามเกี่ยวกับความเป็นส่วนตัว: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="de" markdown="1">

**Zuletzt aktualisiert:** 19. September 2026

iHTC Studio („wir“, „uns“ oder „unser“) hat **iBianQue** (auch bekannt als „爱扁鹊 / 愛扁鵲“, Bundle-ID `com.iHTCboy.iBianQue`) entwickelt. Diese Datenschutzrichtlinie erklärt, welche Daten beim Verwenden der App verarbeitet werden (und welche nicht). **Apple App Review** und Nutzer können sich auf **diese Seite** als öffentliche Datenschutzrichtlinie verlassen. Für App Store Connect öffnen Sie diese Datenschutzrichtlinie in Ihrem Browser und kopieren die Adresse aus der Adressleiste (die Domain der öffentlichen Seite kann sich im Laufe der Zeit ändern).

## Zusammenfassung (Übereinstimmung mit dem Apple-Datenschutzetikett)

| Thema | Unsere Praxis |
|-------|----------------|
| Konto | **Nicht erforderlich** — keine Registrierung, kein Anmelden per E-Mail oder Telefonnummer |
| Datenerhebung durch iHTC Studio | **Keine Daten gesammelt** — wir betreiben kein Backend, das Ihre persönlichen Daten empfängt |
| Netzwerk | Bibliothek, Lesen, Rezitieren, Que Study, Widgets und tägliche Benachrichtigungen funktionieren **offline** nach der Installation |
| Analysen / Werbung / Tracking | **Keine** — keine Analyse-, Werbe- oder Tracking-SDKs von Drittanbietern; keine Nutzung von App Tracking Transparency |
| Optionale Apple-Dienste | **iCloud** (Ihr privates KVS), **Fotomediathek (Nur hinzufügen)** für Lernkarten, **StoreKit** für optionales Trinkgeld, **lokale Benachrichtigungen**, optionale **Live-Aktivitäten**, optional **handschriftliche Eingabe** auf dem Gerät (Vision) |

## Datenerhebung

Wir sammeln, verkaufen oder teilen **keine** persönlichen Informationen für Werbung oder Analysen.

- **Kein Konto** — Sie können alle Kernfunktionen nutzen, ohne ein Konto bei uns zu erstellen.
- **Keine Analysen oder Werbung** — Die App-Binärdatei integriert keine Analyse-, Werbe- oder Absturzbericht-SDKs von Drittanbietern, die Daten an uns senden.
- **Kein Hochladen von Inhalten** — Ihr Leseverlauf, Favoriten, Listen, Notizen, Lernfortschritt und Einstellungen bleiben auf Ihrem Gerät (und optional in **Ihrem** iCloud-Konto). Sie werden niemals auf iHTC Studio Server hochgeladen, da **wir solche Server für diese App nicht betreiben**.

Vier Untersuchungs-Szenen, Meridian-Atlas-Taps und die Zungenskizze auf dem Gerät bleiben lokal. Sie sind kulturelle Diagramme. Sie sind **keine** Diagnose, Verschreibung oder HealthKit-Integration.

## So funktioniert die App

- **Gebündelte Bibliothek** – JSON-Text, Umgangssprache/Englisch, Indizes und Lernhilfen sind im App-/Widget-Paket enthalten. 
- **Sprache auf dem Gerät** – Die Rezitation nutzt Apples System **AVSpeechSynthesizer** (TTS). Wir senden keine Passagentexte an iHTC Studio. 
- **Widgets & App-Gruppe** – Widgets und die App-Freigabeeinstellungen über die App-Gruppe `group.com.iHTCboy.iBianQue` auf Ihrem Gerät. 
- **Tägliche Benachrichtigungen** – Lokal geplant. Durch Tippen auf eine Benachrichtigung wird ein Deep-Link auf dem Gerät geöffnet. 
- **Lernkarten** – Bilder werden auf dem Gerät gerendert. Beim Speichern wird **nur die Add-On-Fotobibliothek** verwendet, wenn Sie auf „Speichern“ tippen. 
- **Handschriftsuche (iOS)** – Die optionale Zeichenerkennung verwendet Apple **Vision** auf dem Gerät. Striche werden nicht hochgeladen. 
- **Optionaler Tipp** – „Tip Developer“ ist ein verbrauchbarer **StoreKit**-Kauf, der von Apple abgewickelt wird. 
- **Siri / Verknüpfungen / Kontrollzentrum** – Optionale Systemintegrationen öffnen Deep Links auf dem Gerät. 
- **Optionales Spotlight** – Wenn Sie die Indizierung aktivieren, indiziert das System Inhalte auf dem Gerät. 

## Auf Ihrem Gerät gespeicherte Daten

| Daten | Wo | Zweck | 
|------|-------|---------| 
| Bian Que / Nan Jing-Bibliothek | App-/Widget-Bundle | Offline-Lesen und Lernen | 
| Favoriten & Listen | Benutzerstandards der App-Gruppe | Markierte Elemente und Benutzerlisten | 
| Leseverlauf / zuletzt gelesen | Benutzerstandards der App-Gruppe | Weiterlesen | 
| Notizen | Benutzerstandards der App-Gruppe | Lesen von Notizen, die Sie schreiben | 
| Studienfortschritt & Beherrschung | Benutzerstandards der App-Gruppe | Unterrichts-/Jagdfortschritt | 
| Streak / Check-in | Benutzerstandards der App-Gruppe | Tägliche Gewohnheit | 
| Aussehen & Lesepräferenzen | Benutzerstandards der App-Gruppe | Thema, Sprache, TTS, Widgets | 
| Tägliche Kunst-Cache- und Benachrichtigungseinstellungen | Benutzerstandards der App-Gruppe | Heutiger Ausweis und Zeitplan | 
| Karteneinstellungen | Benutzerstandards der App-Gruppe | Letzter Stil / Verhältnis | 
| Onboarding- und TipKit-Status | Standardbenutzerstandards | Willkommensführer | 
| Widget-/Live-Aktivitäts-Schnappschüsse | App-Gruppe / ActivityKit | Text anzeigen, den Sie bereits geöffnet haben | 

Durch die Deinstallation der App werden Sandbox- und App-Gruppendaten entfernt (je nach Betriebssystemverhalten). Optionale iCloud-Kopien bleiben in **Ihrer** iCloud, bis Sie sie löschen. 

## iCloud-Synchronisierung (optional)

Wenn Sie **iCloud Sync** in den Einstellungen aktivieren, spiegelt die App ausgewählte Benutzerdaten über Apples **`NSUbiquitousKeyValueStore`**, das an **Ihre Apple-ID** gebunden ist: 

- Favoriten 
- Listen 
- Geschichte lesen 
- Studienfortschritt / Beherrschung 
- Übungssträhnen 
- Notizen 

Der Synchronisierungsverkehr geht an **Apple iCloud**, nicht an iHTC Studio. Wir können Ihre iCloud-Inhalte nicht lesen. 

## Berechtigungen 

iBianQue fordert Berechtigungen nur an, wenn eine Funktion diese benötigt: 

| Erlaubnis | Wann | Warum | 
|------------|------|-----| 
| Benachrichtigungen | Sie aktivieren tägliche Kunsterinnerungen | Lokale Planung | 
| Fotobibliothek (Nur hinzufügen) | Sie speichern eine Karte | Schreiben Sie das gerenderte Bild | 
| iCloud | Sie aktivieren die Synchronisierung | Favoriten/Listen/Verlauf/Fortschritt/Notizen synchronisieren | 
| Live-Aktivitäten (iOS) | Sie aktivieren die Lese-Live-Aktivität | Zeigen Sie die Passage auf dem Sperrbildschirm / Dynamic Island | an 
| Hintergrundaudio (Fähigkeit) | Sie aktivieren die Hintergrundrezitation | TTS im Hintergrund fortsetzen | 

Wir fordern **keine** Kontakte, den genauen Standort, die Kamera, das Mikrofon (über die System-TTS-Wiedergabe hinaus) oder die Nachverfolgung an. 

## Was wir nicht tun

- Wir verkaufen **keine** personenbezogene Daten. 
- Wir erstellen **keine** Werbeprofile. 
- Wir benötigen **kein** Konto oder Social-Login. 
- Wir betten zur Datenerfassung **keine** Werbung, Analysen oder soziale SDKs von Drittanbietern ein. 
- Wir greifen über die Option „Nur hinzufügen“ hinaus **nicht** auf Ihre Fotobibliothek zu, wenn Sie sich für das Speichern einer Karte entscheiden. 
- Wir erhalten **keine** Nummern von StoreKit-Zahlungskarten (Apple verarbeitet Zahlungen). 

## Privatsphäre von Kindern 

iBianQue ist eine Bildungs- und Lesekompetenz-App für ein allgemeines Publikum und gehört **nicht** zur Kategorie „Kinder“. Wir erfassen wissentlich keine personenbezogenen Daten von Kindern. Familien können Lese- und Lernfunktionen offline auf ihren eigenen Geräten nutzen. 

## Dritte 

- **Apple** – App Store-Verteilung, optionales StoreKit, optionales iCloud KVS, System-TTS, von Ihnen ausgewählte Share Sheet-Ziele und Benachrichtigung auf Betriebssystemebene/Live-Aktivität/Siri/Verknüpfungen/Vision-Bereitstellung. 
- **Für die Datenerfassung sind keine weiteren SDKs von Drittanbietern** für Anzeigen, Analysen oder Social-Login enthalten. 

## Internationale Benutzer 

Die App ist so konzipiert, dass sie offline auf Ihrem Gerät funktioniert. Optionale Apple-Dienste unterliegen den Geschäftsbedingungen und der regionalen Verfügbarkeit von Apple. 

## Datenaufbewahrung und -löschung

- **Auf dem Gerät** — Löschen Sie die App, um lokale Sandbox- und App-Gruppendaten zu entfernen (abhängig vom Verhalten des Betriebssystems).
- **iCloud** — Deaktivieren Sie die Synchronisierung und löschen Sie bei Bedarf die zugehörigen Schlüssel aus Ihrem iCloud-Konto; wir können Ihr iCloud-Konto nicht für Sie löschen.
- **Wir speichern nichts** auf den iHTC Studio-Servern für diese App, da wir keine Daten sammeln.

## Richtlinienänderungen

Wir können diese Datenschutzerklärung aktualisieren. Das Datum „Zuletzt aktualisiert“ oben wird sich ändern. Die weitere Nutzung nach einer Aktualisierung bedeutet, dass Sie die überarbeitete Richtlinie akzeptieren.

## Kontakt

Fragen zum Datenschutz: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="fr" markdown="1">

**Dernière mise à jour :** 19 septembre 2026

iHTC Studio (« nous » ou « notre ») a créé **iBianQue** (également connu sous le nom de « 爱扁鹊 / 愛扁鵲 », ID de bundle `com.iHTCboy.iBianQue`). Cette politique de confidentialité explique quelles données sont (et ne sont pas) traitées lorsque vous utilisez l'application. **Apple App Review** et les utilisateurs peuvent se référer à **cette page** comme politique de confidentialité publique. Pour App Store Connect, ouvrez cette politique de confidentialité dans votre navigateur et copiez l'adresse depuis la barre d'adresse (le domaine du site public peut changer au fil du temps).

## Résumé (alignement avec l'étiquette nutritionnelle de confidentialité d'Apple)

| Sujet | Notre pratique |
|-------|----------------|
| Compte | **Non requis** — pas d'inscription, connexion par e-mail ou numéro de téléphone |
| Collecte de données par iHTC Studio | **Données non collectées** — nous ne gérons **pas** de serveur qui reçoit vos données personnelles |
| Réseau | Bibliothèque, lecture, récitation, Que Study, widgets et notifications quotidiennes fonctionnent **hors ligne** après l'installation |
| Analyses / publicités / suivi | **Aucun** — aucun SDK d'analyse tiers, de publicité ou de suivi ; aucune utilisation d’App Tracking Transparency |
| Services Apple optionnels | **iCloud** (votre KVS privé), **Photothèque (ajout uniquement)** pour les cartes d’étude, **StoreKit** pour les pourboires optionnels, **notifications locales**, **Live Activities** optionnel, **écriture manuscrite sur appareil** optionnelle (Vision) |

## Collecte de données

Nous ne collectons, ne vendons ni ne partageons d’informations personnelles à des fins publicitaires ou analytiques.

- **Pas de compte** — Vous pouvez utiliser toutes les fonctionnalités principales sans créer de compte chez nous.
- **Pas d’analytique ni de publicités** — Le binaire de l'application n'intègre pas de modules d'analyse, publicité ou rapports de crash tiers qui enverraient des données vers nous.
- **Pas de téléchargement de contenu** — Votre historique de lecture, vos favoris, listes, notes, progression d'étude et préférences restent sur votre appareil (et éventuellement dans **votre** iCloud). Ils ne sont jamais téléchargés sur les serveurs d’iHTC Studio parce que **nous ne gérons pas de tels serveurs pour cette application**.

Les quatre scènes d’examen, les atlas des méridiens et les croquis de couleur de la langue sur l’appareil restent locaux. Ce sont des diagrammes culturels. Ils ne constituent **pas** un diagnostic, une prescription ou une intégration HealthKit.

## Comment l’application fonctionne

- **Bibliothèque groupée** — Texte JSON, langue vernaculaire/anglais, index et aides à l'étude livrés dans l'ensemble application/widget. 
- **Discours sur l'appareil** — La récitation utilise le système **AVSpeechSynthesizer** (TTS) d'Apple. Nous n'envoyons pas de texte de passage à iHTC Studio. 
- **Widgets et groupe d'applications** — Les widgets et l'application partagent les préférences via le groupe d'applications `group.com.iHTCboy.iBianQue` sur votre appareil. 
- **Notifications quotidiennes** — Planifiées localement. Appuyer sur une notification ouvre un lien profond sur l'appareil. 
- **Cartes d'étude** — Les images sont rendues sur l'appareil. L'enregistrement utilise **le module complémentaire Photothèque** uniquement lorsque vous appuyez sur Enregistrer. 
- **Recherche d'écriture manuscrite (iOS)** : la reconnaissance de caractères facultative utilise Apple **Vision** sur l'appareil. Les traits ne sont pas téléchargés. 
- **Conseil facultatif** — « Tip Developer » est un achat de consommable **StoreKit** traité par Apple. 
- **Siri / Raccourcis / Centre de contrôle** — Les intégrations système facultatives ouvrent des liens profonds sur l'appareil. 
- **Spotlight facultatif** : si vous activez l'indexation, le système indexe le contenu sur l'appareil. 

## Données stockées sur votre appareil

| Données | Où | Objectif | 
|------|-------|--------------| 
| Bibliothèque Bian Que / Nan Jing | Offre groupée d'applications/widgets | Lecture et étude hors ligne | 
| Favoris et listes | Paramètres par défaut du groupe d'applications | Éléments favoris et listes d'utilisateurs | 
| Historique de lecture / dernière lecture | Paramètres par défaut du groupe d'applications | Continuer la lecture | 
| Remarques | Paramètres par défaut du groupe d'applications | Notes de lecture que vous écrivez | 
| Avancement et maîtrise des études | Paramètres par défaut du groupe d'applications | Classe / Progrès de la chasse | 
| Série / enregistrement | Paramètres par défaut du groupe d'applications | Habitude quotidienne | 
| Apparence et préférences de lecture | Paramètres par défaut du groupe d'applications | Thème, langue, TTS, widgets | 
| Cache artistique quotidien et préférences de notification | Paramètres par défaut du groupe d'applications | ID et horaire du jour | 
| Préférences de carte | Paramètres par défaut du groupe d'applications | Dernier style/ratio | 
| État d’intégration et de TipKit | Valeurs par défaut de l'utilisateur standard | Guide de bienvenue | 
| Widget / Instantanés d'activité en direct | Groupe d'applications / ActivityKit | Afficher le texte que vous avez déjà ouvert | 

La désinstallation de l'application supprime les données du bac à sable et du groupe d'applications (sous réserve du comportement du système d'exploitation). Les copies iCloud facultatives restent dans **votre** iCloud jusqu'à ce que vous les effaciez. 

## Synchronisation iCloud (facultatif)

Si vous activez **iCloud Sync** dans Paramètres, l'application reflète les données utilisateur sélectionnées via le **`NSUbiquitousKeyValueStore`** d'Apple lié à **votre identifiant Apple** : 

- Favoris 
- Listes 
- Lire l'histoire 
- Avancement des études/maîtrise 
- Séries d'entraînement 
- Remarques 

Le trafic de synchronisation va vers **Apple iCloud**, pas vers iHTC Studio. Nous ne pouvons pas lire votre contenu iCloud. 

## Autorisations 

iBianQue demande des autorisations uniquement lorsqu'une fonctionnalité en a besoin : 

| Autorisation | Quand | Pourquoi | 
|------------|------|-----| 
| Notifications | Vous activez les rappels Daily Art | Planification locale | 
| Bibliothèque de photos (Ajouter uniquement) | Vous enregistrez une carte | Écrivez l'image rendue | 
| iCloud | Vous activez la synchronisation | Synchroniser les favoris/listes/historique/progression/notes | 
| Activités en direct (iOS) | Vous activez l'activité de lecture en direct | Afficher le passage sur l'écran de verrouillage / Dynamic Island | 
| Audio de fond (capacité) | Vous activez la récitation en arrière-plan | Continuer TTS en arrière-plan | 

Nous ne demandons **pas** de contacts, de localisation précise, de caméra, de microphone (au-delà de la lecture TTS du système) ou de suivi. 

## Ce que nous ne faisons pas

- Nous ne vendons **pas** de données personnelles. 
- Nous ne créons **pas** de profils publicitaires. 
- Nous n'exigeons **pas** de compte ou de connexion sociale. 
- Nous n'intégrons **pas** de publicités tierces, d'analyses ou de SDK sociaux pour la collecte de données. 
- Nous n'accédons **pas** à votre photothèque au-delà du **ajout uniquement** lorsque vous choisissez d'enregistrer une carte. 
- Nous ne recevons **pas** de numéros de carte de paiement StoreKit (Apple traite les paiements). 

## Confidentialité des enfants 

iBianQue est une application d'alphabétisation éducative destinée au grand public et n'est **pas** dans la catégorie Enfants. Nous ne collectons pas sciemment d’informations personnelles auprès des enfants. Les familles peuvent utiliser les fonctionnalités de lecture et d’étude hors ligne sur leurs propres appareils. 

## Tiers 

- **Apple** — Distribution sur l'App Store, StoreKit en option, iCloud KVS en option, TTS système, destinations de feuille de partage que vous choisissez et notification au niveau du système d'exploitation/activité en direct/Siri/raccourcis/livraison Vision. 
- **Aucun autre SDK tiers** pour les publicités, les analyses ou la connexion sociale n'est inclus pour la collecte de données. 

## Utilisateurs internationaux 

L'application est conçue pour fonctionner hors ligne sur votre appareil. Les services Apple en option suivent les conditions d’Apple et la disponibilité régionale. 

## Conservation et suppression des données

- **Sur l'appareil** — Supprimez l'application pour retirer les données locales du bac à sable et du groupe d'applications (sous réserve du comportement du système d'exploitation).  
- **iCloud** — Désactivez la synchronisation et supprimez les clés associées de votre compte iCloud si nécessaire ; nous ne pouvons pas effacer votre iCloud pour vous.  
- **Nous ne conservons rien** sur les serveurs iHTC Studio pour cette application car nous ne collectons pas ces données.

## Modifications de la politique

Nous pouvons mettre à jour cette politique de confidentialité. La date « Dernière mise à jour » en haut sera modifiée. L'utilisation continue après une mise à jour signifie que vous acceptez la politique révisée.

## Contact

Questions sur la vie privée : [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="tr" markdown="1">

**Son güncelleme:** 19 Eylül 2026

iHTC Studio (“biz”, “bize” veya “bizim”) **iBianQue**’yi geliştirdi (aynı zamanda “爱扁鹊 / 愛扁鵲” olarak da bilinir, Paket Kimliği `com.iHTCboy.iBianQue`). Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlendiğini (ve işlenmediğini) açıklar. **Apple App Review** ve kullanıcılar, **bu sayfayı** kamuya açık gizlilik politikası olarak kullanabilir. App Store Connect için bu Gizlilik Politikasını tarayıcınızda açın ve adres çubuğundan adresi kopyalayın (kamu sitesi alan adı zamanla değişebilir).

## Özet (Apple Gizlilik Beslenme Etiketi uyumu)

| Konu | Uygulamamızın uygulaması |
|-------|----------------|
| Hesap | **Gerekli değil** — kayıt, e-posta ile giriş veya telefon numarası yok |
| iHTC Studio tarafından veri toplanması | **Veri Toplanmıyor** — kişisel verilerinizi alan bir arka uç işletmiyoruz |
| Ağ | Kütüphane, okuma, ezberleme, Que Çalışma, widgetlar ve günlük bildirimler kurulumdan sonra **çevrimdışı** çalışır |
| Analitik / reklam / izleme | **Hiçbiri** — üçüncü taraf analitik, reklam veya izleme SDK'ları yok; App Tracking Transparency kullanılmıyor |
| İsteğe bağlı Apple hizmetleri | **iCloud** (özel KVS'niz), çalışma kartları için **Fotoğraf Kitaplığı (Sadece Ekleme)**, isteğe bağlı bahşişler için **StoreKit**, **yerel bildirimler**, isteğe bağlı **Canlı Aktiviteler**, cihazda isteğe bağlı **el yazısı** (Vision) |

## Veri Toplama

Kişisel bilgileri reklam veya analiz amacıyla **toplamıyoruz**, satmıyoruz veya paylaşmıyoruz.

- **Hesap gerekmiyor** — Tüm temel özellikleri bizimle hesap oluşturmadan kullanabilirsiniz.
- **Analitik veya reklam yok** — Uygulama ikili dosyası üçüncü taraf analitik, reklam veya arıza raporlama SDK'larını entegre etmez ve bize veri göndermez.
- **İçerik yükleme yok** — Okuma geçmişiniz, favorileriniz, listeleriniz, notlarınız, çalışma ilerlemeniz ve tercihlerinize cihazınızda (ve isteğe bağlı olarak **iCloud’unuzda**) kalır. Bunlar iHTC Studio sunucularına asla yüklenmez çünkü **bu uygulama için böyle sunucular işletmiyoruz**.

Dört Sınav sahnesi, meridyen atlası dokunuşları ve cihazdaki dil rengi taslağı yerel olarak kalır. Bunlar kültürel diyagramlardır. **Tanı, reçete veya HealthKit entegrasyonu değildir**.

## Uygulama Nasıl Çalışır

- **Paketlenmiş kitaplık** — Metin JSON, yerel dil/İngilizce, dizinler ve çalışma yardımcıları uygulama/widget paketinin içinde gönderilir. 
- **Cihaz içi konuşma** — Okuma, Apple'ın **AVSpeechSynthesizer** (TTS) sistemini kullanır. iHTC Studio'ya pasaj metni göndermiyoruz. 
- **Widget'lar ve Uygulama Grubu** — Cihazınızdaki Uygulama Grubu `group.com.iHTCboy.iBianQue` aracılığıyla widget'lar ve uygulama paylaşım tercihleri. 
- **Günlük bildirimler** — Yerel olarak planlanmıştır. Bir bildirime dokunduğunuzda cihazda derin bir bağlantı açılır. 
- **Çalışma kartları** — Görüntüler cihazda oluşturulur. Kaydetme, **Yalnızca Fotoğraf Kitaplığı eklentisini** yalnızca kaydet'e dokunduğunuzda kullanır. 
- **El yazısı araması (iOS)** — İsteğe bağlı karakter tanıma, cihazda Apple **Vision**'ı kullanır. Konturlar yüklenmedi. 
- **İsteğe bağlı ipucu** — "İpucu Geliştirici", Apple tarafından gerçekleştirilen bir **StoreKit** sarf malzemesidir. 
- **Siri / Kısayollar / Kontrol Merkezi** — İsteğe bağlı sistem entegrasyonları cihazdaki derin bağlantıları açar. 
- **İsteğe Bağlı Spot Işığı** — Dizin oluşturmayı etkinleştirirseniz sistem, cihazdaki içeriği dizine ekler. 

## Cihazınızda Saklanan Veriler

| Veri | Nerede | Amaç | 
|------|-------|-------------| 
| Bian Que / Nan Jing kütüphanesi | Uygulama / Widget paketi | Çevrimdışı okuma ve çalışma | 
| Favoriler ve listeler | Uygulama Grubu Kullanıcı Varsayılanları | Yıldızlı öğeler ve kullanıcı listeleri | 
| Okuma geçmişi / son okuma | Uygulama Grubu Kullanıcı Varsayılanları | Okumaya devam et | 
| Notlar | Uygulama Grubu Kullanıcı Varsayılanları | Yazdığınız notları okuma | 
| Çalışma ilerlemesi ve ustalık | Uygulama Grubu Kullanıcı Varsayılanları | Sınıf / Av ilerlemesi | 
| Seri / giriş | Uygulama Grubu Kullanıcı Varsayılanları | Günlük alışkanlık | 
| Görünüm ve okuma tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Tema, dil, TTS, widget'lar | 
| Daily Art önbelleği ve bildirim tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Bugünün kimliği ve programı | 
| Kart tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Son stil / oran | 
| İlk katılım ve TipKit durumu | Standart Kullanıcı Varsayılanları | Hoş geldiniz kılavuzu | 
| Widget / Canlı Etkinlik anlık görüntüleri | Uygulama Grubu / ActivityKit | Daha önce açmış olduğunuz metni görüntüleyin | 

Uygulamanın kaldırılması, korumalı alanı ve Uygulama Grubu verilerini kaldırır (işletim sistemi davranışına bağlıdır). İsteğe bağlı iCloud kopyaları, siz onları temizleyene kadar **iCloud'unuzda** kalır. 

## iCloud Senkronizasyonu (İsteğe bağlı)

Ayarlar'da **iCloud Senkronizasyonu**'nu etkinleştirirseniz uygulama, seçilen kullanıcı verilerini Apple'ın **`NSUbiquitousKeyValueStore`_** aracılığıyla **Apple Kimliğinize** bağlı olarak yansıtır: 

- Favoriler 
- Listeler 
- Tarih okuma 
- Çalışma ilerlemesi / ustalığı 
- Seri antrenman yapın 
- Notlar 

Senkronizasyon trafiği iHTC Studio'ya değil **Apple iCloud**'a gider. iCloud içeriklerinizi okuyamıyoruz. 

## İzinler 

iBianQue yalnızca bir özellik ihtiyaç duyduğunda izin ister: 

| İzin | Ne zaman | Neden | 
|---------------|----------|-----| 
| Bildirimler | Günlük Sanat hatırlatıcılarını etkinleştirirsiniz | Yerel planlama | 
| Fotoğraf Kitaplığı (Yalnızca Ekle) | Bir kartı kaydedersiniz | İşlenen görüntüyü yazın | 
| iCloud | Senkronizasyonu etkinleştirirsiniz | Favorileri / listeleri / geçmişi / ilerlemeyi / notları senkronize et | 
| Canlı Etkinlikler (iOS) | Canlı Okuma Etkinliğini etkinleştirirsiniz | Pasajı Kilit Ekranında / Dinamik Adada göster | 
| Arka planda ses (yetenek) | Arka planda okumayı etkinleştirirsiniz | Arka planda TTS'ye devam et | 

Kişiler, kesin Konum, Kamera, Mikrofon (sistem TTS oynatmanın ötesinde) veya İzleme **talebi etmeyiz**. 

## Ne Yapmıyoruz

- Kişisel verileri **satmıyoruz**. 
- Reklam profilleri **oluşturmuyoruz**. 
- Bir hesaba veya sosyal girişe **gerek duymayız**. 
- Veri toplama amacıyla üçüncü taraf reklamları, analizleri veya sosyal SDK'ları **yerleştirmeyiz**. 
- Bir kartı kaydetmeyi seçtiğinizde **yalnızca eklenti** dışında Fotoğraf Kitaplığınıza **erişmeyiz**. 
- StoreKit ödeme kartı numaralarını **almıyoruz** (ödemeleri Apple işler). 

## Çocukların Gizliliği 

iBianQue, genel kitleye yönelik bir eğitim okuryazarlığı uygulamasıdır ve Çocuk Kategorisinde **değildir**. Çocuklardan bilerek kişisel bilgi toplamıyoruz. Aileler okuma ve çalışma özelliklerini kendi cihazlarında çevrimdışı olarak kullanabilir. 

## Üçüncü Taraflar 

- **Apple** — App Store dağıtımı, isteğe bağlı StoreKit, isteğe bağlı iCloud KVS, sistem TTS, seçtiğiniz Paylaşım Sayfası hedefleri ve işletim sistemi düzeyinde bildirim / Canlı Etkinlik / Siri / Kısayollar / Vision dağıtımı. 
- **Veri toplama amacıyla reklamlara, analizlere veya sosyal oturum açmaya yönelik başka hiçbir üçüncü taraf SDK'sı** dahil edilmemiştir. 

## Uluslararası Kullanıcılar 

Uygulama, cihazınızda çevrimdışı çalışacak şekilde tasarlanmıştır. İsteğe bağlı Apple hizmetleri, Apple'ın koşullarına ve bölgesel kullanılabilirliğe uygundur. 

## Veri Saklama ve Silme

- **Cihazda** — Yerel sandbox ve App Group verilerini kaldırmak için uygulamayı silin (işletim sistemi davranışına bağlıdır).
- **iCloud** — Senkronizasyonu kapatın ve gerekirse ilgili anahtarları iCloud hesabınızdan temizleyin; iCloud hesabınızı sizin için silemeyiz.
- **Hiçbir şeyi** iHTC Studio sunucularında bu uygulama için saklamıyoruz çünkü bunu toplamıyoruz.

## Politika Değişiklikleri

Bu Gizlilik Politikasını güncelleyebiliriz. Üstteki "Son güncelleme" tarihi değişecektir. Güncellemeden sonra devam eden kullanım, revize edilen politikayı kabul ettiğiniz anlamına gelir.

## İletişim

Gizlilik ile ilgili sorular: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
