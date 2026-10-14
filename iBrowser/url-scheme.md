---
layout: doc
title: iBrowser — Shortcut Links
app_id: iBrowser
doc_title_en: Shortcut Links
doc_title_zh_cn: 快捷链接
doc_title_zh_tw: 快捷連結
description: ibrowser:// deep links for Shortcuts, Siri, widgets and Home Screen quick actions.
---

<section lang="en" markdown="1">

iBrowser supports **`ibrowser://`** deep links — open from Apple **Shortcuts**, **Siri**, Home Screen widgets, or the app icon long-press menu.

> **Child lock:** When **Force-hide address bar** is on, destinations other than **home** / **settings** / **guide** open the **home page** instead (bookmarks list only allows the home URL). Settings still asks for the password if enabled.

## Destinations

| URL | Opens |
|-----|--------|
| `ibrowser://home` | Home page from Settings |
| `ibrowser://search` | Focus the address bar |
| `ibrowser://search?q=keyword` | Search with the configured engine |
| `ibrowser://last` | Last successfully loaded page on this device (falls back to home) |
| `ibrowser://bookmarks` | Bookmark list |
| `ibrowser://settings` | Settings (password if enabled) |
| `ibrowser://guide` | Feature tour |
| `ibrowser://open?url=` | Open a specific `http`/`https` URL (percent-encoded) |

`http` / `https` links handed to the app by the system are **not** deep links — they load as external pages as-is.

## Siri & Shortcuts (iOS 16+)

Ask Siri or build a Shortcut to: open home, search, continue last page, bookmarks, Settings, feature tour, or open a URL.

## Home Screen quick actions

Long-press the app icon (up to **4** items). Defaults: home · continue last · search · bookmarks. Customize order / visibility in **Settings → Home Screen Quick Actions**; you can also add Settings or the feature tour. With child lock on, only **Open Home** remains.

[Support](../) · [FAQ](../faq) · [Privacy Policy](../privacy)

</section>
<section lang="zh-CN" markdown="1">

全屏浏览器支持 **`ibrowser://`** 深链 — 可用于苹果**快捷指令**、**Siri**、主屏小组件或长按图标。

> **儿童锁：** 开启**强制隐藏地址栏**时，除主页 / 设置 / 功能导览外，其他入口会改开**主页**（书签列表也只放行主页 URL）。设置若有密码仍会校验。

## 目标

| URL | 打开 |
|-----|------|
| `ibrowser://home` | 设置中的主页 |
| `ibrowser://search` | 唤出地址栏 |
| `ibrowser://search?q=关键词` | 用当前搜索引擎搜索 |
| `ibrowser://last` | 本机上次成功加载的页面（没有则回主页） |
| `ibrowser://bookmarks` | 书签列表 |
| `ibrowser://settings` | 设置（有密码先校验） |
| `ibrowser://guide` | 功能导览 |
| `ibrowser://open?url=` | 打开指定 `http`/`https` 网址（需编码） |

系统交给应用的 `http` / `https` **不是**深链，会按外来网页原样加载。

## Siri 与快捷指令（iOS 16+）

可打开主页、搜索、继续上次、书签、设置、功能导览，或打开指定网址。

## 主屏幕快捷操作

长按图标最多 **4** 项。默认：主页 · 继续上次 · 搜索 · 书签。在 **设置 → 主屏幕快捷操作** 中排序 / 隐藏，也可换成设置或功能导览。儿童锁开启时无论怎么配置只留「打开主页」。

[支持页](../) · [常见问题](../faq) · [隐私政策](../privacy)

</section>
<section lang="zh-TW" markdown="1">

全螢幕瀏覽器支援 **`ibrowser://`** 深鏈 — 可用於蘋果**捷徑**、**Siri**、主畫面小工具或長按圖示。

> **兒童鎖：** 開啟**強制隱藏網址列**時，除主頁 / 設定 / 功能導覽外，其他入口會改開**主頁**（書籤列表也只放行主頁 URL）。設定若有密碼仍會校驗。

## 目標

| URL | 打開 |
|-----|------|
| `ibrowser://home` | 設定中的主頁 |
| `ibrowser://search` | 喚出網址列 |
| `ibrowser://search?q=關鍵詞` | 用當前搜尋引擎搜尋 |
| `ibrowser://last` | 本機上次成功載入的頁面（沒有則回主頁） |
| `ibrowser://bookmarks` | 書籤列表 |
| `ibrowser://settings` | 設定（有密碼先校驗） |
| `ibrowser://guide` | 功能導覽 |
| `ibrowser://open?url=` | 打開指定 `http`/`https` 網址（需編碼） |

系統交給應用的 `http` / `https` **不是**深鏈，會按外來網頁原樣載入。

## Siri 與捷徑（iOS 16+）

可打開主頁、搜尋、繼續上次、書籤、設定、功能導覽，或打開指定網址。

## 主畫面快捷操作

長按圖示最多 **4** 項。預設：主頁 · 繼續上次 · 搜尋 · 書籤。在 **設定 → 主畫面快捷操作** 中排序 / 隱藏，也可換成設定或功能導覽。兒童鎖開啟時無論怎麼配置只留「打開主頁」。

[支援頁](../) · [常見問題](../faq) · [隱私政策](../privacy)

</section>
<section lang="ja" markdown="1">

iBrowserは、Apple **ショートカット**、**Siri**、ホーム画面ウィジェット、またはアプリアイコンのロングプレスメニューから開く、**            **ディープリンクをサポートしています。

> **子供のロック:** **Force-hideアドレスバー**がオンの場合、**home** / **settings** / **guide**以外の目的地は、**ホームページ**を代わりに開きます(ブックマークリストはホームURLのみを許可します)。 設定は、有効にしている場合は、パスワードを要求します。

## 行き先

| URL | 開く画面 |
|-----|--------|
| `ibrowser://home` | 設定からホームページ |
| `ibrowser://search` | アドレスバーをフォーカス |
| `ibrowser://search?q=keyword` | 構成されたエンジンで検索 |
| `ibrowser://last` | このページの先頭へ戻る |
| `ibrowser://bookmarks` | ブックマークリスト |
| `ibrowser://settings` | 設定(有効な場合のパスワード) |
| `ibrowser://guide` | 特徴ツアー |
| `ibrowser://open?url=` | 特定の `http`/`https` URL (パーセントエンコード) を開く | `ibrowser://` は、システムによってアプリに手渡されたリンクは**深いリンクではなく、外部ページとして読み込みます。

## シリ & ショートカット (iOS 16+)

Siri または Shortcut をビルドする: 自宅を開き、検索、最後のページを続けて、ブックマーク、設定、機能ツアー、または URL を開きます。

## ホーム スクリーンのクイックアクション

アプリアイコンを長押し(最大4**アイテム)。 デフォルト: ホーム・続行・検索・ブックマーク。 *Settings → Home Screen Quick Actions**で注文/可視性をカスタマイズします。設定または機能ツアーを追加することもできます。 お子様のロックをオンにすると、**Open Home**が残っています。

[サポート](../)・[FAQ](../faq)・[プライバシーポリシー](../privacy)

</section>
<section lang="ko" markdown="1">

iBrowser는 ** `ibrowser://` ** 딥 링크 — Apple**Shortcuts**,**Siri**, Home Screen 위젯, 또는 앱 아이콘 롱 프레스 메뉴에서 열립니다.

> ** 어린이 자물쇠:** **Force-hide address bar**가 켜지면 **home**/**settings**/**guide**가 **home 페이지**를 엽니다. 대신 (bookmarks list는 홈 URL만 허용됩니다). 설정은 여전히 사용할 경우 암호를 요청합니다.

## 대상 화면

| URL | 열리는 화면 |
|-----|--------|
| `ibrowser://home` | 설정에서 홈 페이지 |
| `ibrowser://search` | 주소 표시 |
| `ibrowser://search?q=keyword` | 구성된 엔진으로 검색 |
| `ibrowser://last` | 마지막으로 성공적으로이 장치에서 페이지를로드 (가로 돌아가십시오) |
| `ibrowser://bookmarks` | 즐겨찾기 |
| `ibrowser://settings` | 설정 ( 활성화된 경우 패스워드) |
| `ibrowser://guide` | 관광 명소 |
| `ibrowser://open?url=` | 특정한 `http`/`https` URL을 엽니다 (percent-encoded) | `ibrowser://` / `ibrowser://home` 링크를 입력하여 시스템에 의해 앱을 잡은 ** 딥 링크 — 그들은 외부 페이지로로드합니다.

## Siri 및 단축키 (iOS 16+)

Siri를 요청하거나 단축키를 구축하십시오. 집, 검색, 마지막 페이지, 북마크, 설정, 기능 투어 또는 URL을 엽니다.

## 홈 화면 빠른 작업

앱 아이콘(최대 **4** 항목)을 압축합니다. 기본값: 집 · 계속 지속 · 검색 · bookmarks. **Settings → Home Screen Quick Actions**에서 주문 / 가시성을 사용자 정의하십시오. 또한 설정 또는 기능 투어를 추가 할 수 있습니다. 어린이 자물쇠로, **열려있는 집** 남아 있습니다.

[지원](../) · [FAQ](../faq) · [개인정보 보호정책](../privacy)

</section>
<section lang="ru" markdown="1">

iBrowser поддерживает ** `ibrowser://` ** глубокие ссылки — открытые из Apple **Shortcuts**, **Siri**, виджетов домашнего экрана или иконки приложения в меню с длинным нажатием.

> ** Детский замок:** Если адресная строка **Force-hide** включена, пункты назначения, отличные от **home** / **settings** / **guide**, вместо этого откройте страницу **home** (список закладок позволяет использовать только домашний URL). Настройки по-прежнему запрашивают пароль, если он включен.

## Назначения

| URL | Открывает |
|-----|--------|
| `ibrowser://home` | Домашняя страница от Settings |
| `ibrowser://search` | Сосредоточьте адресную строку |
| `ibrowser://search?q=keyword` | Поиск с настроенным движком |
| `ibrowser://last` | Последняя успешно загруженная страница на этом устройстве (возвращается домой) |
| `ibrowser://bookmarks` | Список закладок |
| `ibrowser://settings` | Параметры (пароль, если включен) |
| `ibrowser://guide` | Особенности тура |
| `ibrowser://open?url=` | Откройте конкретный URL http/https (закодированный в процентах) |

Ссылки `ibrowser://` / `ibrowser://home` , передаваемые в приложение системой, являются **не** глубокими ссылками — они загружаются как внешние страницы.

## Siri & Shortcuts (iOS 16+)

Попросите Siri или создайте ярлык: откройте дом, ищите, продолжайте последнюю страницу, закладки, настройки, тур по функциям или откройте URL.

## Домой Экран Быстрые действия

Дальше нажмите значок приложения (до **4** элементов). Дефолты: Home · продолжить последний · поиск · закладки. Настройка порядка / видимости в ** Настройки → Домашний экран Быстрые действия **; Вы также можете добавить Настройки или экскурсию по функциям. При включении детского замка остается только «Открытый дом».

[Поддержка] (../) · [FAQ] (../faq) · [Политика конфиденциальности] (../privacy)

</section>
<section lang="th" markdown="1">

iBrowser รองรับ~ `ibrowser://` BAR ลิงก์ลึก — เปิดจาก Apple ~, ~ เซรี~, วิดเจ็ตหน้าจอส่วนตัว หรือเมนูบีบอัดแบบยาวของแอพ

> ~ล็อค: ~ เมื่อ < force-hide bargow อยู่บน, ปลายทางอื่นที่ไม่ใช่~ / ~ การตั้งค่า ~ /~ เปิดหน้าเว็บส่วนตัว~ การตั้งค่ายังคงร้องขอรหัสผ่านหากเปิดใช้งาน

## ปลายทาง

| URL | เปิด |
|-----|--------|
| `ibrowser://home` | หน้าหลักจากการตั้งค่า |
| `ibrowser://search` | โฟกัสไปยังแถบที่อยู่ |
| `ibrowser://search?q=keyword` | ค้นหาด้วยกลไกปรับแต่ง |
| `ibrowser://last` | เรียกหน้าสุดท้ายที่โหลดมาแล้วบนอุปกรณ์นี้ (ย้อนกลับ) |
| `ibrowser://bookmarks` | รายการที่คั่นหน้า |
| `ibrowser://settings` | ตั้งค่า (เปิดการใช้รหัสผ่าน) |
| `ibrowser://guide` | การเดินทัวร์แบบธรรมชาติ |
| `ibrowser://open?url=` | เปิดที่อยู่ URL ของ 'http'/'https' ที่ระบุ (รหัสหลัก) | `ibrowser://` BAR   BAR `ibrowser://home` BAR ลิงก์ที่ส่งไปยังโปรแกรมโดยระบบคือ... ไม่ใช่ลิงก์ลึก -- มันโหลดเป็นหน้าภายนอกเป็น-s

## Siri & ปุ่มพิมพ์ลัด (inOS 16+)

ถามสิริหรือสร้างปุ่มพิมพ์ลัดให้: open home, สืบค้น, ดําเนินการต่อหน้าสุดท้าย, ที่คั่นหน้า, การตั้งค่า, การพา ชม, หรือเปิดที่อยู่ URL

## การกระทํากับหน้าจอส่วนตัวอย่างรวดเร็ว

กดเมาส์แบบยาว (ขึ้นไป- 4 รายการ) ค่าปริยาย: home  continuation eth search date ปรับแต่งลําดับ / มองเห็นใน ~ ตั้งโปรแกรมหน้าจอส่วนตัว '~; นอกจากนี้คุณยังสามารถเพิ่มการตั้งค่า หรือเรียกดูเนื้อหาได้ มีเด็กล็อค มีเพียงบ้านเปิดเท่านั้น

[Support](./). สืบค้นเมื่อ 20 พฤษภาคม พ.ศ.

</section>
<section lang="de" markdown="1">

iBrowser unterstützt ** `ibrowser://` ** Deep Links – geöffnet von Apple **Shortcuts**, **Siri**, Home Screen Widgets oder dem App-Symbol Long-Press-Menü.

> **Kindersperre:** Wenn die Adressleiste **Force-hide ** eingeschaltet ist, öffnen andere Ziele als **home ** / **settings ** / **guide ** stattdessen die **home-Seite ** (Lesezeichenliste erlaubt nur die Home-URL). Die Einstellungen fragen immer noch nach dem Passwort, wenn es aktiviert ist.

## Ziele

| URL | Öffnet |
|-----|--------|
| `ibrowser://home` | Startseite von Settings |
| `ibrowser://search` | Fokussieren Sie die Adressleiste |
| `ibrowser://search?q=keyword` | Suche mit der konfigurierten Engine |
| `ibrowser://last` | Letzte erfolgreich geladene Seite auf diesem Gerät (fällt zurück nach Hause) |
| `ibrowser://bookmarks` | Lesezeichenliste |
| `ibrowser://settings` | Einstellungen (Passwort, wenn aktiviert) |
| `ibrowser://guide` | Feature Tour |
| `ibrowser://open?url=` | Öffnen Sie eine bestimmte `http`/`https` URL (prozentig codiert) | `ibrowser://` / `ibrowser://home` -Links, die vom System an die App übergeben wurden, sind **nicht** tiefe Links - sie werden als externe Seiten geladen.

## Siri & Shortcuts (iOS 16+)

Fragen Sie Siri oder erstellen Sie eine Verknüpfung zu: Öffnen Sie Ihr Zuhause, suchen Sie, setzen Sie die letzte Seite fort, Lesezeichen, Einstellungen, Feature-Tour oder öffnen Sie eine URL.

## Home Bildschirm Schnelle Aktionen

Drücken Sie das App-Symbol (bis zu **4** Artikel). Standardeinstellungen: home · continue last · search · bookmarks. Anpassen der Reihenfolge / Sichtbarkeit in ** Einstellungen → Startbildschirm Quick Actions **; Sie können auch Einstellungen oder die Feature-Tour hinzufügen. Mit Kindersperre bleibt nur **Open Home** übrig.

[Support](../) · [FAQ](../faq) · [Privacy Policy](../Privacy)

</section>
<section lang="fr" markdown="1">

iBrowser prend en charge ** `ibrowser://` ** liens profonds — ouvert à partir d'Apple **Shortcuts**, **Siri**, Widgets d'écran d'accueil, ou le menu longue pression de l'icône de l'application.

> **Serrure pour enfant:** Lorsque **La barre d'adresses du masque de force** est sur, les destinations autres que **home** / **settings** / **guide** ouvrent la page **home** à la place (la liste des signets permet uniquement l'URL d'accueil). Les paramètres demandent toujours le mot de passe si activé.

## Destinations

| URL | Ouvre |
|-----|--------|
| `ibrowser://home` | Page d'accueil de Paramètres |
| `ibrowser://search` | Concentrez la barre d'adresse |
| `ibrowser://search?q=keyword` | Recherche avec le moteur configuré |
| `ibrowser://last` | Dernière page chargée avec succès sur cet appareil (retour à la maison) |
| `ibrowser://bookmarks` | Liste des signets |
| `ibrowser://settings` | Paramètres (mot de passe si activé) |
| `ibrowser://guide` | Visite principale |
| `ibrowser://open?url=` | Ouvrir une URL spécifique `http`/`https` (encodée en pourcentage) | `ibrowser://` / `ibrowser://home` les liens remis à l'application par le système sont **pas** des liens profonds — ils chargent comme des pages externes comme-est.

## Siri & Raccourcis (iOS 16+)

Demandez à Siri ou créez un raccourci pour : ouvrir la page d'accueil, rechercher, continuer la dernière page, signets, paramètres, visite de fonctionnalités ou ouvrir une URL.

## Actions rapides de l'écran d'accueil

Appuyez longuement sur l'icône de l'application (jusqu'à **4** éléments). Par défaut : accueil · continuer dernière · recherche · signets. Personnalisez l'ordre / la visibilité dans **Paramètres → Actions rapides de l'écran d'accueil**; vous pouvez également ajouter des paramètres ou la visite des fonctionnalités. Avec la fermeture d'enfant, seulement **Open Home** reste.

[Soutien](../) · [FAQ](../faq) · [Politique de confidentialité](../privacy)

</section>
<section lang="tr" markdown="1">

iBrowser, ** `ibrowser://` ** derin bağlantılar - Apple **Shortcuts**, **Siri**, Home Ekran widgets veya uygulama i uzun baskı menülerini destekler.

> **Çocuk kilidi:** **Force-hide adresi bar**, **home'dan başka yerlerdir ** / **kess ** / **guide** sadece ev URL'sine izin verir (kitap işaretleri listesi sadece ev URL'sine izin verir). Ayarlar hala etkinleştirilen şifreyi sorar.

## Hedefler

| URL | Açar |
|-----|--------|
| `ibrowser://home` | Home page from Settings |
| `ibrowser://search` | Adres barı |
| `ibrowser://search?q=keyword` | yapılandırılmış motorla arama |
| `ibrowser://last` | Bu cihazda son başarıyla yüklenen sayfa ( eve geri döner) |
| `ibrowser://bookmarks` | Bookmark listesi |
| `ibrowser://settings` | Ayarlar (belirliyse) |
| `ibrowser://guide` | Özel tur |
| `ibrowser://open?url=` | Belirli bir "http'/"https' URL (percent-encoded) | `ibrowser://` / `ibrowser://home` bağlantı sistemi tarafından uygulamaya verilen bağlantılar ** derin bağlantılar - dış sayfaların as-is olarak yükleniyor.

## Siri & Shortcuts (iOS 16+)

Siri'ye sorun ya da kısa bir yol oluşturun: açık ev, arama, son sayfaya devam edin, kitap işaretleri, Ayarlar, özel tur veya bir URL açın.

## Home Ekran hızlı eylemleri

Uygulama ikonunu uzun baskı ( **4** öğelerine kadar). Varsayılanlikler: ev · son · arama · kitap işaretleri. Özel sipariş / görünürlük **Settings → Home Ekran Hızlı Eylemler**; Ayrıca Ayarlar veya özel tur ekleyebilirsiniz. Çocuk kilidi ile sadece **Open Home** kalır.

[Demek](./) · [FAQ](./faq) · [Privacy Policy](./privacy)

</section>
