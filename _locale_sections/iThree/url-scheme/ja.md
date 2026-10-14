iThreeは** `ithree://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
ithree://{host}?{params}
```


## パッセージと発見

| URL | 開く画面 |
|-----|-------|
| `ithree://home` | ホーム |
| `ithree://daily` | 今日の毎日ライン |
| `ithree://random` | ランダムな章句 |
| `ithree://passage?id={id}` | 章句の詳細 |
| `ithree://recite` / `ithree://recite?id={id}` | 誦読フロー |
| `ithree://favorites` | お気に入り |
| `ithree://famous` | 名句一覧 |
| `ithree://search` / `ithree://search?q={query}` | 検索 |
| `ithree://study` | 学習教室 |
| `ithree://quiz` | 今日のクイズ |
| `ithree://hunt` | 寻 (句) |
| `ithree://mastered` | マスタード |
| `ithree://categories` | ブラウズ |
| `ithree://chapter?id={id}` | トピックス |
| `ithree://stories` / `ithree://story?id={id}` | ストーリー/ストーリー詳細 |
| `ithree://books` / `ithree://book?id={id}` | クラシックインデックス/書籍 |
| `ithree://dynasties` / `ithree://dynasty?id={id}` | ダイナスティ / ダイナスティ |
| `ithree://collection?id=` / `?name=` | コレクション(または空の書籍) |
| `ithree://last-read` | 最後に読んだ項目 |
| `ithree://reading-history` | 閲覧履歴 |
| `ithree://notes` | ノート |

> Note: `ithree://` は互換性のあるエイリアスで、マッチング **chapter** を開きます。

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `ithree://settings` | 設定 |
| `ithree://usage-guide` | 使い方ガイド |
| `ithree://widget-guide` | ウィジェットガイド |
| `ithree://shortcuts-guide` | ショートカットガイド |
| `ithree://feature-guide` | オンボーディングの再生 |
| `ithree://feedback` | フィードバックメール |
| `ithree://in-app-review` | アプリ内／App Store レビュー |
| `ithree://privacy` | アプリ内プライバシー |

## 例


```
ithree://daily
ithree://passage?id=1
ithree://recite?id=1
ithree://study
ithree://hunt
ithree://quiz
ithree://stories
ithree://search?q=人之初
```


これらをショートカットアプリ、ホーム画面のクイックアクション、ウィジェット、コントロールセンター、またはSafariで使用してください。 アプリ内設定 → ショートカットガイド** も参照してください。


