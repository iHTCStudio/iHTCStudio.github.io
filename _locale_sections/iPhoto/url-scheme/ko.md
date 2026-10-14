iPhoto는 ** `iphoto://` ** 깊은 링크와 **App Intents / Siri Shortcuts**를 지원합니다. 링크는 앱 내에서만 이동 - 그들은 데이터를 업로드하지 않습니다.

## 사이트맵


```
iphoto://<host>[?query]
```


| Rule | 제품 정보 |
|------|--------|
| Scheme | iphoto의 |
| Empty | 앱의 기본 탭을 엽니다 |
| Unknown hosts | 안전하다 |

---

## 탭 및 탐색

| URL | 열리는 화면 |
|-----|-------|
| `iphoto://library` | 도서관 탭 |
| `iphoto://capture` | 캡처 탭 |
| `iphoto://settings` | 설정 탭 |
| `iphoto://search` | 검색 탭 (iOS 18+) |
| `iphoto://recent-projects` | 최근 작업에 중점을 둔 도서관 |

---

## 한국어

| URL | 열리는 화면 |
|-----|-------|
| `iphoto://editor?id=<projectID>` | 주어진 프로젝트 ID에 대한 편집기 |

---

## 가이드 & 행동

| URL | 열리는 화면 |
|-----|-------|
| `iphoto://usage-guide` | 사용 가이드 |
| `iphoto://widget-guide` | 위젯 가이드 |
| `iphoto://shortcuts-guide` | 단축어 가이드 |
| `iphoto://feature-guide` | 기능 / 내장 재생 |
| `iphoto://export-presets` | 수출 관련 설정 |
| `iphoto://feedback` | 피드백 이메일 |
| `iphoto://in-app-review` | In-app 검토 신속한 |

---

## Siri 및 단축키

내장 intents 포함:

- 공지사항
- 본문 바로가기
- 수입 사진
- 설정 열기

Shortcuts 앱에 추가하거나 Shortcuts에 표시된 구문을 사용하여 Siri를 호출합니다.

## 예시


```
iphoto://capture
iphoto://library
iphoto://editor?id=YOUR-PROJECT-ID
iphoto://widget-guide
```


[FAQ](../faq) · [개인정보 보호 정책](../privacy) · [iPhoto로 돌아가기](../)


