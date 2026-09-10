---
layout: doc
title: iPomodoro — FAQ
app_id: iPomodoros
doc_title_en: Frequently Asked Questions
doc_title_zh_cn: 常见问题
doc_title_zh_tw: 常見問題
description: Frequently asked questions about iPomodoro — privacy, Quick Actions, URL schemes, statistics, achievements, iCloud sync, widgets, and Live Activity.
---

<section lang="en" markdown="1">

### Why should I choose iPomodoro over other Pomodoro apps?

iPomodoro is a **native SwiftUI** app built for Apple platforms — not a wrapped web timer. You get **five integrated tabs** (Pomodoro, Study Timer, Tasks, Statistics, Settings), **dual Live Activities**, **five widget families**, **9 achievement badges**, **1000+ on-device quotes**, **Siri & URL shortcuts**, and **optional iCloud sync** — all with **zero analytics** and **no account required**. One calm app that covers focus, deadlines, and progress tracking end to end.

### Where are timer and task settings?

Timer durations, sounds, Live Activity, page theme colors, optional **Focus Mode reminder**, and (Pomodoro only) optional **Confirm phase completion** live under each tab's **gear icon** (Pomodoro, Study Timer, Tasks, or **Statistics**). The global **Settings** tab holds appearance, language, **Home Screen shortcuts**, **App Guide**, notification permission, motivational quotes (including **daily motivation notification**), widget guide, feedback, and about — not per-mode durations. **Statistics** settings (page theme, goals, optional iCloud sync, achievements, counting rules, CSV, retention) are under **Statistics tab → gear**.

### How do Home Screen shortcuts and Siri work?

**Long-press the app icon** for Quick Actions — open Pomodoro, Study Timer, Tasks, Statistics, a motivation quote, or feedback. Customize which four appear under **Settings → App settings → Home Screen shortcuts** (drag to reorder). You can also open the same destinations via **`iPomodoro://`** URLs (`pomodoro`, `study`, `tasks`, `stats`, `motivation`, `feedback`; `iPomodoros://` also works). See the full [URL Scheme Reference](url-scheme). **Siri / Shortcuts app** can open tabs or answer *"How long did I focus today in iPomodoro?"* via built-in App Shortcuts.

### What is the in-app App Guide?

**Settings → App settings → App Guide** — a collapsible tutorial covering all five tabs, widgets, shortcuts, iCloud, and FAQ (similar style to the Widget guide).

### Can iPomodoro turn on Focus Mode for me?

No — iOS does not allow third-party apps to enable Focus directly. Optional **Focus Mode reminder** (Pomodoro or Study Timer gear settings) checks whether Focus is off when you start a timer and shows an alert; you can open **Settings** from the alert, but you must turn on Focus yourself.

### Can I pick a color for each countdown task?

Yes. When adding or editing a task, choose one of **9 accent colors**. The list and **Countdown Tasks** widget use that color per row. Colors sync via iCloud when task sync is enabled.

### Can I filter statistics by a custom date range?

Yes. On the Statistics tab (or period report), pick **Custom** in the period bar, then set start and end dates. The range is saved when **Remember filter** is on in Statistics settings.

### Can I get a daily motivation notification?

Yes. **Settings → Motivational Quote Settings** includes an optional **daily motivation notification** — pick a time and iPomodoro schedules a repeating **local notification** with a random line from the on-device notification quote pool (no network). Separate from timer-completion alerts.

### What's the difference between daily quotes and notification quotes?

**Dialog/daily quotes** (**1000+** combined when filter is All — simplified Chinese + English) power the startup popup, settings browse, Live Activity hint, and Motivation widget. **Notification quotes** are a separate on-device pool (**365 general lines per language**) used only for background timer completion alerts. Both respect your quote language filter in Settings.

### What is the Pomodoro Technique?

The Pomodoro Technique is a time-management method: work in focused intervals (classically 25 minutes), then take a short break. After several cycles, take a longer break. iPomodoro automates this rhythm so you can focus on the work, not the clock.

### How is iPomodoro different from the old Flutter version?

This is a **complete SwiftUI rewrite** for Apple platforms. Same core ideas — Pomodoro, study timer, countdown tasks — but native performance, Live Activity, modern widgets, and tighter iOS integration.

### Do I need an account or internet connection?

No iPomodoro account is required. Timers, study statistics, themes, and widgets run **fully offline** on your device. **Optional:** enable **Sync tasks with iCloud** (Tasks → gear) and/or **Sync study statistics with iCloud** (Statistics → gear) to merge data across devices signed into the same Apple ID — this uses Apple CloudKit, not our servers. Internet is also used for App Store updates or feedback email.

### How does Study Statistics work?

Open the **Statistics** tab. Filter by All / Pomodoro / Study Timer and by Today / Week / Month / Year / All time / **Custom date range**. The dashboard shows **today's overview**, **goal progress**, week-over-week comparison, a **monthly heatmap**, **achievements**, weekday/time-of-day charts, and **breakdown by linked task**. Tap the **gear icon** for goals, optional **iCloud sync**, counting rules, **CSV export/import**, and data retention. Statistics are **never uploaded to our servers** (optional iCloud uses Apple CloudKit under your Apple ID).

### Can I export or import study statistics?

Yes. **Statistics tab → gear → Export** shares a CSV file via the system share sheet. **Import** accepts the same format (`kind,started_at,ended_at,duration_seconds,outcome` plus optional `task_id,task_title,cloud_id`) — choose **merge** (skip duplicates) or **replace all**. Useful for backup or manual migration. For automatic cross-device sync, enable **Sync study statistics with iCloud** instead.

### Can I share my stats as an image?

Yes. iPomodoro can render **branded snapshot cards** (focus metrics + App Store QR code) for the **Statistics dashboard** (toolbar share), **period reports**, **year-in-review** summaries, and **achievements** (full list or single badge). Statistics share cards use your **Statistics tab page theme** colors. You can also share an **app promotion card** from Settings → Share App.

### Can I sync study statistics with iCloud?

Yes — **Statistics tab → gear → Sync study statistics with iCloud**. This is **separate** from task iCloud sync. Sessions merge by `cloudId` across your Apple ID devices via CloudKit record type `StudySession`. **Daily goal settings** (`StatsGoals`) and **achievement unlock/celebration state** (`StatsAchievements`) sync under the same toggle when enabled.

### How do daily focus goals work?

**Statistics → gear → Goals**: set daily pomodoro count, daily focus minutes, and weekly focus minutes. Progress appears on the Statistics dashboard and the **Today's Stats** widget when enabled.

### How do I link a countdown task to a focus session?

On the Pomodoro or Study Timer screen, tap **Link task** and pick a task. Or from **Tasks**, long-press a task → **Focus with Pomodoro** or **Focus with Study Timer**. Completed sessions store the task title for **breakdown by task** in Statistics.

### How do I pin or reorder tasks?

In the **Tasks** tab, swipe a row to **Pin** or use the sort menu in the navigation bar. Enter reorder mode to **drag** tasks — sorting switches to custom order automatically. Pinned tasks appear in their own section at the top.

### How does iCloud task sync work?

Tasks tab → gear → toggle **Sync tasks with iCloud**. Tasks merge by last-modified time across your Apple ID devices. Pomodoro / study timers stay local. **Study statistics** can optionally sync separately (Statistics → gear). You must be signed into iCloud in iOS Settings. Sync also runs when you return to the app.

### What does the Statistics dashboard share image include?

Tap **Share** on the Statistics tab toolbar. The long card reflects your **current scope and period** filters — today's hero, goal progress, heatmap, weekday/hour charts, task breakdown, trend bars, and recent sessions — plus branding and an App Store QR code. Colors match your **Statistics tab page theme**.

### Can I customize the Statistics tab theme?

Yes. **Statistics tab → gear → Theme** — same title-bar and background gradient controls as Pomodoro, Study Timer, and Tasks. Default is focus red (`#E53935` / `#EF9A9A`). The Statistics tab tint, navigation bar, and **statistics share cards** all follow these page-theme colors.

### How do achievements work?

Nine local badges unlock as you hit milestones — first pomodoro, streaks, total pomodoros, focus hours, daily goal completion, and more. When you unlock a new badge, a **full-screen celebration** appears on the Statistics tab (tap **Continue** to dismiss). Open **Statistics → gear → Achievements** to browse the grid. **Tap a badge** for a detail sheet; share the **full list** from the achievements toolbar or a **single badge** from the detail screen. Badges are stored on-device; with iCloud sync enabled, unlock and celebration state merge across your devices via CloudKit — not uploaded to our servers.

### How do I browse past months on the focus heatmap?

On the Statistics dashboard, use **Previous / Next month** arrows on the heatmap card, tap the **month title** to open a **year + month picker** sheet, or tap **This month** to jump back to the current month.

### Why do future dates on the heatmap look different?

Days after today in the current month appear as **dashed-outline placeholders** with a lighter fill — they are not counted as focus days. Past days and today use the normal intensity colors.

### How do I add the Today's Stats widget?

Long-press Home Screen → **+** → search **iPomodoro** → add **Today's Stats** (Small, **Medium, Large**, or Lock Screen rectangular / inline). It shows today's focus, pomodoro & **weekly** goal progress, and streak.

### How do I add the tasks widget?

Long-press Home Screen → **+** → search **iPomodoro** → add **Countdown Tasks** (Small / Medium / Large). It shows upcoming pinned tasks and days remaining. Open the app after editing tasks for the fastest refresh.

### Can I refresh the motivation widget quote?

On **iOS 17+**, tap the **refresh** button on the Daily Motivation widget to pick another quote instantly without opening the app.

### Why don't notifications work?

Check **Settings tab → Notifications** for your current iOS permission status. Timer and task reminders require notification access. Open System Settings if permission was denied.

### How do I customize work and break durations?

Tap the **gear icon** on the Pomodoro tab → adjust stepper rows, or **tap the large timer digits** on the main screen to open a duration picker. Long break interval (every N pomodoros) is also configurable.

### What is Confirm phase completion?

**Pomodoro tab → gear → Confirm phase completion**. When **on**, iPomodoro shows a dialog after each work or break segment before starting the next phase. When **off** (default), the next phase starts automatically after the completion alarm — classic hands-free Pomodoro flow.

### How do Live Activity and Dynamic Island work?

Enable **Live Activity** separately in Pomodoro and Study Timer settings (gear icon). Each mode gets its **own** Lock Screen and Dynamic Island countdown — they never overwrite each other. While a session runs, you see a live countdown; when it completes, a brief celebration shows for 10 seconds. If iOS terminates the app while your timer still appears on the Lock Screen, reopening iPomodoro **restores** the session and jumps to the active tab — **unless** you launched via a **Home Screen Quick Action**, which takes priority.

### How do I add widgets?

Long-press the Home Screen → **+** → search for **iPomodoro** (or 爱番茄 / 愛番茄). Pick **iPomodoro · Pomodoro** or **iPomodoro · Study Timer** for timer countdowns (they are separate widgets), **Today's Stats** for daily focus progress, **Countdown Tasks** for deadlines, or **Daily Motivational Quote** for the daily quote. For step-by-step help, open **Settings → Widgets → How to Use**.

### Why doesn't my timer widget update?

Pomodoro and Study Timer are **separate widgets**. Start or pause a session in the **matching tab** and make sure you added the correct widget. iOS may delay refreshes to save battery — open the app once to sync faster.

### Where is the old timer widget?

Timers are now **iPomodoro · Pomodoro** and **iPomodoro · Study Timer**. Remove any old timer widget and add the new ones from the widget gallery.

### How does the daily motivation quote work?

One quote is selected deterministically each day using `(year × 400 + dayOfYear) % total`. Filter quote language under **Settings → Motivational Quote Settings → Motivational Quote Languages** (All / Simplified / Traditional / English). The same quote appears in the Motivation widget and Live Activity hint until midnight. Browse random quotes in **Settings → Motivational Quote Settings → Motivational Quote Anthology** (full-screen, one at a time).

### Can widget backgrounds follow my theme?

Yes. **Settings → Widgets → Widget background follows theme** mirrors your global accent gradient on Home and Lock Screen widgets. Turn it off for a clean white (light) or system dark background while keeping accent colors on titles.

### How do task due reminders work?

When creating or editing a task, enable **Due date reminder** and set a future target date/time. A local notification fires at that exact moment. Manage pending reminders under **Tasks tab → gear → Task due reminders** — tap a row to edit or **delete** the task from the bottom of the edit sheet. Swipe-to-delete on the task list still works too.

### How do I delete a task while editing?

Open a task from the list or from **Task due reminders**, then scroll to the bottom of the edit sheet and tap **Delete**. Confirm in the alert. New tasks (create flow) do not show a delete button.

### Why can't I enable a reminder for a past date?

If the target datetime has already passed, the reminder toggle is hidden and any existing reminder is disabled automatically — there is nothing meaningful left to schedule.

### Can I use a different language than my system?

Yes. Go to **Settings tab → Language** and pick English, Simplified Chinese, or Traditional Chinese. The app name on your Home Screen follows system language; in-app UI follows your in-app choice.

### Does the app collect my data?

No analytics, no tracking. Timers and study statistics stay on your device by default. Tasks and study sessions sync to **your iCloud** only if you enable the separate toggles. We do not receive your task or timer data on our servers. See our [Privacy Policy](privacy) for full details.

### Will macOS be supported?

macOS support is planned. The Xcode project already includes macOS SDK configuration; stay tuned for updates on the App Store.

### Still need help?

Contact us at [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com). We typically respond within 48 hours.

</section>

<section lang="zh-CN" markdown="1">

### 为什么选爱番茄而不是其他番茄钟？

爱番茄是面向 Apple 平台的 **SwiftUI 原生应用**——不是套壳网页计时器。你得到 **五个一体 Tab**（番茄、计时、定任务、统计、设置）、**双 Live Activity**、**五类小组件**、**9 枚成就**、**1000+ 本地语录**、**Siri 与 URL 快捷方式**、**可选 iCloud 同步**——全程 **零统计 SDK**、**无需账号**。一款原生 App，从专注到截止日到进步追踪，一站搞定。

### 计时和任务设置在哪里？

各 Tab **齿轮** 内：番茄/计时的时长、声音、Live Activity、页面主题、可选 **专注模式联动**、番茄专属 **阶段完成确认**；定任务的排序、iCloud、到期提醒等；**统计 Tab 齿轮** 还含 **主题样式**。全局 **设置 Tab** 管外观、语言、**主屏快捷操作**、**应用指南**、通知权限、励志语（含 **每日励志通知**）、小组件教程、反馈与关于——不含各模式时长。**统计设置**（主题、目标、可选 iCloud、成就、计数规则、CSV、保留策略）在 **统计 Tab → 齿轮**。

### 主屏快捷操作和 Siri 怎么用？

**长按 App 图标** 可快速打开番茄/计时/定任务/统计、励志语录或反馈。在 **设置 → 应用设置 → 主屏快捷操作** 中自选最多 4 项并排顺序。亦可通过 **`iPomodoro://`** URL 打开相同入口（`pomodoro`、`study`、`tasks`、`stats`、`motivation`、`feedback`；亦支持 `iPomodoros://`）。完整说明见 [URL Scheme 文档](url-scheme)。**Siri / 快捷指令** 可打开各 Tab，或询问 *「爱番茄今天专注了多久」*。

### 应用指南是什么？

**设置 → 应用设置 → 应用指南** — 折叠式教程，涵盖五 Tab、小组件、快捷入口、iCloud 与 FAQ。

### 爱番茄能帮我打开专注模式吗？

不能——iOS 不允许第三方 App 直接开启 Focus。可在番茄/计时 **齿轮** 开启 **专注模式联动**：开始计时时若 Focus 未开，会弹窗提醒；可从 alert 跳转 **系统设置** 手动开启。

### 定任务可以选颜色吗？

可以。添加或编辑任务时从 **9 种 accent 色** 中选择；列表与 **定任务 Widget** 按任务色显示；开启 iCloud 同步时一并同步。

### 统计能按自定义日期筛选吗？

可以。统计 Tab（或周期报告）周期栏选 **自定义**，再设定起止日期；开启「记住筛选」后会保存范围。

### 能设置每日励志通知吗？

可以。**设置 → 励志语设置** 中有可选 **每日励志通知** — 选择固定时间后，App 会按 repeating 本地通知推送一条 notification 语录（设备本地语料，不经网络），与计时结束推送独立。

### 每日语录和通知语录有什么区别？

**弹窗/每日语料**（「全部」筛选合计 **1000+**，简体 + 英文）用于启动弹窗、设置浏览、Live Activity hint、励志小组件。**通知语料**是独立池（**中/英各 365 条通用短句**），仅用于后台计时结束推送。两者都遵循设置中的语录语言筛选。

### 什么是番茄工作法？

番茄工作法是一种时间管理方法：在一段专注时间内（经典为 25 分钟）深度工作，然后短休息；若干轮后进行一次长休息。爱番茄自动帮你切换节奏，让你专注内容，而不是盯时钟。

### 爱番茄和以前的 Flutter 版有什么区别？

这是面向 Apple 平台的 **SwiftUI 全面重写**。核心理念相同——番茄、计时、倒数任务——但原生性能、Live Activity、现代小组件与更紧密的系统集成。

### 需要账号或联网吗？

不需要爱番茄账号。计时、**学习统计**、主题、小组件均可 **完全离线** 在设备本地运行。**可选：** 在定任务 → 齿轮开启 **通过 iCloud 同步定任务**，或在统计 → 齿轮开启 **通过 iCloud 同步学习统计**（独立开关），经 Apple CloudKit 在同一 Apple ID 设备间合并——不经过我们的服务器。联网亦用于 App Store 更新或反馈邮件。

### 学习统计怎么用？

打开 **统计** Tab，按全部/番茄/计时与今天/本周/本月/今年/全部/**自定义日期**筛选。仪表盘含 **今日概览**、**目标进度**、周对比、**月历热力图**、**成就**、星期/时段分布与 **按任务拆分**。点右上角 **齿轮** 可设目标、可选 **iCloud 同步**、计数规则、**CSV 导出/导入**与数据保留。**统计数据不会上传到我们的服务器**（可选 iCloud 经 Apple CloudKit 在你的 Apple ID 下同步）。

### 能否导出或导入学习统计？

可以。**统计 Tab → 齿轮 → 导出** 通过系统分享 Sheet 导出 CSV；**导入** 支持相同格式（`kind,started_at,ended_at,duration_seconds,outcome`，可选 `task_id,task_title,cloud_id`），可选 **合并**（跳过重复）或 **全部替换**。适合手动备份或迁移。跨设备自动同步请开启 **通过 iCloud 同步学习统计**。

### 能把学习统计分享成图片吗？

可以。爱番茄可离屏渲染 **品牌化快照卡片**（专注数据 + App Store 二维码），用于 **统计 Tab 仪表盘长图**、**周期报告**、**年度回顾** 与 **成就列表/单枚**。统计类分享图配色跟随 **统计 Tab 页面主题**。统计 Tab 点工具栏分享即可；成就页/报告页也可单独分享。设置页 **分享应用** 可生成带 QR 的应用推广卡。

### 学习统计能 iCloud 同步吗？

可以——**统计 Tab → 齿轮 → 通过 iCloud 同步学习统计**，与定任务 iCloud **独立开关**。会话经 CloudKit `StudySession` 类型按 `cloudId` 在 Apple ID 设备间合并；**日/周目标**（`StatsGoals`）与 **成就解锁/庆祝状态**（`StatsAchievements`）在同一开关下同步。

### 每日专注目标怎么用？

**统计 → 齿轮 → 目标**：设置日番茄数、日专注分钟、周专注分钟；开启后在统计 Tab 与 **今日统计** 小组件显示进度。

### 如何把定任务关联到一次专注？

番茄/计时屏点 **关联任务** 选择；或在 **定任务** 长按 → **番茄专注** / **计时专注**。完成的会话会记录任务名，统计页可按任务拆分。

### 如何置顶或排序任务？

在 **定任务** Tab 左滑 **置顶**，或用导航栏排序 Menu；进入排序模式 **拖拽** 行即可——自动切换为「自定义顺序」。置顶任务单独成区显示在顶部。

### iCloud 任务同步如何工作？

定任务 → 齿轮 → 开启 **通过 iCloud 同步定任务**。按最后修改时间合并同一 Apple ID 下的设备。番茄/计时仍仅本地。**学习统计** 可单独在统计 → 齿轮中开启 iCloud 同步。需在 iOS 设置登录 iCloud；回到 App 时也会自动同步。

### 统计 Tab 分享的仪表盘长图包含什么？

在 **统计 Tab** 点工具栏 **分享**。长图会反映你当前的 **范围与周期** 筛选——今日概览、目标进度、热力图、星期/时段分布、任务拆分、趋势柱与最近会话等，并附带品牌信息与 App Store 二维码。配色跟随 **统计 Tab 页面主题**。

### 统计 Tab 能自定义主题色吗？

可以。**统计 Tab → 齿轮 → 主题样式** — 与番茄/计时/定任务相同的标题栏与背景渐变设置。默认专注红（`#E53935` / `#EF9A9A`）。统计 Tab 选中色、导航栏与 **统计类分享图** 均跟随该页面主题。

### 成就如何解锁？

共 9 枚本地成就——首个番茄、连续专注 streak、累计番茄/专注时长、达成日目标等。新解锁时统计 Tab 会弹出 **全屏庆祝**（点「继续」关闭）。进入 **统计 → 齿轮 → 成就** 浏览网格；**点击徽章** 打开详情 Sheet。成就页工具栏可 **分享成就列表**，详情页可 **分享单枚徽章**。开启 iCloud 同步后，解锁与庆祝状态经 CloudKit 在设备间合并；不上传至我们的服务器。

### 热力图如何查看历史月份？

在统计仪表盘热力图卡片上，用 **上/下月** 箭头切换，**点按月份标题** 打开 **年/月选择** Sheet 快速跳转，或点 **回到本月** 返回当前月。

### 热力图里未来日期为什么样式不同？

当月 **今天之后** 的格子以 **虚线边框 + 浅色占位** 显示，不计入专注数据；今天及过去日期仍按强度着色。

### 如何添加「今日统计」小组件？

长按主屏幕 → **+** → 搜索 **爱番茄** → 添加 **今日统计**（小/中/大或锁屏矩形/行内）。展示今日专注、番茄与**周**目标进度、连续 streak。

### 如何添加定任务小组件？

长按主屏幕 → **+** → 搜索 **爱番茄** → 添加 **定任务**（小/中/大），展示置顶优先的倒数日与剩余天数。编辑任务后打开 App 可更快刷新。

### 励志小组件能换一句吗？

**iOS 17+** 可点励志 Widget 上的 **刷新** 按钮，无需打开 App 即换一句。

### 为什么收不到通知？

查看 **设置 Tab → 通知** 中的 iOS 授权状态。计时与任务提醒需通知权限；若已拒绝请前往系统设置开启。

### 如何自定义工作与休息时长？

在番茄 Tab 点 **齿轮** → 调整 Stepper 行，或直接 **点按主屏大号计时数字** 打开滚轮选择器。长休息间隔（每 N 个番茄）也可配置。

### 什么是「阶段完成确认」？

**番茄 Tab → 齿轮 → 阶段完成确认**。开启后，每段工作或休息结束会弹窗确认再进入下一阶段；关闭（默认）则在提示音后自动进入下一阶段，适合免打扰连续番茄。

### Live Activity 和灵动岛怎么用？

在番茄或计时的 **齿轮 → Live Activity** 中**分别**开启。两种模式各自拥有锁屏与（支持的 iPhone）灵动岛倒计时，互不覆盖。会话运行中显示实时倒计时；完成后约 10 秒祝贺态后消失。若系统在计时进行中终止 App 而锁屏仍显示倒计时，重新打开爱番茄会**恢复**会话并跳转到对应 Tab——**除非**通过 **主屏 Quick Action** 启动，快捷操作优先于自动切 Tab。

### 如何添加小组件？

长按主屏幕 → **+** → 搜索 **爱番茄**（或 iPomodoro）。选择 **爱番茄 · 番茄钟** 或 **爱番茄 · 学习计时**（两款独立计时组件）、**今日统计**、**定任务** 或 **今日励志语录**。详细步骤见 **设置 → 小组件 → 使用教程**。

### 计时小组件为什么不更新？

番茄钟与学习计时是**两款独立小组件**。请在**对应 Tab** 开始或暂停计时，并确认添加的是正确的那一款。为省电，系统可能稍晚才刷新——打开 App 可更快同步。

### 找不到原来的计时小组件？

计时已拆分为 **爱番茄 · 番茄钟** 与 **爱番茄 · 学习计时**。请删除旧组件后从组件库重新添加。

### 每日励志语录如何选取？

每日一句由 `(year × 400 + dayOfYear) % 总数` 确定。在 **设置 → 励志语设置 → 励志语录语言** 中筛选（全部 / 仅简体 / 仅繁体 / 仅英文）。励志小组件与 Live Activity hint 共用同一句，到零点切换。在 **设置 → 励志语设置 → 励志语录大全** 全屏随机浏览（一次一条）。

### 小组件背景能跟随主题色吗？

可以。**设置 → 小组件 → 小组件背景跟随主题色** 会让主屏/锁屏组件背景与全局强调色渐变一致；关闭后浅色白底/深色系统底，标题强调色仍跟主题。

### 任务到期提醒如何工作？

创建或编辑任务时开启 **到期提醒** 并设定未来的目标时间，到点触发本地通知。在 **定任务 Tab → 齿轮 → 任务到期提醒** 中管理待触发列表；点进编辑 Sheet 后可在底部 **删除** 任务（列表左滑删除仍可用）。

### 编辑任务时如何删除？

从任务列表或 **任务到期提醒** 进入编辑页，滚动至 Sheet 底部点 **删除** 并确认。新建任务流程不显示删除按钮。

### 为什么过去的时间不能开提醒？

目标时刻已过时，提醒开关会隐藏并自动关闭——没有可合理调度的通知。

### 能否使用与系统不同的语言？

可以。**设置 Tab → 语言** 中选择 English、简体中文或繁體中文。主屏幕应用名跟随系统语言；App 内界面跟随 App 内选择。

### 应用会收集我的数据吗？

无统计、无追踪。计时与学习统计默认留在设备本地。定任务与学习统计仅在你分别开启 iCloud 同步时合并到 **你的 iCloud**。我们不会在我们的服务器收到你的任务或计时数据。详见 [隐私政策](privacy)。

### 会支持 macOS 吗？

macOS 版本在规划中，Xcode 工程已预留 SDK 配置，请关注 App Store 动态。

### 仍需帮助？

请联系 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) ，我们通常 48 小时内回复。

</section>

<section lang="zh-TW" markdown="1">

### 為什麼選愛番茄而不是其他番茄鐘？

愛番茄是面向 Apple 平台的 **SwiftUI 原生應用**——不是套殼網頁計時器。你得到 **五個一體 Tab**（番茄、計時、定任務、統計、設定）、**雙 Live Activity**、**五類小工具**、**9 枚成就**、**1000+ 本地語錄**、**Siri 與 URL 捷徑**、**可選 iCloud 同步**——全程 **零統計 SDK**、**無需帳號**。一款原生 App，從專注到截止日到進步追蹤，一站搞定。

### 計時和任務設定在哪裡？

各 Tab **齒輪** 內：番茄/計時的時長、聲音、Live Activity、頁面主題、可選 **專注模式聯動**、番茄專屬 **階段完成確認**；定任務的排序、iCloud、到期提醒等；**統計 Tab 齒輪** 還含 **主題樣式**。全域 **設定 Tab** 管外觀、語言、**主畫面快捷操作**、**應用指南**、通知權限、勵志語（含 **每日勵志通知**）、小工具教學、回饋與關於——不含各模式時長。**統計設定**（主題、目標、可選 iCloud、成就、計數規則、CSV、保留策略）在 **統計 Tab → 齒輪**。

### 主畫面快捷操作和 Siri 怎麼用？

**長按 App 圖示** 可快速開啟番茄/計時/定任務/統計、勵志語錄或回饋。在 **設定 → 應用設定 → 主畫面快捷操作** 中自選最多 4 項並排序。亦可透過 **`iPomodoro://`** URL 開啟相同入口（`pomodoro`、`study`、`tasks`、`stats`、`motivation`、`feedback`；亦支援 `iPomodoros://`）。完整說明見 [URL Scheme 文件](url-scheme)。**Siri / 快捷指令** 可開啟各 Tab，或詢問 *「愛番茄今天專注了多久」*。

### 應用指南是什麼？

**設定 → 應用設定 → 應用指南** — 摺疊式教學，涵蓋五 Tab、小工具、快捷入口、iCloud 與 FAQ。

### 愛番茄能幫我開啟專注模式嗎？

不能——iOS 不允許第三方 App 直接開啟 Focus。可在番茄/計時 **齒輪** 開啟 **專注模式聯動**：開始計時時若 Focus 未開，會彈窗提醒；可從 alert 跳轉 **系統設定** 手動開啟。

### 定任務可以選顏色嗎？

可以。新增或編輯任務時從 **9 種 accent 色** 中選擇；列表與 **定任務 Widget** 按任務色顯示；開啟 iCloud 同步時一併同步。

### 統計能按自訂日期篩選嗎？

可以。統計 Tab（或週期報告）週期欄選 **自訂**，再設定起訖日期；開啟「記住篩選」後會保存範圍。

### 能設定每日勵志通知嗎？

可以。**設定 → 勵志語錄設定** 中有可選 **每日勵志通知** — 選擇固定時間後，App 會以 repeating 本地通知推送一則 notification 語錄（裝置本地語料，不經網路），與計時結束推送獨立。

### 每日語錄和通知語錄有什麼區別？

**彈窗/每日語料**（「全部」篩選合計 **1000+**，簡體 + 英文）用於啟動彈窗、設定瀏覽、Live Activity hint、勵志小工具。**通知語料**是獨立池（**中/英各 365 條通用短句**），僅用於背景計時結束推送。兩者都遵循設定中的語錄語言篩選。

### 什麼是番茄工作法？

番茄工作法是一種時間管理方法：在一段專注時間內（經典為 25 分鐘）深度工作，然後短休息；若干輪後進行一次長休息。愛番茄自動幫你切換節奏，讓你專注內容，而不是盯時鐘。

### 愛番茄和以前的 Flutter 版有什麼區別？

這是面向 Apple 平台的 **SwiftUI 全面重寫**。核心理念相同——番茄、計時、倒數任務——但原生效能、Live Activity、現代小工具與更緊密的系統整合。

### 需要帳號或連網嗎？

不需要愛番茄帳號。計時、**學習統計**、主題、小工具均可 **完全離線** 在裝置本地運行。**可選：** 在定任務 → 齒輪開啟 **透過 iCloud 同步定任務**，或在統計 → 齒輪開啟 **透過 iCloud 同步學習統計**（獨立開關），經 Apple CloudKit 在同一 Apple ID 裝置間合併——不經過我們的伺服器。連網亦用於 App Store 更新或回饋郵件。

### 學習統計怎麼用？

開啟 **統計** Tab，按全部/番茄/計時與今天/本週/本月/今年/全部/**自訂日期**篩選。儀表板含 **今日概覽**、**目標進度**、週對比、**月曆熱力圖**、**成就**、星期/時段分布與 **按任務拆分**。點右上角 **齒輪** 可設目標、可選 **iCloud 同步**、計數規則、**CSV 匯入/匯出**與資料保留。**統計資料不會上傳到我們的伺服器**（可選 iCloud 經 Apple CloudKit 在你的 Apple ID 下同步）。

### 能否匯出或匯入學習統計？

可以。**統計 Tab → 齒輪 → 匯出** 透過系統分享 Sheet 匯出 CSV；**匯入** 支援相同格式（`kind,started_at,ended_at,duration_seconds,outcome`，可選 `task_id,task_title,cloud_id`），可選 **合併**（跳過重複）或 **全部替換**。適合手動備份或遷移。跨裝置自動同步請開啟 **透過 iCloud 同步學習統計**。

### 能把學習統計分享成圖片嗎？

可以。愛番茄可離屏渲染 **品牌化快照卡片**（專注數據 + App Store QR Code），用於 **統計 Tab 儀表板長圖**、**週期報告**、**年度回顧** 與 **成就列表/單枚**。統計類分享圖配色跟隨 **統計 Tab 頁面主題**。統計 Tab 點工具列分享即可；成就頁/報告頁也可單獨分享。設定頁 **分享應用** 可生成帶 QR 的應用推廣卡。

### 學習統計能 iCloud 同步嗎？

可以——**統計 Tab → 齒輪 → 透過 iCloud 同步學習統計**，與定任務 iCloud **獨立開關**。工作階段經 CloudKit `StudySession` 類型按 `cloudId` 在 Apple ID 裝置間合併；**日/週目標**（`StatsGoals`）與 **成就解鎖/慶祝狀態**（`StatsAchievements`）在同一開關下同步。

### 每日專注目標怎麼用？

**統計 → 齒輪 → 目標**：設定日番茄數、日專注分鐘、週專注分鐘；開啟後在統計 Tab 與 **今日統計** 小工具顯示進度。

### 如何把定任務關聯到一次專注？

番茄/計時屏點 **關聯任務** 選擇；或在 **定任務** 長按 → **番茄專注** / **計時專注**。完成的會話會記錄任務名，統計頁可按任務拆分。

### 如何置頂或排序任務？

在 **定任務** Tab 左滑 **置頂**，或用導覽列排序 Menu；進入排序模式 **拖曳** 列即可——自動切換為「自訂順序」。置頂任務單獨成區顯示在頂部。

### iCloud 任務同步如何運作？

定任務 → 齒輪 → 開啟 **透過 iCloud 同步定任務**。按最後修改時間合併同一 Apple ID 下的裝置。番茄/計時仍僅本地。**學習統計** 可單獨在統計 → 齒輪中開啟 iCloud 同步。需在 iOS 設定登入 iCloud；回到 App 時也會自動同步。

### 統計 Tab 分享的儀表板長圖包含什麼？

在 **統計 Tab** 點工具列 **分享**。長圖會反映你目前的 **範圍與週期** 篩選——今日概覽、目標進度、熱力圖、星期/時段分布、任務拆分、趨勢柱與最近工作階段等，並附帶品牌資訊與 App Store QR Code。配色跟隨 **統計 Tab 頁面主題**。

### 統計 Tab 能自訂主題色嗎？

可以。**統計 Tab → 齒輪 → 主題樣式** — 與番茄/計時/定任務相同的標題列與背景漸層設定。預設專注紅（`#E53935` / `#EF9A9A`）。統計 Tab 選中色、導覽列與 **統計類分享圖** 均跟隨該頁面主題。

### 成就如何解鎖？

共 9 枚本地成就——首個番茄、連續專注 streak、累計番茄/專注時長、達成日目標等。新解鎖時統計 Tab 會彈出 **全螢幕慶祝**（點「繼續」關閉）。進入 **統計 → 齒輪 → 成就** 瀏覽網格；**點擊徽章** 開啟詳情 Sheet。成就頁工具列可 **分享成就列表**，詳情頁可 **分享單枚徽章**。開啟 iCloud 同步後，解鎖與慶祝狀態經 CloudKit 在裝置間合併；不上傳至我們的伺服器。

### 熱力圖如何查看歷史月份？

在統計儀表板熱力圖卡片上，用 **上/下月** 箭頭切換，**點按月份標題** 開啟 **年/月選擇** Sheet 快速跳轉，或點 **回到本月** 返回目前月份。

### 熱力圖裡未來日期為什麼樣式不同？

當月 **今天之後** 的格子以 **虛線邊框 + 淺色占位** 顯示，不計入專注資料；今天及過去日期仍依強度著色。

### 如何新增「今日統計」小工具？

長按主畫面 → **+** → 搜尋 **愛番茄** → 新增 **今日統計**（小/中/大或鎖定畫面矩形/行內）。展示今日專注、番茄與**週**目標進度、連續 streak。

### 如何新增定任務小工具？

長按主畫面 → **+** → 搜尋 **愛番茄** → 新增 **定任務**（小/中/大），展示置頂優先的倒數日與剩餘天數。編輯任務後開啟 App 可更快重新整理。

### 勵志小工具能換一句嗎？

**iOS 17+** 可點勵志 Widget 上的 **重新整理** 按鈕，無需開啟 App 即換一句。

### 為什麼收不到通知？

查看 **設定 Tab → 通知** 中的 iOS 授權狀態。計時與任務提醒需通知權限；若已拒絕請前往系統設定開啟。

### 如何自訂工作與休息時長？

在番茄 Tab 點 **齒輪** → 調整 Stepper 列，或直接 **點按主畫面大型計時數字** 開啟滾輪選擇器。長休息間隔（每 N 個番茄）也可設定。

### 什麼是「階段完成確認」？

**番茄 Tab → 齒輪 → 階段完成確認**。開啟後，每段工作或休息結束會彈窗確認再進入下一階段；關閉（預設）則在提示音後自動進入下一階段，適合免打擾連續番茄。

### Live Activity 和靈動島怎麼用？

在番茄或計時的 **齒輪 → Live Activity** 中**分別**啟用。兩種模式各自擁有鎖定畫面與（支援的 iPhone）靈動島倒數，互不重疊。工作階段執行中顯示即時倒數；完成後約 10 秒祝賀態後消失。若系統在計時進行中終止 App 而鎖定畫面仍顯示倒數，重新開啟愛番茄會**恢復**工作階段並跳轉到對應 Tab——**除非**透過 **主畫面 Quick Action** 啟動，快捷操作優先於自動切 Tab。

### 如何新增小工具？

長按主畫面 → **+** → 搜尋 **愛番茄**（或 iPomodoro）。選擇 **愛番茄 · 番茄鐘** 或 **愛番茄 · 學習計時**（兩款獨立計時元件）、**今日統計**、**定任務** 或 **今日勵志語錄**。詳細步驟見 **設定 → 小工具 → 使用教學**。

### 計時小工具為什麼不更新？

番茄鐘與學習計時是**兩款獨立小工具**。請在**對應 Tab** 開始或暫停計時，並確認新增的是正確的那一款。為省電，系統可能稍晚才重新整理——開啟 App 可更快同步。

### 找不到原來的計時小工具？

計時已拆分為 **愛番茄 · 番茄鐘** 與 **愛番茄 · 學習計時**。請刪除舊元件後從元件庫重新新增。

### 每日勵志語錄如何選取？

每日一句由 `(year × 400 + dayOfYear) % 總數` 確定。在 **設定 → 勵志語錄設定 → 勵志語錄語言** 中篩選（全部 / 僅簡體 / 僅繁體 / 僅英文）。勵志小工具與 Live Activity hint 共用同一句，到零點切換。在 **設定 → 勵志語錄設定 → 勵志語錄大全** 全螢幕隨機瀏覽（一次一條）。

### 小工具背景能跟隨主題色嗎？

可以。**設定 → 小工具 → 小工具背景跟隨主題色** 會讓主畫面/鎖定畫面元件背景與全域強調色漸層一致；關閉後淺色白底/深色系統底，標題強調色仍跟主題。

### 任務到期提醒如何運作？

建立或編輯任務時開啟 **到期提醒** 並設定未來的目標時間，到點觸發本地通知。在 **定任務 Tab → 齒輪 → 任務到期提醒** 中管理待觸發列表；點進編輯 Sheet 後可在底部 **刪除** 任務（列表左滑刪除仍可用）。

### 編輯任務時如何刪除？

從任務列表或 **任務到期提醒** 進入編輯頁，捲動至 Sheet 底部點 **刪除** 並確認。新建任務流程不顯示刪除按鈕。

### 為什麼過去的時間不能開提醒？

目標時刻已過時，提醒開關會隱藏並自動關閉——沒有可合理排程的通知。

### 能否使用與系統不同的語言？

可以。**設定 Tab → 語言** 中選擇 English、简体中文 或 繁體中文。主畫面應用名跟隨系統語言；App 內介面跟隨 App 內選擇。

### 應用會收集我的資料嗎？

無統計、無追蹤。計時與學習統計預設留在裝置本地。定任務與學習統計僅在你分別開啟 iCloud 同步時合併到 **你的 iCloud**。我們不會在我們的伺服器收到你的任務或計時資料。詳見 [隱私政策](privacy)。

### 會支援 macOS 嗎？

macOS 版本在規劃中，Xcode 工程已預留 SDK 設定，請關注 App Store 動態。

### 仍需協助？

請聯絡 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) ，我們通常 48 小時內回覆。

</section>
