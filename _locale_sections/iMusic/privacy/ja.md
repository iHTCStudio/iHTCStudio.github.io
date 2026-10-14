**最終更新:** 2026年9月9日

iHTC Studio（「当社」）は **iMusic**（「爱音乐」/「愛音樂」、Bundle ID `com.iHTCboy.iMusic`）を開発しました。本ページはアプリ利用時にデータがどう扱われるか（および扱われないか）を説明します。**Apple App Review** およびユーザーは本ページを公開プライバシーポリシーとして参照できます。App Store Connect では、ブラウザで本 Privacy Policy を開き、アドレスバーから URL をコピーしてください（公開ドメインは将来変更される場合があります）。

## 概要（Apple プライバシー表示ラベルとの整合）

| 項目 | 当社の方針 |
|-------|----------------|
| アカウント | **不要** — 登録、メールログイン、電話番号なし |
| iHTC Studio によるデータ収集 | **Data Not Collected** — 個人データを受け取る backend を**運用しません** |
| ネットワーク | **ガイド**はインストール後**オフライン**で閲覧可能。**再生**と**曲認識**は認可後に Apple サービスを使用 |
| 分析 / 広告 / 追跡 | **なし** — 第三者 analytics / 広告 / 追跡 SDK なし；App Tracking Transparency 不使用 |
| 任意の Apple サービス | **Apple Music / MusicKit**、**ShazamKit**、**iCloud**（私有 KVS）、シェアカード用 **Photo Library（追加のみ）**、任意チップ **StoreKit**、**ローカル通知**、任意 **Live Activities** |

## データ収集

広告や分析目的で個人情報を収集・販売・共有**しません**。

- **アカウントなし** — 当社アカウントなしで同梱ガイドをすべて閲覧できます。
- **分析・広告なし** — 当社へ電話する第三者 analytics / 広告 / クラッシュ SDK は同梱しません。
- **ガイドのアップロードなし** — お気に入り、リスンリスト、後で聴く、ノート、履歴、設定は端末（および任意で**あなたの** iCloud）に留まり、iHTC Studio サーバーへは送信されません（**当社は本アプリ用の such サーバーを運用しません**）。
- **楽曲ホスティングなし** — フルオーディオは同梱しません。マッチした再生は **Apple Music** が提供。未加入時は最大 **30 秒カタログプレビュー**を端末にキャッシュする場合があります。

## アプリの動作

- **同梱ライブラリ** — 曲索引、ガイド、歌手ノート、カテゴリ、コレクション、名句、日次カレンダーは App / Widget 同梱。ガイド閲覧にネットワーク不要。
- **Apple Music（MusicKit）** — 再生しアクセスを許可すると、精選カタログを照合（ISRC 優先、次にアーティスト + タイトル）し Apple プレイヤーで再生。加入状態は Apple に問い合わせ；タイムアウトは**不明**扱い（「未加入」とは断定しません）。カバー表示のため artwork URL を取得する場合があります。Apple ID や支払情報は当社に届きません。
- **30 秒プレビュー** — 未加入時、Apple プレビューが端末 `Caches` に保存される場合あり（LRU；フルトラックではありません）。セルラー / 低電力 / 低データモードでは次のプレビューを先読みしません。設定で artwork とプレビューキャッシュを個別に削除でき、お気に入りやリスンリストには触れません。
- **曲認識（ShazamKit）** — Recognize を開いたときのみ。マイク音声は **Apple** が処理；録音アーカイブは保持しません。カタログヒットで端末内ガイドを開きます。
- **端末内音声** — ガイド朗読は Apple **AVSpeechSynthesizer**。本文を iHTC Studio へ送りません。
- **Widget と App Group** — App と Widget は端末上 `group.com.iHTCboy.iMusic` で設定共有。Live Activity の artwork は小 JPEG + token（ペイロード全体にフル画像は入れません）。
- **毎日の通知** — ローカルスケジュール。タップで端末内曲 ID への deep link。
- **シェアカード** — 端末でレンダリング。保存タップ時のみ **Photo Library 追加のみ**。
- **任意チップ** — Apple **StoreKit** 消耗型。
- **任意 Spotlight** — **既定オフ**。有効時は端末上でシステムに索引送信。

## 端末に保存されるデータ

| データ | 場所 | 目的 |
|------|-------|---------|
| ガイドライブラリ（索引 + シャード） | App / Widget bundle | オフライン閲覧 |
| お気に入り、リスンリスト、後で聴く | App Group UserDefaults | あなたのリスト |
| ノート、履歴、朗読進捗 | App Group UserDefaults | 聴取 / 閲覧の継続 |
| ストリーク / チェックイン | App Group UserDefaults | 毎日の習慣 |
| 外観、言語、音声、タブ | App Group UserDefaults | 設定 |
| Daily Piece キャッシュと通知設定 | App Group UserDefaults | 今日の ID とスケジュール |
| シェアカード設定 | App Group UserDefaults | 前回のスタイル / キャンバス |
| Artwork URL とデコード画像 | App Group + メモリ / ディスクキャッシュ | カバー表示；MusicKit 認可後のみ静かに先読み |
| 30 秒プレビューファイル | App Caches | 初回ヒット後オフライン再生 |
| Live Activity サムネイル | App Group JPEG + token | ガイド**朗読**中の Lock Screen / Dynamic Island |
| MusicKit / Shazam 認可 | システム | 選択の記憶 |
| オンボーディングと評価プロンプト | 端末 UserDefaults | ウェルカム / レビュー |

アンインストールでサンドボックスと App Group を削除（iOS / macOS の規則に従う）。任意 iCloud コピーは**あなたの** iCloud に残ります。Apple Music ライブラリと加入は Apple 側に残ります。

## iCloud 同期（任意）

設定で **iCloud Sync** を有効にすると、**あなたの Apple ID** に紐づく **`NSUbiquitousKeyValueStore`** で以下をミラーします：

- お気に入り
- リスンリスト
- 後で聴く
- ノート
- 聴取 / 閲覧履歴
- 朗読進捗
- ストリーク

ガイド本文は既に App 同梱。Artwork ファイルとプレビュー音声は KVS 同期**しません**。トラフィックは **Apple iCloud** へ行き、iHTC Studio を経由しません。設定で無効化できます。当社はあなたの iCloud 内容を読めません。

## 権限

iMusic は機能に必要なときだけ権限を要求します：

| 権限 | タイミング | 理由 |
|------------|------|-----|
| **Apple Music / メディアライブラリ** | Music 説明で続行、または再生タップ | カタログ曲の照合と再生；カバー読込 |
| **マイク** | Song ID を開く | 周囲の音楽を認識 |
| **通知** | Daily Piece リマインダーを有効化 | ローカルスケジュール |
| **Photo Library（追加のみ）** | ミュージックカード保存 | レンダリング画像の書き込み；ライブラリ全体は読まない |
| **iCloud** | 同期を有効化 | リスト / ノート / 履歴 / ストリークのミラー |
| **Live Activities（iOS）** | Reading Live Activity をオン（既定オン） | **朗読**中のガイドを Lock Screen / Dynamic Island に表示 |
| **バックグラウンドオーディオ** | バックグラウンドオーディオをオン | 非前面時も MusicKit / プレビュー / TTS を継続 |

連絡先、精密位置、カメラ、Tracking は要求**しません**。Photo Library の読み取りも要求**しません**。

## 当社が行わないこと

- 個人データの販売や広告プロファイルの構築**をしない**
- アカウントやソーシャルログインを強制**しない**
- データ収集目的の第三者 ad / analytics / ソーシャル SDK を同梱**しない**
- 端末や当社サーバーにフル曲を保存**しない**
- 認識後 Shazam マイクバッファを保持**しない**
- **音楽再生**用のカスタム Dynamic Island を表示**しない** — ガイド朗読時のみ（設定でオンの場合）
- StoreKit のカード番号を受け取ら**ない**

## 児童のプライバシー

iMusic は 13 歳未満（または地域の同等年齢）を含め、故意に個人データを収集しません。データ収集 backend がないため、当社に児童プロファイルはありません。Apple Music と Shazam は Apple の規約と年齢ルールに従います。

## 第三者

- **Apple** — App Store、MusicKit / Apple Music、ShazamKit、任意 StoreKit、任意 iCloud KVS、システム TTS、あなたが選ぶ共有先、通知、Live Activities、Siri / Shortcuts
- データ収集目的の **他の第三者 SDK はありません**

## 国際的なユーザー

ガイドは端末でオフライン利用可能。Apple Music、Shazam、iCloud は Apple の規約と地域提供に従います。カタログ照合はサインイン中 Apple ID のストアフロントに依存します。

## データの保持と削除

- **端末** — **設定 → ストレージ**で artwork / プレビューキャッシュを削除。アンインストールでサンドボックスと App Group を削除。
- **iCloud（任意）** — **あなたの** iCloud に残り、同期をオフにするか Apple のツールで消すまで。
- **iHTC Studio** — 削除依頼のサーバー側アカウントデータセットはありません。

## 本ポリシーの変更

随時更新する場合があります。上部の「最終更新」日付が変わり、改訂版が本ページに掲載されます。

## お問い合わせ

- **メール:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

通常 48 時間以内に返信します。
