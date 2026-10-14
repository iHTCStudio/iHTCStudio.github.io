---
layout: doc
title: iArtOfWar — Shortcut Links
app_id: iArtOfWar
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: iartofwar:// deep links for iArtOfWar — passage, daily, recite, study, hunt, collections, themes, settings guides, and more.
---

<section lang="en" markdown="1">

iArtOfWar supports **`iartofwar://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
iartofwar://{host}?{params}
```

## Passages & authors

| URL | Opens |
|-----|-------|
| `iartofwar://passage?id={id}` | Passage detail |
| `iartofwar://couplet?id={id}` / `iartofwar://poem?id={id}` | Same as passage (compatibility) |
| `iartofwar://author?id={id}` | Author detail |
| `iartofwar://recite` / `iartofwar://recite?id={id}` | Recite flow |

## Discovery

| URL | Opens |
|-----|-------|
| `iartofwar://home` | Home |
| `iartofwar://daily` | Today’s Daily Stratagem |
| `iartofwar://random` | Random passage |
| `iartofwar://favorites` | Favorites |
| `iartofwar://famous` | Famous lines / stratagems |
| `iartofwar://search` / `iartofwar://search?q={query}` | Search |
| `iartofwar://study` | Strategy classroom |
| `iartofwar://hunt` | Hunt (寻谋); aliases `keyword-hunt` / `flyflower` |
| `iartofwar://mastered` | Mastered |
| `iartofwar://categories` / `iartofwar://categories?section=` | Browse (`theme`, `volume`, …) |
| `iartofwar://collection?id=` | Book collection (e.g. `sunzi`, `wujing`, `wuzi`; also `name=` / `theme=`) |
| `iartofwar://theme?id=` | Stratagem suite or volume (e.g. `wen-tao`, `winning`, `sunbin-a`) |
| `iartofwar://last-read` | Last read |
| `iartofwar://reading-history` | Reading history |
| `iartofwar://notes` | Notes |

## Settings & guides

| URL | Opens |
|-----|-------|
| `iartofwar://settings` | Settings |
| `iartofwar://usage-guide` | Usage guide |
| `iartofwar://widget-guide` | Widget guide |
| `iartofwar://shortcuts-guide` | Shortcuts guide |
| `iartofwar://feature-guide` | Replay onboarding |
| `iartofwar://feedback` | Feedback email |
| `iartofwar://in-app-review` | In-app / Store review entry |

## Examples

```
iartofwar://daily
iartofwar://passage?id=1
iartofwar://collection?id=wuzi
iartofwar://theme?id=wen-tao
iartofwar://study
iartofwar://hunt
```

Use these in the Shortcuts app, Home Screen quick actions, widgets, or Safari. See also in-app **Settings → Shortcuts Guide**.

</section>
<section lang="zh-CN" markdown="1">

爱兵法支持 **`iartofwar://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
iartofwar://{host}?{params}
```

## 篇目与作者

| URL | 打开 |
|-----|------|
| `iartofwar://passage?id={id}` | 篇目详情 |
| `iartofwar://couplet?id={id}` / `iartofwar://poem?id={id}` | 同上（兼容别名） |
| `iartofwar://author?id={id}` | 作者详情 |
| `iartofwar://recite` / `iartofwar://recite?id={id}` | 诵读 |

## 发现与学习

| URL | 打开 |
|-----|------|
| `iartofwar://home` | 首页 |
| `iartofwar://daily` | 每日一计 |
| `iartofwar://random` | 随机 |
| `iartofwar://favorites` | 收藏 |
| `iartofwar://famous` | 名句 / 名计 |
| `iartofwar://search` / `iartofwar://search?q={query}` | 搜索 |
| `iartofwar://study` | 谋略学堂 |
| `iartofwar://hunt` | 寻谋 |
| `iartofwar://mastered` | 已掌握 |
| `iartofwar://categories` / `iartofwar://categories?section=` | 分类 |
| `iartofwar://collection?id=` | 书目合集（如 `sunzi`、`wujing`、`wuzi`） |
| `iartofwar://theme?id=` | 计套或卷编（如 `wen-tao`、`winning`、`sunbin-a`） |
| `iartofwar://last-read` | 上次阅读 |
| `iartofwar://reading-history` | 浏览记录 |
| `iartofwar://notes` | 笔记 |

## 设置与教程

| URL | 打开 |
|-----|------|
| `iartofwar://settings` | 设置 |
| `iartofwar://usage-guide` | 使用说明 |
| `iartofwar://widget-guide` | 小组件指南 |
| `iartofwar://shortcuts-guide` | 快捷指南 |
| `iartofwar://feature-guide` | 重播功能引导 |
| `iartofwar://feedback` | 反馈邮件 |
| `iartofwar://in-app-review` | 评分入口 |

## 示例

```
iartofwar://daily
iartofwar://passage?id=1
iartofwar://collection?id=wuzi
iartofwar://theme?id=wen-tao
iartofwar://study
iartofwar://hunt
```

可在「快捷指令」、主屏快捷、小组件或 Safari 中使用。详见应用内 **设置 → 快捷指南**。

</section>
<section lang="zh-TW" markdown="1">

愛兵法支援 **`iartofwar://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複開啟。

## 連結格式

```
iartofwar://{host}?{params}
```

## 篇目與作者

| URL | 開啟 |
|-----|------|
| `iartofwar://passage?id={id}` | 篇目詳情 |
| `iartofwar://couplet?id={id}` / `iartofwar://poem?id={id}` | 同上（相容別名） |
| `iartofwar://author?id={id}` | 作者詳情 |
| `iartofwar://recite` / `iartofwar://recite?id={id}` | 誦讀 |

## 發現與學習

| URL | 開啟 |
|-----|------|
| `iartofwar://home` | 首頁 |
| `iartofwar://daily` | 每日一計 |
| `iartofwar://random` | 隨機 |
| `iartofwar://favorites` | 收藏 |
| `iartofwar://famous` | 名句 / 名計 |
| `iartofwar://search` / `iartofwar://search?q={query}` | 搜尋 |
| `iartofwar://study` | 謀略學堂 |
| `iartofwar://hunt` | 尋謀 |
| `iartofwar://mastered` | 已掌握 |
| `iartofwar://categories` / `iartofwar://categories?section=` | 分類 |
| `iartofwar://collection?id=` | 書目合集（如 `sunzi`、`wujing`、`wuzi`） |
| `iartofwar://theme?id=` | 計套或卷編（如 `wen-tao`、`winning`、`sunbin-a`） |
| `iartofwar://last-read` | 上次閱讀 |
| `iartofwar://reading-history` | 瀏覽記錄 |
| `iartofwar://notes` | 筆記 |

## 設定與教學

| URL | 開啟 |
|-----|------|
| `iartofwar://settings` | 設定 |
| `iartofwar://usage-guide` | 使用說明 |
| `iartofwar://widget-guide` | 小工具指南 |
| `iartofwar://shortcuts-guide` | 捷徑指南 |
| `iartofwar://feature-guide` | 重播功能引導 |
| `iartofwar://feedback` | 回饋郵件 |
| `iartofwar://in-app-review` | 評分入口 |

## 範例

```
iartofwar://daily
iartofwar://passage?id=1
iartofwar://collection?id=wuzi
iartofwar://theme?id=wen-tao
iartofwar://study
iartofwar://hunt
```

可在「捷徑」、主畫面捷徑、小工具或 Safari 中使用。詳見應用內 **設定 → 捷徑指南**。

</section>
<section lang="ja" markdown="1">

iArtOfWarは** `iartofwar://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
iartofwar://{host}?{params}
```


## パスポートと著者

| URL | 開く画面 |
|-----|-------|
| `iartofwar://passage?id={id}` | 章句の詳細 |
| `iartofwar://couplet?id={id}` / `iartofwar://poem?id={id}` | 通路と同じ(互換性) |
| `iartofwar://author?id={id}` | 作者の詳細 |
| `iartofwar://recite` / `iartofwar://recite?id={id}` | 誦読フロー |

## 発見

| URL | 開く画面 |
|-----|-------|
| `iartofwar://home` | ホーム |
| `iartofwar://daily` | 今日のデイリー・ストラテジーム |
| `iartofwar://random` | ランダムな章句 |
| `iartofwar://favorites` | お気に入り |
| `iartofwar://famous` | 有名なライン/支柱 |
| `iartofwar://search` / `iartofwar://search?q={query}` | 検索 |
| `iartofwar://study` | 戦略教室 |
| `iartofwar://hunt` | ハント (寻谋); エイリアス `keyword-hunt`/`flyflower` |
| `iartofwar://mastered` | マスタード |
| `iartofwar://categories` / `iartofwar://categories?section=` | ビュー (`theme`、`volume`、...) |
| `iartofwar://collection?id=` | ブックコレクション(例えば、`sunzi`、`wujing`、`wuzi`; も `name=`/`theme=`) |
| `iartofwar://theme?id=` | ストラテジームスイートまたはボリューム(例:`wen-tao`、`win`、`sunbin-a`) |
| `iartofwar://last-read` | 最後に読んだ項目 |
| `iartofwar://reading-history` | 閲覧履歴 |
| `iartofwar://notes` | ノート |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `iartofwar://settings` | 設定 |
| `iartofwar://usage-guide` | 使い方ガイド |
| `iartofwar://widget-guide` | ウィジェットガイド |
| `iartofwar://shortcuts-guide` | ショートカットガイド |
| `iartofwar://feature-guide` | オンボーディングの再生 |
| `iartofwar://feedback` | フィードバックメール |
| `iartofwar://in-app-review` | アプリ内／App Store レビュー |

## 例


```
iartofwar://daily
iartofwar://passage?id=1
iartofwar://collection?id=wuzi
iartofwar://theme?id=wen-tao
iartofwar://study
iartofwar://hunt
```


これらをショートカットアプリ、ホーム画面のクイックアクション、ウィジェット、またはSafariで使用してください。 アプリ内設定 → ショートカットガイド** も参照してください。

</section>
<section lang="ko" markdown="1">

iArtOfWar 지원 ** `iartofwar://` ** 단축키 링크 (URL 계획). 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
iartofwar://{host}?{params}
```


## 책임 & 저자

| URL | 열리는 화면 |
|-----|-------|
| `iartofwar://passage?id={id}` | 구절 상세 |
| `iartofwar://couplet?id={id}` / `iartofwar://poem?id={id}` | 통행과 같 ( 겸용성) |
| `iartofwar://author?id={id}` | 작가 상세 |
| `iartofwar://recite` / `iartofwar://recite?id={id}` | 낭독 흐름 |

## 탐색

| URL | 열리는 화면 |
|-----|-------|
| `iartofwar://home` | 홈 |
| `iartofwar://daily` | 오늘의 매일 Stratagem |
| `iartofwar://random` | 무작위 구절 |
| `iartofwar://favorites` | 즐겨찾기 |
| `iartofwar://famous` | 유명한 선 / stratagems |
| `iartofwar://search` / `iartofwar://search?q={query}` | 검색 |
| `iartofwar://study` | 전략 교실 |
| `iartofwar://hunt` | 헌트 (fly); aliases `keyword-hunt`/`flyflower` |
| `iartofwar://mastered` | 인기있는 |
| `iartofwar://categories` / `iartofwar://categories?section=` | 검색 (`theme`, `volume`, ...) |
| `iartofwar://collection?id=` | 책 수집 (예 : `sunzi`, `wujing`, `wuzi`, `name=`/`theme=`) |
| `iartofwar://theme?id=` | Stratagem 스위트 또는 볼륨 (예 : `wen-tao`, `winning`, `sunbin-a`) |
| `iartofwar://last-read` | 마지막으로 읽은 항목 |
| `iartofwar://reading-history` | 읽기 기록 |
| `iartofwar://notes` | 메모 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `iartofwar://settings` | 설정 |
| `iartofwar://usage-guide` | 사용 가이드 |
| `iartofwar://widget-guide` | 위젯 가이드 |
| `iartofwar://shortcuts-guide` | 단축어 가이드 |
| `iartofwar://feature-guide` | 온보딩 다시 보기 |
| `iartofwar://feedback` | 피드백 이메일 |
| `iartofwar://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
iartofwar://daily
iartofwar://passage?id=1
iartofwar://collection?id=wuzi
iartofwar://theme?id=wen-tao
iartofwar://study
iartofwar://hunt
```


Shortcuts 앱, 홈 화면 빠른 행동, 위젯, 또는 사파리에서 이러한 사용. in-app**Settings → 단축키 가이드** 참조.

</section>
<section lang="ru" markdown="1">

iArtOfWar поддерживает ярлыки ** `iartofwar://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
iartofwar://{host}?{params}
```


## Проходы и авторы

| URL | Открывает |
|-----|-------|
| `iartofwar://passage?id={id}` | Страница отрывка |
| `iartofwar://couplet?id={id}` / `iartofwar://poem?id={id}` | Совместимость (Compatibility) |
| `iartofwar://author?id={id}` | Страница автора |
| `iartofwar://recite` / `iartofwar://recite?id={id}` | Режим чтения вслух |

## Обзор

| URL | Открывает |
|-----|-------|
| `iartofwar://home` | Главная |
| `iartofwar://daily` | Сегодняшняя ежедневная стратагема |
| `iartofwar://random` | Случайный отрывок |
| `iartofwar://favorites` | Избранное |
| `iartofwar://famous` | Знаменитые линии / стратагемы |
| `iartofwar://search` / `iartofwar://search?q={query}` | Поиск |
| `iartofwar://study` | Стратегический класс |
| `iartofwar://hunt` | Охота (`); псевдонимы «охота за ключевыми словами» / «флайфлауэр» |
| `iartofwar://mastered` | мастеринг |
| `iartofwar://categories` / `iartofwar://categories?section=` | Browse («тема», «объем», ...) |
| `iartofwar://collection?id=` | Сборник книг (например, "sunzi", "wujing", "wuzi"; также "name="/"theme=") |
| `iartofwar://theme?id=` | Комплект или объем Stratagem (например, "wen-tao", "winning", "sunbin-a") |
| `iartofwar://last-read` | Последнее прочитанное |
| `iartofwar://reading-history` | История чтения |
| `iartofwar://notes` | Заметки |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `iartofwar://settings` | Настройки |
| `iartofwar://usage-guide` | Руководство по использованию |
| `iartofwar://widget-guide` | Руководство по виджетам |
| `iartofwar://shortcuts-guide` | Руководство по «Командам» |
| `iartofwar://feature-guide` | Повторное знакомство |
| `iartofwar://feedback` | Письмо с отзывом |
| `iartofwar://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
iartofwar://daily
iartofwar://passage?id=1
iartofwar://collection?id=wuzi
iartofwar://theme?id=wen-tao
iartofwar://study
iartofwar://hunt
```


Используйте их в приложении Shortcuts, быстрых действиях Home Screen, виджетах или Safari. См. также in-app **Settings → Shortcuts Guide**.

</section>
<section lang="th" markdown="1">

iArtofwar รองรับ ** `iartofwar://` BAR * ลิงก์ลัด (URL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
iartofwar://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `iartofwar://passage?id={id}` | รายละเอียดข้อความ |
| `iartofwar://couplet?id={id}` / `iartofwar://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `iartofwar://author?id={id}` | รายละเอียดผู้แต่ง |
| `iartofwar://recite` / `iartofwar://recite?id={id}` | โฟลว์การท่อง |

## ค้นพบ

| URL | เปิด |
|-----|-------|
| `iartofwar://home` | หน้าแรก |
| `iartofwar://daily` | ทุก วัน นี้ |
| `iartofwar://random` | ข้อความแบบสุ่ม |
| `iartofwar://favorites` | รายการโปรด |
| `iartofwar://famous` | เส้น เสียง ที่ มี ชื่อ เสียง / เส้น เสียง |
| `iartofwar://search` / `iartofwar://search?q={query}` | ค้นหา |
| `iartofwar://study` | ห้องเรียนช่างวางแผน |
| `iartofwar://hunt` | ล่า (寻谋; สืบค้นเมื่อ 'คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน' |
| `iartofwar://mastered` | สําเร็จการศึกษาแล้ว |
| `iartofwar://categories` / `iartofwar://categories?section=` | เรียกดู ('theme', 'volume', ...) |
| `iartofwar://collection?id=` | คอลเลกชันหนังสือ (e.g. `Sunzi', 'woujing', 'wuzi'; และยังมี 'ชื่อ=' / eme=') |
| `iartofwar://theme?id=` | statagem set หรือ volum (e.g. usn-tao', ~ ชนะ ', 'Sunbin-a') |
| `iartofwar://last-read` | รายการที่อ่านล่าสุด |
| `iartofwar://reading-history` | ประวัติการอ่าน |
| `iartofwar://notes` | บันทึก |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `iartofwar://settings` | การตั้งค่า |
| `iartofwar://usage-guide` | คู่มือการใช้งาน |
| `iartofwar://widget-guide` | คู่มือวิดเจ็ต |
| `iartofwar://shortcuts-guide` | คู่มือทางลัด |
| `iartofwar://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `iartofwar://feedback` | อีเมลข้อเสนอแนะ |
| `iartofwar://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
iartofwar://daily
iartofwar://passage?id=1
iartofwar://collection?id=wuzi
iartofwar://theme?id=wen-tao
iartofwar://study
iartofwar://hunt
```


ใช้เหล่านี้ในโปรแกรมปุ่มพิมพ์ลัด, การกระทําของหน้าจอส่วนตัวอย่างรวดเร็ว, วิดเจ็ต, หรือ Saveri ดูใน-apps ด้วย

</section>
<section lang="de" markdown="1">

iArtOfWar unterstützt ** `iartofwar://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
iartofwar://{host}?{params}
```


## Passagen & Autoren

| URL | Öffnet |
|-----|-------|
| `iartofwar://passage?id={id}` | Passagen-Detail |
| `iartofwar://couplet?id={id}` / `iartofwar://poem?id={id}` | Wie Passage (Kompatibilität) |
| `iartofwar://author?id={id}` | Autorendetail |
| `iartofwar://recite` / `iartofwar://recite?id={id}` | Rezitationsablauf |

## Entdecken

| URL | Öffnet |
|-----|-------|
| `iartofwar://home` | Startseite |
| `iartofwar://daily` | Das heutige Daily Stratagem |
| `iartofwar://random` | Zufällige Passage |
| `iartofwar://favorites` | Favoriten |
| `iartofwar://famous` | Berühmte Linien / Strategemen |
| `iartofwar://search` / `iartofwar://search?q={query}` | Suche |
| `iartofwar://study` | Strategie Klassenzimmer |
| `iartofwar://hunt` | Jagd (寻谋); alias `keyword-hunt` / `flyflower` |
| `iartofwar://mastered` | Beherrscht |
| `iartofwar://categories` / `iartofwar://categories?section=` | Browse (`Theme`, `Volume`, ...) |
| `iartofwar://collection?id=` | Buchsammlung (z.B. `sunzi`, `wujing`, `wuzi`; auch `name=` / `theme=`) |
| `iartofwar://theme?id=` | Stratagem Suite oder Volume (z.B. `wen-tao`, `winning`, `sunbin-a`) |
| `iartofwar://last-read` | Zuletzt gelesen |
| `iartofwar://reading-history` | Leseverlauf |
| `iartofwar://notes` | Notizen |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `iartofwar://settings` | Einstellungen |
| `iartofwar://usage-guide` | Nutzungsanleitung |
| `iartofwar://widget-guide` | Widget-Anleitung |
| `iartofwar://shortcuts-guide` | Kurzbefehle-Anleitung |
| `iartofwar://feature-guide` | Einführung erneut abspielen |
| `iartofwar://feedback` | Feedback-E-Mail |
| `iartofwar://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
iartofwar://daily
iartofwar://passage?id=1
iartofwar://collection?id=wuzi
iartofwar://theme?id=wen-tao
iartofwar://study
iartofwar://hunt
```


Verwenden Sie diese in der Shortcuts-App, den Schnellaktionen für den Startbildschirm, den Widgets oder Safari. Siehe auch In-App **Settings → Shortcuts Guide**.

</section>
<section lang="fr" markdown="1">

iArtOfWar prend en charge les liens de raccourci ** `iartofwar://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
iartofwar://{host}?{params}
```


## Passages et auteurs

| URL | Ouvre |
|-----|-------|
| `iartofwar://passage?id={id}` | Détail du passage |
| `iartofwar://couplet?id={id}` / `iartofwar://poem?id={id}` | Même chose que le passage (compatibilité) |
| `iartofwar://author?id={id}` | Détail de l’auteur |
| `iartofwar://recite` / `iartofwar://recite?id={id}` | Flux de récitation |

## Découverte

| URL | Ouvre |
|-----|-------|
| `iartofwar://home` | Accueil |
| `iartofwar://daily` | Aujourd'hui |
| `iartofwar://random` | Passage aléatoire |
| `iartofwar://favorites` | Favoris |
| `iartofwar://famous` | Lignes célèbres / stratagèmes |
| `iartofwar://search` / `iartofwar://search?q={query}` | Recherche |
| `iartofwar://study` | Salle de classe stratégique |
| `iartofwar://hunt` | Chasse () ; alias « chasse aux mots clés » / « fleurs volantes » |
| `iartofwar://mastered` | Maîtrise |
| `iartofwar://categories` / `iartofwar://categories?section=` | Parcourir (`theme`, `volume`, ...) |
| `iartofwar://collection?id=` | Collection de livres (par exemple `sunzi`, `wujing`, `wuzi`; aussi `name=` / `theme=`) |
| `iartofwar://theme?id=` | Suite ou volume Stratagem (par exemple "wen-tao", "winning", "sunbin-a") |
| `iartofwar://last-read` | Dernière lecture |
| `iartofwar://reading-history` | Historique de lecture |
| `iartofwar://notes` | Notes |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `iartofwar://settings` | Réglages |
| `iartofwar://usage-guide` | Guide d'utilisation |
| `iartofwar://widget-guide` | Guide des widgets |
| `iartofwar://shortcuts-guide` | Guide Raccourcis |
| `iartofwar://feature-guide` | Rejouer l’accueil |
| `iartofwar://feedback` | E-mail de commentaires |
| `iartofwar://in-app-review` | Avis in-app / App Store |

## Exemples


```
iartofwar://daily
iartofwar://passage?id=1
iartofwar://collection?id=wuzi
iartofwar://theme?id=wen-tao
iartofwar://study
iartofwar://hunt
```


Utilisez-les dans l'application Raccourcis, les actions rapides Home Screen, les widgets ou Safari. Voir aussi dans l'application **Paramètres → Guide des raccourcis**.

</section>
<section lang="tr" markdown="1">

iArtOfWar ** `iartofwar://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
iartofwar://{host}?{params}
```


## Geçişler ve yazarlar

| URL | Açar |
|-----|-------|
| `iartofwar://passage?id={id}` | Pasaj ayrıntısı |
| `iartofwar://couplet?id={id}` / `iartofwar://poem?id={id}` | Aynı geçiş (compatability) |
| `iartofwar://author?id={id}` | Yazar ayrıntısı |
| `iartofwar://recite` / `iartofwar://recite?id={id}` | Okuma akışı |

## Keşfet

| URL | Açar |
|-----|-------|
| `iartofwar://home` | Ana sayfa |
| `iartofwar://daily` | Bugünün Günlük Stratagem |
| `iartofwar://random` | Rastgele pasaj |
| `iartofwar://favorites` | Favoriler |
| `iartofwar://famous` | Ünlü çizgiler / stratagems |
| `iartofwar://search` / `iartofwar://search?q={query}` | Ara |
| `iartofwar://study` | Strateji sınıfı |
| `iartofwar://hunt` | Hunt (fly); alias "keyword-hunt" / "flyflower" |
| `iartofwar://mastered` | Mastered |
| `iartofwar://categories` / `iartofwar://categories?section=` | Göz ('theme', 'volume', ...) |
| `iartofwar://collection?id=` | Kitap koleksiyonu (e.g. ‘sunzi’, “wujing’, “wuzi’; aynı zamanda “isim=’ / “theme=’) |
| `iartofwar://theme?id=` | Stratagem süiti veya hacmi (e.g. “wen-tao”, "kazanan", "sunbin-a") |
| `iartofwar://last-read` | Son okunan |
| `iartofwar://reading-history` | Okuma geçmişi |
| `iartofwar://notes` | Notlar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `iartofwar://settings` | Ayarlar |
| `iartofwar://usage-guide` | Kullanım kılavuzu |
| `iartofwar://widget-guide` | Widget kılavuzu |
| `iartofwar://shortcuts-guide` | Kısayol kılavuzu |
| `iartofwar://feature-guide` | Tanıtımı yeniden oynat |
| `iartofwar://feedback` | Geri bildirim e-postası |
| `iartofwar://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
iartofwar://daily
iartofwar://passage?id=1
iartofwar://collection?id=wuzi
iartofwar://theme?id=wen-tao
iartofwar://study
iartofwar://hunt
```


Bunları kısa kesimlerde kullanın, Home Ekran hızlı eylemleri, widgets veya Safari. Ayrıca bakınız **Settings → Kısayollar Kılavuzu**.

</section>
