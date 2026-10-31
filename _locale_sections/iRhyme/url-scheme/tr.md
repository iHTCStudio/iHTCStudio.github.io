iRhyme ** `irhyme://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
irhyme://{host}?{params}
```


## Geçişler ve yazarlar

| URL | Açar |
|-----|-------|
| `irhyme://passage?id={id}` | Pasaj ayrıntısı |
| `irhyme://saying?id={id}` / `irhyme://couplet?id={id}` / `irhyme://poem?id={id}` | Aynı geçiş (compatability) |
| `irhyme://passage?id={id}&card=1` | Pasaj detay ve kart sayfası |
| `irhyme://card?id={id}` / `irhyme://share-card?id={id}` | Rhyme kartları |
| `irhyme://author?id={id}` | Yazar ayrıntısı |
| `irhyme://recite` / `irhyme://recite?id={id}` | Okuma akışı |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `irhyme://home` | Ana sayfa |
| `irhyme://daily` | Bugünün Rhyme |
| `irhyme://random` | Rastgele pasaj |
| `irhyme://favorites` | Favoriler |
| `irhyme://famous` | Ünlü dizeler |
| `irhyme://search` / `irhyme://search?q={query}` | Ara |
| `irhyme://study` / `irhyme://study?id={id}` | Rhyme Akademi |
| `irhyme://hunt` | Rhyme Hunt ('keyword-hunt' / 'flyflower') |
| `irhyme://handwriting` | Hand writing search ('handwrite'; iOS) |
| `irhyme://mastered` | Mastered ('progress') |
| `irhyme://categories` / `irhyme://categories?section=` | Gözat |
| `irhyme://collection?id=` | Collection / book ('shenglv' / "liweng" / "qianjia" / "youxue") |
| `irhyme://corpus` | Bütün geçitler ('all') |
| `irhyme://last-read` | Son okunan |
| `irhyme://reading-history` | Okuma geçmişi |
| `irhyme://notes` | Notlar |
| `irhyme://pair` | Paralellik uygulamaları |
| `irhyme://prosody` | Prosody desk |
| `irhyme://rhyme?id=dong` | Bir rhyme sınıfı |
| `irhyme://compare?rhyme=dong` | Aynı-rhyme Karşılaştırma |
| `irhyme://glossary?id=` | Parlak |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `irhyme://settings` | Ayarlar |
| `irhyme://usage-guide` | Kullanım kılavuzu |
| `irhyme://widget-guide` | Widget kılavuzu |
| `irhyme://shortcuts-guide` | Kısayol kılavuzu |
| `irhyme://feature-guide` | Tanıtımı yeniden oynat |
| `irhyme://feedback` | Geri bildirim e-postası |
| `irhyme://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
irhyme://daily
irhyme://passage?id=1001
irhyme://pair
irhyme://compare?rhyme=dong
irhyme://collection?id=shenglv
irhyme://study
irhyme://hunt
```


## Notlar

- Parametreler, kimliklerin sayısal olduğu durumlarda hassastır.
- Siri, Shortcuts, widgets ve Control Center kontrolleri aynı derin bağlantı yollarını kullanır.
- In-app **Settings → Yardım** en son liste için kılavuzlar.


