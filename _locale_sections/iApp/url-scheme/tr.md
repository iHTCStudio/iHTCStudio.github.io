iApp ** `iapp://` ** ve ** `iappstore://` ** kısayol bağlantıları destekler. Onları **Shortcuts**, Safari kitapmarks veya **Home Ekran widgets ** ve **Live Activity** to ** bir uygulama detay sayfasını açın**, ** filtrelenen Rankings view**, **switch sekmeleri **, veya **En iyi sayfalar için tıklayınız.

> **Not:** Long-press **Home Ekran Hızlı Eylemler ** aynı `iapp://` bağlantı metnini kullanıyor ancak hızlı eylemler olarak gönderilir - aynı yolu Safari / Kısa kesimler URL'leri yalnızca ikon menülerinden açıldığından beri iptal edilmedi.

## Bağlantı biçimi


```
iapp://...
iappstore://...   (older alias, works the same)
```


Hosts **case-in sensitive** ve normalize to **kebab-case** ( `iapp://` ve `iappstore://` → `iapp://{host}` ). Legacy alias: `developer_favorites` → sıra, `developer.favorites` → abonelik, `developer-favorites` → inceleme.

| What you want | Link tipi |
|---------------|-----------|
| Open an app detail page | "Iniapp:" |
| Open Rankings with filters | "Aptal:" |
| Switch tabs or open settings pages | "Aptal http" (aşağıdaki tablolara bakın) |
| Tap an app in a widget | Detaylı sayfayı açın |
| Tap the widget title / blank area | Anahtarlar eşleşen Rankings görünümü |
| Tap a rank **Live Activity** | Anahtarlar eşleşen Rankings görünümü |
| Tap a subscription **Live Activity** | Uygulama detay sayfasını açın |

---

## Bir uygulama detay sayfası açın


```
iapp://app?id={APP_ID}&region={region}&country={cc}
```


| Parameter | Required | Açıklama |
|-----------|----------|-------------|
| `id` | **Yes** | App Store ID |
| `region` | No | Bölge kodu, e.g. ‘cn’, “us’, “jp’ (default: “us’) |
| `country` | No | Seçmeli bölge kodu “region’ is omized |

**Example**


```
iapp://app?id=6446581591&region=cn
```


Tarafından kullanılır: **My Favorites widget** (tap an app), ** Live Live Activity** (tap the activity), ve **Shortcuts ** / kitap işaretleri.

---

## Filtrelerle Açık Sıralamalar

Anahtarlar ** Sortings ** sekmesi ve seçilmiş grafikler, kategori ve bölgenizi uygular.


```
iapp://rank?type={chart}&category={category}&region={region}
```


| Parameter | Açıklama |
|-----------|-------------|
| `type` | Grafik kodu (aşağıdaki tabloya bakınız) |
| `category` | Kategori kodu - ana kategori veya oyun alt kategori |
| `region` | Bölge kodu, e.g. ‘cn’, “us’ |

Tanımlanmamış değerler göz ardı edilir; tanınan değerler hatırlanır.

### Grafik kodları ( `iapp://` ) – 12 grafik

| Code | Grafik |
|------|-------|
| `topFreeApplications` | iPhone Top Free |
| `topPaidApplications` | iPhone Top Ücretli |
| `topGrossingApplications` | iPhone Top Grossing |
| `newApplications` | Yeni Uygulamalar |
| `newFreeApplications` | Yeni Ücretsiz |
| `newPaidApplications` | Yeni Ücretli Yeni |
| `topFreeiPadApplications` | iPad Top Free |
| `topPaidiPadApplications` | iPad Top Paid |
| `topGrossingiPadApplications` | iPad Top Grossing |
| `topFreeMacApplications` | Mac Top Free |
| `topPaidMacApplications` | Mac Top Ücretli |
| `topGrossingMacApplications` | Mac Top Grossing |

### Kategori kodları ( `iapp://` )

| Code | Kategori Kategori |
|------|----------|
| `0` | Tüm Uygulamalar |
| `6014` | Oyunlar (tüm oyunlar) |
| `6005` | Sosyal Sosyal Sosyal |
| `6007` | Verimlilik Verimliliği |
| `6002` | Utilities |
| `6008` | Foto & Video |
| `6017` | Eğitim Eğitimi |
| `6015` | Finans Finans |
| … | 26 ana kategori toplam |

**Game subcategories: ** `iapp://` - `iappstore://` , `iapp://{host}` C3    (18 türler). Örnek: `developer.favorites` = Action.

### Örnekler


```
iapp://rank?type=topFreeApplications&category=6014&region=cn
iapp://rank?type=topFreeMacApplications&category=0&region=us
```


### Eski Çin tarzı bağlantıları (still supported)


```
iapp://rank?type=热门免费榜&category=游戏&region=中国
```


Tarafından kullanılır: ** Sortings widget** (tap unvanı / boş alan), **rank Live Activity** (tap the activity), ve **Shortcuts**.

---

## Widget derin bağlantılar

Widgets ayrı bir URL formatı kullanmaz - aynı `iapp://` ve `iappstore://` bağlantıları otomatik olarak üretirler.

| Widget | Tap target | Açıklar |
|--------|------------|-------|
| **Rankings · iApp** | An app row | "Arap http?"id=...&region=..." |
| **Rankings · iApp** | Title or blank area | "Ses #rank?type=...&category=...&region=..." |
| **My Favorites · iApp** | An app row | "Arap http?"id=...&region=..." |

Pinned favoriler ilk olarak My Favorites widget'da görünüyor. Widget teması ve dili takip **Settings → Widgets** ve uygulama diliniz (18 dilden herhangi biri). widget bölgelerini yapılandırırken, HK / TW / MO listede ve birleşik aramada daha net görüntü isimleri gösterir (e.g. “China”, “HK”); depolama alanı **codes ** bağlantılarda `iapp://` , `iapp://{host}` ---

## Göz geçmişi (bir URL bağlantısı değil)

**App Browse History**, **Settings → Data → App Göz Tarih**. Bir giriş iApp içindeki ayrıntılı sayfayı yeniden açıyor - ** değil - dış kopyalayabilir veya paylaşabileceğiniz bir `iapp://` URL kullanın.

---

## Canlı Aktivite derin bağlantıları

| Live Activity type | Tap behavior | Link |
|--------------------|--------------|----------------|
| **Rankings** (tracking preset) | Opens filtered Rankings | "Aptal:" |
| **Subscriptions** (per subscription) | Opens app detail | "Arap http?"id=...&region=..." |

Enable Rank Live Activity per follow preset in **Settings → Advanced**. Enable abonelik Live Activity in **Settings → Advanced → Live Activity** (separate from Rank Live Activity); o zaman abonelik başına veya düzenleme. Price-drop monitörleri Lock Ekrandaki mevcut fiyatla temel gösteriyor.

---

## Tab & aksiyon bağlantıları (göle)

Bu bir sekme açın veya bir uygulama eylemi tetikler. **Shortcuts**, Safari ve **Home Ekran Hızlı Eylemler**.

### İlk sekmeler

| URL | Açar |
|-----|--------|
| `iapp://search` | Arama sekme + odak arama alanı |
| `iapp://rank` | Sıralamalar sekmesi (gösterme olmadığında filtre değişikliği) |
| `iapp://favorites` | **Favorites sekmesi ** Eğer etkinleştirilirse **Settings → App Ayarları**; aksi takdirde **Settings → App Favorites** |
| `iapp://subscription` | Abonelik sekmesi görünürse; aksi takdirde **Settings → Abonelikler** |
| `iapp://settings` | Ayarlar sekmesi |
| `iapp://feedback` | Geri bildirim e-postası |
| `iapp://review` | In-app App Store rating (alias: "iapp http://rate') |

### ikincil sayfalar

Opens **Settings** sekmesi ilk önce, sonra hedef sayfayı zorlar. Bir eşleşen sekme mevcutsa (e.g. Developer Favorites), bu sekmeyi yerine açar.

| URL | Açar |
|-----|--------|
| `iapp://developer-favorites` | Geliştirici Favorites sekmesi veya **Settings → Developer Favorites** |
| `iapp://browse-history` | **Settings → Data → App Browse History** |
| `iapp://favorite-groups` | **Settings → Data → Favorite groups** |
| `iapp://rank-tracking` | **Settings → Advanced → Rank İzleme** |
| `iapp://live-activity` | **Settings → Advanced → Live Activity** |
| `iapp://apple-services` | **Bölümler → Üçüncü taraf → Apple Services** |
| `iapp://region-switch` | **Settings → Üçüncü taraf → App Store Bölgesi** |
| `iapp://usage-guide` | **Bölümler → Yardım → Kullanım Talimatları** |
| `iapp://widget-guide` | **Settings → Widgets → Widget Guide** (iOS 17+ sadece; URL çalışır ancak Quick Actions picker'de listelenmez) |

---

## Home Screen Quick Actions

Uygulama ikonunu uzun baskı. **4**'ye kadar özelleştirin **15 ** seçenekler in **Settings → Home Ekran Uzun Basın → Kısayollar**.

Varsayılan seçim: arama, sıralama, favoriler, geri bildirim.

Her seçenek `iapp://` kullanır - yukarıdaki gibi aynı URL'ler. Hızlı eylemler ikon menüsü aracılığıyla gönderilir; Dış Kısayollar / Safari birleşik `iappstore://` yolu kullanır.

| Bağlantı | Açar |
|------|--------|
| `iapp://search` | Arama sekmesi + odak |
| `iapp://rank` | Sıralamalar sekmesi |
| `iapp://favorites` | Favoriler sekmesi veya Ayarlar → App Favorites |
| `iapp://developer-favorites` | Geliştirici Favoriler sekmesi veya Ayarlar → Geliştirici Favorites |
| `iapp://subscription` | Abonelik sekmesi veya Ayarlar → Abonelikler |
| `iapp://browse-history` | App Browse History |
| `iapp://favorite-groups` | Favori Grupları |
| `iapp://rank-tracking` | Rank Takip |
| `iapp://live-activity` | Canlı Aktivite ayarları |
| `iapp://apple-services` | Apple Services bağlantıları |
| `iapp://region-switch` | App Store Bölgesi Değiştir |
| `iapp://usage-guide` | Kullanım talimatları |
| `iapp://settings` | Ayarlar sekmesi |
| `iapp://feedback` | Geri bildirim e-postası |
| `iapp://review` | In-app rating | `iapp://` dış bir URL olarak destekleniyor ancak ** Quick Actions picker'de mevcut değil.

---

## Siri & Shortcuts (iOS 16+)

**Shortcuts ** uygulamasında yerleşik eylemleri bulun veya **Siri**’ye sorun. Tüm niyet başlıkları, parametre etiketleri ve Siri cümleleri ** her uygulama dilinde yerelleştirilmiş** - değiştirirler - değiştirirken güncellenirler **Dettings → Görünüm → Dil**.

| Action | What you can set | Etkisi Etkisi Etkisi |
|--------|------------------|--------|
| Search apps | Keyword and region | Opens Search sekmesi with query |
| Open charts | Chart, category, and region | Açıklar filtrelerle Sıralamalar (“iapp //rank’) |
| Add favorite | App ID and region | Favorilere sessizce ekleyin |

**Example Siri cümleleri (İngilizce UI):** *" Arama uygulamaları iApp"*, *"Open grafikler iApp"*, *"Add favorite in iApp"*. .'de, ifadeler Çin'de görünür; tüm 18 dil için aynı.

---

## Mac klavye kısayolları

Mac'te, **.1** aracılığıyla **.N ** sekmelerini değiştirmek için. Sayılar **dinamik olarak ** hangi sekmelere göre belirlenir:

| When visible | Tipik kısayol |
|--------------|------------------|
| Rankings | ⌘1 |
| Search | 2 |
| Subscriptions (if shown) | Sonraki numara |
| Favorites (if tab enabled) | Sonraki numara |
| Developer Favorites (if tab enabled) | Sonraki numara |
| Settings | Son sayı |

Tüm Seçmeli sekmelerle örnek: .1 Rankings · .2 Arama · .3 Abonelik · .4 Favorites · ⌘5 Geliştirici Favoriler · ⌘6 Ayarlar.

Bir sekme gizli olduğunda, kalan sekmeler otomatik olarak tekrarlanır.

---

## Bölge kodları bağlantıları

Derin bağlantılar ve widget tarafından üretilen URL'ler her zaman istikrarlı kullanır **region kodları** ( `iapp://` , `iappstore://` , `developer_favorites` , `developer.favorites` , ...) - yerelleştirilmiş ekran isimleri değil. Bölge seçicileri ve arama daha net etiketler gösterebilir, ancak depolama kodları aynı kalır.

**Örnekler**


```
iapp://app?id=6446581591&region=hk
iapp://rank?type=topFreeApplications&category=0&region=tw
```


---

## In-app search ( URL bağlantıları değil)

Bu çalışma iApp içinde ama **not ** `iapp://` URLs:

| Action | Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl Nasıl?HowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHow HowHowHowHowHowHow HowHowHowHow HowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHowHow HowHow HowHow HowHow HowHow HowHow HowHow HowHowHowHowHowHowHowHowHowHowHow HowHow HowHowHowHowHow HowHow HowHow HowHow HowHow HowHow HowHow HowHow HowHowHow HowHowHow HowHow HowHow HowHow |
|--------|-----|
| **Single App ID search** | Aramada bir sayısal kimlik (6-12 basamak, hiçbir komün) girin |
| **Batch App ID search** | 50 komünlü kimliklere kadar |
| **Add Subscription** | Long-press any app row |
| **Save Developer** | Uzun baskı → **Developer ** submenu, veya detay **More** menüsü |
| **Open by-ranking view** | Context menu → aynı geliştirme uygulamaları veya geliştirici favoriler |
| **Pause / resume subscription** | Bir abonelik sırasına uzun baskı |
| **Reopen from browse history** | **Settings → Data → App Browse History** → musluk girişi |

Kullanım ** `iapp://` ** bağlantıları veya **Siri / Kısa kesimler** uygulama dışında iApp açmanız gerektiğinde.

---

## İpuçları

- Link codes work in any app language — UI dilini değiştirirken değişmezler.
- Widgets ve **Live Activity **, dokunduğunuzda bu bağlantıları otomatik olarak üretir.
- Bazı Mac /iPad için Widget grafik verileri ana uygulamadan biraz farklı olabilir.
- **Add favorite** via Shortcuts does not open the app UI — Doğrudan favorilerinize yazar.
- **Content compare** mode in all-region info cannot export share images — İlk önce liste veya ağ görünümüne geçiş.

[Genellikle] (.) · [FAQ](./faq) · [Privacy] (./privacy)


