**Публикуйте быстрее. Выйдите из лабиринта браузера.**

iAppManager (爱应用者) — **нативная рабочая станция App Store Connect** для iPhone, iPad и Mac. Вход по **API Key**, учётные данные в **Keychain**, общение **напрямую с Apple** — версии, скриншоты, IAP, TestFlight, сертификаты, отчёты о продажах и отзывы клиентов в одном месте. **Без аккаунта iHTC Studio. Без рекламы. Без analytics SDK. Без стороннего backend для данных ASC.**

**Кратко:** мультиаккаунт API Key · список приложений с фильтрами платформы и pipeline · чеклист готовности Overview · версии и review submissions · Build Upload REST (IPA/PKG) · метаданные и медиа с копированием между локалями · Custom Product Pages · In-App Events · App Clips · store experiments · featuring nominations · availability и pricing · возрастной рейтинг · accessibility · App Tags · IAP и подписки · Game Center · TestFlight · отзывы · сертификаты и устройства · пользователи и роли · sales / finance / Analytics · Webhooks · виджеты и deep links `iappmanager://` · English / 简体 / 繁體

> Для инди-разработчиков и небольших команд, которые каждую неделю живут в App Store Connect — стол, похожий на Mac-приложение, а не на ферму вкладок.

## Начало работы

1. Создайте **API Key App Store Connect** (рекомендуется Admin или App Manager): App Store Connect → **Users and Access** → **Integrations** → **App Store Connect API** → создайте ключ, скачайте **`.p8` один раз**, запишите **Issuer ID** + **Key ID**.
2. Откройте iAppManager → вставьте Issuer ID / Key ID / PEM (или выберите `.p8`) → проверка (`GET /v1/apps`). Ключи хранятся в **Keychain** этого устройства.
3. Пройдите короткий **onboarding** (сертификаты · отчёты · виджеты · конфиденциальность). Повтор гайдов в **Настройки → Справка**.
4. В **My Apps** выберите **list / grid / cards**, закрепите избранное, фильтруйте по **платформе** (iOS / macOS / tvOS / visionOS) или **статусу** (в продаже · не в продаже · ожидание · на review · отклонено · ожидает release разработчика).
5. Откройте приложение → начните с **Overview** (последняя версия/build, shortcuts, мягкий чеклист, недавние submissions).
6. Путь релиза: **Versions** → прикрепить **Build** → **Metadata / Media** → **Review Detail** → отправить через **Review Submissions** (или «отправить сейчас»).
7. Добавьте **виджеты Home Screen** (Account Hub, Apps Pulse, Review Desk, Quick Actions) и попробуйте `iappmanager://` из Shortcuts.

> Встроенные гайды **Release / IAP / TestFlight / Reports** — один tap (также deep links ниже).

## Зачем скачать

- **Один нативный стол для всего релиза** — без прыжков между вкладками ASC для версий, assets, IAP, TestFlight, certs и отчётов.
- **API Key, а не ещё один пароль** — Issuer ID + Key ID + `.p8` в Keychain; мультиаккаунт; удаление аккаунта удаляет локальный ключ.
- **Загрузка builds без Transporter** — WWDC25 **Build Upload REST** для IPA/PKG; тот же pipeline на iOS (большие файлы лучше на Mac).
- **Подробные гайды в приложении** — release readiness, IAP, TestFlight и reports объясняют hard vs soft checks до сжигания review cycle.
- **Pipeline на Lock Screen** — виджеты отражают в продаже / ожидание / review / отклонено / pending release (те же buckets, что My Apps).
- **Конфиденциальность архитектурой** — ASC traffic на `api.appstoreconnect.apple.com`; iHTC Studio не хостит ваши apps, keys или reports.

## Возможности

### Вход и аккаунты

- **Только API Key** (Issuer ID / Key ID / `.p8`) — без Apple ID OAuth в приложении
- Keychain; **мультиаккаунт**; sign-out / remove удаляет локальный secret
- In-app **«Как получить API Key»** с иллюстрациями

### My Apps

- **List / grid / cards** (list по умолчанию) с управлением колонками
- **Pin** по аккаунту; фильтры **platform** и **status** с ~10‑минутным cache каталога (force refresh с progress)
- **On sale = доступно хотя бы в одной territory**; pipeline buckets независимы от storefront
- Context menu: pin, jump to modules, copy name / Bundle ID / Apple ID / SKU / store · ASC · deep links / summary; open App Store или ASC
- Icons: ASC build artwork → iTunes Lookup → monogram, disk cache

### Overview и готовность к релизу

- Latest version/build, module shortcuts, recent review submissions
- **Soft checklist** (primary screenshot size, copyright, age rating и др.)
- Versions / Submissions — **hard blockers** (build state, demo credentials при необходимости)
- Guide: `iappmanager://release-guide`

### Versions, builds и submissions

- Create versions, attach builds, submit / cancel, release modes (manual / auto / scheduled), phased release, **Release Now** при pending developer release
- **Build Upload REST** IPA/PKG; build size; diagnostics; Beta App Clip; export compliance
- **Background Assets** (`.aar`) create / chunked upload / External Beta & App Store review paths
- **Encryption declarations** с upload документов; soft check из Overview
- **Review Submissions** draft / add items / submit; «now» или «add to draft»
- **Review Detail** — contact, demo account, notes, attachments, Routing App Coverage

### Store listing и рост

- **Metadata** — App Info vs Version Listing; categories, copyright, EULA, primary locale; Android mapping; multi-locale с ★ primary; **cross-locale copy**
- **Screenshots & previews** — by version / locale / device size; reservation upload; cross-locale; poster frame timecode; coverage real assets
- **Batch assets workstation** — upload across locales × sizes
- **Download-size workbench** — inspect sizes с soft limit hints
- **SKU search** в My Apps; adaptive action bars на узких экранах
- **Custom Product Pages**, **In-App Events**, **App Clips**, **store experiments**, **featuring nominations**
- **Availability**, **pricing** (price point + apply — equalization preview), **age rating**, **accessibility**, **App Tags**
- **⌘S** save на Mac

### Монетизация и Game Center

- IAP / subscription groups, localizations, review screenshots/notes, territorial availability, price points
- Intro / promo / win-back; **Offer Codes**; promotional images; grace period; server notification URLs; CSV import/export; submit
- Guide: `iappmanager://iap-guide`
- **Game Center** — achievements, leaderboards / sets, challenges / activities, multiplayer, matchmaking

### TestFlight

- Groups, public links, recruitment criteria, metrics, invites, individual testers, builds, What to Test, beta license / review
- Feedback inbox и CSV + **bulk export full-size screenshots / crash logs** (Mac folder / iOS zip + manifest)
- Guide: `iappmanager://testflight-guide`

### Сертификаты, пользователи, отчёты, отзывы

- Certificates (in-app CSR / import) · profiles · Bundle IDs & capabilities · Merchant / Pass Type · devices (**macOS**: Keychain install)
- User invites, roles, app visibility, provisioning; Sandbox testers
- **Reports** — sales / finance / Analytics, scenarios, custom presets, **wide TSV preview** и **summary charts**; `iappmanager://reports-guide`
- Customer reviews — filter, search, reply / delete, **reply templates** (max 20 per account)
- **Webhooks** — create / edit / ping / delivery

### Виджеты, shortcuts, polish

- Widgets: **Account Hub**, **Apps Pulse** (S/M/L), **Review Desk**, **Quick Actions**
- `iappmanager://` + App Intents — [Shortcut Links](url-scheme)
- Appearance, accent, EN / 简 / 繁 (hot swap)
- iOS **alternate icons** (IconStyle1–7); StoreKit tip; feedback email

### Конфиденциальность

- API secrets в **Keychain** устройства; business API только **Apple**
- Optional icons via iTunes Lookup; clear thumbnail cache в Settings
- App Group — только **local** widget snapshots; no upload iHTC Studio
- Details: [Privacy Policy](privacy)

## Скачать

| Канал | Ссылка |
|-------|--------|
| App Store | [Download on the App Store](https://apps.apple.com/app/id6794497110) |

## Системные требования

| Компонент | Минимум |
|-----------|---------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |
| Widgets | iOS 17.0+ |
| Большие IPA | **Mac** рекомендуется |

## Контакты

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Обычно отвечаем в течение 48 часов.

[FAQ](faq) · [Shortcut Links](url-scheme) · [Privacy Policy](privacy)
