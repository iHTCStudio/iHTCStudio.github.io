IMüzik ** `imusic://` ** kısayollarını destekler. Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon üzerinden geçer, böylece bir bağlantı dolaptan sonra iki kez açılmaz.

## Bağlantı biçimi


```
imusic://{host}?{params}
```


Scheme ** `imusic://` ** sadece.

## Ev & Bugün

| URL | Açar |
|-----|-------|
| `imusic://` / `imusic://home` | Ana sayfa |
| `imusic://daily` / `imusic://today` | Daily Piece (queue sadece bu yolda) |
| `imusic://random` | Roam (ve-library shuffle) |
| `imusic://play` | Play Play Play |
| `imusic://last` / `imusic://lastheard` | Son duydum |

## Takımlar & sanatçılar

| URL | Açar |
|-----|-------|
| `imusic://piece?id={id}` | Parça kılavuzu ('passage' / 'song' da kabul edildi) |
| `imusic://artist?id={id}` / `imusic://artist?name={name}` | Sanatçı |
| `imusic://artists` / `imusic://singers` | Sanatçı |
| `imusic://famous` / `imusic://lines` | Ünlü dizeler |

Bir pay kartı ayağı, insanlar için `imusic://` (title · sanatçı) ekleyebilir. Maç hala kullanır ** `imusic` sadece**.

## Göze, arama ve dinlemek

| URL | Açar |
|-----|-------|
| `imusic://categories` / `imusic://browse` | Gözyaş (bölüm =catalog' / "all" / "all parça" → All Pieces) |
| `imusic://collection?id={id}` | Koleksiyon ('id=col-all'ın hepsi Sanal Tüm Parçalar listesi) |
| `imusic://search` / `imusic://search?q={query}` | Ara |
| `imusic://favorites` | Favoriler |
| `imusic://later` | Favoriler, daha sonra kaydırıldı |
| `imusic://lists` / `imusic://listenlists` | Dinle listeleri |
| `imusic://history` | Tarih Tarihi |
| `imusic://notes` | Notlar |
| `imusic://mastered` | Bitmiş Bitti |
| `imusic://streak` / `imusic://footprint` | Streak |

Tek bir parça açın, mini bar veya Song ID **resets ** okuma kuyruğunu bu parçaya döndürür. Bir koleksiyondan başlayarak, arama veya sanatçı bu listeyi tutar, böylece Next / Previous kullanılabilir.

## Song ID, school & mood

| URL | Açar |
|-----|-------|
| `imusic://recognize` / `imusic://shazam` | Song ID ID |
| `imusic://school` / `imusic://earschool` | Ear school |
| `imusic://timeline` / `imusic://corridor` | Era koridor |
| `imusic://compare` | Dinle |
| `imusic://mood?id={id}` | O ruh haliye başlayın (bölüm=' / "partId=" sadece başlangıç pistidir; ruh hala "id') |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `imusic://settings` | Ayarlar |
| `imusic://usageguide` / `imusic://featureguide` | Kullanım / özellik kılavuzu |
| `imusic://widgetguide` | Widget kılavuzu |
| `imusic://shortcutsguide` | Kısayol kılavuzu |
| `imusic://feedback` | Geri bildirim |
| `imusic://review` / `imusic://in-app-review` | In-app review ( Mağaza listesi canlı olduğunda) |

## Siri & Home Ekran

Siri'ye bugün parça için sorun, roam, arama, ya da kısayollar ekledikten sonra favoriler. Configure Home Ekran **Settings → Kısakesler**. Tam örnekler in-app Shortcuts kılavuzunda yaşarlar.

[FAQ](./faq) · [Privacy Policy](./privacy)


