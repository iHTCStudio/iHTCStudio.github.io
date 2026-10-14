iPrimerは** `iprimer://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
iprimer://{host}?{params}
```


## 章と著者

| URL | 開く画面 |
|-----|-------|
| `iprimer://chapter?id={id}` | 章の詳細 |
| `iprimer://passage?id={id}` / `iprimer://poem?id={id}` | チャプターと同じ(互換性) |
| `iprimer://author?id={id}` | 作者の詳細 |
| `iprimer://recite` / `iprimer://recite?id={id}` | 誦読フロー |

## 発見

| URL | 開く画面 |
|-----|-------|
| `iprimer://home` | ホーム |
| `iprimer://daily` | 今日の毎日の勉強 |
| `iprimer://random` | ランダムチャプター |
| `iprimer://favorites` | お気に入り |
| `iprimer://famous` | 名句一覧 |
| `iprimer://search` / `iprimer://search?q={query}` | 検索 |
| `iprimer://study` | キャラクタースタディ |
| `iprimer://meditation` | 瞑想コース一覧 |
| `iprimer://meditation?slug={slug}&autostart=1` | セッションとオートスタート(フォアグラウンド) |
| `iprimer://guidance` | ライフガイダンス(ジャーナル&習慣) |
| `iprimer://hunt` | Hunt(笑)。aliases`keyword-hunt`/`flyflower` |
| `iprimer://mastered` | マスターされた章 |
| `iprimer://categories` / `iprimer://categories?section=` | ブラウズ |
| `iprimer://collection?id=xiaoxue` | Xiaoxueコレクション (`name=` もサポート) |
| `iprimer://theme?id=lijiao` | ボリューム/テーマ(`name=立教` または `Relationships` もサポート) |
| `iprimer://last-read` | 最後に読んだ項目 |
| `iprimer://reading-history` | 閲覧履歴 |
| `iprimer://notes` | ノート |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `iprimer://settings` | 設定 |
| `iprimer://usage-guide` | 使い方ガイド |
| `iprimer://widget-guide` | ウィジェットガイド |
| `iprimer://shortcuts-guide` | ショートカットガイド |
| `iprimer://feature-guide` | オンボーディングの再生 |
| `iprimer://feedback` | フィードバックメール |
| `iprimer://in-app-review` | アプリ内／App Store レビュー |

## 例


```
iprimer://daily
iprimer://chapter?id=3
iprimer://collection?id=xiaoxue
iprimer://theme?id=lijiao
iprimer://study
iprimer://meditation?slug=emotion_calm&autostart=1
iprimer://guidance
iprimer://hunt
```


これらをショートカットアプリ、ホーム画面のクイックアクション、ウィジェット、またはSafariで使用してください。 利用できる場合の優先順位の安定した `iprimer://` 変数。 アプリ内設定 → ショートカットガイド** も参照してください。


