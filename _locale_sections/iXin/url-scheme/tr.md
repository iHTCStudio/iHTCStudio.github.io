iXin, ** `ixin://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
ixin://{host}?{params}
```


## Geçişler ve yazarlar

| URL | Açar |
|-----|-------|
| `ixin://passage?id={id}` | Pasaj ayrıntısı |
| `ixin://saying?id={id}` / `ixin://couplet?id={id}` / `ixin://poem?id={id}` | Aynı geçiş (compatability) |
| `ixin://passage?id={id}&card=1` | Pasaj detay ve kart sayfası |
| `ixin://card?id={id}` / `ixin://share-card?id={id}` | İçgörü kartları |
| `ixin://author?id={id}` | Yazar ayrıntısı |
| `ixin://recite` / `ixin://recite?id={id}` | Okuma akışı |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `ixin://home` | Ana sayfa |
| `ixin://daily` | Günlük Bilgi |
| `ixin://random` | Rastgele pasaj |
| `ixin://favorites` | Favoriler |
| `ixin://famous` | Ünlü dizeler |
| `ixin://search` / `ixin://search?q={query}` | Ara |
| `ixin://study` / `ixin://study?id={id}` | Kalp Okulu |
| `ixin://hunt` | Heart Hunt ('keyword-hunt' / 'flyflower') |
| `ixin://handwriting` | Hand writing search ('handwrite'; iOS) |
| `ixin://mastered` | Mastered ('progress') |
| `ixin://categories` / `ixin://categories?section=` | Gözat |
| `ixin://collection?id=` | Koleksiyon / kitap ('chuanxilu' / "daxuewen' / "jiaotiao" / "yilvwen" / şiirler) |
| `ixin://corpus` | Bütün geçitler ('all') |
| `ixin://last-read` | Son okunan |
| `ixin://reading-history` | Okuma geçmişi |
| `ixin://notes` | Notlar |
| `ixin://journal` | Know-Acting |
| `ixin://liangzhi` | Liangzhi'nın Üç Soru |
| `ixin://graph` | Kavram grafiği |
| `ixin://timeline` | Annals / zaman çizelgesi |
| `ixin://map` | Map Map Map Map Map Map |
| `ixin://people` | İnsanlar |
| `ixin://achievements` | Başarılar Başarılar |
| `ixin://theme?id=` | Tema |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `ixin://settings` | Ayarlar |
| `ixin://usage-guide` | Kullanım kılavuzu |
| `ixin://widget-guide` | Widget kılavuzu |
| `ixin://shortcuts-guide` | Kısayol kılavuzu |
| `ixin://feature-guide` | Tanıtımı yeniden oynat |
| `ixin://feedback` | Geri bildirim e-postası |
| `ixin://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
ixin://daily
ixin://passage?id=1
ixin://journal
ixin://liangzhi
ixin://collection?id=chuanxilu
ixin://study
ixin://hunt
```


## Notlar

- Parametreler, kimliklerin sayısal olduğu durumlarda hassastır.
- Siri, Shortcuts, widgets ve Control Center kontrolleri aynı derin bağlantı yollarını kullanır.
- In-app **Settings → Yardım** en son liste için kılavuzlar.


