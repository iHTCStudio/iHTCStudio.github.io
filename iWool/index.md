---
layout: app
title: iWool — Support
app_id: iWool
description: Local deal tracker with reminders, earnings, Live Activities, Quick Countdown, 12 widgets and iwool:// deep links for iPhone and iPad.
---

<section lang="en" markdown="1">

iWool is a privacy-first local tracker built for capturing deals, following activities and counting earnings on **iPhone and iPad**. **`iwool://` deep links** open Home, Calendar, Statistics, Settings, in-app actions (new activity, Quick Countdown, scanner, reminders) or a specific activity — from widgets, Shortcuts or Home Screen Quick Actions. **No sign-up, no upload — your data stays on-device.**

See the full [**`iwool://` URL Scheme reference**](url-scheme) for all supported paths and aliases.

## Getting Started

1. Tap **+** on the home screen to create your first activity.
2. Fill in the title, platform, start and end time. Add reminders if needed.
3. Tap **Save**. The activity appears in your list, grouped by status.
4. When the deal pays off, tap into the detail page and tap **Record Earnings**.
5. Check **Statistics** anytime to see your totals, trends and platform ranking.
6. Add a Home Screen or Lock Screen widget so you never have to open the app to stay updated.

## Features

### Home Screen

- **Seven status summary cards** — Active, Upcoming, All, Expired, Completed, Cancelled, Paused. Tap any card to filter instantly; tap again to jump back to Today.
- **Pause or cancel with an effective date** — hide from Today/calendar and stop reminders while keeping earnings history.
- **Activity share export** — export a share pack friends can import to follow along (separate from full backup).
- **Full-text search** — search across title, notes, platform, requirements and rules.
- **Long-press actions** — mark complete, pause/resume, cancel/restore, archive, duplicate as new, or delete.
- Recurring activities always show **today's occurrence**, so status and time match your actual schedule.

### Calendar

- Switch between **month view** and **week timeline** — your preference is remembered.
- Tap any date to see that day's activities. Dots and left-bar colours follow the platform colour.
- Long-press any list row for the same quick actions as the home screen.
- Pull to refresh anytime.

### Activity Detail

- **Starts in countdown** — shows time until the current or next occurrence; highlights in orange when under 24 hours.
- **Next occurrence date** shown for recurring activities; "no next occurrence" when the series ends.
- Activity URL, requirements, rules and notes all render links. **Single-tap** opens in Safari (http/https) or the associated app; **long-press** brings up the native iOS link menu including "Open in [App]", "Open in Safari", "Copy Link" and "Share".

### Record Earnings

- Half-sheet form with amount, optional note and **record date**.
- Multiple entries per activity, each independently editable or deletable.
- Earnings only appear in Statistics when recorded here — estimated earnings are for display only.

### Statistics

- Totals for today, this week, this month and this year.
- **Monthly trend chart** — tap any bar (if amount > 0) to see every earnings entry in that period.
- **Platform ranking** — independent time scope selector (year / month / week); tap a platform row to drill into per-entry details.
- **Activity overview** — tap a status row or the total row to see the matching activity list.
- Recurring activity earnings policy (strict or lenient) is configurable in Settings.

### Reminders

- Multiple reminders per activity — at start, before start, before deadline or daily fixed time.
- System local notifications. Reminder schedules are tidied up every time you open the app.
- Cancelled activities stop ringing automatically.
- Home and calendar list rows show a **small reminder glyph** so you can see what is scheduled at a glance.

### Share Image Cards

Share an **activity** or your **Statistics dashboard** as a **branded PNG image card** via the system Share Sheet — gradient background, App Store QR code and optional watermark. Toggle whether earnings appear on shared cards in Settings (**off by default**). Images render on-device; nothing is uploaded. Save to Photos may request photo library access.

### Home Screen Quick Actions

Long-press the iWool icon on iOS to launch up to **4** shortcuts. Choose from **9** presets in **Settings → Tools → Home Screen Shortcuts**:

Home · Calendar · Statistics · **Quick Countdown** · New Activity · Scheduled Reminders · Scanner · Rate App · Feedback

Default: **Home, Calendar, Statistics, Quick Countdown**. Each action uses an `iwool://` URL (same router as widgets and Shortcuts).

### Dynamic Island & Live Activities

Two Live Activity types on supported iPhone models:

**1. Event countdown** (iOS 16.1+)

- Tied to wool activities — enable in **Settings → Notifications → Live Activity**.
- Tune **lead time** (1–480 minutes before start). Multiple in-window activities can each show an island, or rotate.
- Long-press an eligible activity on Home or Calendar → **Add to Dynamic Island**.

**2. Quick Countdown** (iOS 16.2+)

- **Standalone** island / lock-screen countdown — **not saved** to your activity database.
- Create from **Settings → Island Reminder** or `iwool://island` / Home Screen Quick Action.
- Duration **1 second to 8 hours** — preset chips (30 s, 1–480 min) or pick a deadline; optional title, note, accent colour and seconds display.
- Ends automatically when time is up; ideal for flash sales, sign-in windows or ad-hoc timers.

### Home Screen & Lock Screen Widgets

**12 widget families** in total (8 Home Screen + 4 Lock Screen accessory styles):

| Widget | Description |
|--------|-------------|
| Today Active | Today's activities currently in progress |
| Today All | All of today's activities |
| Today Upcoming | Today's not-yet-started activities |
| All Events | Full list preview, sorted by status |
| Stats Overview | Active / Upcoming / All counts — Large size adds Expired / Completed / Cancelled |
| Earnings | Today, this week, this month and this year |
| Glance | Activity count + earnings + active count at a glance |
| Top Platforms | This year's earnings ranking by platform |
| Lock Screen (4 styles) | Circular, rectangular and inline accessories — iOS 16+ |

On iOS 17 and later, list widgets support **tap per row** to open the matching activity directly.

A built-in **Widget Guide** in Settings walks you through adding widgets step by step, with a widget gallery and FAQ.

### Activity Form Extras

- **Popular app links** — one-tap fill for common Pay, Bank and shopping app URL schemes.
- **Scan or pick from album** — scan a QR code or pick an image to auto-fill the activity URL.

### QR / Barcode Scanner

A standalone scanner in **Settings → Tools**:

- Real-time camera scan with flashlight support.
- Pick from photo album with Vision-powered detection.
- Results list with one-tap copy, in-app Safari for http/https links and export via Share Sheet.

### Appearance & Language

- 8+ theme colours (Gold, Ocean Blue, Forest Green, Rose Pink, Lavender, Sunset Orange, Mint, Cherry Red…)
- Light / Dark / System appearance — with haptic feedback on switch.
- **20 alternate Home Screen app icons.**
- 13 display languages: English, Simplified Chinese, Traditional Chinese, Japanese, Korean, Thai, Hindi, Spanish, French, German, Brazilian Portuguese, Russian, Arabic — switchable independently of system language.
- Multiple currencies (ISO 4217); customisable **decimal places** for general amounts (default 2) and chart labels (default 0).
- Configurable **app badge strategy** (off / today's count / total pending).
- **More recommendations** — link to the developer's App Store page in Settings → About.

### Data & Privacy

- **Export full backup** — CSV file with all activities, reminders, earnings, recurrence states and templates.
- **Import backup** — replace the entire library or append-only merge (keeps existing data).
- **One-tap archive** — archive all completed / expired / cancelled non-recurring activities at once.
- Archive can be restored anytime from Settings.
- Sharing an activity copies text to clipboard. A **sharing-includes-earnings** toggle (off by default) keeps your earnings amounts private.

## Recurrence Rules

| Type | Options |
|------|---------|
| Daily | Every N days |
| Weekly | Any combination of weekdays |
| Monthly | Single day, through end date or through month end |
| Yearly | Single day, through end date or through Dec 31 |
| Custom | Custom interval in days |

End conditions: a specific end date or a maximum occurrence count.

## System Requirements

| Feature | Minimum |
|---------|---------|
| iPhone / iPad | iOS 15.0+ |
| Lock Screen Widgets | iOS 16.0+ |
| Dynamic Island — event countdown | iOS 16.1+ (supported hardware) |
| Quick Countdown Live Activity | iOS 16.2+ |
| Per-row widget tap | iOS 17.0+ |

## Contact Us

Questions, feedback or need help? Reach us at:

- **In-App:** Settings → Send Feedback
- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

We typically respond within 48 hours.

[FAQ](faq) · [URL Scheme](url-scheme) · [Privacy Policy](privacy)

</section>

<section lang="zh-CN" markdown="1">

爱羊毛是一款隐私优先的本地追踪应用，专为在 **iPhone 与 iPad** 上捕捉活动、跟进进度与统计收益而生。**`iwool://` 深度链接**可打开首页、日历、统计、设置、应用内操作（新建活动、灵动岛提醒、扫码、提醒列表）或指定活动——来自小组件、快捷指令或主屏快捷方式。**无需注册、不上传——所有数据都留在设备本地。**

完整路径与别名见 [**`iwool://` URL Scheme 文档**](url-scheme)。

## 快速上手

1. 在首页点按 **+** 创建你的第一个活动。
2. 填写标题、平台、开始与结束时间。如需提醒，添加提醒。
3. 点按**保存**。活动会出现在列表中，并按状态分组。
4. 当活动有收益时，进入详情页点按**记录收益**。
5. 任意时刻进入**统计**查看总计、趋势与平台排名。
6. 添加主屏或锁屏小组件，无需打开应用就能掌握最新进度。

## 功能特性

### 首页

- **七个状态汇总卡片** — 进行中、即将开始、全部、已过期、已完成、已取消、已暂停。点按任一卡片立即筛选；再次点按返回今日。
- **暂停 / 取消（生效日）** — 今日与日历默认隐藏并停止提醒，已记收益仍计入统计。
- **活动分享导出** — 导出可供好友导入跟进的分享包（与全量备份分开）。
- **全文搜索** — 跨标题、备注、平台、要求与规则进行搜索。
- **长按操作** — 标记完成、暂停/恢复参与、取消/恢复、归档、复制为新、删除。
- 重复活动总是显示**今日实例**，状态与时间始终与实际安排同步。

### 日历

- 在**月视图**与**周时间轴**之间切换——你的偏好会被记住。
- 点按任意日期查看当日活动。圆点与左侧色条跟随平台颜色。
- 长按列表行可使用与首页相同的快捷操作。
- 随时下拉刷新。

### 活动详情

- **倒计时** — 显示距当前或下次实例的剩余时间；不足 24 小时时高亮为橙色。
- 重复活动显示**下次发生日期**；系列结束时显示「无下次发生」。
- 活动 URL、要求、规则与备注中的链接均可点按。**单击**用 Safari（http/https）或对应应用打开；**长按**唤出 iOS 原生链接菜单，包含「在 [App] 中打开」「用 Safari 打开」「拷贝链接」「分享」。

### 记录收益

- 半屏表单：金额、可选备注、**记录日期**。
- 一个活动可有多条记录，每条独立编辑或删除。
- 只有此处记录的收益会进入统计——预估收益仅供显示。

### 统计

- 今日、本周、本月、本年的总计。
- **月度趋势图** — 点按任意柱（金额 > 0）查看该期所有收益记录。
- **平台排名** — 独立时间范围选择（年/月/周）；点按平台行下钻到逐条详情。
- **活动概览** — 点按状态行或总计行查看对应活动列表。
- 重复活动的收益策略（严格 / 宽松）可在设置中配置。

### 提醒

- 一个活动可设置多个提醒——开始时、开始前、截止前、每日固定时刻。
- 使用系统本地通知。打开应用时会自动整理提醒计划。
- 已取消的活动会自动停止响铃。
- 首页与日历列表行显示**小型提醒图标**，让你一眼看清已计划的提醒。

### 分享图卡片

可将**活动**或**统计仪表盘**生成为 **品牌 PNG 分享图**——渐变背景、App Store 二维码、可选水印。设置中可控制分享是否包含收益（**默认关闭**）。保存到相册可能请求相册权限。

### 主屏快捷方式

长按 iWool 图标，最多 **4** 项。在 **设置 → 工具 → 主屏快捷方式** 从 **9** 项中选择：

首页 · 日历 · 统计 · **灵动岛提醒** · 新建活动 · 已登记提醒 · 扫码 · 评分 · 反馈

默认：**首页、日历、统计、灵动岛提醒**。均使用 `iwool://` URL。

### 灵动岛与实时活动

支持两种 Live Activity：

**1. 活动倒计时**（iOS 16.1+）

- 绑定羊毛活动 — **设置 → 通知 → 实时活动** 启用，提前 **1–480 分钟**显示。
- 长按首页/日历活动 → **加入灵动岛**。

**2. 灵动岛提醒 Quick Countdown**（iOS 16.2+）

- **独立**倒计时，**不写入**活动数据库。
- 从 **设置 → 灵动岛提醒** 或 `iwool://island` / 主屏快捷方式创建。
- 时长 **1 秒至 8 小时**；预设（30 秒、1–480 分钟）或截止时刻；可选标题、备注、强调色与秒显示。

### 主屏幕与锁屏小组件

共 **12 款小组件**（8 款主屏 + 4 款锁屏附件样式）：

| 小组件 | 描述 |
|--------|-------------|
| 今日进行中 | 今天正在进行的活动 |
| 今日全部 | 今天的所有活动 |
| 今日待开始 | 今天还未开始的活动 |
| 全部事件 | 完整列表预览，按状态排序 |
| 统计概览 | 进行中 / 即将 / 全部计数 —— 大尺寸增加 已过期 / 已完成 / 已取消 |
| 收益 | 今日、本周、本月、本年 |
| 一览 | 活动数 + 收益 + 进行中数一览 |
| 平台 Top | 本年收益按平台排名 |
| 锁屏（4 种样式）| 圆形、矩形与行内附件—— iOS 16+ |

iOS 17 及以上，列表型小组件支持**逐行点按**直接打开对应活动。

设置内置**小组件指南**，分步引导你添加小组件，含小组件画廊与常见问题。

### 表单工具

- **常用应用链接** — 一键填入常见支付、银行、购物应用的 URL Scheme。
- **扫码或从相册选取** — 扫描二维码或选取图片，自动填入活动 URL。

### 二维码 / 条码扫描

**设置 → 工具**中独立的扫描器：

- 实时相机扫描，支持闪光灯。
- 从相册选取并使用 Vision 识别。
- 结果列表支持一键复制、http/https 链接应用内 Safari 打开、通过分享面板导出。

### 外观与语言

- 8+ 种主题色（金、海洋蓝、森林绿、玫瑰粉、薰衣草、夕阳橙、薄荷、樱桃红…）
- 浅色 / 深色 / 跟随系统外观——切换时带触感反馈。
- **20 款备用主屏应用图标。**
- 13 种显示语言：英文、简体中文、繁体中文、日文、韩文、泰文、印地文、西班牙文、法文、德文、巴西葡萄牙文、俄文、阿拉伯文——独立于系统语言切换。
- 多种货币（ISO 4217）；可自定义**金额小数位**（默认 2）与图表标签小数位（默认 0）。
- 可配置**应用图标徽章策略**（关闭 / 今日数 / 全部待办数）。
- **更多推荐** — 设置 → 关于 中跳转开发者 App Store 页面。

### 数据与隐私

- **导出完整备份** — CSV 文件，包含所有活动、提醒、收益、重复状态与模板。
- **导入备份** — 替换全部数据，或仅追加（保留现有数据）。
- **一键归档** — 一次归档所有已完成 / 已过期 / 已取消的非重复活动。
- 归档随时可在设置中恢复。
- 分享活动会把文本复制到剪贴板。**分享是否包含收益**开关默认关闭，让你的收益金额保持私密。

## 重复规则

| 类型 | 选项 |
|------|---------|
| 每日 | 每 N 天 |
| 每周 | 任意工作日组合 |
| 每月 | 某一天、到结束日期、或到月底 |
| 每年 | 某一天、到结束日期、或到 12 月 31 日 |
| 自定义 | 自定义天数间隔 |

结束条件：指定结束日期或最大发生次数。

## 系统要求

| 功能 | 最低版本 |
|---------|---------|
| iPhone / iPad | iOS 15.0+ |
| 锁屏小组件 | iOS 16.0+ |
| 灵动岛 — 活动倒计时 | iOS 16.1+（相容硬件）|
| 灵动岛提醒 Quick Countdown | iOS 16.2+ |
| 小组件逐行点按 | iOS 17.0+ |

## 联系我们

有问题、反馈或需要帮助？请联系：

- **应用内：**设置 → 发送反馈
- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

我们通常在 48 小时内回复。

[常见问题](faq) · [URL Scheme](url-scheme) · [隐私政策](privacy)

</section>

<section lang="zh-TW" markdown="1">

愛羊毛是一款隱私優先的本地追蹤應用，專為在 **iPhone 與 iPad** 上捕捉活動、跟進進度與統計收益而生。**`iwool://` 深度連結**可開啟首頁、日曆、統計、設定、應用內操作（新建活動、靈動島提醒、掃碼、提醒列表）或指定活動——來自小工具、捷徑或主畫面捷徑。**無需註冊、不上傳——所有資料都留在裝置本地。**

完整路徑見 [**`iwool://` URL Scheme 文件**](url-scheme)。

## 快速上手

1. 在首頁點按 **+** 建立你的第一個活動。
2. 填寫標題、平台、開始與結束時間。如需提醒，新增提醒。
3. 點按**儲存**。活動會出現在列表中，並按狀態分組。
4. 當活動有收益時，進入詳情頁點按**記錄收益**。
5. 任意時刻進入**統計**查看總計、趨勢與平台排名。
6. 新增主畫面或鎖定畫面小工具，無需開啟應用就能掌握最新進度。

## 功能特色

### 首頁

- **七個狀態彙總卡片** — 進行中、即將開始、全部、已過期、已完成、已取消、已暫停。點按任一卡片立即篩選；再次點按返回今日。
- **暫停 / 取消（生效日）** — 今日與日曆預設隱藏並停止提醒，已記收益仍計入統計。
- **活動分享匯出** — 匯出可供好友匯入跟進的分享包（與全量備份分開）。
- **全文搜尋** — 跨標題、備註、平台、要求與規則進行搜尋。
- **長按操作** — 標記完成、暫停/恢復參與、取消/還原、封存、複製為新、刪除。
- 重複活動總是顯示**今日實例**，狀態與時間始終與實際安排同步。

### 日曆

- 在**月檢視**與**週時間軸**之間切換——你的偏好會被記住。
- 點按任意日期查看當日活動。圓點與左側色條跟隨平台顏色。
- 長按列表行可使用與首頁相同的快捷操作。
- 隨時下拉重新整理。

### 活動詳情

- **倒數計時** — 顯示距目前或下次實例的剩餘時間；不足 24 小時時高亮為橙色。
- 重複活動顯示**下次發生日期**；系列結束時顯示「無下次發生」。
- 活動 URL、要求、規則與備註中的連結均可點按。**單擊**用 Safari（http/https）或對應應用開啟；**長按**喚出 iOS 原生連結選單，包含「在 [App] 中開啟」「用 Safari 開啟」「複製連結」「分享」。

### 記錄收益

- 半屏表單：金額、可選備註、**記錄日期**。
- 一個活動可有多筆紀錄，每筆獨立編輯或刪除。
- 只有此處記錄的收益會進入統計——預估收益僅供顯示。

### 統計

- 今日、本週、本月、本年的總計。
- **月度趨勢圖** — 點按任意柱（金額 > 0）查看該期所有收益紀錄。
- **平台排名** — 獨立時間範圍選擇（年/月/週）；點按平台行下鑽到逐筆詳情。
- **活動概覽** — 點按狀態行或總計行查看對應活動列表。
- 重複活動的收益策略（嚴格 / 寬鬆）可在設定中設定。

### 提醒

- 一個活動可設定多個提醒——開始時、開始前、截止前、每日固定時刻。
- 使用系統本地通知。開啟應用時會自動整理提醒計畫。
- 已取消的活動會自動停止響鈴。
- 首頁與日曆列表行顯示**小型提醒圖示**，讓你一眼看清已計畫的提醒。

### 分享圖卡片

可將**活動**或**統計儀表板**生成 **PNG 分享圖**（漸層、App Store QR、可選水印）。分享是否含收益可在設定中關閉（**預設關**）。

### 主畫面捷徑

長按圖示最多 **4** 項。**設定 → 工具 → 主畫面捷徑** 從 **9** 項中選：首頁 · 日曆 · 統計 · **靈動島提醒** · 新建 · 已登記提醒 · 掃碼 · 評分 · 回饋。預設：首頁、日曆、統計、靈動島提醒。

### 靈動島與即時活動

**1. 活動倒數**（iOS 16.1+）— 綁定羊毛活動，提前 1–480 分鐘。**2. 靈動島提醒 Quick Countdown**（iOS 16.2+）— 獨立倒數、不寫入資料庫，1 秒–8 小時，經設定或 `iwool://island` 建立。

### 主畫面與鎖定畫面小工具

共 **12 款小工具**（8 款主畫面 + 4 款鎖定畫面附件樣式）：

| 小工具 | 描述 |
|--------|-------------|
| 今日進行中 | 今天正在進行的活動 |
| 今日全部 | 今天的所有活動 |
| 今日待開始 | 今天還未開始的活動 |
| 全部事件 | 完整列表預覽，按狀態排序 |
| 統計概覽 | 進行中 / 即將 / 全部計數 —— 大尺寸增加 已過期 / 已完成 / 已取消 |
| 收益 | 今日、本週、本月、本年 |
| 一覽 | 活動數 + 收益 + 進行中數一覽 |
| 平台 Top | 本年收益按平台排名 |
| 鎖定畫面（4 種樣式）| 圓形、矩形與行內附件—— iOS 16+ |

iOS 17 及以上，列表型小工具支援**逐行點按**直接開啟對應活動。

設定內建**小工具指南**，分步引導你新增小工具，含小工具畫廊與常見問題。

### 表單工具

- **常用應用連結** — 一鍵填入常見支付、銀行、購物應用的 URL Scheme。
- **掃碼或從相簿選取** — 掃描 QR Code 或選取圖片，自動填入活動 URL。

### QR Code / 條碼掃描

**設定 → 工具**中獨立的掃描器：

- 即時相機掃描，支援閃光燈。
- 從相簿選取並使用 Vision 辨識。
- 結果列表支援一鍵複製、http/https 連結應用內 Safari 開啟、透過分享面板匯出。

### 外觀與語言

- 8+ 種主題色（金、海洋藍、森林綠、玫瑰粉、薰衣草、夕陽橙、薄荷、櫻桃紅…）
- 淺色 / 深色 / 跟隨系統外觀——切換時帶觸感回饋。
- **20 款備用主畫面應用圖示。**
- 13 種顯示語言：英文、簡體中文、繁體中文、日文、韓文、泰文、印地文、西班牙文、法文、德文、巴西葡萄牙文、俄文、阿拉伯文——獨立於系統語言切換。
- 多種貨幣（ISO 4217）；可自訂**金額小數位**（預設 2）與圖表標籤小數位（預設 0）。
- 可設定**應用圖示徽章策略**（關閉 / 今日數 / 全部待辦數）。
- **更多推薦** — 設定 → 關於 中跳轉開發者 App Store 頁面。

### 資料與隱私

- **匯出完整備份** — CSV 檔案，包含所有活動、提醒、收益、重複狀態與範本。
- **匯入備份** — 取代全部資料，或僅附加（保留現有資料）。
- **一鍵封存** — 一次封存所有已完成 / 已過期 / 已取消的非重複活動。
- 封存隨時可在設定中還原。
- 分享活動會把文字複製到剪貼簿。**分享是否包含收益**開關預設關閉，讓你的收益金額保持私密。

## 重複規則

| 類型 | 選項 |
|------|---------|
| 每日 | 每 N 天 |
| 每週 | 任意工作日組合 |
| 每月 | 某一天、到結束日期、或到月底 |
| 每年 | 某一天、到結束日期、或到 12 月 31 日 |
| 自訂 | 自訂天數間隔 |

結束條件：指定結束日期或最大發生次數。

## 系統需求

| 功能 | 最低版本 |
|---------|---------|
| iPhone / iPad | iOS 15.0+ |
| 鎖定畫面小工具 | iOS 16.0+ |
| 靈動島 — 活動倒數 | iOS 16.1+（相容硬體）|
| 靈動島提醒 Quick Countdown | iOS 16.2+ |
| 小工具逐行點按 | iOS 17.0+ |

## 聯絡我們

有問題、回饋或需要協助？請聯絡：

- **應用內：**設定 → 傳送回饋
- **電子郵件：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

我們通常在 48 小時內回覆。

[常見問題](faq) · [URL Scheme](url-scheme) · [隱私政策](privacy)

</section>
