iApp은 ** `iapp://` ** 및 ** `iappstore://` ** 단축키 링크를 지원합니다. **Shortcuts**, Safari bookmarks, 또는 **Home Screen widgets** 및 **Live Activity** 에 ** 앱 세부 페이지를 엽니다 **, ** 필터링 된 랭킹보기에 반환 **, ** 스위치 탭 **, 또는 **Jump to Second pages** (개발자 좋아하는, 역사, 순위 추적 및 더 많은).

> **주의:** Long-press **Home Screen Quick Actions**는 동일한 `iapp://` 링크 텍스트를 사용하지만 빠른 행동으로 파견되어 Safari / Shortcuts URL과 동일한 경로로 나타날 수 없습니다.

## 링크 형식


```
iapp://...
iappstore://...   (older alias, works the same)
```


호스트는 **case-insensitive**이며 ** kebab-case** ( `iapp://` 및 `iappstore://` → `iapp://{host}` )로 정상화됩니다. 레거시 별칭 : `developer_favorites` → 순위, `developer.favorites` → 구독, `developer-favorites` → 검토.

| What you want | 링크 유형 |
|---------------|-----------|
| Open an app detail page | `iapp://app?...` |
| Open Rankings with filters | `iapp://rank?...` |
| Switch tabs or open settings pages | `iapp://{host}` (아래 표 참조) |
| Tap an app in a widget | 자주 묻는 질문 |
| Tap the widget title / blank area | 일치하는 랭킹보기를 엽니다 |
| Tap a rank **Live Activity** | 일치하는 랭킹보기를 엽니다 |
| Tap a subscription **Live Activity** | 앱 세부 페이지를 엽니다 |

---

## 앱 상세 페이지 열기


```
iapp://app?id={APP_ID}&region={region}&country={cc}
```


| Parameter | Required | 이름 * |
|-----------|----------|-------------|
| `id` | **Yes** | 앱 스토어 ID |
| `region` | No | 지역 코드, 예를 들어 `cn`, `us`, `jp`(기본값: `us`) |
| `country` | No | `region`가 omitted라면 선택 영역 코드 |

**예금 **


```
iapp://app?id=6446581591&region=cn
```


에 의해 사용: **내 즐겨찾기 위젯** (앱을 제거), ** 구독 라이브 활동** (활동을 제거), **Shortcuts** / bookmarks.

---

## 필터로 순위 열기

**Rankings** 탭으로 전환하고 선택한 차트, 카테고리 및 지역을 적용합니다.


```
iapp://rank?type={chart}&category={category}&region={region}
```


| Parameter | 이름 * |
|-----------|-------------|
| `type` | 차트 코드 (아래 표 참조) |
| `category` | 범주 코드 - 주요 범주 또는 게임 하위 범주 |
| `region` | 지역 코드, 예를들면 `cn`, `us` |

인식된 값은 무시됩니다; 인식된 값은 기억됩니다.

### 차트 코드 ( `iapp://` ) — 12 차트

| Code | 팟캐스트 |
|------|-------|
| `topFreeApplications` | iPhone 상단 무료 |
| `topPaidApplications` | iPhone 상단 유료 |
| `topGrossingApplications` | 아이폰 탑 Grossing |
| `newApplications` | 새로운 앱 |
| `newFreeApplications` | 무료 새로운 |
| `newPaidApplications` | 새로운 유료 |
| `topFreeiPadApplications` | iPad 상단 무료 |
| `topPaidiPadApplications` | iPad 상단 유료 |
| `topGrossingiPadApplications` | iPad 상단 Grossing |
| `topFreeMacApplications` | 맥 탑 무료 |
| `topPaidMacApplications` | Mac 상단 유료 |
| `topGrossingMacApplications` | 맥 탑 Grossing |

### 범주 코드 ( `iapp://` )

| Code | (주) |
|------|----------|
| `0` | 모든 앱 |
| `6014` | 게임 (모든 게임) |
| `6005` | - 연혁 |
| `6007` | 회사연혁 |
| `6002` | (주) |
| `6008` | 사진 & 비디오 |
| `6017` | 교육과정 |
| `6015` | 재무정보 |
| … | 26 메인 카테고리 전체 |

게임 하위 카테고리:** `iapp://` – `iappstore://` , `iapp://{host}` – `developer_favorites` (18세). 예제: `developer.favorites` = 동작.

### 예시


```
iapp://rank?type=topFreeApplications&category=6014&region=cn
iapp://rank?type=topFreeMacApplications&category=0&region=us
```


### Older Chinese-style 링크 (지원되는 길)


```
iapp://rank?type=热门免费榜&category=游戏&region=中国
```


에 의해 사용: ** 락킹 위젯** (탭 제목 / 공백 영역), **랭크 라이브 활동** (활동을 제거), 및 ** 슬립**.

---

## Widget 깊은 링크

위젯은 별도의 URL 형식을 사용하지 않습니다 - 그들은 같은 생성 `iapp://` 및 `iappstore://` 링크 자동으로.

| Widget | Tap target | 공지사항 |
|--------|------------|-------|
| **Rankings · iApp** | An app row | `iapp://app?id=...&region=...` |
| **Rankings · iApp** | Title or blank area | `iapp://rank?type=...&category=...&region=...` |
| **My Favorites · iApp** | An app row | `iapp://app?id=...&region=...` |

Pinned favorites 처음으로 에 나의 마음에 드는 위젯. 위젯 테마와 언어를 따르십시오 **설정 → 위젯 ** 및 앱 언어 (모든 18 언어). 위젯 영역을 구성 할 때, HK / TW / MO는 목록과 통합 된 검색에 명확한 디스플레이 이름을 보여줍니다 (예 : "중국", "HK"); 저장된 지역 ** 코드 ** 링크에서 남아 있습니다 `iapp://` , `iappstore://` , `iapp://{host}` .

---

## 검색 내역 (URL 링크가 아닙니다)

**App Browse History**는 **Settings → Data → App Browse History**에서 관리됩니다. iApp 내부의 세부 페이지를 다시 열 수 있습니다. ** 사용할 수 없습니다 `iapp://` URL을 복사하거나 외부 공유 할 수 있습니다.

---

## 라이브 활동 깊은 링크

| Live Activity type | Tap behavior | 링크 생성 |
|--------------------|--------------|----------------|
| **Rankings** (tracking preset) | Opens filtered Rankings | `iapp://rank?...` |
| **Subscriptions** (per subscription) | Opens app detail | `iapp://app?id=...&region=...` |

**Settings → Advanced**에서 미리 설정할 수 있는 랭크 라이브 활동. **Settings → Advanced → Live Activity**(랭크 라이브 활동)에서 사용 가능한 구독 라이브 활동); 추가 또는 편집할 때 구독 당 구독. Price-drop 모니터는 Lock Screen의 현재 가격을 표시합니다.

---

## 탭 & 액션 링크 (질문 없음)

이 탭을 열고 in-app 동작을 트리거합니다. **Shortcuts**, Safari 및 **홈 화면 빠른 동작**에서 작동합니다.

### 기본 탭

| URL | 열리는 화면 |
|-----|--------|
| `iapp://search` | 검색 탭 + 초점 검색 필드 |
| `iapp://rank` | 순위 탭(필터 변경 없이 쿼리) |
| `iapp://favorites` | ** 즐겨 찾기 탭 ** ** 설정 → 앱 설정 **; 그렇지 않으면 ** 설정 → 앱 즐겨찾기 ** |
| `iapp://subscription` | 가시다면 구독 탭; 그렇지 않으면 **설정 → 구독** |
| `iapp://settings` | 설정 탭 |
| `iapp://feedback` | 피드백 이메일 |
| `iapp://review` | 앱 스토어 평가 (alias: `iapp://rate`) |

### 두 번째 페이지

opens**Settings** 탭을 먼저 열고, 대상 페이지를 밀어줍니다. 일치 탭이 존재하는 경우 (예: Developer Favorites), 대신 탭을 엽니 다.

| URL | 열리는 화면 |
|-----|--------|
| `iapp://developer-favorites` | 개발자 즐겨s 탭 또는 **Settings → 개발자 즐겨s** |
| `iapp://browse-history` | **설정 → 데이터 → 앱 검색 기록** |
| `iapp://favorite-groups` | **설정 → 데이터 → 즐겨찾기 그룹** |
| `iapp://rank-tracking` | ** 설정 → 고급 → 순위 추적** |
| `iapp://live-activity` | **설정 → 고급 → 실시간 활동** |
| `iapp://apple-services` | **설정 → 제3자 → Apple 서비스** |
| `iapp://region-switch` | **설정 → 제3자 → 앱 스토어 지역** |
| `iapp://usage-guide` | **설정 → 도움말 → 사용 설명서** |
| `iapp://widget-guide` | **설정 → 위젯 → 위젯 가이드 ** (iOS 17+ 만; URL은 Quick Actions Picker에 나열되지 않음) |

---

## 홈 화면 빠른 행동

앱 아이콘을 길게 누릅니다. **4** 부터 **15** 옵션에서 **설정 → 홈 화면 롱 프레스 → 단축키 사용자 지정**.

기본 선택: 검색, 순위, 즐겨찾기, 피드백.

각 옵션 사용 `iapp://` — 위의 URL. 빠른 행동은 아이콘 메뉴를 통해 파견됩니다. 외부 단축키 / Safari는 unified `iappstore://` 경로를 사용합니다.

| 링크 | 열리는 화면 |
|------|--------|
| `iapp://search` | 검색 탭 + 초점 |
| `iapp://rank` | 순위 탭 |
| `iapp://favorites` | 즐겨찾기 탭 또는 설정 → 앱 즐겨찾기 |
| `iapp://developer-favorites` | 개발자 즐겨찾기 탭 또는 설정 → Developer Favorites |
| `iapp://subscription` | 구독 탭 또는 설정 → 구독 |
| `iapp://browse-history` | 앱 검색 |
| `iapp://favorite-groups` | 즐겨찾기 그룹 설정 |
| `iapp://rank-tracking` | 순위 추적 |
| `iapp://live-activity` | Live Activity 설정 |
| `iapp://apple-services` | Apple 서비스 링크 |
| `iapp://region-switch` | App Store 지역 스위치 |
| `iapp://usage-guide` | 사용 설명서 |
| `iapp://settings` | 설정 탭 |
| `iapp://feedback` | 피드백 이메일 |
| `iapp://review` | 앱 평가 | `iapp://` 는 외부 URL로 지원되지만 ** Quick Actions Picker에서 사용할 수 없습니다.

---

## Siri 및 단축키 (iOS 16+)

**Shortcuts** 앱 또는 요청 **Siri**에서 내장 작업을 찾습니다. 모든 intent titles, 매개 변수 레이블 및 Siri 구문은 ** 모든 응용 언어에서 로컬화 ** - 그들은 당신이 변경할 때 업데이트 ** 설정 → 외관 → 언어 **.

| Action | What you can set | 제품 정보 |
|--------|------------------|--------|
| Search apps | Keyword and region | 쿼리로 검색 탭 열기 |
| Open charts | Chart, category, and region | 필터가있는 순위를 엽니다 (예 : `iapp://rank`) |
| Add favorite | App ID and region | 자주 묻는 질문 |

**Example Siri 구문 (English UI) : ** * "iApp에서 검색 응용 프로그램"*, * "iApp의 오픈 차트"*, * "iApp에서 좋아하는 추가"*. 한국어, 구문은 중국어로 나타났습니다. 모든 18 개 언어와 동일합니다.

---

## Mac 키보드 단축키

Mac에서, use **1⌘** via **⌘N** 탭을 전환합니다. 숫자는 할당된 **dynamically ** 어떤 탭을 기준으로:

| When visible | 일반 단축키 |
|--------------|------------------|
| Rankings | ⌘1의 |
| Search | ⌘2의 |
| Subscriptions (if shown) | 다음 번호 |
| Favorites (if tab enabled) | 다음 번호 |
| Developer Favorites (if tab enabled) | 다음 번호 |
| Settings | 계좌번호 |

모든 선택 탭의 예 : ⌘1 랭킹 · ⌘2 검색 · ⌘3 구독 · ⌘4 즐겨찾기 · ⌘5 개발자 즐겨s · ⌘6 설정.

탭이 숨겨져있을 때, 나머지 탭은 자동으로 다시 번호.

---

## 링크에서 지역 코드

딥 링크 및 위젯 생성 된 URL은 항상 안정 ** 등록 코드 ** ( `iapp://` , `iappstore://` , `iapp://{host}` , `developer_favorites` , `developer.favorites` , ...) - 현지화 된 디스플레이 이름. 지역 픽업 및 검색은 더 명확한 라벨을 표시 할 수 있지만 저장된 코드는 동일하게 유지됩니다.

**예시**


```
iapp://app?id=6446581591&region=hk
iapp://rank?type=topFreeApplications&category=0&region=tw
```


---

## 인앱 검색 (URL 링크 없음)

이 작업 내부 iApp 하지만 **not** `iapp://` URL:

| Action | 이름 * |
|--------|-----|
| **Single App ID search** | 숫자 ID를 입력 (6–12자리, comma 없음) 검색 |
| **Batch App ID search** | 최대 50개의 상품 ID |
| **Add Subscription** | 긴 압박 어떤 app 줄 |
| **Save Developer** | Long-press → **개발자 ** submenu, 또는 세부 **More** 메뉴 |
| **Open by-ranking view** | Context menu → 동일한 개발자 앱 또는 개발자 즐겨 찾기 |
| **Pause / resume subscription** | 구독 행에 긴 압박 |
| **Reopen from browse history** | **설정 → 데이터 → App Browse History** → 입력 탭 |

use ** `iapp://` ** 링크 또는 **Siri / Shortcuts** 앱 외부에서 iApp을 열 필요가있을 때.

---

## 제품 정보

- Link codes work in any app language — UI 언어를 전환할 때 변경하지 않습니다.
- Widgets and**Live Activity**이 링크를 자동으로 생성합니다.
- 일부 Mac / iPad 유료 및 grossing 차트에 대한 Widget 차트 데이터는 주요 앱에서 약간 다를 수 있습니다.
- **Add favorite** via Shortcuts does not open the app UI — 즐겨찾기 목록에 직접 쓸 수 있습니다.
- **Content compare** mode in all-region info cannot export share images — 목록 또는 그리드보기로 전환합니다.

[경찰](..) · [FAQ](../faq) · [Privacy](../privacy)


