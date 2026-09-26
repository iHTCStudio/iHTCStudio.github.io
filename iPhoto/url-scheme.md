---
layout: doc
title: iPhoto — Shortcut Links
app_id: iPhoto
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: iphoto:// deep links and Shortcuts for iPhoto — capture, library, editor, guides, and settings.
---

<section lang="en" markdown="1">

iPhoto supports **`iphoto://`** deep links and **App Intents / Siri Shortcuts**. Links only navigate inside the app — they do not upload data.

## Scheme

```
iphoto://<host>[?query]
```

| Rule | Detail |
|------|--------|
| Scheme | `iphoto` |
| Empty | Opens the app’s default tab |
| Unknown hosts | Ignored safely |

---

## Tabs & navigation

| URL | Opens |
|-----|-------|
| `iphoto://library` | Library tab |
| `iphoto://capture` | Capture tab |
| `iphoto://settings` | Settings tab |
| `iphoto://search` | Search tab (iOS 18+) |
| `iphoto://recent-projects` | Library focused on recent work |

---

## Editor

| URL | Opens |
|-----|-------|
| `iphoto://editor?id=<projectID>` | Editor for the given project id |

---

## Guides & actions

| URL | Opens |
|-----|-------|
| `iphoto://usage-guide` | Usage guide |
| `iphoto://widget-guide` | Widget guide |
| `iphoto://shortcuts-guide` | Shortcuts guide |
| `iphoto://feature-guide` | Feature / onboarding replay |
| `iphoto://export-presets` | Export-related settings |
| `iphoto://feedback` | Feedback email |
| `iphoto://in-app-review` | In-app review prompt |

---

## Siri & Shortcuts

Built-in intents include:

- Open Capture
- Open Library
- Import Photos
- Open Settings

Add them in the Shortcuts app or invoke with Siri using the phrases shown in Shortcuts.

## Examples

```
iphoto://capture
iphoto://library
iphoto://editor?id=YOUR-PROJECT-ID
iphoto://widget-guide
```

[FAQ](faq) · [Privacy Policy](privacy) · [Back to iPhoto](./)

</section>

<section lang="zh-CN" markdown="1">

爱修图支持 **`iphoto://`** 深链与 **App Intents / Siri 快捷指令**。链接只用于应用内跳转——不会上传数据。

## 协议

```
iphoto://<host>[?query]
```

| 规则 | 说明 |
|------|------|
| Scheme | `iphoto` |
| 空路径 | 打开默认 Tab |
| 未知 host | 安全忽略 |

---

## 标签页与导航

| URL | 打开 |
|-----|------|
| `iphoto://library` | 资源库 |
| `iphoto://capture` | 拍摄 |
| `iphoto://settings` | 设置 |
| `iphoto://search` | 搜索（iOS 18+） |
| `iphoto://recent-projects` | 资源库并关注最近项目 |

---

## 编辑器

| URL | 打开 |
|-----|------|
| `iphoto://editor?id=<projectID>` | 指定项目的编辑器 |

---

## 指南与操作

| URL | 打开 |
|-----|------|
| `iphoto://usage-guide` | 使用指南 |
| `iphoto://widget-guide` | 小组件指南 |
| `iphoto://shortcuts-guide` | 快捷方式指南 |
| `iphoto://feature-guide` | 功能引导（重播） |
| `iphoto://export-presets` | 导出相关设置 |
| `iphoto://feedback` | 反馈邮件 |
| `iphoto://in-app-review` | 应用内评分 |

---

## Siri 与快捷指令

内置意图包括：

- 打开拍摄
- 打开资源库
- 导入照片
- 打开设置

可在「快捷指令」App 中添加，或用 Siri 按短语唤起。

## 示例

```
iphoto://capture
iphoto://library
iphoto://editor?id=YOUR-PROJECT-ID
iphoto://widget-guide
```

[常见问题](faq) · [隐私政策](privacy) · [返回爱修图](./)

</section>

<section lang="zh-TW" markdown="1">

愛修圖支援 **`iphoto://`** 深鏈與 **App Intents / Siri 捷徑**。連結只用於應用內跳轉——不會上傳資料。

## 協定

```
iphoto://<host>[?query]
```

| 規則 | 說明 |
|------|------|
| Scheme | `iphoto` |
| 空路徑 | 打開預設 Tab |
| 未知 host | 安全忽略 |

---

## 標籤頁與導覽

| URL | 打開 |
|-----|------|
| `iphoto://library` | 資源庫 |
| `iphoto://capture` | 拍攝 |
| `iphoto://settings` | 設定 |
| `iphoto://search` | 搜尋（iOS 18+） |
| `iphoto://recent-projects` | 資源庫並關注最近項目 |

---

## 編輯器

| URL | 打開 |
|-----|------|
| `iphoto://editor?id=<projectID>` | 指定項目的編輯器 |

---

## 指南與操作

| URL | 打開 |
|-----|------|
| `iphoto://usage-guide` | 使用指南 |
| `iphoto://widget-guide` | 小工具指南 |
| `iphoto://shortcuts-guide` | 捷徑指南 |
| `iphoto://feature-guide` | 功能引導（重播） |
| `iphoto://export-presets` | 匯出相關設定 |
| `iphoto://feedback` | 回饋郵件 |
| `iphoto://in-app-review` | 應用內評分 |

---

## Siri 與捷徑

內建意圖包括：

- 打開拍攝
- 打開資源庫
- 匯入照片
- 打開設定

可在「捷徑」App 中添加，或用 Siri 按短語喚起。

## 範例

```
iphoto://capture
iphoto://library
iphoto://editor?id=YOUR-PROJECT-ID
iphoto://widget-guide
```

[常見問題](faq) · [隱私政策](privacy) · [返回愛修圖](./)

</section>
