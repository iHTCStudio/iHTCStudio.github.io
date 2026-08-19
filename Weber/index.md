---
layout: app
title: Weber — Support
app_id: Weber
description: macOS Safari Web Extension for video speed control and Markdown copy.
---

<section lang="en" markdown="1">

Weber is a **macOS-only** Safari Web Extension that gives you precise control over HTML5 video playback speed and lets you copy any web page or link as Markdown with a single right-click. **Lightweight, privacy-friendly, and built for Safari on Mac.**

The **host app** from the Mac App Store registers the extension. Day-to-day controls — speed slider, presets, language and always-autospeed — live in the **Safari toolbar popup**, not inside the host app window.

## Getting Started

1. Download Weber from the Mac App Store and open the host app once to register the extension.
2. Open **Safari → Settings → Extensions** (or **Safari → Preferences → Extensions** on older macOS).
3. Check the box next to **Weber** to enable the extension.
4. Add the Weber icon to the Safari toolbar if needed (right-click the toolbar → Customize Toolbar).
5. Click the **Weber icon in the Safari toolbar** to open the popup — adjust speed, presets, and language here.
6. Optional: enable **always-autospeed** in the popup and grant website access when prompted.

## Features

- **Precise Speed Control** — 0.1×–100× via slider, numeric input, or presets (0.5× / 1× / 1.5× / 2× / 3×).
- **Lazy Injection (Default)** — Script injects only when you open the popup; no broad website access required.
- **Always-Autospeed Mode** — Optional permission so your preferred speed applies on every page load.
- **Speed Memory** — Preference persists via `browser.storage.local` across pages and sessions.
- **Dynamic Video Detection** — MutationObserver covers newly added `<video>` elements.
- **Copy as Markdown** — Context menu for page / selection / link → `[text](url)`.
- **Extension UI Languages** — Toolbar popup in **English** and **Simplified Chinese** (host marketing site is also Traditional Chinese).
- **Light & Dark Mode** — Popup follows macOS appearance.
- **Minimal Host App** — Install / enable the extension; settings stay in Safari.

## Known Limitations

- Works with standard HTML5 `<video>` only — Canvas / WebGL / closed Shadow DOM players may not respond.
- Some sites reset `playbackRate` in script and can override Weber.
- Effective max speed may be lower than 100× depending on codec / Safari.
- **Mac only** — not available on iPhone, iPad, or other browsers.

## System Requirements

| Platform | Minimum Version |
|----------|-----------------|
| Mac (Safari) | macOS 12.0+ |

## Contact Us

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

We typically respond within 48 hours.

[FAQ](faq) · [Privacy Policy](privacy)

</section>

<section lang="zh-CN" markdown="1">

Weber 是一款 **仅限 macOS** 的 Safari 浏览器扩展，可精确控制 HTML5 视频播放速度，还能通过右键菜单一键将网页或链接复制为 Markdown 格式。**轻量、注重隐私、专为 Mac 版 Safari 打造。**

Mac App Store 中的 **宿主应用** 用于注册扩展。日常操作——速度滑块、预设、语言与始终自动调速——均在 **Safari 工具栏弹出窗口** 中完成，不在宿主应用窗口内。

## 快速上手

1. 从 Mac App Store 下载 Weber 并打开宿主应用一次以注册扩展。
2. 打开 **Safari → 设置 → 扩展**（旧版 macOS 为 **Safari → 偏好设置 → 扩展**）。
3. 勾选 **Weber** 以启用扩展。
4. 如需要，将 Weber 图标添加到 Safari 工具栏（右键工具栏 → 自定义工具栏）。
5. 点击 **Safari 工具栏中的 Weber 图标**打开弹出窗口——在此调节速度、预设与语言。
6. 可选：在弹出窗口开启**始终自动调速**，并在提示时授予网站访问权限。

## 功能特性

- **精确速度控制** — 0.1×–100×，滑块 / 数字输入 / 预设（0.5× / 1× / 1.5× / 2× / 3×）。
- **懒注入（默认）** — 仅在打开弹出窗口时注入脚本，无需广泛网站权限。
- **始终自动调速** — 可选授权后，每个页面加载自动应用偏好速度。
- **速度记忆** — 经 `browser.storage.local` 跨页面与会话保存。
- **动态视频检测** — MutationObserver 覆盖动态插入的 `<video>`。
- **复制为 Markdown** — 右键菜单支持页面 / 选中文本 / 链接 → `[text](url)`。
- **扩展界面语言** — 弹出窗口支持 **英文** 与 **简体中文**（官网另有繁体文案）。
- **亮色与深色** — 跟随 macOS 外观。
- **精简宿主应用** — 负责安装与启用扩展；日常设置在 Safari 中完成。

## 已知限制

- 仅标准 HTML5 `<video>`；Canvas / WebGL / 封闭 Shadow DOM 播放器可能无效。
- 部分网站会脚本重置 `playbackRate`，可能覆盖 Weber。
- 实际最高倍率可能低于 100×，取决于编解码器与 Safari。
- **仅限 Mac** — 不支持 iPhone、iPad 或其他浏览器。

## 系统要求

| 平台 | 最低版本 |
|------|----------|
| Mac（Safari）| macOS 12.0+ |

## 联系我们

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

我们通常在 48 小时内回复。

[常见问题](faq) · [隐私政策](privacy)

</section>

<section lang="zh-TW" markdown="1">

Weber 是一款 **僅限 macOS** 的 Safari 延伸功能，可精確控制 HTML5 影片播放速度，還能透過右鍵選單一鍵將網頁或連結複製為 Markdown 格式。**輕量、注重隱私、專為 Mac 版 Safari 打造。**

Mac App Store 中的 **宿主應用** 用於註冊延伸功能。日常操作——速度滑桿、預設、語言與始終自動調速——均在 **Safari 工具列彈出視窗** 中完成，不在宿主應用視窗內。

## 快速上手

1. 從 Mac App Store 下載 Weber 並開啟宿主應用一次以註冊延伸功能。
2. 開啟 **Safari → 設定 → 擴充功能**（舊版 macOS 為 **Safari → 偏好設定 → 擴充功能**）。
3. 勾選 **Weber** 以啟用延伸功能。
4. 如需要，將 Weber 圖示新增到 Safari 工具列（右鍵工具列 → 自訂工具列）。
5. 點按 **Safari 工具列中的 Weber 圖示**開啟彈出視窗——在此調節速度、預設與語言。
6. 可選：在彈出視窗開啟**始終自動調速**，並在提示時授予網站存取權限。

## 功能特色

- **精確速度控制** — 0.1×–100×，滑桿 / 數字輸入 / 預設（0.5× / 1× / 1.5× / 2× / 3×）。
- **延遲注入（預設）** — 僅在開啟彈出視窗時注入腳本，無需廣泛網站權限。
- **始終自動調速** — 可選授權後，每個頁面載入自動套用偏好速度。
- **速度記憶** — 經 `browser.storage.local` 跨頁面與工作階段保存。
- **動態影片偵測** — MutationObserver 涵蓋動態插入的 `<video>`。
- **複製為 Markdown** — 右鍵選單支援頁面 / 選取文字 / 連結 → `[text](url)`。
- **延伸功能介面語言** — 彈出視窗支援 **英文** 與 **簡體中文**（官網另有繁體文案）。
- **亮色與深色** — 跟隨 macOS 外觀。
- **精簡宿主應用** — 負責安裝與啟用延伸功能；日常設定在 Safari 中完成。

## 已知限制

- 僅標準 HTML5 `<video>`；Canvas / WebGL / 封閉 Shadow DOM 播放器可能無效。
- 部分網站會以程式重置 `playbackRate`，可能覆蓋 Weber。
- 實際最高倍率可能低於 100×，取決於編解碼器與 Safari。
- **僅限 Mac** — 不支援 iPhone、iPad 或其他瀏覽器。

## 系統需求

| 平台 | 最低版本 |
|------|----------|
| Mac（Safari）| macOS 12.0+ |

## 聯絡我們

- **電子郵件：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

我們通常在 48 小時內回覆。

[常見問題](faq) · [隱私政策](privacy)

</section>
