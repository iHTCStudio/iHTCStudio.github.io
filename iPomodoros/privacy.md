---
layout: doc
title: iPomodoro — Privacy Policy
app_id: iPomodoros
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iPomodoro — local-first timers, optional iCloud sync, widgets. No analytics.
---

<section lang="en" markdown="1">

iHTC Studio ("we", "us" or "our") built **iPomodoro** (also known as "爱番茄" / "愛番茄") as a productivity app for iPhone and iPad. This page explains how we handle information when you use the app.

## Summary

**iPomodoro does not collect, store, or transmit personal data to our servers.** Timers, study statistics, settings, and motivation content operate on your device. Optional **iCloud sync** for tasks and/or study statistics uses Apple CloudKit under your Apple ID — we do not run that cloud service.

## Data We Do Not Collect

- No name, email, phone number, or user account (unless you voluntarily email us for support).
- No usage analytics, crash reporting SDKs, or advertising identifiers.
- No location tracking.
- No upload of timer sessions or study statistics to **our servers** (optional iCloud sync stores data in your Apple iCloud account).
- Task lists are **not** uploaded to us — optional iCloud sync goes directly between your devices via Apple CloudKit when you enable it.

## Data Stored on Your Device

The following stays **locally** on your iPhone or iPad:

| Data | Storage | Purpose |
|------|---------|---------|
| Pomodoro & study timer settings | UserDefaults | Durations, sounds, themes, notification preferences, optional **Confirm phase completion** (Pomodoro) |
| Countdown tasks (title, date, notes, reminder flag, pin, order, **accent color**) | SQLite database | Task list, due-date reminders, widget colors |
| Study session history | SQLite database | Statistics tab (focus time, charts, task breakdown) |
| Statistics display preferences | UserDefaults | Default filters, **custom date range**, counting rules, Statistics tab theme colors |
| Focus goal & achievement preferences | UserDefaults | Daily/weekly goals, unlocked badges |
| Home Screen shortcut preferences | UserDefaults | Which Quick Actions appear when long-pressing the app icon (up to 4) |
| Focus Mode reminder toggles | UserDefaults | Optional prompt when starting a timer without Focus enabled |
| Daily motivation notification schedule | UserDefaults | Optional repeating local notification time |
| Stats today progress snapshot | App Group UserDefaults | Today's Stats widget |
| Motivation quote corpus (dialog/daily + notification) | App bundle JSON | On-device quote pools (**1000+** dialog/daily combined); notification pool is separate |
| Theme & language preferences | UserDefaults | Appearance and localization |
| Daily motivation quote index | App Group UserDefaults | Motivation widget & Live Activity hint sync |
| Motivation quote language filter | App Group UserDefaults | Widget quote pool matches in-app settings |
| Global theme mirror for widgets | App Group UserDefaults | Widget accent colors & optional gradient background |
| Pomodoro timer snapshot | App Group shared container | Pomodoro widget & Live Activity |
| Study timer snapshot | App Group shared container | Study Timer widget & Live Activity |
| Tasks widget snapshot | App Group shared container | Countdown Tasks widget |

This data is not accessible to us. Uninstalling the app removes local storage (except iOS system backups you may have enabled).

## Optional iCloud Sync (Tasks & Study Statistics)

**Tasks:** If you enable **Sync tasks with iCloud**, countdown tasks sync via CloudKit (`iCloud.com.iHTCboy.iPomodoros`).

**Study statistics:** If you enable **Sync study statistics with iCloud** (Statistics settings), focus session records sync as CloudKit records of type `StudySession` — including optional linked task title/id and a `cloudId` for merge. **Daily goal settings** (`StatsGoals`) and **achievement unlock/celebration state** (`StatsAchievements`) sync under the same toggle. Sync uses incremental CloudKit change tokens after the first full pull. This is **independent** from task sync.

In both cases data stays in **your private iCloud account** through Apple's infrastructure — not iHTC Studio servers. Disable either toggle anytime; local copies remain on each device.

## Notifications

If you grant notification permission, iPomodoro schedules **local notifications** on your device for:

- Timer completion and background study reminders (when enabled in settings) — message text is chosen from a bundled on-device notification quote pool; no network fetch
- **Daily motivation notification** (optional, Settings) — repeating local notification at your chosen time
- Task due-date reminders (when enabled per task)

These notifications are created and delivered by iOS on-device. We do not operate a push notification server or download quote text from our servers.

## App Group (Widgets & Live Activity)

The main app and Widget Extension share minimal timer, motivation, theme, **tasks**, and **today's stats progress** snapshots through Apple's App Group (`group.com.iHTCboy.iPomodoros`). Pomodoro and Study Timer use **separate** on-device snapshot keys so both widgets can coexist. This container stays on your device and is used only to display widgets and Live Activity — not for third-party access.

## In-App Purchase

An optional in-app support purchase is processed entirely by **Apple StoreKit**. We receive only standard App Store purchase receipts through Apple; we do not collect payment details directly.

## Third-Party Services

iPomodoro does **not** integrate third-party analytics, advertising, or social login SDKs.

When you tap **Feedback**, the app may open your mail client with a pre-filled template including device model and app version — you choose whether to send it.

## Children's Privacy

We do not knowingly collect personal information from children. Because we do not collect personal data through the app, no special child-directed provisions beyond standard App Store age ratings apply.

## Changes to This Policy

We may update this Privacy Policy from time to time. Changes will be posted on this page.

## Contact Us

Questions about privacy?

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="zh-CN" markdown="1">

爱火腿肠工作室（iHTC Studio）（「我们」）开发了 **爱番茄**（iPomodoro / 愛番茄），一款面向 iPhone 与 iPad 的效率应用。本页说明你在使用应用时，我们如何处理相关信息。

## 概要

**爱番茄不会向我们的服务器收集、存储或传输个人数据。** 计时、学习统计、设置与励志内容均在你的设备上运行。可选的 **iCloud 同步**（定任务与学习统计，独立开关）经 Apple CloudKit 在你的 Apple ID 设备间同步——不由我们运营云端服务。我们不要求爱番茄账号、不运行统计分析、不出售数据。

## 我们不收集的数据

- 不收集姓名、邮箱、电话或用户账号（除非你主动发邮件寻求支持）。
- 不使用使用统计、崩溃上报 SDK 或广告标识符。
- 不追踪位置。
- 不上传计时记录或学习统计到 **我们的服务器**（可选 iCloud 同步时数据存于你的 Apple iCloud 账户）。
- 任务列表 **不会** 上传给我们——仅在你开启时经 Apple CloudKit 在你的设备间同步。

## 存储在你设备上的数据

以下数据 **仅保存在** 你的 iPhone 或 iPad 本地：

| 数据 | 存储方式 | 用途 |
|------|---------|------|
| 番茄与计时设置 | UserDefaults | 时长、声音、主题、通知偏好、番茄可选 **阶段完成确认** |
| 倒数任务（标题、日期、备注、提醒、置顶、顺序、**accent 色**） | SQLite | 任务列表、到期提醒、Widget 配色 |
| 学习会话记录 | SQLite | 统计 Tab（专注时长、图表、按任务拆分） |
| 统计显示偏好 | UserDefaults | 默认筛选、**自定义日期范围**、计数规则、统计 Tab 页面主题色 |
| 专注目标与成就偏好 | UserDefaults | 日/周目标、已解锁成就 |
| 主屏快捷操作偏好 | UserDefaults | 长按图标显示的 Quick Actions（最多 4 项） |
| 专注模式联动开关 | UserDefaults | 开始计时时可选提醒开启系统 Focus |
| 每日励志通知时间 | UserDefaults | 可选 repeating 本地通知时刻 |
| 今日统计快照 | App Group UserDefaults | 今日统计小组件 |
| 励志语录语料（弹窗/每日 + 通知专用） | App 内置 JSON | 设备本地语录池（dialog/daily **1000+** 合计）；通知语料与弹窗/每日语料分开 |
| 主题与语言偏好 | UserDefaults | 外观与本地化 |
| 每日励志语录索引 | App Group UserDefaults | 励志小组件与 Live Activity hint 同步 |
| 励志语录语言筛选 | App Group UserDefaults | 小组件语录池与 App 内设置一致 |
| 全局主题镜像（小组件） | App Group UserDefaults | 小组件强调色与可选渐变背景 |
| 番茄钟计时快照 | App Group 共享容器 | 番茄钟小组件与 Live Activity |
| 学习计时快照 | App Group 共享容器 | 学习计时小组件与 Live Activity |
| 定任务快照 | App Group 共享容器 | 定任务小组件 |

我们无法访问这些数据。卸载应用会删除本地存储（你已启用的 iOS 系统备份除外）。

## 可选 iCloud 同步（定任务与学习统计）

**定任务：** 开启 **通过 iCloud 同步定任务** 后，经 CloudKit（`iCloud.com.iHTCboy.iPomodoros`）同步。

**学习统计：** 在统计设置中开启 **通过 iCloud 同步学习统计** 后，专注会话记录以 `StudySession` 类型同步（含可选关联任务信息与 `cloudId` 合并键）；**日/周目标**（`StatsGoals`）与 **成就解锁/庆祝状态**（`StatsAchievements`）在同一开关下同步；首次全量拉取后使用 CloudKit 增量 change token。与定任务同步 **独立开关**。

数据均存于 **你的私有 iCloud 账户**，经 Apple 基础设施传输——不经过 iHTC Studio 服务器。可随时关闭；各设备保留本地副本。

## 通知

若你授予通知权限，爱番茄会在设备上调度 **本地通知**，用于：

- 计时结束与后台学习提醒（在设置中开启时）——文案从内置 notification 语录池随机选取，不经网络拉取
- **每日励志通知**（可选，设置中开启）——在你选择的时间重复推送本地通知
- 任务到期提醒（按任务单独开启时）

通知由 iOS 在设备本地创建与投递，我们不运营推送服务器，也不会从我们的服务器下载语录。

## App Group（小组件与 Live Activity）

主应用与 Widget 扩展通过 Apple App Group（`group.com.iHTCboy.iPomodoros`）共享最小化的计时、励志、主题、**定任务**与**今日统计**快照。番茄钟与学习计时使用**独立**的设备内快照键。该容器留在设备上，仅用于展示小组件与 Live Activity——不用于第三方访问。

## 应用内购买

可选的应用内支持由 **Apple StoreKit** 完全处理。我们仅通过 Apple 收到标准 App Store 购买回执，不直接收集支付信息。

## 第三方服务

爱番茄 **不集成** 第三方统计、广告或社交登录 SDK。

点按 **反馈** 时，应用可能打开邮件客户端并预填设备型号与应用版本——是否发送由你决定。

## 儿童隐私

我们不会故意收集儿童个人信息。由于应用本身不收集个人数据，除 App Store 标准年龄分级外无额外儿童定向条款。

## 政策变更

我们可能不时更新本隐私政策，变更将发布于本页并更新日期。

## 联系我们

隐私相关问题？

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="zh-TW" markdown="1">

愛火腿腸工作室（iHTC Studio）（「我們」）開發了 **愛番茄**（iPomodoro / 爱番茄），一款面向 iPhone 與 iPad 的效率應用。本頁說明你在使用應用時，我們如何處理相關資訊。

## 概要

**愛番茄不會向我們的伺服器收集、儲存或傳輸個人資料。** 計時、學習統計、設定與勵志內容均在你的裝置上運行。可選的 **iCloud 同步**（定任務與學習統計，獨立開關）經 Apple CloudKit 在你的 Apple ID 裝置間同步——不由我們營運雲端服務。我們不要求愛番茄帳號、不執行統計分析、不出售資料。

## 我們不收集的資料

- 不收集姓名、電子郵件、電話或使用者帳號（除非你主動發郵件尋求支援）。
- 不使用使用統計、當機回報 SDK 或廣告識別碼。
- 不追蹤位置。
- 不上傳計時紀錄或學習統計到 **我們的伺服器**（可選 iCloud 同步時資料存於你的 Apple iCloud 帳戶）。
- 任務列表 **不會** 上傳給我們——僅在你開啟時經 Apple CloudKit 在你的裝置間同步。

## 儲存在你裝置上的資料

以下資料 **僅保存在** 你的 iPhone 或 iPad 本地：

| 資料 | 儲存方式 | 用途 |
|------|---------|------|
| 番茄與計時設定 | UserDefaults | 時長、聲音、主題、通知偏好、番茄可選 **階段完成確認** |
| 倒數任務（標題、日期、備註、提醒、置頂、順序、**accent 色**） | SQLite | 任務列表、到期提醒、Widget 配色 |
| 學習工作階段紀錄 | SQLite | 統計 Tab（專注時長、圖表、按任務拆分） |
| 統計顯示偏好 | UserDefaults | 預設篩選、**自訂日期範圍**、計數規則、統計 Tab 頁面主題色 |
| 專注目標與成就偏好 | UserDefaults | 日/週目標、已解鎖成就 |
| 主畫面快捷操作偏好 | UserDefaults | 長按圖示顯示的 Quick Actions（最多 4 項） |
| 專注模式聯動開關 | UserDefaults | 開始計時時可選提醒開啟系統 Focus |
| 每日勵志通知時間 | UserDefaults | 可選 repeating 本地通知時刻 |
| 今日統計快照 | App Group UserDefaults | 今日統計小工具 |
| 勵志語錄語料（彈窗/每日 + 通知專用） | App 內建 JSON | 裝置本地語錄池（dialog/daily **1000+** 合計）；通知語料與彈窗/每日語料分開 |
| 主題與語言偏好 | UserDefaults | 外觀與本地化 |
| 每日勵志語錄索引 | App Group UserDefaults | 勵志小工具與 Live Activity hint 同步 |
| 勵志語錄語言篩選 | App Group UserDefaults | 小工具語錄池與 App 內設定一致 |
| 全域主題鏡像（小工具） | App Group UserDefaults | 小工具強調色與可選漸層背景 |
| 番茄鐘計時快照 | App Group 共享容器 | 番茄鐘小工具與 Live Activity |
| 學習計時快照 | App Group 共享容器 | 學習計時小工具與 Live Activity |
| 定任務快照 | App Group 共享容器 | 定任務小工具 |

我們無法存取這些資料。解除安裝應用會刪除本地儲存（你已啟用的 iOS 系統備份除外）。

## 可選 iCloud 同步（定任務與學習統計）

**定任務：** 開啟 **透過 iCloud 同步定任務** 後，經 CloudKit（`iCloud.com.iHTCboy.iPomodoros`）同步。

**學習統計：** 在統計設定中開啟 **透過 iCloud 同步學習統計** 後，專注工作階段紀錄以 `StudySession` 類型同步（含可選關聯任務資訊與 `cloudId` 合併鍵）；**日/週目標**（`StatsGoals`）與 **成就解鎖/慶祝狀態**（`StatsAchievements`）在同一開關下同步；首次全量拉取後使用 CloudKit 增量 change token。與定任務同步 **獨立開關**。

資料均存於 **你的私有 iCloud 帳戶**，經 Apple 基礎設施傳輸——不經過 iHTC Studio 伺服器。可隨時關閉；各裝置保留本地副本。

## 通知

若你授予通知權限，愛番茄會在裝置上排程 **本地通知**，用於：

- 計時結束與背景學習提醒（在設定中開啟時）——文案從內建 notification 語錄池隨機選取，不經網路拉取
- **每日勵志通知**（可選，設定中開啟）——在你選擇的時間重複推送本地通知
- 任務到期提醒（按任務單獨開啟時）

通知由 iOS 在裝置本地建立與投遞，我們不營運推送伺服器，也不會從我們的伺服器下載語錄。

## App Group（小工具與 Live Activity）

主應用與 Widget 延伸功能透過 Apple App Group（`group.com.iHTCboy.iPomodoros`）共享最小化的計時、勵志、主題、**定任務**與**今日統計**快照。番茄鐘與學習計時使用**獨立**的裝置內快照鍵。該容器留在裝置上，僅用於展示小工具與 Live Activity——不用於第三方存取。

## 應用內購買

可選的應用內支持由 **Apple StoreKit** 完全處理。我們僅透過 Apple 收到標準 App Store 購買回執，不直接收集支付資訊。

## 第三方服務

愛番茄 **不整合** 第三方統計、廣告或社交登入 SDK。

點按 **回饋** 時，應用可能開啟郵件用戶端並預填裝置型號與應用版本——是否傳送由你決定。

## 兒童隱私

我們不會故意收集兒童個人資訊。由於應用本身不收集個人資料，除 App Store 標準年齡分級外無額外兒童定向條款。

## 政策變更

我們可能不時更新本隱私政策，變更將發布於本頁。

## 聯絡我們

隱私相關問題？

- **電子郵件：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ja" markdown="1">

iHTC Studio (「私たち」、「私たち」、または「私たちの」) は、iPhone および iPad 用の生産性向上アプリとして **iPomodoro** (「愛情番茄」 / 「愛番茄」としても知られています) を構築しました。 このページでは、アプリご利用時の情報の取り扱いについて説明します。 

## 概要

 **iPomodoro は、個人データを収集、保存、またはサーバーに送信しません。** タイマー、学習統計、設定、モチベーション コンテンツは、お使いのデバイス上で動作します。 タスクや学習統計のオプションの **iCloud 同期**では、Apple ID で Apple CloudKit が使用されます。当社はそのクラウド サービスを実行しません。 

## 当社が収集しないデータ

 - 名前、電子メール、電話番号、またはユーザー アカウントは不要です (サポートのために自発的に電子メールを送信した場合を除く)。 
- 使用状況分析、クラッシュレポート SDK、または広告識別子はありません。 
- 位置追跡はありません。 
- タイマー セッションや研究統計を **当社のサーバー**にアップロードすることはありません (オプションの iCloud 同期により、データが Apple iCloud アカウントに保存されます)。 
- タスクリストは私たちにアップロードされません** - オプションの iCloud 同期は、有効にすると Apple CloudKit 経由でデバイス間で直接行われます。 

## デバイスに保存されているデータ

 以下は iPhone または iPad 上に **ローカル** に残ります。

| データ | ストレージ | 目的 |
 |------|-----------|-----------|
 | ポモドーロと勉強タイマーの設定 | ユーザーデフォルト | 期間、サウンド、テーマ、通知設定、オプション **フェーズ完了の確認** (ポモドーロ) |
 | カウントダウン タスク (タイトル、日付、メモ、リマインダー フラグ、ピン、順序、**アクセント カラー**) | SQLite データベース | タスクリスト、期限リマインダー、ウィジェットの色 |
 | 勉強会の歴史 | SQLite データベース | [統計] タブ (集中時間、グラフ、タスクの内訳) |
 | 統計表示設定 | ユーザーデフォルト | デフォルトのフィルター、**カスタム日付範囲**、カウント ルール、[統計] タブのテーマの色 |
 | 目標と達成に焦点を当てる設定 | ユーザーデフォルト | 毎日/毎週の目標、ロック解除されたバッジ |
 | ホーム画面のショートカット設定 | ユーザーデフォルト | アプリアイコンを長押ししたときに表示されるクイックアクション（最大4つ） |
 | フォーカス モード リマインダーの切り替え | ユーザーデフォルト | フォーカスが有効になっていない状態でタイマーを開始するときのオプションのプロンプト |
 | 毎日のモチベーション通知スケジュール | ユーザーデフォルト | オプションの繰り返しローカル通知時間 |
 | 今日の統計進捗状況のスナップショット | アプリグループのUserDefaults | 今日の統計ウィジェット |
 | モチベーション引用コーパス (ダイアログ/毎日 + 通知) | アプリバンドル JSON | デバイス上の見積もりプール (**1000+** ダイアログ/毎日の合計)。 通知プールは別です |
 | テーマと言語の設定 | ユーザーデフォルト | 外観とローカリゼーション |
 | 毎日のモチベーション引用インデックス | アプリグループのUserDefaults | モチベーション ウィジェットとライブ アクティビティ ヒントの同期 |
 | モチベーション引用言語フィルター | アプリグループのUserDefaults | ウィジェットの引用プールがアプリ内設定と一致する |
 | ウィジェット用のグローバル テーマ ミラー | アプリグループのUserDefaults | ウィジェットのアクセントカラーとオプションのグラデーション背景 |
 | ポモドーロ タイマーのスナップショット | アプリグループ共有コンテナ | ポモドーロ ウィジェットとライブ アクティビティ |
 | 学習タイマーのスナップショット | アプリグループ共有コンテナ | 学習タイマー ウィジェットとライブ アクティビティ |
 | タスク ウィジェットのスナップショット | アプリグループ共有コンテナ | カウントダウン タスク ウィジェット |

このデータには当社はアクセスできません。 アプリをアンインストールすると、ローカル ストレージが削除されます (有効にした iOS システム バックアップを除く)。 

## オプションの iCloud 同期 (タスクと学習統計)

 **タスク:** **iCloud とタスクを同期** を有効にすると、カウントダウン タスクは CloudKit (`iCloud.com.iHTCboy.iPomodoros`) 経由で同期されます。 

**調査統計:** **調査統計を iCloud と同期する** (統計設定) を有効にすると、フォーカス セッション レコードはタイプ `StudySession` の CloudKit レコードとして同期されます (オプションのリンクされたタスク タイトル/ID とマージ用の `cloudId` を含みます)。 **毎日の目標設定** (`StatsGoals`) と **達成ロック解除/お祝い状態** (`StatsAchievements`) は、同じトグルで同期します。 同期では、最初の完全なプルの後、増分 CloudKit 変更トークンが使用されます。 これはタスク同期から**独立**しています。 

どちらの場合も、データは iHTC Studio サーバーではなく、Apple のインフラストラクチャを通じて **プライベート iCloud アカウント**に残ります。 どちらのトグルもいつでも無効にできます。 ローカル コピーは各デバイスに残ります。 

## 通知

 通知許可を与えると、iPomodoro はデバイス上で次の **ローカル通知**をスケジュールします。

- タイマー完了とバックグラウンドスタディリマインダー (設定で有効になっている場合) — メッセージテキストは、バンドルされているデバイス上の通知引用プールから選択されます。 ネットワークフェッチなし
 - **毎日のモチベーション通知** (オプション、設定) — 選択した時間にローカル通知を繰り返します
 - タスクの期日リマインダー (タスクごとに有効にした場合)

 これらの通知は、デバイス上の iOS によって作成および配信されます。 当社はプッシュ通知サーバーを運用したり、サーバーから引用テキストをダウンロードしたりすることはありません。 

## アプリ グループ (ウィジェットとライブ アクティビティ)

 メイン アプリとウィジェット拡張機能は、Apple のアプリ グループ (`group.com.iHTCboy.iPomodoros`) を通じて、最小限のタイマー、モチベーション、テーマ、**タスク**、**今日の統計の進捗状況**のスナップショットを共有します。 Pomodoro と Study Timer は**別々** のデバイス上のスナップショット キーを使用するため、両方のウィジェットを共存できます。 このコンテナはデバイス上に残り、ウィジェットとライブ アクティビティを表示するためにのみ使用され、サードパーティのアクセスには使用されません。 

## アプリ内購入

 オプションのアプリ内サポートの購入は、すべて **Apple StoreKit** によって処理されます。 Apple を通じて受け取るのは、標準の App Store 購入レシートのみです。 当社は支払いの詳細を直接収集しません。 

## サードパーティのサービス

iPomodoroは**サードパーティの分析、広告、またはソーシャルログインSDK**を統合していません。

**フィードバック**をタップすると、アプリはデバイスモデルやアプリのバージョンを含む事前入力されたテンプレートでメールクライアントを開く場合があります — 送信するかどうかはご自身で選択できます。

## 子どものプライバシー

私たちは、子どもから個人情報を故意に収集することはありません。アプリを通じて個人データを収集しないため、標準のApp Storeの年齢制限を超える特別な子ども向けの規定は適用されません。

## 本ポリシーの変更

このプライバシーポリシーは随時更新されることがあります。変更はこのページに掲載されます。

## お問い合わせ

プライバシーについてのご質問は？

- **メール:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ko" markdown="1">

iHTC Studio("당사", "우리" 또는 "우리")는 iPhone 및 iPad용 생산성 앱으로 **iPomodoro**("爱番茄" / "愛番茄"라고도 함)를 구축했습니다. 이 페이지에서는 귀하가 앱을 사용할 때 당사가 정보를 처리하는 방법을 설명합니다. 

## 요약 

**iPomodoro는 개인 데이터를 수집, 저장 또는 당사 서버로 전송하지 않습니다.** 타이머, 학습 통계, 설정 및 동기 부여 콘텐츠가 귀하의 장치에서 작동합니다. 작업 및/또는 연구 통계를 위한 선택적 **iCloud 동기화**는 귀하의 Apple ID로 Apple CloudKit을 사용합니다. 당사는 해당 클라우드 서비스를 실행하지 않습니다. 

## 수집하지 않는 데이터 

- 이름, 이메일, 전화번호 또는 사용자 계정이 없습니다(지원을 위해 자발적으로 이메일을 보내지 않는 한). 
- 사용 분석, 충돌 보고 SDK 또는 광고 식별자가 없습니다. 
- 위치 추적이 되지 않습니다. 
- 타이머 세션이나 연구 통계를 **당사 서버**에 업로드하지 않습니다(옵션인 iCloud 동기화는 Apple iCloud 계정에 데이터를 저장합니다). 
- 작업 목록은 우리에게 업로드되지 **않습니다**. 옵션인 iCloud 동기화는 활성화하면 Apple CloudKit을 통해 장치 간에 직접 이동됩니다. 

## 귀하의 기기에 저장된 데이터 

다음은 iPhone 또는 iPad에 **로컬로** 유지됩니다.

| 데이터 | 저장 | 목적 | 
|------|---------|---------| 
| 뽀모도로 & 공부 타이머 설정 | 사용자 기본값 | 기간, 소리, 테마, 알림 기본 설정, 선택 사항 **단계 완료 확인**(Pomodoro) | 
| 카운트다운 작업(제목, 날짜, 메모, 알림 플래그, 핀, 순서, **악센트 색상**) | SQLite 데이터베이스 | 작업 목록, 마감일 알림, 위젯 색상 | 
| 학습 세션 내역 | SQLite 데이터베이스 | 통계 탭(집중 시간, 차트, 작업 분석) | 
| 통계 표시 기본 설정 | 사용자 기본값 | 기본 필터, **맞춤 기간**, 계산 규칙, 통계 탭 테마 색상 | 
| 집중 목표 및 성과 선호도 | 사용자 기본값 | 일일/주간 목표, 배지 잠금 해제 | 
| 홈 화면 바로가기 환경설정 | 사용자 기본값 | 앱 아이콘을 길게 누르면 나타나는 빠른 작업(최대 4개) | 
| 집중 모드 알림 토글 | 사용자 기본값 | 포커스가 활성화되지 않은 상태에서 타이머를 시작할 때의 선택적 프롬프트 | 
| 일일 동기 부여 알림 일정 | 사용자 기본값 | 선택적 반복 지역 알림 시간 | 
| 오늘의 통계 진행 상황 스냅샷 | 앱 그룹 UserDefaults | 오늘의 통계 위젯 | 
| 동기부여 명언 말뭉치(대화/일일+알림) | 앱 번들 JSON | 온디바이스 견적 풀(**1000+** 대화 상자/일일 결합); 알림 풀은 별도입니다 | 
| 테마 및 언어 환경설정 | 사용자 기본값 | 외관 및 현지화 | 
| 일일 동기 부여 인용 지수 | 앱 그룹 UserDefaults | 동기 부여 위젯 및 실시간 활동 힌트 동기화 | 
| 동기 부여 인용 언어 필터 | 앱 그룹 UserDefaults | 위젯 견적 풀이 인앱 설정과 일치합니다 | 
| 위젯용 글로벌 테마 미러 | 앱 그룹 UserDefaults | 위젯 강조 색상 및 선택적 그라데이션 배경 | 
| 뽀모도로 타이머 스냅샷 | 앱 그룹 공유 컨테이너 | Pomodoro 위젯 및 라이브 활동 | 
| 공부 타이머 스냅샷 | 앱 그룹 공유 컨테이너 | 학습 타이머 위젯 및 실시간 활동 | 
| 작업 위젯 스냅샷 | 앱 그룹 공유 컨테이너 | 카운트다운 작업 위젯 |

이 데이터는 우리가 접근할 수 없습니다. 앱을 제거하면 로컬 저장소가 제거됩니다(활성화한 iOS 시스템 백업 제외). 

## iCloud 동기화 옵션(과제 및 학습 통계) 

**작업:** **iCloud와 작업 동기화**를 활성화하면 카운트다운 작업이 CloudKit(`iCloud.com.iHTCboy.iPomodoros`)을 통해 동기화됩니다. 

**연구 통계:** **iCloud와 연구 통계 동기화**(통계 설정)를 활성화하면 포커스 세션 기록은 선택적으로 연결된 작업 제목/ID 및 병합을 위한 `cloudId`을 포함하여 `StudySession` 유형의 CloudKit 기록으로 동기화됩니다. **일일 목표 설정**(`StatsGoals`) 및 **성취 잠금 해제/축하 상태**(`StatsAchievements`)는 동일한 토글에서 동기화됩니다. 동기화는 첫 번째 전체 가져오기 이후 증분 CloudKit 변경 토큰을 사용합니다. 이는 작업 동기화와 **독립적**입니다. 

두 경우 모두 데이터는 iHTC Studio 서버가 아닌 Apple 인프라를 통해 **개인 iCloud 계정**에 유지됩니다. 언제든지 토글을 비활성화하십시오. 로컬 복사본은 각 장치에 남아 있습니다. 

## 알림 

알림 권한을 부여하면 iPomodoro는 기기에서 다음에 대한 **로컬 알림**을 예약합니다.

- 타이머 완료 및 배경 연구 알림(설정에서 활성화된 경우) — 메시지 텍스트는 번들로 제공되는 기기 내 알림 견적 풀에서 선택됩니다. 네트워크 가져오기 없음 
- **매일 동기부여 알림** (선택, 설정) — 선택한 시간에 지역 알림 반복 
- 작업 마감일 알림(작업별로 활성화된 경우) 

이러한 알림은 iOS 기기에서 생성되고 전달됩니다. 우리는 푸시 알림 서버를 운영하거나 서버에서 인용문을 다운로드하지 않습니다. 

## 앱 그룹(위젯 및 실시간 활동) 

메인 앱과 위젯 확장은 Apple 앱 그룹(`group.com.iHTCboy.iPomodoros`)을 통해 최소한의 타이머, 동기 부여, 테마, **작업** 및 **오늘의 통계 진행** 스냅샷을 공유합니다. Pomodoro와 Study Timer는 **별도** 온디바이스 스냅샷 키를 사용하므로 두 위젯이 공존할 수 있습니다. 이 컨테이너는 장치에 유지되며 위젯과 실시간 활동을 표시하는 데만 사용되며 제3자 액세스에는 사용되지 않습니다. 

## 인앱 구매 

선택적 인앱 지원 구매는 전적으로 **Apple StoreKit**에 의해 처리됩니다. 우리는 Apple을 통해 표준 App Store 구매 영수증만 받습니다. 우리는 결제 세부정보를 직접 수집하지 않습니다. 

## 타사 서비스

iPomodoro는 서드파티 분석, 광고 또는 소셜 로그인 SDK를 **통합하지 않습니다**.

**피드백**을 탭할 때, 앱이 장치 모델과 앱 버전을 포함한 미리 채워진 템플릿과 함께 메일 클라이언트를 열 수 있으며 — 보내는 것은 사용자의 선택입니다.

## 아동 개인정보

우리는 아동으로부터 개인 정보를 의도적으로 수집하지 않습니다. 앱을 통해 개인 데이터를 수집하지 않기 때문에, 표준 App Store 연령 등급을 제외한 특별한 아동 대상 조항은 적용되지 않습니다.

## 본 정책의 변경

우리는 이 개인정보 보호정책을 수시로 업데이트할 수 있습니다. 변경 사항은 이 페이지에 게시됩니다.

## 문의하기

개인정보 관련 질문이 있나요?

- **이메일:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ru" markdown="1">

iHTC Studio («мы», «нас» или «наш») создала **iPomodoro** (также известное как «爱番茄» / «愛番茄») как приложение для повышения производительности для iPhone и iPad. На этой странице объясняется, как мы обрабатываем информацию, когда вы используете приложение. 

## Резюме 

**iPomodoro не собирает, не хранит и не передает персональные данные на наши серверы.** Таймеры, статистика занятий, настройки и мотивационный контент работают на вашем устройстве. Дополнительная **синхронизация с iCloud** для задач и/или статистики исследования использует Apple CloudKit под вашим Apple ID — мы не запускаем этот облачный сервис. 

## Данные, которые мы не собираем 

- Никакого имени, адреса электронной почты, номера телефона или учетной записи пользователя (если вы добровольно не напишите нам для получения поддержки). 
- Никакой аналитики использования, SDK для отчетов о сбоях или рекламных идентификаторов. 
- Нет отслеживания местоположения. 
- Никакой загрузки сеансов таймера или статистики обучения на **наши серверы** (дополнительная синхронизация iCloud сохраняет данные в вашей учетной записи Apple iCloud). 
- Списки задач **не** загружаются к нам — дополнительная синхронизация iCloud осуществляется напрямую между вашими устройствами через Apple CloudKit, когда вы ее включаете. 

## Данные, хранящиеся на вашем устройстве 

Следующие данные остаются **локально** на вашем iPhone или iPad:

| Данные | Хранение | Цель | 
|------|---------|---------| 
| Помидор и настройки таймера исследования | Пользовательские настройки по умолчанию | Длительность, звуки, темы, настройки уведомлений, необязательно **Подтвердить завершение этапа** (Pomodoro) | 
| Задачи обратного отсчета (название, дата, примечания, флажок напоминания, булавка, порядок, **цвет акцента**) | База данных SQLite | Список задач, напоминания о сроках выполнения, цвета виджетов | 
| История занятий | База данных SQLite | Вкладка «Статистика» (время фокусировки, графики, разбивка задач) | 
| Настройки отображения статистики | Пользовательские настройки по умолчанию | Фильтры по умолчанию, **настраиваемый диапазон дат**, правила подсчета, цвета темы вкладки «Статистика» | 
| Сфокусируйтесь на целях и достижениях | Пользовательские настройки по умолчанию | Ежедневные/еженедельные цели, разблокированные значки | 
| Настройки ярлыков на главном экране | Пользовательские настройки по умолчанию | Какие быстрые действия появляются при длительном нажатии на значок приложения (до 4) | 
| Переключение напоминаний о режиме фокусировки | Пользовательские настройки по умолчанию | Дополнительный запрос при запуске таймера без включенного фокуса | 
| График ежедневных уведомлений о мотивации | Пользовательские настройки по умолчанию | Дополнительное повторяющееся время локального уведомления | 
| Статистика сегодня, снимок прогресса | Пользовательские настройки группы приложений | Виджет сегодняшней статистики | 
| Корпус мотивационных цитат (диалог/ежедневно + уведомление) | Пакет приложений JSON | Пулы котировок на устройстве (**1000+** диалогов/ежедневно вместе взятые); пул уведомлений отдельный | 
| Тематические и языковые настройки | Пользовательские настройки по умолчанию | Внешний вид и локализация | 
| Ежедневный индекс котировок мотивации | Пользовательские настройки группы приложений | Виджет мотивации и синхронизация подсказок Live Activity | 
| Языковой фильтр мотивационных цитат | Пользовательские настройки группы приложений | Пул котировок виджета соответствует настройкам в приложении | 
| Глобальное зеркало темы для виджетов | Пользовательские настройки группы приложений | Акцентные цвета виджета и дополнительный градиентный фон | 
| Снимок таймера Pomodoro | Общий контейнер группы приложений | Виджет Pomodoro и живая активность | 
| Снимок таймера исследования | Общий контейнер группы приложений | Виджет «Таймер обучения» и живая активность | 
| Снимок виджета задач | Общий контейнер группы приложений | Виджет задач обратного отсчета |

Эти данные нам недоступны. При удалении приложения удаляется локальное хранилище (за исключением резервных копий системы iOS, которые вы, возможно, включили). 

## Дополнительная синхронизация iCloud (задачи и статистика исследования) 

**Задачи.** Если вы включите **Синхронизировать задачи с iCloud**, задачи обратного отсчета синхронизируются через CloudKit (`iCloud.com.iHTCboy.iPomodoros`). 

**Статистика исследования.** Если вы включите **Синхронизировать статистику исследования с iCloud** (настройки статистики), записи сеанса фокусировки синхронизируются как записи CloudKit типа `StudySession`, включая необязательное название/идентификатор связанной задачи и `cloudId` для слияния. **Настройки ежедневных целей** (`StatsGoals`) и **состояние разблокировки/празднования достижения** (`StatsAchievements`) синхронизируются под одним переключателем. Синхронизация использует дополнительные токены изменений CloudKit после первого полного получения. Это **независимо** от синхронизации задач. 

В обоих случаях данные остаются в **вашей личной учетной записи iCloud** через инфраструктуру Apple, а не на серверах iHTC Studio. Отключите любой переключатель в любое время; локальные копии остаются на каждом устройстве. 

## Уведомления 

Если вы дадите разрешение на уведомления, iPomodoro запланирует **локальные уведомления** на вашем устройстве для:

- Напоминания о завершении таймера и фоновых исследованиях (если они включены в настройках) — текст сообщения выбирается из встроенного пула котировок уведомлений на устройстве; нет загрузки по сети 
- **Ежедневное уведомление о мотивации** (опционально, Настройки) — повторение локального уведомления в выбранное вами время. 
- Напоминания о сроках выполнения задач (если они включены для каждой задачи) 

Эти уведомления создаются и доставляются iOS на устройство. Мы не используем сервер push-уведомлений и не загружаем текст котировок с наших серверов. 

## Группа приложений (Виджеты и интерактивная активность) 

Основное приложение и расширение виджета используют общие снимки минимального таймера, мотивации, темы, **задач** и **сегодняшней статистики** через группу приложений Apple (`group.com.iHTCboy.iPomodoros`). Pomodoro и Study Timer используют **отдельные** ключи снимков на устройстве, поэтому оба виджета могут сосуществовать. Этот контейнер остается на вашем устройстве и используется только для отображения виджетов и активности в реальном времени, а не для доступа третьих лиц. 

## Покупка в приложении 

Дополнительная покупка поддержки в приложении полностью обрабатывается **Apple StoreKit**. Через Apple мы получаем только стандартные квитанции о покупках в App Store; мы не собираем платежные реквизиты напрямую. 

## Сторонние сервисы

iPomodoro **не** интегрирует сторонние SDK для аналитики, рекламы или входа через социальные сети.

Когда вы нажимаете **Обратная связь**, приложение может открыть ваш почтовый клиент с заранее заполненным шаблоном, включающим модель устройства и версию приложения — вы сами решаете, отправлять его или нет.

## Конфиденциальность детей

Мы сознательно не собираем личную информацию о детях. Поскольку мы не собираем персональные данные через приложение, никаких специальных положений, направленных на детей, кроме стандартных возрастных ограничений App Store, не применяется.

## Изменения в данной политике

Мы можем время от времени обновлять настоящую Политику конфиденциальности. Изменения будут публиковаться на этой странице.

## Связаться с нами

Вопросы о конфиденциальности?

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="th" markdown="1">

iHTC Studio ("เรา", "พวกเรา" หรือ "ของเรา") ได้สร้าง **iPomodoro** (หรือที่รู้จักในชื่อ "爱番茄" / "愛番茄") ให้เป็นแอปเพิ่มประสิทธิภาพการทำงานสำหรับ iPhone และ iPad หน้านี้อธิบายวิธีที่เราจัดการข้อมูลเมื่อคุณใช้แอป 

## สรุป 

**iPomodoro ไม่รวบรวม จัดเก็บ หรือส่งข้อมูลส่วนบุคคลไปยังเซิร์ฟเวอร์ของเรา** ตัวจับเวลา สถิติการศึกษา การตั้งค่า และเนื้อหาแรงจูงใจทำงานบนอุปกรณ์ของคุณ **ตัวเลือกการซิงค์ iCloud** สำหรับงานและ/หรือสถิติการศึกษาใช้ Apple CloudKit ภายใต้ Apple ID ของคุณ เราไม่ได้ใช้บริการคลาวด์นั้น 

## ข้อมูลที่เราไม่รวบรวม 

- ไม่มีชื่อ อีเมล หมายเลขโทรศัพท์ หรือบัญชีผู้ใช้ (เว้นแต่คุณจะส่งอีเมลถึงเราด้วยความสมัครใจเพื่อขอความช่วยเหลือ) 
- ไม่มีการวิเคราะห์การใช้งาน SDK รายงานข้อขัดข้อง หรือตัวระบุโฆษณา 
- ไม่มีการติดตามตำแหน่ง 
- ไม่มีการอัปโหลดเซสชันตัวจับเวลาหรือศึกษาสถิติไปยัง **เซิร์ฟเวอร์ของเรา** (ตัวเลือกการซิงค์ iCloud จะจัดเก็บข้อมูลในบัญชี Apple iCloud ของคุณ) 
- รายการงาน **ไม่ได้** อัปโหลดถึงเรา — ตัวเลือกการซิงค์ iCloud จะไประหว่างอุปกรณ์ของคุณโดยตรงผ่าน Apple CloudKit เมื่อคุณเปิดใช้งาน 

## ข้อมูลที่จัดเก็บไว้ในอุปกรณ์ของคุณ 

สิ่งต่อไปนี้จะคงอยู่**ในเครื่อง** บน iPhone หรือ iPad ของคุณ:

| ข้อมูล | พื้นที่เก็บข้อมูล | วัตถุประสงค์ | 
|------|---------|---------| 
| Pomodoro และการตั้งค่าตัวจับเวลาการศึกษา | ค่าเริ่มต้นของผู้ใช้ | ระยะเวลา เสียง ธีม การตั้งค่าการแจ้งเตือน ตัวเลือก **ยืนยันการเสร็จสิ้นเฟส** (Pomodoro) | 
| งานนับถอยหลัง (ชื่อ, วันที่, บันทึกย่อ, ธงเตือนความจำ, หมุด, ลำดับ, **สีเน้นเสียง**) | ฐานข้อมูล SQLite | รายการงาน, การแจ้งเตือนวันครบกำหนด, สีวิดเจ็ต | 
| ประวัติช่วงการศึกษา | ฐานข้อมูล SQLite | แท็บสถิติ (เวลาโฟกัส แผนภูมิ การแยกย่อยงาน) | 
| การตั้งค่าการแสดงสถิติ | ค่าเริ่มต้นของผู้ใช้ | ตัวกรองเริ่มต้น **ช่วงวันที่ที่กำหนดเอง** กฎการนับ สีของธีมแท็บสถิติ | 
| มุ่งเน้นเป้าหมายและการตั้งค่าความสำเร็จ | ค่าเริ่มต้นของผู้ใช้ | เป้าหมายรายวัน/รายสัปดาห์ ปลดล็อคตราสัญลักษณ์ | 
| การตั้งค่าทางลัดบนหน้าจอหลัก | ค่าเริ่มต้นของผู้ใช้ | การดำเนินการด่วนใดจะปรากฏขึ้นเมื่อกดไอคอนแอปค้างไว้ (สูงสุด 4) | 
| สลับการแจ้งเตือนโหมดโฟกัส | ค่าเริ่มต้นของผู้ใช้ | พรอมต์เสริมเมื่อเริ่มจับเวลาโดยไม่เปิดใช้งานโฟกัส | 
| ตารางการแจ้งเตือนแรงจูงใจรายวัน | ค่าเริ่มต้นของผู้ใช้ | ตัวเลือกเวลาแจ้งเตือนท้องถิ่นซ้ำ | 
| สถิติวันนี้ ภาพรวมความคืบหน้า | ค่าเริ่มต้นของกลุ่มแอป | วิดเจ็ตสถิติวันนี้ | 
| คลังคำพูดแรงจูงใจ (โต้ตอบ/รายวัน + การแจ้งเตือน) | ชุดแอป JSON | กลุ่มใบเสนอราคาบนอุปกรณ์ (** กล่องโต้ตอบ 1,000+** / รวมรายวัน) กลุ่มการแจ้งเตือนแยกจากกัน | 
| การตั้งค่าธีมและภาษา | ค่าเริ่มต้นของผู้ใช้ | ลักษณะที่ปรากฏและการแปล | 
| ดัชนีคำพูดแรงจูงใจรายวัน | ค่าเริ่มต้นของกลุ่มแอป | วิดเจ็ตแรงจูงใจ & การซิงค์คำใบ้กิจกรรมสด | 
| ตัวกรองภาษาคำพูดแรงจูงใจ | ค่าเริ่มต้นของกลุ่มแอป | กลุ่มใบเสนอราคาวิดเจ็ตตรงกับการตั้งค่าในแอป | 
| มิเรอร์ธีมสากลสำหรับวิดเจ็ต | ค่าเริ่มต้นของกลุ่มแอป | สีเน้นวิดเจ็ต & พื้นหลังไล่ระดับสีเสริม | 
| ภาพรวมตัวจับเวลา Pomodoro | คอนเทนเนอร์ที่ใช้ร่วมกันของกลุ่มแอป | วิดเจ็ต Pomodoro & กิจกรรมสด | 
| ศึกษาภาพรวมตัวจับเวลา | คอนเทนเนอร์ที่ใช้ร่วมกันของกลุ่มแอป | วิดเจ็ตตัวจับเวลาการศึกษา & กิจกรรมสด | 
| สแนปชอตวิดเจ็ตงาน | คอนเทนเนอร์ที่ใช้ร่วมกันของกลุ่มแอป | วิดเจ็ตงานนับถอยหลัง |

เราไม่สามารถเข้าถึงข้อมูลนี้ได้ การถอนการติดตั้งแอปจะเป็นการลบที่เก็บข้อมูลในตัวเครื่อง (ยกเว้นการสำรองข้อมูลระบบ iOS ที่คุณอาจเปิดใช้งานไว้) 

## ตัวเลือก iCloud Sync (สถิติงานและการศึกษา) 

**งาน:** หากคุณเปิดใช้งาน **ซิงค์งานกับ iCloud** งานนับถอยหลังจะซิงค์ผ่าน CloudKit (`iCloud.com.iHTCboy.iPomodoros`) 

**สถิติการศึกษา:** หากคุณเปิดใช้งาน **ซิงค์สถิติการศึกษากับ iCloud** (การตั้งค่าสถิติ) บันทึกเซสชันโฟกัสจะซิงค์เป็นบันทึก CloudKit ประเภท `StudySession` — รวมถึงชื่อ/id งานที่เชื่อมโยงซึ่งเป็นทางเลือก และ `cloudId` สำหรับการผสาน **การตั้งค่าเป้าหมายรายวัน** (`StatsGoals`) และ **สถานะการปลดล็อก/การเฉลิมฉลองความสำเร็จ** (`StatsAchievements`) ซิงค์ภายใต้การสลับเดียวกัน การซิงค์ใช้โทเค็นการเปลี่ยนแปลง CloudKit แบบเพิ่มหน่วยหลังจากการดึงแบบเต็มครั้งแรก นี่คือ **อิสระ** จากการซิงค์งาน 

ในทั้งสองกรณี ข้อมูลจะยังคงอยู่ใน **บัญชี iCloud ส่วนตัวของคุณ** ผ่านทางโครงสร้างพื้นฐานของ Apple ไม่ใช่เซิร์ฟเวอร์ iHTC Studio ปิดการใช้งานสลับได้ตลอดเวลา สำเนาในเครื่องจะยังคงอยู่ในแต่ละอุปกรณ์ 

## การแจ้งเตือน 

หากคุณให้สิทธิ์ในการแจ้งเตือน iPomodoro จะกำหนดเวลา **การแจ้งเตือนในท้องถิ่น** บนอุปกรณ์ของคุณสำหรับ:

- ตัวจับเวลาเสร็จสิ้นและตัวเตือนการศึกษาภูมิหลัง (เมื่อเปิดใช้งานในการตั้งค่า) — ข้อความถูกเลือกจากกลุ่มใบเสนอราคาการแจ้งเตือนบนอุปกรณ์ ไม่มีการดึงข้อมูลจากเครือข่าย 
- **การแจ้งเตือนแรงจูงใจรายวัน** (ไม่บังคับ การตั้งค่า) — แจ้งเตือนในท้องถิ่นซ้ำตามเวลาที่คุณเลือก 
- การแจ้งเตือนวันครบกำหนดงาน (เมื่อเปิดใช้งานต่องาน) 

การแจ้งเตือนเหล่านี้สร้างและส่งโดย iOS บนอุปกรณ์ เราไม่ได้ดำเนินการเซิร์ฟเวอร์การแจ้งเตือนแบบพุชหรือดาวน์โหลดข้อความอ้างอิงจากเซิร์ฟเวอร์ของเรา 

## กลุ่มแอป (วิดเจ็ต & กิจกรรมสด) 

แอปหลักและส่วนขยายวิดเจ็ตแชร์ตัวจับเวลาขั้นต่ำ แรงจูงใจ ธีม **งาน** และ **ภาพรวมสถิติของวันนี้** ผ่านกลุ่มแอปของ Apple (`group.com.iHTCboy.iPomodoros`) Pomodoro และ Study Timer ใช้คีย์สแนปชอต **แยกกัน** บนอุปกรณ์เพื่อให้วิดเจ็ตทั้งสองอยู่ร่วมกันได้ คอนเทนเนอร์นี้จะคงอยู่ในอุปกรณ์ของคุณและใช้เพื่อแสดงวิดเจ็ตและกิจกรรมสดเท่านั้น — ไม่ใช่สำหรับการเข้าถึงของบุคคลที่สาม 

## การซื้อในแอป 

การซื้อการสนับสนุนในแอปเสริมจะได้รับการประมวลผลโดย **Apple StoreKit** ทั้งหมด เราได้รับเฉพาะใบเสร็จการซื้อ App Store มาตรฐานผ่านทาง Apple เท่านั้น เราไม่รวบรวมรายละเอียดการชำระเงินโดยตรง 

## บริการของบุคคลที่สาม

iPomodoro **ไม่** มีการรวมตัว SDK ของการวิเคราะห์ของบุคคลที่สาม การโฆษณา หรือการเข้าสู่ระบบโซเชียลใดๆ

เมื่อคุณแตะ **Feedback** แอปอาจเปิดโปรแกรมจดหมายของคุณพร้อมเทมเพลตที่กรอกข้อมูลไว้ล่วงหน้า รวมถึงรุ่นอุปกรณ์และเวอร์ชันของแอป — คุณเป็นผู้เลือกว่าจะส่งหรือไม่

## ความเป็นส่วนตัวของเด็ก

เราไม่ได้เก็บรวบรวมข้อมูลส่วนบุคคลจากเด็กโดยรู้ตัว เนื่องจากเราไม่ได้เก็บข้อมูลส่วนบุคคลผ่านแอป ไม่มีข้อกำหนดพิเศษสำหรับเด็กนอกเหนือจากการจัดอันดับอายุมาตรฐานของ App Store

## การเปลี่ยนแปลงนโยบายนี้

เราอาจอัปเดตนโยบายความเป็นส่วนตัวนี้เป็นครั้งคราว การเปลี่ยนแปลงจะถูกโพสต์ในหน้านี้

## ติดต่อเรา

มีคำถามเกี่ยวกับความเป็นส่วนตัวหรือไม่?

- **อีเมล:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="de" markdown="1">

iHTC Studio („wir“, „uns“ oder „unser“) hat **iPomodoro** (auch bekannt als „爱番茄“ / „愛番茄“) als Produktivitäts-App für iPhone und iPad entwickelt. Auf dieser Seite wird erläutert, wie wir mit Informationen umgehen, wenn Sie die App nutzen. 

## Zusammenfassung 

**iPomodoro erhebt, speichert oder übermittelt keine personenbezogenen Daten an unsere Server.** Timer, Lernstatistiken, Einstellungen und Motivationsinhalte funktionieren auf Ihrem Gerät. Die optionale **iCloud-Synchronisierung** für Aufgaben und/oder Studienstatistiken nutzt Apple CloudKit unter Ihrer Apple-ID – wir betreiben diesen Cloud-Dienst nicht. 

## Daten, die wir nicht sammeln 

- Kein Name, keine E-Mail-Adresse, keine Telefonnummer oder kein Benutzerkonto (es sei denn, Sie senden uns freiwillig eine E-Mail für den Support). 
- Keine Nutzungsanalysen, Absturzberichts-SDKs oder Werbekennungen. 
- Keine Standortverfolgung. 
- Kein Hochladen von Timer-Sitzungen oder Studienstatistiken auf **unsere Server** (optionale iCloud-Synchronisierung speichert Daten in Ihrem Apple iCloud-Konto). 
- Aufgabenlisten werden **nicht** auf uns hochgeladen – die optionale iCloud-Synchronisierung erfolgt direkt zwischen Ihren Geräten über Apple CloudKit, wenn Sie sie aktivieren. 

## Auf Ihrem Gerät gespeicherte Daten 

Folgendes bleibt **lokal** auf Ihrem iPhone oder iPad:

| Daten | Lagerung | Zweck | 
|------|---------|---------| 
| Pomodoro- und Lerntimer-Einstellungen | Benutzerstandards | Dauer, Töne, Themen, Benachrichtigungseinstellungen, optional **Phasenabschluss bestätigen** (Pomodoro) | 
| Countdown-Aufgaben (Titel, Datum, Notizen, Erinnerungsflagge, Pin, Reihenfolge, **Akzentfarbe**) | SQLite-Datenbank | Aufgabenliste, Fälligkeitserinnerungen, Widget-Farben | 
| Geschichte der Studiensitzung | SQLite-Datenbank | Registerkarte „Statistik“ (Fokuszeit, Diagramme, Aufgabenaufschlüsselung) | 
| Einstellungen für die Statistikanzeige | Benutzerstandards | Standardfilter, **benutzerdefinierter Datumsbereich**, Zählregeln, Themenfarben für die Registerkarte „Statistik“ | 
| Ziel- und Leistungspräferenzen fokussieren | Benutzerstandards | Tägliche/wöchentliche Ziele, freigeschaltete Abzeichen | 
| Startbildschirm-Verknüpfungseinstellungen | Benutzerstandards | Welche Schnellaktionen erscheinen, wenn Sie lange auf das App-Symbol drücken (bis zu 4) | 
| Fokusmodus-Erinnerung schaltet um | Benutzerstandards | Optionale Eingabeaufforderung beim Starten eines Timers ohne aktivierten Fokus | 
| Täglicher Motivationsbenachrichtigungsplan | Benutzerstandards | Optionale wiederholte lokale Benachrichtigungszeit | 
| Statistiken heute Fortschrittsschnappschuss | Benutzerstandards der App-Gruppe | Heutiges Statistik-Widget | 
| Korpus Motivationszitate (Dialog/Täglich + Benachrichtigung) | App-Bundle JSON | Angebotspools auf dem Gerät (**1000+** Dialoge/Tag kombiniert); Benachrichtigungspool ist separat | 
| Themen- und Spracheinstellungen | Benutzerstandards | Aussehen und Lokalisierung | 
| Index der täglichen Motivationszitate | Benutzerstandards der App-Gruppe | Motivations-Widget und Live-Aktivitätshinweis-Synchronisierung | 
| Sprachfilter für Motivationszitat | Benutzerstandards der App-Gruppe | Widget-Zitatpool entspricht In-App-Einstellungen | 
| Globaler Theme-Spiegel für Widgets | Benutzerstandards der App-Gruppe | Widget-Akzentfarben und optionaler Hintergrund mit Farbverlauf | 
| Pomodoro-Timer-Schnappschuss | Gemeinsamer App-Gruppencontainer | Pomodoro-Widget und Live-Aktivität | 
| Lern-Timer-Schnappschuss | Gemeinsamer App-Gruppencontainer | Lerntimer-Widget und Live-Aktivität | 
| Snapshot des Aufgaben-Widgets | Gemeinsamer App-Gruppencontainer | Countdown-Aufgaben-Widget |

Diese Daten sind für uns nicht zugänglich. Durch die Deinstallation der App wird der lokale Speicher entfernt (mit Ausnahme der iOS-Systemsicherungen, die Sie möglicherweise aktiviert haben). 

## Optionale iCloud-Synchronisierung (Aufgaben und Studienstatistiken) 

**Aufgaben:** Wenn Sie **Aufgaben mit iCloud synchronisieren** aktivieren, werden Countdown-Aufgaben über CloudKit (`iCloud.com.iHTCboy.iPomodoros`) synchronisiert. 

**Studienstatistiken:** Wenn Sie **Studienstatistiken mit iCloud synchronisieren** (Statistikeinstellungen) aktivieren, werden Fokussitzungsdatensätze als CloudKit-Datensätze vom Typ `StudySession` synchronisiert – einschließlich optionalem Titel/ID der verknüpften Aufgabe und eines `cloudId` für die Zusammenführung. **Tageszieleinstellungen** (`StatsGoals`) und **Erfolgs-Freischalt-/Feierstatus** (`StatsAchievements`) werden unter demselben Schalter synchronisiert. Sync verwendet inkrementelle CloudKit-Änderungstokens nach dem ersten vollständigen Pull. Dies ist **unabhängig** von der Aufgabensynchronisierung. 

In beiden Fällen verbleiben die Daten über die Infrastruktur von Apple in **Ihrem privaten iCloud-Konto** – nicht auf iHTC Studio-Servern. Deaktivieren Sie jederzeit einen der beiden Schalter. Lokale Kopien verbleiben auf jedem Gerät. 

## Benachrichtigungen 

Wenn Sie die Benachrichtigungsberechtigung erteilen, plant iPomodoro **lokale Benachrichtigungen** auf Ihrem Gerät für:

- Timer-Abschluss- und Hintergrundlernerinnerungen (sofern in den Einstellungen aktiviert) – der Nachrichtentext wird aus einem gebündelten Angebotspool für Benachrichtigungen auf dem Gerät ausgewählt; kein Netzwerkabruf 
- **Tägliche Motivationsbenachrichtigung** (optional, Einstellungen) – wiederholte lokale Benachrichtigung zu der von Ihnen gewählten Zeit 
- Erinnerungen an das Fälligkeitsdatum einer Aufgabe (sofern pro Aufgabe aktiviert) 

Diese Benachrichtigungen werden von iOS auf dem Gerät erstellt und übermittelt. Wir betreiben keinen Push-Benachrichtigungsserver und laden keine Angebotstexte von unseren Servern herunter. 

## App-Gruppe (Widgets und Live-Aktivitäten) 

Die Haupt-App und die Widget-Erweiterung teilen minimale Timer-, Motivations-, Thema-, **Aufgaben**- und **Heutige-Statistik-Fortschritts-Snapshots** über Apples App Group (`group.com.iHTCboy.iPomodoros`). Pomodoro und Study Timer verwenden **separate** Snapshot-Tasten auf dem Gerät, sodass beide Widgets nebeneinander existieren können. Dieser Container verbleibt auf Ihrem Gerät und wird nur zur Anzeige von Widgets und Live-Aktivitäten verwendet – nicht für den Zugriff Dritter. 

## In-App-Kauf 

Ein optionaler In-App-Supportkauf wird vollständig über **Apple StoreKit** abgewickelt. Wir erhalten über Apple nur Standard-App-Store-Kaufbelege; Wir erfassen Zahlungsdaten nicht direkt. 

## Dienste von Drittanbietern

iPomodoro integriert **nicht** Drittanbieter-Analytics, Werbung oder Social-Login-SDKs.

Wenn Sie auf **Feedback** tippen, kann die App Ihren Mail-Client mit einer vorausgefüllten Vorlage öffnen, die Geräte-Modell und App-Version enthält — Sie entscheiden, ob Sie sie senden.

## Datenschutz von Kindern

Wir sammeln wissentlich keine persönlichen Informationen von Kindern. Da wir keine personenbezogenen Daten über die App sammeln, gelten keine speziellen kindgerechten Bestimmungen über die standardmäßigen App-Store-Altersfreigaben hinaus.

## Änderungen dieser Richtlinie

Wir können diese Datenschutzrichtlinie von Zeit zu Zeit aktualisieren. Änderungen werden auf dieser Seite veröffentlicht.

## Kontaktieren Sie uns

Fragen zum Datenschutz?

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="fr" markdown="1">

iHTC Studio (« nous », « notre » ou « notre ») a créé **iPomodoro** (également connu sous le nom de « 爱番茄 » / « 愛番茄 ») en tant qu'application de productivité pour iPhone et iPad. Cette page explique comment nous traitons les informations lorsque vous utilisez l'application. 

## Résumé 

**iPomodoro ne collecte, ne stocke ni ne transmet de données personnelles à nos serveurs.** Les minuteries, les statistiques d'étude, les paramètres et le contenu de motivation fonctionnent sur votre appareil. La **synchronisation iCloud** facultative pour les tâches et/ou les statistiques d'étude utilise Apple CloudKit sous votre identifiant Apple — nous n'exécutons pas ce service cloud. 

## Données que nous ne collectons pas 

- Aucun nom, e-mail, numéro de téléphone ou compte utilisateur (sauf si vous nous envoyez volontairement un e-mail pour obtenir de l'aide). 
- Pas d'analyse d'utilisation, de SDK de rapport d'erreur ou d'identifiant publicitaire. 
- Aucun suivi de localisation. 
- Pas de téléchargement de sessions chronométrées ou de statistiques d'étude sur **nos serveurs** (la synchronisation iCloud facultative stocke les données dans votre compte Apple iCloud). 
- Les listes de tâches ne nous sont **pas** téléchargées : la synchronisation iCloud facultative s'effectue directement entre vos appareils via Apple CloudKit lorsque vous l'activez. 

## Données stockées sur votre appareil 

Les éléments suivants restent **localement** sur votre iPhone ou iPad :

| Données | Stockage | Objectif | 
|------|---------|---------| 
| Paramètres de Pomodoro et de la minuterie d'étude | Paramètres par défaut de l'utilisateur | Durées, sons, thèmes, préférences de notification, facultatif **Confirmer l'achèvement de la phase** (Pomodoro) | 
| Tâches du compte à rebours (titre, date, notes, indicateur de rappel, épingle, ordre, **couleur d'accent**) | Base de données SQLite | Liste des tâches, rappels de date d'échéance, couleurs des widgets | 
| Historique des sessions d'études | Base de données SQLite | Onglet Statistiques (temps de concentration, graphiques, répartition des tâches) | 
| Préférences d'affichage des statistiques | Paramètres par défaut de l'utilisateur | Filtres par défaut, **plage de dates personnalisée**, règles de comptage, couleurs du thème de l'onglet Statistiques | 
| Objectifs de concentration et préférences de réalisation | Paramètres par défaut de l'utilisateur | Objectifs quotidiens/hebdomadaires, badges débloqués | 
| Préférences de raccourci de l'écran d'accueil | Paramètres par défaut de l'utilisateur | Quelles actions rapides apparaissent lorsque vous appuyez longuement sur l'icône de l'application (jusqu'à 4) | 
| Le rappel du mode de mise au point bascule | Paramètres par défaut de l'utilisateur | Invite facultative lors du démarrage d'une minuterie sans Focus activé | 
| Calendrier de notification de motivation quotidienne | Paramètres par défaut de l'utilisateur | Heure de notification locale répétitive facultative | 
| Aperçu de la progression des statistiques d'aujourd'hui | Paramètres par défaut du groupe d'applications | Widget de statistiques du jour | 
| Corpus de citations de motivation (dialogue/quotidien + notification) | Offre groupée d'applications JSON | Pools de devis sur l'appareil (**1 000+** dialogue/quotidien combiné) ; le pool de notifications est séparé | 
| Préférences de thème et de langue | Paramètres par défaut de l'utilisateur | Apparition et localisation | 
| Index des citations de motivation quotidiennes | Paramètres par défaut du groupe d'applications | Widget de motivation et synchronisation des conseils d'activité en direct | 
| Filtre de langue de citation de motivation | Paramètres par défaut du groupe d'applications | Le pool de devis du widget correspond aux paramètres de l'application | 
| Miroir de thème global pour les widgets | Paramètres par défaut du groupe d'applications | Couleurs d’accent du widget et arrière-plan dégradé en option | 
| Instantané de la minuterie Pomodoro | Conteneur partagé du groupe d'applications | Widget Pomodoro et activité en direct | 
| Instantané de la minuterie d'étude | Conteneur partagé du groupe d'applications | Widget Minuterie d'étude et activité en direct | 
| Instantané du widget Tâches | Conteneur partagé du groupe d'applications | Widget Tâches de compte à rebours |

Ces données ne nous sont pas accessibles. La désinstallation de l'application supprime le stockage local (à l'exception des sauvegardes du système iOS que vous avez peut-être activées). 

## Synchronisation iCloud facultative (tâches et statistiques d'étude) 

**Tâches :** Si vous activez **Synchroniser les tâches avec iCloud**, les tâches de compte à rebours se synchronisent via CloudKit (`iCloud.com.iHTCboy.iPomodoros`). 

**Statistiques d'étude :** Si vous activez **Synchroniser les statistiques d'étude avec iCloud** (paramètres de statistiques), les enregistrements de session de focus sont synchronisés en tant qu'enregistrements CloudKit de type `StudySession` — y compris le titre/l'identifiant de la tâche liée en option et un `cloudId` pour la fusion. **Paramètres d'objectifs quotidiens** (`StatsGoals`) et **état de déverrouillage/célébration des succès** (`StatsAchievements`) se synchronisent sous la même bascule. La synchronisation utilise des jetons de modification CloudKit incrémentiels après la première extraction complète. Ceci est **indépendant** de la synchronisation des tâches. 

Dans les deux cas, les données restent dans **votre compte iCloud privé** via l'infrastructure d'Apple, et non dans les serveurs iHTC Studio. Désactivez l’une ou l’autre bascule à tout moment ; des copies locales restent sur chaque appareil. 

## Notifications 

Si vous accordez l'autorisation de notification, iPomodoro planifie des **notifications locales** sur votre appareil pour :

- Rappels d'achèvement du minuteur et d'étude de fond (lorsqu'ils sont activés dans les paramètres) — le texte du message est choisi parmi un pool de devis de notification groupé sur l'appareil ; pas de récupération réseau 
- **Notification de motivation quotidienne** (facultatif, Paramètres) — notification locale répétée à l'heure choisie 
- Rappels de date d'échéance des tâches (lorsqu'ils sont activés par tâche) 

Ces notifications sont créées et envoyées par iOS sur l'appareil. Nous n'exploitons pas de serveur de notification push et ne téléchargeons pas de texte de devis depuis nos serveurs. 

## Groupe d'applications (Widgets et activité en direct) 

L'application principale et l'extension de widget partagent un minimum de minuterie, de motivation, de thème, de **tâches** et de **progression des statistiques du jour** via le groupe d'applications d'Apple (`group.com.iHTCboy.iPomodoros`). Pomodoro et Study Timer utilisent des clés d'instantané **séparées** sur l'appareil afin que les deux widgets puissent coexister. Ce conteneur reste sur votre appareil et est utilisé uniquement pour afficher les widgets et l'activité en direct, et non pour l'accès de tiers. 

## Achat intégré 

Un achat facultatif de support intégré à l'application est entièrement traité par **Apple StoreKit**. Nous recevons uniquement des reçus d’achat standard sur l’App Store via Apple ; nous ne collectons pas directement les détails de paiement. 

## Services tiers

iPomodoro n'intègre **pas** de SDK d'analyse, de publicité ou de connexion sociale de tiers.

Lorsque vous appuyez sur **Retour d'information**, l'application peut ouvrir votre client de messagerie avec un modèle pré-rempli incluant le modèle de l'appareil et la version de l'application — vous choisissez si vous l'envoyez ou non.

## Vie privée des enfants

Nous ne collectons pas sciemment d'informations personnelles auprès des enfants. Parce que nous ne collectons pas de données personnelles via l'application, aucune disposition spéciale pour les enfants au-delà des classifications d'âge standard de l'App Store ne s'applique.

## Modifications de cette politique

Nous pouvons mettre à jour cette Politique de confidentialité de temps à autre. Les modifications seront publiées sur cette page.

## Contactez-nous

Des questions sur la confidentialité ?

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="tr" markdown="1">

iHTC Studio ("biz", "bizi" veya "bizim") **iPomodoro**'yu ("爱番茄" / "愛番茄" olarak da bilinir) iPhone ve iPad için bir üretkenlik uygulaması olarak geliştirdi. Bu sayfada, uygulamayı kullandığınızda bilgileri nasıl işlediğimiz açıklanmaktadır. 

## Özet 

**iPomodoro kişisel verileri sunucularımıza toplamaz, saklamaz veya iletmez.** Zamanlayıcılar, çalışma istatistikleri, ayarlar ve motivasyon içeriği cihazınızda çalışır. Görevler ve/veya çalışma istatistikleri için isteğe bağlı **iCloud senkronizasyonu**, Apple Kimliğiniz altında Apple CloudKit'i kullanır; bu bulut hizmetini biz çalıştırmıyoruz. 

## Toplamadığımız Veriler 

- İsim, e-posta, telefon numarası veya kullanıcı hesabı yok (destek için bize gönüllü olarak e-posta göndermediğiniz sürece). 
- Kullanım analitiği, kilitlenme raporlama SDK'ları veya reklam tanımlayıcıları yoktur. 
- Konum takibi yok. 
- Zamanlayıcı oturumları veya çalışma istatistikleri **sunucularımıza** yüklenmez (isteğe bağlı iCloud senkronizasyonu, verileri Apple iCloud hesabınızda saklar). 
- Görev listeleri bize **yüklenmez**; isteğe bağlı iCloud senkronizasyonu, etkinleştirdiğinizde Apple CloudKit aracılığıyla doğrudan cihazlarınız arasında gider. 

## Cihazınızda Saklanan Veriler 

Aşağıdakiler iPhone veya iPad'inizde **yerel olarak** kalır:

| Veri | Depolama | Amaç | 
|------|---------|---------| 
| Pomodoro ve çalışma zamanlayıcı ayarları | Kullanıcı Varsayılanları | Süreler, sesler, temalar, bildirim tercihleri, isteğe bağlı **Aşamanın tamamlandığını onaylayın** (Pomodoro) | 
| Geri sayım görevleri (başlık, tarih, notlar, hatırlatma bayrağı, raptiye, sıra, **vurgu rengi**) | SQLite veritabanı | Görev listesi, son tarih hatırlatıcıları, widget renkleri | 
| Çalışma oturumu geçmişi | SQLite veritabanı | İstatistikler sekmesi (odaklanma süresi, grafikler, görev dökümü) | 
| İstatistik görüntüleme tercihleri ​​| Kullanıcı Varsayılanları | Varsayılan filtreler, **özel tarih aralığı**, sayma kuralları, İstatistik sekmesi tema renkleri | 
| Odaklanma hedefi ve başarı tercihleri ​​| Kullanıcı Varsayılanları | Günlük/haftalık hedefler, açılan rozetler | 
| Ana Ekran kısayol tercihleri ​​| Kullanıcı Varsayılanları | Uygulama simgesine uzun basıldığında hangi Hızlı İşlemler görünür (en fazla 4) | 
| Odak Modu hatırlatıcısı geçiş yapar | Kullanıcı Varsayılanları | Odaklanma etkin olmadan bir zamanlayıcı başlatıldığında isteğe bağlı istem | 
| Günlük motivasyon bildirim programı | Kullanıcı Varsayılanları | İsteğe bağlı yinelenen yerel bildirim zamanı | 
| Bugünkü istatistikler ilerleme anlık görüntüsü | Uygulama Grubu Kullanıcı Varsayılanları | Bugünün İstatistikleri widget'ı | 
| Motivasyon teklifi külliyatı (diyalog/günlük + bildirim) | Uygulama paketi JSON | Cihazdaki fiyat teklifi havuzları (**1000+** iletişim kutusu/günlük birleştirilmiş); bildirim havuzu ayrıdır | 
| Tema ve dil tercihleri ​​| Kullanıcı Varsayılanları | Görünüm ve yerelleştirme | 
| Günlük motivasyon teklif endeksi | Uygulama Grubu Kullanıcı Varsayılanları | Motivasyon widget'ı ve Canlı Etkinlik ipucu senkronizasyonu | 
| Motivasyon alıntı dili filtresi | Uygulama Grubu Kullanıcı Varsayılanları | Widget fiyat teklifi havuzu uygulama içi ayarlarla eşleşiyor | 
| Widget'lar için küresel tema aynası | Uygulama Grubu Kullanıcı Varsayılanları | Widget vurgu renkleri ve isteğe bağlı degrade arka plan | 
| Pomodoro zamanlayıcı anlık görüntüsü | Uygulama Grubu paylaşılan kapsayıcısı | Pomodoro widget'ı ve Canlı Etkinlik | 
| Çalışma zamanlayıcısının anlık görüntüsü | Uygulama Grubu paylaşılan kapsayıcısı | Çalışma Zamanlayıcısı widget'ı ve Canlı Etkinlik | 
| Görevler widget'ının anlık görüntüsü | Uygulama Grubu paylaşılan kapsayıcısı | Geri Sayım Görevleri widget'ı |

Bu verilere bizim erişimimiz yoktur. Uygulamanın kaldırılması yerel depolamayı kaldırır (etkinleştirmiş olabileceğiniz iOS sistem yedeklemeleri hariç). 

## İsteğe Bağlı iCloud Senkronizasyonu (Görevler ve Çalışma İstatistikleri) 

**Görevler:** **Görevleri iCloud ile senkronize et** seçeneğini etkinleştirirseniz, geri sayım görevleri CloudKit (`iCloud.com.iHTCboy.iPomodoros`) aracılığıyla senkronize edilir. 

**Çalışma istatistikleri:** **Çalışma istatistiklerini iCloud ile senkronize et** (İstatistik ayarları) seçeneğini etkinleştirirseniz, odak oturumu kayıtları, isteğe bağlı bağlı görev başlığı/kimliği ve birleştirme için bir `cloudId` dahil olmak üzere `StudySession` türündeki CloudKit kayıtları olarak senkronize edilir. **Günlük hedef ayarları** (`StatsGoals`) ve **başarı kilidini açma/kutlama durumu** (`StatsAchievements`) aynı açma/kapama düğmesi altında senkronize edilir. Senkronizasyon, ilk tam çekmeden sonra artımlı CloudKit değişiklik belirteçlerini kullanır. Bu, görev senkronizasyonundan **bağımsızdır**. 

Her iki durumda da veriler, iHTC Studio sunucuları değil, Apple'ın altyapısı aracılığıyla **özel iCloud hesabınızda** kalır. Her iki geçişi de istediğiniz zaman devre dışı bırakın; yerel kopyalar her cihazda kalır. 

## Bildirimler 

Bildirim izni verirseniz iPomodoro, cihazınızda aşağıdakiler için **yerel bildirimler** planlar:

- Zamanlayıcı tamamlama ve arka plan çalışması hatırlatıcıları (ayarlarda etkinleştirildiğinde) — mesaj metni, paket halindeki cihaz üzeri bildirim fiyat teklifi havuzundan seçilir; ağ getirilmiyor 
- **Günlük motivasyon bildirimi** (isteğe bağlı, Ayarlar) — seçtiğiniz saatte tekrarlanan yerel bildirim 
- Görev son tarihi hatırlatıcıları (görev başına etkinleştirildiğinde) 

Bu bildirimler cihazdaki iOS tarafından oluşturulup iletilir. Bir anlık bildirim sunucusu işletmiyoruz veya sunucularımızdan fiyat teklifi metni indirmiyoruz. 

## Uygulama Grubu (Widget'lar ve Canlı Etkinlik) 

Ana uygulama ve Widget Uzantısı, Apple'ın Uygulama Grubu (`group.com.iHTCboy.iPomodoros`) aracılığıyla minimum zamanlayıcı, motivasyon, tema, **görevler** ve **bugünün istatistik ilerlemesi** anlık görüntülerini paylaşır. Pomodoro ve Çalışma Zamanlayıcısı, cihaz üzerinde **ayrı** anlık görüntü anahtarları kullanır, böylece her iki widget bir arada bulunabilir. Bu kapsayıcı cihazınızda kalır ve yalnızca widget'ları ve Canlı Etkinliği görüntülemek için kullanılır; üçüncü taraf erişimi için kullanılmaz. 

## Uygulama İçi Satın Alma 

İsteğe bağlı uygulama içi destek satın alımı tamamen **Apple StoreKit** tarafından gerçekleştirilir. Apple aracılığıyla yalnızca standart App Store satın alma makbuzlarını alıyoruz; Ödeme ayrıntılarını doğrudan toplamıyoruz. 

## Üçüncü Taraf Hizmetleri

iPomodoro, üçüncü taraf analiz, reklam veya sosyal giriş SDK'larını **entegre etmez**.

**Geri Bildirim**e dokunduğunuzda, uygulama cihaz modeli ve uygulama sürümü gibi önceden doldurulmuş bir şablonla mail istemcinizi açabilir — göndermeye karar vermek size kalmıştır.

## Çocukların Gizliliği

Çocuklardan bilinçli olarak kişisel bilgi toplamıyoruz. Uygulama üzerinden kişisel veri toplamadığımız için, standart App Store yaş derecelendirmelerinin ötesinde özel çocuklara yönelik düzenlemeler uygulanmaz.

## Bu Politikadaki Değişiklikler

Bu Gizlilik Politikasını zaman zaman güncelleyebiliriz. Değişiklikler bu sayfada yayınlanacaktır.

## İletişim

Gizlilikle ilgili sorularınız mı var?

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
