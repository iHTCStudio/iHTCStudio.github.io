---
layout: doc
title: iCoder — URL Scheme Reference
app_id: iLeetCoder
doc_title_en: URL Scheme Reference
doc_title_zh_cn: URL Scheme 深度链接文档
doc_title_zh_tw: URL Scheme 深度連結文件
description: Complete reference of iLeetCoder:// deep links, widget links and Home Screen Quick Actions supported by iCoder.
---

<section lang="en" markdown="1">

iCoder supports **`iLeetCoder://`** (case-insensitive) deep links — open a problem, daily quiz, favourites, wrong book, or filter by tag / company from Safari, Shortcuts, widgets, or another app.

## Protocol

| Host | Opens | Query |
|------|-------|-------|
| `problem` | Problem detail | `leetId=` or `id=` (e.g. `1`, `206`) |
| `quiz` | Daily Quiz tab | — |
| `favorites` | Favourites list | — |
| `wrong`, `mistakes`, `wrongquestions` | Wrong book | `record=<UUID>` → linked problem |
| `tag` | Problems filtered by tag | `name=` |
| `company` | Problems filtered by company | `name=` |

## Examples

```
iLeetCoder://problem?leetId=1
iLeetCoder://problem?id=206
iLeetCoder://quiz
iLeetCoder://tag?name=Array
iLeetCoder://company?name=Google
iLeetCoder://wrong?record=550E8400-E29B-41D4-A716-446655440000
```

## Home Screen Quick Actions

Up to **4** in **Settings → Home Screen shortcuts**: `search`, `quiz`, `favorites`, `wrong`, `categories`, `feedback`, `review`. Search / categories / feedback / review are Quick Action channels.

[Back to overview](..) · [FAQ](../faq) · [Privacy](../privacy)

</section>
<section lang="zh-CN" markdown="1">

爱算法支持 **`iLeetCoder://`** 深度链接——打开题目详情、每日测验、收藏、错题本，或按标签 / 公司筛选。

| Host | 打开 | 参数 |
|------|------|------|
| `problem` | 题目详情 | `leetId=` 或 `id=` |
| `quiz` | 每日测验 | — |
| `favorites` | 收藏列表 | — |
| `wrong` / `mistakes` | 错题本 | `record=<UUID>` |
| `tag` | 按标签筛选 | `name=` |
| `company` | 按公司筛选 | `name=` |

```
iLeetCoder://problem?leetId=1
iLeetCoder://tag?name=Array
iLeetCoder://company?name=Google
```

[返回概览](..) · [常见问题](../faq) · [隐私政策](../privacy)

</section>
<section lang="zh-TW" markdown="1">

愛算法支援 **`iLeetCoder://`** 深度連結——開啟題目詳情、每日測驗、收藏、錯題本，或依標籤 / 公司篩選。

| Host | 開啟 | 參數 |
|------|------|------|
| `problem` | 題目詳情 | `leetId=` 或 `id=` |
| `quiz` | 每日測驗 | — |
| `favorites` | 收藏列表 | — |
| `wrong` / `mistakes` | 錯題本 | `record=<UUID>` |
| `tag` | 依標籤篩選 | `name=` |
| `company` | 依公司篩選 | `name=` |

[返回概覽](..) · [常見問題](../faq) · [隱私政策](../privacy)

</section>
<section lang="ja" markdown="1">

iCoderは** `iLeetCoder://` **(大文字認識)ディープリンクをサポートしています。問題、毎日のクイズ、お気に入り、間違ったブック、またはSafari、ショートカット、ウィジェット、または別のアプリからタグ/会社によってフィルタリングします。

## プロトコル

| Host | Opens | クエリ |
|------|-------|-------|
| `problem` | Problem detail | `leetId=` または `id=` (`1`、`206` など) |
| `quiz` | Daily Quiz tab | — |
| `favorites` | Favourites list | — |
| `wrong`, `mistakes`, `wrongquestions` | Wrong book | `record=<UID>` → 連携問題 |
| `tag` | Problems filtered by tag | `name=` |
| `company` | Problems filtered by company | `name=` |

## 例


```
iLeetCoder://problem?leetId=1
iLeetCoder://problem?id=206
iLeetCoder://quiz
iLeetCoder://tag?name=Array
iLeetCoder://company?name=Google
iLeetCoder://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## ホーム スクリーンの速い行為

**4**で**設定 → ホーム画面ショートカット**:                                                                                                                                                                                                                                                                   検索/カテゴリ/フィードバック/レビューはクイックアクションチャンネルです。

[概要に戻る](...)・[FAQ](../faq)・[プライバシーポリシー](../privacy)

</section>
<section lang="ko" markdown="1">

iCoder 지원 ** `iLeetCoder://` ** (case-insensitive) 깊은 링크 - Safari, Shortcuts, 위젯 또는 다른 응용 프로그램에서 태그 / 회사에 의해 문제, 일일 퀴즈, 좋아하는, 잘못된 책, 또는 필터를 엽니 다.

## 프로젝트

| Host | Opens | 글쓰기 |
|------|-------|-------|
| `problem` | Problem detail | `leetId=` 또는 `id=`(예: `1`, `206`) |
| `quiz` | Daily Quiz tab | — |
| `favorites` | Favourites list | — |
| `wrong`, `mistakes`, `wrongquestions` | Wrong book | `record=<UUID>` → 링크된 문제 |
| `tag` | Problems filtered by tag | `이름=` |
| `company` | Problems filtered by company | `이름=` |

## 예시


```
iLeetCoder://problem?leetId=1
iLeetCoder://problem?id=206
iLeetCoder://quiz
iLeetCoder://tag?name=Array
iLeetCoder://company?name=Google
iLeetCoder://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## 홈 화면 빠른 행동

** 4 ** ** 설정 → 홈 화면 단축 **: `iLeetCoder://` , `problem` , `leetId=` , `id=` , `1` , `206` , `quiz` . 검색 / 카테고리 / 피드백 / 리뷰는 Quick Action 채널입니다.

[경찰](..) · [FAQ](../faq) · [Privacy](../privacy)

</section>
<section lang="ru" markdown="1">

iCoder поддерживает ** `iLeetCoder://` ** (случайно-нечувствительные) глубокие ссылки - откройте проблему, ежедневную викторину, фавориты, неправильную книгу или фильтр по тегу / компании из Safari, Shortcuts, виджетов или другого приложения.

## Протокол

| Host | Opens | Запрос |
|------|-------|-------|
| `problem` | Problem detail | "leetId=" или "id=" (например, "1", "206") |
| `quiz` | Daily Quiz tab | — |
| `favorites` | Favourites list | — |
| `wrong`, `mistakes`, `wrongquestions` | Wrong book | «record=<UUID>» → связанная проблема |
| `tag` | Problems filtered by tag | Имя = |
| `company` | Problems filtered by company | Имя = |

## Примеры


```
iLeetCoder://problem?leetId=1
iLeetCoder://problem?id=206
iLeetCoder://quiz
iLeetCoder://tag?name=Array
iLeetCoder://company?name=Google
iLeetCoder://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## Домой Экран Быстрые действия

До **4** в **Настройки → Ярлыки домашнего экрана **: `iLeetCoder://` , `problem` , `leetId=` , `id=` , `1` , `206` , `quiz` . Поиск / категории / отзывы / обзор - это каналы быстрого действия.

[Назад к обзору] (..) · [FAQ] (../faq) · [Privacy] (../privacy)

</section>
<section lang="th" markdown="1">

iCoder รองรับ} `iLeetCoder://` BAR  ลิงก์ลึก (ตัวพิมพ์เล็ก) — เปิดปัญหา, ข้อสอบประจําวัน, ของโปรด, เล่มผิด หรือตัวกรองโดยบริษัทแท็ก / บริษัท จากซาฟารี, ทางลัด, วิดเจ็ต, หรือแอพอื่น ๆ

## โพรโทคอล

| Host | Opens | สืบค้น |
|------|-------|-------|
| `problem` | Problem detail | ROUNTID='หรือ shiid=' (e.g.  `, 206) |
| `quiz` | Daily Quiz tab | — |
| `favorites` | Favourites list | — |
| `wrong`, `mistakes`, `wrongquestions` | Wrong book | 'บันทึก=[UUUID]' 'ปัญหาเชื่อมโยง |
| `tag` | Problems filtered by tag | 'ชื่อ=' |
| `company` | Problems filtered by company | 'ชื่อ=' |

## ตัวอย่าง


```
iLeetCoder://problem?leetId=1
iLeetCoder://problem?id=206
iLeetCoder://quiz
iLeetCoder://tag?name=Array
iLeetCoder://company?name=Google
iLeetCoder://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## การกระทําด่วนของจอส่วนตัว

เพิ่มถึง ** 4 ** ใน ** การตั้งค่า ปุ่มพิมพ์ลัดจอจอส่วนตัว ~: `iLeetCoder://` BAR   BAR `problem` BAR                                                                                                                                                                                                                สืบค้น / หมวดหมู่ / คําติชม / ทบทวนเป็นช่องปฏิบัติการด่วน

[Tack to Broups](. ) สืบค้นเมื่อ 22 พฤษภาคม พ.ศ.

</section>
<section lang="de" markdown="1">

iCoder unterstützt ** `iLeetCoder://` ** (case-insensitive) tiefe Links – öffnen Sie ein Problem, tägliches Quiz, Favoriten, falsches Buch oder filtern Sie nach Tag / Firma von Safari, Shortcuts, Widgets oder einer anderen App.

## Protokoll

| Host | Opens | Abfrage |
|------|-------|-------|
| `problem` | Problem detail | `leetId=` oder `id=` (z.B. `1`, `206`) |
| `quiz` | Daily Quiz tab | — |
| `favorites` | Favourites list | — |
| `wrong`, `mistakes`, `wrongquestions` | Wrong book | `record=<UUID>` → Linked Problem |
| `tag` | Problems filtered by tag | „name= |
| `company` | Problems filtered by company | „name= |

## Beispiele


```
iLeetCoder://problem?leetId=1
iLeetCoder://problem?id=206
iLeetCoder://quiz
iLeetCoder://tag?name=Array
iLeetCoder://company?name=Google
iLeetCoder://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## Home Bildschirm Schnelle Aktionen

Bis zu **4** in **Einstellungen → Home Screen Shortcuts **: `iLeetCoder://` , `problem` , `leetId=` , `id=` , `1` , `206` , `quiz` . Suche / Kategorien / Feedback / Review sind Quick Action-Kanäle.

[Zurück zur Übersicht](..) · [FAQ](../faq) · [Privacy](../privacy]

</section>
<section lang="fr" markdown="1">

iCoder prend en charge ** `iLeetCoder://` ** (insensible aux cas) les liens profonds — ouvrir un problème, quiz quotidien, favoris, mauvais livre, ou filtrer par tag / entreprise de Safari, Raccourcis, widgets, ou une autre application.

## Protocole

| Host | Opens | Demande |
|------|-------|-------|
| `problem` | Problem detail | `leetId=` ou `id=` (par exemple `1`, `206`) |
| `quiz` | Daily Quiz tab | — |
| `favorites` | Favourites list | — |
| `wrong`, `mistakes`, `wrongquestions` | Wrong book | `registr=<UUID>` → problème lié |
| `tag` | Problems filtered by tag | `nom=` |
| `company` | Problems filtered by company | `nom=` |

## Exemples


```
iLeetCoder://problem?leetId=1
iLeetCoder://problem?id=206
iLeetCoder://quiz
iLeetCoder://tag?name=Array
iLeetCoder://company?name=Google
iLeetCoder://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## Actions rapides de l'écran d'accueil

Jusqu'à **4** dans **Paramètres → raccourcis d'écran d'accueil**: `iLeetCoder://` , `problem` , `leetId=` , `id=` , `1` , `206` , `quiz` . Rechercher / catégories / feedback / review sont des canaux d'action rapide.

[Retour à l'aperçu](..) · [FAQ](../faq) · [Confidentialité](../privacité)

</section>
<section lang="tr" markdown="1">

iCoder, ** `iLeetCoder://` ** (case-in sensitive) derin bağlantıları destekler - bir problem açın, günlük bir sınav, favoriler, yanlış kitap veya filtre: tag / şirket Safari, Shortcuts, widgets veya başka bir uygulama.

## Protokol Protokolü

| Host | Opens | Sorgu Sorgulama |
|------|-------|-------|
| `problem` | Problem detail | "Et=" veya "id=" (e.g. "1', "206") |
| `quiz` | Daily Quiz tab | — |
| `favorites` | Favourites list | — |
| `wrong`, `mistakes`, `wrongquestions` | Wrong book | "record=<UUUID>" → bağlantılı problem |
| `tag` | Problems filtered by tag | "isim=" |
| `company` | Problems filtered by company | "isim=" |

## Örnekler


```
iLeetCoder://problem?leetId=1
iLeetCoder://problem?id=206
iLeetCoder://quiz
iLeetCoder://tag?name=Array
iLeetCoder://company?name=Google
iLeetCoder://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## Home Screen Quick Actions

**4** in **Settings → Home Ekran kısayolları**: `iLeetCoder://` , `problem` , `leetId=` , `id=` , `1` , `quiz` Arama / kategoriler / geri bildirimler / inceleme Hızlı Eylem kanallarıdır.

[Genellikle] (.) · [FAQ](./faq) · [Privacy] (./privacy)

</section>
