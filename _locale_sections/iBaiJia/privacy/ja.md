**最終更新日:** 2026年8月18日

iHTC Studio（「当社」）は **iBaiJia**（「爱百家姓」／「爱百家姓」、Bundle ID `com.iHTCboy.iBaiJia`）を開発しました。本プライバシーポリシーは、本アプリの利用時にどのデータが取り扱われ、取り扱われないかを説明します。**Apple App Review** とユーザーは、**本ページ**を公開のプライバシーポリシーとして参照できます。App Store Connect では、ブラウザで本プライバシーポリシーを開き、アドレスバーから URL をコピーしてください（公開サイトのドメインは将来変更される場合があります）。

## 概要（Apple プライバシー栄養表示との整合性）

| トピック | 当社の方針 |
|-------|----------------|
| アカウント | **不要** — 登録、メールサインイン、電話番号は必要ありません |
| iHTC Studioによるデータ収集 | **データは収集しません** — 個人データを受け取るバックエンドは運営していません |
| ネットワーク | Surname library, detail reading, recite, Study Hall, naming inspiration, widgets, and daily notifications work **offline** after install |
| 分析 / 広告 / トラッキング | **なし** — サードパーティの分析、広告、トラッキングSDKは使用しておらず、App Tracking Transparencyも使用していません |
| 任意の Apple サービス | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for 任意チップ, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default), optional **system speech / translation** |

## データの収集

当社は、広告や分析のために個人情報を収集、販売、共有することは**ありません**。

- **アカウント不要** — アカウントを作成せずに、すべての基本機能を使用できます。
- **分析や広告なし** — アプリのバイナリには、サードパーティの分析、広告、クラッシュレポートSDKは統合されておらず、データが当社に送信されることはありません。
- **コンテンツのアップロードなし** — お客様のfavorites, surname lists, notes, reading history, study progress, streaks, naming preferences, and settings stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## アプリの仕組み

- **同梱ライブラリ** — テキスト JSON、白話／英語、索引、学習補助はアプリ／ウィジェット バンドル内に同梱されます。閲覧と学習にネットワークは不要です。
- **端末内音声** — 閲読と朗誦は Apple **AVSpeechSynthesizer**（TTS）。姓氏テキストは iHTC Studio へ送りません。
- **任意のシステム翻訳** — 詳細文を長押しして Apple の Translation（iOS 17.4 / macOS 14.4+）を使う場合、処理は Apple OS 内です。翻訳バックエンドは運営しません。
- **命名インスピレーション** — 同梱データから端末上で完全生成。名前や設定はアップロードされません。
- **ウィジェットと App Group** — ウィジェットとアプリは、端末上の App Group `group.com.iHTCboy.iBaiJia` を通じて設定と軽量な状態を共有します。
- **毎日の通知** — User Notifications でローカルスケジュール。タップで端末のディープリンクを開きます。サーバー配信はありません。
- **カードを共有** — 画像はデバイス上でレンダリングされます。 保存すると、[保存] をタップした場合にのみ **フォト ライブラリの追加のみ**が使用されます。 システム共有シートは、**あなた**が選択したアプリに画像を送信できます。 その場合、その宛先のプライバシー ポリシーが適用されます。
- **任意チップ** — 「Tip Developer」（`com.iHTCboy.iBaiJia.6`）は Apple 処理の消耗型 **StoreKit** 購入です。カード情報は受け取りません。
- **Siri / ショートカット / コントロール センター** — オプションのシステム統合により、デバイス上のディープ リンクが開きます。 彼らはあなたのライブラリを私たちに送ることはありません。
- **任意 Spotlight** — 既定オフ。姓氏は端末上でシステムが索引。検索バックエンドは運営しません。
- **フィードバックメール** — 送信内容に、お客様の文面とトラブルシュート用の端末/アプリ診断（バージョン、OS、言語）が含まれる場合があります。

## 端末に保存されるデータ

 | データ | どこ | 目的 |
 |------|-------|-----------|
| 姓氏 DB と筆順 | App バンドル | オフライン閲読・なぞり書き・学習 |
| お気に入りと姓氏リスト | App Group UserDefaults | 星付き姓氏とリスト |
| メモ | App Group UserDefaults | 姓氏についてのメモ |
| わたしの姓 | App Group UserDefaults | ホームとウィジェットのパーソナライズ |
| 閲読履歴 / 最後に読んだ位置 | App Group UserDefaults | 閲覧続行・履歴 UI |
| 学習進捗とハイスコア | App Group UserDefaults | Study Hall 状態 |
| チェックイン連続 | App Group UserDefaults | 毎日の習慣 |
 | 外観と読み取り設定 | アプリグループのUserDefaults | テーマ、アクセント、言語、レイアウト、TTS、タブ、ウィジェット |
| Daily Surname cache & notification prefs | App Group UserDefaults | 今日の ID, 時刻 |
| 共有カード設定 | App Group UserDefaults | Last style choices |
 | オンボーディングと TipKit の状態 | 標準 UserDefaults (デバイス) | ウェルカムガイド / 発見のヒント |
 | ホーム画面のクイックアクション | システム + ローカル設定 | 設定するショートカット |
 | ウィジェット / ライブ アクティビティのスナップショット | アプリグループ / ActivityKit | すでに開いているテキストを表示 |

アプリをアンインストールすると、アプリに関連するサンドボックスおよびApp Groupデータが削除されます（iOS/macOSの動作に依存します）。任意のiCloudコピーは、あなたが削除するか、同期をオフにして他の場所で削除するまで、**あなたの**iCloudに残ります。

## iCloud同期（オプション）

設定で**iCloud同期**を有効にすると、アプリは選択したユーザーデータをAppleの**`NSUbiquitousKeyValueStore`**を通じてあなたのApple IDに関連付けて同期します：

- お気に入り
- 姓氏リスト
 - 注意事項
- 読書履歴
- 学習進捗 / ハイスコア
- チェックイン連続
- 関連設定

同期トラフィックは**Apple iCloud**にのみ送信され、iHTC Studioには送信されません。設定で同期を無効にできます。私たちはあなたのiCloudの内容を読むことはできません。

## 権限

 iLiezi は、機能が必要な場合にのみアクセス許可を要求します。

| 権限 | タイミング | 理由 |
|------------|------|-----|
| 通知 | Daily Surname reminders を有効にする | ローカルスケジュール |
## iCloud 同期（任意）
| iCloud | 同期を有効にする | お気に入り/リスト/履歴/進捗/連続/メモを同期 |
設定で **iCloud 同期**を有効にすると、アプリは **お客様の Apple ID** に紐づく Apple の **`NSUbiquitousKeyValueStore`** を通じて、選択したユーザーデータをミラーリングします。
| バックグラウンド音声 (iOS) | バックグラウンド朗誦を有効にする | バックグラウンドで TTS 継続 |

 当社は、連絡先、正確な位置情報、カメラ、マイク (システムの TTS 再生を超える)、または追跡を要求しません**。

## 子供のプライバシー

iBaiJia は一般向けの文化学習アプリであり、**Kids Category には属しません**。当社は児童から故意に個人情報を収集しません。アカウントは不要です。家族は各自の端末で、オフラインの読書・学習機能をご利用いただけます。

## 第三者

通常利用の第三者は **Apple** のみ。姓氏データセットには CC BY 4.0 英語 gloss と LGPL/Arphic 筆順字形が含まれます（アプリ内 About で帰属表示）。文化解説は参考用の独自学習素材です。

## データ保持と削除

- **端末上:** 進捗・履歴・メモを消せます。設定でエクスポート/インポート可能。アプリ削除で sandbox / App Group 削除。
- **iCloud:** 設定で同期をオフにできます。システム設定で iCloud ストレージも管理できます。
- **当社は保持しません** — 閲読・メモ・お気に入りのコピーをサーバーに保持しません。

## このポリシーの変更

法令、製品、または App Store コンプライアンスの理由で本ページを更新することがあります。上部の「最終更新日」が変更されます。更新後も利用を続ける場合、改訂版に同意したものとみなされます。

## お問い合わせ

プライバシーに関するご質問: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
