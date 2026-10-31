iZhuangZi 지원 ** `izhuangzi://` ** 단축키 링크 (URL 계획). 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
izhuangzi://{host}?{params}
```


## 책임 & 저자

| URL | 열리는 화면 |
|-----|-------|
| `izhuangzi://passage?id={id}` | 구절 상세 |
| `izhuangzi://saying?id={id}` / `izhuangzi://couplet?id={id}` / `izhuangzi://poem?id={id}` | 통행과 같 ( 겸용성) |
| `izhuangzi://passage?id={id}&card=1` | 통행 세부사항과 카드 장 |
| `izhuangzi://card?id={id}` / `izhuangzi://share-card?id={id}` | 카드 |
| `izhuangzi://author?id={id}` | 작가 상세 |
| `izhuangzi://recite` / `izhuangzi://recite?id={id}` | 낭독 흐름 |

## 디스커버리 & 연습

| URL | 열리는 화면 |
|-----|-------|
| `izhuangzi://home` | 홈 |
| `izhuangzi://daily` | 매일 Zhuangzi |
| `izhuangzi://random` | 무작위 구절 |
| `izhuangzi://favorites` | 즐겨찾기 |
| `izhuangzi://famous` | 명구 목록 |
| `izhuangzi://search` / `izhuangzi://search?q={query}` | 검색 |
| `izhuangzi://study` / `izhuangzi://study?id={id}` | Dao 연구 |
| `izhuangzi://hunt` | 주앙 헌트 (`keyword-hunt`/`flyflower`) |
| `izhuangzi://handwriting` | Handwriting search (`handwrite`; iOS) |
| `izhuangzi://mastered` | 마스터 (`progress`) |
| `izhuangzi://categories` / `izhuangzi://categories?section=` | 둘러보기 |
| `izhuangzi://collection?id=` | 컬렉션/책 (`neipian`/`waipian`/`zapian`) |
| `izhuangzi://corpus` | 모든 통행 (`all`) |
| `izhuangzi://last-read` | 마지막으로 읽은 항목 |
| `izhuangzi://reading-history` | 읽기 기록 |
| `izhuangzi://notes` | 메모 |
| `izhuangzi://ask` | Zhuangzi 소개 |
| `izhuangzi://allegories` | 옵션 정보 |
| `izhuangzi://concepts` | 회사 소개 |
| `izhuangzi://theme?id=neipian` | 내부 / 외부 / 기타 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `izhuangzi://settings` | 설정 |
| `izhuangzi://usage-guide` | 사용 가이드 |
| `izhuangzi://widget-guide` | 위젯 가이드 |
| `izhuangzi://shortcuts-guide` | 단축어 가이드 |
| `izhuangzi://feature-guide` | 온보딩 다시 보기 |
| `izhuangzi://feedback` | 피드백 이메일 |
| `izhuangzi://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
izhuangzi://daily
izhuangzi://passage?id=1
izhuangzi://ask
izhuangzi://allegories
izhuangzi://collection?id=neipian
izhuangzi://study
izhuangzi://hunt
```


## 메모

- 매개 변수는 ID가 숫자인지 여부를 감지합니다.
- Siri, Shortcuts, 위젯 및 제어 센터 제어는 동일한 딥 링크 루트를 사용합니다.
- in-app**Settings → 도움말** 최신 목록 안내


