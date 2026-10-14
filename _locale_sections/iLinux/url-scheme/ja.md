iLinuxは** `ilinux://` **をサポートしています(また、** `iLinux://` **を記述) URLスキームは、**iPhone、iPad、Macでディープリンクします** - コマンド詳細(Linux、CMD、PowerShell)、デイリークイズ、お気に入り、またはSafariから間違った回答ブック、別のアプリ、ウィジェットタップ(iOS / iPad)、またはAppleショートカットを開きます。

コマンド URL は、オプションの ** `ilinux://` ** クエリパラメーターを受け入れますので、ウィジェットのタップとショートカットは Windows エントリを正しく開くことができます。

**ホーム画面クイックアクション**(**iOS / iPadのみのアプリアイコンを長押し**)カバー検索、カテゴリ、フィードバックとレート。 Macユーザーは、代わりに**iLinux**メニューとキーボードショートカットを使うことができます。

> **重要:** iLinux は ** リファレンスと学習アプリ ** です。 URL は、****** 内の** Navigate のみリンクします。 Linux コマンドを実行し、SSH セッションを開くか、リモートサーバに接続しない

## プロトコル仕様


```
ilinux://<host>[/<path>][?query]
iLinux://<host>[/<path>][?query]   ← same scheme, case-insensitive
```


| Rule | 詳細を見る |
|------|--------|
| **Scheme** | `ilinux` / `iLinux` — ケースを無感覚に比較 |
| **Host routing** | プライマリルータはURL **host**です。 いくつかのパスも受け付けています(以下を参照してください) |
| **Command detail** | ホスト `command` **or** パス `/command` |
| **Command ID** | クエリ `name=<id`> ** または** `cmd=<id>` — はバンドルされたコマンドキー (例えば `ls`、`grep`、`dir`、`Get-ChildItem`) と一致しなければなりません。 |
| **Platform** | 省略時に `platform=<value>` をリクエストします。省略時に**Linux** にデフォルト値を指定します。 |
| **Quiz** | ホスト `quiz` **or** パス `/quiz` |
| **Favourites** | ホスト `favorites` **or** パス `/favorites` |
| **Wrong book** | ホスト `wrong`、`mistakes`、または `wrongquestions`;`/wrong` または `/mistakes` も受け入れる |
| **Wrong record** | 間違ったブック URL で `record=<UUID>` をクエリー — レコードのコマンド詳細を開く |
| **Query parameters** | 他のプレフィルパラメータはサポートされていません |
| **Parser** | "ILinuxDeepLink.parse( :)` — `onOpenURL` → `AppRouter.pendingDeepLink` で消費 |

**2つの配達チャネル**

| Channel | Handled by | 例 |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ILinuxDeepLink.parse` → `RootTabView` | `command`、`quiz`、`favorites`、`wrong` |
| **Home Screen Quick Action** | `ShortcutSceneDelegate` → `ShortcutObserver.dispatch` | `search`、`categories`、`feedback`、`review`、`quiz`/`favorites`/`wrong`をオーバーラップ |

クイックアクションタイプは、タイプ文字列にマッチする** `ilinux://` **を使うので、 `iLinux://` とレガシーのバリアントも正しくルーティングします。

---

## 1. コマンド詳細

単一のバンドルされたコマンドで詳細ページを開きます。

| Parameter | Required | コンテンツ |
|-----------|----------|-------------|
| `name` | One of `name` / `cmd` | コマンドID(プラットフォームJSONバンドルの辞書キー) |
| `cmd` | One of `name` / `cmd` | ウィジェットリンクで使用される `name` の同義語 |
| `platform` | No | シェルライブラリ: 下の表を参照してください。 デフォルトで**Linux** |

** `ilinux://` 値** (ケースインセンティブ):

| Value | Shell library | エイリアス |
|-------|---------------|---------|
| *(omit)* or `linux` | Linux (1050 commands) | — |
| `cmd` | CMD / Batch (300 commands) | `batch`, `bat` |
| `powershell` | PowerShell (300 commands) | `ps`, `pwsh` |

**行動**

- **Commands**タブに切り替えて、要求された**shellプラットフォーム**を選択し、解決されたコマンドで`CommandDetailView`を押します。
- ID が **unknown または empty** の場合、リンクは **silently無視** (エラー UI なし) です。
- コマンド ID は **case-pathy** で、バンドルされた JSON キーを正確に一致しなければなりません(通常、`docker` など)。

**オープン `ilinux://` **


```
ilinux://command?name=ls
```


** `ilinux://` (Linux、デフォルト)を開く**


```
ilinux://command?cmd=grep
```


**CMDを開く `ilinux://` **


```
ilinux://command?cmd=dir&platform=cmd
```


PowerShell を開く `ilinux://` **


```
ilinux://command?cmd=Get-ChildItem&platform=powershell
```


**クラウドネイティブLinuxの例**


```
ilinux://command?name=docker
```


---

## 2. 毎日のクイズ

**毎日のクイズ**タブに直接ジャンプします。 ****自動起動や質問をスキップしません。


```
ilinux://quiz
```


パスの形態(また受け入れられます):


```
ilinux:///quiz
```


---

## 3. お気に入り

[設定] ナビゲーションで [**Favourites**] リストを開きます。


```
ilinux://favorites
```


パスの形態(また受け入れられます):


```
ilinux:///favorites
```


---

## 4. 間違った答え帳

### 4.1 リスト

[設定] ナビゲーションの [*間違った回答ブック**] リストを開きます。


```
ilinux://wrong
```


エイリアス(同じ行動):


```
ilinux://mistakes
ilinux://wrongquestions
```


### 4.2 シングルレコード→コマンド詳細 `ilinux://` が保存された間違ったエントリの有効な UUID である場合、アプリは、**Commands**タブを開き、レコードのコマンド(レコードとコマンドがまだ存在する場合)の詳細を押します。

| Parameter | Required | フォーマット |
|-----------|----------|--------|
| `record` | Yes | UUID 文字列、例えば `550e8400-e29b-41d4-a716-446655440000` |


```
ilinux://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


UUIDが無効であるか、レコードが削除された場合、ナビゲーションは間違ったブックリストに戻り、スキップされます。

---

## 5. ホーム スクリーンの速い行為

iLinux のアイコンを長押しする → 4** アクションまで。 *Settings → Home Screen Shortcuts** (7オプション、reorder、デフォルトへのリセット) で設定します。

| Option | Registered `type` | SF Symbol | オープン |
|--------|-------------------|-----------|--------|
| Search | `iLinux://search` | magnifyingglass | **コマンド**タブ+検索バーの有効化 |
| Daily Quiz | `iLinux://quiz` | checklist | **デイリー・クイズ**タブ |
| Favourites | `iLinux://favorites` | star.fill | **お気に入り** リスト |
| Wrong Answer Book | `iLinux://wrong` | xmark.bin.fill | **間違った回答ブック**リスト |
| Categories | `iLinux://categories` | rectangle.grid.2x2.fill | **カテゴリー**タブ |
| Send Feedback | `iLinux://feedback` | envelope.fill | アプリ内メールコンポーズ(または `mailto:` フォールバック) |
| Rate App | `iLinux://review` | star.bubble.fill | StoreKitレビュープロンプト |

**最初のインストールのデフォルト選択:**検索·毎日のクイズ·お気に入り·フィードバックを送信.

**クイックアクションのみの宛先** ( `ilinux://` / `iLinux://` で処理されていない)

- `iLinux://search`
- `iLinux://categories`
- `iLinux://feedback`
- `iLinux://review`

*long-press icon** または Quick Action パイプラインを介して同じタイプを投稿することでこれらを使用して、ショートカットで開く**Open URL**は、アプリが後で明示的なホストをパースしない限り、**動作しない場合があります。

**レガシータイプ(固定):**

| Type | ビーキャビア |
|------|-----------|
| `iLinux://love` | アプリ内のSafariシート(旧静的ショートカット)で作者のブログを開く |

---

## 6.ウィジェットディープリンク

Widget は `iLinux://` によって構築された URL と同じ `ilinux://` を使用します。

| Widget | Tap target | 忍耐 を 生み出 し なさ い . |
|--------|------------|-----|
| Daily Command | Command detail | `iLinux://command?cmd=<id>&platform=<linux\ | cmd\ | パワーシェル>` |
| Category Spotlight | Sample command | `iLinux://command?cmd=<id>&platform=<platform>` |
| Quiz Glance | Daily Quiz | `iLinux://quiz` |
| Favourites Glance | Favourites (or per-row command) | `iLinux://favorites`/`iLinux://command?cmd=<id>&platform=<platform>` |
| Wrong Book Glance | Wrong book (or per-row record) | `iLinux://wrong`/`iLinux://wrong?record=<UID>` |

ウィジェット URL は `ilinux://` で作成され、コマンド タップの [** `iLinux://` **] も含まれています。 プラットフォームは、**Settings → Widgets → Widgetコマンドライブラリ**(Linux / CMD / PowerShell)にマッチします。

**デイリーコマンドシャッフルボタン**(iOS 17+、App Intent)はウィジェットのタイムラインのみをリロードします。** URLは使用しません。

---

## Appleのショートカット

### 名前をコピーした後にコマンドを開く

1.**入力からテキストを取得する**
2.**URLを開く** → `ilinux://` + テキスト

またはハード コード Linux:


```
ilinux://command?name=systemctl
```


CMDコマンドを開きます。


```
ilinux://command?cmd=ipconfig&platform=cmd
```


### 毎日の勉強のリマインダー → クイズ


```
ilinux://quiz
```


個人的なオートメーション(例:毎週9:00)に** URLを開く

### 間違った回答を確認する


```
ilinux://wrong
```


### フォーカスモードショートカットからお気に入りを開く


```
ilinux://favorites
```


---

## Behaviourを起動

アプリケーションが URL または Quick Action を受け取る場合:

| Scenario | フローリング |
|----------|------|
| **Cold start — Quick Action (iOS/iPad only)** | 「ショートカットキー」→「PendingShortcutBuffer」→「ショートカットObserver.onAppear」→「dispatch(type:)」 |
| **Warm start — Quick Action (iOS/iPad only)** | シーンコールバック → 通知 → `dispatch(type:)` |
| **Cold / warm — `onOpenURL` (iOS, iPad, Mac)** | `AppRouter.handleIncomingURL` → `pendingDeepLink` → `RootTabView.onChange` は、 |
| **Feedback / Rate (cold start)** | `deferSheetWork` 遅延**~0.4 s** メールシート / StoreKit はアクティブなウィンドウシーン |
| **Search quick action** | `openSearchTab()` → `searchPulse += 1` → `BrowseCommandsView` の検索 (iOS 17 +: `isPresented` による自動焦点) |
| **Unknown command ID** | ディープリンクがパースされたが、ナビゲーションがスキップされた — アラートなし |

---

## キーボードショートカット

### iPadとMac(共有)

Mac共有のiPadと**iLinux**メニューのハードウェアキーボード:

| Shortcut | アクション |
|----------|--------|
| ⌘F | コマンドタブ+検索(iOS上で検索クイックアクションとして意図) |
| ⌘1 | コマンドタブ |
| ⌘2 | カテゴリー タブ |
| ⌘3 | 毎日のクイズタブ |
| ⌘4 | 設定タブ |

⌘F経由でオートフォーカスを検索するには、**iOS 17.0 +**または**macOS 14.0 +**が必要です。

### Macのみ

| Shortcut | アクション |
|----------|--------|
| ⌘, | 設定タブ |
| ⌘[ / Esc | ポップアップナビゲーションスタック(バック) |
| ⌘← / ⌘→ | 前 / 次のカテゴリ(カテゴリタブ) |
| 1–4 | クイズの回答オプションを選択 |
| ⌘R | リシャッフルデイリークイズ |
| Return | 次のクイズ質問(回答後) |

ディープリンク( `ilinux://` )とメニューショートカットは、iOS上でMac上で同じアプリ内ルータを使用します。

---

## サポートされていないURLと無効なURL

| URL | Result |
|-----|--------|
| `ilinux://command` (no `name` / `cmd`) | 無視される |
| `ilinux://command?name=NotARealCmd` | 無視される(解決されたプラットホームのための図書館でないID) |
| `ilinux://command?cmd=dir` (no platform) | Windows CMD 用の `platform=cmd` を使う |
| `ilinux://search` via Shortcuts Open URL | **「ILinuxDeepLink」で解析されていない — **iOS/iPad**、または**Mac/iPad**で⌘Fを使う |
| `ilinux://categories` via Shortcuts Open URL | 上記と同じ |
| `ilinux://feedback` / `ilinux://review` via Open URL | 上記と同じ |
| Non-`ilinux` schemes | 無視される |

---

## トラブルシューティング

**ショートカットはアプリを開きますが、何も発生しません(コールド起動)**

フィードバック、率および郵便シートは進水の後で~0.4 sを必要とします。 アプリ内からもう一度お試しください。またはコールドスタートでしばらくお待ちください。

**検索クイックアクションは、検索フィールドに焦点を合わせません(iOS 16)**

オートフォーカスはiOS 17以降が必要です。 iOS 16 では、コマンドタブが開きます。 手動で検索フィールドをタップします。

**Widget Tap は期待するコマンドが開けない**

正しい**platform**のためにインストールされたアプリバージョンにまだコマンドが存在することを確認してください。 ウィジェットのリンクは、 `ilinux://` + `iLinux://` を使用し、厳密なコマンド ID が必要です。例: `platform` は、デフォルトの Linux ライブラリではなく、 `ilinux` を必要とします。

**クイックアクションのタイトルは間違った言語です**

*Settings → Language** で言語を変更します。アプリはショートカット項目を自動的に再登録します。

**ディープリンクは、デバイス上で動作しますが、Webページからではありません**

リンクは、カスタムスキームを除去するアプリ内ブラウザでブロックされていない、システム(ノート/メッセージのタップ)によって開いています。

---

[iLinuxサポートに戻る](./) &middot; [FAQ](../faq) &middot; [プライバシーポリシー](./privacy)


