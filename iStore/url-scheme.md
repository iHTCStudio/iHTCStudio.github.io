---
layout: doc
title: iStore — Shortcut Links
app_id: iStore
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: istore:// shortcut links — switch a region, switch last, open tabs, availability check, guides, and Siri & Shortcuts.
---

<section lang="en" markdown="1">

iStore supports **`istore://`** shortcut links. Use them in **Shortcuts**, Safari bookmarks, or from **widgets**, **Control Center**, **Spotlight**, and the **Share Extension** to **switch a region**, **re-switch your last region**, **open a tab**, or **jump to a guide**.

## Link format

```
istore://{host}?{params}
```

Hosts are **case-insensitive**. Region codes use standard **Alpha-2** values (`us`, `cn`, `jp`, `hk`, `tw`, …).

| What you want | Link |
|---------------|------|
| Switch to a region | `istore://switch?region={code}` |
| Switch to your last region | `istore://switch-last` |
| Open the Store / Favorites / Settings tab | `istore://store` · `istore://favorites` · `istore://settings` |
| Open App Availability | `istore://availability` |

---

## Switch to a region

Requests a switch to the given region (routed through the in-app confirmation, if enabled).

```
istore://switch?region={code}
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `region` | **Yes** | Region code, e.g. `us`, `cn`, `jp`, `hk`, `tw` |

**Example**

```
istore://switch?region=us
```

Used by: **interactive widgets**, **Spotlight** results, and **Shortcuts / Siri**.

---

## Switch to your last region

```
istore://switch-last
```

Reads your most recent switch target and switches to it again. Powers the **Switch Last** Control Center control (iOS 18+) and the matching Shortcut / Siri action.

---

## Tabs & pages (no query)

| URL | Opens |
|-----|-------|
| `istore://store` | Store tab |
| `istore://favorites` | Favorites tab |
| `istore://settings` | Settings tab |
| `istore://availability` | Settings → App Availability (also used by the Share Extension) |
| `istore://switch-history` | Switch History |
| `istore://quick-regions` | Quick Regions settings |
| `istore://feature-guide` | Feature guide |
| `istore://widget-guide` | Widget guide |
| `istore://shortcuts-guide` | Shortcuts guide |
| `istore://usage-guide` | Usage guide |
| `istore://feedback` | Feedback email |
| `istore://in-app-review` | In-app App Store rating |

---

## Widgets, Control Center & Spotlight

These generate `istore://` links automatically when you tap:

| Source | Tap target | Effect |
|--------|------------|--------|
| **Quick Regions / Recent / Custom widget** | A region tile | `istore://switch?region=…` |
| **Switch Last control** (iOS 18+) | The control | `istore://switch-last` |
| **Spotlight** | A region result | `istore://switch?region=…` |

Interactive switching from widgets and Control Center opens the app to complete the official App Store redirect.

---

## Share Extension

Share any **App Store link** into iStore. The Share Extension checks availability across popular regions, then can open the app via `istore://availability` so you can review the result and switch.

---

## Siri & Shortcuts

Find built-in actions in the **Shortcuts** app or ask **Siri**. Titles and phrases are localized in English / 简体中文 / 繁體中文.

| Action | What you can set | Effect |
|--------|------------------|--------|
| Switch region | Region | Switches to that region |
| Switch last region | — | Switches to your last target |
| Switch favorite region | A favorite | Switches to a favorited region |
| Open store | — | Opens iStore |
| Check availability | App link or ID | Checks where the app is available |

---

## Region codes in links

Deep links and widget-generated URLs always use stable **region codes** (`us`, `cn`, `hk`, `tw`, …) — not localized display names.

**Examples**

```
istore://switch?region=jp
istore://switch?region=hk
```

[Back to overview](..) · [FAQ](faq) · [Privacy](privacy)

</section>

<section lang="zh-CN" markdown="1">

爱商店支持 **`istore://`** 快捷链接。可在**快捷指令**、Safari 书签，或从**小组件**、**控制中心**、**Spotlight** 与**分享扩展**中用来**切换地区**、**再次切换上次地区**、**打开某个 Tab** 或**直达指南**。

## 链接格式

```
istore://{host}?{参数}
```

Host **不区分大小写**。地区代码使用标准 **Alpha-2** 值（`us`、`cn`、`jp`、`hk`、`tw` 等）。

| 目的 | 链接 |
|------|------|
| 切换到某地区 | `istore://switch?region={代码}` |
| 切换到上次地区 | `istore://switch-last` |
| 打开 商店 / 收藏 / 设置 Tab | `istore://store` · `istore://favorites` · `istore://settings` |
| 打开上架查询 | `istore://availability` |

---

## 切换到某地区

请求切换到指定地区（若已开启，会经过 App 内确认）。

```
istore://switch?region={代码}
```

| 参数 | 必填 | 说明 |
|------|------|------|
| `region` | **是** | 地区代码，如 `us`、`cn`、`jp`、`hk`、`tw` |

**示例**

```
istore://switch?region=us
```

用于：**交互式小组件**、**Spotlight** 结果、**快捷指令 / Siri**。

---

## 切换到上次地区

```
istore://switch-last
```

读取你最近的切换目标并再次切换。驱动**切换上次**控制中心控件（iOS 18+）与对应的快捷指令 / Siri 操作。

---

## Tab 与页面（无 query）

| 链接 | 打开 |
|------|------|
| `istore://store` | 商店 Tab |
| `istore://favorites` | 收藏 Tab |
| `istore://settings` | 设置 Tab |
| `istore://availability` | 设置 → 上架查询（分享扩展也会用到） |
| `istore://switch-history` | 切换历史 |
| `istore://quick-regions` | 常用地区设置 |
| `istore://feature-guide` | 功能引导 |
| `istore://widget-guide` | 小组件指南 |
| `istore://shortcuts-guide` | 快捷指令指南 |
| `istore://usage-guide` | 使用说明 |
| `istore://feedback` | 意见反馈 |
| `istore://in-app-review` | 应用内评分 |

---

## 小组件、控制中心与 Spotlight

点击时自动生成 `istore://` 链接：

| 来源 | 点击目标 | 效果 |
|------|----------|------|
| **常用 / 最近 / 自定义小组件** | 地区磁贴 | `istore://switch?region=…` |
| **切换上次控件**（iOS 18+） | 控件本身 | `istore://switch-last` |
| **Spotlight** | 地区结果 | `istore://switch?region=…` |

从小组件与控制中心进行的交互式切换会打开 App，以完成 App Store 官方跳转。

---

## 分享扩展

把任意 **App Store 链接**分享到爱商店。分享扩展会查询常用地区的上架情况，随后可通过 `istore://availability` 打开 App，让你查看结果并切换。

---

## Siri 与快捷指令

在**快捷指令** App 中添加内置操作，或对 **Siri** 说出指令。标题与短语已本地化为 英文 / 简体中文 / 繁體中文。

| 操作 | 可设置内容 | 效果 |
|------|------------|------|
| 切换地区 | 地区 | 切换到该地区 |
| 切换上次地区 | — | 切换到上次目标 |
| 切换收藏地区 | 某收藏 | 切换到已收藏地区 |
| 打开商店 | — | 打开爱商店 |
| 查询上架 | App 链接或 ID | 查询该 App 的上架地区 |

---

## 链接中的地区代码

快捷链接与小组件生成的 URL 始终使用稳定的**地区代码**（`us`、`cn`、`hk`、`tw` 等），而非本地化显示名称。

**示例**

```
istore://switch?region=jp
istore://switch?region=hk
```

[返回概览](..) · [常见问题](faq) · [隐私政策](privacy)

</section>

<section lang="zh-TW" markdown="1">

愛商店支援 **`istore://`** 快捷連結。可在**捷徑**、Safari 書籤，或從**小工具**、**控制中心**、**Spotlight** 與**分享延伸功能**中用來**切換地區**、**再次切換上次地區**、**開啟某個 Tab** 或**直達指南**。

## 連結格式

```
istore://{host}?{參數}
```

Host **不區分大小寫**。地區代碼使用標準 **Alpha-2** 值（`us`、`cn`、`jp`、`hk`、`tw` 等）。

| 目的 | 連結 |
|------|------|
| 切換到某地區 | `istore://switch?region={代碼}` |
| 切換到上次地區 | `istore://switch-last` |
| 開啟 商店 / 收藏 / 設定 Tab | `istore://store` · `istore://favorites` · `istore://settings` |
| 開啟上架查詢 | `istore://availability` |

---

## 切換到某地區

請求切換到指定地區（若已開啟，會經過 App 內確認）。

```
istore://switch?region={代碼}
```

| 參數 | 必填 | 說明 |
|------|------|------|
| `region` | **是** | 地區代碼，如 `us`、`cn`、`jp`、`hk`、`tw` |

**範例**

```
istore://switch?region=us
```

用於：**互動式小工具**、**Spotlight** 結果、**捷徑 / Siri**。

---

## 切換到上次地區

```
istore://switch-last
```

讀取你最近的切換目標並再次切換。驅動**切換上次**控制中心控制項（iOS 18+）與對應的捷徑 / Siri 操作。

---

## Tab 與頁面（無 query）

| 連結 | 開啟 |
|------|------|
| `istore://store` | 商店 Tab |
| `istore://favorites` | 收藏 Tab |
| `istore://settings` | 設定 Tab |
| `istore://availability` | 設定 → 上架查詢（分享延伸功能也會用到） |
| `istore://switch-history` | 切換歷史 |
| `istore://quick-regions` | 常用地區設定 |
| `istore://feature-guide` | 功能引導 |
| `istore://widget-guide` | 小工具指南 |
| `istore://shortcuts-guide` | 捷徑指南 |
| `istore://usage-guide` | 使用說明 |
| `istore://feedback` | 意見回饋 |
| `istore://in-app-review` | 應用內評分 |

---

## 小工具、控制中心與 Spotlight

點擊時自動產生 `istore://` 連結：

| 來源 | 點擊目標 | 效果 |
|------|----------|------|
| **常用 / 最近 / 自訂小工具** | 地區磁貼 | `istore://switch?region=…` |
| **切換上次控制項**（iOS 18+） | 控制項本身 | `istore://switch-last` |
| **Spotlight** | 地區結果 | `istore://switch?region=…` |

從小工具與控制中心進行的互動式切換會開啟 App，以完成 App Store 官方跳轉。

---

## 分享延伸功能

把任意 **App Store 連結**分享到愛商店。分享延伸功能會查詢常用地區的上架情況，隨後可透過 `istore://availability` 開啟 App，讓你查看結果並切換。

---

## Siri 與捷徑

在**捷徑** App 中新增內建操作，或對 **Siri** 說出指令。標題與短語已本地化為 英文 / 简体中文 / 繁體中文。

| 操作 | 可設定內容 | 效果 |
|------|------------|------|
| 切換地區 | 地區 | 切換到該地區 |
| 切換上次地區 | — | 切換到上次目標 |
| 切換收藏地區 | 某收藏 | 切換到已收藏地區 |
| 開啟商店 | — | 開啟愛商店 |
| 查詢上架 | App 連結或 ID | 查詢該 App 的上架地區 |

---

## 連結中的地區代碼

快捷連結與小工具產生的 URL 始終使用穩定的**地區代碼**（`us`、`cn`、`hk`、`tw` 等），而非本地化顯示名稱。

**範例**

```
istore://switch?region=jp
istore://switch?region=hk
```

[返回概覽](..) · [常見問題](faq) · [隱私政策](privacy)

</section>
