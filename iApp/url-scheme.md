---
layout: doc
title: iApp — Shortcut Links
app_id: iApp
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: iapp:// shortcut links — app detail, filtered Rankings, tab navigation, secondary pages, widgets, Live Activity, and Home Screen Quick Actions.
---

<section lang="en" markdown="1">

iApp supports **`iapp://`** and **`iappstore://`** shortcut links. Use them in **Shortcuts**, Safari bookmarks, or from **Home Screen widgets** and **Live Activity** to **open an app detail page**, **return to a filtered Rankings view**, **switch tabs**, or **jump to secondary pages** (developer favorites, browse history, rank tracking, and more).

> **Note:** Long-press **Home Screen Quick Actions** use the same `iapp://{host}` link text but are dispatched as quick actions — not parsed through the same path as Safari / Shortcuts URLs when opened from the icon menu only.

## Link format

```
iapp://...
iappstore://...   (older alias, works the same)
```

Hosts are **case-insensitive** and normalized to **kebab-case** (`developer_favorites` and `developer.favorites` → `developer-favorites`). Legacy aliases: `rankings` → rank, `subscribe` → subscription, `rate` → review.

| What you want | Link type |
|---------------|-----------|
| Open an app detail page | `iapp://app?...` |
| Open Rankings with filters | `iapp://rank?...` |
| Switch tabs or open settings pages | `iapp://{host}` (see tables below) |
| Tap an app in a widget | Opens the detail page |
| Tap the widget title / blank area | Opens the matching Rankings view |
| Tap a rank **Live Activity** | Opens the matching Rankings view |
| Tap a subscription **Live Activity** | Opens the app detail page |

---

## Open an app detail page

```
iapp://app?id={APP_ID}&region={region}&country={cc}
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `id` | **Yes** | App Store ID |
| `region` | No | Region code, e.g. `cn`, `us`, `jp` (default: `us`) |
| `country` | No | Optional region code if `region` is omitted |

**Example**

```
iapp://app?id=6446581591&region=cn
```

Used by: **My Favorites widget** (tap an app), **subscription Live Activity** (tap the activity), and **Shortcuts** / bookmarks.

---

## Open Rankings with filters

Switches to the **Rankings** tab and applies your chosen chart, category, and region.

```
iapp://rank?type={chart}&category={category}&region={region}
```

| Parameter | Description |
|-----------|-------------|
| `type` | Chart code (see table below) |
| `category` | Category code — main category or game subcategory |
| `region` | Region code, e.g. `cn`, `us` |

Unrecognized values are ignored; recognized values are remembered.

### Chart codes (`type`) — 12 charts

| Code | Chart |
|------|-------|
| `topFreeApplications` | iPhone Top Free |
| `topPaidApplications` | iPhone Top Paid |
| `topGrossingApplications` | iPhone Top Grossing |
| `newApplications` | New Apps |
| `newFreeApplications` | New Free |
| `newPaidApplications` | New Paid |
| `topFreeiPadApplications` | iPad Top Free |
| `topPaidiPadApplications` | iPad Top Paid |
| `topGrossingiPadApplications` | iPad Top Grossing |
| `topFreeMacApplications` | Mac Top Free |
| `topPaidMacApplications` | Mac Top Paid |
| `topGrossingMacApplications` | Mac Top Grossing |

### Category codes (`category`)

| Code | Category |
|------|----------|
| `0` | All Apps |
| `6014` | Games (all games) |
| `6005` | Social |
| `6007` | Productivity |
| `6002` | Utilities |
| `6008` | Photo & Video |
| `6017` | Education |
| `6015` | Finance |
| … | 26 main categories total |

**Game subcategories:** `7001`–`7009`, `7011`–`7019` (18 genres). Example: `7001` = Action.

### Examples

```
iapp://rank?type=topFreeApplications&category=6014&region=cn
iapp://rank?type=topFreeMacApplications&category=0&region=us
```

### Older Chinese-style links (still supported)

```
iapp://rank?type=热门免费榜&category=游戏&region=中国
```

Used by: **Rankings widget** (tap title / blank area), **rank Live Activity** (tap the activity), and **Shortcuts**.

---

## Widget deep links

Widgets do not use a separate URL format — they generate the same `iapp://app` and `iapp://rank` links automatically.

| Widget | Tap target | Opens |
|--------|------------|-------|
| **Rankings · iApp** | An app row | `iapp://app?id=…&region=…` |
| **Rankings · iApp** | Title or blank area | `iapp://rank?type=…&category=…&region=…` |
| **My Favorites · iApp** | An app row | `iapp://app?id=…&region=…` |

Pinned favorites appear first in the My Favorites widget. Widget theme and language follow **Settings → Widgets** and your app language (any of 18 languages). When configuring widget regions, HK / TW / MO show clearer display names in the list and unified search (e.g. “China”, “HK”); stored region **codes** in links remain `hk`, `tw`, `mo`.

---

## Browse history (not a URL link)

**App Browse History** is managed in **Settings → Data → App Browse History**. Tapping an entry reopens the detail page inside iApp — it does **not** use an `iapp://` URL you can copy or share externally.

---

## Live Activity deep links

| Live Activity type | Tap behavior | Link generated |
|--------------------|--------------|----------------|
| **Rankings** (tracking preset) | Opens filtered Rankings | `iapp://rank?…` |
| **Subscriptions** (per subscription) | Opens app detail | `iapp://app?id=…&region=…` |

Enable rank Live Activity per tracking preset in **Settings → Advanced**. Enable subscription Live Activity in **Settings → Advanced → Live Activity** (separate from rank Live Activity); then per subscription when adding or editing. Price-drop monitors show baseline vs current price on the Lock Screen.

---

## Tab & action links (no query)

These open a tab or trigger an in-app action. Works from **Shortcuts**, Safari, and **Home Screen Quick Actions**.

### Primary tabs

| URL | Opens |
|-----|--------|
| `iapp://search` | Search tab + focus search field |
| `iapp://rank` | Rankings tab (no filter change when no query) |
| `iapp://favorites` | **Favorites tab** if enabled in **Settings → App Settings**; otherwise **Settings → App Favorites** |
| `iapp://subscription` | Subscriptions tab if visible; otherwise **Settings → Subscriptions** |
| `iapp://settings` | Settings tab |
| `iapp://feedback` | Feedback email |
| `iapp://review` | In-app App Store rating (alias: `iapp://rate`) |

### Secondary pages

Opens **Settings** tab first, then pushes the target page. If a matching tab exists (e.g. Developer Favorites), opens that tab instead.

| URL | Opens |
|-----|--------|
| `iapp://developer-favorites` | Developer Favorites tab or **Settings → Developer Favorites** |
| `iapp://browse-history` | **Settings → Data → App Browse History** |
| `iapp://favorite-groups` | **Settings → Data → Favorite Groups** |
| `iapp://rank-tracking` | **Settings → Advanced → Rank Tracking** |
| `iapp://live-activity` | **Settings → Advanced → Live Activity** |
| `iapp://apple-services` | **Settings → Third-party → Apple Services** |
| `iapp://region-switch` | **Settings → Third-party → App Store Region** |
| `iapp://usage-guide` | **Settings → Help → Usage Instructions** |
| `iapp://widget-guide` | **Settings → Widgets → Widget Guide** (iOS 17+ only; URL works but not listed in Quick Actions picker) |

---

## Home Screen Quick Actions

Long-press the app icon. Customize up to **4** from **15** options in **Settings → Home Screen Long Press → Customize Shortcuts**.

Default selection: search, rank, favorites, feedback.

Each option uses `iapp://{host}` — same URLs as above. Quick actions are dispatched through the icon menu; external Shortcuts / Safari use the unified `handleURL` path.

| Link | Opens |
|------|--------|
| `iapp://search` | Search tab + focus |
| `iapp://rank` | Rankings tab |
| `iapp://favorites` | Favorites tab or Settings → App Favorites |
| `iapp://developer-favorites` | Developer Favorites tab or Settings → Developer Favorites |
| `iapp://subscription` | Subscriptions tab or Settings → Subscriptions |
| `iapp://browse-history` | App Browse History |
| `iapp://favorite-groups` | Favorite Groups settings |
| `iapp://rank-tracking` | Rank Tracking |
| `iapp://live-activity` | Live Activity settings |
| `iapp://apple-services` | Apple Services links |
| `iapp://region-switch` | App Store Region switch |
| `iapp://usage-guide` | Usage Instructions |
| `iapp://settings` | Settings tab |
| `iapp://feedback` | Feedback email |
| `iapp://review` | In-app rating |

`iapp://widget-guide` is supported as an external URL but **not** available in the Quick Actions picker.

---

## Siri & Shortcuts (iOS 16+)

Find built-in actions in the **Shortcuts** app or ask **Siri**. All intent titles, parameter labels, and Siri phrases are **fully localized** in every app language — they update when you change **Settings → Appearance → Language**.

| Action | What you can set | Effect |
|--------|------------------|--------|
| Search apps | Keyword and region | Opens Search tab with query |
| Open charts | Chart, category, and region | Opens Rankings with filters (same as `iapp://rank`) |
| Add favorite | App ID and region | Adds to favorites silently |

**Example Siri phrases (English UI):** *"Search apps in iApp"*, *"Open charts in iApp"*, *"Add favorite in iApp"*. In 简体中文, phrases appear in Chinese; same for all 18 languages.

---

## Mac keyboard shortcuts

On Mac, use **⌘1** through **⌘N** to switch tabs. Numbers are assigned **dynamically** based on which tabs are visible:

| When visible | Typical shortcut |
|--------------|------------------|
| Rankings | ⌘1 |
| Search | ⌘2 |
| Subscriptions (if shown) | Next number |
| Favorites (if tab enabled) | Next number |
| Developer Favorites (if tab enabled) | Next number |
| Settings | Last number |

Example with all optional tabs on: ⌘1 Rankings · ⌘2 Search · ⌘3 Subscriptions · ⌘4 Favorites · ⌘5 Developer Favorites · ⌘6 Settings.

When a tab is hidden, remaining tabs renumber automatically.

---

## Region codes in links

Deep links and widget-generated URLs always use stable **region codes** (`cn`, `us`, `hk`, `tw`, `mo`, …) — not localized display names. Region pickers and search may show clearer labels, but stored codes stay the same.

**Examples**

```
iapp://app?id=6446581591&region=hk
iapp://rank?type=topFreeApplications&category=0&region=tw
```

---

## In-app search (not URL links)

These work inside iApp but are **not** `iapp://` URLs:

| Action | How |
|--------|-----|
| **Single App ID search** | Enter one numeric ID (6–12 digits, no comma) in Search |
| **Batch App ID search** | Up to 50 comma-separated IDs |
| **Add Subscription** | Long-press any app row |
| **Save Developer** | Long-press → **Developer** submenu, or detail **More** menu |
| **Open by-ranking view** | Context menu → same-developer apps or developer favorites |
| **Pause / resume subscription** | Long-press on a subscription row |
| **Reopen from browse history** | **Settings → Data → App Browse History** → tap entry |

Use **`iapp://`** links or **Siri / Shortcuts** when you need to open iApp from outside the app.

---

## Tips

- Link codes work in any app language — they do not change when you switch UI language.
- Widgets and **Live Activity** generate these links automatically when you tap.
- Widget chart data for some Mac/iPad paid and grossing charts may differ slightly from the main app.
- **Add favorite** via Shortcuts does not open the app UI — it writes directly to your favorites list.
- **Content compare** mode in all-region info cannot export share images — switch to list or grid view first.

[Back to overview](..) · [FAQ](faq) · [Privacy](privacy)

</section>

<section lang="zh-CN" markdown="1">

爱应用支持 **`iapp://`** 与 **`iappstore://`** 快捷链接。可在**快捷指令**、Safari 书签，或从**主屏小组件**、**实时活动**中用来**打开应用详情**、**回到对应榜单**、**切换 Tab**，或**直达二级页面**（开发者收藏、浏览记录、榜单追踪等）。

> **注：** 长按图标的**主屏快捷指令**使用相同的 `iapp://{host}` 链接文字，但由独立机制处理——只能从图标菜单触发。

## 链接格式

```
iapp://...
iappstore://...   （旧版别名，效果相同）
```

Host **不区分大小写**，并规范化为 **kebab-case**（`developer_favorites`、`developer.favorites` → `developer-favorites`）。旧版别名：`rankings` → rank，`subscribe` → subscription，`rate` → review。

| 目的 | 链接类型 |
|------|----------|
| 打开应用详情 | `iapp://app?...` |
| 打开带筛选的榜单 | `iapp://rank?...` |
| 切换 Tab 或打开设置页 | `iapp://{host}`（见下表） |
| 点击小组件中的应用 | 打开详情页 |
| 点击小组件标题 / 空白区 | 打开对应榜单 |
| 点击榜单**实时活动** | 打开对应榜单 |
| 点击订阅**实时活动** | 打开应用详情 |

---

## 打开应用详情

```
iapp://app?id={APP_ID}&region={地区代码}
```

| 参数 | 必填 | 说明 |
|------|------|------|
| `id` | **是** | App Store ID |
| `region` | 否 | 地区代码，如 `cn`、`us`、`jp`（默认 `us`） |
| `country` | 否 | 省略 `region` 时可用的地区代码 |

**示例**

```
iapp://app?id=6446581591&region=cn
```

用于：**我的收藏**小组件（点击应用）、**订阅实时活动**（点击活动）、**快捷指令** / 书签。

---

## 打开榜单并应用筛选

切换到**榜单** Tab，并应用你指定的榜单、分类与地区。

```
iapp://rank?type={榜单代码}&category={分类代码}&region={地区代码}
```

### 榜单代码（`type`）— 12 种

| 代码 | 榜单 |
|------|------|
| `topFreeApplications` | iPhone 热门免费 |
| `topPaidApplications` | iPhone 热门付费 |
| `topGrossingApplications` | iPhone 畅销 |
| `newApplications` | 新上架 |
| `newFreeApplications` | 新上架免费 |
| `newPaidApplications` | 新上架付费 |
| `topFreeiPadApplications` | iPad 热门免费 |
| `topPaidiPadApplications` | iPad 热门付费 |
| `topGrossingiPadApplications` | iPad 畅销 |
| `topFreeMacApplications` | Mac 热门免费 |
| `topPaidMacApplications` | Mac 热门付费 |
| `topGrossingMacApplications` | Mac 畅销 |

### 分类代码（`category`）

| 代码 | 分类 |
|------|------|
| `0` | 所有 App |
| `6014` | 游戏（全部） |
| `6005` | 社交 |
| `6007` | 效率 |
| `6002` | 工具 |
| `6008` | 摄影与录像 |
| … | 共 26 个主分类 |

**游戏子分类：** `7001`–`7009`、`7011`–`7019`（18 个）。例：`7001` = 动作。

### 示例

```
iapp://rank?type=topFreeApplications&category=6014&region=cn
```

### 旧版中文链接（仍支持）

```
iapp://rank?type=热门免费榜&category=游戏&region=中国
```

用于：**榜单**小组件（点击标题 / 空白区）、**榜单实时活动**（点击活动）、**快捷指令**。

---

## 小组件快捷链接

小组件无独立 URL 格式，自动生成相同的 `iapp://app` 与 `iapp://rank` 链接。

| 小组件 | 点击目标 | 打开 |
|--------|----------|------|
| **榜单 · iApp** | 应用行 | `iapp://app?id=…&region=…` |
| **榜单 · iApp** | 标题或空白区 | `iapp://rank?type=…&category=…&region=…` |
| **我的收藏 · iApp** | 应用行 | `iapp://app?id=…&region=…` |

我的收藏小组件中**置顶应用优先**显示。主题与语言跟随 **设置 → 小组件** 及应用语言（支持 18 种语言）。配置小组件地区时，港 / 台 / 澳在列表与搜索中显示更清晰名称；链接中的地区**代码**仍为 `hk` / `tw` / `mo`。

---

## 浏览记录（非 URL 链接）

**App 浏览记录**在 **设置 → 数据 → App 浏览记录** 中管理。点按条目可在应用内重新打开详情页——**不能**复制为可分享的 `iapp://` 链接。

---

## 实时活动快捷链接

| 实时活动类型 | 点击行为 | 生成的链接 |
|--------------|----------|------------|
| **榜单**（追踪预设） | 打开对应榜单 | `iapp://rank?…` |
| **订阅**（单项订阅） | 打开应用详情 | `iapp://app?id=…&region=…` |

在 **设置 → 高级** 中为追踪预设启用榜单实时活动；在 **设置 → 高级 → 实时活动** 中开启订阅实时活动（与榜单独立）；添加 / 编辑订阅时为单项启用。降价监控在锁屏显示基准价与现价。

---

## Tab 与动作链接（无 query）

可在**快捷指令**、Safari 与**主屏快捷指令**中使用。

### 一级 Tab

| 链接 | 打开 |
|------|------|
| `iapp://search` | 搜索 Tab 并聚焦搜索框 |
| `iapp://rank` | 榜单 Tab（无 query 时不改变筛选） |
| `iapp://favorites` | 若已开启收藏 Tab 则打开**收藏 Tab**；否则 **设置 → App 收藏夹** |
| `iapp://subscription` | 订阅 Tab（若可见）；否则 **设置 → 订阅** |
| `iapp://settings` | 设置 Tab |
| `iapp://feedback` | 意见反馈 |
| `iapp://review` | 应用内评分（别名：`iapp://rate`） |

### 二级页面

先切换到**设置** Tab，再推入目标页面。若对应 Tab 已开启（如开发者收藏），则直接打开该 Tab。

| 链接 | 打开 |
|------|------|
| `iapp://developer-favorites` | 开发者收藏 Tab 或 **设置 → 开发者收藏** |
| `iapp://browse-history` | **设置 → 数据 → App 浏览记录** |
| `iapp://favorite-groups` | **设置 → 数据 → 收藏分组** |
| `iapp://rank-tracking` | **设置 → 高级 → 榜单追踪** |
| `iapp://live-activity` | **设置 → 高级 → 实时活动** |
| `iapp://apple-services` | **设置 → 三方服务 → 苹果常用网站** |
| `iapp://region-switch` | **设置 → 三方服务 → App Store 地区** |
| `iapp://usage-guide` | **设置 → 帮助 → 使用说明** |
| `iapp://widget-guide` | **设置 → 小组件 → 小组件指南**（仅 iOS 17+；URL 可用但不在快捷指令可选列表中） |

---

## 主屏快捷指令

长按应用图标触发。在 **设置 → 主屏图标长按 → 自定义快捷指令** 中从 **15 项**里最多选 **4 项**。

默认：搜索、榜单、收藏、反馈。每项使用 `iapp://{host}`，与上表 URL 相同。

| 链接 | 打开 |
|------|------|
| `iapp://search` | 搜索 Tab 并聚焦 |
| `iapp://rank` | 榜单 Tab |
| `iapp://favorites` | 收藏 Tab 或 设置 → App 收藏夹 |
| `iapp://developer-favorites` | 开发者收藏 Tab 或 设置 → 开发者收藏 |
| `iapp://subscription` | 订阅 Tab 或 设置 → 订阅 |
| `iapp://browse-history` | App 浏览记录 |
| `iapp://favorite-groups` | 收藏分组 |
| `iapp://rank-tracking` | 榜单追踪 |
| `iapp://live-activity` | 实时活动设置 |
| `iapp://apple-services` | 苹果常用网站 |
| `iapp://region-switch` | App Store 地区切换 |
| `iapp://usage-guide` | 使用说明 |
| `iapp://settings` | 设置 Tab |
| `iapp://feedback` | 意见反馈 |
| `iapp://review` | 应用内评分 |

`iapp://widget-guide` 支持外部 URL 打开，但**不在**主屏快捷指令可选列表中。

---

## Siri 与快捷指令（iOS 16+）

在**快捷指令** App 中添加内置操作，或对 **Siri** 说出指令。所有操作标题、参数名称与 Siri 短语在 **18 种应用语言**中**完整本地化**——切换 **设置 → 外观 → 语言** 后同步更新。

| 操作 | 可设置内容 | 效果 |
|------|------------|------|
| 搜索应用 | 关键词与地区 | 打开搜索 Tab 并填入查询 |
| 打开榜单 | 榜单、分类与地区 | 打开榜单并应用筛选（同 `iapp://rank`） |
| 添加收藏 | App ID 与地区 | 静默添加到收藏夹 |

**示例（英文界面）：** *「Search apps in iApp」*；简体中文界面下短语为中文。

---

## Mac 键盘快捷键

Mac 上可用 **⌘1** 至 **⌘N** 切换 Tab，编号**随可见 Tab 动态分配**（含可选的收藏 Tab、开发者收藏 Tab）。全部可选 Tab 开启时示例：⌘1 榜单 · ⌘2 搜索 · ⌘3 订阅 · ⌘4 收藏 · ⌘5 开发者收藏 · ⌘6 设置。

---

## 链接中的地区代码

快捷链接与小组件生成的 URL 始终使用稳定的**地区代码**（`cn`、`hk`、`tw`、`mo` 等），而非界面显示名称。地区选择器中的展示名可以不同，但存储代码不变。

---

## 应用内搜索与操作（非 URL 链接）

| 操作 | 方式 |
|------|------|
| **单个 App ID 搜索** | 搜索框输入 6–12 位数字 ID（无逗号） |
| **批量 App ID** | 最多 50 个逗号分隔 ID |
| **加入订阅** | 长按任意应用行 |
| **收藏开发者** | 长按 → **开发者**子菜单 |
| **从浏览记录打开** | **设置 → 数据 → App 浏览记录** → 点按条目 |

从应用外部打开请使用 **`iapp://` 链接**或 **Siri / 快捷指令**。

---

## 提示

- 链接代码不随界面语言变化。
- 小组件与**实时活动**点击时自动生成上述链接。
- 通过快捷指令**添加收藏**不会打开应用界面。
- **内容对比**模式不可导出分享图——请先切回列表或网格视图。

[返回概览](..) · [常见问题](faq) · [隐私政策](privacy)

</section>

<section lang="zh-TW" markdown="1">

愛應用支援 **`iapp://`** 與 **`iappstore://`** 快捷連結。可在**捷徑**、Safari 書籤，或從**主畫面小工具**、**即時動態**中用來**開啟應用詳情**、**回到對應榜單**、**切換 Tab**，或**直達二級頁面**（開發者收藏、瀏覽記錄、榜單追蹤等）。

> **註：** 長按圖示的**主畫面捷徑**使用相同的 `iapp://{host}` 連結文字，但由獨立機制處理——只能從圖示選單觸發。

## 連結格式

```
iapp://...
iappstore://...   （舊版別名，效果相同）
```

Host **不區分大小寫**，並規範化為 **kebab-case**（`developer_favorites`、`developer.favorites` → `developer-favorites`）。舊版別名：`rankings` → rank，`subscribe` → subscription，`rate` → review。

| 目的 | 連結類型 |
|------|----------|
| 開啟應用詳情 | `iapp://app?...` |
| 開啟帶篩選的榜單 | `iapp://rank?...` |
| 切換 Tab 或開啟設定頁 | `iapp://{host}`（見下表） |
| 點擊小工具中的應用 | 開啟詳情頁 |
| 點擊小工具標題 / 空白區 | 開啟對應榜單 |
| 點擊榜單**即時動態** | 開啟對應榜單 |
| 點擊訂閱**即時動態** | 開啟應用詳情 |

---

## 開啟應用詳情

```
iapp://app?id={APP_ID}&region={地區代碼}
```

| 參數 | 必填 | 說明 |
|------|------|------|
| `id` | **是** | App Store ID |
| `region` | 否 | 地區代碼，如 `cn`、`us`、`jp`（預設 `us`） |
| `country` | 否 | 省略 `region` 時可用的地區代碼 |

**範例**

```
iapp://app?id=6446581591&region=cn
```

用於：**我的收藏**小工具（點擊應用）、**訂閱即時動態**（點擊活動）、**捷徑** / 書籤。

---

## 開啟榜單並套用篩選

切換至**榜單** Tab，並套用你指定的榜單、分類與地區。

```
iapp://rank?type={榜單代碼}&category={分類代碼}&region={地區代碼}
```

### 榜單代碼（`type`）— 12 種

| 代碼 | 榜單 |
|------|------|
| `topFreeApplications` | iPhone 熱門免費 |
| `topPaidApplications` | iPhone 熱門付費 |
| `topGrossingApplications` | iPhone 暢銷 |
| `newApplications` | 新上架 |
| `newFreeApplications` | 新上架免費 |
| `newPaidApplications` | 新上架付費 |
| `topFreeiPadApplications` | iPad 熱門免費 |
| `topPaidiPadApplications` | iPad 熱門付費 |
| `topGrossingiPadApplications` | iPad 暢銷 |
| `topFreeMacApplications` | Mac 熱門免費 |
| `topPaidMacApplications` | Mac 熱門付費 |
| `topGrossingMacApplications` | Mac 暢銷 |

### 分類代碼（`category`）

| 代碼 | 分類 |
|------|------|
| `0` | 所有 App |
| `6014` | 遊戲（全部） |
| `6005` | 社交 |
| `6007` | 效率 |
| `6002` | 工具 |
| `6008` | 攝影與錄影 |
| … | 共 26 個主分類 |

**遊戲子分類：** `7001`–`7009`、`7011`–`7019`（18 個）。例：`7001` = 動作。

### 範例

```
iapp://rank?type=topFreeApplications&category=6014&region=cn
```

### 舊版中文連結（仍支援）

```
iapp://rank?type=热门免费榜&category=游戏&region=中国
```

用於：**榜單**小工具（點擊標題 / 空白區）、**榜單即時動態**（點擊活動）、**捷徑**。

---

## 小工具快捷連結

小工具無獨立 URL 格式，自動產生相同的 `iapp://app` 與 `iapp://rank` 連結。

| 小工具 | 點擊目標 | 開啟 |
|--------|----------|------|
| **榜單 · iApp** | 應用列 | `iapp://app?id=…&region=…` |
| **榜單 · iApp** | 標題或空白區 | `iapp://rank?type=…&category=…&region=…` |
| **我的收藏 · iApp** | 應用列 | `iapp://app?id=…&region=…` |

我的收藏小工具中**置頂應用優先**顯示。主題與語言跟隨 **設定 → 小工具** 及應用語言（支援 18 種語言）。設定小工具地區時，港 / 台 / 澳在列表與搜尋中顯示更清晰名稱；連結中的地區**代碼**仍為 `hk` / `tw` / `mo`。

---

## 瀏覽記錄（非 URL 連結）

**App 瀏覽記錄**在 **設定 → 資料 → App 瀏覽記錄** 中管理。點按條目可在應用內重新開啟詳情頁——**不能**複製為可分享的 `iapp://` 連結。

---

## 即時動態快捷連結

| 即時動態類型 | 點擊行為 | 產生的連結 |
|--------------|----------|------------|
| **榜單**（追蹤預設） | 開啟對應榜單 | `iapp://rank?…` |
| **訂閱**（單項訂閱） | 開啟應用詳情 | `iapp://app?id=…&region=…` |

在 **設定 → 進階** 中為追蹤預設啟用榜單即時動態；在 **設定 → 進階 → 即時動態** 中開啟訂閱即時動態（與榜單獨立）；新增 / 編輯訂閱時為單項啟用。降價監控在鎖定畫面顯示基準價與現價。

---

## Tab 與動作連結（無 query）

可在**捷徑**、Safari 與**主畫面捷徑**中使用。

### 一級 Tab

| 連結 | 開啟 |
|------|------|
| `iapp://search` | 搜尋 Tab 並聚焦搜尋列 |
| `iapp://rank` | 榜單 Tab（無 query 時不改變篩選） |
| `iapp://favorites` | 若已開啟收藏 Tab 則開啟**收藏 Tab**；否則 **設定 → App 收藏夾** |
| `iapp://subscription` | 訂閱 Tab（若可見）；否則 **設定 → 訂閱** |
| `iapp://settings` | 設定 Tab |
| `iapp://feedback` | 意見回饋 |
| `iapp://review` | 應用內評分（別名：`iapp://rate`） |

### 二級頁面

先切換至**設定** Tab，再推入目標頁面。若對應 Tab 已開啟（如開發者收藏），則直接開啟該 Tab。

| 連結 | 開啟 |
|------|------|
| `iapp://developer-favorites` | 開發者收藏 Tab 或 **設定 → 開發者收藏** |
| `iapp://browse-history` | **設定 → 資料 → App 瀏覽記錄** |
| `iapp://favorite-groups` | **設定 → 資料 → 收藏分組** |
| `iapp://rank-tracking` | **設定 → 進階 → 榜單追蹤** |
| `iapp://live-activity` | **設定 → 進階 → 即時動態** |
| `iapp://apple-services` | **設定 → 三方服務 → 蘋果常用網站** |
| `iapp://region-switch` | **設定 → 三方服務 → App Store 地區** |
| `iapp://usage-guide` | **設定 → 幫助 → 使用說明** |
| `iapp://widget-guide` | **設定 → 小工具 → 小工具指南**（僅 iOS 17+；URL 可用但不在捷徑可選列表中） |

---

## 主畫面捷徑

長按應用圖示觸發。在 **設定 → 主畫面圖示長按 → 自訂捷徑** 中從 **15 項**裡最多選 **4 項**。

預設：搜尋、榜單、收藏、回饋。每項使用 `iapp://{host}`，與上表 URL 相同。

| 連結 | 開啟 |
|------|------|
| `iapp://search` | 搜尋 Tab 並聚焦 |
| `iapp://rank` | 榜單 Tab |
| `iapp://favorites` | 收藏 Tab 或 設定 → App 收藏夾 |
| `iapp://developer-favorites` | 開發者收藏 Tab 或 設定 → 開發者收藏 |
| `iapp://subscription` | 訂閱 Tab 或 設定 → 訂閱 |
| `iapp://browse-history` | App 瀏覽記錄 |
| `iapp://favorite-groups` | 收藏分組 |
| `iapp://rank-tracking` | 榜單追蹤 |
| `iapp://live-activity` | 即時動態設定 |
| `iapp://apple-services` | 蘋果常用網站 |
| `iapp://region-switch` | App Store 地區切換 |
| `iapp://usage-guide` | 使用說明 |
| `iapp://settings` | 設定 Tab |
| `iapp://feedback` | 意見回饋 |
| `iapp://review` | 應用內評分 |

`iapp://widget-guide` 支援外部 URL 開啟，但**不在**主畫面捷徑可選列表中。

---

## Siri 與捷徑（iOS 16+）

在**捷徑** App 中新增內建操作，或對 **Siri** 說出指令。所有操作標題、參數名稱與 Siri 短語在 **18 種應用語言**中**完整本地化**——切換 **設定 → 外觀 → 語言** 後同步更新。

| 操作 | 可設定內容 | 效果 |
|------|------------|------|
| 搜尋應用 | 關鍵字與地區 | 開啟搜尋 Tab 並填入查詢 |
| 開啟榜單 | 榜單、分類與地區 | 開啟榜單並套用篩選（同 `iapp://rank`） |
| 新增收藏 | App ID 與地區 | 靜默新增至收藏夾 |

---

## Mac 鍵盤快捷鍵

Mac 上可用 **⌘1** 至 **⌘N** 切換 Tab，編號**隨可見 Tab 動態分配**（含可選的收藏 Tab、開發者收藏 Tab）。隱藏 Tab 時其餘 Tab 自動重新編號。

---

## 連結中的地區代碼

快捷連結與小工具產生的 URL 始終使用穩定的**地區代碼**（`cn`、`hk`、`tw`、`mo` 等）。地區選擇器中的展示名可以不同，但儲存代碼不變。

---

## 應用內搜尋與操作（非 URL 連結）

| 操作 | 方式 |
|------|------|
| **單個 App ID 搜尋** | 搜尋列輸入 6–12 位數字 ID（無逗號） |
| **加入訂閱** | 長按任意應用列 |
| **收藏開發者** | 長按 → **開發者**子選單 |
| **從瀏覽記錄開啟** | **設定 → 資料 → App 瀏覽記錄** |

從應用外部開啟請使用 **`iapp://` 連結**或 **Siri / 捷徑**。

---

## 提示

- 連結代碼不隨介面語言變化。
- **內容對比**模式不可匯出分享圖——請先切回列表或網格檢視。

[返回概覽](..) · [常見問題](faq) · [隱私政策](privacy)

</section>
