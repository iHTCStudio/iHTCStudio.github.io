I Three support ** `ithree://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
ithree://{host}?{params}
```


## Pasajlar ve keşif

| URL | Açar |
|-----|-------|
| `ithree://home` | Ana sayfa |
| `ithree://daily` | Bugünün Günlük Hattı |
| `ithree://random` | Rastgele pasaj |
| `ithree://passage?id={id}` | Pasaj ayrıntısı |
| `ithree://recite` / `ithree://recite?id={id}` | Okuma akışı |
| `ithree://favorites` | Favoriler |
| `ithree://famous` | Ünlü dizeler |
| `ithree://search` / `ithree://search?q={query}` | Ara |
| `ithree://study` | Çalışma sınıfı |
| `ithree://quiz` | Bugünün sınav |
| `ithree://hunt` | Hunt ( Hunt) |
| `ithree://mastered` | Mastered |
| `ithree://categories` | Gözat |
| `ithree://chapter?id={id}` | Bölüm Bölüm Bölüm |
| `ithree://stories` / `ithree://story?id={id}` | Hikayeler / hikaye detay |
| `ithree://books` / `ithree://book?id={id}` | Klasik indeksler / kitap |
| `ithree://dynasties` / `ithree://dynasty?id={id}` | Dynas / Hanedan |
| `ithree://collection?id=` / `?name=` | Koleksiyon (veya kitaplar boşsa) |
| `ithree://last-read` | Son okunan |
| `ithree://reading-history` | Okuma geçmişi |
| `ithree://notes` | Notlar |

> Not: `ithree://` bir uyumluluk alias ve eşleşen **chapter** açıyor.

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `ithree://settings` | Ayarlar |
| `ithree://usage-guide` | Kullanım kılavuzu |
| `ithree://widget-guide` | Widget kılavuzu |
| `ithree://shortcuts-guide` | Kısayol kılavuzu |
| `ithree://feature-guide` | Tanıtımı yeniden oynat |
| `ithree://feedback` | Geri bildirim e-postası |
| `ithree://in-app-review` | Uygulama içi / App Store değerlendirme |
| `ithree://privacy` | In-app gizlilik |

## Örnekler


```
ithree://daily
ithree://passage?id=1
ithree://recite?id=1
ithree://study
ithree://hunt
ithree://quiz
ithree://stories
ithree://search?q=人之初
```


Bunları kısa kesimlerde kullanın, Home Ekran hızlı eylemleri, widgets, Control Center veya Safari. Ayrıca bakınız **Settings → Kısayollar Kılavuzu**.


