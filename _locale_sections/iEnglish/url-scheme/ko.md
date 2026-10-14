iEnglish 지원 ** `ienglish://` ** URL 계획 깊은 링크 — 단어를 열고, Daily Quiz, Favourites, Wrong Book, playlist 또는 카테고리에서 사파리, Shortcuts, 위젯, 또는 다른 응용 프로그램.

**홈 화면 빠른 행동** (앱 아이콘을 길게 누르십시오) 검색, 피드백 및 비율을 추가합니다. 그 유형은 ** `ienglish://` 에 의해 파싱하지만 여전히 단축키 관찰자를 통해 앱을 엽니 다.

> **주의:** 앱 내에서만 링크 **navigate**. 그들은 pronunciation를 시작하거나 원격으로 공부 설정을 변경하지 않습니다.

## 프로젝트


```
ienglish://<host>[?query]
```


| Rule | 제품 정보 |
|------|--------|
| **Scheme** | `ienglish`(케이인성) |
| **Word detail** | 호스트 `word` - 쿼리 **`id=<wordID>`** (필수, 비 빈) |
| **Quiz** | 호스트 `quiz` |
| **Favourites** | 호스트 `favorites` |
| **Wrong book** | 호스트 `wrong` 또는 `mistakes` - 옵션 `record=<UUID>`는 하나의 실수를 엽니다. |
| **Playlist** | 호스트 `playlist` |
| **Categories** | 호스트 `categories` |

## 예시


```
ienglish://word?id=apple
ienglish://quiz
ienglish://favorites
ienglish://wrong
ienglish://wrong?record=550E8400-E29B-41D4-A716-446655440000
ienglish://playlist
ienglish://categories
```


## 홈 화면 빠른 행동

**4** in**Settings → 홈 화면 단축키**를 구성합니다. 유형은 포함 `ienglish://` , `IEnglishDeepLink` , `ienglish` , `word` , `id=<wordID>` , `quiz` , `favorites` - 검색 / 피드백 / 리뷰는 빠른 행동으로 전달됩니다.

## Widget 깊은 링크

위젯 탭은 같은 사용 `ienglish://` 호스트 (예 : Daily Quiz → `IEnglishDeepLink` , Favourites 눈 → `ienglish` ).

[경찰](..) · [FAQ](../faq) · [Privacy](../privacy)


