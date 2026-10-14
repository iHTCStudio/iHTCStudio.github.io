iGuanZhiは** `iguanzhi://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
iguanzhi://{host}?{params}
```


## パスポートと著者

| URL | 開く画面 |
|-----|-------|
| `iguanzhi://passage?id={id}` | 章句の詳細 |
| `iguanzhi://saying?id={id}` / `iguanzhi://couplet?id={id}` / `iguanzhi://poem?id={id}` | 通路と同じ(互換性) |
| `iguanzhi://passage?id={id}&card=1` | 通路の細部およびカード シート |
| `iguanzhi://card?id={id}` / `iguanzhi://share-card?id={id}` | 古カード |
| `iguanzhi://author?id={id}` | 作者の詳細 |
| `iguanzhi://recite` / `iguanzhi://recite?id={id}` | 誦読フロー |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `iguanzhi://home` | ホーム |
| `iguanzhi://daily` | 今日のエッセイ |
| `iguanzhi://random` | ランダムな章句 |
| `iguanzhi://favorites` | お気に入り |
| `iguanzhi://famous` | 名句一覧 |
| `iguanzhi://search` / `iguanzhi://search?q={query}` | 検索 |
| `iguanzhi://study` / `iguanzhi://study?id={id}` | 古典スタディ |
| `iguanzhi://hunt` | エッセイハント (`keyword-hunt`/`flyflower`) |
| `iguanzhi://handwriting` | 手書き検索 (`handwrite`; iOS) |
| `iguanzhi://mastered` | マスタード (`progress`) |
| `iguanzhi://categories` / `iguanzhi://categories?section=` | ブラウズ |
| `iguanzhi://collection?id=` | コレクション/書籍 |
| `iguanzhi://corpus` | すべての通路 (`all`) |
| `iguanzhi://last-read` | 最後に読んだ項目 |
| `iguanzhi://reading-history` | 閲覧履歴 |
| `iguanzhi://notes` | ノート |
| `iguanzhi://fables` / `iguanzhi://allegories` / `iguanzhi://concepts` | 利用できる場合の特別な棚 |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `iguanzhi://settings` | 設定 |
| `iguanzhi://usage-guide` | 使い方ガイド |
| `iguanzhi://widget-guide` | ウィジェットガイド |
| `iguanzhi://shortcuts-guide` | ショートカットガイド |
| `iguanzhi://feature-guide` | オンボーディングの再生 |
| `iguanzhi://feedback` | フィードバックメール |
| `iguanzhi://in-app-review` | アプリ内／App Store レビュー |

## 例


```
iguanzhi://daily
iguanzhi://passage?id=1
iguanzhi://study
iguanzhi://hunt
```



