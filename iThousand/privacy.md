---
layout: doc
title: iThousand — Privacy Policy
app_id: iThousand
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iThousand (爱千字文) — fully offline primer literacy app, Data Not Collected, optional iCloud and Photo Library add-only.
---

<section lang="en" markdown="1">

**Last updated:** August 18, 2026

iHTC Studio ("we", "us" or "our") built **iThousand** (also known as "爱千字文" / "愛千字文", Bundle ID `com.iHTCboy.iThousand`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on **this page** as the public privacy policy for the app. For App Store Connect, open this Privacy Policy in your browser and copy the address from the address bar (the public site domain may change over time).

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration, email sign-in, or phone number |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your personal data |
| Network | Library, character cards, reading, recite, Primer Hall, Hunt, widgets, and daily notifications work **offline** after install |
| Analytics / ads / tracking | **None** — no third-party analytics, advertising, or tracking SDKs; no App Tracking Transparency use |
| Optional Apple services | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default), optional **system speech / translation** |

## Data Collection

We do **not** collect, sell, or share personal information for advertising or analytics.

- **No account** — You can use all core features without creating an account with us.
- **No analytics or ads** — The app binary does not integrate third-party analytics, advertising, or crash-reporting SDKs that phone home to us.
- **No content upload** — Your reading history, favorites, lists (千单), saved characters, notes, study progress, streaks, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## How the App Works

- **Bundled library** — Passage JSON, vernacular/English, pinyin, character cards, stroke-order data, and indexes ship inside the app / widget bundle (curated from public web sources). Browsing and study do not require a network request.
- **On-device speech** — Recitation uses Apple’s system **AVSpeechSynthesizer** (TTS). We do not send passage text to iHTC Studio.
- **Optional system translation** — If you use Apple’s on-device / system translation features, processing stays with Apple’s OS. We do not operate a translation backend.
- **Widgets & App Group** — Widgets and the app share preferences and lightweight state via App Group `group.com.iHTCboy.iThousand` on your device.
- **Daily notifications** — Scheduled locally with User Notifications. Tapping a notification opens a deep link to a passage ID on device; no server fan-out.
- **Share cards** — Images are rendered on device. Saving uses **Photo Library add-only** only when you tap save. System Share Sheet may send the image to an app **you** choose; that destination’s privacy policy then applies.
- **Optional tip** — “Tip Developer” (`com.iHTCboy.iThousand.6`) is a consumable **StoreKit** purchase processed by Apple. We do not receive your payment card details.
- **Siri / Shortcuts / Control Center** — Optional system integrations open on-device deep links; they do not send your library to us.
- **Optional Spotlight** — Off by default. If you enable indexing, passages and character cards are indexed by the system on device for local search; we do not operate a search backend.
- **Feedback email** — If you send Feedback, the message may include text you write plus device / app diagnostics (version, OS, language) solely for troubleshooting.

## Data Stored on Your Device

| Data | Where | Purpose |
|------|-------|---------|
| Passage & character database | App / Widget bundle | Offline reading, literacy cards & study |
| Favorites & lists (千单) | App Group UserDefaults | Starred passages and user lists |
| Saved characters & famous-line favorites | App Group UserDefaults | Hard-character bookmarks, starred lines |
| Reading history / last read | App Group UserDefaults | Continue reading, history UI |
| Study progress & mastery | App Group UserDefaults | Primer Hall state, quiz / Hunt progress |
| Notes | App Group UserDefaults | Passage notes you write |
| Study streak / check-in | App Group UserDefaults | Daily habit |
| Appearance & reading prefs | App Group UserDefaults | Theme, accent, language, layout, TTS, tabs, widgets, font scale |
| Daily Line cache & notification prefs | App Group UserDefaults | Today’s ID, schedule time, contextual toggle |
| Share-card preferences | App Group UserDefaults | Last style / ratio choices |
| Onboarding & TipKit state | Standard UserDefaults (device) | Welcome guide / discovery tips |
| Home Screen quick actions | System + local prefs | Shortcuts you configure |
| Widget / Live Activity snapshots | App Group / ActivityKit | Display text you already opened |

Uninstalling the app removes sandbox and App Group data associated with the app (subject to iOS/macOS behavior). Optional iCloud copies remain in **your** iCloud until you clear them or turn sync off and delete elsewhere.

## iCloud Sync (Optional)

If you enable **iCloud Sync** in Settings, the app mirrors selected user data through Apple’s **`NSUbiquitousKeyValueStore`** tied to **your Apple ID**:

- Favorites
- Lists (千单)
- Saved characters / famous-line favorites
- Reading history
- Study progress / mastery
- Study streaks
- Notes

Sync traffic goes to **Apple iCloud**, not to iHTC Studio. You can disable sync in Settings. We cannot read your iCloud contents.

## Permissions

iThousand requests permissions only when a feature needs them:

| Permission | When | Why |
|------------|------|-----|
| Notifications | You enable Daily Line reminders | Local scheduling |
| Photo Library (Add Only) | You save a share card or character image | Write the rendered image |
| iCloud | You enable sync | Sync favorites / lists / history / progress / streaks / notes / saved characters |
| Live Activities (iOS) | You enable Reading Live Activity | Lock Screen / Dynamic Island |
| Background audio | You enable background recitation | Continue TTS in background |

We do **not** request Contacts, precise Location, Camera, Microphone (beyond system TTS playback), or Tracking.

## Children’s Privacy

iThousand is an educational literacy app for a general audience and is **not** in the Kids Category. We do not knowingly collect personal information from children. The app does not require an account. Families may use reading and character-card features offline on their own devices.

## Third Parties

The only third-party services involved in normal use are **Apple** (App Store, iCloud, StoreKit, system TTS, optional system translation, notifications, Live Activities, Spotlight).

## Data Retention & Deletion

- **On device:** You can clear study progress, history, or notes in the app. Delete the app to remove local sandbox and App Group data (subject to system behavior).
- **iCloud:** Disable sync in Settings; you may also manage iCloud storage in system Settings.
- **We do not retain copies** of your reading, notes, or character bookmarks on iHTC Studio servers.

## Changes to This Policy

We may update this page for legal, product, or App Store compliance reasons. The “Last updated” date will change. Continued use after an update means you accept the revised policy.

## Contact

Questions about privacy: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="zh-CN" markdown="1">

**最近更新：** 2026 年 8 月 18 日

爱火腿肠工作室（iHTC Studio）（「我们」）开发了 **爱千字文**（iThousand / 愛千字文，Bundle ID `com.iHTCboy.iThousand`）。本隐私政策说明你在使用本应用时，数据如何被处理。本页可作为 **App Store 审核**与用户查阅的公开隐私政策地址。在 App Store Connect 填写隐私政策 URL 时，请在浏览器中打开本 [隐私政策](../privacy) 页，从地址栏复制当前网址（公开站点域名日后可能变更）。

## 概要（对齐 App Store 隐私标签）

| 主题 | 我们的做法 |
|------|------------|
| 账号 | **不需要** — 无注册、邮箱登录或手机号 |
| 爱火腿肠工作室的数据收集 | **不收集数据** — 我们**不**运营接收你个人数据的后端 |
| 网络 | 安装后，语料、字卡、阅读、诵读、蒙学堂、寻字、小组件与每日通知可**离线** |
| 分析 / 广告 / 追踪 | **无** — 无第三方分析、广告或追踪 SDK；不使用 App 追踪透明度 |
| 可选 Apple 服务 | **iCloud**（你的私有 KVS）、分享卡的**相册（仅添加）**、**StoreKit** 打赏、**本地通知**、可选**实时活动**、可选 **Spotlight**（默认关）、可选**系统朗读 / 翻译** |

## 数据收集

我们**不**为广告或分析收集、出售或共享个人信息。

- **无账号** — 无需向我们注册即可使用全部核心功能。
- **无分析或广告** — 应用未集成会向我们家上报的第三方分析、广告或崩溃 SDK。
- **不上传内容** — 阅读记录、收藏、千单、生字本、笔记、学堂进度与偏好留在你的设备（以及可选的**你的** iCloud），不会上传到 iHTC Studio 服务器，因为**我们不为本应用运营此类服务器**。

## 应用如何工作

- **内置语料** — 篇目 JSON、白话/英文、拼音、字卡、笔顺与索引随 App / 小组件安装（由网络公开资料梳理）。
- **本机朗读** — 使用系统 **AVSpeechSynthesizer**（TTS）；篇章正文不会发送给我们。
- **可选系统翻译** — 若你使用 Apple 系统翻译，处理留在系统侧；我们无翻译后端。
- **小组件与 App Group** — 通过 `group.com.iHTCboy.iThousand` 在本机共享状态。
- **每日通知** — 仅本机调度；点击通过深链打开对应篇目 ID。
- **分享卡** — 本机渲染；仅在你点保存时使用**相册（仅添加）**。
- **可选打赏** — `com.iHTCboy.iThousand.6` 消耗型内购由 **Apple StoreKit** 处理。
- **Siri / 快捷指令 / 控制中心** — 打开本机深链，不上传语料。
- **可选 Spotlight** — 默认关闭；开启后由系统本机索引篇目与字卡。
- **反馈邮件** — 你主动发送时可能包含自愿填写内容与设备/应用诊断信息，仅用于排查。

## 设备上存储的数据

| 数据 | 位置 | 用途 |
|------|------|------|
| 篇目与字卡语料库 | App / 小组件包 | 离线阅读、识字与学堂 |
| 收藏与千单 | App Group UserDefaults | 星标与用户清单 |
| 生字本与名句收藏 | App Group UserDefaults | 难字书签、星标名句 |
| 阅读记录 / 上次阅读 | App Group UserDefaults | 继续阅读、历史界面 |
| 学堂进度与掌握度 | App Group UserDefaults | 蒙学堂、测验/寻字 |
| 笔记 | App Group UserDefaults | 你写下的篇目笔记 |
| 研习打卡连续 | App Group UserDefaults | 每日一句习惯 |
| 外观与阅读偏好 | App Group UserDefaults | 主题、强调色、语言、布局、TTS、Tab、小组件、字号 |
| 每日一句缓存与通知偏好 | App Group UserDefaults | 今日 ID、提醒时间 |
| 分享卡偏好 | App Group UserDefaults | 上次样式选择 |
| 引导与 TipKit 状态 | 标准 UserDefaults | 欢迎引导 |
| 主屏快捷操作 | 系统 + 本地偏好 | 你配置的快捷 |
| 小组件 / 实时活动快照 | App Group / ActivityKit | 你已打开内容的展示 |

卸载应用会移除与该应用关联的沙盒与 App Group 数据（以 iOS/macOS 行为为准）。可选 iCloud 副本留在**你的** iCloud 中，直至你关闭同步或在别处删除。

## iCloud 同步（可选）

在设置中开启 **iCloud 同步**后，应用通过 Apple **`NSUbiquitousKeyValueStore`**（绑定**你的 Apple ID**）镜像：

- 收藏
- 千单
- 生字本 / 名句收藏
- 阅读记录
- 学堂进度 / 掌握度
- 研习打卡连续
- 笔记

同步流量发往 **Apple iCloud**，而非 iHTC Studio。可在设置中关闭。我们无法读取你的 iCloud 内容。

## 权限

仅在功能需要时请求：

| 权限 | 何时 | 原因 |
|------|------|------|
| 通知 | 你开启每日一句提醒 | 本机调度 |
| 相册（仅添加） | 你保存千卡或字卡图 | 写入渲染图片 |
| iCloud | 你开启同步 | 同步收藏/千单/记录/进度/打卡/笔记/生字 |
| 实时活动（iOS） | 你开启品读实时活动 | 锁屏 / 灵动岛 |
| 后台音频 | 你开启后台诵读 | 后台继续 TTS |

我们**不**请求通讯录、精确位置、相机、麦克风（除系统 TTS 播放外）或追踪。

## 儿童隐私

本应用面向一般公众的教育阅读，**非**儿童类别。我们不会有意收集儿童个人信息；应用无需账号。家庭可在自有设备上离线使用品读与字卡功能。

## 第三方

正常使用中涉及的第三方仅为 **Apple**（App Store、iCloud、StoreKit、系统 TTS、可选系统翻译、通知、实时活动、Spotlight）。

## 保留与删除

- **本机：** 可在应用内清除进度、历史或笔记；删除应用可移除本地数据。
- **iCloud：** 在设置中关闭同步，或在系统设置中管理 iCloud 存储。
- **我们不在服务器保留**你的阅读、笔记或生字数据副本。

## 政策变更

我们可能因法律、产品或 App Store 合规需要更新本页；「最近更新」日期会随之变更。继续使用即表示接受修订后的政策。

## 联系

隐私相关问题：[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="zh-TW" markdown="1">

**最近更新：** 2026 年 8 月 18 日

愛火腿腸工作室（iHTC Studio）（「我們」）開發了 **愛千字文**（iThousand，Bundle ID `com.iHTCboy.iThousand`）。本隱私政策說明你在使用本應用時，資料如何被處理。本頁可作為 **App Store 審核**與使用者查閱的公開隱私政策地址。在 App Store Connect 填寫隱私政策 URL 時，請在瀏覽器中開啟本 [隱私政策](../privacy) 頁，從網址列複製目前網址（公開站點網域日後可能變更）。

## 概要（對齊 App Store 隱私標籤）

| 主題 | 我們的做法 |
|------|------------|
| 帳號 | **不需要** |
| 愛火腿腸工作室的資料收集 | **不收集資料** |
| 網路 | 安裝後，語料、字卡、閱讀、誦讀、蒙學堂、尋字、小工具與每日通知可**離線** |
| 分析 / 廣告 / 追蹤 | **無** |
| 可選 Apple 服務 | **iCloud**、分享卡的**照片（僅加入）**、**StoreKit** 打賞、**本地通知**、可選**即時動態**、可選 Spotlight（預設關）、可選系統朗讀 / 翻譯 |

## 資料收集

我們**不**為廣告或分析收集、出售或共享個人資訊。閱讀記錄、收藏、千單、生字本、筆記、學堂進度與偏好留在你的裝置（以及可選的**你的** iCloud），不會上傳到 iHTC Studio 伺服器。

## 應用如何工作

- **內建語料** — 篇目 JSON、白話/英文、拼音、字卡、筆順與索引隨 App / 小工具安裝（由網絡公開資料梳理）。
- **本機朗讀** — 使用系統 TTS。
- **可選系統翻譯** — 處理留在 Apple 系統側。
- **小工具與 App Group** — `group.com.iHTCboy.iThousand` 本機共享。
- **每日通知** — 僅本機排程。
- **分享卡** — 本機渲染；**照片（僅加入）**。
- **可選打賞** — `com.iHTCboy.iThousand.6` 由 Apple 處理。

## 裝置上儲存的資料

含篇目與字卡語料、收藏與千單、生字本與名句收藏、閱讀記錄、學堂進度、筆記、研習打卡、外觀與閱讀偏好、每日一句快取、分享卡偏好、引導狀態、主屏快捷與小工具/即時動態快照（詳見英文版表格）。

## iCloud 同步（可選）

可同步：收藏、千單、生字本/名句收藏、閱讀記錄、學堂進度/掌握度、研習打卡、筆記。流量走 **Apple iCloud**。

## 權限

通知、照片（僅加入）、iCloud、即時動態、背景音訊——僅在對應功能開啟時使用。不請求通訊錄、精確位置、相機、麥克風（除系統 TTS）或追蹤。

## 兒童隱私

面向一般公眾的教育閱讀，**非**兒童類別；無需帳號。

## 第三方

僅 **Apple** 系統服務。

## 保留與刪除

刪除應用可移除本機資料；iCloud 可在設定中關閉。我們不在伺服器保留你的資料副本。

## 政策變更

「最近更新」日期會隨修訂變更。

## 聯絡

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ja" markdown="1">

**最終更新日:** 2026年8月18日

iHTC Studio（「当社」）は **iThousand**（「爱千字文」／「爱千字文」、Bundle ID `com.iHTCboy.iThousand`）を開発しました。本プライバシーポリシーは、本アプリの利用時にどのデータが取り扱われ、取り扱われないかを説明します。**Apple App Review** とユーザーは、**本ページ**を公開のプライバシーポリシーとして参照できます。App Store Connect では、ブラウザで本プライバシーポリシーを開き、アドレスバーから URL をコピーしてください（公開サイトのドメインは将来変更される場合があります）。

## 概要（Apple プライバシー栄養表示との整合性）

| トピック | 当社の方針 |
|-------|----------------|
| アカウント | **不要** — 登録、メールサインイン、電話番号は必要ありません |
| iHTC Studioによるデータ収集 | **データは収集しません** — 個人データを受け取るバックエンドは運営していません |
| ネットワーク | ライブラリ、character cards, reading, recite, Primer Hall, Hunt, widgets, and daily notifications work **offline** after installは、インストール後 **オフライン** で動作します |
| 分析 / 広告 / トラッキング | **なし** — サードパーティの分析、広告、トラッキングSDKは使用しておらず、App Tracking Transparencyも使用していません |
| 任意の Apple サービス | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for 任意チップ, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default), optional **system speech / translation** |

## データの収集

当社は、広告や分析のために個人情報を収集、販売、共有することは**ありません**。

- **アカウント不要** — アカウントを作成せずに、すべての基本機能を使用できます。
- **分析や広告なし** — アプリのバイナリには、サードパーティの分析、広告、クラッシュレポートSDKは統合されておらず、データが当社に送信されることはありません。
- **コンテンツのアップロードなし** — お客様のreading history, favorites, lists (千单), saved characters, notes, study progress, streaks, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## アプリの仕組み

- **同梱ライブラリ** — テキスト JSON、白話／英語、索引、学習補助はアプリ／ウィジェット バンドル内に同梱されます。閲覧と学習にネットワークは不要です。
- **オンデバイス音声** - 朗読には Apple のシステム **AVSpeechSynthesizer** (TTS) が使用されます。 iHTC Studio には文章テキストは送信されません。
- **任意のシステム翻訳** — Apple の端末内/システム翻訳を使う場合、処理は Apple OS 内です。
- **ウィジェットと App Group** — ウィジェットとアプリは、端末上の App Group `group.com.iHTCboy.iThousand` を通じて設定と軽量な状態を共有します。
- **毎日の通知** - ユーザー通知を使用してローカルにスケジュールされます。 通知をタップすると、デバイス上のパッセージ ID へのディープ リンクが開きます。 サーバーのファンアウトはありません。
- **カードを共有** — 画像はデバイス上でレンダリングされます。 保存すると、[保存] をタップした場合にのみ **フォト ライブラリの追加のみ**が使用されます。 システム共有シートは、**あなた**が選択したアプリに画像を送信できます。 その場合、その宛先のプライバシー ポリシーが適用されます。
- **任意チップ** — 「Tip Developer」（`com.iHTCboy.iThousand.6`）は Apple 処理の消耗型 **StoreKit** 購入です。カード情報は受け取りません。
- **Siri / ショートカット / コントロール センター** — オプションのシステム統合により、デバイス上のディープ リンクが開きます。 彼らはあなたのライブラリを私たちに送ることはありません。
- **任意 Spotlight** — 既定オフ。有効時、篇と文字カードは端末上でシステムが索引し、ローカル検索に使います。検索バックエンドは運営しません。
- **フィードバックメール** — 送信内容に、お客様の文面とトラブルシュート用の端末/アプリ診断（バージョン、OS、言語）が含まれる場合があります。

## 端末に保存されるデータ

 | データ | どこ | 目的 |
 |------|-------|-----------|
| 篇目・文字データベース | App / Widget バンドル | オフライン閲読・識字カード・学習 |
| お気に入りとリスト（千单） | App Group UserDefaults | 星付きの篇目とユーザーリスト |
| 保存文字と名文お気に入り | App Group UserDefaults | 難字ブックマーク・星付き行 |
 | 読書履歴 / 最後に読んだ | アプリグループのUserDefaults | 続きを読む、履歴 UI |
| 学習進捗と習熟 | App Group UserDefaults | Primer Hall state, quiz / Hunt progress |
| メモ | App Group UserDefaults | 篇についてのメモ |
| 学習連続 / チェックイン | App Group UserDefaults | 毎日の習慣 |
| 共有カードの設定 | App Group の UserDefaults | 最後に選んだスタイルや比率 |
 | 毎日の Line キャッシュと通知設定 | アプリグループのUserDefaults | 今日の ID、スケジュール時刻、コンテキストの切り替え |
 | 共有カードの設定 | アプリグループのUserDefaults | 最後のスタイル/比率の選択 |
 | オンボーディングと TipKit の状態 | 標準 UserDefaults (デバイス) | ウェルカムガイド / 発見のヒント |
 | ホーム画面のクイックアクション | システム + ローカル設定 | 設定するショートカット |
 | ウィジェット / ライブ アクティビティのスナップショット | アプリグループ / ActivityKit | すでに開いているテキストを表示 |

アプリをアンインストールすると、アプリに関連するサンドボックスおよびApp Groupデータが削除されます（iOS/macOSの動作に依存します）。任意のiCloudコピーは、あなたが削除するか、同期をオフにして他の場所で削除するまで、**あなたの**iCloudに残ります。

## iCloud同期（オプション）

設定で**iCloud同期**を有効にすると、アプリは選択したユーザーデータをAppleの**`NSUbiquitousKeyValueStore`**を通じてあなたのApple IDに関連付けて同期します：

- お気に入り
- リスト（千单）
- 保存した字 / 名文お気に入り
- 読書履歴
- 学習進捗 / 習熟度
- 学習連続記録
 - 注意事項

同期トラフィックは**Apple iCloud**にのみ送信され、iHTC Studioには送信されません。設定で同期を無効にできます。私たちはあなたのiCloudの内容を読むことはできません。

## 権限

 iLiezi は、機能が必要な場合にのみアクセス許可を要求します。

| 権限 | タイミング | 理由 |
|------------|------|-----|
| 通知 | Daily Line reminders を有効にする | ローカルスケジュール |
| 写真ライブラリ（追加のみ） | 共有カード/文字画像を保存 | Write the rendered image |
| iCloud | 同期を有効にする | お気に入り/リスト/履歴/進捗/連続/メモ/保存文字を同期 |
設定で **iCloud 同期**を有効にすると、アプリは **お客様の Apple ID** に紐づく Apple の **`NSUbiquitousKeyValueStore`** を通じて、選択したユーザーデータをミラーリングします。
| バックグラウンド音声 | バックグラウンド朗誦を有効にする | バックグラウンドで TTS 継続 |

 当社は、連絡先、正確な位置情報、カメラ、マイク (システムの TTS 再生を超える)、または追跡を要求しません**。

## 子供のプライバシー

iThousand は一般向け識字アプリで **Kids Category 外**です。児童情報を故意に収集しません。アカウント不要。家族はオフラインで文字カード機能を利用できます。

## 第三者

通常利用の第三者は **Apple** のみ（…任意システム翻訳、Spotlight 含む）。

## データ保持と削除

- **端末上:** アプリ内で学習進捗・履歴・メモを消せます。アプリ削除で sandbox / App Group を削除（OS 依存）。
- **iCloud:** 設定で同期をオフにできます。システム設定で iCloud ストレージも管理できます。
- **当社は保持しません** — 閲読・メモ・文字ブックマークのコピーをサーバーに保持しません。

## このポリシーの変更

法令、製品、または App Store コンプライアンスの理由で本ページを更新することがあります。上部の「最終更新日」が変更されます。更新後も利用を続ける場合、改訂版に同意したものとみなされます。

## お問い合わせ

プライバシーに関するご質問: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ko" markdown="1">

**마지막 업데이트:** 2026년 8월 18일

iHTC Studio("당사")는 **iThousand**("爱千字文" / "爱千字文", Bundle ID `com.iHTCboy.iThousand`)을(를) 개발했습니다. 본 개인정보 처리방침은 앱 사용 시 어떤 데이터가 처리되고 처리되지 않는지 설명합니다. **Apple App Review**와 사용자는 **이 페이지**를 공개 개인정보 처리방침으로 사용할 수 있습니다. App Store Connect에는 브라우저에서 본 개인정보 처리방침을 열고 주소창의 URL을 복사하세요(공개 사이트 도메인은 변경될 수 있습니다).

## 요약 (Apple 개인정보 영양성분표 정렬)

| 주제 | 당사의 정책 |
|-------|----------------|
| 계정 | **필요 없음** — 등록, 이메일 로그인, 전화번호 필요 없음 |
| iHTC 스튜디오의 데이터 수집 | **데이터 수집 없음** — 개인 데이터를 받는 백엔드를 운영하지 않습니다 |
| 네트워크 | 라이브러리, character cards, reading, recite, Primer Hall, Hunt, widgets, and daily notifications work **offline** after install는 설치 후 **오프라인**으로 동작합니다 |
| 분석 / 광고 / 추적 | **없음** — 타사 분석, 광고, 추적 SDK 없음; 앱 추적 투명성(App Tracking Transparency) 사용 없음 |
| 선택 Apple 서비스 | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default), optional **system speech / translation** |

## 데이터 수집

개인 정보를 광고나 분석 목적으로 **수집, 판매, 공유하지 않습니다**.

- **계정 불필요** — 계정을 만들지 않아도 모든 핵심 기능을 사용할 수 있습니다.
- **분석 및 광고 없음** — 앱 바이너리는 당사로 데이터를 전송하는 타사 분석, 광고, 크래시 리포트 SDK를 통합하지 않습니다.
- **콘텐츠 업로드 없음** — 사용자의 reading history, favorites, lists (千单), saved characters, notes, study progress, streaks, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## 앱 작동 방식

- **번들 라이브러리** — 텍스트 JSON, vernacular/English, 색인, 학습 보조 자료가 앱/위젯 번들에 포함됩니다. 탐색과 학습에 네트워크가 필요하지 않습니다.
- **기기 내 음성** — 암송은 Apple 시스템 **AVSpeechSynthesizer**(TTS)를 사용합니다. iHTC Studio에는 문구 텍스트를 보내지 않습니다.
- **선택 시스템 번역** — Apple 기기/시스템 번역 사용 시 Apple OS에서 처리.
- **위젯 및 App Group** — 위젯과 앱은 기기의 App Group `group.com.iHTCboy.iThousand`을 통해 설정과 가벼운 상태를 공유합니다.
- **일일 알림** — 사용자 알림을 통해 로컬로 예약됩니다. 알림을 탭하면 기기의 통로 ID에 대한 딥 링크가 열립니다. 서버 팬아웃이 없습니다.
- **카드 공유** — 이미지가 장치에서 렌더링됩니다. 저장은 저장을 탭한 경우에만 **사진 라이브러리 추가 전용**을 사용합니다. 시스템 공유 시트는 **귀하가** 선택한 앱으로 이미지를 보낼 수 있습니다. 그러면 해당 목적지의 개인정보 보호정책이 적용됩니다.
- **선택 팁** — “Tip Developer”(`com.iHTCboy.iThousand.6`) Apple **StoreKit** 구매. 카드 정보 미수신.
- **Siri / 바로가기 / 제어 센터** — 선택적 시스템 통합으로 기기 내 딥 링크가 열립니다. 그들은 귀하의 라이브러리를 우리에게 보내지 않습니다.
- **선택 Spotlight** — 기본 끔. 구절·문자 카드를 기기에서 색인, 로컬 검색. 검색 백엔드 없음.
- **피드백 이메일** — 보내신 글과 문제 해결용 기기/앱 진단(버전, OS, 언어)이 포함될 수 있습니다.

## 귀하의 장치에 저장된 데이터

| 데이터 | 어디 | 목적 |
|------|-------|---------|
| 구절·문자 DB | App / Widget 번들 | 오프라인·识读 카드·학습 |
| 즐겨찾기 및 목록(千单) | App Group UserDefaults | 별표 표시한 구절과 사용자 목록 |
| 저장 글자·명문 즐겨찾기 | App Group UserDefaults | 어려운 글자·별표 줄 |
| 읽은 이력/마지막 읽은 내용 | 앱 그룹 UserDefaults | 계속 읽기, 기록 UI |
| 학습 진행 및 숙달 | App Group UserDefaults | Primer Hall state, quiz / Hunt progress |
| 메모 | App Group UserDefaults | 구절 메모 |
| 학습 연속 / 체크인 | App Group UserDefaults | 매일 습관 |
| 공유 카드 설정 | App Group UserDefaults | 마지막으로 선택한 스타일 / 비율 |
| 일일 라인 캐시 및 알림 환경 설정 | 앱 그룹 UserDefaults | 오늘의 아이디, 일정시간, 상황별 토글 |
| 공유 카드 환경 설정 | 앱 그룹 UserDefaults | 마지막 스타일/비율 선택 |
| 온보딩 및 TipKit 상태 | 표준 UserDefaults(장치) | 환영 가이드/탐색 팁 |
| 홈 화면 빠른 작업 | 시스템 + 로컬 환경설정 | 구성한 바로가기 |
| 위젯/실시간 활동 스냅샷 | 앱 그룹/ActivityKit | 이미 열어본 텍스트 표시 |

앱을 삭제하면 앱과 연관된 샌드박스 및 앱 그룹 데이터가 제거됩니다(iOS/macOS 동작에 따라 다름). 선택적으로 iCloud에 저장된 복사본은 사용자가 삭제하거나 동기화를 끄고 다른 곳에서 삭제할 때까지 **귀하의** iCloud에 남아 있습니다.

## iCloud 동기화 (선택 사항)

설정에서 **iCloud 동기화**를 활성화하면, 앱은 **귀하의 Apple ID**와 연결된 Apple의 **`NSUbiquitousKeyValueStore`**를 통해 선택한 사용자 데이터를 미러링합니다:

- 즐겨찾기
- 목록(千单)
- 저장한 글자 / 명문 즐겨찾기
- 읽기 기록
- 학습 진행/숙련도
- 학습 연속
- 메모

동기화 트래픽은 iHTC Studio가 아닌 **Apple iCloud**로 전송됩니다. 설정에서 동기화를 비활성화할 수 있습니다. 우리는 귀하의 iCloud 내용을 읽을 수 없습니다.

## 권한

iLiezi는 기능에 필요한 경우에만 권한을 요청합니다.

| 허가 | 언제 | 왜? |
|------------|------|-----|
| 알림 | Daily Line reminders 사용 | 로컬 예약 |
| 사진 보관함(추가 전용) | 공유 카드/글자 이미지 저장 | Write the rendered image |
| iCloud | 동기화 사용 | 즐겨찾기/목록/기록/진행/연속/메모/저장 글자 |
설정에서 **iCloud 동기화**를 켜면 앱은 **사용자의 Apple ID**에 연결된 Apple의 **`NSUbiquitousKeyValueStore`**를 통해 일부 사용자 데이터를 미러링합니다.
| 배경 오디오 | 배경 낭송 사용 | 백그라운드 TTS |

우리는 연락처, 정확한 위치, 카메라, 마이크(시스템 TTS 재생 이외) 또는 추적을 요청하지 **않습니다**.

## 아동 개인정보 보호

iThousand는 일반 대상识读 앱, **Kids Category 아님**. 아동 정보 수집 안 함. 오프라인 문자 카드.

## 제3자

제3자는 **Apple**만(…선택 시스템 번역, Spotlight).

## 데이터 보존 및 삭제

- **기기에서:** 앱에서 학습·기록·메모 삭제 가능. 앱 삭제로 sandbox/App Group 제거.
- **iCloud:** 설정에서 동기화 끄기. 시스템 설정에서 iCloud 저장공간 관리.
- **보관하지 않습니다** — 읽기·메모·글자 북마크 사본 없음.

## 이 정책의 변경

법적, 제품 또는 App Store 준수 사유로 본 페이지를 업데이트할 수 있습니다. 상단의 「최종 업데이트」 날짜가 변경됩니다. 업데이트 후 계속 사용하면 개정된 정책에 동의하는 것입니다.

## 연락처

개인정보 관련 문의: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ru" markdown="1">

**Последнее обновление:** 18 августа 2026 г.

iHTC Studio («мы») создала **iThousand** («爱千字文» / «爱千字文», Bundle ID `com.iHTCboy.iThousand`). Настоящая Политика конфиденциальности объясняет, какие данные обрабатываются (и не обрабатываются) при использовании приложения. **Apple App Review** и пользователи могут использовать **эту страницу** как публичную политику конфиденциальности. Для App Store Connect откройте эту страницу в браузере и скопируйте URL из адресной строки (домен публичного сайта может измениться).

## Сводка (в соответствии с меткой Apple Privacy Nutrition)

| Тема | Наша практика |
|-------|----------------|
| Учетная запись | **Не требуется** — регистрация, вход по электронной почте или номеру телефона не нужны |
| Сбор данных iHTC Studio | **Данные не собираются** — мы **не** используем серверную часть, которая получает ваши личные данные |
| Сеть | Библиотека, character cards, reading, recite, Primer Hall, Hunt, widgets, and daily notifications work **offline** after install работают **офлайн** после установки |
| Аналитика / реклама / отслеживание | **Отсутствует** — нет сторонней аналитики, рекламы или SDK для отслеживания; не используется App Tracking Transparency |
| Необязательные сервисы Apple | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default), optional **system speech / translation** |

## Сбор данных

Мы **не** собираем, не продаем и не делимся личной информацией для рекламы или аналитики.

- **Без аккаунта** — Вы можете использовать все основные функции без создания аккаунта у нас.
- **Без аналитики и рекламы** — В приложении не интегрированы сторонние SDK для аналитики, рекламы или отчётов о сбоях, которые отправляли бы данные нам.
- **Без загрузки контента** — Ваши reading history, favorites, lists (千单), saved characters, notes, study progress, streaks, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## Как работает приложение

- **Встроенная библиотека** — текстовый JSON, vernacular/English, указатели и учебные материалы входят в пакет app/widget. Для просмотра и обучения сеть не нужна.
- **Речь на устройстве** — при декламации используется система Apple **AVSpeechSynthesizer** (TTS). Мы не отправляем текст прохождения в iHTC Studio.
- **Системный перевод** — функции Apple на устройстве; обработка в OS Apple.
- **Виджеты и App Group** — виджеты и приложение обмениваются настройками и лёгким состоянием через App Group `group.com.iHTCboy.iThousand` на вашем устройстве.
- **Ежедневные уведомления** — планируются локально с помощью уведомлений пользователя. При нажатии на уведомление открывается глубокая ссылка на идентификатор прохода на устройстве; нет разветвления сервера.
- **Поделиться картами** — изображения отображаются на устройстве. При сохранении используется **Дополнение «Библиотека фотографий»** только при нажатии «Сохранить». System Share Sheet может отправить изображение в приложение, выбранное вами **; В этом случае применяется политика конфиденциальности этого пункта назначения.
- **Чаевые** — «Tip Developer» (`com.iHTCboy.iThousand.6`), **StoreKit** через Apple. Данные карты не получаем.
- **Siri / Ярлыки / Центр управления** — дополнительные системные интеграции открывают глубокие ссылки на устройстве; они не отправляют нам вашу библиотеку.
- **Необязательный Spotlight** — выкл. по умолчанию. Фрагменты и карточки индексируются на устройстве; без search backend.
- **Email обратной связи** — сообщение может включать ваш текст и диагностику устройства/приложения (версия, ОС, язык) только для устранения неполадок.

## Данные, хранящиеся на вашем устройстве

| Данные | Где | Цель |
|------|-------|---------|
| База фрагментов и иероглифов | Пакет App / Widget | Офлайн, карточки грамотности |
| Избранное и списки (千单) | UserDefaults App Group | Отмеченные фрагменты и пользовательские списки |
| Сохранённые иероглифы и строки | UserDefaults App Group | Закладки сложных иероглифов |
| История чтения / последнее чтение | Пользовательские настройки группы приложений | Продолжить чтение, история пользовательского интерфейса |
| Прогресс и mastery | UserDefaults App Group | Primer Hall state, quiz / Hunt progress |
| Заметки | UserDefaults App Group | Заметки к фрагментам |
| Серия учёбы / check-in | UserDefaults App Group | Ежедневная привычка |
| Настройки карточек для обмена | UserDefaults App Group | Последний выбранный стиль / соотношение сторон |
| Настройки кэша и уведомлений Daily Line | Пользовательские настройки группы приложений | Идентификатор сегодняшнего дня, время расписания, контекстное переключение |
| Настройки карты обмена | Пользовательские настройки группы приложений | Последний выбор стиля/пропорции |
| Регистрация и состояние TipKit | Стандартные настройки пользователя (устройство) | Приветственное руководство / советы по открытию |
| Быстрые действия на главном экране | Система + локальные настройки | Ярлыки, которые вы настраиваете |
| Виджет / Снимки активности в реальном времени | Группа приложений / ActivityKit | Показать текст, который вы уже открыли |

При удалении приложения удаляются данные песочницы и группы приложений, связанные с приложением (в зависимости от поведения iOS/macOS). Дополнительные копии iCloud остаются в **вашем** iCloud до тех пор, пока вы не очистите их или не отключите синхронизацию и не удалите их в другом месте.

## Синхронизация с iCloud (необязательно)

Если вы включите **iCloud Sync** в настройках, приложение зеркально отображает выбранные пользовательские данные через **`NSUbiquitousKeyValueStore`** Apple, привязанный к **вашему Apple ID**:

- Избранное
- Списки (千单)
- Сохранённые иероглифы / избранные строки
- Чтение истории
- Прогресс в учебе/мастерстве
- Учебные серии
- Примечания

Трафик синхронизации поступает в **Apple iCloud**, а не в iHTC Studio. Вы можете отключить синхронизацию в настройках. Мы не можем прочитать ваше содержимое iCloud.

## Разрешения

iLiezi запрашивает разрешения только тогда, когда они нужны функции:

| Разрешение | Когда | Почему |
|------------|------|-----|
| Уведомления | Вы включаете Daily Line reminders | Локальное планирование |
| Фототека (только добавление) | Share card / иероглиф | Write the rendered image |
| iCloud | Включаете синхронизацию | Избранное/списки/история/прогресс/серии/заметки/сохранённые иероглифы |
Если вы включите **синхронизацию iCloud** в настройках, приложение отражает выбранные пользовательские данные через **`NSUbiquitousKeyValueStore`** от Apple, привязанное к **вашему Apple ID**:
| Фоновое аудио | Включаете фоновое чтение | TTS в фоне |

Мы **не** запрашиваем контакты, точное местоположение, камеру, микрофон (кроме системного воспроизведения TTS) или отслеживание.

## Конфиденциальность детей

iThousand — образовательное приложение, **не** Kids Category. Без сбора данных детей.

## Третьи стороны

Третьи стороны — только **Apple** (…системный перевод, Spotlight).

## Сроки хранения и удаление данных

- **На устройстве:** можно очистить прогресс, историю, заметки. Удаление app — sandbox/App Group.
- **iCloud:** отключите синхронизацию в Настройках; управляйте хранилищем iCloud в системных настройках.
- **Не храним копии** чтения, заметок и закладок иероглифов.

## Изменения в этой Политике

Мы можем обновлять эту страницу по юридическим причинам, из‑за продукта или требований App Store. Дата «Последнего обновления» изменится. Продолжение использования после обновления означает принятие пересмотренной политики.

## Контакт

Вопросы о конфиденциальности: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="th" markdown="1">

**อัปเดตล่าสุด:** 18 สิงหาคม 2026

iHTC Studio ("เรา") พัฒนา **iThousand** ("爱千字文" / "爱千字文", Bundle ID `com.iHTCboy.iThousand`) นโยบายความเป็นส่วนตัวนี้อธิบายว่าข้อมูลใดถูกจัดการและไม่ถูกจัดการเมื่อคุณใช้แอป **Apple App Review** และผู้ใช้สามารถใช้**หน้านี้**เป็นนโยบายความเป็นส่วนตัวสาธารณะ สำหรับ App Store Connect ให้เปิดนโยบายนี้ในเบราว์เซอร์แล้วคัดลอก URL จากแถบที่อยู่ (โดเมนสาธารณะอาจเปลี่ยนได้)

## สรุป (การจัดตำแหน่งกับ Nutrition Label ความเป็นส่วนตัวของ Apple)

| หัวข้อ | การปฏิบัติของเรา |
|-------|----------------|
| บัญชี | **ไม่จำเป็น** — ไม่ต้องลงทะเบียน ลงชื่อเข้าใช้ด้วยอีเมล หรือหมายเลขโทรศัพท์ |
| การเก็บข้อมูลโดย iHTC Studio | **ไม่เก็บข้อมูล** — เรา **ไม่ได้**ดำเนินการแบ็กเอนด์ที่รับข้อมูลส่วนตัวของคุณ |
| เครือข่าย | คลังข้อมูล character cards, reading, recite, Primer Hall, Hunt, widgets, and daily notifications work **offline** after install ทำงาน **แบบออฟไลน์** หลังติดตั้ง |
| การวิเคราะห์ / โฆษณา / การติดตาม | **ไม่มี** — ไม่มี SDK การวิเคราะห์ โฆษณา หรือการติดตามจากบุคคลที่สาม; ไม่ใช้ App Tracking Transparency |
| บริการ Apple เสริม | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default), optional **system speech / translation** |

## การเก็บข้อมูล

เราจะ **ไม่**เก็บ ขาย หรือแชร์ข้อมูลส่วนบุคคลเพื่อโฆษณาหรือการวิเคราะห์

- **ไม่ต้องมีบัญชีผู้ใช้** — คุณสามารถใช้คุณสมบัติหลักทั้งหมดได้โดยไม่ต้องสร้างบัญชีกับเรา
- **ไม่มีการวิเคราะห์หรือโฆษณา** — ไฟล์แอปไม่ได้รวม SDK การวิเคราะห์ การโฆษณา หรือการรายงานข้อผิดพลาดจากบุคคลที่สามที่ติดต่อกลับไปยังเรา
- **ไม่อัปโหลดเนื้อหา** — reading history, favorites, lists (千单), saved characters, notes, study progress, streaks, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**. ของคุณ

## วิธีการทำงานของแอป

- **ไลบรารีในชุดแอป** — JSON ข้อความ vernacular/English ดัชนี และตัวช่วยเรียนอยู่ในชุดแอป/วิดเจ็ต การเรียกดูและเรียนไม่ต้องใช้เครือข่าย
- **คำพูดบนอุปกรณ์** — การบรรยายใช้ระบบของ Apple **AVSpeechSynthesizer** (TTS) เราไม่ส่งข้อความข้อความไปที่ iHTC Studio
- **การแปลระบบ** — ฟีเจอร์แปลของ Apple บน OS
- **วิดเจ็ตและ App Group** — วิดเจ็ตและแอปใช้การตั้งค่าและสถานะขนาดเล็กร่วมกันผ่าน App Group `group.com.iHTCboy.iThousand` บนอุปกรณ์ของคุณ
- **การแจ้งเตือนรายวัน** — กำหนดเวลาภายในเครื่องด้วยการแจ้งเตือนผู้ใช้ การแตะการแจ้งเตือนจะเปิดลิงก์ในรายละเอียดไปยังรหัสข้อความบนอุปกรณ์ ไม่มีการปิดเซิร์ฟเวอร์
- **แชร์การ์ด** — รูปภาพถูกเรนเดอร์บนอุปกรณ์ การบันทึกจะใช้ **เฉพาะส่วนเสริมคลังรูปภาพ** เฉพาะเมื่อคุณแตะบันทึก เอกสารการแชร์ระบบอาจส่งรูปภาพไปยังแอป **คุณ** เลือก; นโยบายความเป็นส่วนตัวของปลายทางนั้นจึงจะมีผลใช้บังคับ
- **ทิปเสริม** — “Tip Developer” (`com.iHTCboy.iThousand.6`) **StoreKit** โดย Apple
- **Siri / ทางลัด / ศูนย์ควบคุม** — การรวมระบบที่เป็นตัวเลือกจะเปิดลิงก์ในรายละเอียดบนอุปกรณ์ พวกเขาไม่ได้ส่งห้องสมุดของคุณมาให้เรา
- **Spotlight เสริม** — ปิดตั้งต้น ข้อความและการ์ดถูกจัดทำดัชนีบนเครื่อง ไม่มีแบ็กเอนด์ค้นหา
- **อีเมลความคิดเห็น** — อาจมีข้อความของคุณและการวินิจฉัยอุปกรณ์/แอป (เวอร์ชัน OS ภาษา) เพื่อแก้ปัญหา

## ข้อมูลที่เก็บบนอุปกรณ์

| ข้อมูล | ที่ไหน | วัตถุประสงค์ |
|------|-------|---------|
| ฐานข้อความและตัวอักษร | App / Widget bundle | อ่าน การ์ดอักษร เรียน |
| รายการโปรดและรายการ (千单) | UserDefaults ของ App Group | ข้อความที่ติดดาวและรายการผู้ใช้ |
| ตัวอักษรที่บันทึกและบรรทัดโปรด | UserDefaults ของ App Group | ที่คั่นตัวยาก·บรรทัดติดดาว |
| ประวัติการอ่าน / อ่านครั้งล่าสุด | ค่าเริ่มต้นของกลุ่มแอป | อ่านต่อ ประวัติ UI |
| ความคืบหน้าและความเชี่ยวชาญ | UserDefaults ของ App Group | Primer Hall state, quiz / Hunt progress |
| บันทึก | UserDefaults ของ App Group | บันทึกข้อความ |
| สตรีคเรียน / เช็คอין | UserDefaults ของ App Group | นิสัยรายวัน |
| การตั้งค่าการ์ดแชร์ | UserDefaults ของ App Group | สไตล์ / อัตราส่วนที่เลือกล่าสุด |
| การตั้งค่าแคชและการแจ้งเตือน Daily Line | ค่าเริ่มต้นของกลุ่มแอป | ID ของวันนี้ กำหนดเวลา การสลับตามบริบท |
| การตั้งค่าการ์ดแชร์ | ค่าเริ่มต้นของกลุ่มแอป | ตัวเลือกสไตล์ / อัตราส่วนสุดท้าย |
| การเริ่มต้นใช้งานและสถานะ TipKit | Standard UserDefaults (อุปกรณ์) | คู่มือต้อนรับ / เคล็ดลับการค้นพบ |
| การดำเนินการด่วนบนหน้าจอหลัก | ระบบ + การตั้งค่าท้องถิ่น | ทางลัดที่คุณกำหนดค่า |
| วิดเจ็ต / ภาพรวมกิจกรรมสด | กลุ่มแอป / ActivityKit | แสดงข้อความที่คุณเปิดแล้ว |

การถอนการติดตั้งแอปจะลบข้อมูล sandbox และ App Group ที่เกี่ยวข้องกับแอป (ขึ้นอยู่กับพฤติกรรมของ iOS/macOS) สำเนา iCloud แบบเลือกได้จะยังคงอยู่ใน **iCloud ของคุณ** จนกว่าคุณจะลบหรือปิดการซิงค์และลบจากที่อื่น

## การซิงค์ iCloud (ตัวเลือก)

หากคุณเปิดใช้งาน **การซิงค์ iCloud** ในการตั้งค่า แอปจะสะท้อนข้อมูลผู้ใช้ที่เลือกผ่าน **`NSUbiquitousKeyValueStore`** ของ Apple ที่เชื่อมโยงกับ **Apple ID ของคุณ**:

- รายการโปรด
- รายการ (千单)
- ตัวอักษรที่บันทึก / บรรทัดโปรด
- ประวัติการอ่าน
- ความคืบหน้า/ความชำนาญในการศึกษา
- สตรีคการเรียน
- หมายเหตุ

การจราจรการซิงค์จะไปยัง **Apple iCloud** ไม่ใช่ iHTC Studio คุณสามารถปิดการซิงค์ได้ใน การตั้งค่า เราไม่สามารถอ่านเนื้อหา iCloud ของคุณได้

## สิทธิ์

iLiezi ร้องขอการอนุญาตเฉพาะเมื่อคุณสมบัติต้องการ:

| สิทธิ์ | เมื่อไหร่ | ทำไม |
|------------|------|-----|
| การแจ้งเตือน | คุณเปิด Daily Line reminders | กำหนดเวลาในเครื่อง |
| คลังรูปภาพ (เพิ่มอย่างเดียว) | บันทึกการ์ดแชร์/ตัวอักษร | Write the rendered image |
| iCloud | เปิดซิงค์ | ซิงค์รายการโปรด/รายการ/ประวัติ/ความคืบหน้า/สตรีค/บันทึก/ตัวอักษรที่บันทึก |
หากคุณเปิด **การซิงค์ iCloud** ในการตั้งค่า แอปจะทำสำเนาข้อมูลผู้ใช้บางส่วนผ่าน **`NSUbiquitousKeyValueStore`** ของ Apple ที่ผูกกับ **Apple ID ของคุณ**:
| เสียงพื้นหลัง | เปิดท่องพื้นหลัง | TTS พื้นหลัง |

เราไม่ **ไม่** ขอข้อมูลผู้ติดต่อ ตำแหน่งที่แน่นอน กล้อง ไมโครโฟน (นอกเหนือจากการเล่น TTS ของระบบ) หรือการติดตาม

## ความเป็นส่วนตัวของเด็ก

iThousand แอป识读ทั่วไป **ไม่ใช่** Kids Category

## บุคคลที่สาม

บุคคลที่สามคือ **Apple** (…แปลระบบ Spotlight)

## การเก็บรักษาและการลบข้อมูล

- **บนอุปกรณ์:** ล้างความคืบหน้า/ประวัติ/บันทึกในแอป ลบแอปเพื่อลบ sandbox/App Group
- **iCloud:** ปิดซิงค์ในการตั้งค่า จัดการพื้นที่ iCloud ในการตั้งค่าระบบ
- **ไม่เก็บสำเนา** การอ่าน/บันทึก/ที่คั่นตัวอักษร

## การเปลี่ยนแปลงนโยบายนี้

เราอาจปรับปรุงหน้านี้ด้วยเหตุผลทางกฎหมาย ผลิตภัณฑ์ หรือการปฏิบัติตาม App Store วันที่ 「อัปเดตล่าสุด」 จะเปลี่ยน การใช้งานต่อหลังอัปเดตถือว่าคุณยอมรับนโยบายที่แก้ไข

## ติดต่อ

คำถามเกี่ยวกับความเป็นส่วนตัว: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="de" markdown="1">

**Zuletzt aktualisiert:** 18. August 2026

iHTC Studio („wir“) hat **iThousand** („爱千字文“ / „爱千字文“, Bundle-ID `com.iHTCboy.iThousand`) entwickelt. Diese Datenschutzerklärung erläutert, welche Daten bei der Nutzung verarbeitet werden (und welche nicht). **Apple App Review** und Nutzer können sich auf **diese Seite** als öffentliche Datenschutzerklärung stützen. Für App Store Connect öffnen Sie diese Seite im Browser und kopieren Sie die URL aus der Adressleiste (die Domain kann sich ändern).

## Zusammenfassung (Übereinstimmung mit dem Apple-Datenschutzetikett)

| Thema | Unsere Praxis |
|-------|----------------|
| Konto | **Nicht erforderlich** — keine Registrierung, kein E-Mail-Login oder Telefonnummer erforderlich |
| Datenerhebung durch iHTC Studio | **Keine Datenerhebung** — wir betreiben **keinen** Backend-Service, der Ihre persönlichen Daten empfängt |
| Netzwerk | Bibliothek, character cards, reading, recite, Primer Hall, Hunt, widgets, and daily notifications work **offline** after install funktionieren nach der Installation **offline** |
| Analysen / Werbung / Tracking | **Keine** — keine Analysen von Drittanbietern, Werbung oder Tracking-SDKs; keine Nutzung von App Tracking Transparency |
| Optionale Apple-Dienste | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for optionales Trinkgeld, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default), optional **system speech / translation** |

## Datenerfassung

Wir erheben, verkaufen oder teilen **keine** persönlichen Informationen für Werbung oder Analysen.

- **Kein Konto** — Sie können alle Kernfunktionen nutzen, ohne ein Konto bei uns zu erstellen.
- **Keine Analysen oder Werbung** — Die App-Binärdatei integriert keine Analysen, Werbung oder Crash-Reporting-SDKs von Drittanbietern, die Daten an uns senden.
- **Kein Hochladen von Inhalten** — Ihre reading history, favorites, lists (千单), saved characters, notes, study progress, streaks, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## So funktioniert die App

- **Mitgelieferte Bibliothek** — Text-JSON, Umgangssprache/Englisch, Indizes und Lernhilfen liegen im App-/Widget-Bundle. Durchsuchen und Lernen erfordern kein Netzwerk.
- **Sprache auf dem Gerät** – Die Rezitation nutzt Apples System **AVSpeechSynthesizer** (TTS). Wir senden keine Passagentexte an iHTC Studio.
- **Systemübersetzung** — Apple-Funktionen auf dem Gerät; Apple OS.
- **Widgets und App Group** — Widgets und App teilen Einstellungen und leichten Zustand über die App Group `group.com.iHTCboy.iThousand` auf Ihrem Gerät.
- **Tägliche Benachrichtigungen** – Lokal geplant mit Benutzerbenachrichtigungen. Durch Tippen auf eine Benachrichtigung wird ein Deep-Link zu einer Durchgangs-ID auf dem Gerät geöffnet. Kein Server-Fanout.
- **Karten teilen** – Bilder werden auf dem Gerät gerendert. Beim Speichern wird **nur die Add-On-Fotobibliothek** verwendet, wenn Sie auf „Speichern“ tippen. Das System Share Sheet sendet das Bild möglicherweise an eine von Ihnen ausgewählte App. Es gelten dann die Datenschutzbestimmungen dieses Reiseziels.
- **Optionaler Tipp** — „Tip Developer“ (`com.iHTCboy.iThousand.6`), **StoreKit** via Apple.
- **Siri / Verknüpfungen / Kontrollzentrum** – Optionale Systemintegrationen öffnen Deep Links auf dem Gerät; Sie senden Ihre Bibliothek nicht an uns.
- **Optionales Spotlight** — standardmäßig aus. Passagen/Karten werden auf dem Gerät indiziert; kein Such-Backend.
- **Feedback-E-Mail** — kann Ihren Text und Geräte-/App-Diagnose (Version, OS, Sprache) nur zur Fehlerbehebung enthalten.

## Auf Ihrem Gerät gespeicherte Daten

| Daten | Wo | Zweck |
|------|-------|---------|
| Passagen- & Zeichendatenbank | App-/Widget-Bundle | Offline, Literacy-Karten |
| Favoriten und Listen (千单) | UserDefaults der App Group | Markierte Abschnitte und Nutzerlisten |
| Gespeicherte Zeichen & Zeilen | UserDefaults der App Group | Schwierige Zeichen, markierte Zeilen |
| Leseverlauf / zuletzt gelesen | Benutzerstandards der App-Gruppe | Lesen Sie weiter, Verlauf der Benutzeroberfläche |
| Lernfortschritt und Beherrschung | UserDefaults der App Group | Primer Hall state, quiz / Hunt progress |
| Notizen | UserDefaults der App Group | Passagen-Notizen |
| Lernserie / Check-in | UserDefaults der App Group | Tägliche Gewohnheit |
| Einstellungen der Teilen-Karten | UserDefaults der App Group | Zuletzt gewählter Stil / zuletzt gewähltes Seitenverhältnis |
| Daily Line-Cache- und Benachrichtigungseinstellungen | Benutzerstandards der App-Gruppe | Heutige ID, Zeitplanzeit, kontextbezogenes Umschalten |
| Share-Card-Einstellungen | Benutzerstandards der App-Gruppe | Letzte Stil-/Verhältnisauswahl |
| Onboarding- und TipKit-Status | Standard UserDefaults (Gerät) | Willkommensführer / Entdeckungstipps |
| Schnellaktionen auf dem Startbildschirm | System + lokale Einstellungen | Von Ihnen konfigurierte Verknüpfungen |
| Widget-/Live-Aktivitäts-Schnappschüsse | App-Gruppe / ActivityKit | Text anzeigen, den Sie bereits geöffnet haben |

Die Deinstallation der App entfernt Sandbox- und App-Gruppendaten, die mit der App verbunden sind (abhängig vom Verhalten von iOS/macOS). Optionale iCloud-Kopien bleiben in **deiner** iCloud, bis du sie löschst oder die Synchronisierung ausschaltest und anderswo löschst.

## iCloud-Synchronisierung (optional)

Wenn du **iCloud-Synchronisierung** in den Einstellungen aktivierst, spiegelt die App ausgewählte Benutzerdaten über Apples **`NSUbiquitousKeyValueStore`**, die mit **deiner Apple-ID** verknüpft ist:

- Favoriten
- Listen (千单)
- Gespeicherte Zeichen / Lieblingszeilen
- Leseverlauf
- Lernfortschritt / Kenntnisse
- Lernserien
- Notizen

Der Synchronisationsverkehr geht an **Apple iCloud**, nicht an iHTC Studio. Du kannst die Synchronisierung in den Einstellungen deaktivieren. Wir können deine iCloud-Inhalte nicht lesen.

## Berechtigungen

iLiezi fordert Berechtigungen nur an, wenn eine Funktion diese benötigt:

| Erlaubnis | Wann | Warum |
|------------|------|-----|
| Benachrichtigungen | Sie aktivieren Daily Line reminders | Lokale Planung |
| Fotomediathek (nur Hinzufügen) | Share-Karte/Zeichenbild | Write the rendered image |
| iCloud | Sync aktivieren | Favoriten/Listen/Verlauf/Fortschritt/Serien/Notizen/gespeicherte Zeichen |
| Live-Aktivitäten (iOS) | Sie aktivieren Lese-Live-Aktivität | Sperrbildschirm / Dynamic Island |
| Hintergrundaudio | Hintergrundrezitation aktivieren | TTS im Hintergrund |

Wir fordern **keine** Kontakte, den genauen Standort, die Kamera, das Mikrofon (über die System-TTS-Wiedergabe hinaus) oder die Nachverfolgung an.

## Privatsphäre von Kindern

iThousand — Bildungs-App, **nicht** Kids Category.

## Dritte Parteien

Drittanbieter: **Apple** (…Systemübersetzung, Spotlight).

## Datenaufbewahrung & Löschung

- **Auf dem Gerät:** Fortschritt/Verlauf/Notizen löschen. App löschen entfernt Sandbox/App Group.
- **iCloud:** Sync in Einstellungen deaktivieren; iCloud-Speicher in Systemeinstellungen verwalten.
- **Keine Kopien** von Lesen, Notizen, Zeichen-Lesezeichen.

## Änderungen an dieser Richtlinie

Wir können diese Seite aus rechtlichen Gründen, produktbedingt oder wegen App-Store-Compliance aktualisieren. Das Datum „Zuletzt aktualisiert“ ändert sich. Fortgesetzte Nutzung nach einer Aktualisierung gilt als Zustimmung zur überarbeiteten Richtlinie.

## Kontakt

Fragen zum Datenschutz: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="fr" markdown="1">

**Dernière mise à jour :** 18 août 2026

iHTC Studio (« nous ») a développé **iThousand** (« 爱千字文 » / « 爱千字文 », Bundle ID `com.iHTCboy.iThousand`). Cette politique de confidentialité explique quelles données sont (ou ne sont pas) traitées lorsque vous utilisez l’app. **Apple App Review** et les utilisateurs peuvent s’appuyer sur **cette page** comme politique publique. Pour App Store Connect, ouvrez cette page dans le navigateur et copiez l’URL depuis la barre d’adresse (le domaine public peut changer).

## Résumé (alignement sur l'étiquette nutritionnelle de confidentialité Apple)

| Sujet | Notre pratique |
|-------|----------------|
| Compte | **Non requis** — pas d'inscription, de connexion par e-mail ou de numéro de téléphone |
| Collecte de données par iHTC Studio | **Données non collectées** — nous n'exploitons **pas** de backend qui reçoit vos données personnelles |
| Réseau | Bibliothèque, character cards, reading, recite, Primer Hall, Hunt, widgets, and daily notifications work **offline** after install fonctionnent **hors ligne** après l’installation |
| Analyses / publicités / suivi | **Aucun** — pas de SDK tiers d'analyse, de publicité ou de suivi ; pas d'utilisation de la transparence du suivi des applications |
| Services Apple facultatifs | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for pourboire facultatif, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default), optional **system speech / translation** |

## Collecte de données

Nous ne collectons, vendons ou partageons **pas** d'informations personnelles à des fins publicitaires ou analytiques.

- **Aucun compte** — Vous pouvez utiliser toutes les fonctionnalités principales sans créer de compte chez nous.
- **Aucune analyse ni publicité** — Le binaire de l'application n'intègre pas de SDK tiers d'analyse, de publicité ou de rapport d'erreur qui nous contactent.
- **Aucun envoi de contenu** — Vos reading history, favorites, lists (千单), saved characters, notes, study progress, streaks, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## Comment fonctionne l'application

- **Bibliothèque incluse** — JSON texte, vernaculaire/anglais, index et aides d’étude sont dans le bundle app/widget. Parcourir et étudier ne nécessite pas le réseau.
- **Discours sur l'appareil** — La récitation utilise le système **AVSpeechSynthesizer** (TTS) d'Apple. Nous n'envoyons pas de texte de passage à iHTC Studio.
- **Traduction système** — fonctions Apple ; OS Apple.
- **Widgets et App Group** — Les widgets et l’app partagent des préférences et un état léger via l’App Group `group.com.iHTCboy.iThousand` sur votre appareil.
- **Notifications quotidiennes** — Planifiées localement avec les notifications utilisateur. Appuyer sur une notification ouvre un lien profond vers un identifiant de passage sur l'appareil ; pas de distribution du serveur.
- **Partager des cartes** : les images sont rendues sur l'appareil. L'enregistrement utilise **le module complémentaire Photothèque** uniquement lorsque vous appuyez sur Enregistrer. System Share Sheet peut envoyer l'image à une application **que** vous choisissez ; la politique de confidentialité de cette destination s’applique alors.
- **Pourboire facultatif** — « Tip Developer » (`com.iHTCboy.iThousand.6`), **StoreKit** via Apple.
- **Siri / Raccourcis / Centre de contrôle** — Les intégrations système facultatives ouvrent des liens profonds sur l'appareil ; ils ne nous envoient pas votre bibliothèque.
- **Spotlight facultatif** — désactivé par défaut. Passages et cartes indexés sur l’appareil ; pas de backend de recherche.
- **Email de commentaires** — peut inclure votre texte et des diagnostics appareil/app (version, OS, langue) pour le dépannage.

## Données stockées sur votre appareil

| Données | Où | Objectif |
|------|-------|--------------|
| Base passages et caractères | Bundle App / Widget | Lecture, cartes d’alphabétisation |
| Favoris et listes (千单) | UserDefaults de l’App Group | Passages favoris et listes utilisateur |
| Caractères et lignes favorites | UserDefaults de l’App Group | Caractères difficiles, lignes favorites |
| Historique de lecture / dernière lecture | Paramètres par défaut du groupe d'applications | Continuer la lecture, historique de l'interface utilisateur |
| Progression d’étude et maîtrise | UserDefaults de l’App Group | Primer Hall state, quiz / Hunt progress |
| Notes | UserDefaults de l’App Group | Notes de passages |
| Série d’étude / check-in | UserDefaults de l’App Group | Habitude quotidienne |
| Préférences des cartes de partage | UserDefaults de l'App Group | Derniers choix de style / de format |
| Préférences de cache et de notification de la ligne quotidienne | Paramètres par défaut du groupe d'applications | ID du jour, heure de programmation, bascule contextuelle |
| Préférences de carte partagée | Paramètres par défaut du groupe d'applications | Derniers choix de style/ratio |
| État d’intégration et de TipKit | Paramètres utilisateur standard (appareil) | Guide d'accueil / conseils découverte |
| Actions rapides sur l'écran d'accueil | Système + préférences locales | Raccourcis que vous configurez |
| Widget / Instantanés d'activité en direct | Groupe d'applications / ActivityKit | Afficher le texte que vous avez déjà ouvert |

La désinstallation de l'application supprime les données du bac à sable et du groupe d'applications associées à l'application (selon le comportement d'iOS/macOS). Les copies facultatives dans iCloud restent dans **votre** iCloud jusqu'à ce que vous les supprimiez ou que vous désactiviez la synchronisation et supprimiez ailleurs.

## Synchronisation iCloud (Facultative)

Si vous activez **la synchronisation iCloud** dans les Réglages, l'application reflète les données utilisateur sélectionnées via le **`NSUbiquitousKeyValueStore`** d'Apple lié à **votre identifiant Apple** :

- Favoris
- Listes (千单)
- Caractères enregistrés / passages favoris
- Historique de lecture
- Progression / maîtrise des études
- Séries d’étude
- Remarques

Le trafic de synchronisation passe par **Apple iCloud**, et non par iHTC Studio. Vous pouvez désactiver la synchronisation dans les Réglages. Nous ne pouvons pas lire le contenu de votre iCloud.

## Autorisations

iLiezi demande des autorisations uniquement lorsqu'une fonctionnalité en a besoin :

| Autorisation | Quand | Pourquoi |
|------------|------|-----|
| Notifications | Vous activez Daily Line reminders | Planification locale |
| Photothèque (ajout uniquement) | Carte partagée/caractère | Write the rendered image |
| iCloud | Activez la sync | Favoris/listes/historique/progression/séries/notes/caractères enregistrés |
Si vous activez la **synchronisation iCloud** dans les Réglages, l'app reflète certaines données utilisateur via **`NSUbiquitousKeyValueStore`** d'Apple, lié à **votre identifiant Apple** :
| Audio de fond | Récitation en arrière-plan | TTS en arrière-plan |

Nous ne demandons **pas** de contacts, de localisation précise, de caméra, de microphone (au-delà de la lecture TTS du système) ou de suivi.

## Confidentialité des enfants

iThousand — app éducative, **pas** Kids Category.

## Tiers

Tiers : **Apple** (…traduction système, Spotlight).

## Conservation et suppression des données

- **Sur l’appareil :** effacer progression/historique/notes. Supprimer l’app efface sandbox/App Group.
- **iCloud :** désactivez la sync dans Réglages ; gérez le stockage iCloud dans Réglages système.
- **Pas de copies** de lecture, notes, signets de caractères.

## Modifications de cette politique

Nous pouvons mettre à jour cette page pour des raisons juridiques, produit ou conformité App Store. La date « Dernière mise à jour » changera. L’utilisation continue après une mise à jour vaut acceptation de la politique révisée.

## Nous contacter

Questions sur la vie privée : [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="tr" markdown="1">

**Son güncelleme:** 18 Ağustos 2026

iHTC Studio ("biz"), **iThousand** ("爱千字文" / "爱千字文", Bundle ID `com.iHTCboy.iThousand`) uygulamasını geliştirdi. Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlendiğini (ve işlenmediğini) açıklar. **Apple App Review** ve kullanıcılar **bu sayfayı** herkese açık gizlilik politikası olarak kullanabilir. App Store Connect için tarayıcıda bu sayfayı açın ve adres çubuğundan URL’yi kopyalayın (genel site alan adı zamanla değişebilir).

## Özet (Apple Gizlilik Beslenme Etiketi uyumu)

| Konu | Uygulamamızın uygulaması |
|-------|----------------|
| Hesap | **Gerekli değil** — kayıt, e-posta ile giriş veya telefon numarası yok |
| iHTC Studio tarafından veri toplama | **Veri Toplanmıyor** — kişisel verilerinizi alan bir arka uç işletmiyoruz |
| Ağ | Kütüphane, character cards, reading, recite, Primer Hall, Hunt, widgets, and daily notifications work **offline** after install kurulumdan sonra **çevrimdışı** çalışır |
| Analitik / reklam / izleme | **Yok** — üçüncü taraf analitik, reklam veya izleme SDK'ları yok; Uygulama İzleme Şeffaflığı kullanılmaz |
| İsteğe bağlı Apple hizmetleri | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default), optional **system speech / translation** |

## Veri Toplama

Kişisel bilgileri reklam veya analiz için **toplamıyoruz**, satmıyoruz veya paylaşmıyoruz.

- **Hesap gerekmez** — Tüm temel özellikleri bizde hesap oluşturmadan kullanabilirsiniz.
- **Analitik veya reklam yok** — Uygulama ikili dosyası üçüncü taraf analitik, reklam veya çökme bildirim SDK'larını içermez, telefonla bize veri göndermez.
- **İçerik yüklenmez** — reading history, favorites, lists (千单), saved characters, notes, study progress, streaks, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## Uygulama Nasıl Çalışır

- **Paketlenmiş kitaplık** — Metin JSON, vernacular/English, dizinler ve çalışma yardımcıları uygulama/widget paketinin içindedir. Gezinme ve çalışma için ağ gerekmez.
- **Cihaz içi konuşma** — Okuma, Apple'ın **AVSpeechSynthesizer** (TTS) sistemini kullanır. iHTC Studio'ya pasaj metni göndermiyoruz.
- **Sistem çevirisi** — Apple cihaz/sistem çevirisi; Apple OS.
- **Widget'lar ve App Group** — Widget'lar ve uygulama, cihazınızdaki `group.com.iHTCboy.iThousand` App Group'u üzerinden tercihleri ve hafif durumu paylaşır.
- **Günlük bildirimler** — Kullanıcı Bildirimleriyle yerel olarak planlanır. Bir bildirime dokunulduğunda cihazdaki pasaj kimliğine giden derin bağlantı açılır; sunucu çıkışı yok.
- **Kartları paylaş** — Görüntüler cihazda oluşturulur. Kaydetme, **Yalnızca Fotoğraf Kitaplığı eklentisini** yalnızca kaydet'e dokunduğunuzda kullanır. Sistem Paylaşım Sayfası, görüntüyü **seçtiğiniz** bir uygulamaya gönderebilir; o hedefin gizlilik politikası geçerli olur.
- **İsteğe bağlı bahşiş** — “Tip Developer” (`com.iHTCboy.iThousand.6`), Apple **StoreKit**.
- **Siri / Kısayollar / Kontrol Merkezi** — İsteğe bağlı sistem entegrasyonları cihazdaki derin bağlantıları açar; kütüphanenizi bize göndermiyorlar.
- **İsteğe bağlı Spotlight** — varsayılan kapalı. Pasajlar/kartlar cihazda dizinlenir; arama arka ucu yok.
- **Geri bildirim e-postası** — yalnızca sorun giderme için yazdığınız metin ve cihaz/uygulama tanılaması (sürüm, OS, dil) içerebilir.

## Cihazınızda Saklanan Veriler

| Veri | Nerede | Amaç |
|------|-------|-------------|
| Pasaj ve karakter veritabanı | App / Widget paketi | Çevrimdışı, okuryazarlık kartları |
| Favoriler ve listeler (千单) | App Group UserDefaults | Yıldızlı pasajlar ve kullanıcı listeleri |
| Kayıtlı karakterler ve dizeler | App Group UserDefaults | Zor karakterler, yıldızlı satırlar |
| Okuma geçmişi / son okuma | Uygulama Grubu Kullanıcı Varsayılanları | Okumaya devam et, geçmiş kullanıcı arayüzü |
| Çalışma ilerlemesi ve ustalık | App Group UserDefaults | Primer Hall state, quiz / Hunt progress |
| Notlar | App Group UserDefaults | Pasaj notları |
| Çalışma serisi / check-in | App Group UserDefaults | Günlük alışkanlık |
| Paylaşım kartı tercihleri | App Group UserDefaults | Son stil / oran seçimleri |
| Daily Line önbelleği ve bildirim tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Bugünün kimliği, program zamanı, bağlamsal geçiş |
| Paylaşımlı kart tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Son stil/oran seçenekleri |
| İlk katılım ve TipKit durumu | Standart Kullanıcı Varsayılanları (cihaz) | Hoş geldiniz kılavuzu / keşif ipuçları |
| Ana Ekran hızlı eylemler | Sistem + yerel tercihler | Yapılandırdığınız kısayollar |
| Widget / Canlı Etkinlik anlık görüntüleri | Uygulama Grubu / ActivityKit | Daha önce açmış olduğunuz metni görüntüleyin |

Uygulamayı kaldırmak, uygulamayla ilişkili sandbox ve Uygulama Grubu verilerini kaldırır (iOS/macOS davranışına tabidir). İsteğe bağlı iCloud kopyaları, siz temizleyene veya senkronizasyonu kapatıp başka yerde silene kadar **iCloud’unuzda** kalır.

## iCloud Senkronizasyonu (İsteğe Bağlı)

Eğer Ayarlar’dan **iCloud Senkronizasyonu**’nu etkinleştirirseniz, uygulama seçili kullanıcı verilerini Apple’ın **`NSUbiquitousKeyValueStore`** aracılığıyla **Apple Kimliğinizle** eşler:

- Favoriler
- Listeler (千单)
- Kayıtlı karakterler / favori dizeler
- Okuma geçmişi
- Çalışma ilerlemesi / ustalık
- Çalışma serileri
- Notlar

Senkronizasyon trafiği **Apple iCloud**’a gider, iHTC Studio’ya değil. Ayarlardan senkronizasyonu devre dışı bırakabilirsiniz. iCloud içeriğinizi okuyamayız.

## İzinler

iLiezi yalnızca bir özellik ihtiyaç duyduğunda izin ister:

| İzin | Ne zaman | neden |
|------------|------|-----|
| Bildirimler | Daily Line reminders etkinleştirirsiniz | Yerel zamanlama |
| Fotoğraf Kitaplığı (yalnızca ekleme) | Paylaşım kartı/karakter | Write the rendered image |
| iCloud | Senkronizasyonu açarsınız | Favoriler/listeler/geçmiş/ilerleme/seriler/notlar/kayıtlı karakterler |
Ayarlar'da **iCloud Senkronizasyonu**'nu etkinleştirirseniz, uygulama seçili kullanıcı verilerini **Apple Kimliğinize** bağlı Apple'ın **`NSUbiquitousKeyValueStore`** hizmeti aracılığıyla yansıtır:
| Arka plan sesi | Arka planda okuma | Arka planda TTS |

Kişiler, kesin Konum, Kamera, Mikrofon (sistem TTS oynatmanın ötesinde) veya İzleme **talebi etmeyiz**.

## Çocukların Gizliliği

iThousand — eğitim uygulaması, Kids Category **değil**.

## Üçüncü Taraflar

Üçüncü taraf: **Apple** (…sistem çevirisi, Spotlight).

## Veri Saklama ve Silme

- **Cihazda:** ilerleme/geçmiş/notları temizleyin. Uygulamayı silmek sandbox/App Group’u kaldırır.
- **iCloud:** Ayarlar’da senkronizasyonu kapatın; iCloud depolamayı sistem Ayarları’ndan yönetin.
- **Kopya yok** — okuma, notlar, karakter yer imleri.

## Bu Politika ile İlgili Değişiklikler

Yasal, ürün veya App Store uyumluluğu nedenleriyle bu sayfayı güncelleyebiliriz. 「Son güncelleme」 tarihi değişir. Güncellemeden sonra kullanıma devam etmek, revize edilmiş politikayı kabul ettiğiniz anlamına gelir.

## İletişim

Gizlilik ile ilgili sorular: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
