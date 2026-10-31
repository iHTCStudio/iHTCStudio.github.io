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

**Long-press the app icon** for Quick Actions — open Pomodoro, Study Timer, Tasks, Statistics, a motivation quote, or feedback. Customize which four appear under **Settings → App settings → Home Screen shortcuts** (drag to reorder). You can also open the same destinations via **`iPomodoro://`** URLs (`pomodoro`, `study`, `tasks`, `stats`, `motivation`, `feedback`; `iPomodoros://` also works). See the full [URL Scheme Reference](../url-scheme). **Siri / Shortcuts app** can open tabs or answer *"How long did I focus today in iPomodoro?"* via built-in App Shortcuts.

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

No analytics, no tracking. Timers and study statistics stay on your device by default. Tasks and study sessions sync to **your iCloud** only if you enable the separate toggles. We do not receive your task or timer data on our servers. See our [Privacy Policy](../privacy) for full details.

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

**长按 App 图标** 可快速打开番茄/计时/定任务/统计、励志语录或反馈。在 **设置 → 应用设置 → 主屏快捷操作** 中自选最多 4 项并排顺序。亦可通过 **`iPomodoro://`** URL 打开相同入口（`pomodoro`、`study`、`tasks`、`stats`、`motivation`、`feedback`；亦支持 `iPomodoros://`）。完整说明见 [URL Scheme 文档](../url-scheme)。**Siri / 快捷指令** 可打开各 Tab，或询问 *「爱番茄今天专注了多久」*。

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

无统计、无追踪。计时与学习统计默认留在设备本地。定任务与学习统计仅在你分别开启 iCloud 同步时合并到 **你的 iCloud**。我们不会在我们的服务器收到你的任务或计时数据。详见 [隐私政策](../privacy)。

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

**長按 App 圖示** 可快速開啟番茄/計時/定任務/統計、勵志語錄或回饋。在 **設定 → 應用設定 → 主畫面快捷操作** 中自選最多 4 項並排序。亦可透過 **`iPomodoro://`** URL 開啟相同入口（`pomodoro`、`study`、`tasks`、`stats`、`motivation`、`feedback`；亦支援 `iPomodoros://`）。完整說明見 [URL Scheme 文件](../url-scheme)。**Siri / 快捷指令** 可開啟各 Tab，或詢問 *「愛番茄今天專注了多久」*。

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

無統計、無追蹤。計時與學習統計預設留在裝置本地。定任務與學習統計僅在你分別開啟 iCloud 同步時合併到 **你的 iCloud**。我們不會在我們的伺服器收到你的任務或計時資料。詳見 [隱私政策](../privacy)。

### 會支援 macOS 嗎？

macOS 版本在規劃中，Xcode 工程已預留 SDK 設定，請關注 App Store 動態。

### 仍需協助？

請聯絡 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) ，我們通常 48 小時內回覆。

</section>
<section lang="ja" markdown="1">

### なぜ他のポモドーロアプリではなくiPomodoroを選ぶべきなのですか？

iPomodoroはAppleプラットフォーム向けに作られた**ネイティブSwiftUIアプリ**であり、ウェブタイマーのラップ版ではありません。**5つの統合タブ**（ポモドーロ、勉強タイマー、タスク、統計、設定）、**2つのライブアクティビティ**、**5種類のウィジェット**、**9つの達成バッジ**、**1000以上のデバイス内名言**、**Siri & URLショートカット**、**オプションのiCloud同期**を全て**分析データゼロ**かつ**アカウント不要**で利用できます。一つのシンプルなアプリで、集中、締め切り、進捗管理を全面的にカバーします。

### タイマーとタスクの設定はどこにありますか？

タイマーの時間設定、サウンド、ライブアクティビティ、ページテーマの色、任意の**フォーカスモード通知**、そして（ポモドーロのみ）任意の**フェーズ完了確認**は、各タブの**歯車アイコン**（ポモドーロ、スタディタイマー、タスク、または**統計**）の下にあります。グローバルな**設定**タブには、外観、言語、**ホーム画面ショートカット**、**アプリガイド**、通知許可、モチベーショナルクォート（**毎日のモチベーション通知**を含む）、ウィジェットガイド、フィードバック、アプリ情報があり、モードごとの時間設定はありません。**統計**の設定（ページテーマ、目標、任意のiCloud同期、実績、カウントルール、CSV、保持期間）は**統計タブ → 歯車**の下にあります。

### ホーム画面ショートカットとSiriはどのように機能しますか？

**アプリ アイコンを長押し**すると、クイック アクションが表示されます。ポモドーロ、学習タイマー、タスク、統計、モチベーションの引用、またはフィードバックが開きます。 **[設定] → [アプリ設定] → [ホーム画面のショートカット]** に表示される 4 つのショートカットをカスタマイズします (ドラッグして順序を変更します)。 **`iPomodoro://`** URL 経由で同じ宛先を開くこともできます (`pomodoro`、`study`、`tasks`、`stats`、`motivation`、`feedback`、`iPomodoros://` も機能します)。 完全な [URL スキーム リファレンス](../url-scheme) を参照してください。 **Siri / ショートカット アプリ** は、内蔵のアプリ ショートカットを使用してタブを開いたり、*「今日 iPomodoro でどのくらい集中しましたか?」* に答えたりすることができます。 

### アプリ内アプリガイドとは何ですか?

 **設定 → アプリ設定 → アプリガイド** — 5 つのタブすべて、ウィジェット、ショートカット、iCloud、および FAQ (ウィ​​ジェット ガイドと同様のスタイル) をカバーする折りたたみ可能なチュートリアル。 

### iPomodoro でフォーカス モードをオンにできますか?

 いいえ — iOS では、サードパーティ アプリが Focus を直接有効にすることを許可していません。 オプションの **フォーカス モード リマインダー** (ポモドーロまたはスタディ タイマーのギア設定) は、タイマーの開始時にフォーカスがオフになっているかどうかを確認し、アラートを表示します。 アラートから **設定** を開くことはできますが、自分でフォーカスをオンにする必要があります。 

### 各カウントダウン タスクの色を選択できますか?

はい。タスクを追加または編集する際に、**9つのアクセントカラー**のいずれかを選択できます。リストと**カウントダウンタスク**ウィジェットでは、その色が行ごとに使用されます。タスク同期が有効になっている場合、色はiCloudを通じて同期されます。

### カスタム日付範囲で統計をフィルターできますか？

はい。統計タブ（または期間レポート）で、期間バーから**カスタム**を選び、開始日と終了日を設定します。統計設定で**フィルターを記憶**がオンになっている場合、範囲は保存されます。

### 毎日のモチベーション通知はもらえますか？

はい。**設定 → モチベーションクォート設定**には、任意の**毎日のモチベーション通知**があります — 時間を選ぶと、iPomodoroがデバイス上の通知クォートプールからランダムな一文とともに繰り返しの**ローカル通知**をスケジュールします（ネットワーク不要）。タイマー完了時のアラートとは別です。

### デイリークォートと通知クォートの違いは何ですか？

**ダイアログ／日替わり名言**（フィルターが「すべて」の時に**1000以上** — 簡体字中国語＋英語） は、起動時ポップアップ、設定ブラウズ、ライブアクティビティのヒント、モチベーションウィジェットに使用されます。**通知用名言**は別のデバイス内プール（言語ごとに一般的なフレーズ365個）で、バックグラウンドタイマーの完了通知にのみ使用されます。両方とも設定の名言言語フィルターを尊重します。

### ポモドーロ・テクニックとは？

ポモドーロ・テクニックは時間管理の方法です：集中して作業する時間（古典的には25分）と短い休憩を交互に行います。複数回サイクルを繰り返した後、長めの休憩をとります。iPomodoroはこのリズムを自動化し、時計ではなく作業に集中できるようにします。

### iPomodoroは旧Flutter版とどう違うのですか？

これはAppleプラットフォーム向けの**完全なSwiftUIによる書き直し**です。コアアイデアは同じ — ポモドーロ、学習タイマー、カウントダウンタスク — ですが、ネイティブパフォーマンス、ライブアクティビティ、最新ウィジェット、より緊密なiOS統合を実現しています。

### アカウントやインターネット接続は必要ですか？

iPomodoro アカウントは必要ありません。 タイマー、研究統計、テーマ、ウィジェットは、デバイス上で**完全にオフライン**で実行されます。 **オプション:** **iCloud とタスクを同期** (タスク → ギア) および/または **研究統計を iCloud と同期** (統計 → ギア) を有効にして、同じ Apple ID にサインインしているデバイス間でデータを結合します。これにはサーバーではなく Apple CloudKit が使用されます。 インターネットは、App Store のアップデートやフィードバックの電子メールにも使用されます。 

### 研究統計はどのように機能しますか?

 [**統計**] タブを開きます。 すべて / ポモドーロ / 学習タイマー、および今日 / 週 / 月 / 年 / すべての時間 / **カスタム日付範囲** でフィルターします。 ダッシュボードには、**今日の概要**、**目標の進捗状況**、前週比比較、**月次ヒートマップ**、**実績**、曜日/時間帯グラフ、**リンクされたタスク別の内訳**が表示されます。 **歯車アイコン**をタップして、目標、オプションの**iCloud同期**、カウントルール、**CSVエクスポート/インポート**、およびデータ保持を設定します。 統計情報は **当社のサーバーにアップロードされることはありません** (オプションの iCloud は Apple ID で Apple CloudKit を使用します)。 

### 研究統計をエクスポートまたはインポートできますか?

はい。 **統計タブ→ギア→エクスポート**は、システム共有シートを介して CSV ファイルを共有します。 **インポート** は同じ形式 (`kind,started_at,ended_at,duration_seconds,outcome` とオプションの `task_id,task_title,cloud_id`) を受け入れます。**マージ** (重複をスキップ) または **すべて置換** を選択します。 バックアップまたは手動移行に役立ちます。 デバイス間で自動同期するには、代わりに **研究統計を iCloud と同期する** を有効にしてください。 

### 私の統計を画像として共有できますか?

 はい。 iPomodoro は、**統計ダッシュボード** (ツールバー共有)、**期間レポート**、**年間レビュー** 概要、**実績** (完全なリストまたは 1 つのバッジ) 用に **ブランド付きスナップショット カード** (フォーカス メトリクス + App Store QR コード) をレンダリングできます。 統計共有カードでは、**統計タブ ページのテーマ**の色を使用します。 [設定] → [アプリを共有] から **アプリ プロモーション カード**を共有することもできます。 

### 研究統計を iCloud と同期できますか?

 はい — **「統計」タブ→「ギア」→「iCloud と研究統計を同期」**。 これはタスク iCloud 同期とは**別のもの**です。 セッションは、CloudKit レコード タイプ `StudySession` を介して Apple ID デバイス全体で `cloudId` によってマージされます。 **毎日の目標設定** (`StatsGoals`) と **達成ロック解除/お祝い状態** (`StatsAchievements`) は、有効にすると同じトグルで同期します。

### 毎日の集中目標はどのように機能しますか?

 **Statistics → gear → Goals**: set daily pomodoro count, daily focus minutes, and weekly focus minutes. Progress appears on the Statistics dashboard and the **Today's Stats** widget when enabled.

 ### How do I link a countdown task to a focus session?

 On the Pomodoro or Study Timer screen, tap **Link task** and pick a task. Or from **Tasks**, long-press a task → **Focus with Pomodoro** or **Focus with Study Timer**. Completed sessions store the task title for **breakdown by task** in Statistics.

 ### タスクを固定したり並べ替えたりするにはどうすればよいですか?

 In the **Tasks** tab, swipe a row to **Pin** or use the sort menu in the navigation bar. Enter reorder mode to **drag** tasks — sorting switches to custom order automatically. Pinned tasks appear in their own section at the top.

 ### iCloud タスクの同期はどのように機能しますか?

 Tasks tab → gear → toggle **Sync tasks with iCloud**. Tasks merge by last-modified time across your Apple ID devices. ポモドーロ / 勉強タイマーはローカルに留まります。 **Study statistics** can optionally sync separately (Statistics → gear). iOS の設定で iCloud にサインインする必要があります。 アプリに戻ったときにも同期が実行されます。

### 統計ダッシュボードの共有画像には何が含まれていますか？

統計タブのツールバーで **共有** をタップします。ロングカードには、あなたの **現在の範囲と期間** フィルターに基づく情報が反映されます — 今日のヒーロー、目標進捗、ヒートマップ、曜日/時間別チャート、タスク内訳、トレンドバー、最近のセッション — さらにブランド表示とApp StoreのQRコードも含まれます。色はあなたの **統計タブページのテーマ** に合わせられます。

### 統計タブのテーマをカスタマイズできますか？

はい。**統計タブ → 設定（歯車） → テーマ** — Pomodoro、Study Timer、Tasks と同じタイトルバーと背景グラデーションのコントロールが利用できます。デフォルトはフォーカスレッド (`#E53935` / `#EF9A9A`) です。統計タブのティント、ナビゲーションバー、**統計共有カード** はすべてこのページテーマカラーに従います。

### 実績はどのように機能しますか？

最初のポモドーロ、連続記録、合計ポモドーロ、集中時間、毎日の目標達成など、マイルストーンに達すると、9 つのローカル バッジがロック解除されます。 新しいバッジのロックを解除すると、[統計] タブに **全画面のお祝い**が表示されます (閉じるには [**続行**] をタップします)。 **統計 → ギア → 実績** を開いてグリッドを参照します。 **バッジをタップ**すると詳細シートが表示されます。 実績ツールバーから **完全なリスト** を共有するか、詳細画面から **単一バッジ** を共有します。 バッジはデバイス上に保存されます。 iCloud 同期を有効にすると、サーバーにアップロードされず、CloudKit 経由でデバイス間でロック解除とお祝いの状態がマージされます。 

### フォーカス ヒートマップで過去数か月を参照するにはどうすればよいですか?

 統計ダッシュボードで、ヒートマップ カードの **前月/次月** の矢印を使用し、**月のタイトル**をタップして **年 + 月ピッカー** シートを開くか、**今月**をタップして現在の月に戻ります。 

### ヒートマップ上の将来の日付が異なって見えるのはなぜですか?

 当月の今日以降の日数は、塗りつぶしが薄い **破線のプレースホルダー** として表示されます。これらはフォーカス日としてカウントされません。 過去と今日では、通常の強度の色が使用されます。 

### 今日の統計ウィジェットを追加するにはどうすればよいですか?

ホーム画面を長押し → **+** → **iPomodoro** を検索 → **今日の統計** (小、**中、大**、またはロック画面の長方形/インライン) を追加します。 今日の集中力、ポモドーロ、**週**の目標の進捗状況、連続記録が表示されます。 

### タスク ウィジェットを追加するにはどうすればよいですか?

 ホーム画面を長押し → **+** → **iPomodoro** を検索 → **カウントダウン タスク** (小 / 中 / 大) を追加します。 今後の固定タスクと残り日数が表示されます。 タスクを編集した後にアプリを開くと、最速で更新されます。 

### モチベーション ウィジェットの引用を更新できますか?

 **iOS 17 以降** では、デイリー モチベーション ウィジェットの **更新** ボタンをタップすると、アプリを開かずにすぐに別の引用を選択できます。 

### 通知が機能しないのはなぜですか?

 現在の iOS 権限ステータスについては、**[設定] タブ → [通知]** を確認してください。 タイマーとタスクのリマインダーには通知へのアクセスが必要です。 許可が拒否された場合は、システム設定を開きます。 

### 作業時間と休憩時間をカスタマイズするにはどうすればよいですか?

 [ポモドーロ] タブで **歯車アイコン** をタップしてステッパーの行を調整するか、メイン画面で **タイマーの大きな数字をタップ**して期間ピッカーを開きます。 長い休憩間隔 (N ポモドーロごと) も設定可能です。 

### フェーズ完了の確認とは何ですか?

**ポモドーロタブ → 設定（歯車） → フェーズ完了を確認**。オンにすると、iPomodoroは各作業または休憩セグメントの後、次のフェーズを開始する前にダイアログを表示します。オフの場合（デフォルト）、完了アラーム後に次のフェーズが自動的に開始されます — 従来のハンズフリー・ポモドーロフローです。

### ライブアクティビティとダイナミックアイランドはどう動作するのですか？

ポモドーロとスタディタイマーの設定（歯車アイコン）でそれぞれ**ライブアクティビティ**を個別に有効にします。各モードは**独自**のロック画面とダイナミックアイランドのカウントダウンを持ち、互いに上書きすることはありません。セッション実行中はライブカウントダウンが表示され、完了すると10秒間の短いお祝い表示がされます。iOSがタイマーがロック画面に表示されたままの状態でアプリを終了した場合、iPomodoroを再度開くとセッションが**復元**され、アクティブタブにジャンプします — **ただし**、ホーム画面のクイックアクションから起動した場合はそちらが優先されます。

### ウィジェットはどうやって追加しますか？

ホーム画面を長押し → **+** → **iPomodoro**（または爱番茄 / 愛番茄）を検索。タイマーのカウントダウンには **iPomodoro · Pomodoro** または **iPomodoro · Study Timer**、日ごとの集中進捗には **Today’s Stats**、締め切りには **Countdown Tasks**、日替わりの名言には **Daily Motivational Quote** を選択してください。ステップごとのヘルプは **設定 → ウィジェット → 使い方** を開いて確認できます。

### タイマーウィジェットが更新されないのはなぜですか？

Pomodoro と Study Timer は **別々のウィジェット** です。セッションは **対応するタブ** で開始または一時停止し、正しいウィジェットを追加したことを確認してください。iOS はバッテリー節約のために更新を遅らせることがあります。より早く同期するには、アプリを一度開いてください。

### 以前のタイマーウィジェットはどこですか？

タイマーは現在 **iPomodoro · Pomodoro** と **iPomodoro · Study Timer** です。古いタイマーウィジェットは削除し、ウィジェットギャラリーから新しいものを追加してください。

### 日替わりの名言はどのように機能しますか？

`(year × 400 + dayOfYear) % total` を使用して、毎日 1 つの見積もりが決定的に選択されます。 **[設定] → [動機付けの引用設定] → [動機付けの引用言語]** で引用言語をフィルターします (すべて / 簡体字 / 繁体字 / 英語)。 同じ引用文がモチベーション ウィジェットとライブ アクティビティのヒントに深夜まで表示されます。 **[設定] → [モチベーションの引用設定] → [モチベーションの引用アンソロジー]** でランダムな引用を閲覧します (全画面、一度に 1 つずつ)。 

### ウィジェットの背景はテーマに従うことができますか?

 はい。 **[設定] → [ウィジェット] → [ウィジェットの背景はテーマに従います]** は、ホーム ウィジェットとロック画面ウィジェットのグローバル アクセント グラデーションを反映します。 タイトルのアクセントカラーを維持しながら、きれいな白 (明るい) またはシステムの暗い背景を使用するには、これをオフにします。 

### タスクの期限リマインダーはどのように機能しますか?

 タスクを作成または編集するときは、**期限リマインダー**を有効にして、将来の目標日時を設定します。 まさにその瞬間にローカル通知が発生します。 **[タスク] タブ → ギア → タスク期限リマインダー** で保留中のリマインダーを管理します。行をタップして編集するか、編集シートの下部からタスクを **削除**します。 タスクリストでのスワイプによる削除も引き続き機能します。 

### 編集中にタスクを削除するにはどうすればよいですか?

リストまたは**タスク期限リマインダー**からタスクを開き、編集シートの一番下までスクロールして**削除**をタップします。 アラートで確認してください。 新しいタスク (フローの作成) には削除ボタンが表示されません。 

### 過去の日付のリマインダーを有効にできないのはなぜですか?

 対象の日時がすでに過ぎている場合、リマインダーのトグルは非表示になり、既存のリマインダーは自動的に無効になります。スケジュールする意味のあるものは何も残されていません。 

### 自分のシステムとは異なる言語を使用できますか?

 はい。 **[設定] タブ → [言語]** に移動し、英語、簡体字中国語、または繁体字中国語を選択します。 ホーム画面上のアプリ名はシステム言語に従います。 アプリ内 UI はアプリ内での選択に従います。 

### アプリは私のデータを収集しますか?

 分析も追跡もありません。 タイマーと学習統計はデフォルトでデバイスに残ります。 タスクと勉強セッションは、個別の切り替えを有効にした場合にのみ **iCloud** に同期されます。 当社のサーバーではタスクやタイマーのデータを受信しません。 詳細については、[プライバシー ポリシー](../privacy) をご覧ください。 

### macOS はサポートされますか?

 macOSのサポートも予定されています。 Xcode プロジェクトには、macOS SDK 構成がすでに含まれています。 App Store の最新情報をお待ちください。 

### まだ助けが必要ですか?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) でお問い合わせください。通常、48時間以内に応答します。

&lt;/セクション&gt;

</section>
<section lang="ko" markdown="1">

### 왜 다른 뽀모도로 앱보다 iPomodoro를 선택해야 하나요?

iPomodoro는 웹 타이머를 감싼 것이 아닌, Apple 플랫폼을 위해 개발된 **네이티브 SwiftUI** 앱입니다. **5개의 통합 탭**(뽀모도로, 공부 타이머, 할 일, 통계, 설정), **이중 라이브 액티비티**, **5가지 위젯 패밀리**, **9개의 업적 배지**, **1000개 이상의 기기 내 명언**, **Siri & URL 바로가기**, **선택적 iCloud 동기화**를 제공하며, **분석 없음**과 **계정 필요 없음**을 모두 갖추고 있습니다. 집중, 마감, 진행 상황 추적을 한 번에 다루는 하나의 차분한 앱입니다.

### 타이머 및 작업 설정은 어디에 있나요?

타이머 시간, 소리, 라이브 액티비티, 페이지 테마 색상, 선택적 **집중 모드 알림**, 그리고 (포모도로 전용) 선택적 **단계 완료 확인**은 각 탭의 **톱니바퀴 아이콘**(포모도로, 스터디 타이머, 작업, 또는 **통계**) 아래에 있습니다. 글로벌 **설정** 탭에는 외관, 언어, **홈 화면 바로가기**, **앱 가이드**, 알림 권한, 동기 부여 문구(**일일 동기 부여 알림** 포함), 위젯 가이드, 피드백, 정보가 있으며, 모드별 시간 설정은 포함되지 않습니다. **통계** 설정(페이지 테마, 목표, 선택적 iCloud 동기화, 업적, 계산 규칙, CSV, 보존)은 **통계 탭 → 톱니바퀴** 아래에 있습니다.

### 홈 화면 바로가기와 Siri는 어떻게 작동하나요?

빠른 작업을 수행하려면 **앱 아이콘을 길게 누르세요**. Pomodoro, 학습 타이머, 작업, 통계, 동기 부여 인용문 또는 피드백을 엽니다. **설정 → 앱 설정 → 홈 화면 바로가기**에 표시되는 4가지 항목을 맞춤설정하세요(다시 정렬하려면 드래그하세요). **`iPomodoro://`** URL을 통해 동일한 대상을 열 수도 있습니다(`pomodoro`, `study`, `tasks`, `stats`, `motivation`, `feedback`; `iPomodoros://`도 작동함). 전체 [URL 체계 참조](../url-scheme)를 확인하세요. **Siri / 바로가기 앱**은 내장된 앱 바로가기를 통해 탭을 열거나 *"오늘 iPomodoro에서 얼마나 오랫동안 집중했나요?"*에 답할 수 있습니다. 

### 인앱 앱 가이드란 무엇인가요? 

**설정 → 앱 설정 → 앱 가이드** — 5개 탭, 위젯, 바로가기, iCloud 및 FAQ(위젯 가이드와 유사한 스타일)를 모두 다루는 축소 가능한 튜토리얼입니다. 

### iPomodoro가 나를 위해 집중 모드를 켤 수 있나요? 

아니요 — iOS에서는 타사 앱이 Focus를 직접 활성화하는 것을 허용하지 않습니다. 옵션 **집중 모드 알림**(Pomodoro 또는 학습 타이머 기어 설정)은 타이머를 시작할 때 초점이 꺼져 있는지 확인하고 경고를 표시합니다. 알림에서 **설정**을 열 수 있지만 집중을 직접 켜야 합니다. 

### 각 카운트다운 작업에 대한 색상을 선택할 수 있나요?

예. 작업을 추가하거나 편집할 때, **9가지 강조 색상** 중 하나를 선택하세요. 목록과 **카운트다운 작업** 위젯은 각 행에 해당 색상을 사용합니다. 작업 동기화가 활성화되면 색상은 iCloud를 통해 동기화됩니다.

### 맞춤 날짜 범위로 통계를 필터링할 수 있나요?

예. 통계 탭(또는 기간 보고서)에서, 기간 표시줄에서 **사용자 정의**를 선택한 후 시작 및 종료 날짜를 설정하세요. 통계 설정에서 **필터 기억**이 켜져 있으면 범위가 저장됩니다.

### 하루 동기 부여 알림을 받을 수 있나요?

예. **설정 → 동기 부여 인용문 설정**에는 선택 사항인 **하루 동기 부여 알림**이 포함되어 있습니다 — 시간을 선택하면 iPomodoro가 기기 내 알림 인용문 풀에서 무작위 문장을 사용하여 반복 **로컬 알림**을 예약합니다(네트워크 불필요). 타이머 완료 알림과는 별개입니다.

### 매일 인용문과 알림 인용문의 차이는 무엇인가요?

**대화/일일 명언** (**All 필터 사용 시 1000+개** — 간체 중국어 + 영어) 는 시작 팝업, 설정 탐색, 라이브 액티비티 힌트 및 동기부여 위젯을 지원합니다. **알림 명언**은 별도의 기기 내 풀(**언어별 일반 문구 365개**)로, 배경 타이머 완료 알림에만 사용됩니다. 두 경우 모두 설정에서 선택한 명언 언어 필터를 준수합니다.

### 포모도로 기법이란 무엇인가요?

포모도로 기법은 시간 관리 방법입니다: 집중된 시간 동안 작업을 하고(전통적으로 25분), 짧은 휴식을 취합니다. 여러 사이클 후에는 더 긴 휴식을 가집니다. iPomodoro는 이 리듬을 자동화하여 시계를 신경 쓰지 않고 작업에 집중할 수 있도록 합니다.

### iPomodoro가 이전 Flutter 버전과 다른 점은 무엇인가요?

이는 Apple 플랫폼을 위한 **완전한 SwiftUI 재작성**입니다. 핵심 아이디어는 동일합니다 — 포모도로, 학습 타이머, 카운트다운 작업 — 그러나 네이티브 성능, 라이브 액티비티, 최신 위젯, 더 긴밀한 iOS 통합을 제공합니다.

### 계정이나 인터넷 연결이 필요할까요?

iPomodoro 계정은 필요하지 않습니다. 타이머, 연구 통계, 테마 및 위젯은 기기에서 **완전히 오프라인**으로 실행됩니다. **선택 사항:** **iCloud와 작업 동기화**(작업 → 기어) 및/또는 **iCloud와 연구 통계 동기화**(통계 → 기어)를 활성화하여 동일한 Apple ID에 로그인된 기기 전체의 데이터를 병합합니다. 이는 당사 서버가 아닌 Apple CloudKit을 사용합니다. 인터넷은 App Store 업데이트나 피드백 이메일에도 사용됩니다. 

### 연구 통계는 어떻게 작동하나요? 

**통계** 탭을 엽니다. 전체 / Pomodoro / 학습 타이머 및 오늘 / 주 / 월 / 연도 / 전체 시간 / **사용자 정의 날짜 범위**로 필터링합니다. 대시보드에는 **오늘의 개요**, **목표 진행 상황**, 주별 비교, **월간 히트맵**, **성과**, 요일/시간대 차트, **연결된 작업별 분류**가 표시됩니다. 목표, 선택적 **iCloud 동기화**, 계산 규칙, **CSV 내보내기/가져오기** 및 데이터 보관을 보려면 **기어 아이콘**을 탭하세요. 통계는 **저희 서버에 절대 업로드되지 않습니다**(옵션인 iCloud는 Apple ID로 Apple CloudKit을 사용합니다). 

### 연구 통계를 내보내거나 가져올 수 있나요?

예. **통계 탭 → 기어 → 내보내기**는 시스템 공유 시트를 통해 CSV 파일을 공유합니다. **가져오기**는 동일한 형식(`kind,started_at,ended_at,duration_seconds,outcome` + `task_id,task_title,cloud_id` 옵션)을 허용합니다. **병합**(중복 건너뛰기) 또는 **모두 바꾸기**를 선택하세요. 백업 또는 수동 마이그레이션에 유용합니다. 자동 교차 기기 동기화를 위해서는 대신 **iCloud와 연구 통계 동기화**를 활성화하세요. 

### 내 통계를 이미지로 공유할 수 있나요? 

예. iPomodoro는 **통계 대시보드**(도구 모음 공유), **기간 보고서**, **연간 검토** 요약 및 **성과**(전체 목록 또는 단일 배지)에 대한 **브랜드 스냅샷 카드**(초점 지표 + App Store QR 코드)를 렌더링할 수 있습니다. 통계 공유 카드는 **통계 탭 페이지 테마** 색상을 사용합니다. 설정 → 앱 공유에서 **앱 프로모션 카드**를 공유할 수도 있습니다. 

### 연구 통계를 iCloud와 동기화할 수 있나요? 

예 — **통계 탭 → 기어 → iCloud와 학습 통계 동기화**. 이는 iCloud 동기화 작업과 **별도**입니다. 세션은 CloudKit 레코드 유형 `StudySession`을 통해 Apple ID 장치 전체에서 `cloudId`별로 병합됩니다. **일일 목표 설정**(`StatsGoals`) 및 **성취 잠금 해제/축하 상태**(`StatsAchievements`)는 활성화되면 동일한 토글에서 동기화됩니다.

### 일일 집중 목표는 어떻게 작동하나요? 

**통계 → 장비 → 목표**: 일일 포모도로 수, 일일 집중 시간(분), 주간 집중 시간(분)을 설정합니다. 활성화되면 통계 대시보드와 **오늘의 통계** 위젯에 진행 상황이 표시됩니다. 

### 카운트다운 작업을 포커스 세션에 어떻게 연결하나요? 

뽀모도로 또는 학습 타이머 화면에서 **작업 연결**을 누르고 작업을 선택하세요. 또는 **작업**에서 작업을 길게 누르세요 → **포모도로에 집중** 또는 **공부 타이머에 집중**. 완료된 세션은 통계에 **작업별 분류**에 대한 작업 제목을 저장합니다. 

### 작업을 고정하거나 재정렬하려면 어떻게 해야 하나요? 

**작업** 탭에서 행을 스와이프하여 **고정**하거나 탐색 메뉴의 정렬 메뉴를 사용하세요. 작업을 **드래그**하려면 재정렬 모드를 입력하세요. 자동으로 사용자 정의 순서로 스위치를 정렬합니다. 고정된 작업은 상단의 자체 섹션에 표시됩니다. 

### iCloud 작업 동기화는 어떻게 작동하나요? 

작업 탭 → 기어 → **iCloud와 작업 동기화** 토글. Apple ID 기기 전체에서 마지막 수정 시간을 기준으로 작업이 병합됩니다. 뽀모도로/학습 타이머는 현지에 유지됩니다. **연구 통계**는 선택적으로 별도로 동기화할 수 있습니다(통계 → 기어). iOS 설정에서 iCloud에 로그인되어 있어야 합니다. 앱으로 돌아올 때도 동기화가 실행됩니다.

### 통계 대시보드 공유 이미지에는 무엇이 포함되나요?

통계 탭 툴바에서 **공유**를 탭하세요. 긴 카드에는 현재의 **범위 및 기간** 필터가 반영됩니다 — 오늘의 히어로, 목표 진행, 히트맵, 요일/시간별 차트, 작업 분류, 추세 막대, 최근 세션 — 그리고 브랜딩과 App Store QR 코드가 포함됩니다. 색상은 **통계 탭 페이지 테마**와 일치합니다.

### 통계 탭 테마를 사용자 지정할 수 있나요?

예. **통계 탭 → 설정 → 테마** — 포모도로, 스터디 타이머, 작업과 동일한 제목 표시줄과 배경 그라데이션 컨트롤을 사용할 수 있습니다. 기본값은 집중 레드(`#E53935` / `#EF9A9A`)입니다. 통계 탭 색상, 탐색 바, 그리고 **통계 공유 카드**는 모두 이 페이지 테마 색상을 따릅니다.

### 업적은 어떻게 작동하나요?

첫 번째 포모도로, 연속 기록, 총 포모도로, 집중 시간, 일일 목표 달성 등 주요 목표를 달성하면 9개의 로컬 배지가 잠금 해제됩니다. 새 배지를 잠금 해제하면 통계 탭에 **전체 화면 축하**가 표시됩니다(닫으려면 **계속**을 탭하세요). **통계 → 장비 → 업적**을 열어 그리드를 탐색하세요. 세부정보 시트를 보려면 **배지를 탭하세요**. 성과 툴바에서 **전체 목록**을 공유하거나 세부정보 화면에서 **단일 배지**를 공유하세요. 배지는 기기에 저장됩니다. iCloud 동기화가 활성화되면 잠금 해제 및 축하 상태가 CloudKit을 통해 장치 전체에 병합됩니다. 당사 서버에 업로드되지 않습니다. 

### 포커스 히트맵에서 지난 달을 어떻게 찾아보나요? 

통계 대시보드에서 히트맵 카드의 **이전/다음 달** 화살표를 사용하고 **월 제목**을 탭하여 **연도 + 월 선택기** 시트를 열거나 **이번 달**을 탭하여 이번 달로 돌아갑니다. 

### 히트맵의 미래 날짜가 다르게 보이는 이유는 무엇인가요? 

당월의 오늘 이후의 날은 더 밝은 색상의 **점선 윤곽선 자리 표시자**로 표시되며 집중일로 계산되지 않습니다. 지난 날과 오늘은 일반 강도 색상을 사용합니다. 

### 오늘의 통계 위젯은 어떻게 추가하나요?

홈 화면 길게 누르기 → **+** → **iPomodoro** 검색 → **오늘의 통계** 추가(소형, **중형, 대형** 또는 잠금 화면 직사각형/인라인). 오늘의 집중도, 뽀모도로 및 **주간** 목표 진행 상황, 연속 기록을 보여줍니다. 

### 할 일 위젯은 어떻게 추가하나요? 

홈 화면 길게 누르기 → **+** → **iPomodoro** 검색 → **카운트다운 작업** 추가(소형/중형/대형). 향후 고정된 작업과 남은 일수가 표시됩니다. 가장 빠른 새로 고침을 위해 작업을 편집한 후 앱을 엽니다. 

### 동기 부여 위젯 인용문을 새로 고칠 수 있나요? 

**iOS 17+**에서는 Daily Motivation 위젯의 **새로고침** 버튼을 탭하여 앱을 열지 않고도 즉시 다른 인용문을 선택할 수 있습니다. 

### 알림이 작동하지 않는 이유는 무엇인가요? 

현재 iOS 권한 상태를 보려면 **설정 탭 → 알림**을 확인하세요. 타이머 및 작업 미리 알림에는 알림 액세스가 필요합니다. 권한이 거부된 경우 시스템 설정을 엽니다. 

### 업무 시간과 휴식 시간을 어떻게 맞춤설정하나요? 

Pomodoro 탭에서 **기어 아이콘**을 탭하고 → 스테퍼 행을 조정하거나 메인 화면에서 **큰 타이머 숫자를 탭하여** 기간 선택기를 엽니다. 긴 휴식 간격(N 포모도로마다)도 구성 가능합니다. 

### 단계 완료 확인이란 무엇인가요?

**Pomodoro 탭 → 톱니바퀴 → 단계 완료 확인**. **켬**으로 설정하면 iPomodoro가 각 작업 또는 휴식 구간이 끝난 후 다음 단계로 넘어가기 전에 대화 상자를 표시합니다. **끔**(기본값)일 경우, 완료 알람 후 다음 단계가 자동으로 시작됩니다 — 전형적인 핸즈프리 포모도로 흐름입니다.

### 라이브 액티비티와 다이내믹 아일랜드는 어떻게 작동하나요?

Pomodoro와 공부 타이머 설정(톱니바퀴 아이콘)에서 **별도로** 라이브 액티비티를 활성화하세요. 각 모드는 **자체적인** 잠금 화면 및 다이내믹 아일랜드 카운트다운을 가지며 서로 덮어쓰지 않습니다. 세션이 진행되는 동안 라이브 카운트다운을 볼 수 있으며, 세션이 완료되면 10초 동안 짧은 축하 화면이 표시됩니다. 타이머가 잠금 화면에 여전히 표시되는 동안 iOS가 앱을 종료하면, iPomodoro를 다시 열 때 세션이 **복원**되고 활성 탭으로 이동합니다 — **홈 화면 퀵 액션**을 통해 실행한 경우에는 우선권이 적용됩니다.

### 위젯은 어떻게 추가하나요?

홈 화면을 길게 누른 후 → **+** → **iPomodoro** (또는 爱番茄 / 愛番茄)를 검색하세요. 타이머 카운트다운을 위해서는 **iPomodoro · Pomodoro** 또는 **iPomodoro · Study Timer**를 선택하세요(별도의 위젯입니다), 일일 집중 진행 상황을 보기 위해서는 **오늘의 통계**, 마감일 확인을 위해서는 **카운트다운 작업**, 일일 명언을 위해서는 **오늘의 명언**을 선택하세요. 단계별 도움말을 보려면 **설정 → 위젯 → 사용 방법**을 열십시오.

### 타이머 위젯이 업데이트되지 않는 이유는 무엇인가요?

Pomodoro와 Study Timer는 **별도의 위젯**입니다. 각 세션을 **해당 탭에서** 시작하거나 일시 중지하고 올바른 위젯을 추가했는지 확인하세요. iOS는 배터리를 절약하기 위해 새로고침을 지연할 수 있으므로, 앱을 한 번 열어 동기화를 빠르게 하세요.

### 이전 타이머 위젯은 어디에 있나요?

타이머는 이제 **iPomodoro · Pomodoro**와 **iPomodoro · Study Timer**입니다. 이전 타이머 위젯을 제거하고 위젯 갤러리에서 새 위젯을 추가하세요.

### 일일 명언은 어떻게 작동하나요?

`(year × 400 + dayOfYear) % total`을 사용하여 매일 하나의 견적이 결정론적으로 선택됩니다. **설정 → 동기 부여 인용 설정 → 동기 부여 인용 언어**(전체 / 간체 / 번체 / 영어)에서 인용 언어를 필터링하세요. 동기 부여 위젯과 실시간 활동 힌트에는 자정까지 동일한 인용문이 나타납니다. **설정 → 동기 부여 인용문 설정 → 동기 부여 인용문 모음**(전체 화면, 한 번에 하나씩)에서 임의의 인용문을 찾아보세요. 

### 위젯 배경이 내 테마를 따를 수 있나요? 

예. **설정 → 위젯 → 테마를 따르는 위젯 배경**은 홈 및 잠금 화면 위젯의 전체 악센트 그라데이션을 반영합니다. 제목에 강조 색상을 유지하면서 깔끔한 흰색(밝은) 또는 시스템 어두운 배경을 위해 이 기능을 끄세요. 

### 작업 기한 알림은 어떻게 작동하나요? 

작업을 생성하거나 편집할 때 **마감일 알림**을 활성화하고 향후 목표 날짜/시간을 설정하세요. 정확한 순간에 로컬 알림이 실행됩니다. **작업 탭 → 톱니바퀴 → 작업 기한 알림**에서 대기 중인 알림을 관리하세요. 편집 시트 하단에서 작업을 편집하거나 **삭제**하려면 행을 탭하세요. 작업 목록에서 스와이프하여 삭제하는 기능도 여전히 작동합니다. 

### 작업을 편집하는 동안 어떻게 삭제하나요?

목록이나 **작업 기한 알림**에서 작업을 연 다음 편집 시트 하단으로 스크롤하고 **삭제**를 탭하세요. 알림에서 확인하세요. 새 작업(흐름 만들기)에는 삭제 버튼이 표시되지 않습니다. 

### 지난 날짜에 ​​대한 알림을 활성화할 수 없는 이유는 무엇인가요? 

목표 날짜/시간이 이미 지난 경우 알림 토글이 숨겨지고 기존 알림이 자동으로 비활성화됩니다. 즉, 예약할 의미 있는 내용이 더 이상 남지 않습니다. 

### 내 시스템과 다른 언어를 사용할 수 있나요? 

예. **설정 탭 → 언어**로 이동하여 영어, 중국어 간체, 중국어 번체를 선택하세요. 홈 화면의 앱 이름은 시스템 언어를 따릅니다. 인앱 UI는 인앱 선택을 따릅니다. 

### 앱이 내 데이터를 수집하나요? 

분석도 없고 추적도 없습니다. 타이머와 연구 통계는 기본적으로 장치에 유지됩니다. 작업 및 학습 세션은 별도의 토글을 활성화한 경우에만 **iCloud**에 동기화됩니다. 당사 서버에서는 귀하의 작업이나 타이머 데이터를 수신하지 않습니다. 자세한 내용은 [개인정보 보호정책](../privacy)을 참조하세요. 

### macOS가 지원되나요? 

macOS 지원이 계획되어 있습니다. Xcode 프로젝트에는 이미 macOS SDK 구성이 포함되어 있습니다. App Store의 업데이트를 계속 지켜봐 주시기 바랍니다. 

### 아직도 도움이 필요하신가요?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) 로 문의하십시오. 우리는 일반적으로 48 시간 이내에 응답합니다.

&lt;/섹션&gt;

</section>
<section lang="ru" markdown="1">

### Почему стоит выбрать iPomodoro вместо других приложений Pomodoro?

iPomodoro — это **нативное приложение на SwiftUI**, созданное для платформ Apple, а не обёрнутый веб-таймер. Вы получаете **пять интегрированных вкладок** (Pomodoro, Таймер учебы, Задачи, Статистика, Настройки), **дважды Live Activities**, **пять видов виджетов**, **9 значков достижений**, **более 1000 цитат на устройстве**, **Siri и URL шорткаты**, а также **опциональную синхронизацию с iCloud** — всё это **без аналитики** и **без необходимости создания аккаунта**. Одно спокойное приложение, которое полностью охватывает фокус, дедлайны и отслеживание прогресса.

### Где находятся настройки таймера и задач?

Продолжительности таймеров, звуки, Live Activity, цвета темы страницы, необязательное **напоминание режима фокусировки** и (только для Помодоро) необязательное **подтверждение завершения фазы** находятся под **значком шестеренки** каждой вкладки (Помодоро, Таймер для учебы, Задачи или **Статистика**). Глобальная вкладка **Настройки** содержит параметры внешнего вида, язык, **ярлыки на главном экране**, **Руководство по приложению**, разрешения на уведомления, мотивационные цитаты (включая **ежедневное уведомление с мотивацией**), руководство по виджетам, обратную связь и информацию о приложении — а не продолжительности для каждого режима. Настройки **Статистики** (тема страницы, цели, необязательная синхронизация с iCloud, достижения, правила подсчета, CSV, хранение данных) находятся в **вкладке Статистика → шестеренка**.

### Как работают ярлыки на главном экране и Siri?

**Длительное нажатие на значок приложения** для быстрого действия — откройте «Помидор», «Таймер обучения», «Задачи», «Статистика», мотивационную цитату или отзыв. Настройте, какие четыре из них будут отображаться в разделе **Настройки → Настройки приложения → Ярлыки главного экрана** (перетащите, чтобы изменить порядок). Вы также можете открыть те же места назначения через URL-адреса **`iPomodoro://`** (`pomodoro`, `study`, `tasks`, `stats`, `motivation`, `feedback`; `iPomodoros://` также работает). См. полную версию [Справочник по схеме URL](../url-scheme). **Приложение Siri / Shortcuts** может открывать вкладки или отвечать * «Как долго я сегодня концентрировался на iPomodoro?»* с помощью встроенных ярлыков приложений. 

### Что такое руководство по приложению в приложении? 

**Настройки → Настройки приложения → Руководство по приложению** — складное руководство, охватывающее все пять вкладок, виджеты, ярлыки, iCloud и часто задаваемые вопросы (аналогично руководству по виджетам). 

### Может ли iPomodoro включить для меня режим фокусировки? 

Нет — iOS не позволяет сторонним приложениям напрямую включать Focus. Дополнительное **напоминание о режиме фокусировки** (настройки механизма «Помодоро» или «Таймер исследования») проверяет, выключен ли фокус при запуске таймера, и отображает предупреждение; вы можете открыть **Настройки** из оповещения, но вам придется включить Фокус самостоятельно. 

### Могу ли я выбрать цвет для каждой задачи обратного отсчета?

Да. При добавлении или редактировании задачи выберите один из **9 акцентных цветов**. Список и виджет **Countdown Tasks** используют этот цвет для каждой строки. Цвета синхронизируются через iCloud, если включена синхронизация задач.

### Могу ли я фильтровать статистику по собственному диапазону дат?

Да. На вкладке Статистика (или в отчете за период) выберите **Пользовательский** в панели периодов, затем установите даты начала и окончания. Диапазон сохраняется, если в настройках Статистики включена опция **Запомнить фильтр**.

### Могу ли я получать уведомление с ежедневной мотивацией?

Да. **Настройки → Настройки мотивационных цитат** включают опциональное **ежедневное уведомление о мотивации** — выберите время, и iPomodoro запланирует повторяющееся **локальное уведомление** с случайной строкой из пула цитат, хранящихся на устройстве (без сети). Это уведомление отдельно от сигналов о завершении таймера.

### В чем разница между ежедневными цитатами и цитатами для уведомлений?

**Диалоги/ежедневные цитаты** (**более 1000**, если фильтр установлен на «Все» — упрощённый китайский + английский) используются для всплывающего окна при запуске, просмотра настроек, подсказки Live Activity и виджета Мотивации. **Цитаты для уведомлений** — это отдельный локальный пул (**365 общих строк на каждый язык**), который используется только для уведомлений о завершении фонового таймера. Оба типа цитат учитывают выбранный язык цитат в настройках.

### Что такое техника Помодоро?

Техника Помодоро — это метод управления временем: работать в сосредоточенных интервалах (классически 25 минут), затем делать короткий перерыв. После нескольких циклов делается более длинный перерыв. iPomodoro автоматизирует этот ритм, чтобы вы могли сосредоточиться на работе, а не на часах.

### Чем iPomodoro отличается от старой версии на Flutter?

Это **полностью переписанная версия на SwiftUI** для платформ Apple. Те же основные идеи — Помодоро, таймер для учёбы, обратный отсчёт задач — но с нативной производительностью, Live Activity, современными виджетами и более тесной интеграцией с iOS.

### Нужен ли аккаунт или подключение к интернету?

Никакая учетная запись iPomodoro не требуется. Таймеры, статистика исследования, темы и виджеты работают на вашем устройстве **полностью автономно**. **Необязательно:** включите **Синхронизировать задачи с iCloud** (Задачи → шестерня) и/или **Синхронизировать статистику исследования с iCloud** (Статистика → шестерня), чтобы объединить данные на устройствах, на которых подписан один и тот же Apple ID — при этом используется Apple CloudKit, а не наши серверы. Интернет также используется для получения обновлений в App Store или отправки отзывов по электронной почте. 

### Как работает статистика исследования? 

Откройте вкладку **Статистика**. Фильтруйте по параметрам «Все», «Помидор», «Таймер исследования» и «Сегодня», «Неделя», «Месяц», «Год», «Все время» и «**Настраиваемый диапазон дат**». На информационной панели отображаются **сегодняшний обзор**, **прогресс в достижении цели**, сравнение по неделям, **месячная тепловая карта**, **достижения**, графики дней недели и времени суток и **разбивка по связанным задачам**. Коснитесь **значка шестеренки**, чтобы просмотреть цели, дополнительную **синхронизацию с iCloud**, правила подсчета, **экспорт/импорт CSV** и сохранение данных. Статистика **никогда не загружается на наши серверы** (дополнительно iCloud использует Apple CloudKit под вашим Apple ID). 

### Могу ли я экспортировать или импортировать статистику исследования?

Да. **Вкладка «Статистика» → «Шестерня» → «Экспорт»** предоставляет доступ к CSV-файлу через общий доступ к системе. **Импорт** принимает тот же формат (`kind,started_at,ended_at,duration_seconds,outcome` плюс необязательный `task_id,task_title,cloud_id`) — выберите **объединить** (пропустить дубликаты) или **заменить все**. Полезно для резервного копирования или миграции вручную. Для автоматической синхронизации между устройствами вместо этого включите **Синхронизировать статистику исследования с iCloud**. 

### Могу ли я поделиться своей статистикой в ​​виде изображения? 

Да. iPomodoro может отображать **фирменные карточки со снимками** (показатели фокуса + QR-код App Store) для **Статистической панели** (общий доступ к панели инструментов), **отчетов за периоды**, **сводок за год** и **достижений** (полный список или отдельный значок). В карточках общего доступа к статистике используются цвета **темы вкладки «Статистика»**. Вы также можете поделиться **рекламной картой приложения** в меню «Настройки» → «Поделиться приложением». 

### Могу ли я синхронизировать статистику исследования с iCloud? 

Да — **Вкладка «Статистика» → «Шестерня» → Синхронизировать статистику исследования с iCloud**. Это **отдельно** от синхронизации задач с iCloud. Сеансы объединяются `cloudId` на ваших устройствах Apple ID с помощью типа записи CloudKit `StudySession`. **Настройки ежедневных целей** (`StatsGoals`) и **состояние разблокировки/празднования достижения** (`StatsAchievements`) синхронизируются под одним и тем же переключателем, если они включены.

### Как работают ежедневные цели концентрации? 

**Статистика → Снаряжение → Цели**: установите ежедневное количество помидоров, ежедневные минуты концентрации и еженедельные минуты концентрации. Прогресс отображается на панели статистики и в виджете **Сегодняшняя статистика**, если он включен. 

### Как связать задачу обратного отсчета с сеансом фокусировки? 

На экране «Помидор» или «Таймер обучения» нажмите **Связать задачу** и выберите задачу. Или в разделе **Задачи** нажмите и удерживайте задачу → **Фокус с помощью Помидора** или **Фокус с помощью таймера обучения**. Завершенные сеансы сохраняют название задачи для **разбивки по задачам** в статистике. 

### Как закрепить задачи или изменить их порядок? 

На вкладке **Задачи** проведите по строке до пункта **Закрепить** или воспользуйтесь меню сортировки на панели навигации. Войдите в режим изменения порядка, чтобы **перетаскивать** задачи — сортировка автоматически переключается на индивидуальный порядок. Закрепленные задачи отображаются в отдельном разделе вверху. 

### Как работает синхронизация задач iCloud? 

Вкладка «Задачи» → шестеренка → включите **Синхронизировать задачи с iCloud**. Задачи объединяются по времени последнего изменения на всех ваших устройствах с Apple ID. Таймеры Pomodoro/обучения остаются локальными. **Статистика исследования** при желании может синхронизироваться отдельно (Статистика → снаряжение). Вы должны войти в iCloud в настройках iOS. Синхронизация также запускается, когда вы возвращаетесь в приложение.

### Что включает изображение общего доступа панели Статистики?

Нажмите **Поделиться** на панели инструментов вкладки Статистика. Длинная карточка отражает ваши фильтры **текущего диапазона и периода** — герой дня, прогресс по целям, тепловая карта, диаграммы по дням недели/часам, разбивка задач, гистограммы тенденций и недавние сессии — плюс брендирование и QR-код App Store. Цвета соответствуют **теме страницы вкладки Статистика**.

### Могу ли я настроить тему вкладки Статистика?

Да. **Вкладка Статистика → шестеренка → Тема** — те же элементы управления заголовком и градиентом фона, что и в Pomodoro, Study Timer и Tasks. По умолчанию — красный фокус (`#E53935` / `#EF9A9A`). Оттенок вкладки Статистика, панель навигации и **карточки статистики для общего доступа** следуют цветам темы страницы.

### Как работают достижения?

Девять локальных значков открываются по мере достижения этапов — первый помидор, полоса, общее количество удач, часы концентрации, выполнение ежедневных целей и многое другое. Когда вы разблокируете новый значок, на вкладке «Статистика» появится **полноэкранное празднование** (нажмите **Продолжить**, чтобы закрыть его). Откройте **Статистика → Снаряжение → Достижения**, чтобы просмотреть сетку. **Нажмите значок**, чтобы открыть подробную информацию; поделитесь **полным списком** на панели инструментов достижений или **отдельным значком** на экране подробных сведений. Значки хранятся на устройстве; при включенной синхронизации iCloud состояния разблокировки и празднования объединяются на всех ваших устройствах через CloudKit, а не загружаются на наши серверы. 

### Как просмотреть прошлые месяцы на тепловой карте фокуса? 

На панели статистики используйте стрелки **Предыдущий/Следующий месяц** на карточке тепловой карты, коснитесь **названия месяца**, чтобы открыть лист **год + месяц**, или коснитесь **Этот месяц**, чтобы вернуться к текущему месяцу. 

### Почему будущие даты на тепловой карте выглядят иначе? 

Дни после сегодняшнего дня в текущем месяце отображаются как **заполнители с пунктирным контуром** и более светлой заливкой — они не считаются днями фокуса. В прошлые дни и сегодня используйте цвета нормальной интенсивности. 

### Как добавить виджет сегодняшней статистики?

Нажмите и удерживайте главный экран → **+** → выполните поиск **iPomodoro** → добавьте **Сегодняшнюю статистику** (Маленький, **Средний, Большой** или прямоугольный/встроенный экран блокировки). Он показывает сегодняшнюю концентрацию, «помидор» и **еженедельный** прогресс в достижении цели, а также полосу успехов. 

### Как добавить виджет задач? 

Длительно нажмите главный экран → **+** → выполните поиск **iPomodoro** → добавьте **Задачи обратного отсчета** (Маленький/Средний/Большой). Он показывает предстоящие закрепленные задачи и оставшиеся дни. Откройте приложение после редактирования задач для быстрого обновления. 

### Могу ли я обновить цитату в виджете мотивации? 

На **iOS 17+** нажмите кнопку **обновить** в виджете «Ежедневная мотивация», чтобы мгновенно выбрать другую цитату, не открывая приложение. 

### Почему не работают уведомления? 

Проверьте **вкладку «Настройки» → «Уведомления»**, чтобы узнать текущий статус разрешений iOS. Напоминания о таймере и задачах требуют доступа к уведомлениям. Откройте настройки системы, если в разрешении было отказано. 

### Как настроить продолжительность работы и перерывов? 

Коснитесь **значка шестеренки** на вкладке «Помидор» → отрегулируйте ряды шаговых регуляторов или **коснитесь больших цифр таймера** на главном экране, чтобы открыть окно выбора продолжительности. Длинный интервал перерыва (каждые N помидоров) также настраивается. 

### Что такое подтверждение завершения фазы?

**Вкладка Pomodoro → значок шестерёнки → Подтвердить завершение фазы**. Когда **включено**, iPomodoro показывает диалог после каждого рабочего или перерывного сегмента перед началом следующей фазы. Когда **выключено** (по умолчанию), следующая фаза начинается автоматически после сигнала о завершении — классический бесконтактный Pomodoro.

### Как работают Live Activity и Dynamic Island?

Включите **Live Activity** отдельно в настройках Pomodoro и Study Timer (значок шестерёнки). Каждый режим получает **отдельный** отсчёт на заблокированном экране и в Dynamic Island — они никогда не перезаписывают друг друга. Пока идёт сессия, вы видите живой отсчёт; когда она завершается, краткое празднование показывается в течение 10 секунд. Если iOS закрывает приложение, пока таймер всё ещё отображается на заблокированном экране, повторное открытие iPomodoro **восстанавливает** сессию и автоматически переходит на активную вкладку — **если только** вы не запустили его через **Быстрое действие на главном экране**, которое имеет приоритет.

### Как добавить виджеты?

Долгое нажатие на главный экран → **+** → найдите **iPomodoro** (или 爱番茄 / 愛番茄). Выберите **iPomodoro · Pomodoro** или **iPomodoro · Study Timer** для отсчета времени (это отдельные виджеты), **Today's Stats** для ежедневного прогресса концентрации, **Countdown Tasks** для сроков или **Daily Motivational Quote** для ежедневной цитаты. Для пошаговой помощи откройте **Настройки → Виджеты → Как использовать**.

### Почему мой виджет таймера не обновляется?

Pomodoro и Study Timer — это **отдельные виджеты**. Запускайте или ставьте на паузу сессию во **вкладке соответствующего виджета** и убедитесь, что вы добавили правильный виджет. iOS может задерживать обновления, чтобы экономить заряд батареи — откройте приложение один раз для более быстрой синхронизации.

### Где старый виджет таймера?

Таймеры теперь называются **iPomodoro · Pomodoro** и **iPomodoro · Study Timer**. Удалите любой старый виджет таймера и добавьте новые через галерею виджетов.

### Как работает ежедневная мотивационная цитата?

Одна котировка выбирается детерминированно каждый день с помощью `(year × 400 + dayOfYear) % total`. Отфильтруйте язык цитаты в разделе **Настройки → Настройки мотивационных цитат → Языки мотивационных цитат** (Все / Упрощенный / Традиционный / Английский). Та же цитата отображается в виджете «Мотивация» и в подсказке «Живая активность» до полуночи. Просматривайте случайные цитаты в **Настройки → Настройки мотивационных цитат → Антология мотивационных цитат** (в полноэкранном режиме, по одной). 

### Могут ли фоны виджетов соответствовать моей теме? 

Да. **Настройки → Виджеты → Фон виджета соответствует теме** отражает глобальный градиент акцента на виджетах «Домой» и «Экран блокировки». Отключите его, чтобы получить чистый белый (светлый) или системный темный фон, сохраняя при этом акцентные цвета в заголовках. 

### Как работают напоминания о сроках выполнения задач? 

При создании или редактировании задачи включите **Напоминание о сроке выполнения** и установите будущую целевую дату/время. В этот момент срабатывает локальное уведомление. Управляйте ожидающими напоминаниями в разделе **Вкладка «Задачи» → «Шестеренка» → «Напоминания о сроке выполнения задач»** — коснитесь строки, чтобы отредактировать или **удалить** задачу в нижней части листа редактирования. Удаление свайпом в списке задач по-прежнему работает. 

### Как удалить задачу во время редактирования?

Откройте задачу из списка или из **Напоминаний о сроке выполнения задачи**, затем прокрутите страницу редактирования вниз и нажмите **Удалить**. Подтвердите в оповещении. В новых задачах (создание потока) кнопка удаления не отображается. 

### Почему я не могу включить напоминание о прошлой дате? 

Если целевая дата и время уже прошли, переключатель напоминаний скрыт, а все существующие напоминания отключаются автоматически — в планировании не остается ничего значимого. 

### Могу ли я использовать язык, отличный от языка моей системы? 

Да. Перейдите на вкладку **Настройки → Язык** и выберите английский, упрощенный китайский или традиционный китайский. Название приложения на главном экране соответствует языку системы; Пользовательский интерфейс в приложении соответствует вашему выбору в приложении. 

### Собирает ли приложение мои данные? 

Никакой аналитики, никакого отслеживания. Таймеры и статистика исследований по умолчанию остаются на вашем устройстве. Задачи и учебные занятия синхронизируются с **вашим iCloud**, только если вы включили отдельные переключатели. Мы не получаем данные о ваших задачах или таймерах на наши серверы. Подробную информацию см. в нашей [Политике конфиденциальности](../privacy). 

### Будет ли поддерживаться macOS? 

Планируется поддержка macOS. Проект Xcode уже включает конфигурацию macOS SDK; следите за обновлениями в App Store. 

### Все еще нужна помощь?

Свяжитесь с нами по адресу [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com). Обычно мы отвечаем в течение 48 часов.

&lt;/section&gt;

</section>
<section lang="th" markdown="1">

### ทำไมฉันควรเลือกใช้ iPomodoro แทนแอป Pomodoro อื่นๆ?

iPomodoro เป็นแอป **SwiftUI แบบเนทีฟ** ที่สร้างขึ้นสำหรับแพลตฟอร์มของ Apple — ไม่ใช่ตัวจับเวลาเว็บที่ห่อเข้ามา คุณจะได้รับ **ห้าหมวดแท็บรวมกัน** (Pomodoro, ตัวจับเวลาเรียน, งาน, สถิติ, การตั้งค่า), **กิจกรรมสดสองแบบ**, **วิดเจ็ตห้าครอบครัว**, **9 เหรียญรางวัลความสำเร็จ**, **คำคมมากกว่า 1000 รายการบนอุปกรณ์**, **ทางลัด Siri & URL**, และ **สามารถซิงค์ iCloud ได้ถ้าต้องการ** — ทั้งหมดนี้ **ไม่มีการเก็บข้อมูลวิเคราะห์** และ **ไม่ต้องมีบัญชีผู้ใช้** แอปเดียวที่สงบ ครอบคลุมทั้งความตั้งใจโฟกัส เวลาส่งงาน และติดตามความก้าวหน้าอย่างครบถ้วน

### การตั้งค่าตัวจับเวลาและงานอยู่ที่ไหน?

ระยะเวลาไทม์เมอร์, เสียง, กิจกรรมสด, สีธีมของหน้า, การแจ้งเตือน **โหมดโฟกัส** ที่เลือกได้ และ (เฉพาะโหมด Pomodoro) **ยืนยันการทำเฟสให้เสร็จ** ที่เลือกได้ อยู่ภายใต้ **ไอคอนฟันเฟือง** ของแต่ละแท็บ (Pomodoro, Study Timer, Tasks, หรือ **Statistics**) แท็บ **การตั้งค่า** ทั่วไป จะเก็บการตั้งค่าเรื่องรูปลักษณ์, ภาษา, **ทางลัดหน้าหลัก**, **คู่มือแอป**, การอนุญาตการแจ้งเตือน, คำคมสร้างแรงบันดาลใจ (รวมถึง **การแจ้งเตือนแรงบันดาลใจประจำวัน**), คู่มือวิดเจ็ต, ข้อเสนอแนะ และเกี่ยวกับแอป ไม่ใช่การตั้งค่าเวลาเฉพาะโหมด การตั้งค่า **สถิติ** (ธีมหน้า, เป้าหมาย, การซิงค์ iCloud เลือกได้, ความสำเร็จ, กฎการนับ, CSV, การเก็บข้อมูล) อยู่ที่ **แท็บ Statistics → ฟันเฟือง**  

### ทางลัดหน้าหลักและ Siri ทำงานอย่างไร?

**กดไอคอนแอปค้างไว้** เพื่อดำเนินการด่วน — เปิด Pomodoro, ตัวจับเวลาการเรียน, งาน, สถิติ, คำพูดสร้างแรงบันดาลใจ หรือคำติชม ปรับแต่งสี่รายการที่ปรากฏภายใต้ **การตั้งค่า → การตั้งค่าแอพ → ทางลัดหน้าจอหลัก** (ลากเพื่อเรียงลำดับใหม่) คุณยังสามารถเปิดปลายทางเดียวกันผ่าน URL **`iPomodoro://`_** (`pomodoro`, `study`, `tasks`, `stats`, `motivation`, `feedback`; `iPomodoros://` ก็ใช้งานได้เช่นกัน) ดู [การอ้างอิงโครงร่าง URL](../url-scheme) ฉบับเต็ม **แอป Siri / ทางลัด** สามารถเปิดแท็บหรือตอบได้ว่า *"วันนี้ฉันโฟกัสไปที่ iPomodoro นานแค่ไหน"* ผ่านทางลัดแอปที่มาพร้อมเครื่อง 

### คู่มือแอปในแอปคืออะไร 

**การตั้งค่า → การตั้งค่าแอพ → คู่มือแอพ** — บทช่วยสอนแบบยุบได้ครอบคลุมทั้งห้าแท็บ วิดเจ็ต ทางลัด iCloud และคำถามที่พบบ่อย (รูปแบบคล้ายกับคำแนะนำวิดเจ็ต) 

### iPomodoro สามารถเปิดโหมดโฟกัสให้ฉันได้หรือไม่ 

ไม่ — iOS ไม่อนุญาตให้แอปของบริษัทอื่นเปิดใช้งานโฟกัสโดยตรง **ตัวเลือกเตือนโหมดโฟกัส** (การตั้งค่าเกียร์ Pomodoro หรือ Study Timer) จะตรวจสอบว่าโฟกัสปิดอยู่หรือไม่เมื่อคุณเริ่มจับเวลาและแสดงการแจ้งเตือน คุณสามารถเปิด **การตั้งค่า** ได้จากการแจ้งเตือน แต่คุณต้องเปิดโฟกัสด้วยตัวเอง 

### ฉันสามารถเลือกสีสำหรับงานนับถอยหลังแต่ละงานได้หรือไม่?

ใช่ เมื่อเพิ่มหรือแก้ไขงาน ให้เลือกสีเน้น **9 สี** หนึ่งสี รายการและวิดเจ็ต **Countdown Tasks** จะใช้สีนี้ต่อแต่ละแถว สีจะซิงค์ผ่าน iCloud เมื่อเปิดใช้งานการซิงค์งาน

### ฉันสามารถกรองสถิติตามช่วงวันที่กำหนดเองได้ไหม?

ได้ ในแท็บสถิติ (หรืองบประมาณช่วงเวลา) ให้เลือก **กำหนดเอง** ในแถบช่วงเวลา แล้วตั้งวันเริ่มต้นและวันสิ้นสุด ช่วงเวลาจะถูกบันทึกเมื่อเปิด **จำตัวกรอง** ในการตั้งค่าสถิติ

### ฉันสามารถรับการแจ้งเตือนแรงบันดาลใจประจำวันได้ไหม?

ได้ **การตั้งค่า → การตั้งค่าแรงบันดาลใจ** มีตัวเลือก **การแจ้งเตือนแรงบันดาลใจประจำวัน** — เลือกเวลาแล้ว iPomodoro จะตั้งค่า **การแจ้งเตือนท้องถิ่น** ซ้ำโดยสุ่มประโยคจากกลุ่มคำคมในอุปกรณ์ (ไม่ต้องใช้เครือข่าย) แยกต่างหากจากการแจ้งเตือนเมื่อสิ้นสุดตัวจับเวลา

### ความแตกต่างระหว่างคำคมประจำวันกับคำคมแจ้งเตือนคืออะไร?

**บทสนทนา/คำคมรายวัน** (**รวมกว่า 1000+** เมื่อกรองเป็นทั้งหมด — ภาษาจีนตัวย่อ + ภาษาอังกฤษ) ใช้งานสำหรับป๊อปอัปเริ่มต้น, การเรียกดูการตั้งค่า, การแจ้งเตือนกิจกรรมสด, และวิดเจ็ตแรงบันดาลใจ **คำคมการแจ้งเตือน** เป็นชุดคำคมแยกบนอุปกรณ์ (**365 ประโยคทั่วไปต่อภาษา**) ใช้เฉพาะสำหรับการแจ้งเตือนเมื่อจับเวลาพื้นหลังเสร็จสิ้น ทั้งสองจะเคารพตัวกรองภาษาคำคมที่คุณตั้งค่าไว้

### เทคนิค Pomodoro คืออะไร?

เทคนิค Pomodoro เป็นวิธีการจัดการเวลา: ทำงานเป็นช่วงเวลาอย่างมีสมาธิ (โดยดั้งเดิม 25 นาที) แล้วพักสั้น หลังจากหลายรอบให้พักยาว iPomodoro จะทำให้จังหวะนี้เป็นอัตโนมัติ เพื่อให้คุณมุ่งเน้นงานแทนที่จะมองนาฬิกา

### iPomodoro ต่างจากเวอร์ชัน Flutter เก่าอย่างไร?

นี่คือ **การเขียนใหม่ด้วย SwiftUI แบบสมบูรณ์** สำหรับแพลตฟอร์ม Apple แนวคิดหลักเหมือนเดิม — Pomodoro, ตัวจับเวลาสำหรับศึกษา, งานถอยหลัง — แต่ประสิทธิภาพเนทีฟ, กิจกรรมสด, วิดเจ็ตสมัยใหม่, และการรวมเข้ากับ iOS อย่างแน่นหนามากขึ้น

### จำเป็นต้องมีบัญชีหรือการเชื่อมต่ออินเทอร์เน็ตไหม?

ไม่จำเป็นต้องมีบัญชี iPomodoro ตัวจับเวลา สถิติการศึกษา ธีม และวิดเจ็ตทำงาน **ออฟไลน์โดยสมบูรณ์** บนอุปกรณ์ของคุณ **ทางเลือก:** เปิดใช้งาน **ซิงค์งานด้วย iCloud** (งาน → เกียร์) และ/หรือ **ซิงค์สถิติการศึกษาด้วย iCloud** (สถิติ → เกียร์) เพื่อรวมข้อมูลระหว่างอุปกรณ์ที่ลงชื่อเข้าใช้ด้วย Apple ID เดียวกัน ซึ่งใช้ Apple CloudKit ไม่ใช่เซิร์ฟเวอร์ของเรา อินเทอร์เน็ตยังใช้สำหรับการอัปเดต App Store หรืออีเมลตอบรับอีกด้วย 

### สถิติการศึกษาทำงานอย่างไร? 

เปิดแท็บ **สถิติ** กรองตามทั้งหมด / Pomodoro / ตัวจับเวลาการศึกษา และตามวันนี้ / สัปดาห์ / เดือน / ปี / เวลาทั้งหมด / **ช่วงวันที่ที่กำหนดเอง** แดชบอร์ดจะแสดง **ภาพรวมของวันนี้**, **ความคืบหน้าของเป้าหมาย**, การเปรียบเทียบแบบสัปดาห์ต่อสัปดาห์, **แผนที่ความนิยมรายเดือน**, **ความสำเร็จ**, แผนภูมิวันทำงาน/ช่วงเวลาของวัน และ **รายละเอียดตามงานที่เชื่อมโยง** แตะ **ไอคอนรูปเฟือง** เพื่อดูเป้าหมาย ตัวเลือกเสริม **การซิงค์ iCloud** กฎการนับ **การส่งออก/นำเข้า CSV** และการเก็บรักษาข้อมูล สถิติ **ไม่เคยอัปโหลดไปยังเซิร์ฟเวอร์ของเรา** (ตัวเลือก iCloud ใช้ Apple CloudKit ภายใต้ Apple ID ของคุณ) 

### ฉันสามารถส่งออกหรือนำเข้าสถิติการศึกษาได้หรือไม่?

ใช่. **แท็บสถิติ → เกียร์ → ส่งออก** แชร์ไฟล์ CSV ผ่านแผ่นแบ่งปันของระบบ **นำเข้า** ยอมรับรูปแบบเดียวกัน (`kind,started_at,ended_at,duration_seconds,outcome` บวกตัวเลือก `task_id,task_title,cloud_id`) — เลือก **รวม** (ข้ามรายการที่ซ้ำกัน) หรือ **แทนที่ทั้งหมด** มีประโยชน์สำหรับการสำรองข้อมูลหรือการย้ายข้อมูลด้วยตนเอง สำหรับการซิงค์ข้ามอุปกรณ์อัตโนมัติ ให้เปิดใช้งาน **ซิงค์สถิติการศึกษากับ iCloud** แทน 

### ฉันสามารถแบ่งปันสถิติของฉันเป็นรูปภาพได้หรือไม่ 

ใช่. iPomodoro สามารถเรนเดอร์ **การ์ดสแนปชอตของแบรนด์** (โฟกัสเมตริก + รหัส QR ของ App Store) สำหรับ **แดชบอร์ดสถิติ** (ส่วนแบ่งแถบเครื่องมือ) **รายงานรอบระยะเวลา** สรุป **ระหว่างปีในการทบทวน** และ **ความสำเร็จ** (รายการทั้งหมดหรือป้ายสถานะเดียว) การ์ดแบ่งปันสถิติใช้สี **ธีมของหน้าแท็บสถิติ** คุณยังสามารถแชร์ **การ์ดโปรโมตแอป** ได้จากการตั้งค่า → แชร์แอป 

### ฉันสามารถซิงค์สถิติการเรียนกับ iCloud ได้หรือไม่ 

ใช่ — **แท็บสถิติ → เกียร์ → ซิงค์สถิติการศึกษากับ iCloud** นี่คือ **แยก** จากการซิงค์ iCloud ของงาน เซสชันรวมโดย `cloudId` ในอุปกรณ์ Apple ID ของคุณผ่านประเภทบันทึก CloudKit `StudySession` **การตั้งค่าเป้าหมายรายวัน** (`StatsGoals`) และ **สถานะการปลดล็อก/การเฉลิมฉลองความสำเร็จ** (`StatsAchievements`) ซิงค์ภายใต้การสลับเดียวกันเมื่อเปิดใช้งาน

### เป้าหมายโฟกัสรายวันทำงานอย่างไร 

**สถิติ → เกียร์ → เป้าหมาย**: ตั้งค่าจำนวน Pomodoro รายวัน นาทีโฟกัสรายวัน และนาทีโฟกัสรายสัปดาห์ ความคืบหน้าจะปรากฏบนแดชบอร์ดสถิติและวิดเจ็ต **สถิติวันนี้** เมื่อเปิดใช้งาน 

### ฉันจะเชื่อมโยงงานนับถอยหลังกับเซสชันโฟกัสได้อย่างไร 

ในหน้าจอ Pomodoro หรือ Study Timer ให้แตะ **ลิงก์งาน** และเลือกงาน หรือจาก **งาน** ให้กดงานค้างไว้ → **โฟกัสด้วย Pomodoro** หรือ **โฟกัสด้วยตัวจับเวลาการเรียน** เซสชันที่เสร็จสมบูรณ์จะจัดเก็บชื่องานสำหรับ **รายละเอียดตามงาน** ในสถิติ 

### ฉันจะปักหมุดหรือเรียงลำดับงานได้อย่างไร 

ในแท็บ **งาน** ให้ปัดแถวเพื่อ **ปักหมุด** หรือใช้เมนูจัดเรียงในแถบนำทาง เข้าสู่โหมดจัดลำดับใหม่เพื่อ **ลาก** งาน — การเรียงลำดับจะสลับไปตามลำดับที่กำหนดเองโดยอัตโนมัติ งานที่ปักหมุดไว้จะปรากฏในส่วนของตนเองที่ด้านบน 

### การซิงค์งาน iCloud ทำงานอย่างไร 

แท็บงาน → เกียร์ → สลับ **ซิงค์งานกับ iCloud** งานจะผสานตามเวลาที่แก้ไขล่าสุดในอุปกรณ์ Apple ID ของคุณ Pomodoro / ตัวจับเวลาการศึกษาอยู่ในท้องถิ่น **สถิติการศึกษา** สามารถเลือกซิงค์แยกกันได้ (สถิติ → เกียร์) คุณต้องลงชื่อเข้าใช้ iCloud ในการตั้งค่า iOS การซิงค์ยังทำงานเมื่อคุณกลับไปที่แอป

### ภาพแชร์จากแดชบอร์ดสถิติรวมอะไรบ้าง?

แตะ **แชร์** ที่แถบเครื่องมือแท็บสถิติ การ์ดยาวจะแสดงผลตาม **ช่วงเวลาและขอบเขตปัจจุบัน** ของคุณ — ฮีโร่วันนี้, ความคืบหน้าเป้าหมาย, แผนที่ความร้อน, แผนภูมิวัน/ชั่วโมง, การแยกงาน, แถบแนวโน้ม, และเซสชันล่าสุด — รวมถึงแบรนด์และรหัส QR ของ App Store สีตรงกับ **ธีมหน้าแท็บสถิติ** ของคุณ

### ฉันปรับแต่งธีมของแท็บสถิติได้ไหม?

ได้. **แท็บสถิติ → เกียร์ → ธีม** — มีตัวควบคุมแถบชื่อเรื่องและกราดิเอนต์พื้นหลังเหมือนกับ Pomodoro, Study Timer, และ Tasks ค่าเริ่มต้นเป็นสีแดงโฟกัส (`#E53935` / `#EF9A9A`) สีแท็บสถิติ, แถบการนำทาง, และ **การ์ดแชร์สถิติ** ทั้งหมดจะทำตามสีธีมหน้านี้

### ความสำเร็จทำงานอย่างไร?

ป้ายท้องถิ่นทั้งเก้าจะปลดล็อกเมื่อคุณบรรลุเป้าหมาย — Pomodoro แรก, การต่อเนื่อง, Pomodoro ทั้งหมด, ชั่วโมงโฟกัส, เป้าหมายรายวันที่สำเร็จ และอื่นๆ อีกมากมาย เมื่อคุณปลดล็อกป้ายสถานะใหม่ **การเฉลิมฉลองแบบเต็มหน้าจอ** จะปรากฏบนแท็บสถิติ (แตะ **ดำเนินการต่อ** เพื่อปิด) เปิด **สถิติ → เกียร์ → ความสำเร็จ** เพื่อเรียกดูตาราง **แตะป้าย** เพื่อดูแผ่นรายละเอียด แบ่งปัน **รายการทั้งหมด** จากแถบเครื่องมือรางวัลพิเศษ หรือ **ป้ายสถานะเดียว** จากหน้าจอรายละเอียด ป้ายสถานะจะถูกจัดเก็บไว้ในอุปกรณ์ เมื่อเปิดใช้งานการซิงค์ iCloud ปลดล็อก และเฉลิมฉลองสถานะการผสานระหว่างอุปกรณ์ของคุณผ่าน CloudKit — ไม่ได้อัปโหลดไปยังเซิร์ฟเวอร์ของเรา 

### ฉันจะเรียกดูเดือนที่ผ่านมาบน focus heatmap ได้อย่างไร 

บนแดชบอร์ดสถิติ ให้ใช้ลูกศร **เดือนก่อนหน้า/เดือนถัดไป** บนการ์ดแผนที่ความร้อน แตะ **ชื่อเดือน** เพื่อเปิดชีต **ตัวเลือกปี + เดือน** หรือแตะ **เดือนนี้** เพื่อข้ามกลับไปยังเดือนปัจจุบัน 

### เหตุใดวันที่ในอนาคตบนแผนที่ความร้อนจึงดูแตกต่างออกไป 

วันหลังจากวันนี้ในเดือนปัจจุบันจะปรากฏเป็น **ตัวยึดตำแหน่งเส้นประ** โดยมีการเติมสีอ่อนลง — วันเหล่านั้นจะไม่นับเป็นวันที่โฟกัส วันที่ผ่านมาและวันนี้ใช้สีความเข้มปกติ 

### ฉันจะเพิ่มวิดเจ็ตสถิติวันนี้ได้อย่างไร

กดหน้าจอหลักค้างไว้ → **+** → ค้นหา **iPomodoro** → เพิ่ม **สถิติของวันนี้** (เล็ก **กลาง ใหญ่** หรือหน้าจอล็อคเป็นสี่เหลี่ยม / อินไลน์) มันแสดงให้เห็นโฟกัสของวันนี้ ความคืบหน้าของเป้าหมาย Pomodoro และ **รายสัปดาห์** และสถิติต่อเนื่อง 

### ฉันจะเพิ่มวิดเจ็ตงานได้อย่างไร? 

กดหน้าจอหลักค้างไว้ → **+** → ค้นหา **iPomodoro** → เพิ่ม **งานนับถอยหลัง** (เล็ก / กลาง / ใหญ่) มันแสดงงานที่ปักหมุดที่กำลังจะมาถึงและวันที่เหลือ เปิดแอปหลังจากแก้ไขงานเพื่อการรีเฟรชที่เร็วที่สุด 

### ฉันสามารถรีเฟรชใบเสนอราคาวิดเจ็ตแรงจูงใจได้หรือไม่ 

บน **iOS 17+** ให้แตะปุ่ม **รีเฟรช** บนวิดเจ็ต Daily Motivation เพื่อเลือกคำพูดอื่นทันทีโดยไม่ต้องเปิดแอป 

### ทำไมการแจ้งเตือนไม่ทำงาน? 

ตรวจสอบ **แท็บการตั้งค่า → การแจ้งเตือน** เพื่อดูสถานะการอนุญาต iOS ปัจจุบันของคุณ ตัวจับเวลาและการแจ้งเตือนงานจำเป็นต้องเข้าถึงการแจ้งเตือน เปิดการตั้งค่าระบบหากการอนุญาตถูกปฏิเสธ 

### ฉันจะปรับแต่งงานและระยะเวลาพักได้อย่างไร 

แตะ **ไอคอนรูปเฟือง** บนแท็บ Pomodoro → ปรับแถวสเต็ปเปอร์ หรือ **แตะตัวเลขตัวจับเวลาขนาดใหญ่** บนหน้าจอหลักเพื่อเปิดตัวเลือกระยะเวลา ช่วงเวลาการพักยาว (ทุกๆ N pomodoros) ก็สามารถกำหนดค่าได้เช่นกัน 

### อะไรคือการยืนยันการเสร็จสิ้นขั้นตอน?

**แท็บ Pomodoro → ไอคอนรูปเฟือง → ยืนยันการเสร็จสิ้นของเฟส** เมื่อ **เปิด** iPomodoro จะแสดงไดอะล็อกหลังจากแต่ละช่วงทำงานหรือพักก่อนเริ่มเฟสถัดไป เมื่อ **ปิด** (ค่าเริ่มต้น) เฟสถัดไปจะเริ่มโดยอัตโนมัติหลังจากสัญญาณเตือนการเสร็จสิ้น — เป็นการไหลของ Pomodoro แบบคลาสสิกที่ไม่ต้องใช้มือ

### Live Activity และ Dynamic Island ทำงานอย่างไร?

เปิดใช้งาน **Live Activity** แยกในตั้งค่า Pomodoro และ Study Timer (ไอคอนรูปเฟือง) แต่ละโหมดจะมีนาฬิกานับถอยหลังบนหน้าจอล็อกและ Dynamic Island ของตัวเอง — ไม่เคยทับกัน ขณะเซสชันทำงาน คุณจะเห็นการนับถอยหลังแบบสด เมื่อเสร็จสิ้น จะมีฉากเฉลิมฉลองสั้น ๆ ปรากฏ 10 วินาที หาก iOS ปิดแอปขณะนาฬิกาของคุณยังปรากฏบนหน้าจอล็อก การเปิด iPomodoro ใหม่จะ **กู้คืน** เซสชันและกระโดดไปที่แท็บที่ทำงานอยู่ — **เว้นแต่** คุณเปิดผ่าน **Home Screen Quick Action** ซึ่งจะมีลำดับความสำคัญก่อน

### ฉันจะเพิ่มวิดเจ็ตได้อย่างไร?

กดค้างบนหน้าจอหลัก → **+** → ค้นหา **iPomodoro** (หรือ 爱番茄 / 愛番茄) เลือก **iPomodoro · Pomodoro** หรือ **iPomodoro · Study Timer** สำหรับการนับเวลาถอยหลัง (เป็นวิดเจ็ตแยกกัน), **Today's Stats** สำหรับความคืบหน้าการโฟกัสประจำวัน, **Countdown Tasks** สำหรับกำหนดเวลาส่งงาน หรือ **Daily Motivational Quote** สำหรับคำคมประจำวัน สำหรับวิธีการใช้งานทีละขั้นตอน เปิด **Settings → Widgets → How to Use**  

### ทำไมวิดเจ็ตตัวจับเวลาของฉันถึงไม่อัปเดต?

Pomodoro และ Study Timer เป็น **วิดเจ็ตแยกกัน** เริ่มหรือหยุดชั่วคราวในแท็บที่ **ตรงกัน** และตรวจสอบว่าคุณเพิ่มวิดเจ็ตถูกต้องหรือไม่ iOS อาจชะลอการรีเฟรชเพื่อประหยัดแบตเตอรี่ — เปิดแอปครั้งเดียวเพื่อซิงค์เร็วขึ้น  

### วิดเจ็ตตัวจับเวลาที่เก่าหายไปไหน?

ตัวจับเวลาตอนนี้คือ **iPomodoro · Pomodoro** และ **iPomodoro · Study Timer** ลบวิดเจ็ตตัวจับเวลาที่เก่าออกและเพิ่มตัวใหม่จากแกลเลอรีวิดเจ็ต  

### คำคมแรงบันดาลใจประจำวันทำงานอย่างไร?

ใบเสนอราคาหนึ่งรายการจะถูกเลือกตามที่กำหนดในแต่ละวันโดยใช้ `(year × 400 + dayOfYear) % total` กรองภาษาคำพูดภายใต้ **การตั้งค่า → การตั้งค่าคำพูดสร้างแรงบันดาลใจ → ภาษาคำพูดสร้างแรงบันดาลใจ** (ทั้งหมด / ตัวย่อ / ตัวเต็ม / อังกฤษ) คำพูดเดียวกันนี้ปรากฏในวิดเจ็ตแรงจูงใจและคำใบ้กิจกรรมสดจนถึงเที่ยงคืน เรียกดูคำพูดแบบสุ่มใน **การตั้งค่า → การตั้งค่าคำพูดสร้างแรงบันดาลใจ → กวีนิพนธ์คำพูดสร้างแรงบันดาลใจ** (เต็มหน้าจอ ทีละรายการ) 

### พื้นหลังวิดเจ็ตสามารถติดตามธีมของฉันได้หรือไม่? 

ใช่. **การตั้งค่า → วิดเจ็ต → พื้นหลังวิดเจ็ตตามธีม** สะท้อนการไล่ระดับสีส่วนกลางของคุณบนวิดเจ็ตหน้าจอหลักและหน้าจอล็อค ปิดการตั้งค่านี้สำหรับพื้นหลังสีขาวสะอาด (สว่าง) หรือระบบสีเข้ม โดยยังคงรักษาสีเน้นไว้บนชื่อเรื่อง 

### การแจ้งเตือนงานถึงกำหนดทำงานอย่างไร 

เมื่อสร้างหรือแก้ไขงาน ให้เปิดใช้งาน **การแจ้งเตือนวันครบกำหนด** และตั้งค่าวันที่/เวลาเป้าหมายในอนาคต การแจ้งเตือนในท้องถิ่นจะเริ่มทำงานทันที จัดการการแจ้งเตือนที่รอดำเนินการภายใต้ **แท็บงาน → เกียร์ → การแจ้งเตือนงานครบกำหนด** — แตะแถวเพื่อแก้ไขหรือ **ลบ** งานจากด้านล่างสุดของแผ่นแก้ไข การปัดเพื่อลบในรายการงานยังคงใช้งานได้เช่นกัน 

### ฉันจะลบงานขณะแก้ไขได้อย่างไร

เปิดงานจากรายการหรือจาก **การแจ้งเตือนงานถึงกำหนด** จากนั้นเลื่อนไปที่ด้านล่างของแผ่นแก้ไขแล้วแตะ **ลบ** ยืนยันในการแจ้งเตือน งานใหม่ (สร้างโฟลว์) ไม่แสดงปุ่มลบ 

### เหตุใดฉันจึงไม่สามารถเปิดใช้งานการแจ้งเตือนสำหรับวันที่ที่ผ่านมาได้ 

หากเลยวันที่เวลาเป้าหมายไปแล้ว ปุ่มสลับการเตือนจะถูกซ่อน และการเตือนที่มีอยู่จะถูกปิดใช้งานโดยอัตโนมัติ ไม่มีอะไรสำคัญเหลือให้กำหนดเวลาอีกต่อไป 

### ฉันสามารถใช้ภาษาอื่นนอกเหนือจากระบบของฉันได้หรือไม่? 

ใช่. ไปที่ **แท็บการตั้งค่า → ภาษา** และเลือกภาษาอังกฤษ จีนตัวย่อ หรือจีนตัวเต็ม ชื่อแอปบนหน้าจอหลักของคุณเป็นไปตามภาษาของระบบ UI ในแอปเป็นไปตามตัวเลือกในแอปของคุณ 

### แอปรวบรวมข้อมูลของฉันหรือไม่ 

ไม่มีการวิเคราะห์ ไม่มีการติดตาม ตัวจับเวลาและสถิติการศึกษาจะยังคงอยู่ในอุปกรณ์ของคุณตามค่าเริ่มต้น งานและเซสชันการศึกษาจะซิงค์กับ **iCloud ของคุณ** เฉพาะเมื่อคุณเปิดใช้งานการสลับที่แยกกัน เราไม่ได้รับข้อมูลงานหรือตัวจับเวลาของคุณบนเซิร์ฟเวอร์ของเรา ดู [นโยบายความเป็นส่วนตัว](../privacy) ของเราสำหรับรายละเอียดทั้งหมด 

### macOS จะรองรับหรือไม่ 

มีการวางแผนรองรับ macOS โปรเจ็กต์ Xcode มีการกำหนดค่า macOS SDK อยู่แล้ว คอยติดตามการอัปเดตบน App Store 

### ยังต้องการความช่วยเหลืออยู่ใช่ไหม?

ติดต่อเราได้ที่ [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) โดยปกติเราจะตอบกลับภายใน48ชั่วโมง

&lt;/section&gt;

</section>
<section lang="de" markdown="1">

### Warum sollte ich iPomodoro anderen Pomodoro-Apps vorziehen?

iPomodoro ist eine **native SwiftUI**-App, die für Apple-Plattformen entwickelt wurde — kein verpackter Web-Timer. Du erhältst **fünf integrierte Tabs** (Pomodoro, Study Timer, Aufgaben, Statistik, Einstellungen), **doppelte Live-Aktivitäten**, **fünf Widget-Familien**, **9 Erfolgsabzeichen**, **über 1000 Zitate auf dem Gerät**, **Siri- & URL-Kurzbefehle** sowie **optionale iCloud-Synchronisation** — das alles mit **null Analysen** und **ohne erforderliches Konto**. Eine ruhige App, die Fokus, Deadlines und Fortschrittsverfolgung von Anfang bis Ende abdeckt.

### Wo befinden sich die Timer- und Aufgabeneinstellungen?

Timer-Dauern, Sounds, Live-Aktivität, Seitenhintergrundfarben, optional **Fokus-Modus-Erinnerung** und (nur Pomodoro) optionale **Phase-Abschluss-Bestätigung** befinden sich unter dem **Zahnrad-Symbol** jeder Registerkarte (Pomodoro, Lern-Timer, Aufgaben oder **Statistiken**). Die globale **Einstellungen**-Registerkarte enthält Erscheinungsbild, Sprache, **Startbildschirm-Verknüpfungen**, **App-Anleitung**, Benachrichtigungsberechtigung, motivierende Zitate (einschließlich **täglicher Motivationsbenachrichtigung**), Widget-Anleitung, Feedback und Informationen — nicht die Modi-spezifischen Dauern. **Statistiken**-Einstellungen (Seitenhintergrund, Ziele, optionale iCloud-Synchronisierung, Erfolge, Zählregeln, CSV, Aufbewahrung) befinden sich unter **Statistik-Registerkarte → Zahnrad**.

### Wie funktionieren Startbildschirm-Verknüpfungen und Siri?

**Drücken Sie lange auf das App-Symbol**, um schnelle Aktionen auszuführen – Pomodoro, Lerntimer, Aufgaben, Statistiken, ein Motivationszitat oder Feedback zu öffnen. Passen Sie an, welche vier unter **Einstellungen → App-Einstellungen → Startbildschirm-Verknüpfungen** angezeigt werden (zum Neuordnen ziehen). Sie können dieselben Ziele auch über **`iPomodoro://`** URLs öffnen (`pomodoro`, `study`, `tasks`, `stats`, `motivation`, `feedback`; `iPomodoros://` funktioniert auch). Sehen Sie sich die vollständige [URL-Schema-Referenz](../url-scheme) an. **Siri / Shortcuts-App** kann über integrierte App-Shortcuts Tabs öffnen oder antworten: „Wie lange habe ich mich heute in iPomodoro konzentriert?“*. 

### Was ist der In-App-App-Guide? 

**Einstellungen → App-Einstellungen → App-Leitfaden** – ein zusammenklappbares Tutorial, das alle fünf Registerkarten, Widgets, Verknüpfungen, iCloud und FAQ abdeckt (ähnlicher Stil wie der Widget-Leitfaden). 

### Kann iPomodoro den Fokusmodus für mich aktivieren? 

Nein – iOS erlaubt es Drittanbieter-Apps nicht, Focus direkt zu aktivieren. Die optionale **Fokusmodus-Erinnerung** (Pomodoro- oder Lerntimer-Zahnradeinstellungen) prüft, ob der Fokus ausgeschaltet ist, wenn Sie einen Timer starten, und zeigt eine Warnung an; Sie können **Einstellungen** über die Benachrichtigung öffnen, müssen den Fokus jedoch selbst aktivieren. 

### Kann ich für jede Countdown-Aufgabe eine Farbe auswählen?

Ja. Beim Hinzufügen oder Bearbeiten einer Aufgabe wählen Sie eine von **9 Akzentfarben**. Die Liste und das **Countdown-Aufgaben**-Widget verwenden diese Farbe pro Zeile. Die Farben werden über iCloud synchronisiert, wenn die Aufgaben-Synchronisation aktiviert ist.

### Kann ich Statistiken nach einem benutzerdefinierten Datumsbereich filtern?

Ja. Auf der Registerkarte Statistiken (oder im Periodenbericht) wählen Sie **Benutzerdefiniert** in der Periodenleiste und legen dann Start- und Enddatum fest. Der Bereich wird gespeichert, wenn **Filter merken** in den Statistik-Einstellungen aktiviert ist.

### Kann ich eine tägliche Motivationsbenachrichtigung erhalten?

Ja. **Einstellungen → Motivationszitat-Einstellungen** enthält eine optionale **tägliche Motivationsbenachrichtigung** — wählen Sie eine Uhrzeit und iPomodoro plant eine wiederholte **lokale Benachrichtigung** mit einer zufälligen Zeile aus dem auf dem Gerät gespeicherten Benachrichtigungs-Zitate-Pool (kein Netzwerk). Getrennt von Timer-Abschlusswarnungen.

### Was ist der Unterschied zwischen täglichen Zitaten und Benachrichtigungszitaten?

**Dialog-/tägliche Zitate** (**1000+** zusammen, wenn der Filter auf Alle steht — vereinfachtes Chinesisch + Englisch) versorgen das Start-Popup, die Einstellungen-Browse, den Live-Aktivitäts-Hinweis und das Motivation-Widget. **Benachrichtigungszitate** sind ein separater, geräteinterner Pool (**365 allgemeine Zeilen pro Sprache**), der nur für Hintergrund-Timer-Abschlussbenachrichtigungen verwendet wird. Beide respektieren Ihren Zitat-Sprachfilter in den Einstellungen.  

### Was ist die Pomodoro-Technik?  

Die Pomodoro-Technik ist eine Methode des Zeitmanagements: arbeite in fokussierten Intervallen (klassisch 25 Minuten) und mache dann eine kurze Pause. Nach mehreren Zyklen, mache eine längere Pause. iPomodoro automatisiert diesen Rhythmus, damit du dich auf die Arbeit und nicht auf die Uhr konzentrieren kannst.  

### Wie unterscheidet sich iPomodoro von der alten Flutter-Version?  

Dies ist eine **vollständige SwiftUI-Neuschreibung** für Apple-Plattformen. Gleiche Kernideen — Pomodoro, Lern-Timer, Countdown-Aufgaben — aber mit nativer Leistung, Live-Aktivität, modernen Widgets und engerer iOS-Integration.  

### Brauche ich ein Konto oder eine Internetverbindung?

Es ist kein iPomodoro-Konto erforderlich. Timer, Studienstatistiken, Themen und Widgets laufen **vollständig offline** auf Ihrem Gerät. **Optional:** aktivieren Sie **Aufgaben mit iCloud synchronisieren** (Aufgaben → Zahnrad) und/oder **Studienstatistiken mit iCloud synchronisieren** (Statistik → Zahnrad), um Daten über Geräte hinweg zusammenzuführen, die bei derselben Apple-ID angemeldet sind – dies verwendet Apple CloudKit, nicht unsere Server. Das Internet wird auch für App-Store-Updates oder Feedback-E-Mails genutzt. 

### Wie funktioniert die Studienstatistik? 

Öffnen Sie die Registerkarte **Statistiken**. Filtern Sie nach Alle / Pomodoro / Lerntimer und nach Heute / Woche / Monat / Jahr / Alle Zeiten / **Benutzerdefinierter Datumsbereich**. Das Dashboard zeigt **die heutige Übersicht**, **Zielfortschritt**, einen Wochenvergleich, eine **monatliche Heatmap**, **Erfolge**, Wochentags-/Tageszeitdiagramme und **Aufschlüsselung nach verknüpften Aufgaben**. Tippen Sie auf das **Zahnradsymbol** für Ziele, optionale **iCloud-Synchronisierung**, Zählregeln, **CSV-Export/Import** und Datenaufbewahrung. Statistiken werden **niemals auf unsere Server hochgeladen** (optional nutzt iCloud Apple CloudKit unter Ihrer Apple-ID). 

### Kann ich Studienstatistiken exportieren oder importieren?

Ja. **Registerkarte „Statistik“ → Zahnrad → Exportieren** gibt eine CSV-Datei über das Systemfreigabeblatt frei. **Importieren** akzeptiert das gleiche Format (`kind,started_at,ended_at,duration_seconds,outcome` plus optional `task_id,task_title,cloud_id`) – wählen Sie **zusammenführen** (Duplikate überspringen) oder **alle ersetzen**. Nützlich für Backups oder manuelle Migration. Aktivieren Sie für die automatische geräteübergreifende Synchronisierung stattdessen **Studienstatistiken mit iCloud synchronisieren**. 

### Kann ich meine Statistiken als Bild teilen? 

Ja. iPomodoro kann **Marken-Snapshot-Karten** (Fokusmetriken + App Store-QR-Code) für das **Statistik-Dashboard** (Symbolleistenfreigabe), **Zeitraumberichte**, **Jahresrückblick**-Zusammenfassungen und **Erfolge** (vollständige Liste oder einzelnes Abzeichen) rendern. Statistik-Freigabekarten verwenden die Farben Ihres **Registerkartenthemas „Statistik“**. Sie können eine **App-Werbekarte** auch über Einstellungen → App teilen teilen. 

### Kann ich Studienstatistiken mit iCloud synchronisieren? 

Ja – **Registerkarte „Statistik“ → Zahnrad → Studienstatistiken mit iCloud synchronisieren**. Dies ist **getrennt** von der Aufgabe der iCloud-Synchronisierung. Sitzungen werden nach `cloudId` auf Ihren Apple-ID-Geräten über den CloudKit-Eintragstyp `StudySession` zusammengeführt. **Tageszieleinstellungen** (`StatsGoals`) und **Erfolgs-Freischalt-/Feierstatus** (`StatsAchievements`) werden bei Aktivierung unter demselben Schalter synchronisiert.

### Wie funktionieren tägliche Fokusziele? 

**Statistiken → Ausrüstung → Ziele**: Legen Sie die tägliche Pomodoro-Anzahl, die täglichen Fokusminuten und die wöchentlichen Fokusminuten fest. Der Fortschritt wird im Statistik-Dashboard und im Widget „Heutige Statistiken“ angezeigt, sofern aktiviert. 

### Wie verknüpfe ich eine Countdown-Aufgabe mit einer Fokussitzung? 

Tippen Sie im Pomodoro- oder Study-Timer-Bildschirm auf **Aufgabe verknüpfen** und wählen Sie eine Aufgabe aus. Oder drücken Sie in **Aufgaben** lange auf eine Aufgabe → **Fokus mit Pomodoro** oder **Fokus mit Lerntimer**. Abgeschlossene Sitzungen speichern den Aufgabentitel für die **Aufschlüsselung nach Aufgabe** in der Statistik. 

### Wie kann ich Aufgaben anpinnen oder neu anordnen? 

Wischen Sie auf der Registerkarte **Aufgaben** über eine Zeile zu **Anheften** oder verwenden Sie das Sortiermenü in der Navigationsleiste. Wechseln Sie in den Neuordnungsmodus, um Aufgaben zu **ziehen** – die Sortierung wechselt automatisch zur benutzerdefinierten Reihenfolge. Angeheftete Aufgaben werden oben in einem eigenen Abschnitt angezeigt. 

### Wie funktioniert die iCloud-Aufgabensynchronisierung? 

Registerkarte „Aufgaben“ → Zahnrad → Umschalten zwischen **Aufgaben mit iCloud synchronisieren**. Aufgaben werden nach dem Zeitpunkt der letzten Änderung auf Ihren Apple-ID-Geräten zusammengeführt. Pomodoro / Lerntimer bleiben vor Ort. **Studienstatistiken** können optional separat synchronisiert werden (Statistiken → Zahnrad). Sie müssen in den iOS-Einstellungen bei iCloud angemeldet sein. Die Synchronisierung wird auch ausgeführt, wenn Sie zur App zurückkehren.

### Was beinhaltet das Bild zum Teilen des Statistik-Dashboards?

Tippen Sie auf **Teilen** in der Symbolleiste des Statistik-Tabs. Die lange Karte spiegelt Ihre **aktuellen Filter für Umfang und Zeitraum** wider – der heutige Held, Zielerreichung, Heatmap, Wochentags-/Stunden-Diagramme, Aufgabenaufteilung, Trendbalken und aktuelle Sitzungen – sowie Branding und einen App Store QR-Code. Die Farben entsprechen Ihrem **Seiten-Theme des Statistik-Tabs**.

### Kann ich das Theme des Statistik-Tabs anpassen?

Ja. **Statistik-Tab → Zahnrad → Theme** — die gleichen Titelbalken- und Hintergrundverlaufs-Steuerungen wie bei Pomodoro, Study Timer und Aufgaben. Standard ist Fokus-Rot (`#E53935` / `#EF9A9A`). Die Tönung des Statistik-Tabs, die Navigationsleiste und **Statistik-Share-Karten** folgen alle diesen Seiten-Theme-Farben.

### Wie funktionieren Erfolge?

Neun lokale Abzeichen werden freigeschaltet, wenn Sie Meilensteine ​​erreichen – erster Pomodoro, Streaks, gesamte Pomodoros, Fokusstunden, tägliche Zielerreichung und mehr. Wenn Sie ein neues Abzeichen freischalten, wird auf der Registerkarte „Statistiken“ eine **Vollbild-Feier** angezeigt (tippen Sie zum Schließen auf **Weiter**). Öffnen Sie **Statistik → Ausrüstung → Erfolge**, um das Raster zu durchsuchen. **Tippen Sie auf ein Abzeichen**, um ein Detailblatt anzuzeigen. Teilen Sie die **vollständige Liste** über die Erfolgssymbolleiste oder ein **einzelnes Abzeichen** über den Detailbildschirm. Abzeichen werden auf dem Gerät gespeichert; Wenn die iCloud-Synchronisierung aktiviert ist, werden der Entsperr- und Speicherstatus über CloudKit auf Ihren Geräten zusammengeführt – nicht auf unsere Server hochgeladen. 

### Wie durchsuche ich vergangene Monate auf der Fokus-Heatmap? 

Verwenden Sie im Statistik-Dashboard die Pfeile **Vorheriger/Nächster Monat** auf der Heatmap-Karte, tippen Sie auf den **Monatstitel**, um ein Blatt **Jahr + Monatsauswahl** zu öffnen, oder tippen Sie auf **Diesen Monat**, um zum aktuellen Monat zurückzukehren. 

### Warum sehen zukünftige Daten auf der Heatmap anders aus? 

Tage nach dem heutigen Tag im aktuellen Monat werden als **Platzhalter mit gestricheltem Umriss** und einer helleren Füllung angezeigt – sie werden nicht als Fokustage gezählt. Vergangene Tage und heute verwenden die Farben normaler Intensität. 

### Wie füge ich das Widget „Heutige Statistiken“ hinzu?

Drücken Sie lange auf den Startbildschirm → **+** → suchen Sie nach **iPomodoro** → fügen Sie **Heutige Statistiken** hinzu (Klein, **Mittel, Groß** oder Sperrbildschirm rechteckig/inline). Es zeigt den heutigen Fokus, den Pomodoro und den **wöchentlichen** Zielfortschritt sowie die Serie. 

### Wie füge ich das Aufgaben-Widget hinzu? 

Drücken Sie lange auf den Startbildschirm → **+** → **iPomodoro** suchen → **Countdown-Aufgaben** hinzufügen (Klein / Mittel / Groß). Es zeigt anstehende angeheftete Aufgaben und die verbleibenden Tage an. Öffnen Sie die App, nachdem Sie Aufgaben bearbeitet haben, um eine schnellere Aktualisierung zu gewährleisten. 

### Kann ich das Motivations-Widget-Zitat aktualisieren? 

Tippen Sie unter **iOS 17+** auf die Schaltfläche **Aktualisieren** im Widget „Tägliche Motivation“, um sofort ein anderes Zitat auszuwählen, ohne die App zu öffnen. 

### Warum funktionieren Benachrichtigungen nicht? 

Überprüfen Sie **Registerkarte „Einstellungen“ → Benachrichtigungen** auf Ihren aktuellen iOS-Berechtigungsstatus. Timer- und Aufgabenerinnerungen erfordern Benachrichtigungszugriff. Öffnen Sie die Systemeinstellungen, wenn die Berechtigung verweigert wurde. 

### Wie kann ich die Arbeits- und Pausendauer anpassen? 

Tippen Sie auf das **Zahnradsymbol** auf der Registerkarte „Pomodoro“ → passen Sie die Stepperreihen an oder **tippen Sie auf die großen Timer-Ziffern** auf dem Hauptbildschirm, um eine Dauerauswahl zu öffnen. Ein langes Pausenintervall (alle N Pomodoros) ist ebenfalls konfigurierbar. 

### Was ist der Abschluss der Phase bestätigen?

**Pomodoro-Tab → Zahnrad → Phase als abgeschlossen bestätigen**. Wenn **ein**, zeigt iPomodoro nach jedem Arbeits- oder Pausenabschnitt einen Dialog, bevor die nächste Phase beginnt. Wenn **aus** (Standard), startet die nächste Phase automatisch nach dem Abschlussalarm — klassischer, freihändiger Pomodoro-Ablauf.

### Wie funktionieren Live-Aktivität und Dynamic Island?

Aktivieren Sie **Live-Aktivität** separat in den Pomodoro- und Study-Timer-Einstellungen (Zahnradsymbol). Jeder Modus erhält seinen **eigenen** Sperrbildschirm- und Dynamic-Island-Countdown — sie überschreiben sich niemals gegenseitig. Während einer Sitzung sehen Sie einen Live-Countdown; wenn sie abgeschlossen ist, erscheint eine kurze Feieranzeige für 10 Sekunden. Wenn iOS die App beendet, während Ihr Timer noch auf dem Sperrbildschirm angezeigt wird, stellt das erneute Öffnen von iPomodoro die Sitzung **wieder her** und springt zum aktiven Tab — **es sei denn**, Sie haben die App über eine **Home-Bildschirm-Schnellaktion** gestartet, die Priorität hat.

### Wie füge ich Widgets hinzu?

Langes Drücken des Startbildschirms → **+** → Suche nach **iPomodoro** (oder 爱番茄 / 愛番茄). Wähle **iPomodoro · Pomodoro** oder **iPomodoro · Study Timer** für Timer-Countdowns (sie sind separate Widgets), **Today's Stats** für den täglichen Fortschritt beim Fokus, **Countdown Tasks** für Fristen oder **Daily Motivational Quote** für das tägliche Zitat. Für Schritt-für-Schritt-Hilfe öffne **Einstellungen → Widgets → Anleitung**.

### Warum aktualisiert sich mein Timer-Widget nicht?

Pomodoro und Study Timer sind **separate Widgets**. Starte oder pausiere eine Sitzung im **entsprechenden Tab** und stelle sicher, dass du das richtige Widget hinzugefügt hast. iOS kann die Aktualisierung verzögern, um Akku zu sparen — öffne die App einmal, um schneller zu synchronisieren.

### Wo ist das alte Timer-Widget?

Timer sind jetzt **iPomodoro · Pomodoro** und **iPomodoro · Study Timer**. Entferne alle alten Timer-Widgets und füge die neuen aus der Widget-Galerie hinzu.

### Wie funktioniert das tägliche Motivationszitat?

Mit `(year × 400 + dayOfYear) % total` wird jeden Tag ein Angebot deterministisch ausgewählt. Filtern Sie die Zitatsprache unter **Einstellungen → Einstellungen für motivierende Zitate → Sprachen für motivierende Zitate** (Alle / Vereinfacht / Traditionell / Englisch). Das gleiche Zitat erscheint bis Mitternacht im Motivations-Widget und im Live-Aktivitätshinweis. Durchsuchen Sie zufällige Zitate unter **Einstellungen → Einstellungen für motivierende Zitate → Anthologie mit motivierenden Zitaten** (Vollbild, einzeln). 

### Können Widget-Hintergründe meinem Thema folgen? 

Ja. **Einstellungen → Widgets → Widget-Hintergrund folgt Thema** spiegelt Ihren globalen Akzentverlauf auf Start- und Sperrbildschirm-Widgets wider. Schalten Sie es aus, um einen sauberen weißen (hellen) oder systemdunklen Hintergrund zu erhalten, während die Akzentfarben auf den Titeln beibehalten werden. 

### Wie funktionieren Erinnerungen an fällige Aufgaben? 

Aktivieren Sie beim Erstellen oder Bearbeiten einer Aufgabe die **Erinnerung an Fälligkeitstermine** und legen Sie ein zukünftiges Zieldatum/eine zukünftige Zielzeit fest. Genau in diesem Moment wird eine lokale Benachrichtigung ausgelöst. Verwalten Sie ausstehende Erinnerungen unter **Registerkarte „Aufgaben“ → „Zahnrad“ → „Erinnerungen an fällige Aufgaben“ – tippen Sie unten auf dem Bearbeitungsblatt auf eine Zeile, um die Aufgabe zu bearbeiten oder zu **löschen**. Auch das Wischen zum Löschen in der Aufgabenliste funktioniert weiterhin. 

### Wie lösche ich eine Aufgabe während der Bearbeitung?

Öffnen Sie eine Aufgabe aus der Liste oder aus **Erinnerungen an fällige Aufgaben**, scrollen Sie dann zum Ende des Bearbeitungsblatts und tippen Sie auf **Löschen**. Bestätigen Sie in der Benachrichtigung. Bei neuen Aufgaben (Flow erstellen) wird keine Schaltfläche zum Löschen angezeigt. 

### Warum kann ich eine Erinnerung für ein vergangenes Datum nicht aktivieren? 

Wenn das Zieldatum/Uhrzeit bereits verstrichen ist, wird der Erinnerungsschalter ausgeblendet und alle vorhandenen Erinnerungen werden automatisch deaktiviert – es gibt nichts Sinnvolles mehr zu planen. 

### Kann ich eine andere Sprache als mein System verwenden? 

Ja. Gehen Sie zur **Registerkarte „Einstellungen“ → „Sprache“** und wählen Sie Englisch, vereinfachtes Chinesisch oder traditionelles Chinesisch aus. Der App-Name auf Ihrem Startbildschirm richtet sich nach der Systemsprache. Die In-App-Benutzeroberfläche folgt Ihrer In-App-Auswahl. 

### Sammelt die App meine Daten? 

Keine Analyse, kein Tracking. Timer und Studienstatistiken bleiben standardmäßig auf Ihrem Gerät. Aufgaben und Lernsitzungen werden nur dann mit **Ihrer iCloud** synchronisiert, wenn Sie die separaten Schalter aktivieren. Wir empfangen Ihre Aufgaben- oder Timerdaten nicht auf unseren Servern. Ausführliche Informationen finden Sie in unserer [Datenschutzerklärung](../privacy). 

### Wird macOS unterstützt? 

macOS-Unterstützung ist geplant. Das Xcode-Projekt enthält bereits die macOS SDK-Konfiguration; Bleiben Sie auf dem Laufenden für Updates im App Store. 

### Brauchen Sie noch Hilfe?

Kontaktieren Sie uns unter [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com). Wir antworten normaler weise innerhalb von 48 Stunden.

&lt;/Abschnitt&gt;

</section>
<section lang="fr" markdown="1">

### Pourquoi devrais-je choisir iPomodoro plutôt que d'autres applications Pomodoro ?

iPomodoro est une application **native SwiftUI** conçue pour les plateformes Apple — ce n'est pas un minuteur basé sur le web. Vous bénéficiez de **cinq onglets intégrés** (Pomodoro, Minuteur d'étude, Tâches, Statistiques, Paramètres), de **deux Live Activities**, de **cinq familles de widgets**, de **9 badges de réussite**, de **plus de 1000 citations sur l'appareil**, de **raccourcis Siri et URL**, et de **la synchronisation iCloud en option** — le tout avec **aucune analyse** et **aucun compte requis**. Une application apaisante qui couvre la concentration, les délais et le suivi des progrès de A à Z.

### Où se trouvent les paramètres du minuteur et des tâches ?

Les durées du minuteur, les sons, l’Activité en direct, les couleurs du thème de la page, le **rappel optionnel du mode Focus**, et (Pomodoro seulement) la **confirmation de la fin de phase optionnelle** se trouvent sous l’**icône d’engrenage** de chaque onglet (Pomodoro, Minuteur d’étude, Tâches ou **Statistiques**). L’onglet global **Paramètres** contient l’apparence, la langue, les **raccourcis sur l’écran d’accueil**, le **Guide de l’application**, l’autorisation des notifications, les citations motivantes (y compris la **notification de motivation quotidienne**), le guide des widgets, les retours et les informations — pas les durées propres à chaque mode. Les paramètres **Statistiques** (thème de la page, objectifs, synchronisation iCloud optionnelle, réussites, règles de comptage, CSV, conservation) se trouvent sous **Onglet Statistiques → engrenage**.

### Comment fonctionnent les raccourcis sur l’écran d’accueil et Siri ?

**Appuyez longuement sur l'icône de l'application** pour des actions rapides : ouvrez Pomodoro, le minuteur d'étude, les tâches, les statistiques, une citation de motivation ou des commentaires. Personnalisez les quatre qui apparaissent sous **Paramètres → Paramètres de l'application → Raccourcis de l'écran d'accueil** (faites glisser pour réorganiser). Vous pouvez également ouvrir les mêmes destinations via les URL **`iPomodoro://`** (`pomodoro`, `study`, `tasks`, `stats`, `motivation`, `feedback` ; `iPomodoros://` fonctionne également). Consultez la [Référence du schéma d'URL] complète (../url-scheme). **L'application Siri/Raccourcis** peut ouvrir des onglets ou répondre *"Combien de temps ai-je été concentré aujourd'hui dans iPomodoro ?"* via les raccourcis d'application intégrés. 

### Qu'est-ce que le guide de l'application intégré à l'application ? 

**Paramètres → Paramètres de l'application → Guide de l'application** — un didacticiel pliable couvrant les cinq onglets, widgets, raccourcis, iCloud et FAQ (style similaire au guide des widgets). 

### iPomodoro peut-il activer le mode Focus pour moi ? 

Non : iOS n'autorise pas les applications tierces à activer directement Focus. Le **Rappel du mode de mise au point** en option (paramètres d'équipement Pomodoro ou Study Timer) vérifie si la mise au point est désactivée lorsque vous démarrez une minuterie et affiche une alerte ; vous pouvez ouvrir les **Paramètres** à partir de l'alerte, mais vous devez activer Focus vous-même. 

### Puis-je choisir une couleur pour chaque tâche du compte à rebours ?

Oui. Lors de l'ajout ou de la modification d'une tâche, choisissez l'une des **9 couleurs d'accent**. La liste et le widget **Tâches à compte à rebours** utilisent cette couleur par ligne. Les couleurs se synchronisent via iCloud lorsque la synchronisation des tâches est activée.

### Puis-je filtrer les statistiques par une plage de dates personnalisée ?

Oui. Dans l'onglet Statistiques (ou le rapport de période), sélectionnez **Personnalisé** dans la barre de période, puis définissez les dates de début et de fin. La plage est sauvegardée lorsque **Se souvenir du filtre** est activé dans les paramètres des Statistiques.

### Puis-je recevoir une notification de motivation quotidienne ?

Oui. **Paramètres → Paramètres de citation motivationnelle** inclut une **notification de motivation quotidienne** optionnelle — choisissez une heure et iPomodoro planifie une **notification locale** récurrente avec une ligne aléatoire du pool de citations disponibles sur l'appareil (sans réseau). C'est séparé des alertes de fin de minuterie.

### Quelle est la différence entre les citations quotidiennes et les citations de notification ?

**Dialogues/citations quotidiennes** (**1000+** combinées lorsque le filtre est Tout — chinois simplifié + anglais) alimentent la fenêtre contextuelle au démarrage, la navigation dans les paramètres, l'indice Live Activity et le widget Motivation. **Citations de notifications** sont un pool séparé sur l'appareil (**365 lignes générales par langue**) utilisé uniquement pour les alertes de fin de minuterie en arrière-plan. Les deux respectent votre filtre de langue des citations dans les Paramètres.

### Qu'est-ce que la technique Pomodoro ?

La technique Pomodoro est une méthode de gestion du temps : travailler par intervalles concentrés (classiquement 25 minutes), puis prendre une courte pause. Après plusieurs cycles, prendre une pause plus longue. iPomodoro automatise ce rythme pour que vous puissiez vous concentrer sur le travail, pas sur l'horloge.

### En quoi iPomodoro est-il différent de l'ancienne version Flutter ?

Ceci est une **réécriture complète en SwiftUI** pour les plateformes Apple. Même idée de base — Pomodoro, minuterie d'étude, tâches avec compte à rebours — mais avec des performances natives, Live Activity, widgets modernes et intégration iOS plus poussée.

### Ai-je besoin d'un compte ou d'une connexion Internet ?

Aucun compte iPomodoro n'est requis. Les minuteries, les statistiques d'étude, les thèmes et les widgets fonctionnent **entièrement hors ligne** sur votre appareil. **Facultatif :** activez **Synchroniser les tâches avec iCloud** (Tâches → équipement) et/ou **Synchroniser les statistiques d'étude avec iCloud** (Statistiques → équipement) pour fusionner les données sur tous les appareils connectés au même identifiant Apple. Cela utilise Apple CloudKit, pas nos serveurs. Internet est également utilisé pour les mises à jour de l'App Store ou les e-mails de commentaires. 

### Comment fonctionnent les statistiques d'études ? 

Ouvrez l'onglet **Statistiques**. Filtrer par Tous / Pomodoro / Minuterie d'étude et par Aujourd'hui / Semaine / Mois / Année / Tout le temps / **Plage de dates personnalisée**. Le tableau de bord affiche l'**aperçu du jour**, la **progression des objectifs**, une comparaison semaine après semaine, une **carte thermique mensuelle**, des **réalisations**, des graphiques des jours de la semaine et de l'heure et une **répartition par tâche liée**. Appuyez sur l'**icône d'engrenage** pour les objectifs, la **synchronisation iCloud** facultative, les règles de comptage, l'**exportation/importation CSV** et la conservation des données. Les statistiques ne sont **jamais téléchargées sur nos serveurs** (en option, iCloud utilise Apple CloudKit sous votre identifiant Apple). 

### Puis-je exporter ou importer des statistiques d'études ?

Oui. **Onglet Statistiques → engrenage → Exporter** partage un fichier CSV via la feuille de partage système. **Importer** accepte le même format (`kind,started_at,ended_at,duration_seconds,outcome` plus `task_id,task_title,cloud_id` facultatif) : choisissez **fusionner** (ignorer les doublons) ou **remplacer tout**. Utile pour la sauvegarde ou la migration manuelle. Pour une synchronisation automatique entre appareils, activez plutôt **Synchroniser les statistiques d'étude avec iCloud**. 

### Puis-je partager mes statistiques sous forme d'image ? 

Oui. iPomodoro peut restituer des **cartes instantanées de marque** (métriques de focus + code QR de l'App Store) pour le **tableau de bord de statistiques** (partage de la barre d'outils), les **rapports périodiques**, les résumés de l'**année en revue** et les **réalisations** (liste complète ou badge unique). Les cartes de partage de statistiques utilisent les couleurs de votre **thème de page à onglet Statistiques**. Vous pouvez également partager une **carte de promotion d'application** depuis Paramètres → Partager l'application. 

### Puis-je synchroniser les statistiques d'études avec iCloud ? 

Oui — **Onglet Statistiques → Équipement → Synchroniser les statistiques de l'étude avec iCloud**. Ceci est ** distinct ** de la tâche de synchronisation iCloud. Les sessions fusionnent par `cloudId` sur vos appareils Apple ID via le type d'enregistrement CloudKit `StudySession`. **Paramètres d'objectifs quotidiens** (`StatsGoals`) et **état de déverrouillage/célébration des succès** (`StatsAchievements`) se synchronisent sous la même bascule lorsqu'ils sont activés.

### Comment fonctionnent les objectifs de concentration quotidiens ? 

**Statistiques → équipement → Objectifs** : définissez le nombre quotidien de pomodoro, les minutes de concentration quotidiennes et les minutes de concentration hebdomadaires. La progression apparaît sur le tableau de bord Statistiques et sur le widget **Statistiques du jour** lorsqu'il est activé. 

### Comment lier une tâche de compte à rebours à une session de focus ? 

Sur l'écran Pomodoro ou Study Timer, appuyez sur **Lier la tâche** et choisissez une tâche. Ou depuis **Tâches**, appuyez longuement sur une tâche → **Concentrez-vous avec Pomodoro** ou **Concentrez-vous avec Study Timer**. Les sessions terminées stockent le titre de la tâche pour la **répartition par tâche** dans les statistiques. 

### Comment puis-je épingler ou réorganiser des tâches ? 

Dans l'onglet **Tâches**, faites glisser une ligne vers **Épingler** ou utilisez le menu de tri dans la barre de navigation. Passez en mode de réorganisation pour **faire glisser** les tâches : le tri passe automatiquement à l'ordre personnalisé. Les tâches épinglées apparaissent dans leur propre section en haut. 

### Comment fonctionne la synchronisation des tâches iCloud ? 

Onglet Tâches → équipement → basculer **Synchroniser les tâches avec iCloud**. Les tâches sont fusionnées selon l'heure de la dernière modification sur vos appareils Apple ID. Les minuteries Pomodoro / étude restent locales. **Les statistiques d'étude** peuvent éventuellement être synchronisées séparément (Statistiques → équipement). Vous devez être connecté à iCloud dans les paramètres iOS. La synchronisation s'exécute également lorsque vous revenez à l'application.

### Que comprend l'image de partage du tableau de bord des statistiques ?

Appuyez sur **Partager** dans la barre d'outils de l'onglet Statistiques. La grande carte reflète vos filtres **périmètre et période actuels** — héros du jour, progression des objectifs, carte de chaleur, graphiques par jour de la semaine/heure, répartition des tâches, barres de tendance et sessions récentes — ainsi que la marque et un code QR de l'App Store. Les couleurs correspondent à votre **thème de la page de l'onglet Statistiques**.

### Puis-je personnaliser le thème de l'onglet Statistiques ?

Oui. **Onglet Statistiques → engrenage → Thème** — mêmes contrôles de barre de titre et de dégradé de fond que Pomodoro, Minuteur d'étude et Tâches. La valeur par défaut est rouge focus (`#E53935` / `#EF9A9A`). La teinte de l'onglet Statistiques, la barre de navigation et les **cartes de partage des statistiques** suivent toutes ces couleurs de thème de la page.

### Comment fonctionnent les réalisations ?

Neuf badges locaux se débloquent à mesure que vous franchissez des étapes : premier pomodoro, séquences, total de pomodoros, heures de concentration, réalisation d'objectifs quotidiens, et plus encore. Lorsque vous déverrouillez un nouveau badge, une **célébration en plein écran** apparaît dans l'onglet Statistiques (appuyez sur **Continuer** pour ignorer). Ouvrez **Statistiques → Équipement → Réalisations** pour parcourir la grille. **Appuyez sur un badge** pour obtenir une fiche détaillée ; partagez la **liste complète** depuis la barre d'outils des réalisations ou un **badge unique** depuis l'écran de détail. Les badges sont stockés sur l'appareil ; avec la synchronisation iCloud activée, l'état de déverrouillage et de célébration fusionne sur vos appareils via CloudKit - non téléchargé sur nos serveurs. 

### Comment puis-je parcourir les mois passés sur la carte thermique de focus ? 

Sur le tableau de bord Statistiques, utilisez les flèches **Mois précédent/Mois suivant** sur la carte thermique, appuyez sur le **titre du mois** pour ouvrir une feuille **sélecteur d'année + mois**, ou appuyez sur **Ce mois** pour revenir au mois en cours. 

### Pourquoi les dates futures sur la carte thermique sont-elles différentes ? 

Les jours après aujourd'hui dans le mois en cours apparaissent sous la forme de **espaces réservés à contour en pointillés** avec un remplissage plus clair : ils ne sont pas comptés comme jours de concentration. Les jours passés et aujourd’hui utilisent les couleurs d’intensité normale. 

### Comment ajouter le widget Statistiques du jour ?

Appuyez longuement sur l'écran d'accueil → **+** → recherchez **iPomodoro** → ajoutez **Statistiques du jour** (Petit, **Moyen, Grand** ou Écran de verrouillage rectangulaire/en ligne). Il montre la concentration d'aujourd'hui, la progression des objectifs Pomodoro et **hebdomadaires** et la séquence. 

### Comment ajouter le widget de tâches ? 

Appuyez longuement sur l'écran d'accueil → **+** → recherchez **iPomodoro** → ajoutez **Tâches de compte à rebours** (Petite/Moyenne/Grande). Il affiche les tâches épinglées à venir et les jours restants. Ouvrez l'application après avoir modifié les tâches pour une actualisation plus rapide. 

### Puis-je actualiser le devis du widget de motivation ? 

Sur **iOS 17+**, appuyez sur le bouton **Actualiser** du widget Motivation quotidienne pour choisir instantanément une autre citation sans ouvrir l'application. 

### Pourquoi les notifications ne fonctionnent-elles pas ? 

Vérifiez **Onglet Paramètres → Notifications** pour connaître votre statut d'autorisation iOS actuel. Les rappels de minuterie et de tâches nécessitent un accès aux notifications. Ouvrez les paramètres système si l'autorisation a été refusée. 

### Comment personnaliser les durées de travail et de pause ? 

Appuyez sur l'**icône d'engrenage** sur l'onglet Pomodoro → ajustez les lignes pas à pas, ou **appuyez sur les grands chiffres de la minuterie** sur l'écran principal pour ouvrir un sélecteur de durée. Un intervalle de pause long (tous les N pomodoros) est également configurable. 

### Qu'est-ce que l'achèvement de la phase de confirmation ?

**Onglet Pomodoro → roue dentée → Confirmer la fin de la phase**. Lorsque **activé**, iPomodoro affiche une boîte de dialogue après chaque segment de travail ou de pause avant de commencer la phase suivante. Lorsque **désactivé** (par défaut), la phase suivante démarre automatiquement après l'alarme de fin — flux Pomodoro classique sans intervention.

### Comment fonctionnent Live Activity et Dynamic Island ?

Activez **Live Activity** séparément dans les paramètres de Pomodoro et de Study Timer (icône de roue dentée). Chaque mode possède son **propre** compte à rebours sur l’écran verrouillé et dans Dynamic Island — ils ne s’écrasent jamais mutuellement. Pendant qu’une session est en cours, vous voyez un compte à rebours en direct ; lorsqu’elle se termine, une brève célébration apparaît pendant 10 secondes. Si iOS ferme l’application alors que votre minuteur est encore visible sur l’écran verrouillé, la réouverture de iPomodoro **restaure** la session et passe à l’onglet actif — **sauf** si vous l’avez lancée via une **Action rapide de l’écran d’accueil**, qui prévaut.

### Comment ajouter des widgets ?

Appuyez longuement sur l’écran d’accueil → **+** → recherchez **iPomodoro** (ou 爱番茄 / 愛番茄). Choisissez **iPomodoro · Pomodoro** ou **iPomodoro · Study Timer** pour les comptes à rebours du minuteur (ce sont des widgets séparés), **Today's Stats** pour le suivi de votre concentration quotidienne, **Countdown Tasks** pour les échéances ou **Daily Motivational Quote** pour la citation quotidienne. Pour une aide étape par étape, ouvrez **Réglages → Widgets → Comment utiliser**.

### Pourquoi mon widget de minuteur ne se met-il pas à jour ?

Pomodoro et Study Timer sont des **widgets séparés**. Démarrez ou mettez en pause une session dans l’**onglet correspondant** et assurez-vous d’avoir ajouté le bon widget. iOS peut retarder les actualisations pour économiser la batterie — ouvrez l’application une fois pour synchroniser plus rapidement.

### Où est passé l’ancien widget de minuteur ?

Les minuteurs sont maintenant **iPomodoro · Pomodoro** et **iPomodoro · Study Timer**. Supprimez tout ancien widget de minuteur et ajoutez les nouveaux depuis la galerie de widgets.

### Comment fonctionne la citation motivationnelle quotidienne ?

Un devis est sélectionné de manière déterministe chaque jour à l'aide de `(year × 400 + dayOfYear) % total`. Filtrez la langue des citations sous **Paramètres → Paramètres des citations de motivation → Langues des citations de motivation** (Toutes / Simplifiées / Traditionnelles / Anglais). La même citation apparaît dans le widget Motivation et l'indice d'activité en direct jusqu'à minuit. Parcourez des citations aléatoires dans **Paramètres → Paramètres des citations de motivation → Anthologie des citations de motivation** (en plein écran, une à la fois). 

### Les arrière-plans des widgets peuvent-ils suivre mon thème ? 

Oui. **Paramètres → Widgets → L'arrière-plan du widget suit le thème** reflète votre dégradé d'accent global sur les widgets d'accueil et d'écran de verrouillage. Désactivez-le pour obtenir un arrière-plan blanc pur (clair) ou sombre tout en conservant les couleurs d'accent sur les titres. 

### Comment fonctionnent les rappels de tâches à échéance ? 

Lors de la création ou de la modification d'une tâche, activez **Rappel de date d'échéance** et définissez une date/heure cible future. Une notification locale se déclenche à ce moment précis. Gérez les rappels en attente sous **onglet Tâches → équipement → Rappels de tâches dues** — appuyez sur une ligne pour modifier ou **supprimer** la tâche du bas de la feuille de modification. Le glisser pour supprimer sur la liste des tâches fonctionne toujours également. 

### Comment supprimer une tâche en cours d'édition ?

Ouvrez une tâche dans la liste ou dans **Rappels de tâches dues**, puis faites défiler vers le bas de la feuille de modification et appuyez sur **Supprimer**. Confirmez dans l'alerte. Les nouvelles tâches (créer un flux) n'affichent pas de bouton de suppression. 

### Pourquoi ne puis-je pas activer un rappel pour une date passée ? 

Si la date/heure cible est déjà passée, la bascule de rappel est masquée et tout rappel existant est automatiquement désactivé — il n'y a plus rien d'important à planifier. 

### Puis-je utiliser une langue différente de celle de mon système ? 

Oui. Accédez à **onglet Paramètres → Langue** et choisissez Anglais, Chinois simplifié ou Chinois traditionnel. Le nom de l'application sur votre écran d'accueil suit la langue du système ; L'interface utilisateur intégrée à l'application suit votre choix dans l'application. 

### L'application collecte-t-elle mes données ? 

Pas d'analyse, pas de suivi. Les minuteries et les statistiques d'étude restent sur votre appareil par défaut. Les tâches et les sessions d'étude se synchronisent sur **votre iCloud** uniquement si vous activez les bascules séparées. Nous ne recevons pas vos données de tâches ou de minuterie sur nos serveurs. Consultez notre [Politique de confidentialité](../privacy) pour plus de détails. 

### macOS sera-t-il pris en charge ? 

Le support de macOS est prévu. Le projet Xcode inclut déjà la configuration du SDK macOS ; restez à l'écoute des mises à jour sur l'App Store. 

### Vous avez encore besoin d'aide ?

Contactez-nous à [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com). Nous répondons généralement dans les 48 heures.

&lt;/section&gt;

</section>
<section lang="tr" markdown="1">

### Neden diğer Pomodoro uygulamaları yerine iPomodoro'yu seçmeliyim?

iPomodoro, Apple platformları için geliştirilmiş **yerel SwiftUI** bir uygulamadır — sarmalanmış bir web zamanlayıcı değil. **Beş entegre sekme** (Pomodoro, Çalışma Zamanlayıcısı, Görevler, İstatistikler, Ayarlar), **çift Canlı Aktiviteler**, **beş widget ailesi**, **9 başarı rozeti**, **1000+ cihaz içi alıntı**, **Siri ve URL kısayolları** ve **isteğe bağlı iCloud senkronizasyonu** elde edersiniz — hem de **sıfır analiz** ve **hesap gerekmeksizin**. Tek bir sakin uygulama ile odaklanma, son tarih ve ilerleme takibini baştan sona kapsar.

### Zamanlayıcı ve görev ayarları nerede?

Zamanlayıcı süreleri, sesler, Canlı Aktivite, sayfa tema renkleri, isteğe bağlı **Odak Modu hatırlatıcısı** ve (yalnızca Pomodoro için) isteğe bağlı **Aşama tamamlamayı onayla**, her sekmenin **dişli simgesi** altında bulunur (Pomodoro, Çalışma Zamanlayıcısı, Görevler veya **İstatistikler**). Genel **Ayarlar** sekmesi; görünüm, dil, **Ana Ekran kısayolları**, **Uygulama Rehberi**, bildirim izni, motivasyonel alıntılar (günlük motivasyon bildirimi dahil), widget rehberi, geri bildirim ve hakkında bölümünü içerir — mod başına süreleri içermez. **İstatistikler** ayarları (sayfa teması, hedefler, isteğe bağlı iCloud senkronizasyonu, başarılar, sayım kuralları, CSV, saklama) **İstatistikler sekmesi → dişli** altında bulunur.

### Ana Ekran kısayolları ve Siri nasıl çalışır?

Hızlı İşlemler için **uygulama simgesine uzun basın**; Pomodoro'yu, Çalışma Zamanlayıcısını, Görevleri, İstatistikleri, motivasyon teklifini veya geri bildirimi açın. **Ayarlar → Uygulama ayarları → Ana Ekran kısayolları** altında hangi dördünün görüneceğini özelleştirin (yeniden sıralamak için sürükleyin). Aynı hedefleri **`iPomodoro://`_** URL'ler aracılığıyla da açabilirsiniz (`pomodoro`, `study`, `tasks`, `stats`, `motivation`, `feedback`; `iPomodoros://` de çalışır). [URL Şeması Referansı](../url-şeması)'nın tamamına bakın. **Siri / Kısayollar uygulaması** yerleşik Uygulama Kısayolları aracılığıyla sekmeleri açabilir veya *"Bugün iPomodoro'da ne kadar süre odaklandım?"* yanıtını verebilir. 

### Uygulama içi Uygulama Kılavuzu nedir? 

**Ayarlar → Uygulama ayarları → Uygulama Kılavuzu** — beş sekmenin, widget'ların, kısayolların, iCloud'un ve SSS'nin tamamını kapsayan daraltılabilir bir eğitim (Widget kılavuzuna benzer stil). 

### iPomodoro benim için Odak Modu'nu açabilir mi? 

Hayır — iOS, üçüncü taraf uygulamaların Focus'u doğrudan etkinleştirmesine izin vermez. İsteğe bağlı **Odak Modu hatırlatıcısı** (Pomodoro veya Çalışma Zamanlayıcısı dişli ayarları), bir zamanlayıcıyı başlattığınızda Odak'ın kapalı olup olmadığını kontrol eder ve bir uyarı gösterir; uyarıdan **Ayarlar**'ı açabilirsiniz ancak Odak'ı kendiniz açmanız gerekir. 

### Her geri sayım görevi için bir renk seçebilir miyim?

Evet. Bir görev eklerken veya düzenlerken, **9 vurgu renginden** birini seçin. Liste ve **Geri Sayım Görevleri** widget'ı bu rengi her satır için kullanır. Görev senkronizasyonu etkinleştirildiğinde renkler iCloud üzerinden senkronize edilir.

### İstatistikleri özel bir tarih aralığına göre filtreleyebilir miyim?

Evet. İstatistikler sekmesinde (veya dönem raporunda), dönem çubuğunda **Özel**i seçin, ardından başlangıç ve bitiş tarihlerini ayarlayın. Aralık, İstatistikler ayarlarında **Filtreyi hatırla** açık olduğunda kaydedilir.

### Günlük motivasyon bildirimi alabilir miyim?

Evet. **Ayarlar → Motivasyonel Alıntı Ayarları**, isteğe bağlı bir **günlük motivasyon bildirimi** içerir — bir zaman seçin ve iPomodoro, cihazdaki bildirim alıntı havuzundan rastgele bir satır ile tekrarlayan bir **yerel bildirim** planlar (ağ bağlantısı yok). Zamanlayıcı bitiş uyarılarından ayrıdır.

### Günlük alıntılar ile bildirim alıntıları arasındaki fark nedir?

**Diyalog/günlük alıntılar** (**Tüm filtreleme olduğunda 1000+ toplam — basitleştirilmiş Çince + İngilizce) uygulama başlatma açılır penceresini, ayarlar tarayıcısını, Canlı Aktivite ipucunu ve Motivasyon widget'ını besler. **Bildirim alıntıları** ayrı bir cihaz içi havuzdur (**her dil için 365 genel satır**) ve yalnızca arka plan zamanlayıcı tamamlanma uyarıları için kullanılır. Her ikisi de Ayarlar'daki alıntı dili filtrenize saygı gösterir.

### Pomodoro Tekniği Nedir?

Pomodoro Tekniği bir zaman yönetimi yöntemidir: odaklanmış aralıklarla çalışın (klasik olarak 25 dakika), ardından kısa bir mola verin. Birkaç döngüden sonra daha uzun bir mola verin. iPomodoro bu ritmi otomatikleştirir, böylece saate değil işe odaklanabilirsiniz.

### iPomodoro eski Flutter versiyonundan nasıl farklıdır?

Bu, Apple platformları için **tam bir SwiftUI yeniden yazımıdır**. Aynı temel fikirler — Pomodoro, çalışma zamanlayıcısı, geri sayım görevleri — ama yerel performans, Canlı Aktivite, modern widget'lar ve daha sıkı iOS entegrasyonu vardır.

### Bir hesaba veya internet bağlantısına ihtiyacım var mı?

iPomodoro hesabı gerekmez. Zamanlayıcılar, çalışma istatistikleri, temalar ve widget'lar cihazınızda **tamamen çevrimdışı** çalışır. **İsteğe bağlı:** Verileri aynı Apple kimliğiyle oturum açan cihazlar arasında birleştirmek için **Görevleri iCloud ile senkronize et** (Görevler → dişli) ve/veya **Çalışma istatistiklerini iCloud ile senkronize et** (İstatistikler → dişli) özelliğini etkinleştirin; bu, sunucularımızı değil, Apple CloudKit'i kullanır. İnternet aynı zamanda App Store güncellemeleri veya geri bildirim e-postaları için de kullanılır. 

### Çalışma İstatistikleri nasıl çalışır? 

**İstatistikler** sekmesini açın. Tümü / Pomodoro / Çalışma Zamanlayıcısı ve Bugün / Hafta / Ay / Yıl / Tüm zamanlar / **Özel tarih aralığı**'na göre filtreleyin. Kontrol panelinde **bugünün özeti**, **hedef ilerlemesi**, haftadan haftaya karşılaştırma, **aylık ısı haritası**, **başarılar**, hafta içi/günün saati grafikleri ve **bağlantılı göreve göre döküm** gösterilir. Hedefler, isteğe bağlı **iCloud senkronizasyonu**, sayma kuralları, **CSV dışa aktarma/içe aktarma** ve veri saklama için **dişli simgesine** dokunun. İstatistikler **asla sunucularımıza yüklenmez** (isteğe bağlı iCloud, Apple Kimliğiniz altında Apple CloudKit'i kullanır). 

### Çalışma istatistiklerini dışa veya içe aktarabilir miyim?

Evet. **İstatistikler sekmesi → dişli → Dışa aktar**, sistem paylaşım sayfası aracılığıyla bir CSV dosyasını paylaşır. **İçe aktar** aynı biçimi kabul eder (`kind,started_at,ended_at,duration_seconds,outcome` artı isteğe bağlı `task_id,task_title,cloud_id`) — **birleştir** (kopyaları atla) veya **tümünü değiştir** seçeneğini seçin. Yedekleme veya manuel geçiş için kullanışlıdır. Otomatik cihazlar arası senkronizasyon için bunun yerine **Çalışma istatistiklerini iCloud ile senkronize et** seçeneğini etkinleştirin. 

### İstatistiklerimi resim olarak paylaşabilir miyim? 

Evet. iPomodoro, **İstatistik kontrol paneli** (araç çubuğu paylaşımı), **dönem raporları**, **inceleme yılı** özetleri ve **başarılar** (tam liste veya tek rozet) için **markalı anlık görüntü kartları** (odak ölçümleri + App Store QR kodu) oluşturabilir. İstatistik paylaşım kartları **İstatistikler sekmesi sayfa temanızı** renklerinizi kullanır. Ayrıca Ayarlar → Uygulamayı Paylaş bölümünden de **uygulama tanıtım kartını** paylaşabilirsiniz. 

### Çalışma istatistiklerini iCloud ile senkronize edebilir miyim? 

Evet — **İstatistikler sekmesi → dişli → Çalışma istatistiklerini iCloud ile senkronize edin**. Bu, görev iCloud senkronizasyonundan **ayrıdır**. Oturumlar, CloudKit kayıt türü `StudySession` aracılığıyla Apple ID cihazlarınızda `cloudId` kadar birleştirilir. **Günlük hedef ayarları** (`StatsGoals`) ve **başarı kilidini açma/kutlama durumu** (`StatsAchievements`) etkinleştirildiğinde aynı geçiş altında senkronize edilir.

### Günlük odaklanma hedefleri nasıl çalışır? 

**İstatistikler → donanım → Hedefler**: günlük pomodoro sayısını, günlük odaklanma dakikalarını ve haftalık odaklanma dakikalarını ayarlayın. İlerleme durumu, etkinleştirildiğinde İstatistik kontrol panelinde ve **Günün İstatistikleri** widget'ında görünür. 

### Geri sayım görevini odaklanma oturumuna nasıl bağlarım? 

Pomodoro veya Çalışma Zamanlayıcısı ekranında **Görevi bağla**'ya dokunun ve bir görev seçin. Veya **Görevler**'den bir göreve uzun basın → **Pomodoro ile Odaklan** veya **Çalışma Zamanlayıcısı ile Odaklan**. Tamamlanan oturumlar, İstatistikler'de **göreve göre döküm** için görev başlığını saklar. 

### Görevleri nasıl sabitleyebilirim veya yeniden sıralayabilirim? 

**Görevler** sekmesinde, **Sabitlemek** için bir satırı kaydırın veya gezinme çubuğundaki sıralama menüsünü kullanın. Görevleri **sürüklemek** için yeniden sıralama moduna girin; anahtarları otomatik olarak özel sıraya göre sıralayın. Sabitlenen görevler üst kısımda kendi bölümünde görünür. 

### iCloud görev senkronizasyonu nasıl çalışır? 

Görevler sekmesi → dişli → **Görevleri iCloud ile senkronize et** seçeneğini açın. Görevler, Apple Kimliği aygıtlarınızda son değiştirilme zamanına göre birleştirilir. Pomodoro / çalışma zamanlayıcıları yerel kalır. **Çalışma istatistikleri** isteğe bağlı olarak ayrı olarak senkronize edilebilir (İstatistikler → dişli). İOS Ayarlarında iCloud'da oturum açmış olmanız gerekir. Senkronizasyon, uygulamaya döndüğünüzde de çalışır.

### İstatistikler panosu paylaşım görselinde neler bulunur?

İstatistikler sekmesi araç çubuğunda **Paylaş**a dokunun. Uzun kart, **geçerli kapsam ve dönem** filtrelerinizi yansıtır — bugünün kahramanı, hedef ilerlemesi, ısı haritası, hafta içi/saat grafikleri, görev dağılımı, trend çubukları ve son oturumlar — ayrıca marka ve bir App Store QR kodu içerir. Renkler, **İstatistikler sekmesi sayfa temasıyla** eşleşir.

### İstatistikler sekmesi temasını özelleştirebilir miyim?

Evet. **İstatistikler sekmesi → ayar simgesi → Tema** — Pomodoro, Çalışma Zamanlayıcısı ve Görevlerdeki ile aynı başlık çubuğu ve arka plan gradyan kontrolleri. Varsayılan tema odak kırmızısıdır (`#E53935` / `#EF9A9A`). İstatistikler sekmesi rengi, gezinme çubuğu ve **istatistik paylaşım kartları** bu sayfa teması renklerini takip eder.

### Başarılar nasıl çalışır?

Dokuz yerel rozet, kilometre taşlarına ulaştığınızda açılır: ilk pomodoro, seriler, toplam pomodorolar, odaklanma saatleri, günlük hedef tamamlama ve daha fazlası. Yeni bir rozetin kilidini açtığınızda, İstatistikler sekmesinde **tam ekran kutlama** görünür (kapatmak için **Devam**'a dokunun). Tabloya göz atmak için **İstatistikler → dişli → Başarılar**'ı açın. Ayrıntı sayfası için **bir rozete dokunun**; Başarılar araç çubuğundan **tam listeyi** veya ayrıntılar ekranından **tek bir rozeti** paylaşın. Rozetler cihazda saklanır; iCloud senkronizasyonu etkinken, kilidi açma ve kutlama durumu CloudKit aracılığıyla cihazlarınız arasında birleştirilir; sunucularımıza yüklenmez. 

### Odak ısı haritasında geçmiş aylara nasıl göz atabilirim? 

İstatistik panosunda, ısı haritası kartındaki **Önceki / Gelecek ay** oklarını kullanın, **yıl + ay seçici** sayfasını açmak için **ay başlığına** dokunun veya geçerli aya geri dönmek için **Bu ay**'a dokunun. 

### Isı haritasındaki gelecek tarihler neden farklı görünüyor? 

Geçerli ayda bugünden sonraki günler, daha açık dolgulu **kesik çizgili yer tutucular** olarak görünür; bunlar odak günleri olarak sayılmaz. Geçmiş günler ve bugün normal yoğunluktaki renkleri kullanıyorlar. 

### Bugünün İstatistikleri widget'ını nasıl eklerim?

Ana Ekrana uzun basın → **+** → **iPomodoro**'yu arayın → **Bugünün İstatistikleri** ekleyin (Küçük, **Orta, Büyük** veya Kilit Ekranı dikdörtgen / satır içi). Bugünün odağını, pomodoroyu ve **haftalık** hedef ilerlemesini ve galibiyet serisini gösterir. 

### Görevler widget'ını nasıl eklerim? 

Ana Ekrana uzun basın → **+** → **iPomodoro**'yu arayın → **Geri Sayım Görevleri** (Küçük / Orta / Büyük) ekleyin. Yaklaşan sabitlenmiş görevleri ve kalan günleri gösterir. En hızlı yenileme için görevleri düzenledikten sonra uygulamayı açın. 

### Motivasyon widget'ının teklifini yenileyebilir miyim? 

**iOS 17+**'de, uygulamayı açmadan anında başka bir alıntı seçmek için Günlük Motivasyon widget'ındaki **yenile** düğmesine dokunun. 

### Bildirimler neden çalışmıyor? 

Mevcut iOS izin durumunuz için **Ayarlar sekmesi → Bildirimler**'i kontrol edin. Zamanlayıcı ve görev hatırlatıcıları bildirim erişimi gerektirir. İzin reddedilirse Sistem Ayarlarını açın. 

### Çalışma ve mola sürelerini nasıl özelleştirebilirim? 

Bir süre seçiciyi açmak için Pomodoro sekmesindeki **dişli simgesine** dokunun → adım satırlarını ayarlayın veya ana ekranda **büyük zamanlayıcı rakamlarına dokunun**. Uzun mola aralığı (her N pomodoro) da yapılandırılabilir. 

### Aşamanın tamamlandığını onaylama nedir?

**Pomodoro sekmesi → ayarlar → Faz tamamlamayı onayla**. **Açık** olduğunda, iPomodoro bir sonraki faz başlamadan önce her iş veya mola segmentinden sonra bir iletişim kutusu gösterir. **Kapalı** olduğunda (varsayılan), bir sonraki faz tamamlanma alarmından sonra otomatik olarak başlar — klasik eller serbest Pomodoro akışı.

### Canlı Aktivite ve Dinamik Ada nasıl çalışır?

**Canlı Aktivite**yi Pomodoro ve Çalışma Zamanlayıcı ayarlarında (dişli simgesi) ayrı ayrı açın. Her mod kendi **kilit ekranı** ve Dinamik Ada geri sayımına sahiptir — birbirlerini asla geçersiz kılmazlar. Bir oturum çalışırken canlı bir geri sayım görürsünüz; oturum tamamlandığında kısa bir kutlama 10 saniye gösterilir. iOS, zamanlayıcınız hâlâ Kilit Ekranda görünürken uygulamayı kapatırsa, iPomodoro'yu tekrar açmak oturumu **geri yükler** ve aktif sekmeye gider — **ancak**, uygulamayı bir **Ana Ekran Hızlı İşlemi** üzerinden başlattıysanız, bu önceliklidir.

### Widget'ları nasıl eklerim?

Ana Ekrana uzun basın → **+** → **iPomodoro** (veya 爱番茄 / 愛番茄) arayın. Sayaç geri sayımları için **iPomodoro · Pomodoro** veya **iPomodoro · Study Timer**i seçin (bunlar ayrı widgetlardır), günlük odak ilerlemesi için **Today's Stats**, son tarihler için **Countdown Tasks** veya günlük alıntı için **Daily Motivational Quote**. Adım adım yardım için **Ayarlar → Widgetlar → Nasıl Kullanılır**ı açın.

### Neden zamanlayıcı widget'ım güncellenmiyor?

Pomodoro ve Study Timer **ayrı widgetlardır**. Bir oturumu başlatın veya duraklatın **uygun sekmede** ve doğru widget'ı eklediğinizden emin olun. iOS pil tasarrufu için güncellemeleri geciktirebilir — daha hızlı senkronizasyon için uygulamayı bir kez açın.

### Eski zamanlayıcı widget nerede?

Zamanlayıcılar artık **iPomodoro · Pomodoro** ve **iPomodoro · Study Timer**. Eski zamanlayıcı widget'ları kaldırın ve yeni olanları widget galerisinden ekleyin.

### Günlük motivasyon alıntısı nasıl çalışır?

`(year × 400 + dayOfYear) % total` kullanılarak her gün deterministik olarak bir teklif seçilir. **Ayarlar → Motivasyonel Alıntı Ayarları → Motivasyonel Alıntı Dilleri** (Tümü / Basitleştirilmiş / Geleneksel / İngilizce) altında alıntı dilini filtreleyin. Aynı alıntı Motivasyon widget'ında ve Canlı Etkinlik ipucunda gece yarısına kadar görünür. **Ayarlar → Motivasyonel Alıntı Ayarları → Motivasyonel Alıntı Antolojisinde** (tam ekran, birer birer) rastgele alıntılara göz atın. 

### Widget arka planları temamı takip edebilir mi? 

Evet. **Ayarlar → Widget'lar → Widget arka planı temayı takip eder**, Ana Ekran ve Kilit Ekranı widget'larındaki genel vurgu degradenizi yansıtır. Başlıklarda vurgu renklerini korurken temiz beyaz (açık) veya sistem koyu arka planı için bu özelliği kapatın. 

### Görev zamanı hatırlatıcıları nasıl çalışır? 

Bir görevi oluştururken veya düzenlerken **Son tarih hatırlatıcısını** etkinleştirin ve gelecekteki bir hedef tarih/saati ayarlayın. Tam o anda yerel bir bildirim tetikleniyor. **Görevler sekmesi → dişli → Görev zamanı hatırlatıcıları** altında bekleyen hatırlatıcıları yönetin — görevi düzenlemek için bir satıra dokunun veya düzenleme sayfasının alt kısmından **silin**. Görev listesindeki silmek için hızlıca kaydırma özelliği de hâlâ çalışıyor. 

### Düzenleme sırasında bir görevi nasıl silerim?

Listeden veya **Görev zamanı hatırlatıcılarından** bir görevi açın, ardından düzenleme sayfasının en altına gidin ve **Sil**'e dokunun. Uyarıyı onaylayın. Yeni görevler (akış oluşturma) silme düğmesi göstermez. 

### Neden geçmiş bir tarih için hatırlatıcıyı etkinleştiremiyorum? 

Hedef tarihsaat zaten geçmişse, hatırlatıcı geçişi gizlenir ve mevcut hatırlatıcılar otomatik olarak devre dışı bırakılır; planlanacak anlamlı bir şey kalmaz. 

### Sistemimden farklı bir dil kullanabilir miyim? 

Evet. **Ayarlar sekmesi → Dil**'e gidin ve İngilizce, Basitleştirilmiş Çince veya Geleneksel Çince'yi seçin. Ana Ekranınızdaki uygulama adı sistem dilini takip eder; uygulama içi kullanıcı arayüzü, uygulama içi seçiminizi takip eder. 

### Uygulama verilerimi topluyor mu? 

Analitik yok, izleme yok. Zamanlayıcılar ve çalışma istatistikleri varsayılan olarak cihazınızda kalır. Görevler ve çalışma oturumları yalnızca ayrı geçiş düğmelerini etkinleştirdiğinizde **iCloud'unuzla** senkronize edilir. Görevinizi veya zamanlayıcı verilerinizi sunucularımıza almıyoruz. Tüm ayrıntılar için [Gizlilik Politikamıza](../privacy) bakın. 

### MacOS desteklenecek mi? 

macOS desteği planlanıyor. Xcode projesi zaten macOS SDK yapılandırmasını içeriyor; App Store'daki güncellemeler için bizi takip etmeye devam edin. 

### Hala yardıma mı ihtiyacınız var?

Bize ulaşın [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com). Genellikle 48 saat içinde cevap veririz.

&lt;/section&gt;

</section>
