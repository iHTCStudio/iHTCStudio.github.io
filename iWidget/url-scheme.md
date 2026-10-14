---
layout: doc
title: iWidget — URL Scheme Reference
app_id: iWidget
doc_title_en: URL Scheme Reference
doc_title_zh_cn: URL Scheme 说明
doc_title_zh_tw: URL Scheme 說明
description: iwidget:// deep links — open Today, a specific day, or Settings festival filters from Safari, Shortcuts, or other apps.
---

<section lang="en" markdown="1">

iWidget supports the **`iwidget://`** URL scheme on **iPhone, iPad, and Mac**. Use it in **Safari**, **Apple Shortcuts**, another app, or a QR code to jump into the main app. These links **navigate only** — they do not pass widget design IDs or edit board layouts.

For spoken lunar / festival answers **without** opening the app, use **Siri App Shortcuts** (see [FAQ](../faq) → Siri). For **work/rest on a date**, add the separate **Workday** App Intent in Shortcuts.

## Format

```
iwidget://<host>[?query]
```

| Rule | Detail |
|------|--------|
| **Scheme** | `iwidget` (lowercase) |
| **Host** | Path segment — see table below |
| **Query** | Optional; only documented keys are read |

Unknown hosts are ignored safely (no crash).

---

## Hosts

| Host | Opens | Query |
|------|--------|-------|
| `today` | **Today** tab | — |
| `day` | **Today** tab and queues **day detail** for the given date | **`y`** year · **`m`** month · **`d`** day (integers) |
| `settings` | **Settings** tab | **`scroll=festivals`** scrolls to festival filter section |

If `day` query values are missing or invalid, the app still switches to Today without opening a day sheet.

---

## Examples

**Open Today**

```
iwidget://today
```

**Open 1 January 2026 detail**

```
iwidget://day?y=2026&m=1&d=1
```

**Open Settings → festival filters**

```
iwidget://settings?scroll=festivals
```

---

## Widget & Control Center behavior

- Tapping a **home-screen board** when **intercept taps** is off may open `iwidget://today` (or your configured open behavior via widget intent).
- **Lock Screen** and **Control Center** entries use App Intents; they are not additional URL hosts.
- **Mac menu bar** calendar uses the same `day` URL pattern when you click a date.

---

## Shortcuts tips

1. Add **Open URL** and paste an `iwidget://` link.
2. For **Workday** checks, search the Shortcuts action library for iWidget’s **work/rest day** intent and supply a date — it is **not** available as a URL query.

[Back to iWidget Support](../) · [FAQ](../faq) · [Privacy Policy](../privacy)

</section>
<section lang="zh-CN" markdown="1">

爱组件支持 **`iwidget://`** URL Scheme，适用于 **iPhone、iPad 与 Mac**。可在 **Safari**、**快捷指令**、其他应用或二维码中打开主 App。链接 **仅用于导航**，不会传递小组件设计 ID 或编辑看板布局。

若要在 **不打开 App** 的情况下语音查询农历/节日，请用 **Siri App 快捷指令**（见 [常见问题](../faq)）。查询 **某日是否上班** 请在快捷指令中添加独立的 **是否上班** App Intent，**不能**用 URL 参数代替。

## 格式

```
iwidget://<host>[?query]
```

| 规则 | 说明 |
|------|------|
| **Scheme** | `iwidget`（小写） |
| **Host** | 路径段 — 见下表 |
| **Query** | 可选；仅读取文档中的键 |

未知 host 会被安全忽略（不会崩溃）。

---

## Host 列表

| Host | 打开 | Query |
|------|------|-------|
| `today` | **今日** 标签 | — |
| `day` | **今日** 并排队 **日详情** | **`y`** 年 · **`m`** 月 · **`d`** 日（整数） |
| `settings` | **设置** 标签 | **`scroll=festivals`** 滚动到节日筛选区 |

`day` 参数缺失或无效时，仍会切到今日，但不打开日详情。

---

## 示例

**打开今日**

```
iwidget://today
```

**打开 2026 年 1 月 1 日日详情**

```
iwidget://day?y=2026&m=1&d=1
```

**打开设置 → 节日筛选**

```
iwidget://settings?scroll=festivals
```

---

## 小组件与控制中心

- **主屏看板** 在未开启 **拦截跳转** 时，点按可能打开 `iwidget://today`（或你在小组件 Intent 里配置的打开方式）。
- **锁屏** 与 **控制中心** 使用 App Intent，不是额外的 URL host。
- **Mac 菜单栏** 月历点日期时使用相同的 `day` URL。

---

## 快捷指令提示

1. 添加 **打开 URL**，粘贴 `iwidget://` 链接。
2. **是否上班** 请在动作库搜索爱组件对应 Intent 并传入日期 — **没有** URL 形式。

[返回爱组件支持页](../) · [常见问题](../faq) · [隐私政策](../privacy)

</section>
<section lang="zh-TW" markdown="1">

愛組件支援 **`iwidget://`** URL Scheme，適用於 **iPhone、iPad 與 Mac**。可在 **Safari**、**捷徑**、其他 App 或 QR Code 中開啟主 App。連結 **僅用於導覽**，不會傳遞小工具設計 ID 或編輯看板版面。

若要在 **不開啟 App** 的情況下語音查詢農曆/節日，請用 **Siri App 捷徑**（見 [常見問題](../faq)）。查詢 **某日是否上班** 請在捷徑中新增獨立的 **是否上班** App Intent，**不能**用 URL 參數代替。

## 格式

```
iwidget://<host>[?query]
```

| 規則 | 說明 |
|------|------|
| **Scheme** | `iwidget`（小寫） |
| **Host** | 路徑段 — 見下表 |
| **Query** | 可選；僅讀取文件中的鍵 |

未知 host 會被安全忽略（不會當機）。

---

## Host 列表

| Host | 開啟 | Query |
|------|------|-------|
| `today` | **今日** 標籤 | — |
| `day` | **今日** 並排隊 **日詳情** | **`y`** 年 · **`m`** 月 · **`d`** 日（整數） |
| `settings` | **設定** 標籤 | **`scroll=festivals`** 捲動到節日篩選區 |

`day` 參數缺失或無效時，仍會切到今日，但不開啟日詳情。

---

## 示例

**開啟今日**

```
iwidget://today
```

**開啟 2026 年 1 月 1 日日詳情**

```
iwidget://day?y=2026&m=1&d=1
```

**開啟設定 → 節日篩選**

```
iwidget://settings?scroll=festivals
```

---

## 小工具與控制中心

- **主畫面看板** 在未開啟 **攔截跳轉** 時，點按可能開啟 `iwidget://today`（或你在小工具 Intent 裡設定的開啟方式）。
- **鎖定畫面** 與 **控制中心** 使用 App Intent，不是額外的 URL host。
- **Mac 選單列** 月曆點日期時使用相同的 `day` URL。

---

## 捷徑提示

1. 新增 **開啟 URL**，貼上 `iwidget://` 連結。
2. **是否上班** 請在動作庫搜尋愛組件對應 Intent 並傳入日期 — **沒有** URL 形式。

[返回愛組件支援頁](../) · [常見問題](../faq) · [隱私政策](../privacy)

</section>
<section lang="ja" markdown="1">

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

</section>
<section lang="ko" markdown="1">

iWidget은 ** `iwidget://` ** URL 계획 **iPhone, iPad 및 Mac**을 지원합니다. **Safari**, **Apple Shortcuts**, 또 다른 앱, 또는 QR 코드를 사용하여 메인 앱으로 이동합니다. 이 링크 **navigate 만 ** - 그들은 위젯 디자인 ID를 통과하지 않거나 보드 레이아웃을 편집합니다.

lunar / festival Answer **** 앱 열기, **Siri App Shortcuts** ([FAQ](../faq) → Siri). **일에서 작업/걸기 **, 별도의 **일** App Intent in Shortcuts를 추가합니다.

## 지원하다


```
iwidget://<host>[?query]
```


| Rule | 제품 정보 |
|------|--------|
| **Scheme** | `iwidget`(저장) |
| **Host** | Path 세그먼트 - 아래 표 참조 |
| **Query** | 선택 사항; 만 문서 키는 읽기 |

알 수없는 호스트는 안전하게 무시됩니다 (무한 충돌 없음).

---

## 이름 *

| Host | Opens | 글쓰기 |
|------|--------|-------|
| `today` | **Today** tab | — |
| `day` | **Today** tab and queues **day detail** for the given date | **`y`** year · **`m'** month · **`d`** day (integers) |
| `settings` | **Settings** tab | **`scroll=festivals`** 축제 필터 섹션에 스크롤 | `iwidget://` 쿼리 값이 누락되거나 잘못된 경우, 하루 시트를 열지 않고 오늘에 앱이 여전히 전환됩니다.

---

## 예시

**영업일**


```
iwidget://today
```


**1월 2026일 오픈 **


```
iwidget://day?y=2026&m=1&d=1
```


**설정 → 축제 필터 열기 **


```
iwidget://settings?scroll=festivals
```


---

## Widget 및 제어 센터 행동

- **home-screen board** when**intercept tap**는 `iwidget://today`(또는 위젯 intent를 통해 설정된 오픈 동작)를 열 수 있습니다.
- **Lock Screen** 및 **Control Center** 항목 사용 App Intents; 그들은 추가 URL 호스트가 아닙니다.
- **Mac 메뉴 바 ** 캘린더는 날짜를 클릭 할 때 같은 `일` URL 패턴을 사용합니다.

---

## 단축키 팁

1. 추가 ** URL** 및 붙여넣기 `iwidget://` 링크.
2. ** Workday** 체크를 위해, iWidget의 **work/rest day**를 위한 Shortcuts 액션 라이브러리를 검색하고 날짜를 공급합니다. ** URL 쿼리로 사용할 수 없습니다.

[Back to iWidget Support](../) · [FAQ](../faq) · [개인정보 보호정책](../privacy)

</section>
<section lang="ru" markdown="1">

iWidget поддерживает схему URL ** `iwidget://` ** на **iPhone, iPad и Mac**. Используйте его в **Safari**, **Apple Shortcuts**, другом приложении или QR-коде, чтобы перейти в основное приложение. Эти ссылки ** перемещаются только ** — они не передают идентификаторы дизайна виджетов или макеты досок редактирования.

Для устных лунных / фестивальных ответов ** без ** открытия приложения используйте **Siri App Shortcuts** (см. [FAQ](../faq) → Siri). Для **work/rest на дату ** добавьте отдельное **Workday** App Intent in Shortcuts.

## Формат


```
iwidget://<host>[?query]
```


| Rule | Подробнее |
|------|--------|
| **Scheme** | "iwidget" (нижний регистр) |
| **Host** | Сегмент пути - см. таблицу ниже |
| **Query** | Необязательно; читаются только задокументированные ключи |

Неизвестные хосты игнорируются безопасно (без аварий).

---

## Ведущие

| Host | Opens | Запрос |
|------|--------|-------|
| `today` | **Today** tab | — |
| `day` | **Today** tab and queues **day detail** for the given date | **'y'** year **'m'** month **'d'** day (интеграторы) |
| `settings` | **Settings** tab | **'scroll=festivals'** свитки к секции фестивального фильтра |

Если значения запроса `iwidget://` отсутствуют или недействительны, приложение по-прежнему переключается на Today без открытия дневного листа.

---

## Примеры

** Открыто сегодня**


```
iwidget://today
```


** Открыт 1 января 2026 г. Подробнее**


```
iwidget://day?y=2026&m=1&d=1
```


** Открытые настройки, фестивальные фильтры**


```
iwidget://settings?scroll=festivals
```


---

## Поведение Widget & Control Center

- Нажатие ** домашней экранной доски **, когда ** перехваченные краны ** выключены, может открыть «iwidget://today» (или ваше настроенное открытое поведение через намерение виджета).
- ** Записи на экране блокировки ** и ** Центр управления ** используют App Intents; они не являются дополнительными URL-хостами.
- **Календарь меню Mac** использует тот же шаблон URL-адреса «день», когда вы нажимаете дату.

---

## Короткие подсказки

1. Добавить ** Открытый URL** и вставить ссылку `iwidget://` .
2. Для проверки **Workday** ищите в библиотеке действий Shortcuts намерение iWidget **work/rest day** и указывайте дату — она **не** доступна в качестве запроса URL.

[Назад в поддержку iWidget] (../) · [FAQ] (../faq) · [Политика конфиденциальности] (../privacy)

</section>
<section lang="th" markdown="1">

iWidget รองรับโปรแกรม ~ BAR `iwidget://` BAR ~ รูปแบบที่อยู่ URL บน ~ โทรศัพท์, iPad และ Mac~. ใช้มันใน ~ ซาฟารี~~ ~ทางลัด ~, แอพอีกตัว, หรือรหัส QR เพื่อกระโดดเข้าไปในแอพหลัก ลิงก์เหล่านี้...

สําหรับคําตอบเรื่อง จันทรุปราคา/ เทศกาลต่าง ๆ ที่พูดออกไป -- ยกเว้น -- เปิดแอพ, ใช้ ~ Siri Apps ทางลัด (ดู [FAQ](./faq) → Siri). Off/Rest on a date ~, เพิ่มแยกวันทํางาน ~ App infects

## รูปแบบ


```
iwidget://<host>[?query]
```


| Rule | รายละเอียด |
|------|--------|
| **Scheme** | ไกด์ |
| **Host** | ทาง ซีก — มอง ลง ไป ข้าง ล่าง |
| **Query** | ตัวเลือก; จะอ่านเฉพาะกุญแจเอกสารเท่านั้น |

โฮสต์ที่ไม่รู้จักถูกละเลยอย่างปลอดภัย (ไม่มีความผิดพลาด)

---

## เครื่อง

| Host | Opens | สืบค้น |
|------|--------|-------|
| `today` | **Today** tab | — |
| `day` | **Today** tab and queues **day detail** for the given date | ~~~~ ปี เดือน เดือน~~ วัน (intergers) |
| `settings` | **Settings** tab | ** ม้วนกระดาษถึงส่วนตัวกรองเทศกาล ** |

หาก  c0 BAR ค่าการค้นหาขาดหรือไม่ถูกต้อง แอพยังคงเปลี่ยนมาเป็นวันนี้โดยไม่เปิดแผ่นงาน

---

## ตัวอย่าง

~เปิดวันนี้~


```
iwidget://today
```


~เปิด 1 มกราคม 2026 รายละเอียด~


```
iwidget://day?y=2026&m=1&d=1
```


~ การตั้งค่าเปิด ~


```
iwidget://settings?scroll=festivals
```


---

## พฤติกรรมของวิดเจ็ตและศูนย์ควบคุม

- Tapping board~ เมื่อ ~ ค่าตัดแกนเคาะ ~ อาจเปิด 'ididgettoday' (หรือพฤติกรรมที่เปิดอยู่โดยเจตนาของวิดเจ็ต)
- ~หน้าจอด้านล่าง~ ~และ~~ ~รายการต่าง ๆ ใช้ส่วนต่าง ๆ ของโปรแกรม App; ไม่ใช่โฮสต์ที่อยู่ URL เพิ่ม
- ** แถบเมนู Mac ~ ปฏิทินใช้รูปแบบที่อยู่ URL แบบเดิมเมื่อคลิกวันที่

---

## เคล็ดลับปุ่มพิมพ์ลัด

1. บวก -- เปิดที่อยู่ URL ~ และวางไ c0 link
2. ~ สําหรับวันทํางาน ~ ตรวจสอบ, สืบค้นไลบรารีการกระทําปุ่มพิมพ์ลัดสําหรับ iWidget's Office/ date ~ ซึ่งกําหนดวันและกําหนดวันให้ด้วย — มันไม่สามารถมีได้~ * เป็นการค้นหาจากที่อยู่ URL

[ย้อนกลับการรองรับ iWidget] [.//] สืบค้นเมื่อ 22 พฤษภาคม พ.ศ.

</section>
<section lang="de" markdown="1">

iWidget unterstützt das URL-Schema ** `iwidget://` ** auf **iPhone, iPad und Mac**. Verwenden Sie es in **Safari **, **Apple Shortcuts **, einer anderen App oder einem QR-Code, um in die Haupt-App zu springen. Diese Links **navigieren nur ** - sie übergeben keine Widget-Design-IDs oder Edit-Board-Layouts.

Für gesprochene Mond- / Festival-Antworten **ohne das Öffnen der App verwenden Sie **Siri App Shortcuts ** (siehe [FAQ] (../faq) → Siri). Für ** Arbeit / Ruhe an einem Datum ** fügen Sie die separate ** Workday ** App Intent in Shortcuts hinzu.

## Format


```
iwidget://<host>[?query]
```


| Rule | Einzelheiten |
|------|--------|
| **Scheme** | Iwidget (Kleinbuchstabe) |
| **Host** | Trassensegment — siehe Tabelle |
| **Query** | Optional; nur dokumentierte Schlüssel werden gelesen |

Unbekannte Hosts werden sicher ignoriert (kein Absturz).

---

## Gastgeber

| Host | Opens | Abfrage |
|------|--------|-------|
| `today` | **Today** tab | — |
| `day` | **Today** tab and queues **day detail** for the given date | **`y`** Jahr · **`m`** Monat · **`d`** Tag (ganzzahlig) |
| `settings` | **Settings** tab | **`scroll=festivals`** scrollt zum Filterbereich Festival |

Wenn `iwidget://` Abfragewerte fehlen oder ungültig sind, wechselt die App weiterhin zu Heute, ohne ein Tagesblatt zu öffnen.

---

## Beispiele

**Heute geöffnet**


```
iwidget://today
```


**Offen 1. Januar 2026 Detail **


```
iwidget://day?y=2026&m=1&d=1
```


**Offene Einstellungen → Festivalfilter**


```
iwidget://settings?scroll=festivals
```


---

## Widget & Control Center Verhalten

- Tippen Sie auf ein **home-screen-board**, wenn **intercept taps** ausgeschaltet ist, kann öffnen `iwidget://today` (oder Ihr konfiguriertes offenes Verhalten über widget Absicht).
- **Lock Screen** und **Control Center** Einträge verwenden App Intents; sie sind keine zusätzlichen URL-Hosts.
- **Mac Menüleiste** Kalender verwendet das gleiche "Tag" URL-Muster, wenn Sie auf ein Datum klicken.

---

## Abkürzungen

1. Fügen Sie ** URL ** hinzu und fügen Sie einen `iwidget://` -Link ein.
2. Für **Workday**-Checks suchen Sie in der Aktionsbibliothek Shortcuts nach der **Work/Ruhetag**-Absicht von iWidget und geben Sie ein Datum an – es ist **not** als URL-Abfrage verfügbar.

[Zurück zu iWidget Support](../) · [FAQ](../faq) · [Privacy Policy](../privacy]

</section>
<section lang="fr" markdown="1">

iWidget prend en charge le schéma d'URL ** `iwidget://` ** sur **iPhone, iPad et Mac**. Utilisez-le dans **Safari**, **Shortcuts d'Apple**, une autre application ou un code QR pour sauter dans l'application principale. Ces liens **navigate seulement** — ils ne passent pas les identifiants de conception de widget ou de modification de la configuration du tableau.

Pour les réponses orales lunaires / festival **sans** ouverture de l'application, utilisez **Séri App Raccourcis** (voir [FAQ](../faq) → Siri). Pour **travail / repos à une date**, ajouter le **Travail** App Intent dans Raccourcis.

## Format


```
iwidget://<host>[?query]
```


| Rule | Détail |
|------|--------|
| **Scheme** | `iwidget` (cas inférieur) |
| **Host** | Segment de trajectoire — voir tableau ci-dessous |
| **Query** | Optionnel; seules les clés documentées sont lues |

Les hôtes inconnus sont ignorés en toute sécurité (pas de crash).

---

## Hôtes

| Host | Opens | Demande |
|------|--------|-------|
| `today` | **Today** tab | — |
| `day` | **Today** tab and queues **day detail** for the given date | **'y'** année * **`m`** mois * **`d`** jour (integers) |
| `settings` | **Settings** tab | **`scroll=festivals`** défile vers la section filtre du festival |

Si `iwidget://` ---

## Exemples

**Ouvert aujourd'hui**


```
iwidget://today
```


**Ouvert le 1er janvier 2026 detail**


```
iwidget://day?y=2026&m=1&d=1
```


**Ouvrir les paramètres → filtres du festival**


```
iwidget://settings?scroll=festivals
```


---

## Comportement Widget & Control Center

- Cartographier un tableau d'écran ** à la maison** lorsque **intercept taps** est désactivé peut ouvrir `iwidget://today` (ou votre comportement ouvert configuré via l'intention de widget).
- **Lock Screen** et **Control Center** les entrées utilisent App Intents; ce ne sont pas des hôtes URL supplémentaires.
- **La barre de menu Mac** utilise le même modèle d'URL `jour` lorsque vous cliquez sur une date.

---

## Conseils de raccourcis

1. Ajouter **Ouvrir l'URL** et coller un lien `iwidget://` .
2. Pour les vérifications de **jour de travail**, recherchez la bibliothèque d'action Raccourcis pour iWidgets **jour de travail/rest** intention et fournir une date — il est **non** disponible en tant que requête URL.

[Retour à iWidget Support](../) · [FAQ](../faq) · [Politique de confidentialité](../privacy)

</section>
<section lang="tr" markdown="1">

iWidget, ** `iwidget://` ** URL programı **iPhone, iPad ve Mac** üzerinde destekler. Bunu **Safari**, ** Apple Shortcuts**, başka bir uygulama veya QR kodu ana uygulamaya atlamak için kullanın. Bu bağlantılar ** sadece** - widget tasarım kimlikleri veya düzenleme kurulu düzeni geçmiyorlar.

Konuşmak için Ay / festival cevapları ** Uygulamayı açmadan, kullanın **Siri App Shortcuts ** (see [FAQ] (./faq) → Siri). **Bir tarihteki iş/rest, ayrı **Workday ** Kısayollarda App Niyet.

## Format


```
iwidget://<host>[?query]
```


| Rule | Detaylı Bilgi |
|------|--------|
| **Scheme** | "iwidget" (düşük) |
| **Host** | Pat segmenti - aşağıdaki tabloyu görmek |
| **Query** | Seçmeli; sadece belgelenmiş anahtarlar okunur |

Bilinmeyen evler güvenli bir şekilde göz ardı edilir (öldürülemez).

---

## Hosts

| Host | Opens | Sorgu Sorgulama |
|------|--------|-------|
| `today` | **Today** tab | — |
| `day` | **Today** tab and queues **day detail** for the given date | **'y'** year · **'m'** ay · **'d' ** gün (entegers) |
| `settings` | **Settings** tab | **'scroll =festivals' ** Festival filtresi bölümüne kaydırıyor |

Eğer `iwidget://` sorgu değerleri eksik veya geçersiz ise, uygulama bugün bir gün sayfası açmadan hala anahtarlar.

---

## Örnekler

**Open Today**


```
iwidget://today
```


**Açık 1 Ocak 2026 detay**


```
iwidget://day?y=2026&m=1&d=1
```


**Açık Ayarlar → festival filtreleri**


```
iwidget://settings?scroll=festivals
```


---

## Widget & Control Center davranışı

- Bir **ev ekran kurulu** **intercept muslukları ** kapalı olabilir (ya da yapılandırılmış açık davranışınızı widget niyetiyle).
- **Lock Ekran** ve ** Kontrol Merkezi ** girişleri App niyetlerini kullanır; ek URL barındırmazlar.
- **Mac menüsü bar ** takvim, bir tarihe tıkladığınızda aynı "gün URL modelini kullanır.

---

## Shortcuts ipuçları

1. Ekle **Açık URL** ve bir `iwidget://` bağlantısını yapıştırın.
2. **Workday ** checks, iWidget'in ** işi/rest day** niyeti ve bir tarih tedarik etmek için Kısayollar aksiyon kütüphanesini ara. - It is **not ** available as a URL query.

[Back to iWidget Support](./) · [FAQ](./faq) · [Privacy Policy](./privacy)

</section>
