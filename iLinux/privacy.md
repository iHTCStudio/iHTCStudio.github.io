---
layout: doc
title: iLinux — Privacy Policy
app_id: iLinux
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iLinux.
---

<section lang="en" markdown="1">

iHTC Studio ("we", "us" or "our") built iLinux (also known as "爱 Linux"). This page informs you of our policies regarding the collection, use and disclosure of personal data when you use our app.

## Summary

**iLinux does not collect analytics or sell personal data.** Command libraries run fully offline on your device. Optional **iCloud sync** (when enabled and signed into iCloud) stores favourites, quiz progress, theme and display preferences in **your** iCloud Key-Value Storage under your Apple ID — iHTC Studio does not operate a backend server for this data.

## Data Collection

We do not operate analytics, advertising or tracking. Specifically:

- **No personal information** is collected by iHTC Studio (no name, email, phone number or iHTC Studio account).
- **No usage analytics** or crash-reporting SDKs are integrated.
- **Your learning data** (favourites, quiz scores, wrong answers) stays on your devices and, if you enable sync, in **Apple iCloud** — not on iHTC Studio servers.
- **No cookies or third-party trackers** in the app.

## How the App Works

iLinux stores all user-generated data — favourites, recent views, quiz session results, wrong answer records, shell platform preference, favourites scope, widget command library and app preferences — locally on your device:

- All command data (JSON summaries and Markdown documentation for **Linux, CMD and PowerShell**) is bundled inside the app and never fetched from any external server.
- No internet connection is required to browse commands or take quizzes.
- Optional **iCloud sync** uses Apple's **NSUbiquitousKeyValueStore** when you are signed into iCloud and leave sync enabled. You can turn it off per device in Settings.
- Opening external links from within the app (e.g., tapping a URL in the Feedback section) uses standard iOS networking behaviour; the linked page is loaded by your device directly from its host, not through any iHTC Studio server.
- The optional **App Store version check** (`AppStoreVersionChecker`) makes a single read-only request to the public iTunes Lookup API to compare the installed version with the latest release. No personal data is sent in this request.

## Permissions

iLinux requests **Photo Library** access only when you choose to **save a share card or command screenshot** to Photos. No camera, microphone, location or contacts access is required.

## Data Storage

| Data | Storage Location |
|------|-----------------|
| Favourites, recent views, wrong answer records, learning status (per platform) | Local UserDefaults / App Group on your device |
| Quiz progress and daily session results (keyed by date and shell platform) | Local app sandbox on your device |
| Theme, language, list/grid layout, shell platform, favourites scope, widget library | Local UserDefaults / App Group on your device |
| iCloud sync mirror (optional) | Apple iCloud Key-Value Storage (`crossSync.*` keys) — favourites, quiz progress, theme, app preferences |
| Widget snapshot (iOS/iPad only) | App Group container (`group.com.iHTCboy.iLinuxs`) |

No data is stored on any iHTC Studio-operated server. Optional iCloud data is governed by Apple's iCloud terms.

## iCloud Sync (Optional)

When **iCloud Sync** is enabled and you are signed into iCloud:

- Data synced: **learning progress** (favourites, recents, learning status, quiz scores, wrong-answer records), **theme**, and **app preferences** (language, shell platform, favourites scope, list/grid settings).
- Storage: Apple **iCloud Key-Value Storage**, associated with your Apple ID.
- Merge: conflicting updates are merged on device (e.g. favourites union, latest timestamps).
- Opt-out: disable in **Settings → iCloud Sync** on any device; that device stops uploading and merging but keeps local data.
- iHTC Studio cannot read your iCloud container.

## App Group (Widget Extension — iOS/iPad only)

iLinux uses an App Group (`group.com.iHTCboy.iLinuxs`) to share a small amount of data with its Home Screen widget extension. This data includes:

- The selected content language code (e.g. `en`, `zh-Hans`)
- A theme colour snapshot (accent hex and gradient values)
- A summary of your learning progress (favourites count, quiz stats) for widget display
- The selected **widget command library** (Linux / CMD / PowerShell)
- The Daily Command widget shuffle counter (a simple integer used to pick the next featured command)

This data is written to a shared container on your device only, and is never transmitted anywhere.

## What iLinux Is Not

iLinux does not execute shell commands, open SSH sessions or access remote systems. No command-line input you might type elsewhere is collected by this app.

## In-App Purchase

iLinux includes an optional tip/purchase option. All payment transactions are handled exclusively by **Apple's StoreKit framework**. iHTC Studio does not receive, process or store any payment card information or billing details.

## Children's Privacy

iLinux does not knowingly collect any personal data from anyone, including children under 13. Since we do not collect any data at all, no special provisions are needed.

## Changes to This Policy

We may update this Privacy Policy from time to time. Any changes will be posted on this page with an updated date. We encourage you to review this page periodically.

## Contact Us

If you have any questions about this Privacy Policy, please contact us:

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="zh-CN" markdown="1">

爱火腿肠工作室（iHTC Studio）（「我们」）为 iLinux（亦称"爱 Linux"）这款应用开发并维护本页面，以告知你在使用应用过程中，我们关于个人数据收集、使用与披露的政策。

## 概要

**爱 Linux 不收集统计分析或出售个人数据。** 命令库完全离线。可选 **iCloud 同步**（登录 iCloud 并开启后）将收藏、测验进度、主题与显示偏好存入 **您 Apple ID 下的 iCloud 键值存储**——iHTC Studio 不运营后端服务器。

## 数据收集

iHTC Studio 不运营统计、广告或追踪。您的学习数据留在设备上，启用同步时由 **Apple iCloud** 托管，我们无法访问。

## 应用工作原理

爱 Linux 将所有用户生成的数据——收藏、最近浏览、测验结果、错题记录、Shell 平台偏好、收藏范围、小组件命令库与应用偏好——存储在设备本地：

- 所有命令数据（**Linux、CMD 与 PowerShell** 的 JSON 摘要与 Markdown 文档）都打包在应用内，绝不从任何外部服务器获取。
- 浏览命令与做测验无需联网。
- 可选 **iCloud 同步**使用 Apple **NSUbiquitousKeyValueStore**；可在设置中按设备关闭。
- 应用内打开外部链接（如点按反馈区的 URL）使用标准 iOS 网络行为；链接的页面由你的设备直接从其主机加载，不经过任何 iHTC Studio 服务器。
- 可选的 **App Store 版本检查**（`AppStoreVersionChecker`）会向公开的 iTunes Lookup API 发起一次只读请求，比较已安装版本与最新版本。该请求不发送任何个人数据。

## 权限

仅在您选择将**分享卡片或命令截图保存到相册**时，爱 Linux 会请求**相册**访问权限。无需相机、麦克风、位置或通讯录权限。

## 数据存储

| 数据 | 存储位置 |
|------|-----------------|
| 收藏、最近浏览、错题、学习状态（按平台） | 设备本地 UserDefaults / App Group |
| 测验进度（按日期与 Shell 平台） | 设备本地应用沙盒 |
| 主题、语言、布局、Shell 平台、收藏范围、小组件库 | 设备本地 UserDefaults / App Group |
| iCloud 同步镜像（可选） | Apple iCloud 键值存储 |
| 小组件快照（仅 iOS/iPad） | App Group 容器 |

不在 iHTC Studio 服务器存储数据。

## iCloud 同步（可选）

开启 **iCloud 同步** 且已登录 iCloud 时，同步**学习进度**、**主题**与**应用偏好**；冲突自动合并；可单设备关闭。

## App Group（小组件扩展 — 仅 iOS/iPad）

爱 Linux 使用 App Group（`group.com.iHTCboy.iLinuxs`）与其主屏小组件扩展共享少量数据。包括：

- 当前内容语言代码（如 `en`、`zh-Hans`）
- 主题色快照（主色 hex 与渐变值）
- 学习进度摘要（收藏数、测验统计）用于小组件显示
- 当前**小组件命令库**（Linux / CMD / PowerShell）
- 「每日命令」小组件的随机刷新计数

这些数据仅写入设备本地的共享容器，从不传输到任何地方。

## 应用不是什么

爱 Linux 不执行 Shell 命令、不建立 SSH 连接、不访问远程系统。你在其它环境输入的命令行内容不会被本应用收集。

## 应用内购

爱 Linux 包含可选的打赏 / 购买选项。所有支付交易完全由 **Apple StoreKit 框架** 处理。iHTC Studio 不接收、不处理、也不存储任何支付卡信息或账单细节。

## 儿童隐私

爱 Linux 不会有意收集任何人（包括 13 岁以下儿童）的个人数据。因为我们完全不收集数据，所以无需特别条款。

## 政策变更

我们可能不时更新本隐私政策。任何变更都会更新本页并标注日期。建议你定期回访。

## 联系我们

如果你对本隐私政策有任何疑问，请联系：

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="zh-TW" markdown="1">

愛火腿腸工作室（iHTC Studio）（「我們」）為 iLinux（亦稱「愛 Linux」）這款應用開發並維護本頁面，以告知你在使用應用過程中，我們關於個人資料收集、使用與揭露的政策。

## 摘要

**愛 Linux 不收集統計分析或出售個人資料。** 指令庫完全離線。可選 **iCloud 同步**將收藏、測驗進度、主題與顯示偏好存入 **您 Apple ID 下的 iCloud 鍵值儲存**。

## 資料收集

iHTC Studio 不營運統計、廣告或追蹤。您的學習資料留在裝置上，啟用同步時由 **Apple iCloud** 託管。

## 應用運作原理

愛 Linux 將所有使用者產生的資料——收藏、最近瀏覽、測驗結果、錯題紀錄、Shell 平台偏好、收藏範圍、小工具指令庫與應用偏好——儲存在裝置本地：

- 所有指令資料（**Linux、CMD 與 PowerShell** 的 JSON 摘要與 Markdown 文件）都打包在應用內，絕不從任何外部伺服器取得。
- 瀏覽指令與做測驗無需連網。
- 可選 **iCloud 同步**使用 Apple **NSUbiquitousKeyValueStore**；可在設定中按裝置關閉。
- 應用內開啟外部連結（如點按回饋區的 URL）使用標準 iOS 網路行為；連結的頁面由你的裝置直接從其主機載入，不經過任何 iHTC Studio 伺服器。
- 可選的 **App Store 版本檢查**（`AppStoreVersionChecker`）會向公開的 iTunes Lookup API 發起一次只讀請求，比較已安裝版本與最新版本。該請求不傳送任何個人資料。

## 權限

僅在您選擇將**分享卡片或指令截圖儲存到相簿**時，愛 Linux 會請求**相簿**存取權限。無需相機、麥克風、位置或通訊錄權限。

## 資料儲存

| 資料 | 儲存位置 |
|------|-----------------|
| 收藏、最近瀏覽、錯題、學習狀態（依平台） | 裝置本地 UserDefaults / App Group |
| 測驗進度（依日期與 Shell 平台） | 裝置本地應用沙盒 |
| 主題、語言、佈局、Shell 平台、收藏範圍、小工具庫 | 裝置本地 UserDefaults / App Group |
| iCloud 同步鏡像（可選） | Apple iCloud 鍵值儲存 |
| 小工具快照（僅 iOS/iPad） | App Group 容器 |

不在 iHTC Studio 伺服器儲存資料。

## iCloud 同步（可選）

開啟 **iCloud 同步** 且已登入 iCloud 時，同步**學習進度**、**主題**與**應用偏好**；可單裝置關閉。

## App Group（小工具擴充套件 — 僅 iOS/iPad）

愛 Linux 使用 App Group（`group.com.iHTCboy.iLinuxs`）與其主畫面小工具擴充套件共享少量資料。包括：

- 目前內容語言代碼（如 `en`、`zh-Hans`）
- 主題色快照（主色 hex 與漸層值）
- 學習進度摘要（收藏數、測驗統計）用於小工具顯示
- 目前**小工具指令庫**（Linux / CMD / PowerShell）
- 「每日指令」小工具的隨機刷新計數

這些資料僅寫入裝置本地的共享容器，從不傳送到任何地方。

## 應用不是什麼

愛 Linux 不執行 Shell 指令、不建立 SSH 連線、不存取遠端系統。你在其它環境輸入的指令列內容不會被本應用收集。

## 應用內購

愛 Linux 包含可選的打賞 / 購買選項。所有支付交易完全由 **Apple StoreKit 框架** 處理。iHTC Studio 不接收、不處理、也不儲存任何支付卡資訊或帳單細節。

## 兒童隱私

愛 Linux 不會有意收集任何人（包括 13 歲以下兒童）的個人資料。因為我們完全不收集資料，所以無需特別條款。

## 政策變更

我們可能不時更新本隱私政策。任何變更都會更新本頁並標註日期。建議你定期回訪。

## 聯絡我們

如果你對本隱私政策有任何疑問，請聯絡：

- **電子郵件：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ja" markdown="1">

iHTC Studio (「私たち」、「私たち」、または「私たちの」) は、iLinux (「愛情 Linux」としても知られています) を構築しました。このページでは、お客様が当社のアプリを使用する際の個人データの収集、使用、開示に関する当社のポリシーをお知らせします。

## 概要

**iLinux does not collect analytics or sell personal data.** Command libraries run fully offline on your device. Optional **iCloud sync** (when enabled and signed into iCloud) stores favourites, quiz progress, theme and display preferences in **your** iCloud Key-Value Storage under your Apple ID — iHTC Studio does not operate a backend server for this data.

## データ収集

当社は分析、広告、追跡を行っておりません。具体的には:

- **個人情報**は iHTC Studio によって収集されません (名前、電子メール、電話番号、または iHTC Studio アカウントは収集されません)。
- **使用状況分析** やクラッシュレポート SDK は統合されていません。
- **学習データ** (お気に入り、クイズのスコア、間違った答え) はデバイス上に残ります。同期を有効にしている場合は、iHTC Studio サーバーではなく **Apple iCloud** に残ります。
- **アプリには Cookie やサードパーティ トラッカーはありません**。

## アプリの仕組み

iLinux は、ユーザーが生成したすべてのデータ (お気に入り、最近のビュー、クイズ セッションの結果、誤答記録、シェル プラットフォームの設定、お気に入りの範囲、ウィジェット コマンド ライブラリ、およびアプリの設定) をデバイス上にローカルに保存します。

- すべてのコマンド データ (**Linux、CMD、および PowerShell** の JSON サマリーとマークダウン ドキュメント) はアプリ内にバンドルされており、外部サーバーからフェッチされることはありません。
- コマンドを参照したり、クイズに答えたりするためにインターネット接続は必要ありません。
- オプションの **iCloud 同期**では、iCloud にサインインし、同期を有効にしたままにすると、Apple の **NSUbiquitousKeyValueStore** が使用されます。設定でデバイスごとにオフにすることができます。
- アプリ内から外部リンクを開く (フィードバック セクションで URL をタップするなど) と、標準の iOS ネットワーク動作が使用されます。リンクされたページは、iHTC Studio サーバー経由ではなく、デバイスのホストから直接ロードされます。
- オプションの **App Store バージョン チェック** (`AppStoreVersionChecker`) は、パブリック iTunes Lookup API に対して単一の読み取り専用リクエストを作成し、インストールされているバージョンと最新リリースを比較します。このリクエストでは個人データは送信されません。

## 権限

iLinux は、**共有カードまたはコマンドのスクリーンショット**を写真に保存することを選択した場合にのみ、**フォト ライブラリ** へのアクセスを要求します。カメラ、マイク、位置情報、連絡先へのアクセスは必要ありません。

## データストレージ

| データ | 保管場所 |
|------|-----------------|
| お気に入り、最近のビュー、誤答記録、学習ステータス (プラットフォームごと) | デバイス上のローカル UserDefaults / アプリ グループ |
| クイズの進行状況と毎日のセッションの結果 (日付とシェル プラットフォームでキー設定) | デバイス上のローカル アプリ サンドボックス |
| テーマ、言語、リスト/グリッド レイアウト、シェル プラットフォーム、お気に入りスコープ、ウィジェット ライブラリ | デバイス上のローカル UserDefaults / アプリ グループ |
| iCloud同期ミラー（オプション） | Apple iCloud Key-Value ストレージ (`crossSync.*` キー) — お気に入り、クイズの進行状況、テーマ、アプリの設定 |
| ウィジェットのスナップショット (iOS/iPad のみ) | アプリ グループ コンテナー (`group.com.iHTCboy.iLinuxs`) |

iHTC Studio が運用するサーバーにはデータは保存されません。オプションの iCloud データには、Apple の iCloud 規約が適用されます。

## iCloud同期（オプション）

**iCloud 同期**が有効で、iCloud にサインインしている場合:

- 同期されたデータ: **学習の進捗状況** (お気に入り、最近、学習ステータス、クイズのスコア、誤答記録)、**テーマ**、**アプリの設定** (言語、シェル プラットフォーム、お気に入りの範囲、リスト/グリッド設定)。
- ストレージ: Apple **iCloud Key-Value ストレージ**、Apple ID に関連付けられています。
- マージ: 競合する更新がデバイス上でマージされます (例: お気に入りの結合、最新のタイムスタンプ)。
- オプトアウト: どのデバイスでも **[設定] → [iCloud 同期]** で無効にします。そのデバイスはアップロードとマージを停止しますが、ローカル データは保持します。
- iHTC Studio は iCloud コンテナを読み取ることができません。

## アプリグループ (ウィジェット拡張 — iOS/iPad のみ)

iLinux は、アプリ グループ (`group.com.iHTCboy.iLinuxs`) を使用して、ホーム画面ウィジェット拡張機能と少量のデータを共有します。このデータには次のものが含まれます。

- 選択したコンテンツの言語コード (例: `en`、`zh-Hans`)
- テーマカラーのスナップショット (アクセントの 16 進数とグラデーションの値)
- ウィジェット表示用の学習進捗状況の概要 (お気に入りの数、クイズの統計)
- 選択した **ウィジェット コマンド ライブラリ** (Linux / CMD / PowerShell)
- Daily Command ウィジェット シャッフル カウンター (次に注目されるコマンドを選択するために使用される単純な整数)

このデータはデバイス上の共有コンテナにのみ書き込まれ、どこにも送信されることはありません。

## iLinux ではないもの

iLinux は、シェル コマンドを実行したり、SSH セッションを開いたり、リモート システムにアクセスしたりしません。他の場所で入力したコマンドライン入力は、このアプリによって収集されません。

## アプリ内購入

iLinux には、オプションのチップ/購入オプションが含まれています。すべての支払いトランザクションは **Apple の StoreKit フレームワーク**によって独占的に処理されます。 iHTC Studio は、支払いカード情報や請求の詳細を受信、処理、保存しません。

## 子供のプライバシー

iLinux は、13 歳未満の子供を含むいかなる人物からも、故意に個人データを収集することはありません。データをまったく収集しないため、特別な規定は必要ありません。

## このポリシーの変更

当社は、このプライバシー ポリシーを随時更新することがあります。変更があった場合は、更新日とともにこのページに掲載されます。このページを定期的に確認することをお勧めします。

## お問い合わせ

このプライバシー ポリシーについてご質問がある場合は、以下までお問い合わせください。

- **電子メール:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ko" markdown="1">

iHTC Studio("당사", "당사" 또는 "당사")는 iLinux("爱 Linux"라고도 함)를 구축했습니다. 이 페이지에서는 귀하가 당사 앱을 사용할 때 개인 데이터의 수집, 사용 및 공개에 관한 정책을 알려드립니다.

## 요약

**iLinux는 분석을 수집하거나 개인 데이터를 판매하지 않습니다.** 명령 라이브러리는 장치에서 완전히 오프라인으로 실행됩니다. 옵션 **iCloud 동기화**(활성화되고 iCloud에 로그인된 경우)는 Apple ID 아래의 **귀하의** iCloud 키-값 저장소에 즐겨찾기, 퀴즈 진행 상황, 테마 및 디스플레이 기본 설정을 저장합니다. iHTC Studio는 이 데이터에 대한 백엔드 서버를 운영하지 않습니다.

## 데이터 수집

우리는 분석, 광고 또는 추적을 운영하지 않습니다. 구체적으로:

- **개인 정보**는 iHTC Studio에서 수집하지 않습니다(이름, 이메일, 전화번호 또는 iHTC Studio 계정 없음).
- **사용 분석 없음** 또는 충돌 보고 SDK가 통합되어 있습니다.
- **학습 데이터**(즐겨찾기, 퀴즈 점수, 오답)는 기기에 유지되며, 동기화를 활성화한 경우 iHTC Studio 서버가 아닌 **Apple iCloud**에 유지됩니다.
- **앱에는 쿠키나 제3자 추적기가 없습니다**.

## 앱 작동 방식

iLinux는 즐겨찾기, 최근 보기, 퀴즈 세션 결과, 오답 기록, 쉘 플랫폼 기본 설정, 즐겨찾기 범위, 위젯 명령 라이브러리 및 앱 기본 설정 등 사용자가 생성한 모든 데이터를 장치에 로컬로 저장합니다.

- 모든 명령 데이터(**Linux, CMD 및 PowerShell**에 대한 JSON 요약 및 Markdown 문서)는 앱 내부에 번들로 제공되며 외부 서버에서 가져오지 않습니다.
- 명령을 찾아보거나 퀴즈를 풀기 위해 인터넷 연결이 필요하지 않습니다.
- 선택 사항인 **iCloud 동기화**는 iCloud에 로그인하고 동기화를 활성화한 상태에서 Apple의 **NSUbiquitousKeyValueStore**를 사용합니다. 설정에서 기기별로 이 기능을 끌 수 있습니다.
- 앱 내에서 외부 링크 열기(예: 피드백 섹션에서 URL 누르기)는 표준 iOS 네트워킹 동작을 사용합니다. 연결된 페이지는 iHTC Studio 서버를 통하지 않고 호스트에서 직접 장치에 의해 로드됩니다.
- 선택적 **App Store 버전 확인**(`AppStoreVersionChecker`)은 설치된 버전과 최신 릴리스를 비교하기 위해 공개 iTunes Lookup API에 단일 읽기 전용 요청을 만듭니다. 이 요청에는 개인 데이터가 전송되지 않습니다.

## 권한

iLinux는 사진에 **공유 카드 저장 또는 명령 스크린샷**을 선택한 경우에만 **사진 라이브러리** 액세스를 요청합니다. 카메라, 마이크, 위치 또는 연락처 액세스가 필요하지 않습니다.

## 데이터 저장

| 데이터 | 저장 위치 |
|------|-----------------|
| 즐겨찾기, 최근 조회수, 오답 기록, 학습 현황(플랫폼별) | 장치의 로컬 UserDefaults/앱 그룹 |
| 퀴즈 진행 및 일일 세션 결과(날짜 및 쉘 플랫폼으로 입력) | 기기의 로컬 앱 샌드박스 |
| 테마, 언어, 목록/그리드 레이아웃, 쉘 플랫폼, 즐겨찾기 범위, 위젯 라이브러리 | 장치의 로컬 UserDefaults/앱 그룹 |
| iCloud 동기화 미러(선택 사항) | Apple iCloud 키-값 저장소(`crossSync.*` 키) — 즐겨찾기, 퀴즈 진행, 테마, 앱 기본 설정 |
| 위젯 스냅샷(iOS/iPad 전용) | 앱 그룹 컨테이너(`group.com.iHTCboy.iLinuxs`) |

iHTC Studio가 운영하는 서버에는 데이터가 저장되지 않습니다. 선택적 iCloud 데이터에는 Apple의 iCloud 약관이 적용됩니다.

## iCloud 동기화(선택 사항)

**iCloud 동기화**가 활성화되어 있고 iCloud에 로그인되어 있는 경우:

- 동기화된 데이터: **학습 진행 상황**(즐겨찾기, 최근, 학습 상태, 퀴즈 점수, 오답 기록), **테마** 및 **앱 기본 설정**(언어, 셸 플랫폼, 즐겨찾기 범위, 목록/그리드 설정).
- 저장소: Apple ID와 연결된 Apple **iCloud 키-값 저장소**.
- 병합: 충돌하는 업데이트가 장치에서 병합됩니다(예: 즐겨찾기 통합, 최신 타임스탬프).
- 옵트아웃: 모든 기기의 **설정 → iCloud 동기화**에서 비활성화합니다. 해당 장치는 업로드 및 병합을 중지하지만 로컬 데이터는 유지합니다.
- iHTC Studio가 iCloud 컨테이너를 읽을 수 없습니다.

## 앱 그룹(위젯 확장 - iOS/iPad 전용)

iLinux는 앱 그룹(`group.com.iHTCboy.iLinuxs`)을 사용하여 홈 화면 위젯 확장 프로그램과 소량의 데이터를 공유합니다. 이 데이터에는 다음이 포함됩니다.

- 선택한 콘텐츠 언어 코드(예: `en`, `zh-Hans`)
- 테마 색상 스냅샷(악센트 16진수 및 그라데이션 값)
- 위젯 표시를 위한 학습 진행 상황 요약(즐겨찾기 수, 퀴즈 통계)
- 선택한 **위젯 명령 라이브러리**(Linux/CMD/PowerShell)
- Daily Command 위젯 셔플 카운터(다음 추천 명령을 선택하는 데 사용되는 간단한 정수)

이 데이터는 귀하의 장치에 있는 공유 컨테이너에만 기록되며 어디에도 전송되지 않습니다.

## iLinux가 아닌 것

iLinux는 쉘 명령을 실행하거나 SSH 세션을 열거나 원격 시스템에 액세스하지 않습니다. 다른 곳에 입력할 수 있는 명령줄 입력은 이 앱에서 수집되지 않습니다.

## 인앱 구매

iLinux에는 선택적 팁/구매 옵션이 포함되어 있습니다. 모든 결제 거래는 **Apple의 StoreKit 프레임워크**에 의해서만 처리됩니다. iHTC Studio는 결제 카드 정보나 청구 세부정보를 수신, 처리 또는 저장하지 않습니다.

## 아동의 개인정보 보호

iLinux는 13세 미만의 어린이를 포함하여 그 누구로부터도 고의로 개인 데이터를 수집하지 않습니다. 우리는 데이터를 전혀 수집하지 않기 때문에 특별한 조항이 필요하지 않습니다.

## 본 정책의 변경 사항

당사는 수시로 본 개인정보 보호정책을 업데이트할 수 있습니다. 모든 변경 사항은 업데이트된 날짜와 함께 이 페이지에 게시됩니다. 이 페이지를 정기적으로 검토하시기 바랍니다.

## 문의하기

본 개인정보 보호정책에 대해 질문이 있는 경우 당사에 문의하십시오.

- **이메일:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ru" markdown="1">

iHTC Studio («мы», «нас» или «наш») создала iLinux (также известный как «爱 Linux»). Эта страница информирует вас о нашей политике в отношении сбора, использования и раскрытия личных данных при использовании нашего приложения.

## Резюме

**iLinux не собирает аналитику и не продает личные данные.** Библиотеки команд работают на вашем устройстве полностью автономно. Дополнительная **синхронизация с iCloud** (при включении и входе в iCloud) сохраняет избранное, прогресс викторины, темы и настройки отображения в **вашем** хранилище ключей и значений iCloud под вашим Apple ID — iHTC Studio не использует внутренний сервер для этих данных.

## Сбор данных

Мы не занимаемся аналитикой, рекламой и отслеживанием. В частности:

- **iHTC Studio не собирает никакой личной информации** (без имени, адреса электронной почты, номера телефона или учетной записи iHTC Studio).
- **Аналитика использования** и SDK для отчетов о сбоях не интегрированы.
- **Ваши учебные данные** (избранное, результаты тестов, неправильные ответы) остаются на ваших устройствах и, если вы включите синхронизацию, в **Apple iCloud**, а не на серверах iHTC Studio.
- **В приложении отсутствуют файлы cookie и сторонние трекеры**.

## Как работает приложение

iLinux хранит все пользовательские данные — избранное, недавние просмотры, результаты сеансов викторины, записи неправильных ответов, предпочтения платформы оболочки, область избранного, библиотеку команд виджетов и настройки приложений — локально на вашем устройстве:

- Все данные команд (сводки JSON и документация Markdown для **Linux, CMD и PowerShell**) объединяются внутри приложения и никогда не извлекаются с какого-либо внешнего сервера.
- Для просмотра команд или прохождения тестов не требуется подключение к Интернету.
- Дополнительная **синхронизация с iCloud** использует **NSUbiquitousKeyValueStore** от Apple, когда вы вошли в iCloud и оставили синхронизацию включенной. Вы можете отключить его для каждого устройства в настройках.
- Открытие внешних ссылок из приложения (например, нажатие URL-адреса в разделе «Отзывы») использует стандартное сетевое поведение iOS; связанная страница загружается вашим устройством непосредственно со своего хоста, а не через какой-либо сервер iHTC Studio.
- The optional **App Store version check** (`AppStoreVersionChecker`) makes a single read-only request to the public iTunes Lookup API to compare the installed version with the latest release. No personal data is sent in this request.

## Разрешения

iLinux запрашивает доступ к **Библиотеке фотографий** только в том случае, если вы решите **сохранить карточку общего доступа или скриншот команды** в «Фото». Доступ к камере, микрофону, местоположению или контактам не требуется.

## Хранение данных

| Данные | Место хранения |
|------|-----------------|
| Избранное, недавние просмотры, записи неправильных ответов, статус обучения (для каждой платформы) | Локальные настройки пользователя/группа приложений на вашем устройстве |
| Ход викторины и результаты ежедневных сессий (с указанием даты и платформы оболочки) | Локальная песочница приложения на вашем устройстве |
| Тема, язык, макет списка/сетки, платформа оболочки, область избранного, библиотека виджетов | Локальные настройки пользователя/группа приложений на вашем устройстве |
| Зеркало синхронизации iCloud (необязательно) | Хранилище ключей и значений Apple iCloud (ключи `crossSync.*`) — избранное, ход теста, тема, настройки приложения |
| Снимок виджета (только для iOS/iPad) | Контейнер группы приложений (`group.com.iHTCboy.iLinuxs`) |

Никакие данные не хранятся ни на одном сервере под управлением iHTC Studio. Дополнительные данные iCloud регулируются условиями Apple iCloud.

## Синхронизация с iCloud (необязательно)

Если **iCloud Sync** включен и вы вошли в iCloud:

- Синхронизируются данные: **прогресс обучения** (избранное, последние, статус обучения, баллы за тесты, записи о неправильных ответах), **тема** и **настройки приложения** (язык, платформа оболочки, область избранного, настройки списка/сетки).
- Хранилище: Apple **iCloud Key-Value Storage**, связанное с вашим Apple ID.
- Объединение: конфликтующие обновления объединяются на устройстве (например, объединение избранного, последние временные метки).
- Отказ: отключите его в **Настройки → iCloud Sync** на любом устройстве; это устройство прекращает загрузку и объединение, но сохраняет локальные данные.
- iHTC Studio не может прочитать ваш контейнер iCloud.

## Группа приложений (расширение виджета — только для iOS/iPad)

iLinux uses an App Group (`group.com.iHTCboy.iLinuxs`) to share a small amount of data with its Home Screen widget extension. This data includes:

- Выбранный код языка контента (например, `en`, `zh-Hans`)
- Снимок цвета темы (шестнадцатеричный акцент и значения градиента)
- Сводная информация о вашем прогрессе в обучении (количество избранных, статистика тестов) для отображения в виджете
- Выбранная **библиотека команд виджета** (Linux/CMD/PowerShell)
- Счетчик перемешивания виджета Daily Command (простое целое число, используемое для выбора следующей рекомендуемой команды)

Эти данные записываются только в общий контейнер на вашем устройстве и никогда никуда не передаются.

## Чем iLinux не является

iLinux не выполняет команды оболочки, не открывает сеансы SSH и не получает доступ к удаленным системам. Это приложение не собирает никакие данные командной строки, которые вы можете ввести где-либо еще.

## Покупка в приложении

iLinux включает в себя дополнительную возможность чаевых/покупки. Все платежные транзакции обрабатываются исключительно с помощью **платформы Apple StoreKit**. iHTC Studio не получает, не обрабатывает и не хранит информацию о платежных картах или платежные реквизиты.

## Конфиденциальность детей

iLinux сознательно не собирает никаких личных данных ни от кого, включая детей до 13 лет. Поскольку мы вообще не собираем никаких данных, никаких специальных мер не требуется.

## Изменения в этой политике

Мы можем время от времени обновлять настоящую Политику конфиденциальности. Любые изменения будут опубликованы на этой странице с указанием обновленной даты. Мы рекомендуем вам периодически просматривать эту страницу.

## Свяжитесь с нами

Если у вас есть какие-либо вопросы по поводу настоящей Политики конфиденциальности, свяжитесь с нами:

- **Электронная почта:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="th" markdown="1">

iHTC Studio ("เรา", "พวกเรา" หรือ "ของเรา") ได้สร้าง iLinux (หรือที่รู้จักกันในชื่อ "爱 Linux") หน้านี้แจ้งให้คุณทราบนโยบายของเราเกี่ยวกับการรวบรวม การใช้ และการเปิดเผยข้อมูลส่วนบุคคลเมื่อคุณใช้แอปของเรา

## สรุป

**iLinux ไม่รวบรวมการวิเคราะห์หรือขายข้อมูลส่วนบุคคล** ไลบรารีคำสั่งทำงานแบบออฟไลน์โดยสมบูรณ์บนอุปกรณ์ของคุณ ตัวเลือก **การซิงค์ iCloud** (เมื่อเปิดใช้งานและลงชื่อเข้าใช้ iCloud) จะจัดเก็บรายการโปรด ความคืบหน้าของแบบทดสอบ ธีม และการตั้งค่าการแสดงผลใน **พื้นที่จัดเก็บคีย์-ค่า iCloud ของคุณ** ภายใต้ Apple ID ของคุณ — iHTC Studio จะไม่ดำเนินการเซิร์ฟเวอร์แบ็กเอนด์สำหรับข้อมูลนี้

## การรวบรวมข้อมูล

เราไม่ได้ดำเนินการวิเคราะห์ การโฆษณา หรือการติดตาม โดยเฉพาะ:

- **ไม่มีข้อมูลส่วนบุคคล** ที่ถูกรวบรวมโดย iHTC Studio (ไม่มีชื่อ อีเมล หมายเลขโทรศัพท์ หรือบัญชี iHTC Studio)
- **ไม่มีการผสานรวมการวิเคราะห์การใช้งาน** หรือ SDK การรายงานข้อขัดข้อง
- **ข้อมูลการเรียนรู้ของคุณ** (รายการโปรด คะแนนแบบทดสอบ คำตอบที่ผิด) จะยังคงอยู่ในอุปกรณ์ของคุณ และหากคุณเปิดใช้งานการซิงค์ ก็จะอยู่ใน **Apple iCloud** — ไม่ใช่บนเซิร์ฟเวอร์ iHTC Studio
- **ไม่มีคุกกี้หรือเครื่องมือติดตามบุคคลที่สาม** ในแอป

## แอปทำงานอย่างไร

iLinux จัดเก็บข้อมูลที่ผู้ใช้สร้างขึ้นทั้งหมด — รายการโปรด มุมมองล่าสุด ผลเซสชั่นคำถาม บันทึกคำตอบที่ผิด การตั้งค่าแพลตฟอร์มเชลล์ ขอบเขตรายการโปรด ไลบรารีคำสั่งวิดเจ็ต และการตั้งค่าแอพ — ภายในอุปกรณ์ของคุณ:

- ข้อมูลคำสั่งทั้งหมด (ข้อมูลสรุป JSON และเอกสาร Markdown สำหรับ **Linux, CMD และ PowerShell**) รวมอยู่ในแอปและไม่เคยดึงข้อมูลจากเซิร์ฟเวอร์ภายนอกใดๆ
- ไม่จำเป็นต้องเชื่อมต่ออินเทอร์เน็ตเพื่อเรียกดูคำสั่งหรือทำแบบทดสอบ
- ตัวเลือก **การซิงค์ iCloud** จะใช้ **NSUbiquitousKeyValueStore** ของ Apple เมื่อคุณลงชื่อเข้าใช้ iCloud และเปิดใช้งานการซิงค์ทิ้งไว้ คุณสามารถปิดอุปกรณ์แต่ละเครื่องได้ในการตั้งค่า
- การเปิดลิงก์ภายนอกจากภายในแอป (เช่น การแตะ URL ในส่วนคำติชม) จะใช้พฤติกรรมเครือข่าย iOS มาตรฐาน อุปกรณ์ของคุณโหลดหน้าที่เชื่อมโยงจากโฮสต์โดยตรง ไม่ใช่ผ่านเซิร์ฟเวอร์ iHTC Studio ใดๆ
- ตัวเลือก **การตรวจสอบเวอร์ชันของ App Store** (`AppStoreVersionChecker`) จะส่งคำขอแบบอ่านอย่างเดียวไปยัง iTunes Lookup API สาธารณะเพื่อเปรียบเทียบเวอร์ชันที่ติดตั้งกับรุ่นล่าสุด ไม่มีการส่งข้อมูลส่วนบุคคลในคำขอนี้

## สิทธิ์

iLinux ร้องขอการเข้าถึง **คลังรูปภาพ** เฉพาะเมื่อคุณเลือกที่จะ **บันทึกการ์ดแชร์หรือภาพหน้าจอคำสั่ง** ลงในรูปภาพ ไม่จำเป็นต้องมีการเข้าถึงกล้อง ไมโครโฟน ตำแหน่ง หรือผู้ติดต่อ

## การจัดเก็บข้อมูล

| ข้อมูล | สถานที่จัดเก็บ |
|------|-----------------|
| รายการโปรด การดูล่าสุด บันทึกคำตอบที่ผิด สถานะการเรียนรู้ (ต่อแพลตฟอร์ม) | Local UserDefaults / App Group บนอุปกรณ์ของคุณ |
| ความคืบหน้าของแบบทดสอบและผลเซสชั่นรายวัน (คีย์ตามวันที่และแพลตฟอร์มเชลล์) | แซนด์บ็อกซ์แอปท้องถิ่นบนอุปกรณ์ของคุณ |
| ธีม ภาษา เค้าโครงรายการ/กริด แพลตฟอร์มเชลล์ ขอบเขตรายการโปรด ไลบรารีวิดเจ็ต | Local UserDefaults / App Group บนอุปกรณ์ของคุณ |
| มิเรอร์การซิงค์ iCloud (อุปกรณ์เสริม) | พื้นที่จัดเก็บคีย์-ค่า Apple iCloud (ปุ่ม `crossSync.*`) — รายการโปรด ความคืบหน้าของแบบทดสอบ ธีม การตั้งค่าแอพ |
| สแน็ปช็อตวิดเจ็ต (iOS/iPad เท่านั้น) | คอนเทนเนอร์กลุ่มแอป (`group.com.iHTCboy.iLinuxs`) |

ไม่มีการจัดเก็บข้อมูลบนเซิร์ฟเวอร์ที่ดำเนินการโดย iHTC Studio ข้อมูลเสริม iCloud อยู่ภายใต้ข้อกำหนด iCloud ของ Apple

## iCloud ซิงค์ (ไม่จำเป็น)

เมื่อเปิดใช้งาน **iCloud Sync** และคุณลงชื่อเข้าใช้ iCloud:

- ข้อมูลที่ซิงค์: **ความคืบหน้าการเรียนรู้** (รายการโปรด ล่าสุด สถานะการเรียนรู้ คะแนนแบบทดสอบ บันทึกคำตอบผิด) **ธีม** และ **การตั้งค่าแอป** (ภาษา แพลตฟอร์มเชลล์ ขอบเขตรายการโปรด การตั้งค่ารายการ/ตาราง)
- พื้นที่จัดเก็บข้อมูล: Apple **พื้นที่จัดเก็บข้อมูลคีย์-ค่า iCloud** ที่เชื่อมโยงกับ Apple ID ของคุณ
- ผสาน: การอัปเดตที่ขัดแย้งกันจะถูกผสานบนอุปกรณ์ (เช่น การรวมรายการโปรด การประทับเวลาล่าสุด)
- เลือกไม่รับ: ปิดการใช้งานใน **การตั้งค่า → iCloud Sync** บนอุปกรณ์ใดก็ได้ อุปกรณ์นั้นหยุดการอัปโหลดและการรวม แต่จะเก็บข้อมูลในเครื่องไว้
- iHTC Studio ไม่สามารถอ่านคอนเทนเนอร์ iCloud ของคุณได้

## กลุ่มแอป (ส่วนขยายวิดเจ็ต — iOS/iPad เท่านั้น)

iLinux ใช้ App Group (`group.com.iHTCboy.iLinuxs`) เพื่อแบ่งปันข้อมูลจำนวนเล็กน้อยด้วยส่วนขยายวิดเจ็ตบนหน้าจอหลัก ข้อมูลนี้ประกอบด้วย:

- รหัสภาษาของเนื้อหาที่เลือก (เช่น `en`, `zh-Hans`)
- สแนปชอตสีของธีม (ค่าฐานสิบหกและการไล่ระดับสี)
- สรุปความก้าวหน้าในการเรียนรู้ของคุณ (จำนวนรายการโปรด สถิติแบบทดสอบ) สำหรับการแสดงวิดเจ็ต
- **ไลบรารีคำสั่งวิดเจ็ต** ที่เลือก (Linux / CMD / PowerShell)
- ตัวนับสุ่มวิดเจ็ต Daily Command (จำนวนเต็มธรรมดาที่ใช้เพื่อเลือกคำสั่งเด่นถัดไป)

ข้อมูลนี้เขียนลงในคอนเทนเนอร์ที่ใช้ร่วมกันบนอุปกรณ์ของคุณเท่านั้น และจะไม่ถ่ายโอนไปที่ใดเลย

## iLinux ไม่ใช่อะไร

iLinux ไม่ดำเนินการคำสั่งเชลล์ เปิดเซสชัน SSH หรือเข้าถึงระบบระยะไกล แอปนี้ไม่มีการรวบรวมอินพุตบรรทัดคำสั่งที่คุณอาจพิมพ์ที่อื่น

## การซื้อในแอป

iLinux มีตัวเลือกทิป/การซื้อเสริม ธุรกรรมการชำระเงินทั้งหมดได้รับการจัดการโดย **เฟรมเวิร์ก StoreKit ของ Apple** iHTC Studio จะไม่รับ ประมวลผล หรือจัดเก็บข้อมูลบัตรชำระเงินหรือรายละเอียดการเรียกเก็บเงิน

## ความเป็นส่วนตัวของเด็ก

iLinux จะไม่รวบรวมข้อมูลส่วนบุคคลใด ๆ จากใครก็ตามโดยเจตนา รวมถึงเด็กอายุต่ำกว่า 13 ปี เนื่องจากเราไม่รวบรวมข้อมูลใด ๆ เลย จึงไม่จำเป็นต้องมีข้อกำหนดพิเศษ

## การเปลี่ยนแปลงนโยบายนี้

เราอาจปรับปรุงนโยบายความเป็นส่วนตัวนี้เป็นครั้งคราว การเปลี่ยนแปลงใด ๆ จะถูกโพสต์บนหน้านี้พร้อมวันที่อัปเดต เราขอแนะนำให้คุณตรวจสอบหน้านี้เป็นระยะ

## ติดต่อเรา

หากคุณมีคำถามใด ๆ เกี่ยวกับนโยบายความเป็นส่วนตัวนี้ โปรดติดต่อเรา:

- **อีเมล:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="de" markdown="1">

iHTC Studio („wir“, „uns“ oder „unser“) hat iLinux (auch bekannt als „爱 Linux“) entwickelt. Auf dieser Seite informieren wir Sie über unsere Richtlinien zur Erhebung, Nutzung und Offenlegung personenbezogener Daten bei der Nutzung unserer App.

## Zusammenfassung

**iLinux sammelt keine Analysen und verkauft keine persönlichen Daten.** Befehlsbibliotheken laufen vollständig offline auf Ihrem Gerät. Die optionale **iCloud-Synchronisierung** (sofern aktiviert und bei iCloud angemeldet) speichert Favoriten, Quizfortschritt, Design und Anzeigeeinstellungen in **Ihrem** iCloud-Schlüsselwertspeicher unter Ihrer Apple-ID – iHTC Studio betreibt keinen Backend-Server für diese Daten.

## Datenerfassung

Wir betreiben keine Analysen, Werbung oder Tracking. Konkret:

- **Keine persönlichen Daten** werden von iHTC Studio erfasst (kein Name, E-Mail, Telefonnummer oder iHTC Studio-Konto).
- **Es sind keine Nutzungsanalysen** oder Absturzberichts-SDKs integriert.
- **Ihre Lerndaten** (Favoriten, Quizergebnisse, falsche Antworten) bleiben auf Ihren Geräten und, wenn Sie die Synchronisierung aktivieren, in **Apple iCloud** – nicht auf iHTC Studio-Servern.
- **Keine Cookies oder Tracker von Drittanbietern** in der App.

## So funktioniert die App

iLinux speichert alle vom Benutzer generierten Daten – Favoriten, aktuelle Ansichten, Quizsitzungsergebnisse, Datensätze zu falschen Antworten, Shell-Plattformpräferenz, Favoritenbereich, Widget-Befehlsbibliothek und App-Präferenzen – lokal auf Ihrem Gerät:

- Alle Befehlsdaten (JSON-Zusammenfassungen und Markdown-Dokumentation für **Linux, CMD und PowerShell**) werden in der App gebündelt und niemals von einem externen Server abgerufen.
- Zum Durchsuchen von Befehlen oder zum Durchführen von Tests ist keine Internetverbindung erforderlich.
- Die optionale **iCloud-Synchronisierung** verwendet Apples **NSUbiquitousKeyValueStore**, wenn Sie bei iCloud angemeldet sind und die Synchronisierung aktiviert lassen. Sie können es in den Einstellungen für jedes Gerät deaktivieren.
- Beim Öffnen externer Links innerhalb der App (z. B. durch Tippen auf eine URL im Abschnitt „Feedback“) wird das standardmäßige iOS-Netzwerkverhalten verwendet. Die verlinkte Seite wird von Ihrem Gerät direkt von seinem Host geladen, nicht über einen iHTC Studio-Server.
- The optional **App Store version check** (`AppStoreVersionChecker`) makes a single read-only request to the public iTunes Lookup API to compare the installed version with the latest release. No personal data is sent in this request.

## Berechtigungen

iLinux fordert den Zugriff auf die **Fotobibliothek** nur dann an, wenn Sie sich für das **Speichern einer Freigabekarte oder eines Befehls-Screenshots** in Fotos entscheiden. Es ist kein Zugriff auf Kamera, Mikrofon, Standort oder Kontakte erforderlich.

## Datenspeicherung

| Daten | Speicherort |
|------|-----------------|
| Favoriten, aktuelle Ansichten, Datensätze mit falschen Antworten, Lernstatus (pro Plattform) | Lokale Benutzereinstellungen/App-Gruppe auf Ihrem Gerät |
| Quizfortschritt und tägliche Sitzungsergebnisse (verschlüsselt nach Datum und Shell-Plattform) | Lokale App-Sandbox auf Ihrem Gerät |
| Thema, Sprache, Listen-/Rasterlayout, Shell-Plattform, Favoritenbereich, Widget-Bibliothek | Lokale Benutzereinstellungen/App-Gruppe auf Ihrem Gerät |
| iCloud-Synchronisierungsspiegel (optional) | Apple iCloud Key-Value Storage (`crossSync.*` keys) — favourites, quiz progress, theme, app preferences |
| Widget-Snapshot (nur iOS/iPad) | App Group container (`group.com.iHTCboy.iLinuxs`) |

Auf keinem von iHTC Studio betriebenen Server werden Daten gespeichert. Optionale iCloud-Daten unterliegen den iCloud-Bedingungen von Apple.

## iCloud-Synchronisierung (optional)

Wenn **iCloud Sync** aktiviert ist und Sie bei iCloud angemeldet sind:

- Synchronisierte Daten: **Lernfortschritt** (Favoriten, Aktuelles, Lernstatus, Quizergebnisse, Datensätze zu falschen Antworten), **Thema** und **App-Einstellungen** (Sprache, Shell-Plattform, Favoritenbereich, Listen-/Rastereinstellungen).
- Speicher: Apple **iCloud Key-Value Storage**, verknüpft mit Ihrer Apple-ID.
- Zusammenführen: In Konflikt stehende Aktualisierungen werden auf dem Gerät zusammengeführt (z. B. Favoritenvereinigung, neueste Zeitstempel).
- Opt-out: in **Einstellungen → iCloud Sync** auf jedem Gerät deaktivieren; Dieses Gerät stoppt das Hochladen und Zusammenführen, behält aber lokale Daten.
- iHTC Studio kann Ihren iCloud-Container nicht lesen.

## App-Gruppe (Widget-Erweiterung – nur iOS/iPad)

iLinux uses an App Group (`group.com.iHTCboy.iLinuxs`) to share a small amount of data with its Home Screen widget extension. This data includes:

- The selected content language code (e.g. `en`, `zh-Hans`)
- Eine Momentaufnahme der Themenfarbe (Akzent-Hex-Werte und Farbverlaufswerte)
- Eine Zusammenfassung Ihres Lernfortschritts (Anzahl der Favoriten, Quizstatistiken) zur Widget-Anzeige
- Die ausgewählte **Widget-Befehlsbibliothek** (Linux / CMD / PowerShell)
- Der Shuffle-Zähler des Daily Command-Widgets (eine einfache Ganzzahl, die zur Auswahl des nächsten vorgestellten Befehls verwendet wird)

Diese Daten werden nur in einen gemeinsamen Container auf Ihrem Gerät geschrieben und niemals irgendwohin übertragen.

## Was iLinux nicht ist

iLinux führt keine Shell-Befehle aus, öffnet keine SSH-Sitzungen und greift nicht auf Remote-Systeme zu. Diese App erfasst keine Befehlszeileneingaben, die Sie möglicherweise an anderer Stelle eingeben.

## In-App-Kauf

iLinux beinhaltet eine optionale Trinkgeld-/Kaufoption. Sämtliche Zahlungsvorgänge werden ausschließlich über **Apples StoreKit-Framework** abgewickelt. iHTC Studio empfängt, verarbeitet oder speichert keine Zahlungskarteninformationen oder Rechnungsdetails.

## Privatsphäre von Kindern

iLinux sammelt wissentlich keine personenbezogenen Daten von irgendjemandem, auch nicht von Kindern unter 13 Jahren. Da wir überhaupt keine Daten sammeln, sind keine besonderen Bestimmungen erforderlich.

## Änderungen an dieser Richtlinie

Wir können diese Datenschutzrichtlinie von Zeit zu Zeit aktualisieren. Alle Änderungen werden mit aktualisiertem Datum auf dieser Seite veröffentlicht. Wir empfehlen Ihnen, diese Seite regelmäßig zu überprüfen.

## Kontaktieren Sie uns

Wenn Sie Fragen zu dieser Datenschutzrichtlinie haben, kontaktieren Sie uns bitte:

- **E-Mail:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="fr" markdown="1">

iHTC Studio (« nous », « notre » ou « notre ») a construit iLinux (également connu sous le nom de « 爱 Linux »). Cette page vous informe de nos politiques concernant la collecte, l'utilisation et la divulgation des données personnelles lorsque vous utilisez notre application.

## Résumé

**iLinux ne collecte pas d'analyses et ne vend pas de données personnelles.** Les bibliothèques de commandes s'exécutent entièrement hors ligne sur votre appareil. La **synchronisation iCloud** facultative (lorsqu'elle est activée et connectée à iCloud) stocke les favoris, la progression du quiz, le thème et les préférences d'affichage dans **votre** stockage de valeurs de clé iCloud sous votre identifiant Apple — iHTC Studio n'exploite pas de serveur principal pour ces données.

## Collecte de données

Nous n'opérons pas d'analyse, de publicité ou de suivi. Plus précisément :

- **Aucune information personnelle** n'est collectée par iHTC Studio (pas de nom, email, numéro de téléphone ou compte iHTC Studio).
- **Aucune analyse d'utilisation** ou SDK de rapport d'erreur n'est intégré.
- **Vos données d'apprentissage** (favoris, résultats aux quiz, mauvaises réponses) restent sur vos appareils et, si vous activez la synchronisation, dans **Apple iCloud** — pas sur les serveurs iHTC Studio.
- **Pas de cookies ni de trackers tiers** dans l'application.

## Comment fonctionne l'application

iLinux stocke toutes les données générées par l'utilisateur (favoris, vues récentes, résultats de session de quiz, enregistrements de réponses erronées, préférences de plate-forme shell, portée des favoris, bibliothèque de commandes de widget et préférences d'application) localement sur votre appareil :

- Toutes les données de commande (résumés JSON et documentation Markdown pour **Linux, CMD et PowerShell**) sont regroupées dans l'application et ne sont jamais récupérées depuis un serveur externe.
- Aucune connexion Internet n'est requise pour parcourir les commandes ou répondre à des quiz.
- La **synchronisation iCloud** facultative utilise le **NSUbiquitousKeyValueStore** d'Apple lorsque vous êtes connecté à iCloud et laissez la synchronisation activée. Vous pouvez le désactiver par appareil dans Paramètres.
- L'ouverture de liens externes depuis l'application (par exemple, en appuyant sur une URL dans la section Commentaires) utilise le comportement réseau iOS standard ; la page liée est chargée par votre appareil directement depuis son hôte, et non via un serveur iHTC Studio.
- La **vérification de version de l'App Store** facultative (`AppStoreVersionChecker`) envoie une seule requête en lecture seule à l'API publique de recherche iTunes pour comparer la version installée avec la dernière version. Aucune donnée personnelle n'est envoyée dans cette demande.

## Autorisations

iLinux demande l'accès à la **Photothèque** uniquement lorsque vous choisissez de **enregistrer une carte de partage ou une capture d'écran de commande** dans Photos. Aucun accès à la caméra, au microphone, à l’emplacement ou aux contacts n’est requis.

## Stockage des données

| Données | Emplacement de stockage |
|------|-----------------|
| Favoris, vues récentes, enregistrements de mauvaises réponses, statut d'apprentissage (par plateforme) | Paramètres utilisateur par défaut locaux/groupe d'applications sur votre appareil |
| Progression du quiz et résultats de la session quotidienne (saisis par date et plate-forme shell) | Bac à sable d'application locale sur votre appareil |
| Thème, langue, disposition en liste/grille, plateforme shell, portée des favoris, bibliothèque de widgets | Paramètres utilisateur par défaut locaux/groupe d'applications sur votre appareil |
| Miroir de synchronisation iCloud (facultatif) | Apple iCloud Key-Value Storage (`crossSync.*` keys) — favourites, quiz progress, theme, app preferences |
| Instantané du widget (iOS/iPad uniquement) | Conteneur de groupe d'applications (`group.com.iHTCboy.iLinuxs`) |

Aucune donnée n'est stockée sur un serveur exploité par iHTC Studio. Les données iCloud facultatives sont régies par les conditions iCloud d'Apple.

## Synchronisation iCloud (facultatif)

Lorsque **iCloud Sync** est activé et que vous êtes connecté à iCloud :

- Données synchronisées : **progression de l'apprentissage** (favoris, récents, statut d'apprentissage, résultats du quiz, enregistrements de mauvaises réponses), **thème** et **préférences d'application** (langue, plate-forme shell, portée des favoris, paramètres de liste/grille).
- Stockage : Apple **iCloud Key-Value Storage**, associé à votre identifiant Apple.
- Fusionner : les mises à jour en conflit sont fusionnées sur l'appareil (par exemple, union des favoris, derniers horodatages).
- Désinscription : désactivez-la dans **Paramètres → iCloud Sync** sur n'importe quel appareil ; cet appareil arrête le téléchargement et la fusion mais conserve les données locales.
- iHTC Studio ne peut pas lire votre conteneur iCloud.

## Groupe d’applications (extension de widget – iOS/iPad uniquement)

iLinux utilise un groupe d'applications (`group.com.iHTCboy.iLinuxs`) pour partager une petite quantité de données avec son extension de widget Écran d'accueil. Ces données comprennent :

- The selected content language code (e.g. `en`, `zh-Hans`)
- Un instantané des couleurs du thème (valeurs d'accent hexadécimal et de dégradé)
- Un résumé de vos progrès d'apprentissage (nombre de favoris, statistiques de quiz) pour l'affichage du widget
- La **bibliothèque de commandes de widget** sélectionnée (Linux / CMD / PowerShell)
- Le compteur de lecture aléatoire du widget Daily Command (un simple entier utilisé pour choisir la commande suivante)

Ces données sont écrites dans un conteneur partagé sur votre appareil uniquement et ne sont jamais transmises nulle part.

## Ce qu'iLinux n'est pas

iLinux n'exécute pas de commandes shell, n'ouvre pas de sessions SSH et n'accède pas aux systèmes distants. Aucune entrée de ligne de commande que vous pourriez saisir ailleurs n'est collectée par cette application.

## Achat intégré

iLinux inclut une option facultative de pourboire/achat. Toutes les transactions de paiement sont gérées exclusivement par **le framework StoreKit d'Apple**. iHTC Studio ne reçoit, ne traite ni ne stocke aucune information de carte de paiement ou de facturation.

## Confidentialité des enfants

iLinux ne collecte sciemment aucune donnée personnelle de qui que ce soit, y compris des enfants de moins de 13 ans. Puisque nous ne collectons aucune donnée, aucune disposition particulière n'est nécessaire.

## Modifications de cette politique

Nous pouvons mettre à jour cette politique de confidentialité de temps à autre. Tout changement sera publié sur cette page avec une date mise à jour. Nous vous encourageons à consulter cette page périodiquement.

## Contactez-nous

Si vous avez des questions concernant cette politique de confidentialité, veuillez nous contacter :

- **E-mail :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="tr" markdown="1">

iHTC Studio ("biz", "bize" veya "bizim") iLinux'u ("Linux" olarak da bilinir) oluşturdu. Bu sayfa, uygulamamızı kullandığınızda kişisel verilerinizin toplanması, kullanılması ve ifşa edilmesine ilişkin politikalarımız hakkında sizi bilgilendirir.

## Özet

**iLinux analiz toplamaz veya kişisel verileri satmaz.** Komut kitaplıkları cihazınızda tamamen çevrimdışı çalışır. İsteğe bağlı **iCloud senkronizasyonu** (etkinleştirildiğinde ve iCloud'da oturum açtığınızda) favorileri, sınav ilerlemesini, temayı ve görüntüleme tercihlerini Apple Kimliğiniz altındaki **iCloud Anahtar-Değer Depolama alanınızda** saklar — iHTC Studio bu veriler için bir arka uç sunucusu çalıştırmaz.

## Veri Toplama

Analitik, reklam veya izleme işletmiyoruz. Özellikle:

- **Hiçbir kişisel bilgi** iHTC Studio tarafından toplanmaz (isim, e-posta, telefon numarası veya iHTC Studio hesabı yok).
- **Kullanım analitiği yoktur** veya kilitlenme raporlama SDK'ları entegre değildir.
- **Öğrenim verileriniz** (favoriler, sınav puanları, yanlış cevaplar) cihazlarınızda kalır ve senkronizasyonu etkinleştirirseniz iHTC Studio sunucularında değil **Apple iCloud**'da kalır.
- **Uygulamada çerez veya üçüncü taraf izleyici yoktur**.

## Uygulama Nasıl Çalışır?

iLinux, kullanıcı tarafından oluşturulan tüm verileri (favoriler, son görünümler, sınav oturumu sonuçları, yanlış cevap kayıtları, kabuk platformu tercihi, favori kapsamı, widget komut kitaplığı ve uygulama tercihleri) yerel olarak cihazınızda saklar:

- Tüm komut verileri (**Linux, CMD ve PowerShell** için JSON özetleri ve Markdown belgeleri) uygulamanın içinde paketlenir ve hiçbir zaman herhangi bir harici sunucudan getirilmez.
- Komutlara göz atmak veya sınavlara girmek için internet bağlantısı gerekmez.
- İsteğe bağlı **iCloud senkronizasyonu**, iCloud'da oturum açtığınızda ve senkronizasyonu etkin bıraktığınızda Apple'ın **NSUbiquitousKeyValueStore** özelliğini kullanır. Ayarlar'da her cihaz için bunu kapatabilirsiniz.
- Uygulamanın içinden harici bağlantıları açmak (ör. Geri Bildirim bölümünde bir URL'ye dokunmak) standart iOS ağ oluşturma davranışını kullanır; bağlantılı sayfa herhangi bir iHTC Studio sunucusu aracılığıyla değil, cihazınız tarafından doğrudan ana bilgisayardan yüklenir.
- The optional **App Store version check** (`AppStoreVersionChecker`) makes a single read-only request to the public iTunes Lookup API to compare the installed version with the latest release. No personal data is sent in this request.

## İzinler

iLinux, **Fotoğraf Kitaplığı** erişimini yalnızca Fotoğraflar'a **bir paylaşım kartı kaydetmeyi veya ekran görüntüsünü komut etmeyi** seçtiğinizde ister. Hiçbir kamera, mikrofon, konum veya kişi erişimi gerekmez.

## Veri Depolama

| Veri | Depolama Konumu |
|------|-----------------|
| Favoriler, son görüntülemeler, yanlış cevap kayıtları, öğrenme durumu (platform başına) | Cihazınızdaki Yerel Kullanıcı Varsayılanları / Uygulama Grubu |
| Sınav ilerlemesi ve günlük oturum sonuçları (tarihe ve kabuk platformuna göre anahtarlanmıştır) | Cihazınızdaki yerel uygulama sanal alanı |
| Tema, dil, liste/ızgara düzeni, kabuk platformu, sık kullanılanlar kapsamı, widget kitaplığı | Cihazınızdaki Yerel Kullanıcı Varsayılanları / Uygulama Grubu |
| iCloud senkronizasyon aynası (isteğe bağlı) | Apple iCloud Anahtar-Değer Depolaması (`crossSync.*` tuşları) — favoriler, test ilerleme durumu, tema, uygulama tercihleri |
| Widget anlık görüntüsü (yalnızca iOS/iPad) | Uygulama Grubu kapsayıcısı (`group.com.iHTCboy.iLinuxs`) |

iHTC Studio tarafından çalıştırılan herhangi bir sunucuda hiçbir veri depolanmaz. İsteğe bağlı iCloud verileri, Apple'ın iCloud koşullarına tabidir.

## iCloud Senkronizasyonu (İsteğe bağlı)

**iCloud Senkronizasyonu** etkinleştirildiğinde ve iCloud'da oturum açtığınızda:

- Senkronize edilen veriler: **öğrenme ilerlemesi** (favoriler, en son olanlar, öğrenme durumu, test puanları, yanlış cevap kayıtları), **tema** ve **uygulama tercihleri** (dil, kabuk platformu, favorilerin kapsamı, liste/tablo ayarları).
- Depolama: Apple Kimliğinizle ilişkili Apple **iCloud Anahtar-Değer Depolama Alanı**.
- Birleştirme: Çakışan güncellemeler cihazda birleştirilir (ör. favoriler birliği, en son zaman damgaları).
- Devre dışı bırakma: herhangi bir cihazda **Ayarlar → iCloud Senkronizasyonu** bölümünden devre dışı bırakın; bu cihaz yüklemeyi ve birleştirmeyi durdurur ancak yerel verileri tutar.
- iHTC Studio, iCloud kapsayıcınızı okuyamıyor.

## Uygulama Grubu (Widget Uzantısı — yalnızca iOS/iPad)

iLinux, Ana Ekran widget uzantısıyla az miktarda veri paylaşmak için bir Uygulama Grubu (`group.com.iHTCboy.iLinuxs`) kullanır. Bu veriler şunları içerir:

- Seçilen içerik dili kodu (ör. `en`, `zh-Hans`)
- Bir tema rengi anlık görüntüsü (vurgu onaltılı ve degrade değerleri)
- Widget ekranı için öğrenme ilerlemenizin bir özeti (favoriler sayısı, sınav istatistikleri)
- Seçilen **widget komut kitaplığı** (Linux / CMD / PowerShell)
- Günlük Komut widget'ı karıştırma sayacı (sonraki öne çıkan komutu seçmek için kullanılan basit bir tamsayı)

Bu veriler yalnızca cihazınızdaki paylaşılan bir kaba yazılır ve hiçbir zaman hiçbir yere iletilmez.

## iLinux Ne Değildir?

iLinux kabuk komutlarını çalıştırmaz, SSH oturumlarını açmaz veya uzak sistemlere erişmez. Başka bir yere yazabileceğiniz hiçbir komut satırı girişi bu uygulama tarafından toplanmaz.

## Uygulama İçi Satın Alma

iLinux isteğe bağlı bir ipucu/satın alma seçeneği içerir. Tüm ödeme işlemleri yalnızca **Apple'ın StoreKit çerçevesi** tarafından gerçekleştirilir. iHTC Studio, herhangi bir ödeme kartı bilgisini veya fatura ayrıntısını almaz, işlemez veya saklamaz.

## Çocukların Gizliliği

iLinux, 13 yaşın altındaki çocuklar da dahil olmak üzere hiç kimseden bilerek herhangi bir kişisel veri toplamaz. Hiçbir şekilde veri toplamadığımız için özel hükümlere gerek yoktur.

## Bu Politikadaki Değişiklikler

Bu Gizlilik Politikasını zaman zaman güncelleyebiliriz. Herhangi bir değişiklik güncellenmiş bir tarihle bu sayfada yayınlanacaktır. Bu sayfayı periyodik olarak incelemenizi öneririz.

## Bize Ulaşın

Bu Gizlilik Politikası hakkında herhangi bir sorunuz varsa lütfen bizimle iletişime geçin:

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
