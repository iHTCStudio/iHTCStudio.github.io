---
layout: doc
title: iPrimer — Privacy Policy
app_id: iPrimer
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iPrimer (爱小学) — fully offline Xiaoxue growth app, Data Not Collected, optional iCloud and Photo Library add-only.
---

<section lang="en" markdown="1">

**Last updated:** August 18, 2026

iHTC Studio ("we", "us" or "our") built **iPrimer** (also known as "爱小学" / "愛小學", Bundle ID `com.iHTCboy.iPrimer`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on **this page** as the public privacy policy for the app. For App Store Connect, open this Privacy Policy in your browser and copy the address from the address bar (the public site domain may change over time).

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration, email sign-in, or phone number |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your personal data |
| Network | Library, reading, recite, Character Study, meditation, Life Guidance, widgets, and daily notifications work **offline** after install |
| Analytics / ads / tracking | **None** — no third-party analytics, advertising, or tracking SDKs; no App Tracking Transparency use |
| Optional Apple services | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities** |

## Data Collection

We do **not** collect, sell, or share personal information for advertising or analytics.

- **No account** — You can use all core features without creating an account with us.
- **No analytics or ads** — The app binary does not integrate third-party analytics, advertising, or crash-reporting SDKs that phone home to us.
- **No content upload** — Your reading history, favorites, study lists, reflection journal entries, habit check-ins, meditation streaks, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## How the App Works

- **Bundled library** — Chapter JSON, vernacular/English text, collected notes, glosses, meditation scripts, and indexes ship inside the app / widget bundle (curated from public web sources). Browsing and study do not require a network request.
- **On-device speech** — Recitation uses Apple’s system **AVSpeechSynthesizer** (TTS). We do not send chapter text to iHTC Studio.
- **Widgets & App Group** — Widgets and the app share preferences and lightweight state via App Group `group.com.iHTCboy.iPrimer` on your device.
- **Daily notifications** — Scheduled locally with User Notifications. Tapping a notification opens a deep link to a chapter ID on device; no server fan-out.
- **Share cards** — Images are rendered on device. Saving uses **Photo Library add-only** only when you tap save. System Share Sheet may send the image to an app **you** choose; that destination’s privacy policy then applies.
- **Optional tip** — “Tip Developer” (`com.iHTCboy.iPrimer.6`) is a consumable **StoreKit** purchase processed by Apple. We do not receive your payment card details.
- **Siri / Shortcuts / Control Center** — Optional system integrations open on-device deep links; they do not send your library to us.
- **Optional Spotlight** — If you enable indexing, content is indexed by the system on device for local search; we do not operate a search backend.

## Data Stored on Your Device

| Data | Where | Purpose |
|------|-------|---------|
| Chapter database | App / Widget bundle | Offline reading & study |
| Favorites & study lists | App Group UserDefaults | Starred works and user lists |
| Reading history / last read | App Group UserDefaults | Continue reading, history UI |
| Study progress & mastery | App Group UserDefaults | Character Study state, quiz / Hunt progress |
| Study streak / check-in | App Group UserDefaults | Daily Study habit |
| Reflection journal entries | App Group UserDefaults | Life Guidance journal |
| Habit check-ins (洒扫应对) | App Group UserDefaults | Life Guidance daily habits |
| Meditation streak & session prefs | App Group UserDefaults | Meditation continuity |
| Appearance & reading prefs | App Group UserDefaults | Theme, accent, language, layout, TTS, tabs, widgets, font scale |
| Daily Study cache & notification prefs | App Group UserDefaults | Today’s ID, schedule time, contextual toggle |
| Share-card preferences | App Group UserDefaults | Last style / ratio choices |
| Onboarding & TipKit state | Standard UserDefaults (device) | Welcome guide / discovery tips |
| Home Screen quick actions | System + local prefs | Shortcuts you configure |
| Widget / Live Activity snapshots | App Group / ActivityKit | Display text you already opened |

Uninstalling the app removes sandbox and App Group data associated with the app (subject to iOS/macOS behavior). Optional iCloud copies remain in **your** iCloud until you clear them or turn sync off and delete elsewhere.

## iCloud Sync (Optional)

If you enable **iCloud Sync** in Settings, the app mirrors selected user data through Apple’s **`NSUbiquitousKeyValueStore`** tied to **your Apple ID**:

- Favorites
- Study lists
- Reading history
- Study progress / mastery
- Study streaks
- Reflection journal entries
- Habit check-in history

Sync traffic goes to **Apple iCloud**, not to iHTC Studio. You can disable sync in Settings. We cannot read your iCloud contents.

## Permissions

iPrimer requests permissions only when a feature needs them:

| Permission | When | Why |
|------------|------|-----|
| Notifications | You enable Daily Study or meditation reminders | Local scheduling |
| Photo Library (Add Only) | You save a share card | Write the rendered image |
| iCloud | You enable sync | Sync favorites / lists / history / progress / streaks / journal / habits |
| Live Activities (iOS) | You enable Reading or Meditation Live Activity | Lock Screen / Dynamic Island |
| Background audio | You enable background recitation | Continue TTS in background |

We do **not** request Contacts, precise Location, Camera, Microphone (beyond system TTS playback), or Tracking.

## Children’s Privacy

iPrimer is rated **12+** and is **not** in the Kids Category. We do not knowingly collect personal information from children. The app does not require an account.

## Third Parties

The only third-party services involved in normal use are **Apple** (App Store, iCloud, StoreKit, system TTS, notifications, Live Activities).

## Data Retention & Deletion

- **On device:** Delete the app to remove local sandbox and App Group data (subject to system behavior).
- **iCloud:** Disable sync in Settings; you may also manage iCloud storage in system Settings.
- **We do not retain copies** of your reading, journal, or habit data on iHTC Studio servers.

## Changes to This Policy

We may update this page for legal, product, or App Store compliance reasons. The “Last updated” date will change. Continued use after an update means you accept the revised policy.

## Contact

Questions about privacy: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="zh-CN" markdown="1">

**最近更新：** 2026 年 8 月 18 日

爱火腿肠工作室（iHTC Studio）（「我们」）开发了 **爱小学**（iPrimer / 愛小學，Bundle ID `com.iHTCboy.iPrimer`）。本隐私政策说明你在使用本应用时，数据如何被处理。本页可作为 **App Store 审核**与用户查阅的公开隐私政策地址。在 App Store Connect 填写隐私政策 URL 时，请在浏览器中打开本 [隐私政策](../privacy) 页，从地址栏复制当前网址（公开站点域名日后可能变更）。

## 概要（对齐 App Store 隐私标签）

| 主题 | 我们的做法 |
|------|------------|
| 账号 | **不需要** — 无注册、邮箱登录或手机号 |
| 爱火腿肠工作室的数据收集 | **不收集数据** — 我们**不**运营接收你个人数据的后端 |
| 网络 | 安装后，语料、阅读、诵读、品格学堂、冥想、人生指导、小组件与每日通知可**离线** |
| 分析 / 广告 / 追踪 | **无** — 无第三方分析、广告或追踪 SDK；不使用 App 追踪透明度 |
| 可选 Apple 服务 | **iCloud**（你的私有 KVS）、分享卡的**相册（仅添加）**、**StoreKit** 打赏、**本地通知**、可选**实时活动** |

## 数据收集

我们**不**为广告或分析收集、出售或共享个人信息。

- **无账号** — 无需向我们注册即可使用全部核心功能。
- **无分析或广告** — 应用未集成会向我们家上报的第三方分析、广告或崩溃 SDK。
- **不上传内容** — 阅读记录、收藏、学单、反思日记、习惯打卡、冥想连续、学堂进度与偏好留在你的设备（以及可选的**你的** iCloud），不会上传到 iHTC Studio 服务器，因为**我们不为本应用运营此类服务器**。

## 应用如何工作

- **内置语料** — 篇章 JSON、白话/英文、集注、释义、冥想引导与索引随 App / 小组件安装（由网络公开资料梳理）。
- **本机朗读** — 使用系统 **AVSpeechSynthesizer**（TTS）；篇章正文不会发送给我们。
- **小组件与 App Group** — 通过 `group.com.iHTCboy.iPrimer` 在本机共享状态。
- **每日通知** — 仅本机调度；点击通过深链打开对应篇章 ID。
- **分享卡** — 本机渲染；仅在你点保存时使用**相册（仅添加）**。
- **可选打赏** — `com.iHTCboy.iPrimer.6` 消耗型内购由 **Apple StoreKit** 处理。
- **Siri / 快捷指令 / 控制中心** — 打开本机深链，不上传语料。
- **可选 Spotlight** — 在设置中开启后由系统本机索引；我们无搜索后端。

## 设备上存储的数据

| 数据 | 位置 | 用途 |
|------|------|------|
| 篇章语料库 | App / 小组件包 | 离线阅读与学堂 |
| 收藏与学单 | App Group UserDefaults | 星标与用户清单 |
| 阅读记录 / 上次阅读 | App Group UserDefaults | 继续阅读、历史界面 |
| 学堂进度与掌握度 | App Group UserDefaults | 品格学堂、测验/寻句 |
| 研习打卡连续 | App Group UserDefaults | 每日一学习惯 |
| 反思日记 | App Group UserDefaults | 人生指导日记 |
| 洒扫习惯打卡 | App Group UserDefaults | 人生指导微习惯 |
| 冥想连续与会话偏好 | App Group UserDefaults | 冥想统计 |
| 外观与阅读偏好 | App Group UserDefaults | 主题、强调色、语言、布局、TTS、Tab、小组件、字号 |
| 每日一学缓存与通知偏好 | App Group UserDefaults | 今日 ID、提醒时间 |
| 分享卡偏好 | App Group UserDefaults | 上次样式选择 |
| 引导与 TipKit 状态 | 标准 UserDefaults | 欢迎引导 |
| 主屏快捷操作 | 系统 + 本地偏好 | 你配置的快捷 |
| 小组件 / 实时活动快照 | App Group / ActivityKit | 你已打开内容的展示 |

卸载应用会移除与该应用关联的沙盒与 App Group 数据（以 iOS/macOS 行为为准）。可选 iCloud 副本留在**你的** iCloud 中，直至你关闭同步或在别处删除。

## iCloud 同步（可选）

在设置中开启 **iCloud 同步**后，应用通过 Apple **`NSUbiquitousKeyValueStore`**（绑定**你的 Apple ID**）镜像：

- 收藏
- 学单
- 阅读记录
- 学堂进度 / 掌握度
- 研习打卡连续
- 反思日记
- 习惯打卡历史

同步流量发往 **Apple iCloud**，而非 iHTC Studio。可在设置中关闭。我们无法读取你的 iCloud 内容。

## 权限

仅在功能需要时请求：

| 权限 | 何时 | 原因 |
|------|------|------|
| 通知 | 你开启每日一学或冥想提醒 | 本机调度 |
| 相册（仅添加） | 你保存分享卡 | 写入渲染图片 |
| iCloud | 你开启同步 | 同步收藏/学单/记录/进度/打卡/日记/习惯 |
| 实时活动（iOS） | 你开启品读或冥想实时活动 | 锁屏 / 灵动岛 |
| 后台音频 | 你开启后台诵读 | 后台继续 TTS |

我们**不**请求通讯录、精确位置、相机、麦克风（除系统 TTS 播放外）或追踪。

## 儿童隐私

本应用分级 **12+**，**非**儿童类别。我们不会有意收集儿童个人信息；应用无需账号。

## 第三方

正常使用中涉及的第三方仅为 **Apple**（App Store、iCloud、StoreKit、系统 TTS、通知、实时活动）。

## 保留与删除

- **本机：** 删除应用可移除本地数据。
- **iCloud：** 在设置中关闭同步，或在系统设置中管理 iCloud 存储。
- **我们不在服务器保留**你的阅读、日记或习惯数据副本。

## 政策变更

我们可能因法律、产品或 App Store 合规需要更新本页；「最近更新」日期会随之变更。继续使用即表示接受修订后的政策。

## 联系

隐私相关问题：[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="zh-TW" markdown="1">

**最近更新：** 2026 年 8 月 18 日

愛火腿腸工作室（iHTC Studio）（「我們」）開發了 **愛小學**（iPrimer，Bundle ID `com.iHTCboy.iPrimer`）。本隱私政策說明你在使用本應用時，資料如何被處理。本頁可作為 **App Store 審核**與使用者查閱的公開隱私政策地址。在 App Store Connect 填寫隱私政策 URL 時，請在瀏覽器中開啟本 [隱私政策](../privacy) 頁，從網址列複製目前網址（公開站點網域日後可能變更）。

## 概要（對齊 App Store 隱私標籤）

| 主題 | 我們的做法 |
|------|------------|
| 帳號 | **不需要** |
| 愛火腿腸工作室的資料收集 | **不收集資料** |
| 網路 | 安裝後，語料、閱讀、誦讀、品格學堂、冥想、人生指導、小工具與每日通知可**離線** |
| 分析 / 廣告 / 追蹤 | **無** |
| 可選 Apple 服務 | **iCloud**、分享卡的**照片（僅加入）**、**StoreKit** 打賞、**本地通知**、可選**即時動態** |

## 資料收集

我們**不**為廣告或分析收集、出售或共享個人資訊。閱讀記錄、收藏、學單、反思日記、習慣打卡、冥想連續、學堂進度與偏好留在你的裝置（以及可選的**你的** iCloud），不會上傳到 iHTC Studio 伺服器。

## 應用如何工作

- **內建語料** — 篇章 JSON、白話/英文、集注、釋義、冥想引導與索引隨 App / 小工具安裝（由網絡公開資料梳理）。
- **本機朗讀** — 使用系統 TTS。
- **小工具與 App Group** — `group.com.iHTCboy.iPrimer` 本機共享。
- **每日通知** — 僅本機排程。
- **分享卡** — 本機渲染；**照片（僅加入）**。
- **可選打賞** — `com.iHTCboy.iPrimer.6` 由 Apple 處理。

## 裝置上儲存的資料

含篇章語料、收藏與學單、閱讀記錄、學堂進度、研習打卡、反思日記、灑掃習慣打卡、冥想連續、外觀與閱讀偏好、每日一學快取、分享卡偏好、引導狀態、主屏快捷與小工具/即時活動快照（詳見英文版表格）。

## iCloud 同步（可選）

可同步：收藏、學單、閱讀記錄、學堂進度/掌握度、研習打卡、反思日記、習慣打卡歷史。流量走 **Apple iCloud**。

## 權限

通知、照片（僅加入）、iCloud、即時活動、背景音訊——僅在對應功能開啟時使用。不請求通訊錄、精確位置、相機、麥克風（除系統 TTS）或追蹤。

## 兒童隱私

分級 **12+**，**非**兒童類別；無需帳號。

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

iHTC Studio（「当社」）は **iPrimer**（「爱小学」／「爱小学」、Bundle ID `com.iHTCboy.iPrimer`）を開発しました。本プライバシーポリシーは、本アプリの利用時にどのデータが取り扱われ、取り扱われないかを説明します。**Apple App Review** とユーザーは、**本ページ**を公開のプライバシーポリシーとして参照できます。App Store Connect では、ブラウザで本プライバシーポリシーを開き、アドレスバーから URL をコピーしてください（公開サイトのドメインは将来変更される場合があります）。

## 概要（Apple プライバシー栄養表示との整合性）

| トピック | 当社の方針 |
|-------|----------------|
| アカウント | **不要** — 登録、メールサインイン、電話番号は必要ありません |
| iHTC Studioによるデータ収集 | **データは収集しません** — 個人データを受け取るバックエンドは運営していません |
| ネットワーク | ライブラリ、reading, recite, Character Study, meditation, Life Guidance, widgets, and daily notifications work **offline** after installは、インストール後 **オフライン** で動作します |
| 分析 / 広告 / トラッキング | **なし** — サードパーティの分析、広告、トラッキングSDKは使用しておらず、App Tracking Transparencyも使用していません |
| 任意のAppleサービス | **iCloud**（個人用KVS）、**フォトライブラリ（追加のみ）**でカードを共有、**StoreKit**で任意のチップ、**ローカル通知**、オプションの**Live Activities** |

## データの収集

当社は、広告や分析のために個人情報を収集、販売、共有することは**ありません**。

- **アカウント不要** — アカウントを作成せずに、すべての基本機能を使用できます。
- **分析や広告なし** — アプリのバイナリには、サードパーティの分析、広告、クラッシュレポートSDKは統合されておらず、データが当社に送信されることはありません。
- **コンテンツのアップロードなし** — お客様のreading history, favorites, study lists, reflection journal entries, habit check-ins, meditation streaks, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## アプリの仕組み

- **同梱ライブラリ** — テキスト JSON、白話／英語、索引、学習補助はアプリ／ウィジェット バンドル内に同梱されます。閲覧と学習にネットワークは不要です。
- **オンデバイス音声** - 朗読には Apple のシステム **AVSpeechSynthesizer** (TTS) が使用されます。 章のテキストは iHTC Studio に送信されません。
- **ウィジェットと App Group** — ウィジェットとアプリは、端末上の App Group `group.com.iHTCboy.iPrimer` を通じて設定と軽量な状態を共有します。
- **毎日の通知** - ユーザー通知を使用してローカルにスケジュールされます。 通知をタップすると、デバイス上のチャプタ ID へのディープ リンクが開きます。 サーバーのファンアウトはありません。
- **カードを共有** — 画像はデバイス上でレンダリングされます。 保存すると、[保存] をタップした場合にのみ **フォト ライブラリの追加のみ**が使用されます。 システム共有シートは、**あなた**が選択したアプリに画像を送信できます。 その場合、その宛先のプライバシー ポリシーが適用されます。
- **任意チップ** — 「Tip Developer」（`com.iHTCboy.iPrimer.6`）は Apple 処理の消耗型 **StoreKit** 購入です。カード情報は受け取りません。
- **Siri / ショートカット / コントロール センター** — オプションのシステム統合により、デバイス上のディープ リンクが開きます。 彼らはあなたのライブラリを私たちに送ることはありません。
- **オプションのスポットライト** — インデックス作成を有効にすると、ローカル検索のためにデバイス上のシステムによってコンテンツのインデックスが作成されます。 当社は検索バックエンドを運用していません。

## 端末に保存されるデータ

 | データ | どこ | 目的 |
 |------|-------|-----------|
| Chapter データベース | App / Widget バンドル | オフライン閲読と学習 |
| お気に入りと学習リスト | App Group UserDefaults | 星付き作品とリスト |
 | 読書履歴 / 最後に読んだ | アプリグループのUserDefaults | 続きを読む、履歴 UI |
| 学習進捗と習熟 | App Group UserDefaults | Character Study state, quiz / Hunt progress |
| 学習連続 / チェックイン | App Group UserDefaults | Daily Study 習慣 |
| 省思ジャーナル | App Group UserDefaults | Life Guidance ジャーナル |
| 習慣チェックイン（洒扫应对） | App Group UserDefaults | Life Guidance 毎日の習慣 |
| 瞑想連続とセッション設定 | App Group UserDefaults | 瞑想の継続 |
| 共有カードの設定 | App Group の UserDefaults | 最後に選んだスタイルや比率 |
| Daily Study cache & notification prefs | App Group UserDefaults | 今日の ID, 時刻, 文脈トグル |
 | 共有カードの設定 | アプリグループのUserDefaults | 最後のスタイル/比率の選択 |
 | オンボーディングと TipKit の状態 | 標準 UserDefaults (デバイス) | ウェルカムガイド / 発見のヒント |
 | ホーム画面のクイックアクション | システム + ローカル設定 | 設定するショートカット |
 | ウィジェット / ライブ アクティビティのスナップショット | アプリグループ / ActivityKit | すでに開いているテキストを表示 |

アプリをアンインストールすると、アプリに関連するサンドボックスおよびApp Groupデータが削除されます（iOS/macOSの動作に依存します）。任意のiCloudコピーは、あなたが削除するか、同期をオフにして他の場所で削除するまで、**あなたの**iCloudに残ります。

## iCloud同期（オプション）

設定で**iCloud同期**を有効にすると、アプリは選択したユーザーデータをAppleの**`NSUbiquitousKeyValueStore`**を通じてあなたのApple IDに関連付けて同期します：

- お気に入り
- 学習リスト
- 読書履歴
- 学習進捗 / 習熟度
- 学習連続記録
- 省思ジャーナル
- 習慣チェックイン履歴

同期トラフィックは**Apple iCloud**にのみ送信され、iHTC Studioには送信されません。設定で同期を無効にできます。私たちはあなたのiCloudの内容を読むことはできません。

## 権限

 iLiezi は、機能が必要な場合にのみアクセス許可を要求します。

| 権限 | タイミング | 理由 |
|------------|------|-----|
| 通知 | Daily Study or meditation reminders を有効にする | ローカルスケジュール |
## iCloud 同期（任意）
| iCloud | 同期を有効にする | お気に入り/リスト/履歴/進捗/連続/ジャーナル/習慣を同期 |
| Live Activities (iOS) | Reading / Meditation Live Activity | ロック画面 / Dynamic Island |
| バックグラウンド音声 | バックグラウンド朗誦を有効にする | バックグラウンドで TTS 継続 |

 当社は、連絡先、正確な位置情報、カメラ、マイク (システムの TTS 再生を超える)、または追跡を要求しません**。

## 子供のプライバシー

iPrimer は **12+** で **Kids Category 外**です。児童から故意に個人情報を収集しません。アカウント不要。

## 第三者

通常利用で関与する第三者サービスは **Apple** のみ（App Store、iCloud、StoreKit、システム TTS、通知、Live Activities）。

## データ保持と削除

- **端末上:** アプリを削除するとローカル sandbox と App Group データが削除されます（OS の挙動に依存）。
- **iCloud:** 設定で同期をオフにできます。システム設定で iCloud ストレージも管理できます。
- **当社は保持しません** — 閲読・ジャーナル・習慣データのコピーを iHTC Studio サーバーに保持しません。

## このポリシーの変更

法令、製品、または App Store コンプライアンスの理由で本ページを更新することがあります。上部の「最終更新日」が変更されます。更新後も利用を続ける場合、改訂版に同意したものとみなされます。

## お問い合わせ

プライバシーに関するご質問: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ko" markdown="1">

**마지막 업데이트:** 2026년 8월 18일

iHTC Studio("당사")는 **iPrimer**("爱小学" / "爱小学", Bundle ID `com.iHTCboy.iPrimer`)을(를) 개발했습니다. 본 개인정보 처리방침은 앱 사용 시 어떤 데이터가 처리되고 처리되지 않는지 설명합니다. **Apple App Review**와 사용자는 **이 페이지**를 공개 개인정보 처리방침으로 사용할 수 있습니다. App Store Connect에는 브라우저에서 본 개인정보 처리방침을 열고 주소창의 URL을 복사하세요(공개 사이트 도메인은 변경될 수 있습니다).

## 요약 (Apple 개인정보 영양성분표 정렬)

| 주제 | 당사의 정책 |
|-------|----------------|
| 계정 | **필요 없음** — 등록, 이메일 로그인, 전화번호 필요 없음 |
| iHTC 스튜디오의 데이터 수집 | **데이터 수집 없음** — 개인 데이터를 받는 백엔드를 운영하지 않습니다 |
| 네트워크 | 라이브러리, reading, recite, Character Study, meditation, Life Guidance, widgets, and daily notifications work **offline** after install는 설치 후 **오프라인**으로 동작합니다 |
| 분석 / 광고 / 추적 | **없음** — 타사 분석, 광고, 추적 SDK 없음; 앱 추적 투명성(App Tracking Transparency) 사용 없음 |
| 선택적 Apple 서비스 | **iCloud** (개인 KVS), **사진 라이브러리(추가만 가능)** 공유 카드용, **StoreKit** 선택적 후원용, **로컬 알림**, 선택적 **라이브 활동(Live Activities)** |

## 데이터 수집

개인 정보를 광고나 분석 목적으로 **수집, 판매, 공유하지 않습니다**.

- **계정 불필요** — 계정을 만들지 않아도 모든 핵심 기능을 사용할 수 있습니다.
- **분석 및 광고 없음** — 앱 바이너리는 당사로 데이터를 전송하는 타사 분석, 광고, 크래시 리포트 SDK를 통합하지 않습니다.
- **콘텐츠 업로드 없음** — 사용자의 reading history, favorites, study lists, reflection journal entries, habit check-ins, meditation streaks, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## 앱 작동 방식

- **번들 라이브러리** — 텍스트 JSON, vernacular/English, 색인, 학습 보조 자료가 앱/위젯 번들에 포함됩니다. 탐색과 학습에 네트워크가 필요하지 않습니다.
- **기기 내 음성** — 암송은 Apple 시스템 **AVSpeechSynthesizer**(TTS)를 사용합니다. iHTC Studio에는 장 텍스트를 보내지 않습니다.
- **위젯 및 App Group** — 위젯과 앱은 기기의 App Group `group.com.iHTCboy.iPrimer`을 통해 설정과 가벼운 상태를 공유합니다.
- **일일 알림** — 사용자 알림을 통해 로컬로 예약됩니다. 알림을 탭하면 기기의 챕터 ID에 대한 딥 링크가 열립니다. 서버 팬아웃이 없습니다.
- **카드 공유** — 이미지가 장치에서 렌더링됩니다. 저장은 저장을 탭한 경우에만 **사진 라이브러리 추가 전용**을 사용합니다. 시스템 공유 시트는 **귀하가** 선택한 앱으로 이미지를 보낼 수 있습니다. 그러면 해당 목적지의 개인정보 보호정책이 적용됩니다.
- **선택 팁** — “Tip Developer”(`com.iHTCboy.iPrimer.6`) Apple **StoreKit** 구매. 카드 정보 미수신.
- **Siri / 바로가기 / 제어 센터** — 선택적 시스템 통합으로 기기 내 딥 링크가 열립니다. 그들은 귀하의 라이브러리를 우리에게 보내지 않습니다.
- **선택적 스포트라이트** — 인덱싱을 활성화하면 로컬 검색을 위해 장치의 시스템에서 콘텐츠를 인덱싱합니다. 우리는 검색 백엔드를 운영하지 않습니다.

## 귀하의 장치에 저장된 데이터

| 데이터 | 어디 | 목적 |
|------|-------|---------|
| Chapter 데이터베이스 | App / Widget 번들 | 오프라인 읽기 및 학습 |
| 즐겨찾기·학습 목록 | App Group UserDefaults | 별표 작품·목록 |
| 읽은 이력/마지막 읽은 내용 | 앱 그룹 UserDefaults | 계속 읽기, 기록 UI |
| 학습 진행 및 숙달 | App Group UserDefaults | Character Study state, quiz / Hunt progress |
| 학습 연속 / 체크인 | App Group UserDefaults | Daily Study 습관 |
| 성찰 저널 | App Group UserDefaults | Life Guidance 저널 |
| 습관 체크인(洒扫应对) | App Group UserDefaults | Life Guidance 일일 습관 |
| 명상 연속·세션 설정 | App Group UserDefaults | 명상 연속 |
| 공유 카드 설정 | App Group UserDefaults | 마지막으로 선택한 스타일 / 비율 |
| Daily Study cache & notification prefs | App Group UserDefaults | 오늘 ID, 시간, contextual toggle |
| 공유 카드 환경 설정 | 앱 그룹 UserDefaults | 마지막 스타일/비율 선택 |
| 온보딩 및 TipKit 상태 | 표준 UserDefaults(장치) | 환영 가이드/탐색 팁 |
| 홈 화면 빠른 작업 | 시스템 + 로컬 환경설정 | 구성한 바로가기 |
| 위젯/실시간 활동 스냅샷 | 앱 그룹/ActivityKit | 이미 열어본 텍스트 표시 |

앱을 삭제하면 앱과 연관된 샌드박스 및 앱 그룹 데이터가 제거됩니다(iOS/macOS 동작에 따라 다름). 선택적으로 iCloud에 저장된 복사본은 사용자가 삭제하거나 동기화를 끄고 다른 곳에서 삭제할 때까지 **귀하의** iCloud에 남아 있습니다.

## iCloud 동기화 (선택 사항)

설정에서 **iCloud 동기화**를 활성화하면, 앱은 **귀하의 Apple ID**와 연결된 Apple의 **`NSUbiquitousKeyValueStore`**를 통해 선택한 사용자 데이터를 미러링합니다:

- 즐겨찾기
- 학습 목록
- 읽기 기록
- 학습 진행/숙련도
- 학습 연속
- 성찰 저널
- 습관 체크인 기록

동기화 트래픽은 iHTC Studio가 아닌 **Apple iCloud**로 전송됩니다. 설정에서 동기화를 비활성화할 수 있습니다. 우리는 귀하의 iCloud 내용을 읽을 수 없습니다.

## 권한

iLiezi는 기능에 필요한 경우에만 권한을 요청합니다.

| 허가 | 언제 | 왜? |
|------------|------|-----|
| 알림 | Daily Study or meditation reminders 사용 | 로컬 예약 |
## iCloud 동기화(선택)
| iCloud | 동기화 사용 | 즐겨찾기/목록/기록/진행/연속/저널/습관 |
| Live Activities(iOS) | Reading/Meditation Live Activity | 잠금 화면 / Dynamic Island |
| 배경 오디오 | 배경 낭송 사용 | 백그라운드 TTS |

우리는 연락처, 정확한 위치, 카메라, 마이크(시스템 TTS 재생 이외) 또는 추적을 요청하지 **않습니다**.

## 아동 개인정보 보호

iPrimer **12+**, **Kids Category 아님**. 아동 개인정보 고의 수집 안 함. 계정 불필요.

## 제3자

일반 사용 시 제3자는 **Apple**만(App Store, iCloud, StoreKit, TTS, 알림, Live Activities).

## 데이터 보존 및 삭제

- **기기에서:** 앱 삭제 시 로컬 sandbox·App Group 데이터 제거(시스템 동작에 따름).
- **iCloud:** 설정에서 동기화 끄기. 시스템 설정에서 iCloud 저장공간 관리.
- **보관하지 않습니다** — 읽기·저널·습관 데이터 사본을 iHTC Studio 서버에 두지 않습니다.

## 이 정책의 변경

법적, 제품 또는 App Store 준수 사유로 본 페이지를 업데이트할 수 있습니다. 상단의 「최종 업데이트」 날짜가 변경됩니다. 업데이트 후 계속 사용하면 개정된 정책에 동의하는 것입니다.

## 연락처

개인정보 관련 문의: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ru" markdown="1">

**Последнее обновление:** 18 августа 2026 г.

iHTC Studio («мы») создала **iPrimer** («爱小学» / «爱小学», Bundle ID `com.iHTCboy.iPrimer`). Настоящая Политика конфиденциальности объясняет, какие данные обрабатываются (и не обрабатываются) при использовании приложения. **Apple App Review** и пользователи могут использовать **эту страницу** как публичную политику конфиденциальности. Для App Store Connect откройте эту страницу в браузере и скопируйте URL из адресной строки (домен публичного сайта может измениться).

## Сводка (в соответствии с меткой Apple Privacy Nutrition)

| Тема | Наша практика |
|-------|----------------|
| Учетная запись | **Не требуется** — регистрация, вход по электронной почте или номеру телефона не нужны |
| Сбор данных iHTC Studio | **Данные не собираются** — мы **не** используем серверную часть, которая получает ваши личные данные |
| Сеть | Библиотека, reading, recite, Character Study, meditation, Life Guidance, widgets, and daily notifications work **offline** after install работают **офлайн** после установки |
| Аналитика / реклама / отслеживание | **Отсутствует** — нет сторонней аналитики, рекламы или SDK для отслеживания; не используется App Tracking Transparency |
| Дополнительные сервисы Apple | **iCloud** (ваш личный KVS), **Фототека (только добавление)** для общих карточек, **StoreKit** для необязательных чаевых, **локальные уведомления**, необязательные **Live Activities** |

## Сбор данных

Мы **не** собираем, не продаем и не делимся личной информацией для рекламы или аналитики.

- **Без аккаунта** — Вы можете использовать все основные функции без создания аккаунта у нас.
- **Без аналитики и рекламы** — В приложении не интегрированы сторонние SDK для аналитики, рекламы или отчётов о сбоях, которые отправляли бы данные нам.
- **Без загрузки контента** — Ваши reading history, favorites, study lists, reflection journal entries, habit check-ins, meditation streaks, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## Как работает приложение

- **Встроенная библиотека** — текстовый JSON, vernacular/English, указатели и учебные материалы входят в пакет app/widget. Для просмотра и обучения сеть не нужна.
- **Речь на устройстве** — при декламации используется система Apple **AVSpeechSynthesizer** (TTS). Мы не отправляем текст главы в iHTC Studio.
- **Виджеты и App Group** — виджеты и приложение обмениваются настройками и лёгким состоянием через App Group `group.com.iHTCboy.iPrimer` на вашем устройстве.
- **Ежедневные уведомления** — планируются локально с помощью уведомлений пользователя. При нажатии на уведомление открывается глубокая ссылка на идентификатор главы на устройстве; нет разветвления сервера.
- **Поделиться картами** — изображения отображаются на устройстве. При сохранении используется **Дополнение «Библиотека фотографий»** только при нажатии «Сохранить». System Share Sheet может отправить изображение в приложение, выбранное вами **; В этом случае применяется политика конфиденциальности этого пункта назначения.
- **Чаевые** — «Tip Developer» (`com.iHTCboy.iPrimer.6`), **StoreKit** через Apple. Данные карты не получаем.
- **Siri / Ярлыки / Центр управления** — дополнительные системные интеграции открывают глубокие ссылки на устройстве; они не отправляют нам вашу библиотеку.
- **Дополнительный Spotlight** — если вы включите индексирование, контент индексируется системой на устройстве для локального поиска; мы не используем поисковую систему.

## Данные, хранящиеся на вашем устройстве

| Данные | Где | Цель |
|------|-------|---------|
| База Chapter | Пакет App / Widget | Офлайн-чтение и обучение |
| Избранное и учебные списки | UserDefaults App Group | Избранные произведения |
| История чтения / последнее чтение | Пользовательские настройки группы приложений | Продолжить чтение, история пользовательского интерфейса |
| Прогресс и mastery | UserDefaults App Group | Character Study state, quiz / Hunt progress |
| Серия учёбы / check-in | UserDefaults App Group | Привычка Daily Study |
| Записи рефлексии | UserDefaults App Group | Журнал Life Guidance |
| Привычки (洒扫应对) | UserDefaults App Group | Привычки Life Guidance |
| Серия медитации и настройки | UserDefaults App Group | Непрерывность медитации |
| Настройки карточек для обмена | UserDefaults App Group | Последний выбранный стиль / соотношение сторон |
| Daily Study cache & notification prefs | UserDefaults App Group | ID на сегодня, время, переключатели |
| Настройки карты обмена | Пользовательские настройки группы приложений | Последний выбор стиля/пропорции |
| Регистрация и состояние TipKit | Стандартные настройки пользователя (устройство) | Приветственное руководство / советы по открытию |
| Быстрые действия на главном экране | Система + локальные настройки | Ярлыки, которые вы настраиваете |
| Виджет / Снимки активности в реальном времени | Группа приложений / ActivityKit | Показать текст, который вы уже открыли |

При удалении приложения удаляются данные песочницы и группы приложений, связанные с приложением (в зависимости от поведения iOS/macOS). Дополнительные копии iCloud остаются в **вашем** iCloud до тех пор, пока вы не очистите их или не отключите синхронизацию и не удалите их в другом месте.

## Синхронизация с iCloud (необязательно)

Если вы включите **iCloud Sync** в настройках, приложение зеркально отображает выбранные пользовательские данные через **`NSUbiquitousKeyValueStore`** Apple, привязанный к **вашему Apple ID**:

- Избранное
- Списки обучения
- Чтение истории
- Прогресс в учебе/мастерстве
- Учебные серии
- Записи рефлексивного журнала
- История привычек

Трафик синхронизации поступает в **Apple iCloud**, а не в iHTC Studio. Вы можете отключить синхронизацию в настройках. Мы не можем прочитать ваше содержимое iCloud.

## Разрешения

iLiezi запрашивает разрешения только тогда, когда они нужны функции:

| Разрешение | Когда | Почему |
|------------|------|-----|
| Уведомления | Вы включаете Daily Study or meditation reminders | Локальное планирование |
## Синхронизация через iCloud (необязательно)
| iCloud | Включаете синхронизацию | Избранное/списки/история/прогресс/серии/журнал/привычки |
| Live Activities (iOS) | Reading or Meditation Live Activity | Lock Screen / Dynamic Island |
| Фоновое аудио | Включаете фоновое чтение | TTS в фоне |

Мы **не** запрашиваем контакты, точное местоположение, камеру, микрофон (кроме системного воспроизведения TTS) или отслеживание.

## Конфиденциальность детей

iPrimer — **12+**, **не** Kids Category. Не собираем данные детей сознательно. Без аккаунта.

## Третьи стороны

При обычном использовании задействован только **Apple** (App Store, iCloud, StoreKit, TTS, уведомления, Live Activities).

## Сроки хранения и удаление данных

- **На устройстве:** удалите приложение, чтобы удалить sandbox и данные App Group (поведение системы).
- **iCloud:** отключите синхронизацию в Настройках; управляйте хранилищем iCloud в системных настройках.
- **Мы не храним копии** чтения, журнала и привычек на серверах iHTC Studio.

## Изменения в этой Политике

Мы можем обновлять эту страницу по юридическим причинам, из‑за продукта или требований App Store. Дата «Последнего обновления» изменится. Продолжение использования после обновления означает принятие пересмотренной политики.

## Контакт

Вопросы о конфиденциальности: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="th" markdown="1">

**อัปเดตล่าสุด:** 18 สิงหาคม 2026

iHTC Studio ("เรา") พัฒนา **iPrimer** ("爱小学" / "爱小学", Bundle ID `com.iHTCboy.iPrimer`) นโยบายความเป็นส่วนตัวนี้อธิบายว่าข้อมูลใดถูกจัดการและไม่ถูกจัดการเมื่อคุณใช้แอป **Apple App Review** และผู้ใช้สามารถใช้**หน้านี้**เป็นนโยบายความเป็นส่วนตัวสาธารณะ สำหรับ App Store Connect ให้เปิดนโยบายนี้ในเบราว์เซอร์แล้วคัดลอก URL จากแถบที่อยู่ (โดเมนสาธารณะอาจเปลี่ยนได้)

## สรุป (การจัดตำแหน่งกับ Nutrition Label ความเป็นส่วนตัวของ Apple)

| หัวข้อ | การปฏิบัติของเรา |
|-------|----------------|
| บัญชี | **ไม่จำเป็น** — ไม่ต้องลงทะเบียน ลงชื่อเข้าใช้ด้วยอีเมล หรือหมายเลขโทรศัพท์ |
| การเก็บข้อมูลโดย iHTC Studio | **ไม่เก็บข้อมูล** — เรา **ไม่ได้**ดำเนินการแบ็กเอนด์ที่รับข้อมูลส่วนตัวของคุณ |
| เครือข่าย | คลังข้อมูล reading, recite, Character Study, meditation, Life Guidance, widgets, and daily notifications work **offline** after install ทำงาน **แบบออฟไลน์** หลังติดตั้ง |
| การวิเคราะห์ / โฆษณา / การติดตาม | **ไม่มี** — ไม่มี SDK การวิเคราะห์ โฆษณา หรือการติดตามจากบุคคลที่สาม; ไม่ใช้ App Tracking Transparency |
| บริการ Apple ทางเลือก | **iCloud** (KVS ส่วนตัวของคุณ), **Photo Library (เพิ่มเท่านั้น)** สำหรับการแชร์การ์ด, **StoreKit** สำหรับการให้ทิปเป็นทางเลือก, **การแจ้งเตือนในเครื่อง**, **Live Activities** เป็นทางเลือก |

## การเก็บข้อมูล

เราจะ **ไม่**เก็บ ขาย หรือแชร์ข้อมูลส่วนบุคคลเพื่อโฆษณาหรือการวิเคราะห์

- **ไม่ต้องมีบัญชีผู้ใช้** — คุณสามารถใช้คุณสมบัติหลักทั้งหมดได้โดยไม่ต้องสร้างบัญชีกับเรา
- **ไม่มีการวิเคราะห์หรือโฆษณา** — ไฟล์แอปไม่ได้รวม SDK การวิเคราะห์ การโฆษณา หรือการรายงานข้อผิดพลาดจากบุคคลที่สามที่ติดต่อกลับไปยังเรา
- **ไม่อัปโหลดเนื้อหา** — reading history, favorites, study lists, reflection journal entries, habit check-ins, meditation streaks, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**. ของคุณ

## วิธีการทำงานของแอป

- **ไลบรารีในชุดแอป** — JSON ข้อความ vernacular/English ดัชนี และตัวช่วยเรียนอยู่ในชุดแอป/วิดเจ็ต การเรียกดูและเรียนไม่ต้องใช้เครือข่าย
- **คำพูดบนอุปกรณ์** — การบรรยายใช้ระบบของ Apple **AVSpeechSynthesizer** (TTS) เราไม่ส่งข้อความบทไปที่ iHTC Studio
- **วิดเจ็ตและ App Group** — วิดเจ็ตและแอปใช้การตั้งค่าและสถานะขนาดเล็กร่วมกันผ่าน App Group `group.com.iHTCboy.iPrimer` บนอุปกรณ์ของคุณ
- **การแจ้งเตือนรายวัน** — กำหนดเวลาภายในเครื่องด้วยการแจ้งเตือนผู้ใช้ การแตะการแจ้งเตือนจะเปิดลิงก์ในรายละเอียดไปยัง Chapter ID บนอุปกรณ์ ไม่มีการปิดเซิร์ฟเวอร์
- **แชร์การ์ด** — รูปภาพถูกเรนเดอร์บนอุปกรณ์ การบันทึกจะใช้ **เฉพาะส่วนเสริมคลังรูปภาพ** เฉพาะเมื่อคุณแตะบันทึก เอกสารการแชร์ระบบอาจส่งรูปภาพไปยังแอป **คุณ** เลือก; นโยบายความเป็นส่วนตัวของปลายทางนั้นจึงจะมีผลใช้บังคับ
- **ทิปเสริม** — “Tip Developer” (`com.iHTCboy.iPrimer.6`) **StoreKit** โดย Apple
- **Siri / ทางลัด / ศูนย์ควบคุม** — การรวมระบบที่เป็นตัวเลือกจะเปิดลิงก์ในรายละเอียดบนอุปกรณ์ พวกเขาไม่ได้ส่งห้องสมุดของคุณมาให้เรา
- **สปอตไลท์เสริม** — หากคุณเปิดใช้งานการจัดทำดัชนี เนื้อหาจะถูกจัดทำดัชนีโดยระบบบนอุปกรณ์สำหรับการค้นหาในท้องถิ่น เราไม่ได้ดำเนินการแบ็กเอนด์การค้นหา

## ข้อมูลที่เก็บบนอุปกรณ์

| ข้อมูล | ที่ไหน | วัตถุประสงค์ |
|------|-------|---------|
| ฐานข้อมูล Chapter | App / Widget bundle | การอ่านและเรียนแบบออฟไลน์ |
| รายการโปรดและเรียน | UserDefaults ของ App Group | ผลงานติดดาวและรายการ |
| ประวัติการอ่าน / อ่านครั้งล่าสุด | ค่าเริ่มต้นของกลุ่มแอป | อ่านต่อ ประวัติ UI |
| ความคืบหน้าและความเชี่ยวชาญ | UserDefaults ของ App Group | Character Study state, quiz / Hunt progress |
| สตรีคเรียน / เช็คอין | UserDefaults ของ App Group | นิสัย Daily Study |
| บันทึกสะท้อนคิด | UserDefaults ของ App Group | บันทึก Life Guidance |
| เช็คอินนิสัย (洒扫应对) | UserDefaults ของ App Group | นิสัยรายวัน Life Guidance |
| สตรีคสมาธิและการตั้งค่า | UserDefaults ของ App Group | ความต่อเนื่องสมาธิ |
| การตั้งค่าการ์ดแชร์ | UserDefaults ของ App Group | สไตล์ / อัตราส่วนที่เลือกล่าสุด |
| Daily Study cache & notification prefs | UserDefaults ของ App Group | ID วันนี้, schedule time, contextual toggle |
| การตั้งค่าการ์ดแชร์ | ค่าเริ่มต้นของกลุ่มแอป | ตัวเลือกสไตล์ / อัตราส่วนสุดท้าย |
| การเริ่มต้นใช้งานและสถานะ TipKit | Standard UserDefaults (อุปกรณ์) | คู่มือต้อนรับ / เคล็ดลับการค้นพบ |
| การดำเนินการด่วนบนหน้าจอหลัก | ระบบ + การตั้งค่าท้องถิ่น | ทางลัดที่คุณกำหนดค่า |
| วิดเจ็ต / ภาพรวมกิจกรรมสด | กลุ่มแอป / ActivityKit | แสดงข้อความที่คุณเปิดแล้ว |

การถอนการติดตั้งแอปจะลบข้อมูล sandbox และ App Group ที่เกี่ยวข้องกับแอป (ขึ้นอยู่กับพฤติกรรมของ iOS/macOS) สำเนา iCloud แบบเลือกได้จะยังคงอยู่ใน **iCloud ของคุณ** จนกว่าคุณจะลบหรือปิดการซิงค์และลบจากที่อื่น

## การซิงค์ iCloud (ตัวเลือก)

หากคุณเปิดใช้งาน **การซิงค์ iCloud** ในการตั้งค่า แอปจะสะท้อนข้อมูลผู้ใช้ที่เลือกผ่าน **`NSUbiquitousKeyValueStore`** ของ Apple ที่เชื่อมโยงกับ **Apple ID ของคุณ**:

- รายการโปรด
- รายการเรียน
- ประวัติการอ่าน
- ความคืบหน้า/ความชำนาญในการศึกษา
- สตรีคการเรียน
- บันทึกสะท้อนคิด
- ประวัติเช็คอินนิสัย

การจราจรการซิงค์จะไปยัง **Apple iCloud** ไม่ใช่ iHTC Studio คุณสามารถปิดการซิงค์ได้ใน การตั้งค่า เราไม่สามารถอ่านเนื้อหา iCloud ของคุณได้

## สิทธิ์

iLiezi ร้องขอการอนุญาตเฉพาะเมื่อคุณสมบัติต้องการ:

| สิทธิ์ | เมื่อไหร่ | ทำไม |
|------------|------|-----|
| การแจ้งเตือน | คุณเปิด Daily Study or meditation reminders | กำหนดเวลาในเครื่อง |
## การซิงค์ iCloud (ไม่บังคับ)
| iCloud | เปิดซิงค์ | ซิงค์รายการโปรด/รายการ/ประวัติ/ความคืบหน้า/สตรีค/บันทึก/นิสัย |
| Live Activities (iOS) | Reading/Meditation Live Activity | หน้าจอล็อก / Dynamic Island |
| เสียงพื้นหลัง | เปิดท่องพื้นหลัง | TTS พื้นหลัง |

เราไม่ **ไม่** ขอข้อมูลผู้ติดต่อ ตำแหน่งที่แน่นอน กล้อง ไมโครโฟน (นอกเหนือจากการเล่น TTS ของระบบ) หรือการติดตาม

## ความเป็นส่วนตัวของเด็ก

iPrimer **12+** **ไม่ใช่** Kids Category ไม่เก็บข้อมูลเด็จโดยเจตนา

## บุคคลที่สาม

บริการบุคคลที่สามคือ **Apple** เท่านั้น

## การเก็บรักษาและการลบข้อมูล

- **บนอุปกรณ์:** ลบแอปเพื่อลบ sandbox และ App Group (ตามพฤติกรรมระบบ)
- **iCloud:** ปิดซิงค์ในการตั้งค่า จัดการพื้นที่ iCloud ในการตั้งค่าระบบ
- **เราไม่เก็บสำเนา** ข้อมูลการอ่าน/บันทึก/นิสัยบนเซิร์ฟเวอร์ iHTC Studio

## การเปลี่ยนแปลงนโยบายนี้

เราอาจปรับปรุงหน้านี้ด้วยเหตุผลทางกฎหมาย ผลิตภัณฑ์ หรือการปฏิบัติตาม App Store วันที่ 「อัปเดตล่าสุด」 จะเปลี่ยน การใช้งานต่อหลังอัปเดตถือว่าคุณยอมรับนโยบายที่แก้ไข

## ติดต่อ

คำถามเกี่ยวกับความเป็นส่วนตัว: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="de" markdown="1">

**Zuletzt aktualisiert:** 18. August 2026

iHTC Studio („wir“) hat **iPrimer** („爱小学“ / „爱小学“, Bundle-ID `com.iHTCboy.iPrimer`) entwickelt. Diese Datenschutzerklärung erläutert, welche Daten bei der Nutzung verarbeitet werden (und welche nicht). **Apple App Review** und Nutzer können sich auf **diese Seite** als öffentliche Datenschutzerklärung stützen. Für App Store Connect öffnen Sie diese Seite im Browser und kopieren Sie die URL aus der Adressleiste (die Domain kann sich ändern).

## Zusammenfassung (Übereinstimmung mit dem Apple-Datenschutzetikett)

| Thema | Unsere Praxis |
|-------|----------------|
| Konto | **Nicht erforderlich** — keine Registrierung, kein E-Mail-Login oder Telefonnummer erforderlich |
| Datenerhebung durch iHTC Studio | **Keine Datenerhebung** — wir betreiben **keinen** Backend-Service, der Ihre persönlichen Daten empfängt |
| Netzwerk | Bibliothek, reading, recite, Character Study, meditation, Life Guidance, widgets, and daily notifications work **offline** after install funktionieren nach der Installation **offline** |
| Analysen / Werbung / Tracking | **Keine** — keine Analysen von Drittanbietern, Werbung oder Tracking-SDKs; keine Nutzung von App Tracking Transparency |
| Optionale Apple-Dienste | **iCloud** (Ihr privates KVS), **Fotobibliothek (Nur Hinzufügen)** für geteilte Karten, **StoreKit** für optionale Trinkgelder, **lokale Benachrichtigungen**, optionale **Live-Aktivitäten** |

## Datenerfassung

Wir erheben, verkaufen oder teilen **keine** persönlichen Informationen für Werbung oder Analysen.

- **Kein Konto** — Sie können alle Kernfunktionen nutzen, ohne ein Konto bei uns zu erstellen.
- **Keine Analysen oder Werbung** — Die App-Binärdatei integriert keine Analysen, Werbung oder Crash-Reporting-SDKs von Drittanbietern, die Daten an uns senden.
- **Kein Hochladen von Inhalten** — Ihre reading history, favorites, study lists, reflection journal entries, habit check-ins, meditation streaks, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## So funktioniert die App

- **Mitgelieferte Bibliothek** — Text-JSON, Umgangssprache/Englisch, Indizes und Lernhilfen liegen im App-/Widget-Bundle. Durchsuchen und Lernen erfordern kein Netzwerk.
- **Sprache auf dem Gerät** – Die Rezitation nutzt Apples System **AVSpeechSynthesizer** (TTS). Wir senden keinen Kapiteltext an iHTC Studio.
- **Widgets und App Group** — Widgets und App teilen Einstellungen und leichten Zustand über die App Group `group.com.iHTCboy.iPrimer` auf Ihrem Gerät.
- **Tägliche Benachrichtigungen** – Lokal geplant mit Benutzerbenachrichtigungen. Durch Tippen auf eine Benachrichtigung wird ein Deep-Link zu einer Kapitel-ID auf dem Gerät geöffnet. Kein Server-Fanout.
- **Karten teilen** – Bilder werden auf dem Gerät gerendert. Beim Speichern wird **nur die Add-On-Fotobibliothek** verwendet, wenn Sie auf „Speichern“ tippen. Das System Share Sheet sendet das Bild möglicherweise an eine von Ihnen ausgewählte App. Es gelten dann die Datenschutzbestimmungen dieses Reiseziels.
- **Optionaler Tipp** — „Tip Developer“ (`com.iHTCboy.iPrimer.6`), **StoreKit** via Apple.
- **Siri / Verknüpfungen / Kontrollzentrum** – Optionale Systemintegrationen öffnen Deep Links auf dem Gerät; Sie senden Ihre Bibliothek nicht an uns.
- **Optionales Spotlight** – Wenn Sie die Indizierung aktivieren, werden Inhalte vom System auf dem Gerät für die lokale Suche indiziert; Wir betreiben kein Such-Backend.

## Auf Ihrem Gerät gespeicherte Daten

| Daten | Wo | Zweck |
|------|-------|---------|
| Chapter-Datenbank | App-/Widget-Bundle | Offline-Lesen und -Lernen |
| Favoriten & Lernlisten | UserDefaults der App Group | Markierte Werke & Listen |
| Leseverlauf / zuletzt gelesen | Benutzerstandards der App-Gruppe | Lesen Sie weiter, Verlauf der Benutzeroberfläche |
| Lernfortschritt und Beherrschung | UserDefaults der App Group | Character Study state, quiz / Hunt progress |
| Lernserie / Check-in | UserDefaults der App Group | Daily-Study-Gewohnheit |
| Reflexionstagebuch | UserDefaults der App Group | Life-Guidance-Tagebuch |
| Gewohnheits-Check-ins (洒扫应对) | UserDefaults der App Group | Life-Guidance-Gewohnheiten |
| Meditations-Serie & Sitzungen | UserDefaults der App Group | Meditationskontinuität |
| Einstellungen der Teilen-Karten | UserDefaults der App Group | Zuletzt gewählter Stil / zuletzt gewähltes Seitenverhältnis |
| Daily Study cache & notification prefs | UserDefaults der App Group | Heutige ID, schedule time, contextual toggle |
| Share-Card-Einstellungen | Benutzerstandards der App-Gruppe | Letzte Stil-/Verhältnisauswahl |
| Onboarding- und TipKit-Status | Standard UserDefaults (Gerät) | Willkommensführer / Entdeckungstipps |
| Schnellaktionen auf dem Startbildschirm | System + lokale Einstellungen | Von Ihnen konfigurierte Verknüpfungen |
| Widget-/Live-Aktivitäts-Schnappschüsse | App-Gruppe / ActivityKit | Text anzeigen, den Sie bereits geöffnet haben |

Die Deinstallation der App entfernt Sandbox- und App-Gruppendaten, die mit der App verbunden sind (abhängig vom Verhalten von iOS/macOS). Optionale iCloud-Kopien bleiben in **deiner** iCloud, bis du sie löschst oder die Synchronisierung ausschaltest und anderswo löschst.

## iCloud-Synchronisierung (optional)

Wenn du **iCloud-Synchronisierung** in den Einstellungen aktivierst, spiegelt die App ausgewählte Benutzerdaten über Apples **`NSUbiquitousKeyValueStore`**, die mit **deiner Apple-ID** verknüpft ist:

- Favoriten
- Lernlisten
- Leseverlauf
- Lernfortschritt / Kenntnisse
- Lernserien
- Reflexionstagebuch
- Gewohnheits-Check-ins

Der Synchronisationsverkehr geht an **Apple iCloud**, nicht an iHTC Studio. Du kannst die Synchronisierung in den Einstellungen deaktivieren. Wir können deine iCloud-Inhalte nicht lesen.

## Berechtigungen

iLiezi fordert Berechtigungen nur an, wenn eine Funktion diese benötigt:

| Erlaubnis | Wann | Warum |
|------------|------|-----|
| Benachrichtigungen | Sie aktivieren Daily Study or meditation reminders | Lokale Planung |
| Fotomediathek (nur Hinzufügen) | Sie speichern eine Teilen-Karte | Gerendertes Bild schreiben |
| iCloud | Sync aktivieren | Favoriten/Listen/Verlauf/Fortschritt/Serien/Journal/Gewohnheiten |
| Live Activities (iOS) | Reading/Meditation Live Activity | Sperrbildschirm / Dynamic Island |
| Hintergrundaudio | Hintergrundrezitation aktivieren | TTS im Hintergrund |

Wir fordern **keine** Kontakte, den genauen Standort, die Kamera, das Mikrofon (über die System-TTS-Wiedergabe hinaus) oder die Nachverfolgung an.

## Privatsphäre von Kindern

iPrimer **12+**, **nicht** Kids Category. Keine bewusste Datenerhebung von Kindern.

## Dritte Parteien

Drittanbieter: nur **Apple** (App Store, iCloud, StoreKit, TTS, Benachrichtigungen, Live Activities).

## Datenaufbewahrung & Löschung

- **Auf dem Gerät:** App löschen entfernt Sandbox und App Group (systemabhängig).
- **iCloud:** Sync in Einstellungen deaktivieren; iCloud-Speicher in Systemeinstellungen verwalten.
- **Wir speichern keine Kopien** von Lese-, Journal- und Gewohnheitsdaten auf iHTC Studio-Servern.

## Änderungen an dieser Richtlinie

Wir können diese Seite aus rechtlichen Gründen, produktbedingt oder wegen App-Store-Compliance aktualisieren. Das Datum „Zuletzt aktualisiert“ ändert sich. Fortgesetzte Nutzung nach einer Aktualisierung gilt als Zustimmung zur überarbeiteten Richtlinie.

## Kontakt

Fragen zum Datenschutz: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="fr" markdown="1">

**Dernière mise à jour :** 18 août 2026

iHTC Studio (« nous ») a développé **iPrimer** (« 爱小学 » / « 爱小学 », Bundle ID `com.iHTCboy.iPrimer`). Cette politique de confidentialité explique quelles données sont (ou ne sont pas) traitées lorsque vous utilisez l’app. **Apple App Review** et les utilisateurs peuvent s’appuyer sur **cette page** comme politique publique. Pour App Store Connect, ouvrez cette page dans le navigateur et copiez l’URL depuis la barre d’adresse (le domaine public peut changer).

## Résumé (alignement sur l'étiquette nutritionnelle de confidentialité Apple)

| Sujet | Notre pratique |
|-------|----------------|
| Compte | **Non requis** — pas d'inscription, de connexion par e-mail ou de numéro de téléphone |
| Collecte de données par iHTC Studio | **Données non collectées** — nous n'exploitons **pas** de backend qui reçoit vos données personnelles |
| Réseau | Bibliothèque, reading, recite, Character Study, meditation, Life Guidance, widgets, and daily notifications work **offline** after install fonctionnent **hors ligne** après l’installation |
| Analyses / publicités / suivi | **Aucun** — pas de SDK tiers d'analyse, de publicité ou de suivi ; pas d'utilisation de la transparence du suivi des applications |
| Services Apple en option | **iCloud** (votre KVS privé), **Photothèque (ajout uniquement)** pour les cartes de partage, **StoreKit** pour les pourboires facultatifs, **notifications locales**, **Activités en direct** en option |

## Collecte de données

Nous ne collectons, vendons ou partageons **pas** d'informations personnelles à des fins publicitaires ou analytiques.

- **Aucun compte** — Vous pouvez utiliser toutes les fonctionnalités principales sans créer de compte chez nous.
- **Aucune analyse ni publicité** — Le binaire de l'application n'intègre pas de SDK tiers d'analyse, de publicité ou de rapport d'erreur qui nous contactent.
- **Aucun envoi de contenu** — Vos reading history, favorites, study lists, reflection journal entries, habit check-ins, meditation streaks, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## Comment fonctionne l'application

- **Bibliothèque incluse** — JSON texte, vernaculaire/anglais, index et aides d’étude sont dans le bundle app/widget. Parcourir et étudier ne nécessite pas le réseau.
- **Discours sur l'appareil** — La récitation utilise le système **AVSpeechSynthesizer** (TTS) d'Apple. Nous n'envoyons pas de texte de chapitre à iHTC Studio.
- **Widgets et App Group** — Les widgets et l’app partagent des préférences et un état léger via l’App Group `group.com.iHTCboy.iPrimer` sur votre appareil.
- **Notifications quotidiennes** — Planifiées localement avec les notifications utilisateur. Appuyer sur une notification ouvre un lien profond vers un ID de chapitre sur l'appareil ; pas de distribution du serveur.
- **Partager des cartes** : les images sont rendues sur l'appareil. L'enregistrement utilise **le module complémentaire Photothèque** uniquement lorsque vous appuyez sur Enregistrer. System Share Sheet peut envoyer l'image à une application **que** vous choisissez ; la politique de confidentialité de cette destination s’applique alors.
- **Pourboire facultatif** — « Tip Developer » (`com.iHTCboy.iPrimer.6`), **StoreKit** via Apple.
- **Siri / Raccourcis / Centre de contrôle** — Les intégrations système facultatives ouvrent des liens profonds sur l'appareil ; ils ne nous envoient pas votre bibliothèque.
- **Spotlight facultatif** — Si vous activez l'indexation, le contenu est indexé par le système sur l'appareil pour la recherche locale ; nous n'exploitons pas de backend de recherche.

## Données stockées sur votre appareil

| Données | Où | Objectif |
|------|-------|--------------|
| Base Chapter | Bundle App / Widget | Lecture et étude hors ligne |
| Favoris et listes d’étude | UserDefaults de l’App Group | Œuvres favorites et listes |
| Historique de lecture / dernière lecture | Paramètres par défaut du groupe d'applications | Continuer la lecture, historique de l'interface utilisateur |
| Progression d’étude et maîtrise | UserDefaults de l’App Group | Character Study state, quiz / Hunt progress |
| Série d’étude / check-in | UserDefaults de l’App Group | Habitude Daily Study |
| Journal de réflexion | UserDefaults de l’App Group | Journal Life Guidance |
| Check-ins d’habitude (洒扫应对) | UserDefaults de l’App Group | Habitudes Life Guidance |
| Série méditation et prefs | UserDefaults de l’App Group | Continuité méditation |
| Préférences des cartes de partage | UserDefaults de l'App Group | Derniers choix de style / de format |
| Daily Study cache & notification prefs | UserDefaults de l’App Group | ID du jour, schedule time, contextual toggle |
| Préférences de carte partagée | Paramètres par défaut du groupe d'applications | Derniers choix de style/ratio |
| État d’intégration et de TipKit | Paramètres utilisateur standard (appareil) | Guide d'accueil / conseils découverte |
| Actions rapides sur l'écran d'accueil | Système + préférences locales | Raccourcis que vous configurez |
| Widget / Instantanés d'activité en direct | Groupe d'applications / ActivityKit | Afficher le texte que vous avez déjà ouvert |

La désinstallation de l'application supprime les données du bac à sable et du groupe d'applications associées à l'application (selon le comportement d'iOS/macOS). Les copies facultatives dans iCloud restent dans **votre** iCloud jusqu'à ce que vous les supprimiez ou que vous désactiviez la synchronisation et supprimiez ailleurs.

## Synchronisation iCloud (Facultative)

Si vous activez **la synchronisation iCloud** dans les Réglages, l'application reflète les données utilisateur sélectionnées via le **`NSUbiquitousKeyValueStore`** d'Apple lié à **votre identifiant Apple** :

- Favoris
- Listes d’étude
- Historique de lecture
- Progression / maîtrise des études
- Séries d’étude
- Journal de réflexion
- Historique d’habitudes

Le trafic de synchronisation passe par **Apple iCloud**, et non par iHTC Studio. Vous pouvez désactiver la synchronisation dans les Réglages. Nous ne pouvons pas lire le contenu de votre iCloud.

## Autorisations

iLiezi demande des autorisations uniquement lorsqu'une fonctionnalité en a besoin :

| Autorisation | Quand | Pourquoi |
|------------|------|-----|
| Notifications | Vous activez Daily Study or meditation reminders | Planification locale |
## Synchronisation iCloud (facultative)
| iCloud | Activez la sync | Favoris/listes/historique/progression/séries/journal/habitudes |
| Live Activities (iOS) | Reading/Meditation Live Activity | Écran verrouillé / Dynamic Island |
| Audio de fond | Récitation en arrière-plan | TTS en arrière-plan |

Nous ne demandons **pas** de contacts, de localisation précise, de caméra, de microphone (au-delà de la lecture TTS du système) ou de suivi.

## Confidentialité des enfants

iPrimer **12+**, **pas** Kids Category. Pas de collecte d’enfants.

## Tiers

Services tiers : **Apple** uniquement (App Store, iCloud, StoreKit, TTS, notifications, Live Activities).

## Conservation et suppression des données

- **Sur l’appareil :** supprimer l’app efface le sandbox et l’App Group (selon le système).
- **iCloud :** désactivez la sync dans Réglages ; gérez le stockage iCloud dans Réglages système.
- **Nous ne conservons pas de copies** de lecture, journal ou habitudes sur les serveurs iHTC Studio.

## Modifications de cette politique

Nous pouvons mettre à jour cette page pour des raisons juridiques, produit ou conformité App Store. La date « Dernière mise à jour » changera. L’utilisation continue après une mise à jour vaut acceptation de la politique révisée.

## Nous contacter

Questions sur la vie privée : [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="tr" markdown="1">

**Son güncelleme:** 18 Ağustos 2026

iHTC Studio ("biz"), **iPrimer** ("爱小学" / "爱小学", Bundle ID `com.iHTCboy.iPrimer`) uygulamasını geliştirdi. Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlendiğini (ve işlenmediğini) açıklar. **Apple App Review** ve kullanıcılar **bu sayfayı** herkese açık gizlilik politikası olarak kullanabilir. App Store Connect için tarayıcıda bu sayfayı açın ve adres çubuğundan URL’yi kopyalayın (genel site alan adı zamanla değişebilir).

## Özet (Apple Gizlilik Beslenme Etiketi uyumu)

| Konu | Uygulamamızın uygulaması |
|-------|----------------|
| Hesap | **Gerekli değil** — kayıt, e-posta ile giriş veya telefon numarası yok |
| iHTC Studio tarafından veri toplama | **Veri Toplanmıyor** — kişisel verilerinizi alan bir arka uç işletmiyoruz |
| Ağ | Kütüphane, reading, recite, Character Study, meditation, Life Guidance, widgets, and daily notifications work **offline** after install kurulumdan sonra **çevrimdışı** çalışır |
| Analitik / reklam / izleme | **Yok** — üçüncü taraf analitik, reklam veya izleme SDK'ları yok; Uygulama İzleme Şeffaflığı kullanılmaz |
| İsteğe bağlı Apple hizmetleri | **iCloud** (özel KVS'niz), paylaşım kartları için **Fotoğraf Kitaplığı (Only Add)**, isteğe bağlı bahşiş için **StoreKit**, **yerel bildirimler**, isteğe bağlı **Canlı Etkinlikler** |

## Veri Toplama

Kişisel bilgileri reklam veya analiz için **toplamıyoruz**, satmıyoruz veya paylaşmıyoruz.

- **Hesap gerekmez** — Tüm temel özellikleri bizde hesap oluşturmadan kullanabilirsiniz.
- **Analitik veya reklam yok** — Uygulama ikili dosyası üçüncü taraf analitik, reklam veya çökme bildirim SDK'larını içermez, telefonla bize veri göndermez.
- **İçerik yüklenmez** — reading history, favorites, study lists, reflection journal entries, habit check-ins, meditation streaks, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## Uygulama Nasıl Çalışır

- **Paketlenmiş kitaplık** — Metin JSON, vernacular/English, dizinler ve çalışma yardımcıları uygulama/widget paketinin içindedir. Gezinme ve çalışma için ağ gerekmez.
- **Cihaz içi konuşma** — Okuma, Apple'ın **AVSpeechSynthesizer** (TTS) sistemini kullanır. Bölüm metnini iHTC Studio'ya göndermiyoruz.
- **Widget'lar ve App Group** — Widget'lar ve uygulama, cihazınızdaki `group.com.iHTCboy.iPrimer` App Group'u üzerinden tercihleri ve hafif durumu paylaşır.
- **Günlük bildirimler** — Kullanıcı Bildirimleriyle yerel olarak planlanır. Bir bildirime dokunduğunuzda cihazdaki bölüm kimliğine giden derin bir bağlantı açılır; sunucu çıkışı yok.
- **Kartları paylaş** — Görüntüler cihazda oluşturulur. Kaydetme, **Yalnızca Fotoğraf Kitaplığı eklentisini** yalnızca kaydet'e dokunduğunuzda kullanır. Sistem Paylaşım Sayfası, görüntüyü **seçtiğiniz** bir uygulamaya gönderebilir; o hedefin gizlilik politikası geçerli olur.
- **İsteğe bağlı bahşiş** — “Tip Developer” (`com.iHTCboy.iPrimer.6`), Apple **StoreKit**.
- **Siri / Kısayollar / Kontrol Merkezi** — İsteğe bağlı sistem entegrasyonları cihazdaki derin bağlantıları açar; kütüphanenizi bize göndermiyorlar.
- **İsteğe Bağlı Spotlight** — Dizin oluşturmayı etkinleştirirseniz içerik, yerel arama için cihazdaki sistem tarafından dizine eklenir; bir arama arka ucu kullanmıyoruz.

## Cihazınızda Saklanan Veriler

| Veri | Nerede | Amaç |
|------|-------|-------------|
| Chapter veritabanı | App / Widget paketi | Çevrimdışı okuma ve çalışma |
| Favoriler ve çalışma listeleri | App Group UserDefaults | Yıldızlı eserler ve listeler |
| Okuma geçmişi / son okuma | Uygulama Grubu Kullanıcı Varsayılanları | Okumaya devam et, geçmiş kullanıcı arayüzü |
| Çalışma ilerlemesi ve ustalık | App Group UserDefaults | Character Study state, quiz / Hunt progress |
| Çalışma serisi / check-in | App Group UserDefaults | Daily Study alışkanlığı |
| Yansıma günlüğü | App Group UserDefaults | Life Guidance günlüğü |
| Alışkanlık check-in (洒扫应对) | App Group UserDefaults | Life Guidance alışkanlıkları |
| Meditasyon serisi ve oturum | App Group UserDefaults | Meditasyon sürekliliği |
| Paylaşım kartı tercihleri | App Group UserDefaults | Son stil / oran seçimleri |
| Daily Study cache & notification prefs | App Group UserDefaults | Bugünün ID’si, schedule time, contextual toggle |
| Paylaşımlı kart tercihleri ​​| Uygulama Grubu Kullanıcı Varsayılanları | Son stil/oran seçenekleri |
| İlk katılım ve TipKit durumu | Standart Kullanıcı Varsayılanları (cihaz) | Hoş geldiniz kılavuzu / keşif ipuçları |
| Ana Ekran hızlı eylemler | Sistem + yerel tercihler | Yapılandırdığınız kısayollar |
| Widget / Canlı Etkinlik anlık görüntüleri | Uygulama Grubu / ActivityKit | Daha önce açmış olduğunuz metni görüntüleyin |

Uygulamayı kaldırmak, uygulamayla ilişkili sandbox ve Uygulama Grubu verilerini kaldırır (iOS/macOS davranışına tabidir). İsteğe bağlı iCloud kopyaları, siz temizleyene veya senkronizasyonu kapatıp başka yerde silene kadar **iCloud’unuzda** kalır.

## iCloud Senkronizasyonu (İsteğe Bağlı)

Eğer Ayarlar’dan **iCloud Senkronizasyonu**’nu etkinleştirirseniz, uygulama seçili kullanıcı verilerini Apple’ın **`NSUbiquitousKeyValueStore`** aracılığıyla **Apple Kimliğinizle** eşler:

- Favoriler
- Çalışma listeleri
- Okuma geçmişi
- Çalışma ilerlemesi / ustalık
- Çalışma serileri
- Yansıma günlüğü
- Alışkanlık check-in geçmişi

Senkronizasyon trafiği **Apple iCloud**’a gider, iHTC Studio’ya değil. Ayarlardan senkronizasyonu devre dışı bırakabilirsiniz. iCloud içeriğinizi okuyamayız.

## İzinler

iLiezi yalnızca bir özellik ihtiyaç duyduğunda izin ister:

| İzin | Ne zaman | neden |
|------------|------|-----|
| Bildirimler | Daily Study or meditation reminders etkinleştirirsiniz | Yerel zamanlama |
## iCloud Senkronizasyonu (İsteğe Bağlı)
| iCloud | Senkronizasyonu açarsınız | Favoriler/listeler/geçmiş/ilerleme/seriler/günlük/alışkanlıklar |
| Live Activities (iOS) | Reading/Meditation Live Activity | Kilit Ekranı / Dynamic Island |
| Arka plan sesi | Arka planda okuma | Arka planda TTS |

Kişiler, kesin Konum, Kamera, Mikrofon (sistem TTS oynatmanın ötesinde) veya İzleme **talebi etmeyiz**.

## Çocukların Gizliliği

iPrimer **12+**, Kids Category **değil**. Çocuk verisi toplanmaz.

## Üçüncü Taraflar

Normal kullanımda üçüncü taraf yalnızca **Apple**.

## Veri Saklama ve Silme

- **Cihazda:** uygulamayı silmek sandbox ve App Group verisini kaldırır (sisteme bağlı).
- **iCloud:** Ayarlar’da senkronizasyonu kapatın; iCloud depolamayı sistem Ayarları’ndan yönetin.
- **Kopya tutmuyoruz** — okuma/günlük/alışkanlık verilerini iHTC Studio sunucularında.

## Bu Politika ile İlgili Değişiklikler

Yasal, ürün veya App Store uyumluluğu nedenleriyle bu sayfayı güncelleyebiliriz. 「Son güncelleme」 tarihi değişir. Güncellemeden sonra kullanıma devam etmek, revize edilmiş politikayı kabul ettiğiniz anlamına gelir.

## İletişim

Gizlilik ile ilgili sorular: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
