iPomodoro 지원 ** `iPomodoro://` ** 및 ** `iPomodoros://` ** URL 계획 딥 링크 — Safari, 다른 앱, QR 코드 또는 Apple Shortcuts에서 탭 또는 인앱 시트를 엽니다. 이 URL은 **Home Screen Quick Actions** (앱 아이콘을 길게 누릅니다)로 이용 가능한 목적지를 미러링합니다.

> **주의:** URL 링크가 ** 시작하거나 타이머를 중지, 작업 ID를 전달, 또는 사전 충전 기간. 앱 내에서만 탐색합니다. 앱을 열지 않고 말한 초점 요약을 위해 **Siri App Shortcuts** ([Related: Siri & App Shortcuts](#related-siri--app-shortcuts) 아래 참조).

## 프로토콜


```
iPomodoro://<path>
iPomodoros://<path>
```


| Rule | 제품 정보 |
|------|--------|
| **Schemes** | `iPomodoro` (primary) · `iPomodoros` (또한 허용) |
| **Path** | 단일 세그먼트,**case-insensitive** — URL에서 해결**host** |
| **Query parameters** | 지원되지 않음 (현재 경우 무시) |
| **Equivalent Quick Action type** | `iPomodoro://<path>` (홈 화면 단축키에 등록된 문자열) |

Path matching is **exact** on the 세그먼트 이름 — 앱은 같은 fuzzy-match substrings하지 않습니다 `iPomodoro://` .

---

## 대상 화면

| Path | Opens | 메모 |
|------|--------|-------|
| `pomodoro` | **Pomodoro** tab | 자동 시작은 없습니다. |
| `study` | **Study Timer** tab | 자동 시작은 없습니다. |
| `tasks` | **Tasks** tab |  |
| `stats` | **Statistics** tab |  |
| `motivation` | **Motivational Quote Anthology** full-screen gallery | 같은 UI ** 설정 → 동기 부여 따옴표 설정 → 동기 부여 따옴표 Anthology** |
| `feedback` | **Feedback** sheet | in-app Mail compose를 사용할 때 사용; `mailto:`로 돌아가십시오. |

---

## 예시

**Open Pomodoro 탭 **


```
iPomodoro://pomodoro
```


**Open Study Timer 탭 ** (단일 계획)


```
iPomodoros://study
```


**Open 통계 대시보드 **


```
iPomodoro://stats
```


** 동기 부여 견적**


```
iPomodoro://motivation
```


**Open 피드백**


```
iPomodoro://feedback
```


---

## Behavior 출시

앱이 URL(cold start or while running)을 수신할 때:

1. `iPomodoro://` 는 `iPomodoros://` 를 통해 길을 해결합니다.
2. 항법은 **deferred ~0.45 s ** 그래서 SwiftUI는 거치를 완료할 수 있습니다.
3.**cold start**, URL / Quick Action takes **priority** over automatically jumping to the active Pomodoro or Study tab from the restored Live Activity session.

**Motivation** 및 **feedback**는 오버레이를 직접 엽니다 — 그들은 탭을 먼저 전환하지 않습니다.

---

## Apple 바로가기

**Open Pomodoro 탭 **

1. 행동 추가 ** URL 열기 **
2. URL: `iPomodoro://` ** 초점 블록 후 통계를 엽니 다 **


```
iPomodoro://stats
```


Use**Open URL** 개인 자동화(예: 포커스 모드 종료 후)에서 대시보드로 이동합니다.

---

## 관련: Siri & 앱 바로가기

내장 ** 앱 단축키 ** (시리 / 단축키 앱) URL 링크 보완 :

| Intent | 채용 정보 |
|--------|----------|
| Open Pomodoro | Pomodoro 탭으로 전환 |
| Open Study Timer | Timer 탭으로 전환 |
| Open Statistics | 통계 탭으로 전환 |
| Today's focus summary | 앱 UI를 필요로 하지 않고 오늘 초점 기간과 pomodoro 카운트를 반환 ** |

예 Siri 구문 : * "어떻게 나는 iPomodoro에서 오늘 집중 했습니까?"*

**Settings → App settings → Home Screen Shortcuts** (주문에 드래그) 아래 홈 화면 아이콘에 4 개의 항목이 나타납니다. 위의 URL 경로는 모든 6개의 가능한 목적지를 커버합니다; 단지 4는 한 번에 아이콘에 나타날 수 있습니다.

---

## 문제 해결

| Issue | 자주 묻는 질문 |
|-------|----------------|
| Link does nothing | 앱을 설치합니다. 경로는 위의 6 이름 중 하나이어야합니다. |
| Wrong tab after reopening | 타이머 라이브 활동이 활성화되면 ** Quick Action / URL 실행 overrides** 자동 탭 복원 |
| `feedback` opens Mail app only | 장치에는 구성된 메일 계정이 없습니다. iPomodoro는 `mailto:`로 돌아갑니다. |

---

[Back to iPomodoro Support](../) &middot; [FAQ](../faq) &middot; [개인정보 보호 정책](../privacy)


