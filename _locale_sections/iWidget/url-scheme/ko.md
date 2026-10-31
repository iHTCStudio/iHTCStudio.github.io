iWidget는 **iPhone / iPad / Mac**에서 **`iwidget://`**를 지원합니다. Safari, 단축어, 다른 앱, QR로 열 수 있습니다. 음성만으로 음력/명절을 물을 때는 Siri. 근무일 확인은 Shortcuts의 Workday Intent입니다.

`iwidget://<host>[?query]` — 알 수 없는 host는 무시됩니다.

| Host | 열기 | Query |
|------|------|-------|
| `today` | 오늘 | — |
| `day` | 오늘 → 일 상세 | `y` `m` `d` |
| `library` | 라이브러리 | `preset=` / `set=`, `detail=1` |
| `mine` | 내 위젯 | `design=` / `id=`, `preset=` / `set=` |
| `editor` | 편집기 | `design=` / `id=` (없으면 최근) |
| `import` | 가져오기 | — |
| `settings` | 설정 | `scroll=festivals` · `weather` · `editor` · `access` |
| `membership` | 멤버십 | 일시 정지된 위젯이 엽니다 |
| `launch` | 실행 블록 핸드오프 (iOS) | 위젯이 제공 |

예: `iwidget://today` · `iwidget://library?set=small.calendar&detail=1` · `iwidget://membership`

[지원으로](../) · [FAQ](../faq) · [멤버십](../membership) · [개인정보](../privacy)
