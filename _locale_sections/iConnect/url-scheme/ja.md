iConnectは** `iconnect://` **をサポート URLスキームの深いリンク — タブ、設定ページ、またはSafari、別のアプリ、ブックマーク、またはAppleショートカットからアプリ内シートを開きます。 これらのURLは、iPhoneとiPadで**ホーム画面クイックアクション**として利用可能な目的地をミラーリングします(アプリアイコンを長押し)。

> **注記:** URL は iConnect** 内の **navigate** のみリンクします。 相手に接続したり、転送を開始したり、特定のチャットスレッドを開くことはありません。

## プロトコル仕様


```
iconnect://<host>
iconnect://<host>?refresh=1
```


| Rule | 詳細を見る |
|------|--------|
| **Scheme** | ツイート |
| **Host / path** | 単一のセグメント、**case-inpathy** — URL**host**またはfirst **path**セグメントから解決 |
| **Aliases** | 複数のホストは同義語を受け入れます(下の表を参照して下さい) |
| **Query** | "refresh=1`/`refresh=true` のみ**Devices** はディスカバリーリフレッシュをトリガーします |

同等形態の例:


```
iconnect://devices
iconnect://open/devices
```


---

## タブの宛先

| URL | 開く画面 |
|-----|--------|---------|
| `iconnect://devices` | **Devices** tab (radar / discovery) | デバイス |
| `iconnect://devices?refresh=1` | **Devices** tab and **refreshes** nearby discovery | — |
| `iconnect://chat` | **Chats** tab | 「メッセージ」 |
| `iconnect://transfers` | **Transfers** tab | トランスファー |
| `iconnect://history` | **History** tab (transfer log) | — |
| `iconnect://settings` | **Settings** tab | ログイン |

**参考文献**


```
iconnect://devices?refresh=1
iconnect://devices/refresh
```


---

## 設定サブページ

これらのリンクは、**Settings**に切り替え、一致するページを開きます。

| URL | 開く画面 |
|-----|--------|---------|
| `iconnect://about` | About | — |
| `iconnect://usage` | Usage Guide | `guide`、`help`、`usageguide` |
| `iconnect://shortcuts` | Home Screen shortcuts picker (iOS) | 「ホームショートカット」 |
| `iconnect://debug` | Debug / diagnostics info | `debuginfo` |

---

## アプリ内アクション

| URL | 開く画面 |
|-----|--------|
| `iconnect://share` | iConnectシート共有(App Storeリンク+推奨テキスト) |
| `iconnect://feedback` | フィードバックメールコンポーズ(メールが利用できなくなった場合は、`mailto:` に戻ってフォール) |
| `iconnect://review` | アプリ内アプリ 店の評価のプロンプト |

**レビューエイリアス:** `iconnect://` 、 `iconnect` ---

## 例

**チャットタブを開く**


```
iconnect://chat
```


**転送タブを開く**


```
iconnect://transfers
```


**リフレッシュ装置発見**


```
iconnect://devices?refresh=1
```


**オープン利用ガイド**


```
iconnect://usage
```


**アプリを共有する**


```
iconnect://share
```


---

## ホーム スクリーンクイックアクション (iOS)

iConnectアイコンを長押しします。 **設定 → ホーム画面のショートカット** (再注文するドラッグ)で最大** 4**ショートカットをカスタマイズします。

| Quick Action | サイトマップ |
|--------------|-----|
| Devices | `iconnect://devices` |
| Chats | チャット |
| Transfers | `iconnect://transfer` |
| History | 「iconnect://history」とは |
| Share | 「iconnect://share」 |
| Feedback | `iconnect://feedback` |
| Rate | 「iconnect://review」の |
| About | [iconnect://about`] |

デフォルトで有効:**Devices**、**Chats**、**Share**、**Feedback**。

クイックアクション型は、同じ `iconnect://` 文字列を使用し、外部 URL と同じパーサでルーティングされます。

---

## Appleのショートカット

**転送タブを開く**

1. アクションを追加**URLを開く**
2. URL: `iconnect://` **Wi-Fiに加入した後、近くのデバイスをリフレッシュ**


```
iconnect://devices?refresh=1
```


パーソナルオートメーション(Wi-Fi接続時など)で[URL**を開く]を使用して、発見と再スキャンにジャンプします。

---

## 起動動作

iConnect が URL を受信したときに (cold start または while run)

1. リンクは `iconnect://` で区切られます。
2. タブはすぐにアニメーションを切り替えます。**share**、**feedback**、および**review**は短い遅延(iOSの~0.4 s)後に開くので、UIは取り付けを完了することができます。
3。**Feedback**は、利用可能なときにアプリ内メールを使用します。 それ以外の場合は、 `iconnect://` でデフォルトのメールクライアントを開きます。
4。 Mac上で**共有**は、システム共有ピッカーを使用しています。 iOSでは共有シートが表示されます。

---

## トラブルシューティング

| Issue | 確認する |
|-------|----------------|
| Link does nothing | iConnectがインストールされていることを確認してください。ホストは上記のサポート名に一致しなければなりません |
| `feedback` opens Mail only | デバイスで設定されたメールアカウントがない — 期待されるフォールバック |
| `shortcuts` has no effect on Mac | ホーム スクリーンのショートカットのカスタマイズは**iOS専用** |
| URL does not connect to a device | ディープリンクのみのナビゲーション — デバイスタブを使用して、手動でピアを発見 |

---

[iConnectサポートに戻る](..)・ [FAQ](../faq)・ [プライバシーポリシー](../privacy)


