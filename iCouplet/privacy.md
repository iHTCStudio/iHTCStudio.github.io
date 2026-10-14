---
layout: doc
title: iCouplet — Privacy Policy
app_id: iCouplet
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iCouplet (爱对联) — fully offline couplet app, Data Not Collected, optional iCloud and Photo Library add-only.
---

<section lang="en" markdown="1">

**Last updated:** July 23, 2026

iHTC Studio ("we", "us" or "our") built **iCouplet** (also known as "爱对联" / "愛對聯", Bundle ID `com.iHTCboy.iCouplet`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on this page as the public privacy URL.

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration, email sign-in, or phone number |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your personal data |
| Network | Couplet library, reading, recite, study, widgets, and daily notifications work **offline** after install |
| Analytics / ads / tracking | **None** — no third-party analytics, advertising, or tracking SDKs; no App Tracking Transparency use |
| Optional Apple services | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities** |

## Data Collection

We do **not** collect, sell, or share personal information for advertising or analytics.

- **No account** — You can use all core features without creating an account with us.
- **No analytics or ads** — The app binary does not integrate third-party analytics, advertising, or crash-reporting SDKs that phone home to us.
- **No couplet content upload** — Your reading history, favorites, notes-like progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## How the App Works

- **Bundled library** — Couplet JSON and indexes ship inside the app / widget bundle. Browsing and study do not require a network request.
- **On-device speech** — Recitation uses Apple’s on-device / system **AVSpeechSynthesizer** (TTS). We do not send couplet text to iHTC Studio.
- **Widgets & App Group** — Widgets and the app share preferences and lightweight state via App Group `group.com.iHTCboy.iCouplet` on your device.
- **Daily notifications** — Scheduled locally with User Notifications. Tapping a notification opens a deep link to a couplet ID on device; no server fan-out.
- **Share cards** — Images are rendered on device. Saving uses **Photo Library add-only** only when you tap save. System Share Sheet may send the image to an app **you** choose; that destination’s privacy policy then applies.
- **Optional tip** — “Tip Developer” is a consumable **StoreKit** purchase processed by Apple. We do not receive your payment card details.

## Data Stored on Your Device

| Data | Where | Purpose |
|------|-------|---------|
| Couplet database | App / Widget bundle | Offline reading & study |
| Favorites & couplet lists | App Group UserDefaults | Starred works and user lists |
| Reading history / last read | App Group UserDefaults | Continue reading, history UI |
| Study progress & mastery | App Group UserDefaults | 4-level mastery, quiz state |
| Streak / check-in | App Group UserDefaults | Learning streaks |
| Appearance & reading prefs | App Group UserDefaults | Theme, accent, language, layout, TTS, tabs, widgets |
| Daily couplet cache & notification prefs | App Group UserDefaults | Today’s ID, schedule time, contextual toggle |
| Share-card preferences | App Group UserDefaults | Last style / ratio choices |
| Onboarding & TipKit state | Standard UserDefaults (device) | Welcome guide / discovery tips |
| Home Screen quick actions | System + local prefs | Up to 4 shortcuts you configure |
| Widget / Live Activity snapshots | App Group / ActivityKit | Display text you already opened |

Uninstalling the app removes sandbox and App Group data associated with the app (subject to iOS/macOS behavior). Optional iCloud copies remain in **your** iCloud until you clear them or turn sync off and delete elsewhere.

## iCloud Sync (Optional)

If you enable **iCloud Sync** in Settings, the app mirrors selected user data through Apple’s **`NSUbiquitousKeyValueStore`** tied to **your Apple ID**:

- Favorites
- Couplet lists
- Reading history
- Study progress / mastery
- Streak days

Sync traffic goes to **Apple iCloud**, not to iHTC Studio. You can disable sync in Settings. We cannot read your iCloud contents.

## Permissions

iCouplet requests permissions only when a feature needs them:

| Permission | When | Why |
|------------|------|-----|
| Notifications | You enable Daily Couplet reminders | Local scheduling of reminder notifications |
| Photo Library (Add Only) | You save a share card | Write the rendered image; we do not need full library read access |
| iCloud | You enable sync | Sync favorites / lists / history / progress / streaks |
| Live Activities (iOS) | You enable Reading Live Activity | Show the couplet you are reading on Lock Screen / Dynamic Island |
| Background audio (capability) | You enable background recitation | Continue TTS when the app is not foreground |

We do **not** request Contacts, precise Location, Camera, Microphone (beyond system TTS playback), or Tracking.

## Children’s Privacy

iCouplet does not knowingly collect personal data from anyone, including children under 13 (or the equivalent age in your region). Because we do not operate a data-collection backend, there is no child profile stored with us.

## Third Parties

- **Apple** — App Store distribution, optional StoreKit purchases, optional iCloud KVS, system TTS, Share Sheet destinations you pick, and OS-level notification / Live Activity delivery.
- **No other third-party SDKs** for ads, analytics, or social login are included for data collection.

## International Users

The app is designed to function offline on your device. Optional Apple services follow Apple’s terms and regional availability.

## Changes to This Policy

We may update this Privacy Policy from time to time. The “Last updated” date at the top will change, and the revised policy will be posted on this Privacy Policy page.

## Contact Us

If you have questions about this Privacy Policy or privacy practices:

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

We typically respond within 48 hours.

</section>
<section lang="zh-CN" markdown="1">

**最近更新：** 2026 年 7 月 23 日

爱火腿肠工作室（iHTC Studio）（「我们」）开发了 **爱对联**（iCouplet / 愛對聯，Bundle ID `com.iHTCboy.iCouplet`）。本隐私政策说明你在使用本应用时，数据如何被处理（以及**不会**如何被处理）。本页可作为 **App Store 审核**与用户查阅的公开隐私政策地址。

## 概要（对齐 App Store 隐私标签）

| 主题 | 我们的做法 |
|------|------------|
| 账号 | **不需要**——无需注册、邮箱登录或手机号 |
| iHTC Studio 收集数据 | **不收集数据（Data Not Collected）**——我们**不**运营接收你个人数据的后端 |
| 网络 | 对联库、阅读、诵联、对课、小组件与每日通知在安装后可**离线**使用 |
| 分析 / 广告 / 追踪 | **无**——无第三方分析、广告或追踪 SDK；不使用跨 App 追踪 |
| 可选的 Apple 服务 | **iCloud**（你的私有键值存储）、联卡**相册（仅添加）**、打赏用的 **StoreKit**、**本地通知**、可选**实时活动** |

## 数据收集

我们**不**出于广告或分析目的收集、出售或共享个人信息。

- **无账号** — 无需在我们这边创建账户即可使用核心功能。
- **无分析与广告** — 应用未集成会向我们回传数据的第三方分析、广告或崩溃统计 SDK。
- **无对联内容上传** — 浏览记录、收藏、学习进度与偏好保存在你的设备（以及可选的**你的** iCloud）。它们不会上传到 iHTC Studio 服务器——因为**本应用不为此运营此类服务器**。

## 应用工作原理

- **内置语料** — 对联 JSON 与索引随 App / Widget 安装包提供，浏览与对课无需联网。
- **本机语音合成** — 诵联使用系统 **AVSpeechSynthesizer**，我们不会把联句发送到 iHTC Studio。
- **小组件与 App Group** — App 与小组件通过本机 App Group `group.com.iHTCboy.iCouplet` 共享偏好与轻量状态。
- **每日通知** — 使用本地用户通知调度；点击后通过深链打开本机对联，无服务器推送内容库。
- **联卡分享** — 图片在设备上渲染。仅当你点「保存」时请求**相册仅添加**权限。系统分享会把图片交给**你选择**的目标 App，此后适用该目标的隐私政策。
- **可选打赏** — 「打赏开发者」为 Apple **StoreKit** 消耗型内购，由 Apple 处理支付；我们不会收到你的银行卡信息。

## 设备本地存储

| 数据 | 位置 | 用途 |
|------|------|------|
| 对联数据库 | App / Widget Bundle | 离线阅读与对课 |
| 收藏与联单 | App Group UserDefaults | 星标与自定义联单 |
| 浏览记录 / 最近阅读 | App Group UserDefaults | 继续阅读与历史 |
| 学习进度与掌握度 | App Group UserDefaults | 四级掌握度与测验状态 |
| 打卡连续 | App Group UserDefaults | 学习连续天数 |
| 外观与阅读偏好 | App Group UserDefaults | 主题、强调色、语言、布局、诵联、Tab、小组件 |
| 每日一联缓存与通知偏好 | App Group UserDefaults | 今日 ID、提醒时间、情境开关 |
| 联卡偏好 | App Group UserDefaults | 上次风格 / 比例 |
| 引导与 TipKit 状态 | 标准 UserDefaults | 欢迎引导 / 发现提示 |
| 主屏快捷 | 系统 + 本机偏好 | 你配置的最多 4 项 |
| 小组件 / 实时活动快照 | App Group / ActivityKit | 展示你正在阅读的内容 |

卸载应用会按系统规则删除沙盒与相关 App Group 数据。可选 iCloud 副本仍留在**你的** iCloud，直到你清理或关闭同步。

## iCloud 同步（可选）

若在设置中开启 **iCloud 同步**，应用通过绑定**你的 Apple ID** 的 **`NSUbiquitousKeyValueStore`** 镜像下列用户数据：

- 收藏
- 联单
- 浏览记录
- 学习进度 / 掌握度
- 打卡天数

同步流量通往 **Apple iCloud**，不经过 iHTC Studio。可在设置中关闭。我们无法读取你的 iCloud 内容。

## 权限说明

仅在功能需要时请求：

| 权限 | 时机 | 原因 |
|------|------|------|
| 通知 | 你开启每日一联提醒 | 本地调度提醒 |
| 相册（仅添加） | 你保存联卡 | 写入渲染图片；无需读取全部相册 |
| iCloud | 你开启同步 | 同步收藏 / 联单 / 历史 / 进度 / 打卡 |
| 实时活动（iOS） | 你开启品联实时活动 | 在锁屏 / 灵动岛显示正在品读的联 |
| 后台音频能力 | 你开启后台诵联 | App 不在前台时继续 TTS |

我们**不**请求通讯录、精确位置、相机、麦克风（除系统 TTS 播放外）或追踪权限。

## 儿童隐私

爱对联不会故意收集包括 13 岁以下（或你所在地区同等年龄）儿童在内的任何人的个人数据。由于我们不运营数据收集后端，我们这边不会保存儿童档案。

## 第三方

- **Apple** — App Store 分发、可选 StoreKit 购买、可选 iCloud、系统 TTS、你选择的分享目标，以及系统通知 / 实时活动投递。
- **无其他**用于广告、分析或社交登录的第三方数据收集 SDK。

## 政策变更

我们可能不时更新本政策。页首「最近更新」日期会随之变化，修订版将发布于本隐私政策页面。

## 联系我们

如对隐私政策有疑问：

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

我们通常在 48 小时内回复。

</section>
<section lang="zh-TW" markdown="1">

**最近更新：** 2026 年 7 月 23 日

愛火腿腸工作室（iHTC Studio）（「我們」）開發了 **愛對聯**（iCouplet / 爱对联，Bundle ID `com.iHTCboy.iCouplet`）。本隱私政策說明你在使用本應用時，資料如何被處理（以及**不會**如何被處理）。本頁可作為 **App Store 審核**與使用者查閱的公開隱私政策地址。

## 概要（對齊 App Store 隱私標籤）

| 主題 | 我們的做法 |
|------|------------|
| 帳號 | **不需要**——無需註冊、電子郵件登入或手機號碼 |
| iHTC Studio 收集資料 | **不收集資料（Data Not Collected）**——我們**不**營運接收你個人資料的後端 |
| 網路 | 對聯庫、閱讀、誦聯、對課、小工具與每日通知在安裝後可**離線**使用 |
| 分析 / 廣告 / 追蹤 | **無**——無第三方分析、廣告或追蹤 SDK；不使用跨 App 追蹤 |
| 可選的 Apple 服務 | **iCloud**（你的私有鍵值儲存）、聯卡**照片（僅加入）**、打賞用的 **StoreKit**、**本地通知**、可選**即時動態** |

## 資料收集

我們**不**出於廣告或分析目的收集、出售或共享個人資訊。

- **無帳號** — 無需在我們這邊建立帳戶即可使用核心功能。
- **無分析與廣告** — 應用未整合會向我們回傳資料的第三方分析、廣告或當機統計 SDK。
- **無對聯內容上傳** — 瀏覽紀錄、收藏、學習進度與偏好保存在你的裝置（以及可選的**你的** iCloud）。它們不會上傳到 iHTC Studio 伺服器——因為**本應用不為此營運此類伺服器**。

## 應用工作原理

- **內建語料** — 對聯 JSON 與索引隨 App / Widget 安裝包提供，瀏覽與對課無需連網。
- **本機語音合成** — 誦聯使用系統 **AVSpeechSynthesizer**，我們不會把聯句傳送到 iHTC Studio。
- **小工具與 App Group** — App 與小工具透過本機 App Group `group.com.iHTCboy.iCouplet` 共享偏好與輕量狀態。
- **每日通知** — 使用本地使用者通知排程；點擊後透過深鏈開啟本機對聯，無伺服器推播內容庫。
- **聯卡分享** — 圖片在裝置上渲染。僅當你點「儲存」時請求**照片僅加入**權限。系統分享會把圖片交給**你選擇**的目標 App，此後適用該目標的隱私政策。
- **可選打賞** — 「打賞開發者」為 Apple **StoreKit** 消耗型內購，由 Apple 處理付款；我們不會收到你的银行卡／信用卡資訊。

## 裝置本機儲存

| 資料 | 位置 | 用途 |
|------|------|------|
| 對聯資料庫 | App / Widget Bundle | 離線閱讀與對課 |
| 收藏與聯單 | App Group UserDefaults | 星號與自訂聯單 |
| 瀏覽紀錄 / 最近閱讀 | App Group UserDefaults | 繼續閱讀與歷史 |
| 學習進度與掌握度 | App Group UserDefaults | 四級掌握度與測驗狀態 |
| 打卡連續 | App Group UserDefaults | 學習連續天數 |
| 外觀與閱讀偏好 | App Group UserDefaults | 主題、強調色、語言、版面、誦聯、Tab、小工具 |
| 每日一聯快取與通知偏好 | App Group UserDefaults | 今日 ID、提醒時間、情境開關 |
| 聯卡偏好 | App Group UserDefaults | 上次風格 / 比例 |
| 引導與 TipKit 狀態 | 標準 UserDefaults | 歡迎引導 / 發現提示 |
| 主畫面捷徑 | 系統 + 本機偏好 | 你設定的最多 4 項 |
| 小工具 / 即時動態快照 | App Group / ActivityKit | 展示你正在閱讀的內容 |

解除安裝應用會依系統規則刪除沙盒與相關 App Group 資料。可選 iCloud 副本仍留在**你的** iCloud，直到你清理或關閉同步。

## iCloud 同步（可選）

若在設定中開啟 **iCloud 同步**，應用透過綁定**你的 Apple ID** 的 **`NSUbiquitousKeyValueStore`** 鏡像下列使用者資料：

- 收藏
- 聯單
- 瀏覽紀錄
- 學習進度 / 掌握度
- 打卡天數

同步流量通往 **Apple iCloud**，不經過 iHTC Studio。可在設定中關閉。我們無法讀取你的 iCloud 內容。

## 權限說明

僅在功能需要時請求：

| 權限 | 時機 | 原因 |
|------|------|------|
| 通知 | 你開啟每日一聯提醒 | 本地排程提醒 |
| 照片（僅加入） | 你儲存聯卡 | 寫入渲染圖片；無需讀取全部照片 |
| iCloud | 你開啟同步 | 同步收藏 / 聯單 / 歷史 / 進度 / 打卡 |
| 即時動態（iOS） | 你開啟品聯即時動態 | 在鎖定畫面 / 動態島顯示正在品讀的聯 |
| 背景音訊能力 | 你開啟背景誦聯 | App 不在前景時繼續 TTS |

我們**不**請求通訊錄、精確位置、相機、麥克風（除系統 TTS 播放外）或追蹤權限。

## 兒童隱私

愛對聯不會故意收集包括 13 歲以下（或你所在地區同等年齡）兒童在內的任何人的個人資料。由於我們不營運資料收集後端，我們這邊不會保存兒童檔案。

## 第三方

- **Apple** — App Store 分發、可選 StoreKit 購買、可選 iCloud、系統 TTS、你選擇的分享目標，以及系統通知 / 即時動態投遞。
- **無其他**用於廣告、分析或社交登入的第三方資料收集 SDK。

## 政策變更

我們可能不時更新本政策。頁首「最近更新」日期會隨之變化，修訂版將發佈於本隱私政策頁面。

## 聯絡我們

如對隱私政策有疑問：

- **電子郵件：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

我們通常在 48 小時內回覆。

</section>
<section lang="ja" markdown="1">

**最終更新日：** 2026 年 7 月 23 日

iHTC Studio（以下「当社」）は、**iCouplet**（「爱对联」/「愛對聯」とも呼ばれます。Bundle ID：`com.iHTCboy.iCouplet`）を開発しました。このプライバシーポリシーは、本アプリのご利用時にどのようなデータが取り扱われ、また取り扱われないかを説明するものです。**Apple App Review** およびユーザーの皆様は、このページを公開のプライバシーポリシー URL としてご利用いただけます。

## 概要（Apple のプライバシー栄養表示との対応）

| 項目 | 当社の方針 |
|-------|----------------|
| アカウント | **不要** — 登録、メールでのサインイン、電話番号は必要ありません |
| iHTC Studio によるデータ収集 | **データは収集されません** — お客様の個人データを受信するバックエンドは運用していません |
| ネットワーク | 対聯ライブラリ、閲読、朗誦、学習、ウィジェット、毎日の通知は、インストール後は**オフライン**で動作します |
| 分析・広告・トラッキング | **なし** — サードパーティの分析、広告、トラッキング SDK は使用せず、App Tracking Transparency も使用しません |
| 任意の Apple サービス | **iCloud**（お客様のプライベート KVS）、共有カード用の**写真ライブラリ（追加のみ）**、任意の投げ銭用の **StoreKit**、**ローカル通知**、任意の**ライブアクティビティ** |

## データ収集について

当社は、広告や分析のために個人情報を収集、販売、共有することは**ありません**。

- **アカウントなし** — 当社のアカウントを作成しなくても、すべての主要機能をご利用いただけます。
- **分析や広告なし** — アプリのバイナリには、当社に情報を送信するサードパーティの分析、広告、クラッシュレポート SDK は組み込まれていません。
- **対聯コンテンツのアップロードなし** — 閲読履歴、お気に入り、メモのような学習の進捗、設定は、お客様の端末内（および任意で**お客様自身の** iCloud）にとどまります。**当社は本アプリ向けにそのようなサーバーを運用していない**ため、iHTC Studio のサーバーにアップロードされることはありません。

## アプリの仕組み

- **同梱ライブラリ** — 対聯の JSON とインデックスは、アプリ / ウィジェットのバンドルに含まれています。閲覧や学習にネットワークリクエストは不要です。
- **端末上の音声合成** — 朗誦には Apple の端末内 / システムの **AVSpeechSynthesizer**（TTS）を使用します。対聯のテキストが iHTC Studio に送信されることはありません。
- **ウィジェットと App Group** — ウィジェットとアプリは、端末上の App Group `group.com.iHTCboy.iCouplet` を通じて、設定と軽量な状態を共有します。
- **毎日の通知** — User Notifications を使ってローカルでスケジュールされます。通知をタップすると、端末上の対聯 ID へのディープリンクが開きます。サーバーからの一斉配信はありません。
- **共有カード** — 画像は端末上で生成されます。保存時のみ、保存ボタンをタップしたときに**写真ライブラリへの追加のみ**を使用します。システムの共有シートは、**お客様が選んだ**アプリに画像を送ることがあり、その場合は送信先のプライバシーポリシーが適用されます。
- **任意の投げ銭** — 「開発者を応援」は Apple が処理する消耗型の **StoreKit** 購入です。お客様のお支払いカード情報を当社が受け取ることはありません。

## 端末に保存されるデータ

| データ | 保存場所 | 用途 |
|------|-------|---------|
| 対聯データベース | アプリ / ウィジェットのバンドル | オフラインでの閲読と学習 |
| お気に入りと対聯リスト | App Group の UserDefaults | スターを付けた作品とユーザーのリスト |
| 閲読履歴 / 最後に読んだ位置 | App Group の UserDefaults | 続きから読む、履歴 UI |
| 学習の進捗と習熟度 | App Group の UserDefaults | 4 段階の習熟度、クイズの状態 |
| 連続記録 / チェックイン | App Group の UserDefaults | 学習の連続記録 |
| 外観と閲読の設定 | App Group の UserDefaults | テーマ、アクセント、言語、レイアウト、TTS、タブ、ウィジェット |
| 今日の対聯のキャッシュと通知設定 | App Group の UserDefaults | 今日の ID、通知時刻、文脈に合わせた切り替え |
| 共有カードの設定 | App Group の UserDefaults | 最後に選んだスタイルや比率 |
| オンボーディングと TipKit の状態 | 標準の UserDefaults（端末内） | ウェルカムガイド / 発見のヒント |
| ホーム画面のクイックアクション | システム + ローカル設定 | お客様が設定する最大 4 件のショートカット |
| ウィジェット / ライブアクティビティのスナップショット | App Group / ActivityKit | すでに開いた表示テキスト |

アプリをアンインストールすると、そのアプリに関連するサンドボックスと App Group のデータが削除されます（iOS/macOS の動作に従います）。任意の iCloud 上のコピーは、お客様が削除するか、同期をオフにして別の場所で削除するまで、**お客様の** iCloud に残ります。

## iCloud 同期（任意）

設定で **iCloud 同期**を有効にすると、アプリは **お客様の Apple ID** に紐づく Apple の **`NSUbiquitousKeyValueStore`** を通じて、選択したユーザーデータをミラーリングします。

- お気に入り
- 対聯リスト
- 閲読履歴
- 学習の進捗 / 習熟度
- 連続記録の日数

同期の通信先は **Apple の iCloud** であり、iHTC Studio ではありません。同期は設定でいつでも無効にできます。当社がお客様の iCloud の内容を読み取ることはできません。

## 権限

iCouplet は、機能が必要としたときにのみ権限を要求します。

| 権限 | タイミング | 目的 |
|------------|------|-----|
| 通知 | 「今日の対聯」リマインダーを有効にしたとき | リマインダー通知のローカルでのスケジュール |
| 写真ライブラリ（追加のみ） | 共有カードを保存するとき | 生成した画像の書き込み。ライブラリ全体の読み取りは不要です |
| iCloud | 同期を有効にしたとき | お気に入り / リスト / 履歴 / 進捗 / 連続記録の同期 |
| ライブアクティビティ（iOS） | 閲読のライブアクティビティを有効にしたとき | 読んでいる対聯をロック画面 / ダイナミックアイランドに表示 |
| バックグラウンドオーディオ（機能） | バックグラウンド朗誦を有効にしたとき | アプリがフォアグラウンドでなくても TTS を継続 |

連絡先、正確な位置情報、カメラ、マイク（システム TTS の再生を除く）、トラッキングは要求**しません**。

## お子様のプライバシー

iCouplet は、13 歳未満（またはお住まいの地域で同等の年齢）のお子様を含め、誰からも個人データを意図的に収集することはありません。当社はデータ収集用のバックエンドを運用していないため、お子様のプロフィールが当社に保存されることもありません。

## 第三者

- **Apple** — App Store での配信、任意の StoreKit 購入、任意の iCloud KVS、システム TTS、お客様が選ぶ共有シートの送信先、OS レベルの通知 / ライブアクティビティの配信。
- 広告、分析、ソーシャルログイン向けの**その他のサードパーティ SDK** は、データ収集目的では組み込まれていません。

## 海外のユーザー

本アプリは、端末上でオフラインで動作するよう設計されています。任意の Apple サービスは、Apple の規約と地域ごとの提供状況に従います。

## 本ポリシーの変更

当社は、本プライバシーポリシーを随時更新することがあります。その場合は冒頭の「最終更新日」が変更され、改訂版が本プライバシーポリシーのページに掲載されます。

## お問い合わせ

本プライバシーポリシーまたはプライバシーに関する取り組みについてご質問がある場合：

- **メール：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

通常 48 時間以内に返信します。

</section>
<section lang="ko" markdown="1">

**최종 업데이트:** 2026년 7월 23일

iHTC Studio("당사")는 **iCouplet**("爱对联" / "愛對聯"으로도 알려져 있으며, Bundle ID는 `com.iHTCboy.iCouplet`)을 만들었습니다. 이 개인정보 처리방침은 앱을 사용할 때 어떤 데이터가 처리되고 어떤 데이터가 처리되지 않는지 설명합니다. **Apple 앱 심사**와 사용자는 이 페이지를 공개 개인정보 처리방침 URL로 활용할 수 있습니다.

## 요약(Apple 개인정보 보호 영양 성분 라벨 기준)

| 항목 | 당사의 방침 |
|-------|----------------|
| 계정 | **불필요** — 가입, 이메일 로그인, 전화번호가 필요하지 않습니다 |
| iHTC Studio의 데이터 수집 | **수집되는 데이터 없음** — 개인 데이터를 수신하는 백엔드를 운영하지 않습니다 |
| 네트워크 | 대련 라이브러리, 읽기, 낭송, 학습, 위젯, 일일 알림은 설치 후 **오프라인**으로 동작합니다 |
| 분석 / 광고 / 추적 | **없음** — 서드파티 분석, 광고, 추적 SDK를 사용하지 않으며 앱 추적 투명성(ATT)도 사용하지 않습니다 |
| 선택적 Apple 서비스 | **iCloud**(개인 KVS), 공유 카드용 **사진 보관함(추가 전용)**, 선택적 후원용 **StoreKit**, **로컬 알림**, 선택적 **실시간 현황(Live Activity)** |

## 데이터 수집

당사는 광고나 분석을 위해 개인정보를 수집, 판매 또는 공유하지 **않습니다**.

- **계정 없음** — 당사 계정을 만들지 않아도 모든 핵심 기능을 사용할 수 있습니다.
- **분석·광고 없음** — 앱 바이너리에는 당사로 정보를 보내는 서드파티 분석, 광고, 충돌 보고 SDK가 통합되어 있지 않습니다.
- **대련 콘텐츠 업로드 없음** — 읽기 기록, 즐겨찾기, 메모와 같은 학습 진행 상황, 설정은 기기(및 선택적으로 **사용자 본인의** iCloud)에만 저장됩니다. **당사는 이 앱을 위한 서버를 운영하지 않으므로** iHTC Studio 서버로 업로드되지 않습니다.

## 앱 작동 방식

- **내장 라이브러리** — 대련 JSON과 색인은 앱 / 위젯 번들에 포함되어 있습니다. 탐색과 학습에는 네트워크 요청이 필요하지 않습니다.
- **기기 내 음성** — 낭송에는 Apple의 기기 내 / 시스템 **AVSpeechSynthesizer**(TTS)를 사용합니다. 대련 텍스트를 iHTC Studio로 보내지 않습니다.
- **위젯과 App Group** — 위젯과 앱은 기기의 App Group `group.com.iHTCboy.iCouplet`을 통해 설정과 가벼운 상태를 공유합니다.
- **일일 알림** — User Notifications로 로컬에서 예약됩니다. 알림을 탭하면 기기의 대련 ID로 연결되는 딥링크가 열리며, 서버에서 일괄 발송하지 않습니다.
- **공유 카드** — 이미지는 기기에서 생성됩니다. 저장은 저장 버튼을 탭할 때에만 **사진 보관함 추가 전용** 권한을 사용합니다. 시스템 공유 시트는 **사용자가 선택한** 앱으로 이미지를 보낼 수 있으며, 이 경우 해당 앱의 개인정보 처리방침이 적용됩니다.
- **선택적 후원** — "개발자 후원"은 Apple이 처리하는 소모성 **StoreKit** 구매입니다. 당사는 결제 카드 정보를 받지 않습니다.

## 기기에 저장되는 데이터

| 데이터 | 위치 | 용도 |
|------|-------|---------|
| 대련 데이터베이스 | 앱 / 위젯 번들 | 오프라인 읽기 및 학습 |
| 즐겨찾기 및 대련 목록 | App Group UserDefaults | 별표를 표시한 작품과 사용자 목록 |
| 읽기 기록 / 마지막으로 읽은 위치 | App Group UserDefaults | 이어 읽기, 기록 UI |
| 학습 진행 상황 및 숙달도 | App Group UserDefaults | 4단계 숙달도, 퀴즈 상태 |
| 연속 학습 / 출석 체크 | App Group UserDefaults | 학습 연속 기록 |
| 화면 및 읽기 설정 | App Group UserDefaults | 테마, 강조색, 언어, 레이아웃, TTS, 탭, 위젯 |
| 오늘의 대련 캐시 및 알림 설정 | App Group UserDefaults | 오늘의 ID, 알림 시각, 상황별 추천 스위치 |
| 공유 카드 설정 | App Group UserDefaults | 마지막으로 선택한 스타일 / 비율 |
| 온보딩 및 TipKit 상태 | 표준 UserDefaults(기기) | 시작 가이드 / 발견 팁 |
| 홈 화면 빠른 동작 | 시스템 + 로컬 설정 | 사용자가 설정한 최대 4개의 바로가기 |
| 위젯 / 실시간 현황 스냅숏 | App Group / ActivityKit | 이미 열어 본 표시 텍스트 |

앱을 삭제하면 앱과 관련된 샌드박스 및 App Group 데이터가 삭제됩니다(iOS/macOS 동작에 따름). 선택적 iCloud 사본은 사용자가 지우거나, 동기화를 끄고 다른 곳에서 삭제할 때까지 **사용자 본인의** iCloud에 남습니다.

## iCloud 동기화(선택)

설정에서 **iCloud 동기화**를 켜면 앱은 **사용자의 Apple ID**에 연결된 Apple의 **`NSUbiquitousKeyValueStore`**를 통해 일부 사용자 데이터를 미러링합니다.

- 즐겨찾기
- 대련 목록
- 읽기 기록
- 학습 진행 상황 / 숙달도
- 연속 학습 일수

동기화 트래픽은 iHTC Studio가 아니라 **Apple iCloud**로 전송됩니다. 설정에서 동기화를 끌 수 있습니다. 당사는 사용자의 iCloud 내용을 읽을 수 없습니다.

## 권한

iCouplet은 기능에 필요할 때에만 권한을 요청합니다.

| 권한 | 시점 | 이유 |
|------------|------|-----|
| 알림 | 오늘의 대련 알림을 켤 때 | 알림 메시지의 로컬 예약 |
| 사진 보관함(추가 전용) | 공유 카드를 저장할 때 | 생성된 이미지 저장. 보관함 전체 읽기 권한은 필요하지 않습니다 |
| iCloud | 동기화를 켤 때 | 즐겨찾기 / 목록 / 기록 / 진행 상황 / 연속 기록 동기화 |
| 실시간 현황(iOS) | 읽기 실시간 현황을 켤 때 | 읽고 있는 대련을 잠금 화면 / 다이내믹 아일랜드에 표시 |
| 백그라운드 오디오(기능) | 백그라운드 낭송을 켤 때 | 앱이 포그라운드가 아닐 때도 TTS 계속 재생 |

연락처, 정밀 위치, 카메라, 마이크(시스템 TTS 재생 제외), 추적 권한은 요청하지 **않습니다**.

## 아동 개인정보 보호

iCouplet은 13세 미만(또는 거주 지역의 동등한 연령) 아동을 포함해 누구에게서도 개인 데이터를 의도적으로 수집하지 않습니다. 당사는 데이터 수집 백엔드를 운영하지 않으므로 당사에 저장되는 아동 프로필도 없습니다.

## 제3자

- **Apple** — App Store 배포, 선택적 StoreKit 구매, 선택적 iCloud KVS, 시스템 TTS, 사용자가 선택하는 공유 시트 대상, OS 수준의 알림 / 실시간 현황 전달.
- 데이터 수집을 위한 광고, 분석, 소셜 로그인용 **다른 서드파티 SDK는 포함되어 있지 않습니다**.

## 해외 사용자

이 앱은 기기에서 오프라인으로 동작하도록 설계되었습니다. 선택적 Apple 서비스는 Apple의 약관과 지역별 제공 여부를 따릅니다.

## 본 방침의 변경

당사는 본 개인정보 처리방침을 수시로 업데이트할 수 있습니다. 상단의 "최종 업데이트" 날짜가 변경되며, 개정된 방침은 이 개인정보 처리방침 페이지에 게시됩니다.

## 문의

본 개인정보 처리방침이나 개인정보 보호 관행에 대해 궁금한 점이 있으시면:

- **이메일:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

보통 48시간 이내에 답변드립니다.

</section>
<section lang="ru" markdown="1">

**Дата последнего обновления:** 23 июля 2026 г.

iHTC Studio («мы», «нас» или «наш») создала **iCouplet** (также известное как «爱对联» / «愛對聯», Bundle ID `com.iHTCboy.iCouplet`). Настоящая Политика конфиденциальности объясняет, какие данные обрабатываются (и какие не обрабатываются) при использовании приложения. **Apple App Review** и пользователи могут использовать эту страницу как публичный URL политики конфиденциальности.

## Кратко (соответствие «пищевой этикетке» конфиденциальности Apple)

| Тема | Наша практика |
|-------|----------------|
| Учётная запись | **Не требуется** — ни регистрации, ни входа по электронной почте, ни номера телефона |
| Сбор данных iHTC Studio | **Данные не собираются** — мы **не** используем серверную часть, которая получала бы ваши персональные данные |
| Сеть | Библиотека парных надписей, чтение, декламация, обучение, виджеты и ежедневные уведомления работают **офлайн** после установки |
| Аналитика / реклама / отслеживание | **Нет** — никаких сторонних SDK для аналитики, рекламы или отслеживания; App Tracking Transparency не используется |
| Необязательные сервисы Apple | **iCloud** (ваше личное хранилище KVS), **Фототека (только добавление)** для карточек для обмена, **StoreKit** для необязательной благодарности разработчику, **локальные уведомления**, необязательные **Live Activities** |

## Сбор данных

Мы **не** собираем, не продаём и не передаём персональную информацию для рекламы или аналитики.

- **Без учётной записи** — вы можете пользоваться всеми основными функциями, не создавая у нас учётную запись.
- **Без аналитики и рекламы** — в приложение не встроены сторонние SDK для аналитики, рекламы или отчётов о сбоях, которые отправляли бы данные нам.
- **Без загрузки содержимого на сервер** — история чтения, избранное, прогресс обучения и настройки остаются на вашем устройстве (и, по желанию, в **вашем** iCloud). Они никогда не загружаются на серверы iHTC Studio, потому что **для этого приложения у нас нет таких серверов**.

## Как работает приложение

- **Встроенная библиотека** — JSON с парными надписями и индексы входят в пакет приложения / виджета. Для просмотра и обучения сетевые запросы не нужны.
- **Озвучивание на устройстве** — для декламации используется встроенный в систему Apple синтезатор **AVSpeechSynthesizer** (TTS). Мы не отправляем текст парных надписей в iHTC Studio.
- **Виджеты и App Group** — виджеты и приложение обмениваются настройками и лёгким состоянием через App Group `group.com.iHTCboy.iCouplet` на вашем устройстве.
- **Ежедневные уведомления** — планируются локально с помощью User Notifications. Нажатие на уведомление открывает глубокую ссылку на идентификатор парной надписи на устройстве; серверной рассылки нет.
- **Карточки для обмена** — изображения создаются на устройстве. Сохранение использует **Фототеку (только добавление)** лишь тогда, когда вы нажимаете «Сохранить». Системное меню «Поделиться» может передать изображение приложению, **которое вы выберете**; тогда действует политика конфиденциальности этого получателя.
- **Необязательная благодарность** — «Поддержать разработчика» — это расходуемая покупка **StoreKit**, обрабатываемая Apple. Данные вашей платёжной карты мы не получаем.

## Данные, хранящиеся на вашем устройстве

| Данные | Где | Назначение |
|------|-------|---------|
| База парных надписей | Пакет приложения / виджета | Офлайн-чтение и обучение |
| Избранное и списки надписей | UserDefaults App Group | Отмеченные звёздочкой произведения и пользовательские списки |
| История чтения / последнее прочитанное | UserDefaults App Group | Продолжение чтения, интерфейс истории |
| Прогресс обучения и уровень освоения | UserDefaults App Group | 4 уровня освоения, состояние викторины |
| Серия / отметки | UserDefaults App Group | Серии занятий |
| Внешний вид и параметры чтения | UserDefaults App Group | Тема, акцент, язык, раскладка, TTS, вкладки, виджеты |
| Кэш надписи дня и настройки уведомлений | UserDefaults App Group | Идентификатор на сегодня, время отправки, переключатель подбора по контексту |
| Настройки карточек для обмена | UserDefaults App Group | Последний выбранный стиль / соотношение сторон |
| Состояние первого запуска и TipKit | Стандартный UserDefaults (устройство) | Приветственное руководство / подсказки |
| Быстрые действия на экране «Домой» | Система + локальные настройки | До 4 настроенных вами ярлыков |
| Снимки для виджетов / Live Activity | App Group / ActivityKit | Отображаемый текст, который вы уже открывали |

Удаление приложения удаляет данные песочницы и App Group, связанные с ним (с учётом поведения iOS/macOS). Необязательные копии в iCloud остаются в **вашем** iCloud, пока вы их не удалите или не отключите синхронизацию и не удалите данные в другом месте.

## Синхронизация через iCloud (необязательно)

Если вы включите **синхронизацию iCloud** в настройках, приложение отражает выбранные пользовательские данные через **`NSUbiquitousKeyValueStore`** от Apple, привязанное к **вашему Apple ID**:

- Избранное
- Списки парных надписей
- История чтения
- Прогресс обучения / уровень освоения
- Дни серии

Трафик синхронизации идёт в **Apple iCloud**, а не в iHTC Studio. Синхронизацию можно отключить в настройках. Мы не можем прочитать содержимое вашего iCloud.

## Разрешения

iCouplet запрашивает разрешения только тогда, когда они нужны функции:

| Разрешение | Когда | Зачем |
|------------|------|-----|
| Уведомления | Вы включаете напоминания «Надпись дня» | Локальное планирование уведомлений-напоминаний |
| Фототека (только добавление) | Вы сохраняете карточку для обмена | Запись созданного изображения; полный доступ на чтение фототеки не нужен |
| iCloud | Вы включаете синхронизацию | Синхронизация избранного / списков / истории / прогресса / серий |
| Live Activities (iOS) | Вы включаете Live Activity для чтения | Показ читаемой вами надписи на экране блокировки / в Dynamic Island |
| Фоновое аудио (возможность) | Вы включаете фоновую декламацию | Продолжение озвучивания, когда приложение не на переднем плане |

Мы **не** запрашиваем доступ к контактам, точной геопозиции, камере, микрофону (кроме воспроизведения системного TTS) и отслеживанию.

## Конфиденциальность детей

iCouplet сознательно не собирает персональные данные ни у кого, включая детей младше 13 лет (или эквивалентного возраста в вашем регионе). Поскольку у нас нет серверной части для сбора данных, никакие профили детей у нас не хранятся.

## Третьи стороны

- **Apple** — распространение через App Store, необязательные покупки StoreKit, необязательный iCloud KVS, системный TTS, выбранные вами получатели в меню «Поделиться», а также доставка уведомлений / Live Activity на уровне ОС.
- **Никаких других сторонних SDK** для рекламы, аналитики или входа через соцсети в целях сбора данных не включено.

## Пользователи из других стран

Приложение рассчитано на работу офлайн на вашем устройстве. Необязательные сервисы Apple подчиняются условиям Apple и региональной доступности.

## Изменения в политике

Мы можем время от времени обновлять настоящую Политику конфиденциальности. Дата «Последнего обновления» в начале страницы изменится, а новая редакция будет опубликована на этой странице Политики конфиденциальности.

## Связаться с нами

Если у вас есть вопросы о настоящей Политике конфиденциальности или практике обеспечения конфиденциальности:

- **Эл. почта:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Обычно мы отвечаем в течение 48 часов.

</section>
<section lang="th" markdown="1">

**อัปเดตล่าสุด:** 23 กรกฎาคม 2026

iHTC Studio ("เรา") เป็นผู้พัฒนา **iCouplet** (หรือที่รู้จักในชื่อ "爱对联" / "愛對聯" Bundle ID คือ `com.iHTCboy.iCouplet`) นโยบายความเป็นส่วนตัวนี้อธิบายว่าข้อมูลใดถูกจัดการและไม่ถูกจัดการเมื่อคุณใช้แอป **Apple App Review** และผู้ใช้สามารถใช้หน้านี้เป็น URL นโยบายความเป็นส่วนตัวสาธารณะได้

## สรุป (สอดคล้องกับ Apple Privacy Nutrition Label)

| หัวข้อ | แนวปฏิบัติของเรา |
|-------|----------------|
| บัญชี | **ไม่จำเป็น** — ไม่ต้องสมัคร ลงชื่อเข้าใช้ด้วยอีเมล หรือใช้หมายเลขโทรศัพท์ |
| การเก็บข้อมูลโดย iHTC Studio | **ไม่เก็บข้อมูล** — เรา **ไม่ได้** ดำเนินการแบ็กเอนด์ที่รับข้อมูลส่วนบุคคลของคุณ |
| เครือข่าย | คลังคำคู่ การอ่าน การท่อง การเรียน วิดเจ็ต และการแจ้งเตือนรายวันทำงาน **แบบออฟไลน์** หลังติดตั้ง |
| การวิเคราะห์ / โฆษณา / การติดตาม | **ไม่มี** — ไม่มี SDK วิเคราะห์ โฆษณา หรือติดตามจากบุคคลที่สาม และไม่ใช้ App Tracking Transparency |
| บริการเสริมของ Apple | **iCloud** (KVS ส่วนตัวของคุณ) **คลังรูปภาพ (เพิ่มอย่างเดียว)** สำหรับการ์ดแชร์ **StoreKit** สำหรับการให้ทิปแบบเลือกได้ **การแจ้งเตือนในเครื่อง** และ **Live Activities** แบบเลือกใช้ |

## การเก็บรวบรวมข้อมูล

เรา **ไม่** เก็บรวบรวม ขาย หรือแบ่งปันข้อมูลส่วนบุคคลเพื่อการโฆษณาหรือการวิเคราะห์

- **ไม่มีบัญชี** — คุณใช้ฟีเจอร์หลักทั้งหมดได้โดยไม่ต้องสร้างบัญชีกับเรา
- **ไม่มีการวิเคราะห์หรือโฆษณา** — ตัวแอปไม่ได้รวม SDK วิเคราะห์ โฆษณา หรือรายงานข้อขัดข้องจากบุคคลที่สามที่ส่งข้อมูลกลับมาหาเรา
- **ไม่อัปโหลดเนื้อหาคำคู่** — ประวัติการอ่าน รายการโปรด ความคืบหน้าการเรียนรู้ และการตั้งค่าของคุณอยู่บนอุปกรณ์ของคุณ (และอยู่ใน iCloud **ของคุณเอง** หากเลือกใช้) ข้อมูลเหล่านี้จะไม่ถูกอัปโหลดไปยังเซิร์ฟเวอร์ของ iHTC Studio เพราะ **เราไม่ได้ดำเนินการเซิร์ฟเวอร์เช่นนั้นสำหรับแอปนี้**

## แอปทำงานอย่างไร

- **คลังข้อมูลในตัวแอป** — JSON และดัชนีของคำคู่รวมอยู่ในชุดแอป / วิดเจ็ต การเรียกดูและการเรียนไม่ต้องส่งคำขอผ่านเครือข่าย
- **เสียงบนอุปกรณ์** — การท่องใช้ **AVSpeechSynthesizer** (TTS) ของ Apple บนอุปกรณ์ / ระบบ เราไม่ส่งข้อความคำคู่ไปยัง iHTC Studio
- **วิดเจ็ตและ App Group** — วิดเจ็ตและแอปใช้การตั้งค่าและสถานะขนาดเล็กร่วมกันผ่าน App Group `group.com.iHTCboy.iCouplet` บนอุปกรณ์ของคุณ
- **การแจ้งเตือนรายวัน** — ตั้งเวลาในเครื่องด้วย User Notifications เมื่อแตะการแจ้งเตือนจะเปิดลิงก์ลึกไปยัง ID ของคำคู่บนอุปกรณ์ ไม่มีการส่งกระจายจากเซิร์ฟเวอร์
- **การ์ดแชร์** — รูปภาพสร้างขึ้นบนอุปกรณ์ การบันทึกใช้ **สิทธิ์เพิ่มลงคลังรูปภาพอย่างเดียว** เฉพาะเมื่อคุณแตะบันทึก ชีตแชร์ของระบบอาจส่งรูปภาพไปยังแอปที่ **คุณเลือก** ซึ่งนโยบายความเป็นส่วนตัวของปลายทางนั้นจะมีผลบังคับใช้
- **ทิปแบบเลือกได้** — "ให้ทิปนักพัฒนา" เป็นการซื้อแบบใช้หมด (consumable) ผ่าน **StoreKit** ที่ Apple ดำเนินการ เราไม่ได้รับรายละเอียดบัตรชำระเงินของคุณ

## ข้อมูลที่จัดเก็บบนอุปกรณ์ของคุณ

| ข้อมูล | ที่เก็บ | วัตถุประสงค์ |
|------|-------|---------|
| ฐานข้อมูลคำคู่ | ชุดแอป / วิดเจ็ต | อ่านและเรียนแบบออฟไลน์ |
| รายการโปรดและรายการคำคู่ | UserDefaults ของ App Group | ผลงานที่ติดดาวและรายการของผู้ใช้ |
| ประวัติการอ่าน / ที่อ่านล่าสุด | UserDefaults ของ App Group | อ่านต่อ ส่วนประวัติ |
| ความคืบหน้าการเรียนและระดับความชำนาญ | UserDefaults ของ App Group | ระดับความชำนาญ 4 ระดับ สถานะแบบทดสอบ |
| สถิติต่อเนื่อง / เช็กอิน | UserDefaults ของ App Group | สถิติการเรียนต่อเนื่อง |
| การตั้งค่าหน้าตาและการอ่าน | UserDefaults ของ App Group | ธีม สีเน้น ภาษา เค้าโครง TTS แท็บ วิดเจ็ต |
| แคชคำคู่ประจำวันและการตั้งค่าการแจ้งเตือน | UserDefaults ของ App Group | ID ของวันนี้ เวลาแจ้งเตือน สวิตช์แนะนำตามบริบท |
| การตั้งค่าการ์ดแชร์ | UserDefaults ของ App Group | สไตล์ / อัตราส่วนที่เลือกล่าสุด |
| สถานะการแนะนำและ TipKit | UserDefaults มาตรฐาน (บนอุปกรณ์) | คู่มือต้อนรับ / เคล็ดลับการค้นพบ |
| การทำงานด่วนบนหน้าจอหลัก | ระบบ + การตั้งค่าในเครื่อง | ทางลัดสูงสุด 4 รายการที่คุณกำหนด |
| สแนปช็อตวิดเจ็ต / Live Activity | App Group / ActivityKit | ข้อความที่แสดงซึ่งคุณเปิดดูแล้ว |

การลบแอปจะลบข้อมูลแซนด์บ็อกซ์และ App Group ที่เกี่ยวข้องกับแอป (ขึ้นอยู่กับพฤติกรรมของ iOS/macOS) สำเนาใน iCloud แบบเลือกใช้จะยังอยู่ใน iCloud **ของคุณ** จนกว่าคุณจะล้างหรือปิดการซิงค์แล้วลบที่อื่น

## การซิงค์ iCloud (ไม่บังคับ)

หากคุณเปิด **การซิงค์ iCloud** ในการตั้งค่า แอปจะทำสำเนาข้อมูลผู้ใช้บางส่วนผ่าน **`NSUbiquitousKeyValueStore`** ของ Apple ที่ผูกกับ **Apple ID ของคุณ**:

- รายการโปรด
- รายการคำคู่
- ประวัติการอ่าน
- ความคืบหน้าการเรียน / ระดับความชำนาญ
- จำนวนวันต่อเนื่อง

การรับส่งข้อมูลซิงค์ไปยัง **Apple iCloud** ไม่ใช่ iHTC Studio คุณปิดการซิงค์ได้ในการตั้งค่า เราไม่สามารถอ่านเนื้อหาใน iCloud ของคุณได้

## สิทธิ์การเข้าถึง

iCouplet ขอสิทธิ์เฉพาะเมื่อฟีเจอร์ต้องการเท่านั้น:

| สิทธิ์ | เมื่อใด | เหตุผล |
|------------|------|-----|
| การแจ้งเตือน | คุณเปิดการเตือนคำคู่ประจำวัน | ตั้งเวลาการแจ้งเตือนในเครื่อง |
| คลังรูปภาพ (เพิ่มอย่างเดียว) | คุณบันทึกการ์ดแชร์ | เขียนรูปภาพที่สร้างขึ้น เราไม่จำเป็นต้องอ่านคลังรูปภาพทั้งหมด |
| iCloud | คุณเปิดการซิงค์ | ซิงค์รายการโปรด / รายการ / ประวัติ / ความคืบหน้า / สถิติต่อเนื่อง |
| Live Activities (iOS) | คุณเปิด Live Activity ขณะอ่าน | แสดงคำคู่ที่คุณกำลังอ่านบนหน้าจอล็อก / Dynamic Island |
| เสียงเบื้องหลัง (ความสามารถ) | คุณเปิดการท่องเบื้องหลัง | เล่น TTS ต่อเมื่อแอปไม่ได้อยู่เบื้องหน้า |

เรา **ไม่** ขอสิทธิ์เข้าถึงรายชื่อติดต่อ ตำแหน่งที่แม่นยำ กล้อง ไมโครโฟน (นอกจากการเล่น TTS ของระบบ) หรือการติดตาม

## ความเป็นส่วนตัวของเด็ก

iCouplet ไม่ได้ตั้งใจเก็บข้อมูลส่วนบุคคลจากใครก็ตาม รวมถึงเด็กอายุต่ำกว่า 13 ปี (หรืออายุที่เทียบเท่าในภูมิภาคของคุณ) เนื่องจากเราไม่ได้ดำเนินการแบ็กเอนด์เก็บข้อมูล จึงไม่มีโปรไฟล์ของเด็กเก็บไว้กับเรา

## บุคคลที่สาม

- **Apple** — การเผยแพร่บน App Store การซื้อ StoreKit แบบเลือกใช้ iCloud KVS แบบเลือกใช้ TTS ของระบบ ปลายทางของชีตแชร์ที่คุณเลือก และการส่งการแจ้งเตือน / Live Activity ระดับระบบปฏิบัติการ
- **ไม่มี SDK ของบุคคลที่สามอื่น** สำหรับโฆษณา การวิเคราะห์ หรือการเข้าสู่ระบบด้วยโซเชียลเพื่อเก็บข้อมูล

## ผู้ใช้ต่างประเทศ

แอปออกแบบมาให้ทำงานแบบออฟไลน์บนอุปกรณ์ของคุณ บริการเสริมของ Apple เป็นไปตามข้อกำหนดของ Apple และความพร้อมให้บริการในแต่ละภูมิภาค

## การเปลี่ยนแปลงนโยบายนี้

เราอาจปรับปรุงนโยบายความเป็นส่วนตัวนี้เป็นครั้งคราว วันที่ "อัปเดตล่าสุด" ด้านบนจะเปลี่ยนไป และนโยบายฉบับแก้ไขจะเผยแพร่ในหน้านโยบายความเป็นส่วนตัวนี้

## ติดต่อเรา

หากคุณมีคำถามเกี่ยวกับนโยบายความเป็นส่วนตัวนี้หรือแนวปฏิบัติด้านความเป็นส่วนตัว:

- **อีเมล:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

โดยปกติเราจะตอบกลับภายใน 48 ชั่วโมง

</section>
<section lang="de" markdown="1">

**Zuletzt aktualisiert:** 23. Juli 2026

iHTC Studio („wir“, „uns“ oder „unser“) hat **iCouplet** entwickelt (auch bekannt als „爱对联“ / „愛對聯“, Bundle-ID `com.iHTCboy.iCouplet`). Diese Datenschutzerklärung erläutert, welche Daten bei der Nutzung der App verarbeitet werden (und welche nicht). **Apple App Review** und Nutzer können sich auf diese Seite als öffentliche Datenschutz-URL stützen.

## Zusammenfassung (Abgleich mit Apples Datenschutz-Nährwertkennzeichnung)

| Thema | Unsere Praxis |
|-------|----------------|
| Konto | **Nicht erforderlich** — keine Registrierung, keine Anmeldung per E-Mail, keine Telefonnummer |
| Datenerhebung durch iHTC Studio | **Keine Daten erhoben** — wir betreiben **kein** Backend, das Ihre personenbezogenen Daten empfängt |
| Netzwerk | Couplet-Bibliothek, Lesen, Rezitieren, Lernen, Widgets und tägliche Benachrichtigungen funktionieren nach der Installation **offline** |
| Analyse / Werbung / Tracking | **Keine** — keine Analyse-, Werbe- oder Tracking-SDKs von Drittanbietern; keine Nutzung von App Tracking Transparency |
| Optionale Apple-Dienste | **iCloud** (Ihr privater KVS), **Fotomediathek (nur Hinzufügen)** für Teilen-Karten, **StoreKit** für optionales Trinkgeld, **lokale Benachrichtigungen**, optionale **Live-Aktivitäten** |

## Datenerhebung

Wir erheben, verkaufen oder teilen **keine** personenbezogenen Daten für Werbung oder Analyse.

- **Kein Konto** — Sie können alle Kernfunktionen nutzen, ohne bei uns ein Konto anzulegen.
- **Keine Analyse oder Werbung** — Die App enthält keine SDKs von Drittanbietern für Analyse, Werbung oder Absturzberichte, die Daten an uns senden.
- **Kein Hochladen von Couplet-Inhalten** — Ihr Leseverlauf, Ihre Favoriten, Ihr Lernfortschritt und Ihre Einstellungen bleiben auf Ihrem Gerät (und optional in **Ihrem** iCloud). Sie werden nie auf Server von iHTC Studio hochgeladen, da **wir für diese App keine solchen Server betreiben**.

## Wie die App funktioniert

- **Mitgelieferte Bibliothek** — Couplet-JSON und Indizes sind im App-/Widget-Bundle enthalten. Stöbern und Lernen erfordern keine Netzwerkanfrage.
- **Sprachausgabe auf dem Gerät** — Die Rezitation nutzt Apples geräteinterne System-**AVSpeechSynthesizer** (TTS). Wir senden keinen Couplet-Text an iHTC Studio.
- **Widgets und App Group** — Widgets und App teilen Einstellungen und leichten Zustand über die App Group `group.com.iHTCboy.iCouplet` auf Ihrem Gerät.
- **Tägliche Benachrichtigungen** — Lokal mit User Notifications geplant. Tippen auf eine Benachrichtigung öffnet einen Deep-Link zu einer Couplet-ID auf dem Gerät; es gibt keinen Server-Versand.
- **Teilen-Karten** — Bilder werden auf dem Gerät erzeugt. Das Speichern nutzt **Fotomediathek (nur Hinzufügen)** ausschließlich, wenn Sie auf Speichern tippen. Das System-Share-Sheet kann das Bild an eine App senden, die **Sie** wählen; dann gilt die Datenschutzerklärung dieses Ziels.
- **Optionales Trinkgeld** — „Entwickler unterstützen“ ist ein verbrauchbarer **StoreKit**-Kauf, der von Apple abgewickelt wird. Wir erhalten Ihre Zahlungskartendaten nicht.

## Auf Ihrem Gerät gespeicherte Daten

| Daten | Wo | Zweck |
|------|-------|---------|
| Couplet-Datenbank | App-/Widget-Bundle | Offline lesen und lernen |
| Favoriten und Couplet-Listen | UserDefaults der App Group | Mit Stern markierte Werke und Nutzerlisten |
| Leseverlauf / zuletzt gelesen | UserDefaults der App Group | Weiterlesen, Verlaufsanzeige |
| Lernfortschritt und Beherrschung | UserDefaults der App Group | 4 Beherrschungsstufen, Quizstatus |
| Serie / Check-in | UserDefaults der App Group | Lernserien |
| Darstellungs- und Leseeinstellungen | UserDefaults der App Group | Design, Akzent, Sprache, Layout, TTS, Tabs, Widgets |
| Cache des Tages-Couplets und Benachrichtigungseinstellungen | UserDefaults der App Group | ID von heute, Uhrzeit, Schalter für kontextbezogene Auswahl |
| Einstellungen der Teilen-Karten | UserDefaults der App Group | Zuletzt gewählter Stil / zuletzt gewähltes Seitenverhältnis |
| Onboarding- und TipKit-Status | Standard-UserDefaults (Gerät) | Willkommensanleitung / Entdeckungstipps |
| Home-Bildschirm-Schnellaktionen | System + lokale Einstellungen | Bis zu 4 von Ihnen konfigurierte Kurzbefehle |
| Widget-/Live-Aktivität-Snapshots | App Group / ActivityKit | Anzeigetext, den Sie bereits geöffnet haben |

Das Deinstallieren der App entfernt die zugehörigen Sandbox- und App-Group-Daten (abhängig vom Verhalten von iOS/macOS). Optionale iCloud-Kopien verbleiben in **Ihrem** iCloud, bis Sie sie löschen oder die Synchronisierung ausschalten und anderswo löschen.

## iCloud-Synchronisierung (optional)

Wenn Sie in den Einstellungen die **iCloud-Synchronisierung** aktivieren, spiegelt die App ausgewählte Nutzerdaten über Apples **`NSUbiquitousKeyValueStore`**, der an **Ihre Apple-ID** gebunden ist:

- Favoriten
- Couplet-Listen
- Leseverlauf
- Lernfortschritt / Beherrschung
- Serientage

Der Synchronisierungsverkehr geht an **Apple iCloud**, nicht an iHTC Studio. Sie können die Synchronisierung in den Einstellungen deaktivieren. Wir können den Inhalt Ihres iCloud nicht lesen.

## Berechtigungen

iCouplet fordert Berechtigungen nur an, wenn eine Funktion sie benötigt:

| Berechtigung | Wann | Warum |
|------------|------|-----|
| Mitteilungen | Sie aktivieren die Erinnerungen für das Tages-Couplet | Lokale Planung von Erinnerungsbenachrichtigungen |
| Fotomediathek (nur Hinzufügen) | Sie speichern eine Teilen-Karte | Das erzeugte Bild schreiben; wir benötigen keinen vollen Lesezugriff auf die Mediathek |
| iCloud | Sie aktivieren die Synchronisierung | Favoriten / Listen / Verlauf / Fortschritt / Serien synchronisieren |
| Live-Aktivitäten (iOS) | Sie aktivieren die Lese-Live-Aktivität | Das gerade gelesene Couplet auf dem Sperrbildschirm / in der Dynamic Island anzeigen |
| Hintergrundaudio (Capability) | Sie aktivieren die Hintergrundrezitation | TTS fortsetzen, wenn die App nicht im Vordergrund ist |

Wir fordern **keinen** Zugriff auf Kontakte, genauen Standort, Kamera, Mikrofon (über die Wiedergabe der System-TTS hinaus) oder Tracking an.

## Datenschutz für Kinder

iCouplet erhebt wissentlich von niemandem personenbezogene Daten, auch nicht von Kindern unter 13 Jahren (oder dem entsprechenden Alter in Ihrer Region). Da wir kein Backend zur Datenerhebung betreiben, wird bei uns kein Kinderprofil gespeichert.

## Drittanbieter

- **Apple** — Vertrieb über den App Store, optionale StoreKit-Käufe, optionaler iCloud-KVS, System-TTS, von Ihnen gewählte Ziele im Share Sheet sowie die Zustellung von Benachrichtigungen / Live-Aktivitäten auf Betriebssystemebene.
- **Keine weiteren SDKs von Drittanbietern** für Werbung, Analyse oder Social-Login zur Datenerhebung sind enthalten.

## Internationale Nutzer

Die App ist darauf ausgelegt, offline auf Ihrem Gerät zu funktionieren. Optionale Apple-Dienste unterliegen den Bedingungen von Apple und der regionalen Verfügbarkeit.

## Änderungen dieser Richtlinie

Wir können diese Datenschutzerklärung von Zeit zu Zeit aktualisieren. Das Datum „Zuletzt aktualisiert“ oben ändert sich, und die überarbeitete Erklärung wird auf dieser Datenschutzseite veröffentlicht.

## Kontakt

Wenn Sie Fragen zu dieser Datenschutzerklärung oder zu unseren Datenschutzpraktiken haben:

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Wir antworten in der Regel innerhalb von 48 Stunden.

</section>
<section lang="fr" markdown="1">

**Dernière mise à jour :** 23 juillet 2026

iHTC Studio (« nous », « notre » ou « nos ») a développé **iCouplet** (également connu sous le nom « 爱对联 » / « 愛對聯 », Bundle ID `com.iHTCboy.iCouplet`). Cette politique de confidentialité explique quelles données sont (ou ne sont pas) traitées lorsque vous utilisez l'app. **Apple App Review** et les utilisateurs peuvent s'appuyer sur cette page comme URL publique de confidentialité.

## Résumé (alignement sur l'étiquette de confidentialité d'Apple)

| Sujet | Notre pratique |
|-------|----------------|
| Compte | **Non requis** — aucune inscription, connexion par e-mail ni numéro de téléphone |
| Collecte de données par iHTC Studio | **Aucune donnée collectée** — nous n'exploitons **aucun** serveur qui recevrait vos données personnelles |
| Réseau | La bibliothèque de couplets, la lecture, la récitation, l'étude, les widgets et les notifications quotidiennes fonctionnent **hors ligne** après l'installation |
| Analyse / publicité / suivi | **Aucun** — aucun SDK tiers d'analyse, de publicité ou de suivi ; pas d'App Tracking Transparency |
| Services Apple facultatifs | **iCloud** (votre KVS privé), **Photothèque (ajout uniquement)** pour les cartes de partage, **StoreKit** pour un pourboire facultatif, **notifications locales**, **activités en direct** facultatives |

## Collecte de données

Nous ne collectons, ne vendons ni ne partageons **aucune** information personnelle à des fins publicitaires ou d'analyse.

- **Aucun compte** — Vous pouvez utiliser toutes les fonctionnalités principales sans créer de compte chez nous.
- **Aucune analyse ni publicité** — L'app n'intègre aucun SDK tiers d'analyse, de publicité ou de rapport de plantage qui nous renverrait des informations.
- **Aucun envoi du contenu des couplets** — Votre historique de lecture, vos favoris, votre progression d'étude et vos préférences restent sur votre appareil (et, en option, dans **votre** iCloud). Ils ne sont jamais envoyés aux serveurs d'iHTC Studio, car **nous n'exploitons pas de tels serveurs pour cette app**.

## Fonctionnement de l'app

- **Bibliothèque intégrée** — Le JSON des couplets et les index sont fournis dans le bundle de l'app / du widget. Parcourir et étudier ne nécessite aucune requête réseau.
- **Voix sur l'appareil** — La récitation utilise **AVSpeechSynthesizer** (TTS), la synthèse vocale du système Apple sur l'appareil. Nous n'envoyons aucun texte de couplet à iHTC Studio.
- **Widgets et App Group** — Les widgets et l'app partagent des préférences et un état léger via l'App Group `group.com.iHTCboy.iCouplet` sur votre appareil.
- **Notifications quotidiennes** — Planifiées localement avec User Notifications. Toucher une notification ouvre un lien profond vers l'identifiant d'un couplet sur l'appareil ; aucune diffusion depuis un serveur.
- **Cartes de partage** — Les images sont générées sur l'appareil. L'enregistrement utilise **Photothèque (ajout uniquement)** seulement lorsque vous touchez Enregistrer. La feuille de partage du système peut envoyer l'image à une app **que vous choisissez** ; la politique de confidentialité de cette destination s'applique alors.
- **Pourboire facultatif** — « Soutenir le développeur » est un achat consommable **StoreKit** traité par Apple. Nous ne recevons pas les données de votre carte de paiement.

## Données stockées sur votre appareil

| Données | Où | Finalité |
|------|-------|---------|
| Base de données des couplets | Bundle de l'app / du widget | Lecture et étude hors ligne |
| Favoris et listes de couplets | UserDefaults de l'App Group | Œuvres marquées d'une étoile et listes de l'utilisateur |
| Historique de lecture / dernière lecture | UserDefaults de l'App Group | Reprendre la lecture, interface d'historique |
| Progression d'étude et maîtrise | UserDefaults de l'App Group | 4 niveaux de maîtrise, état du quiz |
| Série / pointage | UserDefaults de l'App Group | Séries d'apprentissage |
| Préférences d'apparence et de lecture | UserDefaults de l'App Group | Thème, accent, langue, mise en page, TTS, onglets, widgets |
| Cache du couplet du jour et préférences de notification | UserDefaults de l'App Group | Identifiant du jour, heure de planification, bascule contextuelle |
| Préférences des cartes de partage | UserDefaults de l'App Group | Derniers choix de style / de format |
| État d'accueil et TipKit | UserDefaults standard (appareil) | Guide de bienvenue / astuces de découverte |
| Actions rapides de l'écran d'accueil | Système + préférences locales | Jusqu'à 4 raccourcis que vous configurez |
| Instantanés de widgets / activités en direct | App Group / ActivityKit | Texte affiché que vous avez déjà ouvert |

La désinstallation de l'app supprime les données du bac à sable et de l'App Group associées à l'app (selon le comportement d'iOS/macOS). Les copies iCloud facultatives restent dans **votre** iCloud jusqu'à ce que vous les effaciez, ou que vous désactiviez la synchronisation et supprimiez ailleurs.

## Synchronisation iCloud (facultative)

Si vous activez la **synchronisation iCloud** dans les Réglages, l'app reflète certaines données utilisateur via **`NSUbiquitousKeyValueStore`** d'Apple, lié à **votre identifiant Apple** :

- Favoris
- Listes de couplets
- Historique de lecture
- Progression d'étude / maîtrise
- Jours de série

Le trafic de synchronisation est envoyé à **Apple iCloud**, et non à iHTC Studio. Vous pouvez désactiver la synchronisation dans les Réglages. Nous ne pouvons pas lire le contenu de votre iCloud.

## Autorisations

iCouplet ne demande des autorisations que lorsqu'une fonctionnalité en a besoin :

| Autorisation | Quand | Pourquoi |
|------------|------|-----|
| Notifications | Vous activez les rappels du couplet du jour | Planification locale des notifications de rappel |
| Photothèque (ajout uniquement) | Vous enregistrez une carte de partage | Écrire l'image générée ; nous n'avons pas besoin d'un accès en lecture à toute la photothèque |
| iCloud | Vous activez la synchronisation | Synchroniser favoris / listes / historique / progression / séries |
| Activités en direct (iOS) | Vous activez l'activité en direct de lecture | Afficher le couplet que vous lisez sur l'écran verrouillé / la Dynamic Island |
| Audio en arrière-plan (capacité) | Vous activez la récitation en arrière-plan | Poursuivre la synthèse vocale lorsque l'app n'est pas au premier plan |

Nous ne demandons **aucun** accès aux contacts, à la localisation précise, à l'appareil photo, au microphone (au-delà de la lecture de la synthèse vocale du système) ni au suivi.

## Confidentialité des enfants

iCouplet ne collecte sciemment de données personnelles auprès de personne, y compris des enfants de moins de 13 ans (ou l'âge équivalent dans votre région). Comme nous n'exploitons aucun serveur de collecte de données, aucun profil d'enfant n'est conservé chez nous.

## Tiers

- **Apple** — distribution sur l'App Store, achats StoreKit facultatifs, iCloud KVS facultatif, synthèse vocale du système, destinations de la feuille de partage que vous choisissez, et acheminement des notifications / activités en direct au niveau du système.
- **Aucun autre SDK tiers** de publicité, d'analyse ou de connexion sociale à des fins de collecte de données n'est inclus.

## Utilisateurs internationaux

L'app est conçue pour fonctionner hors ligne sur votre appareil. Les services Apple facultatifs sont soumis aux conditions d'Apple et à la disponibilité régionale.

## Modifications de cette politique

Nous pouvons mettre à jour cette politique de confidentialité de temps à autre. La date de « Dernière mise à jour » en haut sera modifiée, et la politique révisée sera publiée sur cette page de politique de confidentialité.

## Nous contacter

Si vous avez des questions sur cette politique de confidentialité ou sur nos pratiques en la matière :

- **E-mail :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Nous répondons généralement sous 48 heures.

</section>
<section lang="tr" markdown="1">

**Son güncelleme:** 23 Temmuz 2026

iHTC Studio ("biz" veya "bizim"), **iCouplet**'i (aynı zamanda "爱对联" / "愛對聯" olarak bilinir, Bundle ID `com.iHTCboy.iCouplet`) geliştirmiştir. Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlendiğini (ve işlenmediğini) açıklar. **Apple App Review** ve kullanıcılar bu sayfayı herkese açık gizlilik URL'si olarak kullanabilir.

## Özet (Apple Gizlilik Besin Etiketi ile uyum)

| Konu | Uygulamamız |
|-------|----------------|
| Hesap | **Gerekmez** — kayıt, e-posta ile giriş veya telefon numarası yok |
| iHTC Studio tarafından veri toplama | **Veri Toplanmaz** — kişisel verilerinizi alan bir arka uç **işletmiyoruz** |
| Ağ | Beyit (couplet) kütüphanesi, okuma, seslendirme, çalışma, widget'lar ve günlük bildirimler kurulumdan sonra **çevrimdışı** çalışır |
| Analiz / reklam / izleme | **Yok** — üçüncü taraf analiz, reklam veya izleme SDK'sı yok; App Tracking Transparency kullanılmaz |
| İsteğe bağlı Apple hizmetleri | **iCloud** (özel KVS'niz), paylaşım kartları için **Fotoğraf Kitaplığı (Yalnızca Ekleme)**, isteğe bağlı bahşiş için **StoreKit**, **yerel bildirimler**, isteğe bağlı **Canlı Etkinlikler** |

## Veri Toplama

Reklam veya analiz amacıyla kişisel bilgileri **toplamıyor, satmıyor veya paylaşmıyoruz**.

- **Hesap yok** — Bizimle hesap oluşturmadan tüm temel özellikleri kullanabilirsiniz.
- **Analiz veya reklam yok** — Uygulama ikili dosyası, bize bilgi gönderen üçüncü taraf analiz, reklam veya çökme raporlama SDK'ları içermez.
- **Beyit içeriği yüklenmez** — Okuma geçmişiniz, favorileriniz, çalışma ilerlemeniz ve tercihleriniz cihazınızda (ve isteğe bağlı olarak **kendi** iCloud'unuzda) kalır. **Bu uygulama için böyle sunucular işletmediğimizden** iHTC Studio sunucularına asla yüklenmezler.

## Uygulama Nasıl Çalışır

- **Yerleşik kütüphane** — Beyit JSON'u ve dizinler uygulama / widget paketinin içinde gelir. Göz atma ve çalışma için ağ isteği gerekmez.
- **Cihaz üzerinde konuşma** — Seslendirme, Apple'ın cihaz içi / sistem **AVSpeechSynthesizer** (TTS) özelliğini kullanır. Beyit metnini iHTC Studio'ya göndermeyiz.
- **Widget'lar ve App Group** — Widget'lar ve uygulama, cihazınızdaki `group.com.iHTCboy.iCouplet` App Group'u üzerinden tercihleri ve hafif durumu paylaşır.
- **Günlük bildirimler** — User Notifications ile yerel olarak zamanlanır. Bir bildirime dokunmak, cihazdaki bir beyit kimliğine derin bağlantı açar; sunucudan toplu gönderim yoktur.
- **Paylaşım kartları** — Görseller cihazda oluşturulur. Kaydetme, yalnızca kaydet'e dokunduğunuzda **Fotoğraf Kitaplığı yalnızca ekleme** iznini kullanır. Sistem Paylaşım Sayfası görseli **sizin seçtiğiniz** bir uygulamaya gönderebilir; bu durumda o hedefin gizlilik politikası geçerli olur.
- **İsteğe bağlı bahşiş** — "Geliştiriciye Bahşiş", Apple tarafından işlenen tüketilebilir bir **StoreKit** satın alımıdır. Ödeme kartı bilgilerinizi almayız.

## Cihazınızda Saklanan Veriler

| Veri | Nerede | Amaç |
|------|-------|---------|
| Beyit veritabanı | Uygulama / Widget paketi | Çevrimdışı okuma ve çalışma |
| Favoriler ve beyit listeleri | App Group UserDefaults | Yıldızlanan eserler ve kullanıcı listeleri |
| Okuma geçmişi / son okunan | App Group UserDefaults | Okumaya devam etme, geçmiş arayüzü |
| Çalışma ilerlemesi ve ustalık | App Group UserDefaults | 4 seviyeli ustalık, test durumu |
| Seri / yoklama | App Group UserDefaults | Öğrenme serileri |
| Görünüm ve okuma tercihleri | App Group UserDefaults | Tema, vurgu, dil, düzen, TTS, sekmeler, widget'lar |
| Günün beyiti önbelleği ve bildirim tercihleri | App Group UserDefaults | Bugünün kimliği, zamanlama saati, bağlamsal anahtar |
| Paylaşım kartı tercihleri | App Group UserDefaults | Son stil / oran seçimleri |
| Karşılama ve TipKit durumu | Standart UserDefaults (cihaz) | Karşılama rehberi / keşif ipuçları |
| Ana Ekran hızlı eylemleri | Sistem + yerel tercihler | Yapılandırdığınız en fazla 4 kısayol |
| Widget / Canlı Etkinlik anlık görüntüleri | App Group / ActivityKit | Zaten açtığınız görüntülenen metin |

Uygulamayı kaldırmak, uygulamayla ilişkili kum havuzu (sandbox) ve App Group verilerini siler (iOS/macOS davranışına tabidir). İsteğe bağlı iCloud kopyaları, siz temizleyene veya senkronizasyonu kapatıp başka yerden silene kadar **sizin** iCloud'unuzda kalır.

## iCloud Senkronizasyonu (İsteğe Bağlı)

Ayarlar'da **iCloud Senkronizasyonu**'nu etkinleştirirseniz, uygulama seçili kullanıcı verilerini **Apple Kimliğinize** bağlı Apple'ın **`NSUbiquitousKeyValueStore`** hizmeti aracılığıyla yansıtır:

- Favoriler
- Beyit listeleri
- Okuma geçmişi
- Çalışma ilerlemesi / ustalık
- Seri günleri

Senkronizasyon trafiği iHTC Studio'ya değil, **Apple iCloud'a** gider. Senkronizasyonu Ayarlar'dan devre dışı bırakabilirsiniz. iCloud içeriğinizi okuyamayız.

## İzinler

iCouplet, yalnızca bir özellik gerektirdiğinde izin ister:

| İzin | Ne zaman | Neden |
|------------|------|-----|
| Bildirimler | Günün Beyiti hatırlatıcılarını etkinleştirdiğinizde | Hatırlatma bildirimlerinin yerel zamanlanması |
| Fotoğraf Kitaplığı (Yalnızca Ekleme) | Bir paylaşım kartını kaydettiğinizde | Oluşturulan görseli yazmak; kitaplığın tamamına okuma erişimine ihtiyacımız yok |
| iCloud | Senkronizasyonu etkinleştirdiğinizde | Favorileri / listeleri / geçmişi / ilerlemeyi / serileri senkronize etmek |
| Canlı Etkinlikler (iOS) | Okuma Canlı Etkinliği'ni etkinleştirdiğinizde | Okuduğunuz beyiti Kilit Ekranı / Dynamic Island'da göstermek |
| Arka plan sesi (yetenek) | Arka planda seslendirmeyi etkinleştirdiğinizde | Uygulama ön planda değilken TTS'yi sürdürmek |

Kişiler, kesin Konum, Kamera, Mikrofon (sistem TTS oynatımı dışında) veya İzleme için izin **istemiyoruz**.

## Çocukların Gizliliği

iCouplet, 13 yaşın altındaki çocuklar (veya bölgenizdeki eşdeğer yaş) dahil hiç kimseden bilerek kişisel veri toplamaz. Veri toplayan bir arka uç işletmediğimiz için bizde saklanan bir çocuk profili yoktur.

## Üçüncü Taraflar

- **Apple** — App Store dağıtımı, isteğe bağlı StoreKit satın alımları, isteğe bağlı iCloud KVS, sistem TTS, seçtiğiniz Paylaşım Sayfası hedefleri ve işletim sistemi düzeyinde bildirim / Canlı Etkinlik teslimi.
- Veri toplama amacıyla reklam, analiz veya sosyal giriş için **başka hiçbir üçüncü taraf SDK'sı** yoktur.

## Uluslararası Kullanıcılar

Uygulama, cihazınızda çevrimdışı çalışacak şekilde tasarlanmıştır. İsteğe bağlı Apple hizmetleri Apple'ın şartlarına ve bölgesel kullanılabilirliğe tabidir.

## Bu Politikadaki Değişiklikler

Bu Gizlilik Politikası'nı zaman zaman güncelleyebiliriz. En üstteki "Son güncelleme" tarihi değişecek ve revize edilen politika bu Gizlilik Politikası sayfasında yayımlanacaktır.

## Bize Ulaşın

Bu Gizlilik Politikası veya gizlilik uygulamaları hakkında sorularınız varsa:

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Genellikle 48 saat içinde yanıt veririz.

</section>
