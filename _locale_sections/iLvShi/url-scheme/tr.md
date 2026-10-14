iLvShi, ** `ilvshi://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
ilvshi://{host}?{params}
```


## Geçişler ve yazarlar

| URL | Açar |
|-----|-------|
| `ilvshi://passage?id={id}` | Pasaj ayrıntısı |
| `ilvshi://saying?id={id}` / `ilvshi://couplet?id={id}` / `ilvshi://poem?id={id}` | Aynı geçiş (compatability) |
| `ilvshi://passage?id={id}&card=1` | Pasaj detay ve kart sayfası |
| `ilvshi://card?id={id}` / `ilvshi://share-card?id={id}` | kartları |
| `ilvshi://author?id={id}` | Yazar ayrıntısı |
| `ilvshi://recite` / `ilvshi://recite?id={id}` | Okuma akışı |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `ilvshi://home` | Ana sayfa |
| `ilvshi://daily` | Günlük Geçiş |
| `ilvshi://random` | Rastgele pasaj |
| `ilvshi://favorites` | Favoriler |
| `ilvshi://famous` | Ünlü dizeler |
| `ilvshi://search` / `ilvshi://search?q={query}` | Ara |
| `ilvshi://study` / `ilvshi://study?id={id}` | Spring-Autumn Study |
| `ilvshi://hunt` | Sonbahar Av ('keyword-hunt' / 'flyflower') |
| `ilvshi://handwriting` | Hand writing search ('handwrite'; iOS) |
| `ilvshi://mastered` | Mastered ('progress') |
| `ilvshi://categories` / `ilvshi://categories?section=` | Gözat |
| `ilvshi://collection?id=` | Koleksiyon / kitap |
| `ilvshi://corpus` | Bütün geçitler ('all') |
| `ilvshi://last-read` | Son okunan |
| `ilvshi://reading-history` | Okuma geçmişi |
| `ilvshi://notes` | Notlar |
| `ilvshi://fables` / `ilvshi://allegories` / `ilvshi://concepts` | Mevcut özel raflar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `ilvshi://settings` | Ayarlar |
| `ilvshi://usage-guide` | Kullanım kılavuzu |
| `ilvshi://widget-guide` | Widget kılavuzu |
| `ilvshi://shortcuts-guide` | Kısayol kılavuzu |
| `ilvshi://feature-guide` | Tanıtımı yeniden oynat |
| `ilvshi://feedback` | Geri bildirim e-postası |
| `ilvshi://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
ilvshi://daily
ilvshi://passage?id=1
ilvshi://study
ilvshi://hunt
```



