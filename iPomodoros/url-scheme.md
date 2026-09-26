---
layout: doc
title: iPomodoro — URL Scheme Reference
app_id: iPomodoros
doc_title_en: URL Scheme Reference
doc_title_zh_cn: URL Scheme 深度链接文档
doc_title_zh_tw: URL Scheme 深度連結文件
description: Complete reference of iPomodoro:// and iPomodoros:// deep links — open tabs, motivation quote, or feedback from Safari, Shortcuts, or other apps.
---

<section lang="en" markdown="1">

iPomodoro supports **`iPomodoro://`** and **`iPomodoros://`** URL scheme deep links — open a tab or in-app sheet from Safari, another app, a QR code, or Apple Shortcuts. These URLs mirror the destinations available as **Home Screen Quick Actions** (long-press the app icon).

> **Note:** URL links do **not** start or stop timers, pass task IDs, or pre-fill durations. They only navigate inside the app. For spoken focus summaries without opening the app, use **Siri App Shortcuts** (see [Related: Siri & App Shortcuts](#related-siri--app-shortcuts) below).

## Protocol Specification

```
iPomodoro://<path>
iPomodoros://<path>
```

| Rule | Detail |
|------|--------|
| **Schemes** | `iPomodoro` (primary) · `iPomodoros` (also accepted) |
| **Path** | Single segment, **case-insensitive** — resolved from the URL **host** |
| **Query parameters** | Not supported (ignored if present) |
| **Equivalent Quick Action type** | `iPomodoro://<path>` (same string registered on Home Screen shortcuts) |

Path matching is **exact** on the segment name — the app does not fuzzy-match substrings like `contains("pomodoro")`.

---

## Destinations

| Path | Opens | Notes |
|------|--------|-------|
| `pomodoro` | **Pomodoro** tab | Does not auto-start a session |
| `study` | **Study Timer** tab | Does not auto-start a session |
| `tasks` | **Tasks** tab | |
| `stats` | **Statistics** tab | |
| `motivation` | **Motivational Quote Anthology** full-screen gallery | Same UI as **Settings → Motivational Quote Settings → Motivational Quote Anthology** |
| `feedback` | **Feedback** sheet | Uses in-app Mail compose when available; falls back to `mailto:` |

---

## Examples

**Open Pomodoro tab**

```
iPomodoro://pomodoro
```

**Open Study Timer tab** (alternate scheme)

```
iPomodoros://study
```

**Open Statistics dashboard**

```
iPomodoro://stats
```

**Show a motivation quote**

```
iPomodoro://motivation
```

**Open feedback**

```
iPomodoro://feedback
```

---

## Launch Behavior

When the app receives a URL (cold start or while running):

1. `ShortcutObserver` resolves the path via `AppShortcutOption.matchingShortcutURL`.
2. Navigation is **deferred ~0.45 s** so SwiftUI can finish mounting.
3. On **cold start**, a URL / Quick Action takes **priority** over automatically jumping to an active Pomodoro or Study tab from a restored Live Activity session.

**Motivation** and **feedback** open overlays directly — they do not switch tabs first.

---

## Apple Shortcuts

**Open Pomodoro tab**

1. Add action **Open URL**
2. URL: `iPomodoro://pomodoro`

**Open Statistics after a focus block**

```
iPomodoro://stats
```

Use **Open URL** in a Personal Automation (e.g. after a Focus mode ends) to jump straight to your dashboard.

---

## Related: Siri & App Shortcuts

Built-in **App Shortcuts** (Siri / Shortcuts app) complement URL links:

| Intent | Behavior |
|--------|----------|
| Open Pomodoro | Switches to Pomodoro tab |
| Open Study Timer | Switches to Study Timer tab |
| Open Statistics | Switches to Statistics tab |
| Today's focus summary | Returns today's focus duration and pomodoro count **without requiring the app UI** |

Example Siri phrase: *"How long did I focus today in iPomodoro?"*

Configure which four items appear on the Home Screen icon under **Settings → App settings → Home Screen shortcuts** (drag to reorder). URL paths above cover all six possible destinations; only four can appear on the icon at once.

---

## Troubleshooting

| Issue | What to check |
|-------|----------------|
| Link does nothing | Ensure the app is installed; path must be one of the six names above |
| Wrong tab after reopening | If a timer Live Activity is active, a **Quick Action / URL launch overrides** auto tab restore |
| `feedback` opens Mail app only | Device has no configured Mail account — iPomodoro falls back to `mailto:` |

---

[Back to iPomodoro Support](./) &middot; [FAQ](faq) &middot; [Privacy Policy](privacy)

</section>

<section lang="zh-CN" markdown="1">

爱番茄（iPomodoro）支持 **`iPomodoro://`** 与 **`iPomodoros://`** URL Scheme 深度链接——可从 Safari、其他 App、二维码或苹果快捷指令打开指定 Tab 或应用内页面。这些 URL 与 **主屏 Quick Actions**（长按图标）指向相同目的地。

> **说明：** URL **不会**自动开始/停止计时，也不支持传入任务 ID 或预填时长，仅用于 App 内导航。若需不打开界面即可查询今日专注，请使用 **Siri App Shortcuts**（见下文 [相关：Siri 与 App Shortcuts](#相关siri-与-app-shortcuts)）。

## 协议规范

```
iPomodoro://<path>
iPomodoros://<path>
```

| 规则 | 说明 |
|------|------|
| **Scheme** | `iPomodoro`（主）· `iPomodoros`（亦支持） |
| **Path** | 单段路径，**大小写不敏感** — 从 URL **host** 解析 |
| **查询参数** | 不支持（若附带会被忽略） |
| **等同 Quick Action type** | `iPomodoro://<path>`（与主屏快捷操作注册字符串一致） |

路径匹配为 segment **精确匹配**，不会用模糊 `contains("pomodoro")` 等方式猜测。

---

## 目的地

| Path | 打开 | 说明 |
|------|------|------|
| `pomodoro` | **番茄** Tab | 不会自动开始计时 |
| `study` | **计时** Tab | 不会自动开始计时 |
| `tasks` | **定任务** Tab | |
| `stats` | **统计** Tab | |
| `motivation` | **励志语录大全** 全屏浏览 | 与 **设置 → 励志语设置 → 励志语录大全** 相同 UI |
| `feedback` | **反馈** Sheet | 优先应用内邮件；不可用则 `mailto:` 回退 |

---

## 示例

**打开番茄 Tab**

```
iPomodoro://pomodoro
```

**打开计时 Tab**（备用 scheme）

```
iPomodoros://study
```

**打开统计仪表盘**

```
iPomodoro://stats
```

**展示励志语录**

```
iPomodoro://motivation
```

**打开反馈**

```
iPomodoro://feedback
```

---

## 启动行为

App 收到 URL（冷启动或前台/后台运行中）时：

1. `ShortcutObserver` 经 `AppShortcutOption.matchingShortcutURL` 解析 path。
2. 导航 **延迟约 0.45 秒**，等待 SwiftUI 完成挂载。
3. **冷启动**时，URL / Quick Action **优先于** 因 Live Activity 恢复而自动跳转到活跃番茄/计时 Tab。

**motivation** 与 **feedback** 直接打开全屏/Sheet，不会先切换 Tab。

---

## 苹果快捷指令

**打开番茄 Tab**

1. 添加 **打开 URL** 操作
2. URL 填 `iPomodoro://pomodoro`

**专注结束后查看统计**

```
iPomodoro://stats
```

可在个人自动化（例如 Focus 模式结束时）用 **打开 URL** 直达统计 Tab。

---

## 相关：Siri 与 App Shortcuts

内置 **App Shortcuts**（Siri / 快捷指令 App）与 URL 互补：

| Intent | 行为 |
|--------|------|
| 打开番茄 | 切换到番茄 Tab |
| 打开计时 | 切换到计时 Tab |
| 打开统计 | 切换到统计 Tab |
| 今日专注摘要 | 返回今日专注时长与番茄数，**无需打开 App 界面** |

Siri 示例：*「爱番茄今天专注了多久？」*

主屏图标最多显示 4 项快捷操作，在 **设置 → 应用设置 → 主屏快捷操作** 中自选并排顺序。上述 6 个 path 覆盖全部目的地。

---

## 故障排查

| 现象 | 检查 |
|------|------|
| 链接无反应 | 确认已安装 App；path 必须是上述 6 个名称之一 |
| 重开 App 后 Tab 不对 | 若有活跃 Live Activity，**Quick Action / URL 启动优先**于自动恢复切 Tab |
| feedback 只打开邮件 App | 设备未配置邮件账户 — 爱番茄会回退到 `mailto:` |

---

[返回爱番茄支持页](./) &middot; [常见问题](faq) &middot; [隐私政策](privacy)

</section>

<section lang="zh-TW" markdown="1">

愛番茄（iPomodoro）支援 **`iPomodoro://`** 與 **`iPomodoros://`** URL Scheme 深度連結——可從 Safari、其他 App、QR Code 或 Apple 捷徑開啟指定 Tab 或應用內頁面。這些 URL 與 **主畫面 Quick Actions**（長按圖示）指向相同目的地。

> **說明：** URL **不會**自動開始/停止計時，也不支援傳入任務 ID 或預填時長，僅用於 App 內導覽。若需不開啟介面即可查詢今日專注，請使用 **Siri App Shortcuts**（見下文 [相關：Siri 與 App Shortcuts](#相關siri-與-app-shortcuts)）。

## 協議規範

```
iPomodoro://<path>
iPomodoros://<path>
```

| 規則 | 說明 |
|------|------|
| **Scheme** | `iPomodoro`（主）· `iPomodoros`（亦支援） |
| **Path** | 單段路徑，**大小寫不敏感** — 從 URL **host** 解析 |
| **查詢參數** | 不支援（若附帶會被忽略） |
| **等同 Quick Action type** | `iPomodoro://<path>`（與主畫面快捷操作註冊字串一致） |

路徑匹配為 segment **精確匹配**，不會用模糊 `contains("pomodoro")` 等方式猜測。

---

## 目的地

| Path | 開啟 | 說明 |
|------|------|------|
| `pomodoro` | **番茄** Tab | 不會自動開始計時 |
| `study` | **計時** Tab | 不會自動開始計時 |
| `tasks` | **定任務** Tab | |
| `stats` | **統計** Tab | |
| `motivation` | **勵志語錄大全** 全螢幕瀏覽 | 與 **設定 → 勵志語錄設定 → 勵志語錄大全** 相同 UI |
| `feedback` | **回饋** Sheet | 優先應用內郵件；不可用則 `mailto:` 回退 |

---

## 範例

**開啟番茄 Tab**

```
iPomodoro://pomodoro
```

**開啟計時 Tab**（備用 scheme）

```
iPomodoros://study
```

**開啟統計儀表板**

```
iPomodoro://stats
```

**展示勵志語錄**

```
iPomodoro://motivation
```

**開啟回饋**

```
iPomodoro://feedback
```

---

## 啟動行為

App 收到 URL（冷啟動或前景/背景執行中）時：

1. `ShortcutObserver` 經 `AppShortcutOption.matchingShortcutURL` 解析 path。
2. 導覽 **延遲約 0.45 秒**，等待 SwiftUI 完成掛載。
3. **冷啟動**時，URL / Quick Action **優先於** 因 Live Activity 恢復而自動跳轉到活躍番茄/計時 Tab。

**motivation** 與 **feedback** 直接開啟全螢幕/Sheet，不會先切換 Tab。

---

## Apple 捷徑

**開啟番茄 Tab**

1. 新增 **打開 URL** 動作
2. URL 填 `iPomodoro://pomodoro`

**專注結束後查看統計**

```
iPomodoro://stats
```

可在個人自動化（例如 Focus 模式結束時）用 **打開 URL** 直達統計 Tab。

---

## 相關：Siri 與 App Shortcuts

內建 **App Shortcuts**（Siri / 捷徑 App）與 URL 互補：

| Intent | 行為 |
|--------|------|
| 開啟番茄 | 切換到番茄 Tab |
| 開啟計時 | 切換到計時 Tab |
| 開啟統計 | 切換到統計 Tab |
| 今日專注摘要 | 回傳今日專注時長與番茄數，**無需開啟 App 介面** |

Siri 範例：*「愛番茄今天專注了多久？」*

主畫面圖示最多顯示 4 項快捷操作，在 **設定 → 應用設定 → 主畫面快捷操作** 中自選並排序。上述 6 個 path 涵蓋全部目的地。

---

## 故障排查

| 現象 | 檢查 |
|------|------|
| 連結無反應 | 確認已安裝 App；path 必須是上述 6 個名稱之一 |
| 重開 App 後 Tab 不對 | 若有活躍 Live Activity，**Quick Action / URL 啟動優先**於自動恢復切 Tab |
| feedback 只開啟郵件 App | 裝置未設定郵件帳戶 — 愛番茄會回退到 `mailto:` |

---

[返回愛番茄支援頁](./) &middot; [常見問題](faq) &middot; [隱私政策](privacy)

</section>
