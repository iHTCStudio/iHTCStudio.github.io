iThousand support** `ithousand://` ** 단축키 링크 (URL 계획). 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
ithousand://{host}?{params}
```


## Passages, 저자 및 문자

| URL | 열리는 화면 |
|-----|-------|
| `ithousand://passage?id={id}` | 구절 상세 |
| `ithousand://passage?id={id}&open=study` | Passage → 프라임 홀 |
| `ithousand://passage?id={id}&open=characters` | Passage → 문자 테이블 |
| `ithousand://passage?id={id}&open=note` | Passage → 참고 |
| `ithousand://author?id={id}` | 작가 상세 |
| `ithousand://recite` / `ithousand://recite?id={id}` | 낭독 흐름 |
| `ithousand://characters` | 캐릭터 라이브러리 |
| `ithousand://character?char=天` | 캐릭터 카드 초점 |
| `ithousand://characters?id={id}` | ID로 문자 카드 |
| `ithousand://saved-characters` | 저장된 문자 |
| `ithousand://saved-famous` | 저장된 유명한 선 |

## 탐색

| URL | 열리는 화면 |
|-----|-------|
| `ithousand://home` | 홈 |
| `ithousand://daily` | 오늘의 일일 라인 |
| `ithousand://random` | 무작위 구절 |
| `ithousand://favorites` | 즐겨찾기 |
| `ithousand://list?id={uuid}` | 개인 목록 ()) |
| `ithousand://famous` | 명구 목록 |
| `ithousand://search` / `ithousand://search?q={query}` | 검색 |
| `ithousand://study` | 프라임 홀 |
| `ithousand://hunt` | 헌트 (fly); aliases `keyword-hunt`/`flyflower` |
| `ithousand://mastered` | 인기있는 |
| `ithousand://categories` / `ithousand://categories?section=` | 둘러보기 |
| `ithousand://collection?id=qianziwen` | Primer 컬렉션 (`name=`도 지원) |
| `ithousand://theme?id=dizigui-filial` | 이름 * |
| `ithousand://last-read` | 마지막으로 읽은 항목 |
| `ithousand://reading-history` | 읽기 기록 |
| `ithousand://notes` | 메모 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `ithousand://settings` | 설정 |
| `ithousand://privacy` | In-app 프라이버시 |
| `ithousand://usage-guide` | 사용 가이드 |
| `ithousand://widget-guide` | 위젯 가이드 |
| `ithousand://shortcuts-guide` | 단축어 가이드 |
| `ithousand://feature-guide` | 온보딩 다시 보기 |
| `ithousand://feedback` | 피드백 이메일 |
| `ithousand://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
ithousand://daily
ithousand://passage?id=1
ithousand://passage?id=1&open=characters
ithousand://character?char=天
ithousand://collection?id=qianziwen
ithousand://study
ithousand://hunt
ithousand://saved-characters
```


Shortcuts 앱, 홈 화면 빠른 행동, 위젯, 또는 사파리에서 이러한 사용. Prefer stable `ithousand://` 사용할 때 매개 변수. in-app**Settings → 단축키 가이드** 참조.


