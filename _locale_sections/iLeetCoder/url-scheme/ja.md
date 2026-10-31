iCoderは** `iLeetCoder://` **(大文字認識)ディープリンクをサポートしています。問題、毎日のクイズ、お気に入り、間違ったブック、またはSafari、ショートカット、ウィジェット、または別のアプリからタグ/会社によってフィルタリングします。

## プロトコル

| Host | Opens | クエリ |
|------|-------|-------|
| `problem` | Problem detail | `leetId=` または `id=` (`1`、`206` など) |
| `quiz` | Daily Quiz tab | — |
| `favorites` | Favourites list | — |
| `wrong`, `mistakes`, `wrongquestions` | Wrong book | `record=<UID>` → 連携問題 |
| `tag` | Problems filtered by tag | `name=` |
| `company` | Problems filtered by company | `name=` |

## 例


```
iLeetCoder://problem?leetId=1
iLeetCoder://problem?id=206
iLeetCoder://quiz
iLeetCoder://tag?name=Array
iLeetCoder://company?name=Google
iLeetCoder://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## ホーム スクリーンの速い行為

**4**で**設定 → ホーム画面ショートカット**:                                                                                                                                                                                                                                                                   検索/カテゴリ/フィードバック/レビューはクイックアクションチャンネルです。

[概要に戻る](...)・[FAQ](../faq)・[プライバシーポリシー](../privacy)


