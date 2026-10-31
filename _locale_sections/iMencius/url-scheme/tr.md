iMencius, ** `imencius://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
imencius://{host}?{params}
```


## Geçişler ve yazarlar

| URL | Açar |
|-----|-------|
| `imencius://passage?id={id}` | Pasaj ayrıntısı |
| `imencius://saying?id={id}` / `imencius://couplet?id={id}` / `imencius://poem?id={id}` | Aynı geçiş (compatability) |
| `imencius://passage?id={id}&card=1` | Pasaj detay ve kart sayfası |
| `imencius://card?id={id}` / `imencius://share-card?id={id}` | kartları |
| `imencius://author?id={id}` | Yazar ayrıntısı |
| `imencius://recite` / `imencius://recite?id={id}` | Okuma akışı |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `imencius://home` | Ana sayfa |
| `imencius://daily` | Daily Saying |
| `imencius://random` | Rastgele pasaj |
| `imencius://favorites` | Favoriler |
| `imencius://famous` | Ünlü dizeler |
| `imencius://search` / `imencius://search?q={query}` | Ara |
| `imencius://study` / `imencius://study?id={id}` | Nurturing Qi Study |
| `imencius://hunt` | Yi Hunt ('keyword-hunt' / 'flyflower') |
| `imencius://handwriting` | Hand writing search ('handwrite'; iOS) |
| `imencius://mastered` | Mastered ('progress') |
| `imencius://categories` / `imencius://categories?section=` | Gözat |
| `imencius://collection?id=` | Koleksiyon / kitap |
| `imencius://corpus` | Bütün geçitler ('all') |
| `imencius://last-read` | Son okunan |
| `imencius://reading-history` | Okuma geçmişi |
| `imencius://notes` | Notlar |
| `imencius://fables` / `imencius://allegories` / `imencius://concepts` | Mevcut özel raflar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `imencius://settings` | Ayarlar |
| `imencius://usage-guide` | Kullanım kılavuzu |
| `imencius://widget-guide` | Widget kılavuzu |
| `imencius://shortcuts-guide` | Kısayol kılavuzu |
| `imencius://feature-guide` | Tanıtımı yeniden oynat |
| `imencius://feedback` | Geri bildirim e-postası |
| `imencius://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
imencius://daily
imencius://passage?id=1
imencius://study
imencius://hunt
```



