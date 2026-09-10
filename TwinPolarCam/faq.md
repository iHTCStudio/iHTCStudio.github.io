---
layout: doc
title: TwinPolarCam — FAQ
app_id: TwinPolarCam
doc_title_en: Frequently Asked Questions
doc_title_zh_cn: 常见问题
doc_title_zh_tw: 常見問題
description: Comprehensive FAQ for TwinPolarCam — device support, recording, PiP, interruptions, export, permissions, and troubleshooting.
last_updated: 2026-07-11
---

<section lang="en" markdown="1">

Answers reflect **current app behavior** (recoverable pause/resume, export queue, Live Activity, device gate, Traditional Chinese, in-app guides). For step-by-step walkthroughs see the [User Guide](index).

---

## Device & requirements

### Which iPhones support TwinPolarCam?

TwinPolarCam requires **`AVCaptureMultiCamSession`** — Apple's simultaneous multi-camera API. Supported devices typically include **iPhone XS, iPhone XR, and all later models**, but exact capability depends on hardware generation.

- **Unsupported devices** see a dedicated screen at launch — the camera UI and permission flow do not start.
- **iOS Simulator is not supported** — no physical cameras, no Multi-Cam.
- A **real iPhone** is required.

### Why doesn't TwinPolarCam fall back to single-camera mode?

Dual-camera simultaneous recording is the core product. Single-camera fallback was removed to avoid confusion and unsupported expectations. If your device fails the capability check, use the **refund** option on the unsupported screen or contact support.

### What is the maximum recording resolution?

TwinPolarCam offers **720p, 1080p, 2K, and 4K** per camera (main and PiP independently). Maximum depends on device:

- **iPhone 12 and later** — 4K dual capture is generally available.
- **Older Multi-Cam models** — may cap at 1080p or 2K for one or both lenses.

Unavailable resolutions are **disabled in settings** automatically.

### Why is 60 fps not available?

Apple's multi-camera pipeline limits most devices to **30 fps maximum** when both cameras record simultaneously. TwinPolarCam offers **24 fps and 30 fps**. **60 fps is not supported** — this is a system/hardware constraint, not an arbitrary app limit.

### Can I run TwinPolarCam on iPad or Mac?

**No.** TwinPolarCam is **iPhone-only**.

### What iOS version do I need?

- **Minimum: iOS 15.0**
- **Live Activity: iOS 16.2+**
- **Widget Extension** (Live Activity UI): bundled with app, same OS requirement for Live Activity features

---

## Recording & PiP

### How do I switch which camera is the main view?

Tap the **switch / flip control** during preview or recording. Front and back **roles swap on screen** — both video tracks continue recording regardless of which is displayed full-screen.

### Can I customize the PiP overlay?

Yes:

- **Drag** to move
- **Pinch** to resize (or use scale in PiP settings)
- Adjust **border width, color, corner radius, opacity, and relative size** in **App Settings → Picture-in-Picture**

Changes preview live and are **burned into the exported video**.

### Does PiP position appear in the exported video?

**Yes.** The composer uses your saved scale, normalized position, corner radius, border, and opacity.

### Can I record in portrait?

The **camera interface is optimized for landscape**. You may enable **portrait lock** for Settings or Pending panels, but dual preview and recording work best **horizontally**.

### What is preview pause?

**Preview pause** freezes the **live camera preview** (not recording) so you can adjust PiP or zoom without the image moving. It is **not available during an active recording** — use **recording pause** instead.

### How do zoom presets work?

Pinch or use the on-screen zoom control, then **save the current level as a preset**. Recall presets to reframe quickly. Zoom applies to the **main camera preview when not recording**.

### What does the screenshot button do?

Captures the **current composed main + PiP layout** as a still image and saves directly to **Photos** — works during preview or recording, no export step needed.

### When does the flashlight appear?

When the **back camera is the main view**. During recording, the flashlight button **replaces** the camera switch button on the control arc.

---

## Interruptions & reliability

### What happens if I receive a phone call while recording?

TwinPolarCam **pauses** recording during the call. When the call ends, recording **auto-resumes on the same segment** (same `.mov` file) — **unless you had manually paused** before the call.

Paused time is **cut from the output timeline** (not exported as frozen frames).

### Does pulling down Control Center pause recording?

**No.** Only **full backgrounding** (Home gesture, app switch, lock screen) triggers the background interruption path — not `willResignActive` alone (e.g. Control Center overlay).

### What happens if I switch apps or lock the screen while recording?

1. Recording **pauses**
2. A **background task** keeps the writer briefly alive
3. **Live Activity** may appear (if enabled) with elapsed time and auto-save countdown
4. After **~25 seconds**, the app **proactively saves** the segment to **Pending Exports**
5. If you **return before timeout**, you can **resume** the same segment

### What is emergency save?

A last-resort finalize when the app cannot keep writing:

- Background safety timeout (~25 s)
- App termination (up to ~8 s wait)
- Writer failure, append errors

You get a **toast notification**. Clips land in **Pending**. **Emergency save ends the session** — you cannot resume that segment.

### What's the difference between recoverable and fatal interruptions?

| Type | Examples | Result |
|------|----------|--------|
| **Recoverable** | Call, Siri, brief camera steal, backgrounding | Pause → resume **same segment** |
| **Fatal / emergency** | Media reset, runtime error, disk full, timeout | Finalize → **Pending**, session ends |

### Will pause create a gap in the video?

**Yes — by design.** Paused intervals are **omitted** (PTS jump-cut). The exported file plays continuously without long frozen sections.

### How does crash recovery work?

If the app terminates unexpectedly, **valid finalized segments** remain on disk. On next launch, TwinPolarCam detects recoverable files and can place them in **Pending** with an alert. Use **Rescan Cache** in Pending if needed.

### Why is the screen always on while recording?

Recording **forces keep-awake** regardless of your **Keep Screen Awake** preference — preventing accidental lock mid-shoot. Export queue also keeps the screen on until finished.

### Does Low Power Mode affect recording?

It can increase **background pressure** and thermal throttling. For long sessions, use lower resolution, avoid charging heat, or plug in.

---

## Live Activity

### What is Recording Live Activity?

On **iOS 16.2+**, when you leave the app while a recording session is active, a **Lock Screen / Dynamic Island** widget shows status:

- **Background waiting** — elapsed time + auto-save countdown
- **Saved** — footage secured after background auto-save (until you reopen the app)

### How do I turn Live Activity off?

**App Settings → General → Recording Live Activity**. Reliability is unchanged — only Lock Screen visibility is affected.

### Why does Live Activity stay after auto-save?

After successful **background auto-save**, the activity may show **Saved** so you know footage is safe. It ends when you return to the app (foreground).

---

## Export & Pending

### What export modes are available?

| Mode | Behavior |
|------|----------|
| **Auto Export ON** | Stop → compose + save to Photos immediately |
| **Auto Export OFF** | Stop → original `.mov` in **Pending** until you export manually |

### How does the export queue work?

Batch export is **serial** — one compose + save at a time, **oldest Pending clip first**. This keeps the device stable under heavy 4K load. The next task starts automatically when the current one finishes.

### Can I cancel export?

Yes:

- **Cancel** a single in-progress task
- **Cancel All** — stops active + queued tasks, removes temp mp4 files
- **Original `.mov` files remain** in Pending for retry

### What files appear in Pending?

Only original **`TwinPolarCam_*.mov`** multi-track recordings — not temporary composed `TwinPolarCam_MultiCam_*.mp4` files.

### Can I change PiP style and re-export?

**Yes**, if **Auto-Delete Original After Export** is **off** (default). Adjust PiP settings, then export again from Pending.

### Why is export taking a long time?

4K dual-track composition is **CPU/GPU intensive**. Longer clips and higher frame rates take more time. The screen stays on automatically until the queue completes.

### Export failed — is my video lost?

**No.** The original `.mov` stays in Pending. Check **free storage** and **Photos permission** (Add Only), then retry.

### Where are files stored before export?

`Application Support/TwinPolarCam/Videos/` — excluded from **iCloud Backup** by design.

### What's the output format?

Composed **H.264 / AAC mp4** at high quality; frame duration follows your **main camera frame rate** setting.

### Can I export while recording a new clip?

The export pipeline can run while you start a new session, but **simultaneous heavy load** may cause heat — sequential use is safer.

---

## Settings & language

### What languages does the app support?

**English**, **简体中文**, and **繁體中文** — **App Settings → General → Language**.

### What does Auto-Delete Original After Export do?

When **ON**, the original `.mov` is removed from Pending after a **successful** Photos save. When **OFF** (default), you keep the multi-track source for re-composition.

Default is **OFF** so upgrading users aren't surprised by missing originals.

### Why does my music pause when I start recording?

TwinPolarCam activates the audio session on record start (like Apple's Camera app) for **exclusive microphone capture** — preventing speaker audio from being recorded. Music resumes when recording stops (`notifyOthersOnDeactivation`).

Browsing the app **without recording** does **not** interrupt music.

### How do appearance modes work?

**System / Light / Dark** in General settings — applies immediately across the app via `preferredColorScheme`.

---

## Permissions & privacy

### Does TwinPolarCam collect my data?

**No.** All capture, composition, and storage happen on device. No analytics SDK, no account, no upload. See [Privacy Policy](privacy).

### Why does TwinPolarCam only ask to Add Photos?

**Add Only** permission (iOS 14+) lets the app save finished videos **without reading** your existing library — minimum access, higher trust.

### Are my videos backed up to iCloud?

Original recordings in app storage are marked **excluded from backup**. Exported videos in Photos follow **your** Photos/iCloud settings.

---

## Tips & support

### How do I send feedback?

**App Settings → Send Feedback** (Mail) or `twinpolarcam://feedback`.

### Where are the in-app guides?

**App Settings → Help** — How to Use, Recording & Reliability, Export & Pending, Feature Tour.

### How do I open guides from outside the app?

Home Screen **long-press quick actions**, **Spotlight** search, or **`twinpolarcam://`** links — see [Shortcut Links](url-scheme).

### Still need help?

Email [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — we typically respond within 48 hours.

[User Guide](index) · [Shortcut Links](url-scheme) · [Privacy Policy](privacy)

---

## Complete User Guide

The sections below are the full product walkthrough previously on the support page. Quick Q&A items remain above (if any).

---

## On this page

| Part | Topic |
|------|--------|
| [Part 1](#part-1) | First launch, permissions, unsupported devices |
| [Part 2](#part-2) | Record, pause, screenshot, switch, flash, preview pause |
| [Part 3](#part-3) | Main camera & PiP quality and styling |
| [Part 4](#part-4) | Audio quality, format, channels |
| [Part 5](#part-5) | Start → stop workflow, timer, orientation |
| [Part 6](#part-6) | Interruptions, background save, Live Activity |
| [Part 7](#part-7) | Compose pipeline, queue, batch export, cancel |
| [Part 8](#part-8) | Appearance, screen awake, export toggles, language |
| [Part 9](#part-9) | In-app guides, Spotlight, quick actions, deep links |
| [Part 10](#part-10) | Symptom → cause → fix quick reference |

> **Need a quick answer?** Jump to [FAQ](faq) or [Shortcut Links](url-scheme).

---

## Part 1 — First Launch & Requirements {#part-1}

### Welcome guide (6 pages)

On first launch, a **6-page onboarding** introduces dual capture, PiP, export, reliability, and privacy. Swipe horizontally or use **Continue**; tap **Start Recording** on the last page.

Replay anytime: **App Settings → Help → Feature Tour**, or `twinpolarcam://feature-guide`.

The last onboarding page can open the in-app **How to Use** guide directly.

### Permissions (required)

| Permission | When asked | Why |
|------------|------------|-----|
| **Camera** | First launch on supported devices | Dual video capture |
| **Microphone** | Before first recording | Audio track |
| **Photos (Add Only)** | First export to library | Save finished videos — **does not read** your existing library |

TwinPolarCam uses **Add Only** photo access (iOS 14+). The app never uploads footage.

### Device requirements

| Requirement | Detail |
|-------------|--------|
| **Hardware** | iPhone with Apple **Multi-Cam** support (`AVCaptureMultiCamSession`) — typically **iPhone XS / XR and later** (varies by model) |
| **Platform** | **Real iPhone only** — iOS Simulator has no camera / Multi-Cam |
| **Minimum OS** | iOS **15.0+** (Live Activity requires **iOS 16.2+**) |
| **Orientation** | Camera screen optimized for **landscape**; some panels can lock portrait |

### Unsupported device screen

If your iPhone **cannot run dual-camera mode**, TwinPolarCam shows a **dedicated notice** instead of the camera UI — **no camera or Photos permission prompts** on that screen.

You can still:

- Read all in-app guides (Usage / Recording / Export)
- Request an **App Store refund** (StoreKit 2) when available
- Contact support

> **Important:** TwinPolarCam **no longer falls back to single-camera mode**. Unsupported hardware is blocked at launch by design.

### In-app languages

**English**, **简体中文**, and **繁體中文** — switch in **App Settings → General → Language**. Changes apply immediately. This support website is also available in all three languages.

---

## Part 2 — Main Screen & Controls {#part-2}

Hold the phone in **landscape** for the widest dual preview. The control column sits on one edge; the main view shows one camera, the **PiP overlay** shows the other.

### Control reference

| Control | When available | What it does |
|---------|----------------|--------------|
| **Record** | Preview (not recording) | Starts dual-camera capture + audio |
| **Pause / Resume** | While recording or paused | Pauses frame writing; timer freezes |
| **Stop** | While recording or paused | Finalizes segment → export or Pending |
| **Switch camera** | Preview or recording | Swaps which lens is main vs PiP (both keep recording) |
| **Screenshot** | Preview or recording | Saves composed frame to Photos instantly |
| **Flashlight** | Back camera is main | Toggles torch (replaces switch button while recording) |
| **Preview pause** | Preview only (not while recording) | Freezes live preview to adjust PiP/zoom without motion |
| **Settings** | Always | Opens App Settings panel |
| **Pending Exports** | Always | Opens unexported `.mov` list |

### Gestures

- **Drag PiP** — reposition overlay anywhere on preview (saved between sessions)
- **Pinch PiP** — resize overlay (also configurable in settings)
- **Pinch main preview** — zoom main camera when **not recording**
- **Zoom presets** — save/recall zoom levels from the zoom control widget

### Preview pause vs recording pause

| | Preview pause | Recording pause |
|---|---------------|-----------------|
| **Trigger** | Preview toggle button | Pause button during recording |
| **Preview** | Frozen | May still show last frame |
| **Writer** | Not active | Open but not appending |
| **Resume** | Tap resume preview | Tap resume recording |

Preview pause is for **composition**; recording pause **excludes time from the output** (PTS jump-cut — no frozen frames in export).

---

## Part 3 — Camera & PiP Settings {#part-3}

Open **App Settings** (gear icon). Four tabs: **Main Camera · Picture-in-Picture · Audio · General**.

Settings that affect **live preview** (resolution, frame rate, stabilization, HDR, night mode on each camera) update immediately. **Audio** settings apply on the **next** recording without interrupting preview.

### Main Camera tab

| Setting | Options | Notes |
|---------|---------|-------|
| Resolution | 720p / 1080p / 2K / 4K | Unavailable options disabled per device |
| Quality | Low / Medium / High | Bitrate trade-off |
| Frame rate | 24 / 30 fps | Multi-Cam typically max **30 fps** — no 60 fps |
| Stabilization | Off / Standard / Cinematic | Per-lens |
| HDR | Off / On / Auto | Per-lens |
| Night mode | Off / On / Auto | Per-lens |
| Reset | Per-tab | Restores main camera defaults |

### Picture-in-Picture tab

Same video parameters as main, plus **UI styling**:

| Setting | Range / options |
|---------|-----------------|
| Scale | 10%–100% of short edge |
| Position | Drag on preview (normalized coordinates saved) |
| Border width | Adjustable |
| Border color | Presets + custom |
| Corner radius | Adjustable |
| Opacity | 0–100% |

**Tip:** Lower PiP resolution while keeping main at 4K reduces heat and storage. A light border helps PiP stand out on busy backgrounds.

All PiP styling is applied in the **final exported video**, not just on screen.

---

## Part 4 — Audio Settings {#part-4}

| Setting | Options |
|---------|---------|
| Quality | Low (voice) / Standard / High (music) / Lossless |
| Format | AAC / PCM |
| Channels | Mono / Stereo |

> TwinPolarCam **does not activate** the audio session until you **start recording** — browsing settings won't pause your music. When recording starts, other audio pauses (same as system Camera) so speaker bleed isn't captured.

---

## Part 5 — Recording a Session {#part-5}

### Typical workflow

1. **Grant permissions** if prompted.
2. **Adjust** main/PiP settings and position PiP.
3. Tap **Record** — screen stays awake; audio session activates; timer starts.
4. **Optional:** pause, switch main/PiP, screenshot, zoom (when not recording).
5. Tap **Stop** — segment finalized to app storage (`TwinPolarCam_*.mov`).
6. **Auto Export ON** → compose + save to Photos immediately.
7. **Auto Export OFF** → clip appears in **Pending Exports** for review.

### Recording timer

The timer shows **effective recording time**:

- Counts only while frames are actively written
- **Freezes** on user pause and recoverable interruption pause
- Resets when the session fully ends
- Live Activity shows the same elapsed value when backgrounded

### Orientation behavior

| Screen | Default orientation |
|--------|---------------------|
| Camera preview / recording | **Landscape** enforced |
| App Settings | Landscape, or **portrait lock** if enabled in General |
| Pending Exports | Landscape, or **portrait lock** if enabled in General |

Layout direction follows container size + your lock settings — independent of how you physically hold the phone in locked panels.

### What gets saved when you stop

Each stop produces an **original multi-track `.mov`**:

- Track 0: back camera video
- Track 1: front camera video
- One audio track

Stored under `Application Support/TwinPolarCam/Videos/` — **excluded from iCloud Backup** by design.

---

## Part 6 — Recording Reliability {#part-6}

TwinPolarCam includes an **Interruption Coordinator** that classifies events and protects footage.

### Before you record

- Leave **several GB** free — dual 4K tracks fill storage fast
- Close other **camera apps**
- Consider **1080p PiP** for long sessions if device gets warm
- Enable **Recording Live Activity** (General) to see Lock Screen status when backgrounded

### Recoverable interruptions (pause → resume, **same segment**)

| Event | Behavior |
|-------|----------|
| Phone call / Siri | Recording pauses; **auto-resumes** when call ends (if you didn't manually pause) |
| Another app briefly takes camera | Pauses; may resume when released |
| App **enters background** (Home, app switch, lock) | Pauses; **25 s safety timer** starts |

The **writer stays open** — frames continue on the **same file** after resume. Paused time is **omitted** from output (jump-cut), not exported as frozen frames.

> **Control Center alone does NOT pause recording** — only full backgrounding triggers the background path.

### Non-recoverable events (save to Pending)

| Event | Behavior |
|-------|----------|
| Media services reset | Session finalized → Pending |
| Capture runtime error / overheating shutdown | Saved if possible → Pending |
| Writer failure (disk full, I/O error) | Emergency save → toast |

### Emergency save

Last-resort protection when time runs out:

| Trigger | Action |
|---------|--------|
| **~25 s** in background while paused | Proactively seals file → Pending |
| App termination | Up to **~8 s** to finalize |
| Append failure / writer `.failed` | Immediate save attempt |

After **background auto-save succeeds**, Live Activity may show **Saved** until you return to the app (if Live Activity enabled).

**Emergency save ends the session** — you cannot resume that segment; start a new recording for more footage.

### Live Activity (iOS 16.2+)

When recording continues into background:

| Phase | Lock Screen / Dynamic Island shows |
|-------|-------------------------------------|
| **Background waiting** | Elapsed time + auto-save countdown |
| **Saved** | Clip secured — tap to return to app |

Toggle: **App Settings → General → Recording Live Activity** (default **on**). Disabling does not affect reliability — only Lock Screen presence.

Full detail also in **App Settings → Help → Recording & Reliability**.

---

## Part 7 — Export & Pending Manager {#part-7}

### Export pipeline

Every export follows the same steps:

1. **Original `.mov`** — multi-track file from stop/emergency save
2. **Compose** — `MultiCamVideoComposer` builds main (back) + PiP (front) → temporary `.mp4`
3. **Save** — writes to Photos (Add Only permission)
4. **Cleanup** — removes temp mp4; optionally deletes original `.mov`
5. **Next in queue** — oldest Pending item exports automatically if queued

Frame rate in export follows your **main camera** setting. PiP scale, position, border, radius, and opacity from settings are baked in.

### Pending Exports manager

Open from the **Pending** button on the camera screen or `twinpolarcam://pending`.

| Feature | Detail |
|---------|--------|
| **Contents** | Original `TwinPolarCam_*.mov` only — not temp composed files |
| **Sort** | Creation time — **oldest first** for export priority |
| **Layout** | **List** or **Grid** — column count 2–6 (General setting) |
| **Preview** | Tap to play multi-track clip before exporting |
| **Rescan Cache** | Refreshes list if files exist on disk but UI is empty |
| **Share** | Share individual clips from Pending |
| **Delete** | Remove unwanted originals |

### Batch export & queue

- **Export** one clip, **selected** clips, or **Export All**
- First task runs immediately; others enter a **serial queue** (one compose + save at a time — stable on device)
- **Screen stays awake** until queue finishes
- **Cancel** single task or **Cancel All** — stops compose/save, clears temp mp4; originals remain in Pending

### Export settings (General tab)

| Toggle | Default | Effect |
|--------|---------|--------|
| **Auto Export** | Varies | On stop → immediate compose + Photos save |
| **Auto-Delete Original After Export** | **Off** | Removes `.mov` from Pending after successful Photos save |

Keep **Auto-Delete OFF** if you may re-export with different PiP styling.

Full detail in **App Settings → Help → Export & Pending**.

---

## Part 8 — General Settings {#part-8}

| Section | Options |
|---------|---------|
| **Appearance** | System / Light / Dark — applies app-wide immediately |
| **Keep Screen Awake** | While using app (recording/export always keep awake regardless) |
| **Recording Live Activity** | Lock Screen + Dynamic Island status (iOS 16.2+) |
| **Portrait Lock for Settings** | Rotate to portrait when opening App Settings |
| **Portrait Lock for Pending** | Rotate to portrait when opening Pending Exports |
| **Auto Export** | See Part 7 |
| **Auto-Delete Original** | See Part 7 |
| **Language** | English / 简体中文 / 繁體中文 |
| **Tip Developer** | Optional StoreKit 2 in-app tip |
| **Send Feedback** | Opens Mail composer |
| **Reset All Settings** | Confirmation required — does not delete Pending videos |

### About & App info

**App Settings → App Information:**

- Rate in App / Rate on App Store
- Share App
- **About TwinPolarCam** — version, privacy summary, links

---

## Part 9 — Help, Guides & Shortcuts {#part-9}

### In-app guides (Settings → Help)

| Guide | Contents |
|-------|----------|
| **How to Use** | Quick start, controls, PiP, export overview |
| **Recording & Reliability** | Interruptions, background, Live Activity, FAQ |
| **Export & Pending** | Pipeline, queue, batch, Photos permission |
| **Feature Tour** | Replay 6-page onboarding |

### Home Screen quick actions

**Long-press the app icon** — four fixed shortcuts:

| Action | Deep link |
|--------|-----------|
| Usage Guide | `twinpolarcam://usage-guide` |
| Recording Tips | `twinpolarcam://recording-guide` |
| Export Guide | `twinpolarcam://export-guide` |
| Feature Tour | `twinpolarcam://feature-guide` |

### Spotlight

Search **"TwinPolarCam"** or guide titles on device — indexed guides open the corresponding sheet.

### Other deep links

| URL | Opens |
|-----|-------|
| `twinpolarcam://settings` | App Settings panel |
| `twinpolarcam://pending` | Pending Exports |
| `twinpolarcam://feedback` | Feedback email |
| `twinpolarcam://recording` | Return from Live Activity |

Full reference: [Shortcut Links](url-scheme).

---

## Part 10 — Troubleshooting {#part-10}

| Symptom | Likely cause | What to do |
|---------|--------------|------------|
| Black camera / won't start | Simulator or unsupported device | Use real Multi-Cam iPhone; check unsupported screen |
| Resolution greyed out | Hardware limit | Pick lower tier; 4K may be unavailable on older models |
| Recording paused unexpectedly | Call, background, or camera taken | Return to app; check Part 6; clip may be in Pending |
| Clip in Pending after lock screen | Background safety save (~25 s) | Export from Pending — footage is preserved |
| Export failed | Storage full or Photos denied | Free space; Settings → Privacy → Photos → TwinPolarCam → Add Photos |
| Export slow | 4K + long clip | Normal — screen stays on; wait for queue |
| Music paused when recording | Audio session exclusive on record | Expected — like system Camera |
| Timer doesn't include pause | By design | Effective duration only |
| PiP wrong in export | Settings changed after record | Re-export from original `.mov` with Auto-Delete off |
| List empty but files exist | Stale index | Pending → **Rescan Cache** |
| App hot / throttling | Dual 4K load | Lower PiP resolution; shorten takes; avoid Low Power Mode |
| Refund on unsupported phone | Device gate | Use button on unsupported screen or App Store |

Still stuck? **App Settings → Send Feedback** or email below.

---

</section>

<section lang="zh-CN" markdown="1">

以下答案反映 **App 当前行为**（可恢复暂停/继续、导出队列、Live Activity、设备门槛、繁体中文、应用内教程）。分步说明见 [使用指南](index)。

---

## 设备与要求

### 哪些 iPhone 支持太极双摄？

需要 **`AVCaptureMultiCamSession`**（Apple 双摄同录 API）。通常包括 **iPhone XS、XR 及之后机型**，具体因硬件而异。

- **不支持设备**启动时显示专用页，不会进入相机权限流程。
- **模拟器不支持**。
- 必须 **真机**。

### 为什么不降级单摄？

双摄同录是产品核心；单摄降级已移除。不支持时可使用说明页上的 **退款** 或联系支持。

### 最高录制分辨率？

主摄与 PiP 各自可选 **720p / 1080p / 2K / 4K**。**iPhone 12 及以后**通常可双 4K；较旧机型可能限制为 1080p/2K。不可选项会自动禁用。

### 为什么没有 60 fps？

双摄同录时系统通常限制最高 **30 fps**。应用提供 **24 / 30 fps**，非应用故意限制。

### 支持 iPad 或 Mac 吗？

**不支持**，**仅 iPhone**。

### 需要什么 iOS 版本？

- 最低 **iOS 15.0**
- **Live Activity** 需 **iOS 16.2+**

---

## 录制与画中画

### 如何切换主画面镜头？

点 **切换/翻转** 按钮。屏幕上主/PiP 角色互换，**两路视频轨持续录制**。

### 可以自定义 PiP 吗？

可以：**拖拽**、**捏合缩放**、在 **应用设置 → 画中画** 调边框/圆角/不透明度/比例。效果写入 **导出视频**。

### 导出会保留 PiP 位置吗？

**会**，合成时使用你保存的缩放、位置、圆角、边框与不透明度。

### 可以竖屏录制吗？

相机界面为 **横屏优化**；设置/待导出可开竖屏锁定，但录制建议 **横握**。

### 什么是预览暂停？

**仅冻结预览**（非录制），便于调整 PiP/变焦。**录制中**请用 **暂停** 按钮。

### 缩放预设怎么用？

变焦后 **保存为预设**，之后一键调用。仅在 **未录制** 时对主摄预览生效。

### 截图按钮做什么？

将当前 **主画面 + PiP** 构图存 **相册**，预览或录制中均可，无需导出步骤。

### 闪光灯何时出现？

**后摄为主画面**时；**录制中**闪光灯按钮 **替代** 切换镜头按钮。

---

## 中断与可靠性

### 录制时来电会怎样？

**暂停**；通话结束后 **自动在同一段续录**（同一 `.mov`），除非你之前 **手动暂停**过。暂停时段从成片 **跳剪**。

### 下拉控制中心会暂停吗？

**不会**。只有 **真正进入后台**（Home、切 App、锁屏）才走后台中断路径。

### 切 App 或锁屏会怎样？

1. **暂停**录制  
2. 后台任务短暂保持 Writer  
3. 可能显示 **Live Activity**（已开启时）  
4. 约 **25 秒** 后 **主动保存** 到 **待导出**  
5. **超时前回 App** 可 **继续同一段**

### 什么是紧急保存？

后台超时、App 终止、Writer/写入失败等 **最后手段** 封口。Toast 提示，片段进 **待导出**。**结束后不能在同段续录**。

### 可恢复 vs 致命中断？

| 类型 | 例子 | 结果 |
|------|------|------|
| **可恢复** | 来电、Siri、短暂占相机、后台 | 暂停→**同段**继续 |
| **致命/紧急** | 媒体重置、运行时错误、磁盘满、超时 | 定稿→**待导出**，会话结束 |

### 暂停会在视频里留空档吗？

**会，by design**——暂停段 **跳剪**，不会导出长定格。

### 崩溃恢复？

意外退出后，有效片段仍在磁盘。下次启动可检测并放入 **待导出**；列表不对时用 **重新扫描缓存**。

### 为什么录制时屏幕总亮？

录制 **强制常亮**（不受「屏幕常亮」开关影响）。导出队列期间同样常亮。

---

## Live Activity

### 录制 Live Activity 是什么？

**iOS 16.2+**，录制中离开 App 时，锁屏/灵动岛显示：

- **后台等待** — 已录时长 + 自动保存倒计时  
- **已保存** — 后台自动保存成功后，直到回 App

### 如何关闭？

**应用设置 → 通用 → 录制 Live Activity**。关闭不影响可靠性，仅不显示锁屏。

---

## 导出与待导出

### 导出模式？

| 模式 | 行为 |
|------|------|
| **自动导出开** | 停止后立即合成+存相册 |
| **自动导出关** | 原片进 **待导出** 手动处理 |

### 导出队列？

**串行**——一次只合成+保存一条，**最旧优先**，完成自动下一条。

### 能取消导出吗？

能。**取消单任务** 或 **全部取消**；临时 mp4 清理，**原片 `.mov` 仍在待导出**。

### 待导出里有什么？

仅 **`TwinPolarCam_*.mov` 原片**，不含临时合成 mp4。

### 能改 PiP 再导出吗？

能，若 **导出后自动删除原片** 为 **关**（默认）。

### 导出很慢？

4K 双轨合成耗 CPU/GPU，长片正常；屏幕会保持常亮直到队列结束。

### 导出失败会丢片吗？

**不会**，原片在待导出。查 **空间** 与 **相册仅添加** 权限后重试。

### 原片存在哪？

`Application Support/TwinPolarCam/Videos/`，**不参与 iCloud 备份**。

### 成片格式？

**H.264/AAC mp4**；帧率跟随 **主摄** 设置。

---

## 设置与语言

### 支持哪些语言？

**English / 简体中文 / 繁體中文** — **应用设置 → 通用 → 语言**。

### 导出后自动删除原片？

**开**：相册保存成功后删待导出中的 `.mov`。**关**（默认）：保留多轨原片以便重导。

### 为什么一录制音乐就停？

录制时激活音频会话以 **独占麦克风**（与系统相机一致），避免扬声器声音被录入。停止录制后其他 App 可恢复。**不录制时**浏览 App **不会**打断音乐。

---

## 权限与隐私

### 会收集数据吗？

**不会**。全程本地，无统计 SDK、无账号。见 [隐私政策](privacy)。

### 为什么只要「添加照片」权限？

**仅添加** 可保存成片而 **不读取** 相册，最小权限。

---

## 帮助与支持

### 如何反馈？

**应用设置 → 发送反馈** 或 `twinpolarcam://feedback`。

### 应用内教程在哪？

**应用设置 → 帮助**。

### 仍需要帮助？

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)，通常 48 小时内回复。

[使用指南](index) · [快捷链接](url-scheme) · [隐私政策](privacy)

---

## 完整使用手册

以下为原支持页的完整分步说明（内容完整保留）。上方保留常见问答（如有）。

---

## 本页导航

| 部分 | 主题 |
|------|------|
| [第 1 部分](#part-1) | 首次启动、权限、不支持设备 |
| [第 2 部分](#part-2) | 录制、暂停、截图、切换、闪光灯、预览暂停 |
| [第 3 部分](#part-3) | 主摄与 PiP 画质与样式 |
| [第 4 部分](#part-4) | 音频质量、格式、声道 |
| [第 5 部分](#part-5) | 开始→停止流程、计时、方向 |
| [第 6 部分](#part-6) | 中断、后台保存、Live Activity |
| [第 7 部分](#part-7) | 合成流程、队列、批量导出、取消 |
| [第 8 部分](#part-8) | 外观、常亮、导出开关、语言 |
| [第 9 部分](#part-9) | 应用内教程、Spotlight、快捷菜单、深链 |
| [第 10 部分](#part-10) | 症状 → 原因 → 处理速查 |

> **只想快速找答案？** 直达 [常见问题](faq) 或 [快捷链接](url-scheme)。

---

## 第 1 部分 — 首次启动与设备要求

### 欢迎引导（6 页）

首次打开会显示 **6 页功能引导**：双摄、PiP、导出、可靠性与隐私。左右滑动或点 **继续**；最后一页点 **开始录制**。

随时重看：**应用设置 → 帮助 → 功能导览**，或 `twinpolarcam://feature-guide`。

最后一页可直接进入应用内 **使用说明**。

### 权限（必需）

| 权限 | 询问时机 | 用途 |
|------|----------|------|
| **相机** | 支持设备首次进入 | 双摄采集 |
| **麦克风** | 首次录制前 | 音频轨 |
| **相册（仅添加）** | 首次导出 | 保存成片——**不会读取**现有相册 |

相册权限为 **仅添加（Add Only）**，不上传任何视频。

### 设备要求

| 项目 | 说明 |
|------|------|
| **硬件** | 支持 Apple **Multi-Cam**（`AVCaptureMultiCamSession`）——通常 **iPhone XS / XR 及更新机型** |
| **平台** | **必须真机**——模拟器无相机/Multi-Cam |
| **系统** | iOS **15.0+**（Live Activity 需 **16.2+**） |
| **方向** | 相机界面推荐 **横屏**；部分面板可锁定竖屏 |

### 不支持设备页

若本机**无法双摄同录**，会显示**专用说明页**而非相机界面——该页**不会**请求相机或相册权限。

你仍可：

- 阅读全部应用内教程（使用 / 录制 / 导出）
- 在可用时通过 **App Store 退款**（StoreKit 2）
- 联系开发者

> **重要：** 已不再降级为单摄模式；不支持硬件会在启动时阻断。

### 应用内语言

**English**、**简体中文**、**繁體中文**——在 **应用设置 → 通用 → 语言** 切换，立即生效。本支持网站亦提供三语。

---

## 第 2 部分 — 主界面与控制

**横屏**握持可获得最宽双摄预览。控制列在一侧；主画面显示一个镜头，**PiP 悬浮窗**显示另一个。

### 控制按钮

| 控制 | 可用时机 | 作用 |
|------|----------|------|
| **录制** | 预览未录 | 开始双摄 + 音频 |
| **暂停/继续** | 录制或暂停中 | 停止写入帧；计时冻结 |
| **停止** | 录制或暂停中 | 定稿片段 → 导出或进入待导出 |
| **切换镜头** | 预览或录制 | 交换主画面与 PiP（两路继续录） |
| **截图** | 预览或录制 | 当前构图存相册 |
| **闪光灯** | 后摄为主画面 | 开关手电（录制时替代切换按钮） |
| **预览暂停** | 仅预览（非录制） | 冻结预览以便调整 PiP/变焦 |
| **设置** | 始终 | 打开应用设置 |
| **待导出** | 始终 | 未导出 `.mov` 列表 |

### 手势

- **拖拽 PiP** — 任意位置（位置会保存）
- **捏合 PiP** — 缩放（设置中也可调）
- **捏合主画面** — **未录制时**变焦主摄
- **缩放预设** — 在变焦控件中保存/调用

### 预览暂停 vs 录制暂停

| | 预览暂停 | 录制暂停 |
|---|----------|----------|
| **触发** | 预览切换按钮 | 录制中暂停按钮 |
| **预览** | 冻结 | 可能停在上帧 |
| **写入** | 未开始 | Writer 打开但不 append |
| **恢复** | 点恢复预览 | 点继续录制 |

预览暂停用于**构图**；录制暂停的时间**不会进入成片**（PTS 跳剪，无定格帧）。

---

## 第 3 部分 — 主摄与 PiP 设置

打开 **应用设置**（齿轮）。四个标签：**主画面 · 画中画 · 音频 · 通用**。

影响**实时预览**的参数（分辨率、帧率、防抖、HDR、夜间模式）会立即生效。**音频**在**下一次**录制时生效，不打断预览。

### 主画面

| 设置 | 选项 | 说明 |
|------|------|------|
| 分辨率 | 720p / 1080p / 2K / 4K | 不支持项自动禁用 |
| 质量 | 低 / 中 / 高 | 码率权衡 |
| 帧率 | 24 / 30 fps | Multi-Cam 通常最高 **30 fps** |
| 防抖 | 关 / 标准 / 电影 | 各镜头独立 |
| HDR | 关 / 开 / 自动 | 各镜头独立 |
| 夜间模式 | 关 / 开 / 自动 | 各镜头独立 |

### 画中画

除与主摄相同的视频参数外，还有 **UI 样式**：

| 设置 | 范围 |
|------|------|
| 缩放 | 短边 10%–100% |
| 位置 | 预览上拖拽 |
| 边框宽度 / 颜色 / 圆角 / 不透明度 | 可调 |

**提示：** 主摄 4K + PiP 1080p 可减发热与占用。浅色边框在复杂背景上更清晰。

样式会写入**最终导出视频**，不仅是预览。

---

## 第 4 部分 — 音频设置

| 设置 | 选项 |
|------|------|
| 质量 | 低（语音）/ 标准 / 高（音乐）/ 无损 |
| 格式 | AAC / PCM |
| 声道 | 单声道 / 立体声 |

> **开始录制前**不会激活音频会话——浏览设置时不会打断音乐。录制开始时其他 App 音频会暂停（与系统相机一致），避免扬声器声音被录入。

---

## 第 5 部分 — 一次录制流程

### 典型步骤

1. 按提示**授权**。
2. **调整**主摄/PiP 与 PiP 位置。
3. 点 **录制**——屏幕常亮、音频激活、计时开始。
4. 可选：暂停、切换主/PiP、截图、变焦（未录制时）。
5. 点 **停止**——片段写入应用存储（`TwinPolarCam_*.mov`）。
6. **自动导出开** → 立即合成并存相册。
7. **自动导出关** → 进入 **待导出** 待处理。

### 录制计时

显示**有效录制时长**：

- 仅在实际写入帧时累加
- **用户暂停**与**可恢复中断暂停**时冻结
- 会话完全结束后清零
- 后台时 Live Activity 显示相同 elapsed

### 方向

| 界面 | 默认 |
|------|------|
| 相机预览/录制 | **强制横屏** |
| 应用设置 | 横屏，或开启竖屏锁定 |
| 待导出 | 横屏，或开启竖屏锁定 |

### 停止后保存什么

每条 **原始多轨 `.mov`**：

- 轨 0：后摄视频
- 轨 1：前摄视频
- 一条音频轨

路径：`Application Support/TwinPolarCam/Videos/`，**不参与 iCloud 备份**。

---

## 第 6 部分 — 录制可靠性

内置 **中断协调器** 分类处理并保护素材。

### 录制前建议

- 预留 **数 GB** 空间
- 关闭其他 **相机 App**
- 长时间录制可考虑 **降低 PiP 分辨率**
- 在通用设置中开启 **录制 Live Activity**

### 可恢复中断（暂停 → 继续，**同一段**）

| 事件 | 行为 |
|------|------|
| 来电 / Siri | 暂停；通话结束后**自动继续**（若未手动暂停） |
| 其他 App 短暂占用相机 | 暂停；释放后可能恢复 |
| **进入后台**（Home、切 App、锁屏） | 暂停；启动 **25 秒**安全计时 |

**Writer 保持打开**——恢复后在**同一文件**续写。暂停时段从成片**跳剪**掉，不是定格画面。

> **仅下拉控制中心不会暂停**——必须真正进入后台。

### 不可恢复事件（保存到待导出）

媒体服务重置、采集运行时错误/过热、Writer 失败（磁盘满等）→ 定稿并提示，请到 **待导出** 查看。

### 紧急保存

| 触发 | 行为 |
|------|------|
| 后台暂停约 **25 秒** | 主动封口 → 待导出 |
| App 被终止 | 最多约 **8 秒**尝试 finalize |
| append 失败 / writer 失败 | 立即尝试保存 |

后台自动保存成功后，Live Activity 可能显示 **已保存**，直到回到 App。

**紧急保存会结束本次会话**——无法在同一段上继续，需重新开录。

### Live Activity（iOS 16.2+）

| 阶段 | 锁屏/灵动岛 |
|------|-------------|
| **后台等待** | 已录时长 + 自动保存倒计时 |
| **已保存** | 素材已保护——点按回 App |

开关：**应用设置 → 通用 → 录制 Live Activity**（默认开）。关闭不影响可靠性，仅不显示锁屏状态。

详见 **应用设置 → 帮助 → 录制与可靠性**。

---

## 第 7 部分 — 导出与待导出管理

### 导出流水线

1. **原始 `.mov`**
2. **合成** — 后摄主画面 + 前摄 PiP → 临时 `.mp4`
3. **保存相册**（仅添加权限）
4. **清理** — 删临时 mp4；可选删原始 mov
5. **队列下一项** — 按**最旧优先**自动继续

导出帧率跟随**主摄**设置；PiP 样式写入成片。

### 待导出管理

相机屏 **待导出** 按钮，或 `twinpolarcam://pending`。

| 功能 | 说明 |
|------|------|
| 内容 | 仅 `TwinPolarCam_*.mov` 原片 |
| 排序 | 创建时间，**最旧优先**导出 |
| 布局 | **列表** / **网格**，列数 2–6 |
| 预览 | 导出前可播放多轨原片 |
| 重新扫描 | 磁盘有文件但列表空时使用 |
| 分享 / 删除 | 单条管理 |

### 批量与队列

- 导出一条、**多选**或 **全部导出**
- 首个立即执行，其余 **串行排队**（一次只合成+保存一条，更稳定）
- 队列未空时 **屏幕常亮**
- 可 **取消单任务** 或 **全部取消**——原片仍在待导出

### 导出相关开关（通用）

| 开关 | 默认 | 效果 |
|------|------|------|
| **自动导出** | — | 停止后立即合成+存相册 |
| **导出后自动删除原片** | **关** | 成功后从待导出移除 `.mov` |

需换 PiP 样式重导时，请保持 **自动删除原片** 关闭。

详见 **应用设置 → 帮助 → 导出与待导出**。

---

## 第 8 部分 — 通用设置

| 分区 | 内容 |
|------|------|
| **外观** | 跟随系统 / 浅色 / 深色 |
| **屏幕常亮** | 使用 App 时常亮（录制/导出强制常亮） |
| **录制 Live Activity** | 锁屏与灵动岛状态 |
| **设置页竖屏锁定** | 打开设置时转竖屏 |
| **待导出竖屏锁定** | 打开待导出时转竖屏 |
| **自动导出 / 自动删原片** | 见第 7 部分 |
| **语言** | English / 简体中文 / 繁體中文 |
| **打赏开发者** | StoreKit 2 可选内购 |
| **发送反馈** | 系统邮件 |
| **重置全部设置** | 需确认——不删除待导出视频 |

---

## 第 9 部分 — 帮助、教程与快捷方式

### 应用内教程（设置 → 帮助）

| 教程 | 内容 |
|------|------|
| **使用说明** | 快速上手、控制、PiP、导出概览 |
| **录制与可靠性** | 中断、后台、Live Activity |
| **导出与待导出** | 流水线、队列、批量、相册权限 |
| **功能导览** | 重播 6 页欢迎引导 |

### 主屏长按快捷菜单

| 菜单项 | 深链 |
|--------|------|
| 使用说明 | `twinpolarcam://usage-guide` |
| 录制技巧 | `twinpolarcam://recording-guide` |
| 导出指南 | `twinpolarcam://export-guide` |
| 功能导览 | `twinpolarcam://feature-guide` |

### 其他深链

| 链接 | 打开 |
|------|------|
| `twinpolarcam://settings` | 应用设置 |
| `twinpolarcam://pending` | 待导出 |
| `twinpolarcam://feedback` | 反馈邮件 |
| `twinpolarcam://recording` | 从 Live Activity 返回 |

完整列表：[快捷链接](url-scheme)。

---

## 第 10 部分 — 问题速查

| 现象 | 可能原因 | 处理 |
|------|----------|------|
| 黑屏/无法启动 | 模拟器或不支持设备 | 用真机；看不支持说明页 |
| 分辨率不可选 | 硬件限制 | 选低一档 |
| 意外暂停 | 来电、后台、相机被占 | 回 App；见第 6 部分；可能在待导出 |
| 锁屏后在待导出 | 后台 ~25 秒安全保存 | 从待导出导出——素材在 |
| 导出失败 | 空间满或相册拒权 | 腾空间；设置→隐私→相册→仅添加 |
| 导出慢 | 4K 长片 | 正常；等队列完成 |
| 录时音乐停 | 录制独占音频 | 预期行为 |
| 成片无暂停段 | 跳剪设计 | 有效时长不含暂停 |
| 导出 PiP 不对 | 录后改了样式 | 保留原片重导 |
| 列表空 | 索引过期 | **重新扫描缓存** |
| 发热降频 | 双 4K | 降 PiP 分辨率；避免低电量模式 |

仍无法解决？**应用设置 → 发送反馈** 或下方邮箱。

---

</section>

<section lang="zh-TW" markdown="1">

以下答案反映 **App 目前行為**。分步說明見 [使用指南](index)。

---

## 裝置與要求

### 哪些 iPhone 支援太極雙攝？

需要 **`AVCaptureMultiCamSession`**。通常 **iPhone XS、XR 及之後機型**。**不支援裝置**顯示專用頁；**模擬器不支援**；須 **實機**。

### 為何不降級單攝？

雙攝同錄是核心功能；不支援時可用 **退款** 或聯絡支援。

### 最高解析度？

各鏡頭 **720p–4K**；**iPhone 12+** 通常可雙 4K。無 **60 fps**——系統 Multi-Cam 通常上限 **30 fps**。

### 支援 iPad / Mac？

**不支援**，目前 **僅 iPhone**。最低 **iOS 15.0**；Live Activity 需 **16.2+**。

---

## 錄製與子母畫面

### 如何切換主畫面？

點 **切換** 按鈕；兩路軌道持續錄製。PiP 可 **拖曳、縮放、調樣式**，寫入 **匯出影片**。

### 預覽暫停？

**僅凍結預覽**（非錄製）。錄製中請用 **暫停**。

---

## 中斷與可靠性

### 來電？

**暫停**；結束後 **同一段自動續錄**（除非你曾手動暫停）。暫停段 **跳剪**。

### 控制中心？

**不會**暫停。須 **進入背景**。

### 切 App / 鎖屏？

暫停 → 可能 Live Activity → 約 **25 秒** **主動保存** 至 **待匯出**；超時前回 App 可 **續錄同段**。

### 緊急保存？

超時、終止、Writer 失敗等 → Toast，片段進 **待匯出**；**無法在同段續錄**。

| 可恢復 | 致命/緊急 |
|--------|-----------|
| 來電、Siri、占相机、背景 | 媒體重置、錯誤、磁碟滿 |

### 當機恢復？

有效片段保留；重開可進 **待匯出**；列表不對用 **重新掃描快取**。

---

## Live Activity

**iOS 16.2+** 錄製中離開 App：鎖屏/靈動島顯示計時與倒數，或 **已保存**。開關：**通用 → 錄製 Live Activity**。

---

## 匯出與待匯出

**自動匯出** 或 **待匯出手動**。**串列佇列**、**最舊優先**。可 **取消**；原片 `.mov` 保留。預設 **不** 自動刪原片以便重導。失敗不丟片——查空間與 **僅加入** 相簿權限。

---

## 設定、語言與隱私

**English / 简体中文 / 繁體中文**。錄製時音樂暫停為 **麥克風獨占**（與系統相機一致）；未錄製時不打斷音樂。**不收集資料**；相簿 **僅加入** 權限。

---

## 支援

**應用設定 → 幫助** 或 `twinpolarcam://feedback`。[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

[使用指南](index) · [快捷連結](url-scheme) · [隱私政策](privacy)

---

## 完整使用手冊

以下為原支援頁的完整分步說明（內容完整保留）。上方保留常見問答（如有）。

---

## 本頁導覽

| 部分 | 主題 |
|------|------|
| [第 1 部分](#part-1) | 首次啟動、權限、不支援裝置 |
| [第 2 部分](#part-2) | 錄製、暫停、截圖、切換、閃光燈、預覽暫停 |
| [第 3 部分](#part-3) | 主攝與 PiP 畫質與樣式 |
| [第 4 部分](#part-4) | 音訊品質、格式、聲道 |
| [第 5 部分](#part-5) | 開始→停止流程、計時、方向 |
| [第 6 部分](#part-6) | 中斷、背景保存、Live Activity |
| [第 7 部分](#part-7) | 合成流程、佇列、批次匯出、取消 |
| [第 8 部分](#part-8) | 外觀、常亮、匯出開關、語言 |
| [第 9 部分](#part-9) | 應用內教學、Spotlight、快捷選單、深鏈 |
| [第 10 部分](#part-10) | 症狀 → 原因 → 處理速查 |

> **只想快速找答案？** 直達 [常見問題](faq) 或 [快捷連結](url-scheme)。

---

## 第 1 部分 — 首次啟動與裝置要求

### 歡迎引導（6 頁）

首次開啟會顯示 **6 頁功能引導**。左右滑動或點 **繼續**；最後一頁點 **開始錄製**。

隨時重看：**應用設定 → 幫助 → 功能導覽**，或 `twinpolarcam://feature-guide`。

### 權限（必需）

| 權限 | 詢問時機 | 用途 |
|------|----------|------|
| **相機** | 支援裝置首次進入 | 雙攝擷取 |
| **麥克風** | 首次錄製前 | 音訊軌 |
| **相簿（僅加入）** | 首次匯出 | 保存成片——**不會讀取**現有相簿 |

相簿權限為 **僅加入（Add Only）**。

### 裝置要求

| 項目 | 說明 |
|------|------|
| **硬體** | 支援 Apple **Multi-Cam**——通常 **iPhone XS / XR 及更新機型** |
| **平台** | **必須實機**——模擬器無相機 |
| **系統** | iOS **15.0+**（Live Activity 需 **16.2+**） |
| **方向** | 相機介面建議 **橫向** |

### 不支援裝置頁

若本機**無法雙攝同錄**，顯示**專用說明頁**——**不會**請求相機或相簿權限。仍可閱讀全部教學、申請退款或聯絡支援。

> **重要：** 已不再降級為單攝模式。

### 應用內語言

**English**、**简体中文**、**繁體中文**——在 **應用設定 → 通用 → 語言** 切換。本支援網站亦提供三語。

---

## 第 2 部分 — 主介面與控制

**橫向**握持可獲最寬雙攝預覽。

### 控制按鈕

| 控制 | 可用時機 | 作用 |
|------|----------|------|
| **錄製** | 預覽未錄 | 開始雙攝 + 音訊 |
| **暫停/繼續** | 錄製或暫停中 | 停止寫入幀；計時凍結 |
| **停止** | 錄製或暫停中 | 定稿 → 匯出或待匯出 |
| **切換鏡頭** | 預覽或錄製 | 交換主畫面與 PiP |
| **截圖** | 預覽或錄製 | 當前構圖存相簿 |
| **閃光燈** | 後攝為主畫面 | 手電開關 |
| **預覽暫停** | 僅預覽 | 凍結預覽以便調整 |
| **設定 / 待匯出** | 始終 | 設定面板 / 未匯出列表 |

### 手勢

拖拽 PiP、捏合縮放、主畫面变焦（未錄製時）、**縮放預設**。

### 預覽暫停 vs 錄製暫停

預覽暫停用於構圖；錄製暫停時間**不進入成片**（PTS 跳剪）。

---

## 第 3 部分 — 主攝與 PiP 設定

**應用設定** 四個標籤：**主畫面 · 子母畫面 · 音訊 · 通用**。

### 主畫面 / 子母畫面

分辨率 720p–4K、品質、24/30 fps、防抖、HDR、夜間模式（各鏡頭獨立）。PiP 另有邊框、圓角、不透明度等樣式——全部寫入**最終匯出影片**。

---

## 第 4 部分 — 音訊設定

品質（低/標準/高/無損）、AAC/PCM、單聲道/立體聲。**開始錄製前**不激活音訊會話，不會打斷音樂。

---

## 第 5 部分 — 一次錄製流程

1. 授權 → 2. 調整 PiP → 3. 錄製 → 4. 可選暫停/切換/截圖 → 5. 停止 → 6. 自動匯出或進入待匯出。

計時為**有效錄製時長**；原始檔為多軌 `.mov`，存於 Application Support，**不參與 iCloud 備份**。

---

## 第 6 部分 — 錄製可靠性

### 可恢復中斷（**同一段**續寫）

來電、Siri、短暫相機占用、**進入背景** → 暫停，結束後可自動繼續。Writer 保持打開；暫停段從成片跳剪。

> 僅下拉控制中心**不會**暫停——須真正進入背景。

### 不可恢復 / 緊急保存

媒體重置、執行時錯誤、Writer 失敗 → 定稿至待匯出。背景約 **25 秒**會主動封口。**緊急保存結束本次工作階段**，無法在同段續錄。

### Live Activity（iOS 16.2+）

**背景等待**（計時+倒數）→ **已保存**。開關：**通用 → 錄製 Live Activity**。

詳見 **應用設定 → 幫助 → 錄製與可靠性**。

---

## 第 7 部分 — 匯出與待匯出管理

流水線：原始 mov → 合成 mp4 → 存相簿 → 清理 → 佇列下一項（**最舊優先**）。

待匯出：列表/網格、預覽、多選/全部匯出、**串列佇列**、取消任務、重新掃描。

**自動匯出** / **匯出後自動刪原片**（預設關）在通用設定。

詳見 **應用設定 → 幫助 → 匯出與待匯出**。

---

## 第 8 部分 — 通用設定

外觀、螢幕常亮、Live Activity、設定/待匯出豎屏鎖定、匯出開關、三語、打賞、回饋、重置。

---

## 第 9 部分 — 幫助、教學與快捷方式

**設定 → 幫助**：使用說明、錄製與可靠性、匯出與待匯出、功能導覽。

主畫面長按：`usage-guide` / `recording-guide` / `export-guide` / `feature-guide`。

完整深鏈：[快捷連結](url-scheme)。

---

## 第 10 部分 — 問題速查

| 現象 | 處理 |
|------|------|
| 黑屏 | 用實機；查不支援頁 |
| 意外暫停 | 回 App；查待匯出 |
| 鎖屏後在待匯出 | 背景安全保存——素材在 |
| 匯出失敗 | 騰空間；相簿僅加入權限 |
| 列表空 | 重新掃描快取 |
| 發熱 | 降 PiP 解析度 |

[常見問題](faq) 有更多問答。

---

</section>
