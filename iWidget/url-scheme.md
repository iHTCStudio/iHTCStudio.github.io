---
layout: doc
title: iWidget — URL Scheme Reference
app_id: iWidget
doc_title_en: URL Scheme Reference
doc_title_zh_cn: URL Scheme 说明
doc_title_zh_tw: URL Scheme 說明
description: iwidget:// deep links — Today, Library, My Widgets, editor, import, membership, day detail, and Settings.
---

<section lang="en" markdown="1">

iWidget supports the **`iwidget://`** URL scheme on **iPhone, iPad, and Mac**. Use it in **Safari**, **Apple Shortcuts**, another app, or a QR code to jump into the main app.

For spoken lunar or festival answers **without** opening the app, use **Siri App Shortcuts** (see [FAQ](../faq)). To ask whether a date is a workday, add the separate **Workday** App Intent in Shortcuts — it is not a URL.

## Format

```
iwidget://<host>[?query]
```

| Rule | Detail |
|------|--------|
| **Scheme** | `iwidget` (lowercase) |
| **Host** | See the table below |
| **Query** | Optional; only documented keys are read |

Unknown hosts are ignored safely.

---

## Hosts

| Host | Opens | Query |
|------|--------|-------|
| `today` | **Today** | — |
| `day` | **Today**, then **day detail** | **`y`** year · **`m`** month · **`d`** day |
| `library` | **Widget Library** | **`preset=`** or **`set=`** scrolls to that set; **`detail=1`** opens the set page |
| `mine` | **My Widgets** | **`design=`** or **`id=`** a saved UUID; **`preset=`** / **`set=`** the latest copy of that template |
| `editor` | **Editor** | **`design=`** or **`id=`** opens that saved design; omit to open the most recent one |
| `import` | **My Widgets** and the import picker | — |
| `settings` | **Settings** | **`scroll=festivals`** · **`weather`** · **`editor`** · **`access`** |
| `membership` | **Membership** | paused Home, Lock Screen, and shortcut-launch widgets open this |
| `launch` | Used when a launch block hands off to the app (**iOS**) | provided by the widget |

If `day` values are missing or invalid, the app still switches to Today. If a `design` UUID is missing, **My Widgets** stays in view. If there is no saved design, `editor` opens the library.

---

## Examples

**Open Today**

```
iwidget://today
```

**Open 1 January 2026**

```
iwidget://day?y=2026&m=1&d=1
```

**Open a library set**

```
iwidget://library?set=small.calendar&detail=1
```

**Open the latest copy of a template**

```
iwidget://mine?preset=small.weather
```

**Open Settings → weather**

```
iwidget://settings?scroll=weather
```

**Open Membership**

```
iwidget://membership
```

---

## Widget & Control Center

- Tapping a Home Screen board when **tap shield** is off may open Today, or follow the open behavior you set.
- **Lock Screen** and **Control Center** use App Intents. The Control Center **latest design** button opens the editor for that design.
- The **Mac menu bar** calendar uses the same `day` URL when you click a date.

---

## Shortcuts tips

1. Add **Open URL** and paste an `iwidget://` link.
2. For **Workday** checks, search Shortcuts for iWidget’s work/rest action and supply a date.

[Back to iWidget Support](../) · [FAQ](../faq) · [Membership](../membership) · [Privacy Policy](../privacy)

</section>
<section lang="zh-CN" markdown="1">

爱组件支持 **`iwidget://`** URL Scheme，适用于 **iPhone、iPad 与 Mac**。可在 **Safari**、**快捷指令**、其他应用或二维码中打开主 App。

若要在 **不打开 App** 的情况下语音查询农历或节日，请用 **Siri App 快捷指令**（见 [常见问题](../faq)）。查询 **某日是否上班** 请在快捷指令中添加独立的 **是否上班** App Intent，不能用 URL 代替。

## 格式

```
iwidget://<host>[?query]
```

| 规则 | 说明 |
|------|------|
| **Scheme** | `iwidget`（小写） |
| **Host** | 见下表 |
| **Query** | 可选；仅读取文档中的键 |

未知 host 会被安全忽略。

---

## Host 列表

| Host | 打开 | Query |
|------|------|-------|
| `today` | **今日** | — |
| `day` | **今日**，并打开 **日详情** | **`y`** 年 · **`m`** 月 · **`d`** 日 |
| `library` | **组件库** | **`preset=`** 或 **`set=`** 滚动到该套；**`detail=1`** 打开详情 |
| `mine` | **我的组件** | **`design=`** 或 **`id=`** 已保存 UUID；**`preset=`** / **`set=`** 该模板最近一份副本 |
| `editor` | **编辑器** | **`design=`** 或 **`id=`** 打开该设计；省略则打开最近编辑的一份 |
| `import` | **我的组件** 并弹出导入 | — |
| `settings` | **设置** | **`scroll=festivals`** · **`weather`** · **`editor`** · **`access`** |
| `membership` | **会员说明** | 已暂停的桌面、锁屏与快捷启动组件会打开此项 |
| `launch` | 启动积木回落到 App 时使用（**仅 iOS**） | 由小组件提供 |

`day` 参数缺失或无效时，仍会切到今日。找不到指定 `design` 时留在 **我的组件**。没有已保存设计时，`editor` 会打开组件库。

---

## 示例

**打开今日**

```
iwidget://today
```

**打开 2026 年 1 月 1 日**

```
iwidget://day?y=2026&m=1&d=1
```

**打开组件库某一套**

```
iwidget://library?set=small.calendar&detail=1
```

**打开某套模板最近的副本**

```
iwidget://mine?preset=small.weather
```

**打开设置 → 天气**

```
iwidget://settings?scroll=weather
```

**打开会员页**

```
iwidget://membership
```

---

## 小组件与控制中心

- 主屏看板在未开启 **误触拦截** 时，点按可能打开今日，或跟随你设置的打开方式。
- **锁屏** 与 **控制中心** 使用 App Intents。控制中心的 **最近设计** 会打开该设计的编辑器。
- **Mac 菜单栏** 月历点某一天时，使用同样的 `day` 链接。

---

## 快捷指令提示

1. 添加 **打开 URL**，粘贴 `iwidget://` 链接。
2. 查询是否上班时，在快捷指令动作库中搜索爱组件的休班 Intent，并提供日期。

[返回爱组件支持页](../) · [常见问题](../faq) · [会员说明](../membership) · [隐私政策](../privacy)

</section>
<section lang="zh-TW" markdown="1">

愛組件支援 **`iwidget://`** URL Scheme，適用於 **iPhone、iPad 與 Mac**。可在 **Safari**、**捷徑**、其他 App 或 QR 中打開主 App。

若要在 **不打開 App** 的情況下語音查詢農曆或節日，請用 **Siri App 捷徑**（見 [常見問題](../faq)）。查詢 **某日是否上班** 請在捷徑中加入獨立的 **是否上班** App Intent，不能用 URL 代替。

## 格式

```
iwidget://<host>[?query]
```

| 規則 | 說明 |
|------|------|
| **Scheme** | `iwidget`（小寫） |
| **Host** | 見下表 |
| **Query** | 可選；僅讀取文件中的鍵 |

未知 host 會被安全忽略。

---

## Host 列表

| Host | 打開 | Query |
|------|------|-------|
| `today` | **今日** | — |
| `day` | **今日**，並打開 **日詳情** | **`y`** 年 · **`m`** 月 · **`d`** 日 |
| `library` | **組件庫** | **`preset=`** 或 **`set=`** 捲動到該套；**`detail=1`** 打開詳情 |
| `mine` | **我的組件** | **`design=`** 或 **`id=`** 已儲存 UUID；**`preset=`** / **`set=`** 該範本最近一份副本 |
| `editor` | **編輯器** | **`design=`** 或 **`id=`** 打開該設計；省略則打開最近編輯的一份 |
| `import` | **我的組件** 並跳出匯入 | — |
| `settings` | **設定** | **`scroll=festivals`** · **`weather`** · **`editor`** · **`access`** |
| `membership` | **會員說明** | 已暫停的桌面、鎖屏與捷徑啟動組件會開啟此項 |
| `launch` | 啟動積木回落到 App 時使用（**僅 iOS**） | 由小工具提供 |

`day` 參數缺失或無效時，仍會切到今日。找不到指定 `design` 時留在 **我的組件**。沒有已儲存設計時，`editor` 會打開組件庫。

---

## 示例

**打開今日**

```
iwidget://today
```

**打開 2026 年 1 月 1 日**

```
iwidget://day?y=2026&m=1&d=1
```

**打開組件庫某一套**

```
iwidget://library?set=small.calendar&detail=1
```

**打開某套範本最近的副本**

```
iwidget://mine?preset=small.weather
```

**打開設定 → 天氣**

```
iwidget://settings?scroll=weather
```

**打開會員頁**

```
iwidget://membership
```

---

## 小工具與控制中心

- 主畫面看板在未開啟 **誤觸攔截** 時，點按可能打開今日，或跟隨你設定的打開方式。
- **鎖定畫面** 與 **控制中心** 使用 App Intents。控制中心的 **最近設計** 會打開該設計的編輯器。
- **Mac 選單列** 月曆點某一天時，使用同樣的 `day` 連結。

---

## 捷徑提示

1. 加入 **打開 URL**，貼上 `iwidget://` 連結。
2. 查詢是否上班時，在捷徑動作庫中搜尋愛組件的休班 Intent，並提供日期。

[返回愛組件支援頁](../) · [常見問題](../faq) · [會員說明](../membership) · [隱私政策](../privacy)

</section>
<section lang="ja" markdown="1">

iWidget は **iPhone / iPad / Mac** で **`iwidget://`** を扱います。Safari、ショートカット、他アプリ、QR から開けます。音声だけの旧暦／祝日は Siri。出勤確認は Shortcuts の Workday Intent（URL ではありません）。

## 形式

`iwidget://<host>[?query]` — 未知の host は無視されます。

| Host | 開く | Query |
|------|------|-------|
| `today` | 今日 | — |
| `day` | 今日 → 日詳細 | `y` `m` `d` |
| `library` | ライブラリ | `preset=` / `set=`、`detail=1` |
| `mine` | マイウィジェット | `design=` / `id=`、`preset=` / `set=` |
| `editor` | エディタ | `design=` / `id=`（省略で最近） |
| `import` | 読み込み | — |
| `settings` | 設定 | `scroll=festivals` · `weather` · `editor` · `access` |
| `membership` | メンバーシップ | ロック中のウィジェットが開く |
| `launch` | 起動ブロックのハンドオフ（iOS） | ウィジェットが付与 |

例：`iwidget://today` · `iwidget://library?set=small.calendar&detail=1` · `iwidget://membership`

[サポートへ戻る](../) · [FAQ](../faq) · [メンバーシップ](../membership) · [プライバシー](../privacy)

</section>
<section lang="ko" markdown="1">

iWidget는 **iPhone / iPad / Mac**에서 **`iwidget://`**를 지원합니다. Safari, 단축어, 다른 앱, QR로 열 수 있습니다. 음성만으로 음력/명절을 물을 때는 Siri. 근무일 확인은 Shortcuts의 Workday Intent입니다.

`iwidget://<host>[?query]` — 알 수 없는 host는 무시됩니다.

| Host | 열기 | Query |
|------|------|-------|
| `today` | 오늘 | — |
| `day` | 오늘 → 일 상세 | `y` `m` `d` |
| `library` | 라이브러리 | `preset=` / `set=`, `detail=1` |
| `mine` | 내 위젯 | `design=` / `id=`, `preset=` / `set=` |
| `editor` | 편집기 | `design=` / `id=` (없으면 최근) |
| `import` | 가져오기 | — |
| `settings` | 설정 | `scroll=festivals` · `weather` · `editor` · `access` |
| `membership` | 멤버십 | 일시 정지된 위젯이 엽니다 |
| `launch` | 실행 블록 핸드오프 (iOS) | 위젯이 제공 |

예: `iwidget://today` · `iwidget://library?set=small.calendar&detail=1` · `iwidget://membership`

[지원으로](../) · [FAQ](../faq) · [멤버십](../membership) · [개인정보](../privacy)

</section>
<section lang="ru" markdown="1">

iWidget понимает **`iwidget://`** на **iPhone, iPad и Mac**. Safari, «Команды», другое приложение или QR. Голосовой лунный календарь без открытия приложения — Siri. Рабочий день — отдельный Workday Intent, не URL.

`iwidget://<host>[?query]` — неизвестные host игнорируются.

| Host | Открывает | Query |
|------|-----------|-------|
| `today` | Сегодня | — |
| `day` | Сегодня → день | `y` `m` `d` |
| `library` | Библиотека | `preset=` / `set=`, `detail=1` |
| `mine` | Мои виджеты | `design=` / `id=`, `preset=` / `set=` |
| `editor` | Редактор | `design=` / `id=` (иначе последний) |
| `import` | Импорт | — |
| `settings` | Настройки | `scroll=festivals` · `weather` · `editor` · `access` |
| `membership` | Членство | приостановленные виджеты открывают это |
| `launch` | Handoff ярлыка (iOS) | от виджета |

Примеры: `iwidget://today` · `iwidget://library?set=small.calendar&detail=1` · `iwidget://membership`

[К поддержке](../) · [FAQ](../faq) · [Членство](../membership) · [Конфиденциальность](../privacy)

</section>
<section lang="th" markdown="1">

iWidget รองรับ **`iwidget://`** บน **iPhone, iPad และ Mac** ใช้ใน Safari คำสั่งลัด แอปอื่น หรือ QR คำถามปฏิทินจันทรคติด้วยเสียงโดยไม่เปิดแอปใช้ Siri วันทำงานใช้ Workday Intent ไม่ใช่ URL

`iwidget://<host>[?query]` — host ที่ไม่รู้จักจะถูกละเว้น

| Host | เปิด | Query |
|------|------|-------|
| `today` | วันนี้ | — |
| `day` | วันนี้ → รายวัน | `y` `m` `d` |
| `library` | คลัง | `preset=` / `set=`, `detail=1` |
| `mine` | วิดเจ็ตของฉัน | `design=` / `id=`, `preset=` / `set=` |
| `editor` | ตัวแก้ไข | `design=` / `id=` (ไม่ระบุ = ล่าสุด) |
| `import` | นำเข้า | — |
| `settings` | การตั้งค่า | `scroll=festivals` · `weather` · `editor` · `access` |
| `membership` | สมาชิก | วิดเจ็ตที่หยุดชั่วคราวจะเปิดลิงก์นี้ |
| `launch` | ส่งต่อจากบล็อกทางลัด (iOS) | จากวิดเจ็ต |

ตัวอย่าง: `iwidget://today` · `iwidget://library?set=small.calendar&detail=1` · `iwidget://membership`

[กลับหน้าสนับสนุน](../) · [FAQ](../faq) · [สมาชิก](../membership) · [ความเป็นส่วนตัว](../privacy)

</section>
<section lang="de" markdown="1">

iWidget versteht **`iwidget://`** auf **iPhone, iPad und Mac**. Nutzen Sie Safari, Kurzbefehle, andere Apps oder einen QR-Code. Gesprochene Mond-/Festtage ohne App-Start: Siri. Werktag: separates Workday-Intent, keine URL.

`iwidget://<host>[?query]` — unbekannte Hosts werden ignoriert.

| Host | Öffnet | Query |
|------|--------|-------|
| `today` | Heute | — |
| `day` | Heute → Tagesdetail | `y` `m` `d` |
| `library` | Bibliothek | `preset=` / `set=`, `detail=1` |
| `mine` | Meine Widgets | `design=` / `id=`, `preset=` / `set=` |
| `editor` | Editor | `design=` / `id=` (sonst zuletzt) |
| `import` | Import | — |
| `settings` | Einstellungen | `scroll=festivals` · `weather` · `editor` · `access` |
| `membership` | Mitgliedschaft | pausierte Widgets öffnen dies |
| `launch` | Starter-Handoff (iOS) | vom Widget |

Beispiele: `iwidget://today` · `iwidget://library?set=small.calendar&detail=1` · `iwidget://membership`

[Zurück zum Support](../) · [FAQ](../faq) · [Mitgliedschaft](../membership) · [Datenschutz](../privacy)

</section>
<section lang="fr" markdown="1">

iWidget prend en charge **`iwidget://`** sur **iPhone, iPad et Mac**. Safari, Raccourcis, une autre app ou un QR. Pour la lune / les fêtes à la voix sans ouvrir l’app : Siri. Jour ouvré : intent Workday, pas une URL.

`iwidget://<host>[?query]` — les hôtes inconnus sont ignorés.

| Host | Ouvre | Query |
|------|-------|-------|
| `today` | Aujourd’hui | — |
| `day` | Aujourd’hui → détail du jour | `y` `m` `d` |
| `library` | Bibliothèque | `preset=` / `set=`, `detail=1` |
| `mine` | Mes widgets | `design=` / `id=`, `preset=` / `set=` |
| `editor` | Éditeur | `design=` / `id=` (sinon le plus récent) |
| `import` | Import | — |
| `settings` | Réglages | `scroll=festivals` · `weather` · `editor` · `access` |
| `membership` | Adhésion | les widgets en pause ouvrent ceci |
| `launch` | Handoff d’un lanceur (iOS) | fourni par le widget |

Exemples : `iwidget://today` · `iwidget://library?set=small.calendar&detail=1` · `iwidget://membership`

[Retour au support](../) · [FAQ](../faq) · [Adhésion](../membership) · [Confidentialité](../privacy)

</section>
<section lang="tr" markdown="1">

iWidget, **iPhone, iPad ve Mac** üzerinde **`iwidget://`** kullanır. Safari, Kısayollar, başka bir uygulama veya QR. Uygulamayı açmadan ay/tatil sorusu için Siri. İş günü için ayrı Workday intent; URL değildir.

`iwidget://<host>[?query]` — bilinmeyen host yok sayılır.

| Host | Açar | Query |
|------|------|-------|
| `today` | Bugün | — |
| `day` | Bugün → gün ayrıntısı | `y` `m` `d` |
| `library` | Kitaplık | `preset=` / `set=`, `detail=1` |
| `mine` | Widget’larım | `design=` / `id=`, `preset=` / `set=` |
| `editor` | Düzenleyici | `design=` / `id=` (yoksa en son) |
| `import` | İçe aktarma | — |
| `settings` | Ayarlar | `scroll=festivals` · `weather` · `editor` · `access` |
| `membership` | Üyelik | duraklatılmış widget’lar bunu açar |
| `launch` | Kısayol handoff (iOS) | widget sağlar |

Örnekler: `iwidget://today` · `iwidget://library?set=small.calendar&detail=1` · `iwidget://membership`

[Desteğe dön](../) · [FAQ](../faq) · [Üyelik](../membership) · [Gizlilik](../privacy)

</section>
