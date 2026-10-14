---
layout: doc
title: iPhoto — Shortcut Links
app_id: iPhoto
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接说明
doc_title_zh_tw: 快捷連結說明
description: iphoto:// deep links and Shortcuts for iPhoto — capture, library, editor, guides, and settings.
---

<section lang="en" markdown="1">

iPhoto supports **`iphoto://`** deep links and **App Intents / Siri Shortcuts**. Links only navigate inside the app — they do not upload data.

## Scheme

```
iphoto://<host>[?query]
```

| Rule | Detail |
|------|--------|
| Scheme | `iphoto` |
| Empty | Opens the app’s default tab |
| Unknown hosts | Ignored safely |

---

## Tabs & navigation

| URL | Opens |
|-----|-------|
| `iphoto://library` | Library tab |
| `iphoto://capture` | Capture tab |
| `iphoto://settings` | Settings tab |
| `iphoto://search` | Search tab (iOS 18+) |
| `iphoto://recent-projects` | Library focused on recent work |

---

## Editor

| URL | Opens |
|-----|-------|
| `iphoto://editor?id=<projectID>` | Editor for the given project id |

---

## Guides & actions

| URL | Opens |
|-----|-------|
| `iphoto://usage-guide` | Usage guide |
| `iphoto://widget-guide` | Widget guide |
| `iphoto://shortcuts-guide` | Shortcuts guide |
| `iphoto://feature-guide` | Feature / onboarding replay |
| `iphoto://export-presets` | Export-related settings |
| `iphoto://feedback` | Feedback email |
| `iphoto://in-app-review` | In-app review prompt |

---

## Siri & Shortcuts

Built-in intents include:

- Open Capture
- Open Library
- Import Photos
- Open Settings

Add them in the Shortcuts app or invoke with Siri using the phrases shown in Shortcuts.

## Examples

```
iphoto://capture
iphoto://library
iphoto://editor?id=YOUR-PROJECT-ID
iphoto://widget-guide
```

[FAQ](../faq) · [Privacy Policy](../privacy) · [Back to iPhoto](../)

</section>
<section lang="zh-CN" markdown="1">

爱修图支持 **`iphoto://`** 深链与 **App Intents / Siri 快捷指令**。链接只用于应用内跳转——不会上传数据。

## 协议

```
iphoto://<host>[?query]
```

| 规则 | 说明 |
|------|------|
| Scheme | `iphoto` |
| 空路径 | 打开默认 Tab |
| 未知 host | 安全忽略 |

---

## 标签页与导航

| URL | 打开 |
|-----|------|
| `iphoto://library` | 资源库 |
| `iphoto://capture` | 拍摄 |
| `iphoto://settings` | 设置 |
| `iphoto://search` | 搜索（iOS 18+） |
| `iphoto://recent-projects` | 资源库并关注最近项目 |

---

## 编辑器

| URL | 打开 |
|-----|------|
| `iphoto://editor?id=<projectID>` | 指定项目的编辑器 |

---

## 指南与操作

| URL | 打开 |
|-----|------|
| `iphoto://usage-guide` | 使用指南 |
| `iphoto://widget-guide` | 小组件指南 |
| `iphoto://shortcuts-guide` | 快捷方式指南 |
| `iphoto://feature-guide` | 功能引导（重播） |
| `iphoto://export-presets` | 导出相关设置 |
| `iphoto://feedback` | 反馈邮件 |
| `iphoto://in-app-review` | 应用内评分 |

---

## Siri 与快捷指令

内置意图包括：

- 打开拍摄
- 打开资源库
- 导入照片
- 打开设置

可在「快捷指令」App 中添加，或用 Siri 按短语唤起。

## 示例

```
iphoto://capture
iphoto://library
iphoto://editor?id=YOUR-PROJECT-ID
iphoto://widget-guide
```

[常见问题](../faq) · [隐私政策](../privacy) · [返回爱修图](../)

</section>
<section lang="zh-TW" markdown="1">

愛修圖支援 **`iphoto://`** 深鏈與 **App Intents / Siri 捷徑**。連結只用於應用內跳轉——不會上傳資料。

## 協定

```
iphoto://<host>[?query]
```

| 規則 | 說明 |
|------|------|
| Scheme | `iphoto` |
| 空路徑 | 打開預設 Tab |
| 未知 host | 安全忽略 |

---

## 標籤頁與導覽

| URL | 打開 |
|-----|------|
| `iphoto://library` | 資源庫 |
| `iphoto://capture` | 拍攝 |
| `iphoto://settings` | 設定 |
| `iphoto://search` | 搜尋（iOS 18+） |
| `iphoto://recent-projects` | 資源庫並關注最近項目 |

---

## 編輯器

| URL | 打開 |
|-----|------|
| `iphoto://editor?id=<projectID>` | 指定項目的編輯器 |

---

## 指南與操作

| URL | 打開 |
|-----|------|
| `iphoto://usage-guide` | 使用指南 |
| `iphoto://widget-guide` | 小工具指南 |
| `iphoto://shortcuts-guide` | 捷徑指南 |
| `iphoto://feature-guide` | 功能引導（重播） |
| `iphoto://export-presets` | 匯出相關設定 |
| `iphoto://feedback` | 回饋郵件 |
| `iphoto://in-app-review` | 應用內評分 |

---

## Siri 與捷徑

內建意圖包括：

- 打開拍攝
- 打開資源庫
- 匯入照片
- 打開設定

可在「捷徑」App 中添加，或用 Siri 按短語喚起。

## 範例

```
iphoto://capture
iphoto://library
iphoto://editor?id=YOUR-PROJECT-ID
iphoto://widget-guide
```

[常見問題](../faq) · [隱私政策](../privacy) · [返回愛修圖](../)

</section>
<section lang="ja" markdown="1">

iPhotoは** `iphoto://` **ディープリンクと**アプリのインテント/シリショートカット**をサポートしています。 リンクはアプリ内を移動するだけなので、データをアップロードしません。

## スキーム


```
iphoto://<host>[?query]
```


| Rule | 詳細を見る |
|------|--------|
| Scheme | ライフォト |
| Empty | アプリのデフォルトタブを開きます |
| Unknown hosts | 安全に無視 |

---

## タブとナビゲーション

| URL | 開く画面 |
|-----|-------|
| `iphoto://library` | ライブラリタブ |
| `iphoto://capture` | キャプチャタブ |
| `iphoto://settings` | 設定タブ |
| `iphoto://search` | 検索タブ (iOS 18 +) |
| `iphoto://recent-projects` | 最近の仕事に焦点を当てた図書館 |

---

## ダウンロード

| URL | 開く画面 |
|-----|-------|
| `iphoto://editor?id=<projectID>` | 指定したプロジェクト ID のエディタ |

---

## ガイド&アクション

| URL | 開く画面 |
|-----|-------|
| `iphoto://usage-guide` | 使い方ガイド |
| `iphoto://widget-guide` | ウィジェットガイド |
| `iphoto://shortcuts-guide` | ショートカットガイド |
| `iphoto://feature-guide` | 特徴/転写再生 |
| `iphoto://export-presets` | 輸出関連の設定 |
| `iphoto://feedback` | フィードバックメール |
| `iphoto://in-app-review` | アプリ内レビュー プロンプト |

---

## シリとショートカット

作り付けの意図は下記のものを含んでいます:

- オープンキャプチャ
- オープンライブラリー
- インポート写真
- 設定を開く

Shortcuts アプリで追加するか、ショートカットに示すフレーズを使用して Siri で呼び出す。

## 例


```
iphoto://capture
iphoto://library
iphoto://editor?id=YOUR-PROJECT-ID
iphoto://widget-guide
```


[FAQ](../faq)・[プライバシーポリシー](../privacy)・[iPhotoに戻る](./)

</section>
<section lang="ko" markdown="1">

iPhoto는 ** `iphoto://` ** 깊은 링크와 **App Intents / Siri Shortcuts**를 지원합니다. 링크는 앱 내에서만 이동 - 그들은 데이터를 업로드하지 않습니다.

## 사이트맵


```
iphoto://<host>[?query]
```


| Rule | 제품 정보 |
|------|--------|
| Scheme | iphoto의 |
| Empty | 앱의 기본 탭을 엽니다 |
| Unknown hosts | 안전하다 |

---

## 탭 및 탐색

| URL | 열리는 화면 |
|-----|-------|
| `iphoto://library` | 도서관 탭 |
| `iphoto://capture` | 캡처 탭 |
| `iphoto://settings` | 설정 탭 |
| `iphoto://search` | 검색 탭 (iOS 18+) |
| `iphoto://recent-projects` | 최근 작업에 중점을 둔 도서관 |

---

## 한국어

| URL | 열리는 화면 |
|-----|-------|
| `iphoto://editor?id=<projectID>` | 주어진 프로젝트 ID에 대한 편집기 |

---

## 가이드 & 행동

| URL | 열리는 화면 |
|-----|-------|
| `iphoto://usage-guide` | 사용 가이드 |
| `iphoto://widget-guide` | 위젯 가이드 |
| `iphoto://shortcuts-guide` | 단축어 가이드 |
| `iphoto://feature-guide` | 기능 / 내장 재생 |
| `iphoto://export-presets` | 수출 관련 설정 |
| `iphoto://feedback` | 피드백 이메일 |
| `iphoto://in-app-review` | In-app 검토 신속한 |

---

## Siri 및 단축키

내장 intents 포함:

- 공지사항
- 본문 바로가기
- 수입 사진
- 설정 열기

Shortcuts 앱에 추가하거나 Shortcuts에 표시된 구문을 사용하여 Siri를 호출합니다.

## 예시


```
iphoto://capture
iphoto://library
iphoto://editor?id=YOUR-PROJECT-ID
iphoto://widget-guide
```


[FAQ](../faq) · [개인정보 보호 정책](../privacy) · [iPhoto로 돌아가기](../)

</section>
<section lang="ru" markdown="1">

iPhoto поддерживает ** `iphoto://` ** глубокие ссылки и **App Intents / Siri Shortcuts**. Ссылки перемещаются только внутри приложения — они не загружают данные.

## схема


```
iphoto://<host>[?query]
```


| Rule | Подробнее |
|------|--------|
| Scheme | "Ифото" |
| Empty | Открывает вкладку по умолчанию приложения |
| Unknown hosts | Безопасно игнорируется |

---

## Вкладки и навигация

| URL | Открывает |
|-----|-------|
| `iphoto://library` | Закладка библиотеки |
| `iphoto://capture` | Захват вкладки |
| `iphoto://settings` | Настройка вкладки |
| `iphoto://search` | Поисковая вкладка (iOS 18+) |
| `iphoto://recent-projects` | Библиотека посвящена недавней работе |

---

## редактор

| URL | Открывает |
|-----|-------|
| `iphoto://editor?id=<projectID>` | Редактор для данного проекта id |

---

## Руководство и действия

| URL | Открывает |
|-----|-------|
| `iphoto://usage-guide` | Руководство по использованию |
| `iphoto://widget-guide` | Руководство по виджетам |
| `iphoto://shortcuts-guide` | Руководство по «Командам» |
| `iphoto://feature-guide` | Изображение / onboarding replay |
| `iphoto://export-presets` | Условия, связанные с экспортом |
| `iphoto://feedback` | Письмо с отзывом |
| `iphoto://in-app-review` | Быстрый обзор в приложении |

---

## Siri и Shortcuts

Встроенные намерения включают в себя:

- Открытый захват
- Открытая библиотека
- Импорт фотографий
- Открытые настройки

Добавьте их в приложение Shortcuts или вызовите Siri, используя фразы, показанные в Shortcuts.

## Примеры


```
iphoto://capture
iphoto://library
iphoto://editor?id=YOUR-PROJECT-ID
iphoto://widget-guide
```


[FAQ] (../faq) · [Политика конфиденциальности] (../privacy) · [Назад к iPhoto] (../)

</section>
<section lang="th" markdown="1">

ไอคอมไพล์รองรับ ** `iphoto://` BAR ลิงก์ลึกและ* App Inspects / ปุ่มพิมพ์ลัดเซอร์รี ~. ส่วน เชื่อม ที่ อยู่ ภาย ใน แอพ ไม่ ได้ ส่ง ข้อมูล เข้า ไป.

## ชุดสี


```
iphoto://<host>[?query]
```


| Rule | รายละเอียด |
|------|--------|
| Scheme | อะโอโตะ |
| Empty | เปิดแท็บปริยายของโปรแกรม |
| Unknown hosts | ไม่สนใจความปลอดภัย |

---

## การนําทางแท็บ

| URL | เปิด |
|-----|-------|
| `iphoto://library` | แท็บของไลบรารี |
| `iphoto://capture` | แท็บการจับภาพ |
| `iphoto://settings` | แท็บการตั้งค่า |
| `iphoto://search` | แท็บการค้นหา (iOS 18+) |
| `iphoto://recent-projects` | ห้องสมุดเน้นงานล่าสุด |

---

## เครื่องมือแก้ไข

| URL | เปิด |
|-----|-------|
| `iphoto://editor?id=<projectID>` | เครื่องมือแก้ไขหมายเลขโครงการที่ให้ |

---

## ทิศทางการทํางาน

| URL | เปิด |
|-----|-------|
| `iphoto://usage-guide` | คู่มือการใช้งาน |
| `iphoto://widget-guide` | คู่มือวิดเจ็ต |
| `iphoto://shortcuts-guide` | คู่มือทางลัด |
| `iphoto://feature-guide` | คุณสมบัติ / การเล่นซ้ําบนเครื่อง |
| `iphoto://export-presets` | ตั้งค่าที่เกี่ยวข้องกับการส่งออก |
| `iphoto://feedback` | อีเมลข้อเสนอแนะ |
| `iphoto://in-app-review` | แจ้งเตือนการทบทวนข้อมูลภายใน |

---

## ปุ่มพิมพ์ลัดแบบ Siri

วัตถุประสงค์ที่สร้างขึ้น

- เปิดการจับภาพ
- เปิดไลบรารี
- นําเข้ารูปภาพต่าง ๆ
- ตั้งค่า

เพิ่มพวกเขาในโปรแกรมปุ่มพิมพ์ลัดหรือเรียกใช้งาน Seri โดยใช้วลีที่แสดงในทางลัด

## ตัวอย่าง


```
iphoto://capture
iphoto://library
iphoto://editor?id=YOUR-PROJECT-ID
iphoto://widget-guide
```


[FAQ](./faq). สืบค้นเมื่อ 20 พฤษภาคม พ.ศ.

</section>
<section lang="de" markdown="1">

iPhoto unterstützt ** `iphoto://` ** Deep Links und **App Intents / Siri Shortcuts**. Links navigieren nur innerhalb der App - sie laden keine Daten hoch.

## Regelung


```
iphoto://<host>[?query]
```


| Rule | Einzelheiten |
|------|--------|
| Scheme | „iphoto |
| Empty | Öffnet den Standard-Tab der App |
| Unknown hosts | Ignoriert sicher |

---

## Tabs & Navigation

| URL | Öffnet |
|-----|-------|
| `iphoto://library` | Bibliotheksregister |
| `iphoto://capture` | Fanglasche |
| `iphoto://settings` | Tab Einstellungen |
| `iphoto://search` | Such-Tab (iOS 18+) |
| `iphoto://recent-projects` | Bibliothek konzentriert sich auf die jüngsten Arbeiten |

---

## Herausgeber

| URL | Öffnet |
|-----|-------|
| `iphoto://editor?id=<projectID>` | Editor für die angegebene Projekt-ID |

---

## Leitfäden und Maßnahmen

| URL | Öffnet |
|-----|-------|
| `iphoto://usage-guide` | Nutzungsanleitung |
| `iphoto://widget-guide` | Widget-Anleitung |
| `iphoto://shortcuts-guide` | Kurzbefehle-Anleitung |
| `iphoto://feature-guide` | Feature / Onboarding Replay |
| `iphoto://export-presets` | Einstellungen für Ausfuhren |
| `iphoto://feedback` | Feedback-E-Mail |
| `iphoto://in-app-review` | In-App Review prompt |

---

## Siri & Shortcuts

Eingebaute Absichten umfassen:

- Open Capture
- Offene Bibliothek
- Importfotos
- Offene Einstellungen

Fügen Sie sie in der Shortcuts-App hinzu oder rufen Sie mit Siri die in Shortcuts gezeigten Phrasen auf.

## Beispiele


```
iphoto://capture
iphoto://library
iphoto://editor?id=YOUR-PROJECT-ID
iphoto://widget-guide
```


[FAQ](../faq) · [Privacy Policy](../Privacy) · [Zurück zu iPhoto](../]

</section>
<section lang="fr" markdown="1">

iPhoto prend en charge ** `iphoto://` ** liens profonds et **Apptents / Raccourcis Siri**. Les liens naviguent uniquement à l'intérieur de l'application — ils ne téléchargent pas les données.

## Régime


```
iphoto://<host>[?query]
```


| Rule | Détail |
|------|--------|
| Scheme | "iphoto" |
| Empty | Ouvre l'onglet par défaut de l'application |
| Unknown hosts | Ignoré en toute sécurité |

---

## Tabs & navigation

| URL | Ouvre |
|-----|-------|
| `iphoto://library` | Onglet Bibliothèque |
| `iphoto://capture` | onglet de capture |
| `iphoto://settings` | Onglet Paramètres |
| `iphoto://search` | Onglet Recherche (iOS 18+) |
| `iphoto://recent-projects` | Bibliothèque axée sur les travaux récents |

---

## Éditeur

| URL | Ouvre |
|-----|-------|
| `iphoto://editor?id=<projectID>` | Éditeur pour l'id du projet donné |

---

## Guides et actions

| URL | Ouvre |
|-----|-------|
| `iphoto://usage-guide` | Guide d'utilisation |
| `iphoto://widget-guide` | Guide des widgets |
| `iphoto://shortcuts-guide` | Guide Raccourcis |
| `iphoto://feature-guide` | Fonctionnalité / rejouage à bord |
| `iphoto://export-presets` | Paramètres liés aux exportations |
| `iphoto://feedback` | E-mail de commentaires |
| `iphoto://in-app-review` | Révision rapide de l'application |

---

## Siri & raccourcis

Les objectifs intégrés comprennent :

- Ouvrir la capture
- Ouvrir la bibliothèque
- Importer des photos
- Ouvrir les paramètres

Ajoutez-les dans l'application Raccourcis ou invoquez avec Siri en utilisant les phrases indiquées dans Raccourcis.

## Exemples


```
iphoto://capture
iphoto://library
iphoto://editor?id=YOUR-PROJECT-ID
iphoto://widget-guide
```


[FAQ](../faq) · [Politique de confidentialité](../privacité) · [Retour à iPhoto](../)

</section>
<section lang="tr" markdown="1">

iPhoto, ** `iphoto://` ** derin bağlantılar ve **Uygulama niyetleri / Siri Kısakesler**. Bağlantılar sadece uygulama içinde dolaşıyor - verileri yüklemezler.

## Scheme


```
iphoto://<host>[?query]
```


| Rule | Detaylı Bilgi |
|------|--------|
| Scheme | " |
| Empty | Uygulamanın varsayılan sekmesini açın |
| Unknown hosts | Ignored güvenle |

---

## Tabs & navigasyon

| URL | Açar |
|-----|-------|
| `iphoto://library` | Kütüphane sekmesi |
| `iphoto://capture` | yakalama sekmesi |
| `iphoto://settings` | Ayarlar sekmesi |
| `iphoto://search` | Arama sekmesi (iOS 18+) |
| `iphoto://recent-projects` | Kütüphane son çalışmaya odaklandı |

---

## Editor Editor Editor

| URL | Açar |
|-----|-------|
| `iphoto://editor?id=<projectID>` | Verilen proje için editör |

---

## Rehberler ve eylemler

| URL | Açar |
|-----|-------|
| `iphoto://usage-guide` | Kullanım kılavuzu |
| `iphoto://widget-guide` | Widget kılavuzu |
| `iphoto://shortcuts-guide` | Kısayol kılavuzu |
| `iphoto://feature-guide` | Feature / onboarding replay |
| `iphoto://export-presets` | İhracatla ilgili ayarlar |
| `iphoto://feedback` | Geri bildirim e-postası |
| `iphoto://in-app-review` | In-app review Hızlı |

---

## Siri & Shortcuts

Yerleşik niyetler şunları içerir:

- Open Capture
- Open Library
- İthalat Fotoğraflar
- Açık Ayarlar

Onları Shortcuts uygulamasında veya Siri ile kısa kesimlerde belirtilen cümleleri kullanarak ekleyin.

## Örnekler


```
iphoto://capture
iphoto://library
iphoto://editor?id=YOUR-PROJECT-ID
iphoto://widget-guide
```


[FAQ](./faq) · [Privacy Policy](./privacy)

</section>
