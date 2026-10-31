iMusic 지원 ** `imusic://` ** 단축 링크. 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 이동하므로 링크는 내장 후 두 번 열 수 없습니다.

## 링크 형식


```
imusic://{host}?{params}
```


Scheme은 ** `imusic://` **만 있습니다.

## 홈 & 오늘

| URL | 열리는 화면 |
|-----|-------|
| `imusic://` / `imusic://home` | 홈 |
| `imusic://daily` / `imusic://today` | 매일 조각 (쿼이 트랙 만) |
| `imusic://random` | Roam (전체 리브 shuffle) |
| `imusic://play` | 이름 * |
| `imusic://last` / `imusic://lastheard` | 마지막 듣기 |

## 조각 & 예술가

| URL | 열리는 화면 |
|-----|-------|
| `imusic://piece?id={id}` | 조각 가이드 (`passage` / `song`도 허용) |
| `imusic://artist?id={id}` / `imusic://artist?name={name}` | 아티스트 데스크 |
| `imusic://artists` / `imusic://singers` | 비밀번호 |
| `imusic://famous` / `imusic://lines` | 명구 목록 |

공유 카드 발러 추가 할 수 있습니다 `imusic://` (제목 · 작가) 인간의. 일치는 여전히 사용 ** `imusic` 만 **.

## 검색 및 듣기

| URL | 열리는 화면 |
|-----|-------|
| `imusic://categories` / `imusic://browse` | 검색 (`section=catalog`/`all`/`allpieces`→ 모든 조각) |
| `imusic://collection?id={id}` | 컬렉션 (`id=col-all`는 가상 모든 조각 목록입니다) |
| `imusic://search` / `imusic://search?q={query}` | 검색 |
| `imusic://favorites` | 즐겨찾기 |
| `imusic://later` | 즐겨찾기, 나중에 스크롤 |
| `imusic://lists` / `imusic://listenlists` | 자주 묻는 질문 |
| `imusic://history` | - 연혁 |
| `imusic://notes` | 메모 |
| `imusic://mastered` | 끝마친 |
| `imusic://streak` / `imusic://footprint` | 사이트맵 |

단일 조각, 미니 바, 또는 노래 ID ** 설정 ** 그 조각에 대한 독서 큐. 수집, 검색, 또는 예술가에서 열기는 다음 목록을 유지 / 이전 숙박 가능.

## 노래 ID, 학교 및 분위기

| URL | 열리는 화면 |
|-----|-------|
| `imusic://recognize` / `imusic://shazam` | 송 ID |
| `imusic://school` / `imusic://earschool` | 귀 학교 |
| `imusic://timeline` / `imusic://corridor` | Era 복도 |
| `imusic://compare` | 듣기 비교 |
| `imusic://mood?id={id}` | 그 기분을 시작하십시오 (`piece=` / `pieceId=`는 시작 트랙 만입니다. 기분은 여전히 `id`) |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `imusic://settings` | 설정 |
| `imusic://usageguide` / `imusic://featureguide` | 사용법/기능 가이드 |
| `imusic://widgetguide` | 위젯 가이드 |
| `imusic://shortcutsguide` | 단축어 가이드 |
| `imusic://feedback` | 이름 * |
| `imusic://review` / `imusic://in-app-review` | In-app review (점포 목록이 생길 때) |

## Siri & 홈 화면

오늘 조각, roam, 검색, 또는 당신이 단축키를 추가 한 후 즐겨 찾기에 대한 Siri에 문의하십시오. 홈 화면을 구성 ** 설정 → 단축키 **. 전체 예제 in-app Shortcuts 가이드에서 라이브.

[FAQ](../faq) · [개인정보 보호 정책](../privacy) · [지원](../)


