iXinは** `ixin://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
ixin://{host}?{params}
```


## パスポートと著者

| URL | 開く画面 |
|-----|-------|
| `ixin://passage?id={id}` | 章句の詳細 |
| `ixin://saying?id={id}` / `ixin://couplet?id={id}` / `ixin://poem?id={id}` | 通路と同じ(互換性) |
| `ixin://passage?id={id}&card=1` | 通路の細部およびカード シート |
| `ixin://card?id={id}` / `ixin://share-card?id={id}` | インサイトカード |
| `ixin://author?id={id}` | 作者の詳細 |
| `ixin://recite` / `ixin://recite?id={id}` | 誦読フロー |

## ディスカバリー&プラクティス

| URL | 開く画面 |
|-----|-------|
| `ixin://home` | ホーム |
| `ixin://daily` | デイリーインサイト |
| `ixin://random` | ランダムな章句 |
| `ixin://favorites` | お気に入り |
| `ixin://famous` | 名句一覧 |
| `ixin://search` / `ixin://search?q={query}` | 検索 |
| `ixin://study` / `ixin://study?id={id}` | ハートスクール |
| `ixin://hunt` | ハートハント (`keyword-hunt`/`flyflower`) |
| `ixin://handwriting` | 手書き検索 (`handwrite`; iOS) |
| `ixin://mastered` | マスタード (`progress`) |
| `ixin://categories` / `ixin://categories?section=` | ブラウズ |
| `ixin://collection?id=` | 収蔵品/書籍(「チュアンシルー」/「ダクセン」/「ジオチオ」/「イヴン」/詩」) |
| `ixin://corpus` | すべての通路 (`all`) |
| `ixin://last-read` | 最後に読んだ項目 |
| `ixin://reading-history` | 閲覧履歴 |
| `ixin://notes` | ノート |
| `ixin://journal` | 知能ジャーナル |
| `ixin://liangzhi` | Liangzhiの3つの質問 |
| `ixin://graph` | コンセプトグラフ |
| `ixin://timeline` | アナルス/タイムライン |
| `ixin://map` | サイトマップ |
| `ixin://people` | スタッフ |
| `ixin://achievements` | 実績紹介 |
| `ixin://theme?id=` | テーマ: |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `ixin://settings` | 設定 |
| `ixin://usage-guide` | 使い方ガイド |
| `ixin://widget-guide` | ウィジェットガイド |
| `ixin://shortcuts-guide` | ショートカットガイド |
| `ixin://feature-guide` | オンボーディングの再生 |
| `ixin://feedback` | フィードバックメール |
| `ixin://in-app-review` | アプリ内／App Store レビュー |

## 例


```
ixin://daily
ixin://passage?id=1
ixin://journal
ixin://liangzhi
ixin://collection?id=chuanxilu
ixin://study
ixin://hunt
```


## ノート

- パラメータはIDが数値である場合感度です。
- シリ、ショートカット、ウィジェット、およびコントロールセンターコントロールは、同じディープリンクルートを使用します。
- 最新リストのアプリ内設定 → Help** ガイドを参照してください。


