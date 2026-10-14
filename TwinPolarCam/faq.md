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

**No.** All capture, composition, and storage happen on device. No analytics SDK, no account, no upload. See [Privacy Policy](../privacy).

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

Home Screen **long-press quick actions**, **Spotlight** search, or **`twinpolarcam://`** links — see [Shortcut Links](../url-scheme).

### Still need help?

Email [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — we typically respond within 48 hours.

[User Guide](index) · [Shortcut Links](../url-scheme) · [Privacy Policy](../privacy)

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

> **Need a quick answer?** Jump to [FAQ](../faq) or [Shortcut Links](../url-scheme).

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

Full reference: [Shortcut Links](../url-scheme).

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

**不会**。全程本地，无统计 SDK、无账号。见 [隐私政策](../privacy)。

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

[使用指南](index) · [快捷链接](../url-scheme) · [隐私政策](../privacy)

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

> **只想快速找答案？** 直达 [常见问题](../faq) 或 [快捷链接](../url-scheme)。

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

完整列表：[快捷链接](../url-scheme)。

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

[使用指南](index) · [快捷連結](../url-scheme) · [隱私政策](../privacy)

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

> **只想快速找答案？** 直達 [常見問題](../faq) 或 [快捷連結](../url-scheme)。

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

完整深鏈：[快捷連結](../url-scheme)。

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

[常見問題](../faq) 有更多問答。

---

</section>
<section lang="ja" markdown="1">

回答は **現在のアプリの挙動**（復旧可能な一時停止/再開、エクスポートキュー、Live Activity、デバイスゲート、繁体中文、アプリ内ガイド）を反映しています。手順の詳細は [ユーザーガイド](index) を参照してください。

---

## デバイスと要件

### どの iPhone が TwinPolarCam に対応していますか？

TwinPolarCam には **`AVCaptureMultiCamSession`** — Apple の同時マルチカメラ API — が必要です。対応機種は通常 **iPhone XS、iPhone XR 以降の全モデル** ですが、実際の能力はハードウェア世代により異なります。

- **非対応デバイス** は起動時に専用画面が表示され、カメラ UI と権限フローは開始されません。
- **iOS シミュレータは非対応** — 物理カメラも Multi-Cam もありません。
- **実機の iPhone** が必要です。

### なぜ単一カメラモードにフォールバックしないのですか？

前後カメラの同時録画が製品の核心です。混乱や誤った期待を避けるため、単一カメラへのフォールバックは削除されました。能力チェックに失敗した場合は、非対応画面の **返金** オプションを使うか、サポートに連絡してください。

### 最大録画解像度は？

TwinPolarCam は各カメラ（メインと PiP を個別に）で **720p、1080p、2K、4K** を提供します。上限はデバイス依存です。

- **iPhone 12 以降** — 一般に 4K デュアル撮影が利用可能です。
- **旧 Multi-Cam モデル** — 一方または両方のレンズが 1080p または 2K に制限される場合があります。

利用できない解像度は設定で **自動的に無効** になります。

### なぜ 60 fps は使えないのですか？

Apple のマルチカメラパイプラインは、両カメラ同時録画時に多くのデバイスで **最大 30 fps** に制限します。TwinPolarCam は **24 fps と 30 fps** を提供します。**60 fps は非対応** — これはアプリの任意制限ではなく、システム/ハードウェアの制約です。

### iPad や Mac で使えますか？

**いいえ。** TwinPolarCam は **iPhone 専用** です。

### 必要な iOS バージョンは？

- **最低: iOS 15.0**
- **Live Activity: iOS 16.2+**
- **ウィジェット拡張**（Live Activity UI）: アプリ同梱、Live Activity 機能と同じ OS 要件

---

## 録画と PiP

### メイン表示のカメラを切り替えるには？

プレビューまたは録画中に **切り替え / 反転コントロール** をタップします。前面と背面の **画面上の役割が入れ替わります** — どちらが全画面表示でも、両方の映像トラックは録画を続けます。

### PiP オーバーレイをカスタマイズできますか？

はい:

- **ドラッグ** で移動
- **ピンチ** でサイズ変更（PiP 設定のスケールも可）
- **アプリ設定 → ピクチャ・イン・ピクチャ** で **枠線の太さ、色、角丸、不透明度、相対サイズ** を調整

変更はライブプレビューに反映され、**書き出し動画に焼き込まれます**。

### 書き出し動画に PiP の位置は反映されますか？

**はい。** 合成時に保存したスケール、正規化位置、角丸、枠線、不透明度が使われます。

### 縦向きで録画できますか？

**カメラ UI は横向き向けに最適化** されています。設定や Pending パネル用に **縦向きロック** を有効にできますが、デュアルプレビューと録画は **横向き** が最適です。

### プレビュー一時停止とは？

**プレビュー一時停止** は **ライブカメラプレビュー**（録画ではない）を凍結し、画像が動かない状態で PiP やズームを調整できます。**録画中は利用不可** — 代わりに **録画一時停止** を使ってください。

### ズームプリセットの仕組みは？

ピンチまたは画面上のズームコントロールを使い、**現在のレベルをプリセットとして保存** します。プリセットを呼び出して素早く構図を変えられます。ズームは **録画していないときのメインカメラプレビュー** に適用されます。

### スクリーンショットボタンは何をしますか？

現在の **メイン + PiP 合成レイアウト** を静止画としてキャプチャし、**写真** に直接保存します — プレビュー/録画中どちらでも可、エクスポート手順不要。

### フラッシュライトはいつ表示されますか？

**背面カメラがメイン表示** のとき。録画中は、コントロール弧上でカメラ切り替えボタンの **代わりに** フラッシュライトボタンが表示されます。

---

## 中断と信頼性

### 録画中に電話が来たらどうなりますか？

TwinPolarCam は通話中 **録画を一時停止** します。通話終了後、**同じセグメント**（同じ `.mov` ファイル）で **自動再開** します — **通話前に手動一時停止していた場合を除きます**。

一時停止した時間は **出力タイムラインから切り落とされます**（静止フレームとして書き出されません）。

### コントロールセンターを下ろすと録画は止まりますか？

**いいえ。** **完全なバックグラウンド化**（Home ジェスチャ、アプリ切り替え、ロック画面）のみがバックグラウンド中断パスを起動します — `willResignActive` 単独（例: コントロールセンターのオーバーレイ）ではありません。

### 録画中にアプリを切り替えたり画面をロックすると？

1. 録画 **一時停止**
2. **バックグラウンドタスク** が Writer を短時間維持
3. 有効なら **Live Activity** が経過時間と自動保存カウントダウンを表示
4. **約 25 秒** 後、アプリがセグメントを **Pending Exports** へ **能動的に保存**
5. **タイムアウト前に戻れば** **同じセグメントを再開** 可能

### 緊急保存とは？

書き込みを続けられないときの最終手段の確定:

- バックグラウンド安全タイムアウト（約 25 秒）
- アプリ終了（最大約 8 秒待機）
- Writer 失敗、append エラー

**トースト通知** が表示されます。クリップは **Pending** に入ります。**緊急保存はセッションを終了** — そのセグメントは再開できません。

### 復旧可能と致命的な中断の違いは？

| 種類 | 例 | 結果 |
|------|-----|------|
| **復旧可能** | 通話、Siri、短時間のカメラ奪取、バックグラウンド化 | 一時停止 → **同じセグメント** 再開 |
| **致命的 / 緊急** | メディアリセット、ランタイムエラー、ディスク満杯、タイムアウト | 確定 → **Pending**、セッション終了 |

### 一時停止は動画に隙間を作りますか？

**はい — 設計どおりです。** 一時停止区間は **省略** されます（PTS ジャンプカット）。書き出しファイルは長い静止区間なしで連続再生されます。

### クラッシュ復旧の仕組みは？

アプリが予期せず終了しても、**有効な確定セグメント** はディスクに残ります。次回起動時に TwinPolarCam が復旧可能ファイルを検出し、**Pending** に配置してアラートを表示できます。必要なら Pending で **Rescan Cache** を使用してください。

### 録画中に画面が常に点灯するのはなぜ？

録画は **Keep Screen Awake** 設定に関係なく **常時起動を強制** — 撮影中の誤ロックを防ぎます。エクスポートキューも完了まで画面を点灯させます。

### 低電力モードは録画に影響しますか？

**バックグラウンド圧力** やサーマルスロットリングが増える場合があります。長時間セッションでは解像度を下げ、充電熱を避けるか、電源に接続してください。

---

## Live Activity

### Recording Live Activity とは？

**iOS 16.2+** で、録画セッション中にアプリを離れると、**ロック画面 / Dynamic Island** ウィジェットに状態が表示されます:

- **Background waiting** — 経過時間 + 自動保存カウントダウン
- **Saved** — バックグラウンド自動保存後に映像が保護された状態（アプリを再開するまで）

### Live Activity をオフにするには？

**アプリ設定 → 一般 → Recording Live Activity**。信頼性は変わりません — ロック画面表示のみに影響します。

### 自動保存後も Live Activity が残るのはなぜ？

**バックグラウンド自動保存** 成功後、アクティビティが **Saved** を表示し、映像が安全であることを示す場合があります。アプリに戻る（フォアグラウンド）と終了します。

---

## エクスポートと Pending

### 利用できるエクスポートモードは？

| モード | 動作 |
|------|------|
| **Auto Export ON** | 停止 → 即座に合成 + 写真へ保存 |
| **Auto Export OFF** | 停止 → 元の `.mov` が **Pending** に入り、手動エクスポートまで待機 |

### エクスポートキューの仕組みは？

バッチエクスポートは **直列** — 一度に 1 件の合成 + 保存、**Pending 最古クリップ優先**。4K 高負荷下でもデバイスを安定させます。現在のタスク完了後、次が自動開始します。

### エクスポートをキャンセルできますか？

はい:

- 進行中の **単一タスクをキャンセル**
- **Cancel All** — アクティブ + キュー内タスクを停止、一時 mp4 を削除
- **元の `.mov` は Pending に残り** 再試行可能

### Pending に表示されるファイルは？

オリジナルの **`TwinPolarCam_*.mov`** マルチトラック録画のみ — 一時合成 `TwinPolarCam_MultiCam_*.mp4` ではありません。

### PiP スタイルを変えて再エクスポートできますか？

**Auto-Delete Original After Export** が **オフ**（デフォルト）なら **はい**。PiP 設定を調整し、Pending から再度エクスポートしてください。

### エクスポートに時間がかかるのはなぜ？

4K デュアルトラック合成は **CPU/GPU 集約的** です。長いクリップや高フレームレートほど時間がかかります。キュー完了まで画面は自動的に点灯したままです。

### エクスポート失敗 — 動画は失われますか？

**いいえ。** 元の `.mov` は Pending に残ります。**空き容量** と **写真権限**（Add Only）を確認し、再試行してください。

### エクスポート前の保存場所は？

`Application Support/TwinPolarCam/Videos/` — 意図的に **iCloud バックアップから除外**。

### 出力形式は？

高品質の **H.264 / AAC mp4**；フレーム間隔は **メインカメラのフレームレート** 設定に従います。

### 新しいクリップを録画しながらエクスポートできますか？

新セッション開始中もエクスポートパイプラインは動作できますが、**同時の高負荷** は発熱の原因になる場合があります — 順次利用が安全です。

---

## 設定と言語

### アプリが対応する言語は？

**English**、**简体中文**、**繁體中文** — **アプリ設定 → 一般 → 言語**。

### Auto-Delete Original After Export とは？

**ON** のとき、**成功した** 写真保存後に Pending から元の `.mov` を削除します。**OFF**（デフォルト）のとき、再合成用にマルチトラックソースを保持します。

デフォルトは **OFF** — アップグレードユーザーが元ファイル消失に驚かないためです。

### 録画開始で音楽が止まるのはなぜ？

TwinPolarCam は録画開始時にオーディオセッションを有効化します（Apple カメラアプリと同様）— **マイクの独占取得** のため、スピーカー音声が録音されません。録画停止時に音楽が再開します（`notifyOthersOnDeactivation`）。

**録画せずに** アプリを閲覧しても音楽は **中断されません**。

### 外観モードの仕組みは？

一般設定の **System / Light / Dark** — `preferredColorScheme` 経由でアプリ全体に即時適用されます。

---

## 権限とプライバシー

### TwinPolarCam はデータを収集しますか？

**いいえ。** 撮影、合成、保存はすべて端末内です。分析 SDK なし、アカウントなし、アップロードなし。[プライバシーポリシー](../privacy) を参照。

### なぜ写真は「追加のみ」を求めるのですか？

**Add Only** 権限（iOS 14+）により、既存ライブラリを **読まずに** 完成動画を保存 — 最小権限、高い信頼性。

### 動画は iCloud にバックアップされますか？

アプリストレージ内のオリジナル録画は **バックアップ除外** としてマークされます。写真に書き出した動画は **あなたの** 写真/iCloud 設定に従います。

---

## ヒントとサポート

### フィードバックの送り方は？

**アプリ設定 → Send Feedback**（メール）または `twinpolarcam://feedback`。

### アプリ内ガイドはどこ？

**アプリ設定 → Help** — How to Use、Recording & Reliability、Export & Pending、Feature Tour。

### アプリ外からガイドを開くには？

ホーム画面 **アイコン長押しクイックアクション**、**Spotlight** 検索、または **`twinpolarcam://`** リンク — [ショートカットリンク](../url-scheme) を参照。

### まだ助けが必要？

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) にメール — 通常 48 時間以内に返信します。

[ユーザーガイド](index) · [ショートカットリンク](../url-scheme) · [プライバシーポリシー](../privacy)

---

## 完全ユーザーガイド

以下は以前サポートページにあった製品の完全ウォークスルーです。上部にクイック Q&A（該当する場合）が残っています。

---

## このページの内容

| パート | トピック |
|------|--------|
| [Part 1](#part-1) | 初回起動、権限、非対応デバイス |
| [Part 2](#part-2) | 録画、一時停止、スクリーンショット、切り替え、フラッシュ、プレビュー一時停止 |
| [Part 3](#part-3) | メインカメラと PiP の画質とスタイル |
| [Part 4](#part-4) | オーディオ品質、形式、チャンネル |
| [Part 5](#part-5) | 開始 → 停止ワークフロー、タイマー、向き |
| [Part 6](#part-6) | 中断、バックグラウンド保存、Live Activity |
| [Part 7](#part-7) | 合成パイプライン、キュー、バッチエクスポート、キャンセル |
| [Part 8](#part-8) | 外観、画面常時点灯、エクスポートトグル、言語 |
| [Part 9](#part-9) | アプリ内ガイド、Spotlight、クイックアクション、ディープリンク |
| [Part 10](#part-10) | 症状 → 原因 → 対処クイックリファレンス |

> **すぐ答えが欲しい？** [FAQ](../faq) または [ショートカットリンク](../url-scheme) へ。

---

## Part 1 — 初回起動と要件 {#part-1}

### ウェルカムガイド（6 ページ）

初回起動時、**6 ページのオンボーディング** がデュアル撮影、PiP、エクスポート、信頼性、プライバシーを紹介します。左右スワイプまたは **Continue**；最終ページで **Start Recording** をタップ。

いつでも再生: **アプリ設定 → Help → Feature Tour**、または `twinpolarcam://feature-guide`。

最終オンボーディングページからアプリ内 **How to Use** ガイドを直接開けます。

### 権限（必須）

| 権限 | 要求タイミング | 理由 |
|------------|------------|-----|
| **カメラ** | 対応デバイス初回起動 | デュアル映像取得 |
| **マイク** | 初回録画前 | オーディオトラック |
| **写真（Add Only）** | ライブラリへの初回エクスポート | 完成動画を保存 — 既存ライブラリは **読み取らない** |

TwinPolarCam は **Add Only** 写真アクセス（iOS 14+）を使用します。映像をアップロードすることはありません。

### デバイス要件

| 要件 | 詳細 |
|-------------|--------|
| **ハードウェア** | Apple **Multi-Cam** 対応 iPhone（`AVCaptureMultiCamSession`）— 通常 **iPhone XS / XR 以降**（モデルにより異なる） |
| **プラットフォーム** | **実機 iPhone のみ** — iOS シミュレータにカメラ / Multi-Cam なし |
| **最低 OS** | iOS **15.0+**（Live Activity は **iOS 16.2+**） |
| **向き** | カメラ画面は **横向き** 最適化；一部パネルは縦向きロック可 |

### 非対応デバイス画面

iPhone が **デュアルカメラモードを実行できない** 場合、TwinPolarCam はカメラ UI の代わりに **専用通知** を表示 — その画面では **カメラや写真の権限プロンプトなし**。

引き続き可能:

- すべてのアプリ内ガイドを読む（Usage / Recording / Export）
- 利用可能なら **App Store 返金**（StoreKit 2）をリクエスト
- サポートに連絡

> **重要:** TwinPolarCam は **単一カメラモードにフォールバックしません**。非対応ハードウェアは起動時に意図的にブロックされます。

### アプリ内言語

**English**、**简体中文**、**繁體中文** — **アプリ設定 → 一般 → 言語** で切り替え。変更は即時反映。このサポートサイトも 3 言語で提供されています。

---

## Part 2 — メイン画面とコントロール {#part-2}

**横向き** で端末を持つと最も広いデュアルプレビューが得られます。コントロール列が片側にあり、メインビューが一方のカメラ、**PiP オーバーレイ** がもう一方を表示します。

### コントロール一覧

| コントロール | 利用可能時 | 機能 |
|---------|----------------|--------------|
| **Record** | プレビュー（未録画） | デュアルカメラ + オーディオ録画開始 |
| **Pause / Resume** | 録画または一時停止中 | フレーム書き込み一時停止；タイマー停止 |
| **Stop** | 録画または一時停止中 | セグメント確定 → エクスポートまたは Pending |
| **Switch camera** | プレビューまたは録画 | メインと PiP のレンズ入れ替え（両方録画継続） |
| **Screenshot** | プレビューまたは録画 | 合成フレームを即座に写真へ保存 |
| **Flashlight** | 背面カメラがメイン | トーチ切替（録画中は切替ボタンと入替） |
| **Preview pause** | プレビューのみ（録画中不可） | ライブプレビューを凍結して PiP/ズーム調整 |
| **Settings** | 常時 | アプリ設定パネルを開く |
| **Pending Exports** | 常時 | 未エクスポート `.mov` リスト |

### ジェスチャ

- **PiP をドラッグ** — プレビュー上の任意位置（セッション間で保存）
- **PiP をピンチ** — オーバーレイサイズ変更（設定でも可）
- **メインプレビューをピンチ** — **録画していないとき** メインカメラズーム
- **ズームプリセット** — ズームウィジェットからレベル保存/呼び出し

### プレビュー一時停止 vs 録画一時停止

| | プレビュー一時停止 | 録画一時停止 |
|---|---------------|-----------------|
| **トリガー** | プレビュートグルボタン | 録画中の Pause ボタン |
| **プレビュー** | 凍結 | 最終フレーム表示の場合あり |
| **Writer** | 非アクティブ | 開いているが append なし |
| **再開** | プレビュー再開をタップ | 録画再開をタップ |

プレビュー一時停止は **構図用**；録画一時停止は **出力から時間を除外**（PTS ジャンプカット — 書き出しに静止フレームなし）。

---

## Part 3 — カメラと PiP 設定 {#part-3}

**アプリ設定**（歯車アイコン）を開く。4 タブ: **Main Camera · Picture-in-Picture · Audio · General**。

**ライブプレビュー** に影響する設定（各カメラの解像度、フレームレート、手ブレ補正、HDR、ナイトモード）は即時更新。**Audio** 設定はプレビューを中断せず **次回** 録画に適用されます。

### Main Camera タブ

| 設定 | オプション | メモ |
|---------|---------|-------|
| Resolution | 720p / 1080p / 2K / 4K | 非対応はデバイスごとに無効 |
| Quality | Low / Medium / High | ビットレートトレードオフ |
| Frame rate | 24 / 30 fps | Multi-Cam は通常最大 **30 fps** — 60 fps なし |
| Stabilization | Off / Standard / Cinematic | レンズごと |
| HDR | Off / On / Auto | レンズごと |
| Night mode | Off / On / Auto | レンズごと |
| Reset | タブごと | メインカメラ既定に復元 |

### Picture-in-Picture タブ

メインと同じ映像パラメータに加え **UI スタイル**:

| 設定 | 範囲 / オプション |
|---------|-----------------|
| Scale | 短辺の 10%–100% |
| Position | プレビュー上でドラッグ（正規化座標を保存） |
| Border width | 調整可能 |
| Border color | プリセット + カスタム |
| Corner radius | 調整可能 |
| Opacity | 0–100% |

**ヒント:** メイン 4K のまま PiP 解像度を下げると発熱と容量を削減。明るい枠線は busy な背景で PiP を際立たせます。

すべての PiP スタイルは画面上だけでなく **最終書き出し動画** に適用されます。

---

## Part 4 — オーディオ設定 {#part-4}

| 設定 | オプション |
|---------|---------|
| Quality | Low (voice) / Standard / High (music) / Lossless |
| Format | AAC / PCM |
| Channels | Mono / Stereo |

> TwinPolarCam は **録画開始まで** オーディオセッションを **有効化しません** — 設定を閲覧しても音楽は止まりません。録画開始時、他のオーディオは一時停止します（システムカメラと同様）— スピーカー漏れを防ぐため。

---

## Part 5 — 録画セッション {#part-5}

### 典型的なワークフロー

1. プロンプトがあれば **権限を付与**。
2. メイン/PiP 設定と PiP 位置を **調整**。
3. **Record** をタップ — 画面常時点灯；オーディオセッション有効；タイマー開始。
4. **任意:** 一時停止、メイン/PiP 切替、スクリーンショット、ズーム（未録画時）。
5. **Stop** をタップ — セグメントをアプリストレージに確定（`TwinPolarCam_*.mov`）。
6. **Auto Export ON** → 即座に合成 + 写真保存。
7. **Auto Export OFF** → クリップが **Pending Exports** に表示され確認待ち。

### 録画タイマー

タイマーは **実効録画時間** を表示:

- フレームが実際に書き込まれている間のみカウント
- ユーザー一時停止と復旧可能な中断一時停止で **停止**
- セッション完全終了でリセット
- バックグラウンド時 Live Activity が同じ経過値を表示

### 向きの挙動

| 画面 | 既定の向き |
|--------|---------------------|
| カメラプレビュー / 録画 | **横向き** 強制 |
| アプリ設定 | 横向き、または一般で **縦向きロック** 有効時は縦 |
| Pending Exports | 横向き、または一般で **縦向きロック** 有効時は縦 |

レイアウト方向はコンテナサイズ + ロック設定に従い — ロックパネルでは物理的な持ち方とは独立です。

### 停止時に保存されるもの

各停止で **オリジナルマルチトラック `.mov`** が生成:

- Track 0: 背面カメラ映像
- Track 1: 前面カメラ映像
- オーディオトラック 1 本

`Application Support/TwinPolarCam/Videos/` に保存 — 意図的に **iCloud バックアップから除外**。

---

## Part 6 — 録画の信頼性 {#part-6}

TwinPolarCam にはイベントを分類し映像を保護する **Interruption Coordinator** が含まれます。

### 録画前

- **数 GB** の空きを確保 — デュアル 4K トラックは容量を急速に消費
- 他の **カメラアプリ** を終了
- 端末が温かくなる長時間セッションでは **1080p PiP** を検討
- バックグラウンド時にロック画面状態を見るため **Recording Live Activity**（一般）を有効化

### 復旧可能な中断（一時停止 → 再開、**同じセグメント**）

| イベント | 挙動 |
|-------|----------|
| 電話 / Siri | 録画一時停止；通話終了で **自動再開**（手動一時停止していなければ） |
| 他アプリが短時間カメラを占有 | 一時停止；解放後に再開する場合あり |
| アプリが **バックグラウンド**（Home、アプリ切替、ロック） | 一時停止；**25 秒** 安全タイマー開始 |

**Writer は開いたまま** — 再開後 **同じファイル** にフレームが続きます。一時停止時間は出力から **省略**（ジャンプカット）、静止フレームとして書き出されません。

> **コントロールセンターだけでは録画は一時停止しません** — 完全なバックグラウンド化のみがバックグラウンドパスを起動します。

### 非復旧イベント（Pending へ保存）

| イベント | 挙動 |
|-------|----------|
| メディアサービスリセット | セッション確定 → Pending |
| キャプチャランタイムエラー / 過熱シャットダウン | 可能なら保存 → Pending |
| Writer 失敗（ディスク満杯、I/O エラー） | 緊急保存 → トースト |

### 緊急保存

時間切れ時の最終手段:

| トリガー | アクション |
|---------|--------|
| 一時停止中バックグラウンド **約 25 秒** | 能動的にファイルを封印 → Pending |
| アプリ終了 | 確定まで最大 **約 8 秒** |
| Append 失敗 / writer `.failed` | 即座に保存試行 |

**バックグラウンド自動保存** 成功後、Live Activity が **Saved** を表示する場合があります（Live Activity 有効時、App 復帰まで）。

**緊急保存はセッションを終了** — そのセグメントは再開不可；追加映像は新規録画を開始してください。

### Live Activity（iOS 16.2+）

録画がバックグラウンドに続くとき:

| フェーズ | ロック画面 / Dynamic Island 表示 |
|-------|-------------------------------------|
| **Background waiting** | 経過時間 + 自動保存カウントダウン |
| **Saved** | クリップ保護済み — タップで App へ |

切替: **アプリ設定 → 一般 → Recording Live Activity**（デフォルト **オン**）。無効化しても信頼性は変わりません — ロック画面表示のみ。

詳細は **アプリ設定 → Help → Recording & Reliability** にもあります。

---

## Part 7 — エクスポートと Pending マネージャ {#part-7}

### エクスポートパイプライン

すべてのエクスポートは同じ手順:

1. **オリジナル `.mov`** — 停止/緊急保存からのマルチトラックファイル
2. **Compose** — `MultiCamVideoComposer` がメイン（背面）+ PiP（前面）→ 一時 `.mp4`
3. **Save** — 写真へ書き込み（Add Only 権限）
4. **Cleanup** — 一時 mp4 削除；任意でオリジナル `.mov` 削除
5. **キュー次項目** — キューがあれば Pending 最古項目を自動エクスポート

エクスポートのフレームレートは **メインカメラ** 設定に従います。設定の PiP スケール、位置、枠線、半径、不透明度が焼き込まれます。

### Pending Exports マネージャ

カメラ画面の **Pending** ボタン、または `twinpolarcam://pending` から開く。

| 機能 | 詳細 |
|---------|--------|
| **Contents** | オリジナル `TwinPolarCam_*.mov` のみ — 一時合成ファイルではない |
| **Sort** | 作成時刻 — エクスポート優先は **最古順** |
| **Layout** | **List** または **Grid** — 列数 2–6（一般設定） |
| **Preview** | エクスポート前にマルチトラッククリップを再生 |
| **Rescan Cache** | ディスクにファイルがあるのに UI が空のときリスト更新 |
| **Share** | Pending から個別クリップを共有 |
| **Delete** | 不要なオリジナルを削除 |

### バッチエクスポートとキュー

- 1 クリップ、**選択** クリップ、または **Export All** をエクスポート
- 最初のタスクは即実行；残りは **直列キュー**（一度に 1 合成 + 保存 — 端末上で安定）
- キュー完了まで **画面常時点灯**
- 単一タスクまたは **Cancel All** — 合成/保存を停止、一時 mp4 クリア；オリジナルは Pending に残る

### エクスポート設定（General タブ）

| トグル | デフォルト | 効果 |
|--------|---------|--------|
| **Auto Export** | 状況により | 停止時 → 即合成 + 写真保存 |
| **Auto-Delete Original After Export** | **Off** | 写真保存成功後 Pending から `.mov` 削除 |

PiP スタイルを変えて再エクスポートする可能性がある場合は **Auto-Delete OFF** を維持。

詳細は **アプリ設定 → Help → Export & Pending**。

---

## Part 8 — 一般設定 {#part-8}

| セクション | オプション |
|---------|---------|
| **Appearance** | System / Light / Dark — アプリ全体に即時適用 |
| **Keep Screen Awake** | アプリ使用中（録画/エクスポートは設定に関係なく常時点灯） |
| **Recording Live Activity** | ロック画面 + Dynamic Island 状態（iOS 16.2+） |
| **Portrait Lock for Settings** | アプリ設定を開くとき縦向きに回転 |
| **Portrait Lock for Pending** | Pending Exports を開くとき縦向きに回転 |
| **Auto Export** | Part 7 参照 |
| **Auto-Delete Original** | Part 7 参照 |
| **Language** | English / 简体中文 / 繁體中文 |
| **Tip Developer** | 任意 StoreKit 2 アプリ内チップ |
| **Send Feedback** | メール作成を開く |
| **Reset All Settings** | 確認必要 — Pending 動画は削除しない |

### About & App info

**アプリ設定 → App Information:**

- Rate in App / Rate on App Store
- Share App
- **About TwinPolarCam** — バージョン、プライバシー概要、リンク

---

## Part 9 — ヘルプ、ガイド、ショートカット {#part-9}

### アプリ内ガイド（Settings → Help）

| ガイド | 内容 |
|-------|----------|
| **How to Use** | クイックスタート、コントロール、PiP、エクスポート概要 |
| **Recording & Reliability** | 中断、バックグラウンド、Live Activity、FAQ |
| **Export & Pending** | パイプライン、キュー、バッチ、写真権限 |
| **Feature Tour** | 6 ページオンボーディングの再生 |

### ホーム画面クイックアクション

**アプリアイコンを長押し** — 4 つの固定ショートカット:

| アクション | ディープリンク |
|--------|-----------|
| Usage Guide | `twinpolarcam://usage-guide` |
| Recording Tips | `twinpolarcam://recording-guide` |
| Export Guide | `twinpolarcam://export-guide` |
| Feature Tour | `twinpolarcam://feature-guide` |

### Spotlight

デバイスで **「TwinPolarCam」** またはガイドタイトルを検索 — インデックスされたガイドが対応シートを開きます。

### その他のディープリンク

| URL | 開く画面 |
|-----|-------|
| `twinpolarcam://settings` | アプリ設定パネル |
| `twinpolarcam://pending` | Pending Exports |
| `twinpolarcam://feedback` | フィードバックメール |
| `twinpolarcam://recording` | Live Activity から復帰 |

完全リファレンス: [ショートカットリンク](../url-scheme)。

---

## Part 10 — トラブルシューティング {#part-10}

| 症状 | 想定原因 | 対処 |
|---------|--------------|------------|
| カメラ真っ黒 / 起動しない | シミュレータまたは非対応デバイス | 実機 Multi-Cam iPhone を使用；非対応画面を確認 |
| 解像度がグレーアウト | ハードウェア制限 | 低い段階を選択；旧モデルでは 4K 不可の場合あり |
| 録画が予期せず一時停止 | 通話、バックグラウンド、カメラ占有 | App に戻る；Part 6 を確認；クリップは Pending の可能性 |
| ロック後 Pending にクリップ | バックグラウンド安全保存（約 25 秒） | Pending からエクスポート — 映像は保存済み |
| エクスポート失敗 | 容量不足または写真拒否 | 空きを確保；設定 → プライバシー → 写真 → TwinPolarCam → 写真を追加 |
| エクスポートが遅い | 4K + 長いクリップ | 正常 — 画面点灯；キュー完了を待つ |
| 録画中に音楽停止 | 録画時オーディオセッション独占 | 想定どおり — システムカメラと同様 |
| タイマーに一時停止含まない | 設計どおり | 実効時間のみ |
| 書き出し PiP が不正 | 録画後に設定変更 | Auto-Delete オフでオリジナル `.mov` から再エクスポート |
| リスト空だがファイルあり | インデックス古い | Pending → **Rescan Cache** |
| App 発熱 / スロットリング | デュアル 4K 負荷 | PiP 解像度を下げる；テイクを短く；低電力モードを避ける |
| 非対応端末での返金 | デバイスゲート | 非対応画面のボタンまたは App Store |

まだ解決しない？ **アプリ設定 → Send Feedback** または下記メール。

---

</section>
<section lang="ko" markdown="1">

답변은 **현재 앱 동작**(복구 가능 일시정지/재개, 내보내기 대기열, Live Activity, 기기 게이트, 번체中文, 앱 내 가이드)을 반영합니다. 단계별 안내는 [사용자 가이드](index)를 참고하세요.

---

## 기기 및 요구 사항

### 어떤 iPhone이 TwinPolarCam을 지원하나요?

TwinPolarCam에는 **`AVCaptureMultiCamSession`** — Apple의 동시 멀티 카메라 API — 가 필요합니다. 지원 기기는 일반적으로 **iPhone XS, iPhone XR 및 이후 모든 모델**이지만, 실제 기능은 하드웨어 세대에 따라 다릅니다.

- **지원되지 않는 기기**는 실행 시 전용 화면이 표시되며, 카메라 UI 및 권한 흐름이 시작되지 않습니다.
- **iOS 시뮬레이터는 지원되지 않습니다** — 실물 카메라 및 Multi-Cam 없음.
- **실제 iPhone**이 필요합니다.

### 왜 단일 카메라 모드로 폴백하지 않나요?

전후 카메라 동시 녹화가 핵심 제품입니다. 혼란과 잘못된 기대를 피하기 위해 단일 카메라 폴백은 제거되었습니다. 기능 검사에 실패하면 미지원 화면의 **환불** 옵션을 사용하거나 지원팀에 문의하세요.

### 최대 녹화 해상도는?

TwinPolarCam은 각 카메라(메인과 PiP 독립)에 **720p, 1080p, 2K, 4K**를 제공합니다. 최대치는 기기에 따라 다릅니다.

- **iPhone 12 이후** — 일반적으로 4K 듀얼 촬영 가능.
- **구형 Multi-Cam 모델** — 하나 또는 두 렌즈가 1080p 또는 2K로 제한될 수 있음.

사용 불가 해상도는 설정에서 **자동으로 비활성화**됩니다.

### 60 fps를 사용할 수 없는 이유는?

Apple의 멀티 카메라 파이프라인은 두 카메라 동시 녹화 시 대부분 기기에서 **최대 30 fps**로 제한합니다. TwinPolarCam은 **24 fps 및 30 fps**를 제공합니다.**60 fps는 지원되지 않습니다** — 임의의 앱 제한이 아니라 시스템/하드웨어 제약입니다.

### iPad나 Mac에서 실행할 수 있나요?

**아니요.** TwinPolarCam은 **iPhone 전용**입니다.

### 필요한 iOS 버전은?

- **최소: iOS 15.0**
- **Live Activity: iOS 16.2+**
- **위젯 확장**(Live Activity UI): 앱 번들, Live Activity와 동일 OS 요구

---

## 녹화 및 PiP

### 메인 화면 카메라를 어떻게 전환하나요?

미리보기 또는 녹화 중 **전환 / 뒤집기 컨트롤**을 탭합니다. 전면과 후면 **역할이 화면에서 바뀝니다** — 어느 쪽이 전체 화면이든 두 영상 트랙은 계속 녹화됩니다.

### PiP 오버레이를 사용자 지정할 수 있나요?

예:

- **드래그**로 이동
- **핀치**로 크기 조절(PiP 설정의 배율도 가능)
- **앱 설정 → Picture-in-Picture**에서 **테두리 두께, 색, 모서리 반경, 불투명도, 상대 크기** 조정

변경은 라이브 미리보기에 반영되며 **내보낸 동영상에 굽혀집니다**.

### 내보낸 동영상에 PiP 위치가 나타나나요?

**예.** 합성 시 저장된 배율, 정규화 위치, 모서리 반경, 테두리, 불투명도가 사용됩니다.

### 세로로 녹화할 수 있나요?

**카메라 UI는 가로 모드에 최적화**되어 있습니다. 설정 또는 Pending 패널용 **세로 잠금**을 켤 수 있지만, 듀얼 미리보기와 녹화는 **가로**가 가장 좋습니다.

### 미리보기 일시정지란?

**미리보기 일시정지**는 **라이브 카메라 미리보기**(녹화 아님)를 고정해 PiP나 줌을 조정할 때 화면이 움직이지 않게 합니다.**녹화 중에는 사용 불가** — 대신 **녹화 일시정지**를 사용하세요.

### 줌 프리셋은 어떻게 작동하나요?

핀치 또는 화면 줌 컨트롤을 사용한 뒤 **현재 수준을 프리셋으로 저장**합니다. 프리셋을 불러 빠르게 구도를 바꿉니다. 줌은 **녹화하지 않을 때 메인 카메라 미리보기**에 적용됩니다.

### 스크린샷 버튼은 무엇을 하나요?

현재 **메인 + PiP 합성 레이아웃**을 정지 이미지로 캡처해 **사진**에 바로 저장 — 미리보기/녹화 중 모두 가능, 내보내기 단계 불필요.

### 플래시라이트는 언제 나타나나요?

**후면 카메라가 메인**일 때. 녹화 중에는 컨트롤 호에서 카메라 전환 버튼 **대신** 플래시라이트 버튼이 표시됩니다.

---

## 중단 및 안정성

### 녹화 중 전화가 오면 어떻게 되나요?

TwinPolarCam은 통화 중 **녹화를 일시정지**합니다. 통화 종료 후 **같은 세그먼트**(같은 `.mov` 파일)에서 **자동 재개** — **통화 전에 수동 일시정지하지 않았다면**.

일시정지 시간은 **출력 타임라인에서 잘립니다**(정지 프레임으로 내보내지 않음).

### 제어 센터를 내리면 녹화가 멈추나요?

**아니요.** **완전한 백그라운드 전환**(Home 제스처, 앱 전환, 잠금 화면)만 백그라운드 중단 경로를 트리거 — `willResignActive`만(예: 제어 센터 오버레이)으로는 아님.

### 녹화 중 앱 전환이나 화면 잠금 시?

1. 녹화 **일시정지**
2. **백그라운드 작업**이 Writer를 잠시 유지
3. 켜져 있으면 **Live Activity**에 경과 시간 및 자동 저장 카운트다운
4. **약 25초** 후 앱이 세그먼트를 **Pending Exports**에 **능동 저장**
5. **시간 초과 전 복귀** 시 **같은 세그먼트 재개** 가능

### 긴급 저장이란?

쓰기를 계속할 수 없을 때 최후 수단 확정:

- 백그라운드 안전 시간 초과(약 25초)
- 앱 종료(최대 약 8초 대기)
- Writer 실패, append 오류

**토스트 알림**이 표시됩니다. 클립은 **Pending**에 들어갑니다.**긴급 저장은 세션을 종료** — 해당 세그먼트는 재개 불가.

### 복구 가능 vs 치명적 중단 차이?

| 유형 | 예 | 결과 |
|------|-----|------|
| **복구 가능** | 통화, Siri, 짧은 카메라 점유, 백그라운드 | 일시정지 → **같은 세그먼트** 재개 |
| **치명적 / 긴급** | 미디어 리셋, 런타임 오류, 디스크 가득, 시간 초과 | 확정 → **Pending**, 세션 종료 |

### 일시정지가 영상에 공백을 만드나요?

**예 — 설계상 그렇습니다.** 일시정지 구간은 **생략**(PTS 점프 컷). 내보낸 파일은 긴 정지 구간 없이 연속 재생됩니다.

### 충돌 복구는?

앱이 예기치 않게 종료되어도 **유효한 확정 세그먼트**는 디스크에 남습니다. 다음 실행 시 TwinPolarCam이 복구 가능 파일을 감지해 **Pending**에 넣고 알림을 표시할 수 있습니다. 필요 시 Pending에서 **Rescan Cache** 사용.

### 녹화 중 화면이 항상 켜지는 이유?

녹화는 **Keep Screen Awake** 설정과 관계없이 **항상 깨어 있음 강제** — 촬영 중 실수로 잠기는 것 방지. 내보내기 대기열도 완료까지 화면 유지.

### 저전력 모드 영향?

**백그라운드 압력** 및 발열 스로틀링이 증가할 수 있습니다. 긴 세션에서는 해상도 낮추기, 충전 발열 피하기, 전원 연결을 고려하세요.

---

## Live Activity

### Recording Live Activity란?

**iOS 16.2+**에서 녹화 세션 중 앱을 떠나면 **잠금 화면 / Dynamic Island** 위젯에 상태 표시:

- **Background waiting** — 경과 시간 + 자동 저장 카운트다운
- **Saved** — 백그라운드 자동 저장 후 영상 보호됨(앱 재개까지)

### Live Activity 끄기?

**앱 설정 → 일반 → Recording Live Activity**. 안정성은 변하지 않음 — 잠금 화면 표시만 영향.

### 자동 저장 후 Live Activity가 남는 이유?

**백그라운드 자동 저장** 성공 후 활동이 **Saved**를 표시해 영상이 안전함을 알릴 수 있습니다. 앱으로 돌아오면(포그라운드) 종료.

---

## 내보내기 및 Pending

### 사용 가능한 내보내기 모드?

| 모드 | 동작 |
|------|------|
| **Auto Export ON** | 중지 → 즉시 합성 + 사진 저장 |
| **Auto Export OFF** | 중지 → 원본 `.mov`가 **Pending**에, 수동 내보내기까지 |

### 내보내기 대기열?

배치 내보내기는 **직렬** — 한 번에 하나 합성 + 저장, **Pending 최고래 클립 우선**. 4K 고부하에서도 기기 안정. 현재 작업 완료 시 다음 자동 시작.

### 내보내기 취소?

예:

- 진행 중 **단일 작업 취소**
- **Cancel All** — 활성 + 대기 작업 중지, 임시 mp4 제거
- **원본 `.mov`는 Pending에 남아** 재시도 가능

### Pending에 표시되는 파일?

원본 **`TwinPolarCam_*.mov`** 멀티트랙 녹화만 — 임시 합성 `TwinPolarCam_MultiCam_*.mp4` 아님.

### PiP 스타일 변경 후 재내보내기?

**Auto-Delete Original After Export**가 **꺼짐**(기본)이면 **예**. PiP 설정 조정 후 Pending에서 다시 내보내기.

### 내보내기가 오래 걸리는 이유?

4K 듀얼 트랙 합성은 **CPU/GPU 집약적**. 긴 클립·높은 프레임레이트일수록 시간 증가. 대기열 완료까지 화면 자동 유지.

### 내보내기 실패 — 영상 손실?

**아니요.** 원본 `.mov`는 Pending에 남음.**여유 공간** 및 **사진 권한**(Add Only) 확인 후 재시도.

### 내보내기 전 저장 위치?

`Application Support/TwinPolarCam/Videos/` — **iCloud 백업에서 의도적으로 제외**.

### 출력 형식?

고품질 **H.264 / AAC mp4**; 프레임 간격은 **메인 카메라 프레임레이트** 설정 따름.

### 새 클립 녹화 중 내보내기?

새 세션 시작 중에도 파이프라인 실행 가능하나 **동시 고부하**는 발열 유발 — 순차 사용이 안전.

---

## 설정 및 언어

### 앱 지원 언어?

**English**, **简体中文**, **繁體中文** — **앱 설정 → 일반 → 언어**.

### Auto-Delete Original After Export?

**ON**이면 **성공한** 사진 저장 후 Pending에서 원본 `.mov` 제거.**OFF**(기본)이면 재합성용 멀티트랙 소스 유지.

기본 **OFF** — 업그레이드 사용자가 원본 소실에 놀라지 않도록.

### 녹화 시작 시 음악이 멈추는 이유?

TwinPolarCam은 녹화 시작 시 오디오 세션 활성화(Apple 카메라 앱과 동일) — **마이크 독점**으로 스피커 소리 녹음 방지. 녹화 중지 시 음악 재개(`notifyOthersOnDeactivation`).

**녹화 없이** 앱 탐색 시 음악 **중단 안 됨**.

### 외관 모드?

일반 설정 **System / Light / Dark** — `preferredColorScheme`으로 앱 전체 즉시 적용.

---

## 권한 및 개인정보

### TwinPolarCam이 데이터를 수집하나요?

**아니요.** 촬영·합성·저장 모두 기기 내. 분석 SDK 없음, 계정 없음, 업로드 없음. [개인정보 처리방침](../privacy) 참고.

### 왜 사진은 추가만 요청하나요?

**Add Only** 권한(iOS 14+)으로 기존 라이브러리 **읽지 않고** 완성 동영상 저장 — 최소 권한.

### iCloud 백업?

앱 저장소 원본 녹화는 **백업 제외** 표시. 사진으로 내보낸 동영상은 **사용자** 사진/iCloud 설정 따름.

---

## 팁 및 지원

### 피드백?

**앱 설정 → Send Feedback**(메일) 또는 `twinpolarcam://feedback`.

### 앱 내 가이드?

**앱 설정 → Help** — How to Use, Recording & Reliability, Export & Pending, Feature Tour.

### 앱 밖에서 가이드?

홈 화면 **아이콘 길게 누르기**, **Spotlight**, **`twinpolarcam://`** — [단축 링크](../url-scheme).

### 추가 도움?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 보통 48시간 내 답변.

[사용자 가이드](index) · [단축 링크](../url-scheme) · [개인정보 처리방침](../privacy)

---

## 전체 사용자 가이드

아래는 이전 지원 페이지의 전체 제품 안내입니다. 위에 빠른 Q&A(해당 시)가 남아 있습니다.

---

## 이 페이지 목차

| 파트 | 주제 |
|------|--------|
| [Part 1](#part-1) | 첫 실행, 권한, 미지원 기기 |
| [Part 2](#part-2) | 녹화, 일시정지, 스크린샷, 전환, 플래시, 미리보기 일시정지 |
| [Part 3](#part-3) | 메인 카메라 및 PiP 화질·스타일 |
| [Part 4](#part-4) | 오디오 품질, 형식, 채널 |
| [Part 5](#part-5) | 시작→중지 흐름, 타이머, 방향 |
| [Part 6](#part-6) | 중단, 백그라운드 저장, Live Activity |
| [Part 7](#part-7) | 합성 파이프라인, 대기열, 일괄 내보내기, 취소 |
| [Part 8](#part-8) | 외관, 화면 켜짐, 내보내기 토글, 언어 |
| [Part 9](#part-9) | 앱 내 가이드, Spotlight, 빠른 작업, 딥링크 |
| [Part 10](#part-10) | 증상→원인→조치 빠른 참조 |

> **빠른 답이 필요하면?** [FAQ](../faq) 또는 [단축 링크](../url-scheme).

---

## Part 1 — 첫 실행 및 요구 사항 {#part-1}

### 환영 가이드(6페이지)

첫 실행 시 **6페이지 온보딩**으로 듀얼 촬영, PiP, 내보내기, 안정성, 개인정보 소개. 가로 스와이프 또는 **Continue**; 마지막 페이지 **Start Recording**.

언제든: **앱 설정 → Help → Feature Tour** 또는 `twinpolarcam://feature-guide`.

마지막 온보딩 페이지에서 앱 내 **How to Use** 가이드 직접 열기 가능.

### 권한(필수)

| 권한 | 요청 시점 | 이유 |
|------------|------------|-----|
| **카메라** | 지원 기기 첫 실행 | 듀얼 영상 캡처 |
| **마이크** | 첫 녹화 전 | 오디오 트랙 |
| **사진(Add Only)** | 라이브러리 첫 내보내기 | 완성 동영상 저장 — 기존 라이브러리 **읽지 않음** |

TwinPolarCam은 **Add Only** 사진 접근(iOS 14+) 사용. 영상 업로드 없음.

### 기기 요구 사항

| 요구 | 세부 |
|-------------|--------|
| **하드웨어** | Apple **Multi-Cam** 지원 iPhone(`AVCaptureMultiCamSession`) — 보통 **iPhone XS/XR 이후** |
| **플랫폼** | **실제 iPhone만** — 시뮬레이터 카메라/Multi-Cam 없음 |
| **최소 OS** | iOS **15.0+**(Live Activity **16.2+**) |
| **방향** | 카메라 화면 **가로** 최적화; 일부 패널 세로 잠금 가능 |

### 미지원 기기 화면

**듀얼 카메라 모드 불가** iPhone은 카메라 UI 대신 **전용 안내** — 해당 화면에서 **카메라·사진 권한 요청 없음**.

여전히 가능:

- 모든 앱 내 가이드(Usage/Recording/Export)
- 가능 시 **App Store 환불**(StoreKit 2)
- 지원 문의

> **중요:** TwinPolarCam은 **단일 카메라 모드로 폴백하지 않습니다**. 미지원 하드웨어는 실행 시 차단.

### 앱 내 언어

**English**, **简体中文**, **繁體中文** — **앱 설정 → 일반 → 언어**. 즉시 적용. 이 지원 사이트도 3개 언어.

---

## Part 2 — 메인 화면 및 컨트롤 {#part-2}

**가로**로 기기를 잡으면 가장 넓은 듀얼 미리보기. 한쪽에 컨트롤 열; 메인 뷰는 한 카메라, **PiP 오버레이**는 다른 카메라.

### 컨트롤 참조

| 컨트롤 | 사용 가능 | 기능 |
|---------|----------------|--------------|
| **Record** | 미리보기(미녹화) | 듀얼 카메라+오디오 녹화 시작 |
| **Pause / Resume** | 녹화/일시정지 중 | 프레임 쓰기 일시정지; 타이머 정지 |
| **Stop** | 녹화/일시정지 중 | 세그먼트 확정 → 내보내기 또는 Pending |
| **Switch camera** | 미리보기/녹화 | 메인 vs PiP 렌즈 교환(둘 다 녹화 계속) |
| **Screenshot** | 미리보기/녹화 | 합성 프레임 즉시 사진 저장 |
| **Flashlight** | 후면이 메인 | 토치(녹화 중 전환 버튼 대체) |
| **Preview pause** | 미리보기만 | 라이브 미리보기 고정해 PiP/줌 조정 |
| **Settings** | 항상 | 앱 설정 패널 |
| **Pending Exports** | 항상 | 미내보내기 `.mov` 목록 |

### 제스처

- **PiP 드래그** — 미리보기 어디든(세션 간 저장)
- **PiP 핀치** — 크기(설정에서도)
- **메인 핀치** — **미녹화 시** 메인 줌
- **줌 프리셋** — 줌 위젯에서 저장/불러오기

### 미리보기 vs 녹화 일시정지

| | 미리보기 일시정지 | 녹화 일시정지 |
|---|---------------|-----------------|
| **트리거** | 미리보기 토글 | 녹화 중 Pause |
| **미리보기** | 고정 | 마지막 프레임 가능 |
| **Writer** | 비활성 | 열림, append 없음 |
| **재개** | 미리보기 재개 | 녹화 재개 |

미리보기 일시정지는 **구도용**; 녹화 일시정지는 **출력에서 시간 제외**(PTS 점프 컷).

---

## Part 3 — 카메라 및 PiP 설정 {#part-3}

**앱 설정**(톱니). 4탭: **Main Camera · Picture-in-Picture · Audio · General**.

**라이브 미리보기** 영향 설정(해상도, fps, 손떨림, HDR, 야간 모드) 즉시 반영.**Audio**는 **다음** 녹화에 적용, 미리보기 중단 없음.

### Main Camera 탭

| 설정 | 옵션 | 메모 |
|---------|---------|-------|
| Resolution | 720p/1080p/2K/4K | 미지원은 기기별 비활성 |
| Quality | Low/Medium/High | 비트레이트 |
| Frame rate | 24/30 fps | Multi-Cam 보통 **30 fps** max |
| Stabilization | Off/Standard/Cinematic | 렌즈별 |
| HDR/Night mode | Off/On/Auto | 렌즈별 |

### Picture-in-Picture 탭

메인과 동일 영상 파라미터 + **UI 스타일**(Scale 10–100%, Position, 테두리, 모서리, 불투명도).

**팁:** 메인 4K+PiP 낮은 해상도로 발열·용량 절감. 밝은 테두리는 복잡한 배경에서 PiP 강조.

모든 PiP 스타일은 **최종 내보낸 동영상**에 적용.

---

## Part 4 — 오디오 설정 {#part-4}

| 설정 | 옵션 |
|---------|---------|
| Quality | Low(voice)/Standard/High(music)/Lossless |
| Format | AAC/PCM |
| Channels | Mono/Stereo |

> TwinPolarCam은 **녹화 시작 전** 오디오 세션 **비활성** — 설정 탐색 시 음악 안 멈춤. 녹화 시작 시 다른 오디오 일시정지(시스템 카메라와 동일).

---

## Part 5 — 녹화 세션 {#part-5}

### 일반 흐름

1. **권한 부여**
2. 메인/PiP 및 PiP 위치 **조정**
3. **Record** — 화면 유지; 오디오 활성; 타이머
4. 선택: 일시정지, 전환, 스크린샷, 줌(미녹화)
5. **Stop** — `TwinPolarCam_*.mov` 저장
6. **Auto Export ON** → 즉시 합성+사진
7. **OFF** → **Pending Exports**

### 타이머

**실제 녹화 시간**만; 일시정지·복구 가능 중단 시 **정지**; 세션 종료 시 리셋; 백그라운드 Live Activity 동일 값.

### 방향

| 화면 | 기본 |
|--------|---------------------|
| 카메라 미리보기/녹화 | **가로** 강제 |
| 앱 설정/Pending | 가로 또는 **세로 잠금** |

### 중지 시 저장

**멀티트랙 `.mov`**: Track0 후면, Track1 전면, 오디오 1 — `Application Support/TwinPolarCam/Videos/`, **iCloud 백업 제외**.

---

## Part 6 — 녹화 안정성 {#part-6}

**Interruption Coordinator**가 이벤트 분류 및 영상 보호.

### 녹화 전

- **수 GB** 여유; 다른 **카메라 앱** 종료; 장시간 **1080p PiP** 고려; **Recording Live Activity** 켜기

### 복구 가능(일시정지→재개, **같은 세그먼트**)

| 이벤트 | 동작 |
|-------|----------|
| 전화/Siri | 일시정지; 종료 후 **자동 재개**(수동 일시정지 아니면) |
| 다른 앱 짧은 카메라 점유 | 일시정지; 해제 후 재개 가능 |
| **백그라운드** | 일시정지; **25초** 타이머 |

Writer **열린 채**; 일시정지 구간 **출력에서 생략**(점프 컷).

> **제어 센터만으로는 일시정지 안 됨** — 완전 백그라운드만.

### 비복구(Pending 저장)

미디어 리셋, 런타임 오류/과열, Writer 실패 → Pending.

### 긴급 저장

백그라운드 약 **25초**, 앱 종료 최대 **~8초**, append/writer 실패 → 즉시 저장 시도. **Saved** Live Activity 가능.**세션 종료**, 같은 세그먼트 재개 불가.

### Live Activity(iOS 16.2+)

**Background waiting** / **Saved** — **앱 설정 → 일반 → Recording Live Activity**(기본 on).

---

## Part 7 — 내보내기 및 Pending 관리 {#part-7}

### 파이프라인

1. 원본 `.mov` 2. **Compose**(`MultiCamVideoComposer`) 3. **Save**(Add Only) 4. **Cleanup** 5. 대기열 다음(**최고래 우선**)

### Pending 관리

**Pending** 또는 `twinpolarcam://pending` — 원본 mov만, **최고래 우선**, List/Grid, 미리보기, **Rescan Cache**, 공유/삭제.

### 일괄·대기열

직렬 큐, 화면 유지, **Cancel**/**Cancel All**, 원본 Pending 유지.

### 내보내기 설정

**Auto Export** / **Auto-Delete Original After Export**(기본 Off) — PiP 변경 재내보내기 시 Off 유지.

---

## Part 8 — 일반 설정 {#part-8}

| 섹션 | 옵션 |
|---------|---------|
| **Appearance** | System/Light/Dark |
| **Keep Screen Awake** | 앱 사용 중(녹화/내보내기는 항상) |
| **Recording Live Activity** | 잠금 화면+Dynamic Island |
| **Portrait Lock**(설정/Pending) | 세로 회전 |
| **Language** | English/简体中文/繁體中文 |
| **Tip Developer** | StoreKit 2 |
| **Send Feedback** / **Reset All Settings** | 메일/확인( Pending 영상 유지) |

**App Information:** 평가, 공유, About TwinPolarCam.

---

## Part 9 — 도움말·가이드·단축어 {#part-9}

**Settings → Help:** How to Use, Recording & Reliability, Export & Pending, Feature Tour.

**아이콘 길게 누르기:** `usage-guide`, `recording-guide`, `export-guide`, `feature-guide`.

**Spotlight** 검색. 기타: `settings`, `pending`, `feedback`, `recording`.

[단축 링크](../url-scheme).

---

## Part 10 — 문제 해결 {#part-10}

| 증상 | 원인 | 조치 |
|---------|--------------|------------|
| 검은 화면/시작 안 됨 | 시뮬레이터/미지원 | 실제 Multi-Cam iPhone |
| 해상도 비활성 | 하드웨어 | 낮은 단계 |
| 예기치 않은 일시정지 | 통화/백그라운드/카메라 | Part 6; Pending 확인 |
| 잠금 후 Pending | ~25초 안전 저장 | Pending에서 내보내기 |
| 내보내기 실패 | 공간/사진 거부 | 공간 확보; 사진 추가만 |
| 내보내기 느림 | 4K+긴 클립 | 정상; 대기열 대기 |
| 녹화 시 음악 정지 | 오디오 독점 | 예상됨 |
| 타이머에 일시정지 미포함 | 설계 | 실제 시간만 |
| PiP 불일치 | 녹화 후 설정 변경 | Auto-Delete off 재내보내기 |
| 목록 비었으나 파일 있음 | 인덱스 | **Rescan Cache** |
| 발열 | 듀얼 4K | PiP 해상도↓ |
| 환불 | 기기 게이트 | 미지원 화면/App Store |

**앱 설정 → Send Feedback** 또는 이메일.

---

</section>
<section lang="ru" markdown="1">

Ответы отражают **текущее поведение приложения** (восстанавливаемая пауза/продолжение, очередь экспорта, Live Activity, проверка устройства, 繁體中文, встроенные руководства). Пошаговые инструкции — в [руководстве пользователя](index).

---

## Устройство и требования

### Какие iPhone поддерживают TwinPolarCam?

TwinPolarCam требует **`AVCaptureMultiCamSession`** — API Apple для одновременной съёмки с нескольких камер. Обычно поддерживаются **iPhone XS, iPhone XR и все более новые модели**, но возможности зависят от поколения железа.

- **Неподдерживаемые устройства** при запуске видят отдельный экран — UI камеры и запросы разрешений не начинаются.
- **Симулятор iOS не поддерживается** — нет физических камер и Multi-Cam.
- Нужен **реальный iPhone**.

### Почему нет отката на одну камеру?

Одновременная запись с двух камер — ядро продукта. Откат на одну камеру убран, чтобы избежать путаницы. При провале проверки возможностей используйте **возврат средств** на экране неподдерживаемого устройства или свяжитесь с поддержкой.

### Максимальное разрешение записи?

**720p, 1080p, 2K и 4K** на каждую камеру (основная и PiP независимо). Максимум зависит от устройства:

- **iPhone 12 и новее** — обычно доступна двойная 4K.
- **Старые Multi-Cam модели** — могут ограничивать одну или обе линзы 1080p или 2K.

Недоступные разрешения **автоматически отключены** в настройках.

### Почему нет 60 fps?

Конвейер Multi-Cam Apple на большинстве устройств ограничивает **максимум 30 fps** при одновременной записи. TwinPolarCam предлагает **24 и 30 fps**. **60 fps не поддерживается** — ограничение системы/железа, а не приложения.

### iPad или Mac?

**Нет.** TwinPolarCam **только для iPhone**.

### Какая версия iOS нужна?

- **Минимум: iOS 15.0**
- **Live Activity: iOS 16.2+**
- **Расширение виджета** (UI Live Activity): в составе приложения, те же требования ОС

---

## Запись и PiP

### Как переключить основную камеру?

Нажмите **переключение / отражение** в предпросмотре или при записи. Роли передней и задней камеры **меняются на экране** — обе видеодорожки продолжают запись независимо от полноэкранного вида.

### Можно настроить оверлей PiP?

Да:

- **Перетаскивание**
- **Щипок** для масштаба (или в настройках PiP)
- **Толщина, цвет, скругление, непрозрачность и размер** в **Настройки приложения → Picture-in-Picture**

Изменения видны в предпросмотре и **вшиваются в экспорт**.

### Позиция PiP в экспорте?

**Да.** Компоновщик использует сохранённые масштаб, нормализованную позицию, скругление, рамку и непрозрачность.

### Портретная запись?

**UI камеры оптимизирован для альбомной ориентации.** Можно включить **блокировку портрета** для панелей настроек или Pending, но двойной предпросмотр и запись лучше **горизонтально**.

### Что такое пауза предпросмотра?

**Пауза предпросмотра** замораживает **живой предпросмотр** (не запись) для настройки PiP/зума.**Недоступна во время записи** — используйте **паузу записи**.

### Пресеты зума?

Щипок или элемент зума, затем **сохранить уровень как пресет**. Зум для **основной камеры, когда не идёт запись**.

### Кнопка скриншота?

Сохраняет **текущую компоновку основной + PiP** в **Фото** — в предпросмотре или при записи, без экспорта.

### Когда появляется фонарик?

Когда **задняя камера основная**. При записи кнопка фонарика **заменяет** переключение камеры на дуге управления.

---

## Прерывания и надёжность

### Звонок во время записи?

TwinPolarCam **ставит запись на паузу**. После звонка **автовозобновление того же сегмента** (тот же `.mov`) — **если вы не ставили паузу вручную** до звонка.

Время паузы **вырезается из таймлайна** (не экспортируется как замороженные кадры).

### Центр управления опускает запись на паузу?

**Нет.** Только **полный уход в фон** (Home, переключение приложения, блокировка) — не один `willResignActive` (например, оверлей Центра управления).

### Смена приложения или блокировка экрана?

1. Запись **на паузе**
2. **Фоновая задача** ненадолго держит writer
3. **Live Activity** (если включена) — время и обратный отсчёт автосохранения
4. Через **~25 с** сегмент **активно сохраняется** в **Pending Exports**
5. **До таймаута** можно **продолить тот же сегмент**

### Экстренное сохранение?

Финализация, когда запись невозможна: таймаут фона (~25 с), завершение приложения (до ~8 с), сбой writer/append. **Toast**, клипы в **Pending**. **Сессия завершена** — сегмент не возобновить.

### Восстанавливаемые vs фатальные прерывания?

| Тип | Примеры | Результат |
|------|----------|--------|
| **Восстанавливаемые** | Звонок, Siri, краткий захват камеры, фон | Пауза → **тот же сегмент** |
| **Фатальные** | Сброс медиа, ошибка, диск полон, таймаут | → **Pending**, конец сессии |

### Пауза даёт разрыв в видео?

**Да, по задумке.** Интервалы паузы **опускаются** (PTS jump-cut).

### Восстановление после сбоя?

**Валидные сегменты** остаются на диске; при следующем запуске — **Pending** и алерт; **Rescan Cache** при необходимости.

### Почему экран всегда включён при записи?

**Принудительное не гасить** независимо от **Keep Screen Awake**. Очередь экспорта тоже держит экран.

### Режим низкого заряда?

Может усилить **фоновое давление** и тrottling. Для длинных сессий — ниже разрешение, меньше нагрева.

---

## Live Activity

### Recording Live Activity?

На **iOS 16.2+** при уходе из приложения во время записи виджет **экрана блокировки / Dynamic Island**:

- **Background waiting** — время + обратный отсчёт автосохранения
- **Saved** — после автосохранения в фоне (до возврата в приложение)

### Отключить Live Activity?

**Настройки приложения → Общие → Recording Live Activity**. Надёжность не меняется — только видимость на экране блокировки.

### Почему Live Activity остаётся после автосохранения?

Может показывать **Saved**, пока не вернётесь в приложение.

---

## Экспорт и Pending

### Режимы экспорта?

| Режим | Поведение |
|------|----------|
| **Auto Export ON** | Стоп → сразу компоновка + Фото |
| **Auto Export OFF** | Стоп → исходный `.mov` в **Pending** |

### Очередь экспорта?

**Последовательно** — один compose+save, **сначала старейший Pending**. Следующая задача автоматически.

### Отмена экспорта?

**Cancel** одной задачи или **Cancel All**; **исходные `.mov` в Pending**.

### Что в Pending?

Только **`TwinPolarCam_*.mov`**, не временные `TwinPolarCam_MultiCam_*.mp4`.

### Переэкспорт с другим PiP?

**Да**, если **Auto-Delete Original After Export** **выкл.** (по умолчанию).

### Долгий экспорт?

4K двойная дорожка **нагружает CPU/GPU**; экран включён до конца очереди.

### Сбой экспорта — видео потеряно?

**Нет.** Проверьте **место** и **разрешение Фото** (Add Only).

### Где файлы до экспорта?

`Application Support/TwinPolarCam/Videos/` — **исключено из iCloud Backup**.

### Формат?

**H.264 / AAC mp4**; частота кадров — настройка **основной камеры**.

### Экспорт во время новой записи?

Возможно, но **совместная нагрузка** греет устройство — лучше по очереди.

---

## Настройки и язык

**English**, **简体中文**, **繁體中文** — **Настройки приложения → Общие → Язык**.

**Auto-Delete Original After Export:** при **ON** удаляет `.mov` после успешного сохранения в Фото; **OFF** (по умолчанию) — сохраняет исходник для перекомпоновки.

Музыка паузится при записи (**эксклюзивный микрофон**, как Камера Apple); без записи — **не прерывается**. Внешний вид: **System / Light / Dark** через `preferredColorScheme`.

---

## Разрешения и конфиденциальность

**Данные не собираются.** Всё на устройстве; без аналитики и аккаунта. [Политика конфиденциальности](../privacy).

**Add Only** для Фото (iOS 14+) — сохранение без чтения библиотеки.

Исходники в приложении **исключены из резервной копии**; экспорт в Фото — по вашим настройкам iCloud.

---

## Советы и поддержка

**Настройки → Send Feedback** или `twinpolarcam://feedback`. **Help** — How to Use, Recording & Reliability, Export & Pending, Feature Tour.

Быстрые действия, Spotlight, `twinpolarcam://` — [Shortcut Links](../url-scheme).

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — обычно в течение 48 часов.

[Руководство](index) · [Ссылки](../url-scheme) · [Конфиденциальность](../privacy)

---

## Полное руководство

Ниже — полный обзор продукта с прежней страницы поддержки.

## На этой странице

| Часть | Тема |
|------|--------|
| [Part 1](#part-1) | Первый запуск, разрешения, неподдерживаемые устройства |
| [Part 2](#part-2) | Запись, пауза, скриншот, переключение, вспышка |
| [Part 3](#part-3) | Качество и стиль основной камеры и PiP |
| [Part 4](#part-4) | Аудио |
| [Part 5](#part-5) | Сценарий записи, таймер, ориентация |
| [Part 6](#part-6) | Прерывания, фон, Live Activity |
| [Part 7](#part-7) | Компоновка, очередь, пакетный экспорт |
| [Part 8](#part-8) | Внешний вид, экран, экспорт, язык |
| [Part 9](#part-9) | Руководства, Spotlight, быстрые действия |
| [Part 10](#part-10) | Симптом → причина → решение |

> **Быстрый ответ?** [FAQ](../faq) или [Shortcut Links](../url-scheme).

---

## Part 1 — Первый запуск и требования {#part-1}

**6-страничный onboarding** при первом запуске. **Continue** / **Start Recording**. Повтор: **Help → Feature Tour**, `twinpolarcam://feature-guide`.

| Разрешение | Когда | Зачем |
|------------|------------|-----|
| **Камера** | Первый запуск | Двойная съёмка |
| **Микрофон** | Перед первой записью | Аудио |
| **Фото (Add Only)** | Первый экспорт | Сохранение — **без чтения** библиотеки |

**Multi-Cam** iPhone (обычно **XS/XR+**), **только реальное устройство**, iOS **15.0+** (Live Activity **16.2+**), UI камеры — **альбомная**.

Неподдерживаемое устройство: отдельный экран, **без запросов камеры/Фото**; гайды, **возврат** StoreKit 2, поддержка. **Без отката на одну камеру.**

Языки: **English / 简体中文 / 繁體中文** в настройках.

---

## Part 2 — Главный экран и управление {#part-2}

**Альбомная** ориентация для широкого двойного предпросмотра.

| Элемент | Когда | Действие |
|---------|----------------|--------------|
| **Record** | Предпросмотр | Старт двойной записи + аудио |
| **Pause/Resume** | Запись/пауза | Пауза записи кадров |
| **Stop** | Запись/пауза | Финал → экспорт или Pending |
| **Switch** | Всегда в записи | Меняет main/PiP |
| **Screenshot** | Предпросмотр/запись | Кадр в Фото |
| **Flashlight** | Задняя main | Фонарик |
| **Preview pause** | Только предпросмотр | Заморозка для настройки |
| **Settings / Pending** | Всегда | Панели |

Жесты: drag/pinch PiP, pinch main (без записи), пресеты зума. Пауза предпросмотра vs записи — время записи **не попадает** в файл (PTS jump-cut).

---

## Part 3 — Камера и PiP {#part-3}

**Main Camera · PiP · Audio · General**. Предпросмотр обновляется сразу; аудио — со **следующей** записи.

720p–4K, качество, 24/30 fps (не 60), стабилизация, HDR, night mode по линзам. PiP: те же параметры + масштаб, позиция, рамка, скругление, непрозрачность — **в экспорте**.

---

## Part 4 — Аудио {#part-4}

Качество (Low/Standard/High/Lossless), AAC/PCM, Mono/Stereo. Сессия **не активна** до **Start Recording** — музыка при настройках не стопорится.

---

## Part 5 — Сессия записи {#part-5}

1. Разрешения → 2. Настройка PiP → 3. **Record** → 4. Опции → 5. **Stop** → 6–7. Auto Export или Pending.

Таймер — **эффективное время записи**. Ориентация: камера **альбом**, настройки/Pending — альбом или portrait lock.

`.mov`: track0 задняя, track1 передняя, аудио; `Application Support/...` **без iCloud backup**.

---

## Part 6 — Надёжность записи {#part-6}

**Interruption Coordinator**. Перед записью: **несколько ГБ** свободно, закрыть другие камеры, **1080p PiP** при нагреве, Live Activity.

Восстанавливаемые: звонок/Siri/фон — **тот же сегмент**, writer открыт, пауза вырезается. **Control Center alone не паузит.**

Невосстанавливаемые → Pending. Экстренное сохранение ~25 с фон / ~8 с terminate — **конец сессии**.

Live Activity: **Background waiting** / **Saved**.

---

## Part 7 — Экспорт и Pending {#part-7}

`.mov` → `MultiCamVideoComposer` → temp mp4 → Фото → cleanup → очередь (**старейший первым**).

Pending: list/grid, preview, Rescan, share, delete. Пакет **последовательно**. **Auto Export** / **Auto-Delete** (по умолчанию Off).

---

## Part 8 — Общие настройки {#part-8}

Appearance, Keep Awake, Live Activity, portrait lock, экспорт, языки, чаевые, feedback, reset (Pending не удаляет).

---

## Part 9 — Справка и ссылки {#part-9}

Help-гайды; long-press: usage/recording/export/feature guides; Spotlight; `settings`, `pending`, `feedback`, `recording`. [Shortcut Links](../url-scheme).

---

## Part 10 — Устранение неполадок {#part-10}

| Симптом | Причина | Действие |
|---------|--------------|------------|
| Чёрный экран | Симулятор/неподдерживаемо | Реальный Multi-Cam iPhone |
| Серое разрешение | Железо | Ниже tier |
| Неожиданная пауза | Звонок/фон | Part 6; Pending |
| Pending после блокировки | ~25 с save | Экспорт из Pending |
| Сбой экспорта | Место/Фото | Add Photos |
| Медленный экспорт | 4K длинный клип | Ждать очередь |
| Музыка стоп | Эксклюзив аудио | Норма |
| PiP неверный | Настройки после записи | Re-export, Auto-Delete off |
| Пустой список | Индекс | **Rescan Cache** |
| Нагрев | Dual 4K | Ниже PiP |
| Возврат | Device gate | Экран неподдержки |

**Send Feedback** или email.

---

</section>
<section lang="th" markdown="1">

คำตอบสะท้อน**พฤติกรรมแอปปัจจุบัน** (หยุด/ต่อได้, คิวส่งออก, Live Activity, ตรวจอุปกรณ์, 繁體中文, คู่มือในแอป) ดูขั้นตอนใน [คู่มือผู้ใช้](index)

---

## อุปกรณ์และข้อกำหนด

### iPhone รุ่นใดรองรับ TwinPolarCam?

ต้องใช้ **`AVCaptureMultiCamSession`** — API มัลติแคมของ Apple โดยทั่วไป **iPhone XS/XR ขึ้นไป** ขึ้นกับร поколениеฮาร์ดแวร์

- **ไม่รองรับ** — หน้าจอเฉพาะตอนเปิด ไม่เริ่ม UI กล้อง
- **Simulator ไม่รองรับ**
- ต้องเป็น **iPhone จริง**

### ทำไมไม่ถอยเป็นกล้องเดียว?

การบันทึกสองกล้องพร้อมกันคือแกนผลิตภัณฑ์ ไม่มี fallback — ใช้ **คืนเงิน** หรือติดต่อซัพพอร์ต

### ความละเอียดสูงสุด?

**720p–4K** ต่อกล้อง (Main/PiP แยก) **iPhone 12+** มัก dual 4K ได้ รุ่นเก่าอาจจำกัด 1080p/2K

### ทำไมไม่มี 60 fps?

Multi-Cam ส่วนใหญ่ **สูงสุด 30 fps** TwinPolarCam มี **24/30** **ไม่รองรับ 60 fps**

### iPad/Mac?

**ไม่** — **iPhone เท่านั้น**

### iOS?

**ขั้นต่ำ 15.0** · Live Activity **16.2+**

---

## การบันทึกและ PiP

สลับ Main/PiP ด้วยปุ่ม **Switch/Flip** — ทั้งสองแทร็กบันทึกต่อ PiP ลาก/บีบ ตั้งค่าใน **App Settings → Picture-in-Picture** **ฝังในไฟล์ส่งออก** Preview pause ใช้ได้เมื่อ**ไม่ได้บันทึก** แฟลชเมื่อกล้องหลังเป็น Main

---

## การขัดจังหวะและความน่าเชื่อถือ

โทรศัพท์: **หยุดชั่วคราว** แล้ว**ต่อ segment เดิม** (`.mov`) Control Center อย่างเดียว**ไม่หยุด** พื้นหลัง: หยุด → Live Activity → **~25 วิ** → **Pending** บันทึกฉุกเฉินจบเซสชัน ช่วงหยุด**ตัดออก** (PTS jump-cut)

---

## Live Activity

**iOS 16.2+** **Background waiting** / **Saved** ปิดที่ **General → Recording Live Activity**

---

## ส่งออกและ Pending

Auto Export เปิด/ปิด คิว**เรียงตามเก่าสุด** ยกเลิกได้ ไฟล์ **`TwinPolarCam_*.mov`** **H.264/AAC** เก็บที่ `Application Support/...` **ไม่สำรอง iCloud**

---

## การตั้งค่าและภาษา

**English / 简体中文 / 繁體中文** Auto-Delete Original ค่าเริ่ม **ปิด** เพลงหยุด**เฉพาะตอนบันทึก**

---

## สิทธิ์และความเป็นส่วนตัว

**ไม่เก็บข้อมูล** [นโยบาย](../privacy) รูปภาพ **เพิ่มเท่านั้น**

---

## เคล็ดลับและซัพพอร์ต

**Send Feedback** **Help** `twinpolarcam://` [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

[คู่มือ](index) · [ลิงก์](../url-scheme) · [นโยบาย](../privacy)

---

## คู่มือฉบับเต็ม

Parts 1–10: เริ่มต้น, ควบคุม, PiP, เสียง, เซสชัน, ความน่าเชื่อถือ, ส่งออก, ทั่วไป, ช่วยเหลือ, แก้ปัญหา

---

## Part 1 — เริ่มต้น {#part-1}

Onboarding 6 หน้า สิทธิ์กล้อง/ไมค์/รูป Add Only Multi-Cam **XS/XR+**

---

## Part 2 — หน้าหลัก {#part-2}

แนวนอน Record Pause Stop Switch Screenshot

---

## Part 3 — กล้อง & PiP {#part-3}

720p–4K 24/30 fps

---

## Part 4 — เสียง {#part-4}

AAC/PCM เริ่ม session เมื่อ Record

---

## Part 5 — เซสชัน {#part-5}

`.mov` multi-track

---

## Part 6 — ความน่าเชื่อถือ {#part-6}

~25 วิ พื้นหลัง Interruption Coordinator

---

## Part 7 — ส่งออก {#part-7}

คิวเรียง MultiCamVideoComposer

---

## Part 8 — ทั่วไป {#part-8}

ธีม Live Activity ภาษา

---

## Part 9 — ช่วยเหลือ {#part-9}

Spotlight deep links

---

## Part 10 — แก้ปัญหา {#part-10}

| อาการ | สาเหตุ | แก้ |
|--------|--------|-----|
| จอดำ | Simulator/ไม่รองรับ | iPhone จริง |
| Pending หลังล็อก | ~25 วิ | ส่งออกจาก Pending |
| ส่งออกล้ม | พื้นที่/รูป | Add Photos |
| รายการว่าง | index | **Rescan Cache** |

---

</section>
<section lang="de" markdown="1">

Antworten spiegeln **aktuelles App-Verhalten** (wiederherstellbare Pause/Fortsetzung, Export-Warteschlange, Live Activity, Geräte-Gate, 繁體中文, In-App-Anleitungen). Schritt-für-Schritt: [Benutzerhandbuch](index).

---

## Gerät & Anforderungen

### Welche iPhones unterstützen TwinPolarCam?

TwinPolarCam benötigt **`AVCaptureMultiCamSession`** — Apples API für gleichzeitige Multi-Kamera-Aufnahme. Unterstützt sind typischerweise **iPhone XS, iPhone XR und alle neueren Modelle**; die genaue Fähigkeit hängt von der Hardware ab.

- **Nicht unterstützte Geräte** sehen beim Start einen eigenen Bildschirm — Kamera-UI und Berechtigungsflow starten nicht.
- **iOS-Simulator wird nicht unterstützt** — keine physischen Kameras, kein Multi-Cam.
- Ein **echtes iPhone** ist erforderlich.

### Warum kein Single-Camera-Fallback?

Gleichzeitige Dual-Aufnahme ist das Kernprodukt. Single-Camera-Fallback wurde entfernt, um Verwirrung zu vermeiden. Scheitert der Capability-Check, nutzen Sie **Erstattung** auf dem Unsupported-Bildschirm oder kontaktieren Sie den Support.

### Maximale Aufnahmeauflösung?

**720p, 1080p, 2K und 4K** pro Kamera (Main und PiP unabhängig). Maximum hängt vom Gerät ab:

- **iPhone 12 und neuer** — Dual-4K meist verfügbar.
- **Ältere Multi-Cam-Modelle** — ggf. 1080p oder 2K für eine oder beide Linsen.

Nicht verfügbare Auflösungen werden in den Einstellungen **automatisch deaktiviert**.

### Warum kein 60 fps?

Apples Multi-Cam-Pipeline begrenzt die meisten Geräte bei gleichzeitiger Aufnahme auf **max. 30 fps**. TwinPolarCam bietet **24 und 30 fps**. **60 fps wird nicht unterstützt** — System-/Hardware-Limit, kein willkürliches App-Limit.

### iPad oder Mac?

**Nein.** TwinPolarCam ist **nur für iPhone**.

### Welche iOS-Version?

- **Minimum: iOS 15.0**
- **Live Activity: iOS 16.2+**
- **Widget Extension** (Live-Activity-UI): im App-Bundle, gleiche OS-Anforderung

---

## Aufnahme & PiP

### Main-Kamera wechseln?

Tippen Sie während Vorschau oder Aufnahme auf **Wechsel/Flip**. Front- und Rück-Rollen **tauschen auf dem Bildschirm** — beide Videospuren laufen weiter.

### PiP-Overlay anpassen?

Ja:

- **Ziehen** zum Verschieben
- **Zoomen** (Pinch oder Skala in PiP-Einstellungen)
- **Rahmen, Farbe, Eckenradius, Deckkraft, Größe** unter **App-Einstellungen → Picture-in-Picture**

Änderungen in der Vorschau und **im Export eingebrannt**.

### PiP-Position im Export?

**Ja.** Der Composer nutzt gespeicherte Skala, normalisierte Position, Eckenradius, Rahmen und Deckkraft.

### Hochformat-Aufnahme?

Die **Kamera-UI ist für Querformat optimiert**. **Portrait-Lock** für Einstellungen/Pending möglich; Dual-Vorschau und Aufnahme funktionieren am besten **horizontal**.

### Preview-Pause?

**Preview-Pause** friert die **Live-Vorschau** ein (nicht die Aufnahme) für PiP-/Zoom-Anpassungen. **Nicht während aktiver Aufnahme** — nutzen Sie **Aufnahme-Pause**.

### Zoom-Presets?

Pinch oder Zoom-Steuerung, dann **aktuelles Level als Preset speichern**. Zoom gilt für **Main-Vorschau ohne laufende Aufnahme**.

### Screenshot-Taste?

Speichert **Main + PiP** als Still in **Fotos** — in Vorschau oder Aufnahme, ohne Export.

### Wann erscheint die Taschenlampe?

Wenn die **Rückkamera Main** ist. Bei Aufnahme **ersetzt** die Taschenlampe den Kamera-Wechsel am Bogen.

---

## Unterbrechungen & Zuverlässigkeit

### Anruf während Aufnahme?

TwinPolarCam **pausiert**. Nach dem Anruf **Auto-Fortsetzung desselben Segments** (`.mov`) — **außer** Sie hatten vorher manuell pausiert.

Pausenzeit wird **aus der Timeline geschnitten** (keine eingefrorenen Frames).

### Control Center ziehen — Pause?

**Nein.** Nur **voller Hintergrund** (Home, App-Wechsel, Sperrbildschirm) — nicht allein `willResignActive` (z. B. Control-Center-Overlay).

### App-Wechsel oder Sperrbildschirm?

1. Aufnahme **pausiert**
2. **Background Task** hält Writer kurz
3. **Live Activity** (optional) mit Zeit und Auto-Save-Countdown
4. Nach **~25 s** Speicherung in **Pending Exports**
5. **Vor Timeout** können Sie **dasselbe Segment fortsetzen**

### Notfall-Speicherung?

Finalisierung, wenn nicht weiter geschrieben werden kann: Hintergrund-Timeout (~25 s), App-Ende (~8 s), Writer-Fehler. **Toast**, Clips in **Pending**. **Session beendet** — Segment nicht fortsetzbar.

### Wiederherstellbar vs. fatal?

| Typ | Beispiele | Ergebnis |
|------|----------|--------|
| **Wiederherstellbar** | Anruf, Siri, kurzer Kamera-Diebstahl, Hintergrund | Pause → **gleiches Segment** |
| **Fatal** | Media-Reset, Fehler, voller Speicher, Timeout | → **Pending**, Session-Ende |

### Pause erzeugt Lücke?

**Ja, beabsichtigt.** Pausen werden **weggeschnitten** (PTS jump-cut).

### Absturz-Wiederherstellung?

**Gültige Segmente** bleiben auf der Platte; beim nächsten Start **Pending** und Hinweis; ggf. **Rescan Cache**.

### Bildschirm immer an?

Aufnahme **erzwingt wach** unabhängig von **Keep Screen Awake**. Export-Warteschlange hält den Bildschirm ebenfalls an.

### Stromsparmodus?

Kann **Hintergrunddruck** und Drosselung erhöhen. Für lange Sessions: niedrigere Auflösung, weniger Hitze.

---

## Live Activity

### Recording Live Activity?

Ab **iOS 16.2+** bei Verlassen der App während Aufnahme: Widget auf **Sperrbildschirm / Dynamic Island**:

- **Background waiting** — Zeit + Auto-Save-Countdown
- **Saved** — nach Hintergrund-Auto-Save (bis App wieder im Vordergrund)

### Live Activity ausschalten?

**App-Einstellungen → Allgemein → Recording Live Activity**. Zuverlässigkeit unverändert — nur Sperrbildschirm-Sichtbarkeit.

### Live Activity nach Auto-Save?

Kann **Saved** zeigen, bis Sie die App wieder öffnen.

---

## Export & Pending

### Export-Modi?

| Modus | Verhalten |
|------|----------|
| **Auto Export AN** | Stopp → sofort Compose + Fotos |
| **Auto Export AUS** | Stopp → `.mov` in **Pending** |

### Export-Warteschlange?

**Seriell** — ein Compose+Save, **ältestes Pending zuerst**. Nächste Aufgabe automatisch.

### Export abbrechen?

**Cancel** einzeln oder **Cancel All**; **Originale `.mov` bleiben** in Pending.

### Dateien in Pending?

Nur **`TwinPolarCam_*.mov`**, nicht temporäre `TwinPolarCam_MultiCam_*.mp4`.

### PiP-Stil ändern und neu exportieren?

**Ja**, wenn **Auto-Delete Original After Export** **aus** (Standard).

### Export dauert lange?

Dual-4K **CPU/GPU-intensiv**; Bildschirm bleibt an bis die Warteschlange fertig ist.

### Export fehlgeschlagen — Video weg?

**Nein.** Prüfen Sie **Speicher** und **Fotos-Berechtigung** (Add Only).

### Speicherort vor Export?

`Application Support/TwinPolarCam/Videos/` — **ohne iCloud-Backup**.

### Ausgabeformat?

**H.264 / AAC mp4**; Bildrate folgt **Main-Kamera**.

### Export während neuer Aufnahme?

Möglich, aber **gemeinsame Last** erhitzt das Gerät — nacheinander ist sicherer.

---

## Einstellungen & Sprache

**English**, **简体中文**, **繁體中文** — **App-Einstellungen → Allgemein → Sprache**.

**Auto-Delete Original After Export:** bei **AN** wird `.mov` nach erfolgreichem Fotos-Save gelöscht; **AUS** (Standard) behält Quelle für Re-Compose.

Musik pausiert bei Aufnahme (**exklusives Mikrofon**, wie Apple Kamera); ohne Aufnahme **keine** Unterbrechung. Erscheinungsbild: **System / Hell / Dunkel**.

---

## Berechtigungen & Datenschutz

**Keine Datenerhebung.** Alles on-device; keine Analytics, kein Konto. [Datenschutz](../privacy).

**Add Only** für Fotos — Speichern **ohne** Bibliothek zu lesen.

App-Rohdaten **backup-ausgeschlossen**; exportierte Videos in Fotos folgen **Ihren** iCloud-Einstellungen.

---

## Tipps & Support

**App-Einstellungen → Send Feedback** oder `twinpolarcam://feedback`. **Help** — How to Use, Recording & Reliability, Export & Pending, Feature Tour.

Schnellaktionen, Spotlight, `twinpolarcam://` — [Shortcut Links](../url-scheme).

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — in der Regel innerhalb von 48 Stunden.

[Handbuch](index) · [Shortcut Links](../url-scheme) · [Datenschutz](../privacy)

---

## Vollständiges Handbuch

Nachfolgend der vollständige Produktüberblick.

## Auf dieser Seite

| Teil | Thema |
|------|--------|
| [Part 1](#part-1) | Erster Start, Berechtigungen, Unsupported |
| [Part 2](#part-2) | Aufnahme, Pause, Screenshot, Wechsel |
| [Part 3](#part-3) | Main-Kamera & PiP |
| [Part 4](#part-4) | Audio |
| [Part 5](#part-5) | Workflow, Timer, Orientierung |
| [Part 6](#part-6) | Unterbrechungen, Hintergrund, Live Activity |
| [Part 7](#part-7) | Export-Pipeline, Warteschlange |
| [Part 8](#part-8) | Allgemeine Einstellungen |
| [Part 9](#part-9) | Hilfe, Spotlight, Shortcuts |
| [Part 10](#part-10) | Symptom → Ursache → Lösung |

> **Kurzantwort?** [FAQ](../faq) oder [Shortcut Links](../url-scheme).

---

## Part 1 — Erster Start & Anforderungen {#part-1}

**6-Seiten-Onboarding** beim ersten Start. **Continue** / **Start Recording**. Wiederholung: **Help → Feature Tour**, `twinpolarcam://feature-guide`.

| Berechtigung | Wann | Warum |
|------------|------------|-----|
| **Kamera** | Erster Start | Dual-Aufnahme |
| **Mikrofon** | Vor erster Aufnahme | Audio |
| **Fotos (Add Only)** | Erster Export | Speichern — **ohne Lesen** der Bibliothek |

**Multi-Cam**-iPhone (typisch **XS/XR+**), **nur echtes Gerät**, iOS **15.0+** (Live Activity **16.2+**), Kamera-UI **Querformat**.

Unsupported: eigener Bildschirm, **keine** Kamera/Fotos-Prompts; Guides, **Erstattung** StoreKit 2, Support. **Kein Single-Cam-Fallback.**

Sprachen: **English / 简体中文 / 繁體中文** in Einstellungen.

---

## Part 2 — Hauptbildschirm & Steuerung {#part-2}

**Querformat** für breite Dual-Vorschau.

| Element | Wann | Aktion |
|---------|----------------|--------------|
| **Record** | Vorschau | Dual-Aufnahme + Audio starten |
| **Pause/Resume** | Aufnahme/Pause | Frame-Aufnahme pausieren |
| **Stop** | Aufnahme/Pause | Final → Export oder Pending |
| **Switch** | Immer bei Aufnahme | Main/PiP tauschen |
| **Screenshot** | Vorschau/Aufnahme | Still → Fotos |
| **Flashlight** | Rückseite Main | Taschenlampe |
| **Preview pause** | Nur Vorschau | Einfrieren zum Anpassen |
| **Settings / Pending** | Immer | Panels |

Gesten: PiP ziehen/pinchen, Main pinchen (ohne Aufnahme), Zoom-Presets. Preview- vs Aufnahme-Pause — Pausenzeit **nicht** in Datei (PTS jump-cut).

---

## Part 3 — Kamera & PiP {#part-3}

**Main Camera · PiP · Audio · General**. Vorschau sofort; Audio ab **nächster** Aufnahme.

720p–4K, Qualität, 24/30 fps (kein 60), Stabilisierung, HDR, Night pro Linse. PiP: gleiche Parameter + Skala, Position, Rahmen, Radius, Deckkraft — **im Export**.

---

## Part 4 — Audio {#part-4}

Qualität (Low/Standard/High/Lossless), AAC/PCM, Mono/Stereo. Session **inaktiv** bis **Start Recording** — Musik beim Einstellen nicht gestoppt.

---

## Part 5 — Aufnahme-Session {#part-5}

1. Berechtigungen → 2. PiP → 3. **Record** → 4. Optionen → 5. **Stop** → 6–7. Auto Export oder Pending.

Timer = **effektive Aufnahmezeit**. Orientierung: Kamera **Querformat**, Settings/Pending Quer oder Portrait-Lock.

`.mov`: track0 hinten, track1 vorn, Audio; `Application Support/...` **ohne iCloud-Backup**.

---

## Part 6 — Aufnahme-Zuverlässigkeit {#part-6}

**Interruption Coordinator**. Vor Aufnahme: **mehrere GB** frei, andere Kameras schließen, **1080p PiP** bei Hitze, Live Activity.

Wiederherstellbar: Anruf/Siri/Hintergrund — **gleiches Segment**, Writer offen, Pause geschnitten. **Control Center allein pausiert nicht.**

Nicht wiederherstellbar → Pending. Notfall ~25 s Hintergrund / ~8 s Terminate — **Session-Ende**.

Live Activity: **Background waiting** / **Saved**.

---

## Part 7 — Export & Pending {#part-7}

`.mov` → `MultiCamVideoComposer` → temp mp4 → Fotos → cleanup → Warteschlange (**ältestes zuerst**).

Pending: Liste/Raster, Vorschau, Rescan, Teilen, Löschen. Batch **seriell**. **Auto Export** / **Auto-Delete** (Standard Aus).

---

## Part 8 — Allgemeine Einstellungen {#part-8}

Erscheinungsbild, Keep Awake, Live Activity, Portrait-Lock, Export, Sprachen, Trinkgeld, Feedback, Reset (Pending bleibt).

---

## Part 9 — Hilfe & Links {#part-9}

Help-Guides; Long-Press: usage/recording/export/feature; Spotlight; `settings`, `pending`, `feedback`, `recording`. [Shortcut Links](../url-scheme).

---

## Part 10 — Fehlerbehebung {#part-10}

| Symptom | Ursache | Maßnahme |
|---------|--------------|------------|
| Schwarze Kamera / startet nicht | Simulator oder nicht unterstützt | Echtes Multi-Cam-iPhone |
| Auflösung ausgegraut | Hardware-Limit | Niedrigere Stufe |
| Unerwartete Pause | Anruf, Hintergrund | Part 6; ggf. Pending |
| Clip in Pending nach Sperre | ~25 s Hintergrund-Save | Aus Pending exportieren |
| Export fehlgeschlagen | Speicher / Fotos | Platz; Fotos → TwinPolarCam → Hinzufügen |
| Export langsam | 4K langer Clip | Warteschlange abwarten |
| Musik stoppt | Exklusive Audio-Session | Erwartet |
| PiP falsch im Export | Einstellungen nach Aufnahme | Re-Export, Auto-Delete aus |
| Liste leer | Index | **Rescan Cache** |
| App heiß | Dual-4K | PiP-Auflösung senken |
| Erstattung unsupported | Device gate | Unsupported-Bildschirm |

**Send Feedback** oder E-Mail.

---

</section>
<section lang="fr" markdown="1">

Les réponses reflètent le **comportement actuel de l’app** (pause/reprise récupérable, file d’export, Live Activity, contrôle appareil, 繁體中文, guides in-app). Guide pas à pas : [Guide utilisateur](index).

---

## Appareil et exigences

### Quels iPhone prennent en charge TwinPolarCam ?

TwinPolarCam requiert **`AVCaptureMultiCamSession`** — l’API Apple multi-caméra simultanée. Prise en charge typique : **iPhone XS, iPhone XR et modèles ultérieurs** ; les capacités exactes dépendent du matériel.

- **Appareils non pris en charge** : écran dédié au lancement — pas d’UI caméra ni de flux de permissions.
- **Simulateur iOS non pris en charge** — pas de caméras physiques ni Multi-Cam.
- **iPhone réel** requis.

### Pourquoi pas de repli mono-caméra ?

L’enregistrement dual simultané est le cœur du produit. Le repli mono a été retiré pour éviter la confusion. Échec du test : **remboursement** sur l’écran non pris en charge ou support.

### Résolution maximale ?

**720p, 1080p, 2K et 4K** par caméra (main et PiP indépendamment). Maximum selon l’appareil :

- **iPhone 12 et plus** — dual 4K en général disponible.
- **Anciens Multi-Cam** — plafond 1080p ou 2K sur une ou deux lentilles.

Résolutions indisponibles **désactivées automatiquement** dans les réglages.

### Pourquoi pas 60 fps ?

Le pipeline Multi-Cam Apple limite souvent à **30 fps max** en enregistrement simultané. TwinPolarCam propose **24 et 30 fps**. **60 fps non pris en charge** — contrainte système/matériel.

### iPad ou Mac ?

**Non.** TwinPolarCam est **iPhone uniquement**.

### Version iOS ?

- **Minimum : iOS 15.0**
- **Live Activity : iOS 16.2+**
- **Extension widget** (UI Live Activity) : incluse, mêmes exigences OS

---

## Enregistrement et PiP

### Changer la caméra principale ?

Appuyez sur **basculer/retourner** en prévisualisation ou enregistrement. Les rôles avant/arrière **s’échangent à l’écran** — les deux pistes continuent.

### Personnaliser le PiP ?

Oui : **glisser**, **pincer**, réglages **App → Picture-in-Picture** (bordure, couleur, coins, opacité, taille). **Gravé à l’export**.

### Position PiP à l’export ?

**Oui** — échelle, position normalisée, coins, bordure, opacité sauvegardés.

### Portrait ?

UI **optimisée paysage** ; verrou portrait pour Réglages/Pending possible ; dual preview/enregistrement **horizontal** de préférence.

### Pause aperçu ?

Gèle la **prévisualisation live** (pas l’enregistrement). **Indisponible pendant enregistrement actif** — utilisez **pause enregistrement**.

### Presets zoom ?

Pincer puis **enregistrer le niveau** ; zoom sur **main hors enregistrement**.

### Bouton capture ?

**Main + PiP** → **Photos**, prévisualisation ou enregistrement.

### Lampe torche ?

Quand **arrière = main** ; en enregistrement **remplace** le bouton bascule.

---

## Interruptions et fiabilité

### Appel pendant enregistrement ?

**Pause** ; fin d’appel **reprise du même segment** (`.mov`) sauf pause manuelle avant l’appel. Temps de pause **coupé** de la timeline.

### Centre de contrôle ?

**Non** — seulement **arrière-plan complet** (Accueil, changement d’app, verrouillage).

### Changement d’app ou verrouillage ?

1. **Pause** 2. Tâche arrière-plan 3. **Live Activity** optionnelle 4. **~25 s** → **Pending** 5. **Avant timeout** : **reprise même segment**.

### Sauvegarde d’urgence ?

Finalisation si écriture impossible (~25 s fond, ~8 s fin app, erreur writer). **Toast**, clips **Pending**, **session terminée**.

### Récupérable vs fatal ?

| Type | Exemples | Résultat |
|------|----------|--------|
| **Récupérable** | Appel, Siri, vol caméra bref, fond | Pause → **même segment** |
| **Fatal** | Reset média, erreur, disque plein | **Pending**, fin session |

### Pause = trou dans la vidéo ?

**Oui** — intervalles **omis** (jump-cut PTS).

### Récupération après crash ?

Segments valides sur disque ; au relancement **Pending** + alerte ; **Rescan Cache** si besoin.

### Écran toujours allumé ?

Enregistrement **force éveil** ; file d’export aussi.

### Mode économie d’énergie ?

Peut augmenter pression arrière-plan et throttling.

---

## Live Activity

### Recording Live Activity ?

**iOS 16.2+** : widget **écran verrouillé / Dynamic Island** — **Background waiting** / **Saved**.

### Désactiver ?

**Réglages app → Général → Recording Live Activity**.

### Reste après auto-save ?

Peut afficher **Saved** jusqu’au retour au premier plan.

---

## Export et Pending

| Mode | Comportement |
|------|----------|
| **Auto Export ON** | Stop → Photos immédiat |
| **OFF** | `.mov` dans **Pending** |

File **sérieille**, plus ancien d’abord. **Annulation** possible ; **`.mov` conservés**. Seulement **`TwinPolarCam_*.mov`**. Re-export PiP si **Auto-Delete Original** **off**. 4K dual = lent ; échec export → clip **pas perdu**. Stockage : `Application Support/...` **hors backup iCloud**. **H.264/AAC mp4**.

---

## Réglages et langue

**English / 简体中文 / 繁體中文**. **Auto-Delete Original** : ON supprime `.mov` après succès ; OFF (défaut) garde la source. Musique pausée **uniquement** à l’enregistrement. Apparence **System / Light / Dark**.

---

## Autorisations et confidentialité

**Aucune collecte.** [Confidentialité](../privacy). Photos **Ajout uniquement**. Originaux app **hors sauvegarde** ; Photos selon **votre** iCloud.

---

## Astuces et support

**Send Feedback**, **Help**, `twinpolarcam://`, [Shortcut Links](../url-scheme). [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com).

[Guide](index) · [Liens](../url-scheme) · [Confidentialité](../privacy)

---

## Guide complet

| Partie | Sujet |
|------|--------|
| [Part 1](#part-1) | Premier lancement, permissions |
| [Part 2](#part-2) | Contrôles |
| [Part 3](#part-3) | Caméra & PiP |
| [Part 4](#part-4) | Audio |
| [Part 5](#part-5) | Session |
| [Part 6](#part-6) | Fiabilité |
| [Part 7](#part-7) | Export |
| [Part 8](#part-8) | Général |
| [Part 9](#part-9) | Aide |
| [Part 10](#part-10) | Dépannage |

---

## Part 1 — Premier lancement {#part-1}

Onboarding 6 pages ; permissions Caméra / Micro / Photos Add Only ; Multi-Cam **XS/XR+** ; iOS **15.0+** ; pas de repli mono-caméra.

---

## Part 2 — Écran principal {#part-2}

Paysage ; Record, Pause, Stop, Switch, Screenshot, Flashlight, Preview pause, Settings/Pending.

---

## Part 3 — Caméra & PiP {#part-3}

720p–4K, 24/30 fps, PiP stylé **dans l’export**.

---

## Part 4 — Audio {#part-4}

Qualité, AAC/PCM ; session active au **Record** seulement.

---

## Part 5 — Session {#part-5}

Workflow ; timer = temps effectif ; `.mov` multi-piste.

---

## Part 6 — Fiabilité {#part-6}

Interruption Coordinator ; ~25 s fond ; Live Activity.

---

## Part 7 — Export {#part-7}

`MultiCamVideoComposer` ; file sérieille ; Pending.

---

## Part 8 — Général {#part-8}

Apparence, Live Activity, langues, reset.

---

## Part 9 — Aide {#part-9}

Guides, Spotlight, deep links.

---

## Part 10 — Dépannage {#part-10}

| Symptôme | Cause | Action |
|---------|--------------|------------|
| Écran noir | Simulateur / non pris en charge | iPhone Multi-Cam réel |
| Export échoué | Stockage / Photos | Espace ; permission Ajout |
| Pending après verrou | ~25 s save | Exporter depuis Pending |
| PiP incorrect | Réglages après prise | Re-export, Auto-Delete off |
| Liste vide | Index | **Rescan Cache** |

**Send Feedback** ou e-mail.

---

</section>
<section lang="tr" markdown="1">

Yanıtlar **güncel uygulama davranışını** yansıtır (kurtarılabilir duraklat/devam, dışa aktarma kuyruğu, Live Activity, cihaz kapısı, 繁體中文, uygulama içi kılavuzlar). Adım adım: [Kullanıcı Kılavuzu](index).

---

## Cihaz ve gereksinimler

### Hangi iPhone'lar desteklenir?

TwinPolarCam **`AVCaptureMultiCamSession`** — Apple eşzamanlı çoklu kamera API'si gerektirir. Genelde **iPhone XS/XR ve sonrası**; yetenek donanıma bağlıdır.

- **Desteklenmeyen cihazlar** — özel ekran; kamera UI başlamaz.
- **Simülatör desteklenmez.**
- **Gerçek iPhone** gerekir.

### Neden tek kamera yedeği yok?

Eşzamanlı çift kayıt ürünün özüdür. Desteklenmeyen cihazda **iade** veya destek.

### Maksimum çözünürlük?

**720p–4K** kamera başına. **iPhone 12+** genelde dual 4K. **60 fps yok** — **24/30 fps**.

### iPad/Mac?

**Hayır** — **yalnızca iPhone**.

### iOS?

**En az 15.0** · Live Activity **16.2+**

---

## Kayıt ve PiP

**Switch/Flip** main/PiP değiştirir — her iki iz devam eder. PiP sürükle/pinch; **App Settings → Picture-in-Picture** — **dışa aktarmaya gömülür**. Önizleme duraklatma **aktif kayıtta yok**.

---

## Kesintiler ve güvenilirlik

Arama: **duraklat**, sonra **aynı segment** (`.mov`). Control Center **tek başına duraklatmaz**. Arka plan: **~25 sn** → **Pending**. Acil kayıt oturumu **sonlandırır**. Duraklama **PTS jump-cut**.

---

## Live Activity

**iOS 16.2+** **Background waiting** / **Saved**. Kapat: **General → Recording Live Activity**.

---

## Dışa aktarma ve Pending

Auto Export açık/kapalı; **seri kuyruk**; yalnızca **`TwinPolarCam_*.mov`**; **H.264/AAC**; `Application Support/...` **iCloud yedek dışı**.

---

## Ayarlar ve dil

**English / 简体中文 / 繁體中文**. Auto-Delete Original varsayılan **kapalı**. Müzik yalnızca **kayıtta** durur.

---

## İzinler ve gizlilik

**Veri toplanmaz.** [Gizlilik](../privacy). Fotoğraflar **Yalnızca Ekle**.

---

## İpuçları ve destek

**Send Feedback**, **Help**, `twinpolarcam://`. [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

[Kılavuz](index) · [Bağlantılar](../url-scheme) · [Gizlilik](../privacy)

---

## Tam kılavuz

Part 1–10: başlangıç, kontroller, PiP, ses, oturum, güvenilirlik, dışa aktarma, genel, yardım, sorun giderme.

---

## Part 1 — İlk başlatma {#part-1}

6 sayfa onboarding; Kamera/Mikro/Fotoğraf Add Only; Multi-Cam **XS/XR+**.

---

## Part 2 — Ana ekran {#part-2}

Yatay; Record, Pause, Stop, Switch.

---

## Part 3 — Kamera & PiP {#part-3}

720p–4K, 24/30 fps.

---

## Part 4 — Ses {#part-4}

AAC/PCM; oturum **Record** ile başlar.

---

## Part 5 — Kayıt oturumu {#part-5}

`.mov` çoklu iz.

---

## Part 6 — Güvenilirlik {#part-6}

~25 sn arka plan; Interruption Coordinator.

---

## Part 7 — Dışa aktarma {#part-7}

MultiCamVideoComposer; seri kuyruk.

---

## Part 8 — Genel {#part-8}

Görünüm, Live Activity, diller.

---

## Part 9 — Yardım {#part-9}

Spotlight, deep link.

---

## Part 10 — Sorun giderme {#part-10}

| Belirti | Neden | Çözüm |
|---------|--------------|------------|
| Siyah ekran | Simülatör/destek yok | Gerçek Multi-Cam iPhone |
| Pending kilit sonrası | ~25 sn kayıt | Pending'den dışa aktar |
| Dışa aktarma hatası | Alan/Fotoğraflar | Add Photos |
| Boş liste | indeks | **Rescan Cache** |

---

</section>
