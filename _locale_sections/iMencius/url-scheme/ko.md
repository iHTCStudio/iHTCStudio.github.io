iMencius는 ** `imencius://` ** 단축키 링크 (URL 계획)를 지원합니다. 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
imencius://{host}?{params}
```


## 책임 & 저자

| URL | 열리는 화면 |
|-----|-------|
| `imencius://passage?id={id}` | 구절 상세 |
| `imencius://saying?id={id}` / `imencius://couplet?id={id}` / `imencius://poem?id={id}` | 통행과 같 ( 겸용성) |
| `imencius://passage?id={id}&card=1` | 통행 세부사항과 카드 장 |
| `imencius://card?id={id}` / `imencius://share-card?id={id}` | 카드 종류 |
| `imencius://author?id={id}` | 작가 상세 |
| `imencius://recite` / `imencius://recite?id={id}` | 낭독 흐름 |

## 디스커버리 & 연습

| URL | 열리는 화면 |
|-----|-------|
| `imencius://home` | 홈 |
| `imencius://daily` | 매일 말 |
| `imencius://random` | 무작위 구절 |
| `imencius://favorites` | 즐겨찾기 |
| `imencius://famous` | 명구 목록 |
| `imencius://search` / `imencius://search?q={query}` | 검색 |
| `imencius://study` / `imencius://study?id={id}` | Qi 연구 |
| `imencius://hunt` | 이헌 (`keyword-hunt`/`flyflower`) |
| `imencius://handwriting` | Handwriting search (`handwrite`; iOS) |
| `imencius://mastered` | 마스터 (`progress`) |
| `imencius://categories` / `imencius://categories?section=` | 둘러보기 |
| `imencius://collection?id=` | 컬렉션 / 책 |
| `imencius://corpus` | 모든 통행 (`all`) |
| `imencius://last-read` | 마지막으로 읽은 항목 |
| `imencius://reading-history` | 읽기 기록 |
| `imencius://notes` | 메모 |
| `imencius://fables` / `imencius://allegories` / `imencius://concepts` | 사용할 때 특수 선반 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `imencius://settings` | 설정 |
| `imencius://usage-guide` | 사용 가이드 |
| `imencius://widget-guide` | 위젯 가이드 |
| `imencius://shortcuts-guide` | 단축어 가이드 |
| `imencius://feature-guide` | 온보딩 다시 보기 |
| `imencius://feedback` | 피드백 이메일 |
| `imencius://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
imencius://daily
imencius://passage?id=1
imencius://study
imencius://hunt
```



