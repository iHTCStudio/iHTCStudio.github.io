---
layout: doc
title: iDao — Shortcut Links
app_id: iDao
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: idao:// deep links for iDao — chapter, daily, recite, study, hunt, famous lines, books, settings guides, and more.
---

<section lang="en" markdown="1">

iDao supports **`idao://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
idao://{host}?{params}
```

## Chapters & discovery

| URL | Opens |
|-----|-------|
| `idao://home` | Home |
| `idao://daily` | Today’s Daily Chapter |
| `idao://random` | Random chapter |
| `idao://chapter?id={id}` | Chapter detail |
| `idao://recite` / `idao://recite?id={id}` | Recite flow |
| `idao://favorites` | Favorites |
| `idao://famous` | Famous lines |
| `idao://search` / `idao://search?q={query}` | Search |
| `idao://study` | Study Hall |
| `idao://hunt` | Seek the Tao (寻道) |
| `idao://mastered` | Mastered |
| `idao://categories` / `?section=` | Browse (optional section) |
| `idao://book?id=` | Book collection (`ddj` / `qingjing` / `yinfu`) |
| `idao://author` | Laozi intro |
| `idao://last-read` | Last read |
| `idao://reading-history` | Reading history |
| `idao://notes` | Notes |

> Compatibility aliases: `passage` / `poem` → chapter; `learn` → study; `seek` → hunt; `laozi` → author; `theme?id=` → categories section; `browse` → categories.

## Settings & guides

| URL | Opens |
|-----|-------|
| `idao://settings` | Settings |
| `idao://usage-guide` | Usage guide |
| `idao://widget-guide` | Widget guide |
| `idao://shortcuts-guide` | Shortcuts guide |
| `idao://feature-guide` | Replay onboarding |
| `idao://feedback` | Feedback email |
| `idao://in-app-review` | In-app / Store review entry |

## Examples

```
idao://daily
idao://chapter?id=1
idao://recite?id=1
idao://study
idao://hunt
idao://famous
idao://book?id=ddj
idao://author
idao://search?q=上善若水
```

Use these in the Shortcuts app, Home Screen quick actions, widgets, Control Center, or Safari. See also in-app **Settings → Shortcuts Guide**.

</section>
<section lang="zh-CN" markdown="1">

爱道德经支持 **`idao://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
idao://{host}?{params}
```

## 章节与发现

| URL | 打开 |
|-----|------|
| `idao://home` | 首页 |
| `idao://daily` | 每日一章 |
| `idao://random` | 随机 |
| `idao://chapter?id={id}` | 章节详情 |
| `idao://recite` / `idao://recite?id={id}` | 诵读 |
| `idao://favorites` | 收藏 |
| `idao://famous` | 名句 |
| `idao://search` / `idao://search?q={query}` | 搜索 |
| `idao://study` | 道学堂 |
| `idao://hunt` | 寻道 |
| `idao://mastered` | 已掌握 |
| `idao://categories` / `?section=` | 分类（可选分区） |
| `idao://book?id=` | 书目合集（`ddj` / `qingjing` / `yinfu`） |
| `idao://author` | 老子简介 |
| `idao://last-read` | 上次阅读 |
| `idao://reading-history` | 浏览记录 |
| `idao://notes` | 笔记 |

> 兼容别名：`passage` / `poem` → chapter；`learn` → study；`seek` → hunt；`laozi` → author；`theme?id=` → 分类分区；`browse` → categories。

## 设置与教程

| URL | 打开 |
|-----|------|
| `idao://settings` | 设置 |
| `idao://usage-guide` | 使用说明 |
| `idao://widget-guide` | 小组件指南 |
| `idao://shortcuts-guide` | 快捷指南 |
| `idao://feature-guide` | 重播引导 |
| `idao://feedback` | 反馈邮件 |
| `idao://in-app-review` | 应用内 / 商店评价入口 |

## 示例

```
idao://daily
idao://chapter?id=1
idao://recite?id=1
idao://study
idao://hunt
idao://famous
idao://book?id=ddj
idao://author
idao://search?q=上善若水
```

可在「快捷指令」、主屏快捷、小组件、控制中心或 Safari 中使用。也可查看应用内 **设置 → 快捷指南**。

</section>
<section lang="zh-TW" markdown="1">

愛道德經支援 **`idao://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複開啟。

## 連結格式

```
idao://{host}?{params}
```

## 章節與發現

| URL | 開啟 |
|-----|------|
| `idao://home` | 首頁 |
| `idao://daily` | 每日一章 |
| `idao://random` | 隨機 |
| `idao://chapter?id={id}` | 章節詳情 |
| `idao://recite` / `idao://recite?id={id}` | 誦讀 |
| `idao://favorites` | 收藏 |
| `idao://famous` | 名句 |
| `idao://search` / `idao://search?q={query}` | 搜尋 |
| `idao://study` | 道學堂 |
| `idao://hunt` | 尋道 |
| `idao://mastered` | 已掌握 |
| `idao://categories` / `?section=` | 分類（可選分區） |
| `idao://book?id=` | 書目合集（`ddj` / `qingjing` / `yinfu`） |
| `idao://author` | 老子簡介 |
| `idao://last-read` | 上次閱讀 |
| `idao://reading-history` | 瀏覽記錄 |
| `idao://notes` | 筆記 |

> 相容別名：`passage` / `poem` → chapter；`learn` → study；`seek` → hunt；`laozi` → author；`theme?id=` → 分類分區；`browse` → categories。

## 設定與教學

| URL | 開啟 |
|-----|------|
| `idao://settings` | 設定 |
| `idao://usage-guide` | 使用說明 |
| `idao://widget-guide` | 小工具指南 |
| `idao://shortcuts-guide` | 捷徑指南 |
| `idao://feature-guide` | 重播引導 |
| `idao://feedback` | 回饋郵件 |
| `idao://in-app-review` | App 內 / 商店評價入口 |

## 範例

```
idao://daily
idao://chapter?id=1
idao://recite?id=1
idao://study
idao://hunt
idao://famous
idao://book?id=ddj
idao://author
idao://search?q=上善若水
```

可在「捷徑」、主畫面捷徑、小工具、控制中心或 Safari 中使用。也可查看應用內 **設定 → 捷徑指南**。

</section>
<section lang="ja" markdown="1">

iDaoは** `idao://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
idao://{host}?{params}
```


## 章と発見

| URL | 開く画面 |
|-----|-------|
| `idao://home` | ホーム |
| `idao://daily` | 今日の毎日の章 |
| `idao://random` | ランダムチャプター |
| `idao://chapter?id={id}` | 章の詳細 |
| `idao://recite` / `idao://recite?id={id}` | 誦読フロー |
| `idao://favorites` | お気に入り |
| `idao://famous` | 名句一覧 |
| `idao://search` / `idao://search?q={query}` | 検索 |
| `idao://study` | スタディホール |
| `idao://hunt` | Tao (タオ) |
| `idao://mastered` | マスタード |
| `idao://categories` / `?section=` | ブラウズ(オプションセクション) |
| `idao://book?id=` | ブックコレクション(dd`j`/`qingjing`/`yinfu`) |
| `idao://author` | Laoziイントロ |
| `idao://last-read` | 最後に読んだ項目 |
| `idao://reading-history` | 閲覧履歴 |
| `idao://notes` | ノート |

> 互換性エイリアス: `idao://` ## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `idao://settings` | 設定 |
| `idao://usage-guide` | 使い方ガイド |
| `idao://widget-guide` | ウィジェットガイド |
| `idao://shortcuts-guide` | ショートカットガイド |
| `idao://feature-guide` | オンボーディングの再生 |
| `idao://feedback` | フィードバックメール |
| `idao://in-app-review` | アプリ内／App Store レビュー |

## 例


```
idao://daily
idao://chapter?id=1
idao://recite?id=1
idao://study
idao://hunt
idao://famous
idao://book?id=ddj
idao://author
idao://search?q=上善若水
```


これらをショートカットアプリ、ホーム画面のクイックアクション、ウィジェット、コントロールセンター、またはSafariで使用してください。 アプリ内設定 → ショートカットガイド** も参照してください。

</section>
<section lang="ko" markdown="1">

iDao는 ** `idao://` ** 단축키 링크 (URL 계획)를 지원합니다. 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
idao://{host}?{params}
```


## 장 & 발견

| URL | 열리는 화면 |
|-----|-------|
| `idao://home` | 홈 |
| `idao://daily` | 오늘의 매일 장 |
| `idao://random` | 무작위 장 |
| `idao://chapter?id={id}` | 장 세부 사항 |
| `idao://recite` / `idao://recite?id={id}` | 낭독 흐름 |
| `idao://favorites` | 즐겨찾기 |
| `idao://famous` | 명구 목록 |
| `idao://search` / `idao://search?q={query}` | 검색 |
| `idao://study` | 연구 홀 |
| `idao://hunt` | 타오( Tao道) |
| `idao://mastered` | 인기있는 |
| `idao://categories` / `?section=` | 검색 (옵션 섹션) |
| `idao://book?id=` | 도서 수집 (`ddj`/`qingjing`/`yinfu`) |
| `idao://author` | Laozi 소개 |
| `idao://last-read` | 마지막으로 읽은 항목 |
| `idao://reading-history` | 읽기 기록 |
| `idao://notes` | 메모 |

> 호환성 별명으로: `idao://` / `idao://home` → 장; `idao://daily` → 연구; `idao://random` → 사냥; `idao://chapter?id={id}` → 저자; `idao://recite` → 카테고리 섹션; `idao://recite?id={id}` → 카테고리.

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `idao://settings` | 설정 |
| `idao://usage-guide` | 사용 가이드 |
| `idao://widget-guide` | 위젯 가이드 |
| `idao://shortcuts-guide` | 단축어 가이드 |
| `idao://feature-guide` | 온보딩 다시 보기 |
| `idao://feedback` | 피드백 이메일 |
| `idao://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
idao://daily
idao://chapter?id=1
idao://recite?id=1
idao://study
idao://hunt
idao://famous
idao://book?id=ddj
idao://author
idao://search?q=上善若水
```


Shortcuts 앱에서 이러한 사용, 홈 화면 빠른 행동, 위젯, 제어 센터, 또는 사파리. in-app**Settings → 단축키 가이드** 참조.

</section>
<section lang="ru" markdown="1">

iDao поддерживает ярлыки ** `idao://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
idao://{host}?{params}
```


## Главы и открытия

| URL | Открывает |
|-----|-------|
| `idao://home` | Главная |
| `idao://daily` | Сегодняшняя ежедневная глава |
| `idao://random` | Случайная глава |
| `idao://chapter?id={id}` | Глава подробная |
| `idao://recite` / `idao://recite?id={id}` | Режим чтения вслух |
| `idao://favorites` | Избранное |
| `idao://famous` | Знаменитые строки |
| `idao://search` / `idao://search?q={query}` | Поиск |
| `idao://study` | Учебный зал |
| `idao://hunt` | Ищите Дао ()) |
| `idao://mastered` | мастеринг |
| `idao://categories` / `?section=` | Браузер (необязательный раздел) |
| `idao://book?id=` | Коллекция книг ('ddj' / 'qingjing' / 'yinfu') |
| `idao://author` | Вступление Лаоци |
| `idao://last-read` | Последнее прочитанное |
| `idao://reading-history` | История чтения |
| `idao://notes` | Заметки |

> Совместимость: `idao://` / `idao://home` → глава; `idao://daily` → исследование; `idao://random` → охота; `idao://chapter?id={id}` → автор; `idao://recite` → раздел категорий; `idao://recite?id={id}` → категории.

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `idao://settings` | Настройки |
| `idao://usage-guide` | Руководство по использованию |
| `idao://widget-guide` | Руководство по виджетам |
| `idao://shortcuts-guide` | Руководство по «Командам» |
| `idao://feature-guide` | Повторное знакомство |
| `idao://feedback` | Письмо с отзывом |
| `idao://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
idao://daily
idao://chapter?id=1
idao://recite?id=1
idao://study
idao://hunt
idao://famous
idao://book?id=ddj
idao://author
idao://search?q=上善若水
```


Используйте их в приложении Shortcuts, быстрых действиях Home Screen, виджетах, Центре управления или Safari. См. также in-app **Settings → Shortcuts Guide**.

</section>
<section lang="th" markdown="1">

idao รองรับ} `idao://` BAR ลิงก์ลัด (RUL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
idao://{host}?{params}
```


## การค้นพบในบท

| URL | เปิด |
|-----|-------|
| `idao://home` | หน้าแรก |
| `idao://daily` | ทุก วัน นี้ |
| `idao://random` | หมุน & 90 |
| `idao://chapter?id={id}` | รายละเอียดในบท |
| `idao://recite` / `idao://recite?id={id}` | โฟลว์การท่อง |
| `idao://favorites` | รายการโปรด |
| `idao://famous` | บรรทัดขึ้นชื่อ |
| `idao://search` / `idao://search?q={query}` | ค้นหา |
| `idao://study` | หอ ประชุม ศึกษา |
| `idao://hunt` | สืบค้นเทา (寻道) |
| `idao://mastered` | สําเร็จการศึกษาแล้ว |
| `idao://categories` / `?section=` | เรียกดู (ส่วนตัวเลือก) |
| `idao://book?id=` | คอลเลกชันหนังสือ ('Dju' / hugging) |
| `idao://author` | ภาษาลาวซีName |
| `idao://last-read` | รายการที่อ่านล่าสุด |
| `idao://reading-history` | ประวัติการอ่าน |
| `idao://notes` | บันทึก |

> นามแฝงที่เข้ากันได้: `idao://` BAR `idao://home` c1 c saw;  c2 → การศึกษา;  c3  สืบค้น; `idao://chapter?id={id}` s   s      s. สืบค้น; c        ////s/s/s. parort;   BAR s s/s s/s/s.p.p. parm.

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `idao://settings` | การตั้งค่า |
| `idao://usage-guide` | คู่มือการใช้งาน |
| `idao://widget-guide` | คู่มือวิดเจ็ต |
| `idao://shortcuts-guide` | คู่มือทางลัด |
| `idao://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `idao://feedback` | อีเมลข้อเสนอแนะ |
| `idao://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
idao://daily
idao://chapter?id=1
idao://recite?id=1
idao://study
idao://hunt
idao://famous
idao://book?id=ddj
idao://author
idao://search?q=上善若水
```


ใช้เหล่านี้ในโปรแกรมปุ่มพิมพ์ลัด, การกระทําของหน้าจอส่วนตัวอย่างรวดเร็ว, วิดเจ็ต, ศูนย์ควบคุม, หรือซาฟารี ดูใน-apps ด้วย

</section>
<section lang="de" markdown="1">

iDao unterstützt ** `idao://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
idao://{host}?{params}
```


## Kapitel & Entdeckung

| URL | Öffnet |
|-----|-------|
| `idao://home` | Startseite |
| `idao://daily` | Das heutige tägliche Kapitel |
| `idao://random` | Zufallskapitel |
| `idao://chapter?id={id}` | Einzelheiten des Kapitels |
| `idao://recite` / `idao://recite?id={id}` | Rezitationsablauf |
| `idao://favorites` | Favoriten |
| `idao://famous` | Berühmte Zeilen |
| `idao://search` / `idao://search?q={query}` | Suche |
| `idao://study` | Studienhalle |
| `idao://hunt` | Suche das Tao (寻道) |
| `idao://mastered` | Beherrscht |
| `idao://categories` / `?section=` | Browse (optionaler Abschnitt) |
| `idao://book?id=` | Buchsammlung (`ddj` / `qingjing` / `yinfu`) |
| `idao://author` | Laozi intro |
| `idao://last-read` | Zuletzt gelesen |
| `idao://reading-history` | Leseverlauf |
| `idao://notes` | Notizen |

> Kompatibilitätsalias: `idao://` / `idao://home` → Kapitel; `idao://daily` → Studie; `idao://random` → Jagd; `idao://chapter?id={id}` → Autor; `idao://recite` → Kategorienabschnitt; `idao://recite?id={id}` → Kategorien.

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `idao://settings` | Einstellungen |
| `idao://usage-guide` | Nutzungsanleitung |
| `idao://widget-guide` | Widget-Anleitung |
| `idao://shortcuts-guide` | Kurzbefehle-Anleitung |
| `idao://feature-guide` | Einführung erneut abspielen |
| `idao://feedback` | Feedback-E-Mail |
| `idao://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
idao://daily
idao://chapter?id=1
idao://recite?id=1
idao://study
idao://hunt
idao://famous
idao://book?id=ddj
idao://author
idao://search?q=上善若水
```


Verwenden Sie diese in der Shortcuts-App, den Schnellaktionen für den Startbildschirm, den Widgets, dem Control Center oder Safari. Siehe auch In-App **Settings → Shortcuts Guide**.

</section>
<section lang="fr" markdown="1">

iDao prend en charge les liens de raccourci ** `idao://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
idao://{host}?{params}
```


## Chapitres et découvertes

| URL | Ouvre |
|-----|-------|
| `idao://home` | Accueil |
| `idao://daily` | Aujourd'hui le chapitre quotidien |
| `idao://random` | Chapitre aléatoire |
| `idao://chapter?id={id}` | Détail du chapitre |
| `idao://recite` / `idao://recite?id={id}` | Flux de récitation |
| `idao://favorites` | Favoris |
| `idao://famous` | Vers célèbres |
| `idao://search` / `idao://search?q={query}` | Recherche |
| `idao://study` | Salle d'étude |
| `idao://hunt` | Cherchez le Tao ( |
| `idao://mastered` | Maîtrise |
| `idao://categories` / `?section=` | Parcourir (section facultative) |
| `idao://book?id=` | Collection de livres ( ' ddj ' / ' qingjing ' / ' yinfu ') |
| `idao://author` | Intro Laozi |
| `idao://last-read` | Dernière lecture |
| `idao://reading-history` | Historique de lecture |
| `idao://notes` | Notes |

> Alias de compatibilité : `idao://` / `idao://home` → chapitre; `idao://daily` → étude; `idao://random` → chasse; `idao://chapter?id={id}` → auteur; `idao://recite` → catégorie; `idao://recite?id={id}` → catégorie.

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `idao://settings` | Réglages |
| `idao://usage-guide` | Guide d'utilisation |
| `idao://widget-guide` | Guide des widgets |
| `idao://shortcuts-guide` | Guide Raccourcis |
| `idao://feature-guide` | Rejouer l’accueil |
| `idao://feedback` | E-mail de commentaires |
| `idao://in-app-review` | Avis in-app / App Store |

## Exemples


```
idao://daily
idao://chapter?id=1
idao://recite?id=1
idao://study
idao://hunt
idao://famous
idao://book?id=ddj
idao://author
idao://search?q=上善若水
```


Utilisez-les dans l'application Raccourcis, Actions rapides Home Screen, Widgets, Control Center ou Safari. Voir aussi dans l'application **Paramètres → Guide des raccourcis**.

</section>
<section lang="tr" markdown="1">

iDao, ** `idao://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
idao://{host}?{params}
```


## Bölümler ve keşif

| URL | Açar |
|-----|-------|
| `idao://home` | Ana sayfa |
| `idao://daily` | Bugünün Günlük Bölüm |
| `idao://random` | Random Bölüm |
| `idao://chapter?id={id}` | Bölüm detayı |
| `idao://recite` / `idao://recite?id={id}` | Okuma akışı |
| `idao://favorites` | Favoriler |
| `idao://famous` | Ünlü dizeler |
| `idao://search` / `idao://search?q={query}` | Ara |
| `idao://study` | Çalışma Salonu |
| `idao://hunt` | Tao'yu gör ( the) |
| `idao://mastered` | Mastered |
| `idao://categories` / `?section=` | Göze (isteğenim bölümü) |
| `idao://book?id=` | Book collection ('ddj' / "qing" / "yinfu') |
| `idao://author` | Laozi introtro |
| `idao://last-read` | Son okunan |
| `idao://reading-history` | Okuma geçmişi |
| `idao://notes` | Notlar |

> Uyumluluk aliazlar: `idao://` / `idao://home` → bölüm; `idao://daily` → çalışma; `idao://random` → av; `idao://chapter?id={id}` → yazar; `idao://recite` ## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `idao://settings` | Ayarlar |
| `idao://usage-guide` | Kullanım kılavuzu |
| `idao://widget-guide` | Widget kılavuzu |
| `idao://shortcuts-guide` | Kısayol kılavuzu |
| `idao://feature-guide` | Tanıtımı yeniden oynat |
| `idao://feedback` | Geri bildirim e-postası |
| `idao://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
idao://daily
idao://chapter?id=1
idao://recite?id=1
idao://study
idao://hunt
idao://famous
idao://book?id=ddj
idao://author
idao://search?q=上善若水
```


Bunları kısa kesimlerde kullanın, Home Ekran hızlı eylemleri, widgets, Control Center veya Safari. Ayrıca bakınız **Settings → Kısayollar Kılavuzu**.

</section>
