---
layout: doc
title: iWuBi — URL Scheme Reference
app_id: iWuBi
doc_title_en: URL Scheme Reference
doc_title_zh_cn: URL Scheme 深度链接文档
doc_title_zh_tw: URL Scheme 深度連結文件
description: Complete reference of iWuBi:// deep links, widget links and Home Screen Quick Actions supported by iWuBi.
---

<section lang="en" markdown="1">

iWuBi supports **`iWuBi://`** (case-insensitive scheme `iwubi`) deep links — open lookup, daily quiz, favourites, wrong book, code-length levels, learn hub or typing practice from Safari, Shortcuts, widgets, or another app.

## Protocol

```
iWuBi://<host>[?query]
iWuBi:///path-style   ← host empty; first path segment is the action
```

| Host / action | Opens | Query |
|---------------|-------|-------|
| `search` | Lookup tab, focus search | `q`, `word`, or `name` pre-fills |
| `word`, `char`, `character` | Word detail (or search if query empty) | `q` / `word` / `name` = character |
| `quiz`, `test` | Learn → Daily Quiz | — |
| `favorites`, `favorite` | Settings → Favourites | — |
| `wrong`, `mistakes`, `wrongbook` | Wrong book | `record=<UUID>` → one record |
| `levels`, `level`, `codes` | Levels tab | — |
| `learn`, `study` | Learn tab | — |
| `typing`, `type`, `practice` | Typing tab | — |

## Examples

```
iWuBi://search?q=你好
iWuBi://word?q=好
iWuBi://quiz
iWuBi://wrong?record=550E8400-E29B-41D4-A716-446655440000
iWuBi://levels
iWuBi://typing
```

## Home Screen Quick Actions

Up to **4** in **Settings → Home Screen shortcuts**: `search`, `quiz`, `favorites`, `wrong`, `levels`, `feedback`, `review`. **Feedback** and **review** are Quick Action only.

[Back to overview](..) · [FAQ](../faq) · [Privacy](../privacy)

</section>
<section lang="zh-CN" markdown="1">

爱五笔支持 **`iWuBi://`**（scheme 不区分大小写，注册为 `iwubi`）深度链接——从 Safari、快捷指令、小组件或其他 App 打开查字、每日测验、收藏、错题本、简码、学习或打字练习。

## 协议

| Host / 动作 | 打开 | 查询参数 |
|-------------|------|----------|
| `search` | 查字 Tab，聚焦搜索 | `q` / `word` / `name` 预填 |
| `word` / `char` / `character` | 字词详情（无参数则仅打开搜索） | `q` / `word` / `name` = 汉字 |
| `quiz` / `test` | 学习 → 每日测验 | — |
| `favorites` | 设置 → 收藏 | — |
| `wrong` / `mistakes` / `wrongbook` | 错题本 | `record=<UUID>` 打开单条 |
| `levels` / `level` / `codes` | 简码 Tab | — |
| `learn` / `study` | 学习 Tab | — |
| `typing` / `type` / `practice` | 打字 Tab | — |

## 示例

```
iWuBi://search?q=你好
iWuBi://word?q=好
iWuBi://quiz
iWuBi://wrong?record=550E8400-E29B-41D4-A716-446655440000
```

## 主屏快捷操作

**设置 → 主屏快捷操作** 最多 **4** 项：`search`、`quiz`、`favorites`、`wrong`、`levels`、`feedback`、`review`。

[返回概览](..) · [常见问题](../faq) · [隐私政策](../privacy)

</section>
<section lang="zh-TW" markdown="1">

愛五筆支援 **`iWuBi://`**（scheme 不區分大小寫，註冊為 `iwubi`）深度連結——從 Safari、捷徑、小工具或其他 App 開啟查字、每日測驗、收藏、錯題本、簡碼、學習或打字練習。

## 協定

| Host / 動作 | 開啟 | 查詢參數 |
|-------------|------|----------|
| `search` | 查字 Tab，聚焦搜尋 | `q` / `word` / `name` 預填 |
| `word` / `char` / `character` | 字詞詳情 | `q` / `word` / `name` = 漢字 |
| `quiz` / `test` | 學習 → 每日測驗 | — |
| `favorites` | 設定 → 收藏 | — |
| `wrong` / `mistakes` / `wrongbook` | 錯題本 | `record=<UUID>` 開啟單條 |
| `levels` / `level` / `codes` | 簡碼 Tab | — |
| `learn` / `study` | 學習 Tab | — |
| `typing` / `type` / `practice` | 打字 Tab | — |

## 範例

```
iWuBi://search?q=你好
iWuBi://word?q=好
iWuBi://quiz
```

## 主畫面快捷操作

**設定 → 主畫面快捷操作** 最多 **4** 項。

[返回概覽](..) · [常見問題](../faq) · [隱私政策](../privacy)

</section>
<section lang="ja" markdown="1">

iWuBiは、** `iWuBi://` **(ケース・インセンティブ・スキーム `iwubi` )ディープ・リンクをサポートしています。オープン・ルックアップ、デイリー・クイズ、お気に入り、間違ったブック、コード・長さ・レベル、Safari、ショートカット、ウィジェット、またはその他のアプリからハブまたはタイピング・プラクティスを学びます。

## プロトコル


```
iWuBi://<host>[?query]
iWuBi:///path-style   ← host empty; first path segment is the action
```


| Host / action | Opens | クエリ |
|---------------|-------|-------|
| `search` | Lookup tab, focus search | `q`, `word`, または `name` プリフィル |
| `word`, `char`, `character` | Word detail (or search if query empty) | `q` / `word` / `name` = 文字 |
| `quiz`, `test` | Learn → Daily Quiz | — |
| `favorites`, `favorite` | Settings → Favourites | — |
| `wrong`, `mistakes`, `wrongbook` | Wrong book | `record=<UID>` → 1レコード |
| `levels`, `level`, `codes` | Levels tab | — |
| `learn`, `study` | Learn tab | — |
| `typing`, `type`, `practice` | Typing tab | — |

## 例


```
iWuBi://search?q=你好
iWuBi://word?q=好
iWuBi://quiz
iWuBi://wrong?record=550E8400-E29B-41D4-A716-446655440000
iWuBi://levels
iWuBi://typing
```


## ホーム スクリーンの速い行為

**4**で**設定 → ホーム画面ショートカット**: `iWuBi://` , `iwubi` , `search` , `q` , `word` , `name` , `word` ,

[概要に戻る](...)・[FAQ](../faq)・[プライバシーポリシー](../privacy)

</section>
<section lang="ko" markdown="1">

iWuBi는 ** `iWuBi://` ** (case-insensitive 계획 `iwubi` ) 깊은 링크 - 오픈 뷰업, 일일 퀴즈, 즐겨 찾기, 잘못된 책, 코드 길이 레벨, Safari, Shortcuts, 위젯 또는 다른 응용 프로그램에서 허브 또는 타이핑 연습을 배울 수 있습니다.

## 프로젝트


```
iWuBi://<host>[?query]
iWuBi:///path-style   ← host empty; first path segment is the action
```


| Host / action | Opens | 글쓰기 |
|---------------|-------|-------|
| `search` | Lookup tab, focus search | `q`, `word`, 또는 `name` pre-fills |
| `word`, `char`, `character` | Word detail (or search if query empty) | `q` / `word` / `name` = 캐릭터 |
| `quiz`, `test` | Learn → Daily Quiz | — |
| `favorites`, `favorite` | Settings → Favourites | — |
| `wrong`, `mistakes`, `wrongbook` | Wrong book | `record=<UUID>` → 1개의 기록 |
| `levels`, `level`, `codes` | Levels tab | — |
| `learn`, `study` | Learn tab | — |
| `typing`, `type`, `practice` | Typing tab | — |

## 예시


```
iWuBi://search?q=你好
iWuBi://word?q=好
iWuBi://quiz
iWuBi://wrong?record=550E8400-E29B-41D4-A716-446655440000
iWuBi://levels
iWuBi://typing
```


## 홈 화면 빠른 행동

** 4 ** ** 설정 → 홈 화면 단축 **: `iWuBi://` , `iwubi` , `search` , `q` , `word` , `name` , `word` . ** 및 ** 리뷰**는 빠른 행동 만합니다.

[경찰](..) · [FAQ](../faq) · [Privacy](../privacy)

</section>
<section lang="ru" markdown="1">

iWuBi поддерживает ** `iWuBi://` ** (схема `iwubi` ) глубокие ссылки - открытый поиск, ежедневная викторина, фавориты, неправильная книга, уровни длины кода, хаб обучения или практика набора текста из Safari, ярлыки, виджеты или другое приложение.

## Протокол


```
iWuBi://<host>[?query]
iWuBi:///path-style   ← host empty; first path segment is the action
```


| Host / action | Opens | Запрос |
|---------------|-------|-------|
| `search` | Lookup tab, focus search | "q", "word" или "name" pre-fills |
| `word`, `char`, `character` | Word detail (or search if query empty) | «q» / «слово» / «имя» = символ |
| `quiz`, `test` | Learn → Daily Quiz | — |
| `favorites`, `favorite` | Settings → Favourites | — |
| `wrong`, `mistakes`, `wrongbook` | Wrong book | «record=<UUID>» — одна запись |
| `levels`, `level`, `codes` | Levels tab | — |
| `learn`, `study` | Learn tab | — |
| `typing`, `type`, `practice` | Typing tab | — |

## Примеры


```
iWuBi://search?q=你好
iWuBi://word?q=好
iWuBi://quiz
iWuBi://wrong?record=550E8400-E29B-41D4-A716-446655440000
iWuBi://levels
iWuBi://typing
```


## Домой Экран Быстрые действия

До **4** в **Настройки → Ярлыки домашнего экрана **: `iWuBi://` , `iwubi` , `search` , `q` , `word` , `name` , `word` . **Обратная связь** и **обзор** являются только быстрыми действиями.

[Назад к обзору] (..) · [FAQ] (../faq) · [Privacy] (../privacy)

</section>
<section lang="th" markdown="1">

IWuBII รองรับ... `iWuBi://` BAR ~ (กรณีของ sign-connect scheme           ) ลิงก์ลึก — เปิดการค้นหา, ทดสอบประจําวัน, ชื่นชอบ, ผิดเล่ม, เรียนเลขฐานรากหรือพิมพ์คําสั่งจาก Safari, ปุ่มพิมพ์ลัด, วิดเจ็ต, หรือโปรแกรมอื่น ๆ

## โพรโทคอล


```
iWuBi://<host>[?query]
iWuBi:///path-style   ← host empty; first path segment is the action
```


| Host / action | Opens | สืบค้น |
|---------------|-------|-------|
| `search` | Lookup tab, focus search | คือ (มะลาอิกะฮฺ) ผู้ทรงเกียรติเป็นผู้เฝ้าติดตาม |
| `word`, `char`, `character` | Word detail (or search if query empty) | # ชื่อ # |
| `quiz`, `test` | Learn → Daily Quiz | — |
| `favorites`, `favorite` | Settings → Favourites | — |
| `wrong`, `mistakes`, `wrongbook` | Wrong book | บันทึก=''''หนึ่งแผ่น |
| `levels`, `level`, `codes` | Levels tab | — |
| `learn`, `study` | Learn tab | — |
| `typing`, `type`, `practice` | Typing tab | — |

## ตัวอย่าง


```
iWuBi://search?q=你好
iWuBi://word?q=好
iWuBi://quiz
iWuBi://wrong?record=550E8400-E29B-41D4-A716-446655440000
iWuBi://levels
iWuBi://typing
```


## การกระทําด่วนของจอส่วนตัว

เพิ่มถึง ** 4 ** ใน ** การตั้งค่า ปุ่มพิมพ์ลัดจอจอส่วนตัว ~: `iWuBi://` BAR   BAR `iwubi` /C6                    ///// BAR    BAR        BAR    BAR       BAR

[Tack to Broups](. ) สืบค้นเมื่อ 22 พฤษภาคม พ.ศ.

</section>
<section lang="de" markdown="1">

iWuBi unterstützt ** `iWuBi://` ** (case-insensitive scheme `iwubi` ) tiefe Links — offenes Nachschlagen, tägliches Quiz, Favoriten, falsches Buch, Codelängenstufen, Lernhub oder Tippübung aus Safari, Shortcuts, Widgets oder einer anderen App.

## Protokoll


```
iWuBi://<host>[?query]
iWuBi:///path-style   ← host empty; first path segment is the action
```


| Host / action | Opens | Abfrage |
|---------------|-------|-------|
| `search` | Lookup tab, focus search | `q`, `word` oder `name` pre-fills |
| `word`, `char`, `character` | Word detail (or search if query empty) | `q` / `word` / `name` = Zeichen |
| `quiz`, `test` | Learn → Daily Quiz | — |
| `favorites`, `favorite` | Settings → Favourites | — |
| `wrong`, `mistakes`, `wrongbook` | Wrong book | `record=<UUID> → ein Datensatz |
| `levels`, `level`, `codes` | Levels tab | — |
| `learn`, `study` | Learn tab | — |
| `typing`, `type`, `practice` | Typing tab | — |

## Beispiele


```
iWuBi://search?q=你好
iWuBi://word?q=好
iWuBi://quiz
iWuBi://wrong?record=550E8400-E29B-41D4-A716-446655440000
iWuBi://levels
iWuBi://typing
```


## Home Bildschirm Schnelle Aktionen

Bis zu **4** in **Einstellungen → Home Screen Shortcuts **: `iWuBi://` , `iwubi` , `search` , `q` , `word` , `name` , `word` . **Feedback** und **review** sind nur Quick Action.

[Zurück zur Übersicht](..) · [FAQ](../faq) · [Privacy](../privacy]

</section>
<section lang="fr" markdown="1">

iWuBi prend en charge ** `iWuBi://` ** (case-insensibilise scheme `iwubi` ) liens profonds — recherche ouverte, quiz quotidien, favoris, mauvais livre, niveaux de longueur de code, apprendre le hub ou la pratique de dactylographie de Safari, Raccourcis, widgets, ou une autre application.

## Protocole


```
iWuBi://<host>[?query]
iWuBi:///path-style   ← host empty; first path segment is the action
```


| Host / action | Opens | Demande |
|---------------|-------|-------|
| `search` | Lookup tab, focus search | `q`, `word` ou `name` pré-remplis |
| `word`, `char`, `character` | Word detail (or search if query empty) | `q` / `word` / `name` = caractère |
| `quiz`, `test` | Learn → Daily Quiz | — |
| `favorites`, `favorite` | Settings → Favourites | — |
| `wrong`, `mistakes`, `wrongbook` | Wrong book | `registr=<UUID>` → un enregistrement |
| `levels`, `level`, `codes` | Levels tab | — |
| `learn`, `study` | Learn tab | — |
| `typing`, `type`, `practice` | Typing tab | — |

## Exemples


```
iWuBi://search?q=你好
iWuBi://word?q=好
iWuBi://quiz
iWuBi://wrong?record=550E8400-E29B-41D4-A716-446655440000
iWuBi://levels
iWuBi://typing
```


## Actions rapides de l'écran d'accueil

Jusqu'à **4** dans **Paramètres → raccourcis d'écran d'accueil**: `iWuBi://` , `iwubi` , `search` , `q` , `word` , `name` , `word` . **Feedback** et **review** ne sont que des actions rapides.

[Retour à l'aperçu](..) · [FAQ](../faq) · [Confidentialité](../privacité)

</section>
<section lang="tr" markdown="1">

iWuBi, ** `iWuBi://` ** (case-in sensitive program `iwubi` ) derin bağlantılar - açık göz atın, günlük test, favoriler, yanlış kitap, kod uzunluğu seviyeleri, Safari, kısa kesimler, widgets veya başka bir uygulamadan hub veya yazma.

## Protokol Protokolü


```
iWuBi://<host>[?query]
iWuBi:///path-style   ← host empty; first path segment is the action
```


| Host / action | Opens | Sorgu Sorgulama |
|---------------|-------|-------|
| `search` | Lookup tab, focus search | "q", "word" ya da "isim" öncesi |
| `word`, `char`, `character` | Word detail (or search if query empty) | "q" / "word" / "name" = karakter |
| `quiz`, `test` | Learn → Daily Quiz | — |
| `favorites`, `favorite` | Settings → Favourites | — |
| `wrong`, `mistakes`, `wrongbook` | Wrong book | "record=<UUID>" → bir rekor |
| `levels`, `level`, `codes` | Levels tab | — |
| `learn`, `study` | Learn tab | — |
| `typing`, `type`, `practice` | Typing tab | — |

## Örnekler


```
iWuBi://search?q=你好
iWuBi://word?q=好
iWuBi://quiz
iWuBi://wrong?record=550E8400-E29B-41D4-A716-446655440000
iWuBi://levels
iWuBi://typing
```


## Home Screen Quick Actions

**4** in **Settings → Home Ekran kısayolları**: `iWuBi://` , `iwubi` , `q` , `word` , `name` , `word` . **Feedback** ve **

[Genellikle] (.) · [FAQ](./faq) · [Privacy] (./privacy)

</section>
