iCangJie 지원 ** `iCangJie://` ** URL 계획 딥 링크 — 오픈 검색, 워드 세부 사항, 매일 퀴즈, 타이핑, 즐겨찾기, 잘못된 책, 레벨, 또는 사파리에서 배울, 또 다른 응용 프로그램, QR 코드, 위젯 탭, 또는 애플 단축키.

홈 화면 Quick Actions** (앱 아이콘을 길게 누르십시오)의 병렬 세트는 검색, 피드백 및 비율과 같은 추가 목적지를 포함합니다. **Settings → App Settings → Home Screen Shortcuts**에서 최대 4개의 단축키 구성

## 프로토콜


```
iCangJie://<host>[?query]
```


| Rule | 제품 정보 |
|------|--------|
| **Scheme** | `icangjie`/`iCangJie` — case-insensitively 비교 |
| **Host routing** | 기본 라우터는 URL ** 호스팅 ** |
| **Query aliases** | `q`, `word`, `name`는 검색/word 호스트의 교환이 가능합니다. |
| **Parser** | `ICangJieDeepLink.parse( :)` - `onOpenURL` → `AppRouter.pendingDeepLink`를 통해 소모 |

** 3 배달 채널 **

| Channel | Handled by | 예시 |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ICangJieDeepLink.parse` → `RootTabView` | `search`, `word`, `quiz`, `typing`, `favorites`, `wrong`, `level`, `learn` |
| **Home Screen Quick Action** | `ShortcutObserver.dispatch` | `search`, `quiz`, `favorites`, `wrong`, `level`, `feedback`, `review` |
| **App Intents / Siri / Widget pending URL** | Writes `AppGroup.pendingDeepLinkURL` → `RootTabView.consumePendingDeepLinkFromAppGroup()` | 조회 코드, 시작 퀴즈, 열린 검색 |

Quick-action type use ** `iCangJie://` ** type string에 매칭하므로, `icangjie` 와 레거시 변형은 여전히 올바르게 변형됩니다.

---

## 1. 조회 수

**Lookup** 탭을 엽니다. 선택적으로 사전 채우기 검색 필드.

| Parameter | Required | 이름 * |
|-----------|----------|-------------|
| `q` | No | 검색 쿼리 (코드 접두사, 문자, pinyin, 또는 Jyutping) |
| `word` | No | `q`를 위한 동의어 |
| `name` | No | `q`를 위한 동의어 |

**Open Lookup (비어 있는 검색)**


```
iCangJie://search
```


**코드 접두사 검색 `iCangJie://` **


```
iCangJie://search?q=ab
```


** 캐릭터 검색 **


```
iCangJie://search?q=颉
```


---

## 2. Word 세부사항

단일 문자에 대한 세부 페이지를 엽니다. 비empty 쿼리가 필요합니다.

| Parameter | Required | 이름 * |
|-----------|----------|-------------|
| `q` | One of `q` / `word` / `name` | 대상 Han 캐릭터 |
| `word` | One of `q` / `word` / `name` | `q`를 위한 동의어 |
| `name` | One of `q` / `word` / `name` | `q`를 위한 동의어 |

** 허용 호스트 : ** `iCangJie://` , `icangjie` , `iCangJie` **에 대한 세부 정보 **


```
iCangJie://word?q=倉
```


Alternate 호스트:


```
iCangJie://character?word=颉
```


쿼리가 **empty 또는 문자가 사전 **에 있지 않은 경우, 링크는 ** 분명히 무시 **.

---

## 3. 매일 퀴즈

**Daily Quiz**에 직접 점프하십시오. 자동 시작 또는 건너뛰기 질문은 없습니다.


```
iCangJie://quiz
```


Aliases : `iCangJie://` ---

## 4. 타이핑 연습

** 타이핑** 탭 허브를 엽니다.


```
iCangJie://typing
```


Aliases : `iCangJie://` , `icangjie` ---

## 5. 즐겨찾기

** 즐겨 찾기 ** 목록.


```
iCangJie://favorites
```


별명으로: `iCangJie://` ---

## 6. 잘못된 대답 책

### 6.1 목록

** 잘못된 답변 책 ** 목록.


```
iCangJie://wrong
```


Aliases : `iCangJie://` , `icangjie` ### 6.2 단 하나 기록

언제 `iCangJie://` 는 저장 된 잘못 answer 항목의 유효 UUID, 응용 프로그램은 기록의 단어 세부 사항 (기록이 여전히 존재하는 경우)를 엽니 다.

| Parameter | Required | 지원하다 |
|-----------|----------|--------|
| `record` | Yes | UUID 문자열 |
| `id` | Yes | `record`를 위한 동의어 |


```
iCangJie://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


---

## 7. 수준 (코드 길이)

**Levels** 탭을 엽니다.


```
iCangJie://levels
```


Aliases : `iCangJie://` , `icangjie` ---

## 8. 알아보기 (Tutorials)

**Learn** 허브를 엽니다.


```
iCangJie://learn
```


Aliases : `iCangJie://` ---

## 9. 의견 (빠른 행동 전용)

사전 채워진 피드백 이메일 작곡가 (또는 `iCangJie://` fallback)를 엽니다.


```
iCangJie://feedback
```


으로 처리 **홈 화면 빠른 행동** / `iCangJie://` , 아니 `icangjie` .

---

## 10. App Store Review (빠른 행동 만)

in-app App Store 검토를 취소하십시오.


```
iCangJie://review
```


Alias matching also accepts `iCangJie://` 빠른 액션 타입 문자열.

---

## 11. 앱 의도 및 Siri (iOS 16+)

Built-in **App Shortcuts**는 Shortcuts 앱과 Siri에 나타났습니다. App Group의 각 intent set `iCangJie://` ; 앱은 출시에 소비합니다.

| Intent | Action | URL을 종료 |
|--------|--------|-------------|
| **Look up Cangjie code** | Opens word detail for the given character | `iCangJie://word?q=<char>```` |
| **Start daily quiz** | Opens Daily Quiz | `iCangJie://quiz``````` |
| **Open lookup search** | Opens Lookup tab | `iCangJie://search``````` |

**Example Siri 구문 (영어) **

- * "iCangJie"*에서  for에 대한 Cangjie 코드를 봐
- * "iCangJie에서 매일 퀴즈 시작"*
- * "iCangJie에서 검색 Cangjie"*

**Shortcuts**에서 iCangJie 앱 섹션에서 동작을 추가합니다. **Look up** intent는 **중국어 문자** 매개변수( `iCangJie://` )를 요구합니다.

> App Intents는 **iOS 만 **입니다. macOS는 `iCangJie://` URL 및 메뉴 네비게이션에 의존합니다.

---

## Widget 딥 링크

같은 `iCangJie://` URL을 탭합니다. 예제:

| Widget | 일반적인 URL |
|--------|-------------|
| Daily Character | `iCangJie://word?q=<char>```` |
| Code Length | `iCangJie://levels`````` |
| Daily Quiz | `iCangJie://quiz``````` |
| Typing Glance | `iCangJie://typing`````` |
| Favorites | `iCangJie://favorites`````` |
| Wrong Book | `iCangJie://wrong```````` |
| Recent | `iCangJie://search``````` |
| Learning Progress | `iCangJie://learn``````` |

---

## 단축키 예제

**오늘의 퀴즈 열기 **


```
iCangJie://quiz
```


** 클립보드에서 문자를 찾습니다 **

Shortcuts**Get Clipboard** 동작을 사용하여 **Open URL**:


```
iCangJie://word?q=[Clipboard]
```


**시작 태핑 연습**


```
iCangJie://typing
```


---

## 홈 화면 빠른 행동

iCangJie 앱 아이콘을 오래 누르십시오. 기본 옵션 (설정에서 최대 4까지):

| Action | 사이트 맵 |
|--------|-----|
| Search | `iCangJie://search``````` |
| Daily Quiz | `iCangJie://quiz``````` |
| Favorites | `iCangJie://favorites`````` |
| Wrong Book | `iCangJie://wrong```````` |
| Code Length | `iCangJie://levels`````` |
| Feedback | `iCangJie://feedback````` |
| Rate App | 숙박 플랜 |


