---
layout: doc
title: iVideo — Privacy Policy
app_id: iVideo
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iVideo.
---

<section lang="en" markdown="1">

iHTC Studio ("we", "us" or "our") built iVideo (also known as "爱视频"). This page informs you of our policies regarding the collection, use and disclosure of personal data when you use our app.

## Summary

**iVideo does not collect, store or transmit any personal data.** All video recording, editing, and processing operations are performed entirely on your device. The app requires no account, no internet connection and no cloud services for its core features.

## Data Collection

We do not collect any data. Specifically:

- **No personal information** is collected (no name, email, phone number or account).
- **No usage data** or analytics are collected.
- **No video content, audio, screenshots or other media** you create or edit are accessible to us.
- **No cookies or tracking** technologies are used.
- **No third-party services** (advertising, analytics, crash reporting) are integrated.

## How the App Works

### Video Storage

All videos are stored locally on your device:

- **Recorded videos** are saved to the App Group shared container, accessible only by the app and its screen recording extension.
- **Imported videos** are copied to the app's sandboxed Documents folder.
- **Exported videos** (trimmed, compressed, speed-adjusted, etc.) are saved to the app's sandboxed Documents folder.

Videos are never uploaded to any server or cloud service by the app.

### Screen Recording

- **iOS**: Screen recording uses Apple's ReplayKit Broadcast Upload Extension. The recorded video is saved directly to the App Group container on your device.
- **macOS**: Screen recording uses Apple's ScreenCaptureKit framework. Recordings are saved locally.

Auto-snapshot images taken during recording are also stored locally in the App Group container.

### On-Device Speech Recognition

iVideo uses Apple's Speech framework with `requiresOnDeviceRecognition = true` for subtitle generation. This means:

- All speech-to-text processing happens **entirely on your device**.
- **No audio data** is sent to Apple's servers or any third party.
- Some languages may require downloading an offline language pack via System Settings; even then, recognition runs locally.
- The first use prompts a system permission dialog for Speech Recognition access.

### On-Device Face Detection

The Face Blur tool uses Apple's Vision framework to detect faces in video frames:

- Face detection runs **entirely on-device** — no video frames are uploaded.
- Detection results (face coordinates) are used only within the app to apply blur effects and are not stored or transmitted.

### On-Device Sound Analysis

The Sound Events subtitle mode uses Apple's SoundAnalysis framework to classify non-speech audio (music, applause, laughter, etc.):

- Classification runs **entirely on-device**.
- No audio data is sent to any server.

### On-Device Text Recognition (OCR)

The OCR tool uses Apple's Vision framework to recognize text in video frames:

- Text recognition runs **entirely on-device**.
- Recognized text is displayed for you to copy or share — it is not collected by us.

### On-Device Translation

Bilingual subtitle translation uses Apple's Translation framework:

- Translation runs **entirely on-device**.
- No subtitle text is sent to any server.

### iCloud Key-Value Storage

iVideo optionally uses Apple's `NSUbiquitousKeyValueStore` to sync lightweight preferences across your devices:

- Theme, language, playback speed, mute state
- Custom speed history, favorite tools bar, export presets

This sync uses Apple's iCloud infrastructure only. We have no access to this data. No video files are synced via iCloud. If you are not signed in to iCloud, the app functions normally with local-only preferences.

### Photo Library Access

When you import videos from your Photo Library or save videos to it, iVideo requests the necessary system permissions. Access is strictly limited to the import/save operation you initiate. We do not scan, index, or read your Photo Library beyond the specific items you select.

### Metadata Strip

The Metadata Strip tool removes embedded metadata (EXIF, GPS, device info) from video files. This is a privacy-enhancing feature — the cleaned video is saved locally and the original metadata is not transmitted anywhere.

### Siri & Shortcuts

iVideo registers AppShortcuts (start recording, open video library, Live Photo tool) with the system. These shortcuts are processed entirely on-device by iOS/macOS. No voice data or shortcut usage is sent to us.

### Local Notifications

When enabled, iVideo sends local notifications to inform you when an export task completes. These notifications are processed entirely on-device by iOS/macOS. No notification data is sent to any server. You can disable this in Settings → Export.

### Feedback Email

When you use the in-app feedback feature, the app composes an email using your device's Mail app (or `mailto:` fallback). Device information (model, OS version, app version, language) is included in the email body to help us diagnose issues. This information is only sent when you explicitly choose to send the email. We do not collect this information automatically.

## Data Sharing

We do not share any data with third parties because we do not collect any data.

## Data Retention

Since we do not collect any data, there is nothing to retain. All app data (videos, preferences, notes) resides on your device and is removed when you delete the app.

## Children's Privacy

iVideo does not collect personal information from anyone, including children under 13. The app contains no advertising, no in-app purchases beyond an optional tip, and no social features.

## Changes to This Policy

We may update this privacy policy from time to time. Changes will be posted on this page with an updated effective date.

## Contact Us

If you have any questions about this privacy policy, please contact us:

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="zh-CN" markdown="1">

爱火腿肠工作室（iHTC Studio）（「我们」）开发了 iVideo（爱视频）。本页面告知您在使用本应用时，我们关于个人数据的收集、使用和披露政策。

## 概要

**iVideo 不收集、存储或传输任何个人数据。** 所有视频录制、编辑和处理操作完全在您的设备上进行。应用的核心功能无需账号、无需联网、无需云服务。

## 数据收集

我们不收集任何数据。具体来说：

- **不收集个人信息**（无需姓名、邮箱、手机号或账号）。
- **不收集使用数据**或分析信息。
- **不访问您创建或编辑的任何视频、音频、截图或其他媒体内容**。
- **不使用 Cookie 或追踪**技术。
- **不集成任何第三方服务**（广告、分析、崩溃报告）。

## 应用工作方式

### 视频存储

所有视频存储在您的设备本地：

- **录屏视频** 保存到 App Group 共享容器，仅应用及其录屏扩展可访问。
- **导入视频** 复制到应用沙盒 Documents 文件夹。
- **导出视频**（裁剪、压缩、变速等）保存到应用沙盒 Documents 文件夹。

应用不会将视频上传到任何服务器或云服务。

### 录屏

- **iOS**：录屏使用 Apple ReplayKit 广播上传扩展。录制的视频直接保存到设备上的 App Group 容器。
- **macOS**：录屏使用 Apple ScreenCaptureKit 框架。录制内容保存在本地。

录制过程中的自动截图同样存储在本地 App Group 容器中。

### 设备端语音识别

iVideo 使用 Apple Speech 框架并强制启用 `requiresOnDeviceRecognition = true` 来生成字幕。这意味着：

- 所有语音转文字处理 **完全在设备端进行**。
- **不会将任何音频数据** 发送到 Apple 服务器或任何第三方。
- 部分语言可能需要通过系统设置下载离线语言包；即便如此，识别仍在本地运行。
- 首次使用时系统会弹出语音识别权限请求。

### 设备端人脸检测

人脸打码工具使用 Apple Vision 框架检测视频帧中的人脸：

- 人脸检测 **完全在设备端运行** ——不会上传任何视频画面。
- 检测结果（人脸坐标）仅在应用内用于施加模糊效果，不会被存储或传输。

### 设备端声音分析

声音事件字幕模式使用 Apple SoundAnalysis 框架对非语音音频进行分类（音乐、掌声、笑声等）：

- 分类处理 **完全在设备端进行**。
- 不会将任何音频数据发送到任何服务器。

### 设备端文字识别（OCR）

OCR 工具使用 Apple Vision 框架识别视频帧中的文字：

- 文字识别 **完全在设备端运行**。
- 识别的文字仅供您复制或分享——我们不会收集。

### 设备端翻译

双语字幕翻译使用 Apple Translation 框架：

- 翻译 **完全在设备端运行**。
- 不会将任何字幕文本发送到任何服务器。

### iCloud 键值存储

iVideo 可选使用 Apple 的 `NSUbiquitousKeyValueStore` 在您的设备间同步轻量偏好：

- 主题、语言、播放速度、静音状态
- 自定义速度档历史、常用工具快捷栏、导出预设

此同步仅使用 Apple 的 iCloud 基础设施。我们无法访问这些数据。不会通过 iCloud 同步任何视频文件。若您未登录 iCloud，应用将正常运行，偏好仅保存在本地。

### 相册访问

当您从相册导入视频或将视频保存到相册时，iVideo 会请求必要的系统权限。访问严格限于您发起的导入/保存操作。我们不会扫描、索引或读取您选择的特定项目之外的相册内容。

### 元数据清除

元数据清除工具可移除视频文件中嵌入的元数据（EXIF、GPS、设备信息）。这是一项隐私增强功能——清理后的视频保存在本地，原始元数据不会被传输到任何地方。

### Siri 与快捷指令

iVideo 向系统注册 AppShortcuts（开始录屏、打开视频库、Live Photo 工具）。这些快捷指令完全由 iOS/macOS 在设备上处理。不会向我们发送任何语音数据或快捷指令使用情况。

### 本地通知

启用后，iVideo 会在导出任务完成时发送本地通知提醒。这些通知完全由 iOS/macOS 在设备上处理，不会将任何通知数据发送到任何服务器。您可以在设置 → 导出中关闭此功能。

### 反馈邮件

使用应用内反馈功能时，应用通过设备的邮件 App（或 `mailto:` 回退方案）编写邮件。邮件正文中包含设备信息（型号、系统版本、应用版本、语言）以帮助我们诊断问题。此信息仅在您明确选择发送邮件时才会发出。我们不会自动收集此信息。

## 数据共享

我们不与任何第三方共享数据，因为我们不收集任何数据。

## 数据保留

由于我们不收集任何数据，因此无需保留。所有应用数据（视频、偏好、笔记）均在您的设备上，删除应用时一并移除。

## 儿童隐私

iVideo 不向任何人收集个人信息，包括 13 岁以下的儿童。应用不含广告、除可选打赏外无应用内购买、无社交功能。

## 政策变更

我们可能会不时更新本隐私政策。变更将发布在本页面并注明更新的生效日期。

## 联系我们

如对本隐私政策有任何疑问，请联系：

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="zh-TW" markdown="1">

愛火腿腸工作室（iHTC Studio）（「我們」）開發了 iVideo（愛視頻）。本頁面告知您在使用本應用程式時，我們關於個人資料的收集、使用和揭露政策。

## 概要

**iVideo 不收集、儲存或傳輸任何個人資料。** 所有影片錄製、編輯和處理操作完全在您的裝置上進行。應用程式的核心功能無需帳號、無需連網、無需雲端服務。

## 資料收集

我們不收集任何資料。具體而言：

- **不收集個人資訊**（無需姓名、電子郵件、電話號碼或帳號）。
- **不收集使用資料**或分析資訊。
- **不存取您建立或編輯的任何影片、音訊、截圖或其他媒體內容**。
- **不使用 Cookie 或追蹤**技術。
- **不整合任何第三方服務**（廣告、分析、當機報告）。

## 應用程式運作方式

### 影片儲存

所有影片儲存在您的裝置本地：

- **錄屏影片** 儲存到 App Group 共享容器，僅應用程式及其錄屏延伸功能可存取。
- **匯入影片** 複製到應用沙盒 Documents 資料夾。
- **匯出影片**（裁剪、壓縮、變速等）儲存到應用沙盒 Documents 資料夾。

應用程式不會將影片上傳到任何伺服器或雲端服務。

### 錄屏

- **iOS**：錄屏使用 Apple ReplayKit 廣播上傳延伸功能。錄製的影片直接儲存到裝置上的 App Group 容器。
- **macOS**：錄屏使用 Apple ScreenCaptureKit 框架。錄製內容儲存在本地。

錄製過程中的自動截圖同樣儲存在本地 App Group 容器中。

### 裝置端語音辨識

iVideo 使用 Apple Speech 框架並強制啟用 `requiresOnDeviceRecognition = true` 來產生字幕。這意味著：

- 所有語音轉文字處理 **完全在裝置端進行**。
- **不會將任何音訊資料** 傳送到 Apple 伺服器或任何第三方。
- 部分語言可能需要透過系統設定下載離線語言包；即便如此，辨識仍在本地運行。
- 首次使用時系統會彈出語音辨識權限請求。

### 裝置端人臉偵測

人臉打碼工具使用 Apple Vision 框架偵測影片幀中的人臉：

- 人臉偵測 **完全在裝置端運行** ——不會上傳任何影片畫面。
- 偵測結果（人臉座標）僅在應用內用於施加模糊效果，不會被儲存或傳輸。

### 裝置端聲音分析

聲音事件字幕模式使用 Apple SoundAnalysis 框架對非語音音訊進行分類（音樂、掌聲、笑聲等）：

- 分類處理 **完全在裝置端進行**。
- 不會將任何音訊資料傳送到任何伺服器。

### 裝置端文字辨識（OCR）

OCR 工具使用 Apple Vision 框架辨識影片幀中的文字：

- 文字辨識 **完全在裝置端運行**。
- 辨識的文字僅供您複製或分享——我們不會收集。

### 裝置端翻譯

雙語字幕翻譯使用 Apple Translation 框架：

- 翻譯 **完全在裝置端運行**。
- 不會將任何字幕文字傳送到任何伺服器。

### iCloud 鍵值儲存

iVideo 可選使用 Apple 的 `NSUbiquitousKeyValueStore` 在您的裝置間同步輕量偏好：

- 主題、語言、播放速度、靜音狀態
- 自訂速度檔歷史、常用工具快捷列、匯出預設

此同步僅使用 Apple 的 iCloud 基礎設施。我們無法存取這些資料。不會透過 iCloud 同步任何影片檔案。若您未登入 iCloud，應用程式將正常運行，偏好僅儲存在本地。

### 相簿存取

當您從相簿匯入影片或將影片儲存到相簿時，iVideo 會請求必要的系統權限。存取嚴格限於您發起的匯入/儲存操作。我們不會掃描、索引或讀取您選擇的特定項目之外的相簿內容。

### 中繼資料清除

中繼資料清除工具可移除影片檔案中嵌入的中繼資料（EXIF、GPS、裝置資訊）。這是一項隱私增強功能——清理後的影片儲存在本地，原始中繼資料不會被傳輸到任何地方。

### Siri 與捷徑

iVideo 向系統註冊 AppShortcuts（開始錄屏、開啟影片庫、Live Photo 工具）。這些捷徑完全由 iOS/macOS 在裝置上處理。不會向我們傳送任何語音資料或捷徑使用情況。

### 本地通知

啟用後，iVideo 會在匯出任務完成時傳送本地通知提醒。這些通知完全由 iOS/macOS 在裝置上處理，不會將任何通知資料傳送到任何伺服器。您可以在設定 → 匯出中關閉此功能。

### 回饋郵件

使用應用內回饋功能時，應用程式透過裝置的郵件 App（或 `mailto:` 備用方案）編寫郵件。郵件正文中包含裝置資訊（型號、系統版本、應用版本、語言）以協助我們診斷問題。此資訊僅在您明確選擇傳送郵件時才會發出。我們不會自動收集此資訊。

## 資料共享

我們不與任何第三方共享資料，因為我們不收集任何資料。

## 資料保留

由於我們不收集任何資料，因此無需保留。所有應用資料（影片、偏好、筆記）均在您的裝置上，刪除應用程式時一併移除。

## 兒童隱私

iVideo 不向任何人收集個人資訊，包括 13 歲以下的兒童。應用程式不含廣告、除可選打賞外無應用程式內購買、無社交功能。

## 政策變更

我們可能會不時更新本隱私政策。變更將發佈在本頁面並註明更新的生效日期。

## 聯絡我們

如對本隱私政策有任何疑問，請聯絡：

- **電子郵件：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ja" markdown="1">

iHTC Studio（「当社」）は **iVideo**（「爱视频」）を開発しました。本ページは、アプリ利用時の個人データの収集・利用・開示に関する方針を説明します。

## 概要

**iVideo は個人データを収集・保存・送信しません。** 録画、編集、処理はすべて **端末内** で完結します。コア機能にアカウント、インターネット、クラウドは不要です。

## データ収集

当社はデータを収集しません。具体的には：

- **個人情報**（氏名、メール、電話、アカウント）なし
- **利用状況データ**や analytics なし
- 作成・編集した **動画・音声・スクショ** を当社がアクセスすることはない
- **Cookie やトラッキング**なし
- 広告・analytics・クラッシュレポート等の **第三者サービス** なし

## アプリの動作

### 動画の保存

すべて端末ローカル：

- **録画** — App Group 共有コンテナ（アプリと録画拡張のみ）
- **インポート** — サンドボックス `Documents/ImportedVideos`
- **エクスポート** — サンドボックス `Documents/Exports`

動画がサーバーやクラウドにアップロードされることはありません。

### 画面録画

- **iOS** — ReplayKit Broadcast Upload Extension。App Group に直接保存。
- **macOS** — ScreenCaptureKit。ローカル保存。

録画中の自動スナップショットも App Group にローカル保存。

### 端末内音声認識

字幕生成は Apple Speech、`requiresOnDeviceRecognition = true`：

- 音声テキスト化は **端末内のみ**
- 音声データは Apple サーバーや第三者へ送信されない
- 一部言語はシステム設定でオフライン言語パックが必要；それでも認識はローカル
- 初回は Speech Recognition 権限ダイアログ

### 端末内顔検出

Face Blur は Apple Vision：

- **端末内** のみ — フレームのアップロードなし
- 検出座標はぼかしにのみ使用、保存・送信しない

### 端末内サウンド分析

Sound Events 字幕は SoundAnalysis：

- **端末内** 分類；音声サーバー送信なし

### 端末内 OCR

Vision によるテキスト認識：

- **端末内**；認識結果はコピー／共有用表示のみ、当社は収集しない

### 端末内翻訳

二言語字幕は Apple Translation：

- **端末内**；字幕テキストのサーバー送信なし

### iCloud Key-Value Storage

任意で `NSUbiquitousKeyValueStore` により軽量設定を同期：

- テーマ、言語、再生速度、ミュート、カスタム速度履歴、お気に入りツールバー、エクスポートプリセット

Apple iCloud のみ。当社はアクセス不可。**動画ファイルは iCloud 同期しません。** iCloud 未サインインでもローカル設定で通常動作。

### フォトライブラリ

インポート／保存時のみ必要な権限。選択項目以外はスキャン・索引・読取しません。

### メタデータ除去

Metadata Strip は EXIF／GPS／デバイス情報等を除去 — プライバシー強化。クリーン動画はローカル保存のみ。

### Siri と Shortcuts

AppShortcuts（録画開始、ライブラリ、Live Photo ツール）は iOS/macOS **端末内** 処理。音声や使用状況は当社へ送信されません。

### ローカル通知

エクスポート完了通知（任意）は端末内。**設定 → Export** で無効化可。

### フィードバックメール

**設定 → About → Feedback** で Mail 作成（または `mailto:`）。機種、OS、アプリ版、言語を本文に含む — **送信を選んだ場合のみ**。自動収集はありません。

## データ共有

データを収集しないため、第三者共有もありません。

## データ保持

収集データなし。動画・設定・メモは端末にあり、アプリ削除で除去（iOS/macOS の挙動に従う）。

## 児童のプライバシー

13 歳未満を含め個人情報を収集しません。広告、ソーシャル、必須 IAP（任意チップ除く）なし。

## 本ポリシーの変更

随時更新し、本ページに掲載します。

## お問い合わせ

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ko" markdown="1">

iHTC Studio(「당사」)는 **iVideo**(「爱视频」)를 개발했습니다. 본 페이지는 앱 사용 시 개인 데이터 수집·이용·공개 정책을 설명합니다.

## 요약

**iVideo는 개인 데이터를 수집·저장·전송하지 않습니다.** 녹화·편집·처리는 **100% 기기 내**에서 이루어집니다. 핵심 기능에 계정·인터넷·클라우드가 필요하지 않습니다.

## 데이터 수집

당사는 데이터를 수집하지 않습니다.

- **개인정보**(이름, 이메일, 전화, 계정) 없음
- **사용 analytics** 없음
- 사용자가 만든 **미디어**에 당사가 접근하지 않음
- **쿠키/추적** 없음
- 광고·analytics·크래시 **제3자 SDK** 없음

## 앱 동작

### 동영상 저장

모두 로컬: **녹화**(App Group), **가져오기**(`Documents/ImportedVideos`), **내보내기**(`Documents/Exports`). 서버 업로드 없음.

### 화면 녹화

- **iOS** — ReplayKit Broadcast Upload Extension → App Group
- **macOS** — ScreenCaptureKit, 로컬 저장

### 기기 내 Speech/OCR/Vision/Translation/SoundAnalysis

Apple 프레임워크, `requiresOnDeviceRecognition = true` 등 — **기기 내** 처리, 업로드 없음.

### iCloud KVS

테마, 언어, 재생 속도, 음소거, 속도 기록, 즐겨찾기 도구, 내보내기 프리셋만 동기화. **동영상 파일은 동기화하지 않음.**

### 사진, 메타데이터 제거, Siri, 로컬 알림, 피드백

권한은 사용자가 시작한 작업에만. 피드백은 **보낼 때만** 기기 정보 포함.

## 공유·보관

수집 없음 → 공유 없음. 앱 삭제 시 기기 데이터 제거.

## 아동

13세 미만 포함 고의 수집 없음.

## 변경·문의

정책 업데이트 가능. **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ru" markdown="1">

iHTC Studio («мы») разработала **iVideo** («爱视频»). Эта страница описывает политику сбора и использования персональных данных.

## Кратко

**iVideo не собирает, не хранит и не передаёт персональные данные.** Запись, монтаж и обработка **полностью на устройстве**. Для основных функций не нужны аккаунт, интернет и облако.

## Сбор данных

Мы ничего не собираем: ни персональные данные, ни аналитику использования, ни доступ к вашим медиа, ни tracking, ни сторонние рекламные/analytics SDK.

## Как работает приложение

Видео локально (App Group / Documents). Запись экрана: ReplayKit (iOS), ScreenCaptureKit (macOS). Speech, Vision, OCR, Translation, SoundAnalysis — **на устройстве** (`requiresOnDeviceRecognition` где применимо).

Опционально **`NSUbiquitousKeyValueStore`**: тема, язык, скорость, mute, история, избранные инструменты, пресеты экспорта — **не файлы видео**.

Доступ к Фото только для выбранных операций; Metadata Strip локально; Siri/Shortcuts и локальные уведомления on-device; feedback только при отправке.

## Передача и хранение

Нет сбора → нет передачи. Данные на устройстве до удаления приложения.

## Дети

Намеренно не собираем данные детей младше 13 лет.

## Изменения и контакты

Обновления на этой странице. **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="th" markdown="1">

iHTC Studio («เรา») พัฒนา **iVideo** («爱视频») หน้านี้อธิบายนโยบายการเก็บและใช้ข้อมูลส่วนบุคคล

## สรุป

**iVideo ไม่เก็บ เก็บถาวร หรือส่งข้อมูลส่วนบุคคล** การบันทึก ตัดต่อ และประมวลผล **บนอุปกรณ์ 100%** ไม่ต้องมีบัญชี อินเทอร์เน็ต หรือคลาวด์สำหรับฟีเจอร์หลัก

## การเก็บข้อมูล

เราไม่เก็บข้อมูล — ไม่มีข้อมูลส่วนตัว analytics การเข้าถึงสื่อของคุณ คุกกี้/ติดตาม หรือ SDK โฆษณา/วิเคราะห์

## การทำงาน

วิดีโอเก็บในเครื่อง (App Group / Documents) บันทึกหน้าจอ ReplayKit/ScreenCaptureKit Speech Vision OCR Translation SoundAnalysis **บนเครื่อง**

**`NSUbiquitousKeyValueStore`** (ทางเลือก): ธีม ภาษา ความเร็ว ปิดเสียง ประวัติ แถบเครื่องมือโปรด พรีเซ็ตส่งออก — **ไม่ sync ไฟล์วิดีโอ**

คลังภาพเฉพาะที่คุณเลือก Metadata Strip ในเครื่อง Siri/Shortcuts และการแจ้งเตือนท้องถิ่น อีเมล feedback เมื่อคุณส่งเท่านั้น

## การแชร์และการเก็บ

ไม่เก็บ → ไม่แชร์ ข้อมูลอยู่บนอุปกรณ์จนกว่าจะลบแอป

## เด็ก

ไม่เก็บข้อมูลเด็กตั้งใจ

## การเปลี่ยนแปลงและติดต่อ

อัปเดตบนหน้านี้ **อีเมล:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="de" markdown="1">

iHTC Studio („wir") hat **iVideo** („爱视频") entwickelt. Diese Seite beschreibt Erhebung, Nutzung und Offenlegung personenbezogener Daten.

## Zusammenfassung

**iVideo erhebt, speichert oder überträgt keine personenbezogenen Daten.** Aufnahme, Bearbeitung und Verarbeitung erfolgen **vollständig auf dem Gerät**. Kein Konto, kein Internet und keine Cloud für Kernfunktionen.

## Datenerhebung

Wir erheben keine Daten — keine personenbezogenen Daten, keine Nutzungsanalyse, kein Zugriff auf Ihre Medien, kein Tracking, keine Werbe-/Analytics-SDKs.

## Funktionsweise

Videos liegen lokal (App Group / Documents). Bildschirmaufnahme: ReplayKit (iOS) bzw. ScreenCaptureKit (macOS). Speech, Vision, OCR, Translation und SoundAnalysis laufen **on-device** (`requiresOnDeviceRecognition` wo zutreffend).

Optional **`NSUbiquitousKeyValueStore`**: Theme, Sprache, Geschwindigkeit, Stummschaltung, Verlauf, Favoritenleiste, Export-Presets — **keine Videodateien**.

Fotozugriff nur für von Ihnen gewählte Importe/Exporte. Metadata Strip entfernt EXIF/GPS lokal. Siri/Shortcuts und Export-Benachrichtigungen on-device. Feedback-E-Mail nur bei explizitem Senden.

## Weitergabe & Aufbewahrung

Keine Erhebung → keine Weitergabe. Daten nur auf dem Gerät bis zur Deinstallation.

## Kinder

Keine absichtliche Erhebung bei Kindern unter 13.

## Änderungen & Kontakt

Aktualisierungen auf dieser Seite. **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="fr" markdown="1">

iHTC Studio (« nous ») a développé **iVideo** (« 爱视频 »). Cette page décrit la collecte, l'utilisation et la divulgation des données personnelles.

## Résumé

**iVideo ne collecte, stocke ni transmet de données personnelles.** Enregistrement, montage et traitement **100 % sur l'appareil**. Pas de compte, d'Internet ni de cloud pour les fonctions principales.

## Collecte

Aucune collecte : pas d'infos personnelles, pas d'analytique d'usage, pas d'accès à vos médias, pas de cookies/tracking, pas de SDK publicitaires/analytiques tiers.

## Fonctionnement

Stockage local (App Group / Documents). Capture d'écran : ReplayKit (iOS), ScreenCaptureKit (macOS). Speech, Vision, OCR, Translation, SoundAnalysis **sur l'appareil**.

**`NSUbiquitousKeyValueStore`** optionnel : thème, langue, vitesse, muet, historique, barre d'outils favorites, préréglages d'export — **pas de fichiers vidéo**.

Photothèque limitée à vos actions ; Metadata Strip local ; Siri/Shortcuts et notifications locales on-device ; e-mail de feedback uniquement si vous envoyez.

## Partage & conservation

Pas de collecte → pas de partage. Données sur l'appareil jusqu'à désinstallation.

## Enfants

Pas de collecte volontaire des moins de 13 ans.

## Modifications & contact

Mises à jour sur cette page. **E-mail :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="tr" markdown="1">

iHTC Studio («biz») **iVideo** («爱视频») uygulamasını geliştirdi. Bu sayfa kişisel verilerin toplanması ve kullanımını açıklar.

## Özet

**iVideo kişisel veri toplamaz, saklamaz veya iletmez.** Kayıt, düzenleme ve işleme **tamamen cihazda**. Çekirdek özellikler için hesap, internet veya bulut gerekmez.

## Toplama

Veri toplamıyoruz — kişisel bilgi, kullanım analitiği, medyanıza erişim, çerez/izleme veya üçüncü taraf reklam/analytics SDK yok.

## Nasıl çalışır

Videolar yerelde (App Group / Documents). Ekran kaydı ReplayKit/ScreenCaptureKit. Speech, Vision, OCR, Translation, SoundAnalysis **cihazda**.

İsteğe bağlı **`NSUbiquitousKeyValueStore`**: tema, dil, hız, sessiz, geçmiş, favori araç çubuğu, dışa aktarma ön ayarları — **video dosyaları değil**.

Fotoğraflar yalnızca seçtiğiniz işlemler; Metadata Strip yerelde; Siri/Kısayollar ve yerel bildirimler; geri bildirim yalnızca gönderirseniz.

## Paylaşım ve saklama

Toplama yok → paylaşım yok. Veriler uygulama silinene kadar cihazda.

## Çocuklar

13 yaş altı için kasıtlı toplama yok.

## Değişiklikler ve iletişim

Bu sayfada güncellenir. **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
