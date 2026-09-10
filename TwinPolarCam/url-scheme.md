---
layout: doc
title: TwinPolarCam — Shortcut Links
app_id: TwinPolarCam
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: twinpolarcam:// deep links — guides, settings, pending exports, feedback, and Live Activity return.
last_updated: 2026-07-11
---

<section lang="en" markdown="1">

TwinPolarCam supports **`twinpolarcam://`** shortcut links. Use them in **Safari bookmarks**, the **Shortcuts** app, or from **Home Screen quick actions** and **Spotlight** to jump directly into guides and key screens.

## Link format

```
twinpolarcam://{host}
```

There is no path or query component — routing is by **host name only** (case-insensitive).

---

## Guides

| URL | Opens |
|-----|-------|
| `twinpolarcam://usage-guide` | **How to Use** guide sheet |
| `twinpolarcam://recording-guide` | **Recording & Reliability** guide sheet |
| `twinpolarcam://export-guide` | **Export & Pending** guide sheet |
| `twinpolarcam://feature-guide` | **Feature Tour** (6-page onboarding replay) |

Same destinations as **App Settings → Help**.

---

## App screens

| URL | Opens |
|-----|-------|
| `twinpolarcam://settings` | App Settings panel |
| `twinpolarcam://pending` | Pending Exports manager |
| `twinpolarcam://feedback` | Send Feedback (Mail composer) |
| `twinpolarcam://recording` | Main app (Live Activity / Dynamic Island return) |

---

## Home Screen quick actions

**Long-press the TwinPolarCam icon** — four fixed shortcuts (same hosts as above):

| Quick action | URL |
|--------------|-----|
| Usage Guide | `twinpolarcam://usage-guide` |
| Recording Tips | `twinpolarcam://recording-guide` |
| Export Guide | `twinpolarcam://export-guide` |
| Feature Tour | `twinpolarcam://feature-guide` |

Quick actions work on **cold launch** and when the app is already running. If onboarding hasn't completed yet, the link is **queued** and delivered after you finish the welcome guide.

---

## Spotlight

TwinPolarCam indexes guide pages in **Spotlight**. Search for:

- TwinPolarCam
- Usage Guide / Recording & Reliability / Export & Pending / Feature Tour

Tapping a result opens the matching guide sheet.

---

## Notes

- **Unsupported devices** can still open guide links from the unsupported screen — useful for reading requirements before refund.
- Unknown hosts are **ignored safely** (no crash).
- Guides require the main UI to be ready; cold-start URLs are buffered until initialization completes.

[User Guide](index) · [FAQ](faq) · [Privacy Policy](privacy)

</section>

<section lang="zh-CN" markdown="1">

太极双摄支持 **`twinpolarcam://`** 快捷链接。可用于 **Safari 书签**、**快捷指令**、**主屏长按菜单** 和 **Spotlight**，直达教程与关键界面。

## 链接格式

```
twinpolarcam://{host}
```

仅通过 **host** 路由（不区分大小写），无 path/query。

---

## 教程

| 链接 | 打开 |
|------|------|
| `twinpolarcam://usage-guide` | **使用说明** |
| `twinpolarcam://recording-guide` | **录制与可靠性** |
| `twinpolarcam://export-guide` | **导出与待导出** |
| `twinpolarcam://feature-guide` | **功能导览**（6 页引导重播） |

与 **应用设置 → 帮助** 中入口一致。

---

## 应用界面

| 链接 | 打开 |
|------|------|
| `twinpolarcam://settings` | 应用设置 |
| `twinpolarcam://pending` | 待导出管理 |
| `twinpolarcam://feedback` | 发送反馈（邮件） |
| `twinpolarcam://recording` | 返回主界面（Live Activity / 灵动岛） |

---

## 主屏快捷操作

**长按 App 图标** — 四项固定快捷菜单：

| 菜单 | 链接 |
|------|------|
| 使用说明 | `twinpolarcam://usage-guide` |
| 录制技巧 | `twinpolarcam://recording-guide` |
| 导出指南 | `twinpolarcam://export-guide` |
| 功能导览 | `twinpolarcam://feature-guide` |

冷启动与 App 已打开时均可用。若欢迎引导未完成，链接会 **排队**，完成引导后自动打开。

---

## Spotlight

可在 Spotlight 搜索 **太极双摄** 或教程标题，点按打开对应教程 sheet。

---

## 说明

- **不支持设备** 仍可从说明页打开教程链接，便于了解要求或退款前阅读。
- 未知 host **安全忽略**。
- 冷启动时 URL 会缓冲至主界面就绪。

[使用指南](index) · [常见问题](faq) · [隐私政策](privacy)

</section>

<section lang="zh-TW" markdown="1">

太極雙攝支援 **`twinpolarcam://`** 快捷連結。可用於 **Safari 書籤**、**捷徑**、**主畫面長按選單** 與 **Spotlight**。

## 連結格式

```
twinpolarcam://{host}
```

僅以 **host** 路由（不分大小寫）。

---

## 教學

| 連結 | 開啟 |
|------|------|
| `twinpolarcam://usage-guide` | **使用說明** |
| `twinpolarcam://recording-guide` | **錄製與可靠性** |
| `twinpolarcam://export-guide` | **匯出與待匯出** |
| `twinpolarcam://feature-guide` | **功能導覽** |

同 **應用設定 → 幫助**。

---

## 應用介面

| 連結 | 開啟 |
|------|------|
| `twinpolarcam://settings` | 應用設定 |
| `twinpolarcam://pending` | 待匯出管理 |
| `twinpolarcam://feedback` | 發送回饋 |
| `twinpolarcam://recording` | 返回主畫面（Live Activity） |

---

## 主畫面快捷操作

長按圖示四項固定選單（同上 host）。歡迎引導未完成時連結 **排隊** 後開啟。

---

## Spotlight

可搜尋 App 名稱或教學標題開啟對應 sheet。

[使用指南](index) · [常見問題](faq) · [隱私政策](privacy)

</section>
