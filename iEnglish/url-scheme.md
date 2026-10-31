---
layout: doc
title: iEnglish — URL Scheme Reference
app_id: iEnglish
doc_title_en: URL Scheme Reference
doc_title_zh_cn: URL Scheme 深度链接文档
doc_title_zh_tw: URL Scheme 深度連結文件
description: Complete reference of ienglish:// deep links, widget links and Home Screen Quick Actions supported by iEnglish.
---

<section lang="en" markdown="1">

iEnglish supports **`ienglish://`** URL scheme deep links — open a word, the Daily Quiz, Favourites, Wrong Book, playlist or categories from Safari, Shortcuts, widgets, or another app.

**Home Screen Quick Actions** (long-press the app icon) add Search, Feedback and Rate — those types are **not** parsed by `IEnglishDeepLink` but still open the app via the shortcut observer.

> **Note:** Links only **navigate** inside the app. They do not start pronunciation or change study settings remotely.

## Protocol

```
ienglish://<host>[?query]
```

| Rule | Detail |
|------|--------|
| **Scheme** | `ienglish` (case-insensitive) |
| **Word detail** | Host `word` — query **`id=<wordID>`** (required, non-empty) |
| **Quiz** | Host `quiz` |
| **Favourites** | Host `favorites` |
| **Wrong book** | Host `wrong` or `mistakes` — optional `record=<UUID>` opens one mistake |
| **Playlist** | Host `playlist` |
| **Categories** | Host `categories` |

## Examples

```
ienglish://word?id=apple
ienglish://quiz
ienglish://favorites
ienglish://wrong
ienglish://wrong?record=550E8400-E29B-41D4-A716-446655440000
ienglish://playlist
ienglish://categories
```

## Home Screen Quick Actions

Configure up to **4** in **Settings → Home Screen shortcuts**. Types include `ienglish://search`, `quiz`, `favorites`, `wrong`, `categories`, `feedback`, `review` — Search / Feedback / Review are delivered as Quick Actions only.

## Widget deep links

Widget taps use the same `ienglish://` hosts (e.g. Daily Quiz → `quiz`, Favourites glance → `favorites`).

[Back to overview](..) · [FAQ](../faq) · [Privacy](../privacy)

</section>
<section lang="zh-CN" markdown="1">

爱英语支持 **`ienglish://`** 深度链接——从 Safari、快捷指令、小组件或其他 App 打开单词详情、每日测验、收藏、错题本、播放列表或分类。

**主屏快捷操作**（长按图标）另提供搜索、反馈、评分等入口；其中 **搜索 / 反馈 / 评分** 仅通过 Quick Action 分发，不经 `IEnglishDeepLink.parse`。

> **说明：** 链接仅用于 **App 内导航**，不会远程播放发音或修改学习设置。

## 协议

```
ienglish://<host>[?query]
```

| 规则 | 说明 |
|------|------|
| **Scheme** | `ienglish`（不区分大小写） |
| **单词详情** | Host `word` — 查询参数 **`id=<wordID>`**（必填） |
| **每日测验** | Host `quiz` |
| **收藏** | Host `favorites` |
| **错题本** | Host `wrong` 或 `mistakes` — 可选 `record=<UUID>` 打开单条错题 |
| **播放列表** | Host `playlist` |
| **分类** | Host `categories` |

## 示例

```
ienglish://word?id=apple
ienglish://quiz
ienglish://favorites
ienglish://wrong
ienglish://wrong?record=550E8400-E29B-41D4-A716-446655440000
ienglish://playlist
ienglish://categories
```

## 主屏快捷操作

在 **设置 → 主屏快捷操作** 中最多选 **4** 项，类型含 `ienglish://search`、`quiz`、`favorites`、`wrong`、`categories`、`feedback`、`review`。

## 小组件深度链接

小组件点击使用相同 `ienglish://` 路径（如每日测验 → `quiz`）。

[返回概览](..) · [常见问题](../faq) · [隐私政策](../privacy)

</section>
<section lang="zh-TW" markdown="1">

愛英語支援 **`ienglish://`** 深度連結——從 Safari、捷徑、小工具或其他 App 開啟單字詳情、每日測驗、收藏、錯題本、播放清單或分類。

**主畫面快捷操作**（長按圖示）另提供搜尋、回饋、評分等入口；其中 **搜尋 / 回饋 / 評分** 僅透過 Quick Action 分發，不經 `IEnglishDeepLink.parse`。

> **說明：** 連結僅用於 **App 內導覽**，不會遠端播放發音或修改學習設定。

## 協定

```
ienglish://<host>[?query]
```

| 規則 | 說明 |
|------|------|
| **Scheme** | `ienglish`（不區分大小寫） |
| **單字詳情** | Host `word` — 查詢參數 **`id=<wordID>`**（必填） |
| **每日測驗** | Host `quiz` |
| **收藏** | Host `favorites` |
| **錯題本** | Host `wrong` 或 `mistakes` — 可選 `record=<UUID>` 開啟單條錯題 |
| **播放清單** | Host `playlist` |
| **分類** | Host `categories` |

## 範例

```
ienglish://word?id=apple
ienglish://quiz
ienglish://favorites
ienglish://wrong
ienglish://wrong?record=550E8400-E29B-41D4-A716-446655440000
ienglish://playlist
ienglish://categories
```

## 主畫面快捷操作

在 **設定 → 主畫面快捷操作** 中最多選 **4** 項，類型含 `ienglish://search`、`quiz`、`favorites`、`wrong`、`categories`、`feedback`、`review`。

## 小工具深度連結

小工具點擊使用相同 `ienglish://` 路徑（如每日測驗 → `quiz`）。

[返回概覽](..) · [常見問題](../faq) · [隱私政策](../privacy)

</section>
<section lang="ja" markdown="1">

iEnglishは** `ienglish://` **をサポート URLスキームの深いリンク - 単語、毎日のクイズ、お気に入り、間違ったブック、プレイリスト、またはSafari、ショートカット、ウィジェット、または別のアプリからカテゴリを開きます。

**ホーム画面のクイックアクション**(アプリのアイコンを長押し)検索、フィードバック、およびレートを追加 — これらのタイプは、 `ienglish://` によってパースされていないが、まだショートカットのオブザーバーを介してアプリを開きます。

> **注意:** リンクはアプリ内の**navigate**のみです。 発音や遠隔で学習設定を変更しない。

## プロトコル


```
ienglish://<host>[?query]
```


| Rule | 詳細を見る |
|------|--------|
| **Scheme** | `ienglish` (ケースインセンティブ) |
| **Word detail** | ホスト `word` — クエリ **id=<wordID>`** (必須、非空) |
| **Quiz** | ホスト `quiz` |
| **Favourites** | ホスト `お気に入り` |
| **Wrong book** | ホスト `wrong` または `mistakes` — オプション `record=<UID>` は 1 つの間違いを開きます |
| **Playlist** | ホスト `playlist` |
| **Categories** | ホスト `categories` |

## 例


```
ienglish://word?id=apple
ienglish://quiz
ienglish://favorites
ienglish://wrong
ienglish://wrong?record=550E8400-E29B-41D4-A716-446655440000
ienglish://playlist
ienglish://categories
```


## ホーム スクリーンの速い行為

**設定 → ホーム画面ショートカット**で**4**まで設定します。 種類には、 `ienglish://` 、 `IEnglishDeepLink` 、 `ienglish` 、 `word` 、 `id=<wordID>` 、 `quiz` 、 `favorites` - 検索/フィードバック/レビューは、クイックアクションとしてのみ配信されます。

## ウィジェットディープリンク

Widget は `ienglish://` と同じホストを使用します (例: デイリー・クイズ → `IEnglishDeepLink` , お気に入り・グレンス → `ienglish` )。

[概要に戻る](...)・[FAQ](../faq)・[プライバシーポリシー](../privacy)

</section>
<section lang="ko" markdown="1">

iEnglish 지원 ** `ienglish://` ** URL 계획 깊은 링크 — 단어를 열고, Daily Quiz, Favourites, Wrong Book, playlist 또는 카테고리에서 사파리, Shortcuts, 위젯, 또는 다른 응용 프로그램.

**홈 화면 빠른 행동** (앱 아이콘을 길게 누르십시오) 검색, 피드백 및 비율을 추가합니다. 그 유형은 ** `ienglish://` 에 의해 파싱하지만 여전히 단축키 관찰자를 통해 앱을 엽니 다.

> **주의:** 앱 내에서만 링크 **navigate**. 그들은 pronunciation를 시작하거나 원격으로 공부 설정을 변경하지 않습니다.

## 프로젝트


```
ienglish://<host>[?query]
```


| Rule | 제품 정보 |
|------|--------|
| **Scheme** | `ienglish`(케이인성) |
| **Word detail** | 호스트 `word` - 쿼리 **`id=<wordID>`** (필수, 비 빈) |
| **Quiz** | 호스트 `quiz` |
| **Favourites** | 호스트 `favorites` |
| **Wrong book** | 호스트 `wrong` 또는 `mistakes` - 옵션 `record=<UUID>`는 하나의 실수를 엽니다. |
| **Playlist** | 호스트 `playlist` |
| **Categories** | 호스트 `categories` |

## 예시


```
ienglish://word?id=apple
ienglish://quiz
ienglish://favorites
ienglish://wrong
ienglish://wrong?record=550E8400-E29B-41D4-A716-446655440000
ienglish://playlist
ienglish://categories
```


## 홈 화면 빠른 행동

**4** in**Settings → 홈 화면 단축키**를 구성합니다. 유형은 포함 `ienglish://` , `IEnglishDeepLink` , `ienglish` , `word` , `id=<wordID>` , `quiz` , `favorites` - 검색 / 피드백 / 리뷰는 빠른 행동으로 전달됩니다.

## Widget 깊은 링크

위젯 탭은 같은 사용 `ienglish://` 호스트 (예 : Daily Quiz → `IEnglishDeepLink` , Favourites 눈 → `ienglish` ).

[경찰](..) · [FAQ](../faq) · [Privacy](../privacy)

</section>
<section lang="ru" markdown="1">

Поддержка на английском языке ** `ienglish://` ** Схема URL глубоких ссылок — откройте слово, Daily Quiz, Favourites, Wrong Book, плейлист или категории из Safari, Shortcuts, виджетов или другого приложения.

**Домашний экран Быстрые действия** (долгое нажатие значка приложения) добавить Поиск, Обратная связь и Ставка - эти типы ** не** парсируются `ienglish://` , но все еще открыть приложение через ярлык наблюдателя.

> **Примечание:** Ссылки ** перемещаются ** внутри приложения. Они не запускают произношение и не меняют настройки обучения удаленно.

## Протокол


```
ienglish://<host>[?query]
```


| Rule | Подробнее |
|------|--------|
| **Scheme** | Английский (case-insensitive) |
| **Word detail** | Host 'word' - запрос **'id=<wordID>** (обязательно, не пустой) |
| **Quiz** | Ведущий «Викторины» |
| **Favourites** | Ведущий «Любимые» |
| **Wrong book** | Ведущий «неправильный» или «ошибки» — дополнительная «запись = <UUID>» открывает одну ошибку |
| **Playlist** | Ведущий «Плейлист» |
| **Categories** | Ведущие "категории" |

## Примеры


```
ienglish://word?id=apple
ienglish://quiz
ienglish://favorites
ienglish://wrong
ienglish://wrong?record=550E8400-E29B-41D4-A716-446655440000
ienglish://playlist
ienglish://categories
```


## Домой Экран Быстрые действия

Настройка до **4** в **Настройки → Ярлыки домашнего экрана **. Типы включают `ienglish://` , `IEnglishDeepLink` , `ienglish` , `word` , `id=<wordID>` , `quiz` , `favorites` — Поиск / Обратная связь / Обзор предоставляется только в виде Быстрых действий.

## Виджеты Deep Links

Виджетные краны используют те же хосты `ienglish://` (например, Daily Quiz → `IEnglishDeepLink` , Favourites look → `ienglish` ).

[Назад к обзору] (..) · [FAQ] (../faq) · [Privacy] (../privacy)

</section>
<section lang="th" markdown="1">

การรองรับ i English ~ `ienglish://` BAR ~ ที่อยู่ URL กําหนดตําแหน่งลิงก์ลึก ๆ — เปิดคํา, Daily Quiz, February, Daily Book, play play play หรือ ประเภทจาก Saveri, ปุ่มพิมพ์ลัด, วิดเจ็ต หรือแอปพลิเคชันอื่น ๆ

~~หน้าจอหน้าจอทํางานรวดเร็ว~ ~ (กดดันไอคอนโปรแกรมมานาน) เพิ่มการค้นหา, แหล่งป้อนและอัตรา — ประเภทเหล่านั้นไม่ถูกวิเคราะห์โดย c0     แต่ยังเปิดโปรแกรมผ่านทางผู้สังเกตการณ์ทางลัด

> <i> เชื่อมโยงเท่านั้น... พวก เขา ไม่ เริ่ม ออก เสียง หรือ เปลี่ยน ค่า การ ศึกษา จาก ที่ ห่าง ไกล.

## โพรโทคอล


```
ienglish://<host>[?query]
```


| Rule | รายละเอียด |
|------|--------|
| **Scheme** | 'อังกฤษ' (ถ้าอ่อนไหว) |
| **Word detail** | โฮสต์ 'คํา' — สืบค้น **. สืบค้น = < suffid> '' (require, ไม่ว่างเปล่า) |
| **Quiz** | โฮสต์ |
| **Favourites** | โฮสต์ |
| **Wrong book** | โฮสต์ 'ผิดพลาด' หรือ 'พลาด' -- เลือก 'บันทึก=' เปิดหนึ่งความผิดพลาด |
| **Playlist** | โฮสต์ |
| **Categories** | โฮสต์ |

## ตัวอย่าง


```
ienglish://word?id=apple
ienglish://quiz
ienglish://favorites
ienglish://wrong
ienglish://wrong?record=550E8400-E29B-41D4-A716-446655440000
ienglish://playlist
ienglish://categories
```


## การกระทําด่วนของจอส่วนตัว

ปรับแต่งขึ้นถึง ** 4 ** ในโปรแกรมตั้งค่าหน้าจอส่วนตัว ** ประเภทรวม `ienglish://` C1                                                              สืบค้น/c6 BAR b. — preadback / review จะถูกส่งมาเป็นการกระทําด่วนเท่านั้น

## ส่วนเชื่อมโยงลึกของวิดเจ็ต

เสียงเคาะของวิดเจ็ตใช้เสียงเดียวกัน `ienglish://` BAR โฮสต์ (e.g.Daily Quiz  c1      BAR , FEKSLS wee/C2     BAR         BAR ).

[Tack to Broups](. ) สืบค้นเมื่อ 22 พฤษภาคม พ.ศ.

</section>
<section lang="de" markdown="1">

iEnglisch unterstützt ** `ienglish://` ** URL-Schema Deep Links - öffnen Sie ein Wort, das Daily Quiz, Favoriten, Wrong Book, Playlist oder Kategorien von Safari, Shortcuts, Widgets oder einer anderen App.

**Home Screen Quick Actions** (langes Drücken des App-Symbols) fügen Sie Suchen, Feedback und Rate hinzu - diese Typen werden **nicht ** durch `ienglish://` analysiert, aber öffnen Sie die App trotzdem über den Shortcut-Beobachter.

> **Hinweis:** Links nur **navigieren** innerhalb der App. Sie beginnen nicht mit der Aussprache oder ändern die Studieneinstellungen aus der Ferne.

## Protokoll


```
ienglish://<host>[?query]
```


| Rule | Einzelheiten |
|------|--------|
| **Scheme** | `ienglish` (fallunempfindlich) |
| **Word detail** | Host `word` — abfrage **`id=<wordID>`** (erforderlich, nicht leer) |
| **Quiz** | Host "Quiz" |
| **Favourites** | Gastgeber `Favoriten` |
| **Wrong book** | Host `falsch` oder `Fehler` — optional `record=<UUID>` öffnet einen Fehler |
| **Playlist** | Host "Playlist" |
| **Categories** | Host "Kategorien" |

## Beispiele


```
ienglish://word?id=apple
ienglish://quiz
ienglish://favorites
ienglish://wrong
ienglish://wrong?record=550E8400-E29B-41D4-A716-446655440000
ienglish://playlist
ienglish://categories
```


## Home Bildschirm Schnelle Aktionen

Konfigurieren Sie bis zu **4** in **Einstellungen → Home Screen Shortcuts **. Zu den Typen gehören `ienglish://` , `IEnglishDeepLink` , `ienglish` , `word` , `id=<wordID>` , `quiz` , `favorites` Suchen / Feedback / Review werden nur als Quick Actions geliefert.

## Widget Deep Links

Widget-Haps verwenden die gleichen `ienglish://` -Hosts (z. B. Daily Quiz → `IEnglishDeepLink` , Favoritenblick → `ienglish` ).

[Zurück zur Übersicht](..) · [FAQ](../faq) · [Privacy](../privacy]

</section>
<section lang="fr" markdown="1">

iEnglish supporte ** `ienglish://` ** URL schéma de liens profonds — ouvrir un mot, le Daily Quiz, Favoris, mauvais livre, playlist ou des catégories de Safari, Raccourcis, widgets, ou une autre application.

**Actions rapides à l'écran d'accueil** (cliquez sur l'icône de l'application) ajouter Search, Feedback and Rate — ces types ne sont pas **** analysés par `ienglish://` , mais toujours ouvrir l'application via l'observateur du raccourci.

> **Note :** Liens seulement **navigate** dans l'application. Ils ne commencent pas la prononciation ou changent les paramètres d'étude à distance.

## Protocole


```
ienglish://<host>[?query]
```


| Rule | Détail |
|------|--------|
| **Scheme** | "ifrancais" (insensible aux cas) |
| **Word detail** | Hôte `word` — requête **`id=<wordID>`** (obligatoire, non vide) |
| **Quiz** | Hébergement "quiz" |
| **Favourites** | Accueillir des "favorites" |
| **Wrong book** | Host `wrong` ou `mistakes` — optionnel `record=<UUID>` ouvre une erreur |
| **Playlist** | Hôte `playlist` |
| **Categories** | Catégories d ' hôtes |

## Exemples


```
ienglish://word?id=apple
ienglish://quiz
ienglish://favorites
ienglish://wrong
ienglish://wrong?record=550E8400-E29B-41D4-A716-446655440000
ienglish://playlist
ienglish://categories
```


## Actions rapides de l'écran d'accueil

Configurez jusqu'à **4** dans **Paramètres → raccourcis d'écran d'accueil**. Les types comprennent : `ienglish://` , `IEnglishDeepLink` , `ienglish` , `word` , `id=<wordID>` , `quiz` , `favorites` — Recherche / Rétroaction / Examen ne sont fournis que sous forme de mesures rapides.

## Widget liens profonds

Les touches Widget utilisent les mêmes hôtes `ienglish://` (p. ex. Quiz quotidien → `IEnglishDeepLink` , Coup d'oeil favori → `ienglish` ).

[Retour à l'aperçu](..) · [FAQ](../faq) · [Confidentialité](../privacité)

</section>
<section lang="tr" markdown="1">

İngilizce, ** `ienglish://` ** URL planı derin bağlantıları - bir kelime açın, Daily Quiz, Favourites, yanlış Book, listeler veya Safari, Shortcuts, widgets veya başka bir uygulama.

**Home Ekran Hızlı Eylemler ** (Uygulama ikonunu bastırın) Arama, Geri bildirim ve Puan ekleyin - bu tipler ** değil ** `ienglish://` tarafından yorumlanır, ancak hala uygulamayı kısayol gözlemci aracılığıyla açın.

> **Not:** Linkler sadece **navigate** uygulama içinde. Uzaktan olarak telaffuz etmeye veya araştırma ayarlarını değiştirmeye başlamazlar.

## Protokol Protokolü


```
ienglish://<host>[?query]
```


| Rule | Detaylı Bilgi |
|------|--------|
| **Scheme** | "Sürekli" (sağlıklı) |
| **Word detail** | Host "word" - query **'id=<wordID>'** (gereksiz, boş olmayan) |
| **Quiz** | Host "quiz" |
| **Favourites** | Host "favorites" |
| **Wrong book** | Host "wrong" veya "mistakes" - Seçmeli "record=<UUID>" bir hata açar |
| **Playlist** | Host "playlist" |
| **Categories** | Host "categories" |

## Örnekler


```
ienglish://word?id=apple
ienglish://quiz
ienglish://favorites
ienglish://wrong
ienglish://wrong?record=550E8400-E29B-41D4-A716-446655440000
ienglish://playlist
ienglish://categories
```


## Home Screen Quick Actions

**4 **'e kadar yapılandırın **Settings → Home Ekran kısayolları**. Türler `ienglish://` , `IEnglishDeepLink` , `word` , `id=<wordID>` , `quiz` , `favorites` - Search / Feedback / Review sadece Quick Actions olarak teslim edilir.

## Widget derin bağlantılar

Widget aynı `ienglish://` ev sahipliği kullanır (e.g. Daily Quiz → `IEnglishDeepLink` , Favourites view → `ienglish` ).

[Genellikle] (.) · [FAQ](./faq) · [Privacy] (./privacy)

</section>
