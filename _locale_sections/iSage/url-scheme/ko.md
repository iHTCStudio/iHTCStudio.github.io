iSage는 ** `isage://` ** 단축키 링크 (URL 계획)를 지원합니다. 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
isage://{host}?{params}
```


## Sayings & 저자

| URL | 열리는 화면 |
|-----|-------|
| `isage://passage?id={id}` | 자주 묻는 질문 |
| `isage://saying?id={id}` / `isage://couplet?id={id}` / `isage://poem?id={id}` | 통행과 같 ( 겸용성) |
| `isage://passage?id={id}&card=1` | Saying 세부 사항 및 sage 카드 시트 |
| `isage://card?id={id}` / `isage://share-card?id={id}` | Sage 카드 |
| `isage://author?id={id}` | 작가 상세 |
| `isage://recite` / `isage://recite?id={id}` | 낭독 흐름 |

## 디스커버리 & 연습

| URL | 열리는 화면 |
|-----|-------|
| `isage://home` | 홈 |
| `isage://daily` | 오늘의 지혜 |
| `isage://random` | 무작위 말 |
| `isage://favorites` | 즐겨찾기 |
| `isage://famous` | 명구 목록 |
| `isage://search` / `isage://search?q={query}` | 검색 |
| `isage://study` / `isage://study?id={id}` | Sage 아카데미 |
| `isage://hunt` | Sage Hunt (`keyword-hunt`/`flyflower`) |
| `isage://handwriting` | Handwriting search (`handwrite`; iOS) |
| `isage://mastered` | 마스터 (`progress`) |
| `isage://categories` / `isage://categories?section=` | 둘러보기 |
| `isage://collection?id=guxun` | 클래식 recension (`zhou-shang`/`zhou-xia`; 또한 `book`/`form`) |
| `isage://corpus` | 모든 말 (`all`) |
| `isage://theme?id=conduct` | 테마 (예 : `cultivation`, `learning`, `friendship`, `household`, `wealth`, `virtue`, `fortune`, `speech`, `loyalty`, `diligence`, `world`) |
| `isage://last-read` | 마지막으로 읽은 항목 |
| `isage://reading-history` | 읽기 기록 |
| `isage://notes` | 메모 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `isage://settings` | 설정 |
| `isage://usage-guide` | 사용 가이드 |
| `isage://widget-guide` | 위젯 가이드 |
| `isage://shortcuts-guide` | 단축어 가이드 |
| `isage://feature-guide` | 온보딩 다시 보기 |
| `isage://feedback` | 피드백 이메일 |
| `isage://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
isage://daily
isage://passage?id=1
isage://passage?id=1&card=1
isage://collection?id=guxun
isage://theme?id=conduct
isage://study
isage://hunt
isage://handwriting
```


## 메모

- 매개 변수는 ID가 숫자인지 여부를 감지합니다.
- Siri, Shortcuts, 위젯 및 제어 센터 제어는 동일한 딥 링크 루트를 사용합니다.
- in-app**Settings → 도움말** 최신 목록 안내


