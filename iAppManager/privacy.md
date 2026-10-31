---
layout: doc
title: iAppManager — Privacy Policy
app_id: iAppManager
doc_title_en: Privacy Policy
doc_title_zh_cn: 隐私政策
doc_title_zh_tw: 隱私政策
description: Privacy policy for iAppManager (爱应用者) — API Key in Keychain; ASC traffic to Apple only; no analytics SDK.
---

<section lang="en" markdown="1">

iHTC Studio built iAppManager (爱应用者 / 愛應用者).

## Summary

**iHTC Studio does not operate a backend for your App Store Connect data.** You sign in with an **API Key** stored in **device Keychain**. Business requests go **directly to Apple** (`api.appstoreconnect.apple.com`). **No iHTC Studio account. No ads. No analytics / crash SDK.** Optional StoreKit tip purchases are processed by **Apple**.

## Data Stored on Your Device

| Data | Purpose |
|------|---------|
| API Key accounts (Issuer ID, Key ID, `.p8` PEM) | Authenticate to App Store Connect API — Keychain |
| Account index / current account / preferences | Multi-account switch, appearance, language, accent |
| Remote image cache | App icons & media thumbnails (clearable in Settings) |
| Review reply templates, report presets / stars | Local productivity helpers per account |
| App Group widget snapshot | Pipeline counts, theme/language for widgets — **on device only** |

## Network

| Destination | Why |
|-------------|-----|
| `api.appstoreconnect.apple.com` | All ASC management (JWT signed on device) |
| Apple iTunes Lookup (multi-region) | Optional App icon enrichment |
| Apple CDN / pre-signed upload URLs | Screenshots, previews, IPA/PKG chunk uploads (no Bearer on PUT) |
| `apps.apple.com` / App Store | Open product pages (system / external) |
| Mail client | Feedback you choose to send |

iHTC Studio does **not** receive your API private key, app metadata, IPA contents, sales reports or customer reviews.

## Permissions & platform notes

| Capability | When | Why |
|------------|------|-----|
| Outgoing network | Always while using ASC features | Talk to Apple APIs |
| User-selected files | Upload IPA/screenshots, export reports | You pick the files |
| Keychain | Save / remove API keys | Secure local storage |
| App Group | Widgets | Share local summaries only |
| Photos / share sheet (as offered by OS) | Export / save when you act | User-initiated |

Certificate **install into system Keychain** is intended for **macOS**. iOS focuses on list / download / share.

## What we do not do

- No iHTC Studio cloud account for ASC data
- No advertising or third-party trackers
- No sale of personal data
- Widgets never call ASC by themselves

## Contact

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="zh-CN" markdown="1">

爱火腿肠工作室（iHTC Studio）开发了爱应用者。

## 摘要

**iHTC Studio 不为你的 App Store Connect 数据运营后端。** 你使用 **API Key** 登录，密钥保存在本机 **钥匙串**。业务请求 **直连 Apple**（`api.appstoreconnect.apple.com`）。**无 iHTC Studio 账号。无广告。无分析 / 崩溃 SDK。** 可选 StoreKit 赞赏由 **Apple** 处理。

## 设备本地存储

| 数据 | 用途 |
|------|------|
| API Key 账号（Issuer ID、密钥 ID、`.p8` PEM） | 鉴权 App Store Connect API — 钥匙串 |
| 账号索引 / 当前账号 / 偏好 | 多账号、外观、语言、强调色 |
| 远程图片缓存 | App 图标与素材缩略图（设置可清空） |
| 评价回复模板、报表预设 / 星标 | 按账号的本机效率工具 |
| App Group 小组件快照 | 流水线计数、主题/语言 — **仅本机** |

## 网络

| 目标 | 原因 |
|------|------|
| `api.appstoreconnect.apple.com` | 全部 ASC 管理（JWT 在本机签名） |
| Apple iTunes Lookup（多区） | 可选补全 App 图标 |
| Apple CDN / 预签名上传 URL | 截图、预览、IPA/PKG 分片上传（PUT 不带 Bearer） |
| `apps.apple.com` / App Store | 打开产品页（系统 / 外开） |
| 邮件客户端 | 你主动发送的反馈 |

iHTC Studio **不会**收到你的 API 私钥、App 元数据、IPA 内容、销售报表或顾客评价。

## 权限与平台说明

| 能力 | 时机 | 原因 |
|------|------|------|
| 出站网络 | 使用 ASC 功能时 | 连接 Apple API |
| 用户所选文件 | 上传 IPA/截图、导出报表 | 由你选择文件 |
| 钥匙串 | 保存 / 移除 API Key | 安全本地存储 |
| App Group | 小组件 | 仅共享本机摘要 |
| 照片 / 分享表（系统提供时） | 你主动导出 / 保存 | 用户发起 |

证书 **安装到系统钥匙串** 面向 **macOS**。iOS 以列表 / 下载 / 分享为主。

## 我们不会做的事

- 不为 ASC 数据提供 iHTC Studio 云账号
- 无广告或第三方追踪
- 不出售个人数据
- 小组件不会自行请求 ASC

## 联系

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="zh-TW" markdown="1">

愛火腿腸工作室（iHTC Studio）開發了愛應用者。

## 摘要

**iHTC Studio 不為你的 App Store Connect 資料營運後端。** 你使用 **API Key** 登入，金鑰保存在本機 **鑰匙圈**。業務請求 **直連 Apple**（`api.appstoreconnect.apple.com`）。**無 iHTC Studio 帳號。無廣告。無分析 / 當機 SDK。** 可選 StoreKit 打賞由 **Apple** 處理。

## 裝置本機儲存

| 資料 | 用途 |
|------|------|
| API Key 帳號（Issuer ID、金鑰 ID、`.p8` PEM） | 鑑權 App Store Connect API — 鑰匙圈 |
| 帳號索引 / 目前帳號 / 偏好 | 多帳號、外觀、語言、強調色 |
| 遠端圖片快取 | App 圖示與素材縮圖（設定可清空） |
| 評價回覆範本、報表預設 / 星標 | 按帳號的本機效率工具 |
| App Group 小工具快照 | 流水線計數、主題/語言 — **僅本機** |

## 網路

| 目標 | 原因 |
|------|------|
| `api.appstoreconnect.apple.com` | 全部 ASC 管理（JWT 在本機簽名） |
| Apple iTunes Lookup（多區） | 可選補全 App 圖示 |
| Apple CDN / 預簽名上傳 URL | 截圖、預覽、IPA/PKG 分片上傳（PUT 不帶 Bearer） |
| `apps.apple.com` / App Store | 打開產品頁（系統 / 外開） |
| 郵件用戶端 | 你主動傳送的回饋 |

iHTC Studio **不會**收到你的 API 私鑰、App 中繼資料、IPA 內容、銷售報表或顧客評價。

## 權限與平台說明

| 能力 | 時機 | 原因 |
|------|------|------|
| 出站網路 | 使用 ASC 功能時 | 連線 Apple API |
| 使用者所選檔案 | 上傳 IPA/截圖、匯出報表 | 由你選擇檔案 |
| 鑰匙圈 | 儲存 / 移除 API Key | 安全本機儲存 |
| App Group | 小工具 | 僅共享本機摘要 |
| 照片 / 分享表（系統提供時） | 你主動匯出 / 儲存 | 使用者發起 |

憑證 **安裝到系統鑰匙圈** 面向 **macOS**。iOS 以列表 / 下載 / 分享為主。

## 我們不會做的事

- 不為 ASC 資料提供 iHTC Studio 雲帳號
- 無廣告或第三方追蹤
- 不出售個人資料
- 小工具不會自行請求 ASC

## 聯絡

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ja" markdown="1">

iHTC Studio（当社）は iAppManager（爱应用者 / 愛應用者）を開発しました。

## 概要

**iHTC Studio は App Store Connect データ用のバックエンドを運用しません。** **API Key** でサインインし、鍵は **デバイスの Keychain** に保存されます。業務リクエストは **Apple に直接**（`api.appstoreconnect.apple.com`）送信されます。**iHTC Studio アカウント不要。広告なし。分析 / クラッシュ SDK なし。** 任意の StoreKit チップは **Apple** が処理します。

## デバイスに保存されるデータ

| データ | 用途 |
|------|---------|
| API Key アカウント（Issuer ID、Key ID、`.p8` PEM） | App Store Connect API 認証 — Keychain |
| アカウント索引 / 現在のアカウント / 設定 | マルチアカウント、外観、言語、アクセント |
| リモート画像キャッシュ | App アイコンとメディアサムネイル（設定で削除可） |
| レビュー返信テンプレート、レポートプリセット / スター | アカウントごとのローカル生産性ツール |
| App Group ウィジェットスナップショット | パイプライン件数、テーマ / 言語 — **端末内のみ** |

## ネットワーク

| 宛先 | 理由 |
|-------------|-----|
| `api.appstoreconnect.apple.com` | すべての ASC 管理（JWT は端末で署名） |
| Apple iTunes Lookup（複数地域） | 任意の App アイコン補完 |
| Apple CDN / 事前署名アップロード URL | スクリーンショット、プレビュー、IPA/PKG チャンクアップロード（PUT に Bearer なし） |
| `apps.apple.com` / App Store | 商品ページを開く（システム / 外部） |
| メールクライアント | あなたが送信を選んだフィードバック |

iHTC Studio は API 秘密鍵、App メタデータ、IPA 内容、販売レポート、カスタマーレビューを **受け取りません**。

## 権限とプラットフォーム

| 機能 | タイミング | 理由 |
|------------|------|-----|
| 外向きネットワーク | ASC 機能利用中 | Apple API と通信 |
| ユーザー選択ファイル | IPA / スクリーンショットのアップロード、レポートのエクスポート | あなたがファイルを選ぶ |
| Keychain | API Key の保存 / 削除 | 安全なローカル保存 |
| App Group | ウィジェット | ローカルサマリーの共有のみ |
| 写真 / 共有シート（OS が提供する場合） | あなたがエクスポート / 保存したとき | ユーザー操作 |

証明書の **システム Keychain へのインストール**は **macOS** 向けです。iOS は一覧 / ダウンロード / 共有が中心です。

## 当社が行わないこと

- ASC データ用の iHTC Studio クラウドアカウントなし
- 広告や第三者トラッカーなし
- 個人データの販売なし
- ウィジェットが単独で ASC を呼び出さない

## お問い合わせ

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ko" markdown="1">

iHTC Studio(당사)는 iAppManager(爱应用者 / 愛應用者)를 개발했습니다.

## 요약

**iHTC Studio는 App Store Connect 데이터용 백엔드를 운영하지 않습니다.** **API Key**로 로그인하며 키는 **기기 Keychain**에 저장됩니다. 업무 요청은 **Apple로 직접**(`api.appstoreconnect.apple.com`) 전송됩니다. **iHTC Studio 계정 불필요. 광고 없음. 분석 / 크래시 SDK 없음.** 선택적 StoreKit 팁은 **Apple**이 처리합니다.

## 기기에 저장되는 데이터

| 데이터 | 용도 |
|------|------|
| API Key 계정(Issuer ID, Key ID, `.p8` PEM) | App Store Connect API 인증 — Keychain |
| 계정 색인 / 현재 계정 / 환경설정 | 다중 계정, 모양, 언어, 강조색 |
| 원격 이미지 캐시 | App 아이콘 및 미디어 썸네일(설정에서 삭제 가능) |
| 리뷰 답글 템플릿, 보고서 프리셋 / 별표 | 계정별 로컬 생산성 도구 |
| App Group 위젯 스냅샷 | 파이프라인 건수, 테마 / 언어 — **기기 내부만** |

## 네트워크

| 대상 | 이유 |
|-------------|-----|
| `api.appstoreconnect.apple.com` | 모든 ASC 관리(JWT는 기기에서 서명) |
| Apple iTunes Lookup(다중 지역) | 선택적 App 아이콘 보강 |
| Apple CDN / 사전 서명 업로드 URL | 스크린샷, 미리보기, IPA/PKG 청크 업로드(PUT에 Bearer 없음) |
| `apps.apple.com` / App Store | 제품 페이지 열기(시스템 / 외부) |
| 메일 클라이언트 | 사용자가 보내기를 선택한 피드백 |

iHTC Studio는 API 개인 키, App 메타데이터, IPA 내용, 판매 보고서, 고객 리뷰를 **받지 않습니다**.

## 권한 및 플랫폼

| 기능 | 시점 | 이유 |
|------------|------|-----|
| 아웃바운드 네트워크 | ASC 기능 사용 중 | Apple API 통신 |
| 사용자가 선택한 파일 | IPA/스크린샷 업로드, 보고서 내보내기 | 사용자가 파일 선택 |
| Keychain | API Key 저장 / 제거 | 안전한 로컬 저장 |
| App Group | 위젯 | 로컬 요약만 공유 |
| 사진 / 공유 시트(OS 제공 시) | 사용자가 내보내기 / 저장할 때 | 사용자 주도 |

인증서 **시스템 Keychain 설치**는 **macOS**용입니다. iOS는 목록 / 다운로드 / 공유 중심입니다.

## 하지 않는 일

- ASC 데이터용 iHTC Studio 클라우드 계정 없음
- 광고 또는 서드파티 추적 없음
- 개인 데이터 판매 없음
- 위젯이 스스로 ASC를 호출하지 않음

## 문의

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="ru" markdown="1">

iHTC Studio («мы») разработала iAppManager (爱应用者 / 愛應用者).

## Кратко

**iHTC Studio не эксплуатирует backend для ваших данных App Store Connect.** Вы входите по **API Key**, ключ хранится в **Keychain устройства**. Запросы идут **напрямую в Apple** (`api.appstoreconnect.apple.com`). **Без аккаунта iHTC Studio. Без рекламы. Без analytics / crash SDK.** Необязательные чаевые StoreKit обрабатывает **Apple**.

## Данные на устройстве

| Данные | Назначение |
|------|---------|
| Учётки API Key (Issuer ID, Key ID, `.p8` PEM) | Аутентификация App Store Connect API — Keychain |
| Индекс аккаунтов / текущий аккаунт / настройки | Несколько аккаунтов, тема, язык, акцент |
| Кэш удалённых изображений | Иконки приложений и миниатюры медиа (очистка в настройках) |
| Шаблоны ответов на отзывы, пресеты отчётов / звёзды | Локальные инструменты продуктивности по аккаунту |
| Снимок виджета App Group | Счётчики pipeline, тема / язык — **только на устройстве** |

## Сеть

| Назначение | Зачем |
|-------------|-----|
| `api.appstoreconnect.apple.com` | Всё управление ASC (JWT подписывается на устройстве) |
| Apple iTunes Lookup (несколько регионов) | Необязательное обогащение иконок |
| Apple CDN / pre-signed upload URL | Скриншоты, превью, chunked IPA/PKG (PUT без Bearer) |
| `apps.apple.com` / App Store | Открытие страниц продуктов (система / внешне) |
| Почтовый клиент | Обратная связь, которую вы сами отправляете |

iHTC Studio **не получает** ваш API private key, метаданные приложений, содержимое IPA, отчёты о продажах или отзывы клиентов.

## Разрешения и платформы

| Возможность | Когда | Зачем |
|------------|------|-----|
| Исходящая сеть | При использовании ASC | Обращение к API Apple |
| Файлы, выбранные пользователем | Загрузка IPA/скриншотов, экспорт отчётов | Вы выбираете файлы |
| Keychain | Сохранение / удаление API Key | Безопасное локальное хранение |
| App Group | Виджеты | Только локальные сводки |
| Фото / share sheet (если даёт ОС) | Когда вы экспортируете / сохраняете | Инициатива пользователя |

**Установка сертификатов в системный Keychain** рассчитана на **macOS**. На iOS — список / скачивание / «Поделиться».

## Чего мы не делаем

- Нет облачного аккаунта iHTC Studio для данных ASC
- Нет рекламы и сторонних трекеров
- Не продаём персональные данные
- Виджеты сами не вызывают ASC

## Контакты

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="th" markdown="1">

iHTC Studio («เรา») พัฒนา iAppManager (爱应用者 / 愛應用者)

## สรุป

**iHTC Studio ไม่ได้ให้บริการ backend สำหรับข้อมูล App Store Connect ของคุณ** คุณลงชื่อด้วย **API Key** เก็บคีย์ใน **Keychain บนอุปกรณ์** คำขอธุรกิจไป **ตรง Apple** (`api.appstoreconnect.apple.com`) **ไม่ต้องมีบัญชี iHTC Studio ไม่มีโฆษณา ไม่มี analytics / crash SDK** ทิป StoreKit ทางเลือกประมวลผลโดย **Apple**

## ข้อมูลที่เก็บบนอุปกรณ์

| ข้อมูล | วัตถุประสงค์ |
|------|---------|
| บัญชี API Key (Issuer ID, Key ID, `.p8` PEM) | ยืนยันตัวตน App Store Connect API — Keychain |
| ดัชนีบัญชี / บัญชีปัจจุบัน / การตั้งค่า | หลายบัญชี ธีม ภาษา สีเน้น |
| แคชรูประยะไกล | ไอคอน App และภาพย่อสื่อ (ล้างได้ใน Settings) |
| เทมเพลตตอบรีวิว พรีเซ็ตรายงาน / ดาว | เครื่องมือเพิ่มประสิทธิภาพในเครื่องต่อบัญชี |
| สแนปช็อตวิดเจ็ต App Group | จำนวน pipeline ธีม / ภาษา — **บนอุปกรณ์เท่านั้น** |

## เครือข่าย

| ปลายทาง | เหตุผล |
|-------------|-----|
| `api.appstoreconnect.apple.com` | การจัดการ ASC ทั้งหมด (JWT ลงนามบนอุปกรณ์) |
| Apple iTunes Lookup (หลายภูมิภาค) | เติมไอคอน App ตามต้องการ |
| Apple CDN / URL อัปโหลดล่วงหน้า | ภาพหน้าจอ พรีวิว อัปโหลด IPA/PKG แบบ chunk (PUT ไม่มี Bearer) |
| `apps.apple.com` / App Store | เปิดหน้าผลิตภัณฑ์ (ระบบ / ภายนอก) |
| ไคลเอนต์เมล | ฟีดแบ็กที่คุณเลือกส่ง |

iHTC Studio **ไม่ได้รับ** API private key ข้อมูลเมตา App เนื้อหา IPA รายงานยอดขาย หรือรีวิวลูกค้า

## สิทธิ์และแพลตฟอร์ม

| ความสามารถ | เมื่อ | เหตุผล |
|------------|------|-----|
| เครือข่ายขาออก | ใช้ฟีเจอร์ ASC | ติดต่อ Apple API |
| ไฟล์ที่ผู้ใช้เลือก | อัปโหลด IPA/ภาพหน้าจอ ส่งออกรายงาน | คุณเลือกไฟล์ |
| Keychain | บันทึก / ลบ API Key | เก็บในเครื่องอย่างปลอดภัย |
| App Group | วิดเจ็ต | แชร์สรุปในเครื่องเท่านั้น |
| รูปภาพ / share sheet (ตามที่ OS ให้) | เมื่อคุณส่งออก / บันทึก | ผู้ใช้เริ่มเอง |

การ **ติดตั้งใบรับรองใน system Keychain** สำหรับ **macOS** iOS เน้นรายการ / ดาวน์โหลด / แชร์

## สิ่งที่เราไม่ทำ

- ไม่มีบัญชีคลาวด์ iHTC Studio สำหรับข้อมูล ASC
- ไม่มีโฆษณาหรือตัวติดตามบุคคลที่สาม
- ไม่ขายข้อมูลส่วนบุคคล
- วิดเจ็ตไม่เรียก ASC เอง

## ติดต่อ

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="de" markdown="1">

iHTC Studio („wir") hat iAppManager (爱应用者 / 愛應用者) entwickelt.

## Kurzfassung

**iHTC Studio betreibt kein Backend für deine App-Store-Connect-Daten.** Du meldest dich mit einem **API Key** an; der Schlüssel liegt in der **Geräte-Keychain**. Geschäftsanfragen gehen **direkt zu Apple** (`api.appstoreconnect.apple.com`). **Kein iHTC-Studio-Konto. Keine Werbung. Kein Analytics-/Crash-SDK.** Optionale StoreKit-Trinkgelder verarbeitet **Apple**.

## Auf dem Gerät gespeicherte Daten

| Daten | Zweck |
|------|---------|
| API-Key-Konten (Issuer ID, Key ID, `.p8` PEM) | App Store Connect API-Auth — Keychain |
| Kontenindex / aktuelles Konto / Einstellungen | Multi-Account, Erscheinungsbild, Sprache, Akzent |
| Remote-Bildcache | App-Icons & Medien-Thumbnails (in Einstellungen löschbar) |
| Review-Antwortvorlagen, Report-Presets / Sterne | Lokale Produktivitätshilfen pro Konto |
| App-Group-Widget-Snapshot | Pipeline-Zähler, Theme/Sprache — **nur auf dem Gerät** |

## Netzwerk

| Ziel | Warum |
|-------------|-----|
| `api.appstoreconnect.apple.com` | Gesamte ASC-Verwaltung (JWT auf dem Gerät signiert) |
| Apple iTunes Lookup (mehrere Regionen) | Optionale Icon-Anreicherung |
| Apple CDN / vorab signierte Upload-URLs | Screenshots, Previews, IPA/PKG-Chunk-Uploads (PUT ohne Bearer) |
| `apps.apple.com` / App Store | Produktseiten öffnen (System / extern) |
| Mail-Client | Feedback, das du selbst sendest |

iHTC Studio erhält **nicht** deinen API-Private-Key, App-Metadaten, IPA-Inhalte, Verkaufsberichte oder Kundenreviews.

## Berechtigungen & Plattform

| Fähigkeit | Wann | Warum |
|------------|------|-----|
| Ausgehender Netzwerkverkehr | Bei ASC-Funktionen | Apple-APIs |
| Vom Nutzer gewählte Dateien | IPA/Screenshots hochladen, Reports exportieren | Du wählst Dateien |
| Keychain | API Key speichern / entfernen | Sichere lokale Speicherung |
| App Group | Widgets | Nur lokale Zusammenfassungen |
| Fotos / Share Sheet (vom OS) | Wenn du exportierst / speicherst | Nutzerinitiiert |

**Installation von Zertifikaten in die System-Keychain** ist für **macOS** gedacht. iOS: Liste / Download / Teilen.

## Was wir nicht tun

- Kein iHTC-Studio-Cloud-Konto für ASC-Daten
- Keine Werbung oder Drittanbieter-Tracker
- Kein Verkauf personenbezogener Daten
- Widgets rufen ASC nicht selbst auf

## Kontakt

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="fr" markdown="1">

iHTC Studio (« nous ») a développé iAppManager (爱应用者 / 愛應用者).

## Résumé

**iHTC Studio n'exploite pas de backend pour vos données App Store Connect.** Vous vous connectez avec une **clé API** stockée dans le **Keychain de l'appareil**. Les requêtes métier vont **directement à Apple** (`api.appstoreconnect.apple.com`). **Pas de compte iHTC Studio. Pas de pub. Pas de SDK analytics / crash.** Les pourboires StoreKit optionnels sont traités par **Apple**.

## Données sur l'appareil

| Donnée | Usage |
|------|---------|
| Comptes clé API (Issuer ID, Key ID, `.p8` PEM) | Auth App Store Connect API — Keychain |
| Index de comptes / compte courant / préférences | Multi-comptes, apparence, langue, accent |
| Cache d'images distantes | Icônes d'apps & vignettes média (effaçable dans Réglages) |
| Modèles de réponse aux avis, presets de rapports / étoiles | Aides productivité locales par compte |
| Instantané widget App Group | Compteurs pipeline, thème / langue — **sur l'appareil uniquement** |

## Réseau

| Destination | Pourquoi |
|-------------|-----|
| `api.appstoreconnect.apple.com` | Toute gestion ASC (JWT signé sur l'appareil) |
| Apple iTunes Lookup (multi-régions) | Enrichissement d'icônes optionnel |
| Apple CDN / URL d'upload pré-signées | Captures, previews, upload IPA/PKG par morceaux (PUT sans Bearer) |
| `apps.apple.com` / App Store | Ouvrir les fiches produit (système / externe) |
| Client mail | Retours que vous choisissez d'envoyer |

iHTC Studio **ne reçoit pas** votre clé privée API, métadonnées d'apps, contenu IPA, rapports de ventes ni avis clients.

## Autorisations & plateforme

| Capacité | Quand | Pourquoi |
|------------|------|-----|
| Réseau sortant | Utilisation ASC | APIs Apple |
| Fichiers choisis par l'utilisateur | Upload IPA/captures, export rapports | Vous choisissez les fichiers |
| Keychain | Enregistrer / supprimer clé API | Stockage local sécurisé |
| App Group | Widgets | Partage de résumés locaux uniquement |
| Photos / share sheet (OS) | Quand vous exportez / enregistrez | Initié par l'utilisateur |

**Installation des certificats dans le Keychain système** vise **macOS**. iOS : liste / téléchargement / partage.

## Ce que nous ne faisons pas

- Pas de compte cloud iHTC Studio pour les données ASC
- Pas de pub ni trackers tiers
- Pas de vente de données personnelles
- Les widgets n'appellent pas ASC seuls

## Contact

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
<section lang="tr" markdown="1">

iHTC Studio («biz») iAppManager'ı (爱应用者 / 愛應用者) geliştirdi.

## Özet

**iHTC Studio, App Store Connect verileriniz için bir backend işletmez.** **API Key** ile oturum açarsınız; anahtar **cihaz Keychain**'inde kalır. İş istekleri **doğrudan Apple'a** gider (`api.appstoreconnect.apple.com`). **iHTC Studio hesabı yok. Reklam yok. Analytics / crash SDK yok.** İsteğe bağlı StoreKit bahşişlerini **Apple** işler.

## Cihazda saklanan veriler

| Veri | Amaç |
|------|------|
| API Key hesapları (Issuer ID, Key ID, `.p8` PEM) | App Store Connect API kimliği — Keychain |
| Hesap dizini / geçerli hesap / tercihler | Çoklu hesap, görünüm, dil, vurgu rengi |
| Uzak görsel önbelleği | App simgeleri ve medya küçük resimleri (Ayarlar'da temizlenebilir) |
| Yorum yanıt şablonları, rapor ön ayarları / yıldızlar | Hesap başına yerel verimlilik araçları |
| App Group widget anlık görüntüsü | Pipeline sayıları, tema / dil — **yalnızca cihazda** |

## Ağ

| Hedef | Neden |
|-------------|-----|
| `api.appstoreconnect.apple.com` | Tüm ASC yönetimi (JWT cihazda imzalanır) |
| Apple iTunes Lookup (çoklu bölge) | İsteğe bağlı simge zenginleştirme |
| Apple CDN / önceden imzalı yükleme URL'leri | Ekran görüntüleri, önizlemeler, IPA/PKG parça yüklemeleri (PUT'ta Bearer yok) |
| `apps.apple.com` / App Store | Ürün sayfalarını açma (sistem / harici) |
| Posta istemcisi | Göndermeyi seçtiğiniz geri bildirim |

iHTC Studio API özel anahtarınızı, App meta verilerini, IPA içeriğini, satış raporlarını veya müşteri yorumlarını **almaz**.

## İzinler ve platform

| Yetenek | Ne zaman | Neden |
|------------|------|-----|
| Giden ağ | ASC özellikleri kullanılırken | Apple API'leri |
| Kullanıcının seçtiği dosyalar | IPA/ekran görüntüsü yükleme, rapor dışa aktarma | Dosyaları siz seçersiniz |
| Keychain | API Key kaydet / kaldır | Güvenli yerel depolama |
| App Group | Widget'lar | Yalnızca yerel özet paylaşımı |
| Fotoğraflar / paylaşım sayfası (OS) | Dışa aktarır / kaydederseniz | Kullanıcı başlatır |

Sertifikaların **sistem Keychain'ine kurulumu** **macOS** içindir. iOS: liste / indir / paylaş.

## Yapmadıklarımız

- ASC verileri için iHTC Studio bulut hesabı yok
- Reklam veya üçüncü taraf izleyici yok
- Kişisel veri satışı yok
- Widget'lar kendi başına ASC çağırmaz

## İletişim

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

</section>
