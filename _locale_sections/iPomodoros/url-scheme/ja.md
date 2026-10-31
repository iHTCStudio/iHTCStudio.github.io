iPomodoroは** `iPomodoro://` **と** `iPomodoros://` **をサポートしています URLスキームの深いリンク — Safari、別のアプリ、QRコード、またはAppleショートカットからタブまたはアプリ内シートを開きます。 これらのURLは、**ホーム画面クイックアクション**(アプリアイコンを長押し)として利用可能な目的地をミラーリングします。

> **注記:** URL リンクは** 起動またはタイマーを停止し、タスク ID を渡すか、プレフィルの期間を過ぎません。 それらはアプリ内でのみ移動します。 アプリを開くことなく、音声焦点の要約のために、**Siri App Shortcuts**([関連:Siri & App Shortcuts](#関連-siri-app-shortcuts)を使用してください)。

## プロトコル仕様


```
iPomodoro://<path>
iPomodoros://<path>
```


| Rule | 詳細を見る |
|------|--------|
| **Schemes** | 「iPomodoro」(プライマリ)・「iPomodoros」 |
| **Path** | 単一のセグメント、**case-inpathy** — URL *host**から解決 |
| **Query parameters** | 未対応(現時点で無視) |
| **Equivalent Quick Action type** | `iPomodoro://<path>` (ホーム画面のショートカットに登録された同じ文字列) |

Path マッチングは、セグメント名で **exact** です。このアプリは `iPomodoro://` のような不審なサブ文字列ではありません。

---

## 行き先

| Path | Opens | ノート |
|------|--------|-------|
| `pomodoro` | **Pomodoro** tab | セッションを自動起動しない |
| `study` | **Study Timer** tab | セッションを自動起動しない |
| `tasks` | **Tasks** tab |  |
| `stats` | **Statistics** tab |  |
| `motivation` | **Motivational Quote Anthology** full-screen gallery | 同じUIとして**設定→モチベーション引用設定→モチベーション引用符Anthology** |
| `feedback` | **Feedback** sheet | 利用可能な場合、アプリ内メールコンポースを使用する。 `mailto:` に戻る |

---

## 例

**ポモドーロタブを開く**


```
iPomodoro://pomodoro
```


**学習タイマータブを開く**(代替スキーム)


```
iPomodoros://study
```


**統計ダッシュボードを開く**


```
iPomodoro://stats
```


**モチベーションの引用を表示**


```
iPomodoro://motivation
```


**オープンフィードバック**


```
iPomodoro://feedback
```


---

## Behaviorを起動

アプリが URL を受信したときに (cold start または while run)

1. `iPomodoro://` 2. 運行は*deferred  0.45 s**です従ってSwiftUIは土台を終えることができます。
3。**cold start**では、URL / クイックアクションは**優先度**自動で、復元されたライブアクティビティセッションからアクティブポモドーロまたはスタディタブにジャンプします。

**Motivation** と **feedback** は直接オーバーレイします。それらはタブを最初に切り替えません。

---

## Appleのショートカット

**ポモドーロタブを開く**

1. アクションを追加**URLを開く**
2. URL: `iPomodoro://` **フォーカスブロック後の統計を開く**


```
iPomodoro://stats
```


パーソナルオートメーション(フォーカスモード終了後など)で**URL**を開き、ダッシュボードに直接ジャンプします。

---

## 関連: Siri & App ショートカット

組み込み**Appショートカット**(Siri / Shortcutsアプリ)はURLリンクを補完します。

| Intent | 行動規範 |
|--------|----------|
| Open Pomodoro | ポモドーロタブへの切り替え |
| Open Study Timer | タイマータブを学習するためのスイッチ |
| Open Statistics | 統計タブへの切り替え |
| Today's focus summary | アプリのUIを要求することなく、今日の焦点の持続時間とpomodoroカウントを返します** |

事例 Siri phrase: *「iPomodoro に焦点を当てたのは?」*

設定 → アプリ設定 → ホーム画面のショートカット** (再注文するドラッグ) の下のホーム画面アイコンに 4 つの項目が表示されるかを設定します。 上記のURLパスは、すべての6つの可能な目的地をカバーします。 一度にアイコンに4つしか表示できません。

---

## トラブルシューティング

| Issue | 確認する |
|-------|----------------|
| Link does nothing | アプリケーションがインストールされていることを確認してください。 上記の6つの名前の1つでなければなりません |
| Wrong tab after reopening | タイマーライブアクティビティがアクティブの場合、**クイックアクション/ URL 起動オーバーライド**自動タブ復元 |
| `feedback` opens Mail app only | iPomodoroはメールアカウントを設定していません。 |

---

[iPomodoro サポートに戻る](./) &middot; [FAQ](../faq) &middot; [プライバシーポリシー](./privacy)


