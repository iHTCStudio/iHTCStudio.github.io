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

iHTC Studio ("we", "us" or "our") built iPhoto (also known as "爱修图" / "愛修圖"). This page describes our policies regarding data when you use the app.

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

愛火腿腸工作室（iHTC Studio）（「我們」）為 iPhoto（亦稱「愛修圖」）提供本隱私政策說明。

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
<section lang="ja" markdown="1">

iHTC Studio (「私たち」、「私たち」、または「私たちの」) は、iPhoto (「愛修图」 / 「愛修圖」としても知られています) を構築しました。このページでは、アプリ使用時のデータに関するポリシーについて説明します。

## 概要

**iPhoto にはアカウントは必要なく、写真を iHTC Studio サーバーにアップロードすることもありません。** キャプチャ、美容、フィルター、エクスポートはデバイス上で実行されます。オプションの **iCloud 同期** は設定のみを対象とし、写真ファイルは対象としません。

## データ収集

当社は、お客様の個人情報を収集するバックエンドを運営しません。

- **アカウントなし** — 登録、電子メール、電話番号は必要ありません。
- **分析や広告なし** — サードパーティの分析、広告、または追跡 SDK はありません。
- **分析用の写真のアップロードはありません** — 顔のランドマークとレンダリングはデバイス上に残ります。

## アプリの仕組み

- **ストレージ** — プロジェクト (オリジナル/サムネイル/編集状態) はアプリのサンドボックス内に存在します。ウィジェットのサムネイルは、アプリ グループ コンテナを使用します。
- **顔の美しさ** — 以下の **顔データとデバイス上の美しさの処理**を参照してください。
- **フォト ライブラリ** — アクセスは、選択したインポートと、開始したオプションのエクスポート保存に制限されます。
- **メタデータ ストリップ** — 必要に応じて、作成したエクスポートから EXIF / GPS / デバイス フィールドを削除します。

## 顔データとデバイス上の美容処理

When you use beauty features (Capture live preview, shutter bake, or the editor Beauty tool), iPhoto analyzes faces **only on your device** using Apple’s Vision framework (`VNDetectFaceLandmarksRequest`). This is **not** face recognition, identity matching, biometrics enrollment, or authentication.

### どのような顔データが処理されるか

- **一時的なランドマーク (メモリのみ):** 顔の境界ボックス、顔の輪郭、目、眉毛、外側/内側の唇、瞳孔、およびオプションの化粧編集 (滑らか、美白、スリム、目、歯、頬紅、口紅) 用のマスクを構築するために使用される関連ジオメトリ。
- **プロジェクトとともに保存 (オプション):** **正規化された顔の境界四角形**と選択した**美しさの強さ/色のパラメータ** (`FaceBeautyEdit`)。これにより、プロジェクトを再度開いたときに顔ごとの設定を復元できます。 **完全なランドマーク座標はディスクに書き込まれません。**

### 使用する

Face geometry is used solely to apply the beauty adjustments **you** enable during capture preview, photo capture, editor preview, thumbnail refresh, and export/share. It is not used for advertising, profiling, or identification.

### 共有

**顔データは第三者と共有されることはありません。** iHTC Studio サーバーやクラウド分析 API にアップロードされることはありません。オプションの iCloud Key-Value 同期では、**環境設定のみ** (言語、テーマ、キャプチャービューティレシピの切り替えなど) が対象となり、**写真や顔のランドマークは同期されません**。

### 保管場所

- 写真とプロジェクト編集ファイル: **デバイス上のアプリ サンドボックス**
- 一時的なランドマーク: **RAM のみ** (エディターを終了するとクリア / 分析キャッシュをクリア)
- ウィジェットのサムネイル: デバイス上のアプリ グループ (ランドマーク データセットではなく、レンダリングされたイメージ)

### 保存と削除

- 一時的なランドマークは処理中にのみ存在し、その後は破棄されます。
- Persisted face boxes and beauty parameters remain **only while you keep the related photo project**.
- プロジェクトを**削除**するか、編集を**リセット**するか、アプリを**アンインストール**して関連する顔のメタデータとローカル写真を削除します。

### 第三者

なし。すべての顔の分析とレンダリングには、デバイス上の Apple Vision と Core Image が使用されます。

## デバイスに保存されているデータ

| データ | どこで | 目的 |
|------|-------|---------|
| 写真プロジェクト | アプリのドキュメント | オリジナル、サム、編集状態 |
| 顔の美しさの編集メタデータ | プロジェクト編集状態（サンドボックス） | 正規化されたフェイスボックス + 美容パラメータのみ |
| 設定 | アプリグループのUserDefaults | 言語、テーマ、キャプチャ/エクスポートのオプション |
| ウィジェットのスナップショット | アプリグループ | 最近のプロジェクト/ウィジェットの統計 |
| 美容レシピをキャプチャー | アプリグループ (オプションで記憶) | 強さと美しさのパラメータ |
| iCloudの設定 | あなたのプライベート iCloud KVS | オプションの設定同期 |

## iCloud同期

Optional sync uses Apple's `NSUbiquitousKeyValueStore` for lightweight preferences (appearance, language, export defaults, capture beauty settings, and similar). **Photo files and face landmarks are not synced.** Sync can be turned off in Settings.

## 権限

| 許可 | 目的 |
|------------|---------|
| カメラ | 「キャプチャ」タブ |
| フォトライブラリー（閲覧） | インポート |
| フォトライブラリ（追加のみ） | オプションで写真にエクスポート |
| マイク | 音声付きビデオを録画する場合のオプションの音声。写真のキャプチャには必要ありません |

## アプリ内購入

オプションの **Tip Developer** は消耗品の StoreKit の購入です。機能のロックが解除されることはなく、別のアプリ アカウントは必要ありません。

## 子供のプライバシー

iPhoto は、故意に子供から個人データを収集しません。コア処理はデバイス上に留まり、iHTC Studio データ収集バックエンドはありません。

## 免責事項

iPhoto は **Apple Inc. とは提携していません**

## 変更点

このページでこのポリシーを更新する場合があります。定期的に見直してください。

## お問い合わせ

- **電子メール:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ko" markdown="1">

iHTC Studio("당사", "당사" 또는 "당사")는 iPhoto("爱修图" / "愛修圖"라고도 함)를 구축했습니다. 이 페이지에서는 앱 사용 시 데이터에 관한 정책을 설명합니다.

## 요약

**iPhoto는 계정이 필요하지 않으며 iHTC Studio 서버에 사진을 업로드하지 않습니다.** 캡처, 뷰티, 필터 및 내보내기는 귀하의 장치에서 실행됩니다. 옵션 **iCloud 동기화**에는 환경설정만 적용되며 사진 파일에는 적용되지 않습니다.

## 데이터 수집

당사는 귀하의 개인정보를 수집하는 백엔드를 운영하지 않습니다.

- **계정 없음** — 등록, 이메일 또는 전화번호가 필요하지 않습니다.
- **분석 또는 광고 없음** — 타사 분석, 광고 또는 추적 SDK가 없습니다.
- **분석을 위한 사진 업로드 없음** — 얼굴 랜드마크와 렌더링이 기기에 유지됩니다.

## 앱 작동 방식

- **저장소** — 프로젝트(원본/썸네일/편집 상태)가 앱 샌드박스에 저장됩니다. 위젯 축소판은 앱 그룹 컨테이너를 사용합니다.
- **얼굴 미용** — 아래 **얼굴 데이터 및 기기 내 미용 처리**를 참조하세요.
- **사진 라이브러리** — 액세스는 선택한 가져오기로 제한되며 선택적으로 내보내기를 통해 저장을 시작할 수 있습니다.
- **메타데이터 스트립** — 생성한 내보내기에서 EXIF/GPS/장치 필드를 선택적으로 제거합니다.

## 얼굴 데이터 및 기기 내 미용 처리

뷰티 기능(실시간 미리보기 캡처, 셔터 베이크 또는 편집기 뷰티 도구)을 사용하면 iPhoto는 Apple의 Vision 프레임워크(`VNDetectFaceLandmarksRequest`)를 사용하여 **기기에서만** 얼굴을 분석합니다. 이는 얼굴 인식, 신원 대조, 생체 인식 등록 또는 인증이 **아닙니다**.

### 어떤 얼굴 데이터가 처리되나요?

- **일시적 랜드마크(메모리만 해당):** 얼굴 경계 상자, 얼굴 윤곽선, 눈, 눈썹, 외부/내부 입술, 동공 및 선택적 미용 편집(매끄러움, 미백, 슬림, 눈, 치아, 블러셔, 립스틱)을 위한 마스크를 만드는 데 사용되는 관련 형상입니다.
- **프로젝트와 함께 지속됨(선택 사항):** **정규화된 얼굴 경계 직사각형**과 선택한 **미용 강도/색상 매개변수**(`FaceBeautyEdit`)를 추가하여 프로젝트를 다시 열 때 얼굴별 설정을 복원할 수 있습니다. **전체 랜드마크 좌표는 디스크에 기록되지 않습니다.**

### 사용

얼굴 형상은 캡처 미리 보기, 사진 캡처, 편집기 미리 보기, 썸네일 새로 고침 및 내보내기/공유 중에 **사용자**가 활성화하는 미용 조정을 적용하는 데에만 사용됩니다. 광고, 프로파일링 또는 식별을 위해 사용되지 않습니다.

### 공유

**얼굴 데이터는 제3자와 절대 공유되지 않습니다.** iHTC Studio 서버나 클라우드 분석 API에 업로드되지 않습니다. 선택적인 iCloud 키-값 동기화는 **기본 설정**(예: 언어, 테마, 뷰티 레시피 토글 캡처)에만 적용되며 **사진이나 얼굴 랜드마크는 동기화하지 않습니다**.

### 저장 위치

- 사진 및 프로젝트 편집 파일: **기기의 앱 샌드박스**
- 일시적 랜드마크: **RAM만**(편집기를 종료하면 지워짐/분석 캐시 지우기)
- 위젯 썸네일: 기기의 앱 그룹(랜드마크 데이터세트가 아닌 렌더링된 이미지)

### 보유 및 삭제

- 일시적 랜드마크는 처리 중에만 존재하며 이후에는 삭제됩니다.
- 지속되는 얼굴 상자와 뷰티 매개변수는 **관련 사진 프로젝트를 유지하는 동안에만** 유지됩니다.
- 프로젝트 **삭제**, 편집 내용 **재설정** 또는 앱 **제거**를 통해 관련 얼굴 메타데이터 및 로컬 사진을 제거할 수 있습니다.

### 제3자

없음. 모든 얼굴 분석 및 렌더링은 기기 내 Apple Vision 및 Core Image를 사용합니다.

## 귀하의 장치에 저장된 데이터

| 데이터 | 어디에 | 목적 |
|------|-------|---------|
| 사진 프로젝트 | 앱 문서 | 원본, 썸, 편집 상태 |
| 얼굴 미용 편집 메타데이터 | 프로젝트 편집 상태(샌드박스) | 정규화된 페이스 박스 + 뷰티 매개변수만 해당 |
| 환경설정 | 앱 그룹 사용자 기본값 | 언어, 테마, 캡처/내보내기 옵션 |
| 위젯 스냅샷 | 앱 그룹 | 최근 프로젝트/위젯 통계 |
| 뷰티 레시피 캡처 | 앱 그룹(선택 사항 기억) | 힘과 아름다움의 매개변수 |
| iCloud 환경설정 | 귀하의 개인 iCloud KVS | 선택적 환경설정 동기화 |

## 아이클라우드 동기화

Optional sync uses Apple's `NSUbiquitousKeyValueStore` for lightweight preferences (appearance, language, export defaults, capture beauty settings, and similar). **Photo files and face landmarks are not synced.** Sync can be turned off in Settings.

## 권한

| 허가 | 목적 |
|------------|---------|
| 카메라 | 캡처 탭 |
| 사진 라이브러리(읽기) | 가져오기 |
| 사진 라이브러리(추가 전용) | 사진으로 선택적으로 내보내기 |
| 마이크 | 사운드가 포함된 비디오를 녹화할 때 오디오는 선택 사항입니다. 사진 캡처에는 필요하지 않습니다 |

## 인앱 구매

선택 사항인 **Tip Developer**는 소모성 StoreKit 구매입니다. 기능을 잠금 해제하지 않으며 별도의 앱 계정이 필요하지 않습니다.

## 아동의 개인정보 보호

iPhoto는 의도적으로 어린이로부터 개인 데이터를 수집하지 않습니다. iHTC Studio 데이터 수집 백엔드 없이 핵심 처리가 기기 내에서 유지됩니다.

## 면책조항

iPhoto는 **Apple Inc.와 제휴 관계가 아닙니다**

## 변경 사항

당사는 이 페이지에서 이 정책을 업데이트할 수 있습니다. 정기적으로 검토하시기 바랍니다.

## 연락처

- **이메일:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ru" markdown="1">

iHTC Studio («мы», «нас» или «наш») создала iPhoto (также известный как «爱修图» / «愛修圖»). На этой странице описана наша политика в отношении данных при использовании приложения.

## Резюме

**iPhoto не требует учетной записи и не загружает ваши фотографии на серверы iHTC Studio.** Съёмка, настройка красоты, фильтры и экспорт выполняются на вашем устройстве. Дополнительная **синхронизация с iCloud** охватывает только настройки, но не файлы фотографий.

## Сбор данных

Мы не используем серверную часть, которая собирает вашу личную информацию:

- **Нет учетной записи** — регистрация, адрес электронной почты или номер телефона не требуются.
- **Никакой аналитики и рекламы**. Никакой сторонней аналитики, рекламы или SDK для отслеживания.
- **Фотографии для анализа не загружаются** — Ориентиры на лицах и рендеринг остаются на устройстве.

## Как работает приложение

- **Хранилище** — проекты (исходный вариант/миниатюра/состояние редактирования) хранятся в изолированной программной среде приложения. Миниатюры виджетов используют контейнер группы приложений.
- **Красота лица** — см. раздел **Данные о лице и обработка красоты на устройстве** ниже.
- **Библиотека фотографий** — доступ ограничен только выбранными вами импортированными файлами, а экспорт можно сохранить при необходимости.
- **Полоса метаданных** — при необходимости удаляет поля EXIF/GPS/устройство из созданного вами экспорта.

## Данные о лицах и обработка данных о красоте на устройстве

When you use beauty features (Capture live preview, shutter bake, or the editor Beauty tool), iPhoto analyzes faces **only on your device** using Apple’s Vision framework (`VNDetectFaceLandmarksRequest`). This is **not** face recognition, identity matching, biometrics enrollment, or authentication.

### Какие данные о лицах обрабатываются

- **Переходные ориентиры (только память):** ограничивающая рамка лица, контур лица, глаза, брови, внешние/внутренние губы, зрачки и соответствующая геометрия, используемая для создания масок для дополнительных косметических изменений (сглаживание, отбеливание, стройность, глаза, зубы, румянец, помада).
- **Сохраняется в проекте (необязательно):** **нормализованный прямоугольник, ограничивающий лицо**, плюс выбранные вами **параметры красоты/цвета** (`FaceBeautyEdit`), поэтому настройки для каждого лица можно восстановить при повторном открытии проекта. **Полные координаты ориентира не записываются на диск.**

### Использование

Геометрия лица используется исключительно для применения настроек красоты, которые **вы** включаете во время предварительного просмотра, захвата фотографий, предварительного просмотра в редакторе, обновления миниатюр, а также экспорта и публикации. Он не используется для рекламы, профилирования или идентификации.

### Совместное использование

**Данные о лицах никогда не передаются третьим лицам.** Они не загружаются на серверы iHTC Studio или в какой-либо API облачного анализа. Дополнительная синхронизация ключей и значений iCloud охватывает **только настройки** (например, язык, тему, переключатели рецептов красоты) и **не синхронизирует фотографии или ориентиры на лицах**.

### Место хранения

- Фотографии и файлы редактирования проекта: **песочница приложения на вашем устройстве**
- Временные ориентиры: **Только ОЗУ** (очищается при выходе из редактора/очистке кэша анализа)
- Миниатюры виджетов: группа приложений на вашем устройстве (рендеринговые изображения, а не наборы данных ориентиров).

### Хранение и удаление

- Временные ориентиры существуют только во время обработки и впоследствии отбрасываются.
- Сохраненные рамки лица и параметры красоты сохраняются **только пока вы сохраняете соответствующий фотопроект**.
- **Удалите** проект, **сбросьте** изменения или **удалите** приложение, чтобы удалить связанные метаданные лица и локальные фотографии.

### Третьи стороны

Нет. Для анализа и рендеринга лиц используются встроенные в устройство Apple Vision и Core Image.

## Данные, хранящиеся на вашем устройстве

| Данные | Где | Цель |
|------|-------|---------|
| Фотопроекты | Документы приложения | Оригиналы, превью, состояние редактирования |
| Красота лица: изменить метаданные | Статус редактирования проекта (песочница) | Нормализованное окно лица + только параметры красоты |
| Предпочтения | Пользовательские настройки группы приложений | Язык, тема, параметры захвата/экспорта |
| Снимки виджетов | Группа приложений | Последние проекты/статистика виджетов |
| Захватите рецепт красоты | Группа приложений (необязательно, помните) | Параметры прочности и красоты |
| настройки iCloud | Ваш личный iCloud KVS | Дополнительная синхронизация предпочтений |

## Синхронизация с iCloud

Optional sync uses Apple's `NSUbiquitousKeyValueStore` for lightweight preferences (appearance, language, export defaults, capture beauty settings, and similar). **Photo files and face landmarks are not synced.** Sync can be turned off in Settings.

## Разрешения

| Разрешение | Цель |
|------------|---------|
| Камера | Вкладка «Захват» |
| Фототека (читать) | Импорт |
| Библиотека фотографий (только добавление) | Дополнительный экспорт в фотографии |
| Микрофон | Дополнительный звук при записи видео со звуком; фотосъемка этого не требует |

## Покупки в приложении

Дополнительный **Tip Developer** — это расходный материал, приобретаемый StoreKit. Он не разблокирует функции и не требует отдельной учетной записи приложения.

## Конфиденциальность детей

iPhoto сознательно не собирает персональные данные детей. Основная обработка данных остается на устройстве без использования серверной части сбора данных iHTC Studio.

## Отказ от ответственности

iPhoto **не связан с Apple Inc.**

## Изменения

Мы можем обновить эту политику на этой странице. Пожалуйста, просматривайте его периодически.

## Контакт

- **Электронная почта:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="th" markdown="1">

iHTC Studio ("เรา", "พวกเรา" หรือ "ของเรา") ได้สร้าง iPhoto (หรือที่รู้จักในชื่อ "爱修上" / "愛修圖") หน้านี้อธิบายนโยบายของเราเกี่ยวกับข้อมูลเมื่อคุณใช้แอป

## สรุป

**iPhoto ไม่จำเป็นต้องมีบัญชีและไม่ได้อัปโหลดรูปภาพของคุณไปยังเซิร์ฟเวอร์ iHTC Studio** การจับภาพ ความสวยงาม ฟิลเตอร์ และการส่งออกบนอุปกรณ์ของคุณ ตัวเลือก **การซิงค์ iCloud** จะครอบคลุมเฉพาะการตั้งค่าเท่านั้น ไม่รวมถึงไฟล์รูปภาพ

## การรวบรวมข้อมูล

เราไม่ได้ดำเนินการแบ็กเอนด์ที่รวบรวมข้อมูลส่วนบุคคลของคุณ:

- **ไม่มีบัญชี** — ไม่ต้องลงทะเบียน อีเมล หรือหมายเลขโทรศัพท์
- **ไม่มีการวิเคราะห์หรือโฆษณา** — ไม่มีการวิเคราะห์ การโฆษณา หรือการติดตาม SDK ของบุคคลที่สาม
- **ไม่มีการอัปโหลดรูปภาพเพื่อการวิเคราะห์** — จุดสังเกตของใบหน้าและการเรนเดอร์จะยังคงอยู่ในอุปกรณ์

## แอปทำงานอย่างไร

- **พื้นที่เก็บข้อมูล** — โปรเจ็กต์ (ต้นฉบับ / ภาพย่อ / สถานะแก้ไข) อยู่ในแซนด์บ็อกซ์ของแอป ภาพขนาดย่อของวิดเจ็ตใช้คอนเทนเนอร์กลุ่มแอป
- **ความงามของใบหน้า** — ดู **ข้อมูลใบหน้าและการประมวลผลความงามบนอุปกรณ์** ด้านล่าง
- **คลังรูปภาพ** — การเข้าถึงจะจำกัดเฉพาะการนำเข้าที่คุณเลือก และการส่งออกที่เป็นตัวเลือกจะช่วยให้คุณเริ่มต้นได้
- **แถบข้อมูลเมตา** — เลือกที่จะลบช่อง EXIF ​​/ GPS / อุปกรณ์ออกจากการส่งออกที่คุณสร้าง

## ข้อมูลใบหน้าและการประมวลผลความงามบนอุปกรณ์

When you use beauty features (Capture live preview, shutter bake, or the editor Beauty tool), iPhoto analyzes faces **only on your device** using Apple’s Vision framework (`VNDetectFaceLandmarksRequest`). This is **not** face recognition, identity matching, biometrics enrollment, or authentication.

### ข้อมูลใบหน้าใดที่ได้รับการประมวลผล

- **จุดสังเกตชั่วคราว (หน่วยความจำเท่านั้น):** กรอบขอบเขตใบหน้า โครงร่างใบหน้า ดวงตา คิ้ว ริมฝีปากด้านนอก/ด้านใน รูม่านตา และรูปทรงที่เกี่ยวข้องที่ใช้ในการสร้างมาสก์สำหรับการแก้ไขเสริมความงามเพิ่มเติม (เรียบเนียน ขาวขึ้น ผอมเพรียว ตา ฟัน บลัชออน ลิปสติก)
- **คงอยู่ในโปรเจ็กต์ (ไม่บังคับ):** **สี่เหลี่ยมขอบใบหน้าที่ทำให้เป็นมาตรฐาน** บวกกับ **ความเข้มของความงาม/พารามิเตอร์สี** ที่คุณเลือก (`FaceBeautyEdit`) ดังนั้นจึงสามารถกู้คืนการตั้งค่าต่อใบหน้าได้เมื่อคุณเปิดโปรเจ็กต์อีกครั้ง **พิกัดจุดสังเกตแบบเต็มไม่ได้เขียนลงดิสก์**

### ใช้

เรขาคณิตของใบหน้าใช้เฉพาะเพื่อใช้การปรับความงาม **คุณ** เปิดใช้งานระหว่างการแสดงตัวอย่างการจับภาพ การจับภาพ การแสดงตัวอย่างจากโปรแกรมแก้ไข การรีเฟรชภาพขนาดย่อ และการส่งออก/แชร์ ไม่ได้ใช้สำหรับการโฆษณา การทำโปรไฟล์ หรือการระบุตัวตน

### การแบ่งปัน

**ข้อมูลใบหน้าจะไม่ถูกแชร์กับบุคคลที่สาม** จะไม่มีการอัพโหลดไปยังเซิร์ฟเวอร์ iHTC Studio หรือ API การวิเคราะห์ระบบคลาวด์ใดๆ การซิงค์คีย์-ค่า iCloud ที่เป็นตัวเลือกครอบคลุม **การตั้งค่าเท่านั้น** (เช่น การสลับภาษา ธีม การจับภาพสูตรความงาม) และ **ไม่ซิงค์รูปภาพหรือจุดสังเกตใบหน้า**

### สถานที่จัดเก็บ

- รูปภาพและไฟล์แก้ไขโครงการ: **แซนด์บ็อกซ์ของแอปบนอุปกรณ์ของคุณ**
- จุดสังเกตชั่วคราว: **RAM เท่านั้น** (ล้างเมื่อคุณออกจากตัวแก้ไข / ล้างแคชการวิเคราะห์)
- ภาพขนาดย่อของวิดเจ็ต: กลุ่มแอปบนอุปกรณ์ของคุณ (ภาพที่แสดงผล ไม่ใช่ชุดข้อมูลจุดสังเกต)

### การเก็บรักษาและการลบ

- จุดสังเกตชั่วคราวจะเกิดขึ้นขณะประมวลผลเท่านั้น และจะถูกละทิ้งในภายหลัง
- กล่องใบหน้าและพารามิเตอร์ความงามยังคงอยู่ **เฉพาะในขณะที่คุณเก็บโปรเจ็กต์ภาพถ่ายที่เกี่ยวข้องเท่านั้น**
- **ลบ** โปรเจ็กต์ **รีเซ็ต** การแก้ไข หรือ **ถอนการติดตั้ง** แอปเพื่อลบข้อมูลเมตาของใบหน้าและรูปภาพในเครื่องที่เกี่ยวข้อง

### บุคคลที่สาม

ไม่มี. การวิเคราะห์และการเรนเดอร์ใบหน้าทั้งหมดใช้ Apple Vision และ Core Image บนอุปกรณ์

## ข้อมูลที่จัดเก็บไว้ในอุปกรณ์ของคุณ

| ข้อมูล | ที่ไหน | วัตถุประสงค์ |
|------|-------|---------|
| โครงการภาพถ่าย | เอกสารแอพ | ต้นฉบับ นิ้วหัวแม่มือ สถานะการแก้ไข |
| ข้อมูลเมตาการแก้ไขความงามของใบหน้า | สถานะการแก้ไขโครงการ (แซนด์บ็อกซ์) | กล่องหน้าธรรมดา + พาราเสริมความงามเท่านั้น |
| การตั้งค่า | ค่าเริ่มต้นของกลุ่มแอป | ภาษา ธีม ตัวเลือกการบันทึก/ส่งออก |
| สแนปชอตวิดเจ็ต | กลุ่มแอพ | โครงการล่าสุด / สถิติสำหรับวิดเจ็ต |
| แคปสูตรความงาม | กลุ่มแอป (จำหรือไม่ก็ได้) | พารามิเตอร์ความแข็งแกร่งและความงาม |
| การตั้งค่า iCloud | iCloud KVS ส่วนตัวของคุณ | การซิงค์การตั้งค่าเพิ่มเติม |

## การซิงค์ iCloud

Optional sync uses Apple's `NSUbiquitousKeyValueStore` for lightweight preferences (appearance, language, export defaults, capture beauty settings, and similar). **Photo files and face landmarks are not synced.** Sync can be turned off in Settings.

## สิทธิ์

| การอนุญาต | วัตถุประสงค์ |
|------------|---------|
| กล้อง | แท็บจับภาพ |
| คลังภาพ (อ่าน) | นำเข้า |
| คลังภาพ (เพิ่มเท่านั้น) | ตัวเลือกการส่งออกไปยังรูปถ่าย |
| ไมโครโฟน | เสียงเสริมเมื่อบันทึกวิดีโอพร้อมเสียง ไม่จำเป็นต้องใช้การจับภาพ |

## การซื้อในแอป

ตัวเลือก **Tip Developer** คือการซื้อ StoreKit แบบสิ้นเปลือง มันไม่ได้ปลดล็อคคุณสมบัติและไม่ต้องใช้บัญชีแอพแยกต่างหาก

## ความเป็นส่วนตัวของเด็ก

iPhoto จะไม่เก็บรวบรวมข้อมูลส่วนบุคคลจากเด็กโดยเจตนา การประมวลผลหลักจะยังคงอยู่ในอุปกรณ์โดยไม่มีแบ็กเอนด์การรวบรวมข้อมูลของ iHTC Studio

## ข้อสงวนสิทธิ์

iPhoto **ไม่มีส่วนเกี่ยวข้องกับ Apple Inc.**

## การเปลี่ยนแปลง

เราอาจอัปเดตนโยบายนี้ในหน้านี้ โปรดตรวจสอบเป็นระยะๆ

## ติดต่อ

- **อีเมล:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="de" markdown="1">

iHTC Studio („wir“, „uns“ oder „unser“) hat iPhoto (auch bekannt als „爱修图“ / „愛修圖“) erstellt. Auf dieser Seite werden unsere Richtlinien in Bezug auf Daten beschrieben, wenn Sie die App nutzen.

## Zusammenfassung

**iPhoto erfordert kein Konto und lädt Ihre Fotos nicht auf iHTC Studio-Server hoch.** Aufnahme, Schönheit, Filter und Export laufen auf Ihrem Gerät. Die optionale **iCloud-Synchronisierung** deckt nur Einstellungen ab – niemals Fotodateien.

## Datenerfassung

Wir betreiben kein Backend, das Ihre persönlichen Daten sammelt:

- **Kein Konto** – Es ist keine Registrierung, E-Mail-Adresse oder Telefonnummer erforderlich.
- **Keine Analysen oder Werbung** – Keine Analysen, Werbung oder Tracking-SDKs von Drittanbietern.
- **Kein Foto-Upload zur Analyse** – Gesichtspunkte und Renderings bleiben auf dem Gerät.

## So funktioniert die App

- **Speicher** – Projekte (Original/Miniaturansicht/Bearbeitungsstatus) leben in der App-Sandbox. Widget-Miniaturansichten verwenden den App-Gruppencontainer.
- **Gesichtsschönheit** – Siehe unten **Gesichtsdaten und Schönheitsverarbeitung auf dem Gerät**.
- **Fotobibliothek** – Der Zugriff ist auf die von Ihnen ausgewählten Importe beschränkt und optionale Exportspeicherungen, die Sie starten.
- **Metadatenstreifen** – Entfernt optional EXIF-/GPS-/Gerätefelder aus den von Ihnen erstellten Exporten.

## Gesichtsdaten und Schönheitsverarbeitung auf dem Gerät

When you use beauty features (Capture live preview, shutter bake, or the editor Beauty tool), iPhoto analyzes faces **only on your device** using Apple’s Vision framework (`VNDetectFaceLandmarksRequest`). This is **not** face recognition, identity matching, biometrics enrollment, or authentication.

### Welche Gesichtsdaten werden verarbeitet?

- **Vorübergehende Orientierungspunkte (nur Speicher):** Gesichtsbegrenzungsrahmen, Gesichtskontur, Augen, Augenbrauen, äußere/innere Lippen, Pupillen und zugehörige Geometrie zum Erstellen von Masken für optionale kosmetische Bearbeitungen (glätten, aufhellen, schlank, Augen, Zähne, Rouge, Lippenstift).
- **Persisted with a project (optional):** a **normalized face bounding rectangle** plus your chosen **beauty strength / color parameters** (`FaceBeautyEdit`), so per-face settings can be restored when you reopen the project. **Full landmark coordinates are not written to disk.**

### Benutzen

Face geometry is used solely to apply the beauty adjustments **you** enable during capture preview, photo capture, editor preview, thumbnail refresh, and export/share. It is not used for advertising, profiling, or identification.

### Teilen

**Gesichtsdaten werden niemals an Dritte weitergegeben.** Sie werden nicht auf iHTC Studio-Server oder eine Cloud-Analyse-API hochgeladen. Die optionale iCloud-Schlüsselwertsynchronisierung deckt **nur Einstellungen** ab (z. B. Sprache, Thema, Umschalten zwischen Beauty-Rezepten) und **synchronisiert keine Fotos oder Gesichtspunkte**.

### Speicherort

- Fotos und Projektbearbeitungsdateien: **App-Sandbox auf Ihrem Gerät**
- Vorübergehende Orientierungspunkte: **Nur RAM** (wird gelöscht, wenn Sie den Editor verlassen / Analyse-Cache leeren)
- Widget-Miniaturansichten: App-Gruppe auf Ihrem Gerät (gerenderte Bilder, keine Orientierungsdatensätze)

### Aufbewahrung und Löschung

- Vorübergehende Orientierungspunkte sind nur während der Verarbeitung vorhanden und werden anschließend verworfen.
- Behaltene Gesichtsfelder und Schönheitsparameter bleiben **nur so lange erhalten, wie Sie das zugehörige Fotoprojekt behalten**.
- **Löschen** Sie ein Projekt, **setzen** Sie Änderungen zurück oder **deinstallieren** Sie die App, um zugehörige Gesichtsmetadaten und lokale Fotos zu entfernen.

### Dritte

Keine. Für alle Gesichtsanalysen und -darstellungen werden Apple Vision und Core Image auf dem Gerät verwendet.

## Auf Ihrem Gerät gespeicherte Daten

| Daten | Wo | Zweck |
|------|-------|---------|
| Fotoprojekte | App-Dokumente | Originale, Daumen, Bearbeitungsstand |
| Metadaten zur Gesichtsschönheit bearbeiten | Projektbearbeitungsstatus (Sandbox) | Nur normalisierte Gesichtsbox + Beauty-Parameter |
| Präferenzen | Benutzerstandards für App-Gruppen | Sprache, Thema, Aufnahme-/Exportoptionen |
| Widget-Schnappschüsse | App-Gruppe | Aktuelle Projekte/Statistiken für Widgets |
| Erfassen Sie das Schönheitsrezept | App-Gruppe (optional merken) | Kraft- und Schönheitsparameter |
| iCloud-Einstellungen | Ihr privates iCloud KVS | Optionale Präferenzsynchronisierung |

## iCloud-Synchronisierung

Optional sync uses Apple's `NSUbiquitousKeyValueStore` for lightweight preferences (appearance, language, export defaults, capture beauty settings, and similar). **Photo files and face landmarks are not synced.** Sync can be turned off in Settings.

## Berechtigungen

| Erlaubnis | Zweck |
|------------|---------|
| Kamera | Registerkarte „Erfassen“. |
| Fotobibliothek (lesen) | Importieren |
| Fotobibliothek (nur hinzufügen) | Optionaler Export in Fotos |
| Mikrofon | Optionaler Ton bei Videoaufnahme mit Ton; Für die Fotoaufnahme ist dies nicht erforderlich |

## In-App-Käufe

Der optionale **Tip Developer** ist ein verbrauchbarer StoreKit-Kauf. Es werden keine Funktionen freigeschaltet und es ist kein separates App-Konto erforderlich.

## Privatsphäre von Kindern

iPhoto erfasst wissentlich keine personenbezogenen Daten von Kindern. Die Kernverarbeitung bleibt auf dem Gerät, ohne iHTC Studio-Datenerfassungs-Backend.

## Haftungsausschluss

iPhoto ist **nicht mit Apple Inc. verbunden**

## Änderungen

Wir können diese Richtlinie auf dieser Seite aktualisieren. Bitte überprüfen Sie es regelmäßig.

## Kontakt

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="fr" markdown="1">

iHTC Studio (« nous », « notre » ou « notre ») a créé iPhoto (également connu sous le nom de « 爱修图 » / « 愛修圖 »). Cette page décrit nos politiques concernant les données lorsque vous utilisez l'application.

## Résumé

**iPhoto ne nécessite pas de compte et ne télécharge pas vos photos sur les serveurs iHTC Studio.** La capture, la beauté, les filtres et l'exportation s'exécutent sur votre appareil. La **synchronisation iCloud** facultative couvre uniquement les préférences, jamais les fichiers photo.

## Collecte de données

Nous n'exploitons pas de backend qui collecte vos informations personnelles :

- **Aucun compte** — Aucune inscription, e-mail ou numéro de téléphone n'est requis.
- **Aucune analyse ni publicité** — Aucune analyse, publicité ou SDK de suivi tiers.
- **Aucun téléchargement de photo pour analyse** — Les repères de visage et le rendu restent sur l'appareil.

## Comment fonctionne l'application

- **Stockage** — Les projets (original/vignette/état d'édition) se trouvent dans le bac à sable de l'application. Les miniatures des widgets utilisent le conteneur App Group.
- **Beauté du visage** — Voir **Données du visage et traitement de la beauté sur l'appareil** ci-dessous.
- **Bibliothèque de photos** : l'accès est limité aux importations que vous choisissez et aux sauvegardes d'exportation facultatives que vous démarrez.
- **Bande de métadonnées** — Supprime éventuellement les champs EXIF/GPS/appareil des exportations que vous créez.

## Données faciales et traitement de la beauté sur l'appareil

Lorsque vous utilisez les fonctionnalités de beauté (Capture d'aperçu en direct, Shutter Bake ou l'outil Beauté de l'éditeur), iPhoto analyse les visages **uniquement sur votre appareil** à l'aide du framework Vision d'Apple (`VNDetectFaceLandmarksRequest`). Il ne s'agit **pas** de reconnaissance faciale, de correspondance d'identité, d'enregistrement biométrique ou d'authentification.

### Quelles données de visage sont traitées

- **Repères transitoires (mémoire uniquement) :** cadre de délimitation du visage, contour du visage, yeux, sourcils, lèvres externes/intérieures, pupilles et géométrie associée utilisés pour créer des masques pour des modifications cosmétiques facultatives (lisser, blanchir, affiner, yeux, dents, fard à joues, rouge à lèvres).
- **Persistance avec un projet (facultatif) :** un **rectangle de délimitation de visage normalisé** plus les **paramètres de force de beauté/couleur** choisis (`FaceBeautyEdit`), afin que les paramètres par visage puissent être restaurés lorsque vous rouvrez le projet. **Les coordonnées complètes des points de repère ne sont pas écrites sur le disque.**

### Utiliser

La géométrie du visage est utilisée uniquement pour appliquer les réglages de beauté **que** activez lors de l'aperçu de la capture, de la capture de photos, de l'aperçu de l'éditeur, de l'actualisation des vignettes et de l'exportation/partage. Il n’est pas utilisé à des fins de publicité, de profilage ou d’identification.

### Partage

**Les données faciales ne sont jamais partagées avec des tiers.** Elles ne sont pas téléchargées sur les serveurs iHTC Studio ni sur aucune API d'analyse cloud. La synchronisation facultative iCloud Key-Value couvre **les préférences uniquement** (par exemple, la langue, le thème, les bascules de capture de recette de beauté) et **ne synchronise pas les photos ni les points de repère du visage**.

### Lieu de stockage

- Photos et fichiers de modification de projet : **bac à sable d'application sur votre appareil**
- Repères transitoires : **RAM uniquement** (effacés lorsque vous quittez l'éditeur / vider le cache d'analyse)
- Miniatures du widget : groupe d'applications sur votre appareil (images rendues, pas d'ensembles de données de points de repère)

### Conservation et suppression

- Les repères transitoires n'existent que pendant le traitement et sont ensuite supprimés.
- Les zones de visage et les paramètres de beauté persistants restent **uniquement tant que vous conservez le projet photo associé**.
- **Supprimez** un projet, **réinitialisez** les modifications ou **désinstallez** l'application pour supprimer les métadonnées de visage et les photos locales associées.

### Tiers

Aucun. Toutes les analyses et rendus de visage utilisent Apple Vision et Core Image sur l'appareil.

## Données stockées sur votre appareil

| Données | Où | Objectif |
|------|-------|---------|
| Projets photo | Documents de l'application | Originaux, pouces, état de modification |
| Métadonnées de modification de la beauté du visage | État d'édition du projet (bac à sable) | Coffret visage normalisé + paramètres beauté uniquement |
| Préférences | Paramètres par défaut du groupe d'applications | Options de langue, de thème, de capture/exportation |
| Instantanés de widgets | Groupe d'applications | Projets/statistiques récents pour les widgets |
| Capturer une recette de beauté | Groupe d'applications (facultatif, rappelez-vous) | Paramètres de force et de beauté |
| Préférences iCloud | Votre KVS iCloud privé | Synchronisation des préférences facultative |

## Synchronisation iCloud

Optional sync uses Apple's `NSUbiquitousKeyValueStore` for lightweight preferences (appearance, language, export defaults, capture beauty settings, and similar). **Photo files and face landmarks are not synced.** Sync can be turned off in Settings.

## Autorisations

| Autorisation | Objectif |
|------------|---------|
| Appareil photo | Onglet Capture |
| Photothèque (lire) | Importer |
| Photothèque (ajouter uniquement) | Exportation facultative vers Photos |
| Micro | Audio en option lors de l'enregistrement vidéo avec son ; la capture de photos ne l'exige pas |

## Achats intégrés

**Tip Developer** facultatif est un achat de consommable StoreKit. Il ne déverrouille pas les fonctionnalités et ne nécessite pas de compte d'application distinct.

## Confidentialité des enfants

iPhoto ne collecte pas sciemment de données personnelles auprès des enfants. Le traitement de base reste sur l'appareil sans backend de collecte de données iHTC Studio.

## Avis de non-responsabilité

iPhoto n'est **pas affilié à Apple Inc.**

## Changements

Nous pouvons mettre à jour cette politique sur cette page. Veuillez le consulter périodiquement.

## Contacter

- **E-mail :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="tr" markdown="1">

iHTC Studio ("biz", "bize" veya "bizim") iPhoto'yu ("爱修图" / "愛修圖" olarak da bilinir) oluşturdu. Bu sayfada, uygulamayı kullandığınızda elde edilen verilere ilişkin politikalarımız açıklanmaktadır.

## Özet

**iPhoto bir hesap gerektirmez ve fotoğraflarınızı iHTC Studio sunucularına yüklemez.** Fotoğraf çekme, güzellik, filtreler ve dışa aktarma işlemleri cihazınızda çalışır. İsteğe bağlı **iCloud senkronizasyonu** yalnızca tercihleri ​​kapsar; fotoğraf dosyalarını kapsamaz.

## Veri Toplama

Kişisel bilgilerinizi toplayan bir arka uç işletmiyoruz:

- **Hesap yok** — Kayıt, e-posta veya telefon numarası gerekmez.
- **Analiz veya reklam yok** — Üçüncü taraf analiz, reklam veya izleme SDK'sı yok.
- **Analiz için fotoğraf yükleme yok** — Yüz önemli noktaları ve görüntüleme cihazda kalır.

## Uygulama Nasıl Çalışır?

- **Depolama** — Projeler (orijinal / küçük resim / düzenleme durumu) uygulama sanal alanında yayınlanır. Widget küçük resimleri Uygulama Grubu kapsayıcısını kullanır.
- **Yüz güzelliği** — Aşağıdaki **Yüz Verileri ve Cihaz Üzerinde Güzellik İşleme** konusuna bakın.
- **Fotoğraf Kitaplığı** — Erişim, seçtiğiniz içe aktarma işlemleriyle sınırlıdır ve isteğe bağlı dışa aktarma, başlattığınız kayıtları kaydeder.
- **Meta veri şeridi** — İsteğe bağlı olarak EXIF ​​/ GPS / cihaz alanlarını oluşturduğunuz dışa aktarmalardan kaldırır.

## Yüz Verileri ve Cihaz Üzerinde Güzellik İşleme

When you use beauty features (Capture live preview, shutter bake, or the editor Beauty tool), iPhoto analyzes faces **only on your device** using Apple’s Vision framework (`VNDetectFaceLandmarksRequest`). This is **not** face recognition, identity matching, biometrics enrollment, or authentication.

### Hangi yüz verileri işleniyor?

- **Geçici yer işaretleri (yalnızca bellek):** yüz sınırlayıcı kutu, yüz çevresi, gözler, kaşlar, dış/iç dudaklar, gözbebekleri ve isteğe bağlı kozmetik düzenlemelere (pürüzsüzleştirme, beyazlatma, inceltme, gözler, dişler, allık, ruj) yönelik maskeler oluşturmak için kullanılan ilgili geometri.
- **Bir projede ısrar edildi (isteğe bağlı):** **normalleştirilmiş yüz sınırlayıcı dikdörtgen** artı seçtiğiniz **güzellik gücü / renk parametreleri** (`FaceBeautyEdit`), böylece projeyi yeniden açtığınızda yüze özel ayarlar geri yüklenebilir. **Tam yer işareti koordinatları diske yazılmaz.**

### Kullanım

Yüz geometrisi yalnızca çekim önizlemesi, fotoğraf çekimi, düzenleyici önizlemesi, küçük resim yenileme ve dışa aktarma/paylaşma sırasında **sizin** etkinleştirdiğiniz güzellik ayarlarını uygulamak için kullanılır. Reklam, profil oluşturma veya tanımlama amacıyla kullanılmaz.

### Paylaşma

**Yüz verileri hiçbir zaman üçüncü taraflarla paylaşılmaz.** iHTC Studio sunucularına veya herhangi bir bulut analiz API'sine yüklenmez. İsteğe bağlı iCloud Anahtar-Değer senkronizasyonu **yalnızca tercihleri** kapsar (örneğin dil, tema, güzellik tarifi yakalama geçişleri) ve **fotoğrafları veya yüz yer işaretlerini senkronize etmez**.

### Depolama yeri

- Fotoğraflar ve proje düzenleme dosyaları: **cihazınızdaki uygulama sanal alanı**
- Geçici yer işaretleri: **Yalnızca RAM** (düzenleyiciden çıktığınızda temizlenir / analiz önbelleğini temizler)
- Widget küçük resimleri: Cihazınızdaki Uygulama Grubu (işlenen görüntüler, yer işareti veri kümeleri değil)

### Saklama ve silme

- Geçici yer işaretleri yalnızca işlem sırasında bulunur ve daha sonra atılır.
- Kalıcı yüz kutuları ve güzellik parametreleri **yalnızca ilgili fotoğraf projesini sakladığınızda** kalır.
- İlgili yüz meta verilerini ve yerel fotoğrafları kaldırmak için bir projeyi **silin**, düzenlemeleri **sıfırlayın** veya uygulamayı **kaldırın**.

### Üçüncü taraflar

Yok. Tüm yüz analizi ve görüntüleme, cihazdaki Apple Vision ve Core Image'ı kullanır.

## Cihazınızda Saklanan Veriler

| Veri | Nerede | Amaç |
|------|-------|---------|
| Fotoğraf projeleri | Uygulama Belgeleri | Orijinaller, başparmaklar, düzenleme durumu |
| Yüz güzelliği meta verilerini düzenleme | Proje düzenleme durumu (korumalı alan) | Normalleştirilmiş yüz kutusu + yalnızca güzellik parametreleri |
| Tercihler | Uygulama Grubu Kullanıcı Varsayılanları | Dil, tema, yakalama/dışa aktarma seçenekleri |
| Widget anlık görüntüleri | Uygulama Grubu | Widget'lar için son projeler / istatistikler |
| Güzellik tarifini yakalayın | Uygulama Grubu (isteğe bağlı hatırlayın) | Güç ve güzellik parametreleri |
| iCloud tercihleri | Özel iCloud KVS'niz | İsteğe bağlı tercih senkronizasyonu |

## iCloud Senkronizasyonu

Optional sync uses Apple's `NSUbiquitousKeyValueStore` for lightweight preferences (appearance, language, export defaults, capture beauty settings, and similar). **Photo files and face landmarks are not synced.** Sync can be turned off in Settings.

## İzinler

| İzin | Amaç |
|------------|---------|
| Kamera | Yakalama sekmesi |
| Fotoğraf Kitaplığı (oku) | İthalat |
| Fotoğraf Kitaplığı (yalnızca ekleme) | İsteğe bağlı olarak Fotoğraflar'a aktarma |
| Mikrofon | Sesli video kaydederken isteğe bağlı ses; fotoğraf çekimi bunu gerektirmez |

## Uygulama İçi Satın Alımlar

İsteğe bağlı **İpucu Geliştirici**, bir StoreKit sarf malzemesi satın alımıdır. Özelliklerin kilidini açmaz ve ayrı bir uygulama hesabı gerektirmez.

## Çocukların Gizliliği

iPhoto bilerek çocuklardan kişisel veri toplamaz. Çekirdek işleme, iHTC Studio veri toplama arka ucu olmadan cihazda kalır.

## Sorumluluk reddi beyanı

iPhoto **Apple Inc.'e bağlı değildir**

## Değişiklikler

Bu politikayı bu sayfada güncelleyebiliriz. Lütfen periyodik olarak gözden geçirin.

## İletişim

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
