---
layout: doc
title: iLiezi — Shortcut Links
app_id: iLiezi
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: iliezi:// deep links for iLiezi — Daily Liezi, Liezi Study, unique desks, and settings guides.
---

<section lang="en" markdown="1">

爱列子 / iLiezi supports **`iliezi://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
iliezi://{host}?{params}
```

## Unique desk

| URL | Opens |
|-----|-------|
| `iliezi://daily` | Daily Liezi |
| `iliezi://fable?id=` / `iliezi://fables` | Fable hall |
| `iliezi://concepts` / `iliezi://concept?id=` | xu / wind / ming |
| `iliezi://volume?id=1…8` | Eight parts |
| `iliezi://study` | Liezi Study |
| `iliezi://hunt` | Hunt Liezi |

## Shared reading paths

| URL | Opens |
|-----|-------|
| `iliezi://home` | Home |
| `iliezi://passage?id=` / `iliezi://chapter?id=` | Passage detail |
| `iliezi://recite` / `iliezi://recite?id=` | Recite |
| `iliezi://random` | Random passage |
| `iliezi://favorites` | Favorites |
| `iliezi://search?q=` | Search |
| `iliezi://famous` | Famous lines |
| `iliezi://categories` | Browse |
| `iliezi://last-read` | Last read |
| `iliezi://reading-history` | Reading history |
| `iliezi://notes` | Notes |
| `iliezi://handwriting` | Handwriting search (iOS) |
| `iliezi://settings` | Settings |
| `iliezi://usage-guide` | Usage guide |
| `iliezi://widget-guide` | Widget guide |
| `iliezi://shortcuts-guide` | Shortcuts guide |
| `iliezi://feature-guide` | Replay onboarding |
| `iliezi://feedback` | Feedback email |

## Examples

```
iliezi://daily
iliezi://fables
iliezi://volume?id=5
iliezi://study
```

</section>
<section lang="zh-CN" markdown="1">

爱列子 支持 **`iliezi://`** 快捷链接（URL Scheme）。冷启动与主屏幕快捷方式经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
iliezi://{host}?{params}
```

## 独有书桌

| URL | 打开 |
|-----|------|
| `iliezi://daily` | 每日一列 |
| `iliezi://fable?id=` / `iliezi://fables` | 寓言馆 |
| `iliezi://concepts` / `iliezi://concept?id=` | 贵虚 / 风 / 命 |
| `iliezi://volume?id=1…8` | 八卷 |
| `iliezi://study` | 列学学堂 |
| `iliezi://hunt` | 寻列 |

## 共用阅读路径

| URL | 打开 |
|-----|------|
| `iliezi://home` | 首页 |
| `iliezi://passage?id=` / `iliezi://chapter?id=` | 篇目详情 |
| `iliezi://recite` / `iliezi://recite?id=` | 诵读 |
| `iliezi://random` | 随机一篇 |
| `iliezi://favorites` | 收藏 |
| `iliezi://search?q=` | 搜索 |
| `iliezi://famous` | 名句 |
| `iliezi://categories` | 浏览 |
| `iliezi://last-read` | 上次阅读 |
| `iliezi://reading-history` | 阅读历史 |
| `iliezi://notes` | 笔记 |
| `iliezi://handwriting` | 手写寻句（iOS） |
| `iliezi://settings` | 设置 |
| `iliezi://usage-guide` | 使用说明 |
| `iliezi://widget-guide` | 小组件说明 |
| `iliezi://shortcuts-guide` | 快捷指令说明 |
| `iliezi://feature-guide` | 重看引导 |
| `iliezi://feedback` | 反馈邮件 |

## 示例

```
iliezi://daily
iliezi://fables
iliezi://volume?id=5
iliezi://study
```

</section>
<section lang="zh-TW" markdown="1">

愛列子 支援 **`iliezi://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複打開。

## 連結格式

```
iliezi://{host}?{params}
```

## 獨有書桌

| URL | 打開 |
|-----|------|
| `iliezi://daily` | 每日一列 |
| `iliezi://fable?id=` / `iliezi://fables` | 寓言館 |
| `iliezi://concepts` / `iliezi://concept?id=` | 貴虛 / 風 / 命 |
| `iliezi://volume?id=1…8` | 八卷 |
| `iliezi://study` | 列學學堂 |
| `iliezi://hunt` | 尋列 |

## 共用閱讀路徑

| URL | 打開 |
|-----|------|
| `iliezi://home` | 首頁 |
| `iliezi://passage?id=` / `iliezi://chapter?id=` | 篇目詳情 |
| `iliezi://recite` / `iliezi://recite?id=` | 誦讀 |
| `iliezi://random` | 隨機一篇 |
| `iliezi://favorites` | 收藏 |
| `iliezi://search?q=` | 搜尋 |
| `iliezi://famous` | 名句 |
| `iliezi://categories` | 瀏覽 |
| `iliezi://last-read` | 上次閱讀 |
| `iliezi://reading-history` | 閱讀歷史 |
| `iliezi://notes` | 筆記 |
| `iliezi://handwriting` | 手寫尋句（iOS） |
| `iliezi://settings` | 設定 |
| `iliezi://usage-guide` | 使用說明 |
| `iliezi://widget-guide` | 小工具說明 |
| `iliezi://shortcuts-guide` | 捷徑說明 |
| `iliezi://feature-guide` | 重看引導 |
| `iliezi://feedback` | 回饋郵件 |

## 範例

```
iliezi://daily
iliezi://fables
iliezi://volume?id=5
iliezi://study
```

</section>
<section lang="ja" markdown="1">

iLieziは、** `iliezi://` **のショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
iliezi://{host}?{params}
```


## ユニークなデスク

| URL | 開く画面 |
|-----|-------|
| `iliezi://daily` | デイリー・ライツィヒ |
| `iliezi://fable?id=` / `iliezi://fables` | ファブルホール |
| `iliezi://concepts` / `iliezi://concept?id=` | xu/風/ming |
| `iliezi://volume?id=1…8` | 8つの部品 |
| `iliezi://study` | Lieziスタディ |
| `iliezi://hunt` | 叔母 Liezi |

## 共有読書道

| URL | 開く画面 |
|-----|-------|
| `iliezi://home` | ホーム |
| `iliezi://passage?id=` / `iliezi://chapter?id=` | 章句の詳細 |
| `iliezi://recite` / `iliezi://recite?id=` | リサイト |
| `iliezi://random` | ランダムな章句 |
| `iliezi://favorites` | お気に入り |
| `iliezi://search?q=` | 検索 |
| `iliezi://famous` | 名句一覧 |
| `iliezi://categories` | ブラウズ |
| `iliezi://last-read` | 最後に読んだ項目 |
| `iliezi://reading-history` | 閲覧履歴 |
| `iliezi://notes` | ノート |
| `iliezi://handwriting` | 手書き検索(iOS) |
| `iliezi://settings` | 設定 |
| `iliezi://usage-guide` | 使い方ガイド |
| `iliezi://widget-guide` | ウィジェットガイド |
| `iliezi://shortcuts-guide` | ショートカットガイド |
| `iliezi://feature-guide` | オンボーディングの再生 |
| `iliezi://feedback` | フィードバックメール |

## 例


```
iliezi://daily
iliezi://fables
iliezi://volume?id=5
iliezi://study
```

</section>
<section lang="ko" markdown="1">

short子 / iLiezi 지원 ** `iliezi://` ** 단축 링크 (URL 계획). 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
iliezi://{host}?{params}
```


## 회사 소개

| URL | 열리는 화면 |
|-----|-------|
| `iliezi://daily` | 매일 Liezi |
| `iliezi://fable?id=` / `iliezi://fables` | Fable 홀 |
| `iliezi://concepts` / `iliezi://concept?id=` | xu/바람/ming |
| `iliezi://volume?id=1…8` | 8개 부품 |
| `iliezi://study` | Liezi 연구 |
| `iliezi://hunt` | 사냥 Liezi |

## 자주 묻는 질문

| URL | 열리는 화면 |
|-----|-------|
| `iliezi://home` | 홈 |
| `iliezi://passage?id=` / `iliezi://chapter?id=` | 구절 상세 |
| `iliezi://recite` / `iliezi://recite?id=` | 공지사항 |
| `iliezi://random` | 무작위 구절 |
| `iliezi://favorites` | 즐겨찾기 |
| `iliezi://search?q=` | 검색 |
| `iliezi://famous` | 명구 목록 |
| `iliezi://categories` | 둘러보기 |
| `iliezi://last-read` | 마지막으로 읽은 항목 |
| `iliezi://reading-history` | 읽기 기록 |
| `iliezi://notes` | 메모 |
| `iliezi://handwriting` | Handwriting 검색 (iOS) |
| `iliezi://settings` | 설정 |
| `iliezi://usage-guide` | 사용 가이드 |
| `iliezi://widget-guide` | 위젯 가이드 |
| `iliezi://shortcuts-guide` | 단축어 가이드 |
| `iliezi://feature-guide` | 온보딩 다시 보기 |
| `iliezi://feedback` | 피드백 이메일 |

## 예시


```
iliezi://daily
iliezi://fables
iliezi://volume?id=5
iliezi://study
```

</section>
<section lang="ru" markdown="1">

). / iLiezi поддерживает ярлыки ** `iliezi://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
iliezi://{host}?{params}
```


## Уникальный стол

| URL | Открывает |
|-----|-------|
| `iliezi://daily` | Ежедневный Лиези |
| `iliezi://fable?id=` / `iliezi://fables` | Сказочный зал |
| `iliezi://concepts` / `iliezi://concept?id=` | ху / ветер / мин |
| `iliezi://volume?id=1…8` | Восемь частей |
| `iliezi://study` | Лизи исследование |
| `iliezi://hunt` | Хант Лиези |

## Общие пути чтения

| URL | Открывает |
|-----|-------|
| `iliezi://home` | Главная |
| `iliezi://passage?id=` / `iliezi://chapter?id=` | Страница отрывка |
| `iliezi://recite` / `iliezi://recite?id=` | читать |
| `iliezi://random` | Случайный отрывок |
| `iliezi://favorites` | Избранное |
| `iliezi://search?q=` | Поиск |
| `iliezi://famous` | Знаменитые строки |
| `iliezi://categories` | Обзор |
| `iliezi://last-read` | Последнее прочитанное |
| `iliezi://reading-history` | История чтения |
| `iliezi://notes` | Заметки |
| `iliezi://handwriting` | Поиск почерка (iOS) |
| `iliezi://settings` | Настройки |
| `iliezi://usage-guide` | Руководство по использованию |
| `iliezi://widget-guide` | Руководство по виджетам |
| `iliezi://shortcuts-guide` | Руководство по «Командам» |
| `iliezi://feature-guide` | Повторное знакомство |
| `iliezi://feedback` | Письмо с отзывом |

## Примеры


```
iliezi://daily
iliezi://fables
iliezi://volume?id=5
iliezi://study
```

</section>
<section lang="th" markdown="1">

爱列/ILiezi รองรับ~ `iliezi://` BAR *ลิงก์ลัด (URL scheme). การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
iliezi://{host}?{params}
```


## โต๊ะยูนิโค้ด

| URL | เปิด |
|-----|-------|
| `iliezi://daily` | ลิซี |
| `iliezi://fable?id=` / `iliezi://fables` | ห้องโถง |
| `iliezi://concepts` / `iliezi://concept?id=` | xu / ลม / ming |
| `iliezi://volume?id=1…8` | แปดส่วน |
| `iliezi://study` | การศึกษาแบบไลซี |
| `iliezi://hunt` | ฮันท์ ไลซี |

## พาธในการอ่านร่วมกัน

| URL | เปิด |
|-----|-------|
| `iliezi://home` | หน้าแรก |
| `iliezi://passage?id=` / `iliezi://chapter?id=` | รายละเอียดข้อความ |
| `iliezi://recite` / `iliezi://recite?id=` | บันทึก |
| `iliezi://random` | ข้อความแบบสุ่ม |
| `iliezi://favorites` | รายการโปรด |
| `iliezi://search?q=` | ค้นหา |
| `iliezi://famous` | บรรทัดขึ้นชื่อ |
| `iliezi://categories` | เรียกดู |
| `iliezi://last-read` | รายการที่อ่านล่าสุด |
| `iliezi://reading-history` | ประวัติการอ่าน |
| `iliezi://notes` | บันทึก |
| `iliezi://handwriting` | สืบค้นโดยใช้ลายมือ (ไอOS) |
| `iliezi://settings` | การตั้งค่า |
| `iliezi://usage-guide` | คู่มือการใช้งาน |
| `iliezi://widget-guide` | คู่มือวิดเจ็ต |
| `iliezi://shortcuts-guide` | คู่มือทางลัด |
| `iliezi://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `iliezi://feedback` | อีเมลข้อเสนอแนะ |

## ตัวอย่าง


```
iliezi://daily
iliezi://fables
iliezi://volume?id=5
iliezi://study
```

</section>
<section lang="de" markdown="1">

爱列子 / iLiezi unterstützt ** `iliezi://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
iliezi://{host}?{params}
```


## Einzigartiger Schreibtisch

| URL | Öffnet |
|-----|-------|
| `iliezi://daily` | Tägliche Liezi |
| `iliezi://fable?id=` / `iliezi://fables` | Fable Hall |
| `iliezi://concepts` / `iliezi://concept?id=` | xu/Wind/ming |
| `iliezi://volume?id=1…8` | Acht Teile |
| `iliezi://study` | Liezi-Studie |
| `iliezi://hunt` | Hunt Liezi |

## Gemeinsame Lesepfade

| URL | Öffnet |
|-----|-------|
| `iliezi://home` | Startseite |
| `iliezi://passage?id=` / `iliezi://chapter?id=` | Passagen-Detail |
| `iliezi://recite` / `iliezi://recite?id=` | Rezit |
| `iliezi://random` | Zufällige Passage |
| `iliezi://favorites` | Favoriten |
| `iliezi://search?q=` | Suche |
| `iliezi://famous` | Berühmte Zeilen |
| `iliezi://categories` | Durchsuchen |
| `iliezi://last-read` | Zuletzt gelesen |
| `iliezi://reading-history` | Leseverlauf |
| `iliezi://notes` | Notizen |
| `iliezi://handwriting` | Handschriftsuche (iOS) |
| `iliezi://settings` | Einstellungen |
| `iliezi://usage-guide` | Nutzungsanleitung |
| `iliezi://widget-guide` | Widget-Anleitung |
| `iliezi://shortcuts-guide` | Kurzbefehle-Anleitung |
| `iliezi://feature-guide` | Einführung erneut abspielen |
| `iliezi://feedback` | Feedback-E-Mail |

## Beispiele


```
iliezi://daily
iliezi://fables
iliezi://volume?id=5
iliezi://study
```

</section>
<section lang="fr" markdown="1">

Le logiciel iLiezi prend en charge les liens de raccourci ** `iliezi://` ** (système URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
iliezi://{host}?{params}
```


## Bureau unique

| URL | Ouvre |
|-----|-------|
| `iliezi://daily` | Tous les jours Liezi |
| `iliezi://fable?id=` / `iliezi://fables` | Fable Hall |
| `iliezi://concepts` / `iliezi://concept?id=` | xu / vent / ming |
| `iliezi://volume?id=1…8` | Huit parties |
| `iliezi://study` | Étude Liezi |
| `iliezi://hunt` | Chasse Liezi |

## Voies de lecture partagées

| URL | Ouvre |
|-----|-------|
| `iliezi://home` | Accueil |
| `iliezi://passage?id=` / `iliezi://chapter?id=` | Détail du passage |
| `iliezi://recite` / `iliezi://recite?id=` | Récite |
| `iliezi://random` | Passage aléatoire |
| `iliezi://favorites` | Favoris |
| `iliezi://search?q=` | Recherche |
| `iliezi://famous` | Vers célèbres |
| `iliezi://categories` | Parcourir |
| `iliezi://last-read` | Dernière lecture |
| `iliezi://reading-history` | Historique de lecture |
| `iliezi://notes` | Notes |
| `iliezi://handwriting` | Recherche d'écriture (iOS) |
| `iliezi://settings` | Réglages |
| `iliezi://usage-guide` | Guide d'utilisation |
| `iliezi://widget-guide` | Guide des widgets |
| `iliezi://shortcuts-guide` | Guide Raccourcis |
| `iliezi://feature-guide` | Rejouer l’accueil |
| `iliezi://feedback` | E-mail de commentaires |

## Exemples


```
iliezi://daily
iliezi://fables
iliezi://volume?id=5
iliezi://study
```

</section>
<section lang="tr" markdown="1">

). / iLiezi, ** `iliezi://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
iliezi://{host}?{params}
```


## Benzersiz masası

| URL | Açar |
|-----|-------|
| `iliezi://daily` | Daily Liezi |
| `iliezi://fable?id=` / `iliezi://fables` | Fable hall |
| `iliezi://concepts` / `iliezi://concept?id=` | xu / rüzgar / ming |
| `iliezi://volume?id=1…8` | Sekiz parça |
| `iliezi://study` | Liezi Çalışması |
| `iliezi://hunt` | Hunt Liezi |

## Ortak okuma yolları

| URL | Açar |
|-----|-------|
| `iliezi://home` | Ana sayfa |
| `iliezi://passage?id=` / `iliezi://chapter?id=` | Pasaj ayrıntısı |
| `iliezi://recite` / `iliezi://recite?id=` | Recite |
| `iliezi://random` | Rastgele pasaj |
| `iliezi://favorites` | Favoriler |
| `iliezi://search?q=` | Ara |
| `iliezi://famous` | Ünlü dizeler |
| `iliezi://categories` | Gözat |
| `iliezi://last-read` | Son okunan |
| `iliezi://reading-history` | Okuma geçmişi |
| `iliezi://notes` | Notlar |
| `iliezi://handwriting` | Hand writing search (iOS) |
| `iliezi://settings` | Ayarlar |
| `iliezi://usage-guide` | Kullanım kılavuzu |
| `iliezi://widget-guide` | Widget kılavuzu |
| `iliezi://shortcuts-guide` | Kısayol kılavuzu |
| `iliezi://feature-guide` | Tanıtımı yeniden oynat |
| `iliezi://feedback` | Geri bildirim e-postası |

## Örnekler


```
iliezi://daily
iliezi://fables
iliezi://volume?id=5
iliezi://study
```

</section>
