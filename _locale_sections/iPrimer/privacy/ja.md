**最終更新日:** 2026年8月18日

iHTC Studio（「当社」）は **iPrimer**（「爱小学」／「爱小学」、Bundle ID `com.iHTCboy.iPrimer`）を開発しました。本プライバシーポリシーは、本アプリの利用時にどのデータが取り扱われ、取り扱われないかを説明します。**Apple App Review** とユーザーは、**本ページ**を公開のプライバシーポリシーとして参照できます。App Store Connect では、ブラウザで本プライバシーポリシーを開き、アドレスバーから URL をコピーしてください（公開サイトのドメインは将来変更される場合があります）。

## 概要（Apple プライバシー栄養表示との整合性）

| トピック | 当社の方針 |
|-------|----------------|
| アカウント | **不要** — 登録、メールサインイン、電話番号は必要ありません |
| iHTC Studioによるデータ収集 | **データは収集しません** — 個人データを受け取るバックエンドは運営していません |
| ネットワーク | ライブラリ、reading, recite, Character Study, meditation, Life Guidance, widgets, and daily notifications work **offline** after installは、インストール後 **オフライン** で動作します |
| 分析 / 広告 / トラッキング | **なし** — サードパーティの分析、広告、トラッキングSDKは使用しておらず、App Tracking Transparencyも使用していません |
| 任意のAppleサービス | **iCloud**（個人用KVS）、**フォトライブラリ（追加のみ）**でカードを共有、**StoreKit**で任意のチップ、**ローカル通知**、オプションの**Live Activities** |

## データの収集

当社は、広告や分析のために個人情報を収集、販売、共有することは**ありません**。

- **アカウント不要** — アカウントを作成せずに、すべての基本機能を使用できます。
- **分析や広告なし** — アプリのバイナリには、サードパーティの分析、広告、クラッシュレポートSDKは統合されておらず、データが当社に送信されることはありません。
- **コンテンツのアップロードなし** — お客様のreading history, favorites, study lists, reflection journal entries, habit check-ins, meditation streaks, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## アプリの仕組み

- **同梱ライブラリ** — テキスト JSON、白話／英語、索引、学習補助はアプリ／ウィジェット バンドル内に同梱されます。閲覧と学習にネットワークは不要です。
- **オンデバイス音声** - 朗読には Apple のシステム **AVSpeechSynthesizer** (TTS) が使用されます。 章のテキストは iHTC Studio に送信されません。
- **ウィジェットと App Group** — ウィジェットとアプリは、端末上の App Group `group.com.iHTCboy.iPrimer` を通じて設定と軽量な状態を共有します。
- **毎日の通知** - ユーザー通知を使用してローカルにスケジュールされます。 通知をタップすると、デバイス上のチャプタ ID へのディープ リンクが開きます。 サーバーのファンアウトはありません。
- **カードを共有** — 画像はデバイス上でレンダリングされます。 保存すると、[保存] をタップした場合にのみ **フォト ライブラリの追加のみ**が使用されます。 システム共有シートは、**あなた**が選択したアプリに画像を送信できます。 その場合、その宛先のプライバシー ポリシーが適用されます。
- **任意チップ** — 「Tip Developer」（`com.iHTCboy.iPrimer.6`）は Apple 処理の消耗型 **StoreKit** 購入です。カード情報は受け取りません。
- **Siri / ショートカット / コントロール センター** — オプションのシステム統合により、デバイス上のディープ リンクが開きます。 彼らはあなたのライブラリを私たちに送ることはありません。
- **オプションのスポットライト** — インデックス作成を有効にすると、ローカル検索のためにデバイス上のシステムによってコンテンツのインデックスが作成されます。 当社は検索バックエンドを運用していません。

## 端末に保存されるデータ

 | データ | どこ | 目的 |
 |------|-------|-----------|
| Chapter データベース | App / Widget バンドル | オフライン閲読と学習 |
| お気に入りと学習リスト | App Group UserDefaults | 星付き作品とリスト |
 | 読書履歴 / 最後に読んだ | アプリグループのUserDefaults | 続きを読む、履歴 UI |
| 学習進捗と習熟 | App Group UserDefaults | Character Study state, quiz / Hunt progress |
| 学習連続 / チェックイン | App Group UserDefaults | Daily Study 習慣 |
| 省思ジャーナル | App Group UserDefaults | Life Guidance ジャーナル |
| 習慣チェックイン（洒扫应对） | App Group UserDefaults | Life Guidance 毎日の習慣 |
| 瞑想連続とセッション設定 | App Group UserDefaults | 瞑想の継続 |
| 共有カードの設定 | App Group の UserDefaults | 最後に選んだスタイルや比率 |
| Daily Study cache & notification prefs | App Group UserDefaults | 今日の ID, 時刻, 文脈トグル |
 | 共有カードの設定 | アプリグループのUserDefaults | 最後のスタイル/比率の選択 |
 | オンボーディングと TipKit の状態 | 標準 UserDefaults (デバイス) | ウェルカムガイド / 発見のヒント |
 | ホーム画面のクイックアクション | システム + ローカル設定 | 設定するショートカット |
 | ウィジェット / ライブ アクティビティのスナップショット | アプリグループ / ActivityKit | すでに開いているテキストを表示 |

アプリをアンインストールすると、アプリに関連するサンドボックスおよびApp Groupデータが削除されます（iOS/macOSの動作に依存します）。任意のiCloudコピーは、あなたが削除するか、同期をオフにして他の場所で削除するまで、**あなたの**iCloudに残ります。

## iCloud同期（オプション）

設定で**iCloud同期**を有効にすると、アプリは選択したユーザーデータをAppleの**`NSUbiquitousKeyValueStore`**を通じてあなたのApple IDに関連付けて同期します：

- お気に入り
- 学習リスト
- 読書履歴
- 学習進捗 / 習熟度
- 学習連続記録
- 省思ジャーナル
- 習慣チェックイン履歴

同期トラフィックは**Apple iCloud**にのみ送信され、iHTC Studioには送信されません。設定で同期を無効にできます。私たちはあなたのiCloudの内容を読むことはできません。

## 権限

 iLiezi は、機能が必要な場合にのみアクセス許可を要求します。

| 権限 | タイミング | 理由 |
|------------|------|-----|
| 通知 | Daily Study or meditation reminders を有効にする | ローカルスケジュール |
## iCloud 同期（任意）
| iCloud | 同期を有効にする | お気に入り/リスト/履歴/進捗/連続/ジャーナル/習慣を同期 |
| Live Activities (iOS) | Reading / Meditation Live Activity | ロック画面 / Dynamic Island |
| バックグラウンド音声 | バックグラウンド朗誦を有効にする | バックグラウンドで TTS 継続 |

 当社は、連絡先、正確な位置情報、カメラ、マイク (システムの TTS 再生を超える)、または追跡を要求しません**。

## 子供のプライバシー

iPrimer は **12+** で **Kids Category 外**です。児童から故意に個人情報を収集しません。アカウント不要。

## 第三者

通常利用で関与する第三者サービスは **Apple** のみ（App Store、iCloud、StoreKit、システム TTS、通知、Live Activities）。

## データ保持と削除

- **端末上:** アプリを削除するとローカル sandbox と App Group データが削除されます（OS の挙動に依存）。
- **iCloud:** 設定で同期をオフにできます。システム設定で iCloud ストレージも管理できます。
- **当社は保持しません** — 閲読・ジャーナル・習慣データのコピーを iHTC Studio サーバーに保持しません。

## このポリシーの変更

法令、製品、または App Store コンプライアンスの理由で本ページを更新することがあります。上部の「最終更新日」が変更されます。更新後も利用を続ける場合、改訂版に同意したものとみなされます。

## お問い合わせ

プライバシーに関するご質問: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
