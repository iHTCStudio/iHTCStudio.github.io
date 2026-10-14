iLinux는 ** `ilinux://` **를 지원합니다. (또한 작성된 ** `iLinux://` **) URL 계획 **iPhone, iPad 및 Mac에서 깊은 링크 ** — 오픈 명령 세부 사항 (Linux, CMD 또는 PowerShell), Daily Quiz, Favourites 또는 Wrong 응답 책 사파리, 다른 응용 프로그램, 위젯 탭 (iOS / iPad), 또는 Apple Shortcuts.

명령 URL은 옵션 ** `ilinux://` ** 쿼리 매개 변수를 수락하므로 위젯 탭 및 단축키는 Windows 항목을 올바르게 열 수 있습니다.

**홈 화면 Quick Actions** ( **iOS/iPad 만 **) 커버 검색, 카테고리, 피드백 및 비율. Mac 사용자는 ** iLinux** 메뉴와 키보드 단축키를 사용할 수 있습니다.

> ** 중요 : ** iLinux는 ** 설정 및 학습 앱**입니다. URL 링크는 ** 앱 내부에 **navigate만 있습니다. 그들은**not** Linux 명령을 실행하고 SSH 세션을 열고 원격 서버에 연결합니다.

## 프로토콜


```
ilinux://<host>[/<path>][?query]
iLinux://<host>[/<path>][?query]   ← same scheme, case-insensitive
```


| Rule | 제품 정보 |
|------|--------|
| **Scheme** | `ilinux`/`iLinux` — case-insensitively 비교 |
| **Host routing** | 기본 라우터는 URL ** 호스팅 **; 일부 경로도 허용 (아래 참조) |
| **Command detail** | 호스트 `command` ** 또는** 경로 `/command` |
| **Command ID** | Query `name=<id>` ** 또는** `cmd=<id>` - 번들 명령 키 (예: `ls`, `grep`, `dir`, `Get-ChildItem`)와 일치해야 합니다. |
| **Platform** | Query `platform=<value>` — 선택 사항; 기본값은 **Linux** 때 omitted |
| **Quiz** | 호스트 `quiz` ** 또는** 경로 `/quiz` |
| **Favourites** | 호스트 `favorites` ** 또는** 경로 `/favorites` |
| **Wrong book** | 호스트 `wrong`, `mistake`, 또는 `wrongquestions`; 경로 `/wrong` 또는 `/mistake`도 허용 |
| **Wrong record** | Query `record=<UUID>`는 잘못된 책 URL에 - 레코드의 명령 세부 정보를 엽니다. |
| **Query parameters** | 다른 pre-fill 모수는 지원됩니다 |
| **Parser** | `ILinuxDeepLink.parse( :)` - `onOpenURL` → `AppRouter.pendingDeepLink`를 통해 소모 |

** 2개의 납품 수로 **

| Channel | Handled by | 예시 |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ILinuxDeepLink.parse` → `RootTabView` | `command`, `quiz`, `favorites`, `wrong` |
| **Home Screen Quick Action** | `ShortcutSceneDelegate` → `ShortcutObserver.dispatch` | `search`, `categories`, `feedback`, `review`, plus overlapping `quiz`/`favorites`/`wrong` |

Quick-action type use ** `ilinux://` ** type string에 매칭하므로, `iLinux://` 와 레거시 변형은 여전히 올바르게 변형됩니다.

---

## 1. 명령 세부사항

단일 번들 명령의 세부 페이지를 엽니다.

| Parameter | Required | 이름 * |
|-----------|----------|-------------|
| `name` | One of `name` / `cmd` | 명령 ID (플랫폼 JSON 번들의 사전 키) |
| `cmd` | One of `name` / `cmd` | 동의어: `name` — 위젯 링크에 의해 사용 |
| `platform` | No | Shell 라이브러리: 아래 표 참조. **Linux**에 기본값 |

** `ilinux://` 값** (case-insensitive):

| Value | Shell library | 이름 * |
|-------|---------------|---------|
| *(omit)* or `linux` | Linux (1050 commands) | — |
| `cmd` | CMD / Batch (300 commands) | `배치`, `배치` |
| `powershell` | PowerShell (300 commands) | `ps`, `pwsh` |

**Behaviour **

- **Commands** 탭으로 전환하여 요청된 ** 쉘 플랫폼**을 선택하고, 해결된 명령의 `CommandDetailView`를 밀어줍니다.
- ID가 ** 알려지지 않았거나 빈 **이면, 링크가 **가 무시됩니다 ** (오류 UI 없음).
- Command IDs는 **case-sensitive**이며, 묶음 JSON 키를 정확히 일치해야 합니다(일반적으로 lowcase, 예. `docker`, not `Docker`).

** 오픈 `ilinux://` **


```
ilinux://command?name=ls
```


**Open `ilinux://` (리눅스, 기본) **


```
ilinux://command?cmd=grep
```


CMD `ilinux://` **을 엽니다.


```
ilinux://command?cmd=dir&platform=cmd
```


**Open PowerShell `ilinux://` **


```
ilinux://command?cmd=Get-ChildItem&platform=powershell
```


**Cloud-native Linux 예**


```
ilinux://command?name=docker
```


---

## 2. 매일 퀴즈

**Daily Quiz** 탭으로 이동합니다. ** 자동 시작 또는 건너뛰기 질문.


```
ilinux://quiz
```


경로 형태 (또한 받아들여지는):


```
ilinux:///quiz
```


---

## 3. 특징

**Favourites ** 설정 탐색 아래 목록.


```
ilinux://favorites
```


경로 형태 (또한 받아들여지는):


```
ilinux:///favorites
```


---

## 4. 잘못된 대답 책

### 4.1 목록

** 잘못된 답변 책 ** 설정 탐색 아래 목록.


```
ilinux://wrong
```


Aliases (같은 행동):


```
ilinux://mistakes
ilinux://wrongquestions
```


### 4.2 단일 레코드 → 명령 세부 사항

언제 `ilinux://` 는 저장 된 잘못 answer 항목의 유효 UUID, 응용 프로그램은 ** COMmands** 탭을 열고 그 기록의 명령에 대한 세부 사항을 밀어 (기록 및 명령이 여전히 존재 한 경우).

| Parameter | Required | 지원하다 |
|-----------|----------|--------|
| `record` | Yes | UUID 문자열, 예. `550e8400-e29b-41d4-a716-446655440000` |


```
ilinux://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


UUID가 유효하거나 기록이 삭제 된 경우, 탐색은 잘못된 책 목록으로 돌아가거나 건너 뛰는 것입니다.

---

## 5. 가정 스크린 빠른 활동

iLinux 아이콘 → 최대 **4** 작업.**Settings → Home Screen Shortcuts** (7 옵션, 다시 주문으로 드래그, 기본값으로 재설정).

| Option | Registered `type` | SF Symbol | 공지사항 |
|--------|-------------------|-----------|--------|
| Search | `iLinux://search` | magnifyingglass | **Commands** 탭 + 검색 표시 활성화 |
| Daily Quiz | `iLinux://quiz` | checklist | **Daily Quiz** 탭 |
| Favourites | `iLinux://favorites` | star.fill | **Favourites ** 목록 |
| Wrong Answer Book | `iLinux://wrong` | xmark.bin.fill | ** 잘못된 답변 책 ** 목록 |
| Categories | `iLinux://categories` | rectangle.grid.2x2.fill | **카테고리 ** 탭 |
| Send Feedback | `iLinux://feedback` | envelope.fill | In-app mail compose (또는 `mailto:` fallback) |
| Rate App | `iLinux://review` | star.bubble.fill | StoreKit 리뷰 |

** 첫 번째 설치의 기본 선택 :** 검색 · 일일 퀴즈 · Favourites · 피드백 보내기.

** Quick-action-only 대상 ** (에 의해 처리되지 않음 `ilinux://` / `iLinux://` ):

- `iLinux://search`````````
- `iLinux://카테고리`
- `iLinux://feedback`````
- `iLinux://리뷰`

**long-press icon** 또는 Quick Action 파이프라인을 통해 동일한 유형을 게시함으로써, Shortcuts**Open URL**으로 열 수 있습니다 ** 앱이 나중에 명시된 호스트를 추가하지 않는 경우 작동하지 않을 수 있습니다.

**Legacy 타입 (실행):**

| Type | 채용 정보 |
|------|-----------|
| `iLinux://love` | in-app Safari 시트에서 저자 블로그를 엽니 다 (old static Shortcut) |

---

## 6. 위젯 딥 링크

위젯 탭은 같은 사용 `ilinux://` URL에 의해 내장 `iLinux://` :

| Widget | Tap target | 사이트 맵 |
|--------|------------|-----|
| Daily Command | Command detail | `iLinux://command?cmd=<id>&platform=<linux\ | cmd\ | 파워쉘>` |
| Category Spotlight | Sample command | `iLinux://command?cmd=<id>&platform=<platform>`` |
| Quiz Glance | Daily Quiz | `iLinux://quiz``````` |
| Favourites Glance | Favourites (or per-row command) | `iLinux://favorites`/`iLinux://command?cmd=<id>&platform=<platform>`` |
| Wrong Book Glance | Wrong book (or per-row record) | `iLinux://wrong`/`iLinux://wrong?record=<UUID>` |

Widget URL은 `ilinux://` 에 의해 만들어지고 항상 ** `iLinux://` ** 명령 탭에 포함되어 있습니다. 플랫폼 일치 ** 설정 → 위젯 → 위젯 명령 라이브러리 ** (Linux / CMD / PowerShell).

**Daily Command shuffle button** (iOS 17+, App Intent)는 위젯 타임라인만 다시 로드합니다. **는 URL을 사용하지 않습니다.

---

## Apple 바로가기

### 이름을 복사 한 후 명령을 엽니다.

1. ** 입력에서 텍스트를 가져옵니다 **
2. ** URL 열기 ** → `ilinux://` + 텍스트

또는 하드 코드 리눅스:


```
ilinux://command?name=systemctl
```


CMD 명령을 엽니다:


```
ilinux://command?cmd=ipconfig&platform=cmd
```


### 매일 공부 알림 → 퀴즈


```
ilinux://quiz
```


추가 ** 개인 자동화에서 URL** (예: 매주 9시).

### 잘못된 답변을 검토


```
ilinux://wrong
```


### Focus Mode Shortcut에서 즐겨 찾기


```
ilinux://favorites
```


---

## 시작 Behaviour

앱이 URL 또는 Quick Action을 수신할 때:

| Scenario | 제품정보 |
|----------|------|
| **Cold start — Quick Action (iOS/iPad only)** | `ShortcutSceneDelegate` → `PendingShortcutBuffer` → `ShortcutObserver.onAppear` → `dispatch(type:)` |
| **Warm start — Quick Action (iOS/iPad only)** | 장면 콜백 → 알림 → `dispatch(type:)` |
| **Cold / warm — `onOpenURL` (iOS, iPad, Mac)** | `AppRouter.handleIncomingURL` → `pendingDeepLink` → `RootTabView.onChange` 탐색 |
| **Feedback / Rate (cold start)** | `deferSheetWork` 지연 **~0.4 s** 그래서 메일 시트 / StoreKit는 활성 창 장면을 가지고 |
| **Search quick action** | `openSearchTab()` → `searchPulse += 1` → `BrowseCommandsView` 검색(iOS 17+: `isPresented`를 통해 자동 초점) |
| **Unknown command ID** | 딥 링크 파싱하지만 탐색 건너뛰기 — 알림 없음 |

---

## 키보드 단축키

### iPad 및 Mac (공유)

iPad 및 **iLinux** 메뉴에서 하드웨어 키보드:

| Shortcut | - 연혁 |
|----------|--------|
| ⌘F | 명령 탭 + 검색 (iOS에서 빠른 행동 검색과 동일) |
| ⌘1 | 명령 탭 |
| ⌘2 | 카테고리 탭 |
| ⌘3 | 매일 퀴즈 탭 |
| ⌘4 | 설정 탭 |

⌘F를 통해 자동 초점은 **iOS 17.0+** 또는 **macOS 14.0+**를 요구합니다.

### Mac 전용

| Shortcut | - 연혁 |
|----------|--------|
| ⌘, | 설정 탭 |
| ⌘[ / Esc | Pop 항법 더미 (뒤) |
| ⌘← / ⌘→ | 이전 / 다음 범주 (카테고리 탭) |
| 1–4 | 퀴즈 응답 옵션 선택 |
| ⌘R | 일일 퀴즈 |
| Return | 다음 퀴즈 질문 (응답 후) |

딥 링크 ( `ilinux://` ) 및 메뉴 단축키는 iOS에서 Mac에서 같은 앱 라우터를 사용합니다.

---

## 지원 및 잘못된 URL

| URL | Result |
|-----|--------|
| `ilinux://command` (no `name` / `cmd`) | 이름 * |
| `ilinux://command?name=NotARealCmd` | Ignored (해결된 플랫폼을위한 라이브러리에 있지 않음) |
| `ilinux://command?cmd=dir` (no platform) | Opens**Linux** 라이브러리 — Windows CMD용 `platform=cmd`를 사용합니다. |
| `ilinux://search` via Shortcuts Open URL | **Not**는 `ILinuxDeepLink`에 의해 파싱 — **iOS/iPad**, 또는 ⌘F on **Mac/iPad**에서 빠른 동작을 사용 |
| `ilinux://categories` via Shortcuts Open URL | 위와 같 |
| `ilinux://feedback` / `ilinux://review` via Open URL | 위와 같 |
| Non-`ilinux` schemes | 이름 * |

---

## 문제 해결

**Shortcut은 앱을 열었지만 아무런 일이 없습니다 (cold launch)**

피드백, 비율 및 우편 시트 필요 ~0.4 출시 후 s. 앱 내부에서 다시 시도, 또는 추운 시작에 순간을 기다립니다.

**검색 빠른 동작은 검색 필드에 초점을 맞추지 않습니다 (iOS 16)**

자동 초점은 iOS 17+를 요구합니다. iOS 16에서 명령 탭은 여전히 열려 있습니다. 검색 필드를 수동으로 탭합니다.

**Widget 탭은 예상 명령을 열지 않습니다 **

명령은 여전히 올바른 **platform**에 대한 설치된 앱 버전에서 존재합니다. 위젯 링크 사용 `ilinux://` + `iLinux://` 그리고 정확한 명령 ID가 필요합니다. 예: `platform` 필요 `ilinux` , 기본 Linux 라이브러리가 아닙니다.

**Quick-action 제목은 잘못된 언어입니다 **

언어 변경 **설정 → 언어** — 앱 등록 단축키 항목 자동.

**Deep 링크는 장치에서 작동하지만 웹 페이지에서 작동하지 **

링크를 사용하여 계획 확인 `ilinux://` 및 시스템에 의해 열 (주/메시지에서 제거), 사용자 정의 계획을 스트립 인앱 브라우저에 의해 차단되지.

---

[Back to iLinux Support](../) &middot; [FAQ](../faq) &middot; [개인정보 보호 정책](../privacy)


