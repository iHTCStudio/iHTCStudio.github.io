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


