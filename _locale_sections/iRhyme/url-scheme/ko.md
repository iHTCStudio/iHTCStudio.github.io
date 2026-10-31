iRhyme 지원 ** `irhyme://` ** 단축키 링크 (URL 계획). 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
irhyme://{host}?{params}
```


## 책임 & 저자

| URL | 열리는 화면 |
|-----|-------|
| `irhyme://passage?id={id}` | 구절 상세 |
| `irhyme://saying?id={id}` / `irhyme://couplet?id={id}` / `irhyme://poem?id={id}` | 통행과 같 ( 겸용성) |
| `irhyme://passage?id={id}&card=1` | 통행 세부사항과 카드 장 |
| `irhyme://card?id={id}` / `irhyme://share-card?id={id}` | Rhyme 카드 |
| `irhyme://author?id={id}` | 작가 상세 |
| `irhyme://recite` / `irhyme://recite?id={id}` | 낭독 흐름 |

## 디스커버리 & 연습

| URL | 열리는 화면 |
|-----|-------|
| `irhyme://home` | 홈 |
| `irhyme://daily` | 오늘의 Rhyme |
| `irhyme://random` | 무작위 구절 |
| `irhyme://favorites` | 즐겨찾기 |
| `irhyme://famous` | 명구 목록 |
| `irhyme://search` / `irhyme://search?q={query}` | 검색 |
| `irhyme://study` / `irhyme://study?id={id}` | Rhyme 아카데미 |
| `irhyme://hunt` | Rhyme Hunt (`keyword-hunt`/`flyflower`) |
| `irhyme://handwriting` | Handwriting search (`handwrite`; iOS) |
| `irhyme://mastered` | 마스터 (`progress`) |
| `irhyme://categories` / `irhyme://categories?section=` | 둘러보기 |
| `irhyme://collection?id=` | 컬렉션 / 책 (`shenglv`/`liweng`/`qianjia`/`youxue`) |
| `irhyme://corpus` | 모든 통행 (`all`) |
| `irhyme://last-read` | 마지막으로 읽은 항목 |
| `irhyme://reading-history` | 읽기 기록 |
| `irhyme://notes` | 메모 |
| `irhyme://pair` | 병렬 연습 |
| `irhyme://prosody` | Prosody 책상 |
| `irhyme://rhyme?id=dong` | 1개의 rhyme 종류 |
| `irhyme://compare?rhyme=dong` | Same-rhyme 비교 |
| `irhyme://glossary?id=` | 회사 소개 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `irhyme://settings` | 설정 |
| `irhyme://usage-guide` | 사용 가이드 |
| `irhyme://widget-guide` | 위젯 가이드 |
| `irhyme://shortcuts-guide` | 단축어 가이드 |
| `irhyme://feature-guide` | 온보딩 다시 보기 |
| `irhyme://feedback` | 피드백 이메일 |
| `irhyme://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
irhyme://daily
irhyme://passage?id=1001
irhyme://pair
irhyme://compare?rhyme=dong
irhyme://collection?id=shenglv
irhyme://study
irhyme://hunt
```


## 메모

- 매개 변수는 ID가 숫자인지 여부를 감지합니다.
- Siri, Shortcuts, 위젯 및 제어 센터 제어는 동일한 딥 링크 루트를 사용합니다.
- in-app**Settings → 도움말** 최신 목록 안내


