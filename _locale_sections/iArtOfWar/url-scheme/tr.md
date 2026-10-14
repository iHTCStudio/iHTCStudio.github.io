iArtOfWar ** `iartofwar://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
iartofwar://{host}?{params}
```


## Geçişler ve yazarlar

| URL | Açar |
|-----|-------|
| `iartofwar://passage?id={id}` | Pasaj ayrıntısı |
| `iartofwar://couplet?id={id}` / `iartofwar://poem?id={id}` | Aynı geçiş (compatability) |
| `iartofwar://author?id={id}` | Yazar ayrıntısı |
| `iartofwar://recite` / `iartofwar://recite?id={id}` | Okuma akışı |

## Keşfet

| URL | Açar |
|-----|-------|
| `iartofwar://home` | Ana sayfa |
| `iartofwar://daily` | Bugünün Günlük Stratagem |
| `iartofwar://random` | Rastgele pasaj |
| `iartofwar://favorites` | Favoriler |
| `iartofwar://famous` | Ünlü çizgiler / stratagems |
| `iartofwar://search` / `iartofwar://search?q={query}` | Ara |
| `iartofwar://study` | Strateji sınıfı |
| `iartofwar://hunt` | Hunt (fly); alias "keyword-hunt" / "flyflower" |
| `iartofwar://mastered` | Mastered |
| `iartofwar://categories` / `iartofwar://categories?section=` | Göz ('theme', 'volume', ...) |
| `iartofwar://collection?id=` | Kitap koleksiyonu (e.g. ‘sunzi’, “wujing’, “wuzi’; aynı zamanda “isim=’ / “theme=’) |
| `iartofwar://theme?id=` | Stratagem süiti veya hacmi (e.g. “wen-tao”, "kazanan", "sunbin-a") |
| `iartofwar://last-read` | Son okunan |
| `iartofwar://reading-history` | Okuma geçmişi |
| `iartofwar://notes` | Notlar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `iartofwar://settings` | Ayarlar |
| `iartofwar://usage-guide` | Kullanım kılavuzu |
| `iartofwar://widget-guide` | Widget kılavuzu |
| `iartofwar://shortcuts-guide` | Kısayol kılavuzu |
| `iartofwar://feature-guide` | Tanıtımı yeniden oynat |
| `iartofwar://feedback` | Geri bildirim e-postası |
| `iartofwar://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
iartofwar://daily
iartofwar://passage?id=1
iartofwar://collection?id=wuzi
iartofwar://theme?id=wen-tao
iartofwar://study
iartofwar://hunt
```


Bunları kısa kesimlerde kullanın, Home Ekran hızlı eylemleri, widgets veya Safari. Ayrıca bakınız **Settings → Kısayollar Kılavuzu**.


