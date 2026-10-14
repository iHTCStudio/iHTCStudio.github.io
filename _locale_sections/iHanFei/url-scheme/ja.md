iHanFeiは、** `ihanfei://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
ihanfei://{host}?{params}
```


## パスポートと著者

| URL | 開く画面 |
|-----|-------|
| `ihanfei://passage?id={id}` | 章句の詳細 |
| `ihanfei://saying?id={id}` / `ihanfei://couplet?id={id}` / `ihanfei://poem?id={id}` | 通路と同じ(互換性) |
| `ihanfei://passage?id={id}&card=1` | 通路の細部およびカード シート |
| `ihanfei://card?id={id}` / `ihanfei://share-card?id={id}` | 法カード |
| `ihanfei://author?id={id}` | 作者の詳細 |
| `ihanfei://recite` / `ihanfei://recite?id={id}` | 誦読フロー |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `ihanfei://home` | ホーム |
| `ihanfei://daily` | デイリー・ストラテジーム |
| `ihanfei://random` | ランダムな章句 |
| `ihanfei://favorites` | お気に入り |
| `ihanfei://famous` | 名句一覧 |
| `ihanfei://search` / `ihanfei://search?q={query}` | 検索 |
| `ihanfei://study` / `ihanfei://study?id={id}` | 法律学研究 |
| `ihanfei://hunt` | 法ハント (`keyword-hunt`/`flyflower`) |
| `ihanfei://handwriting` | 手書き検索 (`handwrite`; iOS) |
| `ihanfei://mastered` | マスタード (`progress`) |
| `ihanfei://categories` / `ihanfei://categories?section=` | ブラウズ |
| `ihanfei://collection?id=` | コレクション/書籍 |
| `ihanfei://corpus` | すべての通路 (`all`) |
| `ihanfei://last-read` | 最後に読んだ項目 |
| `ihanfei://reading-history` | 閲覧履歴 |
| `ihanfei://notes` | ノート |
| `ihanfei://fables` / `ihanfei://allegories` / `ihanfei://concepts` | 利用できる場合の特別な棚 |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `ihanfei://settings` | 設定 |
| `ihanfei://usage-guide` | 使い方ガイド |
| `ihanfei://widget-guide` | ウィジェットガイド |
| `ihanfei://shortcuts-guide` | ショートカットガイド |
| `ihanfei://feature-guide` | オンボーディングの再生 |
| `ihanfei://feedback` | フィードバックメール |
| `ihanfei://in-app-review` | アプリ内／App Store レビュー |

## 例


```
ihanfei://daily
ihanfei://passage?id=1
ihanfei://study
ihanfei://hunt
```



