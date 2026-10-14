iCoupletは** `icouplet://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
icouplet://{host}?{params}
```


## カップル&著者

| URL | 開く画面 |
|-----|-------|
| `icouplet://couplet?id={id}` | カップルディテール |
| `icouplet://poem?id={id}` | couplet と同じ (互換性エイリアス) |
| `icouplet://author?id={id}` | 著者(民家) |
| `icouplet://recite` | Recite の流れ(可能であれば自動ピーク) |
| `icouplet://recite?id={id}` | 開いた couplet および自動recite |

## 発見

| URL | 開く画面 |
|-----|-------|
| `icouplet://home` | ホームタブ |
| `icouplet://daily` | 今日の毎日のカップル |
| `icouplet://random` | ランダムカップル |
| `icouplet://favorites` | お気に入り |
| `icouplet://famous` | 有名なラインリスト |
| `icouplet://search` | 検索 |
| `icouplet://search?q={query}` | キーワード付き検索 |
| `icouplet://study` | 研究 / 子子エントリー |
| `icouplet://categories` | カテゴリーをブラウズ |
| `icouplet://categories?section=form` | フォーム(体裁)セクション |
| `icouplet://categories?section=theme` | テーマセクション |
| `icouplet://categories?section=author` | 著者セクション |
| `icouplet://categories?section=famous` | 有名なラインセクション |
| `icouplet://categories?section=corpus` | コレクション / コルパス |
| `icouplet://last-read` | 最終読み couplet |
| `icouplet://reading-history` | 閲覧履歴 |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `icouplet://settings` | 設定ルート |
| `icouplet://usage-guide` | 使い方ガイド |
| `icouplet://widget-guide` | ウィジェットガイド |
| `icouplet://shortcuts-guide` | ショートカットガイド |
| `icouplet://feature-guide` | 再生機能搭載 |
| `icouplet://feedback` | フィードバックメール |
| `icouplet://in-app-review` | アプリ内／App Store レビュー |

## 例


```
icouplet://daily
icouplet://couplet?id=1
icouplet://recite?id=1
icouplet://search?q=春
icouplet://categories?section=famous
icouplet://widget-guide
```


これらをショートカットアプリ、ホーム画面のクイックアクション、ウィジェット、またはSafariで使用してください。 アプリ内設定 → ショートカットガイド** も参照してください。


