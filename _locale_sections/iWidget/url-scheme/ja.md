iWidget は **iPhone / iPad / Mac** で **`iwidget://`** を扱います。Safari、ショートカット、他アプリ、QR から開けます。音声だけの旧暦／祝日は Siri。出勤確認は Shortcuts の Workday Intent（URL ではありません）。

## 形式

`iwidget://<host>[?query]` — 未知の host は無視されます。

| Host | 開く | Query |
|------|------|-------|
| `today` | 今日 | — |
| `day` | 今日 → 日詳細 | `y` `m` `d` |
| `library` | ライブラリ | `preset=` / `set=`、`detail=1` |
| `mine` | マイウィジェット | `design=` / `id=`、`preset=` / `set=` |
| `editor` | エディタ | `design=` / `id=`（省略で最近） |
| `import` | 読み込み | — |
| `settings` | 設定 | `scroll=festivals` · `weather` · `editor` · `access` |
| `membership` | メンバーシップ | ロック中のウィジェットが開く |
| `launch` | 起動ブロックのハンドオフ（iOS） | ウィジェットが付与 |

例：`iwidget://today` · `iwidget://library?set=small.calendar&detail=1` · `iwidget://membership`

[サポートへ戻る](../) · [FAQ](../faq) · [メンバーシップ](../membership) · [プライバシー](../privacy)
