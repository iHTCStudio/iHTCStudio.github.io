iXunZi, ** `ixunzi://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
ixunzi://{host}?{params}
```


## Geçişler ve yazarlar

| URL | Açar |
|-----|-------|
| `ixunzi://passage?id={id}` | Pasaj ayrıntısı |
| `ixunzi://saying?id={id}` / `ixunzi://couplet?id={id}` / `ixunzi://poem?id={id}` | Aynı geçiş (compatability) |
| `ixunzi://passage?id={id}&card=1` | Pasaj detay ve kart sayfası |
| `ixunzi://card?id={id}` / `ixunzi://share-card?id={id}` | kartları |
| `ixunzi://author?id={id}` | Yazar ayrıntısı |
| `ixunzi://recite` / `ixunzi://recite?id={id}` | Okuma akışı |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `ixunzi://home` | Ana sayfa |
| `ixunzi://daily` | Daily Xun |
| `ixunzi://random` | Rastgele pasaj |
| `ixunzi://favorites` | Favoriler |
| `ixunzi://famous` | Ünlü dizeler |
| `ixunzi://search` / `ixunzi://search?q={query}` | Ara |
| `ixunzi://study` / `ixunzi://study?id={id}` | Öğrenme Akademisi |
| `ixunzi://hunt` | Xun Hunt ('keyword-hunt' / 'flyflower') |
| `ixunzi://handwriting` | Hand writing search ('handwrite'; iOS) |
| `ixunzi://mastered` | Mastered ('progress') |
| `ixunzi://categories` / `ixunzi://categories?section=` | Gözat |
| `ixunzi://collection?id=` | Koleksiyon / kitap |
| `ixunzi://corpus` | Bütün geçitler ('all') |
| `ixunzi://last-read` | Son okunan |
| `ixunzi://reading-history` | Okuma geçmişi |
| `ixunzi://notes` | Notlar |
| `ixunzi://ask` | Xunzi |
| `ixunzi://fables` / `ixunzi://allegories` / `ixunzi://concepts` | Mevcut özel raflar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `ixunzi://settings` | Ayarlar |
| `ixunzi://usage-guide` | Kullanım kılavuzu |
| `ixunzi://widget-guide` | Widget kılavuzu |
| `ixunzi://shortcuts-guide` | Kısayol kılavuzu |
| `ixunzi://feature-guide` | Tanıtımı yeniden oynat |
| `ixunzi://feedback` | Geri bildirim e-postası |
| `ixunzi://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
ixunzi://daily
ixunzi://passage?id=1
ixunzi://ask
ixunzi://study
ixunzi://hunt
```



