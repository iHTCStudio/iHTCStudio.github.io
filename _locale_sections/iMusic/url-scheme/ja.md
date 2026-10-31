iMusicは** `imusic://` **のショートカットリンクをサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを通過するので、オンボーディング後にリンクが2回開くことはありません。

## リンク形式


```
imusic://{host}?{params}
```


スキームは** `imusic://` **のみです。

## ホーム&今日

| URL | 開く画面 |
|-----|-------|
| `imusic://` / `imusic://home` | ホーム |
| `imusic://daily` / `imusic://today` | デイリーピース(キューのみ) |
| `imusic://random` | ローム(全ライブラリシャッフル) |
| `imusic://play` | プレイ |
| `imusic://last` / `imusic://lastheard` | 最後に聞いて |

## ピース&アーティスト

| URL | 開く画面 |
|-----|-------|
| `imusic://piece?id={id}` | ピースガイド(「パッセージ」/「ソン」も可) |
| `imusic://artist?id={id}` / `imusic://artist?name={name}` | アーティストデスク |
| `imusic://artists` / `imusic://singers` | アーティストディレクトリ |
| `imusic://famous` / `imusic://lines` | 名句一覧 |

共有カードのフッターは、人のために `imusic://` (タイトル・アーティスト) を追加することができます。 マッチはまだ使用しています** `imusic` のみ**。

## ブラウズ、検索&リスニング

| URL | 開く画面 |
|-----|-------|
| `imusic://categories` / `imusic://browse` | 参照(`section=catalog`/`all`/`allpieces` → All Pieces) |
| `imusic://collection?id={id}` | コレクション (`id=col-all` は仮想オールピースリストです) |
| `imusic://search` / `imusic://search?q={query}` | 検索 |
| `imusic://favorites` | お気に入り |
| `imusic://later` | お気に入り、後でスクロール |
| `imusic://lists` / `imusic://listenlists` | リストを聴く |
| `imusic://history` | プロフィール |
| `imusic://notes` | ノート |
| `imusic://mastered` | 仕上げ |
| `imusic://streak` / `imusic://footprint` | ストール |

シングルピース、ミニバー、またはソング ID **resets** をその部分に読み込みます。 コレクション、検索、またはアーティストがそのリストを保持するので、次/前の滞在が利用可能になります。

## ソングID、学校&気分

| URL | 開く画面 |
|-----|-------|
| `imusic://recognize` / `imusic://shazam` | ソングID |
| `imusic://school` / `imusic://earschool` | イヤースクール |
| `imusic://timeline` / `imusic://corridor` | Eraの廊下 |
| `imusic://compare` | リスニングの比較 |
| `imusic://mood?id={id}` | 気分が始まります(`piece=`/`pieceId=` はスタートトラックのみです。気分は`id` と一致します) |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `imusic://settings` | 設定 |
| `imusic://usageguide` / `imusic://featureguide` | 使用法/特徴ガイド |
| `imusic://widgetguide` | ウィジェットガイド |
| `imusic://shortcutsguide` | ショートカットガイド |
| `imusic://feedback` | フィードバック |
| `imusic://review` / `imusic://in-app-review` | アプリ内レビュー(店舗リストがライブの場合) |

## シリとホーム画面

ショートカットを追加すると、今日のピース、ローム、検索、またはお気に入りを Siri に尋ねます。 **Settings → Shortcuts** でホーム画面のクイックアクションを設定します。 アプリ内ショートカットガイドにフルサンプルが搭載されています。

[FAQ](../faq)・[プライバシーポリシー](../privacy)・[サポート](./)


