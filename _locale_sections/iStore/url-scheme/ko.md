iStore 지원 ** `istore://` ** 단축 링크. **Shortcuts**, Safari bookmarks, 또는 **widgets**, **Control Center**, **Spotlight** 및 **Share Extension** to ** 지역을 전환 **, **re-switch your last area**, ** 탭 열기 **, 또는 **jump to guide**.

## 링크 형식


```
istore://{host}?{params}
```


호스트는 **case-insensitive**입니다. 지역 코드 사용 표준 **Alpha-2** 값 ( `istore://` , `us` , `cn` , `jp` , `hk` , ...).

| What you want | 링크 메뉴 |
|---------------|------|
| Switch to a region | `istore://switch?region={code}`를 호출합니다. |
| Switch to your last region | `istore://switch-last````````` |
| Open the Store / Favorites / Settings tab | `istore://store` · `istore://favorites` · `istore://settings` |
| Open App Availability | `istore://availability```````` |

---

## 지역 전환

지정된 지역에 스위치를 요청합니다 (인앱 확인을 통해 루트).


```
istore://switch?region={code}
```


| Parameter | Required | 이름 * |
|-----------|----------|-------------|
| `region` | **Yes** | 지역 코드, 예를 들어 `us`, `cn`, `jp`, `hk`, `tw` |

**예금 **


```
istore://switch?region=us
```


에 의해 사용하는: **interactive 위젯**, **Spotlight** 결과, **Shortcuts / Siri**.

---

## 당신의 마지막 지역에 스위치


```
istore://switch-last
```


가장 최근의 스위치 대상을 읽고 다시 전환합니다. ** Switch Last** 제어 센터 제어(iOS 18+) 및 일치 단축키 / Siri 동작.

---

## 탭 & 페이지 (질문 없음)

| URL | 열리는 화면 |
|-----|-------|
| `istore://store` | 상점 탭 |
| `istore://favorites` | 즐겨찾기 탭 |
| `istore://settings` | 설정 탭 |
| `istore://availability` | 설정 → App Availability (또한 공유 확장에 의해 사용) |
| `istore://switch-history` | 스위치 History |
| `istore://quick-regions` | 빠른 지역 설정 |
| `istore://feature-guide` | 기능 가이드 |
| `istore://widget-guide` | 위젯 가이드 |
| `istore://shortcuts-guide` | 단축어 가이드 |
| `istore://usage-guide` | 사용 가이드 |
| `istore://feedback` | 피드백 이메일 |
| `istore://in-app-review` | 앱 내 App Store 평가 |

---

## Widgets, 제어 센터 및 스포트라이트

이 생성 `istore://` 링크는 자동으로 입력할 때:

| Source | Tap target | 제품 정보 |
|--------|------------|--------|
| **Quick Regions / Recent / Custom widget** | A region tile | `istore://switch?region=...` |
| **Switch Last control** (iOS 18+) | The control | `istore://switch-last````````` |
| **Spotlight** | A region result | `istore://switch?region=...` |

위젯과 컨트롤 센터의 대화식 전환은 앱을 열고 공식 앱 스토어 리디렉션을 완료합니다.

---

## 공유 확장

** 앱 스토어 링크 ** iStore로 공유하십시오. 대중적인 지역에 걸쳐 공유 확장 체크 가용성, 다음을 통해 앱을 열 수 있습니다 `istore://` 그래서 당신은 결과와 스위치를 검토할 수 있습니다.

---

## Siri 및 단축키

**Shortcuts** 앱 또는 요청 **Siri**에서 내장 작업을 찾습니다. 제목과 문구는 영어로 현지화 / 한국어 / 繁體中文.

| Action | What you can set | 제품 정보 |
|--------|------------------|--------|
| Switch region | Region | 해당 지역으로 전환 |
| Switch last region | — | 당신의 마지막 목표에 전환 |
| Switch favorite region | A favorite | 가장 좋아하는 지역으로 전환 |
| Open store | — | iStore 오픈 |
| Check availability | App link or ID | 앱을 사용할 수 있는 체크 |

---

## 링크에서 지역 코드

딥 링크 및 위젯 생성 된 URL은 항상 안정 ** 등록 코드 ** ( `istore://` , `us` , `cn` , `jp` , ...) - 현지화 된 디스플레이 이름.

**예시**


```
istore://switch?region=jp
istore://switch?region=hk
```


[경찰](..) · [FAQ](../faq) · [Privacy](../privacy)


