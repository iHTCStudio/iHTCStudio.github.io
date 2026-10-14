iLvShi는 ** `ilvshi://` ** 단축키 링크 (URL 계획)를 지원합니다. 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
ilvshi://{host}?{params}
```


## 책임 & 저자

| URL | 열리는 화면 |
|-----|-------|
| `ilvshi://passage?id={id}` | 구절 상세 |
| `ilvshi://saying?id={id}` / `ilvshi://couplet?id={id}` / `ilvshi://poem?id={id}` | 통행과 같 ( 겸용성) |
| `ilvshi://passage?id={id}&card=1` | 통행 세부사항과 카드 장 |
| `ilvshi://card?id={id}` / `ilvshi://share-card?id={id}` | 秋 카드 |
| `ilvshi://author?id={id}` | 작가 상세 |
| `ilvshi://recite` / `ilvshi://recite?id={id}` | 낭독 흐름 |

## 디스커버리 & 연습

| URL | 열리는 화면 |
|-----|-------|
| `ilvshi://home` | 홈 |
| `ilvshi://daily` | 매일 통행 |
| `ilvshi://random` | 무작위 구절 |
| `ilvshi://favorites` | 즐겨찾기 |
| `ilvshi://famous` | 명구 목록 |
| `ilvshi://search` / `ilvshi://search?q={query}` | 검색 |
| `ilvshi://study` / `ilvshi://study?id={id}` | 봄–학사 |
| `ilvshi://hunt` | 가을 사냥 (`keyword-hunt`/`flyflower`) |
| `ilvshi://handwriting` | Handwriting search (`handwrite`; iOS) |
| `ilvshi://mastered` | 마스터 (`progress`) |
| `ilvshi://categories` / `ilvshi://categories?section=` | 둘러보기 |
| `ilvshi://collection?id=` | 컬렉션 / 책 |
| `ilvshi://corpus` | 모든 통행 (`all`) |
| `ilvshi://last-read` | 마지막으로 읽은 항목 |
| `ilvshi://reading-history` | 읽기 기록 |
| `ilvshi://notes` | 메모 |
| `ilvshi://fables` / `ilvshi://allegories` / `ilvshi://concepts` | 사용할 때 특수 선반 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `ilvshi://settings` | 설정 |
| `ilvshi://usage-guide` | 사용 가이드 |
| `ilvshi://widget-guide` | 위젯 가이드 |
| `ilvshi://shortcuts-guide` | 단축어 가이드 |
| `ilvshi://feature-guide` | 온보딩 다시 보기 |
| `ilvshi://feedback` | 피드백 이메일 |
| `ilvshi://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
ilvshi://daily
ilvshi://passage?id=1
ilvshi://study
ilvshi://hunt
```



