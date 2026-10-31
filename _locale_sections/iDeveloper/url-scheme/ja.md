iDeveloperは** `ideveloper://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
ideveloper://{host}?{params}
```


## ツールとブラウズ

| URL | 開く画面 |
|-----|-------|
| `ideveloper://home` | ホーム |
| `ideveloper://tool?id={id}` | ツールの詳細(例:`json`、`base64`、`timestamp`) |
| `ideveloper://category?id={id}` | カテゴリー(例: `encoding`) |
| `ideveloper://search` / `ideveloper://search?q={query}` | 検索 |
| `ideveloper://favorites` | お気に入り |
| `ideveloper://history` | 運用履歴 |
| `ideveloper://reference` / `ideveloper://reference?id={id}` | 参照の中心/記入項目 |
| `ideveloper://new-snippet` | 新しいスニペット |
| `ideveloper://focus` | フォーカスタイマー/ライブアクティビティエントリ |
| `ideveloper://share?tool={id}` | ツールにハンドオフを開く(共有拡張機能+アプリグループペイロード機能) |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `ideveloper://settings` | 設定 |
| `ideveloper://usage-guide` | 使い方ガイド |
| `ideveloper://widget-guide` | ウィジェットガイド |
| `ideveloper://shortcuts-guide` | ショートカットガイド |
| `ideveloper://feature-guide` | オンボーディングの再生 |
| `ideveloper://feedback` | フィードバックメール |
| `ideveloper://in-app-review` | アプリ内／App Store レビュー |

## 例


```
ideveloper://tool?id=json
ideveloper://search?q=base64
ideveloper://reference?id=http-200
ideveloper://favorites
ideveloper://focus
ideveloper://share?tool=json
ideveloper://category?id=encoding
```


これらをショートカットアプリ、ホーム画面のクイックアクション、ウィジェット、コントロールセンター、またはSafariで使用してください。 アプリ内設定 → ショートカットガイド** も参照してください。


