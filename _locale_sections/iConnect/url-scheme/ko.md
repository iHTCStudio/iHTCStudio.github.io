iConnect 지원 ** `iconnect://` ** URL 계획 딥 링크 — 탭을 열고, 설정 페이지, 또는 사파리에서 인앱 시트, 다른 응용 프로그램, 북마크, 또는 애플 단축키. 이 URL은 iPhone 및 iPad에서 **홈 화면 빠른 동작 **로 사용할 수있는 목적지를 미러합니다 (앱 아이콘을 길게 누릅니다).

> **참고: ** URL 링크만 ** iConnect 내부의 navigate **. 그들은 동료에 연결하지 않고 전송을 시작하거나 특정 채팅 스레드를 엽니 다.

## 프로토콜


```
iconnect://<host>
iconnect://<host>?refresh=1
```


| Rule | 제품 정보 |
|------|--------|
| **Scheme** | `iconnect``를 |
| **Host / path** | 단일 세그먼트,**case-insensitive** — URL**host** 또는 첫번째 **path** 세그먼트에서 해결 |
| **Aliases** | 몇몇 주인은 동의를 받아들입니다 (아래 표 참조) |
| **Query** | 단지 `refresh=1`/`refresh=true` 에 **Devices** 트리거 발견 새로 고침 |

동등한 형태의 예:


```
iconnect://devices
iconnect://open/devices
```


---

## 탭 대상

| URL | 열리는 화면 |
|-----|--------|---------|
| `iconnect://devices` | **Devices** tab (radar / discovery) | `장치` |
| `iconnect://devices?refresh=1` | **Devices** tab and **refreshes** nearby discovery | — |
| `iconnect://chat` | **Chats** tab | `메시지` |
| `iconnect://transfers` | **Transfers** tab | `전송` |
| `iconnect://history` | **History** tab (transfer log) | — |
| `iconnect://settings` | **Settings** tab | `설정` |

**추천**


```
iconnect://devices?refresh=1
iconnect://devices/refresh
```


---

## 설정 하위 페이지

이 링크 스위치 ** 설정**, 다음 일치하는 페이지를 엽니다:

| URL | 열리는 화면 |
|-----|--------|---------|
| `iconnect://about` | About | — |
| `iconnect://usage` | Usage Guide | `guide`, `help`, `usageguide` |
| `iconnect://shortcuts` | Home Screen shortcuts picker (iOS) | `homeshortcuts``에 대하여 |
| `iconnect://debug` | Debug / diagnostics info | `debuginfo````를 호출합니다. |

---

## In-app 작업

| URL | 열리는 화면 |
|-----|--------|
| `iconnect://share` | iConnect 시트 (App Store 링크 + 권장 텍스트) |
| `iconnect://feedback` | 피드백 이메일 compose (우편이 사용 불가) |
| `iconnect://review` | 앱 앱 상점 평가 신속한 |

**리뷰 별명:** `iconnect://` , `iconnect` ---

## 예시

** 채팅 탭 열기 **


```
iconnect://chat
```


**환불 탭 열기 **


```
iconnect://transfers
```


** Refresh 장치 발견 **


```
iconnect://devices?refresh=1
```


**사용 가이드**


```
iconnect://usage
```


** 앱 공유 **


```
iconnect://share
```


---

## 홈 화면 빠른 행동 (iOS)

iConnect 아이콘을 오래 누르십시오. **4** shortcuts in **Settings → Home Screen Shortcuts** (주문에 드래그).

| Quick Action | 사이트 맵 |
|--------------|-----|
| Devices | `iconnect://장치` |
| Chats | `iconnect://chat`````````` |
| Transfers | `iconnect://transfers```를 입력합니다. |
| History | `iconnect://history````````` |
| Share | `iconnect://share`````````` |
| Feedback | `iconnect://feedback```````` |
| Rate | [공식 홈페이지] |
| About | `iconnect://about`에 관하여 |

기본 활성화: **Devices**, **Chats**, **Share**, **Feedback**.

Quick-action 유형은 동일한 `iconnect://` 문자열을 사용하며 외부 URL과 동일한 파서를 통해 경로화됩니다.

---

## Apple 바로가기

**환불 탭 열기 **

1. 행동 추가 ** URL 열기 **
2. URL: `iconnect://` ** Wi-Fi 가입 후 주변 장치 검색 **


```
iconnect://devices?refresh=1
```


use **Open URL** 개인 자동화에서 (예: Wi-Fi가 연결될 때) 검색 및 재스캔으로 이동합니다.

---

## 시작 동작

iConnect가 URL (cold 시작 또는 실행 중)을받을 때 :

1. 링크는 `iconnect://` 에 의해 파싱됩니다.
2. 탭은 즉시 animate를 전환합니다; **share**, **feedback**, **review**는 짧은 지연 후에 열립니다 (~0.4 iOS에서 s) 그래서 UI는 설치를 완료할 수 있습니다.
3.**Feedback**는 in-app Mail을 사용할 때 사용합니다. 그렇지 않으면 `iconnect://` 를 통해 기본 메일 클라이언트를 엽니다.
4. ** 공유 ** Mac에서는 시스템 공유 피커를 사용합니다. iOS에서는 공유 시트를 제공합니다.

---

## 문제 해결

| Issue | 자주 묻는 질문 |
|-------|----------------|
| Link does nothing | iConnect가 설치됩니다. 호스트는 위의 지원 이름을 일치해야합니다. |
| `feedback` opens Mail only | 장치에서 구성된 메일 계정 없음 — 예상되는 fallback |
| `shortcuts` has no effect on Mac | 홈 화면 바로 가기 사용자 정의 **iOS 전용 ** |
| URL does not connect to a device | 딥 링크만 탐색 — 장치 탭을 사용하여 찾기를 수동으로 |

---

[iConnect Support](..) · [FAQ](../faq) · [Privacy Policy](../privacy)


