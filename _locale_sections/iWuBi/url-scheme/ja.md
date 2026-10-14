iWuBiは、** `iWuBi://` **(ケース・インセンティブ・スキーム `iwubi` )ディープ・リンクをサポートしています。オープン・ルックアップ、デイリー・クイズ、お気に入り、間違ったブック、コード・長さ・レベル、Safari、ショートカット、ウィジェット、またはその他のアプリからハブまたはタイピング・プラクティスを学びます。

## プロトコル


```
iWuBi://<host>[?query]
iWuBi:///path-style   ← host empty; first path segment is the action
```


| Host / action | Opens | クエリ |
|---------------|-------|-------|
| `search` | Lookup tab, focus search | `q`, `word`, または `name` プリフィル |
| `word`, `char`, `character` | Word detail (or search if query empty) | `q` / `word` / `name` = 文字 |
| `quiz`, `test` | Learn → Daily Quiz | — |
| `favorites`, `favorite` | Settings → Favourites | — |
| `wrong`, `mistakes`, `wrongbook` | Wrong book | `record=<UID>` → 1レコード |
| `levels`, `level`, `codes` | Levels tab | — |
| `learn`, `study` | Learn tab | — |
| `typing`, `type`, `practice` | Typing tab | — |

## 例


```
iWuBi://search?q=你好
iWuBi://word?q=好
iWuBi://quiz
iWuBi://wrong?record=550E8400-E29B-41D4-A716-446655440000
iWuBi://levels
iWuBi://typing
```


## ホーム スクリーンの速い行為

**4**で**設定 → ホーム画面ショートカット**: `iWuBi://` , `iwubi` , `search` , `q` , `word` , `name` , `word` ,

[概要に戻る](...)・[FAQ](../faq)・[プライバシーポリシー](../privacy)


