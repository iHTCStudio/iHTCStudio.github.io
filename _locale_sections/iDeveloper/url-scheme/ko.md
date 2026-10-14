iDeveloper는 ** `ideveloper://` ** 단축키 링크 (URL 계획)를 지원합니다. 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
ideveloper://{host}?{params}
```


## 도구 및 검색

| URL | 열리는 화면 |
|-----|-------|
| `ideveloper://home` | 홈 |
| `ideveloper://tool?id={id}` | 도구 세부 사항 (예 : `json`, `base64`, `timestamp`) |
| `ideveloper://category?id={id}` | 카테고리 (예: `encoding`) |
| `ideveloper://search` / `ideveloper://search?q={query}` | 검색 |
| `ideveloper://favorites` | 즐겨찾기 |
| `ideveloper://history` | 작업 역사 |
| `ideveloper://reference` / `ideveloper://reference?id={id}` | 참조 센터 / 항목 |
| `ideveloper://new-snippet` | 새로운 스니펫 |
| `ideveloper://focus` | Focus timer / 실시간 활동 참여 |
| `ideveloper://share?tool={id}` | 도구로 공유하기 (Share extension + App Group payload) |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `ideveloper://settings` | 설정 |
| `ideveloper://usage-guide` | 사용 가이드 |
| `ideveloper://widget-guide` | 위젯 가이드 |
| `ideveloper://shortcuts-guide` | 단축어 가이드 |
| `ideveloper://feature-guide` | 온보딩 다시 보기 |
| `ideveloper://feedback` | 피드백 이메일 |
| `ideveloper://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
ideveloper://tool?id=json
ideveloper://search?q=base64
ideveloper://reference?id=http-200
ideveloper://favorites
ideveloper://focus
ideveloper://share?tool=json
ideveloper://category?id=encoding
```


Shortcuts 앱에서 이러한 사용, 홈 화면 빠른 행동, 위젯, 제어 센터, 또는 사파리. in-app**Settings → 단축키 가이드** 참조.


