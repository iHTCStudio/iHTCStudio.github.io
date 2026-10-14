IPrecepts ** `iprecepts://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
iprecepts://{host}?{params}
```


## Geçişler ve yazarlar

| URL | Açar |
|-----|-------|
| `iprecepts://passage?id={id}` | Pasaj ayrıntısı |
| `iprecepts://saying?id={id}` / `iprecepts://couplet?id={id}` / `iprecepts://poem?id={id}` | Aynı geçiş (compatability) |
| `iprecepts://passage?id={id}&card=1` | Pasaj detay ve kart sayfası |
| `iprecepts://card?id={id}` / `iprecepts://share-card?id={id}` | Precept kartları |
| `iprecepts://author?id={id}` | Yazar ayrıntısı |
| `iprecepts://recite` / `iprecepts://recite?id={id}` | Okuma akışı |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `iprecepts://home` | Ana sayfa |
| `iprecepts://daily` | Daily Precept |
| `iprecepts://random` | Rastgele pasaj |
| `iprecepts://favorites` | Favoriler |
| `iprecepts://famous` | Ünlü dizeler |
| `iprecepts://search` / `iprecepts://search?q={query}` | Ara |
| `iprecepts://study` / `iprecepts://study?id={id}` | Aile Çalışması |
| `iprecepts://hunt` | Precept Hunt ('keyword-hunt' / "flyflower") |
| `iprecepts://handwriting` | Hand writing search ('handwrite'; iOS) |
| `iprecepts://mastered` | Mastered ('progress') |
| `iprecepts://categories` / `iprecepts://categories?section=` | Gözat |
| `iprecepts://collection?id=` | Koleksiyon / kitap (zhuxi / zhubailu / yanshi / zhuge / zeng / yuanshi / qian / tingxun / kısa çalışmalar) |
| `iprecepts://corpus` | Bütün geçitler ('all') |
| `iprecepts://last-read` | Son okunan |
| `iprecepts://reading-history` | Okuma geçmişi |
| `iprecepts://notes` | Notlar |
| `iprecepts://compare` | Paralel karşılaştırma |
| `iprecepts://theme?id=` | Tema |
| `iprecepts://authors` | Yazarlar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `iprecepts://settings` | Ayarlar |
| `iprecepts://usage-guide` | Kullanım kılavuzu |
| `iprecepts://widget-guide` | Widget kılavuzu |
| `iprecepts://shortcuts-guide` | Kısayol kılavuzu |
| `iprecepts://feature-guide` | Tanıtımı yeniden oynat |
| `iprecepts://feedback` | Geri bildirim e-postası |
| `iprecepts://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
iprecepts://daily
iprecepts://passage?id=1
iprecepts://passage?id=1&card=1
iprecepts://compare
iprecepts://collection?id=yanshi
iprecepts://study
iprecepts://hunt
```


## Notlar

- Parametreler, kimliklerin sayısal olduğu durumlarda hassastır.
- Siri, Shortcuts, widgets ve Control Center kontrolleri aynı derin bağlantı yollarını kullanır.
- In-app **Settings → Yardım** en son liste için kılavuzlar.


