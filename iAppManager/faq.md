---
layout: doc
title: iAppManager — FAQ
app_id: iAppManager
doc_title_en: Frequently Asked Questions
doc_title_zh_cn: 常见问题
doc_title_zh_tw: 常見問題
description: FAQ for iAppManager — API Key login, ASC features, IPA upload, TestFlight, widgets, and privacy.
---

<section lang="en" markdown="1">

### What is iAppManager?

A **native App Store Connect workstation** for iPhone, iPad and Mac. Sign in with an **API Key**, manage versions, screenshots, IAP, TestFlight, certificates, reports and reviews — traffic goes **straight to Apple**. No iHTC Studio account.

### How do I get an API Key?

1. Open [App Store Connect](https://appstoreconnect.apple.com) → **Users and Access** → **Integrations** → **App Store Connect API**
2. Create a key (Admin or App Manager recommended)
3. Download the `.p8` **once**, note **Issuer ID** and **Key ID**
4. Paste them in iAppManager (or pick the file). The in-app guide walks you through screenshots.

### Is my `.p8` uploaded to iHTC Studio?

**No.** The private key stays in **device Keychain**. Requests are signed locally and sent to `api.appstoreconnect.apple.com`. Removing an account deletes the local key.

### Do I need an Apple ID password inside the app?

**No.** Authentication is **API Key only** (Issuer ID + Key ID + `.p8`). You still use your Apple ID in Safari/ASC when a feature has no public API (e.g. privacy nutrition labels, free-app promo codes) — the app opens Apple’s site for those cases.

### Can I upload IPA / PKG without Transporter?

**Yes.** iAppManager uses Apple’s **Build Upload REST** (WWDC25). Prefer **Mac** for large files; iOS supports the same API but is less comfortable for big uploads.

### What does “on sale” mean in filters / widgets?

**Available in at least one App Store territory.** Pipeline buckets (waiting / in review / rejected / pending developer release) are tracked separately. Widget **Needs attention** = waiting + in review + rejected + pending release (local sum, not an ASC field).

### Hard vs soft checks before submit?

**Hard blockers** stop submit (e.g. build not ready, demo account required but missing). **Soft checks** warn (primary screenshot size, copyright, age rating, etc.) and you can confirm to continue. See Overview / Versions / Submissions `?` or `iappmanager://release-guide`.

### Which languages are supported?

**English · 简体中文 · 繁體中文**, follow system or force in Settings. Language hot-swap refreshes copy **without** remounting the root (navigation and drafts stay).

### Widgets don’t show live ASC numbers?

Widgets **do not call ASC**. The main app scans and writes a snapshot (~10‑minute TTL, same buckets as My Apps). Open the app and refresh the list (or force status refresh) to update.

### macOS vs iOS differences?

Both cover store, monetization, TestFlight, Game Center, users, reports, reviews and Webhooks. **Prefer Mac** for large IPA uploads and installing certificates into the system Keychain. Alternate app icons are **iOS only**.

### Where is the privacy policy URL for App Store Connect?

Open this site’s [Privacy Policy](../privacy) page and copy the URL from your browser’s address bar.

### System requirements?

iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+**.

### How do I contact support?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — typically within 48 hours.

</section>
<section lang="zh-CN" markdown="1">

### 爱应用者是什么？

面向 iPhone、iPad 与 Mac 的 **原生 App Store Connect 工作台**。用 **API Key** 登录，管理版本、截图、内购、TestFlight、证书、报表与评价——流量 **直连 Apple**。无需 iHTC Studio 账号。

### 如何获取 API Key？

1. 打开 [App Store Connect](https://appstoreconnect.apple.com) → **用户和访问** → **集成** → **App Store Connect API**
2. 创建密钥（建议 Admin 或 App Manager）
3. **仅一次**下载 `.p8`，记下 **Issuer ID** 与 **密钥 ID**
4. 在爱应用者粘贴（或选择文件）。应用内图文引导逐步说明。

### 我的 `.p8` 会上传到 iHTC Studio 吗？

**不会。** 私钥只存本机 **钥匙串**。请求在本地签名后发往 `api.appstoreconnect.apple.com`。移除账号会删除本机密钥。

### 应用内需要输入 Apple ID 密码吗？

**不需要。** 鉴权 **仅 API Key**（Issuer ID + 密钥 ID + `.p8`）。若某功能暂无公开 API（如隐私营养标签、免费 App 推广码），应用会打开 Apple 网页，由你在 Safari/ASC 侧使用 Apple ID。

### 不用 Transporter 能上传 IPA / PKG 吗？

**可以。** 爱应用者使用 Apple **Build Upload REST**（WWDC25）。大文件建议用 **Mac**；iOS 支持同 API，但大文件体验较弱。

### 筛选 / 小组件里的「已上架」是什么意思？

**至少一地区可用。** 流水线分桶（送审中 / 审核中 / 被拒 / 待开发者发布）单独统计。小组件 **需关注** = 送审中 + 审核中 + 被拒 + 待发布（本地合计，非 ASC 字段）。

### 提审前的硬拦截与软检查？

**硬拦截**会阻止送审（如构建未就绪、需要演示账号却缺失）。**软检查**会提示（主尺寸截图、版权、年龄分级等），可确认后继续。见 Overview / 版本 / 审核提交的 `?`，或 `iappmanager://release-guide`。

### 支持哪些语言？

**English · 简体中文 · 繁體中文**，可跟随系统或在设置强制。热切换文案时 **不会** 重挂根视图（导航与草稿保留）。

### 小组件为什么不是实时 ASC 数字？

小组件 **不直连 ASC**。由主应用扫描后写入快照（约 10 分钟 TTL，与「我的 App」同口径）。打开应用并刷新列表（或强制重扫状态）即可更新。

### macOS 与 iOS 有何差异？

两端均覆盖商店、变现、TestFlight、Game Center、用户、报表、评价与 Webhooks。**大体积 IPA** 与把证书装进系统钥匙串建议用 **Mac**。备用图标仅 **iOS**。

### App Store Connect 隐私政策网址？

打开本站的 [隐私政策](../privacy) 页面，从浏览器地址栏复制当前网址即可。

### 系统要求？

iPhone / iPad **iOS 17.0+**，Mac **macOS 14.0+**。

### 如何联系支持？

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)——通常 48 小时内回复。

</section>
<section lang="zh-TW" markdown="1">

### 愛應用者是什麼？

面向 iPhone、iPad 與 Mac 的 **原生 App Store Connect 工作台**。用 **API Key** 登入，管理版本、截圖、內購、TestFlight、憑證、報表與評價——流量 **直連 Apple**。無需 iHTC Studio 帳號。

### 如何取得 API Key？

1. 打開 [App Store Connect](https://appstoreconnect.apple.com) → **使用者和存取權限** → **整合** → **App Store Connect API**
2. 建立金鑰（建議 Admin 或 App Manager）
3. **僅一次**下載 `.p8`，記下 **Issuer ID** 與 **金鑰 ID**
4. 在愛應用者貼上（或選擇檔案）。應用內圖文引導逐步說明。

### 我的 `.p8` 會上傳到 iHTC Studio 嗎？

**不會。** 私鑰只存本機 **鑰匙圈**。請求在本地簽名後送往 `api.appstoreconnect.apple.com`。移除帳號會刪除本機金鑰。

### 應用內需要輸入 Apple ID 密碼嗎？

**不需要。** 鑑權 **僅 API Key**（Issuer ID + 金鑰 ID + `.p8`）。若某功能暫無公開 API（如隱私營養標籤、免費 App 推廣碼），應用會打開 Apple 網頁，由你在 Safari/ASC 側使用 Apple ID。

### 不用 Transporter 能上傳 IPA / PKG 嗎？

**可以。** 愛應用者使用 Apple **Build Upload REST**（WWDC25）。大檔建議用 **Mac**；iOS 支援同 API，但大檔體驗較弱。

### 篩選 / 小工具裡的「已上架」是什麼意思？

**至少一地區可用。** 流水線分桶（送審中 / 審核中 / 被拒 / 待開發者發佈）單獨統計。小工具 **需關注** = 送審中 + 審核中 + 被拒 + 待發佈（本地合計，非 ASC 欄位）。

### 送審前的硬攔截與軟檢查？

**硬攔截**會阻止送審（如建置未就緒、需要示範帳號卻缺失）。**軟檢查**會提示（主尺寸截圖、版權、年齡分級等），可確認後繼續。見 Overview / 版本 / 審核提交的 `?`，或 `iappmanager://release-guide`。

### 支援哪些語言？

**English · 簡體中文 · 繁體中文**，可跟隨系統或在設定強制。熱切換文案時 **不會** 重掛根檢視（導覽與草稿保留）。

### 小工具為什麼不是即時 ASC 數字？

小工具 **不直連 ASC**。由主應用掃描後寫入快照（約 10 分鐘 TTL，與「我的 App」同口徑）。打開應用並重新整理列表（或強制重掃狀態）即可更新。

### macOS 與 iOS 有何差異？

兩端均涵蓋商店、變現、TestFlight、Game Center、使用者、報表、評價與 Webhooks。**大體積 IPA** 與把憑證裝進系統鑰匙圈建議用 **Mac**。備用圖示僅 **iOS**。

### App Store Connect 隱私權政策網址？

打開本站的 [隱私權政策](../privacy) 頁面，從瀏覽器網址列複製目前網址即可。

### 系統需求？

iPhone / iPad **iOS 17.0+**，Mac **macOS 14.0+**。

### 如何聯絡支援？

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)——通常 48 小時內回覆。

</section>
<section lang="ja" markdown="1">

### iAppManager とは？

iPhone、iPad、Mac 向けの **ネイティブ App Store Connect ワークステーション**です。**API Key** でサインインし、バージョン、スクリーンショット、IAP、TestFlight、証明書、レポート、レビューを管理します。通信は **Apple に直接**。iHTC Studio アカウントは不要です。

### API Key の取得方法は？

1. [App Store Connect](https://appstoreconnect.apple.com) を開く → **Users and Access** → **Integrations** → **App Store Connect API**
2. キーを作成（Admin または App Manager を推奨）
3. `.p8` を **一度だけ** ダウンロードし、**Issuer ID** と **Key ID** を控える
4. iAppManager に貼り付ける（またはファイルを選択）。アプリ内ガイドがスクリーンショット付きで案内します。

### `.p8` は iHTC Studio にアップロードされますか？

**いいえ。** 秘密鍵は **デバイスの Keychain** にのみ保存されます。リクエストはローカルで署名され、`api.appstoreconnect.apple.com` に送信されます。アカウントを削除するとローカルキーも削除されます。

### アプリ内で Apple ID のパスワードは必要ですか？

**不要です。** 認証は **API Key のみ**（Issuer ID + Key ID + `.p8`）です。公開 API がない機能（プライバシー栄養表示ラベル、無料 App プロモコードなど）は Safari/ASC で Apple ID を使います——アプリは Apple のサイトを開きます。

### Transporter なしで IPA / PKG をアップロードできますか？

**はい。** iAppManager は Apple の **Build Upload REST**（WWDC25）を使用します。大容量ファイルは **Mac** を推奨。iOS も同じ API ですが、大きなアップロードは向きません。

### フィルター / ウィジェットの「on sale」とは？

**少なくとも 1 つの App Store 地域で配信可能**という意味です。パイプライン（waiting / in review / rejected / pending developer release）は別途追跡します。ウィジェット **Needs attention** = waiting + in review + rejected + pending release（ローカル合計、ASC フィールドではありません）。

### 提出前の hard / soft チェックとは？

**Hard blockers** は提出を止めます（例：ビルド未準備、デモアカウント必須だが未入力）。**Soft checks** は警告（主スクリーンショットサイズ、著作権、年齢制限など）で、確認後に続行できます。Overview / Versions / Submissions の `?` または `iappmanager://release-guide` を参照。

### 対応言語は？

**English · 简体中文 · 繁體中文**。システムに従うか、設定で固定。言語のホットスワップはルートを **再マウントせず**（ナビゲーションと下書きを保持）。

### ウィジェットが ASC のライブ数値を表示しないのはなぜ？

ウィジェットは **ASC を呼び出しません**。メインアプリがスキャンしスナップショットを書き込みます（約 10 分 TTL、My Apps と同じ区分）。アプリを開きリストを更新（またはステータスを強制更新）してください。

### macOS と iOS の違いは？

両方ともストア、マネタイズ、TestFlight、Game Center、ユーザー、レポート、レビュー、Webhooks をカバー。**大容量 IPA** と証明書のシステム Keychain へのインストールは **Mac** を推奨。代替アプリアイコンは **iOS のみ**。

### App Store Connect 用のプライバシーポリシー URL は？

本サイトの [Privacy Policy](../privacy) を開き、ブラウザのアドレスバーから URL をコピーしてください。

### システム要件は？

iPhone / iPad **iOS 17.0+**、Mac **macOS 14.0+**。

### サポートへの連絡方法は？

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 通常 48 時間以内に返信します。

</section>
<section lang="ko" markdown="1">

### iAppManager란?

iPhone, iPad, Mac용 **네이티브 App Store Connect 워크스테이션**입니다. **API Key**로 로그인해 버전, 스크린샷, IAP, TestFlight, 인증서, 보고서, 리뷰를 관리합니다. 트래픽은 **Apple로 직접** 갑니다. iHTC Studio 계정은 필요 없습니다.

### API Key는 어떻게 받나요?

1. [App Store Connect](https://appstoreconnect.apple.com) → **Users and Access** → **Integrations** → **App Store Connect API**
2. 키 생성(Admin 또는 App Manager 권장)
3. `.p8` **한 번만** 다운로드, **Issuer ID**와 **Key ID** 기록
4. iAppManager에 붙여넣기(또는 파일 선택). 앱 내 가이드가 스크린샷과 함께 안내합니다.

### `.p8`이 iHTC Studio에 업로드되나요?

**아니요.** 개인 키는 **기기 Keychain**에만 저장됩니다. 요청은 로컬에서 서명되어 `api.appstoreconnect.apple.com`으로 전송됩니다. 계정 제거 시 로컬 키도 삭제됩니다.

### 앱 안에서 Apple ID 비밀번호가 필요한가요?

**아니요.** 인증은 **API Key만**(Issuer ID + Key ID + `.p8`)입니다. 공개 API가 없는 기능(프라이버시 영양 라벨, 무료 App 프로모 코드 등)은 Safari/ASC에서 Apple ID를 사용합니다——앱이 Apple 사이트를 엽니다.

### Transporter 없이 IPA / PKG를 업로드할 수 있나요?

**예.** iAppManager는 Apple **Build Upload REST**(WWDC25)를 사용합니다. 큰 파일은 **Mac** 권장. iOS도 동일 API지만 대용량 업로드는 불편합니다.

### 필터 / 위젯의 "on sale"은 무엇을 뜻하나요?

**최소 하나의 App Store 지역에서 이용 가능**합니다. 파이프라인(waiting / in review / rejected / pending developer release)은 별도로 추적합니다. 위젯 **Needs attention** = waiting + in review + rejected + pending release(로컬 합계, ASC 필드 아님).

### 제출 전 hard / soft 체크?

**Hard blockers**는 제출을 막습니다(예: 빌드 미준비, 데모 계정 필요하지만 없음). **Soft checks**는 경고(주 스크린샷 크기, 저작권, 연령 등급 등)이며 확인 후 계속할 수 있습니다. Overview / Versions / Submissions의 `?` 또는 `iappmanager://release-guide` 참고.

### 지원 언어는?

**English · 简体中文 · 繁體中文**. 시스템 따르기 또는 설정에서 고정. 언어 핫스왑 시 루트를 **다시 마운트하지 않음**(내비게이션과 초안 유지).

### 위젯에 실시간 ASC 숫자가 안 보이는 이유?

위젯은 **ASC를 호출하지 않습니다**. 메인 앱이 스캔 후 스냅샷 기록(약 10분 TTL, My Apps와 동일 버킷). 앱을 열고 목록 새로고침(또는 상태 강제 새로고침)하세요.

### macOS vs iOS 차이?

둘 다 스토어, 수익화, TestFlight, Game Center, 사용자, 보고서, 리뷰, Webhooks 지원. **대용량 IPA**와 인증서를 시스템 Keychain에 설치는 **Mac** 권장. 대체 앱 아이콘은 **iOS만**.

### App Store Connect용 프라이버시 정책 URL?

본 사이트 [Privacy Policy](../privacy) 페이지를 열고 브라우저 주소창에서 URL을 복사하세요.

### 시스템 요구 사항?

iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+**.

### 지원 문의?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 보통 48시간 이내 답변.

</section>
<section lang="ru" markdown="1">

### Что такое iAppManager?

**Нативная рабочая станция App Store Connect** для iPhone, iPad и Mac. Вход по **API Key**, управление версиями, скриншотами, IAP, TestFlight, сертификатами, отчётами и отзывами — трафик **напрямую в Apple**. Учётная запись iHTC Studio не нужна.

### Как получить API Key?

1. Откройте [App Store Connect](https://appstoreconnect.apple.com) → **Users and Access** → **Integrations** → **App Store Connect API**
2. Создайте ключ (рекомендуется Admin или App Manager)
3. Скачайте `.p8` **один раз**, запишите **Issuer ID** и **Key ID**
4. Вставьте в iAppManager (или выберите файл). Встроенное руководство с скриншотами проведёт по шагам.

### Загружается ли мой `.p8` в iHTC Studio?

**Нет.** Закрытый ключ хранится только в **Keychain устройства**. Запросы подписываются локально и отправляются на `api.appstoreconnect.apple.com`. Удаление аккаунта удаляет локальный ключ.

### Нужен ли пароль Apple ID в приложении?

**Нет.** Аутентификация **только по API Key** (Issuer ID + Key ID + `.p8`). Если у функции нет публичного API (например, privacy nutrition labels, промокоды бесплатных приложений), приложение откроет сайт Apple — там вы используете Apple ID в Safari/ASC.

### Можно загружать IPA / PKG без Transporter?

**Да.** iAppManager использует **Build Upload REST** Apple (WWDC25). Для больших файлов лучше **Mac**; на iOS тот же API, но крупные загрузки неудобны.

### Что означает «on sale» в фильтрах / виджетах?

**Доступно хотя бы в одной территории App Store.** Статусы пайплайна (waiting / in review / rejected / pending developer release) учитываются отдельно. Виджет **Needs attention** = waiting + in review + rejected + pending release (локальная сумма, не поле ASC).

### Hard vs soft проверки перед отправкой?

**Hard blockers** блокируют отправку (например, сборка не готова, нужен демо‑аккаунт, но его нет). **Soft checks** предупреждают (размер основного скриншота, copyright, возрастной рейтинг и т. д.) — можно подтвердить и продолжить. См. Overview / Versions / Submissions `?` или `iappmanager://release-guide`.

### Какие языки поддерживаются?

**English · 简体中文 · 繁體中文** — по системе или принудительно в настройках. Горячая смена языка **без** перемонтирования корня (навигация и черновики сохраняются).

### Почему виджеты не показывают «живые» цифры ASC?

Виджеты **не вызывают ASC**. Основное приложение сканирует и записывает снимок (~10‑мин TTL, те же корзины, что My Apps). Откройте приложение и обновите список (или принудительно обновите статус).

### Отличия macOS и iOS?

Обе платформы: магазин, монетизация, TestFlight, Game Center, пользователи, отчёты, отзывы, Webhooks. **Крупные IPA** и установка сертификатов в системный Keychain — лучше на **Mac**. Альтернативные иконки — **только iOS**.

### URL политики конфиденциальности для App Store Connect?

Откройте [Privacy Policy](../privacy) на этом сайте и скопируйте URL из адресной строки браузера.

### Системные требования?

iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+**.

### Как связаться с поддержкой?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — обычно в течение 48 часов.

</section>
<section lang="th" markdown="1">

### iAppManager คืออะไร?

**สถานีงาน App Store Connect แบบ native** สำหรับ iPhone, iPad และ Mac ลงชื่อด้วย **API Key** จัดการเวอร์ชัน ภาพหน้าจอ IAP TestFlight ใบรับรอง รายงาน และรีวิว — ทรaffic **ไปที่ Apple โดยตรง** ไม่ต้องมีบัญชี iHTC Studio

### ขอ API Key อย่างไร?

1. เปิด [App Store Connect](https://appstoreconnect.apple.com) → **Users and Access** → **Integrations** → **App Store Connect API**
2. สร้างคีย์ (แนะนำ Admin หรือ App Manager)
3. ดาวน์โหลด `.p8` **ครั้งเดียว** จด **Issuer ID** และ **Key ID**
4. วางใน iAppManager (หรือเลือกไฟล์) คู่มือในแอปมีภาพหน้าจอแนะนำทีละขั้น

### `.p8` ถูกอัปโหลดไป iHTC Studio ไหม?

**ไม่** คีย์ส่วนตัวอยู่ใน **Keychain บนอุปกรณ์** เท่านั้น คำขอถูกเซ็นบนเครื่องแล้วส่งไป `api.appstoreconnect.apple.com` ลบบัญชีจะลบคีย์ในเครื่อง

### ต้องใส่รหัส Apple ID ในแอปไหม?

**ไม่** ยืนยันตัวตนด้วย **API Key เท่านั้น** (Issuer ID + Key ID + `.p8`) ฟีเจอร์ที่ไม่มี public API (เช่น privacy nutrition labels โค้ดโปรโม App ฟรี) แอปจะเปิดเว็บ Apple ให้คุณใช้ Apple ID ใน Safari/ASC

### อัปโหลด IPA / PKG โดยไม่ใช้ Transporter ได้ไหม?

**ได้** iAppManager ใช้ **Build Upload REST** ของ Apple (WWDC25) ไฟล์ใหญ่แนะนำ **Mac** iOS ใช้ API เดียวกันแต่อัปโหลดใหญ่ไม่สะดวก

### "on sale" ในตัวกรอง / วิดเจ็ต หมายถึงอะไร?

**พร้อมจำหน่ายอย่างน้อยหนึ่งประเทศใน App Store** สถานะ pipeline (waiting / in review / rejected / pending developer release) ติดตามแยก วิดเจ็ต **Needs attention** = waiting + in review + rejected + pending release (รวมในเครื่อง ไม่ใช่ฟิลด์ ASC)

### hard vs soft ก่อนส่ง?

**Hard blockers** หยุดการส่ง (เช่น build ยังไม่พร้อม ต้องมี demo account แต่ไม่มี) **Soft checks** เตือน (ขนาดภาพหลัก ลิขสิทธิ์ เรตตингอายุ ฯลฯ) ยืนยันแล้วดำเนินต่อได้ ดู Overview / Versions / Submissions `?` หรือ `iappmanager://release-guide`

### รองรับภาษาอะไร?

**English · 简体中文 · 繁體中文** ตามระบบหรือบังคับใน Settings สลับภาษาแบบ hot-swap **ไม่** remount root (นำทางและ draft คงอยู่)

### ทำไมวิดเจ็ตไม่แสดงตัวเลข ASC สด?

วิดเจ็ต **ไม่เรียก ASC** แอปหลักสแกนแล้วเขียน snapshot (~10 นาที TTL ชุดเดียวกับ My Apps) เปิดแอปแล้วรีเฟรชรายการ (หรือบังคับรีเฟรชสถานะ)

### ความต่าง macOS กับ iOS?

ทั้งคู่ครอบคลุม store monetization TestFlight Game Center users reports reviews Webhooks **IPA ใหญ่** และติดตั้งใบรับรองใน system Keychain แนะนำ **Mac** ไอคอนแอปสำรอง **เฉพาะ iOS**

### URL นโยบายความเป็นส่วนตัวสำหรับ App Store Connect?

เปิด [Privacy Policy](../privacy) บนไซต์นี้แล้วคัดลอก URL จากแถบที่อยู่เบราว์เซอร์

### ความต้องการระบบ?

iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+**

### ติดต่อฝ่ายสนับสนุน?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — โดยทั่วไปภายใน 48 ชั่วโมง

</section>
<section lang="de" markdown="1">

### Was ist iAppManager?

Eine **native App-Store-Connect-Arbeitsstation** für iPhone, iPad und Mac. Anmeldung mit **API Key**, Verwaltung von Versionen, Screenshots, IAP, TestFlight, Zertifikaten, Berichten und Reviews — Traffic **direkt zu Apple**. Kein iHTC-Studio-Konto nötig.

### Wie erhalte ich einen API Key?

1. [App Store Connect](https://appstoreconnect.apple.com) → **Users and Access** → **Integrations** → **App Store Connect API**
2. Schlüssel erstellen (Admin oder App Manager empfohlen)
3. `.p8` **einmal** herunterladen, **Issuer ID** und **Key ID** notieren
4. In iAppManager einfügen (oder Datei wählen). Die In-App-Anleitung mit Screenshots führt dich durch.

### Wird meine `.p8` zu iHTC Studio hochgeladen?

**Nein.** Der private Schlüssel bleibt in der **Geräte-Keychain**. Anfragen werden lokal signiert und an `api.appstoreconnect.apple.com` gesendet. Konto entfernen löscht den lokalen Schlüssel.

### Brauche ich im App das Apple-ID-Passwort?

**Nein.** Authentifizierung **nur per API Key** (Issuer ID + Key ID + `.p8`). Fehlt eine öffentliche API (z. B. Privacy Nutrition Labels, Gratis-App-Promocodes), öffnet die App Apples Website — dort nutzt du Apple ID in Safari/ASC.

### IPA / PKG ohne Transporter hochladen?

**Ja.** iAppManager nutzt Apples **Build Upload REST** (WWDC25). Große Dateien lieber am **Mac**; iOS unterstützt dieselbe API, große Uploads sind dort unbequem.

### Was bedeutet „on sale" in Filtern / Widgets?

**In mindestens einem App-Store-Territorium verfügbar.** Pipeline-Buckets (waiting / in review / rejected / pending developer release) werden getrennt geführt. Widget **Needs attention** = waiting + in review + rejected + pending release (lokale Summe, kein ASC-Feld).

### Hard vs. Soft Checks vor dem Submit?

**Hard blockers** stoppen den Submit (z. B. Build nicht bereit, Demo-Konto nötig aber fehlt). **Soft checks** warnen (Haupt-Screenshot-Größe, Copyright, Altersfreigabe usw.) — nach Bestätigung weiter. Siehe Overview / Versions / Submissions `?` oder `iappmanager://release-guide`.

### Welche Sprachen?

**English · 简体中文 · 繁體中文** — System folgen oder in den Einstellungen erzwingen. Hot-Swap der Sprache **ohne** Root neu zu mounten (Navigation und Entwürfe bleiben).

### Warum zeigen Widgets keine Live-ASC-Zahlen?

Widgets **rufen ASC nicht auf**. Die Haupt-App scannt und schreibt einen Snapshot (~10 Min. TTL, gleiche Buckets wie My Apps). App öffnen und Liste aktualisieren (oder Status erzwingen).

### macOS vs. iOS?

Beide: Store, Monetarisierung, TestFlight, Game Center, Nutzer, Berichte, Reviews, Webhooks. **Große IPAs** und Zertifikate in die System-Keychain — **Mac** bevorzugen. Alternative App-Icons **nur iOS**.

### Privacy-Policy-URL für App Store Connect?

Öffne die [Privacy Policy](../privacy) dieser Site und kopiere die URL aus der Browser-Adressleiste.

### Systemanforderungen?

iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+**.

### Support kontaktieren?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — in der Regel innerhalb von 48 Stunden.

</section>
<section lang="fr" markdown="1">

### Qu'est-ce qu'iAppManager ?

Un **poste de travail App Store Connect natif** pour iPhone, iPad et Mac. Connexion par **clé API**, gestion des versions, captures, IAP, TestFlight, certificats, rapports et avis — trafic **directement vers Apple**. Aucun compte iHTC Studio.

### Comment obtenir une clé API ?

1. Ouvrez [App Store Connect](https://appstoreconnect.apple.com) → **Users and Access** → **Integrations** → **App Store Connect API**
2. Créez une clé (Admin ou App Manager recommandé)
3. Téléchargez le `.p8` **une seule fois**, notez **Issuer ID** et **Key ID**
4. Collez dans iAppManager (ou choisissez le fichier). Le guide in-app avec captures vous accompagne.

### Ma `.p8` est-elle envoyée à iHTC Studio ?

**Non.** La clé privée reste dans le **Keychain de l'appareil**. Les requêtes sont signées localement et envoyées à `api.appstoreconnect.apple.com`. Supprimer le compte efface la clé locale.

### Faut-il le mot de passe Apple ID dans l'app ?

**Non.** Authentification **uniquement par clé API** (Issuer ID + Key ID + `.p8`). Si une fonction n'a pas d'API publique (ex. privacy nutrition labels, codes promo d'apps gratuites), l'app ouvre le site Apple — vous utilisez Apple ID dans Safari/ASC.

### Téléverser IPA / PKG sans Transporter ?

**Oui.** iAppManager utilise **Build Upload REST** d'Apple (WWDC25). Préférez le **Mac** pour les gros fichiers ; iOS supporte la même API mais les gros envois y sont moins confortables.

### Que signifie « on sale » dans les filtres / widgets ?

**Disponible dans au moins un territoire App Store.** Les buckets pipeline (waiting / in review / rejected / pending developer release) sont suivis à part. Widget **Needs attention** = waiting + in review + rejected + pending release (somme locale, pas un champ ASC).

### Checks hard vs soft avant envoi ?

Les **hard blockers** bloquent l'envoi (ex. build pas prêt, compte démo requis mais absent). Les **soft checks** avertissent (taille capture principale, copyright, classification d'âge, etc.) — vous pouvez confirmer et continuer. Voir Overview / Versions / Submissions `?` ou `iappmanager://release-guide`.

### Langues prises en charge ?

**English · 简体中文 · 繁體中文** — suivre le système ou forcer dans Réglages. Changement à chaud **sans** remonter la racine (navigation et brouillons conservés).

### Pourquoi les widgets n'affichent pas les chiffres ASC en direct ?

Les widgets **n'appellent pas ASC**. L'app principale scanne et écrit un instantané (~10 min TTL, mêmes buckets que My Apps). Ouvrez l'app et actualisez la liste (ou forcez le statut).

### macOS vs iOS ?

Les deux couvrent store, monétisation, TestFlight, Game Center, utilisateurs, rapports, avis, Webhooks. **Gros IPA** et installation des certificats dans le Keychain système — préférez le **Mac**. Icônes alternatives **iOS uniquement**.

### URL de politique de confidentialité pour App Store Connect ?

Ouvrez la [Privacy Policy](../privacy) de ce site et copiez l'URL depuis la barre d'adresse du navigateur.

### Configuration requise ?

iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+**.

### Contacter le support ?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — en général sous 48 h.

</section>
<section lang="tr" markdown="1">

### iAppManager nedir?

iPhone, iPad ve Mac için **yerel App Store Connect çalışma istasyonu**. **API Key** ile oturum açın; sürümler, ekran görüntüleri, IAP, TestFlight, sertifikalar, raporlar ve yorumlar — trafik **doğrudan Apple'a**. iHTC Studio hesabı gerekmez.

### API Key nasıl alınır?

1. [App Store Connect](https://appstoreconnect.apple.com) → **Users and Access** → **Integrations** → **App Store Connect API**
2. Anahtar oluşturun (Admin veya App Manager önerilir)
3. `.p8` dosyasını **bir kez** indirin; **Issuer ID** ve **Key ID**'yi not edin
4. iAppManager'a yapıştırın (veya dosyayı seçin). Uygulama içi rehber ekran görüntüleriyle adım adım anlatır.

### `.p8` iHTC Studio'ya yüklenir mi?

**Hayır.** Özel anahtar yalnızca **cihaz Keychain**'inde kalır. İstekler yerelde imzalanır ve `api.appstoreconnect.apple.com`'a gider. Hesabı kaldırmak yerel anahtarı siler.

### Uygulama içinde Apple ID parolası gerekir mi?

**Hayır.** Kimlik doğrulama **yalnızca API Key** (Issuer ID + Key ID + `.p8`). Herkese açık API olmayan özellikler (ör. privacy nutrition labels, ücretsiz uygulama promosyon kodları) için uygulama Apple sitesini açar — Apple ID'yi Safari/ASC tarafında kullanırsınız.

### Transporter olmadan IPA / PKG yüklenebilir mi?

**Evet.** iAppManager Apple **Build Upload REST** (WWDC25) kullanır. Büyük dosyalar için **Mac** tercih edin; iOS aynı API'yi destekler ama büyük yüklemeler zor.

### Filtreler / widget'larda "on sale" ne demek?

**En az bir App Store bölgesinde kullanılabilir.** Pipeline kovaları (waiting / in review / rejected / pending developer release) ayrı izlenir. Widget **Needs attention** = waiting + in review + rejected + pending release (yerel toplam, ASC alanı değil).

### Gönderimden önce hard vs soft kontroller?

**Hard blockers** gönderimi durdurur (ör. build hazır değil, demo hesap gerekli ama yok). **Soft checks** uyarır (ana ekran görüntüsü boyutu, telif, yaş derecesi vb.) — onaylayıp devam edebilirsiniz. Overview / Versions / Submissions `?` veya `iappmanager://release-guide`.

### Hangi diller?

**English · 简体中文 · 繁體中文** — sistemi izleyin veya Ayarlar'da zorlayın. Dil hot-swap **kökü yeniden mount etmeden** (gezinme ve taslaklar kalır).

### Widget'lar neden canlı ASC sayılarını göstermiyor?

Widget'lar **ASC'yi çağırmaz**. Ana uygulama tarar ve anlık görüntü yazar (~10 dk TTL, My Apps ile aynı kovalar). Uygulamayı açıp listeyi yenileyin (veya durumu zorla yenileyin).

### macOS vs iOS?

Her ikisi de mağaza, monetizasyon, TestFlight, Game Center, kullanıcılar, raporlar, yorumlar, Webhooks. **Büyük IPA** ve sertifikaları sistem Keychain'e kurma — **Mac** tercih. Alternatif uygulama simgeleri **yalnızca iOS**.

### App Store Connect gizlilik politikası URL'si?

Bu sitenin [Privacy Policy](../privacy) sayfasını açıp tarayıcı adres çubuğundan URL'yi kopyalayın.

### Sistem gereksinimleri?

iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+**.

### Destek?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — genelde 48 saat içinde.

</section>
