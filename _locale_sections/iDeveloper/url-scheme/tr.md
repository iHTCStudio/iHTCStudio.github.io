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


