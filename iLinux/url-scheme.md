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

[Back to iLinux Support](../) &middot; [FAQ](../faq) &middot; [Privacy Policy](../privacy)

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

[返回爱 Linux 支持页](../) &middot; [常见问题](../faq) &middot; [隐私政策](../privacy)

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

[返回愛 Linux 支援頁](../) &middot; [常見問題](../faq) &middot; [隱私政策](../privacy)

</section>
<section lang="ja" markdown="1">

iLinuxは** `ilinux://` **をサポートしています(また、** `iLinux://` **を記述) URLスキームは、**iPhone、iPad、Macでディープリンクします** - コマンド詳細(Linux、CMD、PowerShell)、デイリークイズ、お気に入り、またはSafariから間違った回答ブック、別のアプリ、ウィジェットタップ(iOS / iPad)、またはAppleショートカットを開きます。

コマンド URL は、オプションの ** `ilinux://` ** クエリパラメーターを受け入れますので、ウィジェットのタップとショートカットは Windows エントリを正しく開くことができます。

**ホーム画面クイックアクション**(**iOS / iPadのみのアプリアイコンを長押し**)カバー検索、カテゴリ、フィードバックとレート。 Macユーザーは、代わりに**iLinux**メニューとキーボードショートカットを使うことができます。

> **重要:** iLinux は ** リファレンスと学習アプリ ** です。 URL は、****** 内の** Navigate のみリンクします。 Linux コマンドを実行し、SSH セッションを開くか、リモートサーバに接続しない

## プロトコル仕様


```
ilinux://<host>[/<path>][?query]
iLinux://<host>[/<path>][?query]   ← same scheme, case-insensitive
```


| Rule | 詳細を見る |
|------|--------|
| **Scheme** | `ilinux` / `iLinux` — ケースを無感覚に比較 |
| **Host routing** | プライマリルータはURL **host**です。 いくつかのパスも受け付けています(以下を参照してください) |
| **Command detail** | ホスト `command` **or** パス `/command` |
| **Command ID** | クエリ `name=<id`> ** または** `cmd=<id>` — はバンドルされたコマンドキー (例えば `ls`、`grep`、`dir`、`Get-ChildItem`) と一致しなければなりません。 |
| **Platform** | 省略時に `platform=<value>` をリクエストします。省略時に**Linux** にデフォルト値を指定します。 |
| **Quiz** | ホスト `quiz` **or** パス `/quiz` |
| **Favourites** | ホスト `favorites` **or** パス `/favorites` |
| **Wrong book** | ホスト `wrong`、`mistakes`、または `wrongquestions`;`/wrong` または `/mistakes` も受け入れる |
| **Wrong record** | 間違ったブック URL で `record=<UUID>` をクエリー — レコードのコマンド詳細を開く |
| **Query parameters** | 他のプレフィルパラメータはサポートされていません |
| **Parser** | "ILinuxDeepLink.parse( :)` — `onOpenURL` → `AppRouter.pendingDeepLink` で消費 |

**2つの配達チャネル**

| Channel | Handled by | 例 |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ILinuxDeepLink.parse` → `RootTabView` | `command`、`quiz`、`favorites`、`wrong` |
| **Home Screen Quick Action** | `ShortcutSceneDelegate` → `ShortcutObserver.dispatch` | `search`、`categories`、`feedback`、`review`、`quiz`/`favorites`/`wrong`をオーバーラップ |

クイックアクションタイプは、タイプ文字列にマッチする** `ilinux://` **を使うので、 `iLinux://` とレガシーのバリアントも正しくルーティングします。

---

## 1. コマンド詳細

単一のバンドルされたコマンドで詳細ページを開きます。

| Parameter | Required | コンテンツ |
|-----------|----------|-------------|
| `name` | One of `name` / `cmd` | コマンドID(プラットフォームJSONバンドルの辞書キー) |
| `cmd` | One of `name` / `cmd` | ウィジェットリンクで使用される `name` の同義語 |
| `platform` | No | シェルライブラリ: 下の表を参照してください。 デフォルトで**Linux** |

** `ilinux://` 値** (ケースインセンティブ):

| Value | Shell library | エイリアス |
|-------|---------------|---------|
| *(omit)* or `linux` | Linux (1050 commands) | — |
| `cmd` | CMD / Batch (300 commands) | `batch`, `bat` |
| `powershell` | PowerShell (300 commands) | `ps`, `pwsh` |

**行動**

- **Commands**タブに切り替えて、要求された**shellプラットフォーム**を選択し、解決されたコマンドで`CommandDetailView`を押します。
- ID が **unknown または empty** の場合、リンクは **silently無視** (エラー UI なし) です。
- コマンド ID は **case-pathy** で、バンドルされた JSON キーを正確に一致しなければなりません(通常、`docker` など)。

**オープン `ilinux://` **


```
ilinux://command?name=ls
```


** `ilinux://` (Linux、デフォルト)を開く**


```
ilinux://command?cmd=grep
```


**CMDを開く `ilinux://` **


```
ilinux://command?cmd=dir&platform=cmd
```


PowerShell を開く `ilinux://` **


```
ilinux://command?cmd=Get-ChildItem&platform=powershell
```


**クラウドネイティブLinuxの例**


```
ilinux://command?name=docker
```


---

## 2. 毎日のクイズ

**毎日のクイズ**タブに直接ジャンプします。 ****自動起動や質問をスキップしません。


```
ilinux://quiz
```


パスの形態(また受け入れられます):


```
ilinux:///quiz
```


---

## 3. お気に入り

[設定] ナビゲーションで [**Favourites**] リストを開きます。


```
ilinux://favorites
```


パスの形態(また受け入れられます):


```
ilinux:///favorites
```


---

## 4. 間違った答え帳

### 4.1 リスト

[設定] ナビゲーションの [*間違った回答ブック**] リストを開きます。


```
ilinux://wrong
```


エイリアス(同じ行動):


```
ilinux://mistakes
ilinux://wrongquestions
```


### 4.2 シングルレコード→コマンド詳細 `ilinux://` が保存された間違ったエントリの有効な UUID である場合、アプリは、**Commands**タブを開き、レコードのコマンド(レコードとコマンドがまだ存在する場合)の詳細を押します。

| Parameter | Required | フォーマット |
|-----------|----------|--------|
| `record` | Yes | UUID 文字列、例えば `550e8400-e29b-41d4-a716-446655440000` |


```
ilinux://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


UUIDが無効であるか、レコードが削除された場合、ナビゲーションは間違ったブックリストに戻り、スキップされます。

---

## 5. ホーム スクリーンの速い行為

iLinux のアイコンを長押しする → 4** アクションまで。 *Settings → Home Screen Shortcuts** (7オプション、reorder、デフォルトへのリセット) で設定します。

| Option | Registered `type` | SF Symbol | オープン |
|--------|-------------------|-----------|--------|
| Search | `iLinux://search` | magnifyingglass | **コマンド**タブ+検索バーの有効化 |
| Daily Quiz | `iLinux://quiz` | checklist | **デイリー・クイズ**タブ |
| Favourites | `iLinux://favorites` | star.fill | **お気に入り** リスト |
| Wrong Answer Book | `iLinux://wrong` | xmark.bin.fill | **間違った回答ブック**リスト |
| Categories | `iLinux://categories` | rectangle.grid.2x2.fill | **カテゴリー**タブ |
| Send Feedback | `iLinux://feedback` | envelope.fill | アプリ内メールコンポーズ(または `mailto:` フォールバック) |
| Rate App | `iLinux://review` | star.bubble.fill | StoreKitレビュープロンプト |

**最初のインストールのデフォルト選択:**検索·毎日のクイズ·お気に入り·フィードバックを送信.

**クイックアクションのみの宛先** ( `ilinux://` / `iLinux://` で処理されていない)

- `iLinux://search`
- `iLinux://categories`
- `iLinux://feedback`
- `iLinux://review`

*long-press icon** または Quick Action パイプラインを介して同じタイプを投稿することでこれらを使用して、ショートカットで開く**Open URL**は、アプリが後で明示的なホストをパースしない限り、**動作しない場合があります。

**レガシータイプ(固定):**

| Type | ビーキャビア |
|------|-----------|
| `iLinux://love` | アプリ内のSafariシート(旧静的ショートカット)で作者のブログを開く |

---

## 6.ウィジェットディープリンク

Widget は `iLinux://` によって構築された URL と同じ `ilinux://` を使用します。

| Widget | Tap target | 忍耐 を 生み出 し なさ い . |
|--------|------------|-----|
| Daily Command | Command detail | `iLinux://command?cmd=<id>&platform=<linux\ | cmd\ | パワーシェル>` |
| Category Spotlight | Sample command | `iLinux://command?cmd=<id>&platform=<platform>` |
| Quiz Glance | Daily Quiz | `iLinux://quiz` |
| Favourites Glance | Favourites (or per-row command) | `iLinux://favorites`/`iLinux://command?cmd=<id>&platform=<platform>` |
| Wrong Book Glance | Wrong book (or per-row record) | `iLinux://wrong`/`iLinux://wrong?record=<UID>` |

ウィジェット URL は `ilinux://` で作成され、コマンド タップの [** `iLinux://` **] も含まれています。 プラットフォームは、**Settings → Widgets → Widgetコマンドライブラリ**(Linux / CMD / PowerShell)にマッチします。

**デイリーコマンドシャッフルボタン**(iOS 17+、App Intent)はウィジェットのタイムラインのみをリロードします。** URLは使用しません。

---

## Appleのショートカット

### 名前をコピーした後にコマンドを開く

1.**入力からテキストを取得する**
2.**URLを開く** → `ilinux://` + テキスト

またはハード コード Linux:


```
ilinux://command?name=systemctl
```


CMDコマンドを開きます。


```
ilinux://command?cmd=ipconfig&platform=cmd
```


### 毎日の勉強のリマインダー → クイズ


```
ilinux://quiz
```


個人的なオートメーション(例:毎週9:00)に** URLを開く

### 間違った回答を確認する


```
ilinux://wrong
```


### フォーカスモードショートカットからお気に入りを開く


```
ilinux://favorites
```


---

## Behaviourを起動

アプリケーションが URL または Quick Action を受け取る場合:

| Scenario | フローリング |
|----------|------|
| **Cold start — Quick Action (iOS/iPad only)** | 「ショートカットキー」→「PendingShortcutBuffer」→「ショートカットObserver.onAppear」→「dispatch(type:)」 |
| **Warm start — Quick Action (iOS/iPad only)** | シーンコールバック → 通知 → `dispatch(type:)` |
| **Cold / warm — `onOpenURL` (iOS, iPad, Mac)** | `AppRouter.handleIncomingURL` → `pendingDeepLink` → `RootTabView.onChange` は、 |
| **Feedback / Rate (cold start)** | `deferSheetWork` 遅延**~0.4 s** メールシート / StoreKit はアクティブなウィンドウシーン |
| **Search quick action** | `openSearchTab()` → `searchPulse += 1` → `BrowseCommandsView` の検索 (iOS 17 +: `isPresented` による自動焦点) |
| **Unknown command ID** | ディープリンクがパースされたが、ナビゲーションがスキップされた — アラートなし |

---

## キーボードショートカット

### iPadとMac(共有)

Mac共有のiPadと**iLinux**メニューのハードウェアキーボード:

| Shortcut | アクション |
|----------|--------|
| ⌘F | コマンドタブ+検索(iOS上で検索クイックアクションとして意図) |
| ⌘1 | コマンドタブ |
| ⌘2 | カテゴリー タブ |
| ⌘3 | 毎日のクイズタブ |
| ⌘4 | 設定タブ |

⌘F経由でオートフォーカスを検索するには、**iOS 17.0 +**または**macOS 14.0 +**が必要です。

### Macのみ

| Shortcut | アクション |
|----------|--------|
| ⌘, | 設定タブ |
| ⌘[ / Esc | ポップアップナビゲーションスタック(バック) |
| ⌘← / ⌘→ | 前 / 次のカテゴリ(カテゴリタブ) |
| 1–4 | クイズの回答オプションを選択 |
| ⌘R | リシャッフルデイリークイズ |
| Return | 次のクイズ質問(回答後) |

ディープリンク( `ilinux://` )とメニューショートカットは、iOS上でMac上で同じアプリ内ルータを使用します。

---

## サポートされていないURLと無効なURL

| URL | Result |
|-----|--------|
| `ilinux://command` (no `name` / `cmd`) | 無視される |
| `ilinux://command?name=NotARealCmd` | 無視される(解決されたプラットホームのための図書館でないID) |
| `ilinux://command?cmd=dir` (no platform) | Windows CMD 用の `platform=cmd` を使う |
| `ilinux://search` via Shortcuts Open URL | **「ILinuxDeepLink」で解析されていない — **iOS/iPad**、または**Mac/iPad**で⌘Fを使う |
| `ilinux://categories` via Shortcuts Open URL | 上記と同じ |
| `ilinux://feedback` / `ilinux://review` via Open URL | 上記と同じ |
| Non-`ilinux` schemes | 無視される |

---

## トラブルシューティング

**ショートカットはアプリを開きますが、何も発生しません(コールド起動)**

フィードバック、率および郵便シートは進水の後で~0.4 sを必要とします。 アプリ内からもう一度お試しください。またはコールドスタートでしばらくお待ちください。

**検索クイックアクションは、検索フィールドに焦点を合わせません(iOS 16)**

オートフォーカスはiOS 17以降が必要です。 iOS 16 では、コマンドタブが開きます。 手動で検索フィールドをタップします。

**Widget Tap は期待するコマンドが開けない**

正しい**platform**のためにインストールされたアプリバージョンにまだコマンドが存在することを確認してください。 ウィジェットのリンクは、 `ilinux://` + `iLinux://` を使用し、厳密なコマンド ID が必要です。例: `platform` は、デフォルトの Linux ライブラリではなく、 `ilinux` を必要とします。

**クイックアクションのタイトルは間違った言語です**

*Settings → Language** で言語を変更します。アプリはショートカット項目を自動的に再登録します。

**ディープリンクは、デバイス上で動作しますが、Webページからではありません**

リンクは、カスタムスキームを除去するアプリ内ブラウザでブロックされていない、システム(ノート/メッセージのタップ)によって開いています。

---

[iLinuxサポートに戻る](./) &middot; [FAQ](../faq) &middot; [プライバシーポリシー](./privacy)

</section>
<section lang="ko" markdown="1">

iLinux는 ** `ilinux://` **를 지원합니다. (또한 작성된 ** `iLinux://` **) URL 계획 **iPhone, iPad 및 Mac에서 깊은 링크 ** — 오픈 명령 세부 사항 (Linux, CMD 또는 PowerShell), Daily Quiz, Favourites 또는 Wrong 응답 책 사파리, 다른 응용 프로그램, 위젯 탭 (iOS / iPad), 또는 Apple Shortcuts.

명령 URL은 옵션 ** `ilinux://` ** 쿼리 매개 변수를 수락하므로 위젯 탭 및 단축키는 Windows 항목을 올바르게 열 수 있습니다.

**홈 화면 Quick Actions** ( **iOS/iPad 만 **) 커버 검색, 카테고리, 피드백 및 비율. Mac 사용자는 ** iLinux** 메뉴와 키보드 단축키를 사용할 수 있습니다.

> ** 중요 : ** iLinux는 ** 설정 및 학습 앱**입니다. URL 링크는 ** 앱 내부에 **navigate만 있습니다. 그들은**not** Linux 명령을 실행하고 SSH 세션을 열고 원격 서버에 연결합니다.

## 프로토콜


```
ilinux://<host>[/<path>][?query]
iLinux://<host>[/<path>][?query]   ← same scheme, case-insensitive
```


| Rule | 제품 정보 |
|------|--------|
| **Scheme** | `ilinux`/`iLinux` — case-insensitively 비교 |
| **Host routing** | 기본 라우터는 URL ** 호스팅 **; 일부 경로도 허용 (아래 참조) |
| **Command detail** | 호스트 `command` ** 또는** 경로 `/command` |
| **Command ID** | Query `name=<id>` ** 또는** `cmd=<id>` - 번들 명령 키 (예: `ls`, `grep`, `dir`, `Get-ChildItem`)와 일치해야 합니다. |
| **Platform** | Query `platform=<value>` — 선택 사항; 기본값은 **Linux** 때 omitted |
| **Quiz** | 호스트 `quiz` ** 또는** 경로 `/quiz` |
| **Favourites** | 호스트 `favorites` ** 또는** 경로 `/favorites` |
| **Wrong book** | 호스트 `wrong`, `mistake`, 또는 `wrongquestions`; 경로 `/wrong` 또는 `/mistake`도 허용 |
| **Wrong record** | Query `record=<UUID>`는 잘못된 책 URL에 - 레코드의 명령 세부 정보를 엽니다. |
| **Query parameters** | 다른 pre-fill 모수는 지원됩니다 |
| **Parser** | `ILinuxDeepLink.parse( :)` - `onOpenURL` → `AppRouter.pendingDeepLink`를 통해 소모 |

** 2개의 납품 수로 **

| Channel | Handled by | 예시 |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ILinuxDeepLink.parse` → `RootTabView` | `command`, `quiz`, `favorites`, `wrong` |
| **Home Screen Quick Action** | `ShortcutSceneDelegate` → `ShortcutObserver.dispatch` | `search`, `categories`, `feedback`, `review`, plus overlapping `quiz`/`favorites`/`wrong` |

Quick-action type use ** `ilinux://` ** type string에 매칭하므로, `iLinux://` 와 레거시 변형은 여전히 올바르게 변형됩니다.

---

## 1. 명령 세부사항

단일 번들 명령의 세부 페이지를 엽니다.

| Parameter | Required | 이름 * |
|-----------|----------|-------------|
| `name` | One of `name` / `cmd` | 명령 ID (플랫폼 JSON 번들의 사전 키) |
| `cmd` | One of `name` / `cmd` | 동의어: `name` — 위젯 링크에 의해 사용 |
| `platform` | No | Shell 라이브러리: 아래 표 참조. **Linux**에 기본값 |

** `ilinux://` 값** (case-insensitive):

| Value | Shell library | 이름 * |
|-------|---------------|---------|
| *(omit)* or `linux` | Linux (1050 commands) | — |
| `cmd` | CMD / Batch (300 commands) | `배치`, `배치` |
| `powershell` | PowerShell (300 commands) | `ps`, `pwsh` |

**Behaviour **

- **Commands** 탭으로 전환하여 요청된 ** 쉘 플랫폼**을 선택하고, 해결된 명령의 `CommandDetailView`를 밀어줍니다.
- ID가 ** 알려지지 않았거나 빈 **이면, 링크가 **가 무시됩니다 ** (오류 UI 없음).
- Command IDs는 **case-sensitive**이며, 묶음 JSON 키를 정확히 일치해야 합니다(일반적으로 lowcase, 예. `docker`, not `Docker`).

** 오픈 `ilinux://` **


```
ilinux://command?name=ls
```


**Open `ilinux://` (리눅스, 기본) **


```
ilinux://command?cmd=grep
```


CMD `ilinux://` **을 엽니다.


```
ilinux://command?cmd=dir&platform=cmd
```


**Open PowerShell `ilinux://` **


```
ilinux://command?cmd=Get-ChildItem&platform=powershell
```


**Cloud-native Linux 예**


```
ilinux://command?name=docker
```


---

## 2. 매일 퀴즈

**Daily Quiz** 탭으로 이동합니다. ** 자동 시작 또는 건너뛰기 질문.


```
ilinux://quiz
```


경로 형태 (또한 받아들여지는):


```
ilinux:///quiz
```


---

## 3. 특징

**Favourites ** 설정 탐색 아래 목록.


```
ilinux://favorites
```


경로 형태 (또한 받아들여지는):


```
ilinux:///favorites
```


---

## 4. 잘못된 대답 책

### 4.1 목록

** 잘못된 답변 책 ** 설정 탐색 아래 목록.


```
ilinux://wrong
```


Aliases (같은 행동):


```
ilinux://mistakes
ilinux://wrongquestions
```


### 4.2 단일 레코드 → 명령 세부 사항

언제 `ilinux://` 는 저장 된 잘못 answer 항목의 유효 UUID, 응용 프로그램은 ** COMmands** 탭을 열고 그 기록의 명령에 대한 세부 사항을 밀어 (기록 및 명령이 여전히 존재 한 경우).

| Parameter | Required | 지원하다 |
|-----------|----------|--------|
| `record` | Yes | UUID 문자열, 예. `550e8400-e29b-41d4-a716-446655440000` |


```
ilinux://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


UUID가 유효하거나 기록이 삭제 된 경우, 탐색은 잘못된 책 목록으로 돌아가거나 건너 뛰는 것입니다.

---

## 5. 가정 스크린 빠른 활동

iLinux 아이콘 → 최대 **4** 작업.**Settings → Home Screen Shortcuts** (7 옵션, 다시 주문으로 드래그, 기본값으로 재설정).

| Option | Registered `type` | SF Symbol | 공지사항 |
|--------|-------------------|-----------|--------|
| Search | `iLinux://search` | magnifyingglass | **Commands** 탭 + 검색 표시 활성화 |
| Daily Quiz | `iLinux://quiz` | checklist | **Daily Quiz** 탭 |
| Favourites | `iLinux://favorites` | star.fill | **Favourites ** 목록 |
| Wrong Answer Book | `iLinux://wrong` | xmark.bin.fill | ** 잘못된 답변 책 ** 목록 |
| Categories | `iLinux://categories` | rectangle.grid.2x2.fill | **카테고리 ** 탭 |
| Send Feedback | `iLinux://feedback` | envelope.fill | In-app mail compose (또는 `mailto:` fallback) |
| Rate App | `iLinux://review` | star.bubble.fill | StoreKit 리뷰 |

** 첫 번째 설치의 기본 선택 :** 검색 · 일일 퀴즈 · Favourites · 피드백 보내기.

** Quick-action-only 대상 ** (에 의해 처리되지 않음 `ilinux://` / `iLinux://` ):

- `iLinux://search`````````
- `iLinux://카테고리`
- `iLinux://feedback`````
- `iLinux://리뷰`

**long-press icon** 또는 Quick Action 파이프라인을 통해 동일한 유형을 게시함으로써, Shortcuts**Open URL**으로 열 수 있습니다 ** 앱이 나중에 명시된 호스트를 추가하지 않는 경우 작동하지 않을 수 있습니다.

**Legacy 타입 (실행):**

| Type | 채용 정보 |
|------|-----------|
| `iLinux://love` | in-app Safari 시트에서 저자 블로그를 엽니 다 (old static Shortcut) |

---

## 6. 위젯 딥 링크

위젯 탭은 같은 사용 `ilinux://` URL에 의해 내장 `iLinux://` :

| Widget | Tap target | 사이트 맵 |
|--------|------------|-----|
| Daily Command | Command detail | `iLinux://command?cmd=<id>&platform=<linux\ | cmd\ | 파워쉘>` |
| Category Spotlight | Sample command | `iLinux://command?cmd=<id>&platform=<platform>`` |
| Quiz Glance | Daily Quiz | `iLinux://quiz``````` |
| Favourites Glance | Favourites (or per-row command) | `iLinux://favorites`/`iLinux://command?cmd=<id>&platform=<platform>`` |
| Wrong Book Glance | Wrong book (or per-row record) | `iLinux://wrong`/`iLinux://wrong?record=<UUID>` |

Widget URL은 `ilinux://` 에 의해 만들어지고 항상 ** `iLinux://` ** 명령 탭에 포함되어 있습니다. 플랫폼 일치 ** 설정 → 위젯 → 위젯 명령 라이브러리 ** (Linux / CMD / PowerShell).

**Daily Command shuffle button** (iOS 17+, App Intent)는 위젯 타임라인만 다시 로드합니다. **는 URL을 사용하지 않습니다.

---

## Apple 바로가기

### 이름을 복사 한 후 명령을 엽니다.

1. ** 입력에서 텍스트를 가져옵니다 **
2. ** URL 열기 ** → `ilinux://` + 텍스트

또는 하드 코드 리눅스:


```
ilinux://command?name=systemctl
```


CMD 명령을 엽니다:


```
ilinux://command?cmd=ipconfig&platform=cmd
```


### 매일 공부 알림 → 퀴즈


```
ilinux://quiz
```


추가 ** 개인 자동화에서 URL** (예: 매주 9시).

### 잘못된 답변을 검토


```
ilinux://wrong
```


### Focus Mode Shortcut에서 즐겨 찾기


```
ilinux://favorites
```


---

## 시작 Behaviour

앱이 URL 또는 Quick Action을 수신할 때:

| Scenario | 제품정보 |
|----------|------|
| **Cold start — Quick Action (iOS/iPad only)** | `ShortcutSceneDelegate` → `PendingShortcutBuffer` → `ShortcutObserver.onAppear` → `dispatch(type:)` |
| **Warm start — Quick Action (iOS/iPad only)** | 장면 콜백 → 알림 → `dispatch(type:)` |
| **Cold / warm — `onOpenURL` (iOS, iPad, Mac)** | `AppRouter.handleIncomingURL` → `pendingDeepLink` → `RootTabView.onChange` 탐색 |
| **Feedback / Rate (cold start)** | `deferSheetWork` 지연 **~0.4 s** 그래서 메일 시트 / StoreKit는 활성 창 장면을 가지고 |
| **Search quick action** | `openSearchTab()` → `searchPulse += 1` → `BrowseCommandsView` 검색(iOS 17+: `isPresented`를 통해 자동 초점) |
| **Unknown command ID** | 딥 링크 파싱하지만 탐색 건너뛰기 — 알림 없음 |

---

## 키보드 단축키

### iPad 및 Mac (공유)

iPad 및 **iLinux** 메뉴에서 하드웨어 키보드:

| Shortcut | - 연혁 |
|----------|--------|
| ⌘F | 명령 탭 + 검색 (iOS에서 빠른 행동 검색과 동일) |
| ⌘1 | 명령 탭 |
| ⌘2 | 카테고리 탭 |
| ⌘3 | 매일 퀴즈 탭 |
| ⌘4 | 설정 탭 |

⌘F를 통해 자동 초점은 **iOS 17.0+** 또는 **macOS 14.0+**를 요구합니다.

### Mac 전용

| Shortcut | - 연혁 |
|----------|--------|
| ⌘, | 설정 탭 |
| ⌘[ / Esc | Pop 항법 더미 (뒤) |
| ⌘← / ⌘→ | 이전 / 다음 범주 (카테고리 탭) |
| 1–4 | 퀴즈 응답 옵션 선택 |
| ⌘R | 일일 퀴즈 |
| Return | 다음 퀴즈 질문 (응답 후) |

딥 링크 ( `ilinux://` ) 및 메뉴 단축키는 iOS에서 Mac에서 같은 앱 라우터를 사용합니다.

---

## 지원 및 잘못된 URL

| URL | Result |
|-----|--------|
| `ilinux://command` (no `name` / `cmd`) | 이름 * |
| `ilinux://command?name=NotARealCmd` | Ignored (해결된 플랫폼을위한 라이브러리에 있지 않음) |
| `ilinux://command?cmd=dir` (no platform) | Opens**Linux** 라이브러리 — Windows CMD용 `platform=cmd`를 사용합니다. |
| `ilinux://search` via Shortcuts Open URL | **Not**는 `ILinuxDeepLink`에 의해 파싱 — **iOS/iPad**, 또는 ⌘F on **Mac/iPad**에서 빠른 동작을 사용 |
| `ilinux://categories` via Shortcuts Open URL | 위와 같 |
| `ilinux://feedback` / `ilinux://review` via Open URL | 위와 같 |
| Non-`ilinux` schemes | 이름 * |

---

## 문제 해결

**Shortcut은 앱을 열었지만 아무런 일이 없습니다 (cold launch)**

피드백, 비율 및 우편 시트 필요 ~0.4 출시 후 s. 앱 내부에서 다시 시도, 또는 추운 시작에 순간을 기다립니다.

**검색 빠른 동작은 검색 필드에 초점을 맞추지 않습니다 (iOS 16)**

자동 초점은 iOS 17+를 요구합니다. iOS 16에서 명령 탭은 여전히 열려 있습니다. 검색 필드를 수동으로 탭합니다.

**Widget 탭은 예상 명령을 열지 않습니다 **

명령은 여전히 올바른 **platform**에 대한 설치된 앱 버전에서 존재합니다. 위젯 링크 사용 `ilinux://` + `iLinux://` 그리고 정확한 명령 ID가 필요합니다. 예: `platform` 필요 `ilinux` , 기본 Linux 라이브러리가 아닙니다.

**Quick-action 제목은 잘못된 언어입니다 **

언어 변경 **설정 → 언어** — 앱 등록 단축키 항목 자동.

**Deep 링크는 장치에서 작동하지만 웹 페이지에서 작동하지 **

링크를 사용하여 계획 확인 `ilinux://` 및 시스템에 의해 열 (주/메시지에서 제거), 사용자 정의 계획을 스트립 인앱 브라우저에 의해 차단되지.

---

[Back to iLinux Support](../) &middot; [FAQ](../faq) &middot; [개인정보 보호 정책](../privacy)

</section>
<section lang="ru" markdown="1">

iLinux поддерживает ** `ilinux://` ** (также пишется ** `iLinux://` **) URL-схема глубоких ссылок на **iPhone, iPad и Mac** — открытая командная деталь (Linux, CMD или PowerShell), Daily Quiz, Favourites или Wrong Answer Book от Safari, другое приложение, нажатие виджета (iOS/iPad) или ярлыки Apple.

Командные URL-адреса принимают необязательный параметр запроса ** `ilinux://` **, поэтому нажатия виджетов и ярлыки могут правильно открывать записи Windows.

**Быстрые действия на домашнем экране** (долго нажимайте значок приложения только на **iOS/iPad**) охватывают поиск, категории, обратную связь и рейтинг. Вместо этого пользователи Mac могут использовать меню **iLinux** и ярлыки клавиатуры.

> **Important: ** iLinux - это ** справочное и обучающее приложение **. URL-ссылки только ** перемещаются внутри приложения **. Они выполняют команды Linux, открывают сеансы SSH или подключаются к удаленным серверам.

## Спецификация протокола


```
ilinux://<host>[/<path>][?query]
iLinux://<host>[/<path>][?query]   ← same scheme, case-insensitive
```


| Rule | Подробнее |
|------|--------|
| **Scheme** | «ilinux» / «iLinux» — сравниваемый случай нечувствительно |
| **Host routing** | Основным маршрутизатором является URL **host **; некоторые пути также принимаются (см. ниже). |
| **Command detail** | Ведущий "командир"** или** путь "/командир" |
| **Command ID** | Запрос «имя = <id>» ** или ** «cmd = <id>» — должен совпадать с командным ключом (например, «ls», «grep», «dir», «Get-ChildItem») |
| **Platform** | Запрос «platform=<value>» — необязательный; по умолчанию **Linux** |
| **Quiz** | Ведущий "виза" ** или** путь "/виза" |
| **Favourites** | Ведущий «любимые» ** или** путь «/любимые» |
| **Wrong book** | Принимать «неправильные», «ошибки» или «неправильные вопросы»; путь «/неправильный» или «/ошибки» также принимается |
| **Wrong record** | Запрос «record=<UUID>» на URL-адресе неправильной книги — открывается командная деталь этой записи |
| **Query parameters** | Другие параметры предварительного заполнения не поддерживаются |
| **Parser** | «ILinuxDeepLink.parse( :)» — потребляется через «onOpenURL» → «AppRouter.pendingDeepLink» |

** Два канала доставки**

| Channel | Handled by | Примеры |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ILinuxDeepLink.parse` → `RootTabView` | «командный», «викторина», «любимые», «неправильный» |
| **Home Screen Quick Action** | `ShortcutSceneDelegate` → `ShortcutObserver.dispatch` | «поиск», «категории», «обратная связь», «обзор» плюс перекрывающиеся «викторины» / «любимые» / «неправильные» |

Типы быстрого действия используют ** `ilinux://` **, совпадающие по строке типа, поэтому как `iLinux://` , так и унаследованные варианты все еще маршрутизируются правильно.

---

## 1 Командная деталь

Откройте страницу детализации для одной команды.

| Parameter | Required | Описание |
|-----------|----------|-------------|
| `name` | One of `name` / `cmd` | Command ID (словарь в платформе JSON) |
| `cmd` | One of `name` / `cmd` | Синоним для «имя» — используется для ссылок виджетов |
| `platform` | No | Библиотека Shell: см. таблицу ниже. По умолчанию: **Linux** |

** `ilinux://` значения ** (случай нечувствительный):

| Value | Shell library | алиасы |
|-------|---------------|---------|
| *(omit)* or `linux` | Linux (1050 commands) | — |
| `cmd` | CMD / Batch (300 commands) | "batch", "bat" |
| `powershell` | PowerShell (300 commands) | "ps", "pwsh" |

** Поведение**

- Переключается на вкладку **Commands**, выбирает запрашиваемую платформу **shell** и нажимает «CommandDetailView» для решенной команды.
- Если идентификатор * * неизвестен или пуст * *, ссылка * * молча игнорируется * * (без ошибок UI).
- Идентификаторы команд ** чувствительны к регистру ** и должны точно соответствовать пакетному ключу JSON (обычно нижний регистр, например, «докер», а не «докер»).

**Открыть `ilinux://` **


```
ilinux://command?name=ls
```


**Open `ilinux://` (Linux, по умолчанию)**


```
ilinux://command?cmd=grep
```


** Открытый CMD `ilinux://` **


```
ilinux://command?cmd=dir&platform=cmd
```


**Открытая PowerShell `ilinux://` **


```
ilinux://command?cmd=Get-ChildItem&platform=powershell
```


**Облачный пример Linux**


```
ilinux://command?name=docker
```


---

## 2. Daily Quiz

Перейдите непосредственно на вкладку **Daily Quiz**. Не запускает и не пропускает вопросы.


```
ilinux://quiz
```


Форма пути (также принята):


```
ilinux:///quiz
```


---

## 3. Любимые

Откройте список **Favourites** в разделе Навигация по настройкам.


```
ilinux://favorites
```


Форма пути (также принята):


```
ilinux:///favorites
```


---

## 4 Неправильная книга ответов

### 4.1 Список

Откройте список «Книга неправильных ответов» в разделе «Навигация по настройкам».


```
ilinux://wrong
```


Алиазы (одно и то же поведение):


```
ilinux://mistakes
ilinux://wrongquestions
```


### 4.2 Единая запись и командная деталь

Когда `ilinux://` является действительным UUID сохраненной записи с неправильным ответом, приложение открывает вкладку **Commands** и нажимает детали для команды этой записи (если запись и команда все еще существуют).

| Parameter | Required | Формат |
|-----------|----------|--------|
| `record` | Yes | UUID строка, например '550e8400-e29b-41d4-a716-446655440000' |


```
ilinux://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


Если UUID недействителен или запись была удалена, навигация возвращается в список неправильных книг или пропускается.

---

## 5. Home Экран Быстрые действия

Длинно нажмите значок iLinux → до **4** действий. Настройка в **Settings → Home Screen Shortcuts** (7 опций, перетаскивание на переупорядочение, сброс по умолчанию).

| Option | Registered `type` | SF Symbol | Открытие |
|--------|-------------------|-----------|--------|
| Search | `iLinux://search` | magnifyingglass | **Командная** вкладка + активировать строку поиска |
| Daily Quiz | `iLinux://quiz` | checklist | ** Daily Quiz** |
| Favourites | `iLinux://favorites` | star.fill | **Любимые** список |
| Wrong Answer Book | `iLinux://wrong` | xmark.bin.fill | ** Неправильная книга ответов** |
| Categories | `iLinux://categories` | rectangle.grid.2x2.fill | **Категория ** Табличка |
| Send Feedback | `iLinux://feedback` | envelope.fill | Композиция электронной почты в приложении (или «mailto:» Fallback) |
| Rate App | `iLinux://review` | star.bubble.fill | Обсуждение StoreKit Quick |

** Выбор по умолчанию при первой установке: ** Поиск · Ежедневный поиск · Любимые · Отправить обратную связь.

** Пункты назначения только для быстрого действия** (не обрабатываются `ilinux://` / `iLinux://` ):

- "iLinux://поиск"
- iLinux://категории
- iLinux://feedback
- "iLinux://review"

Используйте их с помощью значка **long-press** или разместив тот же тип через конвейер Quick Action — открытие их с помощью ярлыков **Открытый URL** может **не работать, если приложение не добавляет явный анализ хоста позже.

** Тип наследства (по-прежнему маршрутизированный): **

| Type | поведение |
|------|-----------|
| `iLinux://love` | Открывает авторский блог в in-app Safari sheet (старый статичный ярлык) |

---

## 6. Widget Deep Links

Виджетные краны используют те же URL-адреса `ilinux://` , что и `iLinux://` :

| Widget | Tap target | URL |
|--------|------------|-----|
| Daily Command | Command detail | `iLinux://command?cmd=<id>&platform=<linux\ | cmd\ | PowerShell |
| Category Spotlight | Sample command | iLinux://command?cmd=<id>&platform=<platform> |
| Quiz Glance | Daily Quiz | "iLinux://quiz" |
| Favourites Glance | Favourites (or per-row command) | «iLinux://favorites» / «iLinux://command?cmd=<id>&platform=<platform>» |
| Wrong Book Glance | Wrong book (or per-row record) | «iLinux://wrong» / «iLinux://wrong?record» |

URL-адреса виджетов построены по `ilinux://` и всегда включают ** `iLinux://` ** для командных нажатий. Платформа соответствует **Настройки → Виджеты → Командная библиотека Виджета** (Linux / CMD / PowerShell).

Кнопка перетасовки **Daily Command (iOS 17+, App Intent) перезагружает только временную шкалу виджета — она не использует URL.

---

## Apple Shortcuts

### Откройте команду после копирования ее имени

1. ** Получить текст из ввода **
2. **Открытые URL** → `ilinux://` + Текст

Жесткий код Linux:


```
ilinux://command?name=systemctl
```


Откройте команду CMD:


```
ilinux://command?cmd=ipconfig&platform=cmd
```


### Ежедневное напоминание об исследовании → викторина


```
ilinux://quiz
```


Добавьте ** Открытые URL** в Персональную автоматизацию (например, каждый будний день в 9:00).

### Неправильные ответы


```
ilinux://wrong
```


### Открытые фавориты из режима Focus


```
ilinux://favorites
```


---

## Запуск поведения

Когда приложение получает URL-адрес или быстрое действие:

| Scenario | Поток |
|----------|------|
| **Cold start — Quick Action (iOS/iPad only)** | «ShortcutSceneDelegate» → «PendingShortcutBuffer» → «ShortcutObserver.onAppear» → «dispatch (тип:)» |
| **Warm start — Quick Action (iOS/iPad only)** | Обратный вызов сцены → уведомление → «отправка (тип:)» |
| **Cold / warm — `onOpenURL` (iOS, iPad, Mac)** | «AppRouter.handleIncomingURL» → «pendingDeepLink» → «RootTabView.onChange» |
| **Feedback / Rate (cold start)** | Задержки «deferSheetWork» **~0,4 с**, поэтому в почтовом листе / StoreKit есть активная сцена окна |
| **Search quick action** | «openSearchTab()» → «searchPulse += 1» → «BrowseCommandsView» представляет поиск (iOS 17+: автофокусировка через «isPresented») |
| **Unknown command ID** | Глубокая связь разобрана, но навигация пропущена - нет предупреждения |

---

## Клавишные ярлыки

### iPad & Mac (совместно)

Аппаратная клавиатура на iPad и меню **iLinux** на Mac Share:

| Shortcut | Меры |
|----------|--------|
| ⌘F | Закладка команд + поиск (то же намерение, что и быстрое действие поиска на iOS) |
| ⌘1 | Закладка команд |
| ⌘2 | Закладка категорий |
| ⌘3 | Ежедневная вкладка Quiz |
| ⌘4 | Настройка вкладки |

Поиск автофокусировки через .F требует **iOS 17.0+** или **macOS 14.0+**.

### только Mac

| Shortcut | Меры |
|----------|--------|
| ⌘, | Настройка вкладки |
| ⌘[ / Esc | Pop navigation stack (назад) |
| ⌘← / ⌘→ | Предыдущая / следующая категория (закладка категории) |
| 1–4 | Выберите вариант ответа на викторину |
| ⌘R | Ежедневная викторина |
| Return | Следующий вопрос (после ответа) |

Глубокие ссылки ( `ilinux://` ) и ярлыки меню используют тот же маршрутизатор в приложении на Mac, что и на iOS.

---

## Неподдерживаемые и недействительные URL

| URL | Result |
|-----|--------|
| `ilinux://command` (no `name` / `cmd`) | игнорируемый |
| `ilinux://command?name=NotARealCmd` | Ignored (ID не в библиотеке для платформы) |
| `ilinux://command?cmd=dir` (no platform) | **Библиотека Linux** — используйте «platform=cmd» для Windows CMD |
| `ilinux://search` via Shortcuts Open URL | **Not** парсируется по «ILinuxDeepLink» — используйте Quick Action на **iOS/iPad** или  F на **Mac/iPad** |
| `ilinux://categories` via Shortcuts Open URL | Как и выше |
| `ilinux://feedback` / `ilinux://review` via Open URL | Как и выше |
| Non-`ilinux` schemes | игнорируемый |

---

## устранение неполадок

Shortcut открывает приложение, но ничего не происходит (холодный запуск)

Обратная связь, тарифы и почтовые листы требуют ~ 0,4 с после запуска. Попробуйте еще раз внутри приложения или подождите немного на холодном старте.

Быстрые действия поиска не фокусируют поле поиска (iOS 16)

Автофокусировка требует iOS 17+. На iOS 16 все еще открывается вкладка команд; нажмите на поле поиска вручную.

**Widget tap не открывает ожидаемую команду**

Убедитесь, что команда все еще существует в вашей установленной версии приложения для правильной платформы. Ссылки виджета используют `ilinux://` + `iLinux://` и требуют точного идентификатора команды. Пример: `platform` нуждается в `ilinux` , а не в библиотеке Linux по умолчанию.

** Заголовки быстрого действия написаны не на том языке**

Изменение языка в ** Настройки → Язык ** — приложение автоматически перерегистрирует элементы ярлыков.

Глубокая ссылка работает на устройстве, но не с веб-страницы **

Подтвердите, что ссылка использует схему `ilinux://` и открывается системой (нажмите в Заметках/Сообщениях), а не блокируется браузером в приложении, который удаляет пользовательские схемы.

---

[Назад к поддержке iLinux](../) &middot; [FAQ](../faq) &middot; [Политика конфиденциальности](../privacy)

</section>
<section lang="th" markdown="1">

ilinux รองรับ~ c0  BAR ~ (ยังเขียนด้วย*  c1  BAR ~) ที่อยู่ URL วางรูปแบบลิงก์ลึกบน ~help, iPad และ Mac~ — รายละเอียดคําสั่งเปิด (inux, CMD หรือ Power Schell), The Daily Quiz, Septembers หรือหนังสือตอบผิดจาก Safari, apps อื่น ๆ, App (inOS/iPad) หรือ ปุ่มพิมพ์ลัดของแอปเปิล

ที่อยู่ URL คําสั่งยอมรับค่าตัวเลือก * BAR `ilinux://` BAR * พารามิเตอร์การค้นหา เพื่อให้วิดเจ็ตเคาะ และปุ่มพิมพ์ลัดสามารถเปิดรายการของวินโดวส์ได้อย่างถูกต้อง

~~~~หน้าจอทํางานด่วน~ (ยาว- กดไอคอนโปรแกรมบน ~iOS/iPad เท่านั้น~) ครอบคลุมการค้นหา, หมวดหมู่, แหล่งป้อนและอัตรา Mac ผู้ใช้สามารถใช้เมนู ~linux ~ และปุ่มพิมพ์ลัดแทน

> ** สืบค้นเมื่อ: ~ ilinux เป็นโปรแกรมที่อ้างอิงและเรียนรู้ **. ที่อยู่ URL เชื่อมโยงเท่านั้น ** พวกมันทํา -- ไม่ใช่ -- ประมวลผลคําสั่งลินุกซ์, เปิดวาระงาน SSH หรือเชื่อมต่อไปยังเซิร์ฟเวอร์ทางไกล

## การกําหนดโพรโทคอล


```
ilinux://<host>[/<path>][?query]
iLinux://<host>[/<path>][?query]   ← same scheme, case-insensitive
```


| Rule | รายละเอียด |
|------|--------|
| **Scheme** | 'ลินุกซ์' / 'ลินนุกซ์' เปรียบเทียบกรณีที่อ่อนไหว |
| **Host routing** | ตัวนําทางหลักคือที่อยู่ URL < load; บางพาธยอมรับ (ดูด้านล่างนี้) |
| **Command detail** | โฮสต์: คําสั่ง ~ หรือ ~ เส้นทาง '/ คําสั่ง' |
| **Command ID** | สืบค้น `name= <id> ~ หรือ~ 'cmd= (id)' -- ต้องตรงกับปุ่มคําสั่งแบบห่อ (e.g.', 'greep', 'dir',','Get-Inm') |
| **Platform** | สืบค้น `partiform= < value>' — ตัวเลือก; ค่าปริยายคือ ~lux~ เมื่อลบ |
| **Quiz** | โฮสต์! |
| **Favourites** | โฮสต์ 'ที่รัก' หรือ 'เส้นทาง' |
| **Wrong book** | ชัยฏอนมารร้ายเอ๋ย! จงผินหลังจากความจริงเถิดหรือ? แท้จริงแนวทาง (การลงโทษ) นั้นถูกตอบแทนเสมอ |
| **Wrong record** | สืบค้น `บันทึก= <UID>' บนที่อยู่ URL ไม่ถูกต้อง — เปิดรายละเอียดของคําสั่งบันทึก |
| **Query parameters** | ไม่สนับสนุนพารามิเตอร์ก่อนเติม |
| **Parser** | 'Lilinux deeplink.partse( )' — บริโภคผ่านทาง 'On OpenURL' "AppRouter.pending dailing' |

~ ช่องส่งสองช่อง ~

| Channel | Handled by | ตัวอย่าง |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ILinuxDeepLink.parse` → `RootTabView` | จงกล่าวเถิดมุฮัมมัด “โอ้บรรดาอาชญากรทั้งหลายเอ๋ย !” |
| **Home Screen Quick Action** | `ShortcutSceneDelegate` → `ShortcutObserver.dispatch` | สืบค้นเมื่อ '%s' expression', 'helpin','helpin', บวก 'quiz' (help) contain' (help) |

ประเภทการกระทําด่วนใช้} BAR `ilinux://` BAR  } ตรงกันกับข้อความชนิด ดังนั้นทั้ง   c1   BAR ข้อมูลมรดกยังคงพาธที่ถูกต้อง

---

## รายละเอียดคําสั่ง 1.

เปิดหน้ารายละเอียดสําหรับคําสั่งรวมเดียว

| Parameter | Required | คําอธิบาย |
|-----------|----------|-------------|
| `name` | One of `name` / `cmd` | ID ของคําสั่ง (กุญแจสําคัญในแพลตฟอร์ม Json มัด) |
| `cmd` | One of `name` / `cmd` | Synonym สําหรับ 'ชื่อ' — ถูกใช้โดยการเชื่อมโยงวิดเจ็ต |
| `platform` | No | ห้องสมุดเชลล์: ดูตารางด้านล่าง ค่าปริยายของ..."ลินุกซ์" |

~ `ilinux://` BAR ค่า ~ (หากไม่อ่อนไหว):

| Value | Shell library | นามแฝง |
|-------|---------------|---------|
| *(omit)* or `linux` | Linux (1050 commands) | — |
| `cmd` | CMD / Batch (300 commands) | "Bat" |
| `powershell` | PowerShell (300 commands) | โอ้.. |

~จงมีชีวิตอยู่~

- สลับไปยัง ~ ตัวประมวลผล~ ~ แท็บ, เลือกรายการที่ร้องขอมา ~Sell Planp * และกด 'ProfileDailyView' สําหรับคําสั่งแก้ไข
- หากหมายเลขดังกล่าวเป็น ~ ไม่ทราบหรือว่างเปล่า~ ลิงก์นี้จะถูกละทิ้ง~ (ไม่มีข้อผิดพลาดใด ๆ UI)
- ID ของคําสั่ง ~ ตัวพิมพ์เล็ก- ใหญ่~ และต้องตรงกับปุ่ม build Json พอดี (ปกติคือ พิมพ์เล็ก, e.g. ` doker', ไม่ใช่ ' doker')

~ เปิด BAR `ilinux://` BAR ~


```
ilinux://command?name=ls
```


~ เปิด BAR `ilinux://` BAR  (ลินุกซ์, ค่าปริยาย) ~


```
ilinux://command?cmd=grep
```


~ เปิด CMD `ilinux://` BAR ~


```
ilinux://command?cmd=dir&platform=cmd
```


** เปิดระบบพลังงาน `ilinux://` BAR ~


```
ilinux://command?cmd=Get-ChildItem&platform=powershell
```


~ตัวอย่างของลินุกซ์~


```
ilinux://command?name=docker
```


---

## 2. เดลี ควิซ

กระโดดตรงไปที่... ดาลี่ เควซ ไม่ได้เริ่มอัตโนมัติ หรือข้ามคําถามไป


```
ilinux://quiz
```


รูปแบบพาธ (ยอมรับ):


```
ilinux:///quiz
```


---

## 3 ตัวแปร

เปิดรายการของ ~Favourite ~ ภายใต้การนําทางของการตั้งค่า


```
ilinux://favorites
```


รูปแบบพาธ (ยอมรับ):


```
ilinux:///favorites
```


---

## 4 หนังสือ ตอบ ผิด

### 4.1 รายชื่อ

เปิดบันทึกคําตอบ Wrong ~ ภายใต้การนําร่องของการตั้งค่า


```
ilinux://wrong
```


นามแฝง (พฤติกรรมเดียวกัน):


```
ilinux://mistakes
ilinux://wrongquestions
```


### 4.2 บันทึกเดี่ยว → รายละเอียดคําสั่ง

เมื่อ  c0   BAR เป็น UUID ที่ถูกต้องของรายการที่บันทึกมาอย่างไม่ถูกต้อง โปรแกรม App จะเปิดแท็บ * และดันรายละเอียดสําหรับคําสั่งบันทึกข้อมูล (หากบันทึกและคําสั่งยังคงอยู่)

| Parameter | Required | รูปแบบ |
|-----------|----------|--------|
| `record` | Yes | สตริง UUID, e.g.  `550E0400-E29b-41d4-a716-4466540000' |


```
ilinux://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


หาก UUID ไม่ถูกต้องหรือแผ่นบันทึกถูกลบออกไป การนําร่องจะล้มเหลวกลับไปที่รายการหนังสือผิดหรือข้ามไป

---

## 5. การกระทําของหน้าจอส่วนตัวด่วน

กดไอคอนลินุกซ์ให้ยาวขึ้นถึง #4 การกระทํา ปรับแต่งใน ~ ตั้งค่าปุ่มพิมพ์ลัดส่วนตัวของจอ ~ (7 ตัวเลือก) ลากเพื่อทําการเรียงใหม่ และตั้งค่าเป็นค่าปริยาย

| Option | Registered `type` | SF Symbol | เปิด |
|--------|-------------------|-----------|--------|
| Search | `iLinux://search` | magnifyingglass | ** ใช้ค่า ** แท็บ + เปิดใช้งานแถบการค้นหา |
| Daily Quiz | `iLinux://quiz` | checklist | ~Darly Quiz~ ~แท็บ~ |
| Favourites | `iLinux://favorites` | star.fill | <i> |
| Wrong Answer Book | `iLinux://wrong` | xmark.bin.fill | <i> |
| Categories | `iLinux://categories` | rectangle.grid.2x2.fill | ** แท็บ ** |
| Send Feedback | `iLinux://feedback` | envelope.fill | เขียนจดหมายเข้ามา (หรือ 'mail to:' login back) |
| Rate App | `iLinux://review` | star.bubble.fill | แจ้งเตือนการเรียกดู Kit |

** เลือกรายการในการติดตั้งชุดแรก: ~ สืบค้นเมื่อ 27 Daily Quiz's access evolution.

** จุดหมายปลายทางเดียวของ Quick-acter~ (ไม่ได้จัดการโดย `ilinux://` /    BAR `iLinux://` BAR ):

- สืบค้นเมื่อ 'ILinux'
- 'ลินุกซ์'
- 'inux bookbook back'
- IILinux University'

ใช้นี่ผ่าน... ไอคอนกดยาว~ หรือด้วยการโพสต์ชนิดเดียวกันผ่านท่อส่งด่วนด่วน เปิดมันด้วยทางลัด *. ไม่ทํางาน นอกจากโปรแกรมจะเพิ่มข้อมูลโฮสต์โดยตรงในภายหลัง

~คนประเภทรัก (เพลง: ~

| Type | พฤติกรรม |
|------|-----------|
| `iLinux://love` | เปิดบล็อกของผู้เขียนในแผ่นภาษาซาฟารี (ปุ่มพิมพ์ลัดแบบคงที่เก่า) |

---

## 6. วิดเจ็ตที่อยู่เชื่อมโยงแบบลึก

การเคาะของวิดเจ็ตใช้ตําแหน่งเดียวกัน  c0    r. ที่อยู่ URL สร้างขึ้นโดย `iLinux://` :

| Widget | Tap target | ที่อยู่ URL |
|--------|------------|-----|
| Daily Command | Command detail | `iLinux://command?cmd=<id>&platform=<linux\ | cmd\ | ' |
| Category Spotlight | Sample command | 2553). สืบค้นเมื่อ 7 December 2015. |
| Quiz Glance | Daily Quiz | 'ลินุกซ์' |
| Favourites Glance | Favourites (or per-row command) | 2551). สืบค้นเมื่อ 7 พฤษภาคม พ.ศ. |
| Wrong Book Glance | Wrong book (or per-row record) | บันทึก=.' |

ที่อยู่ URL ของวิดเจ็ตถูกสร้างโดย `ilinux://` BAR และมักจะรวม... `iLinux://` * สําหรับเคาะคําสั่ง Planpal ตรงกับ ~ ettings allets allets allets getson (inux / CMD / Powerchell).

ปุ่มสลับคําสั่ง (IOS 17+, App Intents) ทําการโหลดไทม์ของคอนโทรลของวิดเจ็ตเท่านั้น — มันใช้ไม่ได้- ~ ใช้ที่อยู่ URL

---

## ปุ่มพิมพ์ลัดของแอปเปิล

### เปิดคําสั่ง หลังจากคัดลอกชื่อ

1. ** รับข้อความจากค่าที่ป้อนมา **
2. ** เปิดที่อยู่ URL **

หรือลินุกซ์รหัสแข็ง


```
ilinux://command?name=systemctl
```


เปิดคําสั่ง CMD:


```
ilinux://command?cmd=ipconfig&platform=cmd
```


### ข้อ เตือน ใจ สําหรับ การ ศึกษา ประจํา วัน


```
ilinux://quiz
```


เพิ่ม ** ที่อยู่ URL เปิด ** ในระบบอัตโนมัติส่วนตัว (เช่น ทุก ๆ วัน เวลา 9:00 น.

### ทบทวนคําตอบผิด


```
ilinux://wrong
```


### เปิดรายการโปรดจากปุ่มพิมพ์ลัดของโหมดโฟกัส


```
ilinux://favorites
```


---

## พฤติกรรมการเรียกใช้

เมื่อโปรแกรมได้รับที่อยู่ URL หรือการกระทําด่วน:

| Scenario | ลื่นไถล |
|----------|------|
| **Cold start — Quick Action (iOS/iPad only)** | 'OPESTESEneDEGEGE' '' สืบค้นข้อมูลประเภท:' |
| **Warm start — Quick Action (iOS/iPad only)** | ฉากการเรียกกลับ ○ แจ้งเตือน 'despatch( ประเภท:)' |
| **Cold / warm — `onOpenURL` (iOS, iPad, Mac)** | 'AppRouter. HandininingURL' สืบค้นเมื่อ 20 พฤษภาคม พ.ศ. |
| **Feedback / Rate (cold start)** | ~dever Shetwork' ล่าช้า~0.4 s~ ดังนั้นแผ่นงาน / ร้านค้าคิตมีฉากหน้าต่างที่ทํางานอยู่ |
| **Search quick action** | 'เปิดการค้นหาTab ()' ';' สืบค้นข้อมูล Pulse +=1' 'helpsublicsView' นําเสนอการค้นหา (inOS 17+: อัตโนมัติ-โฟกัสผ่านทาง 'subliced') |
| **Unknown command ID** | การ เชื่อม โยง ที่ ลึก เข้า ไป |

---

## ปุ่มพิมพ์ลัด

### iPad & Mac (ใช้ร่วมกัน)

คีย์บอร์ดฮาร์ดแวร์บน iPad และเมนู "ILinux" บน Mac share:

| Shortcut | การกระทํา |
|----------|--------|
| ⌘F | คําสั่งแท็บ + การค้นหา (หมายเช่นเดียวกันกับการค้นหาการกระทําอย่างรวดเร็วบน OS) |
| ⌘1 | แท็บคําสั่ง |
| ⌘2 | แท็บหมวดหมู่ |
| ⌘3 | แท็บของเดลี่ Quiz |
| ⌘4 | แท็บการตั้งค่า |

สืบค้นจากโฟกัสอัตโนมัติผ่านทาง ⌘F ต้องการ ~iOS 17. 0+~ หรือ ~macOS 14. 0+~.

### เมกะไบต์

| Shortcut | การกระทํา |
|----------|--------|
| ⌘, | แท็บการตั้งค่า |
| ⌘[ / Esc | สแต็กการนําทางแบบป๊อป (ด้านหลัง) |
| ⌘← / ⌘→ | หมวดหมู่ก่อน/ ถัดไป (แท็บของหมวดหมู่) |
| 1–4 | เลือกตัวเลือกทดสอบ |
| ⌘R | ทํา กิจวัตร ประจํา วัน |
| Return | คําถามต่อไป (หลังคําตอบ) |

ส่วนเชื่อมโยงแบบลึก ( `ilinux://` ) และปุ่มพิมพ์ลัดของเมนู ใช้ตัวนําทางแบบใน-app บน Mac เช่นเดียวกับ OS

---

## ยังไม่รองรับที่อยู่ URL ไม่ถูกต้อง

| URL | Result |
|-----|--------|
| `ilinux://command` (no `name` / `cmd`) | ไม่สนใจ |
| `ilinux://command?name=NotARealCmd` | ไม่สนใจ (ID ไม่อยู่ในไลบรารีสําหรับแก้ไขแพลตฟอร์ม) |
| `ilinux://command?cmd=dir` (no platform) | ไลบรารี Opens ~Linux~ — ใช้ 'partiform=cmd' สําหรับวินโดวส์ CMD |
| `ilinux://search` via Shortcuts Open URL | <i> ไม่ถูกวิเคราะห์โดย "Ilinux Deeplink' — ใช้การกระทําด่วนบน ~iOS/iPad~ หรือ ⌘F on ~Mac/iPad~ |
| `ilinux://categories` via Shortcuts Open URL | เหมือนกับด้านบน |
| `ilinux://feedback` / `ilinux://review` via Open URL | เหมือนกับด้านบน |
| Non-`ilinux` schemes | ไม่สนใจ |

---

## การยิงปัญหา

~แต่ไม่มีอะไรเกิดขึ้นเลย~

Footback, อัตราและตารางจดหมายต้องการ ~0.4 s หลังจากเปิดตัว ลองอีกครั้งจากภายในแอพ หรือรอสักครู่ในการเริ่มต้นที่เย็น

** ดําเนินการอย่างรวดเร็วไม่เน้นไปยังสนามค้นหา (inOS 16) ~

การโฟกัสอัตโนมัติต้องการ OS 17+. บน OS 16 แท็บคําสั่งยังคงเปิด เคาะสนามการค้นหาด้วยตนเอง

~เสียงเคาะไม่เปิดคําสั่งที่คาดหวัง~

โปรดแน่ใจว่าคําสั่งนี้ยังอยู่ในรุ่นของโปรแกรมที่ถูกติดตั้งแล้วของคุณเพื่อที่ถูกต้อง~. platiform ~ ส่วนเชื่อมโยงของวิดเจ็ตใช้ `ilinux://` / `iLinux://` และต้องใช้หมายเลขคําสั่งที่แน่นอน ตัวอย่าง: `platform` ต้องการ `ilinux` r ไม่ใช่ไลบรารีลินุกซ์ปริยาย

~ชื่อเล่นของ Quick-acter เป็นภาษาที่ผิด~

เปลี่ยนภาษาใน~

** ลิงก์ Deep ทํางานได้บนอุปกรณ์ แต่ไม่ใช่จากหน้าเว็บ~

ยืนยันการใช้ลิงก์ในรูปแบบ `ilinux://` BAR  และเปิดใช้โดยระบบ (tap in locals/septegraphs) ไม่ได้บล็อคด้วยเบราว์เซอร์ที่ถอดรูปแบบเอง

---

[การรองรับ iLinux](./) & middot; [FAQ](./figg) & middot; [นโยบายการแสวงหาข้อมูล](./ prinvancey)

</section>
<section lang="de" markdown="1">

iLinux unterstützt ** `ilinux://` ** (auch geschrieben ** `iLinux://` **) URL-Schema Deep Links auf ** iPhone, iPad und Mac ** - offene Befehlsdetails (Linux, CMD oder PowerShell), das tägliche Quiz, Favoriten oder das falsche Antwortbuch von Safari, eine andere App, ein Widget-Tipp (iOS / iPad) oder Apple Shortcuts.

Befehls-URLs akzeptieren einen optionalen ** `ilinux://` ** Abfrageparameter, sodass Widget-Tipps und Shortcuts Windows-Einträge korrekt öffnen können.

**Home Screen Quick Actions** (langes Drücken des App-Symbols nur auf ** iOS / iPad**) decken Suche, Kategorien, Feedback und Rate ab. Mac-Benutzer können stattdessen das **iLinux**-Menü und die Tastenkombinationen verwenden.

> **Wichtig:** iLinux ist eine **Referenz- und Lern-App**. URL-Links **navigieren nur innerhalb der App**. Sie führen **nicht ** Linux-Befehle aus, öffnen SSH-Sitzungen oder stellen eine Verbindung zu Remote-Servern her.

## Protokollspezifikation


```
ilinux://<host>[/<path>][?query]
iLinux://<host>[/<path>][?query]   ← same scheme, case-insensitive
```


| Rule | Einzelheiten |
|------|--------|
| **Scheme** | `ilinux` / `iLinux` — fallunempfindlich verglichen |
| **Host routing** | Primärer Router ist die URL **host**; einige Pfade werden auch akzeptiert (siehe unten) |
| **Command detail** | Host `Befehl` **oder ** Pfad `/Befehl` |
| **Command ID** | Abfrage `name=<id>` **or** `cmd=<id>` muss mit einem gebündelten Befehlsschlüssel übereinstimmen (z.B. `ls`, `grep`, `dir`, `Get-ChildItem`). |
| **Platform** | Abfrage `platform=<value>` — optional; standardmäßig auf **Linux**, wenn weggelassen |
| **Quiz** | Host `quiz` **or** path `/quiz` |
| **Favourites** | Host `Favoriten` **oder** Pfad `/Favoriten` |
| **Wrong book** | Host `falsch`, `Fehler` oder `falsche Fragen`; Pfad `/falsch` oder `/Fehler` auch akzeptiert |
| **Wrong record** | Abfrage `record=<UUID>` auf einer falschen Buch-URL - öffnet die Befehlsdetails dieses Datensatzes |
| **Query parameters** | Keine anderen Vorfüllparameter werden unterstützt |
| **Parser** | `ILinuxDeepLink.parse( :):` — verbraucht über `onOpenURL` → `AppRouter.pendingDeepLink` |

**Zwei Lieferkanäle **

| Channel | Handled by | Beispiele |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ILinuxDeepLink.parse` → `RootTabView` | "Befehl", "Quiz", "Favoriten", "falsch" |
| **Home Screen Quick Action** | `ShortcutSceneDelegate` → `ShortcutObserver.dispatch` | `search`, `categories`, `feedback`, `review` plus überlappendes `quiz` / `favorites` / `falsch` |

Quick-Action-Typen verwenden ** `ilinux://` ** Matching auf der Typzeichenfolge, so dass sowohl `iLinux://` als auch Legacy-Varianten immer noch korrekt routen.

---

## 1. Befehlsdetail

Öffnen Sie die Detailseite für einen einzelnen gebündelten Befehl.

| Parameter | Required | Beschreibung |
|-----------|----------|-------------|
| `name` | One of `name` / `cmd` | Command ID (Wörterbuchschlüssel im Plattform-JSON-Bundle) |
| `cmd` | One of `name` / `cmd` | Synonym für `name` - wird von Widget-Links verwendet |
| `platform` | No | Shell-Bibliothek: siehe Tabelle unten. Standardmäßig **Linux** |

** `ilinux://` -Werte** (fallunempfindlich):

| Value | Shell library | Aliasnamen |
|-------|---------------|---------|
| *(omit)* or `linux` | Linux (1050 commands) | — |
| `cmd` | CMD / Batch (300 commands) | Batch, Bat |
| `powershell` | PowerShell (300 commands) | ps, pwsh |

**Verhalten**

- Wechselt zur Registerkarte **Commands**, wählt die angeforderte **shell-Plattform** aus und drückt `CommandDetailView` für den aufgelösten Befehl.
- Wenn die ID **unbekannt oder leer ** ist, wird der Link **stillschweigend ignoriert ** (keine Fehler-Benutzeroberfläche).
- Befehls-IDs sind **case-sensitiv** und müssen genau mit dem gebündelten JSON-Schlüssel übereinstimmen (normalerweise Kleinbuchstaben, z.B. `Docker`, nicht `Docker`).

**Offen `ilinux://` **


```
ilinux://command?name=ls
```


**Offen `ilinux://` (Linux, standardmäßig)**


```
ilinux://command?cmd=grep
```


**Open CMD `ilinux://` **


```
ilinux://command?cmd=dir&platform=cmd
```


**Open PowerShell `ilinux://` **


```
ilinux://command?cmd=Get-ChildItem&platform=powershell
```


**Cloud-natives Linux-Beispiel**


```
ilinux://command?name=docker
```


---

## 2. Tägliches Quiz

Springen Sie direkt zum Tab **Daily Quiz**. Startet **nicht ** autostart oder überspringt fragen.


```
ilinux://quiz
```


Trassenform (auch akzeptiert):


```
ilinux:///quiz
```


---

## 3. Favoriten

Öffnen Sie die ** Favoriten** Liste unter Einstellungen Navigation.


```
ilinux://favorites
```


Trassenform (auch akzeptiert):


```
ilinux:///favorites
```


---

## 4. Falsches Antwortbuch

### 4.1 Liste

Öffnen Sie die **Wrong Answer Book** Liste unter Einstellungen Navigation.


```
ilinux://wrong
```


Aliasnamen (gleiches Verhalten):


```
ilinux://mistakes
ilinux://wrongquestions
```


### 4.2 Einzeldatensatz → Befehlsdetail

Wenn `ilinux://` eine gültige UUID eines gespeicherten Falschantworteintrags ist, öffnet die App die Registerkarte **Befehle** und drückt Details für den Befehl dieses Datensatzes (wenn der Datensatz und der Befehl noch vorhanden sind).

| Parameter | Required | Format |
|-----------|----------|--------|
| `record` | Yes | UUID-String, z. B. `550e8400-e29b-41d4-a716-446655440000` |


```
ilinux://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


Wenn die UUID ungültig ist oder der Datensatz gelöscht wurde, fällt die Navigation auf die Liste der falschen Bücher zurück oder wird übersprungen.

---

## 5. Home Screen Schnelle Aktionen

Langes Drücken des iLinux-Symbols → bis zu **4** Aktionen. Konfigurieren Sie in ** Einstellungen → Home Screen Shortcuts ** (7 Optionen, Drag to Reorder, Zurücksetzen auf Standard).

| Option | Registered `type` | SF Symbol | Offen |
|--------|-------------------|-----------|--------|
| Search | `iLinux://search` | magnifyingglass | **Befehle** Tab + Suchleiste aktivieren |
| Daily Quiz | `iLinux://quiz` | checklist | **Daily Quiz** Tab |
| Favourites | `iLinux://favorites` | star.fill | ** Favoriten** Liste |
| Wrong Answer Book | `iLinux://wrong` | xmark.bin.fill | ** Falsches Antwortbuch** Liste |
| Categories | `iLinux://categories` | rectangle.grid.2x2.fill | **Tab Kategorien** |
| Send Feedback | `iLinux://feedback` | envelope.fill | In-App Mail Compose (oder `mailto:` Fallback) |
| Rate App | `iLinux://review` | star.bubble.fill | StoreKit Review prompt |

**Standardauswahl bei der ersten Installation:** Suche · Tägliches Quiz · Favoriten · Feedback senden.

** Quick-Action-only Destinationen** (nicht behandelt von `ilinux://` / `iLinux://` ):

- „iLinux://search
- „iLinux://categories
- „iLinux://feedback
- „iLinux://review

Verwenden Sie diese über **Long-Press-Symbol ** oder indem Sie den gleichen Typ über die Quick Action-Pipeline veröffentlichen - Öffnen Sie sie mit Shortcuts **Open URL ** kann **nicht ** funktionieren, es sei denn, die App fügt später explizites Host-Parsing hinzu.

**Legacy-Typ (noch geroutet):**

| Type | Verhalten |
|------|-----------|
| `iLinux://love` | Öffnet Autor Blog in In-App Safari Blatt (alte statische Verknüpfung) |

---

## 6. Widget Deep Links

Widget Taps verwenden die gleichen `ilinux://` URLs, die von `iLinux://` erstellt wurden:

| Widget | Tap target | URL |
|--------|------------|-----|
| Daily Command | Command detail | `iLinux://command?cmd=<id>&platform=<linux\ | cmd\ | powershell> |
| Category Spotlight | Sample command | `iLinux://command?cmd=<id>&plattform=<plattform>` |
| Quiz Glance | Daily Quiz | „iLinux://quiz |
| Favourites Glance | Favourites (or per-row command) | `iLinux://favorites` / `iLinux://command?cmd=<id>&platform=<plattform>` |
| Wrong Book Glance | Wrong book (or per-row record) | `iLinux://wrong` / `iLinux://wrong?record=<UUID>` |

Widget-URLs werden von `ilinux://` erstellt und enthalten immer ** `iLinux://` ** für Kommando-Taps. Die Plattform passt **Einstellungen → Widgets → Widget-Befehlsbibliothek** (Linux / CMD / PowerShell).

Die Schaltfläche **Daily Command shuffle ** (iOS 17+, App Intent) lädt nur die Widget-Timeline neu – sie verwendet **nicht ** eine URL.

---

## Apple Shortcuts

### Öffnen Sie einen Befehl nach dem Kopieren seines Namens

1. ** Holen Sie sich Text von Input **
2. **Offene URLs** → `ilinux://` + Text

Oder Hard-Code Linux:


```
ilinux://command?name=systemctl
```


Öffnen Sie einen CMD-Befehl:


```
ilinux://command?cmd=ipconfig&platform=cmd
```


### Tägliche Studie Erinnerung → Quiz


```
ilinux://quiz
```


Fügen Sie **Open URLs** in einer Personal Automation hinzu (z.B. jeden Wochentag um 9:00 Uhr).

### Überprüfen Sie falsche Antworten


```
ilinux://wrong
```


### Offene Favoriten aus einer Focus Mode Shortcut


```
ilinux://favorites
```


---

## Startverhalten

Wenn die App eine URL oder Quick Action erhält:

| Scenario | Durchfluss |
|----------|------|
| **Cold start — Quick Action (iOS/iPad only)** | `ShortcutSceneDelegate` → `PendingShortcutBuffer` → `ShortcutObserver.onAppear` → `dispatch(type:)` |
| **Warm start — Quick Action (iOS/iPad only)** | Scene Callback → Benachrichtigung → `dispatch(type:)` |
| **Cold / warm — `onOpenURL` (iOS, iPad, Mac)** | `AppRouter.handleIncomingURL` → `pendingDeepLink` → `RootTabView.onChange` navigiert |
| **Feedback / Rate (cold start)** | `deferSheetWork` Verzögerungen **~0,4 s** so Mailsheet / StoreKit hat eine aktive Fensterszene |
| **Search quick action** | `openSearchTab()` → `searchPulse += 1` → `BrowseCommandsView` präsentiert die Suche (iOS 17+: Autofokus über `isPresented`) |
| **Unknown command ID** | Deep Link analysiert, Navigation übersprungen – kein Alarm |

---

## Tastenkürzel

### iPad & Mac (geteilt)

Hardware-Tastatur auf dem iPad und das **iLinux**-Menü auf dem Mac:

| Shortcut | Aktion |
|----------|--------|
| ⌘F | Befehle tab + suche (gleiche absicht wie search quick action auf ios). |
| ⌘1 | Tab Befehle |
| ⌘2 | Tab Kategorien |
| ⌘3 | Täglicher Quiz Tab |
| ⌘4 | Tab Einstellungen |

Suchen Sie Autofokus über ⌘F erfordert **iOS 17.0+** oder **macOS 14.0+**.

### Nur Mac

| Shortcut | Aktion |
|----------|--------|
| ⌘, | Tab Einstellungen |
| ⌘[ / Esc | Pop Navigation Stack (zurück) |
| ⌘← / ⌘→ | Vorherige / nächste Kategorie (Tab Kategorien) |
| 1–4 | Wählen Sie Quiz-Antwort-Option |
| ⌘R | Reshuffing tägliches Quiz |
| Return | Nächste Quizfrage (nach der Beantwortung) |

Deep Links ( `ilinux://` ) und Menükombinationen verwenden den gleichen In-App-Router auf dem Mac wie auf iOS.

---

## Nicht unterstützte und ungültige URLs

| URL | Result |
|-----|--------|
| `ilinux://command` (no `name` / `cmd`) | ignoriert |
| `ilinux://command?name=NotARealCmd` | Ignoriert (ID nicht in Bibliothek für aufgelöste Plattform) |
| `ilinux://command?cmd=dir` (no platform) | Öffnet **Linux**-Bibliothek - verwenden Sie `platform=cmd` für Windows CMD |
| `ilinux://search` via Shortcuts Open URL | **Nicht ** analysiert von `ILinuxDeepLink` — verwenden Sie Quick Action auf **iOS/iPad** oder ⌘F auf **Mac/iPad** |
| `ilinux://categories` via Shortcuts Open URL | Wie oben |
| `ilinux://feedback` / `ilinux://review` via Open URL | Wie oben |
| Non-`ilinux` schemes | ignoriert |

---

## Fehlerbehebung

** Shortcut öffnet die App, aber nichts passiert (Kaltstart) **

Feedback, Rate und Mailsheets benötigen ~ 0,4 s nach dem Start. Versuchen Sie es erneut aus der App heraus oder warten Sie einen Moment beim Kaltstart.

**Die Suche nach einer schnellen Aktion fokussiert das Suchfeld nicht (iOS 16)**

Autofokus erfordert iOS 17+. Unter iOS 16 wird die Registerkarte Befehle immer noch geöffnet; tippen Sie manuell auf das Suchfeld.

**Widget tap öffnet den erwarteten Befehl nicht **

Stellen Sie sicher, dass der Befehl in Ihrer installierten App-Version für die richtige ** Plattform ** noch vorhanden ist. Widget-Links verwenden `ilinux://` + `iLinux://` und erfordern eine genaue Befehls-ID. Beispiel: `platform` braucht `ilinux` , nicht die Standard-Linux-Bibliothek.

** Quick-Action-Titel sind in der falschen Sprache**

Ändern Sie die Sprache in **Einstellungen → Sprache ** - die App registriert die Verknüpfungselemente automatisch neu.

** Deep Link funktioniert auf dem Gerät, aber nicht von einer Webseite **

Bestätigen Sie, dass der Link das Schema `ilinux://` verwendet und vom System geöffnet wird (Tipp in Notizen / Nachrichten), nicht von einem In-App-Browser blockiert, der benutzerdefinierte Schemata entfernt.

---

[Zurück zu iLinux Support](../) &middot; [FAQ](../faq) &middot; [Privacy Policy](../privacy]

</section>
<section lang="fr" markdown="1">

iLinux prend en charge ** `ilinux://` ** (également écrit ** `iLinux://` **) URL scheme deep links on **iPhone, iPad and Mac** — open command detail (Linux, CMD ou PowerShell), the Daily Quiz, Favorites or the Wrong Answer Book from Safari, another app, a widget tap (iOS/iPad), or Apple Shortcuts.

Les URLs de commande acceptent un paramètre de requête optionnel ** `ilinux://` ** afin que les touches de widget et les raccourcis puissent ouvrir les entrées Windows correctement.

**Écran d'accueil Actions rapides** (long-presse l'icône de l'application sur **iOS/iPad seulement**) couverture Recherche, catégories, rétroaction et taux. Les utilisateurs Mac peuvent utiliser le menu **iLinux** et les raccourcis clavier.

> **Important:** iLinux est une application **de référence et d'apprentissage**. Liens URL seulement **navigate dans l'application**. Ils ne **pas** exécuter des commandes Linux, ouvrir des sessions SSH ou se connecter à des serveurs distants.

## Spécification du protocole


```
ilinux://<host>[/<path>][?query]
iLinux://<host>[/<path>][?query]   ← same scheme, case-insensitive
```


| Rule | Détail |
|------|--------|
| **Scheme** | `ilinux` / `iLinux` — comparaison sensible aux cas |
| **Host routing** | Le routeur principal est l'URL **host**; certains chemins sont également acceptés (voir ci-dessous) |
| **Command detail** | Chemin `command` **ou** `/command` |
| **Command ID** | Query `name=<id>` **ou** `cmd=<id>` – doit correspondre à une touche de commande groupée (par exemple `ls`, `grep`, `dir`, `Get-ChildItem`) |
| **Platform** | Interroger `platform=<value>` — facultatif; par défaut **Linux** en cas d'omission |
| **Quiz** | Hébergement `quiz` **ou** chemin `/quiz` |
| **Favourites** | Hôtes `favorites` **ou** chemin `/favorites` |
| **Wrong book** | Hôte `mauvais`, `erreurs` ou `questions douteuses`; chemin `/mauvais` ou `/erreurs` également accepté |
| **Wrong record** | Interroger `record=<UUID>` sur une URL du mauvais livre — ouvre le détail de commande de cet enregistrement |
| **Query parameters** | Aucun autre paramètre de pré-remplissement n'est pris en charge |
| **Parser** | `ILinuxDeepLink.parse( :)` — consommé via `onOpenURL` → `AppRouter.pendingDeepLink` |

**Deux canaux de livraison**

| Channel | Handled by | Exemples |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ILinuxDeepLink.parse` → `RootTabView` | `commande`, `quiz`, `favorites`, `mauvais` |
| **Home Screen Quick Action** | `ShortcutSceneDelegate` → `ShortcutObserver.dispatch` | `recherche`, `catégories`, `feedback`, `review`, plus chevauchement `quiz` / `favorites` / `wrong` |

Les types d'action rapide utilisent ** `ilinux://` ** correspondant sur la chaîne de type, de sorte que les variantes `iLinux://` et les variantes héritées suivent toujours correctement.

---

## 1. Détail de la commande

Ouvrez la page de détails pour une seule commande groupée.

| Parameter | Required | Désignation des marchandises |
|-----------|----------|-------------|
| `name` | One of `name` / `cmd` | ID de commande (clé dictionnaire dans le paquet JSON plate-forme) |
| `cmd` | One of `name` / `cmd` | Synonyme pour `name` — utilisé par les liens widget |
| `platform` | No | Bibliothèque Shell: voir tableau ci-dessous. Par défaut à **Linux** |

**    C     valeurs** (insensible aux cas):

| Value | Shell library | Autres |
|-------|---------------|---------|
| *(omit)* or `linux` | Linux (1050 commands) | — |
| `cmd` | CMD / Batch (300 commands) | `bat', `bat' |
| `powershell` | PowerShell (300 commands) | `ps`, `pwsh` |

**Comportement**

- Switches vers l'onglet **Commandes**, sélectionne la plateforme **shell** demandée et pousse `CommandeDetailView` pour la commande résolue.
- Si l'ID est **inconnu ou vide**, le lien est **silencieusement ignoré** (interface utilisateur sans erreur).
- Les identifiants de commande sont **sensibles aux cas** et doivent correspondre exactement à la clé JSON groupée (généralement minuscule, par exemple `docker`, pas `Docker`).

**Ouvert `ilinux://` **


```
ilinux://command?name=ls
```


**Ouvrir `ilinux://` (Linux, par défaut)**


```
ilinux://command?cmd=grep
```


**Ouvrir CMD `ilinux://` **


```
ilinux://command?cmd=dir&platform=cmd
```


**Open PowerShell `ilinux://` **


```
ilinux://command?cmd=Get-ChildItem&platform=powershell
```


**Exemple Linux natif-cloud**


```
ilinux://command?name=docker
```


---

## 2. Quiz quotidien

Sautez directement à l'onglet **Quiz quotidien**. Ne **pas** auto-démarrer ou sauter les questions.


```
ilinux://quiz
```


Formulaire de chemin (également accepté):


```
ilinux:///quiz
```


---

## 3. Favoris

Ouvrez la liste **Favourites** sous Paramètres de navigation.


```
ilinux://favorites
```


Formulaire de chemin (également accepté):


```
ilinux:///favorites
```


---

## 4. Livre de mauvaise réponse

### 4.1 Liste

Ouvrez la liste **Wrong Answer Book** sous Paramètres de navigation.


```
ilinux://wrong
```


Aliases (même comportement):


```
ilinux://mistakes
ilinux://wrongquestions
```


### 4.2 Détails de commande d'enregistrement unique →

Lorsque `ilinux://` est un UUID valide d'une entrée de mauvaise réponse enregistrée, l'application ouvre l'onglet **Commandes** et pousse le détail pour la commande de cet enregistrement (si l'enregistrement et la commande existent toujours).

| Parameter | Required | Format |
|-----------|----------|--------|
| `record` | Yes | Chaîne UUID, par exemple `550e8400-e29b-41d4-a716-446655440000` |


```
ilinux://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


Si l'UUID est invalide ou que l'enregistrement a été supprimé, la navigation revient à la mauvaise liste de livres ou est ignorée.

---

## 5. Actions rapides de l'écran d'accueil

Appuyez longuement sur l'icône iLinux → jusqu'à **4** actions. Configurez dans **Paramètres → Raccourcis d'écran d'accueil** (7 options, faites glisser pour réorganiser, réinitialisez aux valeurs par défaut).

| Option | Registered `type` | SF Symbol | Ouvre |
|--------|-------------------|-----------|--------|
| Search | `iLinux://search` | magnifyingglass | **Commandes** onglet + barre de recherche active |
| Daily Quiz | `iLinux://quiz` | checklist | ** Jeu-questionnaire quotidien** |
| Favourites | `iLinux://favorites` | star.fill | ** Liste des favoris** |
| Wrong Answer Book | `iLinux://wrong` | xmark.bin.fill | **Liste des livres de réponses de Wong** |
| Categories | `iLinux://categories` | rectangle.grid.2x2.fill | **Catégories** onglet |
| Send Feedback | `iLinux://feedback` | envelope.fill | Le courrier dans l'application compose (ou `mailto:` fallback) |
| Rate App | `iLinux://review` | star.bubble.fill | Demande de révision de StoreKit |

** Sélection par défaut lors de la première installation :** Recherche · Quiz quotidien · Favoris · Envoyer des commentaires.

** Destinations à action rapide** (non traitées par `ilinux://` / `iLinux://` ):

- "iLinux://search"
- «iLinux://catégories»
- «iLinux://feedback»
- «iLinux://review»

Utilisez ceux-ci via l'icône **long-press** ou en affichant le même type dans le pipeline Quick Action — les ouvrant avec Raccourcis **Ouvrir l'URL** ne peut **pas** fonctionner à moins que l'application ajoute explicitement l'analyse de l'hôte plus tard.

**Type de légataire (toujours acheminé):**

| Type | Comportement |
|------|-----------|
| `iLinux://love` | Ouvre le blog de l'auteur dans l'application Feuille Safari (ancien raccourci statique) |

---

## 6. Liens profonds Widget

Les touches Widget utilisent les mêmes URLs `ilinux://` construites par `iLinux://` :

| Widget | Tap target | URL |
|--------|------------|-----|
| Daily Command | Command detail | `iLinux://command?cmd=<id>&platform=<linux\ | cmd\ | moteur >` |
| Category Spotlight | Sample command | `iLinux://command?cmd=<id>&platform=<platform>` |
| Quiz Glance | Daily Quiz | 'iLinux://quiz' |
| Favourites Glance | Favourites (or per-row command) | `iLinux://favorites` / `iLinux://command?cmd=<id>&platform=<platform>` |
| Wrong Book Glance | Wrong book (or per-row record) | `iLinux://wrong` / `iLinux://wrong?record=<UUID>` |

Les URLs Widget sont construites par `ilinux://` et incluent toujours ** `iLinux://` ** pour les touches de commande. La plate-forme correspond **Paramètres → Widgets → Bibliothèque de commandes Widget** (Linux / CMD / PowerShell).

Le bouton **Daily Command shuffle** (iOS 17+, App Intent) recharge uniquement la timeline du widget — il ne **pas** utiliser une URL.

---

## Raccourcis des pommes

### Ouvrir une commande après avoir copié son nom

1. **Obtenez le texte de l'entrée**
2. **Ouvrir les URL** → `ilinux://` + Texte

Ou Linux code dur :


```
ilinux://command?name=systemctl
```


Ouvrez une commande CMD :


```
ilinux://command?cmd=ipconfig&platform=cmd
```


### Rappel quotidien d'étude → quiz


```
ilinux://quiz
```


Ajouter **Ouvrir les URL** dans une automatisation personnelle (par exemple tous les jours de la semaine à 9h).

### Examiner les mauvaises réponses


```
ilinux://wrong
```


### Ouvrir les favoris à partir d'un raccourci mode Focus


```
ilinux://favorites
```


---

## Comportement de lancement

Lorsque l'application reçoit une URL ou une action rapide :

| Scenario | Débit |
|----------|------|
| **Cold start — Quick Action (iOS/iPad only)** | `ScorecutSceneDelegate` → `PendingShortcutBuffer` → `ShortcutObserver.onAppear` → `dispatch(type:)` |
| **Warm start — Quick Action (iOS/iPad only)** | Callback de scène → notification → `dispatch(type:)` |
| **Cold / warm — `onOpenURL` (iOS, iPad, Mac)** | `AppRouter.handleIncomingURL` → `pendingDeepLink` → `RootTabView.onChange` navigue |
| **Feedback / Rate (cold start)** | `deferSheetWork` retards **~0.4 s** donc feuille de courrier / StoreKit a une scène de fenêtre active |
| **Search quick action** | `openSearchTab()` → `searchPulse += 1` → `BrowseCommandsView` présente la recherche (iOS 17+: auto-focus via `isPresented`) |
| **Unknown command ID** | Lien profond analysé mais la navigation sautée — pas d'alerte |

---

## Raccourcis clavier

### iPad & Mac (partagé)

Clavier hardware sur iPad et le menu **iLinux** sur Mac partage:

| Shortcut | Décision |
|----------|--------|
| ⌘F | Onglet Commandes + recherche (même intention que Recherche action rapide sur iOS) |
| ⌘1 | onglet Commandes |
| ⌘2 | Onglet Catégories |
| ⌘3 | Onglet Quiz quotidien |
| ⌘4 | Onglet Paramètres |

La recherche auto-focus via la touche F nécessite **iOS 17.0+** ou **macOS 14.0+**.

### Mac seulement

| Shortcut | Décision |
|----------|--------|
| ⌘, | Onglet Paramètres |
| ⌘[ / Esc | Pile de navigation pop (arrière) |
| ⌘← / ⌘→ | Catégorie précédente / suivante (onglet Catégories) |
| 1–4 | Sélectionnez l'option de réponse au quiz |
| ⌘R | Remaniement du quiz quotidien |
| Return | Question suivante (après réponse) |

Les liens profonds ( `ilinux://` ) et les raccourcis de menu utilisent le même routeur in-app sur Mac que sur iOS.

---

## URLs non prises en charge & invalides

| URL | Result |
|-----|--------|
| `ilinux://command` (no `name` / `cmd`) | Ignorées |
| `ilinux://command?name=NotARealCmd` | Ignoré (ID non dans la bibliothèque pour la plateforme résolue) |
| `ilinux://command?cmd=dir` (no platform) | Ouvre la bibliothèque **Linux** — utilisez `platform=cmd` pour Windows CMD |
| `ilinux://search` via Shortcuts Open URL | **Non** analysé par `ILinuxDeepLink` — Utilisez une action rapide sur **iOS/iPad**, ou sur **Mac/iPad** |
| `ilinux://categories` via Shortcuts Open URL | Comme ci-dessus |
| `ilinux://feedback` / `ilinux://review` via Open URL | Comme ci-dessus |
| Non-`ilinux` schemes | Ignorées |

---

## Dépannage

**Shortcut ouvre l'application mais rien ne se passe (lancement froid)**

Feedback, Rate et les feuilles de courrier ont besoin ~0.4 s après le lancement. Essayez de nouveau de l'intérieur de l'application, ou attendez un moment sur le démarrage froid.

**La recherche rapide ne focalise pas le champ de recherche (iOS 16)**

Autofocus nécessite iOS 17+. Sur iOS 16, l'onglet Commandes s'ouvre toujours; appuyez manuellement sur le champ de recherche.

**Le bouton Widget n'ouvre pas la commande attendue**

Assurez-vous que la commande existe toujours dans votre version d'application installée pour le bon **platform**. Les liens Widget utilisent `ilinux://` + `iLinux://` et nécessitent un identifiant de commande exact. Exemple : `platform` nécessite `ilinux` , pas la bibliothèque Linux par défaut.

**Les titres d'action rapide sont dans la mauvaise langue**

Changer de langue dans **Paramètres → Langue** — l'application ré-enregistre automatiquement les éléments raccourcis.

**Le lien profond fonctionne sur l'appareil mais pas sur une page Web**

Confirmer que le lien utilise le schéma `ilinux://` et est ouvert par le système (tap dans Notes/Messages), non bloqué par un navigateur in-app qui bande les schémas personnalisés.

---

[Retour à iLinux Support](../) &middot; [FAQ](../faq) &middot; [Politique de confidentialité](../privacy)

</section>
<section lang="tr" markdown="1">

iLinux ** `ilinux://` ** (ayrıca yazılmıştır ** `iLinux://` **) URL programı, **iPhone, iPad ve Mac** ile ilgili derin bağlantılar - açık komut detay (Linux, CMD veya PowerShell), Daily Quiz, Favourites veya yanlış cevap Kitabı Safari, başka bir uygulama, bir widget dokunuş (iOS/iPad) veya Apple Shortcuts.

Komut URL'leri isteğe bağlı olarak kabul eder ** `ilinux://` ** sorgu parametresi bu yüzden widget musluklar ve Kısa kesimler Windows girişlerini doğru şekilde açabilir.

**Home Ekran Hızlı Eylemler **iOS /iPad'in yalnızca**) kapak Arama, Kategoriler, Geri bildirim ve Puan. Mac kullanıcıları bunun yerine **iLinux** menü ve klavye kısayollarını kullanabilir.

> **İmportant: ** iLinux bir **reference ve öğrenme uygulaması**. URL bağlantıları sadece ** uygulama içinde iptal edin**. **Not ** Linux komutları, açık SSH seansları veya uzaktan sunuculara bağlanır.

## Protokol Doğrulaması


```
ilinux://<host>[/<path>][?query]
iLinux://<host>[/<path>][?query]   ← same scheme, case-insensitive
```


| Rule | Detaylı Bilgi |
|------|--------|
| **Scheme** | "ilinux" / "iLinux" - vakaya karşı hassas bir şekilde karşılaştırıldığında |
| **Host routing** | Birincil yönlendirici URL **host**; bazı yollar da kabul edilir (aşağıda bakın) |
| **Command detail** | Host "command" **or ** yol "/command" |
| **Command ID** | Sorgu "isim=<id>" **or** "cmd=<id>" - bir paketli komut anahtarla eşleştirmeli (e.g. "ls', "grep', " |
| **Platform** | Sorgu " platform =<value>" - isteğe bağlı; **Linux**'ye varsayılan olarak |
| **Quiz** | Host "quiz" **or ** yol " /quiz" |
| **Favourites** | Host "favorites" **or ** yol "/favorites" |
| **Wrong book** | Host "wrong", "mistakes", ya da "wrongquestions"; yol "/wrong" veya " /mistakes" de kabul edildi |
| **Wrong record** | Sorgu "record=<UUUID>" yanlış bir kitap URL'de - bu rekorun komut detayını açıyor |
| **Query parameters** | Diğer önceden tamamlanma parametreleri desteklenmez |
| **Parser** | "ILinux DeepLink.parse( :)" - "onOpenURL" → "AppRouter.pending DeepLink" |

** İki teslimat kanalı**

| Channel | Handled by | Örnekler |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ILinuxDeepLink.parse` → `RootTabView` | "Amand", "quiz", "favorites", "wrong" |
| **Home Screen Quick Action** | `ShortcutSceneDelegate` → `ShortcutObserver.dispatch` | “Arapçalar”, “sağlık”, “öğrenme”, artı örtüşme ‘quiz’ / “favorites’ / “wrong’ |

Hızlı aksiyon türleri ** `ilinux://` ** tipi dizede eşleşen, bu yüzden hem de `iLinux://` ve mirası seçenekleri hala doğru rotayı doğru şekilde rotalar.

---

## 1. Komut Detayları

Tek bir paketli komut için detay sayfasını açın.

| Parameter | Required | Açıklama |
|-----------|----------|-------------|
| `name` | One of `name` / `cmd` | Komutan ID (Rehlikeary key in the platform JSONpack) |
| `cmd` | One of `name` / `cmd` | "isim" için eş anlamlı - widget bağlantıları tarafından kullanılır |
| `platform` | No | Shell kütüphanesi: aşağıda masayı görün. **Linux** |

** `ilinux://` values ** (case-in sensitive):

| Value | Shell library | Aliases |
|-------|---------------|---------|
| *(omit)* or `linux` | Linux (1050 commands) | — |
| `cmd` | CMD / Batch (300 commands) | "batch", "bat" |
| `powershell` | PowerShell (300 commands) | "Pwsh" |

** Davranışı

- Anahtarlar **Commands ** sekmesi, talep edilen **shell platform**'i seçin ve "CommandDetailView"'i çözdü.
- Eğer kimlik ** bilinen veya boş** ise, bağlantı ** açıkça göz ardı edilir** (no error UI).
- Komutan kimlikleri **case-sensitive** ve tam olarak paketlenmiş JSON anahtarını eşleştirmeli (tipik olarak daha düşük, e.g. "docker", "Docker" değil.

**Açık `ilinux://` **


```
ilinux://command?name=ls
```


**Açık `ilinux://` (Linux, varsayılan)**


```
ilinux://command?cmd=grep
```


**Açık CMD `ilinux://` **


```
ilinux://command?cmd=dir&platform=cmd
```


**Open PowerShell `ilinux://` **


```
ilinux://command?cmd=Get-ChildItem&platform=powershell
```


**Cloud-native Linux örneği**


```
ilinux://command?name=docker
```


---

## 2. Günlük Quiz

Doğrudan **Daily Quiz** sekmesine atlayın. **Not ** auto-start veya soruları atlar.


```
ilinux://quiz
```


Pat formu (ayrıca kabul):


```
ilinux:///quiz
```


---

## 3. Favourites

**Favourites** listesi Ayarlar navigasyon altında.


```
ilinux://favorites
```


Pat formu (ayrıca kabul):


```
ilinux:///favorites
```


---

## 4. Yanlış Cevap Kitabı

### 4.1 Listesi

**Wrong Answer Book** listesini Ayarlar navigasyon altında açın.


```
ilinux://wrong
```


Aliases (same davranışı):


```
ilinux://mistakes
ilinux://wrongquestions
```


### 4.2 Tek kayıt → komut detay `ilinux://` , kurtarılmış bir yanlış cevap girişinin geçerli bir UUID'si olduğunda, uygulama **Commands ** sekmesini açar ve bu rekorun komutunu detaylandırır (eğer kayıt ve komut hala mevcutsa).

| Parameter | Required | Format |
|-----------|----------|--------|
| `record` | Yes | UUID string, e.g. "550e8400-e29b-41d4-a716-446655440000" |


```
ilinux://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


UUID geçersizyse veya kayıt silindiyse, navigasyon yanlış kitap listesine geri döner veya atılır.

---

## 5. Ev Ekran Hızlı Eylemler

Long-press the iLinux icon → up to **4** actions. **Ev Ekran Kısakesler** (7 seçenek, yeniden sipariş için sürüklenme, varsayılanlara sıfırlama).

| Option | Registered `type` | SF Symbol | Açıklar |
|--------|-------------------|-----------|--------|
| Search | `iLinux://search` | magnifyingglass | **Commands ** sekmesi + aktif arama çubuğu |
| Daily Quiz | `iLinux://quiz` | checklist | **Daily Quiz ** sekmesi |
| Favourites | `iLinux://favorites` | star.fill | **Favourites ** listesi |
| Wrong Answer Book | `iLinux://wrong` | xmark.bin.fill | **Wrong Cevap Kitabı** listesi |
| Categories | `iLinux://categories` | rectangle.grid.2x2.fill | **Kategoriler ** sekmesi |
| Send Feedback | `iLinux://feedback` | envelope.fill | In-app mail form (veya "mailto:' fallback) |
| Rate App | `iLinux://review` | star.bubble.fill | StoreKit incelemesi Hızlı |

**İlk yüklemedeDefault seçimi: ** Arama · Günlük Quiz · Favourites · Geri bildirim gönderin.

**Quick-action-only destinasyonlar** ( `ilinux://` / `iLinux://` tarafından ele alınma):

- "iLinux"
- "iLinux http://categories"
- "iLinux:
- "iLinux http

Bunu **long-press i + veya Quick Action boru hattı aracılığıyla aynı türü yayınlayarak - onları kısa kesimlerle açın **Open URL **, **, uygulama daha sonra açık ev sahibi parsing eklerken çalışmayabilir.

**Legacy type (still rotad):**

| Type | Davranış |
|------|-----------|
| `iLinux://love` | Opens author blog in in-app Safari page (eski statik kısayol) |

---

## 6. Widget Deep Links

Widget musluklar, `ilinux://` URL'ler tarafından inşa edilen aynı `iLinux://` :

| Widget | Tap target | URL URL URL URL |
|--------|------------|-----|
| Daily Command | Command detail | `iLinux://command?cmd=<id>&platform=<linux\ | cmd\ | ► |
| Category Spotlight | Sample command | "iLinux httpcommand?cmd=<id>&shop=< platform>" |
| Quiz Glance | Daily Quiz | "iLinux " |
| Favourites Glance | Favourites (or per-row command) | "iLinux http://favorites' / "iLinux httpcommand?cmd=<id>&shop=< platform> |
| Wrong Book Glance | Wrong book (or per-row record) | "iLinux httpwrong' / "iLinux http://wrong?record=<UUID>" |

Widget URL'ler, `ilinux://` tarafından inşa edilir ve her zaman ** `iLinux://` ** komut parçaları için içerir. Platform maçları **Settings → Widgets → Widget komut kütüphanesi** (Linux / CMD / PowerShell).

**Daily Komutanlığı shuffle düğmesine ** (iOS 17+, App Niye) sadece widget zaman çizelgesini yeniden yükler - ** değil ** URL kullanın.

---

## Apple Shortcuts

### Adını kopyalamaktan sonra bir komut açın

1. ** Girişten Text alın**
2. **Açık URLler** → `ilinux://` + Text

Ya da zor kod Linux:


```
ilinux://command?name=systemctl
```


Bir CMD komut açın:


```
ilinux://command?cmd=ipconfig&platform=cmd
```


### Günlük çalışma hatırlatması → sınav


```
ilinux://quiz
```


Add **Open URLs ** in a Personal Automation (e.g. every weekday at 9:00).

### Yanlış cevaplar


```
ilinux://wrong
```


### Bir Focus modundan açık favoriler


```
ilinux://favorites
```


---

## Behaviour

Uygulama bir URL veya Hızlı Eylem aldığında:

| Scenario | Akış Akış |
|----------|------|
| **Cold start — Quick Action (iOS/iPad only)** | "ShortcutSceneDelegate" → "PendingShortcutBuffer" → "ShortcutObserver.onAppear' → "dispatch (tip:)" |
| **Warm start — Quick Action (iOS/iPad only)** | Sahne geri dönüş → bildirim → "dispatch (tip:)" |
| **Cold / warm — `onOpenURL` (iOS, iPad, Mac)** | "AppRouter.handleIncomingURL" → "Zending DeepLink" → "RootTabView.onChange' navigates |
| **Feedback / Rate (cold start)** | "deferSheetWork'in gecikmeleri **~0.4 s** bu yüzden posta sayfası / MağazaKit aktif bir pencere sahnesine sahiptir |
| **Search quick action** | "Açık AramaTab()" → "searchPulse + = 1' → "BrowseCommandsView" (iOS 17+: oto-focus via "isPresented") |
| **Unknown command ID** | Derin bağlantı parsed ama navigasyon atladı - uyarı yok |

---

## Finger Shortcuts

### iPad & Mac (shared)

iPad'de Donanım klavyesi ve **iLinux** Mac Share:

| Shortcut | Eylem |
|----------|--------|
| ⌘F | Komutanlar sekmesi + arama ( iOS'ta hızlı bir eylem olarak niyet) |
| ⌘1 | Komutanlar sekmesi |
| ⌘2 | Kategoriler sekmesi |
| ⌘3 | Daily Quiz sekmesi |
| ⌘4 | Ayarlar sekmesi |

Arama otomatik-focus via .F requires **iOS 17.0+** veya **macOS 14.0+**.

### Mac sadece Mac

| Shortcut | Eylem |
|----------|--------|
| ⌘, | Ayarlar sekmesi |
| ⌘[ / Esc | Pop navigasyon yığını (geri) |
| ⌘← / ⌘→ | Önceki / sonraki kategori (Kategoriler sekmesi) |
| 1–4 | Test cevabı seçeneği seçeneği seçin |
| ⌘R | Reshuffle günlük test |
| Return | Sonraki sınav sorusu (ondan sonra) |

Derin bağlantılar ( `ilinux://` ) ve menü kısayolları Mac'de iOS'ta olduğu gibi aynı uygulama yönlendiricisini kullanır.

---

## Desteksiz ve Invalid URLs

| URL | Result |
|-----|--------|
| `ilinux://command` (no `name` / `cmd`) | Ignored |
| `ilinux://command?name=NotARealCmd` | Ignored (ID not in library for solution platform) |
| `ilinux://command?cmd=dir` (no platform) | Opens **Linux** kütüphanesi - Windows CMD için "platform=cmd" kullanın |
| `ilinux://search` via Shortcuts Open URL | **ILinux DeepLink tarafından parsed değil - **iOS /iPad** veya PadF üzerinde Hızlı Eylem kullanın **Mac/iPad ** |
| `ilinux://categories` via Shortcuts Open URL | Yukarıdaki gibi |
| `ilinux://feedback` / `ilinux://review` via Open URL | Yukarıdaki gibi |
| Non-`ilinux` schemes | Ignored |

---

## Sorun Giderme

**Shortcut uygulamayı açar ama hiçbir şey olmaz (cold lansmanı)**

Geri bildirim, Puan ve posta çarşafları başlatıldıktan sonra ~0.4 s gerekir. Uygulamanın içinde tekrar deneyin veya soğuk bir başlangıçta bir anı bekleyin.

**Hızlı eylem arama alanına odaklanmıyor (iOS 16)**

Auto-focus iOS 17+ gerektirir. iOS 16'da Komutlar sekmesi hala açılıyor; arama alanına el bas.

**Widget dokunuşu beklenen komutu açmaz**

komutun hala doğru ** platform** için yüklü uygulama sürüminizde var olmasını sağlayın. Widget bağlantıları, `ilinux://` + `iLinux://` ve tam bir komut ID'sini gerektirir: `platform` 'nin varsayılan Linux kütüphanesi değil.

**Quick-action başlıkları yanlış dildedir**

Change language in **Settings → Dil** - Uygulama otomatik olarak kayıt yaptırır.

** Deep link cihaz üzerinde çalışır, ancak bir web sayfasından değil**

Bağlantının kullanım biçimini onaylayın `ilinux://` ve sistem tarafından açılır ( Notlar/Messages'ta), striptizcilerin özel programları tarafından engellenmez.

---

[Back to iLinux Support](./) &middot; [FAQ](./faq) &middot; [Privacy Policy](./privacy)

</section>
