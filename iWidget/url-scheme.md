---
layout: doc
title: iWidget — URL Scheme Reference
app_id: iWidget
doc_title_en: URL Scheme Reference
doc_title_zh_cn: URL Scheme 说明
doc_title_zh_tw: URL Scheme 說明
description: iwidget:// deep links — open Today, a specific day, or Settings festival filters from Safari, Shortcuts, or other apps.
---

<section lang="en" markdown="1">

iWidget supports the **`iwidget://`** URL scheme on **iPhone, iPad, and Mac**. Use it in **Safari**, **Apple Shortcuts**, another app, or a QR code to jump into the main app. These links **navigate only** — they do not pass widget design IDs or edit board layouts.

For spoken lunar / festival answers **without** opening the app, use **Siri App Shortcuts** (see [FAQ](../faq) → Siri). For **work/rest on a date**, add the separate **Workday** App Intent in Shortcuts.

## Format

```
iwidget://<host>[?query]
```

| Rule | Detail |
|------|--------|
| **Scheme** | `iwidget` (lowercase) |
| **Host** | Path segment — see table below |
| **Query** | Optional; only documented keys are read |

Unknown hosts are ignored safely (no crash).

---

## Hosts

| Host | Opens | Query |
|------|--------|-------|
| `today` | **Today** tab | — |
| `day` | **Today** tab and queues **day detail** for the given date | **`y`** year · **`m`** month · **`d`** day (integers) |
| `settings` | **Settings** tab | **`scroll=festivals`** scrolls to festival filter section |

If `day` query values are missing or invalid, the app still switches to Today without opening a day sheet.

---

## Examples

**Open Today**

```
iwidget://today
```

**Open 1 January 2026 detail**

```
iwidget://day?y=2026&m=1&d=1
```

**Open Settings → festival filters**

```
iwidget://settings?scroll=festivals
```

---

## Widget & Control Center behavior

- Tapping a **home-screen board** when **intercept taps** is off may open `iwidget://today` (or your configured open behavior via widget intent).
- **Lock Screen** and **Control Center** entries use App Intents; they are not additional URL hosts.
- **Mac menu bar** calendar uses the same `day` URL pattern when you click a date.

---

## Shortcuts tips

1. Add **Open URL** and paste an `iwidget://` link.
2. For **Workday** checks, search the Shortcuts action library for iWidget’s **work/rest day** intent and supply a date — it is **not** available as a URL query.

[Back to iWidget Support](../) · [FAQ](../faq) · [Privacy Policy](../privacy)

</section>

<section lang="zh-CN" markdown="1">

爱组件支持 **`iwidget://`** URL Scheme，适用于 **iPhone、iPad 与 Mac**。可在 **Safari**、**快捷指令**、其他应用或二维码中打开主 App。链接 **仅用于导航**，不会传递小组件设计 ID 或编辑看板布局。

若要在 **不打开 App** 的情况下语音查询农历/节日，请用 **Siri App 快捷指令**（见 [常见问题](../faq)）。查询 **某日是否上班** 请在快捷指令中添加独立的 **是否上班** App Intent，**不能**用 URL 参数代替。

## 格式

```
iwidget://<host>[?query]
```

| 规则 | 说明 |
|------|------|
| **Scheme** | `iwidget`（小写） |
| **Host** | 路径段 — 见下表 |
| **Query** | 可选；仅读取文档中的键 |

未知 host 会被安全忽略（不会崩溃）。

---

## Host 列表

| Host | 打开 | Query |
|------|------|-------|
| `today` | **今日** 标签 | — |
| `day` | **今日** 并排队 **日详情** | **`y`** 年 · **`m`** 月 · **`d`** 日（整数） |
| `settings` | **设置** 标签 | **`scroll=festivals`** 滚动到节日筛选区 |

`day` 参数缺失或无效时，仍会切到今日，但不打开日详情。

---

## 示例

**打开今日**

```
iwidget://today
```

**打开 2026 年 1 月 1 日日详情**

```
iwidget://day?y=2026&m=1&d=1
```

**打开设置 → 节日筛选**

```
iwidget://settings?scroll=festivals
```

---

## 小组件与控制中心

- **主屏看板** 在未开启 **拦截跳转** 时，点按可能打开 `iwidget://today`（或你在小组件 Intent 里配置的打开方式）。
- **锁屏** 与 **控制中心** 使用 App Intent，不是额外的 URL host。
- **Mac 菜单栏** 月历点日期时使用相同的 `day` URL。

---

## 快捷指令提示

1. 添加 **打开 URL**，粘贴 `iwidget://` 链接。
2. **是否上班** 请在动作库搜索爱组件对应 Intent 并传入日期 — **没有** URL 形式。

[返回爱组件支持页](../) · [常见问题](../faq) · [隐私政策](../privacy)

</section>

<section lang="zh-TW" markdown="1">

愛組件支援 **`iwidget://`** URL Scheme，適用於 **iPhone、iPad 與 Mac**。可在 **Safari**、**捷徑**、其他 App 或 QR Code 中開啟主 App。連結 **僅用於導覽**，不會傳遞小工具設計 ID 或編輯看板版面。

若要在 **不開啟 App** 的情況下語音查詢農曆/節日，請用 **Siri App 捷徑**（見 [常見問題](../faq)）。查詢 **某日是否上班** 請在捷徑中新增獨立的 **是否上班** App Intent，**不能**用 URL 參數代替。

## 格式

```
iwidget://<host>[?query]
```

| 規則 | 說明 |
|------|------|
| **Scheme** | `iwidget`（小寫） |
| **Host** | 路徑段 — 見下表 |
| **Query** | 可選；僅讀取文件中的鍵 |

未知 host 會被安全忽略（不會當機）。

---

## Host 列表

| Host | 開啟 | Query |
|------|------|-------|
| `today` | **今日** 標籤 | — |
| `day` | **今日** 並排隊 **日詳情** | **`y`** 年 · **`m`** 月 · **`d`** 日（整數） |
| `settings` | **設定** 標籤 | **`scroll=festivals`** 捲動到節日篩選區 |

`day` 參數缺失或無效時，仍會切到今日，但不開啟日詳情。

---

## 示例

**開啟今日**

```
iwidget://today
```

**開啟 2026 年 1 月 1 日日詳情**

```
iwidget://day?y=2026&m=1&d=1
```

**開啟設定 → 節日篩選**

```
iwidget://settings?scroll=festivals
```

---

## 小工具與控制中心

- **主畫面看板** 在未開啟 **攔截跳轉** 時，點按可能開啟 `iwidget://today`（或你在小工具 Intent 裡設定的開啟方式）。
- **鎖定畫面** 與 **控制中心** 使用 App Intent，不是額外的 URL host。
- **Mac 選單列** 月曆點日期時使用相同的 `day` URL。

---

## 捷徑提示

1. 新增 **開啟 URL**，貼上 `iwidget://` 連結。
2. **是否上班** 請在動作庫搜尋愛組件對應 Intent 並傳入日期 — **沒有** URL 形式。

[返回愛組件支援頁](../) · [常見問題](../faq) · [隱私政策](../privacy)

</section>
