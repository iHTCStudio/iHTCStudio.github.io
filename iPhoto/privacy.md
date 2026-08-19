---
layout: doc
title: iPhoto — Privacy Policy
app_id: iPhoto
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iPhoto — on-device photo processing, no account, no photo upload.
---

<section lang="en" markdown="1">

iHTC Studio ("we", "us" or "our"; formerly iHTCTeam) built iPhoto (also known as "爱修图" / "愛修圖"). This page describes our policies regarding data when you use the app.

## Summary

**iPhoto does not require an account and does not upload your photos to iHTC Studio servers.** Capture, beauty, filters, and export run on your device. Optional **iCloud sync** covers preferences only — never photo files.

## Data Collection

We do not operate a backend that collects your personal information:

- **No account** — No registration, email, or phone number is required.
- **No analytics or ads** — No third-party analytics, advertising, or tracking SDKs.
- **No photo upload for analysis** — Face landmarks and rendering stay on-device.

## How the App Works

- **Storage** — Projects (original / thumbnail / edit state) live in the app sandbox. Widget thumbnails use the App Group container.
- **Face beauty** — See **Face Data and On-Device Beauty Processing** below.
- **Photo Library** — Access is limited to imports you choose and optional export saves you start.
- **Metadata strip** — Optionally removes EXIF / GPS / device fields from exports you create.

## Face Data and On-Device Beauty Processing

When you use beauty features (Capture live preview, shutter bake, or the editor Beauty tool), iPhoto analyzes faces **only on your device** using Apple’s Vision framework (`VNDetectFaceLandmarksRequest`). This is **not** face recognition, identity matching, biometrics enrollment, or authentication.

### What face data is processed

- **Transient landmarks (memory only):** face bounding box, face contour, eyes, eyebrows, outer/inner lips, pupils, and related geometry used to build masks for optional cosmetic edits (smooth, whiten, slim, eyes, teeth, blush, lipstick).
- **Persisted with a project (optional):** a **normalized face bounding rectangle** plus your chosen **beauty strength / color parameters** (`FaceBeautyEdit`), so per-face settings can be restored when you reopen the project. **Full landmark coordinates are not written to disk.**

### Use

Face geometry is used solely to apply the beauty adjustments **you** enable during capture preview, photo capture, editor preview, thumbnail refresh, and export/share. It is not used for advertising, profiling, or identification.

### Sharing

**Face data is never shared with third parties.** It is not uploaded to iHTC Studio servers or any cloud analysis API. Optional iCloud Key-Value sync covers **preferences only** (for example language, theme, capture beauty recipe toggles) and **does not sync photos or face landmarks**.

### Storage location

- Photos and project edit files: **app sandbox on your device**
- Transient landmarks: **RAM only** (cleared when you leave the editor / clear analysis cache)
- Widget thumbnails: App Group on your device (rendered images, not landmark datasets)

### Retention and deletion

- Transient landmarks exist only while processing and are discarded afterward.
- Persisted face boxes and beauty parameters remain **only while you keep the related photo project**.
- **Delete** a project, **reset** edits, or **uninstall** the app to remove associated face metadata and local photos.

### Third parties

None. All face analysis and rendering use on-device Apple Vision and Core Image.

## Data Stored on Your Device

| Data | Where | Purpose |
|------|-------|---------|
| Photo projects | App Documents | Originals, thumbs, edit state |
| Face beauty edit metadata | Project edit state (sandbox) | Normalized face box + beauty params only |
| Preferences | App Group UserDefaults | Language, theme, capture/export options |
| Widget snapshots | App Group | Recent projects / stats for widgets |
| Capture beauty recipe | App Group (optional remember) | Strength and beauty parameters |
| iCloud preferences | Your private iCloud KVS | Optional preference sync |

## iCloud Sync

Optional sync uses Apple's `NSUbiquitousKeyValueStore` for lightweight preferences (appearance, language, export defaults, capture beauty settings, and similar). **Photo files and face landmarks are not synced.** Sync can be turned off in Settings.

## Permissions

| Permission | Purpose |
|------------|---------|
| Camera | Capture tab |
| Photo Library (read) | Import |
| Photo Library (add only) | Optional export to Photos |
| Microphone | Optional audio when recording video with sound; photo capture does not require it |

## In-App Purchases

Optional **Tip Developer** is a consumable StoreKit purchase. It does not unlock features and does not require a separate app account.

## Children's Privacy

iPhoto does not knowingly collect personal data from children. Core processing stays on-device with no iHTC Studio data-collection backend.

## Disclaimer

iPhoto is **not affiliated with Apple Inc.**

## Changes

We may update this policy on this page. Please review it periodically.

## Contact

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>

<section lang="zh-CN" markdown="1">

iHTC Studio（「我们」）为 iPhoto（亦称「爱修图」/「愛修圖」）提供本隐私政策说明。

## 概要

**爱修图无需账号，也不会把你的照片上传到 iHTC Studio 服务器。** 拍摄、美颜、滤镜与导出都在本机完成。可选 **iCloud 同步**仅同步偏好——不同步照片文件。

## 数据收集

我们不运营用于收集个人信息的后端：

- **无账号** — 无需注册、邮箱或手机号。
- **无分析与广告** — 未集成第三方分析、广告或追踪 SDK。
- **不上传照片进行分析** — 人脸关键点与渲染均留在本机。

## 应用如何工作

- **存储** — 项目（原图 / 缩略图 / 编辑状态）保存在 App 沙盒。小组件缩略图使用 App Group。
- **人脸美颜** — 详见下文 **「人脸数据与设备端美颜处理」**。
- **相册** — 仅访问你选择导入的照片，以及你主动发起的可选导出保存。
- **清除元数据** — 可按你的选择去除导出文件中的 EXIF / 定位 / 设备信息。

## 人脸数据与设备端美颜处理

当你使用美颜功能（拍摄实时预览、快门烘焙或编辑器美颜工具）时，爱修图**仅在本机**使用 Apple Vision 框架（`VNDetectFaceLandmarksRequest`）分析人脸。这**不是**人脸识别、身份比对、生物特征注册或身份验证。

### 处理哪些人脸数据

- **临时关键点（仅内存）：** 人脸框、轮廓、眼、眉、内外唇、瞳孔及相关几何，用于生成可选美颜蒙版（磨皮、美白、瘦脸、大眼、美牙、腮红、唇彩）。
- **随项目可选持久化：** **归一化人脸矩形框** 以及你选择的 **美颜强度 / 颜色参数**，以便再次打开项目时恢复按脸设置。**完整关键点坐标不会写入磁盘。**

### 用途

人脸几何**仅**用于在拍摄预览、成片、编辑预览、缩略图与导出/分享时施加**你开启**的美颜效果；不用于广告、画像或身份识别。

### 共享

**人脸数据不会与任何第三方共享**，不会上传到 iHTC Studio 服务器或任何云端分析 API。可选 iCloud 键值同步**仅同步偏好**（如语言、主题、拍摄美颜配方开关），**不同步照片或人脸关键点**。

### 存储位置

- 照片与项目编辑文件：**本机 App 沙盒**
- 临时关键点：**仅内存**（离开编辑器 / 清除分析缓存后丢弃）
- 小组件缩略图：本机 App Group（渲染后的图像，非关键点数据集）

### 保留与删除

- 临时关键点仅在处理期间存在，随后丢弃。
- 持久化的人脸框与美颜参数**仅在你保留对应照片项目期间**存在。
- **删除**项目、**还原**编辑或**卸载**应用，即可移除相关人脸元数据与本地照片。

### 第三方

无。全部人脸分析与渲染均使用设备端 Apple Vision 与 Core Image。

## 本机保存的数据

| 数据 | 位置 | 用途 |
|------|------|------|
| 照片项目 | App Documents | 原图、缩略图、编辑状态 |
| 人脸美颜编辑元数据 | 项目编辑状态（沙盒） | 仅归一化人脸框 + 美颜参数 |
| 偏好设置 | App Group UserDefaults | 语言、主题、拍摄/导出选项 |
| 小组件快照 | App Group | 最近项目 / 统计 |
| 拍摄美颜配方 | App Group（可选记住） | 强度与美颜参数 |
| iCloud 偏好 | 你的私人 iCloud KVS | 可选偏好同步 |

## iCloud 同步

可选同步通过 Apple 的键值存储同步轻量偏好（外观、语言、导出默认、拍摄美颜等）。**不同步照片文件与人脸关键点。** 可在设置中关闭。

## 权限

| 权限 | 用途 |
|------|------|
| 相机 | 拍摄页 |
| 相册（读取） | 导入 |
| 相册（仅添加） | 可选导出到系统相册 |
| 麦克风 | 录制有声视频时可选；拍摄照片不需要 |

## 内购

可选「打赏开发者」为消耗型 StoreKit 购买，**不解锁功能**，也不需要单独的应用账号。

## 儿童隐私

爱修图不会故意收集儿童的个人数据。核心处理在本机完成，且无 iHTC Studio 数据收集后端。

## 声明

爱修图**与 Apple Inc. 无关联**。

## 变更

我们可能更新本页面政策，请定期查阅。

## 联系

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>

<section lang="zh-TW" markdown="1">

愛火腿腸工作室（iHTC Studio）（「我們」；原 iHTCTeam）為 iPhoto（亦稱「愛修圖」）提供本隱私政策說明。

## 概要

**愛修圖無需帳號，也不會把你的照片上傳到 iHTC Studio 伺服器。** 拍攝、美顏、濾鏡與匯出都在本機完成。可選 **iCloud 同步**僅同步偏好——不同步照片檔案。

## 資料收集

我們不營運用於收集個人資訊的後端：

- **無帳號** — 無需註冊、信箱或手機號碼。
- **無分析與廣告** — 未整合第三方分析、廣告或追蹤 SDK。
- **不上傳照片進行分析** — 人臉關鍵點與渲染均留在本機。

## 應用如何運作

- **儲存** — 項目（原圖 / 縮圖 / 編輯狀態）保存在 App 沙盒。小工具縮圖使用 App Group。
- **人臉美顏** — 詳見下文 **「人臉資料與裝置端美顏處理」**。
- **相簿** — 僅存取你選擇匯入的照片，以及你主動發起的可選匯出儲存。
- **清除中繼資料** — 可依你的選擇去除匯出檔案中的 EXIF / 定位 / 裝置資訊。

## 人臉資料與裝置端美顏處理

當你使用美顏功能（拍攝即時預覽、快門烘焙或編輯器美顏工具）時，愛修圖**僅在本機**使用 Apple Vision 框架（`VNDetectFaceLandmarksRequest`）分析人臉。這**不是**人臉辨識、身分比對、生物特徵註冊或身分驗證。

### 處理哪些人臉資料

- **臨時關鍵點（僅記憶體）：** 人臉框、輪廓、眼、眉、內外唇、瞳孔及相關幾何，用於產生可選美顏遮罩（磨皮、美白、瘦臉、大眼、美牙、腮紅、唇彩）。
- **隨項目可選持久化：** **正規化人臉矩形框** 以及你選擇的 **美顏強度 / 顏色參數**，以便再次開啟項目時還原按臉設定。**完整關鍵點座標不會寫入磁碟。**

### 用途

人臉幾何**僅**用於在拍攝預覽、成片、編輯預覽、縮圖與匯出/分享時施加**你開啟**的美顏效果；不用於廣告、畫像或身分識別。

### 共享

**人臉資料不會與任何第三方共享**，不會上傳到 iHTC Studio 伺服器或任何雲端分析 API。可選 iCloud 鍵值同步**僅同步偏好**（如語言、主題、拍攝美顏配方開關），**不同步照片或人臉關鍵點**。

### 儲存位置

- 照片與項目編輯檔案：**本機 App 沙盒**
- 臨時關鍵點：**僅記憶體**（離開編輯器 / 清除分析快取後丟棄）
- 小工具縮圖：本機 App Group（渲染後的影像，非關鍵點資料集）

### 保留與刪除

- 臨時關鍵點僅在處理期間存在，隨後丟棄。
- 持久化的人臉框與美顏參數**僅在你保留對應照片項目期間**存在。
- **刪除**項目、**還原**編輯或**解除安裝**應用，即可移除相關人臉中繼資料與本機照片。

### 第三方

無。全部人臉分析與渲染均使用裝置端 Apple Vision 與 Core Image。

## 本機儲存的資料

| 資料 | 位置 | 用途 |
|------|------|------|
| 照片項目 | App Documents | 原圖、縮圖、編輯狀態 |
| 人臉美顏編輯中繼資料 | 項目編輯狀態（沙盒） | 僅正規化人臉框 + 美顏參數 |
| 偏好設定 | App Group UserDefaults | 語言、主題、拍攝/匯出選項 |
| 小工具快照 | App Group | 最近項目 / 統計 |
| 拍攝美顏配方 | App Group（可選記住） | 強度與美顏參數 |
| iCloud 偏好 | 你的私人 iCloud KVS | 可選偏好同步 |

## iCloud 同步

可選同步透過 Apple 的鍵值儲存同步輕量偏好（外觀、語言、匯出預設、拍攝美顏等）。**不同步照片檔案與人臉關鍵點。** 可在設定中關閉。

## 權限

| 權限 | 用途 |
|------|------|
| 相機 | 拍攝頁 |
| 相簿（讀取） | 匯入 |
| 相簿（僅加入） | 可選匯出到系統相簿 |
| 麥克風 | 錄製有聲影片時可選；拍攝照片不需要 |

## 內購

可選「打賞開發者」為消耗型 StoreKit 購買，**不解鎖功能**，也不需要單獨的應用帳號。

## 兒童隱私

愛修圖不會故意收集兒童的個人資料。核心處理在本機完成，且無 iHTC Studio 資料收集後端。

## 聲明

愛修圖**與 Apple Inc. 無關聯**。

## 變更

我們可能更新本頁政策，請定期查閱。

## 聯絡

- **信箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
