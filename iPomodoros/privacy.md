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

iHTC Studio ("we", "us" or "our"; formerly iHTCTeam) built **iPomodoro** (also known as "爱番茄" / "愛番茄") as a productivity app for iPhone and iPad. This page explains how we handle information when you use the app.

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

爱火腿肠工作室（iHTC Studio）（「我们」；原 iHTCTeam）开发了 **爱番茄**（iPomodoro / 愛番茄），一款面向 iPhone 与 iPad 的效率应用。本页说明你在使用应用时，我们如何处理相关信息。

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

愛火腿腸工作室（iHTC Studio）（「我們」；原 iHTCTeam）開發了 **愛番茄**（iPomodoro / 爱番茄），一款面向 iPhone 與 iPad 的效率應用。本頁說明你在使用應用時，我們如何處理相關資訊。

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
