---
layout: doc
title: iWool — URL Scheme Reference
app_id: iWool
doc_title_en: URL Scheme Reference
doc_title_zh_cn: URL Scheme 深度链接文档
doc_title_zh_tw: URL Scheme 深度連結文件
description: Complete reference of iwool:// deep links — tabs, actions, event detail, widgets and Home Screen Quick Actions.
---

<section lang="en" markdown="1">

iWool supports **`iwool://`** URL scheme deep links — open a tab, start an in-app action, or jump to a specific activity from Safari, Apple Shortcuts, a widget tap, or a Home Screen Quick Action (long-press the app icon).

> **Important:** Deep links only **navigate inside iWool**. They do not create server connections or sync data to the cloud.

## Protocol Specification

```
iwool://<path>[?query]
```

| Rule | Detail |
|------|--------|
| **Scheme** | `iwool` (case-insensitive) |
| **Routing** | First path segment (host or path) selects the destination |
| **Empty URL** | `iwool://` with no path → **Home** |
| **Unknown paths** | **Ignored** (no silent fallback to Home) |
| **Parser** | `IWoolDeepLink.parse(_:)` → `ContentView.applyDeepLink` |

---

## 1. Tab destinations

| URL | Opens | Aliases |
|-----|--------|---------|
| `iwool://home` | **Home** tab | — |
| `iwool://calendar` | **Calendar** tab | `cal` |
| `iwool://stats` | **Statistics** tab | `statistics`, `stat` |
| `iwool://settings` | **Settings** tab | `setting`, `preferences` |

---

## 2. In-app actions

These routes match **Home Screen Quick Actions** and open sheets or sub-pages:

| URL | Opens | Aliases |
|-----|--------|---------|
| `iwool://new` | **Create activity** sheet | `create`, `add`, `new-event`, `newevent` |
| `iwool://island` | **Quick Countdown** (Dynamic Island reminder) sheet | `island-reminder`, `islandreminder`, `countdown`, `quick-countdown`, `quickcountdown` |
| `iwool://reminders` | **Scheduled local reminders** list (Settings) | `scheduled-reminders`, `scheduledreminders`, `scheduled`, `notification-reminders` |
| `iwool://scanner` | **QR / barcode scanner** (Settings → Tools) | `scan`, `qrcode`, `barcode` |
| `iwool://rate` | In-app **App Store rating** prompt | `rating`, `review`, `rate-in-app`, `rateinapp` |
| `iwool://feedback` | **Feedback** email compose | `mail`, `support`, `contact` |

**Nested settings paths** (same actions):

```
iwool://settings/scanner
iwool://settings/reminders
iwool://settings/rate
iwool://settings/feedback
```

---

## 3. Activity detail

Open a single wool activity by database ID.

| Parameter | Required | Description |
|-----------|----------|-------------|
| Path `event/{id}` | One of path / query | Activity ID (positive integer) |
| Query `id={id}` | One of path / query | Same as path form |
| Query `day={seconds}` | No | For **recurring** activities — natural-day start as `timeIntervalSince1970` (midnight of that occurrence day) |

**Open activity 42**

```
iwool://event/42
iwool://event?id=42
```

**Recurring occurrence on a specific day**

```
iwool://event/42?day=189345600
```

When building links for recurring series, iWool can derive `day` from the same logic as the home list (`IWoolDeepLink.occurrenceDayStartForDeepLink`).

---

## 4. Home Screen Quick Actions (iOS)

Long-press the iWool icon → up to **4** actions. Customize in **Settings → Tools → Home Screen Shortcuts** (9 options, drag to reorder, reset to defaults).

| Option | URL |
|--------|-----|
| Home | `iwool://home` |
| Calendar | `iwool://calendar` |
| Statistics | `iwool://stats` |
| Quick Countdown | `iwool://island` |
| New Activity | `iwool://new` |
| Scheduled Reminders | `iwool://reminders` |
| Scanner | `iwool://scanner` |
| Rate App | `iwool://rate` |
| Feedback | `iwool://feedback` |

**Default on first install:** Home · Calendar · Statistics · Quick Countdown.

Quick-action `type` strings use the same `iwool://` paths and route through `ShortcutSceneDelegate` → `ShortcutObserver` on cold start.

---

## 5. Widget deep links

Widget taps use the same `iwool://` URLs:

| Widget | Tap target | URL |
|--------|------------|-----|
| Today Active / Today All / Today Upcoming / All Events | Home | `iwool://home` |
| Stats Overview / Earnings / Top Platforms | Statistics | `iwool://stats` |
| Glance | First event or Home | `iwool://event/{id}` or `iwool://home` |
| Lock Screen accessories | First event or Home | `iwool://event/{id}` or `iwool://home` |
| List row (iOS 17+) | Activity detail | `iwool://event/{id}` |

Quick Countdown Live Activities use in-app UI only — **no separate URL** to start an island countdown from outside the app (use `iwool://island` to open the creation sheet).

---

## Apple Shortcuts examples

**Open Statistics**

```
iwool://stats
```

**Create a new activity**

```
iwool://new
```

**Open Quick Countdown sheet**

```
iwool://island
```

**Open activity after copying ID**

```
iwool://event?id=42
```

---

## Launch behaviour

| Scenario | Flow |
|----------|------|
| **Widget / Shortcuts `onOpenURL`** | `AppRouter` → `applyDeepLink` |
| **Cold start — Quick Action** | `ShortcutSceneDelegate` → `PendingShortcutBuffer` → `ShortcutObserver` |
| **Warm start — Quick Action** | Scene callback → notification → `ShortcutObserver` |
| **Feedback / Rate (cold start)** | Short delay so mail sheet / StoreKit has an active window scene |
| **Invalid event ID** | Link ignored — no alert |

---

## Troubleshooting

| Issue | What to check |
|-------|----------------|
| Link opens app but nothing happens | Path must match a supported route; unknown paths are not redirected to Home |
| `event` link shows wrong occurrence | Add `?day=` for recurring activities |
| Quick Action does nothing on cold launch | Wait ~0.4 s or retry; feedback/rate need UI mount time |
| `iwool://island` does not start countdown automatically | Opens the **creation sheet** — confirm duration and tap Start inside the app |
| Quick Countdown requires iOS 16.2+ | Event Live Activities need iOS 16.1+; standalone island countdown needs 16.2+ |

---

[Back to iWool Support](..) · [FAQ](faq) · [Privacy Policy](privacy)

</section>

<section lang="zh-CN" markdown="1">

爱羊毛支持 **`iwool://`** URL Scheme 深度链接——从 Safari、苹果快捷指令、小组件点击或主屏快捷方式（长按图标）打开标签页、应用内操作或指定活动。

> **说明：** 深度链接仅用于**应用内导航**，不会连接服务器或上传数据。

## 协议规范

```
iwool://<path>[?query]
```

| 规则 | 说明 |
|------|------|
| **Scheme** | `iwool`（不区分大小写） |
| **空 URL** | `iwool://` → **首页** |
| **未知路径** | **忽略**（不再静默回首页） |

---

## 1. Tab 入口

| URL | 打开 | 别名 |
|-----|------|------|
| `iwool://home` | **首页** | — |
| `iwool://calendar` | **日历** | `cal` |
| `iwool://stats` | **统计** | `statistics`、`stat` |
| `iwool://settings` | **设置** | `setting`、`preferences` |

---

## 2. 应用内操作

| URL | 打开 | 别名 |
|-----|------|------|
| `iwool://new` | **新建活动** | `create`、`add`、`new-event` |
| `iwool://island` | **灵动岛提醒**（Quick Countdown 创建页） | `countdown`、`quick-countdown` 等 |
| `iwool://reminders` | **已登记本地提醒**列表 | `scheduled-reminders`、`scheduled` |
| `iwool://scanner` | **扫码器** | `scan`、`qrcode`、`barcode` |
| `iwool://rate` | 应用内**评分** | `rating`、`review` |
| `iwool://feedback` | **意见反馈** | `mail`、`support`、`contact` |

嵌套路径示例：`iwool://settings/scanner`

---

## 3. 活动详情

| 参数 | 说明 |
|------|------|
| `iwool://event/{id}` 或 `?id=` | 活动 ID |
| `?day={秒}` | 重复活动指定自然日 0 点的 `timeIntervalSince1970` |

```
iwool://event/42
iwool://event/42?day=189345600
```

---

## 4. 主屏快捷方式（iOS）

长按图标 → 最多 **4** 项。在 **设置 → 工具 → 主屏快捷方式** 配置（9 项可选）。

默认：**首页 · 日历 · 统计 · 灵动岛提醒**。

| 选项 | URL |
|------|-----|
| 首页 | `iwool://home` |
| 日历 | `iwool://calendar` |
| 统计 | `iwool://stats` |
| 灵动岛提醒 | `iwool://island` |
| 新建活动 | `iwool://new` |
| 已登记提醒 | `iwool://reminders` |
| 扫码 | `iwool://scanner` |
| 评分 | `iwool://rate` |
| 反馈 | `iwool://feedback` |

---

## 5. 小组件深度链接

| 小组件 | URL |
|--------|-----|
| 今日系列 / 全部活动 | `iwool://home` |
| 统计 / 收益 / 平台排行 | `iwool://stats` |
| 列表单行（iOS 17+） | `iwool://event/{id}` |

`iwool://island` 打开创建页，不会从外部直接启动倒计时——需在应用内确认时长。

---

## 示例

```
iwool://stats
iwool://new
iwool://island
iwool://event?id=42
```

---

## 常见问题

| 现象 | 处理 |
|------|------|
| 链接无反应 | 路径须为支持名称；无效路径不会回首页 |
| 重复活动场次不对 | 加 `?day=` 参数 |
| 灵动岛提醒需 iOS 16.2+ | 活动 Live Activity 为 16.1+ |

---

[返回爱羊毛支持](..) · [常见问题](faq) · [隐私政策](privacy)

</section>

<section lang="zh-TW" markdown="1">

愛羊毛支援 **`iwool://`** URL Scheme 深度連結——從 Safari、Apple 捷徑、小工具點擊或主畫面捷徑（長按圖示）開啟標籤頁、應用內操作或指定活動。

> **說明：** 深度連結僅用於**應用內導覽**，不會連接伺服器或上傳資料。

## 協定規範

| 規則 | 說明 |
|------|------|
| **Scheme** | `iwool` |
| **空 URL** | `iwool://` → **首頁** |
| **未知路徑** | **忽略** |

---

## 1. Tab 入口

| URL | 開啟 | 別名 |
|-----|------|------|
| `iwool://home` | **首頁** | — |
| `iwool://calendar` | **日曆** | `cal` |
| `iwool://stats` | **統計** | `statistics`、`stat` |
| `iwool://settings` | **設定** | `setting`、`preferences` |

---

## 2. 應用內操作

| URL | 開啟 | 別名 |
|-----|------|------|
| `iwool://new` | **新建活動** | `create`、`add` |
| `iwool://island` | **靈動島提醒**（Quick Countdown） | `countdown`、`quick-countdown` |
| `iwool://reminders` | **已登記本地提醒** | `scheduled-reminders` |
| `iwool://scanner` | **掃碼器** | `scan`、`qrcode` |
| `iwool://rate` | 應用內**評分** | `rating`、`review` |
| `iwool://feedback` | **意見回饋** | `mail`、`support` |

---

## 3. 活動詳情

```
iwool://event/42
iwool://event/42?day=189345600
```

`?day=` 為重複活動指定自然日場次。

---

## 4. 主畫面捷徑（iOS）

最多 **4** 項；**設定 → 工具 → 主畫面捷徑**（9 項可選）。預設：首頁 · 日曆 · 統計 · 靈動島提醒。

---

## 5. 小工具連結

今日系列 → `iwool://home`；統計系列 → `iwool://stats`；列表列 → `iwool://event/{id}`。

---

[返回愛羊毛支援](..) · [常見問題](faq) · [隱私政策](privacy)

</section>
