i store, ** `istore://` ** kısayollarını destekliyor. Onları **Shortcuts**, Safari kitap işaretlerini veya **widgets**, **Control Center**, **Spotlight** ve **Share Extension a region**, **re-switch your last region**, **

## Bağlantı biçimi


```
istore://{host}?{params}
```


Hosts **case-in sensitive**. Bölge kodları standart **Alpha-2** değerleri ( `istore://` , `us` , `cn` , `jp` , `hk` | What you want | Link Link Link Link |
|---------------|------|
| Switch to a region | "Etmen: http://switch?region={code} |
| Switch to your last region | "istore httpswitch-last" |
| Open the Store / Favorites / Settings tab | "istore httpstore" · "istore https://favorites' · "istore https" |
| Open App Availability | "istore httpavailability" |

---

## Bir bölgeye geçiş

Verilen bölgeye bir geçiş talep eder (eğer etkinleştirirse)


```
istore://switch?region={code}
```


| Parameter | Required | Açıklama |
|-----------|----------|-------------|
| `region` | **Yes** | Bölge kodu, e.g. "us', "cn", "jp', "hk", "tw" |

**Example**


```
istore://switch?region=us
```


Tarafından kullanılır: **interaktif widgets**, **Spotlight** sonuçları ve **Shortcuts / Siri**.

---

## Son bölgenize geçiş


```
istore://switch-last
```


En son geçiş hedefinizi ve anahtarlarınızı tekrar okuyun. Güçler ** Son** Kontrol Merkezi kontrolü (iOS 18+) ve eşleşen Kısa kesim / Siri eylemi.

---

## Tabs & sayfalar (no query)

| URL | Açar |
|-----|-------|
| `istore://store` | Mağaza sekmesi |
| `istore://favorites` | Favoriler sekmesi |
| `istore://settings` | Ayarlar sekmesi |
| `istore://availability` | Ayarlar → App Availability (ayrıca Share Extension tarafından da kullanılır) |
| `istore://switch-history` | Tarih |
| `istore://quick-regions` | Hızlı Bölgeler |
| `istore://feature-guide` | Özellik kılavuzu |
| `istore://widget-guide` | Widget kılavuzu |
| `istore://shortcuts-guide` | Kısayol kılavuzu |
| `istore://usage-guide` | Kullanım kılavuzu |
| `istore://feedback` | Geri bildirim e-postası |
| `istore://in-app-review` | Uygulama içi App Store puanı |

---

## Widgets, Control Center & Spotlight

Bunlar, dokunduğunuzda `istore://` bağlantıları otomatik olarak üretir:

| Source | Tap target | Etkisi Etkisi Etkisi |
|--------|------------|--------|
| **Quick Regions / Recent / Custom widget** | A region tile | "Oturan: " |
| **Switch Last control** (iOS 18+) | The control | "istore httpswitch-last" |
| **Spotlight** | A region result | "Oturan: " |

Widgets ve Control Center'dan interaktif geçiş, resmi App Store yönlendirmesini tamamlamak için uygulamayı açar.

---

## Paylaş

Herhangi bir **App Store linkini paylaşın - i Shop. Share Extension, popüler bölgelerde kullanılabilirliği kontrol eder, sonra uygulama `istore://` aracılığıyla açabilirsiniz, böylece sonucu gözden geçirebilirsiniz ve değiştirebilirsiniz.

---

## Siri & Shortcuts

**Shortcuts ** uygulamasında yerleşik eylemleri bulun veya **Siri**’ye sorun. Başlıklar ve kelimeler İngilizce / . / .'de lokalize edilir.

| Action | What you can set | Etkisi Etkisi Etkisi |
|--------|------------------|--------|
| Switch region | Region | Bu bölgeye Anahtarlar |
| Switch last region | — | Son hedefinize Anahtarlar |
| Switch favorite region | A favorite | Favori bir bölgeye Anahtarlar |
| Open store | — | Opens i store |
| Check availability | App link or ID | Uygulamanın mevcut olduğu kontroller |

---

## Bölge kodları bağlantıları

Derin bağlantılar ve widget tarafından üretilen URL'ler her zaman istikrarlı kullanır **region kodları** ( `istore://` , `us` , `cn` , `jp` , ...) - yerelleştirilmiş ekran isimleri değil.

**Örnekler**


```
istore://switch?region=jp
istore://switch?region=hk
```


[Genellikle] (.) · [FAQ](./faq) · [Privacy] (./privacy)


