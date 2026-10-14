iThousand ** `ithousand://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
ithousand://{host}?{params}
```


## Pasajlar, yazarlar ve karakterler

| URL | Açar |
|-----|-------|
| `ithousand://passage?id={id}` | Pasaj ayrıntısı |
| `ithousand://passage?id={id}&open=study` | Passage → Primer Hall |
| `ithousand://passage?id={id}&open=characters` | Passage → karakter masası |
| `ithousand://passage?id={id}&open=note` | Pasaj → not |
| `ithousand://author?id={id}` | Yazar ayrıntısı |
| `ithousand://recite` / `ithousand://recite?id={id}` | Okuma akışı |
| `ithousand://characters` | Karakter kütüphanesi |
| `ithousand://character?char=天` | Bir karakter kartı |
| `ithousand://characters?id={id}` | Karakter kartı ID |
| `ithousand://saved-characters` | Saved Characters |
| `ithousand://saved-famous` | Kaydeten ünlü hatları |

## Keşfet

| URL | Açar |
|-----|-------|
| `ithousand://home` | Ana sayfa |
| `ithousand://daily` | Bugünün Günlük Hattı |
| `ithousand://random` | Rastgele pasaj |
| `ithousand://favorites` | Favoriler |
| `ithousand://list?id={uuid}` | Kişisel bir liste (千单) |
| `ithousand://famous` | Ünlü dizeler |
| `ithousand://search` / `ithousand://search?q={query}` | Ara |
| `ithousand://study` | Primer Hall |
| `ithousand://hunt` | Hunt (fly); alias "keyword-hunt" / "flyflower" |
| `ithousand://mastered` | Mastered |
| `ithousand://categories` / `ithousand://categories?section=` | Gözat |
| `ithousand://collection?id=qianziwen` | Primer koleksiyonu (isim='un da desteklenen) |
| `ithousand://theme?id=dizigui-filial` | Tema |
| `ithousand://last-read` | Son okunan |
| `ithousand://reading-history` | Okuma geçmişi |
| `ithousand://notes` | Notlar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `ithousand://settings` | Ayarlar |
| `ithousand://privacy` | In-app gizlilik |
| `ithousand://usage-guide` | Kullanım kılavuzu |
| `ithousand://widget-guide` | Widget kılavuzu |
| `ithousand://shortcuts-guide` | Kısayol kılavuzu |
| `ithousand://feature-guide` | Tanıtımı yeniden oynat |
| `ithousand://feedback` | Geri bildirim e-postası |
| `ithousand://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
ithousand://daily
ithousand://passage?id=1
ithousand://passage?id=1&open=characters
ithousand://character?char=天
ithousand://collection?id=qianziwen
ithousand://study
ithousand://hunt
ithousand://saved-characters
```


Bunları kısa kesimlerde kullanın, Home Ekran hızlı eylemleri, widgets veya Safari. Mevcut olduğunda istikrarlı `ithousand://` parametreleri tercih edin. Ayrıca bakınız **Settings → Kısayollar Kılavuzu**.


