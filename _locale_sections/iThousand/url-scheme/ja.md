iThousandは** `ithousand://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
ithousand://{host}?{params}
```


## パス、著者、キャラクター

| URL | 開く画面 |
|-----|-------|
| `ithousand://passage?id={id}` | 章句の詳細 |
| `ithousand://passage?id={id}&open=study` | パッセージ → プライマーホール |
| `ithousand://passage?id={id}&open=characters` | パッセージ→キャラクターテーブル |
| `ithousand://passage?id={id}&open=note` | パッセージ → ノート |
| `ithousand://author?id={id}` | 作者の詳細 |
| `ithousand://recite` / `ithousand://recite?id={id}` | 誦読フロー |
| `ithousand://characters` | キャラクターライブラリ |
| `ithousand://character?char=天` | キャラクターカードをフォーカス |
| `ithousand://characters?id={id}` | IDによるキャラクターカード |
| `ithousand://saved-characters` | 保存されたキャラクター |
| `ithousand://saved-famous` | 有名なラインを保存 |

## 発見

| URL | 開く画面 |
|-----|-------|
| `ithousand://home` | ホーム |
| `ithousand://daily` | 今日の毎日ライン |
| `ithousand://random` | ランダムな章句 |
| `ithousand://favorites` | お気に入り |
| `ithousand://list?id={uuid}` | 個人的なリスト (千人) |
| `ithousand://famous` | 名句一覧 |
| `ithousand://search` / `ithousand://search?q={query}` | 検索 |
| `ithousand://study` | プライマーホール |
| `ithousand://hunt` | Hunt(漢字)。aliases`keyword-hunt`/`flyflower` |
| `ithousand://mastered` | マスタード |
| `ithousand://categories` / `ithousand://categories?section=` | ブラウズ |
| `ithousand://collection?id=qianziwen` | プライマーコレクション(`name=` もサポート) |
| `ithousand://theme?id=dizigui-filial` | テーマ: |
| `ithousand://last-read` | 最後に読んだ項目 |
| `ithousand://reading-history` | 閲覧履歴 |
| `ithousand://notes` | ノート |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `ithousand://settings` | 設定 |
| `ithousand://privacy` | アプリ内プライバシー |
| `ithousand://usage-guide` | 使い方ガイド |
| `ithousand://widget-guide` | ウィジェットガイド |
| `ithousand://shortcuts-guide` | ショートカットガイド |
| `ithousand://feature-guide` | オンボーディングの再生 |
| `ithousand://feedback` | フィードバックメール |
| `ithousand://in-app-review` | アプリ内／App Store レビュー |

## 例


```
ithousand://daily
ithousand://passage?id=1
ithousand://passage?id=1&open=characters
ithousand://character?char=天
ithousand://collection?id=qianziwen
ithousand://study
ithousand://hunt
ithousand://saved-characters
```


これらをショートカットアプリ、ホーム画面のクイックアクション、ウィジェット、またはSafariで使用してください。 利用できる場合の優先順位の安定した `ithousand://` 変数。 アプリ内設定 → ショートカットガイド** も参照してください。


