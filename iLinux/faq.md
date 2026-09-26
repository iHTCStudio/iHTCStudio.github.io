---
layout: doc
title: iLinux — FAQ
app_id: iLinux
doc_title_en: Frequently Asked Questions
doc_title_zh_cn: 常见问题
doc_title_zh_tw: 常見問題
description: Frequently asked questions about iLinux — Linux, CMD, PowerShell, macOS, iCloud sync, equivalents, quiz and widgets.
---

<section lang="en" markdown="1">

### Does iLinux require an account or internet connection?

No. iLinux works entirely offline for command libraries. All command data (JSON summaries and Markdown documentation) is bundled inside the app. No sign-up is needed to browse, read documentation or take quizzes. Optional **iCloud sync** uses your Apple ID to align favourites and progress across devices — it does not upload command content.

### Does iLinux support Mac?

Yes. iLinux is a **native macOS app** (macOS **13.0+**, not Mac Catalyst) with a **sidebar desktop layout**, resizable window, and extended keyboard shortcuts (**⌘,**, **⌘[**, **Esc**, **⌘←/→**, quiz keys **1–4** / **⌘R** / **Return**). All core features — three shell libraries, equivalents, quiz, deep links and themes — work on Mac.

**Not on Mac:** Home Screen widgets, Home Screen quick actions and alternate app icons are **iPhone/iPad only**. Configure widgets on iOS; Mac shows an in-app notice.

### How does iCloud sync work?

When signed into **iCloud** with the same Apple ID, enable **iCloud Sync** in **Settings → Learning stats**. iLinux syncs **favourites**, **quiz progress**, **theme**, and **display preferences** (language, shell platform, favourites scope, list/grid) across **iPhone, iPad and Mac** via iCloud Key-Value Storage. Conflicts merge automatically (e.g. favourites union). You can **disable sync on one device** without affecting others. Command libraries remain fully offline; only your personal progress syncs.

### Does iLinux run commands on a real Linux terminal?

No. iLinux is a **reference and learning tool only**. It does not provide a shell, SSH client or remote execution environment. Commands are documented for study — you practise them on your own Linux machine, Windows PC, server or cloud instance.

### Which shell platforms does iLinux support?

iLinux ships three offline command libraries per content language:

- **Linux** — 1050 commands in 14 categories
- **Windows CMD / Batch** — 300 commands in 10 categories
- **PowerShell** — 300 commands in 10 categories

**1650+ commands total** per language (English, Simplified Chinese, Traditional Chinese). Switch libraries from the toolbar Shell menu on **Commands**, **Categories** or **Daily Quiz**.

### How do I switch between Linux, CMD and PowerShell?

Tap the **Shell platform** menu (terminal icon) in the toolbar on the Commands, Categories or Daily Quiz tab. Your selection persists and scopes search, categories, quiz questions and learning stats for that platform.

In **Settings → Home quick access**, you can also set a default shell platform, **favourites scope** (all platforms vs current platform only), and the **widget command library** for Daily Command and Category Spotlight widgets.

### What are cross-platform equivalent commands?

**100+ equivalent groups** link commands that accomplish the same task across Linux, CMD and PowerShell — for example `ls`, `dir` and `Get-ChildItem`. On a command detail page, the **Equivalents** bar shows related entries; tap one to jump to that platform's documentation instantly.

### How many commands are included?

Each content language includes **1650+** commands across three shell libraries:

| Platform | Commands | Categories |
|----------|----------|------------|
| Linux | 1050 | 14 |
| CMD / Batch | 300 | 10 |
| PowerShell | 300 | 10 |

All documentation is available offline in English, Simplified Chinese and Traditional Chinese.

### How do I search for a command?

Tap the magnifier icon on the Commands tab, or press **⌘F** on a hardware keyboard. Type a command name, keyword or part of a description. Results update in real time as you type.

### How do I switch between list and grid view?

On the **Commands** or **Categories** tab, open the toolbar filter menu (funnel icon). Under **View Mode**, choose **List** or **Grid**. In grid mode, use the **+ / −** buttons to set columns per row (**1–6 on iPhone**, **1–8 on iPad and Mac**). You can also change the default in **Settings → Display**.

### How do I track my learning progress?

Open a command's detail page and set its status to **Unlearned**, **Learned** or **Mastered**. In list view, swipe a row for quick status and favourite actions. In grid view, use the star button to favourite and the context menu for status. Filter to **Unlearned** from the toolbar menu to focus on commands you haven't studied yet.

### What languages are available?

iLinux supports three languages for both the app interface and the command documentation:

- **English**
- **Simplified Chinese (简体中文)**
- **Traditional Chinese (繁體中文)**

You can also choose **System** to follow your device's locale. Change the language in **Settings → Language**. The entire app — including widgets — updates immediately.

### How does the Daily Quiz work?

Each day a new set of quiz questions is generated using a date-based seed, **scoped to the active shell platform** (Linux, CMD or PowerShell). Everyone using iLinux on the same day gets the same base quiz set for that platform. Two question types appear:

- **Match Summary** — you see a short description and must choose the correct command name.
- **Match Option Meaning** — you see a flag's description (e.g. `-r: recursive`) and must identify which command it belongs to.

Tap the **refresh button** (circular arrow) in the toolbar to get a different randomised set at any time. **Perfect streak** days (consecutive days with a perfect score) are tracked per platform and shown in the quiz screen and Quiz Glance widget. Generic help flags like `-h` and `--version` are excluded to keep questions unambiguous.

### My wrong answers aren't being saved. What should I do?

Wrong answers are saved automatically after you complete a quiz session. Make sure you finish the full quiz round (answer all questions and reach the result screen). Partially completed sessions are not saved.

You can review all saved wrong answers in **Settings → Wrong Answer Book**.

### How do I add a command to Favourites?

Open any command's detail page and tap the **star icon** in the top-right corner. In **grid view**, tap the star on the command cell directly. Access all favourites from **Settings → Favourites** or the **Favourites** quick filter.

### How do I set up Home Screen Widgets?

1. Long-press an empty area of your Home Screen and tap the **+** button in the top corner.
2. Search for **iLinux** in the widget gallery.
3. Choose a widget style and tap **Add Widget**.

A step-by-step **Widget Guide** is also available in **Settings → Widget Guide**. To make widget backgrounds follow your app theme gradient, enable the option in **Settings → Widgets**.

**Widget command library:** In **Settings → Widgets**, choose which shell library (Linux / CMD / PowerShell) feeds the Daily Command and Category Spotlight widgets. This is independent of the in-app shell switch — useful if you want widgets to show Windows commands while browsing Linux inside the app.

### The Daily Command widget shows the same command every day. How do I change it?

Tap the **circular arrow (shuffle) button** in the top-right corner of the Daily Command widget to immediately load a different command. This feature requires **iOS 17 or later**.

On iOS 16, the Daily Command widget displays a fixed command for each day and does not include the shuffle button.

### How do I configure Home Screen Quick Actions?

Long-press the iLinux app icon to see up to **4** quick actions. Choose which actions appear in **Settings → Home Screen Shortcuts**. Seven options are available: **Search**, **Daily Quiz**, **Favourites**, **Wrong Answer Book**, **Categories**, **Send Feedback** and **Rate App**. You can reorder and reset to defaults from the same screen.

### How do I use iLinux with the Shortcuts app?

iLinux supports the `ilinux://` URL scheme. Use an **Open URLs** action in the Shortcuts app. Examples:

- `ilinux://command?name=grep` — opens Linux command `grep` (`cmd=` works too)
- `ilinux://command?cmd=dir&platform=cmd` — opens CMD command `dir`
- `ilinux://command?cmd=Get-ChildItem&platform=powershell` — opens PowerShell command
- `ilinux://quiz` — opens the Daily Quiz tab
- `ilinux://favorites` — opens your Favourites list
- `ilinux://wrong` or `ilinux://mistakes` — opens the Wrong Answer Book

**Platform parameter:** `platform=linux` (default), `cmd` (aliases: `batch`, `bat`), or `powershell` (aliases: `ps`, `pwsh`). Omit for Linux commands.

Note: **Search** and **Categories** are available as Home Screen quick actions but are not registered as universal deep-link hosts. See the full [URL Scheme Reference](url-scheme).

### How do I share a command?

On any command detail page, tap **Share** in the toolbar. You can export the command as a **Markdown file** or generate a **styled PNG share card** (with App Store QR code) to send through the system Share Sheet. Saving images to Photos may request photo library access.

### How do I change the theme colour?

Go to **Settings → Theme**. Scroll through 15 built-in colour presets or tap the **Custom Colour** row to pick any colour using the system colour picker. The accent colour, gradients and widget mirror all update immediately.

### Can I change the app icon?

Yes. Go to **Settings → App Icon** to choose from **6 icons** (default plus 5 alternates). The setting is applied instantly without relaunching the app.

### The widget colour doesn't match my theme. How do I fix it?

Widgets sync their theme colour via an App Group shared between the main app and the widget extension. If the widget looks out of date:

1. Open iLinux once — this forces the App Group data to refresh.
2. If the widget still doesn't update, long-press the widget and tap **Edit Widget** (or remove and re-add it) to trigger a timeline reload.

Make sure the **iLinux Widget** extension and the main app are both up to date (same version).

### Does iLinux support iPad?

Yes. iLinux runs natively on iPad with adaptive layouts. Grid mode supports up to **8 columns**. Widgets, alternate icons, Home Screen shortcuts and haptics are fully supported on iPad.

### How do I change the language on Mac?

The in-app **language picker** is in **Settings → Language** on **iPhone and iPad**. On **Mac**, language preference typically arrives via **iCloud sync** from another device, or follows your stored preference / system locale on first launch. Enable iCloud sync to keep language aligned across devices.

### Still need help?

Contact us at [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) or use the in-app **Settings → Send Feedback** option. We typically respond within 48 hours.

</section>

<section lang="zh-CN" markdown="1">

### 爱 Linux 需要账号或联网吗？

不需要。命令库完全离线打包在应用内。浏览、阅读文档或做测验无需注册。可选 **iCloud 同步**通过 Apple ID 在设备间对齐收藏与进度，不会上传命令内容。

### 爱 Linux 支持 Mac 吗？

支持。爱 Linux 是 **原生 macOS 应用**（**macOS 13.0+**，非 Mac Catalyst），采用**侧边栏桌面布局**、可调整窗口大小，并提供扩展快捷键（**⌘,**、**⌘[**、**Esc**、**⌘←/→**，测验 **1–4** / **⌘R** / **Return**）。三大 Shell 库、等效命令、测验、深度链接与主题在 Mac 上均可用。

**Mac 不含：** 主屏小组件、主屏快捷方式、备用图标（请在 iPhone/iPad 上配置小组件）。

### iCloud 同步如何工作？

登录同一 **Apple ID** 的 iCloud 后，在 **设置 → 学习统计** 开启 **iCloud 同步**。通过 iCloud 键值存储，**收藏、测验进度、主题、显示偏好**（语言、Shell 平台、收藏范围、列表/网格）在 **iPhone、iPad、Mac** 间同步，冲突自动合并。可单设备关闭。命令库仍完全离线。

### 爱 Linux 能在真实 Linux 终端里执行命令吗？

不能。爱 Linux **仅为参考与学习工具**，不提供 Shell、SSH 或远程执行环境。命令文档供你学习记忆——实际练习请在你自己的 Linux 机器、Windows PC、服务器或云实例上进行。

### 爱 Linux 支持哪些 Shell 平台？

每种内容语言内置三套离线命令库：

- **Linux** — 1050 条，14 个分类
- **Windows CMD / Batch** — 300 条，10 个分类
- **PowerShell** — 300 条，10 个分类

合计 **1650+** 条（英文 / 简体中文 / 繁体中文）。在**命令**、**分类**或**每日测验**页的工具栏 Shell 菜单中切换。

### 如何在 Linux、CMD 与 PowerShell 之间切换？

在**命令**、**分类**或**每日测验**页，点工具栏 **Shell 平台**菜单（终端图标）。选择会持久保存，并作用于搜索、分类、测验与学习统计。

**设置 → 首页快捷** 中还可设置默认 Shell 平台、**收藏范围**（全部平台 / 仅当前平台）以及**小组件命令库**。

### 什么是跨平台等效命令？

**100+ 组等效对照** 关联 Linux、CMD 与 PowerShell 中完成同类任务的命令——例如 `ls`、`dir`、`Get-ChildItem`。命令详情页顶部的**等效命令**栏可一键跳转到其它平台文档。

### 包含多少条命令？

每种内容语言 **1650+** 条，分属三大库：

| 平台 | 命令数 | 分类数 |
|------|--------|--------|
| Linux | 1050 | 14 |
| CMD / Batch | 300 | 10 |
| PowerShell | 300 | 10 |

英文、简体中文、繁体中文文档均可离线阅读。

### 如何搜索命令？

在「命令」标签点放大镜，或按 **⌘F**。输入命令名、关键词或描述片段，结果实时更新。

### 如何在列表与网格之间切换？

在**命令**或**分类**页，打开工具栏筛选菜单（漏斗图标），在**视图模式**下选择**列表**或**网格**。网格模式下用 **+ / −** 调整每行列数（**iPhone 1–6**、**iPad / Mac 1–8**）。也可在**设置 → 显示**中修改默认样式。

### 如何记录学习进度？

在命令详情页将状态设为**未学**、**已学**或**熟练**。列表模式下右滑行可快速改状态或收藏；网格模式下点星标收藏，长按菜单改状态。工具栏筛选选**未学**可集中复习尚未掌握的命令。

### 提供哪些语言？

界面与命令文档均支持英文、简体中文、繁体中文；也可选**系统**跟随设备。在 **设置 → 语言** 切换，含小组件在内的整个应用立即更新。

### 每日测验如何运作？

每天基于日期种子生成题集，**按当前 Shell 平台**（Linux / CMD / PowerShell）独立出题。两种题型：**匹配简介**、**匹配选项含义**。点工具栏**刷新按钮**可随时换题。**满分连胜**按平台统计。`-h`、`--version` 等通用帮助参数会从题目中排除。

### 错题没有保存怎么办？

需完整完成一轮测验（答完所有题并到达结果页）后才会保存错题。可在 **设置 → 错题本** 查看。

### 如何收藏命令？

详情页点右上角星标；**网格模式**下可直接点 cell 上的星标。在 **设置 → 收藏** 或**收藏**快速筛选中查看全部。

### 如何添加主屏小组件？

1. 长按主屏空白处，点 **+**。
2. 搜索 **iLinux**，选择样式并添加。

**设置 → 小组件指南** 有分步说明。**设置 → 小组件** 中可开启背景跟随主题渐变。

**小组件命令库：** 在 **设置 → 小组件** 选择 Linux / CMD / PowerShell，供「每日命令」与「分类聚焦」使用，可与应用内 Shell 切换独立设置。

### 每日命令小组件如何换一条命令？

点右上角**圆形箭头**（需 **iOS 17+**）。iOS 16 上每日固定一条，无刷新按钮。

### 如何配置主屏快捷方式？

长按应用图标显示最多 **4** 个快捷项。在 **设置 → 主屏快捷方式** 从 7 项中勾选：**搜索**、**每日测验**、**收藏**、**错题本**、**分类**、**发送反馈**、**评分**。可排序并重置为默认。

### 如何在快捷指令中使用？

使用 **打开 URL** 动作，例如：

- `ilinux://command?name=grep`（`cmd=` 等效）
- `ilinux://command?cmd=dir&platform=cmd`
- `ilinux://command?cmd=Get-ChildItem&platform=powershell`
- `ilinux://quiz`
- `ilinux://favorites`
- `ilinux://wrong` 或 `ilinux://mistakes`

**platform 参数：** `linux`（默认）、`cmd`（别名 `batch`/`bat`）、`powershell`（别名 `ps`/`pwsh`）。Linux 命令可省略。

**搜索**与**分类**仅作为主屏快捷方式。完整说明见 [URL Scheme 文档](url-scheme)。

### 如何分享命令？

命令详情页点 **分享**，可导出 **Markdown 文件**或生成 **PNG 分享卡片**（含 App Store 二维码）。保存图片到相册时可能请求相册权限。

### 如何更换主题色？

**设置 → 主题** — 15 款预设或**自定义颜色**。主题色与小组件镜像立即更新。

### 可以更换应用图标吗？

可以。**设置 → 应用图标**，**6 款**图标（默认 + 5 备用），即时生效。

### 小组件颜色与主题不匹配怎么办？

1. 打开一次应用刷新 App Group 数据。
2. 仍不对则长按小组件**编辑**或删除后重新添加。

请确保主应用与小组件扩展版本一致。

### 支持 iPad 吗？

支持。iPad 上网格最多 **8 列**；小组件、备用图标、主屏快捷方式与触觉反馈完整可用。

### Mac 上如何切换语言？

**语言选择器**在 **iPhone / iPad → 设置 → 语言**。Mac 上通常通过 **iCloud 同步**从其它设备获取偏好，或跟随已存储偏好 / 系统语言。建议开启 iCloud 同步以保持多设备一致。

### 仍需帮助？

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) 或 **设置 → 发送反馈**。通常 48 小时内回复。

</section>

<section lang="zh-TW" markdown="1">

### 愛 Linux 需要帳號或連網嗎？

不需要。指令庫完全離線打包在應用內。可選 **iCloud 同步**透過 Apple ID 對齊收藏與進度。

### 愛 Linux 支援 Mac 嗎？

支援。**macOS 13.0+** 原生側邊欄桌面應用（非 Mac Catalyst），含 **⌘,**、**⌘[**、**Esc**、**⌘←/→** 及測驗快捷鍵。主畫面小工具、捷徑、備用圖示**僅 iOS/iPad**。

### iCloud 同步如何運作？

在 **設定 → 學習統計** 開啟後，**收藏、測驗進度、主題、顯示偏好**在 **iPhone、iPad、Mac** 間透過 iCloud 鍵值儲存同步，衝突自動合併。指令庫仍完全離線。

### 愛 Linux 能在真實 Linux 終端機裡執行指令嗎？

不能。愛 Linux **僅為參考與學習工具**，不提供 Shell、SSH 或遠端執行環境。指令文件供你學習記憶——實際練習請在你自己的 Linux 機器、Windows PC、伺服器或雲端執行個體上進行。

### 愛 Linux 支援哪些 Shell 平台？

每種內容語言內建三套離線指令庫：

- **Linux** — 1050 條，14 個分類
- **Windows CMD / Batch** — 300 條，10 個分類
- **PowerShell** — 300 條，10 個分類

合計 **1650+** 條。在**指令**、**分類**或**每日測驗**頁的工具列 Shell 選單中切換。

### 如何在 Linux、CMD 與 PowerShell 之間切換？

在**指令**、**分類**或**每日測驗**頁，點工具列 **Shell 平台**選單。**設定 → 首頁快捷** 中可設預設平台、**收藏範圍**與**小工具指令庫**。

### 什麼是跨平台等效指令？

**100+ 組等效對照** 關聯 Linux、CMD 與 PowerShell 中同類任務的指令（如 `ls` / `dir` / `Get-ChildItem`）。詳情頁**等效指令**列可一鍵跳轉。

### 包含多少條指令？

每種內容語言 **1650+** 條：

| 平台 | 指令數 | 分類數 |
|------|--------|--------|
| Linux | 1050 | 14 |
| CMD / Batch | 300 | 10 |
| PowerShell | 300 | 10 |

### 如何搜尋指令？

在「指令」標籤點放大鏡，或按 **⌘F**。輸入指令名、關鍵字或描述片段，結果即時更新。

### 如何在列表與網格之間切換？

在**指令**或**分類**頁，開啟工具列篩選選單（漏斗圖示），在**檢視模式**下選擇**列表**或**網格**。網格模式下用 **+ / −** 調整每行列數（**iPhone 1–6**、**iPad / Mac 1–8**）。

### 如何記錄學習進度？

在指令詳情頁將狀態設為**未學**、**已學**或**熟練**。列表模式下右滑列可快速改狀態或收藏；網格模式下點星標收藏，長按選單改狀態。工具列篩選選**未學**可集中複習尚未掌握的指令。

### 提供哪些語言？

介面與指令文件均支援英文、簡體中文、繁體中文；也可選**系統**跟隨裝置。在 **設定 → 語言** 切換，含小工具在內的整個應用立即更新。

### 每日測驗如何運作？

每天基於日期種子產生題集，**依目前 Shell 平台**獨立出題。兩種題型：**配對簡介**、**配對選項含義**。點工具列**刷新按鈕**可隨時換題。**滿分連勝**按平台統計。

### 錯題沒有儲存怎麼辦？

需完整完成一輪測驗（答完所有題並到達結果頁）後才會儲存錯題。可在 **設定 → 錯題本** 查看。

### 如何收藏指令？

詳情頁點右上角星標；**網格模式**下可直接點 cell 上的星標。在 **設定 → 收藏** 或**收藏**快速篩選中查看全部。

### 如何新增主畫面小工具？

1. 長按主畫面空白處，點 **+**。
2. 搜尋 **iLinux**，選擇樣式並新增。

**設定 → 小工具指南** 有分步說明。**設定 → 小工具** 中可選 **小工具指令庫**（Linux / CMD / PowerShell），與應用內 Shell 切換可獨立設定。

### 每日指令小工具如何換一條指令？

點右上角**圓形箭頭**（需 **iOS 17+**）。iOS 16 上每日固定一條，無刷新按鈕。

### 如何設定主畫面捷徑？

長按應用圖示顯示最多 **4** 個捷徑。在 **設定 → 主畫面捷徑** 從 7 項中勾選：**搜尋**、**每日測驗**、**收藏**、**錯題本**、**分類**、**傳送回饋**、**評分**。可排序並重設為預設。

### 如何在捷徑中使用？

使用 **開啟 URL** 動作，例如：

- `ilinux://command?name=grep`
- `ilinux://command?cmd=dir&platform=cmd`
- `ilinux://command?cmd=Get-ChildItem&platform=powershell`
- `ilinux://quiz` / `ilinux://favorites` / `ilinux://wrong`

**platform：** `linux`（預設）、`cmd`、`powershell`（別名 `ps`/`pwsh`）。

完整說明見 [URL Scheme 文件](url-scheme)。

### 如何分享指令？

詳情頁 **分享** → **Markdown 檔**或 **PNG 分享卡片**。儲存至相簿可能請求相簿權限。

### 如何更換主題色？

**設定 → 主題** — 15 款預設或**自訂顏色**。主題色與小工具鏡像立即更新。

### 可以更換應用圖示嗎？

可以。**設定 → 應用圖示**，**6 款**圖示（預設 + 5 備用），即時生效。

### 小工具顏色與主題不相符怎麼辦？

1. 開啟一次應用重新整理 App Group 資料。
2. 仍不對則長按小工具**編輯**或刪除後重新新增。

請確保主應用與小工具擴充套件版本一致。

### 支援 iPad 嗎？

支援。iPad 上網格最多 **8 欄**；小工具、備用圖示、主畫面捷徑完整可用。

### Mac 上如何切換語言？

**語言選擇器**在 **iPhone / iPad → 設定 → 語言**。Mac 上通常經 **iCloud 同步**取得偏好。建議開啟 iCloud 同步。

### 仍需協助？

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) 或 **設定 → 傳送回饋**。通常 48 小時內回覆。

</section>
