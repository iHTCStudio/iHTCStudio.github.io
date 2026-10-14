iPrimer 지원 ** `iprimer://` ** 단축키 링크 (URL 계획). 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
iprimer://{host}?{params}
```


## 장 & 저자

| URL | 열리는 화면 |
|-----|-------|
| `iprimer://chapter?id={id}` | 장 세부 사항 |
| `iprimer://passage?id={id}` / `iprimer://poem?id={id}` | 챕터와 동일 ( 호환성) |
| `iprimer://author?id={id}` | 작가 상세 |
| `iprimer://recite` / `iprimer://recite?id={id}` | 낭독 흐름 |

## 탐색

| URL | 열리는 화면 |
|-----|-------|
| `iprimer://home` | 홈 |
| `iprimer://daily` | 오늘의 일일 학습 |
| `iprimer://random` | 무작위 장 |
| `iprimer://favorites` | 즐겨찾기 |
| `iprimer://famous` | 명구 목록 |
| `iprimer://search` / `iprimer://search?q={query}` | 검색 |
| `iprimer://study` | 문자 학습 |
| `iprimer://meditation` | Meditation 과정 목록 |
| `iprimer://meditation?slug={slug}&autostart=1` | 세션 및 자동 시작 (foreground) |
| `iprimer://guidance` | 삶의 길 (journal & 습관) |
| `iprimer://hunt` | 헌트 (fly); aliases `keyword-hunt`/`flyflower` |
| `iprimer://mastered` | 마스터드 장 |
| `iprimer://categories` / `iprimer://categories?section=` | 둘러보기 |
| `iprimer://collection?id=xiaoxue` | Xiaoxue 컬렉션 (`name=`도 지원) |
| `iprimer://theme?id=lijiao` | Volume / theme (`name=鶏` 또는 `Relationships`도 지원) |
| `iprimer://last-read` | 마지막으로 읽은 항목 |
| `iprimer://reading-history` | 읽기 기록 |
| `iprimer://notes` | 메모 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `iprimer://settings` | 설정 |
| `iprimer://usage-guide` | 사용 가이드 |
| `iprimer://widget-guide` | 위젯 가이드 |
| `iprimer://shortcuts-guide` | 단축어 가이드 |
| `iprimer://feature-guide` | 온보딩 다시 보기 |
| `iprimer://feedback` | 피드백 이메일 |
| `iprimer://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
iprimer://daily
iprimer://chapter?id=3
iprimer://collection?id=xiaoxue
iprimer://theme?id=lijiao
iprimer://study
iprimer://meditation?slug=emotion_calm&autostart=1
iprimer://guidance
iprimer://hunt
```


Shortcuts 앱, 홈 화면 빠른 행동, 위젯, 또는 사파리에서 이러한 사용. Prefer stable `iprimer://` 사용할 때 매개 변수. in-app**Settings → 단축키 가이드** 참조.


