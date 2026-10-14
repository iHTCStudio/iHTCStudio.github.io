iTer は、**iPhone と iPad** の**     ** URLスキームをサポートしています。 ショートカット、Safari、ウィジェット、またはその他のアプリで質問、毎日のクイズ、お気に入り、または間違ったanswerブックを開きます。

**ホーム画面クイックアクション**(アプリアイコンを長押し)は、同じ `iTer://` 文字列を再利用します。 **7**オプションから**4**まで選択します。

> **注記:** アプリ内のディープリンク**navigate** クイズの設定を変更したり、質問をリモートでマークしたりすることはありません。 **Mac**はホーム画面のクイックアクションを登録しません。 ウィジェットとアプリ内ナビゲーションはMac上で動作します。

## プロトコル


```
iTer://<host>[?query]
```


| Rule | 詳細を見る |
|------|--------|
| **Scheme** | `iTer` (ケースインセンティブ) |
| **Question detail** | ホスト `question` — クエリ`id=<questionID>`** または**`q=<questionID>`** (必須) |
| **Daily Quiz** | ホスト `quiz` |
| **Favourites** | ホスト `favorites` → 設定 → お気に入りリスト |
| **Wrong book** | ホスト `wrong`、 `mistakes`、または `wrongquestions` — オプション **`record=<UID>`** 1つの間違いを開く |
| **Search** | ホスト `search` — クイックアクション / ショートカットのみ (グローバル検索タブを開きます) |
| **Categories** | ホスト `categories` — クイックアクション / ショートカットのみ (カテゴリタブを開く) |
| **Feedback** | ホスト `feedback` — クイックアクションのみ (メールコンポースまたは `mailto:` フォールバック) |
| **Rate app** | ホスト `review` — クイックアクションのみ (StoreKit アプリ内レビュー)。 `star` を含むレガシータイプも機能します。 |

ホストが空の場合、 `iTer://` などのパスが受け入れられ、パスセグメントがマッチします。

## 例


```
iTer://question?id=94c34bb2bdef11e6a0e100163e0021c8
iTer://quiz
iTer://favorites
iTer://wrong
iTer://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## ホーム スクリーンの速い行為

| Type | 典型的な使用 |
|------|-------------|
| `iTer://search` | グローバル検索 |
| `iTer://quiz` | 毎日のクイズタブ |
| `iTer://favorites` | お気に入りリスト |
| `iTer://wrong` | 間違ったanswerブック |
| `iTer://categories` | カテゴリー タブ |
| `iTer://feedback` | フィードバックを送信 |
| `iTer://review` | アプリのレート(StoreKit) |

デフォルト選択: 検索、クイズ、お気に入り、フィードバック。 *Settings → Home Screen Shortcuts** (max 4) で注文または交換します。 app は、**contains** でショートカット `iTer://` 文字列にマッチします。そのため、これらのパスを含むレガシーなバリアントは正しくルートされます。

## ウィジェットディープリンク

| Widget | 典型的な URL |
|--------|-------------|
| Daily Question | `iTer://question?id=...` |
| Quiz Glance | ツイート |
| Favourites Glance | お気に入り |
| Wrong Book Glance | `iTer://wrong` または `iTer://wrong?record=<UUID>` |

---

[iTerサポートに戻る](../)・ [FAQ](../faq)・ [プライバシーポリシー](../privacy)


