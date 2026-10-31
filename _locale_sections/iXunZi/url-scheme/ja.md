iXunZiは** `ixunzi://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
ixunzi://{host}?{params}
```


## パスポートと著者

| URL | 開く画面 |
|-----|-------|
| `ixunzi://passage?id={id}` | 章句の詳細 |
| `ixunzi://saying?id={id}` / `ixunzi://couplet?id={id}` / `ixunzi://poem?id={id}` | 通路と同じ(互換性) |
| `ixunzi://passage?id={id}&card=1` | 通路の細部およびカード シート |
| `ixunzi://card?id={id}` / `ixunzi://share-card?id={id}` | カード |
| `ixunzi://author?id={id}` | 作者の詳細 |
| `ixunzi://recite` / `ixunzi://recite?id={id}` | 誦読フロー |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `ixunzi://home` | ホーム |
| `ixunzi://daily` | デイリー・クーン |
| `ixunzi://random` | ランダムな章句 |
| `ixunzi://favorites` | お気に入り |
| `ixunzi://famous` | 名句一覧 |
| `ixunzi://search` / `ixunzi://search?q={query}` | 検索 |
| `ixunzi://study` / `ixunzi://study?id={id}` | 学習アカデミーの奨励 |
| `ixunzi://hunt` | Xun ハント (`keyword-hunt`/`flyflower`) |
| `ixunzi://handwriting` | 手書き検索 (`handwrite`; iOS) |
| `ixunzi://mastered` | マスタード (`progress`) |
| `ixunzi://categories` / `ixunzi://categories?section=` | ブラウズ |
| `ixunzi://collection?id=` | コレクション/書籍 |
| `ixunzi://corpus` | すべての通路 (`all`) |
| `ixunzi://last-read` | 最後に読んだ項目 |
| `ixunzi://reading-history` | 閲覧履歴 |
| `ixunzi://notes` | ノート |
| `ixunzi://ask` | Xunziを尋ねる |
| `ixunzi://fables` / `ixunzi://allegories` / `ixunzi://concepts` | 利用できる場合の特別な棚 |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `ixunzi://settings` | 設定 |
| `ixunzi://usage-guide` | 使い方ガイド |
| `ixunzi://widget-guide` | ウィジェットガイド |
| `ixunzi://shortcuts-guide` | ショートカットガイド |
| `ixunzi://feature-guide` | オンボーディングの再生 |
| `ixunzi://feedback` | フィードバックメール |
| `ixunzi://in-app-review` | アプリ内／App Store レビュー |

## 例


```
ixunzi://daily
ixunzi://passage?id=1
ixunzi://ask
ixunzi://study
ixunzi://hunt
```



