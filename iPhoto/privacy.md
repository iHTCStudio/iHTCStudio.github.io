---
layout: doc
title: iVeil — Privacy Policy
app_id: iPhoto
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iVeil (爱修图) — on-device privacy checks before you share. No account, no tracking, no photo upload.
---

<section lang="en" markdown="1">

iHTC Studio ("we", "us"; formerly iHTCTeam) makes **iVeil** (爱修图 / 愛修圖; earlier versions were called iPhoto). This policy explains what happens to your data when you use the app and its Share extension, Photos editing extension, widgets, Control Center controls and Lock Screen camera.

*Last updated: October 18, 2026*

## Summary

- **No account, no ads, no analytics, no tracking.** iVeil contains no third-party analytics, advertising or tracking SDKs.
- **Your photos and videos never leave your device through iVeil.** Detection, editing and export run on your device. We do not operate servers that receive your content.
- **You decide what is shared.** iVeil creates new copies. Your originals in Photos are only changed if you save an edit with the Photos editing extension, and that edit can be reverted in Photos.

## What iVeil processes on your device

| Data | Why | What is kept |
|------|-----|--------------|
| Photos and videos you choose (Photos, the Share menu, Files, or the camera) | To check, hide and edit them | Stored in the app sandbox until you delete them. Photos handed over from the Share extension pass briefly through the App Group container and are moved into the app. |
| Faces and people (Apple Vision) | To find and hide faces, keep the people you choose, tilt an emoji veil with the head, cut out a person you kept, and optional portrait retouching | Rectangles or outlines needed to redraw your hides are saved with the project. Facial landmarks stay in memory only. |
| Text in images (Vision text recognition and Apple data detectors) | To find phone numbers, emails, addresses, card and ID numbers, passport lines, order numbers, account IDs and links | Only the area and the type of item are saved. The recognized text itself is not saved. |
| QR codes and barcodes | To hide them and, with Code X-ray, tell you what kind of information they carry | Only the category and field names (for example "boarding pass: seat") are saved, never the contents. |
| File details (location, capture time, camera, lens, serial numbers) | To show what a file reveals and remove it from the copies you share | Read from your file. Copies keep only what you choose; serial numbers and owner names are always removed. |
| Possibly sensitive images (Apple Sensitive Content Analysis) | To blur nudity or graphic content before you share, only if you turned on Sensitive Content Warning or Communication Safety in Settings | Analysis runs on device inside Apple's framework. Results are not stored or sent. |
| Apple Intelligence (optional, iOS 26) | "Look Again with Apple Intelligence" and "Describe a Look" | Runs on Apple's on-device model. It receives only recognized text lines and counts, or the sentence you type, never images or face data. |
| Invisible Mark (optional) | To check later who you sent a photo to | A 32-bit code is hidden in the image brightness. The recipient names you enter are kept in a list on your device (up to 500 entries) that you can edit or clear in Settings → Invisible Mark. |
| Lifts and Genmoji veils | To reuse cut-outs and custom emoji | Saved as images in the App Group container on your device until you remove them. |
| Recently Deleted | To undo a deletion | Deleted projects are kept for 30 days, then removed permanently. |
| Preferences | Language, appearance, capture and export options | Stored in the App Group container on your device. |

## Face data

iVeil uses Apple's Vision framework on your device to **locate** faces and people. This is **not** face recognition: iVeil does not identify who anyone is, does not compare faces, and does not create biometric templates.

- **Use:** hiding faces, keeping the people you choose, aligning emoji veils, cutting out a person you kept, and optional portrait retouching.
- **Storage:** normalized face rectangles, person outlines and your retouch settings are saved inside the project in the app sandbox. Full facial landmarks are never written to disk.
- **Sharing:** face data is never uploaded and never shared with us or any third party, and it is not synced to iCloud.
- **Retention:** face data stays only as long as the project. Deleting a project (after 30 days in Recently Deleted) or uninstalling the app removes it.

## Network use

iVeil has no servers of its own. The only network requests come from Apple services:

- **Maps.** When a photo has a location, iVeil shows it on an Apple Maps map, which loads map tiles for that area from Apple. When you pick **City block**, the place name is looked up from Apple using the center of a ~5 km grid cell, not the exact coordinates. No image content is sent. Apple handles these requests under [Apple's Privacy Policy](https://www.apple.com/legal/privacy/).
- **Optional tip.** "Tip Developer" is a consumable in-app purchase processed by Apple through StoreKit. It unlocks nothing, and we receive no personal information.
- **Optional iCloud sync (off by default).** When you turn it on, a few preferences (such as language, appearance and capture or export options) sync through your private iCloud key-value store. Photos, videos, face data and the Invisible Mark list are never synced.

## Permissions

| Permission | Purpose |
|------------|---------|
| Photos | Open the photos you pick and show their location and camera details |
| Photos (add only) | Save the copies you export |
| Camera | Capture tab, Live Veil, and the Veil Camera on the Lock Screen |

iVeil does not request microphone, location, contacts or tracking permission. Video Veil uses the audio already in the video you pick and can remove it.

## Background work and Live Activities

Batch Safe Share and Video Veil exports that **you start** may continue briefly in the background. A Live Activity can show the job title and progress on the Lock Screen. It never shows image content.

## Children

iVeil does not knowingly collect personal data from anyone, including children, because content is processed on device and we have no data-collection backend.

## Disclaimer

iVeil is an independent app and is **not affiliated with Apple Inc.** Automatic detection is a first pass, not a guarantee. Please review a photo before sharing it.

## Changes

We will update this page if our practices change and revise the date above.

## Contact

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="zh-CN" markdown="1">

iHTC Studio（「我们」；原 iHTCTeam）开发了 **爱修图**（英文名 iVeil；早期版本名为 iPhoto）。本政策说明你使用本 App 及其分享扩展、「照片」编辑扩展、小组件、控制中心控件与锁定屏幕相机时，数据如何被处理。

*最后更新：2026 年 10 月 18 日*

## 概要

- **无账号、无广告、无统计、无追踪。** 未集成任何第三方统计、广告或追踪 SDK。
- **你的照片和视频不会经由爱修图离开设备。** 识别、编辑与导出都在本机完成；我们没有接收你内容的服务器。
- **分享什么由你决定。** 爱修图只生成新的副本；只有当你在「照片」编辑扩展中保存编辑时才会修改「照片」里的原图，且可以在「照片」中复原。

## 爱修图在本机处理哪些数据

| 数据 | 用途 | 保留什么 |
|------|------|----------|
| 你选择的照片与视频（来自「照片」、分享菜单、「文件」或相机） | 检查、遮蔽与编辑 | 存放在 App 沙盒，直到你删除。分享扩展转交的照片会短暂经过 App Group 容器，随后移入 App。 |
| 人脸与人物（Apple Vision） | 找出并遮住人脸、保留你选择的人、让表情面纱跟随头部倾斜、抠出保留的人，以及可选的人像精修 | 仅随项目保存重新绘制遮蔽所需的矩形或轮廓；面部关键点只在内存中。 |
| 图中文字（Vision 文字识别与 Apple 数据检测） | 找出手机号、邮箱、地址、卡号与证件号、护照机读码、订单号、账号与链接 | 只保存区域与类型，**不保存识别出的文字本身**。 |
| 二维码与条码 | 遮住它们，并通过「码里藏着什么」告诉你其中装着哪类信息 | 只保存类别与字段名（如「登机牌：座位」），**从不保存内容**。 |
| 文件信息（位置、拍摄时间、相机、镜头、序列号） | 告诉你文件透露了什么，并从你分享的副本中去除 | 从你的文件中读取；副本只保留你选择保留的部分，序列号与机主姓名始终去除。 |
| 可能敏感的画面（Apple 敏感内容分析） | 仅当你在系统设置中开启「敏感内容警告」或「通信安全」时，在分享前模糊裸露或血腥内容 | 在 Apple 框架内于本机分析，结果不保存、不发送。 |
| Apple 智能（可选，iOS 26） | 「让 Apple 智能再看一遍」与「描述一种风格」 | 由 Apple 端侧模型处理，只接收识别出的文字行与数量，或你输入的一句话，**从不接收图像或人脸数据**。 |
| 隐形标记（可选） | 日后查出照片发给了谁 | 在图像亮度中写入 32 位编码；你填写的接收人名称保存在本机列表中（最多 500 条），可在「设置 → 隐形标记」中删除或清空。 |
| 抠图与 Genmoji 面纱 | 重复使用抠出的人物与自定义表情 | 以图片形式保存在本机 App Group 容器中，直到你移除。 |
| 最近删除 | 撤销误删 | 删除的项目保留 30 天，之后永久删除。 |
| 偏好设置 | 语言、外观、拍摄与导出选项 | 保存在本机 App Group 容器中。 |

## 人脸数据

爱修图在本机使用 Apple Vision 框架**定位**人脸与人物。这**不是**人脸识别：爱修图不会识别任何人的身份，不比对人脸，也不生成生物特征模板。

- **用途：** 遮住人脸、保留你选择的人、对齐表情面纱、抠出保留的人，以及可选的人像精修。
- **存储：** 归一化人脸矩形、人物轮廓与你的精修参数保存在 App 沙盒内的项目中；完整面部关键点从不写入磁盘。
- **共享：** 人脸数据不会上传，不会提供给我们或任何第三方，也不会同步到 iCloud。
- **保留期限：** 人脸数据仅随项目存在。删除项目（在「最近删除」中保留 30 天后）或卸载 App 即会移除。

## 网络使用

爱修图没有自己的服务器，仅有以下来自 Apple 服务的网络请求：

- **地图。** 照片带有位置时，爱修图用 Apple 地图显示，地图会向 Apple 加载该区域的图块。选择**大约位置**时，地名使用约 5 公里网格的中心点向 Apple 查询，而不是精确坐标。不会发送任何图像内容。这些请求由 Apple 依据 [Apple 隐私政策](https://www.apple.com/cn/legal/privacy/) 处理。
- **可选打赏。** 「打赏开发者」是由 Apple 通过 StoreKit 处理的消耗型内购，不解锁任何功能，我们不会收到你的个人信息。
- **可选 iCloud 同步（默认关闭）。** 开启后，少量偏好（如语言、外观、拍摄或导出选项）通过你私人的 iCloud 键值存储同步。照片、视频、人脸数据与隐形标记名单从不同步。

## 权限

| 权限 | 用途 |
|------|------|
| 照片 | 打开你选择的照片，显示位置与相机信息 |
| 照片（仅添加） | 保存你导出的副本 |
| 相机 | 拍摄页、实时面纱与锁定屏幕上的面纱相机 |

爱修图不请求麦克风、定位、通讯录或追踪权限。视频面纱使用你所选视频中已有的声音，并可将其去除。

## 后台任务与实时活动

由**你发起**的批量安心分享与视频面纱导出可能会在后台短暂继续。实时活动可在锁定屏幕显示任务标题与进度，从不显示图像内容。

## 儿童隐私

由于内容均在本机处理、且我们没有数据收集后端，爱修图不会有意收集任何人（包括儿童）的个人数据。

## 声明

爱修图为独立应用，**与 Apple Inc. 无关联**。自动识别是第一道防线，并非万无一失，分享前请再检查一遍。

## 变更

若我们的做法发生变化，将更新本页并修改上方日期。

## 联系

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="zh-TW" markdown="1">

愛火腿腸工作室（iHTC Studio）（「我們」；原 iHTCTeam）開發了 **愛修圖**（英文名 iVeil；早期版本名為 iPhoto）。本政策說明你使用本 App 及其分享延伸功能、「照片」編輯延伸功能、小工具、控制中心控制項與鎖定畫面相機時，資料如何被處理。

*最後更新：2026 年 10 月 18 日*

## 概要

- **無帳號、無廣告、無統計、無追蹤。** 未整合任何第三方統計、廣告或追蹤 SDK。
- **你的照片和影片不會經由愛修圖離開裝置。** 辨識、編輯與匯出都在本機完成；我們沒有接收你內容的伺服器。
- **分享什麼由你決定。** 愛修圖只產生新的副本；只有當你在「照片」編輯延伸功能中儲存編輯時才會修改「照片」裡的原圖，且可以在「照片」中復原。

## 愛修圖在本機處理哪些資料

| 資料 | 用途 | 保留什麼 |
|------|------|----------|
| 你選擇的照片與影片（來自「照片」、分享選單、「檔案」或相機） | 檢查、遮蔽與編輯 | 存放在 App 沙盒，直到你刪除。分享延伸功能轉交的照片會短暫經過 App Group 容器，隨後移入 App。 |
| 人臉與人物（Apple Vision） | 找出並遮住人臉、保留你選擇的人、讓表情面紗跟隨頭部傾斜、摳出保留的人，以及可選的人像精修 | 僅隨項目儲存重新繪製遮蔽所需的矩形或輪廓；臉部關鍵點只在記憶體中。 |
| 圖中文字（Vision 文字辨識與 Apple 資料偵測） | 找出電話號碼、電子郵件、地址、卡號與證件號碼、護照機讀碼、訂單編號、帳號與連結 | 只儲存區域與類型，**不儲存辨識出的文字本身**。 |
| QR 碼與條碼 | 遮住它們，並透過「碼裡藏著什麼」告訴你其中裝著哪類資訊 | 只儲存類別與欄位名稱（如「登機證：座位」），**從不儲存內容**。 |
| 檔案資訊（位置、拍攝時間、相機、鏡頭、序號） | 告訴你檔案透露了什麼，並從你分享的副本中移除 | 從你的檔案中讀取；副本只保留你選擇保留的部分，序號與擁有者姓名一律移除。 |
| 可能敏感的畫面（Apple 敏感內容分析） | 僅當你在系統設定中開啟「敏感內容警告」或「通訊安全」時，在分享前模糊裸露或血腥內容 | 在 Apple 框架內於本機分析，結果不儲存、不傳送。 |
| Apple Intelligence（可選，iOS 26） | 「讓 Apple Intelligence 再看一遍」與「描述一種風格」 | 由 Apple 裝置端模型處理，只接收辨識出的文字行與數量，或你輸入的一句話，**從不接收影像或人臉資料**。 |
| 隱形標記（可選） | 日後查出照片傳給了誰 | 在影像亮度中寫入 32 位元編碼；你填寫的接收人名稱儲存在本機列表中（最多 500 筆），可在「設定 → 隱形標記」中刪除或清空。 |
| 去背與 Genmoji 面紗 | 重複使用摳出的人物與自訂表情 | 以圖片形式儲存在本機 App Group 容器中，直到你移除。 |
| 最近刪除 | 復原誤刪 | 刪除的項目保留 30 天，之後永久刪除。 |
| 偏好設定 | 語言、外觀、拍攝與匯出選項 | 儲存在本機 App Group 容器中。 |

## 人臉資料

愛修圖在本機使用 Apple Vision 框架**定位**人臉與人物。這**不是**人臉辨識：愛修圖不會辨識任何人的身分，不比對人臉，也不產生生物特徵模板。

- **用途：** 遮住人臉、保留你選擇的人、對齊表情面紗、摳出保留的人，以及可選的人像精修。
- **儲存：** 正規化人臉矩形、人物輪廓與你的精修參數儲存在 App 沙盒內的項目中；完整臉部關鍵點從不寫入磁碟。
- **共享：** 人臉資料不會上傳，不會提供給我們或任何第三方，也不會同步到 iCloud。
- **保留期限：** 人臉資料僅隨項目存在。刪除項目（在「最近刪除」中保留 30 天後）或解除安裝 App 即會移除。

## 網路使用

愛修圖沒有自己的伺服器，僅有以下來自 Apple 服務的網路請求：

- **地圖。** 照片帶有位置時，愛修圖以 Apple 地圖顯示，地圖會向 Apple 載入該區域的圖磚。選擇**大約位置**時，地名使用約 5 公里網格的中心點向 Apple 查詢，而不是精確座標。不會傳送任何影像內容。這些請求由 Apple 依據 [Apple 隱私權政策](https://www.apple.com/tw/legal/privacy/) 處理。
- **可選打賞。** 「打賞開發者」是由 Apple 透過 StoreKit 處理的消耗型 App 內購買，不解鎖任何功能，我們不會收到你的個人資訊。
- **可選 iCloud 同步（預設關閉）。** 開啟後，少量偏好（如語言、外觀、拍攝或匯出選項）透過你私人的 iCloud 鍵值儲存同步。照片、影片、人臉資料與隱形標記名單從不同步。

## 權限

| 權限 | 用途 |
|------|------|
| 照片 | 打開你選擇的照片，顯示位置與相機資訊 |
| 照片（僅加入） | 儲存你匯出的副本 |
| 相機 | 拍攝頁、即時面紗與鎖定畫面上的面紗相機 |

愛修圖不請求麥克風、定位、聯絡人或追蹤權限。影片面紗使用你所選影片中已有的聲音，並可將其移除。

## 背景作業與即時動態

由**你發起**的批次安心分享與影片面紗匯出可能會在背景短暫繼續。即時動態可在鎖定畫面顯示作業標題與進度，從不顯示影像內容。

## 兒童隱私

由於內容均在本機處理、且我們沒有資料收集後端，愛修圖不會有意收集任何人（包括兒童）的個人資料。

## 聲明

愛修圖為獨立應用程式，**與 Apple Inc. 無關聯**。自動辨識是第一道防線，並非萬無一失，分享前請再檢查一遍。

## 變更

若我們的做法有所改變，將更新本頁並修改上方日期。

## 聯絡

- **信箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ja" markdown="1">

iHTC Studio（「当社」。旧 iHTCTeam）は **iVeil**（爱修图 / 愛修圖。初期バージョンの名称は iPhoto）を開発しています。本ポリシーは、本 App およびその共有機能拡張、「写真」編集機能拡張、ウィジェット、コントロールセンターのコントロール、ロック画面カメラを使うとき、データがどのように扱われるかを説明します。

*最終更新：2026 年 10 月 18 日*

## 概要

- **アカウントなし、広告なし、解析なし、追跡なし。** 第三者の解析、広告、追跡 SDK は組み込まれていません。
- **写真とビデオが iVeil を通じて端末の外に出ることはありません。** 検出、編集、書き出しはすべて端末上で行われます。コンテンツを受け取るサーバーは運営していません。
- **何を共有するかはあなたが決めます。** iVeil は新しいコピーを作るだけです。「写真」内の原本が変わるのは、「写真」編集機能拡張で編集を保存したときだけで、その編集は「写真」で元に戻せます。

## iVeil が端末上で処理するデータ

| データ | 目的 | 残るもの |
|------|-----|--------------|
| 選んだ写真とビデオ（「写真」、共有メニュー、「ファイル」、またはカメラ） | 確認、非表示、編集のため | 削除するまで App のサンドボックスに保存されます。共有機能拡張から渡された写真は、いったん App Group コンテナを通り、その後 App 内へ移されます。 |
| 顔と人物（Apple Vision） | 顔を見つけて隠す、残したい人を残す、絵文字ベールを頭の傾きに合わせる、残した人を切り抜く、任意のポートレート補正 | 隠した部分を描き直すのに必要な矩形または輪郭だけをプロジェクトとともに保存します。顔のランドマークはメモリ上だけです。 |
| 画像内の文字（Vision の文字認識と Apple のデータ検出） | 電話番号、メール、住所、カード番号と身分証番号、パスポートの機械読取行、注文番号、アカウント ID、リンクを見つける | 領域と種類だけを保存します。認識した文字そのものは保存しません。 |
| QR コードとバーコード | それらを隠し、「コードの中身」で、どんな種類の情報が入っているかを知らせる | 分類と項目名（例：「搭乗券：座席」）だけを保存し、中身は決して保存しません。 |
| ファイル情報（位置情報、撮影日時、カメラ、レンズ、シリアル番号） | ファイルが何を明かしているかを示し、共有するコピーから取り除く | ファイルから読み取ります。コピーには選んだものだけが残ります。シリアル番号と所有者名は常に削除されます。 |
| センシティブな可能性のある画像（Apple のセンシティブコンテンツ解析） | 設定で「センシティブコンテンツの警告」または「コミュニケーションの安全性」をオンにしている場合に限り、共有前に裸や生々しい内容をぼかす | Apple のフレームワーク内で端末上で解析します。結果は保存も送信もされません。 |
| Apple Intelligence（任意、iOS 26） | 「Apple Intelligence でもう一度見る」と「ルックを説明する」 | Apple の端末上モデルで動きます。受け取るのは認識したテキスト行と件数、または入力した一文だけで、画像や顔データは決して受け取りません。 |
| 見えない印（任意） | あとから、写真を誰に送ったか確認する | 32 ビットの符号を画像の明るさに埋め込みます。入力した受取人の名前は端末上のリスト（最大 500 件）に残り、「設定 → 見えない印」で編集または消去できます。 |
| 切り抜きと Genmoji ベール | 切り抜いた人物とカスタム絵文字を再利用する | 削除するまで、端末の App Group コンテナに画像として保存されます。 |
| 最近削除した項目 | 削除を取り消す | 削除したプロジェクトは 30 日間残り、その後完全に削除されます。 |
| 環境設定 | 言語、外観、撮影と書き出しのオプション | 端末の App Group コンテナに保存されます。 |

## 顔データ

iVeil は端末上の Apple Vision フレームワークで顔と人物の**位置を特定**します。これは顔認識ではありません。iVeil は誰かを特定せず、顔を照合せず、生体テンプレートも作りません。

- **用途：** 顔を隠す、残したい人を残す、絵文字ベールの位置を合わせる、残した人を切り抜く、任意のポートレート補正。
- **保存：** 正規化した顔の矩形、人物の輪郭、補正設定は、App サンドボックス内のプロジェクトに保存されます。顔のランドマーク一式がディスクに書き込まれることはありません。
- **共有：** 顔データはアップロードされず、当社や第三者に渡されず、iCloud にも同期されません。
- **保持期間：** 顔データはプロジェクトがある間だけ残ります。プロジェクトを削除する（「最近削除した項目」に 30 日残ったあと）か、App を削除すると消えます。

## ネットワークの利用

iVeil に自前のサーバーはありません。ネットワーク要求は Apple のサービスからのみ発生します。

- **マップ。** 写真に位置情報があるとき、iVeil は Apple マップ上に表示し、その地域の地図タイルを Apple から読み込みます。**街区程度**を選ぶと、地名は正確な座標ではなく、約 5 km の格子の中心から Apple に問い合わせます。画像の内容は送信されません。これらの要求は [Apple のプライバシーポリシー](https://www.apple.com/jp/legal/privacy/) に従って Apple が処理します。
- **任意のチップ。** 「開発者にチップ」は、StoreKit を通じて Apple が処理する消耗型の App 内課金です。機能は解放されず、当社が個人情報を受け取ることもありません。
- **任意の iCloud 同期（既定ではオフ）。** オンにすると、言語、外観、撮影や書き出しのオプションなど少数の環境設定が、個人の iCloud キー値ストアを通じて同期されます。写真、ビデオ、顔データ、見えない印のリストが同期されることはありません。

## アクセス許可

| 許可 | 目的 |
|------------|---------|
| 写真 | 選んだ写真を開き、位置情報とカメラ情報を表示する |
| 写真（追加のみ） | 書き出したコピーを保存する |
| カメラ | 撮影タブ、ライブベール、ロック画面のベールカメラ |

iVeil はマイク、位置情報、連絡先、追跡の許可を求めません。ビデオベールは、選んだビデオに既に入っている音声を使い、それを取り除くこともできます。

## バックグラウンド処理とライブアクティビティ

**自分で開始した**一括の安心共有とビデオベールの書き出しは、しばらくバックグラウンドで続くことがあります。ライブアクティビティは、ロック画面に作業名と進行状況を表示できます。画像の内容は決して表示しません。

## 子ども

内容は端末上で処理され、データを収集するバックエンドがないため、iVeil が子どもを含む誰かの個人データを故意に収集することはありません。

## 免責

iVeil は独立した App であり、**Apple Inc. とは関係がありません。** 自動検出は最初の一手であり、保証ではありません。共有する前に写真を確認してください。

## 変更

取り扱いが変わった場合は本ページを更新し、上記の日付を改めます。

## 連絡先

- **メール：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ko" markdown="1">

iHTC Studio(「당사」, 구 iHTCTeam)는 **iVeil**(爱修图 / 愛修圖, 초기 버전 이름은 iPhoto)을 만듭니다. 이 정책은 본 앱과 공유 확장, 「사진」 편집 확장, 위젯, 제어 센터 제어 항목, 잠금 화면 카메라를 사용할 때 데이터가 어떻게 처리되는지 설명합니다.

*최종 업데이트: 2026년 10월 18일*

## 요약

- **계정 없음, 광고 없음, 분석 없음, 추적 없음.** 제3자 분석, 광고, 추적 SDK가 들어 있지 않습니다.
- **사진과 비디오는 iVeil을 통해 기기를 떠나지 않습니다.** 인식, 편집, 내보내기는 모두 기기에서 이루어집니다. 콘텐츠를 받는 서버는 운영하지 않습니다.
- **무엇을 공유할지는 직접 정합니다.** iVeil은 새 사본만 만듭니다. 「사진」의 원본이 바뀌는 경우는 「사진」 편집 확장에서 편집을 저장할 때뿐이며, 그 편집은 「사진」에서 되돌릴 수 있습니다.

## iVeil이 기기에서 처리하는 데이터

| 데이터 | 목적 | 남는 것 |
|------|-----|--------------|
| 선택한 사진과 비디오(「사진」, 공유 메뉴, 「파일」 또는 카메라) | 확인하고, 가리고, 편집하기 위해 | 삭제할 때까지 앱 샌드박스에 저장됩니다. 공유 확장에서 넘긴 사진은 App Group 컨테이너를 잠시 거친 뒤 앱으로 옮겨집니다. |
| 얼굴과 사람(Apple Vision) | 얼굴을 찾아 가리고, 남길 사람을 남기고, 이모지 베일을 고개 기울기에 맞추고, 남긴 사람을 오려 내고, 선택적 인물 보정 | 가린 부분을 다시 그리는 데 필요한 사각형이나 윤곽만 프로젝트와 함께 저장합니다. 얼굴 특징점은 메모리에만 있습니다. |
| 그림 속 글자(Vision 텍스트 인식과 Apple 데이터 감지) | 전화번호, 이메일, 주소, 카드 번호와 신분증 번호, 여권 기계 판독 줄, 주문 번호, 계정 ID, 링크를 찾기 위해 | 영역과 종류만 저장합니다. 인식된 글자 자체는 저장하지 않습니다. |
| QR 코드와 바코드 | 가리고, 「코드 속 내용」으로 어떤 종류의 정보가 들어 있는지 알려 주기 위해 | 분류와 필드 이름(예: 「탑승권: 좌석」)만 저장하며, 내용은 절대 저장하지 않습니다. |
| 파일 정보(위치, 촬영 시각, 카메라, 렌즈, 일련번호) | 파일이 무엇을 드러내는지 보여 주고, 공유하는 사본에서 제거하기 위해 | 파일에서 읽습니다. 사본에는 남기기로 한 것만 남고, 일련번호와 소유자 이름은 항상 제거됩니다. |
| 민감할 수 있는 화면(Apple 민감 콘텐츠 분석) | 설정에서 「민감한 콘텐츠 경고」 또는 「커뮤니케이션 안전」을 켠 경우에만, 공유 전에 노출이나 잔인한 장면을 흐리게 | Apple 프레임워크 안에서 기기에서 분석합니다. 결과는 저장하거나 보내지 않습니다. |
| Apple Intelligence(선택, iOS 26) | 「Apple Intelligence로 다시 보기」와 「스타일 설명하기」 | Apple의 온디바이스 모델에서 실행됩니다. 인식된 텍스트 줄과 개수, 또는 입력한 문장만 받으며, 이미지나 얼굴 데이터는 절대 받지 않습니다. |
| 보이지 않는 표시(선택) | 나중에 사진을 누구에게 보냈는지 확인하기 위해 | 32비트 부호를 이미지 밝기에 숨깁니다. 입력한 받는 사람 이름은 기기 목록(최대 500개)에 남으며, 「설정 → 보이지 않는 표시」에서 고치거나 지울 수 있습니다. |
| 오려 내기와 Genmoji 베일 | 오려 낸 사람과 맞춤 이모지를 다시 쓰기 위해 | 제거할 때까지 기기의 App Group 컨테이너에 이미지로 저장됩니다. |
| 최근 삭제된 항목 | 삭제를 되돌리기 위해 | 삭제한 프로젝트는 30일 동안 남았다가 영구 삭제됩니다. |
| 환경설정 | 언어, 모양, 촬영과 내보내기 옵션 | 기기의 App Group 컨테이너에 저장됩니다. |

## 얼굴 데이터

iVeil은 기기의 Apple Vision 프레임워크로 얼굴과 사람의 **위치만 찾습니다.** 이것은 얼굴 인식이 아닙니다. iVeil은 누구인지 식별하지 않고, 얼굴을 대조하지 않으며, 생체 템플릿도 만들지 않습니다.

- **용도:** 얼굴을 가리고, 남길 사람을 남기고, 이모지 베일을 맞추고, 남긴 사람을 오려 내고, 선택적으로 인물을 보정합니다.
- **저장:** 정규화된 얼굴 사각형, 사람 윤곽, 보정 설정은 앱 샌드박스의 프로젝트 안에 저장됩니다. 전체 얼굴 특징점은 디스크에 기록되지 않습니다.
- **공유:** 얼굴 데이터는 업로드되지 않고, 당사나 제3자에게 전달되지 않으며, iCloud에도 동기화되지 않습니다.
- **보관 기간:** 얼굴 데이터는 프로젝트가 있는 동안만 남습니다. 프로젝트를 삭제하면(「최근 삭제된 항목」에 30일 남은 뒤) 또는 앱을 삭제하면 제거됩니다.

## 네트워크 사용

iVeil에는 자체 서버가 없습니다. 네트워크 요청은 Apple 서비스에서만 발생합니다.

- **지도.** 사진에 위치가 있으면 iVeil은 Apple 지도에 표시하고, 해당 지역의 지도 타일을 Apple에서 불러옵니다. **대략적인 위치**를 고르면 지명은 정확한 좌표가 아니라 약 5 km 격자 중심을 Apple에 조회합니다. 이미지 내용은 전송되지 않습니다. 이 요청은 [Apple 개인정보 처리방침](https://www.apple.com/kr/legal/privacy/)에 따라 Apple이 처리합니다.
- **선택적 후원.** 「개발자에게 후원」은 StoreKit을 통해 Apple이 처리하는 소모성 앱 내 구입입니다. 기능을 잠금 해제하지 않으며, 당사는 개인 정보를 받지 않습니다.
- **선택적 iCloud 동기화(기본 꺼짐).** 켜면 언어, 모양, 촬영 또는 내보내기 옵션 같은 일부 환경설정이 개인 iCloud 키-값 저장소를 통해 동기화됩니다. 사진, 비디오, 얼굴 데이터, 보이지 않는 표시 목록은 동기화되지 않습니다.

## 권한

| 권한 | 용도 |
|------------|---------|
| 사진 | 선택한 사진을 열고 위치와 카메라 정보를 표시 |
| 사진(추가만) | 내보낸 사본을 저장 |
| 카메라 | 촬영 탭, 라이브 베일, 잠금 화면의 베일 카메라 |

iVeil은 마이크, 위치, 연락처, 추적 권한을 요청하지 않습니다. 비디오 베일은 선택한 비디오에 이미 들어 있는 소리를 쓰며, 그 소리를 제거할 수 있습니다.

## 백그라운드 작업과 라이브 액티비티

**직접 시작한** 일괄 안심 공유와 비디오 베일 내보내기는 백그라운드에서 잠시 이어질 수 있습니다. 라이브 액티비티는 잠금 화면에 작업 이름과 진행률을 표시할 수 있습니다. 이미지 내용은 표시하지 않습니다.

## 어린이

콘텐츠는 기기에서 처리되고 데이터를 수집하는 백엔드가 없으므로, iVeil은 어린이를 포함한 누구의 개인 데이터도 고의로 수집하지 않습니다.

## 고지

iVeil은 독립 앱이며 **Apple Inc.와 제휴하지 않습니다.** 자동 인식은 첫 단계일 뿐 보장이 아닙니다. 공유하기 전에 사진을 한 번 더 확인해 주세요.

## 변경

처리 방식이 바뀌면 이 페이지를 업데이트하고 위 날짜를 고칩니다.

## 연락처

- **이메일:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ru" markdown="1">

iHTC Studio («мы»; ранее iHTCTeam) разрабатывает **iVeil** (爱修图 / 愛修圖; ранние версии назывались iPhoto). Эта политика объясняет, что происходит с вашими данными, когда вы пользуетесь приложением, его расширением «Поделиться», расширением редактирования «Фото», виджетами, элементами Пункта управления и камерой на экране блокировки.

*Обновлено: 18 октября 2026 г.*

## Кратко

- **Нет аккаунта, рекламы, аналитики и слежения.** В iVeil нет сторонних SDK аналитики, рекламы или отслеживания.
- **Ваши фото и видео не покидают устройство через iVeil.** Распознавание, правка и экспорт выполняются на устройстве. У нас нет серверов, которые принимают ваш контент.
- **Вы решаете, чем делиться.** iVeil создаёт новые копии. Оригиналы в «Фото» меняются только если вы сохраните правку расширением редактирования «Фото», и эту правку можно отменить в «Фото».

## Какие данные iVeil обрабатывает на устройстве

| Данные | Зачем | Что сохраняется |
|------|-----|--------------|
| Фото и видео, которые вы выбираете («Фото», меню «Поделиться», «Файлы» или камера) | Проверить, скрыть и отредактировать | Хранятся в песочнице приложения, пока вы их не удалите. Фото из расширения «Поделиться» ненадолго проходят через контейнер App Group и затем переносятся в приложение. |
| Лица и люди (Apple Vision) | Найти и скрыть лица, оставить выбранных людей, наклонить эмодзи-вуаль вместе с головой, вырезать оставленного человека и по желанию ретушировать портрет | С проектом сохраняются только прямоугольники или контуры, нужные чтобы заново нарисовать скрытие. Ориентиры лица остаются только в памяти. |
| Текст на изображениях (распознавание текста Vision и детекторы данных Apple) | Найти телефоны, почту, адреса, номера карт и документов, машиночитаемые строки паспорта, номера заказов, идентификаторы аккаунтов и ссылки | Сохраняются только область и тип. Сам распознанный текст не сохраняется. |
| QR-коды и штрихкоды | Скрыть их и через «Что внутри кода» показать, какого рода сведения там лежат | Сохраняются только категория и имена полей (например, «посадочный: место»), содержимое — никогда. |
| Сведения о файле (место, время съёмки, камера, объектив, серийные номера) | Показать, что выдаёт файл, и убрать это из копий, которыми вы делитесь | Читаются из вашего файла. В копии остаётся только то, что вы выбрали; серийные номера и имена владельцев удаляются всегда. |
| Возможно деликатные изображения (анализ деликатного контента Apple) | Размыть наготу или шокирующие кадры перед отправкой, только если в Настройках включены предупреждение о деликатном контенте или безопасность общения | Анализ идёт на устройстве внутри фреймворка Apple. Результаты не хранятся и не отправляются. |
| Apple Intelligence (необязательно, iOS 26) | «Посмотреть ещё раз с Apple Intelligence» и «Описать образ» | Работает на модели Apple на устройстве. Ей передаются только распознанные строки текста и их число или введённое вами предложение, но не изображения и не данные лица. |
| Невидимая метка (необязательно) | Позже проверить, кому вы отправили фото | 32-битный код прячется в яркости изображения. Имена получателей, которые вы вводите, хранятся в списке на устройстве (до 500 записей). Его можно править или очистить в Настройки → Невидимая метка. |
| Вырезки и вуали Genmoji | Снова использовать вырезанных людей и свои эмодзи | Сохраняются как изображения в контейнере App Group на устройстве, пока вы их не удалите. |
| Недавно удалённые | Отменить удаление | Удалённые проекты хранятся 30 дней, затем удаляются навсегда. |
| Настройки | Язык, оформление, параметры съёмки и экспорта | Хранятся в контейнере App Group на устройстве. |

## Данные лица

iVeil использует фреймворк Vision от Apple на вашем устройстве, чтобы **находить** лица и людей. Это **не** распознавание лиц: iVeil не определяет, кто это, не сравнивает лица и не создаёт биометрические шаблоны.

- **Использование:** скрытие лиц, сохранение выбранных людей, выравнивание эмодзи-вуалей, вырезание оставленного человека и необязательная ретушь портрета.
- **Хранение:** нормализованные прямоугольники лиц, контуры людей и параметры ретуши сохраняются внутри проекта в песочнице приложения. Полные ориентиры лица никогда не записываются на диск.
- **Передача:** данные лица не загружаются, не передаются нам или третьим лицам и не синхронизируются с iCloud.
- **Срок:** данные лица живут только вместе с проектом. Удаление проекта (через 30 дней в «Недавно удалённых») или удаление приложения их стирает.

## Сеть

У iVeil нет собственных серверов. Сетевые запросы идут только к службам Apple:

- **Карты.** Если у фото есть место, iVeil показывает его на карте Apple, которая загружает тайлы этой области у Apple. Если выбрать **Квартал**, название места запрашивается у Apple по центру ячейки сетки около 5 км, а не по точным координатам. Содержимое изображения не отправляется. Apple обрабатывает эти запросы по [политике конфиденциальности Apple](https://www.apple.com/legal/privacy/).
- **Необязательная поддержка.** «Поддержать разработчика» — расходуемая покупка в приложении, которую Apple проводит через StoreKit. Она ничего не открывает, и мы не получаем личных сведений.
- **Необязательная синхронизация iCloud (выключена по умолчанию).** Если её включить, несколько настроек (язык, оформление, параметры съёмки или экспорта) синхронизируются через ваше личное хранилище «ключ-значение» iCloud. Фото, видео, данные лица и список невидимых меток никогда не синхронизируются.

## Разрешения

| Разрешение | Назначение |
|------------|---------|
| Фото | Открывать выбранные фото и показывать место и данные камеры |
| Фото (только добавление) | Сохранять экспортированные копии |
| Камера | Вкладка съёмки, живая вуаль и камера-вуаль на экране блокировки |

iVeil не запрашивает доступ к микрофону, геопозиции, контактам или отслеживанию. Видео-вуаль использует звук, уже записанный в выбранном видео, и может его убрать.

## Фоновая работа и Live Activity

Пакетная безопасная отправка и экспорт видео-вуали, которые **запускаете вы**, могут недолго продолжаться в фоне. Live Activity может показать название задачи и ход на экране блокировки. Содержимое изображения она не показывает.

## Дети

iVeil сознательно не собирает личные данные ни у кого, включая детей, потому что контент обрабатывается на устройстве, а сервера сбора данных у нас нет.

## Оговорка

iVeil — независимое приложение и **не связано с Apple Inc.** Автоматическое распознавание — первый проход, а не гарантия. Посмотрите фото ещё раз перед отправкой.

## Изменения

Если наши правила изменятся, мы обновим эту страницу и дату выше.

## Контакт

- **Почта:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="th" markdown="1">

iHTC Studio («เรา» เดิมชื่อ iHTCTeam) พัฒนา **iVeil** (爱修图 / 愛修圖 เวอร์ชันแรกใช้ชื่อ iPhoto) นโยบายนี้อธิบายว่าข้อมูลของคุณถูกจัดการอย่างไรเมื่อใช้แอป ส่วนขยายการแชร์ ส่วนขยายแก้ไขของ «รูปภาพ» วิดเจ็ต ตัวควบคุมในศูนย์ควบคุม และกล้องบนหน้าจอล็อก

*อัปเดตล่าสุด: 18 ตุลาคม 2026*

## สรุป

- **ไม่มีบัญชี ไม่มีโฆษณา ไม่มีการวิเคราะห์ ไม่มีการติดตาม** iVeil ไม่มี SDK ของบุคคลที่สามสำหรับการวิเคราะห์ โฆษณา หรือการติดตาม
- **รูปและวิดีโอของคุณไม่หลุดออกจากเครื่องผ่าน iVeil** การตรวจ การแต่ง และการส่งออกทำงานบนเครื่อง เราไม่มีเซิร์ฟเวอร์ที่รับเนื้อหาของคุณ
- **คุณเป็นคนตัดสินใจว่าจะแชร์อะไร** iVeil สร้างสำเนาใหม่เท่านั้น ต้นฉบับใน «รูปภาพ» จะเปลี่ยนก็ต่อเมื่อคุณบันทึกการแต่งด้วยส่วนขยายแก้ไขของ «รูปภาพ» และการแต่งนั้นย้อนกลับได้ใน «รูปภาพ»

## ข้อมูลที่ iVeil ประมวลผลบนเครื่อง

| ข้อมูล | เหตุผล | สิ่งที่เก็บไว้ |
|------|-----|--------------|
| รูปและวิดีโอที่คุณเลือก («รูปภาพ» เมนูแชร์ «ไฟล์» หรือกล้อง) | เพื่อตรวจ ซ่อน และแต่ง | เก็บในแซนด์บ็อกซ์ของแอปจนกว่าคุณจะลบ รูปที่ส่งมาจากส่วนขยายการแชร์จะผ่านคอนเทนเนอร์ App Group ชั่วครู่ แล้วถูกย้ายเข้าแอป |
| ใบหน้าและบุคคล (Apple Vision) | หาและซ่อนใบหน้า เก็บคนที่คุณเลือกให้เอียงม่านอีโมจิตามศีรษะ ตัดคนที่เก็บไว้ และรีทัชภาพบุคคลหากต้องการ | เก็บเฉพาะสี่เหลี่ยมหรือเส้นขอบที่ต้องใช้วาดส่วนที่ซ่อนใหม่ไว้กับโปรเจกต์ จุดแลนด์มาร์กใบหน้าอยู่ในหน่วยความจำเท่านั้น |
| ข้อความในภาพ (การรู้จำข้อความของ Vision และตัวตรวจข้อมูลของ Apple) | หาเบอร์โทร อีเมล ที่อยู่ หมายเลขบัตรและบัตรประจำตัว บรรทัดเครื่องอ่านพาสปอร์ต เลขคำสั่งซื้อ รหัสบัญชี และลิงก์ | เก็บเฉพาะบริเวณและประเภท ไม่เก็บตัวอักษรที่รู้จำได้ |
| คิวอาร์โค้ดและบาร์โค้ด | ซ่อน และใช้ «โค้ดซ่อนอะไร» บอกว่าข้างในเป็นข้อมูลประเภทใด | เก็บเฉพาะหมวดและชื่อช่อง (เช่น «บอร์ดดิ้งพาส: ที่นั่ง») ไม่เก็บเนื้อหา |
| รายละเอียดไฟล์ (ตำแหน่ง เวลาถ่าย กล้อง เลนส์ หมายเลขซีเรียล) | แสดงว่าไฟล์เปิดเผยอะไร และเอาออกจากสำเนาที่คุณแชร์ | อ่านจากไฟล์ของคุณ สำเนาเก็บเฉพาะสิ่งที่คุณเลือก หมายเลขซีเรียลและชื่อเจ้าของถูกเอาออกเสมอ |
| ภาพที่อาจละเอียดอ่อน (การวิเคราะห์เนื้อหาละเอียดอ่อนของ Apple) | เบลอภาพเปลือยหรือภาพรุนแรงก่อนแชร์ เฉพาะเมื่อคุณเปิดคำเตือนเนื้อหาละเอียดอ่อนหรือความปลอดภัยในการสื่อสารในการตั้งค่า | วิเคราะห์บนเครื่องภายในเฟรมเวิร์กของ Apple ไม่เก็บและไม่ส่งผลลัพธ์ |
| Apple Intelligence (ไม่บังคับ, iOS 26) | «ให้ Apple Intelligence ดูอีกครั้ง» และ «อธิบายลุค» | ทำงานบนโมเดลบนเครื่องของ Apple รับเฉพาะบรรทัดข้อความที่รู้จำได้พร้อมจำนวน หรือประโยคที่คุณพิมพ์ ไม่รับภาพหรือข้อมูลใบหน้า |
| เครื่องหมายล่องหน (ไม่บังคับ) | ใช้ตรวจภายหลังว่ารูปส่งให้ใคร | ซ่อนรหัส 32 บิตไว้ในความสว่างของภาพ ชื่อผู้รับที่คุณกรอกอยู่ในรายการบนเครื่อง (สูงสุด 500 รายการ) แก้ไขหรือล้างได้ที่ การตั้งค่า → เครื่องหมายล่องหน |
| ภาพตัดและม่าน Genmoji | ใช้คนที่ตัดออกและอีโมจิที่กำหนดเองซ้ำ | บันทึกเป็นภาพในคอนเทนเนอร์ App Group บนเครื่องจนกว่าคุณจะเอาออก |
| ลบล่าสุด | เลิกทำการลบ | โปรเจกต์ที่ลบจะอยู่ 30 วัน แล้วถูกลบถาวร |
| ค่ากำหนด | ภาษา ลักษณะ ตัวเลือกการถ่ายและการส่งออก | เก็บในคอนเทนเนอร์ App Group บนเครื่อง |

## ข้อมูลใบหน้า

iVeil ใช้เฟรมเวิร์ก Vision ของ Apple บนเครื่องเพื่อ**ระบุตำแหน่ง**ใบหน้าและบุคคล นี่**ไม่ใช่**การรู้จำใบหน้า: iVeil ไม่ระบุว่าเป็นใคร ไม่เปรียบเทียบใบหน้า และไม่สร้างเทมเพลตชีวมาตร

- **การใช้:** ซ่อนใบหน้า เก็บคนที่คุณเลือก จัดม่านอีโมจิ ตัดคนที่เก็บไว้ และรีทัชภาพบุคคลหากต้องการ
- **การเก็บ:** สี่เหลี่ยมใบหน้าที่ปรับให้เป็นมาตรฐาน เส้นขอบบุคคล และการตั้งค่ารีทัชถูกบันทึกในโปรเจกต์ภายในแซนด์บ็อกซ์ จุดแลนด์มาร์กใบหน้าแบบเต็มไม่ถูกเขียนลงดิสก์
- **การแชร์:** ข้อมูลใบหน้าไม่ถูกอัปโหลด ไม่ถูกส่งให้เราหรือบุคคลที่สาม และไม่ซิงค์ไป iCloud
- **ระยะเวลา:** ข้อมูลใบหน้าอยู่เท่าที่โปรเจกต์ยังอยู่ การลบโปรเจกต์ (หลังอยู่ใน «ลบล่าสุด» 30 วัน) หรือการถอนการติดตั้งแอปจะลบข้อมูลนี้

## การใช้เครือข่าย

iVeil ไม่มีเซิร์ฟเวอร์ของตัวเอง คำขอเครือข่ายมาจากบริการของ Apple เท่านั้น:

- **แผนที่** เมื่อรูปมีตำแหน่ง iVeil แสดงบนแผนที่ Apple ซึ่งโหลดแผ่นแผนที่ของบริเวณนั้นจาก Apple เมื่อเลือก**ตำแหน่งโดยประมาณ** ชื่อสถานที่จะถูกถามจาก Apple โดยใช้จุดกึ่งกลางของช่องกริดราว 5 กม. ไม่ใช่พิกัดที่แน่นอน ไม่มีการส่งเนื้อหาภาพ Apple จัดการคำขอเหล่านี้ตาม [นโยบายความเป็นส่วนตัวของ Apple](https://www.apple.com/legal/privacy/)
- **ทิปที่ไม่บังคับ** «ให้ทิปนักพัฒนา» คือการซื้อในแอปแบบใช้แล้วหมดซึ่ง Apple ประมวลผลผ่าน StoreKit ไม่ปลดล็อกฟีเจอร์ใด และเราไม่ได้รับข้อมูลส่วนบุคคล
- **การซิงค์ iCloud ที่ไม่บังคับ (ปิดไว้เป็นค่าเริ่มต้น)** เมื่อเปิด ค่ากำหนดไม่กี่อย่าง (เช่น ภาษา ลักษณะ และตัวเลือกการถ่ายหรือส่งออก) จะซิงค์ผ่านที่เก็บคีย์-ค่า iCloud ส่วนตัวของคุณ รูป วิดีโอ ข้อมูลใบหน้า และรายการเครื่องหมายล่องหนไม่ถูกซิงค์

## สิทธิ์

| สิทธิ์ | วัตถุประสงค์ |
|------------|---------|
| รูปภาพ | เปิดรูปที่คุณเลือก และแสดงตำแหน่งกับรายละเอียดกล้อง |
| รูปภาพ (เพิ่มอย่างเดียว) | บันทึกสำเนาที่ส่งออก |
| กล้อง | แท็บถ่ายภาพ ม่านสด และกล้องม่านบนหน้าจอล็อก |

iVeil ไม่ขอสิทธิ์ไมโครโฟน ตำแหน่ง รายชื่อ หรือการติดตาม ม่านวิดีโอใช้เสียงที่มีอยู่ในวิดีโอที่คุณเลือก และสามารถเอาเสียงออกได้

## งานเบื้องหลังและ Live Activity

การแชร์อย่างปลอดภัยเป็นชุดและการส่งออกม่านวิดีโอที่**คุณเป็นคนเริ่ม**อาจทำงานต่อในเบื้องหลังชั่วครู่ Live Activity แสดงชื่องานและความคืบหน้าบนหน้าจอล็อกได้ และไม่แสดงเนื้อหาภาพ

## เด็ก

iVeil ไม่เก็บข้อมูลส่วนบุคคลของใครโดยเจตนา รวมถึงเด็ก เพราะเนื้อหาถูกประมวลผลบนเครื่อง และเราไม่มีระบบหลังบ้านสำหรับเก็บข้อมูล

## ข้อสงวน

iVeil เป็นแอปอิสระ และ**ไม่มีส่วนเกี่ยวข้องกับ Apple Inc.** การตรวจอัตโนมัติเป็นด่านแรก ไม่ใช่การรับประกัน โปรดตรวจรูปอีกครั้งก่อนแชร์

## การเปลี่ยนแปลง

หากวิธีปฏิบัติของเราเปลี่ยน เราจะอัปเดตหน้านี้และแก้ไขวันที่ด้านบน

## ติดต่อ

- **อีเมล:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="de" markdown="1">

iHTC Studio („wir“; früher iHTCTeam) entwickelt **iVeil** (爱修图 / 愛修圖; frühere Versionen hießen iPhoto). Diese Richtlinie erklärt, was mit Ihren Daten geschieht, wenn Sie die App und ihre Teilen-Erweiterung, die Fotos-Bearbeitungserweiterung, Widgets, Kontrollzentrum-Steuerungen und die Kamera auf dem Sperrbildschirm verwenden.

*Zuletzt aktualisiert: 18. Oktober 2026*

## Kurzfassung

- **Kein Account, keine Werbung, keine Analyse, kein Tracking.** iVeil enthält keine SDKs von Drittanbietern für Analyse, Werbung oder Tracking.
- **Ihre Fotos und Videos verlassen Ihr Gerät über iVeil nicht.** Erkennung, Bearbeitung und Export laufen auf dem Gerät. Wir betreiben keine Server, die Ihre Inhalte empfangen.
- **Sie entscheiden, was geteilt wird.** iVeil erzeugt neue Kopien. Originale in Fotos ändern sich nur, wenn Sie eine Bearbeitung mit der Fotos-Bearbeitungserweiterung sichern, und diese Bearbeitung lässt sich in Fotos zurücksetzen.

## Welche Daten iVeil auf Ihrem Gerät verarbeitet

| Daten | Zweck | Was bleibt |
|------|-----|--------------|
| Fotos und Videos, die Sie auswählen (Fotos, das Teilen-Menü, Dateien oder die Kamera) | Zum Prüfen, Verbergen und Bearbeiten | Im App-Sandbox gespeichert, bis Sie sie löschen. Fotos aus der Teilen-Erweiterung durchlaufen kurz den App-Group-Container und werden dann in die App verschoben. |
| Gesichter und Personen (Apple Vision) | Gesichter finden und verbergen, gewählte Personen behalten, einen Emoji-Schleier an die Kopfneigung anpassen, eine behaltene Person freistellen und optional ein Porträt retuschieren | Rechtecke oder Umrisse, die zum erneuten Zeichnen Ihrer Abdeckungen nötig sind, werden mit dem Projekt gespeichert. Gesichtsmerkmale bleiben nur im Arbeitsspeicher. |
| Text in Bildern (Vision-Texterkennung und Apple-Datendetektoren) | Telefonnummern, E-Mails, Adressen, Karten- und Ausweisnummern, Passzeilen, Bestellnummern, Konto-IDs und Links finden | Gespeichert werden nur Bereich und Art. Der erkannte Text selbst wird nicht gespeichert. |
| QR-Codes und Strichcodes | Sie verbergen und mit „Was im Code steckt“ anzeigen, welche Art von Information sie enthalten | Nur Kategorie und Feldnamen (zum Beispiel „Bordkarte: Sitz“) werden gespeichert, niemals der Inhalt. |
| Dateidetails (Ort, Aufnahmezeit, Kamera, Objektiv, Seriennummern) | Zeigen, was eine Datei verrät, und es aus den Kopien entfernen, die Sie teilen | Aus Ihrer Datei gelesen. Kopien behalten nur, was Sie auswählen; Seriennummern und Besitzernamen werden immer entfernt. |
| Möglicherweise sensible Bilder (Apple Sensitive Content Analysis) | Nacktheit oder drastische Inhalte vor dem Teilen weichzeichnen, nur wenn Sie in den Einstellungen die Warnung zu sensiblen Inhalten oder die Kommunikationssicherheit aktiviert haben | Die Analyse läuft auf dem Gerät innerhalb von Apples Framework. Ergebnisse werden weder gespeichert noch gesendet. |
| Apple Intelligence (optional, iOS 26) | „Mit Apple Intelligence erneut prüfen“ und „Einen Look beschreiben“ | Läuft auf Apples On-Device-Modell. Es erhält nur erkannte Textzeilen und Anzahlen oder den Satz, den Sie eingeben, niemals Bilder oder Gesichtsdaten. |
| Unsichtbare Markierung (optional) | Später nachsehen, an wen Sie ein Foto gesendet haben | Ein 32-Bit-Code wird in der Bildhelligkeit verborgen. Die Empfängernamen, die Sie eingeben, bleiben in einer Liste auf Ihrem Gerät (bis zu 500 Einträge), die Sie unter Einstellungen → Unsichtbare Markierung bearbeiten oder leeren können. |
| Freistellungen und Genmoji-Schleier | Ausgeschnittene Personen und eigene Emoji erneut verwenden | Als Bilder im App-Group-Container auf Ihrem Gerät gespeichert, bis Sie sie entfernen. |
| Zuletzt gelöscht | Eine Löschung rückgängig machen | Gelöschte Projekte bleiben 30 Tage und werden danach dauerhaft entfernt. |
| Einstellungen | Sprache, Erscheinungsbild, Aufnahme- und Exportoptionen | Im App-Group-Container auf Ihrem Gerät gespeichert. |

## Gesichtsdaten

iVeil nutzt Apples Vision-Framework auf Ihrem Gerät, um Gesichter und Personen zu **lokalisieren**. Das ist **keine** Gesichtserkennung: iVeil erkennt nicht, wer jemand ist, vergleicht keine Gesichter und erstellt keine biometrischen Vorlagen.

- **Verwendung:** Gesichter verbergen, die Personen behalten, die Sie auswählen, Emoji-Schleier ausrichten, eine behaltene Person freistellen und optional ein Porträt retuschieren.
- **Speicherung:** Normalisierte Gesichtsrechtecke, Personenkonturen und Ihre Retusche-Einstellungen werden im Projekt in der App-Sandbox gespeichert. Vollständige Gesichtsmerkmale werden nie auf die Festplatte geschrieben.
- **Weitergabe:** Gesichtsdaten werden nie hochgeladen, nie an uns oder Dritte weitergegeben und nicht mit iCloud synchronisiert.
- **Aufbewahrung:** Gesichtsdaten bleiben nur so lange wie das Projekt. Das Löschen eines Projekts (nach 30 Tagen in Zuletzt gelöscht) oder das Entfernen der App löscht sie.

## Netzwerk

iVeil hat keine eigenen Server. Die einzigen Netzwerkanfragen stammen von Apple-Diensten:

- **Karten.** Hat ein Foto einen Ort, zeigt iVeil ihn auf einer Apple-Karte, die Kartenkacheln für dieses Gebiet von Apple lädt. Bei **Straßenblock** wird der Ortsname bei Apple anhand der Mitte einer etwa 5 km großen Rasterzelle abgefragt, nicht anhand der genauen Koordinaten. Es werden keine Bildinhalte gesendet. Apple verarbeitet diese Anfragen gemäß [Apples Datenschutzrichtlinie](https://www.apple.com/de/legal/privacy/).
- **Optionales Trinkgeld.** „Entwickler unterstützen“ ist ein Verbrauchskauf in der App, den Apple über StoreKit abwickelt. Er schaltet nichts frei, und wir erhalten keine persönlichen Daten.
- **Optionale iCloud-Synchronisierung (standardmäßig aus).** Wenn Sie sie einschalten, werden wenige Einstellungen (etwa Sprache, Erscheinungsbild und Aufnahme- oder Exportoptionen) über Ihren privaten iCloud-Schlüsselwertspeicher synchronisiert. Fotos, Videos, Gesichtsdaten und die Liste der unsichtbaren Markierung werden nie synchronisiert.

## Berechtigungen

| Berechtigung | Zweck |
|------------|---------|
| Fotos | Die ausgewählten Fotos öffnen und Ort sowie Kameradaten anzeigen |
| Fotos (nur hinzufügen) | Die exportierten Kopien sichern |
| Kamera | Aufnahmetab, Live-Schleier und die Schleier-Kamera auf dem Sperrbildschirm |

iVeil fordert keine Berechtigung für Mikrofon, Ort, Kontakte oder Tracking an. Der Video-Schleier verwendet den Ton, der bereits im ausgewählten Video enthalten ist, und kann ihn entfernen.

## Hintergrundarbeit und Live Activities

Stapel von Sicher teilen und Exporte des Video-Schleiers, die **Sie starten**, können kurz im Hintergrund weiterlaufen. Eine Live Activity kann Titel und Fortschritt auf dem Sperrbildschirm anzeigen. Sie zeigt niemals Bildinhalte.

## Kinder

iVeil erhebt wissentlich keine personenbezogenen Daten von irgendjemandem, auch nicht von Kindern, weil Inhalte auf dem Gerät verarbeitet werden und wir kein Backend zur Datenerhebung betreiben.

## Hinweis

iVeil ist eine unabhängige App und **nicht mit Apple Inc. verbunden.** Die automatische Erkennung ist ein erster Durchgang, keine Garantie. Bitte prüfen Sie ein Foto, bevor Sie es teilen.

## Änderungen

Wenn sich unsere Praxis ändert, aktualisieren wir diese Seite und das Datum oben.

## Kontakt

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="fr" markdown="1">

iHTC Studio (« nous » ; anciennement iHTCTeam) développe **iVeil** (爱修图 / 愛修圖 ; les versions antérieures s’appelaient iPhoto). Cette politique explique ce qu’il advient de vos données lorsque vous utilisez l’app, son extension de partage, l’extension de retouche Photos, les widgets, les commandes du Centre de contrôle et l’appareil photo de l’écran verrouillé.

*Dernière mise à jour : 18 octobre 2026*

## En bref

- **Pas de compte, pas de publicité, pas d’analyse, pas de suivi.** iVeil ne contient aucun SDK tiers d’analyse, de publicité ou de suivi.
- **Vos photos et vidéos ne quittent jamais votre appareil par iVeil.** La détection, la retouche et l’exportation s’exécutent sur l’appareil. Nous n’exploitons aucun serveur qui reçoit vos contenus.
- **Vous décidez de ce qui est partagé.** iVeil crée de nouvelles copies. Vos originaux dans Photos ne changent que si vous enregistrez une retouche avec l’extension de retouche Photos, et cette retouche peut être annulée dans Photos.

## Ce qu’iVeil traite sur votre appareil

| Données | Pourquoi | Ce qui est conservé |
|------|-----|--------------|
| Photos et vidéos que vous choisissez (Photos, le menu Partager, Fichiers ou l’appareil) | Pour les vérifier, les masquer et les retoucher | Stockées dans le bac à sable de l’app jusqu’à ce que vous les supprimiez. Les photos transmises par l’extension de partage passent brièvement par le conteneur App Group, puis sont déplacées dans l’app. |
| Visages et personnes (Apple Vision) | Trouver et masquer des visages, garder les personnes choisies, incliner un voile emoji avec la tête, détourer une personne gardée, et retouche de portrait facultative | Les rectangles ou contours nécessaires pour redessiner vos masques sont enregistrés avec le projet. Les points du visage restent uniquement en mémoire. |
| Texte dans les images (reconnaissance de texte Vision et détecteurs de données Apple) | Trouver numéros de téléphone, e-mails, adresses, numéros de carte et de pièce d’identité, lignes de passeport, numéros de commande, identifiants de compte et liens | Seuls la zone et le type sont enregistrés. Le texte reconnu lui-même n’est pas enregistré. |
| Codes QR et codes-barres | Les masquer et, avec « Ce que cache le code », indiquer quel type d’information ils contiennent | Seuls la catégorie et les noms de champs (par exemple « carte d’embarquement : siège ») sont enregistrés, jamais le contenu. |
| Détails du fichier (lieu, date de prise de vue, appareil, objectif, numéros de série) | Montrer ce qu’un fichier révèle et le retirer des copies que vous partagez | Lus dans votre fichier. Les copies ne gardent que ce que vous choisissez ; les numéros de série et les noms de propriétaire sont toujours retirés. |
| Images potentiellement sensibles (analyse de contenu sensible d’Apple) | Flouter la nudité ou un contenu choquant avant le partage, seulement si vous avez activé l’avertissement de contenu sensible ou la sécurité des communications dans Réglages | L’analyse s’exécute sur l’appareil, dans le cadre d’Apple. Les résultats ne sont ni stockés ni envoyés. |
| Apple Intelligence (facultatif, iOS 26) | « Regarder à nouveau avec Apple Intelligence » et « Décrire un look » | S’exécute sur le modèle d’Apple sur l’appareil. Il ne reçoit que les lignes de texte reconnues et leur nombre, ou la phrase que vous saisissez, jamais d’images ni de données de visage. |
| Marque invisible (facultatif) | Vérifier plus tard à qui vous avez envoyé une photo | Un code de 32 bits est caché dans la luminosité de l’image. Les noms de destinataires que vous saisissez restent dans une liste sur votre appareil (jusqu’à 500 entrées), que vous pouvez modifier ou effacer dans Réglages → Marque invisible. |
| Détourages et voiles Genmoji | Réutiliser les personnes détourées et les emoji personnalisés | Enregistrés comme images dans le conteneur App Group de votre appareil jusqu’à ce que vous les retiriez. |
| Récemment supprimés | Annuler une suppression | Les projets supprimés sont conservés 30 jours, puis retirés définitivement. |
| Préférences | Langue, apparence, options de capture et d’exportation | Stockées dans le conteneur App Group de votre appareil. |

## Données de visage

iVeil utilise le cadre Vision d’Apple sur votre appareil pour **localiser** les visages et les personnes. Ce n’est **pas** de la reconnaissance faciale : iVeil n’identifie personne, ne compare pas les visages et ne crée pas de modèles biométriques.

- **Usage :** masquer des visages, garder les personnes que vous choisissez, aligner les voiles emoji, détourer une personne gardée et retouche de portrait facultative.
- **Stockage :** les rectangles de visage normalisés, les contours de personne et vos réglages de retouche sont enregistrés dans le projet, dans le bac à sable de l’app. Les points complets du visage ne sont jamais écrits sur le disque.
- **Partage :** les données de visage ne sont jamais téléversées, jamais transmises à nous ni à un tiers, et ne sont pas synchronisées avec iCloud.
- **Conservation :** les données de visage ne durent que le temps du projet. Supprimer un projet (après 30 jours dans Récemment supprimés) ou désinstaller l’app les retire.

## Utilisation du réseau

iVeil n’a pas de serveurs propres. Les seules requêtes réseau viennent des services Apple :

- **Plans.** Lorsqu’une photo a un lieu, iVeil l’affiche sur un plan Apple Plans, qui charge auprès d’Apple les tuiles de cette zone. Si vous choisissez **Pâté de maisons**, le nom du lieu est demandé à Apple à partir du centre d’une cellule d’environ 5 km, et non des coordonnées exactes. Aucun contenu d’image n’est envoyé. Apple traite ces requêtes selon la [politique de confidentialité d’Apple](https://www.apple.com/fr/legal/privacy/).
- **Pourboire facultatif.** « Pourboire au développeur » est un achat intégré consommable traité par Apple via StoreKit. Il ne débloque rien, et nous ne recevons aucune information personnelle.
- **Synchronisation iCloud facultative (désactivée par défaut).** Lorsque vous l’activez, quelques préférences (langue, apparence, options de capture ou d’exportation) se synchronisent via votre propre stockage clé-valeur iCloud. Les photos, les vidéos, les données de visage et la liste de la marque invisible ne sont jamais synchronisées.

## Autorisations

| Autorisation | Objet |
|------------|---------|
| Photos | Ouvrir les photos choisies et afficher leur lieu et les détails de l’appareil |
| Photos (ajout uniquement) | Enregistrer les copies exportées |
| Appareil photo | Onglet Capture, Voile en direct et l’appareil à voile sur l’écran verrouillé |

iVeil ne demande pas l’autorisation du microphone, du lieu, des contacts ni du suivi. Le voile vidéo utilise le son déjà présent dans la vidéo choisie et peut le retirer.

## Travail en arrière-plan et Live Activities

Les partages sûrs groupés et les exportations de voile vidéo que **vous lancez** peuvent se poursuivre brièvement en arrière-plan. Une Live Activity peut afficher le titre de la tâche et sa progression sur l’écran verrouillé. Elle ne montre jamais le contenu de l’image.

## Enfants

iVeil ne collecte sciemment aucune donnée personnelle de quiconque, y compris des enfants, parce que le contenu est traité sur l’appareil et que nous n’avons pas de serveur de collecte.

## Avertissement

iVeil est une app indépendante et **n’est pas affiliée à Apple Inc.** La détection automatique est une première passe, pas une garantie. Veuillez relire une photo avant de la partager.

## Modifications

Si nos pratiques changent, nous mettrons cette page à jour et réviserons la date ci-dessus.

## Contact

- **E-mail :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="tr" markdown="1">

iHTC Studio («biz»; eski adı iHTCTeam) **iVeil** uygulamasını geliştirir (爱修图 / 愛修圖; önceki sürümler iPhoto adını taşıyordu). Bu politika, uygulamayı ve Paylaş uzantısını, Fotoğraflar düzenleme uzantısını, widget’ları, Denetim Merkezi denetimlerini ve Kilit Ekranı kamerasını kullandığınızda verilerinize ne olduğunu açıklar.

*Son güncelleme: 18 Ekim 2026*

## Özet

- **Hesap yok, reklam yok, analiz yok, izleme yok.** iVeil’de üçüncü taraf analiz, reklam veya izleme SDK’sı yoktur.
- **Fotoğraflarınız ve videolarınız iVeil üzerinden cihazınızdan çıkmaz.** Algılama, düzenleme ve dışa aktarma cihazınızda çalışır. İçeriğinizi alan sunucularımız yoktur.
- **Neyin paylaşılacağına siz karar verirsiniz.** iVeil yeni kopyalar oluşturur. Fotoğraflar’daki özgünleriniz yalnızca Fotoğraflar düzenleme uzantısıyla bir düzenlemeyi kaydettiğinizde değişir ve bu düzenleme Fotoğraflar’da geri alınabilir.

## iVeil’in cihazınızda işlediği veriler

| Veri | Neden | Ne saklanır |
|------|-----|--------------|
| Seçtiğiniz fotoğraflar ve videolar (Fotoğraflar, Paylaş menüsü, Dosyalar veya kamera) | Kontrol etmek, gizlemek ve düzenlemek için | Siz silene kadar uygulama kum havuzunda saklanır. Paylaş uzantısından gelen fotoğraflar kısa süre App Group kabından geçer, sonra uygulamaya taşınır. |
| Yüzler ve kişiler (Apple Vision) | Yüzleri bulup gizlemek, seçtiğiniz kişileri tutmak, emoji örtüsünü başın eğimine uydurmak, tuttuğunuz kişiyi kesmek ve isteğe bağlı portre rötuşu | Gizlemelerinizi yeniden çizmek için gereken dikdörtgenler veya dış çizgiler projeyle birlikte saklanır. Yüz işaret noktaları yalnızca bellekte kalır. |
| Görüntülerdeki metin (Vision metin tanıma ve Apple veri algılayıcıları) | Telefon numaralarını, e-postaları, adresleri, kart ve kimlik numaralarını, pasaport satırlarını, sipariş numaralarını, hesap kimliklerini ve bağlantıları bulmak için | Yalnızca alan ve tür saklanır. Tanınan metnin kendisi saklanmaz. |
| QR kodları ve barkodlar | Onları gizlemek ve «Kodun içinde ne var» ile ne tür bilgi taşıdıklarını söylemek için | Yalnızca kategori ve alan adları saklanır (örneğin «biniş kartı: koltuk»), içerik asla saklanmaz. |
| Dosya ayrıntıları (konum, çekim zamanı, kamera, lens, seri numaraları) | Bir dosyanın ne açığa çıkardığını göstermek ve paylaştığınız kopyalardan kaldırmak için | Dosyanızdan okunur. Kopyalar yalnızca sizin seçtiklerinizi tutar; seri numaraları ve sahip adları her zaman kaldırılır. |
| Hassas olabilecek görüntüler (Apple Hassas İçerik Analizi) | Ayarlar’da Hassas İçerik Uyarısı veya İletişim Güvenliği açıksa, paylaşmadan önce çıplaklığı veya rahatsız edici içeriği bulandırmak için | Analiz, Apple’ın çerçevesi içinde cihazda çalışır. Sonuçlar saklanmaz ve gönderilmez. |
| Apple Intelligence (isteğe bağlı, iOS 26) | «Apple Intelligence ile yeniden bak» ve «Bir görünümü tanımla» | Apple’ın cihazdaki modelinde çalışır. Yalnızca tanınan metin satırlarını ve sayılarını ya da yazdığınız cümleyi alır; görüntü veya yüz verisi almaz. |
| Görünmez İşaret (isteğe bağlı) | Bir fotoğrafı daha sonra kime gönderdiğinizi kontrol etmek için | 32 bitlik bir kod görüntünün parlaklığına gizlenir. Girdiğiniz alıcı adları cihazınızdaki bir listede kalır (en fazla 500 kayıt). Ayarlar → Görünmez İşaret bölümünden düzenlenebilir veya temizlenebilir. |
| Kesmeler ve Genmoji örtüleri | Kesilen kişileri ve özel emojiyi yeniden kullanmak için | Siz kaldırana kadar cihazınızdaki App Group kabında görüntü olarak saklanır. |
| Son Silinenler | Bir silmeyi geri almak için | Silinen projeler 30 gün tutulur, sonra kalıcı olarak kaldırılır. |
| Tercihler | Dil, görünüm, çekim ve dışa aktarma seçenekleri | Cihazınızdaki App Group kabında saklanır. |

## Yüz verisi

iVeil, yüzleri ve kişileri **konumlandırmak** için cihazınızdaki Apple Vision çerçevesini kullanır. Bu yüz tanıma **değildir:** iVeil kim olduğunu belirlemez, yüzleri karşılaştırmaz ve biyometrik şablon oluşturmaz.

- **Kullanım:** yüzleri gizlemek, seçtiğiniz kişileri tutmak, emoji örtülerini hizalamak, tuttuğunuz kişiyi kesmek ve isteğe bağlı portre rötuşu.
- **Saklama:** normalleştirilmiş yüz dikdörtgenleri, kişi dış çizgileri ve rötuş ayarlarınız uygulama kum havuzundaki projenin içinde saklanır. Tam yüz işaret noktaları diske yazılmaz.
- **Paylaşım:** yüz verisi yüklenmez, bize veya üçüncü taraflara verilmez ve iCloud ile eşitlenmez.
- **Saklama süresi:** yüz verisi yalnızca proje durduğu sürece kalır. Bir projeyi silmek (Son Silinenler’de 30 gün sonra) veya uygulamayı kaldırmak onu siler.

## Ağ kullanımı

iVeil’in kendi sunucusu yoktur. Ağ istekleri yalnızca Apple hizmetlerinden gelir:

- **Haritalar.** Bir fotoğrafın konumu varsa iVeil onu bir Apple Haritası üzerinde gösterir; harita o bölgenin karolarını Apple’dan yükler. **Kabaca konum** seçildiğinde yer adı, tam koordinatlar yerine yaklaşık 5 km’lik bir ızgara hücresinin merkezinden Apple’a sorulur. Görüntü içeriği gönderilmez. Apple bu istekleri [Apple’ın Gizlilik İlkesi](https://www.apple.com/legal/privacy/) kapsamında işler.
- **İsteğe bağlı bahşiş.** «Geliştiriciye bahşiş», Apple’ın StoreKit ile işlediği tüketilebilir bir uygulama içi satın almadır. Hiçbir şeyin kilidini açmaz ve biz kişisel bilgi almayız.
- **İsteğe bağlı iCloud eşitlemesi (varsayılan olarak kapalı).** Açtığınızda dil, görünüm ve çekim veya dışa aktarma seçenekleri gibi birkaç tercih, özel iCloud anahtar-değer deponuz üzerinden eşitlenir. Fotoğraflar, videolar, yüz verisi ve Görünmez İşaret listesi asla eşitlenmez.

## İzinler

| İzin | Amaç |
|------------|---------|
| Fotoğraflar | Seçtiğiniz fotoğrafları açmak ve konum ile kamera ayrıntılarını göstermek |
| Fotoğraflar (yalnızca ekleme) | Dışa aktardığınız kopyaları kaydetmek |
| Kamera | Çekim sekmesi, Canlı Örtü ve Kilit Ekranındaki Örtü Kamerası |

iVeil mikrofon, konum, kişiler veya izleme izni istemez. Video Örtüsü, seçtiğiniz videoda zaten bulunan sesi kullanır ve onu kaldırabilir.

## Arka plan işi ve Canlı Etkinlikler

**Sizin başlattığınız** toplu Güvenli Paylaşım ve Video Örtüsü dışa aktarmaları kısa süre arka planda sürebilir. Bir Canlı Etkinlik, Kilit Ekranında işin adını ve ilerlemesini gösterebilir. Görüntü içeriğini asla göstermez.

## Çocuklar

İçerik cihazda işlendiği ve veri toplayan bir arka ucumuz olmadığı için iVeil, çocuklar dahil hiç kimseden bilerek kişisel veri toplamaz.

## Sorumluluk reddi

iVeil bağımsız bir uygulamadır ve **Apple Inc. ile bağlantılı değildir.** Otomatik algılama bir ilk geçiştir, garanti değildir. Paylaşmadan önce fotoğrafa bir kez daha bakın.

## Değişiklikler

Uygulamamız değişirse bu sayfayı günceller ve yukarıdaki tarihi yenileriz.

## İletişim

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
