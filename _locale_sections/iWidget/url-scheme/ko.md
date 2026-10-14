iWidget은 ** `iwidget://` ** URL 계획 **iPhone, iPad 및 Mac**을 지원합니다. **Safari**, **Apple Shortcuts**, 또 다른 앱, 또는 QR 코드를 사용하여 메인 앱으로 이동합니다. 이 링크 **navigate 만 ** - 그들은 위젯 디자인 ID를 통과하지 않거나 보드 레이아웃을 편집합니다.

lunar / festival Answer **** 앱 열기, **Siri App Shortcuts** ([FAQ](../faq) → Siri). **일에서 작업/걸기 **, 별도의 **일** App Intent in Shortcuts를 추가합니다.

## 지원하다


```
iwidget://<host>[?query]
```


| Rule | 제품 정보 |
|------|--------|
| **Scheme** | `iwidget`(저장) |
| **Host** | Path 세그먼트 - 아래 표 참조 |
| **Query** | 선택 사항; 만 문서 키는 읽기 |

알 수없는 호스트는 안전하게 무시됩니다 (무한 충돌 없음).

---

## 이름 *

| Host | Opens | 글쓰기 |
|------|--------|-------|
| `today` | **Today** tab | — |
| `day` | **Today** tab and queues **day detail** for the given date | **`y`** year · **`m'** month · **`d`** day (integers) |
| `settings` | **Settings** tab | **`scroll=festivals`** 축제 필터 섹션에 스크롤 | `iwidget://` 쿼리 값이 누락되거나 잘못된 경우, 하루 시트를 열지 않고 오늘에 앱이 여전히 전환됩니다.

---

## 예시

**영업일**


```
iwidget://today
```


**1월 2026일 오픈 **


```
iwidget://day?y=2026&m=1&d=1
```


**설정 → 축제 필터 열기 **


```
iwidget://settings?scroll=festivals
```


---

## Widget 및 제어 센터 행동

- **home-screen board** when**intercept tap**는 `iwidget://today`(또는 위젯 intent를 통해 설정된 오픈 동작)를 열 수 있습니다.
- **Lock Screen** 및 **Control Center** 항목 사용 App Intents; 그들은 추가 URL 호스트가 아닙니다.
- **Mac 메뉴 바 ** 캘린더는 날짜를 클릭 할 때 같은 `일` URL 패턴을 사용합니다.

---

## 단축키 팁

1. 추가 ** URL** 및 붙여넣기 `iwidget://` 링크.
2. ** Workday** 체크를 위해, iWidget의 **work/rest day**를 위한 Shortcuts 액션 라이브러리를 검색하고 날짜를 공급합니다. ** URL 쿼리로 사용할 수 없습니다.

[Back to iWidget Support](../) · [FAQ](../faq) · [개인정보 보호정책](../privacy)


