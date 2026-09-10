---
layout: doc
title: Weber — FAQ
app_id: Weber
doc_title_en: Frequently Asked Questions
doc_title_zh_cn: 常见问题
doc_title_zh_tw: 常見問題
description: Frequently asked questions about Weber.
---

<section lang="en" markdown="1">

### How do I enable the Weber extension in Safari?

Open the Weber host app from your Applications folder once, then go to **Safari → Settings → Extensions** (or **Safari → Preferences → Extensions** on older macOS) and check the box next to **Weber**. The Weber icon should then appear in the Safari toolbar. If you do not see it, right-click the toolbar and choose "Customize Toolbar" to add it.

### Where do I change Weber settings?

In the **Safari toolbar popup** — click the Weber icon next to the address bar. Speed, presets, language and always-autospeed are configured there. The Mac App Store host app is only for installing and enabling the extension, not for day-to-day settings.

### How does speed control work?

Click the Weber icon in the Safari toolbar to open the popup. You can adjust the video playback speed using the slider, type a specific value in the numeric input field, or tap one of the preset buttons (0.5x / 1x / 1.5x / 2x / 3x). The speed range is 0.1x to 100x. Your chosen speed is saved automatically and remembered across pages and browser sessions.

### What is always-autospeed mode?

By default, Weber uses **lazy injection** — the content script is injected only when you open the popup, so no broad website access is needed. If you enable **always-autospeed mode**, Weber requests optional website access permission and automatically applies your saved speed to every page as it loads, without needing to open the popup each time.

### Why doesn't speed control work on some videos?

Weber controls standard HTML5 `<video>` elements. Videos that are rendered via Canvas or WebGL, embedded inside a closed Shadow DOM, or delivered through proprietary player frameworks that do not expose a standard `<video>` element may not be detected. Additionally, some websites programmatically reset the playback rate, which can override Weber's setting.

### How does "Copy as Markdown Format" work?

Right-click on any page, selected text, or link and choose **"Copy as Markdown Format"** from the context menu. Weber will copy the content in Markdown syntax to your clipboard:

- **On a page (no selection):** Copies `[Page Title](URL)`.
- **On selected text:** Copies `[Selected Text](URL)`.
- **On a link:** Copies `[Link Text](Link URL)`.

### What permissions does Weber require and why?

| Permission | Purpose |
|------------|---------|
| storage | Save your speed preference locally in the browser |
| tabs | Read the current tab's URL and title for Markdown copy |
| activeTab | Inject the speed-control script into the active tab |
| contextMenus | Add the "Copy as Markdown Format" right-click menu item |
| scripting | Programmatically inject content scripts |
| optional_host_permissions | Only requested if you enable always-autospeed mode |

All permissions are used solely for the stated purposes. No data is transmitted externally.

### Does Weber support dark mode?

Yes. Weber's popup interface automatically adapts to your macOS appearance setting. If your Mac is in dark mode, the popup will use a dark theme; if in light mode, it will use a light theme.

### What languages does the extension UI support?

The **toolbar popup** is available in **English** and **Simplified Chinese (简体中文)**. Switch language from the popup settings.

### Does Weber run on iPhone or iPad?

No. Weber is a **macOS-only** Safari Web Extension. It requires Safari on Mac (macOS 12.0+).

### Still need help?

Contact us at [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) and we will get back to you within 48 hours.

</section>

<section lang="zh-CN" markdown="1">

### 如何在 Safari 中启用 Weber 扩展？

从应用程序文件夹打开一次 Weber 宿主应用，然后前往 **Safari → 设置 → 扩展**（旧版 macOS 为 **Safari → 偏好设置 → 扩展**），勾选 **Weber**。Weber 图标会出现在 Safari 工具栏中。如果看不到，请右键点击工具栏并选择"自定义工具栏"来添加。

### 在哪里更改 Weber 设置？

在 **Safari 工具栏弹出窗口** 中——点击地址栏旁的 Weber 图标。速度、预设、语言与始终自动调速均在此配置。Mac App Store 宿主应用仅用于安装与启用扩展，不是日常设置界面。

### 速度控制是如何工作的？

点击 Safari 工具栏中的 Weber 图标打开弹出窗口。你可以通过滑块调整视频播放速度、在数字输入框中输入特定值，或点击预设按钮（0.5x / 1x / 1.5x / 2x / 3x）。速度范围为 0.1x 到 100x。你选择的速度会自动保存，并在跨页面和跨浏览器会话中持久保留。

### 什么是始终自动调速模式？

默认情况下，Weber 使用**懒注入**模式 — 内容脚本仅在你打开弹出窗口时注入，无需广泛的网站访问权限。如果你启用**始终自动调速模式**，Weber 会请求可选的网站访问权限，并在每个页面加载时自动应用你保存的速度，无需每次都打开弹出窗口。

### 为什么某些视频无法控制速度？

Weber 控制标准的 HTML5 `<video>` 元素。通过 Canvas 或 WebGL 渲染的视频、嵌入在封闭 Shadow DOM 内的视频，或使用不暴露标准 `<video>` 元素的专有播放器框架的视频可能无法被检测到。此外，某些网站会以编程方式重置播放速率，这可能会覆盖 Weber 的设置。

### 「复制为 Markdown 格式」如何使用？

在任意页面、选中的文本或链接上右键点击，从右键菜单中选择**「复制为 Markdown 格式」**。Weber 会将内容以 Markdown 语法复制到剪贴板：

- **在页面上（无选中内容）：** 复制 `[页面标题](URL)`。
- **选中文本时：** 复制 `[选中的文本](URL)`。
- **在链接上：** 复制 `[链接文字](链接 URL)`。

### Weber 需要哪些权限，为什么？

| 权限 | 用途 |
|------------|---------|
| storage | 在浏览器中本地保存你的速度偏好 |
| tabs | 读取当前标签页的 URL 和标题以用于 Markdown 复制 |
| activeTab | 将速度控制脚本注入活动标签页 |
| contextMenus | 添加「复制为 Markdown 格式」右键菜单项 |
| scripting | 以编程方式注入内容脚本 |
| optional_host_permissions | 仅在你启用始终自动调速模式时请求 |

所有权限仅用于上述目的。不会向外部传输任何数据。

### Weber 支持深色模式吗？

支持。Weber 的弹出窗口界面会自动适配你的 macOS 外观设置。Mac 处于深色模式时弹出窗口使用深色主题，浅色模式时使用浅色主题。

### 扩展界面支持哪些语言？

**工具栏弹出窗口** 支持 **英文** 与 **简体中文**。可在弹出窗口设置中切换语言。

### Weber 能在 iPhone 或 iPad 上使用吗？

不能。Weber 是 **仅限 macOS** 的 Safari Web Extension，需要 Mac 版 Safari（macOS 12.0+）。

### 仍需帮助？

发邮件到 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)，我们会在 48 小时内回复。

</section>

<section lang="zh-TW" markdown="1">

### 如何在 Safari 中啟用 Weber 擴充功能？

從應用程式資料夾開啟一次 Weber 宿主應用，然後前往 **Safari → 設定 → 擴充功能**（舊版 macOS 為 **Safari → 偏好設定 → 擴充功能**），勾選 **Weber**。Weber 圖示會出現在 Safari 工具列中。如果看不到，請右鍵點按工具列並選擇「自訂工具列」來新增。

### 在哪裡變更 Weber 設定？

在 **Safari 工具列彈出視窗** 中——點按網址列旁的 Weber 圖示。速度、預設、語言與始終自動調速均在此設定。Mac App Store 宿主應用僅用於安裝與啟用延伸功能，不是日常設定介面。

### 速度控制是如何運作的？

點按 Safari 工具列中的 Weber 圖示開啟彈出視窗。你可以透過滑桿調整影片播放速度、在數字輸入框中輸入特定值，或點按預設按鈕（0.5x / 1x / 1.5x / 2x / 3x）。速度範圍為 0.1x 到 100x。你選擇的速度會自動儲存，並在跨頁面和跨瀏覽器工作階段中持久保留。

### 什麼是始終自動調速模式？

預設情況下，Weber 使用**延遲注入**模式 — 內容腳本僅在你開啟彈出視窗時注入，無需廣泛的網站存取權限。如果你啟用**始終自動調速模式**，Weber 會請求選用的網站存取權限，並在每個頁面載入時自動套用你儲存的速度，無需每次都開啟彈出視窗。

### 為什麼某些影片無法控制速度？

Weber 控制標準的 HTML5 `<video>` 元素。透過 Canvas 或 WebGL 繪製的影片、嵌入在封閉 Shadow DOM 內的影片，或使用不公開標準 `<video>` 元素的專有播放器框架的影片可能無法被偵測到。此外，某些網站會以程式方式重設播放速率，這可能會覆蓋 Weber 的設定。

### 「複製為 Markdown 格式」如何使用？

在任意頁面、選取的文字或連結上右鍵點按，從右鍵選單中選擇**「複製為 Markdown 格式」**。Weber 會將內容以 Markdown 語法複製到剪貼簿：

- **在頁面上（無選取內容）：** 複製 `[頁面標題](URL)`。
- **選取文字時：** 複製 `[選取的文字](URL)`。
- **在連結上：** 複製 `[連結文字](連結 URL)`。

### Weber 需要哪些權限，為什麼？

| 權限 | 用途 |
|------------|---------|
| storage | 在瀏覽器中本地儲存你的速度偏好 |
| tabs | 讀取目前標籤頁的 URL 和標題以用於 Markdown 複製 |
| activeTab | 將速度控制腳本注入使用中的標籤頁 |
| contextMenus | 新增「複製為 Markdown 格式」右鍵選單項目 |
| scripting | 以程式方式注入內容腳本 |
| optional_host_permissions | 僅在你啟用始終自動調速模式時請求 |

所有權限僅用於上述目的。不會向外部傳送任何資料。

### Weber 支援深色模式嗎？

支援。Weber 的彈出視窗介面會自動適配你的 macOS 外觀設定。Mac 處於深色模式時彈出視窗使用深色主題，淺色模式時使用淺色主題。

### 延伸功能介面支援哪些語言？

**工具列彈出視窗** 支援 **英文** 與 **簡體中文**。可在彈出視窗設定中切換語言。

### Weber 能在 iPhone 或 iPad 上使用嗎？

不能。Weber 是 **僅限 macOS** 的 Safari Web Extension，需要 Mac 版 Safari（macOS 12.0+）。

### 仍需協助？

寄信到 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)，我們會在 48 小時內回覆。

</section>
