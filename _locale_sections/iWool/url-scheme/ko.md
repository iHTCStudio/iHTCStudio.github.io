iWool 지원 ** `iwool://` ** URL 계획 딥 링크 — 탭을 열고, 앱 액션을 시작하거나, Safari, Apple Shortcuts, 위젯 탭 또는 홈 화면 빠른 행동 (앱 아이콘을 길게 누릅니다)에서 특정 활동으로 이동합니다.

> ** 중요 : ** 딥 링크 만 ** iWool 내부 나비 게이트 **. 서버 연결 또는 동기화 데이터를 클라우드로 만들지 않습니다.

## 프로토콜


```
iwool://<path>[?query]
```


| Rule | 제품 정보 |
|------|--------|
| **Scheme** | `iwool` (케이스 민감성) |
| **Routing** | 첫 번째 경로 세그먼트 (호스트 또는 경로) 목적지 선택 |
| **Empty URL** | `iwool://` 경로 없음 → **홈** |
| **Unknown paths** | ** 임신 ** (집에 침묵 낙하 없음) |
| **Parser** | `IWoolDeepLink.parse( :)`→ `ContentView.applyDeepLink`````````````` |

---

## 1. 탭 대상

| URL | 열리는 화면 |
|-----|--------|---------|
| `iwool://home` | **Home** tab | — |
| `iwool://calendar` | **Calendar** tab | '칼' |
| `iwool://stats` | **Statistics** tab | `statistics`, `stat` |
| `iwool://settings` | **Settings** tab | `설정`, `preferences` |

---

## 2. 앱 작업

이 경로 일치 **홈 화면 빠른 행동** 및 열린 시트 또는 하위 페이지:

| URL | 열리는 화면 |
|-----|--------|---------|
| `iwool://new` | **Create activity** sheet | `create`, `add`, `new-event`, `newevent` |
| `iwool://island` | **Quick Countdown** (Dynamic Island reminder) sheet | `island-reminder`, `islandreminder`, `countdown`, `quick-countdown`, `quickcountdown` |
| `iwool://reminders` | **Scheduled local reminders** list (Settings) | `scheduled-reminders`, `scheduledreminders`, `scheduled`, `notification-reminders` |
| `iwool://scanner` | **QR / barcode scanner** (Settings → Tools) | `scan`, `qrcode`, `barcode` |
| `iwool://rate` | In-app **App Store rating** prompt | `rating`, `review`, `rate-in-app`, `rateinapp` |
| `iwool://feedback` | **Feedback** email compose | `mail`, `support`, `contact` |

**제한 설정 경로**(same action):


```
iwool://settings/scanner
iwool://settings/reminders
iwool://settings/rate
iwool://settings/feedback
```


---

## 3. 활동 세부사항

데이터베이스 ID로 단일 울 활동을 엽니 다.

| Parameter | Required | 이름 * |
|-----------|----------|-------------|
| Path `event/{id}` | One of path / query | 활동 ID (긍정 정수) |
| Query `id={id}` | One of path / query | 경로 형태와 동일 |
| Query `day={seconds}` | No | ** 등록 ** 활동 - 자연 일 시작으로 `timeIntervalSince1970` (그런 결과의 밤) |

**영업 42**


```
iwool://event/42
iwool://event?id=42
```


**특정 당일에 발생한 발생 **


```
iwool://event/42?day=189345600
```


recurring 시리즈를 위한 건물 연결 때, iWool는 가정 명부 ( `iwool` )와 동일한 논리에서 derive `iwool://` 할 수 있습니다.

---

## 4. 홈 화면 빠른 행동 (iOS)

iWool 아이콘 → 최대 **4** 작업. 에서 사용자 지정 ** 설정 → 도구 → 홈 화면 단축키 ** (9 옵션, 명령으로 드래그, 기본값으로 재설정).

| Option | 사이트 맵 |
|--------|-----|
| Home | `iwool=홈` |
| Calendar | `iwool://calendar``````` |
| Statistics | `iwool://stats`````` |
| Quick Countdown | `iwool://island````````` |
| New Activity | `iwool://new````````` |
| Scheduled Reminders | `iwool://reminders`````` |
| Scanner | `iwool://scanner```````` |
| Rate App | `iwool://rate```````` |
| Feedback | `iwool://feedback`````` |

**기본 설치:** 집 · 달력 · 통계 · 빠른 카운트 다운.

Quick-action `iwool://` 문자열은 같은 사용 `iwool` 경로와 경로를 통해 `iwool://` → `IWoolDeepLink.parse(_:)` 감기 시작.

---

## 5. 위젯 딥 링크

위젯 탭은 같은 사용 `iwool://` URL:

| Widget | Tap target | 사이트 맵 |
|--------|------------|-----|
| Today Active / Today All / Today Upcoming / All Events | Home | `iwool=홈` |
| Stats Overview / Earnings / Top Platforms | Statistics | `iwool://stats`````` |
| Glance | First event or Home | `iwool://event/{id}` 또는 `iwool://home` |
| Lock Screen accessories | First event or Home | `iwool://event/{id}` 또는 `iwool://home` |
| List row (iOS 17+) | Activity detail | `iwool://event/{id}````` |

Quick Countdown Live Activities use in-app UI only — ** 별도의 URL** 앱 외부에서 섬 카운트 다운을 시작합니다 (use `iwool://` 생성 시트를 열려면).

---

## Apple Shortcuts 예제

** 통계 숨기기 **


```
iwool://stats
```


**새로운 활동을 등록 **


```
iwool://new
```


** Quick Countdown 시트 열기 **


```
iwool://island
```


** ID 복사 후 활동 열기 **


```
iwool://event?id=42
```


---

## 시작 동작

| Scenario | 제품정보 |
|----------|------|
| **Widget / Shortcuts `onOpenURL`** | `AppRouter` → `applyDeep 링크` |
| **Cold start — Quick Action** | `ShortcutSceneDelegate` → `PendingShortcutBuffer` → `ShortcutObserver` |
| **Warm start — Quick Action** | 장면 콜백 → 알림 → `ShortcutObserver` |
| **Feedback / Rate (cold start)** | 짧은 지연 그래서 메일 시트 / StoreKit는 활성 창 장면 |
| **Invalid event ID** | 링크 무시 — 알림 없음 |

---

## 문제 해결

| Issue | 자주 묻는 질문 |
|-------|----------------|
| Link opens app but nothing happens | 경로는 지원된 경로에 일치해야합니다; 알 수없는 경로는 홈으로 리디렉션되지 않습니다 |
| `event` link shows wrong occurrence | recurring 활동을 위한 `?day=` 추가 |
| Quick Action does nothing on cold launch | ~0.4 s 또는 retry를 대기하십시오; 의견/rate 필요 UI 산 시간 |
| `iwool://island` does not start countdown automatically | **creation sheet**를 엽니다. - 앱 내에서 지속적이고 탭 시작을 확인합니다. |
| Quick Countdown requires iOS 16.2+ | 이벤트 라이브 활동 필요 iOS 16.1+; 독립 섬 카운트 다운 필요 16.2+ |

---

[Back to iWool Support](..) · [FAQ](../faq) · [개인정보 보호정책](../privacy)


