---
layout: doc
title: iDeveloper — Shortcut Links
app_id: iDeveloper
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: ideveloper:// deep links for iDeveloper — tools, categories, search, references, focus, share, settings guides, and more.
---

<section lang="en" markdown="1">

iDeveloper supports **`ideveloper://`** shortcut links (URL scheme). Cold start and Home Screen shortcuts are delivered through a unified buffer so links are not opened twice after onboarding.

## Link format

```
ideveloper://{host}?{params}
```

## Tools & browse

| URL | Opens |
|-----|-------|
| `ideveloper://home` | Home |
| `ideveloper://tool?id={id}` | Tool detail (e.g. `json`, `base64`, `timestamp`) |
| `ideveloper://category?id={id}` | Category (e.g. `encoding`) |
| `ideveloper://search` / `ideveloper://search?q={query}` | Search |
| `ideveloper://favorites` | Favorites |
| `ideveloper://history` | Operation history |
| `ideveloper://reference` / `ideveloper://reference?id={id}` | Reference center / entry |
| `ideveloper://new-snippet` | New snippet |
| `ideveloper://focus` | Focus timer / Live Activity entry |
| `ideveloper://share?tool={id}` | Open Share handoff into a tool (works with the Share extension + App Group payload) |

## Settings & guides

| URL | Opens |
|-----|-------|
| `ideveloper://settings` | Settings |
| `ideveloper://usage-guide` | Usage guide |
| `ideveloper://widget-guide` | Widget guide |
| `ideveloper://shortcuts-guide` | Shortcuts guide |
| `ideveloper://feature-guide` | Replay onboarding |
| `ideveloper://feedback` | Feedback email |
| `ideveloper://in-app-review` | In-app / Store review entry |

## Examples

```
ideveloper://tool?id=json
ideveloper://search?q=base64
ideveloper://reference?id=http-200
ideveloper://favorites
ideveloper://focus
ideveloper://share?tool=json
ideveloper://category?id=encoding
```

Use these in the Shortcuts app, Home Screen quick actions, widgets, Control Center, or Safari. See also in-app **Settings → Shortcuts Guide**.

</section>
<section lang="zh-CN" markdown="1">

爱开发者支持 **`ideveloper://`** 快捷链接（URL Scheme）。冷启动与主屏快捷经统一缓冲投递，避免引导后重复打开。

## 链接格式

```
ideveloper://{host}?{params}
```

## 工具与浏览

| URL | 打开 |
|-----|------|
| `ideveloper://home` | 首页 |
| `ideveloper://tool?id={id}` | 工具详情（如 `json`、`base64`、`timestamp`） |
| `ideveloper://category?id={id}` | 分类（如 `encoding`） |
| `ideveloper://search` / `ideveloper://search?q={query}` | 搜索 |
| `ideveloper://favorites` | 收藏 |
| `ideveloper://history` | 操作历史 |
| `ideveloper://reference` / `ideveloper://reference?id={id}` | 速查中心 / 条目 |
| `ideveloper://new-snippet` | 新建代码片段 |
| `ideveloper://focus` | 专注计时 / 实时活动 |
| `ideveloper://share?tool={id}` | 分享投递到指定工具（配合分享扩展与 App Group） |

## 设置与教程

| URL | 打开 |
|-----|------|
| `ideveloper://settings` | 设置 |
| `ideveloper://usage-guide` | 使用说明 |
| `ideveloper://widget-guide` | 小组件指南 |
| `ideveloper://shortcuts-guide` | 快捷指南 |
| `ideveloper://feature-guide` | 重播功能引导 |
| `ideveloper://feedback` | 反馈邮件 |
| `ideveloper://in-app-review` | 评分入口 |

## 示例

```
ideveloper://tool?id=json
ideveloper://search?q=base64
ideveloper://reference?id=http-200
ideveloper://favorites
ideveloper://focus
ideveloper://share?tool=json
ideveloper://category?id=encoding
```

可在「快捷指令」、主屏快捷、小组件、控制中心或 Safari 中使用。详见应用内 **设置 → 快捷指南**。

</section>
<section lang="zh-TW" markdown="1">

愛開發者支援 **`ideveloper://`** 快捷連結（URL Scheme）。冷啟動與主畫面捷徑經統一緩衝投遞，避免引導後重複開啟。

## 連結格式

```
ideveloper://{host}?{params}
```

## 工具與瀏覽

| URL | 開啟 |
|-----|------|
| `ideveloper://home` | 首頁 |
| `ideveloper://tool?id={id}` | 工具詳情（如 `json`、`base64`、`timestamp`） |
| `ideveloper://category?id={id}` | 分類（如 `encoding`） |
| `ideveloper://search` / `ideveloper://search?q={query}` | 搜尋 |
| `ideveloper://favorites` | 收藏 |
| `ideveloper://history` | 操作歷史 |
| `ideveloper://reference` / `ideveloper://reference?id={id}` | 速查中心 / 條目 |
| `ideveloper://new-snippet` | 新建程式碼片段 |
| `ideveloper://focus` | 專注計時 / 即時動態 |
| `ideveloper://share?tool={id}` | 分享投遞到指定工具（配合分享延伸功能與 App Group） |

## 設定與教學

| URL | 開啟 |
|-----|------|
| `ideveloper://settings` | 設定 |
| `ideveloper://usage-guide` | 使用說明 |
| `ideveloper://widget-guide` | 小工具指南 |
| `ideveloper://shortcuts-guide` | 捷徑指南 |
| `ideveloper://feature-guide` | 重播功能引導 |
| `ideveloper://feedback` | 回饋郵件 |
| `ideveloper://in-app-review` | 評分入口 |

## 範例

```
ideveloper://tool?id=json
ideveloper://search?q=base64
ideveloper://reference?id=http-200
ideveloper://favorites
ideveloper://focus
ideveloper://share?tool=json
ideveloper://category?id=encoding
```

可在「捷徑」、主畫面捷徑、小工具、控制中心或 Safari 中使用。詳見應用內 **設定 → 捷徑指南**。

</section>
<section lang="ja" markdown="1">

iDeveloperは** `ideveloper://` **ショートカットリンク(URLスキーム)をサポートしています。 コールドスタートとホーム画面のショートカットは、統一されたバッファを介して配信されますので、リンクはオンボーディング後2回開いていません。

## リンク形式


```
ideveloper://{host}?{params}
```


## ツールとブラウズ

| URL | 開く画面 |
|-----|-------|
| `ideveloper://home` | ホーム |
| `ideveloper://tool?id={id}` | ツールの詳細(例:`json`、`base64`、`timestamp`) |
| `ideveloper://category?id={id}` | カテゴリー(例: `encoding`) |
| `ideveloper://search` / `ideveloper://search?q={query}` | 検索 |
| `ideveloper://favorites` | お気に入り |
| `ideveloper://history` | 運用履歴 |
| `ideveloper://reference` / `ideveloper://reference?id={id}` | 参照の中心/記入項目 |
| `ideveloper://new-snippet` | 新しいスニペット |
| `ideveloper://focus` | フォーカスタイマー/ライブアクティビティエントリ |
| `ideveloper://share?tool={id}` | ツールにハンドオフを開く(共有拡張機能+アプリグループペイロード機能) |

## 設定とガイド

| URL | 開く画面 |
|-----|-------|
| `ideveloper://settings` | 設定 |
| `ideveloper://usage-guide` | 使い方ガイド |
| `ideveloper://widget-guide` | ウィジェットガイド |
| `ideveloper://shortcuts-guide` | ショートカットガイド |
| `ideveloper://feature-guide` | オンボーディングの再生 |
| `ideveloper://feedback` | フィードバックメール |
| `ideveloper://in-app-review` | アプリ内／App Store レビュー |

## 例


```
ideveloper://tool?id=json
ideveloper://search?q=base64
ideveloper://reference?id=http-200
ideveloper://favorites
ideveloper://focus
ideveloper://share?tool=json
ideveloper://category?id=encoding
```


これらをショートカットアプリ、ホーム画面のクイックアクション、ウィジェット、コントロールセンター、またはSafariで使用してください。 アプリ内設定 → ショートカットガイド** も参照してください。

</section>
<section lang="ko" markdown="1">

iDeveloper는 ** `ideveloper://` ** 단축키 링크 (URL 계획)를 지원합니다. 콜드 시작 및 홈 화면 단축은 통합 버퍼를 통해 전달되므로 링크가 내장 된 후 두 번 열리지 않습니다.

## 링크 형식


```
ideveloper://{host}?{params}
```


## 도구 및 검색

| URL | 열리는 화면 |
|-----|-------|
| `ideveloper://home` | 홈 |
| `ideveloper://tool?id={id}` | 도구 세부 사항 (예 : `json`, `base64`, `timestamp`) |
| `ideveloper://category?id={id}` | 카테고리 (예: `encoding`) |
| `ideveloper://search` / `ideveloper://search?q={query}` | 검색 |
| `ideveloper://favorites` | 즐겨찾기 |
| `ideveloper://history` | 작업 역사 |
| `ideveloper://reference` / `ideveloper://reference?id={id}` | 참조 센터 / 항목 |
| `ideveloper://new-snippet` | 새로운 스니펫 |
| `ideveloper://focus` | Focus timer / 실시간 활동 참여 |
| `ideveloper://share?tool={id}` | 도구로 공유하기 (Share extension + App Group payload) |

## 설정 및 가이드

| URL | 열리는 화면 |
|-----|-------|
| `ideveloper://settings` | 설정 |
| `ideveloper://usage-guide` | 사용 가이드 |
| `ideveloper://widget-guide` | 위젯 가이드 |
| `ideveloper://shortcuts-guide` | 단축어 가이드 |
| `ideveloper://feature-guide` | 온보딩 다시 보기 |
| `ideveloper://feedback` | 피드백 이메일 |
| `ideveloper://in-app-review` | 앱 내 / App Store 리뷰 |

## 예시


```
ideveloper://tool?id=json
ideveloper://search?q=base64
ideveloper://reference?id=http-200
ideveloper://favorites
ideveloper://focus
ideveloper://share?tool=json
ideveloper://category?id=encoding
```


Shortcuts 앱에서 이러한 사용, 홈 화면 빠른 행동, 위젯, 제어 센터, 또는 사파리. in-app**Settings → 단축키 가이드** 참조.

</section>
<section lang="ru" markdown="1">

iDeveloper поддерживает ярлыки ** `ideveloper://` ** (схема URL). Холодный старт и ярлыки домашнего экрана доставляются через единый буфер, поэтому ссылки не открываются дважды после входа.

## Формат ссылки


```
ideveloper://{host}?{params}
```


## Инструменты & Browse

| URL | Открывает |
|-----|-------|
| `ideveloper://home` | Главная |
| `ideveloper://tool?id={id}` | Детали инструмента (например, "json", "base64", "timestamp") |
| `ideveloper://category?id={id}` | Категория (например, "кодирование") |
| `ideveloper://search` / `ideveloper://search?q={query}` | Поиск |
| `ideveloper://favorites` | Избранное |
| `ideveloper://history` | История операции |
| `ideveloper://reference` / `ideveloper://reference?id={id}` | Справочный центр / вход |
| `ideveloper://new-snippet` | Новый фрагмент |
| `ideveloper://focus` | Фокус таймер / Live Activity |
| `ideveloper://share?tool={id}` | Открытая передача Share в инструмент (работает с расширением Share + полезной нагрузкой App Group) |

## Настройки и руководства

| URL | Открывает |
|-----|-------|
| `ideveloper://settings` | Настройки |
| `ideveloper://usage-guide` | Руководство по использованию |
| `ideveloper://widget-guide` | Руководство по виджетам |
| `ideveloper://shortcuts-guide` | Руководство по «Командам» |
| `ideveloper://feature-guide` | Повторное знакомство |
| `ideveloper://feedback` | Письмо с отзывом |
| `ideveloper://in-app-review` | Отзыв в приложении / App Store |

## Примеры


```
ideveloper://tool?id=json
ideveloper://search?q=base64
ideveloper://reference?id=http-200
ideveloper://favorites
ideveloper://focus
ideveloper://share?tool=json
ideveloper://category?id=encoding
```


Используйте их в приложении Shortcuts, быстрых действиях Home Screen, виджетах, Центре управления или Safari. См. также in-app **Settings → Shortcuts Guide**.

</section>
<section lang="th" markdown="1">

idevolloper รองรับ~ c0 BAR * ลิงก์ลัด (URL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
ideveloper://{host}?{params}
```


## เครื่องมือเรียกดู

| URL | เปิด |
|-----|-------|
| `ideveloper://home` | หน้าแรก |
| `ideveloper://tool?id={id}` | รายละเอียดเครื่องมือ (e.g. `jon', 'เบส64', 'เวลา') |
| `ideveloper://category?id={id}` | หมวดหมู่ (e.g. สืบค้นเมื่อ) |
| `ideveloper://search` / `ideveloper://search?q={query}` | ค้นหา |
| `ideveloper://favorites` | รายการโปรด |
| `ideveloper://history` | ประวัติการปฏิบัติการ |
| `ideveloper://reference` / `ideveloper://reference?id={id}` | ศูนย์อ้างอิง / รายการ |
| `ideveloper://new-snippet` | ชิ้นส่วนตัวใหม่ |
| `ideveloper://focus` | โฟกัสตัวจับเวลา / ถ่ายทอดสด |
| `ideveloper://share?tool={id}` | เปิดการใช้งานร่วมกันเป็นเครื่องมือ (ทํางานกับนามสกุลใช้งานร่วมกัน + App Group) |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `ideveloper://settings` | การตั้งค่า |
| `ideveloper://usage-guide` | คู่มือการใช้งาน |
| `ideveloper://widget-guide` | คู่มือวิดเจ็ต |
| `ideveloper://shortcuts-guide` | คู่มือทางลัด |
| `ideveloper://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `ideveloper://feedback` | อีเมลข้อเสนอแนะ |
| `ideveloper://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
ideveloper://tool?id=json
ideveloper://search?q=base64
ideveloper://reference?id=http-200
ideveloper://favorites
ideveloper://focus
ideveloper://share?tool=json
ideveloper://category?id=encoding
```


ใช้เหล่านี้ในโปรแกรมปุ่มพิมพ์ลัด, การกระทําของหน้าจอส่วนตัวอย่างรวดเร็ว, วิดเจ็ต, ศูนย์ควบคุม, หรือซาฟารี ดูใน-apps ด้วย

</section>
<section lang="de" markdown="1">

iDeveloper unterstützt ** `ideveloper://` ** Shortcut Links (URL-Schema). Kaltstart- und Home Screen-Verknüpfungen werden über einen einheitlichen Puffer geliefert, so dass Links nach dem Onboarding nicht zweimal geöffnet werden.

## Linkformat


```
ideveloper://{host}?{params}
```


## Tools & Browsing

| URL | Öffnet |
|-----|-------|
| `ideveloper://home` | Startseite |
| `ideveloper://tool?id={id}` | Werkzeugdetail (z.B. `json`, `base64`, `timestamp`) |
| `ideveloper://category?id={id}` | Kategorie (z. B. 'encoding') |
| `ideveloper://search` / `ideveloper://search?q={query}` | Suche |
| `ideveloper://favorites` | Favoriten |
| `ideveloper://history` | Betriebsgeschichte |
| `ideveloper://reference` / `ideveloper://reference?id={id}` | Referenzzentrum / Eingang |
| `ideveloper://new-snippet` | Neues Snippet |
| `ideveloper://focus` | Focus Timer / Live Activity Eintrag |
| `ideveloper://share?tool={id}` | Open Share Handoff in ein Tool (funktioniert mit der Share Extension + App Group Payload) |

## Einstellungen & Anleitungen

| URL | Öffnet |
|-----|-------|
| `ideveloper://settings` | Einstellungen |
| `ideveloper://usage-guide` | Nutzungsanleitung |
| `ideveloper://widget-guide` | Widget-Anleitung |
| `ideveloper://shortcuts-guide` | Kurzbefehle-Anleitung |
| `ideveloper://feature-guide` | Einführung erneut abspielen |
| `ideveloper://feedback` | Feedback-E-Mail |
| `ideveloper://in-app-review` | In-App- / App-Store-Bewertung |

## Beispiele


```
ideveloper://tool?id=json
ideveloper://search?q=base64
ideveloper://reference?id=http-200
ideveloper://favorites
ideveloper://focus
ideveloper://share?tool=json
ideveloper://category?id=encoding
```


Verwenden Sie diese in der Shortcuts-App, den Schnellaktionen für den Startbildschirm, den Widgets, dem Control Center oder Safari. Siehe auch In-App **Settings → Shortcuts Guide**.

</section>
<section lang="fr" markdown="1">

iDeveloper prend en charge les liens de raccourci ** `ideveloper://` ** (schéma URL). Les raccourcis de démarrage à froid et d'écran d'accueil sont livrés via un tampon unifié de sorte que les liens ne sont pas ouverts deux fois après l'embarquement.

## Format de lien


```
ideveloper://{host}?{params}
```


## Outils et navigation

| URL | Ouvre |
|-----|-------|
| `ideveloper://home` | Accueil |
| `ideveloper://tool?id={id}` | Détails de l'outil (par exemple `json`, `base64`, `timestamp`) |
| `ideveloper://category?id={id}` | Catégorie (par exemple «encodage») |
| `ideveloper://search` / `ideveloper://search?q={query}` | Recherche |
| `ideveloper://favorites` | Favoris |
| `ideveloper://history` | Historique de l'opération |
| `ideveloper://reference` / `ideveloper://reference?id={id}` | Centre de référence / entrée |
| `ideveloper://new-snippet` | Nouveau extrait |
| `ideveloper://focus` | Temps de focalisation / Entrée d'activité en direct |
| `ideveloper://share?tool={id}` | Ouvrir le partage dans un outil (travaille avec l'extension Partager + charge utile du groupe App) |

## Réglages et guides

| URL | Ouvre |
|-----|-------|
| `ideveloper://settings` | Réglages |
| `ideveloper://usage-guide` | Guide d'utilisation |
| `ideveloper://widget-guide` | Guide des widgets |
| `ideveloper://shortcuts-guide` | Guide Raccourcis |
| `ideveloper://feature-guide` | Rejouer l’accueil |
| `ideveloper://feedback` | E-mail de commentaires |
| `ideveloper://in-app-review` | Avis in-app / App Store |

## Exemples


```
ideveloper://tool?id=json
ideveloper://search?q=base64
ideveloper://reference?id=http-200
ideveloper://favorites
ideveloper://focus
ideveloper://share?tool=json
ideveloper://category?id=encoding
```


Utilisez-les dans l'application Raccourcis, Actions rapides Home Screen, Widgets, Control Center ou Safari. Voir aussi dans l'application **Paramètres → Guide des raccourcis**.

</section>
<section lang="tr" markdown="1">

iDe Developmenter ** `ideveloper://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
ideveloper://{host}?{params}
```


## Araçlar & tarama

| URL | Açar |
|-----|-------|
| `ideveloper://home` | Ana sayfa |
| `ideveloper://tool?id={id}` | Tool detay (e.g. “json’un, “base64”, "timestamp") |
| `ideveloper://category?id={id}` | Kategori (e.g. "encoding") |
| `ideveloper://search` / `ideveloper://search?q={query}` | Ara |
| `ideveloper://favorites` | Favoriler |
| `ideveloper://history` | Tarih |
| `ideveloper://reference` / `ideveloper://reference?id={id}` | Referans merkezi / giriş |
| `ideveloper://new-snippet` | Yeni parçalar |
| `ideveloper://focus` | Focus timer / Live Activity entry entry |
| `ideveloper://share?tool={id}` | Open Share handoff into a tool ( Share extension + App Group ödemeload) |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `ideveloper://settings` | Ayarlar |
| `ideveloper://usage-guide` | Kullanım kılavuzu |
| `ideveloper://widget-guide` | Widget kılavuzu |
| `ideveloper://shortcuts-guide` | Kısayol kılavuzu |
| `ideveloper://feature-guide` | Tanıtımı yeniden oynat |
| `ideveloper://feedback` | Geri bildirim e-postası |
| `ideveloper://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
ideveloper://tool?id=json
ideveloper://search?q=base64
ideveloper://reference?id=http-200
ideveloper://favorites
ideveloper://focus
ideveloper://share?tool=json
ideveloper://category?id=encoding
```


Bunları kısa kesimlerde kullanın, Home Ekran hızlı eylemleri, widgets, Control Center veya Safari. Ayrıca bakınız **Settings → Kısayollar Kılavuzu**.

</section>
