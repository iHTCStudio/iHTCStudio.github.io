---
layout: doc
title: iLunYu — Shortcut Links
app_id: iLunYu
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: ilunyu:// deep links for iLunYu — passage, daily, recite, study, hunt, themes, settings guides, and more.
---

<section lang="en" markdown="1">

iLunYu supports **`ilunyu://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
ilunyu://{host}?{params}
```

## Chapters & authors

| URL | Opens |
|-----|-------|
| `ilunyu://passage?id={id}` | Chapter detail |
| `ilunyu://couplet?id={id}` / `ilunyu://poem?id={id}` | Same as passage (compatibility) |
| `ilunyu://author?id={id}` | Author detail |
| `ilunyu://recite` | Recite flow |
| `ilunyu://recite?id={id}` | Open chapter and auto-recite |

## Discovery

| URL | Opens |
|-----|-------|
| `ilunyu://home` | Home tab |
| `ilunyu://daily` | Today’s Daily Verse |
| `ilunyu://random` | Random chapter |
| `ilunyu://favorites` | Favorites |
| `ilunyu://famous` | Famous lines |
| `ilunyu://search` / `ilunyu://search?q={query}` | Search |
| `ilunyu://study` | Study classroom |
| `ilunyu://hunt` | Hunt (寻章); aliases `keyword-hunt` / `flyflower` |
| `ilunyu://mastered` / `ilunyu://progress` | Mastered / progress |
| `ilunyu://categories` / `ilunyu://categories?section=` | Browse |
| `ilunyu://collection?id=lunyu` | Book collection (aliases `book` / `form`; also `name=`) |
| `ilunyu://theme?id=` | Theme or volume (e.g. `junzi`, `xue-er`; aliases `suite` / `volume`) |
| `ilunyu://last-read` | Last read |
| `ilunyu://reading-history` | Reading history |
| `ilunyu://notes` | Notes |

## Settings & guides

| URL | Opens |
|-----|-------|
| `ilunyu://settings` | Settings |
| `ilunyu://usage-guide` | Usage guide |
| `ilunyu://widget-guide` | Widget guide |
| `ilunyu://shortcuts-guide` | Shortcuts guide |
| `ilunyu://feature-guide` | Replay onboarding |
| `ilunyu://feedback` | Feedback email |
| `ilunyu://in-app-review` | In-app / Store review entry |

## Examples

```
ilunyu://daily
ilunyu://passage?id=1
ilunyu://recite?id=20
ilunyu://theme?id=junzi
ilunyu://study
ilunyu://hunt
```

Use these in the Shortcuts app, Home Screen quick actions, widgets, or Safari. See also in-app **Settings → Shortcuts Guide**.

</section>
<section lang="zh-CN" markdown="1">

爱论语支持 **`ilunyu://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
ilunyu://{host}?{params}
```

## 章句与作者

| URL | 打开 |
|-----|------|
| `ilunyu://passage?id={id}` | 章句详情 |
| `ilunyu://couplet?id={id}` / `ilunyu://poem?id={id}` | 同上（兼容别名） |
| `ilunyu://author?id={id}` | 作者详情 |
| `ilunyu://recite` | 诵读 |
| `ilunyu://recite?id={id}` | 打开章句并自动诵读 |

## 发现与学习

| URL | 打开 |
|-----|------|
| `ilunyu://home` | 首页 |
| `ilunyu://daily` | 每日一则 |
| `ilunyu://random` | 随机 |
| `ilunyu://favorites` | 收藏 |
| `ilunyu://famous` | 名句 |
| `ilunyu://search` / `ilunyu://search?q={query}` | 搜索 |
| `ilunyu://study` | 习礼学堂 |
| `ilunyu://hunt` | 寻章（别名 `keyword-hunt` / `flyflower`） |
| `ilunyu://mastered` / `ilunyu://progress` | 已掌握 / 进度 |
| `ilunyu://categories` / `ilunyu://categories?section=` | 分类 |
| `ilunyu://collection?id=lunyu` | 书目合集 |
| `ilunyu://theme?id=` | 主题或篇目（如 `junzi`、`xue-er`） |
| `ilunyu://last-read` | 上次阅读 |
| `ilunyu://reading-history` | 浏览记录 |
| `ilunyu://notes` | 笔记 |

## 设置与教程

| URL | 打开 |
|-----|------|
| `ilunyu://settings` | 设置 |
| `ilunyu://usage-guide` | 使用说明 |
| `ilunyu://widget-guide` | 小组件指南 |
| `ilunyu://shortcuts-guide` | 快捷指南 |
| `ilunyu://feature-guide` | 重播功能引导 |
| `ilunyu://feedback` | 反馈邮件 |
| `ilunyu://in-app-review` | 评分入口 |

## 示例

```
ilunyu://daily
ilunyu://passage?id=1
ilunyu://recite?id=20
ilunyu://theme?id=junzi
ilunyu://study
ilunyu://hunt
```

可在「快捷指令」、主屏快捷、小组件或 Safari 中使用。详见应用内 **设置 → 快捷指南**。

</section>
<section lang="zh-TW" markdown="1">

愛論語支援 **`ilunyu://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複開啟。

## 連結格式

```
ilunyu://{host}?{params}
```

## 章句與作者

| URL | 開啟 |
|-----|------|
| `ilunyu://passage?id={id}` | 章句詳情 |
| `ilunyu://couplet?id={id}` / `ilunyu://poem?id={id}` | 同上（相容別名） |
| `ilunyu://author?id={id}` | 作者詳情 |
| `ilunyu://recite` | 誦讀 |
| `ilunyu://recite?id={id}` | 打開章句並自動誦讀 |

## 發現與學習

| URL | 開啟 |
|-----|------|
| `ilunyu://home` | 首頁 |
| `ilunyu://daily` | 每日一則 |
| `ilunyu://random` | 隨機 |
| `ilunyu://favorites` | 收藏 |
| `ilunyu://famous` | 名句 |
| `ilunyu://search` / `ilunyu://search?q={query}` | 搜尋 |
| `ilunyu://study` | 習禮學堂 |
| `ilunyu://hunt` | 尋章（別名 `keyword-hunt` / `flyflower`） |
| `ilunyu://mastered` / `ilunyu://progress` | 已掌握 / 進度 |
| `ilunyu://categories` / `ilunyu://categories?section=` | 分類 |
| `ilunyu://collection?id=lunyu` | 書目合集 |
| `ilunyu://theme?id=` | 主題或篇目（如 `junzi`、`xue-er`） |
| `ilunyu://last-read` | 上次閱讀 |
| `ilunyu://reading-history` | 瀏覽記錄 |
| `ilunyu://notes` | 筆記 |

## 設定與教學

| URL | 開啟 |
|-----|------|
| `ilunyu://settings` | 設定 |
| `ilunyu://usage-guide` | 使用說明 |
| `ilunyu://widget-guide` | 小工具指南 |
| `ilunyu://shortcuts-guide` | 捷徑指南 |
| `ilunyu://feature-guide` | 重播功能引導 |
| `ilunyu://feedback` | 回饋郵件 |
| `ilunyu://in-app-review` | 評分入口 |

## 範例

```
ilunyu://daily
ilunyu://passage?id=1
ilunyu://recite?id=20
ilunyu://theme?id=junzi
ilunyu://study
ilunyu://hunt
```

可在「捷徑」、主畫面捷徑、小工具或 Safari 中使用。詳見應用內 **設定 → 捷徑指南**。

</section>
<section lang="ja" markdown="1">

iLunYuは** `ilunyu://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
ilunyu://{host}?{params}
```


## 章と著者

| URL | 開く画面 |
|-----|-------|
| `ilunyu://passage?id={id}` | 章の詳細 |
| `ilunyu://couplet?id={id}` / `ilunyu://poem?id={id}` | 通路と同じ(互換性) |
| `ilunyu://author?id={id}` | 作者の詳細 |
| `ilunyu://recite` | 誦読フロー |
| `ilunyu://recite?id={id}` | 章を開き、自動recite |

## 発見

| URL | 開く画面 |
|-----|-------|
| `ilunyu://home` | ホームタブ |
| `ilunyu://daily` | 本日のデイリーVerse |
| `ilunyu://random` | ランダムチャプター |
| `ilunyu://favorites` | お気に入り |
| `ilunyu://famous` | 名句一覧 |
| `ilunyu://search` / `ilunyu://search?q={query}` | 検索 |
| `ilunyu://study` | 学習教室 |
| `ilunyu://hunt` | Hunt(寻)。aliases`keyword-hunt`/`flyflower` |
| `ilunyu://mastered` / `ilunyu://progress` | マスタード/進行 |
| `ilunyu://categories` / `ilunyu://categories?section=` | ブラウズ |
| `ilunyu://collection?id=lunyu` | ブックコレクション(別名 `book`/`form`;`name=`) |
| `ilunyu://theme?id=` | テーマまたはボリューム(例えば `junzi`、`xue-er`; aliases`suite`/`volume`) |
| `ilunyu://last-read` | 最後に読んだ項目 |
| `ilunyu://reading-history` | 閲覧履歴 |
| `ilunyu://notes` | ノート |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `ilunyu://settings` | 設定 |
| `ilunyu://usage-guide` | 使い方ガイド |
| `ilunyu://widget-guide` | ウィジェットガイド |
| `ilunyu://shortcuts-guide` | ショートカットガイド |
| `ilunyu://feature-guide` | オンボーディングの再生 |
| `ilunyu://feedback` | フィードバックメール |
| `ilunyu://in-app-review` | アプリ内／App Store レビュー |

## 例


```
ilunyu://daily
ilunyu://passage?id=1
ilunyu://recite?id=20
ilunyu://theme?id=junzi
ilunyu://study
ilunyu://hunt
```


これらをショートカットアプリ、ホーム画面のクイックアクション、ウィジェット、またはSafariで使用してください。 アプリ内設定 → ショートカットガイド** も参照してください。

</section>
<section lang="ko" markdown="1">

iLunYu는 ** `ilunyu://` ** 단축키 링크 (URL 계획)를 지원합니다. 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
ilunyu://{host}?{params}
```


## 장 & 저자

| URL | 열리는 화면 |
|-----|-------|
| `ilunyu://passage?id={id}` | 장 세부 사항 |
| `ilunyu://couplet?id={id}` / `ilunyu://poem?id={id}` | 통행과 같 ( 겸용성) |
| `ilunyu://author?id={id}` | 작가 상세 |
| `ilunyu://recite` | 낭독 흐름 |
| `ilunyu://recite?id={id}` | 챕터 및 자동 인용 |

## 탐색

| URL | 열리는 화면 |
|-----|-------|
| `ilunyu://home` | 홈 탭 |
| `ilunyu://daily` | 오늘의 일일 Verse |
| `ilunyu://random` | 무작위 장 |
| `ilunyu://favorites` | 즐겨찾기 |
| `ilunyu://famous` | 명구 목록 |
| `ilunyu://search` / `ilunyu://search?q={query}` | 검색 |
| `ilunyu://study` | 학습 교실 |
| `ilunyu://hunt` | 헌트 (fly); aliases `keyword-hunt`/`flyflower` |
| `ilunyu://mastered` / `ilunyu://progress` | 마스터 / 진행 |
| `ilunyu://categories` / `ilunyu://categories?section=` | 둘러보기 |
| `ilunyu://collection?id=lunyu` | 책 모음 (aliases `book` / `form`; 또한 `name=`) |
| `ilunyu://theme?id=` | 테마 또는 볼륨 (예 : `junzi`, `xue-er`; 별칭 `suite`/`volume`) |
| `ilunyu://last-read` | 마지막으로 읽은 항목 |
| `ilunyu://reading-history` | 읽기 기록 |
| `ilunyu://notes` | 메모 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `ilunyu://settings` | 설정 |
| `ilunyu://usage-guide` | 사용 가이드 |
| `ilunyu://widget-guide` | 위젯 가이드 |
| `ilunyu://shortcuts-guide` | 단축어 가이드 |
| `ilunyu://feature-guide` | 온보딩 다시 보기 |
| `ilunyu://feedback` | 피드백 이메일 |
| `ilunyu://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
ilunyu://daily
ilunyu://passage?id=1
ilunyu://recite?id=20
ilunyu://theme?id=junzi
ilunyu://study
ilunyu://hunt
```


Shortcuts 앱, 홈 화면 빠른 행동, 위젯, 또는 사파리에서 이러한 사용. in-app**Settings → 단축키 가이드** 참조.

</section>
<section lang="ru" markdown="1">

iLunYu поддерживает ярлыки ** `ilunyu://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
ilunyu://{host}?{params}
```


## Главы и авторы

| URL | Открывает |
|-----|-------|
| `ilunyu://passage?id={id}` | Глава подробная |
| `ilunyu://couplet?id={id}` / `ilunyu://poem?id={id}` | Совместимость (Compatibility) |
| `ilunyu://author?id={id}` | Страница автора |
| `ilunyu://recite` | Режим чтения вслух |
| `ilunyu://recite?id={id}` | Открытая глава и автоцитирование |

## Обзор

| URL | Открывает |
|-----|-------|
| `ilunyu://home` | Вкладка «Главная» |
| `ilunyu://daily` | Ежедневный стих сегодня |
| `ilunyu://random` | Случайная глава |
| `ilunyu://favorites` | Избранное |
| `ilunyu://famous` | Знаменитые строки |
| `ilunyu://search` / `ilunyu://search?q={query}` | Поиск |
| `ilunyu://study` | Учебный класс |
| `ilunyu://hunt` | Охота (`); псевдонимы «охота за ключевыми словами» / «флайфлауэр» |
| `ilunyu://mastered` / `ilunyu://progress` | Мастеринг / Прогресс |
| `ilunyu://categories` / `ilunyu://categories?section=` | Обзор |
| `ilunyu://collection?id=lunyu` | Сборник книг (ссылки "книга" / "форма"; также "имя =") |
| `ilunyu://theme?id=` | Тема или объем (например, "junzi", "xue-er"; псевдонимы "suite"/"volume") |
| `ilunyu://last-read` | Последнее прочитанное |
| `ilunyu://reading-history` | История чтения |
| `ilunyu://notes` | Заметки |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `ilunyu://settings` | Настройки |
| `ilunyu://usage-guide` | Руководство по использованию |
| `ilunyu://widget-guide` | Руководство по виджетам |
| `ilunyu://shortcuts-guide` | Руководство по «Командам» |
| `ilunyu://feature-guide` | Повторное знакомство |
| `ilunyu://feedback` | Письмо с отзывом |
| `ilunyu://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
ilunyu://daily
ilunyu://passage?id=1
ilunyu://recite?id=20
ilunyu://theme?id=junzi
ilunyu://study
ilunyu://hunt
```


Используйте их в приложении Shortcuts, быстрых действиях Home Screen, виджетах или Safari. См. также in-app **Settings → Shortcuts Guide**.

</section>
<section lang="th" markdown="1">

iLunYu รองรับ~ `ilunyu://` BAR * ลิงก์ลัด (RUL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
ilunyu://{host}?{params}
```


## บทและผู้เขียน

| URL | เปิด |
|-----|-------|
| `ilunyu://passage?id={id}` | รายละเอียดในบท |
| `ilunyu://couplet?id={id}` / `ilunyu://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `ilunyu://author?id={id}` | รายละเอียดผู้แต่ง |
| `ilunyu://recite` | โฟลว์การท่อง |
| `ilunyu://recite?id={id}` | เปิดและปรับอัตโนมัติ |

## ค้นพบ

| URL | เปิด |
|-----|-------|
| `ilunyu://home` | แท็บหน้าแรก |
| `ilunyu://daily` | ข้อ คัมภีร์ ประจํา วัน |
| `ilunyu://random` | หมุน & 90 |
| `ilunyu://favorites` | รายการโปรด |
| `ilunyu://famous` | บรรทัดขึ้นชื่อ |
| `ilunyu://search` / `ilunyu://search?q={query}` | ค้นหา |
| `ilunyu://study` | ห้องเรียนเรียน |
| `ilunyu://hunt` | ล่า (寻章; สืบค้นเมื่อ 'คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน' |
| `ilunyu://mastered` / `ilunyu://progress` | ประมวลผล / คืบหน้า |
| `ilunyu://categories` / `ilunyu://categories?section=` | เรียกดู |
| `ilunyu://collection?id=lunyu` | คอลเลกชันหนังสือ (อัลบั้ม ''' / ฟอร์ม'; และยัง 'ชื่อ=') |
| `ilunyu://theme?id=` | ชุดตกแต่ง หรือ ระดับเสียง (เช่น 'hunzi', 'xue-er'; นามแฝง an suffe' / 'volume') |
| `ilunyu://last-read` | รายการที่อ่านล่าสุด |
| `ilunyu://reading-history` | ประวัติการอ่าน |
| `ilunyu://notes` | บันทึก |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `ilunyu://settings` | การตั้งค่า |
| `ilunyu://usage-guide` | คู่มือการใช้งาน |
| `ilunyu://widget-guide` | คู่มือวิดเจ็ต |
| `ilunyu://shortcuts-guide` | คู่มือทางลัด |
| `ilunyu://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `ilunyu://feedback` | อีเมลข้อเสนอแนะ |
| `ilunyu://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
ilunyu://daily
ilunyu://passage?id=1
ilunyu://recite?id=20
ilunyu://theme?id=junzi
ilunyu://study
ilunyu://hunt
```


ใช้เหล่านี้ในโปรแกรมปุ่มพิมพ์ลัด, การกระทําของหน้าจอส่วนตัวอย่างรวดเร็ว, วิดเจ็ต, หรือ Saveri ดูใน-apps ด้วย

</section>
<section lang="de" markdown="1">

iLunYu unterstützt ** `ilunyu://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
ilunyu://{host}?{params}
```


## Kapitel & Autoren

| URL | Öffnet |
|-----|-------|
| `ilunyu://passage?id={id}` | Einzelheiten des Kapitels |
| `ilunyu://couplet?id={id}` / `ilunyu://poem?id={id}` | Wie Passage (Kompatibilität) |
| `ilunyu://author?id={id}` | Autorendetail |
| `ilunyu://recite` | Rezitationsablauf |
| `ilunyu://recite?id={id}` | Offenes Kapitel und Auto-Recite |

## Entdecken

| URL | Öffnet |
|-----|-------|
| `ilunyu://home` | Register „Start“ |
| `ilunyu://daily` | Der heutige tägliche Vers |
| `ilunyu://random` | Zufallskapitel |
| `ilunyu://favorites` | Favoriten |
| `ilunyu://famous` | Berühmte Zeilen |
| `ilunyu://search` / `ilunyu://search?q={query}` | Suche |
| `ilunyu://study` | Studienraum |
| `ilunyu://hunt` | Jagd (寻章); alias `keyword-hunt` / `flyflower` |
| `ilunyu://mastered` / `ilunyu://progress` | Beherrscht/Fortschritt |
| `ilunyu://categories` / `ilunyu://categories?section=` | Durchsuchen |
| `ilunyu://collection?id=lunyu` | Buchsammlung (alias `book` / `form`; auch `name=`) |
| `ilunyu://theme?id=` | Thema oder Volumen (z.B. `junzi`, `xue-er`; aliases `suite` / `volume`) |
| `ilunyu://last-read` | Zuletzt gelesen |
| `ilunyu://reading-history` | Leseverlauf |
| `ilunyu://notes` | Notizen |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `ilunyu://settings` | Einstellungen |
| `ilunyu://usage-guide` | Nutzungsanleitung |
| `ilunyu://widget-guide` | Widget-Anleitung |
| `ilunyu://shortcuts-guide` | Kurzbefehle-Anleitung |
| `ilunyu://feature-guide` | Einführung erneut abspielen |
| `ilunyu://feedback` | Feedback-E-Mail |
| `ilunyu://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
ilunyu://daily
ilunyu://passage?id=1
ilunyu://recite?id=20
ilunyu://theme?id=junzi
ilunyu://study
ilunyu://hunt
```


Verwenden Sie diese in der Shortcuts-App, den Schnellaktionen für den Startbildschirm, den Widgets oder Safari. Siehe auch In-App **Settings → Shortcuts Guide**.

</section>
<section lang="fr" markdown="1">

iLunYu prend en charge les liens de raccourci ** `ilunyu://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
ilunyu://{host}?{params}
```


## Chapitres & auteurs

| URL | Ouvre |
|-----|-------|
| `ilunyu://passage?id={id}` | Détail du chapitre |
| `ilunyu://couplet?id={id}` / `ilunyu://poem?id={id}` | Même chose que le passage (compatibilité) |
| `ilunyu://author?id={id}` | Détail de l’auteur |
| `ilunyu://recite` | Flux de récitation |
| `ilunyu://recite?id={id}` | Ouvrir le chapitre et la lecture automatique |

## Découverte

| URL | Ouvre |
|-----|-------|
| `ilunyu://home` | Onglet Accueil |
| `ilunyu://daily` | Aujourd'hui verset quotidien |
| `ilunyu://random` | Chapitre aléatoire |
| `ilunyu://favorites` | Favoris |
| `ilunyu://famous` | Vers célèbres |
| `ilunyu://search` / `ilunyu://search?q={query}` | Recherche |
| `ilunyu://study` | Cours |
| `ilunyu://hunt` | Chasse () ; alias « chasse aux mots clés » / « fleurs volantes » |
| `ilunyu://mastered` / `ilunyu://progress` | Maîtrise / progrès |
| `ilunyu://categories` / `ilunyu://categories?section=` | Parcourir |
| `ilunyu://collection?id=lunyu` | Collection de livres (alias `book` / `form`; aussi `name=`) |
| `ilunyu://theme?id=` | Thème ou volume (par exemple `junzi`, `xue-er`; alias `suite` / `volume`) |
| `ilunyu://last-read` | Dernière lecture |
| `ilunyu://reading-history` | Historique de lecture |
| `ilunyu://notes` | Notes |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `ilunyu://settings` | Réglages |
| `ilunyu://usage-guide` | Guide d'utilisation |
| `ilunyu://widget-guide` | Guide des widgets |
| `ilunyu://shortcuts-guide` | Guide Raccourcis |
| `ilunyu://feature-guide` | Rejouer l’accueil |
| `ilunyu://feedback` | E-mail de commentaires |
| `ilunyu://in-app-review` | Avis in-app / App Store |

## Exemples


```
ilunyu://daily
ilunyu://passage?id=1
ilunyu://recite?id=20
ilunyu://theme?id=junzi
ilunyu://study
ilunyu://hunt
```


Utilisez-les dans l'application Raccourcis, les actions rapides Home Screen, les widgets ou Safari. Voir aussi dans l'application **Paramètres → Guide des raccourcis**.

</section>
<section lang="tr" markdown="1">

iLunYu, ** `ilunyu://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
ilunyu://{host}?{params}
```


## Bölümler & Yazarlar

| URL | Açar |
|-----|-------|
| `ilunyu://passage?id={id}` | Bölüm detayı |
| `ilunyu://couplet?id={id}` / `ilunyu://poem?id={id}` | Aynı geçiş (compatability) |
| `ilunyu://author?id={id}` | Yazar ayrıntısı |
| `ilunyu://recite` | Okuma akışı |
| `ilunyu://recite?id={id}` | Açık bölüm ve auto-recite |

## Keşfet

| URL | Açar |
|-----|-------|
| `ilunyu://home` | Ana sayfa sekmesi |
| `ilunyu://daily` | Bugünün Günlük Kur'an |
| `ilunyu://random` | Random Bölüm |
| `ilunyu://favorites` | Favoriler |
| `ilunyu://famous` | Ünlü dizeler |
| `ilunyu://search` / `ilunyu://search?q={query}` | Ara |
| `ilunyu://study` | Çalışma sınıfı |
| `ilunyu://hunt` | Hunt (fly); alias "keyword-hunt" / "flyflower" |
| `ilunyu://mastered` / `ilunyu://progress` | Mastered / ilerleme |
| `ilunyu://categories` / `ilunyu://categories?section=` | Gözat |
| `ilunyu://collection?id=lunyu` | Book collection (alias "book" / "form"; aynı zamanda "isim=") |
| `ilunyu://theme?id=` | Tema veya hacim (e.g. "junzi", "xue-er"; alias "suite' / "volume") |
| `ilunyu://last-read` | Son okunan |
| `ilunyu://reading-history` | Okuma geçmişi |
| `ilunyu://notes` | Notlar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `ilunyu://settings` | Ayarlar |
| `ilunyu://usage-guide` | Kullanım kılavuzu |
| `ilunyu://widget-guide` | Widget kılavuzu |
| `ilunyu://shortcuts-guide` | Kısayol kılavuzu |
| `ilunyu://feature-guide` | Tanıtımı yeniden oynat |
| `ilunyu://feedback` | Geri bildirim e-postası |
| `ilunyu://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
ilunyu://daily
ilunyu://passage?id=1
ilunyu://recite?id=20
ilunyu://theme?id=junzi
ilunyu://study
ilunyu://hunt
```


Bunları kısa kesimlerde kullanın, Home Ekran hızlı eylemleri, widgets veya Safari. Ayrıca bakınız **Settings → Kısayollar Kılavuzu**.

</section>
