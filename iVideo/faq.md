---
layout: doc
title: iVideo — FAQ
app_id: iVideo
doc_title_en: Frequently Asked Questions
doc_title_zh_cn: 常见问题
doc_title_zh_tw: 常見問題
description: Frequently asked questions about iVideo.
---

<section lang="en" markdown="1">

### What video formats does iVideo support?

iVideo supports all formats that iOS and macOS can decode natively, including MP4, MOV, M4V, and more. Exports are available in MP4 or MOV format at your chosen quality preset.

### Where are my videos stored?

All videos are stored locally on your device:

- **Recorded videos** — In the shared App Group container.
- **Imported videos** — In the app's Documents/ImportedVideos folder.
- **Exported videos** — In the app's Documents/Exports folder.

No video data is uploaded to any cloud service.

### Can I edit 4K videos?

Yes. iVideo fully supports 4K video processing. You can import, edit, and export 4K videos. The export quality picker includes an Ultra HD (4K) preset alongside Original, 2K, 1080p, 720p, and 540p options.

### How does variable speed work?

iVideo supports playback speed from 0.1× to 8×. You can:

- **Use presets** — 8 built-in speed chips (0.25× / 0.5× / 0.75× / 1× / 1.25× / 1.5× / 2× / 4×).
- **Custom slider** — Drag the slider for any speed between 0.1× and 8×.
- **Recently used** — Your last 2 custom speeds are remembered (LRU).
- **JKL shortcuts** — Press L repeatedly to increase forward speed (1× → 2× → 4× → 8×), J for reverse, K to pause.
- **Pinch to adjust (iPhone)** — Two-finger pinch gesture to scale speed up or down.

Speed preferences persist across sessions and sync via iCloud.

### What are JKL keyboard shortcuts?

JKL is a professional video editing shortcut inspired by Final Cut Pro:

- **J** — Reverse playback, press again to increase reverse speed.
- **K** — Pause and reset speed.
- **L** — Forward playback, press again to increase forward speed.
- **K + J/L** — Hold K while pressing J or L for 0.5× slow speed.

JKL speed is displayed via an on-screen HUD and optionally on the Lock Screen / Dynamic Island via Live Activity (iOS 16.1+).

### How does screen recording work?

- **iOS** — Uses ReplayKit Broadcast Upload Extension. Start from the Record tab; the system shows a Broadcast Picker. Auto-snapshots can be configured in Settings.
- **macOS** — Uses ScreenCaptureKit. Supports multi-display recording and optional system audio capture. First use requires granting Screen Recording permission in System Settings → Privacy & Security.

Screen recording on iOS requires a real device — the Simulator does not support ReplayKit broadcasting.

### What is the Live Activity feature?

When using JKL keyboard shortcuts to control playback, iVideo can display the current speed tier on the Lock Screen and Dynamic Island via iOS Live Activity. This requires:

- iOS 16.1 or later
- Enable in Settings → Appearance → Live Activity toggle
- An external keyboard connected to use JKL shortcuts

### Does iVideo sync data across devices?

iVideo syncs lightweight preferences via iCloud Key-Value Storage:

- Theme, language, playback speed, mute state
- Custom speed history, favorite tools bar

Video files themselves are **not** synced — they stay on each device.

### What does "Metadata Strip" do?

The Metadata Strip tool removes embedded metadata from your video file, including EXIF data, GPS location, device model, and other identifying information. This is useful for privacy when sharing videos publicly.

### How do I use video collage?

1. In the Video Library, multi-select 2–4 videos.
2. Tap the Collage button in the batch action bar.
3. Choose a layout: side-by-side, top-bottom, or 4-grid.
4. The output is a single 1920×1080 video with all inputs playing simultaneously.

Duration equals the shortest input video. Each slot uses aspect-fill with center cropping.

### Can I convert videos to Live Photo or GIF?

Yes. The Live Photo Studio supports bidirectional conversion:

- **Video → Live Photo** — Choose a key frame and duration to create a Live Photo wallpaper.
- **Live Photo → Video / GIF / Still** — Convert with original encoding preserved. Batch mode supports multi-select.

### How do on-device subtitles work?

iVideo generates subtitles entirely on your device using Apple's Speech framework (forced on-device: `requiresOnDeviceRecognition`). No audio is uploaded.

1. Open a video in the Workspace and select the Subtitle tool.
2. Choose a mode: Speech (voice-to-text), Sound Events (music/applause/laughter detection), or Combined.
3. Select a recognition language (60+ languages available; some may require downloading an offline language pack in System Settings).
4. Results appear as editable segments — tap to seek, edit text, or delete.
5. Export as SRT file, ASS subtitle file (with vertical layout support), or burn directly into the video.
6. Bilingual translation is available via Apple Translation framework for an on-device secondary language line.

### How does face blur work?

The Face Blur tool uses Apple's Vision framework to automatically detect faces in every frame and apply Gaussian blur or mosaic (style and intensity adjustable).

For areas that face detection can't catch (license plates, signs, watermarks), use the Manual Region editor to drag and draw custom blur rectangles that apply to the entire video.

All processing happens on-device — no video frames are uploaded.

### What is batch processing?

Batch processing lets you apply the same set of operations to multiple videos at once:

1. In the Video Library, multi-select videos.
2. Choose "Batch Process" from the action bar.
3. Configure a recipe: rotate → speed → mute → watermark → metadata strip → compress (in fixed order).
4. The app processes each video serially. Individual failures don't block the batch.
5. Your last-used recipe is saved for quick reuse.

### What are Edit Projects (multi-track editor)?

Edit Projects is a full non-linear editor, separate from the single-clip tools. Open it from the **Edit Projects** tab in the tab bar.

- **Multi-track timeline** — add clips, split, delete, reorder, crossfade; ruler with drag-to-seek, pinch-to-zoom, multi-frame thumbnails
- **Overlays** — timed text, stickers, or picture-in-picture video, positioned by dragging in the preview
- **Dual audio** — BGM + narration with loop-fill and automatic ducking under speech
- **Per-clip reprocessing** — Stabilize, Smart Reframe (landscape→portrait), Smooth Slow-Mo, Multicam; baked as reversible derived media
- **Canvas ratios** — Original / 9:16 / 1:1 / 4:5 / 16:9
- **Publish Wizard** — platform aspect, cover frame, subtitle burn-in (SRT/ASS) → saved to Library
- **Self-contained** — media is copied into the project, so deleting originals won't break it; undo/redo and debounced auto-save

Preview and export share the same composition, so what you see is what you get.

### How does the export queue work?

iVideo uses a global export queue that processes exports in the background:

- Exports run serially so your device stays responsive.
- iOS background tasks keep exports alive even when you switch apps.
- The queue view (accessible from the library toolbar badge) shows pending, in-progress, completed, and failed items.
- You can share completed exports directly from the queue.
- Optional local notifications alert you when exports finish (configurable in Settings → Export).

### What are export presets?

Export presets save your preferred quality + container combination for one-tap switching:

- **4 built-in presets** cover common scenarios.
- **Custom presets** — Create your own with a name, quality tier, and container format (MP4/MOV).
- Switch presets from the workspace ⋯ menu or Settings → Export.

### How does color grading work?

The Color Grading tool offers 7 adjustable parameters: exposure, brightness, contrast, saturation, vibrance, white balance, and tint. Real-time preview lets you see changes instantly; press and hold to compare with the original.

Additional options:

- **Built-in LUT Pack** — 6 procedurally generated styles (Teal & Orange, Bleach Bypass, Vintage, Cool Shadow, Warm Shadow, High-Contrast B&W).
- **Filter Presets** — 11 built-in presets plus `.cube` 3D LUT file import (Adobe/Resolve format).

### What is speed ramp?

Speed Ramp lets you create keyframe-based variable speed within a single video:

1. Split the timeline into segments at chosen points.
2. Assign a different speed to each segment.
3. A color-band visual editor shows the speed profile at a glance.

This is different from the global speed tool — speed ramp gives you creative control over pacing within a clip.

### How does beat sync montage work?

Beat Sync analyzes your video's audio to detect beats and BPM, then creates a montage where the video cuts on every beat while keeping the audio continuous.

You can choose from 4 stackable transition effects: zoom, slide, flash, and black. Multiple transitions can be combined for creative variety.

### What are social format presets?

Social Format converts your video to common social media aspect ratios (9:16, 1:1, 4:5, 16:9) with three fill modes:

- **Blur Background** — Fills empty space with a blurred version of the video.
- **Solid Color** — Fills with a solid color border.
- **Crop to Fill** — Crops the video to fill the entire frame.

Real-time single-frame preview with safe area guides. Optional caption bar at top or bottom with semi-transparent color band.

### How do I send feedback or report a bug?

Go to Settings → About → Feedback. The app composes an email with your device info (model, OS version, app version, language) pre-filled. If the system Mail app is unavailable, a `mailto:` link opens your default email client.

You can also email us directly at [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com).

### Is iVideo free?

iVideo is free to download. An optional Tip Jar is available to support continued development.

</section>

<section lang="zh-CN" markdown="1">

### iVideo 支持哪些视频格式？

iVideo 支持 iOS 与 macOS 原生可解码的所有格式，包括 MP4、MOV、M4V 等。导出支持 MP4 或 MOV 格式，可自由选择画质档位。

### 我的视频存在哪里？

所有视频都存储在您的设备本地：

- **录屏视频** — 存放在共享的 App Group 容器中。
- **导入视频** — 存放在应用沙盒 Documents/ImportedVideos 文件夹。
- **导出视频** — 存放在应用沙盒 Documents/Exports 文件夹。

没有任何视频数据上传到云端。

### 可以编辑 4K 视频吗？

可以。iVideo 完整支持 4K 视频处理。您可以导入、编辑和导出 4K 视频。导出画质选择器提供超高清（4K）档位，另有原画、2K、1080p、720p 与 540p 可选。

### 变速功能如何使用？

iVideo 支持 0.1× 到 8× 的播放速度。您可以：

- **使用预设** — 8 个内置速度档位（0.25× / 0.5× / 0.75× / 1× / 1.25× / 1.5× / 2× / 4×）。
- **自定义滑块** — 拖动滑块选择 0.1× 到 8× 之间的任意速度。
- **最近使用** — 自动记住最近用过的 2 个自定义速度（LRU）。
- **JKL 快捷键** — 连按 L 加速前进（1× → 2× → 4× → 8×），J 反向，K 暂停。
- **双指捏合（iPhone）** — 双指捏合手势缩放速度。

速度偏好跨会话保留，并通过 iCloud 同步。

### JKL 键盘快捷键是什么？

JKL 是受 Final Cut Pro 启发的专业视频编辑快捷键：

- **J** — 反向播放，再按加速反向。
- **K** — 暂停并重置速度。
- **L** — 正向播放，再按加速正向。
- **K + J/L** — 按住 K 同时按 J 或 L 进入 0.5× 慢速档。

JKL 速度通过屏幕 HUD 浮窗显示，也可在锁屏/灵动岛通过 Live Activity 展示（iOS 16.1+）。

### 录屏功能如何使用？

- **iOS** — 使用 ReplayKit 广播上传扩展。从「录屏」标签启动，系统弹出 Broadcast Picker。可在设置中配置自动截图间隔。
- **macOS** — 使用 ScreenCaptureKit。支持多显示器录屏和可选系统音频捕获。首次使用需在系统设置 → 隐私与安全性 → 屏幕录制中授权。

iOS 录屏需要真机测试，模拟器不支持 ReplayKit 广播。

### Live Activity 功能是什么？

使用 JKL 键盘快捷键控制播放时，iVideo 可以在锁屏与灵动岛通过 iOS Live Activity 显示当前速度档。使用条件：

- iOS 16.1 或更高版本
- 在设置 → 外观中开启「Live Activity」开关
- 连接外接键盘使用 JKL 快捷键

### iVideo 会跨设备同步数据吗？

iVideo 通过 iCloud 键值存储同步轻量偏好：

- 主题、语言、播放速度、静音状态
- 自定义速度档历史、常用工具快捷栏

视频文件本身 **不会** 同步——它们保留在各设备本地。

### 「元数据清除」是做什么的？

元数据清除工具可以移除视频文件中嵌入的元数据，包括 EXIF 数据、GPS 位置、设备型号及其他可识别身份的信息。在公开分享视频时，这对保护隐私非常有用。

### 如何使用视频拼图？

1. 在视频库中多选 2–4 个视频。
2. 点击批量操作栏中的「拼图」按钮。
3. 选择布局：左右、上下或四宫格。
4. 输出为单个 1920×1080 视频，所有输入同时播放。

时长等于最短的输入视频。每个画面使用 aspect-fill 居中裁剪。

### 可以将视频转为 Live Photo 或 GIF 吗？

可以。Live Photo 工作室支持双向转换：

- **视频 → Live Photo** — 选择关键帧与时长，创建 Live Photo 壁纸。
- **Live Photo → 视频/GIF/静图** — 批量转换，保留原始编码。

### 设备端自动字幕如何使用？

iVideo 使用 Apple Speech 框架完全在设备端生成字幕（强制设备端识别：`requiresOnDeviceRecognition`）。不上传任何音频。

1. 在工作台中打开视频并选择「字幕」工具。
2. 选择模式：语音转写（语音→文字）、声音事件（检测音乐/掌声/笑声等）或合并模式。
3. 选择识别语言（60+ 种可用；部分语言可能需要在系统设置中下载离线语言包）。
4. 结果以可编辑条目显示——点击跳转、编辑文本或删除。
5. 导出为 SRT 文件、ASS 字幕文件（支持竖排布局）或烧录进视频。
6. 可通过 Apple Translation 框架进行设备端双语翻译。

### 人脸打码如何使用？

人脸打码工具使用 Apple Vision 框架逐帧自动检测人脸，并施加高斯模糊或马赛克（样式与强度可调）。

对于人脸检测无法命中的区域（车牌、招牌、水印等），可使用手动框选编辑器拖拽绘制矩形打码区域，应用于整段视频。

全程在设备本地处理——不上传任何视频画面。

### 什么是批处理？

批处理允许您对多个视频批量套用同一组操作：

1. 在视频库中多选视频。
2. 从操作栏选择「批处理」。
3. 配置配方：旋转 → 变速 → 去音轨 → 水印 → 清元数据 → 压缩（固定顺序）。
4. 应用逐个串行处理，单个失败不阻断整批。
5. 上次使用的配方自动保存，下次快速复用。

### 什么是剪辑工程（多轨编辑器）？

剪辑工程是完整的非线性编辑器，独立于单视频工具，入口在底部 **剪辑工程** 标签。

- **多轨时间线** — 添加片段、分割、删除、换序、叠化；刻度尺拖动 seek、双指缩放、多帧缩略图
- **叠加层** — 定时文字、贴图或画中画视频，预览拖拽定位
- **双轨音频** — BGM + 旁白，循环铺满 + 说话区间自动闪避
- **逐片段重处理** — 画面稳定、智能构图（横→竖）、平滑慢动作、双机位；烘焙为可回退派生媒体
- **画布比例** — 原始 / 9:16 / 1:1 / 4:5 / 16:9
- **发布向导** — 平台画幅、封面帧、字幕烧录（SRT/ASS）→ 存入视频库
- **自包含** — 片段拷入工程，删原片不断链；支持撤销/重做与防抖自动保存

预览与导出共用同一合成，所见即所得。

### 导出队列如何运作？

iVideo 使用全局导出队列在后台处理导出任务：

- 导出串行执行，确保设备响应流畅。
- iOS 后台任务保持导出在切换应用后继续运行。
- 队列视图（从视频库工具栏角标进入）展示排队中、进行中、已完成和失败的任务。
- 已完成的导出可直接从队列分享。
- 可选本地通知在导出完成时提醒（在设置 → 导出中配置）。

### 什么是导出预设？

导出预设保存您偏好的「画质 + 容器」组合，一键切换：

- **4 个内建预设** 覆盖常见场景。
- **自定义预设** — 创建自己的预设，包含名称、画质档位与容器格式（MP4/MOV）。
- 在工作台 ⋯ 菜单或设置 → 导出中切换。

### 调色功能如何使用？

调色工具提供 7 个可调参数：曝光、亮度、对比度、饱和度、自然饱和度、色温与色调。实时预览即时查看效果，按住可对比原图。

额外选项：

- **内置 LUT 包** — 6 种程序化生成的调色风格（青橙、漂白、复古、冷影、暖影、高反黑白）。
- **滤镜预设** — 11 种内建预设，支持导入 `.cube` 3D LUT 文件（Adobe/Resolve 格式）。

### 什么是变速曲线？

变速曲线让您在单个视频中创建基于关键帧的分段变速：

1. 在选定的位置将时间线分段。
2. 为每个段设置不同的速度。
3. 色带式可视化编辑器直观展示速度分布。

这与全局变速工具不同——变速曲线让您对单个片段的节奏拥有创意控制。

### 卡点混剪如何使用？

卡点混剪分析视频音频中的节拍和 BPM，然后创建画面随节拍跳切、音乐连续的混剪效果。

可选 4 种可叠加的转场效果：缩放、滑入、闪白与黑场。多种转场可自由组合。

### 什么是社媒画幅预设？

社媒画幅将视频转换为常见社交媒体比例（9:16 / 1:1 / 4:5 / 16:9），提供三种填充模式：

- **模糊背景** — 用模糊版本的视频填充空白区域。
- **纯色边** — 用纯色填充边框。
- **裁剪填满** — 裁剪视频以完全填充画面。

实时单帧预览带安全区参考线。可选字幕条（顶/底），带半透明色条。

### 如何发送反馈或报告 Bug？

前往设置 → 关于 → 反馈。应用会生成一封预填设备信息（型号、系统版本、应用版本、语言）的邮件。若系统邮件不可用，则通过 `mailto:` 链接打开默认邮件客户端。

您也可以直接发邮件至 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)。

### iVideo 免费吗？

iVideo 免费下载。应用内提供可选打赏功能以支持持续开发。

</section>

<section lang="zh-TW" markdown="1">

### iVideo 支援哪些影片格式？

iVideo 支援 iOS 與 macOS 原生可解碼的所有格式，包括 MP4、MOV、M4V 等。匯出支援 MP4 或 MOV 格式，可自由選擇畫質檔位。

### 我的影片存在哪裡？

所有影片都儲存在您的裝置本地：

- **錄屏影片** — 存放在共享的 App Group 容器中。
- **匯入影片** — 存放在應用沙盒 Documents/ImportedVideos 資料夾。
- **匯出影片** — 存放在應用沙盒 Documents/Exports 資料夾。

沒有任何影片資料上傳到雲端。

### 可以編輯 4K 影片嗎？

可以。iVideo 完整支援 4K 影片處理。您可以匯入、編輯和匯出 4K 影片。匯出畫質選擇器提供超高清（4K）檔位，另有原畫、2K、1080p、720p 與 540p 可選。

### 變速功能如何使用？

iVideo 支援 0.1× 到 8× 的播放速度。您可以：

- **使用預設** — 8 個內建速度檔位（0.25× / 0.5× / 0.75× / 1× / 1.25× / 1.5× / 2× / 4×）。
- **自訂滑桿** — 拖動滑桿選擇 0.1× 到 8× 之間的任意速度。
- **最近使用** — 自動記住最近用過的 2 個自訂速度（LRU）。
- **JKL 快捷鍵** — 連按 L 加速前進（1× → 2× → 4× → 8×），J 反向，K 暫停。
- **雙指捏合（iPhone）** — 雙指捏合手勢縮放速度。

速度偏好跨工作階段保留，並透過 iCloud 同步。

### JKL 鍵盤快捷鍵是什麼？

JKL 是受 Final Cut Pro 啟發的專業影片編輯快捷鍵：

- **J** — 反向播放，再按加速反向。
- **K** — 暫停並重設速度。
- **L** — 正向播放，再按加速正向。
- **K + J/L** — 按住 K 同時按 J 或 L 進入 0.5× 慢速檔。

JKL 速度透過螢幕 HUD 浮窗顯示，也可在鎖定畫面/靈動島透過 Live Activity 展示（iOS 16.1+）。

### 錄屏功能如何使用？

- **iOS** — 使用 ReplayKit 廣播上傳延伸功能。從「錄屏」標籤啟動，系統彈出 Broadcast Picker。可在設定中配置自動截圖間隔。
- **macOS** — 使用 ScreenCaptureKit。支援多顯示器錄屏和可選系統音訊擷取。首次使用需在系統設定 → 隱私與安全性 → 螢幕錄製中授權。

iOS 錄屏需要真機測試，模擬器不支援 ReplayKit 廣播。

### Live Activity 功能是什麼？

使用 JKL 鍵盤快捷鍵控制播放時，iVideo 可以在鎖定畫面與靈動島透過 iOS Live Activity 顯示目前速度檔。使用條件：

- iOS 16.1 或更高版本
- 在設定 → 外觀中開啟「Live Activity」開關
- 連接外接鍵盤使用 JKL 快捷鍵

### iVideo 會跨裝置同步資料嗎？

iVideo 透過 iCloud 鍵值儲存同步輕量偏好：

- 主題、語言、播放速度、靜音狀態
- 自訂速度檔歷史、常用工具快捷列

影片檔案本身 **不會** 同步——它們保留在各裝置本地。

### 「中繼資料清除」是做什麼的？

中繼資料清除工具可以移除影片檔案中嵌入的中繼資料，包括 EXIF 資料、GPS 位置、裝置型號及其他可識別身分的資訊。在公開分享影片時，這對保護隱私非常有用。

### 如何使用影片拼圖？

1. 在影片庫中多選 2–4 個影片。
2. 點擊批次操作列中的「拼圖」按鈕。
3. 選擇佈局：左右、上下或四宮格。
4. 輸出為單個 1920×1080 影片，所有輸入同時播放。

時長等於最短的輸入影片。每個畫面使用 aspect-fill 居中裁剪。

### 可以將影片轉為 Live Photo 或 GIF 嗎？

可以。Live Photo 工作室支援雙向轉換：

- **影片 → Live Photo** — 選擇關鍵幀與時長，建立 Live Photo 桌布。
- **Live Photo → 影片/GIF/靜圖** — 批次轉換，保留原始編碼。

### 裝置端自動字幕如何使用？

iVideo 使用 Apple Speech 框架完全在裝置端產生字幕（強制裝置端辨識：`requiresOnDeviceRecognition`）。不上傳任何音訊。

1. 在工作台中開啟影片並選擇「字幕」工具。
2. 選擇模式：語音轉寫（語音→文字）、聲音事件（偵測音樂/掌聲/笑聲等）或合併模式。
3. 選擇辨識語言（60+ 種可用；部分語言可能需要在系統設定中下載離線語言包）。
4. 結果以可編輯條目顯示——點擊跳轉、編輯文字或刪除。
5. 匯出為 SRT 檔案、ASS 字幕檔案（支援直排佈局）或燒錄進影片。
6. 可透過 Apple Translation 框架進行裝置端雙語翻譯。

### 人臉打碼如何使用？

人臉打碼工具使用 Apple Vision 框架逐幀自動偵測人臉，並施加高斯模糊或馬賽克（樣式與強度可調）。

對於人臉偵測無法命中的區域（車牌、招牌、浮水印等），可使用手動框選編輯器拖曳繪製矩形打碼區域，應用於整段影片。

全程在裝置本地處理——不上傳任何影片畫面。

### 什麼是批次處理？

批次處理允許您對多個影片批次套用同一組操作：

1. 在影片庫中多選影片。
2. 從操作列選擇「批次處理」。
3. 配置配方：旋轉 → 變速 → 去音軌 → 浮水印 → 清中繼資料 → 壓縮（固定順序）。
4. 應用逐個串行處理，單個失敗不阻斷整批。
5. 上次使用的配方自動儲存，下次快速複用。

### 什麼是剪輯工程（多軌編輯器）？

剪輯工程是完整的非線性編輯器，獨立於單影片工具，入口在底部 **剪輯工程** 標籤。

- **多軌時間線** — 加入片段、分割、刪除、換序、疊化；刻度尺拖動 seek、雙指縮放、多幀縮圖
- **疊加層** — 定時文字、貼圖或子母畫面影片，預覽拖曳定位
- **雙軌音訊** — BGM + 旁白，循環鋪滿 + 說話區間自動閃避
- **逐片段重處理** — 畫面穩定、智能構圖（橫→豎）、平滑慢動作、雙機位；烘焙為可回退派生媒體
- **畫布比例** — 原始 / 9:16 / 1:1 / 4:5 / 16:9
- **發布嚮導** — 平台畫幅、封面幀、字幕燒錄（SRT/ASS）→ 存入影片庫
- **自包含** — 片段拷入工程，刪原片不斷鏈；支援撤銷/重做與防抖自動保存

預覽與匯出共用同一合成，所見即所得。

### 匯出佇列如何運作？

iVideo 使用全域匯出佇列在後台處理匯出任務：

- 匯出串行執行，確保裝置回應流暢。
- iOS 後台任務保持匯出在切換應用後繼續運行。
- 佇列檢視（從影片庫工具列角標進入）展示排隊中、進行中、已完成和失敗的任務。
- 已完成的匯出可直接從佇列分享。
- 可選本地通知在匯出完成時提醒（在設定 → 匯出中配置）。

### 什麼是匯出預設？

匯出預設儲存您偏好的「畫質 + 容器」組合，一鍵切換：

- **4 個內建預設** 覆蓋常見場景。
- **自訂預設** — 建立自己的預設，包含名稱、畫質檔位與容器格式（MP4/MOV）。
- 在工作台 ⋯ 選單或設定 → 匯出中切換。

### 調色功能如何使用？

調色工具提供 7 個可調參數：曝光、亮度、對比度、飽和度、自然飽和度、色溫與色調。即時預覽即時查看效果，按住可對比原圖。

額外選項：

- **內建 LUT 包** — 6 種程式化生成的調色風格（青橙、漂白、復古、冷影、暖影、高反黑白）。
- **濾鏡預設** — 11 種內建預設，支援匯入 `.cube` 3D LUT 檔案（Adobe/Resolve 格式）。

### 什麼是變速曲線？

變速曲線讓您在單個影片中建立基於關鍵幀的分段變速：

1. 在選定的位置將時間線分段。
2. 為每個段設定不同的速度。
3. 色帶式視覺化編輯器直觀展示速度分佈。

這與全域變速工具不同——變速曲線讓您對單個片段的節奏擁有創意控制。

### 卡點混剪如何使用？

卡點混剪分析影片音訊中的節拍和 BPM，然後建立畫面隨節拍跳切、音樂連續的混剪效果。

可選 4 種可疊加的轉場效果：縮放、滑入、閃白與黑場。多種轉場可自由組合。

### 什麼是社媒畫幅預設？

社媒畫幅將影片轉換為常見社群媒體比例（9:16 / 1:1 / 4:5 / 16:9），提供三種填充模式：

- **模糊背景** — 用模糊版本的影片填充空白區域。
- **純色邊** — 用純色填充邊框。
- **裁剪填滿** — 裁剪影片以完全填充畫面。

即時單幀預覽帶安全區參考線。可選字幕條（頂/底），帶半透明色條。

### 如何傳送回饋或回報 Bug？

前往設定 → 關於 → 回饋。應用程式會產生一封預填裝置資訊（型號、系統版本、應用版本、語言）的郵件。若系統郵件不可用，則透過 `mailto:` 連結開啟預設郵件用戶端。

您也可以直接寄信至 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)。

### iVideo 免費嗎？

iVideo 免費下載。應用內提供可選打賞功能以支持持續開發。

</section>
