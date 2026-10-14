---
layout: doc
title: iShangYang — Privacy Policy
app_id: iShangYang
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iShangYang — offline Shangjunshu historical study, Data Not Collected, not a ruling prescription.
---

<section lang="en" markdown="1">

**Last updated:** September 19, 2026

iHTC Studio ("we", "us" or "our") built **iShangYang** (also known as "爱商鞅 / 愛商鞅", Bundle ID `com.iHTCboy.iShangYang`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on **this page** as the public privacy policy. For App Store Connect, open this Privacy Policy in your browser and copy the address from the address bar (the public site domain may change over time).

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration, email sign-in, or phone number |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your personal data |
| Network | Library, reading, recite, Reform Study, widgets, and daily notifications work **offline** after install |
| Analytics / ads / tracking | **None** — no third-party analytics, advertising, or tracking SDKs; no App Tracking Transparency use |
| Optional Apple services | **iCloud** (your private KVS), **Photo Library (Add Only)** for study cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional on-device **handwriting** (Vision) |

## Data Collection

We do **not** collect, sell, or share personal information for advertising or analytics.

- **No account** — You can use all core features without creating an account with us.
- **No analytics or ads** — The app binary does not integrate third-party analytics, advertising, or crash-reporting SDKs that phone home to us.
- **No content upload** — Your reading history, favorites, lists, notes, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

These texts belong to **Warring States institutional history**. We present sources and put them back in their setting. This is historical study, **not** advocacy of harsh penalties.

## How the App Works

- **Bundled library** — Text JSON, vernacular/English, indexes, and study aids ship inside the app / widget bundle.
- **On-device speech** — Recitation uses Apple’s system **AVSpeechSynthesizer** (TTS). We do not send passage text to iHTC Studio.
- **Widgets & App Group** — Widgets and the app share preferences via App Group `group.com.iHTCboy.iShangYang` on your device.
- **Daily notifications** — Scheduled locally. Tapping a notification opens a deep link on device.
- **Study cards** — Images are rendered on device. Saving uses **Photo Library add-only** only when you tap save.
- **Handwriting search (iOS)** — Optional character recognition uses Apple **Vision** on device. Strokes are not uploaded.
- **Optional tip** — “Tip Developer” is a consumable **StoreKit** purchase processed by Apple.
- **Siri / Shortcuts / Control Center** — Optional system integrations open on-device deep links.
- **Optional Spotlight** — If you enable indexing, the system indexes content on device.

## Data Stored on Your Device

| Data | Where | Purpose |
|------|-------|---------|
| Shangjunshu library | App / Widget bundle | Offline reading & study |
| Favorites & lists | App Group UserDefaults | Starred items and user lists |
| Reading history / last read | App Group UserDefaults | Continue reading |
| Notes | App Group UserDefaults | Reading notes you write |
| Study progress & mastery | App Group UserDefaults | Classroom / Hunt progress |
| Streak / check-in | App Group UserDefaults | Daily habit |
| Appearance & reading prefs | App Group UserDefaults | Theme, language, TTS, widgets |
| Daily Reform cache & notification prefs | App Group UserDefaults | Today’s ID and schedule |
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

iShangYang requests permissions only when a feature needs them:

| Permission | When | Why |
|------------|------|-----|
| Notifications | You enable Daily Reform reminders | Local scheduling |
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

iShangYang is an educational literacy app for a general audience and is **not** in the Kids Category. We do not knowingly collect personal information from children. Families may use reading and study features offline on their own devices.

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

爱火腿肠工作室（iHTC Studio）（「我们」）开发了 **爱商鞅**（iShangYang / 愛商鞅，Bundle ID `com.iHTCboy.iShangYang`）。本隐私政策说明你在使用本应用时，数据如何被处理。本页可作为 **App Store 审核**与用户查阅的公开隐私政策。填写 App Store Connect 时：打开本站[隐私政策](../privacy)页，从浏览器地址栏复制当前网址（站点域名日后可能变更，请勿依赖写死的完整域名）。

## 摘要（对齐 Apple 隐私标签）

| 主题 | 我们的做法 |
|------|------------|
| 账号 | **不需要** — 无注册、邮箱登录或手机号 |
| iHTC Studio 数据采集 | **Data Not Collected** — 我们**不**运营接收你个人数据的后端 |
| 网络 | 语料、品读、诵读、变法学堂、小组件与每日通知安装后均可**离线** |
| 分析 / 广告 / 追踪 | **无** — 无第三方分析、广告或追踪 SDK；不使用 ATT |
| 可选 Apple 服务 | **iCloud**（你的私人 KVS）、保存研读卡时的**照片图库（仅添加）**、可选 **StoreKit** 打赏、**本地通知**、可选**实时活动**、可选本机**手写识别** |

## 数据采集

我们**不**收集、出售或共享用于广告或分析的个人信息。

- **无账号** — 核心功能无需向我们注册。
- **无分析或广告** — 应用未集成会向我们回传的第三方分析、广告或崩溃 SDK。
- **无内容上传** — 阅读历史、收藏、清单、笔记、学习进度与偏好留在本机（并可选手动同步到**你的** iCloud）。

这些文字属于**战国制度史**。我们呈现史料、放回当时的语境。这是历史研读，**不是**提倡严刑。

## 应用如何工作

- **内置语料** — 正文 JSON、白话／英译、索引与学习辅助随 App／小组件打包。
- **本机语音** — 诵读使用系统 **AVSpeechSynthesizer**。我们不会把正文发送到 iHTC Studio。
- **小组件与 App Group** — 通过本机 App Group `group.com.iHTCboy.iShangYang` 共享偏好。
- **每日通知** — 本地调度；点按后经深链打开本机篇目。
- **研读卡** — 在设备上渲染。仅在你点保存时使用**照片图库（仅添加）**。
- **手写寻句（iOS）** — 使用本机 Apple **Vision**。笔迹不会上传。
- **可选打赏** — Apple 处理的消耗型 **StoreKit** 购买。
- **Siri／快捷指令／控制中心** — 打开本机深链。
- **可选 Spotlight** — 由系统在本机索引。

## 本机存储的数据

| 数据 | 位置 | 用途 |
|------|------|------|
| 商君书语料 | App／小组件 Bundle | 离线阅读与学习 |
| 收藏与清单 | App Group UserDefaults | 星标与用户清单 |
| 阅读历史／上次阅读 | App Group UserDefaults | 继续阅读 |
| 笔记 | App Group UserDefaults | 你写下的笔记 |
| 学习进度与掌握度 | App Group UserDefaults | 学堂／寻句进度 |
| 打卡／连续天数 | App Group UserDefaults | 每日习惯 |
| 外观与阅读偏好 | App Group UserDefaults | 主题、语言、TTS、小组件 |
| 今日一变缓存与通知偏好 | App Group UserDefaults | 今日 ID 与提醒 |
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
| 通知 | 你开启今日一变提醒 | 本地调度 |
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

爱商鞅是面向一般读者的教育类语文应用，**不属于** Kids Category。我们不会故意收集儿童个人信息。家庭可在自有设备上离线使用阅读与学习功能。

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

愛火腿腸工作室（iHTC Studio）（「我們」）開發了 **愛商鞅**（iShangYang / 爱商鞅，Bundle ID `com.iHTCboy.iShangYang`）。本隱私政策說明你在使用本應用時，資料如何被處理。本頁可作為 **App Store 審核**與使用者查閱的公開隱私政策。填寫 App Store Connect 時：打開本站[隱私政策](../privacy)頁，從瀏覽器網址列複製目前網址（網站網域日後可能變更，請勿依賴寫死的完整網域）。

## 摘要（對齊 Apple 隱私標籤）

| 主題 | 我們的做法 |
|------|------------|
| 帳號 | **不需要** — 無註冊、電子郵件登入或手機號碼 |
| iHTC Studio 資料蒐集 | **Data Not Collected** — 我們**不**營運接收你個人資料的後端 |
| 網路 | 語料、品讀、誦讀、變法學堂、小工具與每日通知安裝後均可**離線** |
| 分析 / 廣告 / 追蹤 | **無** — 無第三方分析、廣告或追蹤 SDK；不使用 ATT |
| 可選 Apple 服務 | **iCloud**（你的私人 KVS）、儲存研讀卡時的**照片（僅加入）**、可選 **StoreKit** 打賞、**本機通知**、可選**即時動態**、可選本機**手寫辨識** |

## 資料蒐集

我們**不**蒐集、出售或共享用於廣告或分析的個人資訊。

- **無帳號** — 核心功能無需向我們註冊。
- **無分析或廣告** — 應用未整合會向我們回傳的第三方分析、廣告或當機 SDK。
- **無內容上傳** — 閱讀歷史、收藏、清單、筆記、學習進度與偏好留在本機（並可選手動同步到**你的** iCloud）。

這些文字屬於**戰國制度史**。我們呈現史料、放回當時的語境。這是歷史研讀，**不是**提倡嚴刑。

## 應用如何工作

- **內建語料** — 正文 JSON、白話／英譯、索引與學習輔助隨 App／小工具打包。
- **本機語音** — 誦讀使用系統 **AVSpeechSynthesizer**。我們不會把正文傳送到 iHTC Studio。
- **小工具與 App Group** — 透過本機 App Group `group.com.iHTCboy.iShangYang` 共享偏好。
- **每日通知** — 本機排程；點按後經深鏈打開本機篇目。
- **研讀卡** — 在裝置上渲染。僅在你點儲存時使用**照片（僅加入）**。
- **手寫尋句（iOS）** — 使用本機 Apple **Vision**。筆跡不會上傳。
- **可選打賞** — Apple 處理的消耗型 **StoreKit** 購買。
- **Siri／捷徑／控制中心** — 打開本機深鏈。
- **可選 Spotlight** — 由系統在本機建立索引。

## 本機儲存的資料

| 資料 | 位置 | 用途 |
|------|------|------|
| 商君書語料 | App／小工具 Bundle | 離線閱讀與學習 |
| 收藏與清單 | App Group UserDefaults | 星號與使用者清單 |
| 閱讀歷史／上次閱讀 | App Group UserDefaults | 繼續閱讀 |
| 筆記 | App Group UserDefaults | 你寫下的筆記 |
| 學習進度與掌握度 | App Group UserDefaults | 學堂／尋句進度 |
| 打卡／連續天數 | App Group UserDefaults | 每日習慣 |
| 外觀與閱讀偏好 | App Group UserDefaults | 主題、語言、TTS、小工具 |
| 今日一變快取與通知偏好 | App Group UserDefaults | 今日 ID 與提醒 |
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
| 通知 | 你開啟今日一變提醒 | 本機排程 |
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

愛商鞅是面向一般讀者的教育類語文應用，**不屬於** Kids Category。我們不會故意蒐集兒童個人資訊。家庭可在自有裝置上離線使用閱讀與學習功能。

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

 iHTC Studio (「私たち」、「私たち」、または「私たちの」) は **iLiezi** (「愛情列子 / 愛列子」とも呼ばれ、バンドル ID `com.iHTCboy.iLiezi`) をビルドしました。 このプライバシー ポリシーでは、アプリを使用するときにどのようなデータが処理される (および扱われない) かについて説明します。 **Apple App Review** およびユーザーは、公開プライバシー ポリシーとして **このページ** を信頼することができます。 App Store Connect の場合は、ブラウザでこのプライバシー ポリシーを開き、アドレス バーからアドレスをコピーします (パブリック サイトのドメインは時間の経過とともに変更される可能性があります)。

## 概要（Apple プライバシー栄養表示との整合性）

| トピック | 当社の方針 |
|-------|----------------|
| アカウント | **不要** — 登録、メールサインイン、電話番号は必要ありません |
| iHTC Studioによるデータ収集 | **データは収集しません** — 個人データを受け取るバックエンドは運営していません |
| ネットワーク | ライブラリ、読書、暗唱、学習、Hunt、ウィジェット、日次通知はインストール後**オフライン**で動作します |
| 分析 / 広告 / トラッキング | **なし** — サードパーティの分析、広告、トラッキングSDKは使用しておらず、App Tracking Transparencyも使用していません |
| 任意のAppleサービス | **iCloud**（あなたのプライベートKVS）、**写真ライブラリ（追加のみ）**（学習カード用）、**StoreKit**（任意のチップ用）、**ローカル通知**、任意の**ライブアクティビティ**、任意のデバイス上での**手書き入力**（Vision） |

## データの収集

当社は、広告や分析のために個人情報を収集、販売、共有することは**ありません**。

- **アカウント不要** — アカウントを作成せずに、すべての基本機能を使用できます。
- **分析や広告なし** — アプリのバイナリには、サードパーティの分析、広告、クラッシュレポートSDKは統合されておらず、データが当社に送信されることはありません。
- **コンテンツのアップロードなし** — 閲読履歴、お気に入り、リスト、メモ、学習進捗、設定は端末内（および任意で**お客様の** iCloud）に留まります。**当社は本アプリ向けにそのようなサーバーを運用していない**ため、iHTC Studio のサーバーにアップロードされることはありません。

これらは**戦国制度史**の文献です。史料を提示し文脈に戻します。**厳刑を鼓吹するものではありません**。

## アプリの仕組み

- **バンドルされたライブラリ** — テキスト JSON、現地語/英語、インデックス、および学習支援機能がアプリ / ウィジェット バンドル内に同梱されています。
- **オンデバイス音声** - 朗読には Apple のシステム **AVSpeechSynthesizer** (TTS) が使用されます。 iHTC Studio には文章テキストは送信されません。
- **ウィジェットとアプリ グループ** - ウィジェットとアプリは、デバイス上のアプリ グループ `group.com.iHTCboy.iLiezi` を介して設定を共有します。
- **毎日の通知** — ローカルでスケジュールされます。 通知をタップすると、デバイス上でディープリンクが開きます。
- **学習カード** — 画像はデバイス上でレンダリングされます。 保存すると、[保存] をタップした場合にのみ **フォト ライブラリの追加のみ**が使用されます。
- **手書き検索 (iOS)** - オプションの文字認識では、デバイス上の Apple **Vision** を使用します。 ストロークはアップロードされません。
- **オプションのチップ** - 「チップ開発者」は、Apple によって処理される消耗品 **StoreKit** の購入です。
- **Siri / ショートカット / コントロール センター** — オプションのシステム統合により、デバイス上のディープ リンクが開きます。
- **オプションのスポットライト** — インデックス作成を有効にすると、システムはデバイス上のコンテンツにインデックスを付けます。

## 端末に保存されるデータ

 | データ | どこ | 目的 |
 |------|-------|-----------|
| 商君書ライブラリ | App / Widget バンドル | オフライン閲読と学習 |
 | お気に入りとリスト | アプリグループのUserDefaults | スター付きアイテムとユーザーリスト |
 | 読書履歴 / 最後に読んだ | アプリグループのUserDefaults | 続きを読む |
 | メモ | アプリグループのUserDefaults | あなたが書いた読書メモ |
 | 学習の進捗と習熟度 | アプリグループのUserDefaults | 教室/狩りの進行状況 |
 | 連続記録 / チェックイン | アプリグループのUserDefaults | 日々の習慣 |
 | 外観と読み取り設定 | アプリグループのUserDefaults | テーマ、言語、TTS、ウィジェット |
| Daily Reform cache & notification prefs | App Group UserDefaults | 今日の ID とスケジュール |
 | カードの好み | アプリグループのUserDefaults | 最後のスタイル/比率 |
 | オンボーディングと TipKit の状態 | 標準の UserDefaults | ウェルカムガイド |
 | ウィジェット / ライブ アクティビティのスナップショット | アプリグループ / ActivityKit | すでに開いているテキストを表示 |

 アプリをアンインストールすると、サンドボックスとアプリ グループのデータが削除されます (OS の動作に依存します)。 オプションの iCloud コピーは、クリアするまで **あなたの** iCloud に残ります。

## iCloud同期（オプション）

設定で**iCloud同期**を有効にすると、アプリは選択したユーザーデータをAppleの**`NSUbiquitousKeyValueStore`**を通じてあなたのApple IDに関連付けて同期します：

- お気に入り
 - リスト
- 読書履歴
- 学習進捗 / 習熟度
- 練習の連続日数
 - 注意事項

 同期トラフィックは iHTC Studio ではなく **Apple iCloud** に送信されます。 iCloud のコンテンツを読み取ることができません。

## 権限

 iLiezi は、機能が必要な場合にのみアクセス許可を要求します。

| 権限 | タイミング | 理由 |
|------------|------|-----|
| 通知 | Daily Reform reminders を有効にする | ローカルスケジュール |
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

 iLiezi は一般向けの読み書き教育アプリであり、キッズ カテゴリには含まれません**。 当社は故意に子供から個人情報を収集しません。 家族は各自のデバイスでオフラインで読書および学習機能を使用できます。

## 第三者

 - **Apple** — App Store ディストリビューション、オプションの StoreKit、オプションの iCloud KVS、システム TTS、選択した共有シートの宛先、および OS レベルの通知 / ライブ アクティビティ / Siri / ショートカット / ビジョン配信。
- 広告、分析、ソーシャルログインのデータ収集のために**他のサードパーティSDKは含まれていません**。

## 国際ユーザー

このアプリは、お使いのデバイス上でオフラインで機能するように設計されています。オプションのAppleサービスは、Appleの利用規約および地域での利用可能性に従います。

## データ保持と削除

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

iHTC Studio("당사", "당사" 또는 "우리의")는 **iLiezi**("爱列子 / 愛列子"라고도 함, 번들 ID `com.iHTCboy.iLiezi`)를 구축했습니다. 본 개인정보 보호정책은 귀하가 앱을 사용할 때 처리되는 데이터와 처리되지 않는 데이터에 대해 설명합니다. **Apple App Review** 및 사용자는 **이 페이지**를 공개 개인 정보 보호 정책으로 사용할 수 있습니다. App Store Connect의 경우 브라우저에서 이 개인정보 보호정책을 열고 주소 표시줄에서 주소를 복사하세요(공개 사이트 도메인은 시간이 지남에 따라 변경될 수 있음).

## 요약 (Apple 개인정보 영양성분표 정렬)

| 주제 | 당사의 정책 |
|-------|----------------|
| 계정 | **필요 없음** — 등록, 이메일 로그인, 전화번호 필요 없음 |
| iHTC 스튜디오의 데이터 수집 | **데이터 수집 없음** — 개인 데이터를 받는 백엔드를 운영하지 않습니다 |
| 네트워크 | 라이브러리, 읽기, 암기, 학습, Hunt, 위젯, 일일 알림은 설치 후 **오프라인**에서도 작동 |
| 분석 / 광고 / 추적 | **없음** — 타사 분석, 광고, 추적 SDK 없음; 앱 추적 투명성(App Tracking Transparency) 사용 없음 |
| 선택적 Apple 서비스 | **iCloud** (개인 KVS), 학습 카드용 **사진 라이브러리(추가만 가능)**, 선택적 팁용 **StoreKit**, **로컬 알림**, 선택적 **Live Activities**, 선택적 기기 내 **손글씨**(Vision) |

## 데이터 수집

개인 정보를 광고나 분석 목적으로 **수집, 판매, 공유하지 않습니다**.

- **계정 불필요** — 계정을 만들지 않아도 모든 핵심 기능을 사용할 수 있습니다.
- **분석 및 광고 없음** — 앱 바이너리는 당사로 데이터를 전송하는 타사 분석, 광고, 크래시 리포트 SDK를 통합하지 않습니다.
- **콘텐츠 업로드 없음** — 읽기 기록, 즐겨찾기, 목록, 메모, 학습 진행, 설정은 기기(및 선택적으로 **사용자의** iCloud)에만 남습니다. **이 앱용 서버를 운영하지 않으므로** iHTC Studio 서버로 업로드되지 않습니다.

이 텍스트는 **전국 제도사**입니다. **가혹한 형벌 옹호가 아닙니다**.

## 앱 작동 방식

- **번들 라이브러리** — 텍스트 JSON, 모국어/영어, 색인 및 학습 보조 자료가 앱/위젯 번들 내에 포함되어 있습니다.
- **기기 내 음성** — 암송은 Apple 시스템 **AVSpeechSynthesizer**(TTS)를 사용합니다. iHTC Studio에는 문구 텍스트를 보내지 않습니다.
- **위젯 및 앱 그룹** — 위젯과 앱은 기기의 앱 그룹 `group.com.iHTCboy.iLiezi`을(를) 통해 기본 설정을 공유합니다.
- **매일 알림** — 로컬로 예약됩니다. 알림을 탭하면 기기에서 딥 링크가 열립니다.
- **학습 카드** — 이미지가 장치에서 렌더링됩니다. 저장은 저장을 탭한 경우에만 **사진 라이브러리 추가 전용**을 사용합니다.
- **필기 검색(iOS)** — 선택적 문자 인식은 장치에서 Apple **Vision**을 사용합니다. 스트로크는 업로드되지 않습니다.
- **선택적 팁** — "팁 개발자"는 Apple에서 처리하는 소모품 **StoreKit** 구매입니다.
- **Siri / 바로가기 / 제어 센터** — 선택적 시스템 통합으로 기기 내 딥 링크가 열립니다.
- **선택적 스포트라이트** — 인덱싱을 활성화하면 시스템이 장치의 콘텐츠를 인덱싱합니다.

## 귀하의 장치에 저장된 데이터

| 데이터 | 어디 | 목적 |
|------|-------|---------|
| 상군서 라이브러리 | App / Widget 번들 | 오프라인 읽기·학습 |
| 즐겨찾기 및 목록 | 앱 그룹 UserDefaults | 별표 표시된 항목 및 사용자 목록 |
| 읽은 이력/마지막 읽은 내용 | 앱 그룹 UserDefaults | 계속 읽기 |
| 메모 | 앱 그룹 UserDefaults | 당신이 쓴 메모 읽기 |
| 학습 진행 및 숙달 | 앱 그룹 UserDefaults | 교실/사냥 진행 |
| 연속/체크인 | 앱 그룹 UserDefaults | 일상습관 |
| 모양 및 읽기 기본 설정 | 앱 그룹 UserDefaults | 테마, 언어, TTS, 위젯 |
| Daily Reform cache & notification prefs | App Group UserDefaults | 오늘 ID and schedule |
| 카드 환경설정 | 앱 그룹 UserDefaults | 마지막 스타일/비율 |
| 온보딩 및 TipKit 상태 | 표준 사용자 기본값 | 환영 가이드 |
| 위젯/실시간 활동 스냅샷 | 앱 그룹/ActivityKit | 이미 열어본 텍스트 표시 |

앱을 제거하면 샌드박스 및 앱 그룹 데이터가 제거됩니다(OS 동작에 따라 다름). 선택적인 iCloud 사본은 귀하가 삭제할 때까지 **귀하의** iCloud에 남아 있습니다.

## iCloud 동기화 (선택 사항)

설정에서 **iCloud 동기화**를 활성화하면, 앱은 **귀하의 Apple ID**와 연결된 Apple의 **`NSUbiquitousKeyValueStore`**를 통해 선택한 사용자 데이터를 미러링합니다:

- 즐겨찾기
- 목록
- 읽기 기록
- 학습 진행/숙련도
- 연습 연속 기록
- 메모

동기화 트래픽은 iHTC Studio가 아닌 **Apple iCloud**로 이동합니다. 귀하의 iCloud 콘텐츠를 읽을 수 없습니다.

## 권한

iLiezi는 기능에 필요한 경우에만 권한을 요청합니다.

| 허가 | 언제 | 왜? |
|------------|------|-----|
| 알림 | Daily Reform reminders 사용 | 로컬 예약 |
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

iLiezi는 일반 청중을 위한 교육용 읽기 쓰기 앱이며 어린이 카테고리에 **아닙니다**. 우리는 어린이로부터 고의로 개인정보를 수집하지 않습니다. 가족은 자신의 기기에서 오프라인으로 독서 및 학습 기능을 사용할 수 있습니다.

## 제3자

- **Apple** — App Store 배포, 선택적 StoreKit, 선택적 iCloud KVS, 시스템 TTS, 선택한 공유 시트 대상 및 OS 수준 알림/실시간 활동/Siri/바로가기/비전 전달.
- 광고, 분석, 소셜 로그인 등을 위한 **기타 제3자 SDK**는 데이터 수집을 위해 포함되지 않았습니다.

## 국제 사용자

앱은 사용자의 장치에서 오프라인 기능이 가능하도록 설계되었습니다. 선택적 Apple 서비스는 Apple의 이용 약관 및 지역 가용성을 따릅니다.

## 데이터 보존 및 삭제

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

iHTC Studio («мы», «нас» или «наш») создала **iLiezi** (также известное как «爱列子 / 愛列子», Bundle ID `com.iHTCboy.iLiezi`). Эта Политика конфиденциальности объясняет, какие данные обрабатываются (и не обрабатываются) при использовании приложения. **Apple App Review** и пользователи могут ссылаться на **эту страницу** как на публичную политику конфиденциальности. Для App Store Connect откройте эту Политику конфиденциальности в браузере и скопируйте адрес из адресной строки (домен публичного сайта может со временем поменяться).

## Сводка (в соответствии с меткой Apple Privacy Nutrition)

| Тема | Наша практика |
|-------|----------------|
| Учетная запись | **Не требуется** — регистрация, вход по электронной почте или номеру телефона не нужны |
| Сбор данных iHTC Studio | **Данные не собираются** — мы **не** используем серверную часть, которая получает ваши личные данные |
| Сеть | Библиотека, чтение, повторение, учеба, Охота, виджеты и ежедневные уведомления работают **оффлайн** после установки |
| Аналитика / реклама / отслеживание | **Отсутствует** — нет сторонней аналитики, рекламы или SDK для отслеживания; не используется App Tracking Transparency |
| Опциональные сервисы Apple | **iCloud** (ваш личный KVS), **Фототека (только добавление)** для учебных карточек, **StoreKit** для опциональных чаевых, **локальные уведомления**, опционально **Live Activities**, опционально на устройстве **ручное письмо** (Vision) |

## Сбор данных

Мы **не** собираем, не продаем и не делимся личной информацией для рекламы или аналитики.

- **Без аккаунта** — Вы можете использовать все основные функции без создания аккаунта у нас.
- **Без аналитики и рекламы** — В приложении не интегрированы сторонние SDK для аналитики, рекламы или отчётов о сбоях, которые отправляли бы данные нам.
- **Без загрузки контента** — история чтения, избранное, списки, заметки, прогресс обучения и настройки остаются на устройстве (и, по желанию, в **вашем** iCloud). Они не загружаются на серверы iHTC Studio, потому что **мы не эксплуатируем такие серверы для этого приложения**.

Тексты относятся к **истории институтов Сражающихся царств**. **Не** пропаганда жестоких наказаний.

## Как работает приложение

- **Встроенная библиотека**. Текст в формате JSON, на местном/английском языке, указатели и учебные пособия поставляются в комплекте приложения/виджета.
- **Речь на устройстве** — при декламации используется система Apple **AVSpeechSynthesizer** (TTS). Мы не отправляем текст прохождения в iHTC Studio.
- **Виджеты и группа приложений** — виджеты и настройки приложения делятся через группу приложений `group.com.iHTCboy.iLiezi` на вашем устройстве.
- **Ежедневные уведомления** — по расписанию. При нажатии на уведомление открывается глубокая ссылка на устройстве.
- **Обучающие карточки** — изображения обрабатываются на устройстве. При сохранении используется **Дополнение «Библиотека фотографий»** только при нажатии «Сохранить».
- **Поиск по рукописному вводу (iOS)** — дополнительное распознавание символов использует Apple **Vision** на устройстве. Штрихи не загружаются.
- **Необязательный совет**. «Tip Developer» — это расходный материал, приобретаемый **StoreKit** и обрабатываемый Apple.
- **Siri / Ярлыки / Центр управления** — дополнительные системные интеграции открывают глубокие ссылки на устройстве.
- **Дополнительный Spotlight** — если вы включите индексирование, система будет индексировать контент на устройстве.

## Данные, хранящиеся на вашем устройстве

| Данные | Где | Цель |
|------|-------|---------|
| Библиотека Shangjunshu | Пакет App / Widget | Офлайн-чтение и обучение |
| Избранное и списки | Пользовательские настройки группы приложений | Избранные элементы и списки пользователей |
| История чтения / последнее чтение | Пользовательские настройки группы приложений | Продолжить чтение |
| Заметки | Пользовательские настройки группы приложений | Чтение заметок, которые вы пишете |
| Ход учебы и мастерство | Пользовательские настройки группы приложений | Прогресс в классе/охоте |
| Полоса / регистрация | Пользовательские настройки группы приложений | Ежедневная привычка |
| Настройки внешнего вида и чтения | Пользовательские настройки группы приложений | Тема, язык, TTS, виджеты |
| Daily Reform cache & notification prefs | UserDefaults App Group | ID на сегодня, время, переключатели |
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

iLiezi запрашивает разрешения только тогда, когда они нужны функции:

| Разрешение | Когда | Почему |
|------------|------|-----|
| Уведомления | Вы включаете Daily Reform reminders | Локальное планирование |
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

iLiezi — это образовательное приложение для широкой аудитории, которое **не** в категории «Дети». Мы сознательно не собираем личную информацию от детей. Семьи могут использовать функции чтения и обучения в автономном режиме на своих устройствах.

## Третьи стороны

- **Apple** — распространение в App Store, дополнительный StoreKit, дополнительный iCloud KVS, системный TTS, выбранные вами места назначения Share Sheet, а также уведомления на уровне ОС / Live Activity / Siri / Ярлыки / Доставка Vision.
- **Никакие другие сторонние SDK** для рекламы, аналитики или социальной авторизации не включены для сбора данных.

## Пользователи из других стран

Приложение предназначено для работы в автономном режиме на вашем устройстве. Необязательные сервисы Apple подчиняются условиям Apple и региональной доступности.

## Сроки хранения и удаление данных

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

iHTC Studio ("เรา", "พวกเรา" หรือ "ของเรา") ได้สร้าง **iLiezi** (ซึ่งรู้จักกันในชื่อ "爱列子 / 愛列子", Bundle ID `com.iHTCboy.iLiezi`) นโยบายความเป็นส่วนตัวนี้อธิบายว่าข้อมูลใดบ้างที่ถูกจัดการ (และไม่ได้ถูกจัดการ) เมื่อคุณใช้แอป **Apple App Review** และผู้ใช้สามารถอ้างอิง **หน้านี้** เป็นนโยบายความเป็นส่วนตัวสาธารณะ สำหรับ App Store Connect ให้เปิดนโยบายความเป็นส่วนตัวนี้ในเบราว์เซอร์ของคุณและคัดลอกที่อยู่จากแถบที่อยู่ (โดเมนของเว็บไซต์สาธารณะอาจเปลี่ยนแปลงได้ตามเวลา)

## สรุป (การจัดตำแหน่งกับ Nutrition Label ความเป็นส่วนตัวของ Apple)

| หัวข้อ | การปฏิบัติของเรา |
|-------|----------------|
| บัญชี | **ไม่จำเป็น** — ไม่ต้องลงทะเบียน ลงชื่อเข้าใช้ด้วยอีเมล หรือหมายเลขโทรศัพท์ |
| การเก็บข้อมูลโดย iHTC Studio | **ไม่เก็บข้อมูล** — เรา **ไม่ได้**ดำเนินการแบ็กเอนด์ที่รับข้อมูลส่วนตัวของคุณ |
| เครือข่าย | ห้องสมุด การอ่าน การท่องจำ การศึกษา การล่า วิดเจ็ต และการแจ้งเตือนประจำวันทำงาน **ออฟไลน์** หลังการติดตั้ง |
| การวิเคราะห์ / โฆษณา / การติดตาม | **ไม่มี** — ไม่มี SDK การวิเคราะห์ โฆษณา หรือการติดตามจากบุคคลที่สาม; ไม่ใช้ App Tracking Transparency |
| บริการของ Apple ที่เลือกใช้ได้ | **iCloud** (KVS ส่วนตัวของคุณ), **คลังรูปภาพ (เพิ่มได้เท่านั้น)** สำหรับการ์ดศึกษา, **StoreKit** สำหรับการให้ทิปที่เลือกได้, **การแจ้งเตือนภายในเครื่อง**, **กิจกรรมสด (Live Activities)** ที่เลือกได้, **การเขียนด้วยมือบนอุปกรณ์ (Vision)** ที่เลือกได้ |

## การเก็บข้อมูล

เราจะ **ไม่**เก็บ ขาย หรือแชร์ข้อมูลส่วนบุคคลเพื่อโฆษณาหรือการวิเคราะห์

- **ไม่ต้องมีบัญชีผู้ใช้** — คุณสามารถใช้คุณสมบัติหลักทั้งหมดได้โดยไม่ต้องสร้างบัญชีกับเรา
- **ไม่มีการวิเคราะห์หรือโฆษณา** — ไฟล์แอปไม่ได้รวม SDK การวิเคราะห์ การโฆษณา หรือการรายงานข้อผิดพลาดจากบุคคลที่สามที่ติดต่อกลับไปยังเรา
- **ไม่อัปโหลดเนื้อหา** — ประวัติการอ่าน รายการโปรด รายการ บันทึก ความคืบหน้าการเรียน และการตั้งค่าอยู่บนอุปกรณ์ (และอาจอยู่ใน iCloud **ของคุณ**) จะไม่ถูกอัปโหลดไปยังเซิร์ฟเวอร์ iHTC Studio เพราะ **เราไม่ได้ดำเนินการเซิร์ฟเวอร์เช่นนั้นสำหรับแอปนี้**

ข้อความเป็น**ประวัติราชการยุค战国** **ไม่ใช่**สนับสนุนโทษหนัก

## วิธีการทำงานของแอป

- **ไลบรารีที่รวมกลุ่ม** — ข้อความ JSON ภาษาพื้นถิ่น/อังกฤษ ดัชนี และตัวช่วยในการเรียนจะจัดส่งภายในชุดแอป/วิดเจ็ต
- **คำพูดบนอุปกรณ์** — การบรรยายใช้ระบบของ Apple **AVSpeechSynthesizer** (TTS) เราไม่ส่งข้อความข้อความไปที่ iHTC Studio
- **วิดเจ็ตและกลุ่มแอป** — วิดเจ็ตและแอปแชร์การตั้งค่าผ่านกลุ่มแอป `group.com.iHTCboy.iLiezi` บนอุปกรณ์ของคุณ
- **การแจ้งเตือนรายวัน** — กำหนดเวลาในเครื่อง การแตะการแจ้งเตือนจะเปิดลิงก์ในรายละเอียดบนอุปกรณ์
- **การ์ดการศึกษา** — รูปภาพถูกเรนเดอร์บนอุปกรณ์ การบันทึกจะใช้ **เฉพาะส่วนเสริมคลังรูปภาพ** เฉพาะเมื่อคุณแตะบันทึก
- **การค้นหาด้วยลายมือ (iOS)** — ตัวเลือกการรู้จำอักขระใช้ Apple **Vision** บนอุปกรณ์ จังหวะไม่ได้อัปโหลด
- **เคล็ดลับเสริม** — “Tip Developer” เป็นการซื้อ **StoreKit** แบบบริโภคที่ดำเนินการโดย Apple
- **Siri / ทางลัด / ศูนย์ควบคุม** — การบูรณาการระบบที่เป็นตัวเลือกจะเปิดลิงก์ในรายละเอียดบนอุปกรณ์
- **สปอตไลท์เสริม** — หากคุณเปิดใช้งานการจัดทำดัชนี ระบบจะจัดทำดัชนีเนื้อหาบนอุปกรณ์

## ข้อมูลที่เก็บบนอุปกรณ์

| ข้อมูล | ที่ไหน | วัตถุประสงค์ |
|------|-------|---------|
| คลัง Shangjunshu | App / Widget bundle | อ่านและเรียนออฟไลน์ |
| รายการโปรดและรายการ | ค่าเริ่มต้นของกลุ่มแอป | รายการที่ติดดาวและรายชื่อผู้ใช้ |
| ประวัติการอ่าน / อ่านครั้งล่าสุด | ค่าเริ่มต้นของกลุ่มแอป | อ่านต่อ |
| หมายเหตุ | ค่าเริ่มต้นของกลุ่มแอป | อ่านบันทึกที่คุณเขียน |
| ความก้าวหน้าและความเชี่ยวชาญด้านการศึกษา | ค่าเริ่มต้นของกลุ่มแอป | ห้องเรียน / ล่าความคืบหน้า |
| สตรีค/เช็คอิน | ค่าเริ่มต้นของกลุ่มแอป | นิสัยประจำวัน |
| ลักษณะที่ปรากฏและการตั้งค่าการอ่าน | ค่าเริ่มต้นของกลุ่มแอป | ธีม, ภาษา, TTS, วิดเจ็ต |
| Daily Reform cache & notification prefs | UserDefaults ของ App Group | ID วันนี้ and schedule |
| การตั้งค่าการ์ด | ค่าเริ่มต้นของกลุ่มแอป | รูปแบบสุดท้าย / อัตราส่วน |
| การเริ่มต้นใช้งานและสถานะ TipKit | ค่าเริ่มต้นของผู้ใช้มาตรฐาน | คู่มือต้อนรับ |
| วิดเจ็ต / ภาพรวมกิจกรรมสด | กลุ่มแอป / ActivityKit | แสดงข้อความที่คุณเปิดแล้ว |

การถอนการติดตั้งแอปจะลบข้อมูลแซนด์บ็อกซ์และกลุ่มแอป (ขึ้นอยู่กับพฤติกรรมของระบบปฏิบัติการ) สำเนา iCloud ที่เป็นตัวเลือกจะยังคงอยู่ใน iCloud **ของคุณ** จนกว่าคุณจะล้างข้อมูลเหล่านั้น

## การซิงค์ iCloud (ตัวเลือก)

หากคุณเปิดใช้งาน **การซิงค์ iCloud** ในการตั้งค่า แอปจะสะท้อนข้อมูลผู้ใช้ที่เลือกผ่าน **`NSUbiquitousKeyValueStore`** ของ Apple ที่เชื่อมโยงกับ **Apple ID ของคุณ**:

- รายการโปรด
- รายการ
- ประวัติการอ่าน
- ความคืบหน้า/ความชำนาญในการศึกษา
- สถิติการฝึกต่อเนื่อง
- หมายเหตุ

การรับส่งข้อมูลการซิงค์ไปที่ **Apple iCloud** ไม่ใช่ไปที่ iHTC Studio เราไม่สามารถอ่านเนื้อหา iCloud ของคุณได้

## สิทธิ์

iLiezi ร้องขอการอนุญาตเฉพาะเมื่อคุณสมบัติต้องการ:

| สิทธิ์ | เมื่อไหร่ | ทำไม |
|------------|------|-----|
| การแจ้งเตือน | คุณเปิด Daily Reform reminders | กำหนดเวลาในเครื่อง |
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

iLiezi เป็นแอปความรู้ด้านการศึกษาสำหรับผู้ชมทั่วไป และ **ไม่** อยู่ในหมวดหมู่เด็ก เราไม่รวบรวมข้อมูลส่วนบุคคลจากเด็กโดยเจตนา ครอบครัวอาจใช้คุณสมบัติการอ่านและการศึกษาแบบออฟไลน์บนอุปกรณ์ของตนเอง

## บุคคลที่สาม

- **Apple** — การจำหน่าย App Store, StoreKit ที่เป็นตัวเลือก, iCloud KVS ที่เป็นตัวเลือก, TTS ระบบ, ปลายทาง Share Sheet ที่คุณเลือก และการแจ้งเตือนระดับระบบปฏิบัติการ / กิจกรรมสด / Siri / ทางลัด / การส่งมอบวิสัยทัศน์
- **ไม่มี SDK ของบุคคลที่สามอื่น ๆ** สำหรับโฆษณา, การวิเคราะห์, หรือการเข้าสู่ระบบโซเชียลรวมอยู่เพื่อการเก็บข้อมูล

## ผู้ใช้ระหว่างประเทศ

แอปออกแบบมาให้ทำงานแบบออฟไลน์บนอุปกรณ์ของคุณ บริการของ Apple ตามตัวเลือกจะเป็นไปตามข้อกำหนดของ Apple และความพร้อมใช้งานในภูมิภาค

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

iHTC Studio ("wir", "uns" oder "unser") hat **iLiezi** (auch bekannt als "爱列子 / 愛列子", Bundle-ID `com.iHTCboy.iLiezi`) entwickelt. Diese Datenschutzerklärung erklärt, welche Daten beim Verwenden der App verarbeitet werden (und welche nicht). **Apple App Review** und Benutzer können sich auf **diese Seite** als die öffentliche Datenschutzerklärung verlassen. Für App Store Connect öffnen Sie diese Datenschutzerklärung in Ihrem Browser und kopieren die Adresse aus der Adressleiste (die Domain der öffentlichen Seite kann sich im Laufe der Zeit ändern).

## Zusammenfassung (Übereinstimmung mit dem Apple-Datenschutzetikett)

| Thema | Unsere Praxis |
|-------|----------------|
| Konto | **Nicht erforderlich** — keine Registrierung, kein E-Mail-Login oder Telefonnummer erforderlich |
| Datenerhebung durch iHTC Studio | **Keine Datenerhebung** — wir betreiben **keinen** Backend-Service, der Ihre persönlichen Daten empfängt |
| Netzwerk | Bibliothek, Lesen, Rezitieren, Lernen, Hunt, Widgets und tägliche Benachrichtigungen funktionieren **offline** nach der Installation |
| Analysen / Werbung / Tracking | **Keine** — keine Analysen von Drittanbietern, Werbung oder Tracking-SDKs; keine Nutzung von App Tracking Transparency |
| Optionale Apple-Dienste | **iCloud** (Ihr privates KVS), **Fotomediathek (Nur hinzufügen)** für Lernkarten, **StoreKit** für optionales Trinkgeld, **lokale Benachrichtigungen**, optionale **Live-Aktivitäten**, optional **handschriftliche Eingabe** auf dem Gerät (Vision) |

## Datenerfassung

Wir erheben, verkaufen oder teilen **keine** persönlichen Informationen für Werbung oder Analysen.

- **Kein Konto** — Sie können alle Kernfunktionen nutzen, ohne ein Konto bei uns zu erstellen.
- **Keine Analysen oder Werbung** — Die App-Binärdatei integriert keine Analysen, Werbung oder Crash-Reporting-SDKs von Drittanbietern, die Daten an uns senden.
- **Kein Hochladen von Inhalten** — Leseverlauf, Favoriten, Listen, Notizen, Lernfortschritt und Einstellungen bleiben auf dem Gerät (optional in **Ihrem** iCloud). Sie werden nicht auf iHTC Studio-Server hochgeladen, da **wir für diese App keine solchen Server betreiben**.

Texte der **Institutionsgeschichte der Streitenden Reiche**. **Keine** Plädoyer für harte Strafen.

## So funktioniert die App

- **Gebündelte Bibliothek** – JSON-Text, Umgangssprache/Englisch, Indizes und Lernhilfen sind im App-/Widget-Paket enthalten.
- **Sprache auf dem Gerät** – Die Rezitation nutzt Apples System **AVSpeechSynthesizer** (TTS). Wir senden keine Passagentexte an iHTC Studio.
- **Widgets & App-Gruppe** – Widgets und die App-Freigabeeinstellungen über die App-Gruppe `group.com.iHTCboy.iLiezi` auf Ihrem Gerät.
- **Tägliche Benachrichtigungen** – Lokal geplant. Durch Tippen auf eine Benachrichtigung wird ein Deep-Link auf dem Gerät geöffnet.
- **Lernkarten** – Bilder werden auf dem Gerät gerendert. Beim Speichern wird **nur die Add-On-Fotobibliothek** verwendet, wenn Sie auf „Speichern“ tippen.
- **Handschriftsuche (iOS)** – Die optionale Zeichenerkennung verwendet Apple **Vision** auf dem Gerät. Striche werden nicht hochgeladen.
- **Optionaler Tipp** – „Tip Developer“ ist ein verbrauchbarer **StoreKit**-Kauf, der von Apple abgewickelt wird.
- **Siri / Verknüpfungen / Kontrollzentrum** – Optionale Systemintegrationen öffnen Deep Links auf dem Gerät.
- **Optionales Spotlight** – Wenn Sie die Indizierung aktivieren, indiziert das System Inhalte auf dem Gerät.

## Auf Ihrem Gerät gespeicherte Daten

| Daten | Wo | Zweck |
|------|-------|---------|
| Shangjunshu-Bibliothek | App-/Widget-Bundle | Offline-Lesen und -Lernen |
| Favoriten & Listen | Benutzerstandards der App-Gruppe | Markierte Elemente und Benutzerlisten |
| Leseverlauf / zuletzt gelesen | Benutzerstandards der App-Gruppe | Weiterlesen |
| Notizen | Benutzerstandards der App-Gruppe | Lesen von Notizen, die Sie schreiben |
| Studienfortschritt & Beherrschung | Benutzerstandards der App-Gruppe | Unterrichts-/Jagdfortschritt |
| Streak / Check-in | Benutzerstandards der App-Gruppe | Tägliche Gewohnheit |
| Aussehen & Lesepräferenzen | Benutzerstandards der App-Gruppe | Thema, Sprache, TTS, Widgets |
| Daily Reform cache & notification prefs | UserDefaults der App Group | Heutige ID and schedule |
| Karteneinstellungen | Benutzerstandards der App-Gruppe | Letzter Stil / Verhältnis |
| Onboarding- und TipKit-Status | Standardbenutzerstandards | Willkommensführer |
| Widget-/Live-Aktivitäts-Schnappschüsse | App-Gruppe / ActivityKit | Text anzeigen, den Sie bereits geöffnet haben |

Durch die Deinstallation der App werden Sandbox- und App-Gruppendaten entfernt (je nach Betriebssystemverhalten). Optionale iCloud-Kopien bleiben in **Ihrer** iCloud, bis Sie sie löschen.

## iCloud-Synchronisierung (optional)

Wenn du **iCloud-Synchronisierung** in den Einstellungen aktivierst, spiegelt die App ausgewählte Benutzerdaten über Apples **`NSUbiquitousKeyValueStore`**, die mit **deiner Apple-ID** verknüpft ist:

- Favoriten
- Listen
- Leseverlauf
- Lernfortschritt / Kenntnisse
- Übungsserien
- Notizen

Der Synchronisierungsverkehr geht an **Apple iCloud**, nicht an iHTC Studio. Wir können Ihre iCloud-Inhalte nicht lesen.

## Berechtigungen

iLiezi fordert Berechtigungen nur an, wenn eine Funktion diese benötigt:

| Erlaubnis | Wann | Warum |
|------------|------|-----|
| Benachrichtigungen | Sie aktivieren Daily Reform reminders | Lokale Planung |
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

iLiezi ist eine Bildungs- und Lesekompetenz-App für ein allgemeines Publikum und gehört **nicht** zur Kategorie „Kinder“. Wir erfassen wissentlich keine personenbezogenen Daten von Kindern. Familien können Lese- und Lernfunktionen offline auf ihren eigenen Geräten nutzen.

## Dritte Parteien

- **Apple** – App Store-Verteilung, optionales StoreKit, optionales iCloud KVS, System-TTS, von Ihnen ausgewählte Share Sheet-Ziele und Benachrichtigung auf Betriebssystemebene/Live-Aktivität/Siri/Verknüpfungen/Vision-Bereitstellung.
- **Keine weiteren Drittanbieter-SDKs** für Werbung, Analysen oder Social-Login sind zur Datenerfassung enthalten.

## Internationale Nutzer

Die App ist darauf ausgelegt, offline auf Ihrem Gerät zu funktionieren. Optionale Apple-Dienste unterliegen den Bedingungen von Apple und der regionalen Verfügbarkeit.

## Datenaufbewahrung & Löschung

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

iHTC Studio (« nous », « notre » ou « nos ») a créé **iLiezi** (également connu sous le nom de « 爱列子 / 愛列子 », ID de bundle `com.iHTCboy.iLiezi`). Cette politique de confidentialité explique quelles données sont (et ne sont pas) traitées lorsque vous utilisez l'application. **Apple App Review** et les utilisateurs peuvent se référer à **cette page** comme politique de confidentialité publique. Pour App Store Connect, ouvrez cette politique de confidentialité dans votre navigateur et copiez l'adresse depuis la barre d'adresse (le domaine du site public peut changer avec le temps).

## Résumé (alignement sur l'étiquette nutritionnelle de confidentialité Apple)

| Sujet | Notre pratique |
|-------|----------------|
| Compte | **Non requis** — pas d'inscription, de connexion par e-mail ou de numéro de téléphone |
| Collecte de données par iHTC Studio | **Données non collectées** — nous n'exploitons **pas** de backend qui reçoit vos données personnelles |
| Réseau | La bibliothèque, la lecture, la récitation, l'étude, la chasse, les widgets et les notifications quotidiennes fonctionnent **hors ligne** après l'installation |
| Analyses / publicités / suivi | **Aucun** — pas de SDK tiers d'analyse, de publicité ou de suivi ; pas d'utilisation de la transparence du suivi des applications |
| Services Apple optionnels | **iCloud** (votre KVS privé), **Photothèque (ajout uniquement)** pour les cartes d’étude, **StoreKit** pour les pourboires optionnels, **notifications locales**, **Live Activities** optionnel, **écriture manuscrite sur appareil** optionnelle (Vision) |

## Collecte de données

Nous ne collectons, vendons ou partageons **pas** d'informations personnelles à des fins publicitaires ou analytiques.

- **Aucun compte** — Vous pouvez utiliser toutes les fonctionnalités principales sans créer de compte chez nous.
- **Aucune analyse ni publicité** — Le binaire de l'application n'intègre pas de SDK tiers d'analyse, de publicité ou de rapport d'erreur qui nous contactent.
- **Aucun envoi de contenu** — historique, favoris, listes, notes, progression d’étude et préférences restent sur l’appareil (et, en option, dans **votre** iCloud). Ils ne sont jamais envoyés aux serveurs iHTC Studio car **nous n’exploitons pas de tels serveurs pour cette app**.

Textes d’**histoire institutionnelle des Royaumes combattants**. **Pas** de plaidoyer pour peines sévères.

## Comment fonctionne l'application

- **Bibliothèque groupée** — Texte JSON, langue vernaculaire/anglais, index et aides à l'étude livrés dans l'ensemble application/widget.
- **Discours sur l'appareil** — La récitation utilise le système **AVSpeechSynthesizer** (TTS) d'Apple. Nous n'envoyons pas de texte de passage à iHTC Studio.
- **Widgets et groupe d'applications** — Les widgets et l'application partagent les préférences via le groupe d'applications `group.com.iHTCboy.iLiezi` sur votre appareil.
- **Notifications quotidiennes** — Planifiées localement. Appuyer sur une notification ouvre un lien profond sur l'appareil.
- **Cartes d'étude** — Les images sont rendues sur l'appareil. L'enregistrement utilise **le module complémentaire Photothèque** uniquement lorsque vous appuyez sur Enregistrer.
- **Recherche d'écriture manuscrite (iOS)** : la reconnaissance de caractères facultative utilise Apple **Vision** sur l'appareil. Les traits ne sont pas téléchargés.
- **Conseil facultatif** — « Tip Developer » est un achat de consommable **StoreKit** traité par Apple.
- **Siri / Raccourcis / Centre de contrôle** — Les intégrations système facultatives ouvrent des liens profonds sur l'appareil.
- **Spotlight facultatif** : si vous activez l'indexation, le système indexe le contenu sur l'appareil.

## Données stockées sur votre appareil

| Données | Où | Objectif |
|------|-------|--------------|
| Bibliothèque Shangjunshu | Bundle App / Widget | Lecture et étude hors ligne |
| Favoris et listes | Paramètres par défaut du groupe d'applications | Éléments favoris et listes d'utilisateurs |
| Historique de lecture / dernière lecture | Paramètres par défaut du groupe d'applications | Continuer la lecture |
| Remarques | Paramètres par défaut du groupe d'applications | Notes de lecture que vous écrivez |
| Avancement et maîtrise des études | Paramètres par défaut du groupe d'applications | Classe / Progrès de la chasse |
| Série / enregistrement | Paramètres par défaut du groupe d'applications | Habitude quotidienne |
| Apparence et préférences de lecture | Paramètres par défaut du groupe d'applications | Thème, langue, TTS, widgets |
| Daily Reform cache & notification prefs | UserDefaults de l’App Group | ID du jour and schedule |
| Préférences de carte | Paramètres par défaut du groupe d'applications | Dernier style/ratio |
| État d’intégration et de TipKit | Valeurs par défaut de l'utilisateur standard | Guide de bienvenue |
| Widget / Instantanés d'activité en direct | Groupe d'applications / ActivityKit | Afficher le texte que vous avez déjà ouvert |

La désinstallation de l'application supprime les données du bac à sable et du groupe d'applications (sous réserve du comportement du système d'exploitation). Les copies iCloud facultatives restent dans **votre** iCloud jusqu'à ce que vous les effaciez.

## Synchronisation iCloud (Facultative)

Si vous activez **la synchronisation iCloud** dans les Réglages, l'application reflète les données utilisateur sélectionnées via le **`NSUbiquitousKeyValueStore`** d'Apple lié à **votre identifiant Apple** :

- Favoris
- Listes
- Historique de lecture
- Progression / maîtrise des études
- Séries de pratique
- Remarques

Le trafic de synchronisation va vers **Apple iCloud**, pas vers iHTC Studio. Nous ne pouvons pas lire votre contenu iCloud.

## Autorisations

iLiezi demande des autorisations uniquement lorsqu'une fonctionnalité en a besoin :

| Autorisation | Quand | Pourquoi |
|------------|------|-----|
| Notifications | Vous activez Daily Reform reminders | Planification locale |
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

iLiezi est une application d'alphabétisation éducative destinée à un public général et n'est **pas** dans la catégorie Enfants. Nous ne collectons pas sciemment d’informations personnelles auprès des enfants. Les familles peuvent utiliser les fonctionnalités de lecture et d’étude hors ligne sur leurs propres appareils.

## Tiers

- **Apple** — Distribution sur l'App Store, StoreKit en option, iCloud KVS en option, TTS système, destinations de feuille de partage que vous choisissez et notification au niveau du système d'exploitation/activité en direct/Siri/raccourcis/livraison Vision.
- **Aucun autre SDK tiers** pour la publicité, l'analyse ou la connexion sociale n'est inclus pour la collecte de données.

## Utilisateurs internationaux

L'application est conçue pour fonctionner hors ligne sur votre appareil. Les services Apple optionnels suivent les conditions et la disponibilité régionale d'Apple.

## Conservation et suppression des données

- **Sur l'appareil** — Supprimez l'application pour retirer les données locales du bac à sable et du groupe d'applications (sous réserve du comportement du système d'exploitation).
- **iCloud** — Désactivez la synchronisation et supprimez les clés associées de votre compte iCloud si nécessaire ; nous ne pouvons pas effacer votre iCloud pour vous.
- **Nous ne conservons rien** sur les serveurs iHTC Studio pour cette application car nous ne collectons pas ces données.

## Modifications de la politique

Nous pouvons mettre à jour cette politique de confidentialité. La date « Dernière mise à jour » en haut sera modifiée. L'utilisation continue après une mise à jour signifie que vous acceptez la politique révisée.

## Nous contacter

Questions sur la vie privée : [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="tr" markdown="1">

**Son güncelleme:** 19 Eylül 2026

iHTC Studio ("biz", "bize" veya "bizim") **iLiezi**yi (ayrıca "爱列子 / 愛列子" olarak da bilinir, Paket Kimliği `com.iHTCboy.iLiezi`) geliştirdi. Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlendiğini (ve hangilerinin işlenmediğini) açıklar. **Apple Uygulama İncelemesi** ve kullanıcılar, **bu sayfaya** kamuya açık gizlilik politikası olarak güvenebilir. App Store Connect için, bu Gizlilik Politikasını tarayıcınızda açın ve adres çubuğundan adresi kopyalayın (kamuya açık site alan adı zamanla değişebilir).

## Özet (Apple Gizlilik Beslenme Etiketi uyumu)

| Konu | Uygulamamızın uygulaması |
|-------|----------------|
| Hesap | **Gerekli değil** — kayıt, e-posta ile giriş veya telefon numarası yok |
| iHTC Studio tarafından veri toplama | **Veri Toplanmıyor** — kişisel verilerinizi alan bir arka uç işletmiyoruz |
| Ağ | Kütüphane, okuma, ezberleme, çalışma, avlanma, widgetlar ve günlük bildirimler kurulumdan sonra **çevrimdışı** çalışır |
| Analitik / reklam / izleme | **Yok** — üçüncü taraf analitik, reklam veya izleme SDK'ları yok; Uygulama İzleme Şeffaflığı kullanılmaz |
| İsteğe bağlı Apple hizmetleri | **iCloud** (özel KVS'niz), çalışma kartları için **Fotoğraf Kitaplığı (Sadece Ekleme)**, isteğe bağlı bahşişler için **StoreKit**, **yerel bildirimler**, isteğe bağlı **Canlı Aktiviteler**, cihazda isteğe bağlı **el yazısı** (Vision) |

## Veri Toplama

Kişisel bilgileri reklam veya analiz için **toplamıyoruz**, satmıyoruz veya paylaşmıyoruz.

- **Hesap gerekmez** — Tüm temel özellikleri bizde hesap oluşturmadan kullanabilirsiniz.
- **Analitik veya reklam yok** — Uygulama ikili dosyası üçüncü taraf analitik, reklam veya çökme bildirim SDK'larını içermez, telefonla bize veri göndermez.
- **İçerik yüklenmez** — Okuma geçmişi, favoriler, listeler, notlar, çalışma ilerlemesi ve tercihler cihazınızda (ve isteğe bağlı **iCloud’unuzda**) kalır. **Bu uygulama için böyle sunucular işletmediğimizden** iHTC Studio sunucularına yüklenmez.

Metinler **Savaşan Devletler kurum tarihi**. **Sert cezaları savunmaz**.

## Uygulama Nasıl Çalışır

- **Paketlenmiş kitaplık** — Metin JSON, yerel dil/İngilizce, dizinler ve çalışma yardımcıları uygulama/widget paketinin içinde gönderilir.
- **Cihaz içi konuşma** — Okuma, Apple'ın **AVSpeechSynthesizer** (TTS) sistemini kullanır. iHTC Studio'ya pasaj metni göndermiyoruz.
- **Widget'lar ve Uygulama Grubu** — Cihazınızdaki Uygulama Grubu `group.com.iHTCboy.iLiezi` aracılığıyla widget'lar ve uygulama paylaşım tercihleri.
- **Günlük bildirimler** — Yerel olarak planlanmıştır. Bir bildirime dokunduğunuzda cihazda derin bir bağlantı açılır.
- **Çalışma kartları** — Görüntüler cihazda oluşturulur. Kaydetme, **Yalnızca Fotoğraf Kitaplığı eklentisini** yalnızca kaydet'e dokunduğunuzda kullanır.
- **El yazısı araması (iOS)** — İsteğe bağlı karakter tanıma, cihazda Apple **Vision**'ı kullanır. Konturlar yüklenmedi.
- **İsteğe bağlı ipucu** — "İpucu Geliştirici", Apple tarafından gerçekleştirilen bir **StoreKit** sarf malzemesidir.
- **Siri / Kısayollar / Kontrol Merkezi** — İsteğe bağlı sistem entegrasyonları cihazdaki derin bağlantıları açar.
- **İsteğe Bağlı Spot Işığı** — Dizin oluşturmayı etkinleştirirseniz sistem, cihazdaki içeriği dizine ekler.

## Cihazınızda Saklanan Veriler

| Veri | Nerede | Amaç |
|------|-------|-------------|
| Shangjunshu kitaplığı | App / Widget paketi | Çevrimdışı okuma ve çalışma |
| Favoriler ve listeler | Uygulama Grubu Kullanıcı Varsayılanları | Yıldızlı öğeler ve kullanıcı listeleri |
| Okuma geçmişi / son okuma | Uygulama Grubu Kullanıcı Varsayılanları | Okumaya devam et |
| Notlar | Uygulama Grubu Kullanıcı Varsayılanları | Yazdığınız notları okuma |
| Çalışma ilerlemesi ve ustalık | Uygulama Grubu Kullanıcı Varsayılanları | Sınıf / Av ilerlemesi |
| Seri / giriş | Uygulama Grubu Kullanıcı Varsayılanları | Günlük alışkanlık |
| Görünüm ve okuma tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Tema, dil, TTS, widget'lar |
| Daily Reform cache & notification prefs | App Group UserDefaults | Bugünün ID’si and schedule |
| Kart tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Son stil / oran |
| İlk katılım ve TipKit durumu | Standart Kullanıcı Varsayılanları | Hoş geldiniz kılavuzu |
| Widget / Canlı Etkinlik anlık görüntüleri | Uygulama Grubu / ActivityKit | Daha önce açmış olduğunuz metni görüntüleyin |

Uygulamanın kaldırılması, korumalı alanı ve Uygulama Grubu verilerini kaldırır (işletim sistemi davranışına bağlıdır). İsteğe bağlı iCloud kopyaları, siz onları temizleyene kadar **iCloud'unuzda** kalır.

## iCloud Senkronizasyonu (İsteğe Bağlı)

Eğer Ayarlar’dan **iCloud Senkronizasyonu**’nu etkinleştirirseniz, uygulama seçili kullanıcı verilerini Apple’ın **`NSUbiquitousKeyValueStore`** aracılığıyla **Apple Kimliğinizle** eşler:

- Favoriler
- Listeler
- Okuma geçmişi
- Çalışma ilerlemesi / ustalık
- Pratik serileri
- Notlar

Senkronizasyon trafiği iHTC Studio'ya değil **Apple iCloud**'a gider. iCloud içeriklerinizi okuyamıyoruz.

## İzinler

iLiezi yalnızca bir özellik ihtiyaç duyduğunda izin ister:

| İzin | Ne zaman | neden |
|------------|------|-----|
| Bildirimler | Daily Reform reminders etkinleştirirsiniz | Yerel zamanlama |
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

iLiezi genel kitleye yönelik bir eğitim okuryazarlığı uygulamasıdır ve Çocuk Kategorisinde **değildir**. Çocuklardan bilerek kişisel bilgi toplamıyoruz. Aileler okuma ve çalışma özelliklerini kendi cihazlarında çevrimdışı olarak kullanabilir.

## Üçüncü Taraflar

- **Apple** — App Store dağıtımı, isteğe bağlı StoreKit, isteğe bağlı iCloud KVS, sistem TTS, seçtiğiniz Paylaşım Sayfası hedefleri ve işletim sistemi düzeyinde bildirim / Canlı Etkinlik / Siri / Kısayollar / Vision dağıtımı.
- Reklam, analiz veya sosyal giriş için başka hiçbir üçüncü taraf SDK’sı veri toplama amacıyla dahil edilmemiştir.

## Uluslararası Kullanıcılar

Uygulama, cihazınızda çevrimdışı çalışacak şekilde tasarlanmıştır. İsteğe bağlı Apple hizmetleri Apple’ın şartlarına ve bölgesel kullanılabilirliğe tabidir.

## Veri Saklama ve Silme

- **Cihazda** — Yerel sandbox ve App Group verilerini kaldırmak için uygulamayı silin (işletim sistemi davranışına bağlıdır).
- **iCloud** — Senkronizasyonu kapatın ve gerekirse ilgili anahtarları iCloud hesabınızdan temizleyin; iCloud hesabınızı sizin için silemeyiz.
- **Hiçbir şeyi** iHTC Studio sunucularında bu uygulama için saklamıyoruz çünkü bunu toplamıyoruz.

## Politika Değişiklikleri

Bu Gizlilik Politikasını güncelleyebiliriz. Üstteki "Son güncelleme" tarihi değişecektir. Güncellemeden sonra devam eden kullanım, revize edilen politikayı kabul ettiğiniz anlamına gelir.

## İletişim

Gizlilik ile ilgili sorular: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
