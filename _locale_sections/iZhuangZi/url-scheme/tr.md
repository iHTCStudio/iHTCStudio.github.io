iZhuangZi, ** `izhuangzi://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
izhuangzi://{host}?{params}
```


## Geçişler ve yazarlar

| URL | Açar |
|-----|-------|
| `izhuangzi://passage?id={id}` | Pasaj ayrıntısı |
| `izhuangzi://saying?id={id}` / `izhuangzi://couplet?id={id}` / `izhuangzi://poem?id={id}` | Aynı geçiş (compatability) |
| `izhuangzi://passage?id={id}&card=1` | Pasaj detay ve kart sayfası |
| `izhuangzi://card?id={id}` / `izhuangzi://share-card?id={id}` | kartları |
| `izhuangzi://author?id={id}` | Yazar ayrıntısı |
| `izhuangzi://recite` / `izhuangzi://recite?id={id}` | Okuma akışı |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `izhuangzi://home` | Ana sayfa |
| `izhuangzi://daily` | Daily Zhuangzi |
| `izhuangzi://random` | Rastgele pasaj |
| `izhuangzi://favorites` | Favoriler |
| `izhuangzi://famous` | Ünlü dizeler |
| `izhuangzi://search` / `izhuangzi://search?q={query}` | Ara |
| `izhuangzi://study` / `izhuangzi://study?id={id}` | Dao Study |
| `izhuangzi://hunt` | Zhuang Hunt ('keyword-hunt' / 'flyflower') |
| `izhuangzi://handwriting` | Hand writing search ('handwrite'; iOS) |
| `izhuangzi://mastered` | Mastered ('progress') |
| `izhuangzi://categories` / `izhuangzi://categories?section=` | Gözat |
| `izhuangzi://collection?id=` | Collection / book ('neipian' / "waipian' / "zapian") |
| `izhuangzi://corpus` | Bütün geçitler ('all') |
| `izhuangzi://last-read` | Son okunan |
| `izhuangzi://reading-history` | Okuma geçmişi |
| `izhuangzi://notes` | Notlar |
| `izhuangzi://ask` | Zhuangzi |
| `izhuangzi://allegories` | Parables |
| `izhuangzi://concepts` | Kavramlar |
| `izhuangzi://theme?id=neipian` | İç / Dış / Miscellane |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `izhuangzi://settings` | Ayarlar |
| `izhuangzi://usage-guide` | Kullanım kılavuzu |
| `izhuangzi://widget-guide` | Widget kılavuzu |
| `izhuangzi://shortcuts-guide` | Kısayol kılavuzu |
| `izhuangzi://feature-guide` | Tanıtımı yeniden oynat |
| `izhuangzi://feedback` | Geri bildirim e-postası |
| `izhuangzi://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
izhuangzi://daily
izhuangzi://passage?id=1
izhuangzi://ask
izhuangzi://allegories
izhuangzi://collection?id=neipian
izhuangzi://study
izhuangzi://hunt
```


## Notlar

- Parametreler, kimliklerin sayısal olduğu durumlarda hassastır.
- Siri, Shortcuts, widgets ve Control Center kontrolleri aynı derin bağlantı yollarını kullanır.
- In-app **Settings → Yardım** en son liste için kılavuzlar.


