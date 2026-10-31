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

Note: **Search** and **Categories** are available as Home Screen quick actions but are not registered as universal deep-link hosts. See the full [URL Scheme Reference](../url-scheme).

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

**搜索**与**分类**仅作为主屏快捷方式。完整说明见 [URL Scheme 文档](../url-scheme)。

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

完整說明見 [URL Scheme 文件](../url-scheme)。

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
<section lang="ja" markdown="1">

### iLinux にはアカウントやインターネット接続が必要ですか?

いいえ、iLinux はコマンド ライブラリに対して完全にオフラインで動作します。すべてのコマンド データ (JSON サマリーと Markdown ドキュメント) はアプリ内にバンドルされています。ドキュメントを閲覧したり、読んだり、クイズに答えたりするには、サインアップは必要ありません。オプションの **iCloud 同期**は、Apple ID を使用してデバイス間でお気に入りと進行状況を調整します。コマンドのコンテンツはアップロードされません。

### iLinux は Mac をサポートしていますか?

はい。 iLinux は、**サイドバー デスクトップ レイアウト**、サイズ変更可能なウィンドウ、拡張キーボード ショートカット (**⌘,**, **⌘[**, **Esc**, **⌘←/→**、クイズ キー **1–4** / **⌘R** / **Return**) を備えた **ネイティブ macOS アプリ** (Mac Catalyst ではなく macOS **13.0+**) です。すべてのコア機能 (3 つのシェル ライブラリ、同等のライブラリ、クイズ、ディープ リンク、テーマ) は Mac 上で動作します。

**Mac では使用できません:** ホーム画面ウィジェット、ホーム画面のクイック アクション、代替アプリ アイコンは **iPhone/iPad のみ**です。 iOS でウィジェットを構成します。 Mac ではアプリ内通知が表示されます。

### iCloud同期はどのように機能しますか?

同じ Apple ID で **iCloud** にサインインしている場合は、**[設定] → [学習統計]** で **iCloud 同期**を有効にします。 iLinux は、**お気に入り**、**クイズの進行状況**、**テーマ**、**表示設定** (言語、シェル プラットフォーム、お気に入りの範囲、リスト/グリッド) を iCloud Key-Value ストレージ経由で **iPhone、iPad、Mac** 間で同期します。競合は自動的にマージされます (お気に入りの結合など)。 **1 台のデバイスで同期を無効にする**ことができ、他のデバイスには影響を与えません。コマンド ライブラリは完全にオフラインのままです。個人的な進行状況のみが同期されます。

### iLinux は実際の Linux ターミナル上でコマンドを実行しますか?

いいえ、iLinux は **参照および学習ツールのみ**です。シェル、SSH クライアント、またはリモート実行環境は提供されません。コマンドは学習用に文書化されており、自分の Linux マシン、Windows PC、サーバー、またはクラウド インスタンスで練習できます。

### iLinux はどのシェル プラットフォームをサポートしていますか?

iLinux には、コンテンツ言語ごとに 3 つのオフライン コマンド ライブラリが同梱されています。

- **Linux** — 14 カテゴリの 1050 コマンド
- **Windows CMD / バッチ** — 10 カテゴリの 300 コマンド
- **PowerShell** — 10 カテゴリの 300 コマンド

**各言語 (英語、簡体字中国語、繁体字中国語) ごとに合計 1650 以上のコマンド**。 **コマンド**、**カテゴリ**、または**デイリークイズ**のツールバーのシェルメニューからライブラリを切り替えます。

### Linux、CMD​​、PowerShell の間で切り替えるにはどうすればよいですか?

[コマンド]、[カテゴリ]、または [デイリー クイズ] タブのツールバーにある **シェル プラットフォーム** メニュー (端末アイコン) をタップします。選択内容は保持され、そのプラットフォームの検索、カテゴリ、クイズの質問、学習統計が対象になります。

**[設定] → [ホーム] クイック アクセス** では、デフォルトのシェル プラットフォーム、**お気に入りの範囲** (すべてのプラットフォームと現在のプラットフォームのみ)、デイリー コマンド ウィジェットとカテゴリ スポットライト ウィジェットの **ウィジェット コマンド ライブラリ** を設定することもできます。

### クロスプラットフォームで同等のコマンドとは何ですか?

**100 を超える同等のグループ** は、Linux、CMD​​、PowerShell 全体で同じタスクを実行するコマンドをリンクします (例: `ls`、`dir`、`Get-ChildItem`)。コマンドの詳細ページでは、**同等** バーに関連エントリが表示されます。いずれかをタップすると、そのプラットフォームのドキュメントに即座にジャンプします。

### コマンドはいくつ含まれていますか?

各コンテンツ言語には、次の 3 つのシェル ライブラリにわたる **1650+** コマンドが含まれています。

| プラットフォーム | コマンド | カテゴリー |
|----------|----------|------------|
| Linux | 1050 | 14 |
| CMD / バッチ | 300 | 10 |
| パワーシェル | 300 | 10 |

すべてのドキュメントは、英語、簡体字中国語、繁体字中国語でオフラインで利用できます。

### コマンドを検索するにはどうすればよいですか?

[コマンド] タブの拡大鏡アイコンをタップするか、ハードウェア キーボードで **⌘F** を押します。コマンド名、キーワード、または説明の一部を入力します。入力すると結果がリアルタイムで更新されます。

### リスト表示とグリッド表示を切り替えるにはどうすればよいですか?

[**コマンド**] タブまたは [**カテゴリ**] タブで、ツールバーのフィルター メニュー (漏斗アイコン) を開きます。 **表示モード**で、**リスト**または**グリッド**を選択します。グリッド モードでは、**+ / −** ボタンを使用して行ごとに列を設定します (iPhone**では**1 ～ 6、iPad および Mac**では**1 ～ 8)。 **[設定] → [表示]** でデフォルトを変更することもできます。

### 学習の進捗状況を追跡するにはどうすればよいですか?

コマンドの詳細ページを開き、ステータスを **未学習**、**学習**、または **習得** に設定します。リスト ビューで行をスワイプすると、ステータスやお気に入りのアクションを簡単に表示できます。グリッド ビューでは、スター ボタンを使用してお気に入りを設定し、コンテキスト メニューを使用してステータスを確認します。ツールバー メニューから [**未学習**] にフィルターして、まだ学習していないコマンドに焦点を当てます。

### どのような言語が利用可能ですか?

iLinux は、アプリ インターフェイスとコマンド ドキュメントの両方で 3 つの言語をサポートしています。

- **英語**
- **簡体字中国語 (简体中文)**
- **繁体字中国語 (繁體中文)**

[**システム**] を選択して、デバイスのロケールに従うこともできます。 **[設定] → [言語]** で言語を変更します。ウィジェットを含むアプリ全体がすぐに更新されます。

### 毎日のクイズはどのように機能しますか?

毎日、**アクティブなシェル プラットフォーム** (Linux、CMD​​、または PowerShell) を対象とした日付ベースのシードを使用して、新しいクイズの質問セットが生成されます。同じ日に iLinux を使用する全員が、そのプラットフォーム用の同じ基本クイズ セットを受け取ります。次の 2 つの質問タイプが表示されます。

- **一致概要** — 短い説明が表示され、正しいコマンド名を選択する必要があります。
- **オプションの意味の一致** — フラグの説明 (例: `-r: recursive`) が表示され、それがどのコマンドに属しているかを識別する必要があります。

Tap the **refresh button** (circular arrow) in the toolbar to get a different randomised set at any time. **Perfect streak** days (consecutive days with a perfect score) are tracked per platform and shown in the quiz screen and Quiz Glance widget. Generic help flags like `-h` and `--version` are excluded to keep questions unambiguous.

### 間違った回答は保存されません。どうすればいいですか？

間違った回答は、クイズ セッションの完了後に自動的に保存されます。必ずクイズをすべて完了してください (すべての質問に答えて結果画面に到達してください)。部分的に完了したセッションは保存されません。

**[設定] → [誤答ブック]** で、保存されたすべての誤答を確認できます。

### コマンドをお気に入りに追加するにはどうすればよいですか?

コマンドの詳細ページを開き、右上隅にある **星アイコン** をタップします。 **グリッド ビュー**では、コマンド セルの星を直接タップします。 **[設定] → [お気に入り**] または [**お気に入り**] クイック フィルターからすべてのお気に入りにアクセスします。

### ホーム画面ウィジェットを設定するにはどうすればよいですか?

1. ホーム画面の何もない領域を長押しし、上隅にある **+** ボタンをタップします。
2. ウィジェット ギャラリーで **iLinux** を検索します。
3. ウィジェット スタイルを選択し、**ウィジェットを追加** をタップします。

ステップバイステップの **ウィジェット ガイド** は、**[設定] → [ウィジェット ガイド]** でも利用できます。ウィジェットの背景をアプリのテーマのグラデーションに従うようにするには、**[設定] → [ウィジェット]** のオプションを有効にします。

**ウィジェット コマンド ライブラリ:** **[設定] → [ウィジェット]** で、デイリー コマンド ウィジェットとカテゴリ スポットライト ウィジェットにフィードするシェル ライブラリ (Linux / CMD / PowerShell) を選択します。これはアプリ内シェル スイッチとは独立しています。アプリ内で Linux を参照しているときにウィジェットに Windows コマンドを表示したい場合に便利です。

### Daily Command ウィジェットには、同じコマンドが毎日表示されます。どうすれば変更できますか?

Daily Command ウィジェットの右上隅にある **円形の矢印 (シャッフル) ボタン**をタップすると、別のコマンドがすぐにロードされます。この機能には **iOS 17 以降** が必要です。

iOS 16 では、デイリー コマンド ウィジェットには毎日の固定コマンドが表示され、シャッフル ボタンは含まれません。

### ホーム画面のクイックアクションを設定するにはどうすればよいですか?

iLinux アプリのアイコンを長押しすると、最大 **4** のクイック アクションが表示されます。 **[設定] → [ホーム画面のショートカット]** に表示されるアクションを選択します。 **検索**、**デイリークイズ**、**お気に入り**、**誤答集**、**カテゴリ**、**フィードバックを送信**、**アプリを評価**の7つのオプションが利用可能です。同じ画面から並べ替えたり、デフォルトにリセットしたりできます。

### iLinux をショートカット アプリで使用するにはどうすればよいですか?

iLinux supports the `ilinux://` URL scheme. Use an **Open URLs** action in the Shortcuts app. Examples:

- `ilinux://command?name=grep` — Linux コマンド `grep` を開きます (`cmd=` も機能します)
- `ilinux://command?cmd=dir&platform=cmd` — CMD コマンド `dir` を開きます
- `ilinux://command?cmd=Get-ChildItem&platform=powershell` — PowerShell コマンドを開きます
- `ilinux://quiz` — [デイリークイズ] タブを開きます
- `ilinux://favorites` — お気に入りリストを開きます
- `ilinux://wrong` or `ilinux://mistakes` — opens the Wrong Answer Book

**プラットフォーム パラメーター:** `platform=linux` (デフォルト)、`cmd` (エイリアス: `batch`、`bat`)、または `powershell` (エイリアス: `ps`、`pwsh`)。 Linux コマンドの場合は省略します。

注: **検索** と **カテゴリ** はホーム画面のクイック アクションとして使用できますが、ユニバーサル ディープリンク ホストとしては登録されません。完全な [URL スキーム リファレンス](../url-scheme) を参照してください。

### コマンドを共有するにはどうすればよいですか?

コマンドの詳細ページで、ツールバーの **共有** をタップします。コマンドを **Markdown ファイル**としてエクスポートすることも、**スタイル付きの PNG 共有カード** (App Store QR コード付き) を生成して、システムの共有シートを通じて送信することもできます。画像を写真に保存すると、フォト ライブラリへのアクセスが要求される場合があります。

### テーマの色を変更するにはどうすればよいですか?

**[設定] → [テーマ]** に移動します。 15 の組み込みカラー プリセットをスクロールするか、**カスタム カラー** 行をタップして、システム カラー ピッカーを使用して任意の色を選択します。アクセントカラー、グラデーション、ウィジェットミラーはすべてすぐに更新されます。

### アプリのアイコンを変更できますか?

はい。 **[設定] → [アプリ アイコン]** に移動し、**6 つのアイコン** (デフォルトと 5 つの代替アイコン) から選択します。設定はアプリを再起動しなくてもすぐに適用されます。

### ウィジェットの色がテーマと一致しません。どうすれば修正できますか?

ウィジェットは、メイン アプリとウィジェット拡張機能の間で共有されるアプリ グループを介してテーマの色を同期します。ウィジェットが古いように見える場合:

1. iLinux を 1 回開きます。これにより、アプリ グループ データが強制的に更新されます。
2. それでもウィジェットが更新されない場合は、ウィジェットを長押しし、[**ウィジェットの編集**] をタップして (または削除して再追加し)、タイムラインの再読み込みをトリガーします。

**iLinux ウィジェット** 拡張機能とメイン アプリが両方とも最新 (同じバージョン) であることを確認してください。

### iLinux は iPad をサポートしていますか?

はい。 iLinux は、アダプティブ レイアウトを使用して iPad 上でネイティブに実行されます。グリッド モードは最大 **8 列**をサポートします。ウィジェット、代替アイコン、ホーム画面のショートカット、および触覚は iPad で完全にサポートされています。

### Mac で言語を変更するにはどうすればよいですか?

アプリ内の **言語ピッカー**は、**iPhone および iPad** の **[設定] → [言語]** にあります。 **Mac** では、言語設定は通常、**iCloud 同期**を介して別のデバイスから受信されるか、初回起動時に保存された設定/システム ロケールに従います。 iCloud 同期を有効にして、デバイス間で言語を一致させます。

### まだ助けが必要ですか?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) までお問い合わせいただくか、アプリ内の **[設定] → [フィードバックを送信]** オプションを使用してください。通常、48 時間以内に返信いたします。

</section>
<section lang="ko" markdown="1">

### iLinux에는 계정이나 인터넷 연결이 필요합니까?

아니요. iLinux는 명령 라이브러리에 대해 완전히 오프라인으로 작동합니다. 모든 명령 데이터(JSON 요약 및 Markdown 문서)는 앱 내에 번들로 제공됩니다. 문서를 탐색하고, 읽고, 퀴즈를 풀기 위해 가입이 필요하지 않습니다. 옵션인 **iCloud 동기화**는 Apple ID를 사용하여 여러 기기에서 즐겨찾기와 진행 상황을 정렬합니다. 명령 콘텐츠는 업로드하지 않습니다.

### iLinux는 Mac을 지원합니까?

예. iLinux는 **사이드바 데스크탑 레이아웃**, 크기 조정 가능한 창, 확장된 키보드 단축키(**⌘,**, **⌘[**, **Esc**, **⌘←/→**, 퀴즈 키 **1–4** / **⌘R** / **Return**)를 갖춘 **기본 macOS 앱**(Mac Catalyst가 아닌 macOS **13.0+**)입니다. 세 가지 쉘 라이브러리, 이에 상응하는 항목, 퀴즈, 딥 링크, 테마 등 모든 핵심 기능이 Mac에서 작동합니다.

**Mac에서는 해당되지 않음:** 홈 화면 위젯, 홈 화면 빠른 작업 및 대체 앱 아이콘은 **iPhone/iPad 전용**입니다. iOS에서 위젯을 구성합니다. Mac에 앱 내 알림이 표시됩니다.

### iCloud 동기화는 어떻게 작동하나요?

동일한 Apple ID로 **iCloud**에 로그인한 경우 **설정 → 학습 통계**에서 **iCloud 동기화**를 활성화하세요. iLinux는 iCloud 키-값 저장소를 통해 **iPhone, iPad 및 Mac** 전체에서 **즐겨찾기**, **퀴즈 진행**, **테마** 및 **표시 기본 설정**(언어, 쉘 플랫폼, 즐겨찾기 범위, 목록/그리드)을 동기화합니다. 충돌은 자동으로 병합됩니다(예: 즐겨찾기 통합). 다른 기기에 영향을 주지 않고 **한 기기에서 동기화를 비활성화**할 수 있습니다. 명령 라이브러리는 완전히 오프라인 상태로 유지됩니다. 개인 진행 상황만 동기화됩니다.

### iLinux는 실제 Linux 터미널에서 명령을 실행합니까?

아니요. iLinux는 **참조 및 학습 도구**일 뿐입니다. 쉘, SSH 클라이언트 또는 원격 실행 환경을 제공하지 않습니다. 학습을 위해 명령이 문서화되어 있으므로 자신의 Linux 시스템, Windows PC, 서버 또는 클라우드 인스턴스에서 연습할 수 있습니다.

### iLinux는 어떤 쉘 플랫폼을 지원합니까?

iLinux는 콘텐츠 언어별로 세 가지 오프라인 명령 라이브러리를 제공합니다.

- **Linux** — 14개 카테고리의 1050개 명령
- **Windows CMD / 배치** — 10개 카테고리에 300개 명령
- **PowerShell** — 10개 카테고리의 300개 명령

**언어당 총 1650개 이상의 명령**(영어, 중국어 간체, 중국어 번체). **명령**, **카테고리** 또는 **일일 퀴즈**의 도구 모음 셸 메뉴에서 라이브러리를 전환하세요.

### Linux, CMD, PowerShell 간에 어떻게 전환하나요?

명령, 범주 또는 일일 퀴즈 탭의 도구 모음에서 **쉘 플랫폼** 메뉴(터미널 아이콘)를 탭합니다. 귀하의 선택은 유지되며 해당 플랫폼에 대한 검색, 카테고리, 퀴즈 질문 및 학습 통계의 범위를 정합니다.

**설정 → 홈 빠른 액세스**에서 기본 셸 플랫폼, **즐겨찾는 범위**(모든 플랫폼과 현재 플랫폼만 해당), 일일 명령 및 카테고리 스포트라이트 위젯에 대한 **위젯 명령 라이브러리**를 설정할 수도 있습니다.

### 크로스 플랫폼에 해당하는 명령이란 무엇입니까?

**100개 이상의 동등한 그룹** 링크 명령은 Linux, CMD 및 PowerShell에서 동일한 작업을 수행합니다(예: `ls`, `dir` 및 `Get-ChildItem`). 명령 세부 사항 페이지에서 **동등한 항목** 막대에는 관련 항목이 표시됩니다. 하나를 탭하면 해당 플랫폼의 문서로 즉시 이동합니다.

### 얼마나 많은 명령이 포함되어 있습니까?

각 콘텐츠 언어에는 세 가지 셸 라이브러리에 걸쳐 **1650+** 명령이 포함되어 있습니다.

| 플랫폼 | 명령 | 카테고리 |
|----------|----------|------------|
| 리눅스 | 1050 | 14 |
| CMD/배치 | 300 | 10 |
| 파워셸 | 300 | 10 |

모든 문서는 오프라인에서 영어, 중국어 간체, 중국어 번체로 제공됩니다.

### 명령을 검색하려면 어떻게 해야 합니까?

명령 탭에서 돋보기 아이콘을 탭하거나 하드웨어 키보드에서 **⌘F**를 누르세요. 명령 이름, 키워드 또는 설명의 일부를 입력하십시오. 입력하는 동안 결과가 실시간으로 업데이트됩니다.

### 목록 보기와 그리드 보기 간에 어떻게 전환하나요?

On the **Commands** or **Categories** tab, open the toolbar filter menu (funnel icon). Under **View Mode**, choose **List** or **Grid**. In grid mode, use the **+ / −** buttons to set columns per row (**1–6 on iPhone**, **1–8 on iPad and Mac**). You can also change the default in **Settings → Display**.

### 학습 진행 상황을 어떻게 추적하나요?

명령의 세부 정보 페이지를 열고 해당 상태를 **학습 안함**, **학습됨** 또는 **마스터됨**으로 설정합니다. 목록 보기에서 행을 스와이프하여 빠른 상태 및 즐겨찾는 작업을 확인하세요. 그리드 보기에서는 즐겨찾기에 별표 버튼을 사용하고 상태에 대한 컨텍스트 메뉴를 사용합니다. 아직 학습하지 않은 명령에 집중하려면 도구 모음 메뉴에서 **학습되지 않음**으로 필터링하세요.

### 어떤 언어를 사용할 수 있나요?

iLinux는 앱 인터페이스와 명령 문서 모두에 대해 세 가지 언어를 지원합니다.

- **영어**
- **중국어 간체(简体中文)**
- **중국어 번체(繁體中文)**

**시스템**을 선택하여 기기의 언어를 따를 수도 있습니다. **설정 → 언어**에서 언어를 변경하세요. 위젯을 포함한 전체 앱이 즉시 업데이트됩니다.

### 일일 퀴즈는 어떻게 진행되나요?

매일 **활성 셸 플랫폼으로 범위가 지정된**(Linux, CMD 또는 PowerShell) 날짜 기반 시드를 사용하여 새로운 퀴즈 질문 세트가 생성됩니다. 같은 날 iLinux를 사용하는 모든 사람은 해당 플랫폼에 대해 동일한 기본 퀴즈 세트를 받게 됩니다. 두 가지 질문 유형이 나타납니다.

- **일치 요약** — 간단한 설명이 표시되며 올바른 명령 이름을 선택해야 합니다.
- **일치 옵션 의미** — 플래그 설명(예: `-r: recursive`)을 보고 해당 플래그가 속한 명령을 식별해야 합니다.

툴바에서 **새로고침 버튼**(원형 화살표)을 탭하면 언제든지 다른 무작위 세트를 얻을 수 있습니다. **완벽한 연속** 일수(만점을 연속으로 달성한 일수)는 플랫폼별로 추적되며 퀴즈 화면과 Quiz Glance 위젯에 표시됩니다. 질문을 명확하게 유지하기 위해 `-h` 및 `--version`과 같은 일반 도움말 플래그는 제외됩니다.

### 오답이 저장되지 않습니다. 어떻게 해야 하나요?

퀴즈 세션을 완료하면 오답이 자동으로 저장됩니다. 전체 퀴즈 라운드를 완료했는지 확인하세요(모든 질문에 답하고 결과 화면에 도달). 부분적으로 완료된 세션은 저장되지 않습니다.

저장된 모든 오답은 **설정 → 오답록**에서 확인하실 수 있습니다.

### 즐겨찾기에 명령을 어떻게 추가하나요?

명령의 세부정보 페이지를 열고 오른쪽 상단에 있는 **별표 아이콘**을 탭하세요. **그리드 보기**에서는 명령 셀의 별표를 직접 탭하세요. **설정 → 즐겨찾기** 또는 **즐겨찾기** 퀵 필터에서 모든 즐겨찾기에 액세스하세요.

### 홈 화면 위젯을 어떻게 설정하나요?

1. 홈 화면의 빈 공간을 길게 누르고 상단 모서리에 있는 ****버튼을 탭하세요.
2. 위젯 갤러리에서 **iLinux**를 검색하세요.
3. 위젯 스타일을 선택하고 **위젯 추가**를 탭하세요.

단계별 **위젯 가이드**는 **설정 → 위젯 가이드**에서도 확인할 수 있습니다. 위젯 배경이 앱 테마 그라데이션을 따르도록 하려면 **설정 → 위젯**에서 옵션을 활성화하세요.

**위젯 명령 라이브러리:** **설정 → 위젯**에서 일일 명령 및 카테고리 스포트라이트 위젯에 피드를 제공하는 셸 라이브러리(Linux/CMD/PowerShell)를 선택합니다. 이는 앱 내 셸 스위치와 별개입니다. 앱 내에서 Linux를 검색하는 동안 위젯에 Windows 명령이 표시되도록 하려는 경우 유용합니다.

### Daily Command 위젯은 매일 동일한 명령을 표시합니다. 어떻게 바꾸나요?

일일 명령 위젯의 오른쪽 상단에 있는 **원형 화살표(셔플) 버튼**을 탭하면 다른 명령을 즉시 로드할 수 있습니다. 이 기능을 사용하려면 **iOS 17 이상**이 필요합니다.

iOS 16에서 일일 명령 위젯은 매일 고정된 명령을 표시하며 순서 섞기 버튼을 포함하지 않습니다.

### 홈 화면 빠른 작업을 어떻게 구성합니까?

iLinux 앱 아이콘을 길게 누르면 최대 **4** 빠른 작업을 볼 수 있습니다. **설정 → 홈 화면 바로가기**에 표시할 작업을 선택하세요. **검색**, **일일 퀴즈**, **즐겨찾기**, **오답록**, **카테고리**, **피드백 보내기**, **앱 평가** 등 7가지 옵션을 사용할 수 있습니다. 동일한 화면에서 순서를 변경하고 기본값으로 재설정할 수 있습니다.

### 단축어 앱으로 iLinux를 어떻게 사용하나요?

iLinux는 `ilinux://` URL 체계를 지원합니다. 바로가기 앱에서 **URL 열기** 작업을 사용하세요. 예:

- `ilinux://command?name=grep` — Linux 명령 `grep`을 엽니다(`cmd=`도 작동함)
- `ilinux://command?cmd=dir&platform=cmd` — CMD 명령 `dir`을 엽니다.
- `ilinux://command?cmd=Get-ChildItem&platform=powershell` — PowerShell 명령을 엽니다.
- `ilinux://quiz` — 일일 퀴즈 탭을 엽니다.
- `ilinux://favorites` — 즐겨찾기 목록을 엽니다.
- `ilinux://wrong` 또는 `ilinux://mistakes` — 틀린 답안집을 엽니다.

**플랫폼 매개변수:** `platform=linux`(기본값), `cmd`(별칭: `batch`, `bat`) 또는 `powershell`(별칭: `ps`, `pwsh`). Linux 명령의 경우 생략합니다.

참고: **검색** 및 **카테고리**는 홈 화면 빠른 작업으로 사용할 수 있지만 범용 딥 링크 호스트로 등록되지는 않습니다. 전체 [URL 체계 참조](../url-scheme)를 확인하세요.

### 명령을 어떻게 공유하나요?

명령 세부정보 페이지의 도구 모음에서 **공유**를 탭하세요. 명령을 **마크다운 파일**로 내보내거나 **스타일이 지정된 PNG 공유 카드**(App Store QR 코드 포함)를 생성하여 시스템 공유 시트를 통해 보낼 수 있습니다. 사진에 이미지를 저장하면 사진 라이브러리 액세스가 필요할 수 있습니다.

### 테마 색상을 어떻게 변경하나요?

**설정 → 테마**로 이동하세요. 15가지 내장 색상 사전 설정을 스크롤하거나 **사용자 정의 색상** 행을 탭하여 시스템 색상 선택기를 사용하여 원하는 색상을 선택하세요. 강조 색상, 그라데이션 및 위젯 미러가 모두 즉시 업데이트됩니다.

### 앱 아이콘을 변경할 수 있나요?

예. **설정 → 앱 아이콘**으로 이동하여 **6개 아이콘**(기본값 + 대체 5개) 중에서 선택하세요. 앱을 다시 실행하지 않고도 설정이 즉시 적용됩니다.

### 위젯 색상이 내 테마와 일치하지 않습니다. 어떻게 해결하나요?

위젯은 기본 앱과 위젯 확장 간에 공유되는 앱 그룹을 통해 테마 색상을 동기화합니다. 위젯이 오래된 것처럼 보이는 경우:

1. iLinux를 한 번 엽니다. 그러면 앱 그룹 데이터가 강제로 새로 고쳐집니다.
2. 그래도 위젯이 업데이트되지 않으면 위젯을 길게 누르고 **위젯 편집**을 탭하여(또는 제거했다가 다시 추가) 타임라인 새로고침을 실행하세요.

**iLinux Widget** 확장 프로그램과 기본 앱이 모두 최신 버전인지(동일한 버전) 확인하세요.

### iLinux는 iPad를 지원합니까?

예. iLinux는 적응형 레이아웃을 통해 iPad에서 기본적으로 실행됩니다. 그리드 모드는 최대 **8개 열**을 지원합니다. 위젯, 대체 아이콘, 홈 화면 단축키 및 햅틱이 iPad에서 완벽하게 지원됩니다.

### Mac에서 언어를 어떻게 변경하나요?

인앱 **언어 선택기**는 **iPhone 및 iPad**의 **설정 → 언어**에 있습니다. **Mac**에서 언어 기본 설정은 일반적으로 다른 기기의 **iCloud 동기화**를 통해 도착하거나 처음 실행 시 저장된 기본 설정/시스템 로케일을 따릅니다. 기기 전반에 걸쳐 언어를 정렬하려면 iCloud 동기화를 활성화하세요.

### 아직도 도움이 필요하신가요?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)으로 문의하시거나 앱 내 **설정 → 피드백 보내기** 옵션을 이용하세요. 우리는 일반적으로 48시간 이내에 응답합니다.

</section>
<section lang="ru" markdown="1">

### Требуется ли iLinux учетная запись или подключение к Интернету?

Нет. iLinux работает полностью автономно для библиотек команд. Все данные команд (сводки JSON и документация Markdown) объединены внутри приложения. Для просмотра, чтения документации или прохождения тестов регистрация не требуется. Дополнительная функция **синхронизация с iCloud** использует ваш Apple ID для согласования избранного и прогресса на разных устройствах — при этом содержимое команд не загружается.

### Поддерживает ли iLinux Mac?

Да. iLinux — это **собственное приложение для macOS** (macOS **13.0+**, а не Mac Catalyst) с **раскладкой рабочего стола на боковой панели**, окном с изменяемым размером и расширенными сочетаниями клавиш (**⌘,**, **⌘[**, **Esc**, **⌘ ←/→**, клавиши викторины **1–4** / **⌘R** / **Return**). Все основные функции — три библиотеки оболочки, эквиваленты, тесты, глубокие ссылки и темы — работают на Mac.

**Не на Mac:** виджеты главного экрана, быстрые действия на главном экране и альтернативные значки приложений доступны **только для iPhone/iPad**. Настроить виджеты на iOS; Mac показывает уведомление в приложении.

### Как работает синхронизация с iCloud?

Войдя в **iCloud** с тем же Apple ID, включите **iCloud Sync** в **Настройки → Статистика обучения**. iLinux синхронизирует **избранное**, **прогресс теста**, **тему** и **настройки отображения** (язык, платформа оболочки, область избранного, список/сетка) на **iPhone, iPad и Mac** через хранилище ключей и значений iCloud. Конфликты автоматически объединяются (например, объединение избранных). Вы можете **отключить синхронизацию на одном устройстве**, не затрагивая другие. Библиотеки команд остаются полностью автономными; синхронизируется только ваш личный прогресс.

### Выполняет ли iLinux команды на реальном терминале Linux?

Нет. iLinux — это **только справочный и обучающий инструмент**. Он не предоставляет оболочку, SSH-клиент или среду удаленного выполнения. Команды документированы для изучения — вы практикуете их на своем компьютере с Linux, ПК с Windows, сервере или облачном экземпляре.

### Какие платформы оболочки поддерживает iLinux?

iLinux предлагает три библиотеки автономных команд для каждого языка контента:

- **Linux** — 1050 команд в 14 категориях.
- **Windows CMD/Batch** — 300 команд в 10 категориях.
- **PowerShell** — 300 команд в 10 категориях.

**Всего более 1650 команд** на каждом языке (английский, упрощенный китайский, традиционный китайский). Переключайте библиотеки из меню оболочки на панели инструментов в **Командах**, **Категориях** или **Ежедневной викторине**.

### Как мне переключаться между Linux, CMD и PowerShell?

Нажмите меню **Платформа Shell** (значок терминала) на панели инструментов на вкладке «Команды», «Категории» или «Ежедневная викторина». Ваш выбор сохраняется и охватывает поиск, категории, вопросы викторины и статистику обучения для этой платформы.

В **Настройки → Быстрый доступ на главную** вы также можете установить платформу оболочки по умолчанию, **область избранного** (все платформы или только текущая платформа) и **библиотеку команд виджета** для виджетов Daily Command и Category Spotlight.

### Что такое кроссплатформенные эквивалентные команды?

**более 100 эквивалентных групп** связывают команды, которые выполняют одну и ту же задачу в Linux, CMD и PowerShell — например, `ls`, `dir` и `Get-ChildItem`. На странице сведений о команде на панели **Эквиваленты** отображаются связанные записи; коснитесь одного, чтобы мгновенно перейти к документации этой платформы.

### Сколько команд включено?

Каждый язык контента включает **1650+** команд в трех библиотеках оболочки:

| Платформа | Команды | Категории |
|----------|----------|------------|
| Линукс | 1050 | 14 |
| CMD/пакетный режим | 300 | 10 |
| PowerShell | 300 | 10 |

Вся документация доступна в автономном режиме на английском, упрощенном и традиционном китайском языках.

### Как найти команду?

Коснитесь значка лупы на вкладке «Команды» или нажмите **⌘F** на аппаратной клавиатуре. Введите имя команды, ключевое слово или часть описания. Результаты обновляются в режиме реального времени по мере ввода.

### Как переключиться между списком и сеткой?

На вкладке **Команды** или **Категории** откройте меню фильтров панели инструментов (значок воронки). В разделе **Режим просмотра** выберите **Список** или **Сетка**. В режиме сетки используйте кнопки **+/-** для установки столбцов в каждой строке (**1–6 на iPhone**, **1–8 на iPad и Mac**). Вы также можете изменить значение по умолчанию в **Настройки → Дисплей**.

### Как отслеживать прогресс в обучении?

Откройте страницу сведений о команде и установите для нее статус **Необучено**, **Обучено** или **Освоено**. В режиме списка проведите пальцем по строке, чтобы просмотреть быстрый статус и избранные действия. В виде сетки используйте кнопку со звездочкой для избранного и контекстное меню для статуса. Установите фильтр **Необученные** в меню панели инструментов, чтобы сосредоточиться на командах, которые вы еще не изучили.

### Какие языки доступны?

iLinux поддерживает три языка как для интерфейса приложения, так и для командной документации:

- **Английский**
- **Упрощенный китайский (简体中文)**
- **Традиционный китайский (繁體中文)**

Вы также можете выбрать **Система**, чтобы следовать языковому стандарту вашего устройства. Измените язык в **Настройки → Язык**. Все приложение, включая виджеты, обновляется немедленно.

### Как работает ежедневная викторина?

Каждый день создается новый набор вопросов викторины с использованием начального числа на основе даты, **привязанного к активной платформе оболочки** (Linux, CMD или PowerShell). Каждый, кто использует iLinux в один и тот же день, получает один и тот же базовый набор тестов для этой платформы. Появятся два типа вопросов:

- **Сводка матча** — вы видите краткое описание и должны выбрать правильное имя команды.
- **Match Option Meaning** — you see a flag's description (e.g. `-r: recursive`) and must identify which command it belongs to.

Tap the **refresh button** (circular arrow) in the toolbar to get a different randomised set at any time. **Perfect streak** days (consecutive days with a perfect score) are tracked per platform and shown in the quiz screen and Quiz Glance widget. Generic help flags like `-h` and `--version` are excluded to keep questions unambiguous.

### Мои неправильные ответы не сохраняются. Что я должен делать?

Неправильные ответы сохраняются автоматически после завершения сеанса викторины. Обязательно завершите полный раунд викторины (ответьте на все вопросы и дойдите до экрана с результатами). Частично завершенные сеансы не сохраняются.

Вы можете просмотреть все сохраненные неправильные ответы в **Настройки → Книга неправильных ответов**.

### Как добавить команду в Избранное?

Откройте страницу сведений о любой команде и коснитесь **значка звездочки** в правом верхнем углу. В режиме **сетки** коснитесь звездочки непосредственно в командной ячейке. Доступ ко всему избранному осуществляется через **Настройки → Избранное** или с помощью быстрого фильтра **Избранное**.

### Как настроить виджеты главного экрана?

1. Нажмите и удерживайте пустую область главного экрана и нажмите кнопку **+** в верхнем углу.
2. Найдите **iLinux** в галерее виджетов.
3. Выберите стиль виджета и нажмите **Добавить виджет**.

Пошаговое **Руководство по виджетам** также доступно в разделе **Настройки → Руководство по виджетам**. Чтобы фон виджетов соответствовал градиенту темы вашего приложения, включите эту опцию в **Настройки → Виджеты**.

**Библиотека команд виджета:** В меню **Настройки → Виджеты** выберите, какая библиотека оболочки (Linux/CMD/PowerShell) будет использоваться для виджетов Daily Command и Category Spotlight. Это не зависит от переключателя оболочки в приложении — полезно, если вы хотите, чтобы виджеты отображали команды Windows при просмотре Linux внутри приложения.

### Виджет Daily Command показывает одну и ту же команду каждый день. Как мне это изменить?

Нажмите кнопку **круговую стрелку (перемешать)** в правом верхнем углу виджета «Ежедневные команды», чтобы немедленно загрузить другую команду. Для этой функции требуется **iOS 17 или новее**.

В iOS 16 виджет «Ежедневная команда» отображает фиксированную команду на каждый день и не включает кнопку перемешивания.

### Как настроить быстрые действия на главном экране?

Нажмите и удерживайте значок приложения iLinux, чтобы увидеть до **4** быстрых действий. Выберите, какие действия будут отображаться в **Настройки → Ярлыки главного экрана**. Доступно семь вариантов: **Поиск**, **Ежедневный тест**, **Избранное**, **Книга с неправильными ответами**, **Категории**, **Отправить отзыв** и **Оценить приложение**. Вы можете изменить порядок и восстановить настройки по умолчанию на том же экране.

### Как использовать iLinux с приложением «Ярлыки»?

iLinux поддерживает схему URL `ilinux://`. Используйте действие **Открыть URL-адреса** в приложении «Быстрые команды». Примеры:

- `ilinux://command?name=grep` — открывает команду Linux `grep` (`cmd=` тоже работает)
- `ilinux://command?cmd=dir&platform=cmd` — открывает команду CMD `dir`
- `ilinux://command?cmd=Get-ChildItem&platform=powershell` — открывает команду PowerShell.
- `ilinux://quiz` — открывает вкладку «Ежедневная викторина».
- `ilinux://favorites` — открывает список избранного.
- `ilinux://wrong` или `ilinux://mistakes` — открывает книгу неправильных ответов.

**Параметр платформы:** `platform=linux` (по умолчанию), `cmd` (псевдонимы: `batch`, `bat`) или `powershell` (псевдонимы: `ps`, `pwsh`). Опустите для команд Linux.

Примечание. **Поиск** и **Категории** доступны в качестве быстрых действий на главном экране, но не регистрируются как универсальные узлы глубоких ссылок. См. полную версию [Справочник по схеме URL](../url-scheme).

### Как поделиться командой?

На любой странице сведений о команде нажмите **Поделиться** на панели инструментов. Вы можете экспортировать команду в виде **файла Markdown** или создать **карточку общего доступа в стиле PNG** (с QR-кодом App Store) для отправки через системный лист обмена. При сохранении изображений в фотографиях может потребоваться доступ к библиотеке фотографий.

### Как изменить цвет темы?

Откройте **Настройки → Тема**. Прокрутите список из 15 встроенных предустановок цвета или коснитесь строки **Пользовательский цвет**, чтобы выбрать любой цвет с помощью системной палитры цветов. Цвет акцента, градиенты и виджет зеркально обновляются немедленно.

### Могу ли я изменить значок приложения?

Да. Перейдите в **Настройки → Значок приложения** и выберите один из **6 значков** (по умолчанию плюс 5 альтернативных). Настройка применяется мгновенно без перезапуска приложения.

### Цвет виджета не соответствует моей теме. Как это исправить?

Виджеты синхронизируют цвет своей темы через группу приложений, общую для основного приложения и расширения виджета. Если виджет выглядит устаревшим:

1. Откройте iLinux один раз — это приведет к обновлению данных группы приложений.
2. Если виджет по-прежнему не обновляется, нажмите и удерживайте виджет и нажмите **Редактировать виджет** (или удалите и снова добавьте его), чтобы вызвать перезагрузку временной шкалы.

Убедитесь, что расширение **iLinux Widget** и основное приложение обновлены (одна и та же версия).

### Поддерживает ли iLinux iPad?

Да. iLinux изначально работает на iPad с адаптивными макетами. Режим сетки поддерживает до **8 столбцов**. Виджеты, альтернативные значки, ярлыки главного экрана и тактильные ощущения полностью поддерживаются на iPad.

### Как изменить язык на Mac?

В приложении **выбор языка** находится в разделе **Настройки → Язык** на **iPhone и iPad**. На **Mac** языковые настройки обычно передаются посредством **синхронизации iCloud** с другого устройства или следуют вашим сохраненным предпочтениям/языку системы при первом запуске. Включите синхронизацию iCloud, чтобы синхронизировать язык на всех устройствах.

### Все еще нужна помощь?

Свяжитесь с нами по адресу [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) или воспользуйтесь функцией **Настройки → Отправить отзыв** в приложении. Обычно мы отвечаем в течение 48 часов.

</section>
<section lang="th" markdown="1">

### iLinux จำเป็นต้องมีบัญชีหรือการเชื่อมต่ออินเทอร์เน็ตหรือไม่?

ไม่ iLinux ทำงานแบบออฟไลน์ทั้งหมดสำหรับไลบรารีคำสั่ง ข้อมูลคำสั่งทั้งหมด (สรุป JSON และเอกสารประกอบ Markdown) รวมอยู่ในแอป ไม่จำเป็นต้องลงทะเบียนเพื่อเรียกดู อ่านเอกสาร หรือทำแบบทดสอบ ตัวเลือก **การซิงค์ iCloud** จะใช้ Apple ID ของคุณเพื่อจัดเรียงรายการโปรดและความคืบหน้าในอุปกรณ์ต่างๆ โดยจะไม่อัปโหลดเนื้อหาคำสั่ง

### iLinux รองรับ Mac หรือไม่

ใช่. iLinux เป็น **แอป macOS ดั้งเดิม** (macOS **13.0+** ไม่ใช่ Mac Catalyst) ที่มี **เค้าโครงเดสก์ท็อปแถบด้านข้าง** หน้าต่างที่ปรับขนาดได้ และแป้นพิมพ์ลัดแบบขยาย (**⌘,**, **⌘[**, **Esc**, **⌘←/→**, ปุ่มทดสอบ **1–4** / **⌘R** / **Return**) คุณสมบัติหลักทั้งหมด — ไลบรารีเชลล์สามไลบรารี เทียบเท่า แบบทดสอบ ลิงก์ในรายละเอียด และธีม — ใช้งานได้บน Mac

**ไม่มีใน Mac:** วิดเจ็ตบนหน้าจอหลัก การดำเนินการด่วนบนหน้าจอหลัก และไอคอนแอปสำรองมีเฉพาะใน **iPhone/iPad เท่านั้น** กำหนดค่าวิดเจ็ตบน iOS Mac แสดงการแจ้งเตือนภายในแอพ

### การซิงค์ iCloud ทำงานอย่างไร

เมื่อลงชื่อเข้าใช้ **iCloud** ด้วย Apple ID เดียวกัน ให้เปิดใช้งาน **iCloud Sync** ใน **การตั้งค่า → สถิติการเรียนรู้** iLinux ซิงค์ **รายการโปรด**, **ความคืบหน้าของแบบทดสอบ**, **ธีม** และ **การตั้งค่าการแสดงผล** (ภาษา แพลตฟอร์มเชลล์ ขอบเขตรายการโปรด รายการ/ตาราง) ผ่าน **iPhone, iPad และ Mac** ผ่านพื้นที่จัดเก็บคีย์-ค่าของ iCloud ความขัดแย้งจะผสานโดยอัตโนมัติ (เช่น การรวมรายการโปรด) คุณสามารถ **ปิดการซิงค์บนอุปกรณ์เครื่องหนึ่ง** ได้โดยไม่กระทบต่ออุปกรณ์อื่นๆ ไลบรารีคำสั่งยังคงออฟไลน์โดยสมบูรณ์ ซิงค์ความคืบหน้าส่วนตัวของคุณเท่านั้น

### iLinux รันคำสั่งบนเทอร์มินัล Linux จริงหรือไม่

ไม่ iLinux เป็น **เครื่องมืออ้างอิงและการเรียนรู้เท่านั้น** ไม่มีเชลล์ ไคลเอ็นต์ SSH หรือสภาพแวดล้อมการดำเนินการระยะไกล คำสั่งได้รับการบันทึกไว้เพื่อการศึกษา — คุณฝึกฝนคำสั่งเหล่านั้นบนเครื่อง Linux, Windows PC, เซิร์ฟเวอร์ หรืออินสแตนซ์คลาวด์ของคุณเอง

### iLinux รองรับแพลตฟอร์มเชลล์ใดบ้าง

iLinux จัดส่งไลบรารีคำสั่งออฟไลน์สามไลบรารีต่อภาษาของเนื้อหา:

- **Linux** — 1,050 คำสั่งใน 14 หมวดหมู่
- **Windows CMD / Batch** — 300 คำสั่งใน 10 หมวดหมู่
- **PowerShell** — 300 คำสั่งใน 10 หมวดหมู่

**ทั้งหมดมากกว่า 1,650 คำสั่ง** ต่อภาษา (อังกฤษ, จีนตัวย่อ, จีนตัวเต็ม) สลับไลบรารีจากเมนูเชลล์ของแถบเครื่องมือบน **คำสั่ง**, **หมวดหมู่** หรือ **แบบทดสอบรายวัน**

### ฉันจะสลับระหว่าง Linux, CMD และ PowerShell ได้อย่างไร

แตะเมนู **แพลตฟอร์ม Shell** (ไอคอนเทอร์มินัล) ในแถบเครื่องมือบนแท็บคำสั่ง หมวดหมู่ หรือแบบทดสอบรายวัน การเลือกของคุณยังคงอยู่และขอบเขตการค้นหา หมวดหมู่ คำถามแบบทดสอบ และสถิติการเรียนรู้สำหรับแพลตฟอร์มนั้น

ใน **การตั้งค่า → การเข้าถึงด่วนที่บ้าน** คุณยังสามารถตั้งค่าแพลตฟอร์มเชลล์เริ่มต้น **ขอบเขตรายการโปรด** (ทุกแพลตฟอร์มเทียบกับแพลตฟอร์มปัจจุบันเท่านั้น) และ **ไลบรารีคำสั่งวิดเจ็ต** สำหรับคำสั่งรายวันและวิดเจ็ต Spotlight หมวดหมู่

### คำสั่งที่เทียบเท่าข้ามแพลตฟอร์มคืออะไร?

คำสั่งลิงก์ **กลุ่มที่เทียบเท่ามากกว่า 100 กลุ่ม** ที่ทำงานเดียวกันบน Linux, CMD และ PowerShell — เช่น `ls`, `dir` และ `Get-ChildItem` บนหน้ารายละเอียดคำสั่ง แถบ **เทียบเท่า** จะแสดงรายการที่เกี่ยวข้อง แตะอันใดอันหนึ่งเพื่อข้ามไปยังเอกสารประกอบของแพลตฟอร์มนั้นทันที

### รวมกี่คำสั่ง?

ภาษาของเนื้อหาแต่ละภาษาประกอบด้วยคำสั่ง **1650+** ในไลบรารีเชลล์สามไลบรารี:

| แพลตฟอร์ม | คำสั่ง | หมวดหมู่ |
|----------|----------|------------|
| ลินุกซ์ | 1050 | 14 |
| CMD / แบทช์ | 300 | 10 |
| พาวเวอร์เชลล์ | 300 | 10 |

เอกสารทั้งหมดมีให้บริการแบบออฟไลน์เป็นภาษาอังกฤษ จีนตัวย่อ และจีนตัวเต็ม

### ฉันจะค้นหาคำสั่งได้อย่างไร?

แตะไอคอนแว่นขยายบนแท็บคำสั่ง หรือกด **⌘F** บนแป้นพิมพ์ฮาร์ดแวร์ พิมพ์ชื่อคำสั่ง คำสำคัญ หรือส่วนหนึ่งของคำอธิบาย ผลลัพธ์จะอัปเดตแบบเรียลไทม์ในขณะที่คุณพิมพ์

### ฉันจะสลับระหว่างมุมมองรายการและตารางได้อย่างไร

บนแท็บ **คำสั่ง** หรือ **หมวดหมู่** เปิดเมนูตัวกรองแถบเครื่องมือ (ไอคอนช่องทาง) ใต้ **โหมดดู** ให้เลือก **รายการ** หรือ **ตาราง** ในโหมดตาราง ให้ใช้ปุ่ม **+ / −** เพื่อตั้งค่าคอลัมน์ต่อแถว (**1–6 บน iPhone**, **1–8 บน iPad และ Mac**) คุณยังสามารถเปลี่ยนค่าเริ่มต้นได้ใน **การตั้งค่า → การแสดงผล**

### ฉันจะติดตามความก้าวหน้าในการเรียนรู้ของฉันได้อย่างไร?

เปิดหน้ารายละเอียดของคำสั่งและตั้งค่าสถานะเป็น **ไม่ได้เรียนรู้**, **เรียนรู้แล้ว** หรือ **เชี่ยวชาญ** ในมุมมองรายการ ให้ปัดแถวเพื่อดูสถานะด่วนและการกระทำที่ชื่นชอบ ในมุมมองตาราง ให้ใช้ปุ่มรูปดาวเป็นรายการโปรดและใช้เมนูบริบทเพื่อดูสถานะ กรองเป็น **ยังไม่ได้เรียนรู้** จากเมนูแถบเครื่องมือเพื่อเน้นไปที่คำสั่งที่คุณยังไม่ได้ศึกษา

### มีภาษาอะไรบ้าง?

iLinux รองรับสามภาษาสำหรับทั้งอินเทอร์เฟซแอพและเอกสารคำสั่ง:

- **ภาษาอังกฤษ**
- **จีนตัวย่อ (简体中文)**
- **ภาษาจีนตัวเต็ม (繁體中文)**

คุณยังเลือก **ระบบ** เพื่อติดตามภาษาของอุปกรณ์ของคุณได้ด้วย เปลี่ยนภาษาใน **การตั้งค่า → ภาษา** แอปทั้งหมดรวมถึงวิดเจ็ตจะอัปเดตทันที

### แบบทดสอบรายวันทำงานอย่างไร

ในแต่ละวัน คำถามชุดใหม่จะถูกสร้างขึ้นโดยใช้ข้อมูลเริ่มต้นตามวันที่ **กำหนดขอบเขตไว้ที่แพลตฟอร์มเชลล์ที่ใช้งานอยู่** (Linux, CMD หรือ PowerShell) ทุกคนที่ใช้ iLinux ในวันเดียวกันจะได้รับชุดคำถามพื้นฐานแบบเดียวกันสำหรับแพลตฟอร์มนั้น คำถามสองประเภทปรากฏขึ้น:

- **สรุปการแข่งขัน** — คุณเห็นคำอธิบายสั้นๆ และต้องเลือกชื่อคำสั่งที่ถูกต้อง
- **Match Option Meaning** — คุณเห็นคำอธิบายของแฟล็ก (เช่น `-r: recursive`) และต้องระบุว่าเป็นของคำสั่งใด

แตะ **ปุ่มรีเฟรช** (ลูกศรวงกลม) ในแถบเครื่องมือเพื่อรับชุดการสุ่มที่แตกต่างกันได้ตลอดเวลา **วันต่อเนื่องที่สมบูรณ์แบบ** (วันต่อเนื่องกันด้วยคะแนนสมบูรณ์แบบ) จะถูกติดตามในแต่ละแพลตฟอร์ม และแสดงในหน้าจอตอบคำถามและวิดเจ็ต Quiz Glance แฟล็กความช่วยเหลือทั่วไป เช่น `-h` และ `--version` จะถูกแยกออก เพื่อให้คำถามไม่คลุมเครือ

### คำตอบที่ผิดของฉันไม่ได้รับการบันทึก ฉันควรทำอย่างไร?

คำตอบที่ผิดจะถูกบันทึกโดยอัตโนมัติหลังจากที่คุณเสร็จสิ้นเซสชั่นแบบทดสอบ ตรวจสอบให้แน่ใจว่าคุณทำแบบทดสอบครบทุกรอบแล้ว (ตอบคำถามทุกข้อและไปที่หน้าจอผลลัพธ์) เซสชันที่เสร็จสมบูรณ์บางส่วนจะไม่ถูกบันทึก

คุณสามารถตรวจสอบคำตอบที่ผิดที่บันทึกไว้ทั้งหมดได้ใน **การตั้งค่า → หนังสือคำตอบที่ผิด**

### ฉันจะเพิ่มคำสั่งไปยังรายการโปรดได้อย่างไร

เปิดหน้ารายละเอียดของคำสั่งใดๆ แล้วแตะ **ไอคอนรูปดาว** ที่มุมขวาบน ใน **มุมมองตาราง** ให้แตะดาวบนเซลล์คำสั่งโดยตรง เข้าถึงรายการโปรดทั้งหมดจาก **การตั้งค่า → รายการโปรด** หรือตัวกรองด่วน **รายการโปรด**

### ฉันจะตั้งค่าวิดเจ็ตหน้าจอหลักได้อย่างไร?

1. กดพื้นที่ว่างบนหน้าจอหลักค้างไว้แล้วแตะปุ่ม **+** ที่มุมด้านบน
2. ค้นหา **iLinux** ในแกลเลอรีวิดเจ็ต
3. เลือกสไตล์วิดเจ็ตแล้วแตะ **เพิ่มวิดเจ็ต**

**คำแนะนำวิดเจ็ต** ทีละขั้นตอนมีอยู่ใน **การตั้งค่า → คำแนะนำวิดเจ็ต** หากต้องการให้พื้นหลังวิดเจ็ตเป็นไปตามการไล่ระดับธีมแอปของคุณ ให้เปิดใช้งานตัวเลือกใน **การตั้งค่า → วิดเจ็ต**

**ไลบรารีคำสั่งวิดเจ็ต:** ใน **การตั้งค่า → วิดเจ็ต** ให้เลือกไลบรารีเชลล์ (Linux / CMD / PowerShell) ที่จะป้อนวิดเจ็ต Daily Command และ Category Spotlight สิ่งนี้ไม่ขึ้นอยู่กับสวิตช์เชลล์ในแอป — มีประโยชน์หากคุณต้องการให้วิดเจ็ตแสดงคำสั่ง Windows ในขณะที่เรียกดู Linux ภายในแอป

### วิดเจ็ต Daily Command จะแสดงคำสั่งเดียวกันทุกวัน ฉันจะเปลี่ยนมันได้อย่างไร?

แตะปุ่ม **ลูกศรวงกลม (สุ่ม)** ที่มุมขวาบนของวิดเจ็ต Daily Command เพื่อโหลดคำสั่งอื่นทันที ฟีเจอร์นี้ต้องใช้ **iOS 17 ขึ้นไป**

บน iOS 16 วิดเจ็ต Daily Command จะแสดงคำสั่งคงที่ในแต่ละวันและไม่มีปุ่มสับเปลี่ยน

### ฉันจะกำหนดค่าการดำเนินการด่วนบนหน้าจอหลักได้อย่างไร

กดไอคอนแอป iLinux ค้างไว้เพื่อดูการดำเนินการด่วนสูงสุด **4** เลือกการกระทำที่จะปรากฏใน **การตั้งค่า → ทางลัดหน้าจอหลัก** มีเจ็ดตัวเลือกให้เลือก: **ค้นหา**, **แบบทดสอบรายวัน**, **รายการโปรด**, **สมุดคำตอบที่ไม่ถูกต้อง**, **หมวดหมู่**, **ส่งคำติชม** และ **ให้คะแนนแอป** คุณสามารถเรียงลำดับใหม่และรีเซ็ตเป็นค่าเริ่มต้นได้จากหน้าจอเดียวกัน

### ฉันจะใช้ iLinux กับแอปทางลัดได้อย่างไร

iLinux รองรับรูปแบบ URL `ilinux://` ใช้การกระทำ **เปิด URL** ในแอพคำสั่งลัด ตัวอย่าง:

- `ilinux://command?name=grep` — เปิดคำสั่ง Linux `grep` (`cmd=` ก็ใช้ได้เช่นกัน)
- `ilinux://command?cmd=dir&platform=cmd` — เปิดคำสั่ง CMD `dir`
- `ilinux://command?cmd=Get-ChildItem&platform=powershell` — เปิดคำสั่ง PowerShell
- `ilinux://quiz` — เปิดแท็บ Daily Quiz
- `ilinux://favorites` — เปิดรายการโปรดของคุณ
- `ilinux://wrong` หรือ `ilinux://mistakes` — เปิดหนังสือคำตอบที่ไม่ถูกต้อง

**พารามิเตอร์แพลตฟอร์ม:** `platform=linux` (ค่าเริ่มต้น), `cmd` (นามแฝง: `batch`, `bat`) หรือ `powershell` (นามแฝง: `ps`, `pwsh`) ละเว้นสำหรับคำสั่ง Linux

Note: **Search** and **Categories** are available as Home Screen quick actions but are not registered as universal deep-link hosts. See the full [URL Scheme Reference](../url-scheme).

### ฉันจะแชร์คำสั่งได้อย่างไร

บนหน้ารายละเอียดคำสั่งใดๆ ให้แตะ **แชร์** ในแถบเครื่องมือ คุณสามารถส่งออกคำสั่งเป็น **ไฟล์ Markdown** หรือสร้าง **การ์ดแชร์ PNG ที่มีสไตล์** (พร้อมโค้ด QR ของ App Store) เพื่อส่งผ่าน Share Sheet ของระบบ การบันทึกรูปภาพลงใน Photos อาจร้องขอการเข้าถึงไลบรารีรูปภาพ

### ฉันจะเปลี่ยนสีของธีมได้อย่างไร?

ไปที่ **การตั้งค่า → ธีม** เลื่อนดูค่าสีที่กำหนดไว้ล่วงหน้า 15 สีหรือแตะแถว **สีที่กำหนดเอง** เพื่อเลือกสีใดก็ได้โดยใช้เครื่องมือเลือกสีของระบบ สีเฉพาะจุด การไล่ระดับสี และกระจกวิดเจ็ตทั้งหมดจะอัปเดตทันที

### ฉันสามารถเปลี่ยนไอคอนแอพได้หรือไม่?

ใช่. ไปที่ **การตั้งค่า → ไอคอนแอป** เพื่อเลือกจาก **6 ไอคอน** (ค่าเริ่มต้นบวกอีก 5 รายการ) การตั้งค่าจะมีผลทันทีโดยไม่ต้องเปิดแอปอีกครั้ง

### สีของวิดเจ็ตไม่ตรงกับธีมของฉัน ฉันจะแก้ไขได้อย่างไร?

วิดเจ็ตซิงค์สีของธีมผ่านกลุ่มแอปที่แชร์ระหว่างแอปหลักและส่วนขยายวิดเจ็ต หากวิดเจ็ตดูล้าสมัย:

1. เปิด iLinux หนึ่งครั้ง - เป็นการบังคับให้ข้อมูลกลุ่มแอปรีเฟรช
2. หากวิดเจ็ตยังไม่อัปเดต ให้กดวิดเจ็ตค้างไว้แล้วแตะ **แก้ไขวิดเจ็ต** (หรือลบและเพิ่มใหม่) เพื่อทริกเกอร์การโหลดไทม์ไลน์ซ้ำ

ตรวจสอบให้แน่ใจว่าส่วนขยาย **iLinux Widget** และแอปหลักเป็นเวอร์ชันล่าสุด (เวอร์ชันเดียวกัน)

### iLinux รองรับ iPad หรือไม่

ใช่. iLinux ทำงานบน iPad ด้วยรูปแบบที่ปรับเปลี่ยนได้ โหมดตารางรองรับสูงสุด **8 คอลัมน์** วิดเจ็ต ไอคอนสำรอง ปุ่มลัดบนหน้าจอโฮม และระบบสัมผัสต่างๆ ได้รับการรองรับบน iPad อย่างสมบูรณ์

### ฉันจะเปลี่ยนภาษาบน Mac ได้อย่างไร

**เครื่องมือเลือกภาษา** ในแอปอยู่ใน **การตั้งค่า → ภาษา** บน **iPhone และ iPad** บน **Mac** โดยทั่วไปการตั้งค่าภาษาจะมาถึงผ่าน **การซิงค์ iCloud** จากอุปกรณ์อื่น หรือติดตามการตั้งค่า / ภาษาของระบบที่บันทึกไว้ในการเปิดตัวครั้งแรก เปิดใช้งานการซิงค์ iCloud เพื่อให้ภาษาสอดคล้องกับอุปกรณ์ต่างๆ

### ยังต้องการความช่วยเหลืออยู่ใช่ไหม?

ติดต่อเราที่ [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) หรือใช้ตัวเลือก **การตั้งค่า → ส่งคำติชม** ในแอป โดยปกติเราจะตอบกลับภายใน 48 ชั่วโมง

</section>
<section lang="de" markdown="1">

### Benötigt iLinux ein Konto oder eine Internetverbindung?

Nein. iLinux funktioniert für Befehlsbibliotheken vollständig offline. Alle Befehlsdaten (JSON-Zusammenfassungen und Markdown-Dokumentation) sind in der App gebündelt. Es ist keine Anmeldung erforderlich, um die Dokumentation zu durchsuchen, zu lesen oder an Tests teilzunehmen. Die optionale **iCloud-Synchronisierung** verwendet Ihre Apple-ID, um Favoriten und Fortschritte geräteübergreifend abzugleichen – es werden keine Befehlsinhalte hochgeladen.

### Unterstützt iLinux Mac?

Ja. iLinux ist eine **native macOS-App** (macOS **13.0+**, nicht Mac Catalyst) mit einem **Seitenleisten-Desktop-Layout**, einem skalierbaren Fenster und erweiterten Tastaturkürzeln (**⌘,**, **⌘[**, **Esc**, **⌘←/→**, Quiztasten **1–4** / **⌘R** / **Return**). Alle Kernfunktionen – drei Shell-Bibliotheken, Äquivalente, Quiz, Deep Links und Themes – funktionieren auf dem Mac.

**Nicht auf Mac:** Startbildschirm-Widgets, Startbildschirm-Schnellaktionen und alternative App-Symbole sind **nur für iPhone/iPad**. Widgets unter iOS konfigurieren; Mac zeigt einen In-App-Hinweis an.

### Wie funktioniert die iCloud-Synchronisierung?

Wenn Sie mit derselben Apple-ID bei **iCloud** angemeldet sind, aktivieren Sie **iCloud Sync** unter **Einstellungen → Lernstatistiken**. iLinux synchronisiert **Favoriten**, **Quizfortschritt**, **Thema** und **Anzeigeeinstellungen** (Sprache, Shell-Plattform, Favoritenbereich, Liste/Raster) über **iPhone, iPad und Mac** über iCloud Key-Value Storage. Konflikte werden automatisch zusammengeführt (z. B. Favoritenzusammenführung). Sie können die **Synchronisierung auf einem Gerät deaktivieren**, ohne dass dies Auswirkungen auf andere hat. Befehlsbibliotheken bleiben vollständig offline; Nur Ihr persönlicher Fortschritt wird synchronisiert.

### Führt iLinux Befehle auf einem echten Linux-Terminal aus?

Nein. iLinux ist nur ein **Referenz- und Lerntool**. Es stellt keine Shell, keinen SSH-Client oder keine Remote-Ausführungsumgebung bereit. Befehle werden zum Lernen dokumentiert – Sie üben sie auf Ihrem eigenen Linux-Rechner, Windows-PC, Server oder Cloud-Instanz.

### Welche Shell-Plattformen unterstützt iLinux?

iLinux liefert drei Offline-Befehlsbibliotheken pro Inhaltssprache:

- **Linux** – 1050 Befehle in 14 Kategorien
- **Windows CMD / Batch** – 300 Befehle in 10 Kategorien
- **PowerShell** – 300 Befehle in 10 Kategorien

**insgesamt über 1650 Befehle** pro Sprache (Englisch, vereinfachtes Chinesisch, traditionelles Chinesisch). Wechseln Sie zwischen den Bibliotheken im Shell-Menü der Symbolleiste auf **Befehle**, **Kategorien** oder **Tägliches Quiz**.

### Wie wechsle ich zwischen Linux, CMD und PowerShell?

Tippen Sie in der Symbolleiste auf der Registerkarte „Befehle“, „Kategorien“ oder „Tägliches Quiz“ auf das Menü **Shell-Plattform** (Terminalsymbol). Ihre Auswahl bleibt bestehen und umfasst die Suche, Kategorien, Quizfragen und Lernstatistiken für diese Plattform.

Unter **Einstellungen → Home-Schnellzugriff** können Sie auch eine Standard-Shell-Plattform, einen **Favoritenbereich** (alle Plattformen vs. nur aktuelle Plattform) und die **Widget-Befehlsbibliothek** für Daily Command- und Category Spotlight-Widgets festlegen.

### Was sind plattformübergreifende äquivalente Befehle?

**100+ equivalent groups** link commands that accomplish the same task across Linux, CMD and PowerShell — for example `ls`, `dir` and `Get-ChildItem`. On a command detail page, the **Equivalents** bar shows related entries; tap one to jump to that platform's documentation instantly.

### Wie viele Befehle sind enthalten?

Jede Inhaltssprache umfasst **1650+** Befehle in drei Shell-Bibliotheken:

| Plattform | Befehle | Kategorien |
|----------|----------|------------|
| Linux | 1050 | 14 |
| CMD / Stapel | 300 | 10 |
| PowerShell | 300 | 10 |

Die gesamte Dokumentation ist offline in Englisch, vereinfachtem Chinesisch und traditionellem Chinesisch verfügbar.

### Wie suche ich nach einem Befehl?

Tippen Sie auf der Registerkarte „Befehle“ auf das Lupensymbol oder drücken Sie **⌘F** auf einer Hardwaretastatur. Geben Sie einen Befehlsnamen, ein Schlüsselwort oder einen Teil einer Beschreibung ein. Die Ergebnisse werden während der Eingabe in Echtzeit aktualisiert.

### Wie wechsle ich zwischen Listen- und Rasteransicht?

Öffnen Sie auf der Registerkarte **Befehle** oder **Kategorien** das Filtermenü der Symbolleiste (Trichtersymbol). Wählen Sie unter **Ansichtsmodus** die Option **Liste** oder **Raster**. Verwenden Sie im Rastermodus die Tasten **+ / −**, um Spalten pro Zeile festzulegen (**1–6 auf dem iPhone**, **1–8 auf iPad und Mac**). Sie können die Standardeinstellung auch unter **Einstellungen → Anzeige** ändern.

### Wie verfolge ich meinen Lernfortschritt?

Open a command's detail page and set its status to **Unlearned**, **Learned** or **Mastered**. In list view, swipe a row for quick status and favourite actions. In grid view, use the star button to favourite and the context menu for status. Filter to **Unlearned** from the toolbar menu to focus on commands you haven't studied yet.

### Welche Sprachen sind verfügbar?

iLinux unterstützt drei Sprachen sowohl für die App-Oberfläche als auch für die Befehlsdokumentation:

- **Englisch**
- **Vereinfachtes Chinesisch (简体中文)**
- **Traditionelles Chinesisch (繁體中文)**

Sie können auch **System** auswählen, um dem Gebietsschema Ihres Geräts zu folgen. Ändern Sie die Sprache unter **Einstellungen → Sprache**. Die gesamte App – einschließlich Widgets – wird sofort aktualisiert.

### Wie funktioniert das tägliche Quiz?

Jeden Tag wird ein neuer Satz von Quizfragen mithilfe eines datumsbasierten Startwerts generiert, der **auf die aktive Shell-Plattform beschränkt ist** (Linux, CMD oder PowerShell). Jeder, der iLinux am selben Tag nutzt, erhält das gleiche Basis-Quizset für diese Plattform. Es erscheinen zwei Fragetypen:

- **Übereinstimmungszusammenfassung** – Sie sehen eine kurze Beschreibung und müssen den richtigen Befehlsnamen auswählen.
- **Match Option Meaning** — you see a flag's description (e.g. `-r: recursive`) and must identify which command it belongs to.

Tap the **refresh button** (circular arrow) in the toolbar to get a different randomised set at any time. **Perfect streak** days (consecutive days with a perfect score) are tracked per platform and shown in the quiz screen and Quiz Glance widget. Generic help flags like `-h` and `--version` are excluded to keep questions unambiguous.

### Meine falschen Antworten werden nicht gespeichert. Was soll ich tun?

Falsche Antworten werden automatisch gespeichert, nachdem Sie eine Quizsitzung abgeschlossen haben. Stellen Sie sicher, dass Sie die gesamte Quizrunde abgeschlossen haben (beantworten Sie alle Fragen und gelangen Sie zum Ergebnisbildschirm). Teilweise abgeschlossene Sitzungen werden nicht gespeichert.

Sie können alle gespeicherten falschen Antworten unter **Einstellungen → Falsche Antworten** überprüfen.

### Wie füge ich einen Befehl zu den Favoriten hinzu?

Öffnen Sie die Detailseite eines beliebigen Befehls und tippen Sie auf das **Sternsymbol** in der oberen rechten Ecke. Tippen Sie in der **Rasteransicht** direkt auf den Stern in der Befehlszelle. Greifen Sie auf alle Favoriten über **Einstellungen → Favoriten** oder den Schnellfilter **Favoriten** zu.

### Wie richte ich Startbildschirm-Widgets ein?

1. Long-press an empty area of your Home Screen and tap the **+** button in the top corner.
2. Suchen Sie in der Widget-Galerie nach **iLinux**.
3. Wählen Sie einen Widget-Stil und tippen Sie auf **Widget hinzufügen**.

Eine schrittweise **Widget-Anleitung** ist auch unter **Einstellungen → Widget-Anleitung** verfügbar. Damit die Widget-Hintergründe dem Farbverlauf Ihres App-Designs folgen, aktivieren Sie die Option unter **Einstellungen → Widgets**.

**Widget-Befehlsbibliothek:** Wählen Sie unter **Einstellungen → Widgets** aus, welche Shell-Bibliothek (Linux / CMD / PowerShell) die Daily Command- und Category Spotlight-Widgets speist. Dies ist unabhängig vom In-App-Shell-Schalter – nützlich, wenn Sie möchten, dass Widgets Windows-Befehle anzeigen, während Sie in der App Linux durchsuchen.

### Das Widget „Täglicher Befehl“ zeigt jeden Tag denselben Befehl an. Wie ändere ich es?

Tippen Sie auf die **kreisförmige Pfeilschaltfläche (Shuffle)** in der oberen rechten Ecke des Daily Command-Widgets, um sofort einen anderen Befehl zu laden. Für diese Funktion ist **iOS 17 oder höher** erforderlich.

Unter iOS 16 zeigt das Widget „Täglicher Befehl“ einen festen Befehl für jeden Tag an und enthält keine Zufallsschaltfläche.

### Wie konfiguriere ich Schnellaktionen auf dem Startbildschirm?

Drücken Sie lange auf das iLinux-App-Symbol, um bis zu **4** Schnellaktionen anzuzeigen. Wählen Sie aus, welche Aktionen unter **Einstellungen → Startbildschirm-Verknüpfungen** angezeigt werden. Es stehen sieben Optionen zur Verfügung: **Suche**, **Tägliches Quiz**, **Favoriten**, **Buch mit falschen Antworten**, **Kategorien**, **Feedback senden** und **App bewerten**. Sie können auf demselben Bildschirm die Reihenfolge ändern und auf die Standardeinstellungen zurücksetzen.

### Wie verwende ich iLinux mit der Shortcuts-App?

iLinux supports the `ilinux://` URL scheme. Use an **Open URLs** action in the Shortcuts app. Examples:

- `ilinux://command?name=grep` – öffnet den Linux-Befehl `grep` (`cmd=` funktioniert auch)
- `ilinux://command?cmd=dir&platform=cmd` — opens CMD command `dir`
- `ilinux://command?cmd=Get-ChildItem&platform=powershell` — opens PowerShell command
- `ilinux://quiz` — opens the Daily Quiz tab
- `ilinux://favorites` — opens your Favourites list
- `ilinux://wrong` or `ilinux://mistakes` — opens the Wrong Answer Book

**Platform parameter:** `platform=linux` (default), `cmd` (aliases: `batch`, `bat`), or `powershell` (aliases: `ps`, `pwsh`). Omit for Linux commands.

Hinweis: **Suche** und **Kategorien** sind als Schnellaktionen auf dem Startbildschirm verfügbar, aber nicht als universelle Deep-Link-Hosts registriert. Sehen Sie sich die vollständige [URL-Schema-Referenz](../url-scheme) an.

### Wie teile ich einen Befehl?

Tippen Sie auf einer beliebigen Befehlsdetailseite in der Symbolleiste auf **Teilen**. Sie können den Befehl als **Markdown-Datei** exportieren oder eine **im PNG-Format gestaltete Freigabekarte** (mit App Store-QR-Code) erstellen, um sie über das Freigabeblatt des Systems zu senden. Beim Speichern von Bildern in Fotos kann der Zugriff auf die Fotobibliothek erforderlich sein.

### Wie ändere ich die Designfarbe?

Gehen Sie zu **Einstellungen → Thema**. Scrollen Sie durch 15 integrierte Farbvoreinstellungen oder tippen Sie auf die Zeile **Benutzerdefinierte Farbe**, um mit der Systemfarbauswahl eine beliebige Farbe auszuwählen. Die Akzentfarbe, die Farbverläufe und der Widget-Spiegel werden alle sofort aktualisiert.

### Kann ich das App-Symbol ändern?

Ja. Gehen Sie zu **Einstellungen → App-Symbol**, um aus **6 Symbolen** auszuwählen (Standard plus 5 Alternativen). Die Einstellung wird sofort übernommen, ohne dass die App neu gestartet werden muss.

### Die Widget-Farbe passt nicht zu meinem Thema. Wie kann ich das Problem beheben?

Widgets synchronisieren ihre Designfarbe über eine App-Gruppe, die von der Haupt-App und der Widget-Erweiterung gemeinsam genutzt wird. Wenn das Widget veraltet aussieht:

1. Öffnen Sie iLinux einmal – dies erzwingt eine Aktualisierung der App-Gruppendaten.
2. Wenn das Widget immer noch nicht aktualisiert wird, drücken Sie lange auf das Widget und tippen Sie auf **Widget bearbeiten** (oder entfernen Sie es und fügen Sie es erneut hinzu), um ein Neuladen der Zeitleiste auszulösen.

Stellen Sie sicher, dass die **iLinux Widget**-Erweiterung und die Haupt-App beide auf dem neuesten Stand sind (gleiche Version).

### Unterstützt iLinux das iPad?

Ja. iLinux läuft nativ auf dem iPad mit adaptiven Layouts. Der Rastermodus unterstützt bis zu **8 Spalten**. Widgets, alternative Symbole, Startbildschirm-Verknüpfungen und Haptik werden auf dem iPad vollständig unterstützt.

### Wie ändere ich die Sprache auf dem Mac?

Die In-App-**Sprachauswahl** befindet sich unter **Einstellungen → Sprache** auf **iPhone und iPad**. Auf **Mac** erfolgt die Spracheinstellung normalerweise über **iCloud-Synchronisierung** von einem anderen Gerät oder folgt beim ersten Start Ihren gespeicherten Einstellungen/Systemgebietsschemas. Aktivieren Sie die iCloud-Synchronisierung, um die Sprache auf allen Geräten anzugleichen.

### Brauchen Sie noch Hilfe?

Kontaktieren Sie uns unter [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) oder nutzen Sie die In-App-Option **Einstellungen → Feedback senden**. Wir antworten in der Regel innerhalb von 48 Stunden.

</section>
<section lang="fr" markdown="1">

### iLinux nécessite-t-il un compte ou une connexion Internet ?

Non, iLinux fonctionne entièrement hors ligne pour les bibliothèques de commandes. Toutes les données de commande (résumés JSON et documentation Markdown) sont regroupées dans l'application. Aucune inscription n'est nécessaire pour parcourir, lire la documentation ou répondre à des quiz. La **synchronisation iCloud** facultative utilise votre identifiant Apple pour aligner les favoris et la progression sur tous les appareils — elle ne télécharge pas le contenu des commandes.

### Does iLinux support Mac?

Oui. iLinux est une **application macOS native** (macOS **13.0+**, pas Mac Catalyst) avec une **disposition de bureau en barre latérale**, une fenêtre redimensionnable et des raccourcis clavier étendus (**⌘,**, **⌘[**, **Esc**, **⌘←/→**, touches de quiz **1–4** / **⌘R** / **Return**). Toutes les fonctionnalités principales (trois bibliothèques shell, équivalents, quiz, liens profonds et thèmes) fonctionnent sur Mac.

**Pas sur Mac :** Les widgets de l'écran d'accueil, les actions rapides de l'écran d'accueil et les icônes d'applications alternatives sont **iPhone/iPad uniquement**. Configurer les widgets sur iOS ; Mac affiche une notification dans l'application.

### Comment fonctionne la synchronisation iCloud ?

Une fois connecté à **iCloud** avec le même identifiant Apple, activez **iCloud Sync** dans **Paramètres → Statistiques d'apprentissage**. iLinux synchronise les **favoris**, la **progression du quiz**, le **thème** et les **préférences d'affichage** (langue, plate-forme shell, portée des favoris, liste/grille) sur **iPhone, iPad et Mac** via le stockage de valeurs-clés iCloud. Les conflits fusionnent automatiquement (par exemple union des favoris). Vous pouvez **désactiver la synchronisation sur un appareil** sans affecter les autres. Les bibliothèques de commandes restent entièrement hors ligne ; seule votre progression personnelle est synchronisée.

### iLinux exécute-t-il des commandes sur un vrai terminal Linux ?

Non. iLinux est un **outil de référence et d'apprentissage uniquement**. Il ne fournit pas de shell, de client SSH ou d'environnement d'exécution à distance. Les commandes sont documentées pour étude : vous les pratiquez sur votre propre machine Linux, PC Windows, serveur ou instance cloud.

### Quelles plates-formes shell iLinux prend-il en charge ?

iLinux propose trois bibliothèques de commandes hors ligne par langue de contenu :

- **Linux** — 1 050 commandes réparties en 14 catégories
- **Windows CMD / Batch** — 300 commandes réparties en 10 catégories
- **PowerShell** — 300 commandes réparties en 10 catégories

**Plus de 1 650 commandes au total** par langue (anglais, chinois simplifié, chinois traditionnel). Changez de bibliothèque à partir du menu Shell de la barre d'outils sur **Commandes**, **Catégories** ou **Daily Quiz**.

### Comment basculer entre Linux, CMD et PowerShell ?

Appuyez sur le menu **Plateforme Shell** (icône de terminal) dans la barre d'outils sous l'onglet Commandes, Catégories ou Quiz quotidien. Votre sélection persiste et couvre la recherche, les catégories, les questions de quiz et les statistiques d'apprentissage pour cette plate-forme.

Dans **Paramètres → Accès rapide à l'accueil**, vous pouvez également définir une plate-forme shell par défaut, une **portée des favoris** (toutes les plates-formes par rapport à la plate-forme actuelle uniquement) et la **bibliothèque de commandes de widget** pour les widgets Daily Command et Category Spotlight.

### Que sont les commandes équivalentes multiplateformes ?

**Plus de 100 groupes équivalents** lient des commandes qui accomplissent la même tâche sur Linux, CMD et PowerShell — par exemple `ls`, `dir` et `Get-ChildItem`. Sur une page de détails de commande, la barre **Équivalents** affiche les entrées associées ; appuyez sur un pour accéder instantanément à la documentation de cette plate-forme.

### Combien de commandes sont incluses ?

Chaque langage de contenu comprend **1 650+** commandes réparties dans trois bibliothèques shell :

| Plateforme | Commandes | Catégories |
|----------|----------|------------|
| Linux | 1050 | 14 |
| CMD / Batch | 300 | 10 |
| PowerShell | 300 | 10 |

Toute la documentation est disponible hors ligne en anglais, chinois simplifié et chinois traditionnel.

### Comment rechercher une commande ?

Appuyez sur l'icône en forme de loupe dans l'onglet Commandes ou appuyez sur **⌘F** sur un clavier matériel. Tapez un nom de commande, un mot-clé ou une partie d'une description. Les résultats sont mis à jour en temps réel au fur et à mesure que vous tapez.

### Comment puis-je basculer entre la vue liste et la vue grille ?

Dans l'onglet **Commandes** ou **Catégories**, ouvrez le menu de filtrage de la barre d'outils (icône en forme d'entonnoir). Sous **Mode d'affichage**, choisissez **Liste** ou **Grille**. En mode grille, utilisez les boutons **+ / −** pour définir les colonnes par ligne (**1 à 6 sur iPhone**, **1 à 8 sur iPad et Mac**). Vous pouvez également modifier la valeur par défaut dans **Paramètres → Affichage**.

### Comment puis-je suivre mes progrès d’apprentissage ?

Ouvrez la page de détails d'une commande et définissez son état sur **Non appris**, **Appris** ou **Maîtrisé**. En mode liste, faites glisser une ligne pour afficher un état rapide et des actions favorites. En mode grille, utilisez le bouton étoile pour favoris et le menu contextuel pour l'état. Filtrez sur **Non appris** dans le menu de la barre d'outils pour vous concentrer sur les commandes que vous n'avez pas encore étudiées.

### Quelles langues sont disponibles ?

iLinux prend en charge trois langues pour l'interface de l'application et la documentation des commandes :

- **English**
- **Chinois simplifié (简体中文)**
- **Chinois traditionnel (繁體中文)**

Vous pouvez également choisir **Système** pour suivre les paramètres régionaux de votre appareil. Changez la langue dans **Paramètres → Langue**. L'ensemble de l'application, y compris les widgets, est mis à jour immédiatement.

### Comment fonctionne le Quiz Quotidien ?

Chaque jour, un nouvel ensemble de questions de quiz est généré à l'aide d'une graine basée sur la date, **portée sur la plate-forme shell active** (Linux, CMD ou PowerShell). Toute personne utilisant iLinux le même jour reçoit le même jeu de quiz de base pour cette plate-forme. Deux types de questions apparaissent :

- **Résumé du match** : vous voyez une brève description et devez choisir le nom de commande correct.
- **Match Option Meaning** — you see a flag's description (e.g. `-r: recursive`) and must identify which command it belongs to.

Appuyez sur le **bouton d'actualisation** (flèche circulaire) dans la barre d'outils pour obtenir un ensemble aléatoire différent à tout moment. Les jours **de séquence parfaite** (jours consécutifs avec un score parfait) sont suivis par plateforme et affichés dans l'écran du quiz et le widget Quiz Glance. Les indicateurs d'aide génériques comme `-h` et `--version` sont exclus pour garder les questions sans ambiguïté.

### Mes mauvaises réponses ne sont pas enregistrées. Que dois-je faire?

Les mauvaises réponses sont automatiquement enregistrées une fois que vous avez terminé une session de quiz. Assurez-vous de terminer le tour de quiz complet (répondez à toutes les questions et accédez à l'écran des résultats). Les sessions partiellement terminées ne sont pas enregistrées.

Vous pouvez consulter toutes les mauvaises réponses enregistrées dans **Paramètres → Carnet de mauvaises réponses**.

### Comment ajouter une commande aux Favoris ?

Ouvrez la page de détails de n'importe quelle commande et appuyez sur l'**icône étoile** dans le coin supérieur droit. En **vue grille**, appuyez directement sur l'étoile sur la cellule de commande. Accédez à tous les favoris depuis **Paramètres → Favoris** ou le filtre rapide **Favoris**.

### Comment configurer les widgets de l'écran d'accueil ?

1. Appuyez longuement sur une zone vide de votre écran d'accueil et appuyez sur le bouton **+** dans le coin supérieur.
2. Recherchez **iLinux** dans la galerie de widgets.
3. Choisissez un style de widget et appuyez sur **Ajouter un widget**.

Un **Guide des widgets** étape par étape est également disponible dans **Paramètres → Guide des widgets**. Pour que les arrière-plans des widgets suivent le dégradé du thème de votre application, activez l'option dans **Paramètres → Widgets**.

**Bibliothèque de commandes de widget :** Dans **Paramètres → Widgets**, choisissez quelle bibliothèque shell (Linux / CMD / PowerShell) alimente les widgets Daily Command et Category Spotlight. Ceci est indépendant du commutateur shell intégré à l'application - utile si vous souhaitez que les widgets affichent les commandes Windows lors de la navigation sur Linux dans l'application.

### Le widget Daily Command affiche la même commande chaque jour. Comment puis-je le changer ?

Appuyez sur le **bouton flèche circulaire (lecture aléatoire)** dans le coin supérieur droit du widget Commande quotidienne pour charger immédiatement une commande différente. Cette fonctionnalité nécessite **iOS 17 ou version ultérieure**.

Sur iOS 16, le widget Daily Command affiche une commande fixe pour chaque jour et n'inclut pas le bouton de lecture aléatoire.

### Comment configurer les actions rapides de l'écran d'accueil ?

Appuyez longuement sur l'icône de l'application iLinux pour voir jusqu'à **4** actions rapides. Choisissez les actions à afficher dans **Paramètres → Raccourcis de l'écran d'accueil**. Sept options sont disponibles : **Rechercher**, **Quiz quotidien**, **Favoris**, **Cahier de mauvaises réponses**, **Catégories**, **Envoyer des commentaires** et **Évaluer l'application**. Vous pouvez réorganiser et réinitialiser les paramètres par défaut à partir du même écran.

### Comment utiliser iLinux avec l'application Raccourcis ?

iLinux prend en charge le schéma d'URL `ilinux://`. Utilisez une action **Ouvrir les URL** dans l'application Raccourcis. Exemples :

- `ilinux://command?name=grep` — ouvre la commande Linux `grep` (`cmd=` fonctionne aussi)
- `ilinux://command?cmd=dir&platform=cmd` — ouvre la commande CMD `dir`
- `ilinux://command?cmd=Get-ChildItem&platform=powershell` — ouvre la commande PowerShell
- `ilinux://quiz` — ouvre l'onglet Quiz quotidien
- `ilinux://favorites` — ouvre votre liste de favoris
- `ilinux://wrong` ou `ilinux://mistakes` — ouvre le livre des mauvaises réponses

**Paramètre de plate-forme :** `platform=linux` (par défaut), `cmd` (alias : `batch`, `bat`) ou `powershell` (alias : `ps`, `pwsh`). Omettre pour les commandes Linux.

Note: **Search** and **Categories** are available as Home Screen quick actions but are not registered as universal deep-link hosts. See the full [URL Scheme Reference](../url-scheme).

### Comment partager une commande ?

Sur n'importe quelle page de détails de commande, appuyez sur **Partager** dans la barre d'outils. Vous pouvez exporter la commande sous forme de **fichier Markdown** ou générer une **carte de partage PNG stylisée** (avec le code QR de l'App Store) à envoyer via la feuille de partage du système. L'enregistrement d'images dans Photos peut nécessiter l'accès à la photothèque.

### Comment changer la couleur du thème ?

Accédez à **Paramètres → Thème**. Faites défiler les 15 préréglages de couleurs intégrés ou appuyez sur la ligne **Couleur personnalisée** pour sélectionner n'importe quelle couleur à l'aide du sélecteur de couleurs du système. La couleur d'accent, les dégradés et le widget reflètent tous les mises à jour immédiatement.

### Puis-je changer l’icône de l’application ?

Oui. Accédez à **Paramètres → Icône de l'application** pour choisir parmi **6 icônes** (par défaut plus 5 alternatives). Le paramètre est appliqué instantanément sans relancer l'application.

### La couleur du widget ne correspond pas à mon thème. Comment puis-je le réparer ?

Les widgets synchronisent la couleur de leur thème via un groupe d'applications partagé entre l'application principale et l'extension du widget. Si le widget semble obsolète :

1. Ouvrez iLinux une fois : cela force l'actualisation des données du groupe d'applications.
2. Si le widget ne se met toujours pas à jour, appuyez longuement sur le widget et appuyez sur **Modifier le widget** (ou supprimez-le et rajoutez-le) pour déclencher un rechargement de la chronologie.

Assurez-vous que l'extension **iLinux Widget** et l'application principale sont toutes deux à jour (même version).

### iLinux prend-il en charge l'iPad ?

Oui. iLinux fonctionne nativement sur iPad avec des mises en page adaptatives. Le mode Grille prend en charge jusqu'à **8 colonnes**. Les widgets, les icônes alternatives, les raccourcis de l'écran d'accueil et les haptiques sont entièrement pris en charge sur iPad.

### Comment changer la langue sur Mac ?

Le **sélecteur de langue** intégré à l'application se trouve dans **Paramètres → Langue** sur **iPhone et iPad**. Sur **Mac**, les préférences linguistiques arrivent généralement via la **synchronisation iCloud** à partir d'un autre appareil, ou suivent vos préférences enregistrées/paramètres régionaux du système lors du premier lancement. Activez la synchronisation iCloud pour que la langue reste alignée sur tous les appareils.

### Vous avez encore besoin d'aide ?

Contactez-nous à [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) ou utilisez l'option **Paramètres → Envoyer des commentaires** de l'application. Nous répondons généralement dans les 48 heures.

</section>
<section lang="tr" markdown="1">

### iLinux bir hesap veya internet bağlantısı gerektiriyor mu?

Hayır. iLinux komut kitaplıkları için tamamen çevrimdışı çalışır. Tüm komut verileri (JSON özetleri ve Markdown belgeleri) uygulamanın içinde paketlenmiştir. Belgelere göz atmak, belgeleri okumak veya sınavlara katılmak için kaydolmanıza gerek yoktur. İsteğe bağlı **iCloud senkronizasyonu**, favorilerinizi hizalamak ve cihazlar arasında ilerlemek için Apple Kimliğinizi kullanır; komut içeriğini yüklemez.

### iLinux Mac'i destekliyor mu?

Evet. iLinux **kenar çubuğu masaüstü düzeni**, yeniden boyutlandırılabilir pencere ve genişletilmiş klavye kısayolları (**⌘,**, **⌘[**, **Esc**, **⌘←/→**, test tuşları **1–4** / **⌘R** / **Return**) içeren **yerel bir macOS uygulamasıdır** (macOS **13.0+**, Mac Catalyst değil). Tüm temel özellikler (üç kabuk kitaplığı, eşdeğerleri, sınav, derin bağlantılar ve temalar) Mac'te çalışır.

**Mac'te geçerli değildir:** Ana Ekran widget'ları, Ana Ekran hızlı eylemleri ve alternatif uygulama simgeleri **yalnızca iPhone/iPad'de mevcuttur**. İOS'ta widget'ları yapılandırın; Mac, uygulama içi bir bildirim gösteriyor.

### iCloud senkronizasyonu nasıl çalışır?

**iCloud**'da aynı Apple kimliğiyle oturum açtığınızda, **Ayarlar → Öğrenme istatistikleri** bölümünde **iCloud Senkronizasyonu**'nu etkinleştirin. iLinux, **favorileri**, **sınav ilerlemesini**, **temayı** ve **görüntüleme tercihlerini** (dil, kabuk platformu, favori kapsamı, liste/tablo) iCloud Anahtar-Değer Depolama aracılığıyla **iPhone, iPad ve Mac** genelinde senkronize eder. Çatışmalar otomatik olarak birleşir (örneğin, favorilerin birleşmesi). Diğerlerini etkilemeden **bir cihazdaki senkronizasyonu devre dışı bırakabilirsiniz**. Komut kitaplıkları tamamen çevrimdışı kalır; yalnızca kişisel ilerlemeniz senkronize edilir.

### iLinux komutları gerçek bir Linux terminalinde çalıştırıyor mu?

Hayır. iLinux **yalnızca bir referans ve öğrenme aracıdır**. Bir kabuk, SSH istemcisi veya uzaktan yürütme ortamı sağlamaz. Komutlar çalışma amacıyla belgelenmiştir; bunları kendi Linux makinenizde, Windows PC'nizde, sunucunuzda veya bulut örneğinizde uygularsınız.

### iLinux hangi kabuk platformlarını destekliyor?

iLinux içerik dili başına üç çevrimdışı komut kütüphanesi sunar:

- **Linux** — 14 kategoride 1050 komut
- **Windows CMD / Batch** — 10 kategoride 300 komut
- **PowerShell** — 10 kategoride 300 komut

Dil başına **toplam 1650'den fazla komut** (İngilizce, Basitleştirilmiş Çince, Geleneksel Çince). Araç çubuğu Kabuk menüsünden **Komutlar**, **Kategoriler** veya **Günlük Sınav** üzerinden kitaplıklar arasında geçiş yapın.

### Linux, CMD ve PowerShell arasında nasıl geçiş yapabilirim?

Komutlar, Kategoriler veya Günlük Test sekmesindeki araç çubuğundaki **Shell platformu** menüsüne (terminal simgesi) dokunun. Seçiminiz devam eder ve o platform için aramayı, kategorileri, sınav sorularını ve öğrenme istatistiklerini kapsar.

**Ayarlar → Ana sayfa hızlı erişimi** bölümünde ayrıca varsayılan bir kabuk platformu, **sık kullanılanlar kapsamı** (tüm platformlar ve yalnızca mevcut platform) ve Günlük Komut ve Kategori Gündemi widget'ları için **widget komut kitaplığı** da ayarlayabilirsiniz.

### Platformlar arası eşdeğer komutlar nelerdir?

**100+ equivalent groups** link commands that accomplish the same task across Linux, CMD and PowerShell — for example `ls`, `dir` and `Get-ChildItem`. On a command detail page, the **Equivalents** bar shows related entries; tap one to jump to that platform's documentation instantly.

### Kaç tane komut yer alıyor?

Her içerik dili, üç kabuk kitaplığında **1650+** komutlar içerir:

| platformu | Komutlar | Kategoriler |
|----------|----------|------------|
| Linux | 1050 | 14 |
| CMD / Toplu | 300 | 10 |
| PowerShell | 300 | 10 |

Tüm belgeler çevrimdışı olarak İngilizce, Basitleştirilmiş Çince ve Geleneksel Çince dillerinde mevcuttur.

### Bir komutu nasıl arayabilirim?

Komutlar sekmesindeki büyüteç simgesine dokunun veya donanım klavyesinde **⌘F** tuşuna basın. Bir komut adı, anahtar kelime veya açıklamanın bir kısmını yazın. Sonuçlar siz yazdıkça gerçek zamanlı olarak güncellenir.

### Liste ve tablo görünümü arasında nasıl geçiş yapabilirim?

**Komutlar** veya **Kategoriler** sekmesinde araç çubuğu filtre menüsünü (huni simgesi) açın. **Görüntüleme Modu** altında **Liste** veya **Izgara**'yı seçin. Izgara modunda, satır başına sütunları ayarlamak için **+ / −** düğmelerini kullanın (iPhone'da **1–6**, iPad ve Mac'te **1–8**). Varsayılanı **Ayarlar → Ekran** bölümünden de değiştirebilirsiniz.

### Öğrenme ilerlememi nasıl takip ederim?

Bir komutun ayrıntı sayfasını açın ve durumunu **Öğrenilmemiş**, **Öğrenilmiş** veya **Uzmanlaşmış** olarak ayarlayın. Liste görünümünde hızlı durum ve favori eylemler için bir satırı kaydırın. Izgara görünümünde favorilere eklemek için yıldız düğmesini ve durum için içerik menüsünü kullanın. Henüz çalışmadığınız komutlara odaklanmak için araç çubuğu menüsünden **Öğrenilmemiş** olarak filtreleyin.

### Hangi diller mevcut?

iLinux, hem uygulama arayüzü hem de komut belgeleri için üç dili destekler:

- **İngilizce**
- **Basitleştirilmiş Çince (简体中文)**
- **Geleneksel Çince (繁體中文)**

Cihazınızın yerel ayarını takip etmek için **Sistem**'i de seçebilirsiniz. **Ayarlar → Dil** bölümünden dili değiştirin. Widget'lar da dahil olmak üzere uygulamanın tamamı anında güncellenir.

### Günlük Sınav nasıl çalışır?

Her gün, **aktif kabuk platformuna göre belirlenen** (Linux, CMD veya PowerShell) tarihe dayalı bir tohum kullanılarak yeni bir test soruları seti oluşturulur. iLinux'u aynı gün kullanan herkes, o platform için aynı temel sınav setini alır. İki soru türü görünür:

- **Eşleşme Özeti** — kısa bir açıklama görürsünüz ve doğru komut adını seçmelisiniz.
- **Eşleştirme Seçeneği Anlamı** — bir bayrağın açıklamasını görürsünüz (ör. `-r: recursive`) ve bunun hangi komuta ait olduğunu tanımlamanız gerekir.

Tap the **refresh button** (circular arrow) in the toolbar to get a different randomised set at any time. **Perfect streak** days (consecutive days with a perfect score) are tracked per platform and shown in the quiz screen and Quiz Glance widget. Generic help flags like `-h` and `--version` are excluded to keep questions unambiguous.

### Yanlış cevaplarım kaydedilmiyor. Ne yapmalıyım?

Bir sınav oturumunu tamamladıktan sonra yanlış cevaplar otomatik olarak kaydedilir. Test turunun tamamını bitirdiğinizden emin olun (tüm soruları yanıtlayın ve sonuç ekranına ulaşın). Kısmen tamamlanan oturumlar kaydedilmez.

Kaydedilen tüm yanlış cevapları **Ayarlar → Yanlış Cevap Defteri** bölümünden inceleyebilirsiniz.

### Favorilere nasıl komut eklerim?

Herhangi bir komutun ayrıntı sayfasını açın ve sağ üst köşedeki **yıldız simgesine** dokunun. **tablo görünümünde** doğrudan komut hücresindeki yıldıza dokunun. Tüm favorilere **Ayarlar → Favoriler** veya **Favoriler** hızlı filtresinden erişin.

### Ana Ekran Widget'larını nasıl ayarlarım?

1. Ana Ekranınızın boş bir alanına uzun basın ve üst köşedeki **+** düğmesine dokunun.
2. Widget galerisinde **iLinux**'u arayın.
3. Bir widget stili seçin ve **Widget Ekle**'ye dokunun.

Adım adım **Widget Kılavuzu** ayrıca **Ayarlar → Widget Kılavuzu**'nda da mevcuttur. Widget arka planlarının uygulama temanızın eğimini takip etmesini sağlamak için **Ayarlar → Widget'lar** bölümündeki seçeneği etkinleştirin.

**Widget komut kitaplığı:** **Ayarlar → Widget'lar** bölümünde, Günlük Komut ve Kategori Spot Işığı widget'larını hangi kabuk kitaplığının (Linux / CMD / PowerShell) besleyeceğini seçin. Bu, uygulama içi kabuk anahtarından bağımsızdır; uygulama içinde Linux'a göz atarken widget'ların Windows komutlarını göstermesini istiyorsanız kullanışlıdır.

### Günlük Komut widget'ı her gün aynı komutu gösterir. Bunu nasıl değiştiririm?

Hemen farklı bir komut yüklemek için Günlük Komut widget'ının sağ üst köşesindeki **dairesel ok (karıştır) düğmesine** dokunun. Bu özellik **iOS 17 veya üzeri** gerektirir.

iOS 16'da Günlük Komut widget'ı her gün için sabit bir komut görüntüler ve karıştırma düğmesini içermez.

### Ana Ekran Hızlı Eylemlerini nasıl yapılandırabilirim?

**4** adede kadar hızlı eylemi görmek için iLinux uygulama simgesine uzun basın. **Ayarlar → Ana Ekran Kısayolları**'nda hangi eylemlerin görüneceğini seçin. Yedi seçenek mevcuttur: **Arama**, **Günlük Test**, **Favoriler**, **Yanlış Cevap Defteri**, **Kategoriler**, **Geri Bildirim Gönder** ve **Uygulamaya Puan Ver**. Aynı ekrandan yeniden sıralayabilir ve varsayılanlara sıfırlayabilirsiniz.

### iLinux'u Kısayollar uygulamasıyla nasıl kullanırım?

iLinux supports the `ilinux://` URL scheme. Use an **Open URLs** action in the Shortcuts app. Examples:

- `ilinux://command?name=grep` — Linux komutu `grep`i açar (`cmd=` da çalışır)
- `ilinux://command?cmd=dir&platform=cmd` — CMD komutu `dir`i açar
- `ilinux://command?cmd=Get-ChildItem&platform=powershell` — PowerShell komutunu açar
- `ilinux://quiz` — opens the Daily Quiz tab
- `ilinux://favorites` — Favoriler listenizi açar
- `ilinux://wrong` veya `ilinux://mistakes` — Yanlış Yanıtlar Kitabı'nı açar

**Platform parameter:** `platform=linux` (default), `cmd` (aliases: `batch`, `bat`), or `powershell` (aliases: `ps`, `pwsh`). Omit for Linux commands.

Not: **Arama** ve **Kategoriler** Ana Ekrandaki hızlı işlemler olarak kullanılabilir ancak evrensel derin bağlantı ana bilgisayarları olarak kayıtlı değildir. [URL Şeması Referansı](../url-scheme)'nin tamamına bakın.

### Bir komutu nasıl paylaşabilirim?

Herhangi bir komut ayrıntısı sayfasında, araç çubuğunda **Paylaş**'a dokunun. Komutu bir **Markdown dosyası** olarak dışa aktarabilir veya sistem Paylaşım Sayfası aracılığıyla göndermek üzere **stillendirilmiş bir PNG paylaşım kartı** (App Store QR koduyla) oluşturabilirsiniz. Görüntülerin Fotoğraflar'a kaydedilmesi, fotoğraf kitaplığına erişim gerektirebilir.

### Tema rengini nasıl değiştiririm?

**Ayarlar → Tema**'ya gidin. 15 yerleşik renk ön ayarı arasında ilerleyin veya sistemin renk seçicisini kullanarak herhangi bir rengi seçmek için **Özel Renk** satırına dokunun. Vurgu rengi, degradeler ve widget aynasının tümü anında güncellenir.

### Uygulama simgesini değiştirebilir miyim?

Evet. **6 simge** (varsayılan artı 5 alternatif) arasından seçim yapmak için **Ayarlar → Uygulama Simgesi**'ne gidin. Ayar, uygulamayı yeniden başlatmaya gerek kalmadan anında uygulanır.

### Widget rengi temamla eşleşmiyor. Bunu nasıl düzeltebilirim?

Widget'lar, ana uygulama ile widget uzantısı arasında paylaşılan bir Uygulama Grubu aracılığıyla tema renklerini senkronize eder. Widget güncelliğini kaybetmiş görünüyorsa:

1. iLinux'u bir kez açın; bu, Uygulama Grubu verilerinin yenilenmesini zorlar.
2. Widget hâlâ güncellenmiyorsa, zaman çizelgesinin yeniden yüklenmesini tetiklemek için widget'a uzun basın ve **Widget'ı Düzenle**'ye dokunun (veya kaldırıp yeniden ekleyin).

**iLinux Widget** uzantısının ve ana uygulamanın güncel (aynı sürüm) olduğundan emin olun.

### iLinux iPad'i destekliyor mu?

Evet. iLinux, uyarlanabilir düzenlerle iPad'de yerel olarak çalışır. Izgara modu **8 sütuna** kadar destekler. Widget'lar, alternatif simgeler, Ana Ekran kısayolları ve dokunsal özellikler iPad'de tam olarak desteklenir.

### Mac'te dili nasıl değiştiririm?

Uygulama içi **dil seçici**, **iPhone ve iPad**'de **Ayarlar → Dil** bölümünde bulunur. **Mac**'te dil tercihi genellikle başka bir cihazdan **iCloud senkronizasyonu** yoluyla gelir veya ilk başlatmada kayıtlı tercihinizi/sistem yerel ayarınızı takip eder. Dili cihazlar arasında uyumlu tutmak için iCloud senkronizasyonunu etkinleştirin.

### Hala yardıma mı ihtiyacınız var?

Bize [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) adresinden ulaşın veya uygulama içi **Ayarlar → Geri Bildirim Gönder** seçeneğini kullanın. Genellikle 48 saat içinde yanıt veririz.

</section>
