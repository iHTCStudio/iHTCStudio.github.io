iHanFei, ** `ihanfei://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
ihanfei://{host}?{params}
```


## Geçişler ve yazarlar

| URL | Açar |
|-----|-------|
| `ihanfei://passage?id={id}` | Pasaj ayrıntısı |
| `ihanfei://saying?id={id}` / `ihanfei://couplet?id={id}` / `ihanfei://poem?id={id}` | Aynı geçiş (compatability) |
| `ihanfei://passage?id={id}&card=1` | Pasaj detay ve kart sayfası |
| `ihanfei://card?id={id}` / `ihanfei://share-card?id={id}` | kartları |
| `ihanfei://author?id={id}` | Yazar ayrıntısı |
| `ihanfei://recite` / `ihanfei://recite?id={id}` | Okuma akışı |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `ihanfei://home` | Ana sayfa |
| `ihanfei://daily` | Daily Stratagem |
| `ihanfei://random` | Rastgele pasaj |
| `ihanfei://favorites` | Favoriler |
| `ihanfei://famous` | Ünlü dizeler |
| `ihanfei://search` / `ihanfei://search?q={query}` | Ara |
| `ihanfei://study` / `ihanfei://study?id={id}` | Yasallık Çalışması |
| `ihanfei://hunt` | Law Hunt ('keyword-hunt' / 'flyflower') |
| `ihanfei://handwriting` | Hand writing search ('handwrite'; iOS) |
| `ihanfei://mastered` | Mastered ('progress') |
| `ihanfei://categories` / `ihanfei://categories?section=` | Gözat |
| `ihanfei://collection?id=` | Koleksiyon / kitap |
| `ihanfei://corpus` | Bütün geçitler ('all') |
| `ihanfei://last-read` | Son okunan |
| `ihanfei://reading-history` | Okuma geçmişi |
| `ihanfei://notes` | Notlar |
| `ihanfei://fables` / `ihanfei://allegories` / `ihanfei://concepts` | Mevcut özel raflar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `ihanfei://settings` | Ayarlar |
| `ihanfei://usage-guide` | Kullanım kılavuzu |
| `ihanfei://widget-guide` | Widget kılavuzu |
| `ihanfei://shortcuts-guide` | Kısayol kılavuzu |
| `ihanfei://feature-guide` | Tanıtımı yeniden oynat |
| `ihanfei://feedback` | Geri bildirim e-postası |
| `ihanfei://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
ihanfei://daily
ihanfei://passage?id=1
ihanfei://study
ihanfei://hunt
```



