---
layout: doc
title: iLinux — URL Scheme Reference
app_id: iLinux
doc_title_en: URL Scheme Reference
doc_title_zh_cn: URL Scheme 深度链接文档
doc_title_zh_tw: URL Scheme 深度連結文件
description: Complete reference of ilinux:// deep links on iOS, iPad and Mac — command detail with platform parameter, quiz, favourites, wrong book, widgets and Home Screen Quick Actions.
---

<section lang="en" markdown="1">

iLinux supports **`ilinux://`** (also written **`iLinux://`**) URL scheme deep links on **iPhone, iPad and Mac** — open command detail (Linux, CMD or PowerShell), the Daily Quiz, Favourites or the Wrong Answer Book from Safari, another app, a widget tap (iOS/iPad), or Apple Shortcuts.

Command URLs accept an optional **`platform`** query parameter so widget taps and Shortcuts can open Windows entries correctly.

**Home Screen Quick Actions** (long-press the app icon on **iOS/iPad only**) cover Search, Categories, Feedback and Rate. Mac users can use the **iLinux** menu and keyboard shortcuts instead.

> **Important:** iLinux is a **reference and learning app**. URL links only **navigate inside the app**. They do **not** execute Linux commands, open SSH sessions or connect to remote servers.

## Protocol Specification

```
ilinux://<host>[/<path>][?query]
iLinux://<host>[/<path>][?query]   ← same scheme, case-insensitive
```

| Rule | Detail |
|------|--------|
| **Scheme** | `ilinux` / `iLinux` — compared case-insensitively |
| **Host routing** | Primary router is the URL **host**; some paths also accepted (see below) |
| **Command detail** | Host `command` **or** path `/command` |
| **Command ID** | Query `name=<id>` **or** `cmd=<id>` — must match a bundled command key (e.g. `ls`, `grep`, `dir`, `Get-ChildItem`) |
| **Platform** | Query `platform=<value>` — optional; defaults to **Linux** when omitted |
| **Quiz** | Host `quiz` **or** path `/quiz` |
| **Favourites** | Host `favorites` **or** path `/favorites` |
| **Wrong book** | Host `wrong`, `mistakes`, or `wrongquestions`; path `/wrong` or `/mistakes` also accepted |
| **Wrong record** | Query `record=<UUID>` on a wrong-book URL — opens that record's command detail |
| **Query parameters** | No other pre-fill parameters are supported |
| **Parser** | `ILinuxDeepLink.parse(_:)` — consumed via `onOpenURL` → `AppRouter.pendingDeepLink` |

**Two delivery channels**

| Channel | Handled by | Examples |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ILinuxDeepLink.parse` → `RootTabView` | `command`, `quiz`, `favorites`, `wrong` |
| **Home Screen Quick Action** | `ShortcutSceneDelegate` → `ShortcutObserver.dispatch` | `search`, `categories`, `feedback`, `review`, plus overlapping `quiz` / `favorites` / `wrong` |

Quick-action types use **`contains`** matching on the type string, so both `iLinux://search` and legacy variants still route correctly.

---

## 1. Command Detail

Open the detail page for a single bundled command.

| Parameter | Required | Description |
|-----------|----------|-------------|
| `name` | One of `name` / `cmd` | Command ID (dictionary key in the platform JSON bundle) |
| `cmd` | One of `name` / `cmd` | Synonym for `name` — used by widget links |
| `platform` | No | Shell library: see table below. Defaults to **Linux** |

**`platform` values** (case-insensitive):

| Value | Shell library | Aliases |
|-------|---------------|---------|
| *(omit)* or `linux` | Linux (1050 commands) | — |
| `cmd` | CMD / Batch (300 commands) | `batch`, `bat` |
| `powershell` | PowerShell (300 commands) | `ps`, `pwsh` |

**Behaviour**

- Switches to the **Commands** tab, selects the requested **shell platform**, and pushes `CommandDetailView` for the resolved command.
- If the ID is **unknown or empty**, the link is **silently ignored** (no error UI).
- Command IDs are **case-sensitive** and must match the bundled JSON key exactly (typically lowercase, e.g. `docker`, not `Docker`).

**Open `ls`**

```
ilinux://command?name=ls
```

**Open `grep` (Linux, default)**

```
ilinux://command?cmd=grep
```

**Open CMD `dir`**

```
ilinux://command?cmd=dir&platform=cmd
```

**Open PowerShell `Get-ChildItem`**

```
ilinux://command?cmd=Get-ChildItem&platform=powershell
```

**Cloud-native Linux example**

```
ilinux://command?name=docker
```

---

## 2. Daily Quiz

Jump directly to the **Daily Quiz** tab. Does **not** auto-start or skip questions.

```
ilinux://quiz
```

Path form (also accepted):

```
ilinux:///quiz
```

---

## 3. Favourites

Open the **Favourites** list under Settings navigation.

```
ilinux://favorites
```

Path form (also accepted):

```
ilinux:///favorites
```

---

## 4. Wrong Answer Book

### 4.1 List

Open the **Wrong Answer Book** list under Settings navigation.

```
ilinux://wrong
```

Aliases (same behaviour):

```
ilinux://mistakes
ilinux://wrongquestions
```

### 4.2 Single record → command detail

When `record` is a valid UUID of a saved wrong-answer entry, the app opens the **Commands** tab and pushes detail for that record's command (if the record and command still exist).

| Parameter | Required | Format |
|-----------|----------|--------|
| `record` | Yes | UUID string, e.g. `550e8400-e29b-41d4-a716-446655440000` |

```
ilinux://wrong?record=550e8400-e29b-41d4-a716-446655440000
```

If the UUID is invalid or the record was deleted, navigation falls back to the wrong-book list or is skipped.

---

## 5. Home Screen Quick Actions

Long-press the iLinux icon → up to **4** actions. Configure in **Settings → Home Screen Shortcuts** (7 options, drag to reorder, reset to defaults).

| Option | Registered `type` | SF Symbol | Opens |
|--------|-------------------|-----------|--------|
| Search | `iLinux://search` | magnifyingglass | **Commands** tab + activate search bar |
| Daily Quiz | `iLinux://quiz` | checklist | **Daily Quiz** tab |
| Favourites | `iLinux://favorites` | star.fill | **Favourites** list |
| Wrong Answer Book | `iLinux://wrong` | xmark.bin.fill | **Wrong Answer Book** list |
| Categories | `iLinux://categories` | rectangle.grid.2x2.fill | **Categories** tab |
| Send Feedback | `iLinux://feedback` | envelope.fill | In-app mail compose (or `mailto:` fallback) |
| Rate App | `iLinux://review` | star.bubble.fill | StoreKit review prompt |

**Default selection on first install:** Search · Daily Quiz · Favourites · Send Feedback.

**Quick-action-only destinations** (not handled by `ILinuxDeepLink.parse` / `onOpenURL`):

- `iLinux://search`
- `iLinux://categories`
- `iLinux://feedback`
- `iLinux://review`

Use these via **long-press icon** or by posting the same type through the Quick Action pipeline — opening them with Shortcuts **Open URL** may **not** work unless the app adds explicit host parsing later.

**Legacy type (still routed):**

| Type | Behaviour |
|------|-----------|
| `iLinux://love` | Opens author blog in in-app Safari sheet (old static shortcut) |

---

## 6. Widget Deep Links

Widget taps use the same `iLinux://` URLs built by `WidgetDeepLink`:

| Widget | Tap target | URL |
|--------|------------|-----|
| Daily Command | Command detail | `iLinux://command?cmd=<id>&platform=<linux\|cmd\|powershell>` |
| Category Spotlight | Sample command | `iLinux://command?cmd=<id>&platform=<platform>` |
| Quiz Glance | Daily Quiz | `iLinux://quiz` |
| Favourites Glance | Favourites (or per-row command) | `iLinux://favorites` / `iLinux://command?cmd=<id>&platform=<platform>` |
| Wrong Book Glance | Wrong book (or per-row record) | `iLinux://wrong` / `iLinux://wrong?record=<UUID>` |

Widget URLs are built by `WidgetDeepLink.command(_:platform:)` and always include **`platform`** for command taps. The platform matches **Settings → Widgets → Widget command library** (Linux / CMD / PowerShell).

The **Daily Command shuffle button** (iOS 17+, App Intent) reloads the widget timeline only — it does **not** use a URL.

---

## Apple Shortcuts

### Open a command after copying its name

1. **Get Text from Input**
2. **Open URLs** → `ilinux://command?name=` + Text

Or hard-code Linux:

```
ilinux://command?name=systemctl
```

Open a CMD command:

```
ilinux://command?cmd=ipconfig&platform=cmd
```

### Daily study reminder → quiz

```
ilinux://quiz
```

Add **Open URLs** in a Personal Automation (e.g. every weekday at 9:00).

### Review wrong answers

```
ilinux://wrong
```

### Open favourites from a Focus mode shortcut

```
ilinux://favorites
```

---

## Launch Behaviour

When the app receives a URL or Quick Action:

| Scenario | Flow |
|----------|------|
| **Cold start — Quick Action (iOS/iPad only)** | `ShortcutSceneDelegate` → `PendingShortcutBuffer` → `ShortcutObserver.onAppear` → `dispatch(type:)` |
| **Warm start — Quick Action (iOS/iPad only)** | Scene callback → notification → `dispatch(type:)` |
| **Cold / warm — `onOpenURL` (iOS, iPad, Mac)** | `AppRouter.handleIncomingURL` → `pendingDeepLink` → `RootTabView.onChange` navigates |
| **Feedback / Rate (cold start)** | `deferSheetWork` delays **~0.4 s** so mail sheet / StoreKit has an active window scene |
| **Search quick action** | `openSearchTab()` → `searchPulse += 1` → `BrowseCommandsView` presents search (iOS 17+: auto-focus via `isPresented`) |
| **Unknown command ID** | Deep link parsed but navigation skipped — no alert |

---

## Keyboard Shortcuts

### iPad & Mac (shared)

Hardware keyboard on iPad and the **iLinux** menu on Mac share:

| Shortcut | Action |
|----------|--------|
| ⌘F | Commands tab + search (same intent as Search quick action on iOS) |
| ⌘1 | Commands tab |
| ⌘2 | Categories tab |
| ⌘3 | Daily Quiz tab |
| ⌘4 | Settings tab |

Search auto-focus via ⌘F requires **iOS 17.0+** or **macOS 14.0+**.

### Mac only

| Shortcut | Action |
|----------|--------|
| ⌘, | Settings tab |
| ⌘[ / Esc | Pop navigation stack (back) |
| ⌘← / ⌘→ | Previous / next category (Categories tab) |
| 1–4 | Select quiz answer option |
| ⌘R | Reshuffle daily quiz |
| Return | Next quiz question (after answering) |

Deep links (`onOpenURL`) and menu shortcuts use the same in-app router on Mac as on iOS.

---

## Unsupported & Invalid URLs

| URL | Result |
|-----|--------|
| `ilinux://command` (no `name` / `cmd`) | Ignored |
| `ilinux://command?name=NotARealCmd` | Ignored (ID not in library for resolved platform) |
| `ilinux://command?cmd=dir` (no platform) | Opens **Linux** library — use `platform=cmd` for Windows CMD |
| `ilinux://search` via Shortcuts Open URL | **Not** parsed by `ILinuxDeepLink` — use Quick Action on **iOS/iPad**, or ⌘F on **Mac/iPad** |
| `ilinux://categories` via Shortcuts Open URL | Same as above |
| `ilinux://feedback` / `ilinux://review` via Open URL | Same as above |
| Non-`ilinux` schemes | Ignored |

---

## Troubleshooting

**Shortcut opens the app but nothing happens (cold launch)**

Feedback, Rate and mail sheets need ~0.4 s after launch. Try again from inside the app, or wait a moment on cold start.

**Search quick action doesn't focus the search field (iOS 16)**

Auto-focus requires iOS 17+. On iOS 16 the Commands tab still opens; tap the search field manually.

**Widget tap doesn't open the expected command**

Ensure the command still exists in your installed app version for the correct **platform**. Widget links use `cmd=` + `platform=` and require an exact command ID. Example: `dir` needs `platform=cmd`, not the default Linux library.

**Quick-action titles are in the wrong language**

Change language in **Settings → Language** — the app re-registers shortcut items automatically.

**Deep link works on device but not from a web page**

Confirm the link uses scheme `ilinux://` and is opened by the system (tap in Notes/Messages), not blocked by an in-app browser that strips custom schemes.

---

[Back to iLinux Support](./) &middot; [FAQ](faq) &middot; [Privacy Policy](privacy)

</section>

<section lang="zh-CN" markdown="1">

爱 Linux 支持 **`ilinux://`**（亦可写作 **`iLinux://`**）URL Scheme 深度链接——从 Safari、其它应用、二维码、主屏小组件点击或苹果快捷指令，打开命令详情、每日测验、收藏或错题本。命令 URL 支持可选的 **`platform`** 查询参数，便于小组件点击与快捷指令正确打开 Windows 命令。

另有一套 **主屏快捷方式**（长按应用图标），提供搜索、分类、反馈、评分等额外入口。

> **重要：** 爱 Linux 是**命令参考与学习应用**。链接仅用于**应用内导航**，**不会**执行 Linux 命令、建立 SSH 或连接远程服务器。

## 协议规范

```
ilinux://<host>[/<path>][?query]
iLinux://<host>[/<path>][?query]   ← 同一 Scheme，不区分大小写
```

| 规则 | 说明 |
|------|------|
| **Scheme** | `ilinux` / `iLinux` — 比较时不区分大小写 |
| **Host 路由** | 以 URL **host** 为主；部分 path 形式亦支持 |
| **命令详情** | Host 为 `command` **或** path 为 `/command` |
| **命令 ID** | 查询参数 `name=<id>` **或** `cmd=<id>` — 须与对应平台 JSON 键一致（如 `ls`、`dir`、`Get-ChildItem`） |
| **平台** | 查询参数 `platform=<值>` — 可选；省略时默认为 **Linux** |
| **测验** | Host `quiz` **或** path `/quiz` |
| **收藏** | Host `favorites` **或** path `/favorites` |
| **错题本** | Host `wrong`、`mistakes`、`wrongquestions`；path `/wrong`、`/mistakes` 亦可 |
| **错题记录** | 错题 URL 加 `record=<UUID>` — 打开该记录对应命令详情 |
| **其它参数** | 不支持预填或额外参数 |
| **解析器** | `ILinuxDeepLink.parse(_:)` — 经 `onOpenURL` → `AppRouter.pendingDeepLink` 消费 |

**两种投递通道**

| 通道 | 处理方 | 示例 |
|------|--------|------|
| **通用深度链接**（`onOpenURL`） | `ILinuxDeepLink.parse` → `RootTabView` | `command`、`quiz`、`favorites`、`wrong` |
| **主屏快捷方式** | `ShortcutSceneDelegate` → `ShortcutObserver.dispatch` | `search`、`categories`、`feedback`、`review`，以及重叠的 `quiz` / `favorites` / `wrong` |

快捷方式 type 使用 **`contains`** 宽松匹配，兼容 `iLinux://search` 及历史变体。

---

## 1. 命令详情

打开单条内置命令的详情页。

| 参数 | 必填 | 说明 |
|------|------|------|
| `name` | `name` / `cmd` 二选一 | 命令 ID |
| `cmd` | `name` / `cmd` 二选一 | 与 `name` 同义 — 小组件使用 |
| `platform` | 否 | Shell 库，见下表；默认 **Linux** |

**`platform` 取值**（不区分大小写）：

| 值 | Shell 库 | 别名 |
|----|----------|------|
| 省略或 `linux` | Linux（1050 条） | — |
| `cmd` | CMD / Batch（300 条） | `batch`、`bat` |
| `powershell` | PowerShell（300 条） | `ps`、`pwsh` |

**行为**

- 切到**命令**标签，切换到请求的 **Shell 平台**，并打开命令详情。
- ID **不存在或为空**时链接**静默忽略**（无错误提示）。
- 命令 ID **区分大小写**，须与 JSON 键完全一致（通常小写，如 `docker` 而非 `Docker`）。

**打开 `ls`**

```
ilinux://command?name=ls
```

**打开 `grep`（Linux，默认）**

```
ilinux://command?cmd=grep
```

**打开 CMD `dir`**

```
ilinux://command?cmd=dir&platform=cmd
```

**打开 PowerShell `Get-ChildItem`**

```
ilinux://command?cmd=Get-ChildItem&platform=powershell
```

---

## 2. 每日测验

直接跳转到**每日测验**标签。不会自动开始或跳过题目。

```
ilinux://quiz
```

---

## 3. 收藏

打开设置导航下的**收藏**列表。

```
ilinux://favorites
```

---

## 4. 错题本

### 4.1 列表

```
ilinux://wrong
```

等效别名：

```
ilinux://mistakes
ilinux://wrongquestions
```

### 4.2 单条记录 → 命令详情

`record` 为有效 UUID 时，打开该错题对应命令的详情（记录与命令仍存在时）。

```
ilinux://wrong?record=550e8400-e29b-41d4-a716-446655440000
```

UUID 无效或记录已删除时，回退到错题列表或跳过导航。

---

## 5. 主屏快捷方式

长按 iLinux 图标 → 最多 **4** 项。在 **设置 → 主屏快捷方式** 配置（7 项可选、可排序、可恢复默认）。

| 选项 | 注册 type | 图标 | 打开 |
|------|-----------|------|------|
| 搜索 | `iLinux://search` | magnifyingglass | **命令**页 + 激活搜索栏 |
| 每日测验 | `iLinux://quiz` | checklist | **每日测验**标签 |
| 收藏 | `iLinux://favorites` | star.fill | **收藏**列表 |
| 错题本 | `iLinux://wrong` | xmark.bin.fill | **错题本**列表 |
| 分类 | `iLinux://categories` | rectangle.grid.2x2.fill | **分类**标签 |
| 发送反馈 | `iLinux://feedback` | envelope.fill | 应用内邮件（或 `mailto:` 回退） |
| 评分 | `iLinux://review` | star.bubble.fill | StoreKit 评分 |

**首次安装默认：** 搜索 · 每日测验 · 收藏 · 发送反馈。

**仅快捷方式通道**（`ILinuxDeepLink.parse` / `onOpenURL` **不处理**）：

- `iLinux://search`
- `iLinux://categories`
- `iLinux://feedback`
- `iLinux://review`

请通过**长按图标**触发；在快捷指令中用 **打开 URL** 打开上述地址**可能无效**。

**遗留 type（仍路由）：**

| Type | 行为 |
|------|------|
| `iLinux://love` | 应用内 Safari 打开作者博客（旧版静态快捷项） |

---

## 6. 小组件深度链接

小组件点击使用 `WidgetDeepLink` 构建的相同 URL：

| 小组件 | 点击目标 | URL |
|--------|----------|-----|
| 每日命令 | 命令详情 | `iLinux://command?cmd=<id>&platform=<linux\|cmd\|powershell>` |
| 分类聚焦 | 示例命令 | `iLinux://command?cmd=<id>&platform=<platform>` |
| 测验一览 | 每日测验 | `iLinux://quiz` |
| 收藏速览 | 收藏 / 单行命令 | `iLinux://favorites` / `iLinux://command?cmd=<id>&platform=<platform>` |
| 错题速览 | 错题本 / 单行记录 | `iLinux://wrong` / `iLinux://wrong?record=<UUID>` |

小组件由 `WidgetDeepLink` 构建，命令链接始终携带 **`platform`**，与 **设置 → 小组件 → 小组件命令库** 一致。

**每日命令随机刷新按钮**（iOS 17+ App Intent）仅刷新时间线，**不使用 URL**。

---

## 苹果快捷指令

### 打开指定命令

```
ilinux://command?name=systemctl
```

### 每日提醒 → 做测验

```
ilinux://quiz
```

在个人自动化（如工作日 9:00）中添加 **打开 URL**。

### 复习错题

```
ilinux://wrong
```

### 打开收藏

```
ilinux://favorites
```

---

## 启动行为

| 场景 | 流程 |
|------|------|
| **冷启动 — 快捷方式** | `ShortcutSceneDelegate` → `PendingShortcutBuffer` → `ShortcutObserver.onAppear` → `dispatch` |
| **热启动 — 快捷方式** | Scene 回调 → 通知 → `dispatch` |
| **冷启动 — onOpenURL** | `handleIncomingURL` → `pendingDeepLink` → `RootTabView` 导航 |
| **反馈/评分（冷启动）** | 延迟 **约 0.4 秒**，等待 sheet / StoreKit 就绪 |
| **搜索快捷方式** | `searchPulse` → 展开搜索栏（iOS 17+ 自动聚焦） |
| **未知命令 ID** | 解析成功但跳过导航 — 无弹窗 |

---

## 键盘快捷键

### iPad 与 Mac（共用）

| 快捷键 | 动作 |
|--------|------|
| ⌘F | 命令页 + 搜索 |
| ⌘1 – ⌘4 | 命令 / 分类 / 测验 / 设置 |

⌘F 自动聚焦需 **iOS 17.0+** 或 **macOS 14.0+**。

### 仅 Mac

| 快捷键 | 动作 |
|--------|------|
| ⌘, | 设置 |
| ⌘[ / Esc | 返回 |
| ⌘← / ⌘→ | 上/下一分类 |
| 1–4 | 选择测验选项 |
| ⌘R | 换题 |
| Return | 下一题（作答后） |

---

## 不支持与无效 URL

| URL | 结果 |
|-----|------|
| `ilinux://command`（无 `name`/`cmd`） | 忽略 |
| `ilinux://command?name=NotARealCmd` | 忽略 |
| `ilinux://search` 经快捷指令打开 | **不**经 `ILinuxDeepLink` 解析 |
| `ilinux://categories` / `feedback` / `review` 同上 | 请用主屏快捷方式 |
| 非 `ilinux` Scheme | 忽略 |

---

## 故障排查

**冷启动点快捷方式没反应**

反馈、评分、邮件需启动后约 0.4 秒。可进应用后再试，或稍等片刻。

**搜索快捷方式在 iOS 16 不自动聚焦**

iOS 17+ 才支持 `searchable` 的 `isPresented`。iOS 16 仍会打开命令页，需手动点搜索框。

**小组件点击未打开预期命令**

确认命令 ID 与当前版本内置库一致；小组件使用 `cmd=` 且 ID 须完全匹配。

**快捷方式标题语言不对**

在 **设置 → 语言** 切换 — 应用会自动重新注册快捷项。

**网页里点链接无效**

确认使用 `ilinux://`，且由系统打开（备忘录/信息），而非被内置浏览器拦截自定义 Scheme。

---

[返回爱 Linux 支持页](./) &middot; [常见问题](faq) &middot; [隐私政策](privacy)

</section>

<section lang="zh-TW" markdown="1">

愛 Linux 支援 **`ilinux://`**（亦可寫作 **`iLinux://`**）URL Scheme 深度連結——從 Safari、其它應用、QR Code、主畫面小工具點擊或 Apple 捷徑，開啟指令詳情、每日測驗、收藏或錯題本。指令 URL 支援可選的 **`platform`** 查詢參數，便於小工具點擊與捷徑正確開啟 Windows 指令。

另有一套 **主畫面捷徑**（長按應用圖示），提供搜尋、分類、回饋、評分等額外入口。

> **重要：** 愛 Linux 是**指令參考與學習應用**。連結僅用於**應用內導覽**，**不會**執行 Linux 指令、建立 SSH 或連接遠端伺服器。

## 協定規範

```
ilinux://<host>[/<path>][?query]
iLinux://<host>[/<path>][?query]   ← 同一 Scheme，不分大小寫
```

| 規則 | 說明 |
|------|------|
| **Scheme** | `ilinux` / `iLinux` — 比較時不分大小寫 |
| **Host 路由** | 以 URL **host** 為主；部分 path 形式亦支援 |
| **指令詳情** | Host 為 `command` **或** path 為 `/command` |
| **指令 ID** | 查詢參數 `name=<id>` **或** `cmd=<id>` — 須與對應平台 JSON 鍵一致 |
| **平台** | 查詢參數 `platform=<值>` — 可選；省略時預設 **Linux** |
| **測驗** | Host `quiz` **或** path `/quiz` |
| **收藏** | Host `favorites` **或** path `/favorites` |
| **錯題本** | Host `wrong`、`mistakes`、`wrongquestions`；path `/wrong`、`/mistakes` 亦可 |
| **錯題紀錄** | 錯題 URL 加 `record=<UUID>` — 開啟該紀錄對應指令詳情 |
| **其它參數** | 不支援預填或額外參數 |
| **解析器** | `ILinuxDeepLink.parse(_:)` — 經 `onOpenURL` → `AppRouter.pendingDeepLink` 消費 |

**兩種投遞通道**

| 通道 | 處理方 | 範例 |
|------|--------|------|
| **通用深度連結**（`onOpenURL`） | `ILinuxDeepLink.parse` → `RootTabView` | `command`、`quiz`、`favorites`、`wrong` |
| **主畫面捷徑** | `ShortcutSceneDelegate` → `ShortcutObserver.dispatch` | `search`、`categories`、`feedback`、`review`，以及重疊的 `quiz` / `favorites` / `wrong` |

捷徑 type 使用 **`contains`** 寬鬆匹配，相容 `iLinux://search` 及歷史變體。

---

## 1. 指令詳情

開啟單條內建指令的詳情頁。

| 參數 | 必填 | 說明 |
|------|------|------|
| `name` | `name` / `cmd` 二選一 | 指令 ID |
| `cmd` | `name` / `cmd` 二選一 | 與 `name` 同義 |
| `platform` | 否 | Shell 庫；預設 **Linux** |

**`platform` 取值：** 省略/`linux` → Linux；`cmd`（別名 `batch`/`bat`）→ CMD；`powershell`（別名 `ps`/`pwsh`）→ PowerShell。

**行為** — 切到**指令**標籤、切換 Shell 平台並開啟詳情。
- ID **不存在或為空**時連結**靜默忽略**（無錯誤提示）。
- 指令 ID **區分大小寫**，須與 JSON 鍵完全一致（通常小寫，如 `docker` 而非 `Docker`）。

**開啟 `ls`**

```
ilinux://command?name=ls
```

**開啟 CMD `dir`**

```
ilinux://command?cmd=dir&platform=cmd
```

**開啟 PowerShell `Get-ChildItem`**

```
ilinux://command?cmd=Get-ChildItem&platform=powershell
```

---

## 2. 每日測驗

直接跳轉到**每日測驗**標籤。不會自動開始或跳過題目。

```
ilinux://quiz
```

---

## 3. 收藏

開啟設定導覽下的**收藏**列表。

```
ilinux://favorites
```

---

## 4. 錯題本

### 4.1 列表

```
ilinux://wrong
```

等效別名：

```
ilinux://mistakes
ilinux://wrongquestions
```

### 4.2 單條紀錄 → 指令詳情

`record` 為有效 UUID 時，開啟該錯題對應指令的詳情（紀錄與指令仍存在時）。

```
ilinux://wrong?record=550e8400-e29b-41d4-a716-446655440000
```

UUID 無效或紀錄已刪除時，回退到錯題列表或跳過導覽。

---

## 5. 主畫面捷徑

長按 iLinux 圖示 → 最多 **4** 項。在 **設定 → 主畫面捷徑** 設定（7 項可選、可排序、可恢復預設）。

| 選項 | 註冊 type | 圖示 | 開啟 |
|------|-----------|------|------|
| 搜尋 | `iLinux://search` | magnifyingglass | **指令**頁 + 啟動搜尋列 |
| 每日測驗 | `iLinux://quiz` | checklist | **每日測驗**標籤 |
| 收藏 | `iLinux://favorites` | star.fill | **收藏**列表 |
| 錯題本 | `iLinux://wrong` | xmark.bin.fill | **錯題本**列表 |
| 分類 | `iLinux://categories` | rectangle.grid.2x2.fill | **分類**標籤 |
| 傳送回饋 | `iLinux://feedback` | envelope.fill | 應用內郵件（或 `mailto:` 回退） |
| 評分 | `iLinux://review` | star.bubble.fill | StoreKit 評分 |

**首次安裝預設：** 搜尋 · 每日測驗 · 收藏 · 傳送回饋。

**僅捷徑通道**（`ILinuxDeepLink.parse` / `onOpenURL` **不處理**）：

- `iLinux://search`
- `iLinux://categories`
- `iLinux://feedback`
- `iLinux://review`

請透過**長按圖示**觸發；在捷徑中用 **開啟 URL** 開啟上述位址**可能無效**。

**遺留 type（仍路由）：**

| Type | 行為 |
|------|------|
| `iLinux://love` | 應用內 Safari 開啟作者部落格（舊版靜態捷徑） |

---

## 6. 小工具深度連結

小工具點擊使用 `WidgetDeepLink` 建構的相同 URL：

| 小工具 | 點擊目標 | URL |
|--------|----------|-----|
| 每日指令 | 指令詳情 | `iLinux://command?cmd=<id>&platform=<linux\|cmd\|powershell>` |
| 分類焦點 | 範例指令 | `iLinux://command?cmd=<id>&platform=<platform>` |
| 測驗一覽 | 每日測驗 | `iLinux://quiz` |
| 收藏速覽 | 收藏 / 單列指令 | `iLinux://favorites` / `iLinux://command?cmd=<id>&platform=<platform>` |
| 錯題速覽 | 錯題本 / 單列紀錄 | `iLinux://wrong` / `iLinux://wrong?record=<UUID>` |

小工具連結由 `WidgetDeepLink` 建構，命令連結均含 **`platform`**。

**每日指令隨機刷新按鈕**（iOS 17+ App Intent）僅重新整理時間軸，**不使用 URL**。

---

## Apple 捷徑

### 開啟指定指令

```
ilinux://command?name=systemctl
```

### 每日提醒 → 做測驗

```
ilinux://quiz
```

在個人自動化（如平日 9:00）中新增 **開啟 URL**。

### 複習錯題

```
ilinux://wrong
```

### 開啟收藏

```
ilinux://favorites
```

---

## 啟動行為

| 場景 | 流程 |
|------|------|
| **冷啟動 — 捷徑** | `ShortcutSceneDelegate` → `PendingShortcutBuffer` → `ShortcutObserver.onAppear` → `dispatch` |
| **熱啟動 — 捷徑** | Scene 回呼 → 通知 → `dispatch` |
| **冷啟動 — onOpenURL** | `handleIncomingURL` → `pendingDeepLink` → `RootTabView` 導覽 |
| **回饋/評分（冷啟動）** | 延遲 **約 0.4 秒**，等待 sheet / StoreKit 就緒 |
| **搜尋捷徑** | `searchPulse` → 展開搜尋列（iOS 17+ 自動聚焦） |
| **未知指令 ID** | 解析成功但跳過導覽 — 無彈窗 |

---

## 鍵盤快捷鍵

### iPad 與 Mac（共用）

⌘F 搜尋；⌘1–⌘4 切換四區。自動聚焦需 iOS 17.0+ / macOS 14.0+。

### 僅 Mac

⌘, 設定；⌘[/Esc 返回；⌘←/→ 分類；測驗 1–4 / ⌘R / Return。

---

## 不支援與無效 URL

| URL | 結果 |
|-----|------|
| `ilinux://command`（無 `name`/`cmd`） | 忽略 |
| `ilinux://command?name=NotARealCmd` | 忽略 |
| `ilinux://search` 經捷徑開啟 | **不**經 `ILinuxDeepLink` 解析 |
| `ilinux://categories` / `feedback` / `review` 同上 | 請用主畫面捷徑 |
| 非 `ilinux` Scheme | 忽略 |

---

## 故障排查

**冷啟動點捷徑沒反應**

回饋、評分、郵件需啟動後約 0.4 秒。可進應用後再試，或稍等片刻。

**搜尋捷徑在 iOS 16 不自動聚焦**

iOS 17+ 才支援 `searchable` 的 `isPresented`。iOS 16 仍會開啟指令頁，需手動點搜尋框。

**小工具點擊未開啟預期指令**

確認指令 ID 與目前版本內建庫一致；小工具使用 `cmd=` 且 ID 須完全匹配。

**捷徑標題語言不對**

在 **設定 → 語言** 切換 — 應用會自動重新註冊捷徑項。

**網頁裡點連結無效**

確認使用 `ilinux://`，且由系統開啟（備忘錄/訊息），而非被內建瀏覽器攔截自訂 Scheme。

---

[返回愛 Linux 支援頁](./) &middot; [常見問題](faq) &middot; [隱私政策](privacy)

</section>
