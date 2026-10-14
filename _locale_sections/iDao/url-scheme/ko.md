iDao는 ** `idao://` ** 단축키 링크 (URL 계획)를 지원합니다. 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
idao://{host}?{params}
```


## 장 & 발견

| URL | 열리는 화면 |
|-----|-------|
| `idao://home` | 홈 |
| `idao://daily` | 오늘의 매일 장 |
| `idao://random` | 무작위 장 |
| `idao://chapter?id={id}` | 장 세부 사항 |
| `idao://recite` / `idao://recite?id={id}` | 낭독 흐름 |
| `idao://favorites` | 즐겨찾기 |
| `idao://famous` | 명구 목록 |
| `idao://search` / `idao://search?q={query}` | 검색 |
| `idao://study` | 연구 홀 |
| `idao://hunt` | 타오( Tao道) |
| `idao://mastered` | 인기있는 |
| `idao://categories` / `?section=` | 검색 (옵션 섹션) |
| `idao://book?id=` | 도서 수집 (`ddj`/`qingjing`/`yinfu`) |
| `idao://author` | Laozi 소개 |
| `idao://last-read` | 마지막으로 읽은 항목 |
| `idao://reading-history` | 읽기 기록 |
| `idao://notes` | 메모 |

> 호환성 별명으로: `idao://` / `idao://home` → 장; `idao://daily` → 연구; `idao://random` → 사냥; `idao://chapter?id={id}` → 저자; `idao://recite` → 카테고리 섹션; `idao://recite?id={id}` → 카테고리.

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `idao://settings` | 설정 |
| `idao://usage-guide` | 사용 가이드 |
| `idao://widget-guide` | 위젯 가이드 |
| `idao://shortcuts-guide` | 단축어 가이드 |
| `idao://feature-guide` | 온보딩 다시 보기 |
| `idao://feedback` | 피드백 이메일 |
| `idao://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
idao://daily
idao://chapter?id=1
idao://recite?id=1
idao://study
idao://hunt
idao://famous
idao://book?id=ddj
idao://author
idao://search?q=上善若水
```


Shortcuts 앱에서 이러한 사용, 홈 화면 빠른 행동, 위젯, 제어 센터, 또는 사파리. in-app**Settings → 단축키 가이드** 참조.


