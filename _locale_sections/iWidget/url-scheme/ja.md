iWidgetは、**iPhone、iPad、Mac**で**     ** URLスキームをサポートしています。 *Safari**、**Apple Shortcuts**、別のアプリ、またはQRコードでメインアプリにジャンプします。 これらのリンク **のみナビゲート** — 彼らはウィジェットの設計IDやボードのレイアウトを編集することはできません。

音声の月/祝祭の回答は、**アプリを開くことなく、**Siri App Shortcuts**([FAQ](./faq)→Siriを参照してください)を使用します。 **仕事/休息日**の場合、別々の**Workday** App Intent in Shortcutsを追加します。

## フォーマット


```
iwidget://<host>[?query]
```


| Rule | 詳細を見る |
|------|--------|
| **Scheme** | `iwidget` (大文字) |
| **Host** | パスセグメント — 下の表を参照 |
| **Query** | オプション; 文書化されたキーのみ読み取り |

不明なホストは安全に無視されます(クラッシュなし)。

---

## ホスト

| Host | Opens | クエリ |
|------|--------|-------|
| `today` | **Today** tab | — |
| `day` | **Today** tab and queues **day detail** for the given date | **`y`** 年・**`m`` 月・**`d`** 日(整数) |
| `settings` | **Settings** tab | **`scroll=festivals`** はフェスティバルフィルターセクションにスクロールします | `iwidget://` ---

## 例

今日を開く**


```
iwidget://today
```


**オープン 1 1月 2026 詳細**


```
iwidget://day?y=2026&m=1&d=1
```


**設定を開く → フェスティバルフィルタ**


```
iwidget://settings?scroll=festivals
```


---

## ウィジェットとコントロールセンターの動作

- **intercept Taps** がオフの場合、**home-screen board** をタップすると、`iwidget://today` (またはウィジェットのインテントを介して設定されたオープン動作) が開きます。
- **Lock Screen** と **Control Center** エントリは App Intents を使用します。それらは追加の URL ホストではありません。
- **Macメニューバー** カレンダーは、日付をクリックすると同じ`day` URL パターンを使用します。

---

## ショートカットのヒント

1. URL を開き、 `iwidget://` を貼り付けます。
2。**Workday**チェックのために、iWidget's **work/rest Day**のショートカットアクションライブラリを検索し、日付を供給します。** URLクエリとして利用できません。

[iWidgetサポートに戻る](./)・ [FAQ](../faq)・ [プライバシーポリシー](../privacy)


