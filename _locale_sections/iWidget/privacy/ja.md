**最終更新:** 2026年9月30日

iHTC Studio（「当社」）は **iWidget**（「爱组件」/「愛組件」、Bundle ID `com.iHTCboy.iWidget`）を開発しました。本プライバシーポリシーは、アプリとウィジェット拡張利用時に扱う（および扱わない）データを説明します。**Apple App Review** とユーザーは本ページを公開プライバシーポリシーとして参照できます。App Store Connect ではブラウザで [Privacy Policy](../privacy) を開き、アドレスバーから URL をコピーしてください（公開ドメインは将来変わる場合があります）。

## 概要（Apple Privacy Nutrition Label 整合）

| 項目 | 当社の方針 |
|------|------------|
| アカウント | **不要** — iHTC Studio への登録・サインインなし |
| iHTC Studio によるデータ収集 | **Data Not Collected** — ウィジェットデザイン・壁紙・カレンダーデータを受け取る backend を運用しない |
| 広告 / analytics | **なし** — 広告、第三者 analytics、トラッキング SDK なし |
| コア暦・黄历 | **端末内** 同梱表から計算；任意で祝日 JSON を公開 GitHub ミラーから取得（下記） |
| 天気 | 天気ブロックまたは今日の天気有効時 **Apple WeatherKit** — リクエストは **Apple** へ、iHTC Studio へではない |
| 任意 Apple サービス | デザイン同期の **iCloud (CloudKit)**、**HealthKit**（歩数/距離読取）、**使用中のみ位置**（または手動都市）、**ローカル通知**、**Background App Refresh** |

## データ収集

- **アカウントなし** — 当社アカウントなしで利用可能。
- **広告・analytics SDK なし** — iHTC Studio へ usage analytics を送らない。
- **デザイン用 iHTC Studio クラウドなし** — レイアウト、クロップ壁紙、カウントダウン、キャッシュは **App Group**（任意で **あなたの** iCloud）。当社は boards をホストしない。

## ネットワーク利用

| 機能 | 内容 |
|------|------|
| **WeatherKit** | 選択位置/都市の予報を Apple に問い合わせ。UI に **Apple Weather** 帰属表示。 |
| **法定休日更新** | 公開祝日 JSON（例：**holiday-cn**）を数日ごとに取得し休/班を更新。個人識別子は当社から送らない。 |
| **任意 OSS フォント** | Smiley Sans / LXGW WenKai を選択時 App Group にダウンロード。 |
| **開発者へのチップ** | 任意 StoreKit 消耗型は Apple が処理。カード番号は当社が受け取らない。 |
| **Feedback メール** | 送信時 Mail が非秘密診断（バージョン、機種）を添付可能。送信はユーザー操作。 |

暦・黄历・エディタ・プレビュー・ウィジェット（ライブ天気取得除く）・通知スケジュールは、インストール後 **オフライン** で動作。

## 端末保存（App Group）

App Group `group.com.iHTCboy.iWidget` 例：

| データ | 目的 |
|------|------|
| `designs/*.json` | 保存ウィジェットボード |
| `images/*`, `wallpaper/*` | クロップ壁紙スロット（明暗） |
| `countdowns/items.json` | カウントダウン一覧 |
| `cache/weather.json` | 天気スナップショット |
| `cache/battery.json` 等 | デバイスブロックスナップショット (iOS) |
| `cache/holidays/{year}.json` | ダウンロードした法定休日表 |
| UserDefaults | 言語、テーマ、祝日 filt、ウィジェットセッション、失効デザイン ID 等 |

アンインストールで sandbox / App Group データは OS 挙動に従い削除。

## iCloud 同期（任意、既定オフ）

**設定** で **iCloud** を有効にすると **CloudKit** 私有 DB `iCloud.com.iHTCboy.iWidget`（ゾーン **Designs**）、`CKSyncEngine` で同期：

- デザイン JSON サマリーと全文
- デザイン関連クロップ壁紙

通信は **Apple iCloud**（**あなたの Apple ID**）。当社は iCloud 内容を読めない。オフで同期停止；ローカルは削除するまで残る。

## 権限

| 権限 | タイミング | 理由 |
|------|------------|------|
| **使用中のみ位置** | 位置ベース天気 | WeatherKit 用都市；**手動都市** 可 |
| **HealthKit（読取）** | 歩数ブロック | 今日の歩数/歩行距離 |
| **Apple Music / メディア** | Now Playing | 再生中タイトル・アートワーク |
| **通知** | リマインダー有効 | 祝日/カウントダウン/休班のローカル通知 |
| **Background App Refresh** | システム許可 | 天気/デバイスキャッシュ定期更新（約 6 h） |
| **iCloud** | 同期トグル | 端末間デザインバックアップ |

連絡先、カメラ、マイク録音、広告 ATT は **要求しません**。

## ウィジェット拡張

拡張はアプリと **同一 App Group** を読み、設定 UI で選んだデザインを描画。インタラクティブ intent（天気更新、カウントダウンサイクル、月移動）は端末内。ウィジェットの天気取得は時間制限（例 ~8 s）、失敗時キャッシュ。

## プライバシーマニフェスト

`PrivacyInfo.xcprivacy` で **UserDefaults** を理由 **CA92.1**（アプリ機能）として宣言。

## 児童のプライバシー

故意に児童の個人情報を収集しません。データ収集 backend を運用しないため、特別な児童アカウントは不要です。

## 変更

方針を更新する場合、本ページの日付を更新します。

## お問い合わせ

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
