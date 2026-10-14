---
layout: doc
title: iPrimer — Shortcut Links
app_id: iPrimer
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: iprimer:// deep links for iPrimer — chapter, daily, recite, study, meditation, guidance, hunt, collections, themes, settings guides, and more.
---

<section lang="en" markdown="1">

iPrimer supports **`iprimer://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
iprimer://{host}?{params}
```

## Chapters & authors

| URL | Opens |
|-----|-------|
| `iprimer://chapter?id={id}` | Chapter detail |
| `iprimer://passage?id={id}` / `iprimer://poem?id={id}` | Same as chapter (compatibility) |
| `iprimer://author?id={id}` | Author detail |
| `iprimer://recite` / `iprimer://recite?id={id}` | Recite flow |

## Discovery

| URL | Opens |
|-----|-------|
| `iprimer://home` | Home |
| `iprimer://daily` | Today’s Daily Study |
| `iprimer://random` | Random chapter |
| `iprimer://favorites` | Favorites |
| `iprimer://famous` | Famous lines |
| `iprimer://search` / `iprimer://search?q={query}` | Search |
| `iprimer://study` | Character Study |
| `iprimer://meditation` | Meditation course list |
| `iprimer://meditation?slug={slug}&autostart=1` | Open session and auto-start (foreground) |
| `iprimer://guidance` | Life Guidance (journal & habits) |
| `iprimer://hunt` | Hunt (寻句); aliases `keyword-hunt` / `flyflower` |
| `iprimer://mastered` | Mastered chapters |
| `iprimer://categories` / `iprimer://categories?section=` | Browse |
| `iprimer://collection?id=xiaoxue` | Xiaoxue collection (`name=` also supported) |
| `iprimer://theme?id=lijiao` | Volume / theme (`name=立教` or `Relationships` also supported) |
| `iprimer://last-read` | Last read |
| `iprimer://reading-history` | Reading history |
| `iprimer://notes` | Notes |

## Settings & guides

| URL | Opens |
|-----|-------|
| `iprimer://settings` | Settings |
| `iprimer://usage-guide` | Usage guide |
| `iprimer://widget-guide` | Widget guide |
| `iprimer://shortcuts-guide` | Shortcuts guide |
| `iprimer://feature-guide` | Replay onboarding |
| `iprimer://feedback` | Feedback email |
| `iprimer://in-app-review` | In-app / Store review entry |

## Examples

```
iprimer://daily
iprimer://chapter?id=3
iprimer://collection?id=xiaoxue
iprimer://theme?id=lijiao
iprimer://study
iprimer://meditation?slug=emotion_calm&autostart=1
iprimer://guidance
iprimer://hunt
```

Use these in the Shortcuts app, Home Screen quick actions, widgets, or Safari. Prefer stable `id` parameters when available. See also in-app **Settings → Shortcuts Guide**.

</section>
<section lang="zh-CN" markdown="1">

爱小学支持 **`iprimer://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
iprimer://{host}?{params}
```

## 篇章与作者

| URL | 打开 |
|-----|------|
| `iprimer://chapter?id={id}` | 篇章详情 |
| `iprimer://passage?id={id}` / `iprimer://poem?id={id}` | 同篇章（兼容） |
| `iprimer://author?id={id}` | 作者详情 |
| `iprimer://recite` / `iprimer://recite?id={id}` | 诵读 |

## 发现与练习

| URL | 打开 |
|-----|------|
| `iprimer://home` | 首页 |
| `iprimer://daily` | 今日每日一学 |
| `iprimer://random` | 随机篇章 |
| `iprimer://favorites` | 收藏 |
| `iprimer://famous` | 名句 |
| `iprimer://search` / `iprimer://search?q={关键词}` | 搜索 |
| `iprimer://study` | 品格学堂 |
| `iprimer://meditation` | 静心冥想课表 |
| `iprimer://meditation?slug={slug}&autostart=1` | 直达课程并自动开始（需前景） |
| `iprimer://guidance` | 人生指导（反思日记与洒扫打卡） |
| `iprimer://hunt` | 寻句 |
| `iprimer://mastered` | 已掌握 |
| `iprimer://categories` | 分类浏览 |
| `iprimer://collection?id=xiaoxue` | 《小学》合集 |
| `iprimer://theme?id=lijiao` | 六卷 / 主题（`name=立教` 等仍兼容） |
| `iprimer://last-read` | 上次阅读 |
| `iprimer://reading-history` | 阅读历史 |
| `iprimer://notes` | 笔记 |

## 设置与引导

| URL | 打开 |
|-----|------|
| `iprimer://settings` | 设置 |
| `iprimer://usage-guide` | 使用说明 |
| `iprimer://widget-guide` | 小组件指南 |
| `iprimer://shortcuts-guide` | 快捷指南 |
| `iprimer://feature-guide` | 重播欢迎引导 |
| `iprimer://feedback` | 反馈邮件 |
| `iprimer://in-app-review` | 应用内评价入口 |

## 示例

```
iprimer://daily
iprimer://chapter?id=3
iprimer://theme?id=lijiao
iprimer://study
iprimer://meditation?slug=emotion_calm&autostart=1
iprimer://guidance
```

可在快捷指令、主屏快捷、小组件或 Safari 中使用。建议优先使用稳定的 `id` 参数。详见应用内 **设置 → 快捷指南**。

</section>
<section lang="zh-TW" markdown="1">

愛小學支援 **`iprimer://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複開啟。

## 連結格式

```
iprimer://{host}?{params}
```

## 篇章與作者

| URL | 開啟 |
|-----|------|
| `iprimer://chapter?id={id}` | 篇章詳情 |
| `iprimer://author?id={id}` | 作者詳情 |
| `iprimer://recite` / `iprimer://recite?id={id}` | 誦讀 |

## 發現與練習

| URL | 開啟 |
|-----|------|
| `iprimer://daily` | 今日每日一學 |
| `iprimer://study` | 品格學堂 |
| `iprimer://meditation` | 靜心冥想 |
| `iprimer://guidance` | 人生指導 |
| `iprimer://hunt` | 尋句 |
| `iprimer://collection?id=xiaoxue` | 《小學》合集 |
| `iprimer://theme?id=lijiao` | 六卷 / 主題 |

## 設定與引導

`iprimer://settings` · `iprimer://usage-guide` · `iprimer://widget-guide` · `iprimer://shortcuts-guide` · `iprimer://feature-guide` · `iprimer://feedback`

詳見應用內 **設定 → 捷徑指南**。

</section>
<section lang="ja" markdown="1">

iPrimerは** `iprimer://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
iprimer://{host}?{params}
```


## 章と著者

| URL | 開く画面 |
|-----|-------|
| `iprimer://chapter?id={id}` | 章の詳細 |
| `iprimer://passage?id={id}` / `iprimer://poem?id={id}` | チャプターと同じ(互換性) |
| `iprimer://author?id={id}` | 作者の詳細 |
| `iprimer://recite` / `iprimer://recite?id={id}` | 誦読フロー |

## 発見

| URL | 開く画面 |
|-----|-------|
| `iprimer://home` | ホーム |
| `iprimer://daily` | 今日の毎日の勉強 |
| `iprimer://random` | ランダムチャプター |
| `iprimer://favorites` | お気に入り |
| `iprimer://famous` | 名句一覧 |
| `iprimer://search` / `iprimer://search?q={query}` | 検索 |
| `iprimer://study` | キャラクタースタディ |
| `iprimer://meditation` | 瞑想コース一覧 |
| `iprimer://meditation?slug={slug}&autostart=1` | セッションとオートスタート(フォアグラウンド) |
| `iprimer://guidance` | ライフガイダンス(ジャーナル&習慣) |
| `iprimer://hunt` | Hunt(笑)。aliases`keyword-hunt`/`flyflower` |
| `iprimer://mastered` | マスターされた章 |
| `iprimer://categories` / `iprimer://categories?section=` | ブラウズ |
| `iprimer://collection?id=xiaoxue` | Xiaoxueコレクション (`name=` もサポート) |
| `iprimer://theme?id=lijiao` | ボリューム/テーマ(`name=立教` または `Relationships` もサポート) |
| `iprimer://last-read` | 最後に読んだ項目 |
| `iprimer://reading-history` | 閲覧履歴 |
| `iprimer://notes` | ノート |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `iprimer://settings` | 設定 |
| `iprimer://usage-guide` | 使い方ガイド |
| `iprimer://widget-guide` | ウィジェットガイド |
| `iprimer://shortcuts-guide` | ショートカットガイド |
| `iprimer://feature-guide` | オンボーディングの再生 |
| `iprimer://feedback` | フィードバックメール |
| `iprimer://in-app-review` | アプリ内／App Store レビュー |

## 例


```
iprimer://daily
iprimer://chapter?id=3
iprimer://collection?id=xiaoxue
iprimer://theme?id=lijiao
iprimer://study
iprimer://meditation?slug=emotion_calm&autostart=1
iprimer://guidance
iprimer://hunt
```


これらをショートカットアプリ、ホーム画面のクイックアクション、ウィジェット、またはSafariで使用してください。 利用できる場合の優先順位の安定した `iprimer://` 変数。 アプリ内設定 → ショートカットガイド** も参照してください。

</section>
<section lang="ko" markdown="1">

iPrimer 지원 ** `iprimer://` ** 단축키 링크 (URL 계획). 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
iprimer://{host}?{params}
```


## 장 & 저자

| URL | 열리는 화면 |
|-----|-------|
| `iprimer://chapter?id={id}` | 장 세부 사항 |
| `iprimer://passage?id={id}` / `iprimer://poem?id={id}` | 챕터와 동일 ( 호환성) |
| `iprimer://author?id={id}` | 작가 상세 |
| `iprimer://recite` / `iprimer://recite?id={id}` | 낭독 흐름 |

## 탐색

| URL | 열리는 화면 |
|-----|-------|
| `iprimer://home` | 홈 |
| `iprimer://daily` | 오늘의 일일 학습 |
| `iprimer://random` | 무작위 장 |
| `iprimer://favorites` | 즐겨찾기 |
| `iprimer://famous` | 명구 목록 |
| `iprimer://search` / `iprimer://search?q={query}` | 검색 |
| `iprimer://study` | 문자 학습 |
| `iprimer://meditation` | Meditation 과정 목록 |
| `iprimer://meditation?slug={slug}&autostart=1` | 세션 및 자동 시작 (foreground) |
| `iprimer://guidance` | 삶의 길 (journal & 습관) |
| `iprimer://hunt` | 헌트 (fly); aliases `keyword-hunt`/`flyflower` |
| `iprimer://mastered` | 마스터드 장 |
| `iprimer://categories` / `iprimer://categories?section=` | 둘러보기 |
| `iprimer://collection?id=xiaoxue` | Xiaoxue 컬렉션 (`name=`도 지원) |
| `iprimer://theme?id=lijiao` | Volume / theme (`name=鶏` 또는 `Relationships`도 지원) |
| `iprimer://last-read` | 마지막으로 읽은 항목 |
| `iprimer://reading-history` | 읽기 기록 |
| `iprimer://notes` | 메모 |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `iprimer://settings` | 설정 |
| `iprimer://usage-guide` | 사용 가이드 |
| `iprimer://widget-guide` | 위젯 가이드 |
| `iprimer://shortcuts-guide` | 단축어 가이드 |
| `iprimer://feature-guide` | 온보딩 다시 보기 |
| `iprimer://feedback` | 피드백 이메일 |
| `iprimer://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
iprimer://daily
iprimer://chapter?id=3
iprimer://collection?id=xiaoxue
iprimer://theme?id=lijiao
iprimer://study
iprimer://meditation?slug=emotion_calm&autostart=1
iprimer://guidance
iprimer://hunt
```


Shortcuts 앱, 홈 화면 빠른 행동, 위젯, 또는 사파리에서 이러한 사용. Prefer stable `iprimer://` 사용할 때 매개 변수. in-app**Settings → 단축키 가이드** 참조.

</section>
<section lang="ru" markdown="1">

iPrimer поддерживает ярлыки ** `iprimer://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
iprimer://{host}?{params}
```


## Главы и авторы

| URL | Открывает |
|-----|-------|
| `iprimer://chapter?id={id}` | Глава подробная |
| `iprimer://passage?id={id}` / `iprimer://poem?id={id}` | Совместимость (Compatibility) |
| `iprimer://author?id={id}` | Страница автора |
| `iprimer://recite` / `iprimer://recite?id={id}` | Режим чтения вслух |

## Обзор

| URL | Открывает |
|-----|-------|
| `iprimer://home` | Главная |
| `iprimer://daily` | Сегодняшнее ежедневное исследование |
| `iprimer://random` | Случайная глава |
| `iprimer://favorites` | Избранное |
| `iprimer://famous` | Знаменитые строки |
| `iprimer://search` / `iprimer://search?q={query}` | Поиск |
| `iprimer://study` | Изучение характера |
| `iprimer://meditation` | Список курсов медитации |
| `iprimer://meditation?slug={slug}&autostart=1` | Открытая сессия и автозапуск (на переднем плане) |
| `iprimer://guidance` | Руководство по жизни (журнал и привычки) |
| `iprimer://hunt` | Охота (`); псевдонимы «охота за ключевыми словами» / «флайфлауэр» |
| `iprimer://mastered` | Освоенные главы |
| `iprimer://categories` / `iprimer://categories?section=` | Обзор |
| `iprimer://collection?id=xiaoxue` | Коллекция Xiaoxue («имя =» также поддерживается) |
| `iprimer://theme?id=lijiao` | Объем / тема (также поддерживается «имя = )» или «Отношения») |
| `iprimer://last-read` | Последнее прочитанное |
| `iprimer://reading-history` | История чтения |
| `iprimer://notes` | Заметки |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `iprimer://settings` | Настройки |
| `iprimer://usage-guide` | Руководство по использованию |
| `iprimer://widget-guide` | Руководство по виджетам |
| `iprimer://shortcuts-guide` | Руководство по «Командам» |
| `iprimer://feature-guide` | Повторное знакомство |
| `iprimer://feedback` | Письмо с отзывом |
| `iprimer://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
iprimer://daily
iprimer://chapter?id=3
iprimer://collection?id=xiaoxue
iprimer://theme?id=lijiao
iprimer://study
iprimer://meditation?slug=emotion_calm&autostart=1
iprimer://guidance
iprimer://hunt
```


Используйте их в приложении Shortcuts, быстрых действиях Home Screen, виджетах или Safari. Предпочитаю стабильные параметры `iprimer://` при наличии. См. также in-app **Settings → Shortcuts Guide**.

</section>
<section lang="th" markdown="1">

iPrimiter รองรับ ** `iprimer://` BAR * ลิงก์ลัด (URL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
iprimer://{host}?{params}
```


## บทและผู้เขียน

| URL | เปิด |
|-----|-------|
| `iprimer://chapter?id={id}` | รายละเอียดในบท |
| `iprimer://passage?id={id}` / `iprimer://poem?id={id}` | เหมือนกับบท (ความเข้ากันได้) |
| `iprimer://author?id={id}` | รายละเอียดผู้แต่ง |
| `iprimer://recite` / `iprimer://recite?id={id}` | โฟลว์การท่อง |

## ค้นพบ

| URL | เปิด |
|-----|-------|
| `iprimer://home` | หน้าแรก |
| `iprimer://daily` | การ ศึกษา ประจํา วัน |
| `iprimer://random` | หมุน & 90 |
| `iprimer://favorites` | รายการโปรด |
| `iprimer://famous` | บรรทัดขึ้นชื่อ |
| `iprimer://search` / `iprimer://search?q={query}` | ค้นหา |
| `iprimer://study` | การศึกษาอักขระ |
| `iprimer://meditation` | พิจารณารายการหลักสูตร |
| `iprimer://meditation?slug={slug}&autostart=1` | เปิดวาระการใช้งานและเริ่มอัตโนมัติ (จากก่อน) |
| `iprimer://guidance` | การนําทางชีวิต (นิสัยต่าง ๆ) |
| `iprimer://hunt` | ล่า (寻句; สืบค้นเมื่อ 'คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน' |
| `iprimer://mastered` | บทหลัก |
| `iprimer://categories` / `iprimer://categories?section=` | เรียกดู |
| `iprimer://collection?id=xiaoxue` | คลังภาพ Sublicue (ชื่อ'=' รองรับด้วย) |
| `iprimer://theme?id=lijiao` | ระดับเสียง / ชุดตกแต่ง (ชื่อ) |
| `iprimer://last-read` | รายการที่อ่านล่าสุด |
| `iprimer://reading-history` | ประวัติการอ่าน |
| `iprimer://notes` | บันทึก |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `iprimer://settings` | การตั้งค่า |
| `iprimer://usage-guide` | คู่มือการใช้งาน |
| `iprimer://widget-guide` | คู่มือวิดเจ็ต |
| `iprimer://shortcuts-guide` | คู่มือทางลัด |
| `iprimer://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `iprimer://feedback` | อีเมลข้อเสนอแนะ |
| `iprimer://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
iprimer://daily
iprimer://chapter?id=3
iprimer://collection?id=xiaoxue
iprimer://theme?id=lijiao
iprimer://study
iprimer://meditation?slug=emotion_calm&autostart=1
iprimer://guidance
iprimer://hunt
```


ใช้เหล่านี้ในโปรแกรมปุ่มพิมพ์ลัด, การกระทําของหน้าจอส่วนตัวอย่างรวดเร็ว, วิดเจ็ต, หรือ Saveri ค่าคงที่ `iprimer://` พารามิเตอร์เมื่อใช้ได้ ดูใน-apps ด้วย

</section>
<section lang="de" markdown="1">

iPrimer unterstützt ** `iprimer://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
iprimer://{host}?{params}
```


## Kapitel & Autoren

| URL | Öffnet |
|-----|-------|
| `iprimer://chapter?id={id}` | Einzelheiten des Kapitels |
| `iprimer://passage?id={id}` / `iprimer://poem?id={id}` | Wie Kapitel (Kompatibilität) |
| `iprimer://author?id={id}` | Autorendetail |
| `iprimer://recite` / `iprimer://recite?id={id}` | Rezitationsablauf |

## Entdecken

| URL | Öffnet |
|-----|-------|
| `iprimer://home` | Startseite |
| `iprimer://daily` | Die heutige tägliche Studie |
| `iprimer://random` | Zufallskapitel |
| `iprimer://favorites` | Favoriten |
| `iprimer://famous` | Berühmte Zeilen |
| `iprimer://search` / `iprimer://search?q={query}` | Suche |
| `iprimer://study` | Charakterstudie |
| `iprimer://meditation` | Meditationskursliste |
| `iprimer://meditation?slug={slug}&autostart=1` | Offene Sitzung und Autostart (Vordergrund) |
| `iprimer://guidance` | Lebensberatung (Journal & Gewohnheiten) |
| `iprimer://hunt` | Jagd (寻句); alias `keyword-hunt` / `flyflower` |
| `iprimer://mastered` | Mastered Chapters |
| `iprimer://categories` / `iprimer://categories?section=` | Durchsuchen |
| `iprimer://collection?id=xiaoxue` | Xiaoxue Collection (`name=` wird auch unterstützt) |
| `iprimer://theme?id=lijiao` | Volume / Theme (`name=立教` oder `Relationships` auch unterstützt) |
| `iprimer://last-read` | Zuletzt gelesen |
| `iprimer://reading-history` | Leseverlauf |
| `iprimer://notes` | Notizen |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `iprimer://settings` | Einstellungen |
| `iprimer://usage-guide` | Nutzungsanleitung |
| `iprimer://widget-guide` | Widget-Anleitung |
| `iprimer://shortcuts-guide` | Kurzbefehle-Anleitung |
| `iprimer://feature-guide` | Einführung erneut abspielen |
| `iprimer://feedback` | Feedback-E-Mail |
| `iprimer://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
iprimer://daily
iprimer://chapter?id=3
iprimer://collection?id=xiaoxue
iprimer://theme?id=lijiao
iprimer://study
iprimer://meditation?slug=emotion_calm&autostart=1
iprimer://guidance
iprimer://hunt
```


Verwenden Sie diese in der Shortcuts-App, den Schnellaktionen für den Startbildschirm, den Widgets oder Safari. Bevorzugt stabile `iprimer://` -Parameter, wenn verfügbar. Siehe auch In-App **Settings → Shortcuts Guide**.

</section>
<section lang="fr" markdown="1">

iPrimer prend en charge les liens de raccourci ** `iprimer://` ** (plan URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
iprimer://{host}?{params}
```


## Chapitres & auteurs

| URL | Ouvre |
|-----|-------|
| `iprimer://chapter?id={id}` | Détail du chapitre |
| `iprimer://passage?id={id}` / `iprimer://poem?id={id}` | Même chapitre (compatibilité) |
| `iprimer://author?id={id}` | Détail de l’auteur |
| `iprimer://recite` / `iprimer://recite?id={id}` | Flux de récitation |

## Découverte

| URL | Ouvre |
|-----|-------|
| `iprimer://home` | Accueil |
| `iprimer://daily` | Aujourd'hui |
| `iprimer://random` | Chapitre aléatoire |
| `iprimer://favorites` | Favoris |
| `iprimer://famous` | Vers célèbres |
| `iprimer://search` / `iprimer://search?q={query}` | Recherche |
| `iprimer://study` | Étude de caractère |
| `iprimer://meditation` | Liste des cours de méditation |
| `iprimer://meditation?slug={slug}&autostart=1` | Ouvrir la session et démarrer automatiquement (précédent) |
| `iprimer://guidance` | Guide de vie (journal & habitudes) |
| `iprimer://hunt` | Chasse () ; alias « chasse aux mots clés » / « fleurs volantes » |
| `iprimer://mastered` | Chapitres maîtrisables |
| `iprimer://categories` / `iprimer://categories?section=` | Parcourir |
| `iprimer://collection?id=xiaoxue` | Collection Xiaoxue (`nom=` également supporté) |
| `iprimer://theme?id=lijiao` | Volume / thème (`name=. |
| `iprimer://last-read` | Dernière lecture |
| `iprimer://reading-history` | Historique de lecture |
| `iprimer://notes` | Notes |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `iprimer://settings` | Réglages |
| `iprimer://usage-guide` | Guide d'utilisation |
| `iprimer://widget-guide` | Guide des widgets |
| `iprimer://shortcuts-guide` | Guide Raccourcis |
| `iprimer://feature-guide` | Rejouer l’accueil |
| `iprimer://feedback` | E-mail de commentaires |
| `iprimer://in-app-review` | Avis in-app / App Store |

## Exemples


```
iprimer://daily
iprimer://chapter?id=3
iprimer://collection?id=xiaoxue
iprimer://theme?id=lijiao
iprimer://study
iprimer://meditation?slug=emotion_calm&autostart=1
iprimer://guidance
iprimer://hunt
```


Utilisez-les dans l'application Raccourcis, les actions rapides Home Screen, les widgets ou Safari. Préférez les paramètres stables `iprimer://` lorsque disponibles. Voir aussi dans l'application **Paramètres → Guide des raccourcis**.

</section>
<section lang="tr" markdown="1">

iPrimer ** `iprimer://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
iprimer://{host}?{params}
```


## Bölümler & Yazarlar

| URL | Açar |
|-----|-------|
| `iprimer://chapter?id={id}` | Bölüm detayı |
| `iprimer://passage?id={id}` / `iprimer://poem?id={id}` | Bölüm (compatability) |
| `iprimer://author?id={id}` | Yazar ayrıntısı |
| `iprimer://recite` / `iprimer://recite?id={id}` | Okuma akışı |

## Keşfet

| URL | Açar |
|-----|-------|
| `iprimer://home` | Ana sayfa |
| `iprimer://daily` | Bugünün Günlük Çalışması |
| `iprimer://random` | Random Bölüm |
| `iprimer://favorites` | Favoriler |
| `iprimer://famous` | Ünlü dizeler |
| `iprimer://search` / `iprimer://search?q={query}` | Ara |
| `iprimer://study` | Karakter Çalışması |
| `iprimer://meditation` | Meditasyon kursu listesi |
| `iprimer://meditation?slug={slug}&autostart=1` | Açık oturum ve otomatik başlangıç (foreground) |
| `iprimer://guidance` | Hayat Rehberliği ( muhabir ve alışkanlıklar) |
| `iprimer://hunt` | Hunt (fly); alias "keyword-hunt" / "flyflower" |
| `iprimer://mastered` | Mastered bölümler |
| `iprimer://categories` / `iprimer://categories?section=` | Gözat |
| `iprimer://collection?id=xiaoxue` | Xiaoxue koleksiyonu (isim=' aynı zamanda desteklenen) |
| `iprimer://theme?id=lijiao` | Volume / tema (isim=立教' veya "Relationships" desteklenmektedir) |
| `iprimer://last-read` | Son okunan |
| `iprimer://reading-history` | Okuma geçmişi |
| `iprimer://notes` | Notlar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `iprimer://settings` | Ayarlar |
| `iprimer://usage-guide` | Kullanım kılavuzu |
| `iprimer://widget-guide` | Widget kılavuzu |
| `iprimer://shortcuts-guide` | Kısayol kılavuzu |
| `iprimer://feature-guide` | Tanıtımı yeniden oynat |
| `iprimer://feedback` | Geri bildirim e-postası |
| `iprimer://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
iprimer://daily
iprimer://chapter?id=3
iprimer://collection?id=xiaoxue
iprimer://theme?id=lijiao
iprimer://study
iprimer://meditation?slug=emotion_calm&autostart=1
iprimer://guidance
iprimer://hunt
```


Bunları kısa kesimlerde kullanın, Home Ekran hızlı eylemleri, widgets veya Safari. Mevcut olduğunda istikrarlı `iprimer://` parametreleri tercih edin. Ayrıca bakınız **Settings → Kısayollar Kılavuzu**.

</section>
