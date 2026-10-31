---
layout: doc
permalink: /iWidget/privacy/
title: iWidget — Privacy Policy
app_id: iWidget
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iWidget (爱组件) — widget designer, on-device designs, optional iCloud, WeatherKit & HealthKit when enabled.
---

<section lang="en" markdown="1">

**Last updated:** September 30, 2026

iHTC Studio ("we", "us" or "our") built **iWidget** (also known as "爱组件" / "愛組件", Bundle ID `com.iHTCboy.iWidget`). This Privacy Policy explains what data is (and is not) handled when you use the app and its widget extension. **Apple App Review** and users may rely on this page as the public privacy policy. For App Store Connect, open this [Privacy Policy](../privacy) page in your browser and copy the address from the address bar (the public site domain may change over time).

## Summary (Apple Privacy Nutrition Label alignment)

| Topic | Our practice |
|-------|----------------|
| Account | **Not required** — no registration or sign-in with iHTC Studio |
| Data collection by iHTC Studio | **Data Not Collected** — we do **not** operate a backend that receives your widget designs, wallpapers, or calendar data |
| Advertising / analytics | **None** — no ads, no third-party analytics or tracking SDKs |
| Core calendar & almanac | Computed **on device** from bundled tables; optional holiday JSON may be fetched from a public GitHub mirror (see below) |
| Weather | **Apple WeatherKit** when you enable weather blocks or Today weather — requests go to **Apple**, not iHTC Studio |
| Optional Apple services | **iCloud (CloudKit)** for design sync, **HealthKit** (read steps/distance), **Location When In Use** (or manual city), **local notifications**, **Background App Refresh** task |

## Data Collection

- **No account** — You can use the app without creating an account with us.
- **No advertising or analytics SDK** — The app does not show ads or send usage analytics to iHTC Studio.
- **No iHTC Studio cloud for your designs** — Widget layouts, cropped wallpapers, countdowns, and caches live in the **App Group** on your device (and optionally in **your** iCloud container). We do not host a server that stores your boards.

## Network Use

| Feature | What happens |
|---------|----------------|
| **WeatherKit** | Your device asks Apple for forecast data for your chosen location or city. Weather UI shows **Apple Weather** attribution where required. |
| **Statutory holiday updates** | The app may download public holiday JSON (e.g. from the open **holiday-cn** project) roughly every few days to refresh work/rest marks. No personal identifiers are sent by us. |
| **Optional open-source fonts** | Selected open-source faces ship with the main app and are registered before widget timelines render. The app does not download extra font files. |
| **Tip Developer** | Optional **StoreKit** consumable processed by Apple. We do not receive payment card numbers. |
| **Feedback email** | If you choose **Send feedback**, Mail compose may attach non-secret diagnostics (version, device model). You control sending. |

All other features — lunar calendar, almanac, editor, previews, widgets (except live weather fetch), notifications scheduling — work **offline** after install.

## Data Stored on Your Device (App Group)

Design files, caches, and preferences are stored under App Group `group.com.iHTCboy.iWidget`, for example:

| Data | Purpose |
|------|---------|
| `designs/*.json` | Saved widget board layouts |
| `images/*`, `wallpaper/*` | Cropped wallpaper slots (light/dark) |
| `countdowns/items.json` | Countdown list |
| `cache/weather.json` | Weather snapshot cache |
| `cache/battery.json`, `cache/storage.json`, `cache/music.json`, `cache/steps.json` | Device block snapshots (iOS) |
| `cache/holidays/{year}.json` | Downloaded statutory holiday tables |
| UserDefaults keys | Language, theme, festival filters, widget session cursors, stale design IDs, etc. |

Uninstalling the app removes sandbox and App Group data subject to iOS/macOS behavior.

## iCloud Sync (Optional, Off by Default)

When you enable **iCloud** in Settings, the app uses **CloudKit** private database `iCloud.com.iHTCboy.iWidget` (zone **Designs**) via `CKSyncEngine` to sync:

- Design JSON summaries and full documents
- Cropped wallpaper assets associated with designs

Traffic goes to **Apple iCloud** under **your Apple ID**. We cannot read your iCloud contents. Turning iCloud off stops sync; local copies remain on device until you delete them.

## Permissions

| Permission | When | Why |
|------------|------|-----|
| **Location When In Use** | You enable location-based weather | Resolve city for WeatherKit; you may use **manual city** instead |
| **HealthKit (read)** | You enable step blocks | Read today’s steps / walking distance for widget display |
| **Apple Music / Media** | Now Playing block | Read currently playing title & artwork (Info.plist usage strings) |
| **Notifications** | You enable reminder categories | Schedule local holiday / countdown / workday reminders |
| **Background App Refresh** | System allows | Periodic refresh of weather/device caches (~6 h) |
| **iCloud** | You toggle sync | Design backup across your devices |

We do **not** request Contacts, Camera, Microphone recording, or App Tracking Transparency for ads.

## Widget Extension

The widget extension reads the **same App Group** as the app. It renders the design you selected in the widget configuration UI. Interactive intents (refresh weather, cycle countdown, shift month) run on device. Weather fetches in widgets are time-limited (e.g. ~8 s) and may use cached data on failure.

## Privacy Manifest

The app ships `PrivacyInfo.xcprivacy` declaring **UserDefaults** access for reason **CA92.1** (app functionality).

## Children’s Privacy

We do not knowingly collect personal information from children. Because we do not operate a data collection backend for this app, no special child account is required.

## Changes

We may update this policy. Material changes will be reflected on this page with an updated date.

## Membership

Apple processes payments; we do not receive card details. The app processes verified product and transaction identifiers, validity dates and renewal states locally to provide editing access. The device Keychain stores the free experience start date and may retain it after reinstalling. We do not send these records to a developer server or include membership credentials in shared designs or iCloud design sync. Public policy pages are hosted by GitHub Pages, which receives normal web requests.

## Contact

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="zh-CN" markdown="1">

**最后更新：** 2026 年 9 月 30 日

爱火腿肠工作室（iHTC Studio）（「我们」）开发了 **爱组件**（iWidget / 愛組件，Bundle ID `com.iHTCboy.iWidget`）。本隐私政策说明你在使用主 App 与小组件扩展时，数据如何被处理。本页可供 **App Store 审核**与用户查阅。填写 App Store Connect 时：打开本站 [隐私政策](../privacy) 页，从浏览器地址栏复制当前网址（站点域名日后可能变更）。

## 概要（与 Apple 隐私标签对齐）

| 主题 | 做法 |
|------|------|
| 账号 | **不需要** — 无需向爱火腿肠工作室注册或登录 |
| 我们侧数据收集 | **Data Not Collected** — **不**运营接收你的设计、壁纸或日历内容的后端 |
| 广告 / 统计 | **无** — 无广告、无第三方分析或追踪 SDK |
| 日历与黄历 | **本机离线**计算；法定调休数据可能从公开 GitHub 镜像按需下载 |
| 天气 | 启用天气相关能力时使用 **Apple WeatherKit**，请求发往 **Apple** |
| 可选 Apple 服务 | **iCloud（CloudKit）** 同步设计、**HealthKit**（读步数/距离）、**使用期间定位**（或手动城市）、**本地通知**、**后台刷新**任务 |

## 数据收集

- **无账号** — 无需创建我们侧账号即可使用。
- **无广告或分析 SDK** — 不向爱火腿肠工作室上报使用统计。
- **无设计云备份（我们侧）** — 看板布局、裁切壁纸、倒数与缓存保存在 **App Group**（及可选 **你的 iCloud**）。

## 网络使用

| 功能 | 说明 |
|------|------|
| **WeatherKit** | 设备向 Apple 请求所选位置/城市的预报；界面按要求展示 **Apple Weather** 标识。 |
| **法定假日更新** | 可能每隔数日下载公开 holiday JSON（如 holiday-cn 项目），用于刷新休/班标记；我们不附带个人标识。 |
| **开源字体** | 选定的开源字体由主 App 随包提供，小组件出时间线前注册；不会另外从网络下载字体文件。 |
| **开发者赞赏** | 可选 **StoreKit** 消耗型，由 Apple 处理支付。 |
| **反馈邮件** | 你选择发送时，邮件可能附带版本、机型等非敏感诊断信息。 |

除上述外，农历、黄历、编辑器、预览、小组件渲染（除实时天气拉取）、通知调度等均在安装后 **可离线** 使用。

## 本机存储（App Group）

数据位于 App Group `group.com.iHTCboy.iWidget`，例如：

| 数据 | 用途 |
|------|------|
| `designs/*.json` | 已保存的小组件看板 |
| `images/*`、`wallpaper/*` | 深浅色壁纸槽位裁切图 |
| `countdowns/items.json` | 倒数日列表 |
| `cache/weather.json` 等 | 天气与设备积木缓存 |
| `cache/holidays/{year}.json` | 下载的法定调休表 |
| UserDefaults | 语言、主题、节日筛选、小组件会话游标等 |

卸载 App 将按系统规则删除沙盒与 App Group 数据。

## iCloud 同步（可选，默认关）

在设置中开启 **iCloud** 后，通过 **CloudKit** 私有库 `iCloud.com.iHTCboy.iWidget`（**Designs** 区域）同步设计 JSON 与关联裁切壁纸。流量走 **你的 Apple ID** 的 iCloud；我们无法读取你的 iCloud 内容。关闭后停止同步，本机副本仍保留直至你删除。

## 权限

| 权限 | 触发时机 | 用途 |
|------|----------|------|
| **使用期间定位** | 启用定位天气 | WeatherKit 解析城市；可改用手动选城市 |
| **HealthKit（读）** | 启用步数积木 | 读取今日步数/步行距离 |
| **媒体与 Apple Music** | 正在播放积木 | 读取当前播放信息与封面 |
| **通知** | 开启提醒类别 | 本地调度调休/节日/节气/倒数提醒 |
| **后台 App 刷新** | 系统允许 | 约 6 小时刷新天气/设备等缓存 |
| **iCloud** | 你打开同步开关 | 跨设备备份设计 |

**不**请求通讯录、相机、麦克风录音或用于广告的 ATT。

## 小组件扩展

扩展与主 App 共用 **App Group**，渲染你在系统小组件配置里选择的设计。交互 Intent（刷新天气、切换倒数、翻月等）在本机执行；扩展内拉天气有时间上限，失败时可回退缓存。

## 隐私清单

App 内置 `PrivacyInfo.xcprivacy`，声明因 **CA92.1**（App 功能）访问 **UserDefaults**。

## 儿童隐私

我们不会有意收集儿童个人信息；本 App 不运营用户数据后端。

## 政策变更

我们可能更新本页，并在文首更新日期。

## 会员

Apple 处理付款，我们不接收银行卡信息。App 在本地处理经验证的商品、交易标识、有效期与续订状态，用于提供编辑权限。本机 Keychain 保存免费体验起点，重新安装后可能保留。上述记录不发送到开发者服务器，会员凭据不随设计分享或 iCloud 设计同步。公开政策网页由 GitHub Pages 托管，托管方会接收正常网页请求。

## 联系

- **邮箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="zh-TW" markdown="1">

**最後更新：** 2026 年 9 月 30 日

愛火腿腸工作室（iHTC Studio）（「我們」）開發了 **愛組件**（iWidget / 爱组件，Bundle ID `com.iHTCboy.iWidget`）。本隱私政策說明你在使用主 App 與小工具延伸功能時，資料如何被處理。本頁可供 **App Store 審核**與使用者查閱。填寫 App Store Connect 時：打開本站 [隱私政策](../privacy) 頁，從瀏覽器網址列複製目前網址（站點網域日後可能變更）。

## 概要（與 Apple 隱私標籤對齊）

| 主題 | 做法 |
|------|------|
| 帳號 | **不需要** — 無需向愛火腿腸工作室註冊或登入 |
| 我們側資料收集 | **Data Not Collected** — **不**營運接收你的設計、桌布或日曆內容的後端 |
| 廣告 / 統計 | **無** — 無廣告、無第三方分析或追蹤 SDK |
| 日曆與黃曆 | **本機離線**計算；法定調休資料可能從公開 GitHub 鏡像按需下載 |
| 天氣 | 啟用天氣相關能力時使用 **Apple WeatherKit**，請求送往 **Apple** |
| 可選 Apple 服務 | **iCloud（CloudKit）** 同步設計、**HealthKit**（讀步數/距離）、**使用期間定位**（或手動城市）、**本地通知**、**背景重新整理**任務 |

## 資料收集

- **無帳號** — 無需建立我們側帳號即可使用。
- **無廣告或分析 SDK** — 不向愛火腿腸工作室上報使用統計。
- **無設計雲備份（我們側）** — 看板版面、裁切桌布、倒數與快取保存在 **App Group**（及可選 **你的 iCloud**）。

## 網路使用

| 功能 | 說明 |
|------|------|
| **WeatherKit** | 裝置向 Apple 請求所選位置/城市的預報；介面按要求展示 **Apple Weather** 標示。 |
| **法定假日更新** | 可能每隔數日下載公開 holiday JSON（如 holiday-cn 專案），用於更新休/班標記。 |
| **開源字體** | 選定的開源字體由主 App 隨包提供，小工具出時間線前註冊；不會另外從網路下載字型檔。 |
| **開發者打賞** | 可選 **StoreKit** 消耗型，由 Apple 處理付款。 |
| **反馈郵件** | 你選擇傳送時，郵件可能附版本、機型等非敏感診斷資訊。 |

除上述外，農曆、黃曆、編輯器、預覽、小工具渲染（除即時天氣拉取）、通知排程等均在安裝後 **可離線** 使用。

## 本機儲存（App Group）

資料位於 App Group `group.com.iHTCboy.iWidget`，例如：`designs/*.json`、裁切桌布、倒數列表、天氣/裝置快取、調休表與 UserDefaults 偏好。

卸載 App 將依系統規則刪除沙盒與 App Group 資料。

## iCloud 同步（可選，預設關）

開啟 **iCloud** 後，透過 **CloudKit** 私有庫同步設計 JSON 與裁切桌布；流量走 **你的 Apple ID** 的 iCloud。關閉後停止同步。

## 權限

定位（使用期間）或手動城市、HealthKit 讀取步數、媒體/Apple Music（正在播放）、通知、背景重新整理、iCloud — 均仅在对应功能开启时使用。**不**請求通訊錄、相機、麥克風錄音或用于廣告的 ATT。

## 小工具延伸功能

與主 App 共用 **App Group**；互動 Intent 在本機執行；拉取天氣有時間上限並可回退快取。

## 隱私清單

App 內含 `PrivacyInfo.xcprivacy`，声明因 **CA92.1** 存取 **UserDefaults**。

## 兒童隱私

我們不會有意收集兒童個人資訊。

## 政策變更

我們可能更新本頁並調整日期。

## 會員

Apple 處理付款，我們不接收銀行卡資訊。App 在本機處理經驗證的商品、交易識別碼、有效期與續訂狀態，用於提供編輯權限。裝置 Keychain 儲存免費體驗起點，重新安裝後可能保留。上述紀錄不傳送至開發者伺服器，會員憑證不隨設計分享或 iCloud 設計同步。公開政策網頁由 GitHub Pages 代管，代管方會接收正常網頁請求。

## 聯絡

- **信箱：** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ja" markdown="1">

**最終更新:** 2026年9月30日

iHTC Studio（「当社」）は **iWidget**（「爱组件」/「愛組件」、Bundle ID `com.iHTCboy.iWidget`）を開発しました。本プライバシーポリシーは、アプリとウィジェット拡張利用時に扱う（および扱わない）データを説明します。**Apple App Review** とユーザーは本ページを公開プライバシーポリシーとして参照できます。App Store Connect ではブラウザで [Privacy Policy](../privacy) を開き、アドレスバーから URL をコピーしてください（公開ドメインは将来変わる場合があります）。

## 概要（Apple Privacy Nutrition Label 整合）

| 項目 | 当社の方針 |
|------|------------|
| アカウント | **不要** — iHTC Studio への登録・サインインなし |
| iHTC Studio によるデータ収集 | **Data Not Collected** — ウィジェットデザイン・壁紙・カレンダーデータを受け取る backend を運用しない |
| 広告 / analytics | **なし** — 広告、第三者 analytics、トラッキング SDK なし |
| コア暦・黄历 | **端末内** 同梱表から計算；任意で祝日 JSON を公開 GitHub ミラーから取得（下記） |
| 天気 | 天気ブロックまたは今日の天気有効時 **Apple WeatherKit** — リクエストは **Apple** へ、iHTC Studio へではない |
| 任意 Apple サービス | デザイン同期の **iCloud (CloudKit)**、**HealthKit**（歩数/距離読取）、**使用中のみ位置**（または手動都市）、**ローカル通知**、**Background App Refresh** |

## データ収集

- **アカウントなし** — 当社アカウントなしで利用可能。
- **広告・analytics SDK なし** — iHTC Studio へ usage analytics を送らない。
- **デザイン用 iHTC Studio クラウドなし** — レイアウト、クロップ壁紙、カウントダウン、キャッシュは **App Group**（任意で **あなたの** iCloud）。当社は boards をホストしない。

## ネットワーク利用

| 機能 | 内容 |
|------|------|
| **WeatherKit** | 選択位置/都市の予報を Apple に問い合わせ。UI に **Apple Weather** 帰属表示。 |
| **法定休日更新** | 公開祝日 JSON（例：**holiday-cn**）を数日ごとに取得し休/班を更新。個人識別子は当社から送らない。 |
| **任意 OSS フォント** | 選択したオープンソースフォントはメイン App に同梱され、ウィジェット描画前に登録。追加のフォントファイルはダウンロードしません。 |
| **開発者へのチップ** | 任意 StoreKit 消耗型は Apple が処理。カード番号は当社が受け取らない。 |
| **Feedback メール** | 送信時 Mail が非秘密診断（バージョン、機種）を添付可能。送信はユーザー操作。 |

暦・黄历・エディタ・プレビュー・ウィジェット（ライブ天気取得除く）・通知スケジュールは、インストール後 **オフライン** で動作。

## 端末保存（App Group）

App Group `group.com.iHTCboy.iWidget` 例：

| データ | 目的 |
|------|------|
| `designs/*.json` | 保存ウィジェットボード |
| `images/*`, `wallpaper/*` | クロップ壁紙スロット（明暗） |
| `countdowns/items.json` | カウントダウン一覧 |
| `cache/weather.json` | 天気スナップショット |
| `cache/battery.json` 等 | デバイスブロックスナップショット (iOS) |
| `cache/holidays/{year}.json` | ダウンロードした法定休日表 |
| UserDefaults | 言語、テーマ、祝日 filt、ウィジェットセッション、失効デザイン ID 等 |

アンインストールで sandbox / App Group データは OS 挙動に従い削除。

## iCloud 同期（任意、既定オフ）

**設定** で **iCloud** を有効にすると **CloudKit** 私有 DB `iCloud.com.iHTCboy.iWidget`（ゾーン **Designs**）、`CKSyncEngine` で同期：

- デザイン JSON サマリーと全文
- デザイン関連クロップ壁紙

通信は **Apple iCloud**（**あなたの Apple ID**）。当社は iCloud 内容を読めない。オフで同期停止；ローカルは削除するまで残る。

## 権限

| 権限 | タイミング | 理由 |
|------|------------|------|
| **使用中のみ位置** | 位置ベース天気 | WeatherKit 用都市；**手動都市** 可 |
| **HealthKit（読取）** | 歩数ブロック | 今日の歩数/歩行距離 |
| **Apple Music / メディア** | Now Playing | 再生中タイトル・アートワーク |
| **通知** | リマインダー有効 | 祝日/カウントダウン/休班のローカル通知 |
| **Background App Refresh** | システム許可 | 天気/デバイスキャッシュ定期更新（約 6 h） |
| **iCloud** | 同期トグル | 端末間デザインバックアップ |

連絡先、カメラ、マイク録音、広告 ATT は **要求しません**。

## ウィジェット拡張

拡張はアプリと **同一 App Group** を読み、設定 UI で選んだデザインを描画。インタラクティブ intent（天気更新、カウントダウンサイクル、月移動）は端末内。ウィジェットの天気取得は時間制限（例 ~8 s）、失敗時キャッシュ。

## プライバシーマニフェスト

`PrivacyInfo.xcprivacy` で **UserDefaults** を理由 **CA92.1**（アプリ機能）として宣言。

## 児童のプライバシー

故意に児童の個人情報を収集しません。データ収集 backend を運用しないため、特別な児童アカウントは不要です。

## 変更

方針を更新する場合、本ページの日付を更新します。

## メンバーシップ

Apple が決済を処理し、当社はカード情報を受け取りません。App は検証済みの商品・取引識別子、有効期限、更新状態を端末内で処理し、編集権限の提供に使います。無料体験の開始日は端末の Keychain に保存され、再インストール後も残る場合があります。これらの記録を開発者サーバーへ送ることはなく、メンバーシップ資格を共有デザインや iCloud デザイン同期に含めません。公開ポリシーページは GitHub Pages でホストされ、ホストは通常のウェブリクエストを受け取ります。

## お問い合わせ

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ko" markdown="1">

**최종 업데이트 / 最終更新:** September 30, 2026

iHTC Studio built **iWidget** (Bundle ID `com.iHTCboy.iWidget`). Public privacy policy for App Store Review.

## 요약
계정 불필요. **Data Not Collected** by iHTC Studio backend. No ads/analytics. Calendar on-device; WeatherKit to Apple; optional iCloud CloudKit, HealthKit, Location, notifications.

App Group `group.com.iHTCboy.iWidget` stores designs, wallpapers, countdowns, caches. Optional iCloud `iCloud.com.iHTCboy.iWidget`. Widget extension reads same App Group. PrivacyInfo.xcprivacy UserDefaults CA92.1.

## 멤버십

결제는 Apple이 처리하며 카드 정보는 받지 않습니다. 앱은 검증된 상품·거래 식별자, 유효 기간, 갱신 상태를 기기에서 처리해 편집 권한을 제공합니다. 무료 체험 시작일은 기기 Keychain에 저장되며 재설치 후에도 남을 수 있습니다. 이 기록은 개발자 서버로 보내지 않으며, 멤버십 자격은 공유 디자인이나 iCloud 디자인 동기화에 포함되지 않습니다. 공개 정책 페이지는 GitHub Pages에서 호스팅되며 호스트는 일반 웹 요청을 받습니다.

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ru" markdown="1">

**Обновлено:** 30 сентября 2026

**iWidget** — без аккаунта iHTC Studio, **Data Not Collected**, без рекламы/analytics. Календарь on-device, WeatherKit к Apple, опциональный iCloud CloudKit. App Group `group.com.iHTCboy.iWidget`.

## Членство

Платежи обрабатывает Apple, данные карты мы не получаем. Приложение локально обрабатывает проверенные идентификаторы товара и транзакции, сроки действия и состояние продления, чтобы открывать редактирование. Дата начала бесплатного периода хранится в Keychain устройства и может сохраниться после переустановки. Эти записи не отправляются на сервер разработчика и не включаются в общие макеты или синхронизацию дизайнов iCloud. Публичные страницы политики размещены на GitHub Pages, хост получает обычные веб-запросы.

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="th" markdown="1">

**อัปเดตล่าสุด:** 30 กันยายน 2026

**iWidget** — ไม่ต้องมีบัญชี **Data Not Collected** ไม่มีโฆษณา/analytics ปฏิทินบนเครื่อง WeatherKit ไป Apple iCloud เลือกได้ App Group `group.com.iHTCboy.iWidget`

## สมาชิก

Apple เป็นผู้ประมวลผลการชำระเงิน เราไม่ได้รับข้อมูลบัตร แอปประมวลผลรหัสสินค้าและธุรกรรมที่ตรวจสอบแล้ว วันหมดอายุ และสถานะต่ออายุในเครื่อง เพื่อให้สิทธิ์แก้ไข จุดเริ่มต้นของช่วงทดลองฟรีเก็บใน Keychain ของอุปกรณ์ และอาจยังอยู่หลังติดตั้งใหม่ บันทึกเหล่านี้ไม่ถูกส่งไปเซิร์ฟเวอร์นักพัฒนา และไม่รวมข้อมูลสมาชิกในดีไซน์ที่แชร์หรือซิงค์ iCloud หน้า नीतिสาธารณะโฮสต์บน GitHub Pages ซึ่งรับคำขอเว็บตามปกติ

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="de" markdown="1">

**Zuletzt aktualisiert:** 30. September 2026

iHTC Studio („wir“) entwickelte **iWidget** (Bundle ID `com.iHTCboy.iWidget`). Diese Datenschutzerklärung erklärt, welche Daten verarbeitet werden — und welche nicht.

## Überblick

| Thema | Praxis |
|-------|--------|
| Konto | **Nicht erforderlich** |
| iHTC Studio | **Data Not Collected** — kein Backend für Designs/Wallpaper |
| Werbung/Analytics | **Keine** |
| Kalender/Almanach | **On-device**; optional holiday JSON von GitHub |
| Wetter | **Apple WeatherKit** |
| Optional | **iCloud CloudKit**, **HealthKit**, **Standort**, Benachrichtigungen, Background Refresh |

Kein iHTC-Studio-Konto. Designs in App Group `group.com.iHTCboy.iWidget`. Optional iCloud `iCloud.com.iHTCboy.iWidget`. Berechtigungen nur bei aktivierten Features.

Details wie EN-Privacy: Widget-Erweitung, Privacy Manifest CA92.1, Kinder, Änderungen.

## Mitgliedschaft

Apple verarbeitet Zahlungen; Kartendaten erhalten wir nicht. Die App verarbeitet geprüfte Produkt- und Transaktionskennungen, Gültigkeitsdaten und Verlängerungsstatus lokal, um den Bearbeitungszugang bereitzustellen. Das Startdatum der kostenlosen Testphase liegt in der Geräte-Keychain und kann nach einer Neuinstallation erhalten bleiben. Diese Datensätze senden wir nicht an einen Entwickler-Server und legen keine Mitgliedschaftsdaten in geteilte Designs oder die iCloud-Design-Synchronisierung. Öffentliche Richtlinien-Seiten liegen auf GitHub Pages; der Hoster empfängt normale Webanfragen.

## Kontakt

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="fr" markdown="1">

**Dernière mise à jour :** 30 septembre 2026

iHTC Studio a développé **iWidget** (`com.iHTCboy.iWidget`). Pas de compte. **Data Not Collected**. Pas de pub/analytics. Almanach on-device ; WeatherKit vers Apple ; iCloud CloudKit optionnel. App Group et iCloud comme ci-dessus.

## Adhésion

Apple traite les paiements ; nous ne recevons pas les données de carte. L’app traite localement les identifiants de produit et de transaction vérifiés, les dates de validité et l’état de renouvellement pour fournir l’accès à l’édition. La date de début de l’essai gratuit est stockée dans le Trousseau de l’appareil et peut rester après une réinstallation. Nous n’envoyons pas ces enregistrements vers un serveur développeur et n’incluons pas les justificatifs d’adhésion dans les designs partagés ou la sync iCloud. Les pages publiques de politique sont hébergées par GitHub Pages, qui reçoit les requêtes web habituelles.

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="tr" markdown="1">

**Son güncelleme:** 30 Eylül 2026

**iWidget** — hesap yok, **Data Not Collected**, reklam/analytics yok. Takvim cihaz içi, WeatherKit Apple'a, isteğe bağlı iCloud CloudKit. App Group `group.com.iHTCboy.iWidget`.

## Üyelik

Ödemeleri Apple işler; kart bilgisi almayız. Uygulama, düzenleme erişimi için doğrulanmış ürün ve işlem kimliklerini, geçerlilik tarihlerini ve yenileme durumunu cihazda işler. Ücretsiz denemenin başlangıcı cihaz Keychain’inde saklanır ve yeniden kurulumdan sonra kalabilir. Bu kayıtları geliştirici sunucusuna göndermeyiz; üyelik bilgilerini paylaşılan tasarımlara veya iCloud tasarım senkronuna eklemeyiz. Kamuya açık politika sayfaları GitHub Pages’te barınır; barındırıcı olağan web isteklerini alır.

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
