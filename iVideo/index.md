---
layout: app
title: iVideo — Support
app_id: iVideo
description: Complete user guide for iVideo — screen recording, 31 on-device tools, dedicated Edit Projects tab, multi-track timelines, subtitles, face blur, color grading, batch processing, export queue, Siri & iCloud.
---

<section lang="en" markdown="1">

iVideo (爱视频) is a **privacy-first professional video toolbox** for iPhone, iPad and Mac — screen recorder, frame-accurate player, **31 editing tools**, and a **multi-track edit-project editor**, all processed **100% on-device**. **No cloud, no account, no upload, no ads, no tracking.** This page is a **complete step-by-step guide**.

**At a glance:** Library + **Edit Projects** (always on) · optional Record (off by default) & Live Photo (on by default) · 31 tools in 7 categories · multi-track timelines · on-device subtitles (60+ languages) · face blur · color grading + LUTs · batch processing · 6 quality tiers + 4 named export presets · JKL pro playback · alternate icons · Siri · optional iCloud sync.

---

## Part 1 — First Launch & Interface

### Onboarding & sample video

On first launch a short **guided onboarding** highlights the pillars: professional workspace, frame-level precision, color creation, privacy-first, on-device subtitles. A **sample video is auto-added** so your library isn't empty — open it and try any tool immediately. Replay the tour anytime in **Settings → Help**.

### The main tabs

| Tab | What it does |
|-----|----------------|
| **Library** | All your videos — search, filter, sort, batch-edit |
| **Edit Projects** | Always-on project library — create, rename, duplicate, open multi-track timelines |
| **Record** *(optional, off by default)* | Screen recording; tab badge shows live elapsed time. Enable in Settings → Show in Tab Bar. |
| **Live Photo** *(optional, on by default)* | Convert to/from Live Photos; hide in Settings if unused |
| **Settings** | Theme, language, app icon, export, recording, storage, help, tab visibility |

When Record or Live Photo is hidden from the tab bar, you can still open them from Settings, Siri / Shortcuts, or an empty-library CTA (sheet).

---

## Part 2 — Getting Videos In

### Screen recording

**iOS:** Open the **Record** tab → tap the record button → the system **Broadcast Picker** appears → choose **iVideo** → **Start Broadcast**. A live duration badge shows on the Record tab. Auto-snapshots can be captured at an interval you set in Settings.

> iOS screen recording requires a **real device** — the Simulator can't broadcast.

**macOS:** Uses **ScreenCaptureKit** with multi-display and optional system audio. The first time, grant permission in **System Settings → Privacy & Security → Screen Recording**.

### Import

- **From Photos** — zero transcoding, with live progress
- **From Files** — multi-select import (iOS)
- **Remote URL** — direct-link download (hidden by default; enable in Settings → Advanced if shown)

---

## Part 3 — The Video Library

### Search, filter & sort

- **Search** by filename, custom name, or tag
- **Filter**: All / Favorites / Recorded / Imported / Exported / Has Notes
- **Sort** (Files-app style): by **date / name / size / kind / favorite**, each with **ascending / descending** — tap the same field again to flip direction

### Layout

Use the **View** menu: **Grid** or **List**, with adjustable columns (iPhone 1–4, iPad & Mac 2–6). List rows show thumbnail, title, source, size, favorite, notes and tags. Cards/rows also show the creation date.

### Batch operations

Multi-select, then: **Share**, **Save to Photos**, **Favorite**, **Merge**, **Collage**, **Batch Process**, or **Delete** (shows total storage freed).

### Custom cover

In the workspace menu, choose **Set current frame as cover** — the library shows it automatically.

---

## Part 4 — The Workspace & Playback

Open any video (iOS full-screen, macOS sheet) to enter the **Workspace**: dark preview, compact playback bar, tool categories, and the tool grid.

### Playback controls

- **Play/Pause**, frame step, ⏪10s / ⏩10s skip
- **Scrubber** with floating **thumbnail preview** and time bubble
- **Speed capsule** — shows real-time speed; **long-press** (0.5s) opens the custom-speed sheet
- **Horizontal swipe** on the preview to seek
- **Double-tap** to enter immersive full-screen; **pinch** to zoom the preview (1×–12×)
- **AirPlay & PiP** from the ⋯ menu (iOS)

### Variable speed

- **8 presets** (0.25× … 4×) + **custom slider** (0.1×–8×) + **2 recent** chips
- **Pinch to adjust** speed on iPhone
- Speed & mute **persist across sessions** and sync via iCloud

### JKL professional shuttle (great with a keyboard)

| Key | Action |
|-----|--------|
| **L** | Play forward; press again 2× → 4× → 8× |
| **J** | Reverse; press again to speed up reverse |
| **K** | Pause & reset |
| **K + J/L** | Hold K for 0.5× slow motion |
| **Space** | Play/pause |
| **← →** | Step 1 frame · **Shift+← →** skip 10s · **, .** step |

A **JKL HUD** shows current speed; optional **Live Activity** mirrors it on Lock Screen / Dynamic Island (iOS 16.1+). The scrubber turns **red** during reverse.

### Favorite tools bar

**Long-press** any tool → **Add to favorites** to pin it to a quick-access bar at the top (up to 5, synced via iCloud).

---

## Part 5 — The 31 Tools (7 Categories)

Open a video, pick a category, tap a tool, adjust parameters, then run. Export goes to the global queue.

| Category | Tools |
|----------|-------|
| **Basic** | Screenshot · Frame Extraction · Video Info · Scene Chapters · Text Recognition · Scopes · Annotation |
| **Clip** | Duration Trim · Aspect Crop · Rotate · Text Edit · Beat Montage · Jump Cut |
| **Speed** | Variable Speed (0.1–8×) · Reverse · Speed Ramp |
| **Audio** | Mute · Audio Extraction (M4A/WAV/CAF) · On-Device Subtitles · Denoise & Enhance |
| **Visual** | Watermark · Metadata Strip · Compression · Face Blur · Color Grading |
| **Convert** | Live Photo · GIF · Social Format · Before/After Compare |
| **Notes** | Video Notes · Frame Compare |

**Screenshot / Frame extraction:** adjustable **JPEG quality** slider (100% = "Original"); can save to Photos or the **Files** app.
**Video Info:** codec, resolution, fps, bitrate, duration, size.
**OCR:** recognizes text on the current frame; result is **editable**; copy or share. Results are cached across sheets.
**Waveform Scope:** RGB histogram + luma waveform for the current frame.
**Annotation:** draw arrows/circles/rectangles/freehand/text → export full-resolution PNG.

---

## Part 6 — On-Device Subtitles (Flagship)

1. Open a video → **Audio → Subtitles**
2. Choose a **source mode**: **Speech**, **Sound events** (music/applause/laughter → `[tags]`), or **Speech + Sound**
3. Pick the **recognition language** (searchable list, 60+ languages; an orange "Download" badge means you need the offline pack in system settings)
4. Tap generate — everything runs **on-device** (`requiresOnDeviceRecognition`); nothing is uploaded
5. **Edit** any line, delete, or tap a line to seek
6. Open **Style** for weight, shadow, box/outline opacity, alignment, vertical layout, and custom primary/secondary colors — save as a **named preset**
7. Optional **bilingual translation** (Apple Translation, on-device) adds a secondary line
8. **Export SRT / ASS**, or **burn-in** to the video (cancellable)

> On iOS 26 / macOS 26 the modern `SpeechAnalyzer` path gives stable long-audio recognition with word-level timing.

---

## Part 7 — Face Blur (Flagship)

1. Open a video → **Visual → Face Blur**
2. Faces are **auto-detected** every frame (Vision)
3. Choose **Gaussian blur** or **Mosaic**, adjust **intensity**
4. For plates, signs, or logos detection can't catch, **draw a manual rectangle** — it applies to the whole clip
5. Export — soft-edge masks and the original audio are preserved; the frames never leave your device

---

## Part 8 — Color Grading, LUTs & Filters

- **7-parameter grading** — exposure, brightness, contrast, saturation, vibrance, white balance, tint; real-time preview with **hold-to-compare**
- **Built-in LUT pack** — 6 styles (Teal & Orange, Bleach Bypass, Vintage, Cool Shadow, Warm Shadow, High-Contrast B&W), zero resource files
- **Filter presets** — 11 built-in; **import `.cube` 3D LUTs** from Adobe/Resolve

---

## Part 9 — Speed Ramp, Silence Removal & Beat Sync

- **Speed Ramp** — split the timeline into segments and assign a speed per segment with a color-band editor
- **Silence Removal** — auto jump-cut silent parts (RMS + adaptive threshold), with a canvas preview of kept/removed ranges
- **Beat Sync** — detects beats/BPM and cuts on every beat with continuous audio; stack transitions (zoom, slide, flash, black)

---

## Part 10 — Social Format, Compare, Merge & Collage

- **Social Format** — 9:16 / 1:1 / 4:5 / 16:9 with blur background, solid color, or crop-to-fill; safe-area guides; optional top/bottom caption bar
- **Before/After** — side-by-side or top/bottom split with divider and labels
- **Merge** — concatenate clips with optional crossfade
- **Collage** — 2–4 videos side-by-side, top-bottom, or 4-grid at 1920×1080

---

## Part 11 — Live Photo Studio

- **Video → Live Photo** — pick a key frame and duration to make a Live wallpaper
- **Live Photo → Video / GIF / Still** — original encoding preserved; exports use a protected copy so your Photos Live pair is not broken
- **Batch mode** — multi-select Live Photos for bulk conversion

---

## Part 12 — Batch Processing (Recipes)

1. In the Library, **multi-select** videos → **Batch Process**
2. Build a **recipe** — a fixed chain: rotate → speed → mute → watermark → metadata strip → compress
3. Run — videos process serially; a single failure won't stop the batch; completed items are added to the library incrementally
4. Your last recipe is remembered for next time

---

## Part 13 — Edit Projects (Multi-Track Editor)

For real timeline editing, open the **Edit Projects** tab. This is a savable, composable, publishable non-linear editor.

### Create & arrange

1. **New project** → **Add clips** from your library
2. **Multi-track timeline** — split, delete, drag to reorder, crossfade between clips
3. **Timeline controls** — ruler with drag-to-seek, **pinch to zoom** (remembered), double-tap to reset, multi-frame thumbnails on long clips, active clip highlighted

### Overlays & audio

- **Overlays** — timed **text**, **stickers**, or **picture-in-picture video**
- **PiP free placement** — drag the PiP center freely, or snap to corners; scale roughly 0.15–0.7
- **Dual audio** — **BGM + narration** with loop-fill and **automatic ducking** under speech
- **Preview volume** updates instantly while dragging (no full preview rebuild)
- **Close confirmation** — Keep / Discard / Keep editing when leaving with unsaved changes
- **Scrub release** resumes playback (including JKL direction/speed) when you were playing before scrubbing

### Per-clip reprocessing (baked, reversible)

- **Stabilize** (Vision frame alignment)
- **Smart Reframe** (face-follow landscape → portrait)
- **Smooth Slow-Mo** (frame blending)
- **Multicam** (A/B offset align + switch / PiP)

### Canvas & publish

1. Pick a **canvas ratio** (Original / 9:16 / 1:1 / 4:5 / 16:9)
2. Use **Undo/Redo**; the project **auto-saves** (debounced)
3. Open the **Publish Wizard** — choose platform aspect, cover frame, and subtitle burn-in (SRT/ASS) → saved to your Library

> Projects are **self-contained** (media is copied in), so deleting originals won't break a project. Preview and export share the same composition — what you see is what you get.

---

## Part 14 — Export

| Preset | Resolution |
|--------|-----------|
| Original | Source |
| Ultra HD | 4K |
| Super HD | 2K |
| HD | 1080p |
| Standard | 720p |
| Compact | 540p |

- Format **MP4** or **MOV**
- **Export presets** — 4 built-in + custom (quality + container); switch globally from the workspace ⋯ menu or Settings
- **Global export queue** — background serial processing with progress; view pending / running / completed / failed; iOS keeps exports alive in the background
- **Completion notification** — optional local notification (toggle in Settings → Export)
- **Quick share** — the export toast has an inline Share button; session history lets you re-share

---

## Part 15 — Siri & Shortcuts

Built-in **App Shortcuts** (Siri & the Shortcuts app):

- **Start recording**
- **Open video library**
- **Open Live Photo tool**

Add them to Siri or build automations in the Shortcuts app.

---

## Part 16 — Settings Walkthrough

- **Appearance** — theme (light/dark/system), language (EN / 简中 / 繁中, instant switch), **Live Activity** toggle (JKL, off by default), **alternate app icons** on iOS (default + 8 styles)
- **Export** — default preset, export presets manager (4 built-in named presets + custom), completion notification toggle
- **Recording** — auto-snapshot interval, macOS audio options; Record / Live Photo **Show in Tab Bar**
- **Watermark** — default watermark settings
- **Storage** — thumbnail cache summary and clear
- **Help** — usage guide, all-tools reference, permissions, FAQ, replay onboarding
- **About** — app stats, highlights, rate, share, feedback (email auto-attaches device info)
- Top of Settings has a **search** field

---

## Part 17 — iCloud Sync

Lightweight preference sync via `NSUbiquitousKeyValueStore`:

| Synced | Not synced |
|--------|------------|
| Theme, language | Video files themselves |
| Playback speed, mute | Library sort/filter |
| Custom speed history | Remote-download toggle |
| Favorite tools bar | — |

Works only when signed into iCloud; otherwise everything still works locally.

---

## Part 18 — Privacy

- **All processing on-device** — recording, editing, speech, face detection, OCR, translation, color
- **No cloud, no account, no analytics SDK, no tracking**
- Optional iCloud syncs only lightweight preferences

Details: [Privacy Policy](privacy)

---

## System Requirements

| Platform | Minimum |
|----------|---------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |

## Contact Us

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — we typically reply within 48 hours.

[FAQ](faq) · [Privacy Policy](privacy)

</section>

<section lang="zh-CN" markdown="1">

爱视频是一款面向 iPhone、iPad 和 Mac 的 **隐私优先专业视频工具箱**——录屏、逐帧播放器、**31 种剪辑工具**，以及**多轨剪辑工程编辑器**，全部**在设备本地处理**。**无云端、无账号、零上传、无广告、无追踪。** 本页为**完整分步教程**。

**一览：** 视频库 + **剪辑工程**（常驻）· 可选录屏（默认关）与实况（默认开）· 7 大类 31 种工具 · 多轨时间线 · 设备端字幕（60+ 语言）· 人脸打码 · 调色 + LUT · 批处理 · 6 档画质 + 4 个命名导出预设 · JKL 专业播放 · 备用图标 · Siri · 可选 iCloud 同步。

---

## 第一部分 — 首次启动与界面

### 引导与演示样片

首次启动有一段**走查引导**，呈现几大支柱：专业工作台、逐帧级精准、调色创作、隐私优先、本地字幕。首启会**自动注入一段演示样片**，让视频库不为空——直接打开就能试用任意工具。随时可在 **设置 → 帮助** 重看引导。

### 主要标签

| 标签 | 作用 |
|------|------|
| **视频库** | 全部视频——搜索、过滤、排序、批量编辑 |
| **剪辑工程** | 常驻工程库——新建、重命名、复制，打开多轨时间线 |
| **录屏**（可选，默认关闭） | 屏幕录制；Tab 角标实时时长；在设置 → 在标签栏显示中开启 |
| **Live Photo**（可选，默认开启） | Live Photo 双向转换；不用时可在设置中隐藏 |
| **设置** | 主题、语言、App 图标、导出、录屏、存储、帮助、标签显隐 |

录屏或实况从标签栏隐藏后，仍可从设置、Siri / 快捷指令，或空库引导以 sheet 打开。

---

## 第二部分 — 把视频导进来

### 录屏

**iOS：** 打开 **录屏** 标签 → 点录制按钮 → 系统弹出 **广播选择器** → 选 **爱视频** → **开始直播**。录屏 Tab 显示实时时长徽标；可在设置中设定录制中自动截图的间隔。

> iOS 录屏需**真机**——模拟器不支持广播。

**macOS：** 使用 **ScreenCaptureKit**，支持多显示器与系统音频可选。首次录屏需在 **系统设置 → 隐私与安全性 → 屏幕录制** 授权。

### 导入

- **从相册** — 零转码，实时进度
- **从文件 App** — 多选导入（iOS）
- **远程直链** — 直链下载（默认隐藏；如显示可在设置 → 高级启用）

---

## 第三部分 — 视频库

### 搜索、过滤与排序

- 按**文件名、自定义名、标签**搜索
- **过滤**：全部 / 收藏 / 录屏 / 导入 / 已导出 / 含笔记
- **排序**（文件 App 风格）：按**日期 / 名称 / 大小 / 种类 / 收藏**，各带**升序 / 降序**——再次点同一字段可翻转方向

### 布局

用 **视图** 菜单：**网格** 或 **列表**，列数可调（iPhone 1–4，iPad 与 Mac 2–6）。列表行显示缩略图、标题、来源、大小、收藏、笔记与标签，并显示创建日期。

### 批量操作

多选后：**分享**、**存相册**、**收藏**、**拼接**、**拼图**、**批处理**、**删除**（显示释放的总空间）。

### 自定义封面

在工作台菜单选 **设当前帧为封面**，视频库会自动优先显示。

---

## 第四部分 — 工作台与播放

打开任意视频（iOS 全屏、macOS sheet）进入**工作台**：暗色预览、紧凑播放栏、工具类别与工具网格。

### 播放控制

- **播放/暂停**、逐帧、⏪10 秒 / ⏩10 秒
- **进度条**带悬浮**缩略图预览**与时间气泡
- **速度胶囊** — 实时显示速度；**长按**（0.5 秒）打开自定义速度面板
- 预览区**水平滑动**快进
- **双击**进入沉浸全屏；**双指捏合**缩放预览（1×–12×）
- ⋯ 菜单里的 **AirPlay 与画中画**（iOS）

### 变速

- **8 档预设**（0.25× … 4×）+ **自定义滑块**（0.1×–8×）+ **最近 2 档**
- iPhone **双指捏合**调速
- 速度与静音**跨会话保留**并通过 iCloud 同步

### JKL 专业快退快进（配键盘更佳）

| 键 | 作用 |
|----|------|
| **L** | 正向播放；再按 2× → 4× → 8× |
| **J** | 倒放；再按加快倒放速度 |
| **K** | 暂停并复位 |
| **K + J/L** | 按住 K 进入 0.5× 慢动作 |
| **Space** | 播放/暂停 |
| **← →** | 逐帧 · **Shift+← →** 跳 10 秒 · **, .** 逐帧 |

**JKL HUD** 显示当前速度；可选 **Live Activity** 同步到锁屏 / 灵动岛（iOS 16.1+）。倒放时进度条变**红**。

### 常用工具快捷栏

**长按**任意工具 → **加入快捷栏**，钉到工作台顶部（最多 5 个，iCloud 同步）。

---

## 第五部分 — 31 种工具（7 大类）

打开视频，选类别，点工具，调参数，执行。导出进入全局队列。

| 类别 | 工具 |
|------|------|
| **基础** | 截图 · 拆帧 · 视频信息 · 场景章节 · 文字识别 · 示波器 · 逐帧标注 |
| **剪辑** | 时长裁剪 · 画面裁剪 · 旋转 · 文字剪辑 · 卡点混剪 · 去静音跳剪 |
| **速度** | 变速（0.1–8×）· 倒放 · 变速曲线 |
| **音频** | 静音 · 音频分离（M4A/WAV/CAF）· 设备端字幕 · 降噪增强 |
| **视觉** | 水印 · 元数据清除 · 压缩 · 人脸打码 · 调色 |
| **转换** | Live Photo · GIF · 社媒画幅 · 前后对比拼屏 |
| **笔记** | 视频笔记 · 帧对比 |

**截图 / 拆帧：** JPEG **质量可调**（100% 显示「原画」）；可存相册或**文件 App**。
**视频信息：** 编码、分辨率、帧率、码率、时长、大小。
**OCR：** 识别当前帧文字；结果**可编辑**；复制或分享。结果跨 sheet 缓存。
**示波器：** 当前帧 RGB 直方图 + 亮度波形。
**逐帧标注：** 画箭头/圈/框/自由笔/文字 → 导出全分辨率 PNG。

---

## 第六部分 — 设备端字幕（旗舰）

1. 打开视频 → **音频 → 字幕**
2. 选**来源模式**：**语音**、**声音事件**（音乐/掌声/笑声 → `[标注]`）、或**语音 + 声音**
3. 选**识别语言**（可搜索，60+ 语言；橙色「需下载」表示需在系统设置装离线包）
4. 点生成——全程**设备端**（`requiresOnDeviceRecognition`），不上传
5. 逐条**编辑**、删除，或点某条**跳转**到对应时间
6. 打开**样式**：字重、阴影、底框/描边透明度、对齐、竖排、自定义主/副色——可存为**命名预设**
7. 可选**双语翻译**（Apple Translation，设备端）加副语言行
8. **导出 SRT / ASS**，或**烧录**进视频（可取消）

> iOS 26 / macOS 26 走现代 `SpeechAnalyzer` 路径，长音频识别更稳，带词级时间戳。

---

## 第七部分 — 人脸打码（旗舰）

1. 打开视频 → **视觉 → 人脸打码**
2. 逐帧**自动检测**人脸（Vision）
3. 选 **高斯模糊** 或 **马赛克**，调**强度**
4. 车牌、招牌、角标等检测不到的，**手动画矩形框**——对整段生效
5. 导出——柔化遮罩 + 原音轨保留，画面全程不出设备

---

## 第八部分 — 调色、LUT 与滤镜

- **7 参数调色** — 曝光、亮度、对比度、饱和度、自然饱和度、色温、色调；实时预览 + **按住看原图**
- **内置 LUT 包** — 6 种风格（青橙、漂白、复古、冷影、暖影、高反黑白），零资源文件
- **滤镜预设** — 11 种内建；支持**导入 `.cube` 3D LUT**（Adobe/Resolve）

---

## 第九部分 — 变速曲线、去静音与卡点混剪

- **变速曲线** — 时间线分段，逐段设速度，色带式编辑
- **去静音跳剪** — 自动跳过静音段（RMS + 自适应阈值），Canvas 预览保留/移除段
- **卡点混剪** — 检测节拍/BPM，画面随节拍跳切、音乐连续；可叠加转场（缩放、滑入、闪白、黑场）

---

## 第十部分 — 社媒画幅、对比、拼接与拼图

- **社媒画幅** — 9:16 / 1:1 / 4:5 / 16:9，模糊背景/纯色边/裁剪填满；安全区参考线；可选顶/底字幕条
- **前后对比** — 左右或上下拼屏，带分隔线与 Before/After 标签
- **拼接** — 多段首尾相接，可选交叉淡化
- **拼图** — 2–4 个视频左右/上下/四宫格，输出 1920×1080

---

## 第十一部分 — Live Photo 工作室

- **视频 → Live Photo** — 选关键帧与时长，做动态壁纸
- **Live Photo → 视频 / GIF / 静图** — 保留原始编码；导出使用受保护副本，避免损坏相册中的 Live 配对源
- **批量模式** — 多选 Live Photo 批量转换

---

## 第十二部分 — 批处理（配方）

1. 视频库**多选** → **批处理**
2. 组一套**配方**——固定链：旋转 → 变速 → 去音轨 → 水印 → 清元数据 → 压缩
3. 执行——逐个串行处理，单个失败不阻断整批，完成的增量入库
4. 自动记住上次配方

---

## 第十三部分 — 剪辑工程（多轨编辑器）

需要真正的时间线剪辑时，打开 **剪辑工程** 标签。工程库支持重命名与复制；这是可保存、可组合、可发布的非线性编辑器。

### 新建与排列

1. **新建工程** → 从库中**添加片段**
2. **多轨时间线** — 分割、删除、拖拽换序、片段间叠化
3. **时间线操作** — 刻度尺拖动 seek、**双指缩放**（记忆）、双击复位、长片段多帧缩略图、正在播放片段高亮

### 叠加层与音频

- **叠加层** — 定时**文字**、**贴图**、**画中画视频**
- **PiP 自由定位** — 拖动画中画中心，或贴四角；缩放约 0.15–0.7
- **双轨音频** — **BGM + 旁白**，循环铺满 + 说话区间**自动闪避**
- **预览音量**拖动即时生效（不重建画面预览）
- **关闭确认** — 有未保存修改时：保留修改 / 放弃修改 / 继续编辑
- **Scrub 松手**恢复播放（含 JKL 方向与速率）

### 逐片段重处理（烘焙，可回退）

- **画面稳定**（Vision 帧间配准）
- **智能构图**（人脸跟随，横→竖）
- **平滑慢动作**（相邻帧融合）
- **双机位**（A/B 偏移对齐 + 切换 / PiP）

### 画布与发布

1. 选**画布比例**（原始 / 9:16 / 1:1 / 4:5 / 16:9）
2. 支持**撤销/重做**；工程**防抖自动保存**
3. 打开**发布向导**——选平台画幅、封面帧、字幕烧录（SRT/ASS）→ 存入视频库

> 工程是**自包含**的（片段会拷入工程），删原片也不断链。预览与导出共用同一合成，所见即所得。

---

## 第十四部分 — 导出

| 档位 | 分辨率 |
|------|--------|
| 原画 | 源分辨率 |
| 超高清 | 4K |
| 超清 | 2K |
| 高清 | 1080p |
| 标清 | 720p |
| 省流 | 540p |

- 格式 **MP4** 或 **MOV**
- **导出预设** — 4 内建 + 自定义（画质 + 容器）；工作台 ⋯ 菜单或设置一键切换
- **全局导出队列** — 后台串行处理带进度；查看排队/进行/完成/失败；iOS 后台保活
- **完成通知** — 可选本地通知（设置 → 导出）
- **快速分享** — 导出 Toast 内联分享按钮；会话历史可再分享

---

## 第十五部分 — Siri 与快捷指令

内置 **App Shortcuts**（Siri 与快捷指令 App）：

- **开始录屏**
- **打开视频库**
- **打开 Live Photo 工具**

可加入 Siri 或在快捷指令 App 里做自动化。

---

## 第十六部分 — 设置逐项

- **外观** — 主题（浅/深/系统）、语言（英/简/繁，即时切换）、**实时活动** 开关（JKL，默认关）、iOS **备用 App 图标**（默认 + 8 款）
- **导出** — 默认预设、导出预设管理（4 个内建命名预设 + 自定义）、完成通知开关
- **录屏** — 自动截图间隔、macOS 音频选项；录屏 / 实况 **在标签栏显示**
- **水印** — 默认水印设置
- **存储** — 缩略图缓存汇总与清理
- **帮助** — 使用指南、全部工具速查、权限说明、FAQ、重看引导
- **关于** — 应用数据、亮点、评分、分享、反馈（邮件自动附设备信息）
- 设置顶部有**搜索**框

---

## 第十七部分 — iCloud 同步

基于 `NSUbiquitousKeyValueStore` 的轻量偏好同步：

| 会同步 | 不同步 |
|--------|--------|
| 主题、语言 | 视频文件本身 |
| 播放速度、静音 | 库排序/过滤 |
| 自定义速度历史 | 远程下载开关 |
| 常用工具快捷栏 | — |

仅在登录 iCloud 时生效；未登录时本地功能照常。

---

## 第十八部分 — 隐私

- **全部处理在设备本地** — 录屏、剪辑、语音、人脸检测、OCR、翻译、调色
- **无云端、无账号、无分析 SDK、无追踪**
- 可选 iCloud 仅同步轻量偏好

详见 [隐私政策](privacy)

---

## 系统要求

| 平台 | 最低版本 |
|------|----------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |

## 联系我们

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 通常 48 小时内回复。

[常见问题](faq) · [隐私政策](privacy)

</section>

<section lang="zh-TW" markdown="1">

愛視頻是一款面向 iPhone、iPad 和 Mac 的 **隱私優先專業影片工具箱**——錄屏、逐幀播放器、**31 種剪輯工具**，以及**多軌剪輯工程編輯器**，全部**在裝置本地處理**。**無雲端、無帳號、零上傳、無廣告、無追蹤。** 本頁為**完整分步教程**。

**一覽：** 影片庫 + **剪輯工程**（常駐）· 可選錄屏（預設關）與原況（預設開）· 7 大類 31 種工具 · 多軌時間線 · 裝置端字幕（60+ 語言）· 人臉打碼 · 調色 + LUT · 批次處理 · 6 檔畫質 + 4 個命名匯出預設 · JKL 專業播放 · 備用圖示 · Siri · 可選 iCloud 同步。

---

## 第一部分 — 首次啟動與介面

### 引導與示範樣片

首次啟動有一段**走查引導**，呈現幾大支柱：專業工作台、逐幀級精準、調色創作、隱私優先、本地字幕。首啟會**自動注入一段示範樣片**，讓影片庫不為空——直接開啟就能試用任意工具。隨時可在 **設定 → 幫助** 重看引導。

### 四個標籤

| 標籤 | 作用 |
|------|------|
| **影片庫** | 全部影片——搜尋、過濾、排序、批次編輯 |
| **剪輯工程** | 常駐工程庫——新建、重新命名、複製，開啟多軌時間線 |
| **錄屏**（可選，預設關閉） | 螢幕錄製；Tab 角標即時時長；在設定 → 在標籤列顯示中開啟 |
| **原況照片**（可選，預設開啟） | 原況照片互轉；不用時可在設定中隱藏 |
| **設定** | 主題、語言、App 圖示、匯出、錄屏、儲存、說明、標籤顯隱 |

錄屏或原況從標籤列隱藏後，仍可從設定、Siri / 捷徑，或空庫引導以 sheet 開啟。


---

## 第二部分 — 把影片匯進來

### 錄屏

**iOS：** 開啟 **錄屏** 標籤 → 點錄製按鈕 → 系統彈出 **廣播選擇器** → 選 **愛視頻** → **開始廣播**。錄屏 Tab 顯示即時時長徽標；可在設定中設定錄製中自動截圖的間隔。

> iOS 錄屏需**真機**——模擬器不支援廣播。

**macOS：** 使用 **ScreenCaptureKit**，支援多顯示器與系統音訊可選。首次錄屏需在 **系統設定 → 隱私與安全性 → 螢幕錄製** 授權。

### 匯入

- **從相簿** — 零轉碼，即時進度
- **從檔案 App** — 多選匯入（iOS）
- **遠端直連** — 直連下載（預設隱藏；如顯示可在設定 → 進階啟用）

---

## 第三部分 — 影片庫

### 搜尋、過濾與排序

- 按**檔案名、自訂名、標籤**搜尋
- **過濾**：全部 / 收藏 / 錄屏 / 匯入 / 已匯出 / 含筆記
- **排序**（檔案 App 風格）：按**日期 / 名稱 / 大小 / 種類 / 收藏**，各帶**升序 / 降序**——再次點同一欄位可翻轉方向

### 版面

用 **檢視** 選單：**網格** 或 **列表**，欄數可調（iPhone 1–4，iPad 與 Mac 2–6）。列表列顯示縮圖、標題、來源、大小、收藏、筆記與標籤，並顯示建立日期。

### 批次操作

多選後：**分享**、**存相簿**、**收藏**、**拼接**、**拼圖**、**批次處理**、**刪除**（顯示釋放的總空間）。

### 自訂封面

在工作台選單選 **設當前幀為封面**，影片庫會自動優先顯示。

---

## 第四部分 — 工作台與播放

開啟任意影片（iOS 全螢幕、macOS sheet）進入**工作台**：暗色預覽、緊湊播放列、工具類別與工具網格。

### 播放控制

- **播放/暫停**、逐幀、⏪10 秒 / ⏩10 秒
- **進度條**帶懸浮**縮圖預覽**與時間氣泡
- **速度膠囊** — 即時顯示速度；**長按**（0.5 秒）開啟自訂速度面板
- 預覽區**水平滑動**快進
- **雙擊**進入沉浸全螢幕；**雙指捏合**縮放預覽（1×–12×）
- ⋯ 選單裡的 **AirPlay 與子母畫面**（iOS）

### 變速

- **8 檔預設**（0.25× … 4×）+ **自訂滑桿**（0.1×–8×）+ **最近 2 檔**
- iPhone **雙指捏合**調速
- 速度與靜音**跨工作階段保留**並透過 iCloud 同步

### JKL 專業快退快進（配鍵盤更佳）

| 鍵 | 作用 |
|----|------|
| **L** | 正向播放；再按 2× → 4× → 8× |
| **J** | 倒放；再按加快倒放速度 |
| **K** | 暫停並復位 |
| **K + J/L** | 按住 K 進入 0.5× 慢動作 |
| **Space** | 播放/暫停 |
| **← →** | 逐幀 · **Shift+← →** 跳 10 秒 · **, .** 逐幀 |

**JKL HUD** 顯示目前速度；可選 **Live Activity** 同步到鎖定畫面 / 靈動島（iOS 16.1+）。倒放時進度條變**紅**。

### 常用工具快捷列

**長按**任意工具 → **加入快捷列**，釘到工作台頂部（最多 5 個，iCloud 同步）。

---

## 第五部分 — 31 種工具（7 大類）

開啟影片，選類別，點工具，調參數，執行。匯出進入全域佇列。

| 類別 | 工具 |
|------|------|
| **基礎** | 截圖 · 拆幀 · 影片資訊 · 場景章節 · 文字辨識 · 示波器 · 逐幀標註 |
| **剪輯** | 時長裁剪 · 畫面裁剪 · 旋轉 · 文字剪輯 · 卡點混剪 · 去靜音跳剪 |
| **速度** | 變速（0.1–8×）· 倒放 · 變速曲線 |
| **音訊** | 靜音 · 音訊分離（M4A/WAV/CAF）· 裝置端字幕 · 降噪增強 |
| **視覺** | 浮水印 · 中繼資料清除 · 壓縮 · 人臉打碼 · 調色 |
| **轉換** | Live Photo · GIF · 社媒畫幅 · 前後對比拼屏 |
| **筆記** | 影片筆記 · 幀對比 |

**截圖 / 拆幀：** JPEG **品質可調**（100% 顯示「原畫」）；可存相簿或**檔案 App**。
**影片資訊：** 編碼、解析度、幀率、位元率、時長、大小。
**OCR：** 辨識當前幀文字；結果**可編輯**；複製或分享。結果跨 sheet 快取。
**示波器：** 當前幀 RGB 直方圖 + 亮度波形。
**逐幀標註：** 畫箭頭/圈/框/自由筆/文字 → 匯出全解析度 PNG。

---

## 第六部分 — 裝置端字幕（旗艦）

1. 開啟影片 → **音訊 → 字幕**
2. 選**來源模式**：**語音**、**聲音事件**（音樂/掌聲/笑聲 → `[標註]`）、或**語音 + 聲音**
3. 選**辨識語言**（可搜尋，60+ 語言；橙色「需下載」表示需在系統設定裝離線包）
4. 點生成——全程**裝置端**（`requiresOnDeviceRecognition`），不上傳
5. 逐條**編輯**、刪除，或點某條**跳轉**到對應時間
6. 開啟**樣式**：字重、陰影、底框/描邊透明度、對齊、直排、自訂主/副色——可存為**命名預設**
7. 可選**雙語翻譯**（Apple Translation，裝置端）加副語言行
8. **匯出 SRT / ASS**，或**燒錄**進影片（可取消）

> iOS 26 / macOS 26 走現代 `SpeechAnalyzer` 路徑，長音訊辨識更穩，帶詞級時間戳。

---

## 第七部分 — 人臉打碼（旗艦）

1. 開啟影片 → **視覺 → 人臉打碼**
2. 逐幀**自動偵測**人臉（Vision）
3. 選 **高斯模糊** 或 **馬賽克**，調**強度**
4. 車牌、招牌、角標等偵測不到的，**手動畫矩形框**——對整段生效
5. 匯出——柔化遮罩 + 原音軌保留，畫面全程不出裝置

---

## 第八部分 — 調色、LUT 與濾鏡

- **7 參數調色** — 曝光、亮度、對比度、飽和度、自然飽和度、色溫、色調；即時預覽 + **按住看原圖**
- **內建 LUT 包** — 6 種風格（青橙、漂白、復古、冷影、暖影、高反黑白），零資源檔案
- **濾鏡預設** — 11 種內建；支援**匯入 `.cube` 3D LUT**（Adobe/Resolve）

---

## 第九部分 — 變速曲線、去靜音與卡點混剪

- **變速曲線** — 時間線分段，逐段設速度，色帶式編輯
- **去靜音跳剪** — 自動跳過靜音段（RMS + 自適應閾值），Canvas 預覽保留/移除段
- **卡點混剪** — 偵測節拍/BPM，畫面隨節拍跳切、音樂連續；可疊加轉場（縮放、滑入、閃白、黑場）

---

## 第十部分 — 社媒畫幅、對比、拼接與拼圖

- **社媒畫幅** — 9:16 / 1:1 / 4:5 / 16:9，模糊背景/純色邊/裁剪填滿；安全區參考線；可選頂/底字幕條
- **前後對比** — 左右或上下拼屏，帶分隔線與 Before/After 標籤
- **拼接** — 多段首尾相接，可選交叉淡化
- **拼圖** — 2–4 個影片左右/上下/四宮格，輸出 1920×1080

---

## 第十一部分 — Live Photo 工作室

- **影片 → Live Photo** — 選關鍵幀與時長，做動態桌布
- **Live Photo → 影片 / GIF / 靜圖** — 保留原始編碼；匯出使用受保護副本，避免損壞相簿中的原況配對源
- **批次模式** — 多選 Live Photo 批次轉換

---

## 第十二部分 — 批次處理（配方）

1. 影片庫**多選** → **批次處理**
2. 組一套**配方**——固定鏈：旋轉 → 變速 → 去音軌 → 浮水印 → 清中繼資料 → 壓縮
3. 執行——逐個串行處理，單個失敗不阻斷整批，完成的增量入庫
4. 自動記住上次配方

---

## 第十三部分 — 剪輯工程（多軌編輯器）

需要真正的時間線剪輯時，開啟 **剪輯工程** 標籤。工程庫支援重新命名與複製；這是可保存、可組合、可發布的非線性編輯器。

### 新建與排列

1. **新建工程** → 從庫中**加入片段**
2. **多軌時間線** — 分割、刪除、拖曳換序、片段間疊化
3. **時間線操作** — 刻度尺拖動 seek、**雙指縮放**（記憶）、雙擊復位、長片段多幀縮圖、正在播放片段高亮

### 疊加層與音訊

- **疊加層** — 定時**文字**、**貼圖**、**子母畫面影片**
- **PiP 自由定位** — 拖動子母畫面中心，或貼四角；縮放約 0.15–0.7
- **雙軌音訊** — **BGM + 旁白**，循環鋪滿 + 說話區間**自動閃避**
- **預覽音量**拖動即時生效（不重建畫面預覽）
- **關閉確認** — 有未保存修改時：保留修改 / 放棄修改 / 繼續編輯
- **Scrub 鬆手**恢復播放（含 JKL 方向與速率）

### 逐片段重處理（烘焙，可回退）

- **畫面穩定**（Vision 幀間配準）
- **智能構圖**（人臉跟隨，橫→豎）
- **平滑慢動作**（相鄰幀融合）
- **雙機位**（A/B 偏移對齊 + 切換 / PiP）

### 畫布與發布

1. 選**畫布比例**（原始 / 9:16 / 1:1 / 4:5 / 16:9）
2. 支援**撤銷/重做**；工程**防抖自動保存**
3. 開啟**發布嚮導**——選平台畫幅、封面幀、字幕燒錄（SRT/ASS）→ 存入影片庫

> 工程是**自包含**的（片段會拷入工程），刪原片也不斷鏈。預覽與匯出共用同一合成，所見即所得。

---

## 第十四部分 — 匯出

| 檔位 | 解析度 |
|------|--------|
| 原畫 | 來源解析度 |
| 超高清 | 4K |
| 超清 | 2K |
| 高清 | 1080p |
| 標清 | 720p |
| 省流 | 540p |

- 格式 **MP4** 或 **MOV**
- **匯出預設** — 4 內建 + 自訂（畫質 + 容器）；工作台 ⋯ 選單或設定一鍵切換
- **全域匯出佇列** — 後台串行處理帶進度；查看排隊/進行/完成/失敗；iOS 後台保活
- **完成通知** — 可選本地通知（設定 → 匯出）
- **快速分享** — 匯出 Toast 內嵌分享按鈕；工作階段歷史可再分享

---

## 第十五部分 — Siri 與捷徑

內建 **App Shortcuts**（Siri 與捷徑 App）：

- **開始錄屏**
- **開啟影片庫**
- **開啟 Live Photo 工具**

可加入 Siri 或在捷徑 App 裡做自動化。

---

## 第十六部分 — 設定逐項

- **外觀** — 主題（淺/深/系統）、語言（英/簡/繁，即時切換）、**即時動態** 開關（JKL，預設關）、iOS **備用 App 圖示**（預設 + 8 款）
- **匯出** — 預設檔位、匯出預設管理（4 個內建命名預設 + 自訂）、完成通知開關
- **錄屏** — 自動截圖間隔、macOS 音訊選項；錄屏 / 原況 **在標籤列顯示**
- **浮水印** — 預設浮水印設定
- **儲存** — 縮圖快取彙總與清理
- **幫助** — 使用指南、全部工具速查、權限說明、FAQ、重看引導
- **關於** — 應用資料、亮點、評分、分享、回饋（郵件自動附裝置資訊）
- 設定頂部有**搜尋**框

---

## 第十七部分 — iCloud 同步

基於 `NSUbiquitousKeyValueStore` 的輕量偏好同步：

| 會同步 | 不同步 |
|--------|--------|
| 主題、語言 | 影片檔案本身 |
| 播放速度、靜音 | 庫排序/過濾 |
| 自訂速度歷史 | 遠端下載開關 |
| 常用工具快捷列 | — |

僅在登入 iCloud 時生效；未登入時本地功能照常。

---

## 第十八部分 — 隱私

- **全部處理在裝置本地** — 錄屏、剪輯、語音、人臉偵測、OCR、翻譯、調色
- **無雲端、無帳號、無分析 SDK、無追蹤**
- 可選 iCloud 僅同步輕量偏好

詳見 [隱私政策](privacy)

---

## 系統需求

| 平台 | 最低版本 |
|------|----------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |

## 聯絡我們

- **電子郵件：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 通常 48 小時內回覆。

[常見問題](faq) · [隱私政策](privacy)

</section>
