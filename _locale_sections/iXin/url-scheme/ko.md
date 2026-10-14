iXin은 ** `ixin://` ** 단축키 링크 (URL 계획)를 지원합니다. 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
ixin://{host}?{params}
```


## 책임 & 저자

| URL | 열리는 화면 |
|-----|-------|
| `ixin://passage?id={id}` | 구절 상세 |
| `ixin://saying?id={id}` / `ixin://couplet?id={id}` / `ixin://poem?id={id}` | 통행과 같 ( 겸용성) |
| `ixin://passage?id={id}&card=1` | 통행 세부사항과 카드 장 |
| `ixin://card?id={id}` / `ixin://share-card?id={id}` | Insight 카드 |
| `ixin://author?id={id}` | 작가 상세 |
| `ixin://recite` / `ixin://recite?id={id}` | 낭독 흐름 |

## 디스커버리 & 연습

| URL | 열리는 화면 |
|-----|-------|
| `ixin://home` | 홈 |
| `ixin://daily` | 매일 통찰력 |
| `ixin://random` | 무작위 구절 |
| `ixin://favorites` | 즐겨찾기 |
| `ixin://famous` | 명구 목록 |
| `ixin://search` / `ixin://search?q={query}` | 검색 |
| `ixin://study` / `ixin://study?id={id}` | 심장 학교 |
| `ixin://hunt` | 하트 헌트 (`keyword-hunt`/`flyflower`) |
| `ixin://handwriting` | Handwriting search (`handwrite`; iOS) |
| `ixin://mastered` | 마스터 (`progress`) |
| `ixin://categories` / `ixin://categories?section=` | 둘러보기 |
| `ixin://collection?id=` | 컬렉션 / 책 (`chuanxilu`/`daxuewen`/`jiaotiao`/`yilvwen`/시) |
| `ixin://corpus` | 모든 통행 (`all`) |
| `ixin://last-read` | 마지막으로 읽은 항목 |
| `ixin://reading-history` | 읽기 기록 |
| `ixin://notes` | 메모 |
| `ixin://journal` | Knowing-Acting 저널 |
| `ixin://liangzhi` | Liangzhi의 세 가지 질문 |
| `ixin://graph` | 컨셉 그래프 |
| `ixin://timeline` | 연락처 |
| `ixin://map` | 지도보기 |
| `ixin://people` | 이름 * |
| `ixin://achievements` | 회사연혁 |
| `ixin://theme?id=` | 이름 * |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `ixin://settings` | 설정 |
| `ixin://usage-guide` | 사용 가이드 |
| `ixin://widget-guide` | 위젯 가이드 |
| `ixin://shortcuts-guide` | 단축어 가이드 |
| `ixin://feature-guide` | 온보딩 다시 보기 |
| `ixin://feedback` | 피드백 이메일 |
| `ixin://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
ixin://daily
ixin://passage?id=1
ixin://journal
ixin://liangzhi
ixin://collection?id=chuanxilu
ixin://study
ixin://hunt
```


## 메모

- 매개 변수는 ID가 숫자인지 여부를 감지합니다.
- Siri, Shortcuts, 위젯 및 제어 센터 제어는 동일한 딥 링크 루트를 사용합니다.
- in-app**Settings → 도움말** 최신 목록 안내


