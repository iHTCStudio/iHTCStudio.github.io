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

[Back to overview](..) · [FAQ](../faq) · [Privacy](../privacy)

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

[返回概览](..) · [常见问题](../faq) · [隐私政策](../privacy)

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

[返回概覽](..) · [常見問題](../faq) · [隱私政策](../privacy)

</section>
<section lang="ja" markdown="1">

iAppは** `iapp://` **と** `iappstore://` **のショートカットリンクをサポートしています。 *Shortcuts**、Safariブックマーク、または**ホームスクリーンウィジェット**と**ライブアクティビティ**で、アプリ詳細ページを開く**、**フィルタリングされたランキングビューに戻る**、**スイッチタブ**、または**二次ページへのジャンプ**(開発者のお気に入り、閲覧履歴、ランクトラッキングなど)。

> **注意:** ロングプレス **ホーム画面クイックアクション** は、同じ `iapp://` リンクテキストを使用しますが、クイックアクションとしてディスパッチされます。ただし、アイコンメニューから開くと、Safari / Shortcuts URLと同じパスをパースするわけではありません。

## リンク形式


```
iapp://...
iappstore://...   (older alias, works the same)
```


**kebab-case** ( `iapp://` および `iappstore://` レガシーエイリアス: `developer_favorites` → ランク、 `developer.favorites` → サブスクリプション、 `developer-favorites` → レビュー。

| What you want | リンクの種類 |
|---------------|-----------|
| Open an app detail page | iapp://app?... |
| Open Rankings with filters | 「iapp://rank?...」 |
| Switch tabs or open settings pages | `iapp://{host}` (下の表を参照) |
| Tap an app in a widget | 詳細ページを開く |
| Tap the widget title / blank area | マッチングランキングビューを開く |
| Tap a rank **Live Activity** | マッチングランキングビューを開く |
| Tap a subscription **Live Activity** | アプリ詳細ページを開く |

---

## アプリ詳細ページを開く


```
iapp://app?id={APP_ID}&region={region}&country={cc}
```


| Parameter | Required | コンテンツ |
|-----------|----------|-------------|
| `id` | **Yes** | アプリストアID |
| `region` | No | 地域コード、例えば `cn`、`us`、`jp` (デフォルト: `us`) |
| `country` | No | `region` が省略された場合のオプションの地域コード |

**例**


```
iapp://app?id=6446581591&region=cn
```


によって使用される:**My Favoritesウィジェット**(アプリをタップ)、**サブスクリプションライブアクティビティ**(アクティビティをタップ)、**ショートカット** /ブックマーク。

---

## フィルターでランキングを開く

**Rankings**タブに切り替えて、選択したチャート、カテゴリ、および地域に適用されます。


```
iapp://rank?type={chart}&category={category}&region={region}
```


| Parameter | コンテンツ |
|-----------|-------------|
| `type` | チャートコード(下表参照) |
| `category` | カテゴリコード — 主なカテゴリまたはゲームサブカテゴリ |
| `region` | 地域コード、例えば `cn`、`us` |

認識されていない値は無視されます。認識された値は記憶されます。

### チャートコード( `iapp://` ) — 12 チャート

| Code | チャート |
|------|-------|
| `topFreeApplications` | iPhoneトップ無料 |
| `topPaidApplications` | iPhoneトップ有料 |
| `topGrossingApplications` | iPhoneのトップの総計 |
| `newApplications` | 新しいアプリ |
| `newFreeApplications` | 新しい無料 |
| `newPaidApplications` | 新しい有料 |
| `topFreeiPadApplications` | iPadのトップ無料 |
| `topPaidiPadApplications` | iPadトップ有料 |
| `topGrossingiPadApplications` | iPadの上の総計 |
| `topFreeMacApplications` | Macトップ無料 |
| `topPaidMacApplications` | Macのトップ有料 |
| `topGrossingMacApplications` | Macのトップの総計 |

### 分類コード( `iapp://` )

| Code | カテゴリー |
|------|----------|
| `0` | すべてのアプリ |
| `6014` | ゲーム(すべてのゲーム) |
| `6005` | 社会招聘 |
| `6007` | 生産性 |
| `6002` | ユーティリティ |
| `6008` | フォト&ビデオ |
| `6017` | 教育機関 |
| `6015` | ファイナンス |
| … | 26 主なカテゴリ 合計 |

**ゲームサブカテゴリ:** `iapp://` 例: `developer.favorites` = アクション。

### 例


```
iapp://rank?type=topFreeApplications&category=6014&region=cn
iapp://rank?type=topFreeMacApplications&category=0&region=us
```


### 古い中国スタイルのリンク(サポートされる)


```
iapp://rank?type=热门免费榜&category=游戏&region=中国
```


によって使用される:**Rankingsウィジェット**(tap title / blank area)、**rank Live Activity**(アクティビティをタップ)、**ショートカット**。

---

## ウィジェットディープリンク

Widgets は別の URL 形式を使用しないため、同じ `iapp://` と `iappstore://` が自動的に生成されます。

| Widget | Tap target | オープン |
|--------|------------|-------|
| **Rankings · iApp** | An app row | iapp://app?id=...&region=... |
| **Rankings · iApp** | Title or blank area | 「iapp://rank?type=...&category=...&region=...」 |
| **My Favorites · iApp** | An app row | iapp://app?id=...&region=... |

私のお気に入りウィジェットで最初にピン留めされたお気に入りが表示されます。 ウィジェットのテーマと言語は、**Settings → Widgets**とアプリの言語(18言語のいずれか)に従います。 ウィジェットの領域を設定するとき、HK / TW / MOはリストと統一された検索(例:「中国」、「HK」);保存された領域**は、 `iapp://` 、 `iappstore://` 、 `iapp://{host}` に残ります。

---

## 履歴を参照する(URLリンクではありません)

**App Browses History** は、**Settings → Data → App Browses History** で管理されています。 エントリーをタップすると、iApp内の詳細ページが開きます。**not** は、外部にコピーまたは共有できる `iapp://` URL を使用します。

---

## ライブ活動ディープリンク

| Live Activity type | Tap behavior | 生成されるリンク |
|--------------------|--------------|----------------|
| **Rankings** (tracking preset) | Opens filtered Rankings | 「iapp://rank?...」 |
| **Subscriptions** (per subscription) | Opens app detail | iapp://app?id=...&region=... |

**Settings → Advanced** でプリセットを追跡するためのランクライブアクティビティを有効にします。**Settings → Advanced → Live Activity** でサブスクリプションライブアクティビティを有効にします。その後、追加または編集するときにサブスクリプションごとに設定します。 価格低下モニターは、ロック画面上のベースライン対現在の価格を示しています。

---

## タブ&アクションリンク(クエリなし)

タブを開き、アプリ内アクションをトリガーします。 **ショートカット**、Safari、**ホーム画面のクイックアクション**から動作します。

### プライマリタブ

| URL | 開く画面 |
|-----|--------|
| `iapp://search` | 検索タブ + フォーカス検索フィールド |
| `iapp://rank` | ランキングタブ(クエリなしのフィルタ変更なし) |
| `iapp://favorites` | **Favoritesタブ** **Settings → App Settings**で有効にされている場合; それ以外の **Settings → App Favorites** |
| `iapp://subscription` | サブスクリプションタブが表示された場合; その他 **設定 → サブスクリプション** |
| `iapp://settings` | 設定タブ |
| `iapp://feedback` | フィードバックメール |
| `iapp://review` | アプリ内アプリストアの評価(別名:`iapp://rate`) |

### 二次ページ

[Settings**]タブを最初に開き、対象ページを押します。 マッチングタブが存在している場合(開発者のお気に入りなど)、代わりにタブを開きます。

| URL | 開く画面 |
|-----|--------|
| `iapp://developer-favorites` | 開発者のお気に入りタブまたは**設定 → 開発者のお気に入り** |
| `iapp://browse-history` | **設定 → データ → アプリの閲覧履歴** |
| `iapp://favorite-groups` | **設定→データ→お気に入りグループ** |
| `iapp://rank-tracking` | **設定 → アドバンスト → ランクトラッキング** |
| `iapp://live-activity` | **設定 → アドバンスト → ライブアクティビティ** |
| `iapp://apple-services` | **設定 → サードパーティ → Apple サービス** |
| `iapp://region-switch` | **設定 → サードパーティ → App Store Region** |
| `iapp://usage-guide` | **設定→ヘルプ→使用説明書** |
| `iapp://widget-guide` | **設定 → ウィジェット → ウィジェットガイド** (iOS 17 + のみ; URL は、クイックアクションピッカーにリストされていない) |

---

## ホーム スクリーンの速い行為

アプリアイコンを長押しします。 **15**オプションから**4**までカスタマイズできます。

デフォルト選択:検索、ランク、お気に入り、フィードバック。

各オプションは、上記と同じURLを使用します。 クイックアクションは、アイコンメニューでディスパッチされます。 外部ショートカット/Safariは、統一された `iappstore://` パスを使用します。

| リンク | 開く画面 |
|------|--------|
| `iapp://search` | 検索タブ + フォーカス |
| `iapp://rank` | ランキングタブ |
| `iapp://favorites` | お気に入りタブまたは設定 → アプリお気に入り |
| `iapp://developer-favorites` | 開発者のお気に入りタブまたは設定 → 開発者のお気に入り |
| `iapp://subscription` | サブスクリプションタブまたは設定 → サブスクリプション |
| `iapp://browse-history` | App 閲覧履歴 |
| `iapp://favorite-groups` | お気に入りグループの設定 |
| `iapp://rank-tracking` | ランクトラッキング |
| `iapp://live-activity` | ライブアクティビティの設定 |
| `iapp://apple-services` | Appleサービスリンク |
| `iapp://region-switch` | App Storeの地域スイッチ |
| `iapp://usage-guide` | 使用法 指示 |
| `iapp://settings` | 設定タブ |
| `iapp://feedback` | フィードバックメール |
| `iapp://review` | アプリ内評価 | `iapp://` は外部 URL としてサポートしていますが、Quick Actions のピッカーでは利用できません。

---

## シリ & ショートカット (iOS 16+)

**ショートカット**アプリでビルトインアクションを検索するか、**Siri**を尋ねます。 すべてのインテントタイトル、パラメータラベル、およびシリフレーズは、すべてのアプリ言語で**十分にローカライズされています。**設定→外観→言語**を変更したときに更新されます。

| Action | What you can set | エフェクト |
|--------|------------------|--------|
| Search apps | Keyword and region | クエリで検索タブを開く |
| Open charts | Chart, category, and region | フィルターでランキングを開く('iapp://rank` と同じ) |
| Add favorite | App ID and region | サイレントにお気に入りに追加 |

**例 Siri phrases (英語 UI):** *" iApp の検索アプリ"*、*"iApp でチャートを開く"*、*"iApp でお気に入り追加"*。 中国語(簡体字)、韓国語(簡体字)、中国語(簡体字)、中国語(簡体字)、韓国語(簡体字)、中国語(簡体字)、韓国語(簡体字)、中国語(簡体字)、韓国語(簡体字)、中国語(簡体字)、中国語(簡体字)、韓国語(簡体字)、中国語(簡体字)、中国語(簡体字)、韓国語(簡体字)、中国語(簡体字)、中国語(簡体字)

---

## Macキーボードショートカット

Mac 上では、**⌘1** を** にしてタブを切り替えます。 数値は、どのタブが表示されるかに基づいて**動的に割り当てられます。

| When visible | 典型的なショートカット |
|--------------|------------------|
| Rankings | ディレクトリ |
| Search | ディレクトリ |
| Subscriptions (if shown) | 次の番号 |
| Favorites (if tab enabled) | 次の番号 |
| Developer Favorites (if tab enabled) | 次の番号 |
| Settings | 最後の番号 |

⌘1 のランキング・ ⌘2 検索・ ⌘3 サブスクリプション・ ⌘4 お気に入り・ ⌘5 開発者のお気に入り・ ⌘6 設定

タブが隠されると、残りのタブが自動的に再番号されます。

---

## リンクの地域コード

ディープリンクとウィジェット生成された URL は、常に安定した **region コード** ( `iapp://` , `iappstore://` , `iapp://{host}` , `developer_favorites` , `developer.favorites` ,...) — ローカル表示名ではありません。 リージョンピッカーと検索は、より明確にラベルを表示することができますが、保存されたコードは同じままです。

**例**


```
iapp://app?id=6446581591&region=hk
iapp://rank?type=topFreeApplications&category=0&region=tw
```


---

## アプリ内検索(URLリンクではなく)

iApp内のこれらの作業は、** `iapp://` URL:

| Action | アクセス方法 |
|--------|-----|
| **Single App ID search** | 1つの数値ID(6〜12桁、コンマなし)を検索で入力 |
| **Batch App ID search** | 最大50個のコンマ区切りID |
| **Add Subscription** | アプリの行を長押し |
| **Save Developer** | ロングプレス → **Developer** サブメニュー、または詳細 **その他** メニュー |
| **Open by-ranking view** | コンテキストメニュー → 同じ開発者アプリや開発者のお気に入り |
| **Pause / resume subscription** | サブスクリプション行のロングプレス |
| **Reopen from browse history** | **設定 → データ → アプリの閲覧履歴** → エントリをタップ |

外部アプリからiAppを開く必要がある場合、**       **リンクまたは**Siri /ショートカット**を使用してください。

---

## ニュース

- Link codes work in any app language — UI言語を切り替えると変更しません。
- Widgets と**Live Activity** は、タップしたときに自動的にこれらのリンクを生成します。
- 有料のMac / iPadおよびgrosssingチャート用のウィジェットチャートデータがメインアプリとは若干異なる場合があります。
- **Add favorite** via Shortcuts does not open the app UI — お気に入りリストに直接書きます。
- **Content compare** mode in all-region info cannot export share images — リストまたはグリッド表示を最初に切り替えます。

[概要に戻る](...)・[FAQ](../faq)・[プライバシーポリシー](../privacy)

</section>
<section lang="ko" markdown="1">

iApp은 ** `iapp://` ** 및 ** `iappstore://` ** 단축키 링크를 지원합니다. **Shortcuts**, Safari bookmarks, 또는 **Home Screen widgets** 및 **Live Activity** 에 ** 앱 세부 페이지를 엽니다 **, ** 필터링 된 랭킹보기에 반환 **, ** 스위치 탭 **, 또는 **Jump to Second pages** (개발자 좋아하는, 역사, 순위 추적 및 더 많은).

> **주의:** Long-press **Home Screen Quick Actions**는 동일한 `iapp://` 링크 텍스트를 사용하지만 빠른 행동으로 파견되어 Safari / Shortcuts URL과 동일한 경로로 나타날 수 없습니다.

## 링크 형식


```
iapp://...
iappstore://...   (older alias, works the same)
```


호스트는 **case-insensitive**이며 ** kebab-case** ( `iapp://` 및 `iappstore://` → `iapp://{host}` )로 정상화됩니다. 레거시 별칭 : `developer_favorites` → 순위, `developer.favorites` → 구독, `developer-favorites` → 검토.

| What you want | 링크 유형 |
|---------------|-----------|
| Open an app detail page | `iapp://app?...` |
| Open Rankings with filters | `iapp://rank?...` |
| Switch tabs or open settings pages | `iapp://{host}` (아래 표 참조) |
| Tap an app in a widget | 자주 묻는 질문 |
| Tap the widget title / blank area | 일치하는 랭킹보기를 엽니다 |
| Tap a rank **Live Activity** | 일치하는 랭킹보기를 엽니다 |
| Tap a subscription **Live Activity** | 앱 세부 페이지를 엽니다 |

---

## 앱 상세 페이지 열기


```
iapp://app?id={APP_ID}&region={region}&country={cc}
```


| Parameter | Required | 이름 * |
|-----------|----------|-------------|
| `id` | **Yes** | 앱 스토어 ID |
| `region` | No | 지역 코드, 예를 들어 `cn`, `us`, `jp`(기본값: `us`) |
| `country` | No | `region`가 omitted라면 선택 영역 코드 |

**예금 **


```
iapp://app?id=6446581591&region=cn
```


에 의해 사용: **내 즐겨찾기 위젯** (앱을 제거), ** 구독 라이브 활동** (활동을 제거), **Shortcuts** / bookmarks.

---

## 필터로 순위 열기

**Rankings** 탭으로 전환하고 선택한 차트, 카테고리 및 지역을 적용합니다.


```
iapp://rank?type={chart}&category={category}&region={region}
```


| Parameter | 이름 * |
|-----------|-------------|
| `type` | 차트 코드 (아래 표 참조) |
| `category` | 범주 코드 - 주요 범주 또는 게임 하위 범주 |
| `region` | 지역 코드, 예를들면 `cn`, `us` |

인식된 값은 무시됩니다; 인식된 값은 기억됩니다.

### 차트 코드 ( `iapp://` ) — 12 차트

| Code | 팟캐스트 |
|------|-------|
| `topFreeApplications` | iPhone 상단 무료 |
| `topPaidApplications` | iPhone 상단 유료 |
| `topGrossingApplications` | 아이폰 탑 Grossing |
| `newApplications` | 새로운 앱 |
| `newFreeApplications` | 무료 새로운 |
| `newPaidApplications` | 새로운 유료 |
| `topFreeiPadApplications` | iPad 상단 무료 |
| `topPaidiPadApplications` | iPad 상단 유료 |
| `topGrossingiPadApplications` | iPad 상단 Grossing |
| `topFreeMacApplications` | 맥 탑 무료 |
| `topPaidMacApplications` | Mac 상단 유료 |
| `topGrossingMacApplications` | 맥 탑 Grossing |

### 범주 코드 ( `iapp://` )

| Code | (주) |
|------|----------|
| `0` | 모든 앱 |
| `6014` | 게임 (모든 게임) |
| `6005` | - 연혁 |
| `6007` | 회사연혁 |
| `6002` | (주) |
| `6008` | 사진 & 비디오 |
| `6017` | 교육과정 |
| `6015` | 재무정보 |
| … | 26 메인 카테고리 전체 |

게임 하위 카테고리:** `iapp://` – `iappstore://` , `iapp://{host}` – `developer_favorites` (18세). 예제: `developer.favorites` = 동작.

### 예시


```
iapp://rank?type=topFreeApplications&category=6014&region=cn
iapp://rank?type=topFreeMacApplications&category=0&region=us
```


### Older Chinese-style 링크 (지원되는 길)


```
iapp://rank?type=热门免费榜&category=游戏&region=中国
```


에 의해 사용: ** 락킹 위젯** (탭 제목 / 공백 영역), **랭크 라이브 활동** (활동을 제거), 및 ** 슬립**.

---

## Widget 깊은 링크

위젯은 별도의 URL 형식을 사용하지 않습니다 - 그들은 같은 생성 `iapp://` 및 `iappstore://` 링크 자동으로.

| Widget | Tap target | 공지사항 |
|--------|------------|-------|
| **Rankings · iApp** | An app row | `iapp://app?id=...&region=...` |
| **Rankings · iApp** | Title or blank area | `iapp://rank?type=...&category=...&region=...` |
| **My Favorites · iApp** | An app row | `iapp://app?id=...&region=...` |

Pinned favorites 처음으로 에 나의 마음에 드는 위젯. 위젯 테마와 언어를 따르십시오 **설정 → 위젯 ** 및 앱 언어 (모든 18 언어). 위젯 영역을 구성 할 때, HK / TW / MO는 목록과 통합 된 검색에 명확한 디스플레이 이름을 보여줍니다 (예 : "중국", "HK"); 저장된 지역 ** 코드 ** 링크에서 남아 있습니다 `iapp://` , `iappstore://` , `iapp://{host}` .

---

## 검색 내역 (URL 링크가 아닙니다)

**App Browse History**는 **Settings → Data → App Browse History**에서 관리됩니다. iApp 내부의 세부 페이지를 다시 열 수 있습니다. ** 사용할 수 없습니다 `iapp://` URL을 복사하거나 외부 공유 할 수 있습니다.

---

## 라이브 활동 깊은 링크

| Live Activity type | Tap behavior | 링크 생성 |
|--------------------|--------------|----------------|
| **Rankings** (tracking preset) | Opens filtered Rankings | `iapp://rank?...` |
| **Subscriptions** (per subscription) | Opens app detail | `iapp://app?id=...&region=...` |

**Settings → Advanced**에서 미리 설정할 수 있는 랭크 라이브 활동. **Settings → Advanced → Live Activity**(랭크 라이브 활동)에서 사용 가능한 구독 라이브 활동); 추가 또는 편집할 때 구독 당 구독. Price-drop 모니터는 Lock Screen의 현재 가격을 표시합니다.

---

## 탭 & 액션 링크 (질문 없음)

이 탭을 열고 in-app 동작을 트리거합니다. **Shortcuts**, Safari 및 **홈 화면 빠른 동작**에서 작동합니다.

### 기본 탭

| URL | 열리는 화면 |
|-----|--------|
| `iapp://search` | 검색 탭 + 초점 검색 필드 |
| `iapp://rank` | 순위 탭(필터 변경 없이 쿼리) |
| `iapp://favorites` | ** 즐겨 찾기 탭 ** ** 설정 → 앱 설정 **; 그렇지 않으면 ** 설정 → 앱 즐겨찾기 ** |
| `iapp://subscription` | 가시다면 구독 탭; 그렇지 않으면 **설정 → 구독** |
| `iapp://settings` | 설정 탭 |
| `iapp://feedback` | 피드백 이메일 |
| `iapp://review` | 앱 스토어 평가 (alias: `iapp://rate`) |

### 두 번째 페이지

opens**Settings** 탭을 먼저 열고, 대상 페이지를 밀어줍니다. 일치 탭이 존재하는 경우 (예: Developer Favorites), 대신 탭을 엽니 다.

| URL | 열리는 화면 |
|-----|--------|
| `iapp://developer-favorites` | 개발자 즐겨s 탭 또는 **Settings → 개발자 즐겨s** |
| `iapp://browse-history` | **설정 → 데이터 → 앱 검색 기록** |
| `iapp://favorite-groups` | **설정 → 데이터 → 즐겨찾기 그룹** |
| `iapp://rank-tracking` | ** 설정 → 고급 → 순위 추적** |
| `iapp://live-activity` | **설정 → 고급 → 실시간 활동** |
| `iapp://apple-services` | **설정 → 제3자 → Apple 서비스** |
| `iapp://region-switch` | **설정 → 제3자 → 앱 스토어 지역** |
| `iapp://usage-guide` | **설정 → 도움말 → 사용 설명서** |
| `iapp://widget-guide` | **설정 → 위젯 → 위젯 가이드 ** (iOS 17+ 만; URL은 Quick Actions Picker에 나열되지 않음) |

---

## 홈 화면 빠른 행동

앱 아이콘을 길게 누릅니다. **4** 부터 **15** 옵션에서 **설정 → 홈 화면 롱 프레스 → 단축키 사용자 지정**.

기본 선택: 검색, 순위, 즐겨찾기, 피드백.

각 옵션 사용 `iapp://` — 위의 URL. 빠른 행동은 아이콘 메뉴를 통해 파견됩니다. 외부 단축키 / Safari는 unified `iappstore://` 경로를 사용합니다.

| 링크 | 열리는 화면 |
|------|--------|
| `iapp://search` | 검색 탭 + 초점 |
| `iapp://rank` | 순위 탭 |
| `iapp://favorites` | 즐겨찾기 탭 또는 설정 → 앱 즐겨찾기 |
| `iapp://developer-favorites` | 개발자 즐겨찾기 탭 또는 설정 → Developer Favorites |
| `iapp://subscription` | 구독 탭 또는 설정 → 구독 |
| `iapp://browse-history` | 앱 검색 |
| `iapp://favorite-groups` | 즐겨찾기 그룹 설정 |
| `iapp://rank-tracking` | 순위 추적 |
| `iapp://live-activity` | Live Activity 설정 |
| `iapp://apple-services` | Apple 서비스 링크 |
| `iapp://region-switch` | App Store 지역 스위치 |
| `iapp://usage-guide` | 사용 설명서 |
| `iapp://settings` | 설정 탭 |
| `iapp://feedback` | 피드백 이메일 |
| `iapp://review` | 앱 평가 | `iapp://` 는 외부 URL로 지원되지만 ** Quick Actions Picker에서 사용할 수 없습니다.

---

## Siri 및 단축키 (iOS 16+)

**Shortcuts** 앱 또는 요청 **Siri**에서 내장 작업을 찾습니다. 모든 intent titles, 매개 변수 레이블 및 Siri 구문은 ** 모든 응용 언어에서 로컬화 ** - 그들은 당신이 변경할 때 업데이트 ** 설정 → 외관 → 언어 **.

| Action | What you can set | 제품 정보 |
|--------|------------------|--------|
| Search apps | Keyword and region | 쿼리로 검색 탭 열기 |
| Open charts | Chart, category, and region | 필터가있는 순위를 엽니다 (예 : `iapp://rank`) |
| Add favorite | App ID and region | 자주 묻는 질문 |

**Example Siri 구문 (English UI) : ** * "iApp에서 검색 응용 프로그램"*, * "iApp의 오픈 차트"*, * "iApp에서 좋아하는 추가"*. 한국어, 구문은 중국어로 나타났습니다. 모든 18 개 언어와 동일합니다.

---

## Mac 키보드 단축키

Mac에서, use **1⌘** via **⌘N** 탭을 전환합니다. 숫자는 할당된 **dynamically ** 어떤 탭을 기준으로:

| When visible | 일반 단축키 |
|--------------|------------------|
| Rankings | ⌘1의 |
| Search | ⌘2의 |
| Subscriptions (if shown) | 다음 번호 |
| Favorites (if tab enabled) | 다음 번호 |
| Developer Favorites (if tab enabled) | 다음 번호 |
| Settings | 계좌번호 |

모든 선택 탭의 예 : ⌘1 랭킹 · ⌘2 검색 · ⌘3 구독 · ⌘4 즐겨찾기 · ⌘5 개발자 즐겨s · ⌘6 설정.

탭이 숨겨져있을 때, 나머지 탭은 자동으로 다시 번호.

---

## 링크에서 지역 코드

딥 링크 및 위젯 생성 된 URL은 항상 안정 ** 등록 코드 ** ( `iapp://` , `iappstore://` , `iapp://{host}` , `developer_favorites` , `developer.favorites` , ...) - 현지화 된 디스플레이 이름. 지역 픽업 및 검색은 더 명확한 라벨을 표시 할 수 있지만 저장된 코드는 동일하게 유지됩니다.

**예시**


```
iapp://app?id=6446581591&region=hk
iapp://rank?type=topFreeApplications&category=0&region=tw
```


---

## 인앱 검색 (URL 링크 없음)

이 작업 내부 iApp 하지만 **not** `iapp://` URL:

| Action | 이름 * |
|--------|-----|
| **Single App ID search** | 숫자 ID를 입력 (6–12자리, comma 없음) 검색 |
| **Batch App ID search** | 최대 50개의 상품 ID |
| **Add Subscription** | 긴 압박 어떤 app 줄 |
| **Save Developer** | Long-press → **개발자 ** submenu, 또는 세부 **More** 메뉴 |
| **Open by-ranking view** | Context menu → 동일한 개발자 앱 또는 개발자 즐겨 찾기 |
| **Pause / resume subscription** | 구독 행에 긴 압박 |
| **Reopen from browse history** | **설정 → 데이터 → App Browse History** → 입력 탭 |

use ** `iapp://` ** 링크 또는 **Siri / Shortcuts** 앱 외부에서 iApp을 열 필요가있을 때.

---

## 제품 정보

- Link codes work in any app language — UI 언어를 전환할 때 변경하지 않습니다.
- Widgets and**Live Activity**이 링크를 자동으로 생성합니다.
- 일부 Mac / iPad 유료 및 grossing 차트에 대한 Widget 차트 데이터는 주요 앱에서 약간 다를 수 있습니다.
- **Add favorite** via Shortcuts does not open the app UI — 즐겨찾기 목록에 직접 쓸 수 있습니다.
- **Content compare** mode in all-region info cannot export share images — 목록 또는 그리드보기로 전환합니다.

[경찰](..) · [FAQ](../faq) · [Privacy](../privacy)

</section>
<section lang="ru" markdown="1">

iApp поддерживает ярлыки ** `iapp://` ** и ** `iappstore://` **. Используйте их в **Shortcuts**, закладках Safari или от ** виджетов Home Screen** и **Live Activity** до ** откройте страницу с подробным описанием приложения**, ** вернитесь к отфильтрованному просмотру рейтинга**, **переключите вкладки** или ** перейдите на второстепенные страницы** (любимые разработчики, история просмотра, отслеживание рангов и многое другое).

> **Примечание: ** Быстрые действия на домашнем экране ** используют тот же текст ссылки `iapp://` , но отправляются как быстрые действия — не анализируются по тому же пути, что и URL-адреса Safari / Shortcuts при открытии только из меню значков.

## Формат ссылки


```
iapp://...
iappstore://...   (older alias, works the same)
```


Хосты **case-insensitive** и нормализованы до **kebab-case** ( `iapp://` и `iappstore://` → `iapp://{host}` ). Наследственные псевдонимы: `developer_favorites` → ранг, `developer.favorites` → подписка, `developer-favorites` → обзор.

| What you want | Тип ссылки |
|---------------|-----------|
| Open an app detail page | "iapp://app?" |
| Open Rankings with filters | "iapp://rank?" |
| Switch tabs or open settings pages | "iapp://{host}" (см. таблицы ниже) |
| Tap an app in a widget | Откройте страницу детализации |
| Tap the widget title / blank area | Открывает соответствующий вид рейтинга |
| Tap a rank **Live Activity** | Открывает соответствующий вид рейтинга |
| Tap a subscription **Live Activity** | Откройте страницу детали приложения |

---

## Откройте страницу детали приложения


```
iapp://app?id={APP_ID}&region={region}&country={cc}
```


| Parameter | Required | Описание |
|-----------|----------|-------------|
| `id` | **Yes** | App Store ID |
| `region` | No | Код региона, например "cn", "us", "jp" (по умолчанию: "us") |
| `country` | No | Факультативный код региона, если "регион" опущен |

**Пример **


```
iapp://app?id=6446581591&region=cn
```


Используется: **My Favorites widget** (нажмите приложение), ** подписка Live Activity** (нажмите действие) и **Shortcuts** / закладки.

---

## Открытые рейтинги с фильтрами

Переключается на вкладку **Rankings** и применяет выбранный вами график, категорию и регион.


```
iapp://rank?type={chart}&category={category}&region={region}
```


| Parameter | Описание |
|-----------|-------------|
| `type` | Код диаграммы (см. таблицу ниже) |
| `category` | Категория кода — основная категория или подкатегория игры |
| `region` | Код региона, например "cn", "us" |

Непризнанные ценности игнорируются, признанные ценности запоминаются.

### Коды диаграмм ( `iapp://` ) — 12 диаграмм

| Code | Чарт |
|------|-------|
| `topFreeApplications` | iPhone Top Free бесплатно |
| `topPaidApplications` | iPhone платный |
| `topGrossingApplications` | iPhone Top Grossing |
| `newApplications` | Новые приложения |
| `newFreeApplications` | Новый Free |
| `newPaidApplications` | Новый платный |
| `topFreeiPadApplications` | iPad Top бесплатно |
| `topPaidiPadApplications` | iPad платный |
| `topGrossingiPadApplications` | iPad стал самым кассовым |
| `topFreeMacApplications` | Mac Top Free бесплатно |
| `topPaidMacApplications` | Mac Top Payed |
| `topGrossingMacApplications` | Mac Top Гроссинг |

### Коды категорий ( `iapp://` )

| Code | Категория |
|------|----------|
| `0` | Все приложения |
| `6014` | Игры (все игры) |
| `6005` | социальный |
| `6007` | Производительность |
| `6002` | коммунальные услуги |
| `6008` | Фото и видео |
| `6017` | Образование |
| `6015` | Финансы |
| … | Всего 26 основных категорий |

**Игровые подкатегории:** `iapp://` C1   , `iapp://{host}` C3    (18 жанров). Пример: `developer.favorites` = Действие.

### Примеры


```
iapp://rank?type=topFreeApplications&category=6014&region=cn
iapp://rank?type=topFreeMacApplications&category=0&region=us
```


### Старые ссылки в китайском стиле (по-прежнему поддерживаются)


```
iapp://rank?type=热门免费榜&category=游戏&region=中国
```


Используется: **Rankings widget** (заголовок заголовка / пустая область), **rank Live Activity** (заголовок действия) и **Shortcuts**.

---

## Виджеты Deep Links

Виджеты не используют отдельный формат URL — они автоматически генерируют одни и те же ссылки `iapp://` и `iappstore://` .

| Widget | Tap target | Открытие |
|--------|------------|-------|
| **Rankings · iApp** | An app row | «iapp://app?id=...&region=...» |
| **Rankings · iApp** | Title or blank area | "iapp://rank?type=...&category=...&region=..." |
| **My Favorites · iApp** | An app row | «iapp://app?id=...&region=...» |

Пиннированные фавориты появляются первыми в виджете My Favorites. Тема и язык виджета следуют ** Настройки → Виджеты ** и язык вашего приложения (любой из 18 языков). При настройке областей виджетов HK/TW/MO показывает более четкие имена отображения в списке и унифицированный поиск (например, «Китай», «HK»); сохраненные коды региона *** в ссылках остаются `iapp://` , `iappstore://` , `iapp://{host}` .

---

## История просмотра (не ссылка URL)

**App Browse History** управляется в **Settings → Data → App Browse History** Нажатие на запись вновь открывает страницу детализации внутри iApp — она ** не ** использует URL-адрес `iapp://` , который вы можете скопировать или поделиться внешне.

---

## Живая активность Глубокие ссылки

| Live Activity type | Tap behavior | Ссылка генерируется |
|--------------------|--------------|----------------|
| **Rankings** (tracking preset) | Opens filtered Rankings | "iapp://rank?" |
| **Subscriptions** (per subscription) | Opens app detail | «iapp://app?id=...&region=...» |

Включите ранжирование Live Activity за предустановленное отслеживание в **Настройки → Advanced**.Включить подписку Live Activity в **Настройки → Advanced → Live Activity** (отдельно от ранга Live Activity); затем за подписку при добавлении или редактировании. Мониторы ценового падения показывают базовую линию против текущей цены на экране блокировки.

---

## Ссылки Tab & Action (без запроса)

Они открывают вкладку или запускают действие в приложении. Работает с **Shortcuts**, Safari и **Home Screen Quick Actions**.

### Основные вкладки

| URL | Открывает |
|-----|--------|
| `iapp://search` | Поисковая вкладка + поле поиска фокуса |
| `iapp://rank` | Закладка рейтинга (без изменения фильтра при отсутствии запроса) |
| `iapp://favorites` | **Любимая вкладка**, если включена в **Настройки → Настройки приложений**; в противном случае **Настройки → Любимые приложения** |
| `iapp://subscription` | Закладка подписки, если она видна; в противном случае ** Настройки → Подписки** |
| `iapp://settings` | Настройка вкладки |
| `iapp://feedback` | Письмо с отзывом |
| `iapp://review` | Рейтинг App Store в приложении (за исключением: «iapp: / / rate») |

### Вторичные страницы

Сначала открывается вкладка **Настройки**, затем нажимает целевую страницу. Если соответствующая вкладка существует (например, «Фавориты разработчиков»), она открывает эту вкладку.

| URL | Открывает |
|-----|--------|
| `iapp://developer-favorites` | Разработчик Любимые вкладки или **Настройки → Любимые разработчики** |
| `iapp://browse-history` | **Настройки → Данные → История просмотра приложений ** |
| `iapp://favorite-groups` | **Настройки → Данные → Любимые группы** |
| `iapp://rank-tracking` | ** Настройки → Advanced → Отслеживание рангов** |
| `iapp://live-activity` | **Настройки → Продвинутая → Живая активность** |
| `iapp://apple-services` | **Настройки → Сторонние сервисы Apple** |
| `iapp://region-switch` | **Настройки → Сторонние → Регион App Store** |
| `iapp://usage-guide` | **Настройки → Помощь → Инструкции по использованию** |
| `iapp://widget-guide` | **Настройки → Виджеты → Руководство по виджетам** (только iOS 17+; URL работает, но не указан в разделе «Быстрые действия») |

---

## Домой Экран Быстрые действия

Дальше нажмите значок приложения. Настройка до **4** от ***15** опций в **Настройки → Домашний экран Длинный пресс → Настройка ярлыков **.

Выбор по умолчанию: поиск, ранг, фавориты, обратная связь.

Каждая опция использует `iapp://` — те же URL, что и выше. Быстрые действия отправляются через меню значков; внешние ярлыки / Safari используют унифицированный путь `iappstore://` .

| Ссылка | Открывает |
|------|--------|
| `iapp://search` | Поисковая вкладка + фокус |
| `iapp://rank` | Закладка рейтинга |
| `iapp://favorites` | Любимые вкладки или настройки → Любимые приложения |
| `iapp://developer-favorites` | Разработчик Любимые вкладки или настройки → Любимые разработчики |
| `iapp://subscription` | Subscriptions tab или Settings → Подписки |
| `iapp://browse-history` | App Browse История |
| `iapp://favorite-groups` | Любимые групповые настройки |
| `iapp://rank-tracking` | Отслеживание рангов |
| `iapp://live-activity` | Настройки Live Activity |
| `iapp://apple-services` | Сервисы Apple Services |
| `iapp://region-switch` | Регион App Store переключается |
| `iapp://usage-guide` | Инструкции по использованию |
| `iapp://settings` | Настройка вкладки |
| `iapp://feedback` | Письмо с отзывом |
| `iapp://review` | Рейтинг in-app | `iapp://` поддерживается как внешний URL-адрес, но ** не** доступен в Quick Actions picker.

---

## Siri & Shortcuts (iOS 16+)

Найдите встроенные действия в приложении **Shortcuts** или спросите **Siri**. Все заголовки намерений, ярлыки параметров и фразы Siri полностью локализованы на каждом языке приложений — они обновляются при изменении настроек → внешнего вида → языка **.

| Action | What you can set | Эффект |
|--------|------------------|--------|
| Search apps | Keyword and region | Открывает вкладку Поиск с запросом |
| Open charts | Chart, category, and region | Открывает рейтинги с помощью фильтров (так же, как «iapp: / /rank») |
| Add favorite | App ID and region | Добавить в избранное молча |

** Примеры фраз Siri (англ. UI): ** * «Поисковые приложения в iApp»*, * «Открытые диаграммы в iApp»*, * «Добавить любимое в iApp»*. В .中. фразы появляются на китайском языке; одинаково для всех 18 языков.

---

## Ярлыки клавиатуры Mac

На Mac используйте **.1** через **.N** для переключения вкладок. Числа присваиваются ** динамически** на основании которых видны вкладки:

| When visible | Типичный короткий путь |
|--------------|------------------|
| Rankings | 1 |
| Search | 2 |
| Subscriptions (if shown) | Следующий номер |
| Favorites (if tab enabled) | Следующий номер |
| Developer Favorites (if tab enabled) | Следующий номер |
| Settings | Последнее число |

Пример со всеми дополнительными вкладками: .1 Rankings · .2 Search · .3 Subscriptions · .4 Favorites · .5 Developer Favorites · .6 Settings.

Когда вкладка скрыта, оставшиеся вкладки автоматически перенумеруются.

---

## Коды регионов в ссылках

Глубокие ссылки и URL-адреса, генерируемые виджетами, всегда используют стабильные коды **региона ** ( `iapp://` , `iappstore://` , `iapp://{host}` , `developer_favorites` , `developer.favorites` , ...) — не локализованные имена дисплеев. Выборщики регионов и поиск могут показывать более четкие ярлыки, но сохраненные коды остаются прежними.

**Примеры**


```
iapp://app?id=6446581591&region=hk
iapp://rank?type=topFreeApplications&category=0&region=tw
```


---

## Поиск в приложении (не URL-ссылки)

Работает внутри iApp, но не является ** `iapp://` URL:

| Action | Как |
|--------|-----|
| **Single App ID search** | Введите один цифровой идентификатор (6-12 цифр, без запятой) в поиске |
| **Batch App ID search** | До 50 идентификаторов, разделенных запятыми |
| **Add Subscription** | Long-press любое приложение |
| **Save Developer** | Дальний пресс → **Developer** submenu, или деталь **Больше** меню |
| **Open by-ranking view** | Контекстное меню → приложения-разработчики или фавориты разработчиков |
| **Pause / resume subscription** | Long-press в строке подписки |
| **Reopen from browse history** | ** Настройки → Данные → История просмотра приложений ** → запись нажатия |

Используйте ** `iapp://` ** ссылки или **Siri / Shortcuts**, когда вам нужно открыть iApp из-за пределов приложения.

---

## Советы

- Link codes work in any app language — Они не меняются, когда вы меняете язык.
- Виджеты и Live Activity автоматически генерируют эти ссылки при нажатии.
- Данные диаграмм Виджета для некоторых платных и кассовых графиков Mac/iPad могут немного отличаться от основного приложения.
- **Add favorite** via Shortcuts does not open the app UI — Он пишет прямо в список ваших любимых.
- **Content compare** mode in all-region info cannot export share images — Сначала переключитесь на список или вид сетки.

[Назад к обзору] (..) · [FAQ] (../faq) · [Privacy] (../privacy)

</section>
<section lang="th" markdown="1">

iApp รองรับ... `iapp://` BAR ~ และ*  BAR ลิงก์ลัด ใช้มันใน~~~~, คั่นหน้าซาฟารี, หรือจากวิดเจ็ตของจอต่าง ๆ ~ และ~ เปิดกิจกรรม ~ เพื่อเปิดหน้ารายการแอปพลิเคชัน~ ~ ย้อนกลับไปดูวิวที่กรองแล้ว~

> ~ ข้อควรทราบ: ~ * การกระทําด่วนด่วนของจอภาพแบบยาว * ~ ใช้  c0  ลิงก์เดียวกัน แต่ถูกส่งไปเป็นการกระทําอย่างรวดเร็ว — ไม่ได้วิเคราะห์โดยใช้พาธเดียวกันกับที่อยู่ URL ซาฟารี / ปุ่มพิมพ์ลัด เมื่อเปิดใช้จากเมนูไอคอนเท่านั้น

## รูปแบบลิงก์


```
iapp://...
iappstore://...   (older alias, works the same)
```


โฮสต์มี ** secontinuous~ และปรับเป็น ~kebab- case~ ( c0    BAR และ `iappstore://` s BAR `iapp://{host}` ). นามแฝง: `developer_favorites` BAR การจัดอันดับ, `developer.favorites` BAR มิวสิก, `developer-favorites` BAR รีวิว

| What you want | ชนิดที่อยู่เชื่อมโยง |
|---------------|-----------|
| Open an app detail page | 'อุบสาห์?' |
| Open Rankings with filters | 'ร้องตะโกน '...' |
| Switch tabs or open settings pages | (ดูตารางด้านล่างนี้) |
| Tap an app in a widget | เปิดหน้ารายละเอียด |
| Tap the widget title / blank area | เปิดมุมมองที่เข้าคู่กัน |
| Tap a rank **Live Activity** | เปิดมุมมองที่เข้าคู่กัน |
| Tap a subscription **Live Activity** | เปิดหน้ารายละเอียดของโปรแกรม |

---

## เปิดหน้ารายละเอียดของโปรแกรม


```
iapp://app?id={APP_ID}&region={region}&country={cc}
```


| Parameter | Required | คําอธิบาย |
|-----------|----------|-------------|
| `id` | **Yes** | หมายเลขร้าน App |
| `region` | No | รหัสเขต, e.g. 'cn', us', ojp' (ค่าปริยาย: us) |
| `country` | No | รหัสพื้นที่เลือก หากยกเลิก 'region' |

~Example~


```
iapp://app?id=6446581591&region=cn
```


ถูกใช้โดย: ~ วิดเจ็ตโปรดของฉัน ~ (จับ App) ~ รองรับการถ่ายทอดสด ~ (กิจกรรมต่าง ๆ) และ~ / ที่คั่นหน้า

---

## เปิดการกระดอนด้วยตัวกรอง

สลับไปยังแท็บ ~Runkings ~ และใช้แผนภูมิ, หมวดหมู่, และพื้นที่ของคุณ


```
iapp://rank?type={chart}&category={category}&region={region}
```


| Parameter | คําอธิบาย |
|-----------|-------------|
| `type` | โค้ดของแผนภูมิ (ดูตารางด้านล่างนี้) |
| `category` | รหัส ประจํา กลุ่ม หรือ เกม หลัก |
| `region` | รหัสเขต, e.g. 'cn', us' |

ค่าที่ไม่สามารถจัดการได้จะถูกละทิ้ง; ค่าที่ยอมรับได้จะถูกจดจํา

### `iapp://` ) — 12 แผนภูมิ

| Code | แผนภูมิ |
|------|-------|
| `topFreeApplications` | ไม่ใช้ไอโฟน |
| `topPaidApplications` | ค่าใช้จ่ายสูงสุดจากไอโฟน |
| `topGrossingApplications` | การพ่นสีบนไอโฟน |
| `newApplications` | แอปใหม่ |
| `newFreeApplications` | ว่างใหม่ |
| `newPaidApplications` | จ่ายใหม่ |
| `topFreeiPadApplications` | ไม่ใช้ไอแพด |
| `topPaidiPadApplications` | ไอแพดที่จ่ายสูงที่สุด |
| `topGrossingiPadApplications` | ไอแพด ท็อป สโลป |
| `topFreeMacApplications` | ว่าง Mac Top |
| `topPaidMacApplications` | เงินจ่าย Mac Top |
| `topGrossingMacApplications` | Mac Top Srunting |

### รหัสหมวดหมู่ ( `iapp://` )

| Code | ประเภท |
|------|----------|
| `0` | แอพเพล็ตทั้งหมด |
| `6014` | เกม (ทุกเกม) |
| `6005` | สังคม |
| `6007` | ความจุ |
| `6002` | ความจุ |
| `6008` | ภาพถ่ายและวิดีโอ |
| `6017` | การศึกษา |
| `6015` | การเงิน |
| … | 26 ประเภทหลักทั้งหมด |

~สัญญาย่อย: ~ `iapp://` BAR BAR `iappstore://` BAR ,  BAR `iapp://{host}` BAR `developer_favorites` BAR 18 genres. ตัวอย่าง: `developer.favorites` =การกระทํา

### ตัวอย่าง


```
iapp://rank?type=topFreeApplications&category=6014&region=cn
iapp://rank?type=topFreeMacApplications&category=0&region=us
```


### ส่วนเชื่อมโยงแบบจีนเก่า (ยังคงรองรับ)


```
iapp://rank?type=热门免费榜&category=游戏&region=中国
```


ถูกใช้โดย: ** วิดเจ็ตต่าง ๆ * (ชื่อเรื่อง / พื้นที่ว่าง) ~ การเคลื่อนไหวของสิ่งมีชีวิต ~ (ปฏิบัติการ) และ~

---

## ส่วนเชื่อมโยงลึกของวิดเจ็ต

วิดเจ็ตไม่ได้ใช้รูปแบบที่อยู่ URL ที่แยกต่างหาก — มันสร้าง  c0       BAR ลิงก์เดียวกันโดยอัตโนมัติ

| Widget | Tap target | เปิด |
|--------|------------|-------|
| **Rankings · iApp** | An app row | 'iappippp?id=....&region=...' |
| **Rankings · iApp** | Title or blank area | ~ippsgrangek? type=.... httpceptegory=... |
| **My Favorites · iApp** | An app row | 'iappippp?id=....&region=...' |

ของโปรด Pined ปรากฎครั้งแรกในวิดเจ็ต My Loves ชุดตกแต่งวิดเจ็ตและภาษาต่าง ๆ ตามหลังจาก # ตั้งค่าวิดเจ็ตและภาษาโปรแกรมของคุณ (ทั้ง 18 ภาษา) เมื่อทําการปรับแต่งขอบเขตของวิดเจ็ต HK / TW / MO จะแสดงชื่อที่แสดงในรายการให้ชัดเจนขึ้น และรวมการค้นหา (เช่น "จีน", "HK"); เก็บขอบเขต *.

---

## เรียกดูประวัติ (ไม่ใช่ที่อยู่เชื่อมโยงแบบ URL)

** ประวัติการเรียกดูของ App ~ มีการจัดการใน~ การเคาะรายการ เปิดอีกครั้งในหน้ารายละเอียดภายใน iApp ซึ่งไม่ * ใช้  c0  ที่อยู่ URL คุณสามารถคัดลอกหรือร่วมกันภายนอกได้

---

## กิจกรรม ที่ ไม่ มี ใด เหมือน

| Live Activity type | Tap behavior | เชื่อมโยงที่สร้างมา |
|--------------------|--------------|----------------|
| **Rankings** (tracking preset) | Opens filtered Rankings | 'ร้องตะโกน '...' |
| **Subscriptions** (per subscription) | Opens app detail | 'iappippp?id=....&region=...' |

เปิดการใช้งานระดับการถ่ายทอดสดต่อรายการชุดที่ตั้งไว้ใน ~settings ขั้นสูง~ ~. เปิดใช้งานกิจกรรมการบอกรับข้อมูลใน~. ตั้งค่าการถ่ายทอดสดขั้นสูง ○ feface Profile * (แยกจากกิจกรรมการถ่ายทอดสดตามอันดับ; จากนั้นต่อรายการย่อยเมื่อเพิ่มหรือแก้ไขข้อมูล จอภาพ Price-drop แสดงราคาพื้นฐาน vs ปัจจุบันบนหน้าจอล็อค

---

## แท็บที่อยู่เชื่อมโยงการกระทํา (ไม่ต้องถาม)

เหล่านี้จะเปิดแท็บหรือเรียกการกระทําในการใช้งาน ทํางานจาก... ........

### แท็บหลัก

| URL | เปิด |
|-----|--------|
| `iapp://search` | ค้นหาในแท็บ + การค้นหาแบบโฟกัส |
| `iapp://rank` | เพิ่มระยะเวลา... |
| `iapp://favorites` | <i> <i> เปิด <i> หากเปิดใช้งาน </i> ตั้งค่าแอปพลิเคชัน ~; ไม่อย่างนั้น~ |
| `iapp://subscription` | แท็บสําหรับบอกรับถ้าเห็นได้ ไม่เช่นนั้นก็จะใช้ตัวเลือก EXAs * |
| `iapp://settings` | แท็บการตั้งค่า |
| `iapp://feedback` | อีเมลข้อเสนอแนะ |
| `iapp://review` | เรตติ้งของ In-app buff (เลีย: 'iapplirate') |

### หน้าที่สอง

เปิด... ตั้งค่า 'แท็บ' ก่อน จากนั้นกดหน้าเป้าหมาย หากมีแท็บที่เข้าคู่กัน (เช่น ผู้พัฒนาโปรด), เปิดแท็บดังกล่าวแทน

| URL | เปิด |
|-----|--------|
| `iapp://developer-favorites` | ผู้พัฒนาจะเปิดใช้งานแท็บของรายการโปรดของแท็บ หรือ # การตั้งค่าโปรแกรมผู้พัฒนา # |
| `iapp://browse-history` | ~ |
| `iapp://favorite-groups` | ~ตั้งค่าข้อมูล~ |
| `iapp://rank-tracking` | ~รีเซตส์ → ขั้นสูง → Ranking~ |
| `iapp://live-activity` | ~รีเซตส์ เสริมการถ่ายทอดสด~ |
| `iapp://apple-services` | ~รีเซตส์ → party apple Service~ |
| `iapp://region-switch` | ~รีเซ็ตติ้งส์ → party pp stage~ |
| `iapp://usage-guide` | ~การตั้งโปรแกรมช่วยในการสอน~ |
| `iapp://widget-guide` | ~ ตั้งวิดเจ็ต ○ วิดเจ็ต '~ (เช่น IOS 17+ เท่านั้น; ที่อยู่ URL ทํางานได้แต่ไม่ได้แสดงอยู่ในการเลือกการกระทําด่วน) |

---

## การกระทําด่วนของจอส่วนตัว

กดยาวไอคอนแอพ กําหนดให้ใช้ <i> จาก </~~~~ ~ ตัวเลือกใน~

การเลือกปริยาย: สืบค้น, ตําแหน่ง, รายการโปรด, คําติชม

แต่ละตัวเลือกใช้ `iapp://` /  — ที่อยู่ URL เดียวกันกับด้านบน การกระทําด่วนถูกส่งผ่านทางเมนูไอคอน; ปุ่มพิมพ์ลัดภายนอก / ซาฟารีใช้การรวม  c1  พาธ

| ลิงก์ | เปิด |
|------|--------|
| `iapp://search` | ค้นหาในแท็บ + โฟกัส |
| `iapp://rank` | แท็บการกระดอน |
| `iapp://favorites` | แท็บ หรือ ตั้งค่าต่าง ๆ ของรายการโปรด |
| `iapp://developer-favorites` | ผู้พัฒนาโปรดแท็บหรือการตั้งค่า ○ ผู้พัฒนาโปรด |
| `iapp://subscription` | แท็บ หรือ ตั้งค่าต่าง ๆ |
| `iapp://browse-history` | ประวัติการเรียกดูของ App |
| `iapp://favorite-groups` | ตั้งค่ากลุ่มที่ควรใช้ |
| `iapp://rank-tracking` | แทร็กเกอร์ของ Runk |
| `iapp://live-activity` | ตั้งค่ากิจกรรมต่าง ๆ |
| `iapp://apple-services` | เชื่อมโยงบริการของแอปเปิล |
| `iapp://region-switch` | สลับส่วนขอบเขตของ App |
| `iapp://usage-guide` | วิธี สอน |
| `iapp://settings` | แท็บการตั้งค่า |
| `iapp://feedback` | อีเมลข้อเสนอแนะ |
| `iapp://review` | เรตติ้งในโปรแกรม | `iapp://` BAR ได้รับการสนับสนุนให้เป็นที่อยู่ URL ภายนอก แต่* ไม่สามารถใช้ได้ในเครื่องมือเลือกการกระทําด่วน

---

## Siri & ปุ่มพิมพ์ลัด (inOS 16+)

ค้นหาการกระทําที่สร้างขึ้นในโปรแกรมนี้ ทุกชื่อเรื่องจุดประสงค์, พารามิเตอร์, และวลีสีสิริ ถูกใช้ในท้องถิ่นอย่างเต็มรูปแบบ ในทุกภาษาแอพ

| Action | What you can set | ลูกเล่น |
|--------|------------------|--------|
| Search apps | Keyword and region | เปิดแท็บการค้นหาด้วยการค้นหา |
| Open charts | Chart, category, and region | Opens Runkings ด้วยตัวกรอง (เช่น 'iappening') |
| Add favorite | App ID and region | เพิ่มไปยังรายการโปรดแบบเงียบ ๆ |

~ Example Sirpi sites (อังกฤษ:): ~"ค้นหาแอพใน iApp"*,"เปิดชาร์ตใน iApp"*, *"Addd ชื่นชอบใน iApp"*. ○ วลี ต่าง ๆ ปรากฏ ใน ภาษา จีน; เช่น เดียว กัน สําหรับ ทั้ง 18 ภาษา.

---

## ปุ่มพิมพ์ลัด Mac

On Mac, wratch ~1 ~ ผ่าน~~~~เพื่อเปลี่ยนแท็บ ตัวเลขถูกมอบหมายให้กระทํา ** โดยปกติ * โดยอิงจากแท็บที่มองเห็นได้:

| When visible | ปุ่มพิมพ์ลัดทั่วไป |
|--------------|------------------|
| Rankings | ⌘1 |
| Search | ⌘2 |
| Subscriptions (if shown) | หมายเลขถัดไป |
| Favorites (if tab enabled) | หมายเลขถัดไป |
| Developer Favorites (if tab enabled) | หมายเลขถัดไป |
| Settings | หมายเลขสุดท้าย |

ตัวอย่างกับแท็บที่เลือกใช้ทั้งหมดบน: ⌘1 Runkings ecember ⌘2. สืบค้นเมื่อ 27-3  Subscription4s effects eldermans ·5 กลุ่มผู้พัฒนาที่ชื่นชอบ ⌘6 ตั้งค่า

เมื่อมีการซ่อนแท็บ ให้ทําการเพิ่มหมายเลขแท็บที่เหลือโดยอัตโนมัติ

---

## รหัสเขตอยู่ในลิงก์

ลิงก์ลึกและที่อยู่ URL ที่สร้างจากวิดเจ็ต จะใช้รหัสที่เสถียรเสมอ ** ( `iapp://` BAR   BAR `iappstore://` BAR `iapp://{host}` BAR           BAR               ) —/N BAR ชื่อที่แสดงในท้องถิ่น เครื่องขุดเจาะและการค้นหา อาจแสดงป้ายชัดขึ้น แต่รหัสที่เก็บไว้ยังคงเหมือนเดิม

**ตัวอย่าง**


```
iapp://app?id=6446581591&region=hk
iapp://rank?type=topFreeApplications&category=0&region=tw
```


---

## ค้นหาภายใน (ไม่ใช่ที่อยู่เชื่อมโยง)

มันทํางานภายใน iApp แต่ไม่ได้ -- ไม่ BAR `iapp://` BAR  ที่อยู่ URL:

| Action | ยังไง |
|--------|-----|
| **Single App ID search** | ใส่หมายเลขตัวเลขหนึ่ง (6-112 ตัวเลข, ไม่มีเครื่องหมายจุลภาค) ในการค้นหา |
| **Batch App ID search** | หมายเลขผู้ใช้ที่แยกได้ถึง 50 ลูกน้ํา |
| **Add Subscription** | แสดงแถวของโปรแกรมแบบยาว |
| **Save Developer** | Long-press →~Developer ~ ซับเมนูหรือรายละเอียด~ ~เมนูอื่น~ |
| **Open by-ranking view** | เมนูของคอนเท็กซ์: |
| **Pause / resume subscription** | กดยาวบนคอลัมน์ |
| **Reopen from browse history** | ~รีเซ็ตติ้งข้อมูล → App Ab Review History~ ~ → การเข้าสัมผัส |

ใช้} `iapp://` BAR ลิงก์หรือ~ เซรี / ปุ่มพิมพ์ลัด ~ เมื่อคุณต้องการเปิด iApp จากข้างนอกโปรแกรม

---

## ข้อ แนะ

- Link codes work in any app language — เขาไม่เปลี่ยนเมื่อคุณสลับภาษายูไอ
- วิดเจ็ตและ* กิจกรรม Live ~ สร้างลิงก์เหล่านี้โดยอัตโนมัติเมื่อคุณเคาะ
- ข้อมูลแผนภูมิวิดเจ็ตสําหรับบาง Mac/iPad ที่จ่ายและ arching ตารางอาจจะแตกต่างกันเล็กน้อยจากแอพหลัก
- **Add favorite** via Shortcuts does not open the app UI — มันเขียนถึงรายการโปรดของคุณโดยตรง
- **Content compare** mode in all-region info cannot export share images — เปลี่ยนเป็นรายการหรือมุมมองตารางก่อน

[Tack to Broups](. ) สืบค้นเมื่อ 22 พฤษภาคม พ.ศ.

</section>
<section lang="de" markdown="1">

iApp unterstützt ** `iapp://` ** und ** `iappstore://` ** Shortcut Links. Verwenden Sie sie in **Shortcuts**, Safari-Lesezeichen oder von **Home Screen Widgets** und **Live Activity**, um ** eine App-Detailseite** zu öffnen, **zurück zu einer gefilterten Rankings-Ansicht**, **Tabs** zu wechseln oder **zu sekundären Seiten** zu springen (Entwicklerfavoriten, Browserverlauf, Rangverfolgung und mehr).

> **Hinweis:** Long-Presse **Home Screen Quick Actions** verwenden den gleichen `iapp://` -Linktext, werden aber als Quick Actions gesendet – nicht durch den gleichen Pfad wie Safari / Shortcuts URLs analysiert, wenn sie nur aus dem Symbolmenü geöffnet werden.

## Linkformat


```
iapp://...
iappstore://...   (older alias, works the same)
```


Hosts sind **case-insensitive ** und normalisiert zu **kebab-case ** ( `iapp://` und `iappstore://` → `iapp://{host}` ). Legacy Aliase: `developer_favorites` → rank, `developer.favorites` → subscription, `developer-favorites` → review.

| What you want | Art der Verbindung |
|---------------|-----------|
| Open an app detail page | „iapp://app? |
| Open Rankings with filters | „iapp://rank? |
| Switch tabs or open settings pages | `iapp://{host}` (siehe Tabellen unten) |
| Tap an app in a widget | Öffnet die Detailseite |
| Tap the widget title / blank area | Öffnet die passende Rankings-Ansicht |
| Tap a rank **Live Activity** | Öffnet die passende Rankings-Ansicht |
| Tap a subscription **Live Activity** | Öffnet die App-Detailseite |

---

## Öffnen Sie eine App-Detailseite


```
iapp://app?id={APP_ID}&region={region}&country={cc}
```


| Parameter | Required | Beschreibung |
|-----------|----------|-------------|
| `id` | **Yes** | App Store ID |
| `region` | No | Regionscode, z. B. `cn`, `us`, `jp` (Standard: `us`) |
| `country` | No | Fakultativer Regionencode, wenn „Region weggelassen wird |

**Beispiel**


```
iapp://app?id=6446581591&region=cn
```


Verwendet von: **Mein Favoriten-Widget** (tippen Sie auf eine App), **Abonnement Live Activity** (tippen Sie auf die Aktivität) und **Shortcuts** / Lesezeichen.

---

## Offene Rankings mit Filtern

Wechselt zur Registerkarte **Rankings** und wendet das gewählte Diagramm, die Kategorie und die Region an.


```
iapp://rank?type={chart}&category={category}&region={region}
```


| Parameter | Beschreibung |
|-----------|-------------|
| `type` | Kartencode (siehe Tabelle unten) |
| `category` | Kategoriecode — Hauptkategorie oder Spielunterkategorie |
| `region` | Regionscode, z.B. `cn`, `us` |

Unerkannte Werte werden ignoriert; anerkannte Werte werden erinnert.

### Kartencodes ( `iapp://` ) — 12 Karten

| Code | Karte |
|------|-------|
| `topFreeApplications` | iPhone Top Free |
| `topPaidApplications` | iPhone Top bezahlt |
| `topGrossingApplications` | iPhone Top Grossing |
| `newApplications` | Neue Apps |
| `newFreeApplications` | Neu kostenlos |
| `newPaidApplications` | Neu bezahlt |
| `topFreeiPadApplications` | iPad Top Free |
| `topPaidiPadApplications` | iPad Top bezahlt |
| `topGrossingiPadApplications` | iPad Top Grossing |
| `topFreeMacApplications` | Mac Top Free |
| `topPaidMacApplications` | Mac Top bezahlt |
| `topGrossingMacApplications` | Mac Top-Brutto |

### Kategoriecodes ( `iapp://` )

| Code | Kategorie |
|------|----------|
| `0` | Alle Apps |
| `6014` | Spiele (alle Spiele) |
| `6005` | sozial |
| `6007` | Produktivität |
| `6002` | Versorgungsunternehmen |
| `6008` | Foto & Video |
| `6017` | Bildung |
| `6015` | Finanzen |
| … | 26 Hauptkategorien insgesamt |

**Spielunterkategorien: `iapp://` – `iappstore://` , `iapp://{host}` – `developer_favorites` (18 Genres). Beispiel: `developer.favorites` = Aktion.

### Beispiele


```
iapp://rank?type=topFreeApplications&category=6014&region=cn
iapp://rank?type=topFreeMacApplications&category=0&region=us
```


### Ältere Links im chinesischen Stil (immer noch unterstützt)


```
iapp://rank?type=热门免费榜&category=游戏&region=中国
```


Verwendet von: **Rankings-Widget** (Titel / leerer Bereich), **Rank Live Activity** (Tippen Sie die Aktivität) und **Shortcuts**.

---

## Widget Deep Links

Widgets verwenden kein separates URL-Format – sie erzeugen automatisch die gleichen `iapp://` und `iappstore://` -Links.

| Widget | Tap target | Offen |
|--------|------------|-------|
| **Rankings · iApp** | An app row | „iapp://app?id=...&region=... |
| **Rankings · iApp** | Title or blank area | `iapp://rank?type=...&category=...&region=...` |
| **My Favorites · iApp** | An app row | „iapp://app?id=...&region=... |

Angeheftete Favoriten erscheinen zuerst im Widget Meine Favoriten. Widget-Thema und -Sprache folgen **Einstellungen → Widgets** und Ihrer App-Sprache (alle 18 Sprachen). Beim Konfigurieren von Widget-Regionen zeigt HK / TW / MO klarere Anzeigenamen in der Liste und vereinheitlichte Suche (z.B. „China“, „HK“); gespeicherte Region **codes** in Links bleiben `iapp://` , `iappstore://` , `iapp://{host}` .

---

## Browserverlauf (kein URL-Link)

**App Browse History** wird unter **Einstellungen → Daten → App Browse History** verwaltet. Wenn Sie auf einen Eintrag tippen, wird die Detailseite in der iApp erneut geöffnet - sie verwendet **nicht ** eine `iapp://` URL, die Sie extern kopieren oder teilen können.

---

## Live Activity Deep Links

| Live Activity type | Tap behavior | Geschaffene Verbindung |
|--------------------|--------------|----------------|
| **Rankings** (tracking preset) | Opens filtered Rankings | „iapp://rank? |
| **Subscriptions** (per subscription) | Opens app detail | „iapp://app?id=...&region=... |

Aktivieren Sie die Live-Aktivität des Rangs pro Tracking-Voreinstellung in **Einstellungen → Erweitert**. Aktivieren Sie die Live-Aktivität des Abonnements in **Einstellungen → Erweitert → Live-Aktivität** (getrennt vom Rang Live-Aktivität); dann pro Abonnement beim Hinzufügen oder Bearbeiten. Preis-Drop-Monitore zeigen Baseline vs aktuellen Preis auf dem Sperrbildschirm.

---

## Tab & Action Links (keine Abfrage)

Diese öffnen einen Tab oder lösen eine In-App-Aktion aus. Funktioniert von **Shortcuts **, Safari und **Home Screen Quick Actions **.

### Hauptregisterkarten

| URL | Öffnet |
|-----|--------|
| `iapp://search` | Suchtab + Fokus Suchfeld |
| `iapp://rank` | Rankings Tab (keine Filteränderung, wenn keine Abfrage) |
| `iapp://favorites` | **Favoriten-Tab** wenn aktiviert in **Einstellungen → App-Einstellungen**; ansonsten **Einstellungen → App-Favoriten** |
| `iapp://subscription` | Registerkarte Abonnements, falls sichtbar; ansonsten **Einstellungen → Abonnements** |
| `iapp://settings` | Tab Einstellungen |
| `iapp://feedback` | Feedback-E-Mail |
| `iapp://review` | In-App App Store Rating (alias `iapp://rate`) |

### Sekundärseiten

Öffnet zuerst die Registerkarte **Einstellungen ** und drückt dann die Zielseite. Wenn eine passende Registerkarte vorhanden ist (z. B. Entwicklerfavoriten), öffnet diese Registerkarte stattdessen.

| URL | Öffnet |
|-----|--------|
| `iapp://developer-favorites` | Tab Entwicklerfavoriten oder **Einstellungen → Entwicklerfavoriten** |
| `iapp://browse-history` | **Einstellungen → Daten → App Browse History** |
| `iapp://favorite-groups` | **Einstellungen → Daten → Lieblingsgruppen** |
| `iapp://rank-tracking` | **Einstellungen → Erweitert → Rank Tracking** |
| `iapp://live-activity` | **Einstellungen → Fortgeschrittene → Live-Aktivität** |
| `iapp://apple-services` | **Einstellungen → Drittanbieter → Apple Services** |
| `iapp://region-switch` | **Einstellungen → Drittanbieter → App Store Region** |
| `iapp://usage-guide` | **Einstellungen → Hilfe → Gebrauchsanweisungen** |
| `iapp://widget-guide` | **Einstellungen → Widgets → Widget Guide** (nur iOS 17+; URL funktioniert, aber nicht im Quick Actions Picker aufgeführt) |

---

## Home Bildschirm Schnelle Aktionen

Langes Drücken des App-Icons. Passen Sie bis zu **4** von **15** Optionen in **Settings → Home Screen Long Press → Customize Shortcuts** an.

Standardauswahl: Suche, Rang, Favoriten, Feedback.

Jede Option verwendet `iapp://` dieselben URLs wie oben. Schnelle Aktionen werden über das Icon-Menü gesendet; externe Shortcuts / Safari verwenden den einheitlichen `iappstore://` Pfad.

| Link | Öffnet |
|------|--------|
| `iapp://search` | Such-Tab + Fokus |
| `iapp://rank` | Tab Rankings |
| `iapp://favorites` | Favoriten Tab oder Einstellungen → App Favoriten |
| `iapp://developer-favorites` | Tab Developer Favorites oder Einstellungen → Developer Favorites |
| `iapp://subscription` | Tab Abonnements oder Einstellungen → Abonnements |
| `iapp://browse-history` | App Browse History |
| `iapp://favorite-groups` | Lieblingsgruppeneinstellungen |
| `iapp://rank-tracking` | Rangverfolgung |
| `iapp://live-activity` | Einstellungen für Live-Aktivitäten |
| `iapp://apple-services` | Apple Services Links |
| `iapp://region-switch` | App Store Region Switch |
| `iapp://usage-guide` | Gebrauchsanweisung |
| `iapp://settings` | Tab Einstellungen |
| `iapp://feedback` | Feedback-E-Mail |
| `iapp://review` | In-App-Rating | `iapp://` wird als externe URL unterstützt, aber **not** ist im Quick Actions Picker verfügbar.

---

## Siri & Shortcuts (iOS 16+)

Finden Sie integrierte Aktionen in der **Shortcuts** App oder fragen Sie **Siri**. Alle Intent-Titel, Parameter-Beschriftungen und Siri-Phrasen sind in jeder App-Sprache **voll lokalisiert ** - sie werden aktualisiert, wenn Sie ** Einstellungen → Aussehen → Sprache ** ändern.

| Action | What you can set | Wirkung |
|--------|------------------|--------|
| Search apps | Keyword and region | Öffnet Such-Tab mit Abfrage |
| Open charts | Chart, category, and region | Öffnet Rankings mit Filtern (gleich wie `iapp://rank`) |
| Add favorite | App ID and region | Addiert zu Favoriten schweigend |

**Beispiel Siri Phrasen (englische Benutzeroberfläche): *"Suchen Sie Apps in iApp"*, *"Öffnen Sie Diagramme in iApp"*, *"Favorit in iApp hinzufügen"*. In 简体中� erscheinen Phrasen auf Chinesisch; dasselbe für alle 18 Sprachen.

---

## Mac Keyboard Shortcuts

Verwenden Sie auf dem Mac **⌘1** bis **⌘N**, um die Registerkarten zu wechseln. Zahlen werden **dynamisch ** zugewiesen, basierend darauf, welche Tabs sichtbar sind:

| When visible | Typische Abkürzung |
|--------------|------------------|
| Rankings | ⌘1 |
| Search | ⌘2 |
| Subscriptions (if shown) | Nächste Nummer |
| Favorites (if tab enabled) | Nächste Nummer |
| Developer Favorites (if tab enabled) | Nächste Nummer |
| Settings | Letzte Nummer |

Beispiel mit allen optionalen Registerkarten auf: ⌘1 Rankings · ⌘2 Suche · ⌘3 Abonnements · ⌘4 Favoriten · ⌘5 Entwicklerfavoriten · ⌘6 Einstellungen.

Wenn ein Tab ausgeblendet wird, werden die verbleibenden Tabs automatisch neu nummeriert.

---

## Regionscodes in Links

Deep Links und widgetgenerierte URLs verwenden immer stabile **Regionalcodes** ( `iapp://` , `iappstore://` , `iapp://{host}` , `developer_favorites` , `developer.favorites` , ...) — keine lokalisierten Anzeigenamen. Region Picker und Suche können klarere Etiketten zeigen, aber gespeicherte Codes bleiben gleich.

**Beispiele**


```
iapp://app?id=6446581591&region=hk
iapp://rank?type=topFreeApplications&category=0&region=tw
```


---

## In-App-Suche (nicht URL-Links)

Diese funktionieren in iApp, sind aber **nicht `iapp://` URLs:

| Action | Wie |
|--------|-----|
| **Single App ID search** | Geben Sie eine numerische ID (6-12 Ziffern, kein Komma) in der Suche ein |
| **Batch App ID search** | Bis zu 50 Komma-getrennte IDs |
| **Add Subscription** | Lange drücken Sie jede App-Reihe |
| **Save Developer** | Long-Press → **Developer** Untermenü oder Detail **Mehr ** Menü |
| **Open by-ranking view** | Kontextmenü → Entwickler-Apps oder Entwicklerfavoriten |
| **Pause / resume subscription** | Long-Press auf einer Subscription-Reihe |
| **Reopen from browse history** | **Einstellungen → Daten → App Browse History** → Tap-Eintrag |

Verwenden Sie ** `iapp://` ** Links oder **Siri / Shortcuts**, wenn Sie iApp von außerhalb der App öffnen müssen.

---

## Tipps

- Link codes work in any app language — Sie ändern sich nicht, wenn Sie die UI-Sprache wechseln.
- Widgets und **Live Activity** erzeugen diese Links automatisch, wenn Sie tippen.
- Widget-Diagrammdaten für einige Mac / iPad bezahlt und Hochrechnung Charts können leicht von der Haupt-App abweichen.
- **Add favorite** via Shortcuts does not open the app UI — Es schreibt direkt in Ihre Favoritenliste.
- **Content compare** mode in all-region info cannot export share images — Wechseln Sie zuerst zur Listen- oder Rasteransicht.

[Zurück zur Übersicht](..) · [FAQ](../faq) · [Privacy](../privacy]

</section>
<section lang="fr" markdown="1">

iApp prend en charge les liens de raccourci ** `iapp://` ** et ** `iappstore://` **. Utilisez-les dans **Shortcuts**, signets Safari, ou à partir de **Widgets d'écran d'accueil** et **Activité en direct** pour **ouvrir une page de détail de l'application**, **retourner à une vue des classements filtrés**, **switch onglets**, ou **jeter vers des pages secondaires** ( favorites du développeur, parcourir l'historique, suivi des classements, etc.).

> **Note:** Long-press **Home Screen Quick Actions** utilisent le même texte de lien `iapp://` , mais sont envoyés comme actions rapides — non analysé par le même chemin que les URL Safari / Raccourcis lorsqu'elles sont ouvertes depuis le menu icône seulement.

## Format de lien


```
iapp://...
iappstore://...   (older alias, works the same)
```


Les hôtes sont **insensibles aux cas** et normalisés à **cas de kebab** ( `iapp://` et `iappstore://` → `iapp://{host}` ). Legacy alias: `developer_favorites` → rang, `developer.favorites` → abonnement, `developer-favorites` → revue.

| What you want | Type de lien |
|---------------|-----------|
| Open an app detail page | "iapp://app ?" |
| Open Rankings with filters | "iapp://rank?" |
| Switch tabs or open settings pages | `iapp://{host}` (voir tableaux ci-dessous) |
| Tap an app in a widget | Ouvre la page de détail |
| Tap the widget title / blank area | Ouvre la vue correspondante des classements |
| Tap a rank **Live Activity** | Ouvre la vue correspondante des classements |
| Tap a subscription **Live Activity** | Ouvre la page de détail de l'application |

---

## Ouvrir une page de détail de l'application


```
iapp://app?id={APP_ID}&region={region}&country={cc}
```


| Parameter | Required | Désignation des marchandises |
|-----------|----------|-------------|
| `id` | **Yes** | ID de l'App Store |
| `region` | No | Code régional, par exemple `cn`, `us`, `jp` (par défaut: `us`) |
| `country` | No | Code régional facultatif si la "région" est omise |

**Exemple**


```
iapp://app?id=6446581591&region=cn
```


Utilisé par : **Mes favoris widget** (tap une application), **s'abonner Activité en direct** (tap l'activité), et **Shortcuts** / signets.

---

## Ouvrir les classements avec les filtres

Passez à l'onglet **Rankings** et applique votre carte, catégorie et région choisie.


```
iapp://rank?type={chart}&category={category}&region={region}
```


| Parameter | Désignation des marchandises |
|-----------|-------------|
| `type` | Code graphique (voir tableau ci-dessous) |
| `category` | Code de la catégorie — catégorie principale ou sous-catégorie de jeu |
| `region` | Code régional, par exemple `cn`, `us` |

Les valeurs non reconnues sont ignorées; les valeurs reconnues sont rappelées.

### Codes graphiques ( `iapp://` ) — 12 graphiques

| Code | Graphique |
|------|-------|
| `topFreeApplications` | Haut de l'iPhone Gratuit |
| `topPaidApplications` | iPhone Top payé |
| `topGrossingApplications` | iPhone Top Grossing |
| `newApplications` | Nouvelles applications |
| `newFreeApplications` | Nouveau gratuit |
| `newPaidApplications` | Nouveaux paiements |
| `topFreeiPadApplications` | Haut de iPad Gratuit |
| `topPaidiPadApplications` | iPad Top payé |
| `topGrossingiPadApplications` | iPad Top Grossing |
| `topFreeMacApplications` | Mac Haut libre |
| `topPaidMacApplications` | Mac Haut payé |
| `topGrossingMacApplications` | Mac Top Grossage |

### Codes de catégorie ( `iapp://` )

| Code | Catégorie |
|------|----------|
| `0` | Toutes les applications |
| `6014` | Jeux (tous les jeux) |
| `6005` | Social |
| `6007` | Productivité |
| `6002` | Services publics |
| `6008` | Photo & Vidéo |
| `6017` | Éducation |
| `6015` | Financement |
| … | 26 catégories principales |

** Sous-catégories de jeux :** `iapp://` C1   , `iapp://{host}` C3   (18 genres). Exemple : `developer.favorites` = Action.

### Exemples


```
iapp://rank?type=topFreeApplications&category=6014&region=cn
iapp://rank?type=topFreeMacApplications&category=0&region=us
```


### Liens plus anciens de style chinois (toujours pris en charge)


```
iapp://rank?type=热门免费榜&category=游戏&region=中国
```


Utilisé par : **Rankings widget** (titre de tap / zone vide), **rank Live Activity** (tap l'activité), et **Shortcuts**.

---

## Widget liens profonds

Les widgets n'utilisent pas un format URL séparé — ils génèrent automatiquement les mêmes liens `iapp://` et `iappstore://` .

| Widget | Tap target | Ouvre |
|--------|------------|-------|
| **Rankings · iApp** | An app row | «iapp://app?id=...&region=...» |
| **Rankings · iApp** | Title or blank area | «iapp://rank?type=...&category=...&region=...» |
| **My Favorites · iApp** | An app row | «iapp://app?id=...&region=...» |

Les favoris épinglés apparaissent en premier dans le widget Mes Favoris. Widget thème et langue suivent **Paramètres → Widgets** et votre langue de l'application (l'une des 18 langues). Lors de la configuration des régions de widgets, HK / TW / MO affichent des noms d'affichage plus clairs dans la liste et la recherche unifiée (par exemple, Chine, Chine, Chine, Chine); la région stockée **codes** dans les liens reste `iapp://` , `iappstore://` , `iapp://{host}` .

---

## Parcourir l'historique (pas un lien URL)

**App Parcourir l'histoire** est géré dans **Paramètres → Données → App Parcourir l'histoire**. Taper une entrée rouvre la page de détail à l'intérieur de iApp — il ne **pas** utiliser une URL `iapp://` que vous pouvez copier ou partager à l'extérieur.

---

## Live Activity liens profonds

| Live Activity type | Tap behavior | Lien généré |
|--------------------|--------------|----------------|
| **Rankings** (tracking preset) | Opens filtered Rankings | "iapp://rank?" |
| **Subscriptions** (per subscription) | Opens app detail | «iapp://app?id=...&region=...» |

Activer l'activité en direct par suivi préréglé dans **Paramètres → Avancé**. Activer l'abonnement Activité en direct dans **Paramètres → Avancé → Activité en direct** (séparer du rang Activité en direct); puis par abonnement lors de l'ajout ou de l'édition. Les moniteurs de baisse des prix indiquent le prix de base par rapport au prix actuel sur l'écran de verrouillage.

---

## Liens d'action (pas de requête)

Ils ouvrent un onglet ou déclenchent une action dans l'application. Fonctionne à partir de ** Raccourcis**, Safari et **Actions rapides d'écran d'accueil**.

### Onglets primaires

| URL | Ouvre |
|-----|--------|
| `iapp://search` | Onglet de recherche + champ de recherche |
| `iapp://rank` | Onglet de classement (aucun filtre ne change quand aucune requête) |
| `iapp://favorites` | **Onglet Favorites** si activé dans **Paramètres → Paramètres de l'application**; sinon **Paramètres → Favoris de l'application** |
| `iapp://subscription` | Onglet Abonnements si visible; sinon **Paramètres → Abonnements** |
| `iapp://settings` | Onglet Paramètres |
| `iapp://feedback` | E-mail de commentaires |
| `iapp://review` | Note App Store in-app (alias: `iapp://rate`) |

### Pages secondaires

Ouvre l'onglet **Paramètres** d'abord, puis pousse la page cible. Si un onglet correspondant existe (p. ex. Favoris du développeur), ouvre plutôt cet onglet.

| URL | Ouvre |
|-----|--------|
| `iapp://developer-favorites` | Onglet Favoris du développeur ou **Paramètres → Favoris du développeur** |
| `iapp://browse-history` | **Paramètres → Données → App Parcourir l'histoire** |
| `iapp://favorite-groups` | **Paramètres → Données → Groupes favoris** |
| `iapp://rank-tracking` | **Paramètres → Avancé → Suivi des classements** |
| `iapp://live-activity` | **Paramètres → Avancé → Activité en direct** |
| `iapp://apple-services` | **Paramètres → tiers → Services Apple** |
| `iapp://region-switch` | **Paramètres → tiers → App Store Region** |
| `iapp://usage-guide` | **Paramètres → Aide → Instructions d'utilisation** |
| `iapp://widget-guide` | **Paramètres → Widgets → Widget Guide** (iOS 17+ seulement; URL fonctionne mais n'est pas répertorié dans Quick Actions Selecter) |

---

## Actions rapides de l'écran d'accueil

Appuyez longuement sur l'icône de l'application. Personnalisez jusqu'à **4** à partir de **15** options dans **Paramètres → Écran d'accueil Presse longue → Personnalisez les raccourcis**.

Sélection par défaut : recherche, rang, favoris, rétroaction.

Chaque option utilise les mêmes URL que ci-dessus. Les actions rapides sont envoyées par le menu icône ; les raccourcis externes / Safari utilisent le chemin unifié `iappstore://` .

| Lien | Ouvre |
|------|--------|
| `iapp://search` | Onglet de recherche + focus |
| `iapp://rank` | Tableau des classements |
| `iapp://favorites` | onglet ou paramètres favoris → App Favoris |
| `iapp://developer-favorites` | Onglet ou paramètres favoris du développeur → Favoris du développeur |
| `iapp://subscription` | Onglet ou paramètres d'abonnement → Abonnements |
| `iapp://browse-history` | App Parcourir l'historique |
| `iapp://favorite-groups` | Paramètres des groupes favoris |
| `iapp://rank-tracking` | Suivi des classements |
| `iapp://live-activity` | Paramètres d'activité en direct |
| `iapp://apple-services` | Liens Apple Services |
| `iapp://region-switch` | Commutateur de région App Store |
| `iapp://usage-guide` | Instructions d'utilisation |
| `iapp://settings` | Onglet Paramètres |
| `iapp://feedback` | E-mail de commentaires |
| `iapp://review` | Note dans l'application | `iapp://` ---

## Siri & Raccourcis (iOS 16+)

Trouvez des actions intégrées dans l'application **Shortcuts** ou demandez **Siri**. Tous les titres d'intention, étiquettes de paramètres et phrases Siri sont ** entièrement localisés** dans chaque langue de l'application — ils mettent à jour lorsque vous changez **Paramètres → Apparence → Langue**.

| Action | What you can set | Effet |
|--------|------------------|--------|
| Search apps | Keyword and region | Ouvre l'onglet Recherche avec la requête |
| Open charts | Chart, category, and region | Ouvre les classements avec filtres (même que `iapp://rank`) |
| Add favorite | App ID and region | Ajoute aux favoris silencieusement |

**Exemple Siri phrases (interface utilisateur) :** *"Rechercher des applications dans iApp"*, *"Ouvrir des graphiques dans iApp"*, *"Ajouter des favoris dans iApp"*. Dans la version 简体中文, les phrases apparaissent en chinois, même pour les 18 langues.

---

## raccourcis clavier Mac

Sur Mac, utilisez **. Les nombres sont attribués **dynamiquement** en fonction des onglets visibles:

| When visible | Raccourci typique |
|--------------|------------------|
| Rankings | 1 |
| Search | *2 |
| Subscriptions (if shown) | Numéro suivant |
| Favorites (if tab enabled) | Numéro suivant |
| Developer Favorites (if tab enabled) | Numéro suivant |
| Settings | Dernier numéro |

Exemple avec tous les onglets optionnels sur: -1 Classements · -2 Recherche · -3 Abonnements · -4 Favoris · -5 Favoris du développeur · -6 Paramètres.

Lorsqu'un onglet est caché, les onglets restants renumérotent automatiquement.

---

## Codes régionaux en liens

Les liens profonds et les URL générées par widget utilisent toujours des codes stables **region** ( `iapp://` , `iappstore://` , `iapp://{host}` , `developer_favorites` , `developer.favorites` , ...) — non pas des noms d'affichage localisés. Les récupérateurs régionaux et les chercheurs peuvent afficher des étiquettes plus claires, mais les codes stockés restent les mêmes.

**Exemples**


```
iapp://app?id=6446581591&region=hk
iapp://rank?type=topFreeApplications&category=0&region=tw
```


---

## Recherche dans l'application (pas les liens URL)

Ces travaux à l'intérieur de iApp mais ne sont pas **** URLs :

| Action | Comment |
|--------|-----|
| **Single App ID search** | Saisissez un ID numérique (6–12 chiffres, pas de virgule) dans Recherche |
| **Batch App ID search** | Jusqu'à 50 identifiants séparés par des virgules |
| **Add Subscription** | Appuyez sur n'importe quelle ligne d'application |
| **Save Developer** | Long-press → **Développeur** sous-menu, ou détail **Plus** menu |
| **Open by-ranking view** | Menu contextuel → apps ou favoris du développeur |
| **Pause / resume subscription** | Long-press sur une ligne d'abonnement |
| **Reopen from browse history** | **Paramètres → Données → App Parcourir l'histoire** → tap entry |

Utilisez des liens **        ** ou **Siri / Raccourcis** lorsque vous devez ouvrir iApp depuis l'extérieur de l'application.

---

## Conseils

- Link codes work in any app language — Ils ne changent pas lorsque vous changez de langue d'assurance-chômage.
- Widgets et **Live Activity** génèrent ces liens automatiquement lorsque vous appuyez sur.
- Les données des graphiques Widget pour certains graphiques de Mac/iPad payés et de grossissement peuvent différer légèrement de l'application principale.
- **Add favorite** via Shortcuts does not open the app UI — il écrit directement à votre liste de favoris.
- **Content compare** mode in all-region info cannot export share images — passer d'abord à la liste ou à la grille.

[Retour à l'aperçu](..) · [FAQ](../faq) · [Confidentialité](../privacité)

</section>
<section lang="tr" markdown="1">

iApp ** `iapp://` ** ve ** `iappstore://` ** kısayol bağlantıları destekler. Onları **Shortcuts**, Safari kitapmarks veya **Home Ekran widgets ** ve **Live Activity** to ** bir uygulama detay sayfasını açın**, ** filtrelenen Rankings view**, **switch sekmeleri **, veya **En iyi sayfalar için tıklayınız.

> **Not:** Long-press **Home Ekran Hızlı Eylemler ** aynı `iapp://` bağlantı metnini kullanıyor ancak hızlı eylemler olarak gönderilir - aynı yolu Safari / Kısa kesimler URL'leri yalnızca ikon menülerinden açıldığından beri iptal edilmedi.

## Bağlantı biçimi


```
iapp://...
iappstore://...   (older alias, works the same)
```


Hosts **case-in sensitive** ve normalize to **kebab-case** ( `iapp://` ve `iappstore://` → `iapp://{host}` ). Legacy alias: `developer_favorites` → sıra, `developer.favorites` → abonelik, `developer-favorites` → inceleme.

| What you want | Link tipi |
|---------------|-----------|
| Open an app detail page | "Iniapp:" |
| Open Rankings with filters | "Aptal:" |
| Switch tabs or open settings pages | "Aptal http" (aşağıdaki tablolara bakın) |
| Tap an app in a widget | Detaylı sayfayı açın |
| Tap the widget title / blank area | Anahtarlar eşleşen Rankings görünümü |
| Tap a rank **Live Activity** | Anahtarlar eşleşen Rankings görünümü |
| Tap a subscription **Live Activity** | Uygulama detay sayfasını açın |

---

## Bir uygulama detay sayfası açın


```
iapp://app?id={APP_ID}&region={region}&country={cc}
```


| Parameter | Required | Açıklama |
|-----------|----------|-------------|
| `id` | **Yes** | App Store ID |
| `region` | No | Bölge kodu, e.g. ‘cn’, “us’, “jp’ (default: “us’) |
| `country` | No | Seçmeli bölge kodu “region’ is omized |

**Example**


```
iapp://app?id=6446581591&region=cn
```


Tarafından kullanılır: **My Favorites widget** (tap an app), ** Live Live Activity** (tap the activity), ve **Shortcuts ** / kitap işaretleri.

---

## Filtrelerle Açık Sıralamalar

Anahtarlar ** Sortings ** sekmesi ve seçilmiş grafikler, kategori ve bölgenizi uygular.


```
iapp://rank?type={chart}&category={category}&region={region}
```


| Parameter | Açıklama |
|-----------|-------------|
| `type` | Grafik kodu (aşağıdaki tabloya bakınız) |
| `category` | Kategori kodu - ana kategori veya oyun alt kategori |
| `region` | Bölge kodu, e.g. ‘cn’, “us’ |

Tanımlanmamış değerler göz ardı edilir; tanınan değerler hatırlanır.

### Grafik kodları ( `iapp://` ) – 12 grafik

| Code | Grafik |
|------|-------|
| `topFreeApplications` | iPhone Top Free |
| `topPaidApplications` | iPhone Top Ücretli |
| `topGrossingApplications` | iPhone Top Grossing |
| `newApplications` | Yeni Uygulamalar |
| `newFreeApplications` | Yeni Ücretsiz |
| `newPaidApplications` | Yeni Ücretli Yeni |
| `topFreeiPadApplications` | iPad Top Free |
| `topPaidiPadApplications` | iPad Top Paid |
| `topGrossingiPadApplications` | iPad Top Grossing |
| `topFreeMacApplications` | Mac Top Free |
| `topPaidMacApplications` | Mac Top Ücretli |
| `topGrossingMacApplications` | Mac Top Grossing |

### Kategori kodları ( `iapp://` )

| Code | Kategori Kategori |
|------|----------|
| `0` | Tüm Uygulamalar |
| `6014` | Oyunlar (tüm oyunlar) |
| `6005` | Sosyal Sosyal Sosyal |
| `6007` | Verimlilik Verimliliği |
| `6002` | Utilities |
| `6008` | Foto & Video |
| `6017` | Eğitim Eğitimi |
| `6015` | Finans Finans |
| … | 26 ana kategori toplam |

**Game subcategories: ** `iapp://` - `iappstore://` , `iapp://{host}` C3    (18 türler). Örnek: `developer.favorites` = Action.

### Örnekler


```
iapp://rank?type=topFreeApplications&category=6014&region=cn
iapp://rank?type=topFreeMacApplications&category=0&region=us
```


### Eski Çin tarzı bağlantıları (still supported)


```
iapp://rank?type=热门免费榜&category=游戏&region=中国
```


Tarafından kullanılır: ** Sortings widget** (tap unvanı / boş alan), **rank Live Activity** (tap the activity), ve **Shortcuts**.

---

## Widget derin bağlantılar

Widgets ayrı bir URL formatı kullanmaz - aynı `iapp://` ve `iappstore://` bağlantıları otomatik olarak üretirler.

| Widget | Tap target | Açıklar |
|--------|------------|-------|
| **Rankings · iApp** | An app row | "Arap http?"id=...&region=..." |
| **Rankings · iApp** | Title or blank area | "Ses #rank?type=...&category=...&region=..." |
| **My Favorites · iApp** | An app row | "Arap http?"id=...&region=..." |

Pinned favoriler ilk olarak My Favorites widget'da görünüyor. Widget teması ve dili takip **Settings → Widgets** ve uygulama diliniz (18 dilden herhangi biri). widget bölgelerini yapılandırırken, HK / TW / MO listede ve birleşik aramada daha net görüntü isimleri gösterir (e.g. “China”, “HK”); depolama alanı **codes ** bağlantılarda `iapp://` , `iapp://{host}` ---

## Göz geçmişi (bir URL bağlantısı değil)

**App Browse History**, **Settings → Data → App Göz Tarih**. Bir giriş iApp içindeki ayrıntılı sayfayı yeniden açıyor - ** değil - dış kopyalayabilir veya paylaşabileceğiniz bir `iapp://` URL kullanın.

---

## Canlı Aktivite derin bağlantıları

| Live Activity type | Tap behavior | Link |
|--------------------|--------------|----------------|
| **Rankings** (tracking preset) | Opens filtered Rankings | "Aptal:" |
| **Subscriptions** (per subscription) | Opens app detail | "Arap http?"id=...&region=..." |

Enable Rank Live Activity per follow preset in **Settings → Advanced**. Enable abonelik Live Activity in **Settings → Advanced → Live Activity** (separate from Rank Live Activity); o zaman abonelik başına veya düzenleme. Price-drop monitörleri Lock Ekrandaki mevcut fiyatla temel gösteriyor.

---

## Tab & aksiyon bağlantıları (göle)

Bu bir sekme açın veya bir uygulama eylemi tetikler. **Shortcuts**, Safari ve **Home Ekran Hızlı Eylemler**.

### İlk sekmeler

| URL | Açar |
|-----|--------|
| `iapp://search` | Arama sekme + odak arama alanı |
| `iapp://rank` | Sıralamalar sekmesi (gösterme olmadığında filtre değişikliği) |
| `iapp://favorites` | **Favorites sekmesi ** Eğer etkinleştirilirse **Settings → App Ayarları**; aksi takdirde **Settings → App Favorites** |
| `iapp://subscription` | Abonelik sekmesi görünürse; aksi takdirde **Settings → Abonelikler** |
| `iapp://settings` | Ayarlar sekmesi |
| `iapp://feedback` | Geri bildirim e-postası |
| `iapp://review` | In-app App Store rating (alias: "iapp http://rate') |

### ikincil sayfalar

Opens **Settings** sekmesi ilk önce, sonra hedef sayfayı zorlar. Bir eşleşen sekme mevcutsa (e.g. Developer Favorites), bu sekmeyi yerine açar.

| URL | Açar |
|-----|--------|
| `iapp://developer-favorites` | Geliştirici Favorites sekmesi veya **Settings → Developer Favorites** |
| `iapp://browse-history` | **Settings → Data → App Browse History** |
| `iapp://favorite-groups` | **Settings → Data → Favorite groups** |
| `iapp://rank-tracking` | **Settings → Advanced → Rank İzleme** |
| `iapp://live-activity` | **Settings → Advanced → Live Activity** |
| `iapp://apple-services` | **Bölümler → Üçüncü taraf → Apple Services** |
| `iapp://region-switch` | **Settings → Üçüncü taraf → App Store Bölgesi** |
| `iapp://usage-guide` | **Bölümler → Yardım → Kullanım Talimatları** |
| `iapp://widget-guide` | **Settings → Widgets → Widget Guide** (iOS 17+ sadece; URL çalışır ancak Quick Actions picker'de listelenmez) |

---

## Home Screen Quick Actions

Uygulama ikonunu uzun baskı. **4**'ye kadar özelleştirin **15 ** seçenekler in **Settings → Home Ekran Uzun Basın → Kısayollar**.

Varsayılan seçim: arama, sıralama, favoriler, geri bildirim.

Her seçenek `iapp://` kullanır - yukarıdaki gibi aynı URL'ler. Hızlı eylemler ikon menüsü aracılığıyla gönderilir; Dış Kısayollar / Safari birleşik `iappstore://` yolu kullanır.

| Bağlantı | Açar |
|------|--------|
| `iapp://search` | Arama sekmesi + odak |
| `iapp://rank` | Sıralamalar sekmesi |
| `iapp://favorites` | Favoriler sekmesi veya Ayarlar → App Favorites |
| `iapp://developer-favorites` | Geliştirici Favoriler sekmesi veya Ayarlar → Geliştirici Favorites |
| `iapp://subscription` | Abonelik sekmesi veya Ayarlar → Abonelikler |
| `iapp://browse-history` | App Browse History |
| `iapp://favorite-groups` | Favori Grupları |
| `iapp://rank-tracking` | Rank Takip |
| `iapp://live-activity` | Canlı Aktivite ayarları |
| `iapp://apple-services` | Apple Services bağlantıları |
| `iapp://region-switch` | App Store Bölgesi Değiştir |
| `iapp://usage-guide` | Kullanım talimatları |
| `iapp://settings` | Ayarlar sekmesi |
| `iapp://feedback` | Geri bildirim e-postası |
| `iapp://review` | In-app rating | `iapp://` dış bir URL olarak destekleniyor ancak ** Quick Actions picker'de mevcut değil.

---

## Siri & Shortcuts (iOS 16+)

**Shortcuts ** uygulamasında yerleşik eylemleri bulun veya **Siri**’ye sorun. Tüm niyet başlıkları, parametre etiketleri ve Siri cümleleri ** her uygulama dilinde yerelleştirilmiş** - değiştirirler - değiştirirken güncellenirler **Dettings → Görünüm → Dil**.

| Action | What you can set | Etkisi Etkisi Etkisi |
|--------|------------------|--------|
| Search apps | Keyword and region | Opens Search sekmesi with query |
| Open charts | Chart, category, and region | Açıklar filtrelerle Sıralamalar (“iapp //rank’) |
| Add favorite | App ID and region | Favorilere sessizce ekleyin |

**Example Siri cümleleri (İngilizce UI):** *" Arama uygulamaları iApp"*, *"Open grafikler iApp"*, *"Add favorite in iApp"*. .'de, ifadeler Çin'de görünür; tüm 18 dil için aynı.

---

## Mac klavye kısayolları

Mac'te, **.1** aracılığıyla **.N ** sekmelerini değiştirmek için. Sayılar **dinamik olarak ** hangi sekmelere göre belirlenir:

| When visible | Tipik kısayol |
|--------------|------------------|
| Rankings | ⌘1 |
| Search | 2 |
| Subscriptions (if shown) | Sonraki numara |
| Favorites (if tab enabled) | Sonraki numara |
| Developer Favorites (if tab enabled) | Sonraki numara |
| Settings | Son sayı |

Tüm Seçmeli sekmelerle örnek: .1 Rankings · .2 Arama · .3 Abonelik · .4 Favorites · ⌘5 Geliştirici Favoriler · ⌘6 Ayarlar.

Bir sekme gizli olduğunda, kalan sekmeler otomatik olarak tekrarlanır.

---

## Bölge kodları bağlantıları

Derin bağlantılar ve widget tarafından üretilen URL'ler her zaman istikrarlı kullanır **region kodları** ( `iapp://` , `iappstore://` , `developer_favorites` , `developer.favorites` , ...) - yerelleştirilmiş ekran isimleri değil. Bölge seçicileri ve arama daha net etiketler gösterebilir, ancak depolama kodları aynı kalır.

**Örnekler**


```
iapp://app?id=6446581591&region=hk
iapp://rank?type=topFreeApplications&category=0&region=tw
```


---

## In-app search ( URL bağlantıları değil)

Bu çalışma iApp içinde ama **not ** `iapp://` URLs:

| Action | Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl?HowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHow HowHowHowHowHowHow HowHowHowHow HowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHow HowHow HowHow HowHow HowHow HowHow HowHow HowHowHowHowHowHowHowHowHowHowHow HowHow HowHowHowHowHow HowHow HowHow HowHow HowHow HowHow HowHow HowHow HowHowHow HowHowHow HowHow HowHow HowHow |
|--------|-----|
| **Single App ID search** | Aramada bir sayısal kimlik (6-12 basamak, hiçbir komün) girin |
| **Batch App ID search** | 50 komünlü kimliklere kadar |
| **Add Subscription** | Long-press any app row |
| **Save Developer** | Uzun baskı → **Developer ** submenu, veya detay **More** menüsü |
| **Open by-ranking view** | Context menu → aynı geliştirme uygulamaları veya geliştirici favoriler |
| **Pause / resume subscription** | Bir abonelik sırasına uzun baskı |
| **Reopen from browse history** | **Settings → Data → App Browse History** → musluk girişi |

Kullanım ** `iapp://` ** bağlantıları veya **Siri / Kısa kesimler** uygulama dışında iApp açmanız gerektiğinde.

---

## İpuçları

- Link codes work in any app language — UI dilini değiştirirken değişmezler.
- Widgets ve **Live Activity **, dokunduğunuzda bu bağlantıları otomatik olarak üretir.
- Bazı Mac /iPad için Widget grafik verileri ana uygulamadan biraz farklı olabilir.
- **Add favorite** via Shortcuts does not open the app UI — Doğrudan favorilerinize yazar.
- **Content compare** mode in all-region info cannot export share images — İlk önce liste veya ağ görünümüne geçiş.

[Genellikle] (.) · [FAQ](./faq) · [Privacy] (./privacy)

</section>
