iPrecepts 지원 ** `iprecepts://` ** 단축키 링크 (URL 계획). 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
iprecepts://{host}?{params}
```


## 책임 & 저자

| URL | 열리는 화면 |
|-----|-------|
| `iprecepts://passage?id={id}` | 구절 상세 |
| `iprecepts://saying?id={id}` / `iprecepts://couplet?id={id}` / `iprecepts://poem?id={id}` | 통행과 같 ( 겸용성) |
| `iprecepts://passage?id={id}&card=1` | 통행 세부사항과 카드 장 |
| `iprecepts://card?id={id}` / `iprecepts://share-card?id={id}` | 카드 제외 |
| `iprecepts://author?id={id}` | 작가 상세 |
| `iprecepts://recite` / `iprecepts://recite?id={id}` | 낭독 흐름 |

## 디스커버리 & 연습

| URL | 열리는 화면 |
|-----|-------|
| `iprecepts://home` | 홈 |
| `iprecepts://daily` | 매일 |
| `iprecepts://random` | 무작위 구절 |
| `iprecepts://favorites` | 즐겨찾기 |
| `iprecepts://famous` | 명구 목록 |
| `iprecepts://search` / `iprecepts://search?q={query}` | 검색 |
| `iprecepts://study` / `iprecepts://study?id={id}` | 가족 학습 |
| `iprecepts://hunt` | 헌트를 제외하고 (`keyword-hunt`/`flyflower`) |
| `iprecepts://handwriting` | Handwriting search (`handwrite`; iOS) |
| `iprecepts://mastered` | 마스터 (`progress`) |
| `iprecepts://categories` / `iprecepts://categories?section=` | 둘러보기 |
| `iprecepts://collection?id=` | 수집/책 (zhuxi/zhubailu/yanshi/zhuge/zeng/yuanshi/Qian/tingxun/shortworks) |
| `iprecepts://corpus` | 모든 통행 (`all`) |
| `iprecepts://last-read` | 마지막으로 읽은 항목 |
| `iprecepts://reading-history` | 읽기 기록 |
| `iprecepts://notes` | 메모 |
| `iprecepts://compare` | 병렬 비교 |
| `iprecepts://theme?id=` | 이름 * |
| `iprecepts://authors` | 이름 * |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `iprecepts://settings` | 설정 |
| `iprecepts://usage-guide` | 사용 가이드 |
| `iprecepts://widget-guide` | 위젯 가이드 |
| `iprecepts://shortcuts-guide` | 단축어 가이드 |
| `iprecepts://feature-guide` | 온보딩 다시 보기 |
| `iprecepts://feedback` | 피드백 이메일 |
| `iprecepts://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
iprecepts://daily
iprecepts://passage?id=1
iprecepts://passage?id=1&card=1
iprecepts://compare
iprecepts://collection?id=yanshi
iprecepts://study
iprecepts://hunt
```


## 메모

- 매개 변수는 ID가 숫자인지 여부를 감지합니다.
- Siri, Shortcuts, 위젯 및 제어 센터 제어는 동일한 딥 링크 루트를 사용합니다.
- in-app**Settings → 도움말** 최신 목록 안내


