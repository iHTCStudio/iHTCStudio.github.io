ISage, ** `isage://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
isage://{host}?{params}
```


## Sayings & Yazarlar

| URL | Açar |
|-----|-------|
| `isage://passage?id={id}` | De ki: |
| `isage://saying?id={id}` / `isage://couplet?id={id}` / `isage://poem?id={id}` | Aynı geçiş (compatability) |
| `isage://passage?id={id}&card=1` | Detaylı ve sage-kart sayfası |
| `isage://card?id={id}` / `isage://share-card?id={id}` | Sage kartı |
| `isage://author?id={id}` | Yazar ayrıntısı |
| `isage://recite` / `isage://recite?id={id}` | Okuma akışı |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `isage://home` | Ana sayfa |
| `isage://daily` | Bugünün Bilgeliği |
| `isage://random` | Random diyor |
| `isage://favorites` | Favoriler |
| `isage://famous` | Ünlü dizeler |
| `isage://search` / `isage://search?q={query}` | Ara |
| `isage://study` / `isage://study?id={id}` | Sage Academy |
| `isage://hunt` | Sage Hunt ('keyword-hunt' / 'flyflower') |
| `isage://handwriting` | Hand writing search ('handwrite'; iOS) |
| `isage://mastered` | Mastered ('progress') |
| `isage://categories` / `isage://categories?section=` | Gözat |
| `isage://collection?id=guxun` | Klasik reension ('zhou-shang' / "zhou-xia"; Ayrıca "book' / "form") |
| `isage://corpus` | Bütün sözler ('all') |
| `isage://theme?id=conduct` | Tema (e.g. "cultivation", "öğrenme", "arkadaşlık", "evhold", "wealth", "virtue", "fortune", "speech", " |
| `isage://last-read` | Son okunan |
| `isage://reading-history` | Okuma geçmişi |
| `isage://notes` | Notlar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `isage://settings` | Ayarlar |
| `isage://usage-guide` | Kullanım kılavuzu |
| `isage://widget-guide` | Widget kılavuzu |
| `isage://shortcuts-guide` | Kısayol kılavuzu |
| `isage://feature-guide` | Tanıtımı yeniden oynat |
| `isage://feedback` | Geri bildirim e-postası |
| `isage://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
isage://daily
isage://passage?id=1
isage://passage?id=1&card=1
isage://collection?id=guxun
isage://theme?id=conduct
isage://study
isage://hunt
isage://handwriting
```


## Notlar

- Parametreler, kimliklerin sayısal olduğu durumlarda hassastır.
- Siri, Shortcuts, widgets ve Control Center kontrolleri aynı derin bağlantı yollarını kullanır.
- In-app **Settings → Yardım** en son liste için kılavuzlar.


