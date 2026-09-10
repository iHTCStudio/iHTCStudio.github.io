---
layout: doc
title: iConnect — URL Scheme Reference
app_id: iConnect
doc_title_en: URL Scheme Reference
doc_title_zh_cn: URL Scheme 深度链接文档
doc_title_zh_tw: URL Scheme 深度連結文件
description: Complete reference of iconnect:// deep links — open tabs, settings pages, share, feedback, and review from Safari, Shortcuts, or other apps.
---

<section lang="en" markdown="1">

iConnect supports **`iconnect://`** URL scheme deep links — open a tab, a Settings page, or an in-app sheet from Safari, another app, a bookmark, or Apple Shortcuts. These URLs mirror the destinations available as **Home Screen Quick Actions** on iPhone and iPad (long-press the app icon).

> **Note:** URL links only **navigate inside iConnect**. They do not connect to a peer, start a transfer, or open a specific chat thread.

## Protocol Specification

```
iconnect://<host>
iconnect://<host>?refresh=1
```

| Rule | Detail |
|------|--------|
| **Scheme** | `iconnect` |
| **Host / path** | Single segment, **case-insensitive** — resolved from the URL **host** or first **path** segment |
| **Aliases** | Several hosts accept synonyms (see table below) |
| **Query** | Only `refresh=1` / `refresh=true` on **Devices** triggers a discovery refresh |

Examples of equivalent forms:

```
iconnect://devices
iconnect://open/devices
```

---

## Tab destinations

| URL | Opens | Aliases |
|-----|--------|---------|
| `iconnect://devices` | **Devices** tab (radar / discovery) | `device` |
| `iconnect://devices?refresh=1` | **Devices** tab and **refreshes** nearby discovery | — |
| `iconnect://chat` | **Chats** tab | `messages` |
| `iconnect://transfers` | **Transfers** tab | `transfer` |
| `iconnect://history` | **History** tab (transfer log) | — |
| `iconnect://settings` | **Settings** tab | `setting` |

**Refresh discovery**

```
iconnect://devices?refresh=1
iconnect://devices/refresh
```

---

## Settings sub-pages

These links switch to **Settings**, then open the matching page:

| URL | Opens | Aliases |
|-----|--------|---------|
| `iconnect://about` | About | — |
| `iconnect://usage` | Usage Guide | `guide`, `help`, `usageguide` |
| `iconnect://shortcuts` | Home Screen shortcuts picker (iOS) | `homeshortcuts` |
| `iconnect://debug` | Debug / diagnostics info | `debuginfo` |

---

## In-app actions

| URL | Opens |
|-----|--------|
| `iconnect://share` | Share iConnect sheet (App Store link + recommendation text) |
| `iconnect://feedback` | Feedback email compose (falls back to `mailto:` if Mail is unavailable) |
| `iconnect://review` | In-app App Store rating prompt |

**Review aliases:** `iconnect://rate`, `iconnect://rating`

---

## Examples

**Open Chats tab**

```
iconnect://chat
```

**Open Transfers tab**

```
iconnect://transfers
```

**Refresh device discovery**

```
iconnect://devices?refresh=1
```

**Open Usage Guide**

```
iconnect://usage
```

**Share the app**

```
iconnect://share
```

---

## Home Screen Quick Actions (iOS)

Long-press the iConnect icon. Customize up to **4** shortcuts in **Settings → Home Screen shortcuts** (drag to reorder).

| Quick Action | URL |
|--------------|-----|
| Devices | `iconnect://devices` |
| Chats | `iconnect://chat` |
| Transfers | `iconnect://transfers` |
| History | `iconnect://history` |
| Share | `iconnect://share` |
| Feedback | `iconnect://feedback` |
| Rate | `iconnect://review` |
| About | `iconnect://about` |

Default enabled: **Devices**, **Chats**, **Share**, **Feedback**.

Quick-action types use the same `iconnect://` strings and are routed through the same parser as external URLs.

---

## Apple Shortcuts

**Open Transfers tab**

1. Add action **Open URL**
2. URL: `iconnect://transfers`

**Refresh nearby devices after joining Wi‑Fi**

```
iconnect://devices?refresh=1
```

Use **Open URL** in a Personal Automation (e.g. when Wi‑Fi connects) to jump to discovery and rescan.

---

## Launch behavior

When iConnect receives a URL (cold start or while running):

1. The link is parsed by `IConnectDeepLink`.
2. Tab switches animate immediately; **share**, **feedback**, and **review** open after a short delay (~0.4 s on iOS) so the UI can finish mounting.
3. **Feedback** uses in-app Mail when available; otherwise opens the default mail client via `mailto:`.
4. **Share** on Mac uses the system share picker; on iOS it presents a share sheet.

---

## Troubleshooting

| Issue | What to check |
|-------|----------------|
| Link does nothing | Ensure iConnect is installed; host must match a supported name above |
| `feedback` opens Mail only | No Mail account configured on the device — expected fallback |
| `shortcuts` has no effect on Mac | Home Screen shortcut customization is **iOS-only** |
| URL does not connect to a device | Deep links only navigate — use the Devices tab to discover peers manually |

---

[Back to iConnect Support](..) · [FAQ](faq) · [Privacy Policy](privacy)

</section>

<section lang="zh-CN" markdown="1">

爱联（iConnect）支持 **`iconnect://`** URL Scheme 深度链接——可从 Safari、其他 App、书签或苹果快捷指令打开指定 Tab、设置页或应用内操作。这些 URL 与 iPhone / iPad 上 **主屏 Quick Actions**（长按图标）指向相同目的地。

> **说明：** URL 仅用于 **应用内导航**，不会自动连接设备、发起传输或打开某个聊天会话。

## 协议规范

```
iconnect://<host>
iconnect://<host>?refresh=1
```

| 规则 | 说明 |
|------|------|
| **Scheme** | `iconnect` |
| **Host / 路径** | 单段名称，**不区分大小写** — 从 URL **host** 或第一段 **path** 解析 |
| **别名** | 部分 host 支持同义词（见下表） |
| **Query** | 仅 **设备** 页支持 `refresh=1` / `refresh=true` 触发重新扫描 |

---

## Tab 入口

| URL | 打开 | 别名 |
|-----|------|------|
| `iconnect://devices` | **设备** Tab（雷达 / 发现） | `device` |
| `iconnect://devices?refresh=1` | **设备** Tab 并**刷新**附近设备 | — |
| `iconnect://chat` | **聊天** Tab | `messages` |
| `iconnect://transfers` | **传输** Tab | `transfer` |
| `iconnect://history` | **历史** Tab（传输记录） | — |
| `iconnect://settings` | **设置** Tab | `setting` |

**刷新发现**

```
iconnect://devices?refresh=1
iconnect://devices/refresh
```

---

## 设置子页面

以下链接会先进入 **设置**，再打开对应页面：

| URL | 打开 | 别名 |
|-----|------|------|
| `iconnect://about` | 关于 | — |
| `iconnect://usage` | 使用说明 | `guide`、`help`、`usageguide` |
| `iconnect://shortcuts` | 主屏快捷指令配置（iOS） | `homeshortcuts` |
| `iconnect://debug` | 调试 / 诊断信息 | `debuginfo` |

---

## 应用内操作

| URL | 打开 |
|-----|------|
| `iconnect://share` | 分享爱联（App Store 链接 + 推荐文案） |
| `iconnect://feedback` | 意见反馈邮件（无邮件账户时回退 `mailto:`） |
| `iconnect://review` | 应用内 App Store 评分 |

**评分别名：** `iconnect://rate`、`iconnect://rating`

---

## 示例

```
iconnect://chat
iconnect://transfers
iconnect://devices?refresh=1
iconnect://usage
iconnect://share
```

---

## 主屏 Quick Actions（iOS）

长按爱联图标。在 **设置 → 主屏快捷指令** 中最多选 **4** 项并排顺序。

| 快捷指令 | URL |
|----------|-----|
| 设备 | `iconnect://devices` |
| 聊天 | `iconnect://chat` |
| 传输 | `iconnect://transfers` |
| 历史 | `iconnect://history` |
| 分享 | `iconnect://share` |
| 反馈 | `iconnect://feedback` |
| 评分 | `iconnect://review` |
| 关于 | `iconnect://about` |

默认启用：**设备**、**聊天**、**分享**、**反馈**。

---

## 苹果快捷指令

**打开传输 Tab**

1. 添加 **打开 URL**
2. URL：`iconnect://transfers`

**连上 Wi‑Fi 后刷新附近设备**

```
iconnect://devices?refresh=1
```

可在个人自动化（例如「Wi‑Fi 连接时」）中使用 **打开 URL**。

---

## 启动行为

- Tab 切换立即执行；**分享**、**反馈**、**评分** 在 iOS 上约延迟 0.4 秒后弹出，以便界面完成加载。
- **反馈** 优先使用应用内邮件；否则打开系统邮件客户端。
- Mac 上 **分享** 使用系统分享面板。

---

## 常见问题

| 现象 | 处理 |
|------|------|
| 链接无反应 | 确认已安装爱联；host 须为上表支持名称 |
| `feedback` 只打开邮件 App | 设备未配置邮件账户 — 属正常回退 |
| Mac 上 `shortcuts` 无效 | 主屏快捷指令配置**仅 iOS** |
| URL 无法连接设备 | 深度链接仅导航 — 请在设备 Tab 手动发现 |

---

[返回爱联支持](..) · [常见问题](faq) · [隐私政策](privacy)

</section>

<section lang="zh-TW" markdown="1">

愛聯（iConnect）支援 **`iconnect://`** URL Scheme 深度連結——可從 Safari、其他 App、書籤或 Apple 捷徑開啟指定 Tab、設定頁或應用內操作。這些 URL 與 iPhone / iPad 上 **主畫面 Quick Actions**（長按圖示）指向相同目的地。

> **說明：** URL 僅用於 **應用內導覽**，不會自動連線裝置、發起傳輸或開啟某個聊天對話。

## 協定規範

```
iconnect://<host>
iconnect://<host>?refresh=1
```

| 規則 | 說明 |
|------|------|
| **Scheme** | `iconnect` |
| **Host / 路徑** | 單段名稱，**不區分大小寫** — 從 URL **host** 或第一段 **path** 解析 |
| **別名** | 部分 host 支援同義詞（見下表） |
| **Query** | 僅 **裝置** 頁支援 `refresh=1` / `refresh=true` 觸發重新掃描 |

---

## Tab 入口

| URL | 開啟 | 別名 |
|-----|------|------|
| `iconnect://devices` | **裝置** Tab（雷達 / 探索） | `device` |
| `iconnect://devices?refresh=1` | **裝置** Tab 並**刷新**附近裝置 | — |
| `iconnect://chat` | **聊天** Tab | `messages` |
| `iconnect://transfers` | **傳輸** Tab | `transfer` |
| `iconnect://history` | **歷史** Tab（傳輸紀錄） | — |
| `iconnect://settings` | **設定** Tab | `setting` |

**刷新探索**

```
iconnect://devices?refresh=1
iconnect://devices/refresh
```

---

## 設定子頁面

以下連結會先進入 **設定**，再開啟對應頁面：

| URL | 開啟 | 別名 |
|-----|------|------|
| `iconnect://about` | 關於 | — |
| `iconnect://usage` | 使用說明 | `guide`、`help`、`usageguide` |
| `iconnect://shortcuts` | 主畫面捷徑設定（iOS） | `homeshortcuts` |
| `iconnect://debug` | 偵錯 / 診斷資訊 | `debuginfo` |

---

## 應用內操作

| URL | 開啟 |
|-----|------|
| `iconnect://share` | 分享愛聯（App Store 連結 + 推薦文案） |
| `iconnect://feedback` | 意見回饋郵件（無郵件帳戶時回退 `mailto:`） |
| `iconnect://review` | 應用內 App Store 評分 |

**評分別名：** `iconnect://rate`、`iconnect://rating`

---

## 範例

```
iconnect://chat
iconnect://transfers
iconnect://devices?refresh=1
iconnect://usage
iconnect://share
```

---

## 主畫面 Quick Actions（iOS）

長按愛聯圖示。在 **設定 → 主畫面捷徑** 中最多選 **4** 項並排序。

| 捷徑 | URL |
|------|-----|
| 裝置 | `iconnect://devices` |
| 聊天 | `iconnect://chat` |
| 傳輸 | `iconnect://transfers` |
| 歷史 | `iconnect://history` |
| 分享 | `iconnect://share` |
| 回饋 | `iconnect://feedback` |
| 評分 | `iconnect://review` |
| 關於 | `iconnect://about` |

預設啟用：**裝置**、**聊天**、**分享**、**回饋**。

---

## Apple 捷徑

**開啟傳輸 Tab**

1. 新增 **打開 URL**
2. URL：`iconnect://transfers`

**連上 Wi‑Fi 後刷新附近裝置**

```
iconnect://devices?refresh=1
```

---

## 啟動行為

- Tab 切換立即執行；**分享**、**回饋**、**評分** 在 iOS 上約延遲 0.4 秒後彈出。
- **回饋** 優先使用應用內郵件；否則開啟系統郵件用戶端。
- Mac 上 **分享** 使用系統分享面板。

---

## 常見問題

| 現象 | 處理 |
|------|------|
| 連結無反應 | 確認已安裝愛聯；host 須為上表支援名稱 |
| `feedback` 只開啟郵件 App | 裝置未設定郵件帳戶 — 屬正常回退 |
| Mac 上 `shortcuts` 無效 | 主畫面捷徑設定**僅 iOS** |
| URL 無法連線裝置 | 深度連結僅導覽 — 請在裝置 Tab 手動探索 |

---

[返回愛聯支援](..) · [常見問題](faq) · [隱私政策](privacy)

</section>
