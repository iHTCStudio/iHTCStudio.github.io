iGuanZhi ** `iguanzhi://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
iguanzhi://{host}?{params}
```


## Geçişler ve yazarlar

| URL | Açar |
|-----|-------|
| `iguanzhi://passage?id={id}` | Pasaj ayrıntısı |
| `iguanzhi://saying?id={id}` / `iguanzhi://couplet?id={id}` / `iguanzhi://poem?id={id}` | Aynı geçiş (compatability) |
| `iguanzhi://passage?id={id}&card=1` | Pasaj detay ve kart sayfası |
| `iguanzhi://card?id={id}` / `iguanzhi://share-card?id={id}` | kartları |
| `iguanzhi://author?id={id}` | Yazar ayrıntısı |
| `iguanzhi://recite` / `iguanzhi://recite?id={id}` | Okuma akışı |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `iguanzhi://home` | Ana sayfa |
| `iguanzhi://daily` | Bugün Deneme |
| `iguanzhi://random` | Rastgele pasaj |
| `iguanzhi://favorites` | Favoriler |
| `iguanzhi://famous` | Ünlü dizeler |
| `iguanzhi://search` / `iguanzhi://search?q={query}` | Ara |
| `iguanzhi://study` / `iguanzhi://study?id={id}` | Classics Study |
| `iguanzhi://hunt` | Essay Hunt ('keyword-hunt' / 'flyflower') |
| `iguanzhi://handwriting` | Hand writing search ('handwrite'; iOS) |
| `iguanzhi://mastered` | Mastered ('progress') |
| `iguanzhi://categories` / `iguanzhi://categories?section=` | Gözat |
| `iguanzhi://collection?id=` | Koleksiyon / kitap |
| `iguanzhi://corpus` | Bütün geçitler ('all') |
| `iguanzhi://last-read` | Son okunan |
| `iguanzhi://reading-history` | Okuma geçmişi |
| `iguanzhi://notes` | Notlar |
| `iguanzhi://fables` / `iguanzhi://allegories` / `iguanzhi://concepts` | Mevcut özel raflar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `iguanzhi://settings` | Ayarlar |
| `iguanzhi://usage-guide` | Kullanım kılavuzu |
| `iguanzhi://widget-guide` | Widget kılavuzu |
| `iguanzhi://shortcuts-guide` | Kısayol kılavuzu |
| `iguanzhi://feature-guide` | Tanıtımı yeniden oynat |
| `iguanzhi://feedback` | Geri bildirim e-postası |
| `iguanzhi://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
iguanzhi://daily
iguanzhi://passage?id=1
iguanzhi://study
iguanzhi://hunt
```



