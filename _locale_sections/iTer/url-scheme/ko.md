iTer는 ** `iTer://` ** URL 계획 **iPhone 및 iPad**를 지원합니다. Shortcuts, Safari, 위젯, 또는 다른 앱에서 질문을 열고, 매일 퀴즈, 즐겨 찾기, 또는 잘못된-answer 책.

**홈 화면 Quick Actions** (앱 아이콘을 길게 누르십시오) `iTer://` 문자열을 재사용합니다. **7 ** 옵션 ** 설정 → 홈 화면 단축 **에서 ** 4**까지 선택하십시오.

> **참고:** 딥 링크 **navigate** 앱 내부. 그들은 퀴즈 설정을 변경하지 않거나 질문을 원격으로 표시하지 않습니다. **Mac**는 홈 화면 빠른 동작을 등록하지 않습니다. 위젯과 인앱 탐색은 여전히 Mac에서 작동합니다.

## 프로젝트


```
iTer://<host>[?query]
```


| Rule | 제품 정보 |
|------|--------|
| **Scheme** | `iTer` (case-insensitive)를 호출합니다. |
| **Question detail** | 호스트 `question` — 쿼리 **`id=<questionID>`** 또는 **`q=<questionID>`** (필수) |
| **Daily Quiz** | 호스트 `quiz` |
| **Favourites** | 호스트 `favorites` → 설정 → Favourites 목록 |
| **Wrong book** | 호스트 `wrong`, `mistakes`, 또는 `wrongquestions` — 옵션 **`record=<UUID>`**는 한 실수를 엽니다. |
| **Search** | Host `search` — Quick Action / 단축키 만 (글로벌 검색 탭 열기) |
| **Categories** | 호스트 `categories` — 빠른 행동 / 단축키 만 (카테고리 카테고리 탭 열기) |
| **Feedback** | 호스트 `feedback` - 빠른 행동 만 (이메일 compose 또는 `mailto:` fallback) |
| **Rate app** | 호스트 `review` — Quick Action only (StoreKit in-app review). 'star'도 일하는 레거시 유형. | `iTer://` 과 같은 경로는 호스트가 비어있을 때 허용됩니다.

## 예시


```
iTer://question?id=94c34bb2bdef11e6a0e100163e0021c8
iTer://quiz
iTer://favorites
iTer://wrong
iTer://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## 홈 화면 빠른 행동

| Type | 일반 사용 |
|------|-------------|
| `iTer://search` | 글로벌 검색 |
| `iTer://quiz` | 매일 퀴즈 탭 |
| `iTer://favorites` | Favourites 목록 |
| `iTer://wrong` | Wrong-answer 책 |
| `iTer://categories` | 카테고리 탭 |
| `iTer://feedback` | 견적 요청 |
| `iTer://review` | 앱 평가 (StoreKit) |

기본 선택: 검색, Quiz, Favourites, 피드백. 주문 또는 ** 설정 → 홈 화면 단축키 ** (최대 4). app match shortcut `iTer://` strings with**contains**, 이 경로는 여전히 올바른 경로가 포함 된 유산 변형.

## Widget 깊은 링크

| Widget | 일반적인 URL |
|--------|-------------|
| Daily Question | `iTer://question?id=...` |
| Quiz Glance | `iTer://quiz```````` |
| Favourites Glance | `iTer://favorites`````` |
| Wrong Book Glance | `iTer://wrong` 또는 `iTer://wrong?record=<UUID>` |

---

[iTer Support로 돌아가기](../) · [FAQ](../faq) · [Privacy Policy](../privacy)


