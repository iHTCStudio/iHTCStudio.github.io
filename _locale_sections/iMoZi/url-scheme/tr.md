iMoZi, ** `imozi://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
imozi://{host}?{params}
```


## Geçişler ve yazarlar

| URL | Açar |
|-----|-------|
| `imozi://passage?id={id}` | Pasaj ayrıntısı |
| `imozi://saying?id={id}` / `imozi://couplet?id={id}` / `imozi://poem?id={id}` | Aynı geçiş (compatability) |
| `imozi://passage?id={id}&card=1` | Pasaj detay ve kart sayfası |
| `imozi://card?id={id}` / `imozi://share-card?id={id}` | kartları |
| `imozi://author?id={id}` | Yazar ayrıntısı |
| `imozi://recite` / `imozi://recite?id={id}` | Okuma akışı |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `imozi://home` | Ana sayfa |
| `imozi://daily` | Bugünün Moları |
| `imozi://random` | Rastgele pasaj |
| `imozi://favorites` | Favoriler |
| `imozi://famous` | Ünlü dizeler |
| `imozi://search` / `imozi://search?q={query}` | Ara |
| `imozi://study` / `imozi://study?id={id}` | Mohizm Çalışması |
| `imozi://hunt` | Sentence Hunt ('keyword-hunt' / 'flyflower') |
| `imozi://handwriting` | Hand writing search ('handwrite'; iOS) |
| `imozi://mastered` | Mastered ('progress') |
| `imozi://categories` / `imozi://categories?section=` | Gözat |
| `imozi://collection?id=` | Koleksiyon / kitap |
| `imozi://corpus` | Bütün geçitler ('all') |
| `imozi://last-read` | Son okunan |
| `imozi://reading-history` | Okuma geçmişi |
| `imozi://notes` | Notlar |
| `imozi://ask` | Mozi |
| `imozi://fables` / `imozi://allegories` / `imozi://concepts` | Mevcut özel raflar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `imozi://settings` | Ayarlar |
| `imozi://usage-guide` | Kullanım kılavuzu |
| `imozi://widget-guide` | Widget kılavuzu |
| `imozi://shortcuts-guide` | Kısayol kılavuzu |
| `imozi://feature-guide` | Tanıtımı yeniden oynat |
| `imozi://feedback` | Geri bildirim e-postası |
| `imozi://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
imozi://daily
imozi://passage?id=1
imozi://ask
imozi://study
imozi://hunt
```



