---
layout: doc
title: iPomodoro — URL Scheme Reference
app_id: iPomodoros
doc_title_en: URL Scheme Reference
doc_title_zh_cn: URL Scheme 深度链接文档
doc_title_zh_tw: URL Scheme 深度連結文件
description: Complete reference of iPomodoro:// and iPomodoros:// deep links — open tabs, motivation quote, or feedback from Safari, Shortcuts, or other apps.
---

<section lang="en" markdown="1">

iPomodoro supports **`iPomodoro://`** and **`iPomodoros://`** URL scheme deep links — open a tab or in-app sheet from Safari, another app, a QR code, or Apple Shortcuts. These URLs mirror the destinations available as **Home Screen Quick Actions** (long-press the app icon).

> **Note:** URL links do **not** start or stop timers, pass task IDs, or pre-fill durations. They only navigate inside the app. For spoken focus summaries without opening the app, use **Siri App Shortcuts** (see [Related: Siri & App Shortcuts](#related-siri--app-shortcuts) below).

## Protocol Specification

```
iPomodoro://<path>
iPomodoros://<path>
```

| Rule | Detail |
|------|--------|
| **Schemes** | `iPomodoro` (primary) · `iPomodoros` (also accepted) |
| **Path** | Single segment, **case-insensitive** — resolved from the URL **host** |
| **Query parameters** | Not supported (ignored if present) |
| **Equivalent Quick Action type** | `iPomodoro://<path>` (same string registered on Home Screen shortcuts) |

Path matching is **exact** on the segment name — the app does not fuzzy-match substrings like `contains("pomodoro")`.

---

## Destinations

| Path | Opens | Notes |
|------|--------|-------|
| `pomodoro` | **Pomodoro** tab | Does not auto-start a session |
| `study` | **Study Timer** tab | Does not auto-start a session |
| `tasks` | **Tasks** tab | |
| `stats` | **Statistics** tab | |
| `motivation` | **Motivational Quote Anthology** full-screen gallery | Same UI as **Settings → Motivational Quote Settings → Motivational Quote Anthology** |
| `feedback` | **Feedback** sheet | Uses in-app Mail compose when available; falls back to `mailto:` |

---

## Examples

**Open Pomodoro tab**

```
iPomodoro://pomodoro
```

**Open Study Timer tab** (alternate scheme)

```
iPomodoros://study
```

**Open Statistics dashboard**

```
iPomodoro://stats
```

**Show a motivation quote**

```
iPomodoro://motivation
```

**Open feedback**

```
iPomodoro://feedback
```

---

## Launch Behavior

When the app receives a URL (cold start or while running):

1. `ShortcutObserver` resolves the path via `AppShortcutOption.matchingShortcutURL`.
2. Navigation is **deferred ~0.45 s** so SwiftUI can finish mounting.
3. On **cold start**, a URL / Quick Action takes **priority** over automatically jumping to an active Pomodoro or Study tab from a restored Live Activity session.

**Motivation** and **feedback** open overlays directly — they do not switch tabs first.

---

## Apple Shortcuts

**Open Pomodoro tab**

1. Add action **Open URL**
2. URL: `iPomodoro://pomodoro`

**Open Statistics after a focus block**

```
iPomodoro://stats
```

Use **Open URL** in a Personal Automation (e.g. after a Focus mode ends) to jump straight to your dashboard.

---

## Related: Siri & App Shortcuts

Built-in **App Shortcuts** (Siri / Shortcuts app) complement URL links:

| Intent | Behavior |
|--------|----------|
| Open Pomodoro | Switches to Pomodoro tab |
| Open Study Timer | Switches to Study Timer tab |
| Open Statistics | Switches to Statistics tab |
| Today's focus summary | Returns today's focus duration and pomodoro count **without requiring the app UI** |

Example Siri phrase: *"How long did I focus today in iPomodoro?"*

Configure which four items appear on the Home Screen icon under **Settings → App settings → Home Screen shortcuts** (drag to reorder). URL paths above cover all six possible destinations; only four can appear on the icon at once.

---

## Troubleshooting

| Issue | What to check |
|-------|----------------|
| Link does nothing | Ensure the app is installed; path must be one of the six names above |
| Wrong tab after reopening | If a timer Live Activity is active, a **Quick Action / URL launch overrides** auto tab restore |
| `feedback` opens Mail app only | Device has no configured Mail account — iPomodoro falls back to `mailto:` |

---

[Back to iPomodoro Support](../) &middot; [FAQ](../faq) &middot; [Privacy Policy](../privacy)

</section>
<section lang="zh-CN" markdown="1">

爱番茄（iPomodoro）支持 **`iPomodoro://`** 与 **`iPomodoros://`** URL Scheme 深度链接——可从 Safari、其他 App、二维码或苹果快捷指令打开指定 Tab 或应用内页面。这些 URL 与 **主屏 Quick Actions**（长按图标）指向相同目的地。

> **说明：** URL **不会**自动开始/停止计时，也不支持传入任务 ID 或预填时长，仅用于 App 内导航。若需不打开界面即可查询今日专注，请使用 **Siri App Shortcuts**（见下文 [相关：Siri 与 App Shortcuts](#相关siri-与-app-shortcuts)）。

## 协议规范

```
iPomodoro://<path>
iPomodoros://<path>
```

| 规则 | 说明 |
|------|------|
| **Scheme** | `iPomodoro`（主）· `iPomodoros`（亦支持） |
| **Path** | 单段路径，**大小写不敏感** — 从 URL **host** 解析 |
| **查询参数** | 不支持（若附带会被忽略） |
| **等同 Quick Action type** | `iPomodoro://<path>`（与主屏快捷操作注册字符串一致） |

路径匹配为 segment **精确匹配**，不会用模糊 `contains("pomodoro")` 等方式猜测。

---

## 目的地

| Path | 打开 | 说明 |
|------|------|------|
| `pomodoro` | **番茄** Tab | 不会自动开始计时 |
| `study` | **计时** Tab | 不会自动开始计时 |
| `tasks` | **定任务** Tab | |
| `stats` | **统计** Tab | |
| `motivation` | **励志语录大全** 全屏浏览 | 与 **设置 → 励志语设置 → 励志语录大全** 相同 UI |
| `feedback` | **反馈** Sheet | 优先应用内邮件；不可用则 `mailto:` 回退 |

---

## 示例

**打开番茄 Tab**

```
iPomodoro://pomodoro
```

**打开计时 Tab**（备用 scheme）

```
iPomodoros://study
```

**打开统计仪表盘**

```
iPomodoro://stats
```

**展示励志语录**

```
iPomodoro://motivation
```

**打开反馈**

```
iPomodoro://feedback
```

---

## 启动行为

App 收到 URL（冷启动或前台/后台运行中）时：

1. `ShortcutObserver` 经 `AppShortcutOption.matchingShortcutURL` 解析 path。
2. 导航 **延迟约 0.45 秒**，等待 SwiftUI 完成挂载。
3. **冷启动**时，URL / Quick Action **优先于** 因 Live Activity 恢复而自动跳转到活跃番茄/计时 Tab。

**motivation** 与 **feedback** 直接打开全屏/Sheet，不会先切换 Tab。

---

## 苹果快捷指令

**打开番茄 Tab**

1. 添加 **打开 URL** 操作
2. URL 填 `iPomodoro://pomodoro`

**专注结束后查看统计**

```
iPomodoro://stats
```

可在个人自动化（例如 Focus 模式结束时）用 **打开 URL** 直达统计 Tab。

---

## 相关：Siri 与 App Shortcuts

内置 **App Shortcuts**（Siri / 快捷指令 App）与 URL 互补：

| Intent | 行为 |
|--------|------|
| 打开番茄 | 切换到番茄 Tab |
| 打开计时 | 切换到计时 Tab |
| 打开统计 | 切换到统计 Tab |
| 今日专注摘要 | 返回今日专注时长与番茄数，**无需打开 App 界面** |

Siri 示例：*「爱番茄今天专注了多久？」*

主屏图标最多显示 4 项快捷操作，在 **设置 → 应用设置 → 主屏快捷操作** 中自选并排顺序。上述 6 个 path 覆盖全部目的地。

---

## 故障排查

| 现象 | 检查 |
|------|------|
| 链接无反应 | 确认已安装 App；path 必须是上述 6 个名称之一 |
| 重开 App 后 Tab 不对 | 若有活跃 Live Activity，**Quick Action / URL 启动优先**于自动恢复切 Tab |
| feedback 只打开邮件 App | 设备未配置邮件账户 — 爱番茄会回退到 `mailto:` |

---

[返回爱番茄支持页](../) &middot; [常见问题](../faq) &middot; [隐私政策](../privacy)

</section>
<section lang="zh-TW" markdown="1">

愛番茄（iPomodoro）支援 **`iPomodoro://`** 與 **`iPomodoros://`** URL Scheme 深度連結——可從 Safari、其他 App、QR Code 或 Apple 捷徑開啟指定 Tab 或應用內頁面。這些 URL 與 **主畫面 Quick Actions**（長按圖示）指向相同目的地。

> **說明：** URL **不會**自動開始/停止計時，也不支援傳入任務 ID 或預填時長，僅用於 App 內導覽。若需不開啟介面即可查詢今日專注，請使用 **Siri App Shortcuts**（見下文 [相關：Siri 與 App Shortcuts](#相關siri-與-app-shortcuts)）。

## 協議規範

```
iPomodoro://<path>
iPomodoros://<path>
```

| 規則 | 說明 |
|------|------|
| **Scheme** | `iPomodoro`（主）· `iPomodoros`（亦支援） |
| **Path** | 單段路徑，**大小寫不敏感** — 從 URL **host** 解析 |
| **查詢參數** | 不支援（若附帶會被忽略） |
| **等同 Quick Action type** | `iPomodoro://<path>`（與主畫面快捷操作註冊字串一致） |

路徑匹配為 segment **精確匹配**，不會用模糊 `contains("pomodoro")` 等方式猜測。

---

## 目的地

| Path | 開啟 | 說明 |
|------|------|------|
| `pomodoro` | **番茄** Tab | 不會自動開始計時 |
| `study` | **計時** Tab | 不會自動開始計時 |
| `tasks` | **定任務** Tab | |
| `stats` | **統計** Tab | |
| `motivation` | **勵志語錄大全** 全螢幕瀏覽 | 與 **設定 → 勵志語錄設定 → 勵志語錄大全** 相同 UI |
| `feedback` | **回饋** Sheet | 優先應用內郵件；不可用則 `mailto:` 回退 |

---

## 範例

**開啟番茄 Tab**

```
iPomodoro://pomodoro
```

**開啟計時 Tab**（備用 scheme）

```
iPomodoros://study
```

**開啟統計儀表板**

```
iPomodoro://stats
```

**展示勵志語錄**

```
iPomodoro://motivation
```

**開啟回饋**

```
iPomodoro://feedback
```

---

## 啟動行為

App 收到 URL（冷啟動或前景/背景執行中）時：

1. `ShortcutObserver` 經 `AppShortcutOption.matchingShortcutURL` 解析 path。
2. 導覽 **延遲約 0.45 秒**，等待 SwiftUI 完成掛載。
3. **冷啟動**時，URL / Quick Action **優先於** 因 Live Activity 恢復而自動跳轉到活躍番茄/計時 Tab。

**motivation** 與 **feedback** 直接開啟全螢幕/Sheet，不會先切換 Tab。

---

## Apple 捷徑

**開啟番茄 Tab**

1. 新增 **打開 URL** 動作
2. URL 填 `iPomodoro://pomodoro`

**專注結束後查看統計**

```
iPomodoro://stats
```

可在個人自動化（例如 Focus 模式結束時）用 **打開 URL** 直達統計 Tab。

---

## 相關：Siri 與 App Shortcuts

內建 **App Shortcuts**（Siri / 捷徑 App）與 URL 互補：

| Intent | 行為 |
|--------|------|
| 開啟番茄 | 切換到番茄 Tab |
| 開啟計時 | 切換到計時 Tab |
| 開啟統計 | 切換到統計 Tab |
| 今日專注摘要 | 回傳今日專注時長與番茄數，**無需開啟 App 介面** |

Siri 範例：*「愛番茄今天專注了多久？」*

主畫面圖示最多顯示 4 項快捷操作，在 **設定 → 應用設定 → 主畫面快捷操作** 中自選並排序。上述 6 個 path 涵蓋全部目的地。

---

## 故障排查

| 現象 | 檢查 |
|------|------|
| 連結無反應 | 確認已安裝 App；path 必須是上述 6 個名稱之一 |
| 重開 App 後 Tab 不對 | 若有活躍 Live Activity，**Quick Action / URL 啟動優先**於自動恢復切 Tab |
| feedback 只開啟郵件 App | 裝置未設定郵件帳戶 — 愛番茄會回退到 `mailto:` |

---

[返回愛番茄支援頁](../) &middot; [常見問題](../faq) &middot; [隱私政策](../privacy)

</section>
<section lang="ja" markdown="1">

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

</section>
<section lang="ko" markdown="1">

iPomodoro 지원 ** `iPomodoro://` ** 및 ** `iPomodoros://` ** URL 계획 딥 링크 — Safari, 다른 앱, QR 코드 또는 Apple Shortcuts에서 탭 또는 인앱 시트를 엽니다. 이 URL은 **Home Screen Quick Actions** (앱 아이콘을 길게 누릅니다)로 이용 가능한 목적지를 미러링합니다.

> **주의:** URL 링크가 ** 시작하거나 타이머를 중지, 작업 ID를 전달, 또는 사전 충전 기간. 앱 내에서만 탐색합니다. 앱을 열지 않고 말한 초점 요약을 위해 **Siri App Shortcuts** ([Related: Siri & App Shortcuts](#related-siri--app-shortcuts) 아래 참조).

## 프로토콜


```
iPomodoro://<path>
iPomodoros://<path>
```


| Rule | 제품 정보 |
|------|--------|
| **Schemes** | `iPomodoro` (primary) · `iPomodoros` (또한 허용) |
| **Path** | 단일 세그먼트,**case-insensitive** — URL에서 해결**host** |
| **Query parameters** | 지원되지 않음 (현재 경우 무시) |
| **Equivalent Quick Action type** | `iPomodoro://<path>` (홈 화면 단축키에 등록된 문자열) |

Path matching is **exact** on the 세그먼트 이름 — 앱은 같은 fuzzy-match substrings하지 않습니다 `iPomodoro://` .

---

## 대상 화면

| Path | Opens | 메모 |
|------|--------|-------|
| `pomodoro` | **Pomodoro** tab | 자동 시작은 없습니다. |
| `study` | **Study Timer** tab | 자동 시작은 없습니다. |
| `tasks` | **Tasks** tab |  |
| `stats` | **Statistics** tab |  |
| `motivation` | **Motivational Quote Anthology** full-screen gallery | 같은 UI ** 설정 → 동기 부여 따옴표 설정 → 동기 부여 따옴표 Anthology** |
| `feedback` | **Feedback** sheet | in-app Mail compose를 사용할 때 사용; `mailto:`로 돌아가십시오. |

---

## 예시

**Open Pomodoro 탭 **


```
iPomodoro://pomodoro
```


**Open Study Timer 탭 ** (단일 계획)


```
iPomodoros://study
```


**Open 통계 대시보드 **


```
iPomodoro://stats
```


** 동기 부여 견적**


```
iPomodoro://motivation
```


**Open 피드백**


```
iPomodoro://feedback
```


---

## Behavior 출시

앱이 URL(cold start or while running)을 수신할 때:

1. `iPomodoro://` 는 `iPomodoros://` 를 통해 길을 해결합니다.
2. 항법은 **deferred ~0.45 s ** 그래서 SwiftUI는 거치를 완료할 수 있습니다.
3.**cold start**, URL / Quick Action takes **priority** over automatically jumping to the active Pomodoro or Study tab from the restored Live Activity session.

**Motivation** 및 **feedback**는 오버레이를 직접 엽니다 — 그들은 탭을 먼저 전환하지 않습니다.

---

## Apple 바로가기

**Open Pomodoro 탭 **

1. 행동 추가 ** URL 열기 **
2. URL: `iPomodoro://` ** 초점 블록 후 통계를 엽니 다 **


```
iPomodoro://stats
```


Use**Open URL** 개인 자동화(예: 포커스 모드 종료 후)에서 대시보드로 이동합니다.

---

## 관련: Siri & 앱 바로가기

내장 ** 앱 단축키 ** (시리 / 단축키 앱) URL 링크 보완 :

| Intent | 채용 정보 |
|--------|----------|
| Open Pomodoro | Pomodoro 탭으로 전환 |
| Open Study Timer | Timer 탭으로 전환 |
| Open Statistics | 통계 탭으로 전환 |
| Today's focus summary | 앱 UI를 필요로 하지 않고 오늘 초점 기간과 pomodoro 카운트를 반환 ** |

예 Siri 구문 : * "어떻게 나는 iPomodoro에서 오늘 집중 했습니까?"*

**Settings → App settings → Home Screen Shortcuts** (주문에 드래그) 아래 홈 화면 아이콘에 4 개의 항목이 나타납니다. 위의 URL 경로는 모든 6개의 가능한 목적지를 커버합니다; 단지 4는 한 번에 아이콘에 나타날 수 있습니다.

---

## 문제 해결

| Issue | 자주 묻는 질문 |
|-------|----------------|
| Link does nothing | 앱을 설치합니다. 경로는 위의 6 이름 중 하나이어야합니다. |
| Wrong tab after reopening | 타이머 라이브 활동이 활성화되면 ** Quick Action / URL 실행 overrides** 자동 탭 복원 |
| `feedback` opens Mail app only | 장치에는 구성된 메일 계정이 없습니다. iPomodoro는 `mailto:`로 돌아갑니다. |

---

[Back to iPomodoro Support](../) &middot; [FAQ](../faq) &middot; [개인정보 보호 정책](../privacy)

</section>
<section lang="ru" markdown="1">

iPomodoro поддерживает ** `iPomodoro://` ** и ** `iPomodoros://` ** Схема URL глубоких ссылок — откройте вкладку или лист в приложении от Safari, другого приложения, QR-кода или ярлыков Apple. Эти URL-адреса отражают пункты назначения, доступные как ** Home Screen Quick Actions** (иконка приложения с длинным нажатием).

> **Примечание: ** URL-ссылки запускают или останавливают таймеры, передают идентификаторы задач или длительность предварительного заполнения. Они перемещаются только внутри приложения. Для резюме разговорной фокусировки без открытия приложения используйте **Siri App Shortcuts** (см. [Связанные: Siri & App Shortcuts] (#related-siri--app-shortcuts) ниже).

## Спецификация протокола


```
iPomodoro://<path>
iPomodoros://<path>
```


| Rule | Подробнее |
|------|--------|
| **Schemes** | «iPomodoro» (первичный) • «iPomodoros» (также принимается) |
| **Path** | Единый сегмент, **case-insensitive** — решен из URL **host** |
| **Query parameters** | Не поддерживается (игнорируется, если присутствует) |
| **Equivalent Quick Action type** | «iPomodoro://<path>» (одна и та же строка зарегистрирована на ярлыках Home Screen) |

Сопоставление маршрута - это * * точное * * на названии сегмента - приложение не имеет нечетких подстрок, таких как `iPomodoro://` .

---

## Назначения

| Path | Opens | Заметки |
|------|--------|-------|
| `pomodoro` | **Pomodoro** tab | Не запускает сеанс автоматически |
| `study` | **Study Timer** tab | Не запускает сеанс автоматически |
| `tasks` | **Tasks** tab |  |
| `stats` | **Statistics** tab |  |
| `motivation` | **Motivational Quote Anthology** full-screen gallery | Тот же пользовательский интерфейс, что и **Настройки → Настройки мотивационных цитат → Антология мотивационных цитат ** |
| `feedback` | **Feedback** sheet | Использует in-app Mail compose, когда он доступен; возвращается к 'mailto:' |

---

## Примеры

** Открытая вкладка Pomodoro**


```
iPomodoro://pomodoro
```


** Закладка таймера открытого исследования** (альтернативная схема)


```
iPomodoros://study
```


** Открытая панель статистики**


```
iPomodoro://stats
```


**Показать мотивационную цитату**


```
iPomodoro://motivation
```


** Открытая обратная связь**


```
iPomodoro://feedback
```


---

## Запуск поведения

Когда приложение получает URL (холодный запуск или во время работы):

1. `iPomodoro://` решает путь через `iPomodoros://` .
2. Навигация ** откладывается ~ 0,45 с**, поэтому SwiftUI может завершить монтаж.
3.На **холодном старте ** URL / Quick Action занимает **приоритет ** над автоматическим переходом на активную вкладку Pomodoro или Study с восстановленной сессии Live Activity.

** Мотивация** и ** обратная связь** открывают наложения напрямую — они не переключают вкладки первыми.

---

## Apple Shortcuts

** Открытая вкладка Pomodoro**

1 Добавить действие ** Открытый URL**
2. URL: `iPomodoro://` ** Открытая статистика после блока фокусировки**


```
iPomodoro://stats
```


Используйте **Открытый URL** в Личной Автоматизации (например, после окончания режима Focus), чтобы перейти прямо на приборную панель.

---

## Разработчик: Siri & App Shortcuts

Встроенные **App Shortcuts** (Siri / Shortcuts app) дополняют URL-ссылки:

| Intent | поведение |
|--------|----------|
| Open Pomodoro | Переход на вкладку Pomodoro |
| Open Study Timer | Переключатели для изучения вкладки Timer |
| Open Statistics | Переход на вкладку Статистика |
| Today's focus summary | Возвращает сегодняшнюю продолжительность фокусировки и количество помидоров ** без необходимости использования пользовательского интерфейса приложения ** |

Пример фразы Siri: «Сколько времени я сосредоточился сегодня в iPomodoro?»

Настройте, какие четыре элемента отображаются на значке «Домой экран» в разделе **Настройки → Настройки приложений → Ярлыки «Домой экран»** (перезагрузите для повторного заказа). Пути URL-адресов выше охватывают все шесть возможных пунктов назначения; только четыре могут появиться на значке сразу.

---

## устранение неполадок

| Issue | Что проверить |
|-------|----------------|
| Link does nothing | Убедитесь, что приложение установлено; путь должен быть одним из шести названий выше. |
| Wrong tab after reopening | Если таймер Live Activity активен, запуск **Quick Action / URL переопределяет ** автозакладку |
| `feedback` opens Mail app only | Устройство не имеет настроенной учетной записи Mail — iPomodoro возвращается к emailto: |

---

[Назад в поддержку iPomodoro] (../) &middot; [FAQ] (../faq) &middot; [Политика конфиденциальности] (../privacy)

</section>
<section lang="th" markdown="1">

iPomodoro รองรับ~ BAR `iPomodoro://` BAR  BAR `iPomodoros://` BAR ~ ที่อยู่ URL วางตําแหน่งเชื่อมโยงแบบลึกไว้ — เปิดแท็บหรือแท็บจากซาฟารี, แอพอีกอัน, รหัส QR หรือปุ่มพิมพ์ลัดของแอปเปิล ที่อยู่ URL เหล่านี้จะสะท้อนไปยังปลายทางที่มีให้ใช้อยู่เป็น ~Home screen expercution ~ (พยายามกดไอคอนโปรแกรมอยู่)

> ** ข้อสังเกต: * ลิงก์ที่อยู่ URL ไม่ทํางาน ** พวกมันแค่นําทางเข้าไปในแอพ สําหรับผลรวมโฟกัสที่พูดโดยไม่ต้องเปิดโปรแกรม, ให้ใช้ -- Siri Apps ทางลัด (ดู [ini & Apps]) ด้านล่างนี้

## การกําหนดโพรโทคอล


```
iPomodoro://<path>
iPomodoros://<path>
```


| Rule | รายละเอียด |
|------|--------|
| **Schemes** | iPomodoro' (เมษายน) ·  `  `  `  ` Po Po Po Po Po Po Po Po Po Po  ( ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) |
| **Path** | สัดส่วนเดียว ความไวต่อความรู้สึก ถูกแก้ไขจากที่อยู่ URL |
| **Query parameters** | ไม่สนับสนุน (หากมีอยู่) |
| **Equivalent Quick Action type** | 'IPomodoro' < path>' (สตริงเดียวกันที่ลงทะเบียนบนทางลัดจอบ้าน) |

พาธที่เข้าคู่กันคือ ~exact] บนชื่อส่วนของเส้นตรง — app ไม่ได้จับคู่ด้วยข้อความย่อยเช่น `iPomodoro://` .

---

## ปลายทาง

| Path | Opens | บันทึก |
|------|--------|-------|
| `pomodoro` | **Pomodoro** tab | ยังไม่ได้เริ่มวาระงานอัตโนมัติ |
| `study` | **Study Timer** tab | ยังไม่ได้เริ่มวาระงานอัตโนมัติ |
| `tasks` | **Tasks** tab |  |
| `stats` | **Statistics** tab |  |
| `motivation` | **Motivational Quote Anthology** full-screen gallery | UI แบบเดียวกันกับ..."การตั้งค่าการอ้างถึงการย้ายถิ่นฐาน |
| `feedback` | **Feedback** sheet | ใช้การเขียนจดหมายแบบบรรจุ- app เมื่อมีให้ใช้; ถอยกลับไปยัง `mailto:' |

---

## ตัวอย่าง

~เปิดแท็บโพโมโดโร~


```
iPomodoro://pomodoro
```


** เปิดทําการจับเวลา **


```
iPomodoros://study
```


~สถิติเปิด! ~


```
iPomodoro://stats
```


~แสดงแรงจูงใจของคําพูด~


```
iPomodoro://motivation
```


~เสียงตอบรับแบบเปิด -- ~


```
iPomodoro://feedback
```


---

## พฤติกรรมการเรียกใช้

เมื่อโปรแกรมได้รับที่อยู่ URL (เริ่มโปรแกรมหรือทํางาน):

1. `iPomodoro://` BAR แก้ไขพาธผ่านทาง `iPomodoros://` BAR
2. การนําร่องคือ ~ป้องกัน ~0.45 s~ ดังนั้นไวฟต์ยูไอสามารถขึ้นได้สําเร็จ
3. On ~ cooled start~, ที่อยู่ URL / ปฏิบัติการด่วน **

** แรงจูงใจ~ และ ** เปิดฝาครอบโดยตรง -- พวกมันไม่สลับที่แท็บก่อน

---

## ปุ่มพิมพ์ลัดของแอปเปิล

~เปิดแท็บโพโมโดโร~

1. เพิ่มการกระทํา... เปิดที่อยู่ URL ~
2. ที่อยู่ URL:   ค.ศ.

~สถิติเปิดหลังจากจุดโฟกัส~


```
iPomodoro://stats
```


ใช้ที่อยู่ URL เปิด * ในระบบอัตโนมัติส่วนตัว (เช่น หลังจบโหมดโฟกัส) เพื่อกระโดดตรงไปที่หน้าปัดของคุณ

---

## เชื่อมโยง: ปุ่มพิมพ์ลัดของ Siri & App

ผสานที่อยู่ URL:

| Intent | พฤติกรรม |
|--------|----------|
| Open Pomodoro | สลับเป็นแท็บโพโมโดโร |
| Open Study Timer | สลับไปยังแท็บตัวจับเวลาสําหรับการศึกษา |
| Open Statistics | สลับไปยังแท็บสถิติ |
| Today's focus summary | กลับมาในช่วงโฟกัสของวันนี้และนับโพโมโดโร -- โดยไม่ต้องเรียกแอพยูไอ! |

ตัวอย่างวลี Seri: *"ฉันเน้นที่ ipomodoro มานานแค่ไหนแล้ว?"

ปรับแต่งว่าจะให้มีรายการใด 4 รายการบนไอคอนหน้าจอหลักที่อยู่ใต้ # ตั้งโปรแกรมโปรแกรม apps apts outta outta outta mographate ~ (ลากเพื่อทําการเรียงใหม่) พาธที่อยู่ URL ด้านบนครอบคลุมไปยังที่หมายทั้งหมด 6 ที่เท่านั้น; จะปรากฏเพียง 4 ที่เท่านั้นบนไอคอนในครั้งเดียว

---

## การยิงปัญหา

| Issue | จะตรวจอะไร |
|-------|----------------|
| Link does nothing | เพื่อให้แน่ใจว่าโปรแกรมได้ถูกติดตั้งแล้ว; พาธต้องเป็นชื่อหนึ่งในหกชื่อที่อยู่ด้านบน |
| Wrong tab after reopening | หากมีกิจกรรมของตัวจับเวลาอยู่ ให้ทําการเรียกใช้งานโปรแกรม * Office/ URL แทนการเรียกคืนแท็บอัตโนมัติ |
| `feedback` opens Mail app only | อุปกรณ์ยังไม่มีการปรับแต่งบัญชีผู้ใช้อีเมล — iPomodoro จะถอยกลับไปยัง `mailto:' |

---

[ย้อนกลับการรองรับ iPomodoro](./) & middot; [FAQ](./figg) & miiddot; [นโยบายความนิยม](./ prinjivancey)

</section>
<section lang="de" markdown="1">

iPomodoro unterstützt ** `iPomodoro://` ** und ** `iPomodoros://` ** URL-Schema Deep Links - Öffnen Sie einen Tab oder In-App-Blatt von Safari, einer anderen App, einem QR-Code oder Apple Shortcuts. Diese URLs spiegeln die verfügbaren Ziele als **Home Screen Quick Actions** wider (langes Drücken des App-Symbols).

> **Hinweis:** URL-Links starten oder stoppen keine Timer, übergeben Aufgaben-IDs oder Vorfülldauern. Sie navigieren nur innerhalb der App. Für gesprochene Fokuszusammenfassungen, ohne die App zu öffnen, verwenden Sie **Siri App Shortcuts** (siehe [Related: Siri & App Shortcuts](#related-siri--app-shortcuts) unten).

## Protokollspezifikation


```
iPomodoro://<path>
iPomodoros://<path>
```


| Rule | Einzelheiten |
|------|--------|
| **Schemes** | `iPomodoro` (primär) · `iPomodoros` (auch akzeptiert) |
| **Path** | Ein einzelnes Segment, **case-unsensitive ** - aufgelöst von der URL **host ** |
| **Query parameters** | Nicht unterstützt (ignoriert, wenn vorhanden) |
| **Equivalent Quick Action type** | `iPomodoro://<path>` (gleicher String auf den Home Screen Shortcuts registriert) |

Pfadmatching ist ** genau ** auf dem segmentnamen - die app hat keine fuzzy-match-substrings wie     c0   .

---

## Ziele

| Path | Opens | Notizen |
|------|--------|-------|
| `pomodoro` | **Pomodoro** tab | Startet eine Sitzung nicht automatisch |
| `study` | **Study Timer** tab | Startet eine Sitzung nicht automatisch |
| `tasks` | **Tasks** tab |  |
| `stats` | **Statistics** tab |  |
| `motivation` | **Motivational Quote Anthology** full-screen gallery | Gleiche Benutzeroberfläche wie ** Einstellungen → Motivational Quote Settings → Motivational Quote Anthology** |
| `feedback` | **Feedback** sheet | Verwendet In-App-Mail-Compose, wenn verfügbar; fällt zurück auf "mailto:" |

---

## Beispiele

** Öffnen Sie Pomodoro Tab**


```
iPomodoro://pomodoro
```


**Open Study Timer Registerkarte** (alternatives Schema)


```
iPomodoros://study
```


**Open Statistics Dashboard**


```
iPomodoro://stats
```


** Zeigen Sie ein Motivationsangebot **


```
iPomodoro://motivation
```


**Offenes Feedback**


```
iPomodoro://feedback
```


---

## Startverhalten

Wenn die App eine URL erhält (Kaltstart oder während des Laufens):

1. `iPomodoro://` löst den Pfad über `iPomodoros://` auf.
2. Navigation ist **aufgeschoben ~ 0,45 s **, so dass SwiftUI die Montage beenden kann.
3. Am **kalten Start ** nimmt eine URL / Quick Action ** Vorrang vor dem automatischen Springen zu einem aktiven Pomodoro- oder Study-Tab aus einer wiederhergestellten Live-Aktivitätssitzung.

**Motivation** und **Feedback** öffnen Overlays direkt – sie wechseln nicht zuerst die Tabs.

---

## Apple Shortcuts

** Öffnen Sie Pomodoro Tab**

1. Aktion hinzufügen **Offene URL**
2. URL: `iPomodoro://` **Open Statistics nach einem Fokusblock**


```
iPomodoro://stats
```


Verwenden Sie **Offene URL** in einer persönlichen Automatisierung (z. B. nach Beendigung eines Fokusmodus), um direkt zu Ihrem Dashboard zu springen.

---

## Related: Siri & App Shortcuts

**App Shortcuts** (Siri / Shortcuts App) ergänzen URL-Links:

| Intent | Verhalten |
|--------|----------|
| Open Pomodoro | Wechsel zu Pomodoro Tab |
| Open Study Timer | Wechsel zum Study Timer Tab |
| Open Statistics | Wechsel zum Register Statistik |
| Today's focus summary | Gibt die heutige Fokusdauer und pomodoro-Anzahl ** zurück, ohne dass die App-Benutzeroberfläche erforderlich ist ** |

Beispiel Siri Satz: *"Wie lange habe ich mich heute in iPomodoro konzentriert?" *

Konfigurieren Sie, welche vier Elemente auf dem Home Screen-Symbol unter **Einstellungen → App-Einstellungen → Home Screen-Verknüpfungen** erscheinen (drag zum Nachbestellen). URL-Pfade oben decken alle sechs möglichen Ziele ab; nur vier können auf dem Symbol gleichzeitig erscheinen.

---

## Fehlerbehebung

| Issue | Was zu überprüfen ist |
|-------|----------------|
| Link does nothing | Stellen Sie sicher, dass die App installiert ist; Pfad muss einer der sechs oben genannten Namen sein |
| Wrong tab after reopening | Wenn ein Timer Live Activity aktiv ist, überschreibt ein ** Quick Action / URL-Start die automatische Tab-Wiederherstellung |
| `feedback` opens Mail app only | Gerät hat kein konfiguriertes Mail-Konto - iPomodoro fällt auf "mailto" zurück: |

---

[Zurück zu iPomodoro Support](../) &middot; [FAQ](../faq) &middot; [Privacy Policy](../privacy]

</section>
<section lang="fr" markdown="1">

iPomodoro prend en charge ** `iPomodoro://` ** et ** `iPomodoros://` ** Les liens profonds du schéma URL — ouvrez un onglet ou une feuille d'application depuis Safari, une autre application, un code QR ou des raccourcis Apple. Ces URL reflètent les destinations disponibles sous la forme de **Home Screen Quick Actions** (cliquez sur l'icône de l'application).

> **Note:** Liens URL ne **pas** timers de démarrage ou d'arrêt, pass IDs de tâches, ou durées de pré-remplissage. Ils naviguent seulement dans l'application. Pour les résumés de focus parlés sans ouvrir l'application, utilisez **Shortcuts d'application Siri** (voir [Related: Siri & App Shortcuts] (#related-siri--app-shortcuts) ci-dessous).

## Spécification du protocole


```
iPomodoro://<path>
iPomodoros://<path>
```


| Rule | Détail |
|------|--------|
| **Schemes** | `iPomodoro` (primaire) · `iPomodoros` (également accepté) |
| **Path** | Segment unique, **insensible** — résolu à partir de l'URL **host** |
| **Query parameters** | Non pris en charge (ignoré si présent) |
| **Equivalent Quick Action type** | `iPomodoro://<path>` (même chaîne enregistrée sur les raccourcis Home Screen) |

La correspondance de chemin est **exacte** sur le nom du segment — l'application ne fait pas de sous-chaînes floues comme `iPomodoro://` .

---

## Destinations

| Path | Opens | Notes |
|------|--------|-------|
| `pomodoro` | **Pomodoro** tab | Ne démarre pas automatiquement une session |
| `study` | **Study Timer** tab | Ne démarre pas automatiquement une session |
| `tasks` | **Tasks** tab |  |
| `stats` | **Statistics** tab |  |
| `motivation` | **Motivational Quote Anthology** full-screen gallery | Même UI que **Paramètres → Paramètres des citations motivationnelles → Anthologie des citations motivationnelles** |
| `feedback` | **Feedback** sheet | Utilisations in-app Mail composer lorsque disponible; tombe à `mailto:` |

---

## Exemples

**Ouvrir l'onglet Pomodoro**


```
iPomodoro://pomodoro
```


**Open Study Timer tab** (système alternatif)


```
iPomodoros://study
```


**Tableau de bord des statistiques ouvertes**


```
iPomodoro://stats
```


**Afficher une citation de motivation**


```
iPomodoro://motivation
```


**Rétroaction ouverte**


```
iPomodoro://feedback
```


---

## Comportement de lancement

Lorsque l'application reçoit une URL (démarrage froid ou en cours d'exécution) :

1. `iPomodoro://` résout le chemin par `iPomodoros://` .
2. La navigation est ** différée ~0.45 s** pour que SwiftUI puisse terminer le montage.
3. Sur **cold start**, une URL / Quick Action prend **priority** au lieu de sauter automatiquement à un onglet actif Pomodoro ou Study d'une session d'activité en direct restaurée.

**Motivation** et **feedback** ouvrir les superpositions directement — ils ne changent pas les onglets d'abord.

---

## Raccourcis des pommes

**Ouvrir l'onglet Pomodoro**

1. Ajouter une action **Ouvrir l'URL**
2. URL : `iPomodoro://` **Ouvrir les statistiques après un bloc de concentration**


```
iPomodoro://stats
```


Utilisez **Ouvrir l'URL** dans une automatisation personnelle (par exemple après la fin d'un mode Focus) pour sauter directement dans votre tableau de bord.

---

## Related: Siri & App Raccourcis

Intégration **Les raccourcis d'application** (application Siri / Raccourcis) complètent les liens URL :

| Intent | Comportement |
|--------|----------|
| Open Pomodoro | Switches vers l'onglet Pomodoro |
| Open Study Timer | Switches to Study Timer tab |
| Open Statistics | Basculer vers l'onglet Statistiques |
| Today's focus summary | Retourne la durée de mise au point et le nombre de pomodoros **sans exiger l'application UI** |

Exemple de phrase Siri : *"Combien de temps ai-je mis aujourd'hui dans iPomodoro?"*

Configurez les quatre éléments qui apparaissent sur l'icône de l'écran d'accueil sous **Paramètres → Paramètres de l'application → Raccourcis de l'écran d'accueil** (gouttez pour réorganiser). Les chemins d'URL ci-dessus couvrent les six destinations possibles; seulement quatre peuvent apparaître sur l'icône à la fois.

---

## Dépannage

| Issue | Quoi vérifier |
|-------|----------------|
| Link does nothing | S'assurer que l'application est installée; chemin doit être l'un des six noms ci-dessus |
| Wrong tab after reopening | Si un timer Live Activity est actif, un **Quick Action / URL lance remplace** auto tab restaurer |
| `feedback` opens Mail app only | Le périphérique n'a pas de compte Mail configuré — iPomodoro revient à `mailto:` |

---

[Retour à iPomodoro Support](../) &middot; [FAQ](../faq) &middot; [Politique de confidentialité](../privacy)

</section>
<section lang="tr" markdown="1">

iPomodoro, ** `iPomodoro://` ** ve ** `iPomodoros://` ** URL planı derin bağlantıları - bir sekme açın veya Safari'den başka bir uygulama, bir QR kodu veya Apple Shortcuts. Bu URL'ler **Home Ekran Hızlı Eylemler ** olarak mevcut olan yerleri yansıtıyor ( Uygulama ikonunu uzun baskı).

> **Not: ** URL bağlantıları ** başlangıç veya zamanlayıcıları durdurmuyor, görev kimliklerini veya önceden teslimat süresini geç. Sadece uygulama içinde dolaşıyorlar. For speak focus summaries without open the app, use **Siri App Shortcuts ** (see [Related: Siri & App Shortcuts] (# related-siri-app-cuts) aşağıda).

## Protokol Doğrulaması


```
iPomodoro://<path>
iPomodoros://<path>
```


| Rule | Detaylı Bilgi |
|------|--------|
| **Schemes** | "iPomodoro" (primary) · "iPomodoros" (ayrıca kabul edildi) |
| **Path** | Single segment, **case-in sensitive** - URL'den çözüldü **host** |
| **Query parameters** | Desteklenen değil (şimdiyse) |
| **Equivalent Quick Action type** | "iPomodoro:<path>" (Ev Ekran kısayollarında kayıtlı bir dize) |

Yol eşleştirmesi ** segment adında - uygulama `iPomodoro://` gibi bulanık olmayan substrings değildir.

---

## Hedefler

| Path | Opens | Notlar |
|------|--------|-------|
| `pomodoro` | **Pomodoro** tab | Bir seans otomatik olarak başlama |
| `study` | **Study Timer** tab | Bir seans otomatik olarak başlama |
| `tasks` | **Tasks** tab |  |
| `stats` | **Statistics** tab |  |
| `motivation` | **Motivational Quote Anthology** full-screen gallery | Aynı UI as **Settings → Motivasyonel Sözlüğü Ayarlar → Motivasyonel Sözlüğü |
| `feedback` | **Feedback** sheet | Mevcut olduğunda Mail'i kullanın; "mailto'ya geri dönün:" |

---

## Örnekler

**Açık Pomodoro sekmesi **


```
iPomodoro://pomodoro
```


**Open Study Timer sekmesi ** (alternate program)


```
iPomodoros://study
```


**Açık İstatistikler paneli**


```
iPomodoro://stats
```


**Bir motivasyon alıntısını göster**


```
iPomodoro://motivation
```


**Open feedback**


```
iPomodoro://feedback
```


---

## Başlangıç Davranışları

Uygulama bir URL aldığında (cold start or while running):

1. `iPomodoro://` , yolu `iPomodoros://` ile çözer.
2. Navigation **dedilmiş ~0.45 s** bu yüzden SwiftUI monte edilebilir.
3. **cold start**, bir URL / Hızlı Eylem **priority** otomatik olarak restore edilmiş bir Canlı Aktivite seansından aktif bir Pomodoro veya Çalışma sekmesine atlamak.

**Motivation** ve ** feedback** doğrudan açılır - ilk önce sekmeleri değiştirmezler.

---

## Apple Shortcuts

**Açık Pomodoro sekmesi **

1. Hareket ekleyin **Open URL**
2. URL: `iPomodoro://` **Open Statistics after a focus block**


```
iPomodoro://stats
```


Use **Open URL ** in a Personal Automation (e.g. after a Focus mode end) doğrudan paniğe atlamak için.

---

## İlgili: Siri & App Shortcuts

Yerleşik **App Shortcuts** (Siri / Kısakes uygulama) URL bağlantılarını tamamlamak:

| Intent | Davranış Davranış |
|--------|----------|
| Open Pomodoro | Pomodoro sekmesine Anahtarlar |
| Open Study Timer | Zamanlayıcı sekmesine Anahtarlar |
| Open Statistics | İstatistikler sekmesine Anahtarlar |
| Today's focus summary | Bugünün odak süresi ve pomodoro sayısı ** Uygulamayı gerektirmez ** |

Örnek Siri cümlesi: *"Bugün iPomodoro'da ne kadar süre odaklandığımı?*

Home Ekran simgesinde hangi dört öğenin ortaya çıktığını yapılandırın **Settings → App ayarları → Ev Ekran kısayolları ** (drag to reorder). Yukarıdaki URL yolları tüm altı olası destinasyonları kapsar; sadece dört tanesi bir anda ikonda görünebilir.

---

## Sorun Giderme

| Issue | Ne kontrol edecek |
|-------|----------------|
| Link does nothing | Uygulamanın yüklenmesini sağlamak; yol yukarıdaki altı isimden biri olmalıdır |
| Wrong tab after reopening | Bir zamanlayıcı Canlı Aktivite aktifse, a **Quick Action / URL lansmanı overrides ** otomatik sekme geri yükleme |
| `feedback` opens Mail app only | Cihazın yapılandırılmış bir Mail hesabı yoktur - iPomodoro "mailto:" |

---

[Back to iPomodoro Support](./) &middot; [FAQ](./faq) &middot; [Privacy Policy](./privacy)

</section>
