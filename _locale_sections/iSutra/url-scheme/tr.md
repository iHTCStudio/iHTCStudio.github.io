iSutra, ** `isutra://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
isutra://{host}?{params}
```


## Sutras & Yazarlar

| URL | Açar |
|-----|-------|
| `isutra://passage?id={id}` | Sutra detayı |
| `isutra://couplet?id={id}` / `isutra://poem?id={id}` | Aynı geçiş (compatability) |
| `isutra://author?id={id}` | Translator / yazar detay |
| `isutra://recite` / `isutra://recite?id={id}` | Okuma akışı |
| `isutra://large?id=diamond` / `isutra://large?id=dizang` | Büyük Kitap Kataloğu |

## Discovery & practice

| URL | Açar |
|-----|-------|
| `isutra://home` | Ana sayfa |
| `isutra://daily` | Bugünün Günlük Sutra |
| `isutra://random` | Rastgele pasaj |
| `isutra://favorites` | Favoriler |
| `isutra://famous` | Ünlü dizeler |
| `isutra://search` / `isutra://search?q={query}` | Ara |
| `isutra://study` | Çalışma Salonu |
| `isutra://hunt` | Hunt (fly); alias "keyword-hunt" / "flyflower" |
| `isutra://count` | Balık avant ('chant' / "muyu' / "karşılık") |
| `isutra://copy` / `isutra://copy?id={id}` | Copy-sutra (iOS) |
| `isutra://practice` | Sabah / akşam pratik |
| `isutra://mastered` | Mastered |
| `isutra://categories` / `isutra://categories?section=` | Gözat |
| `isutra://collection?id=` | Koleksiyon (e.g. "prajna", "forty-iki"; aynı zamanda "isim=") |
| `isutra://theme?id=` | Tema (e.g. "xingyuan", "yaoshi", " platform") |
| `isutra://last-read` | Son okunan |
| `isutra://reading-history` | Okuma geçmişi |
| `isutra://notes` | Notlar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `isutra://settings` | Ayarlar |
| `isutra://usage-guide` | Kullanım kılavuzu |
| `isutra://widget-guide` | Widget kılavuzu |
| `isutra://shortcuts-guide` | Kısayol kılavuzu |
| `isutra://feature-guide` | Tanıtımı yeniden oynat |
| `isutra://privacy` | In-app gizlilik |
| `isutra://feedback` | Geri bildirim e-postası |
| `isutra://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
isutra://daily
isutra://passage?id=1
isutra://large?id=diamond
isutra://count
isutra://copy?id=1
isutra://practice
isutra://collection?id=prajna
isutra://theme?id=xingyuan
isutra://study
isutra://hunt
```


Bunları kısa kesimlerde kullanın, Home Ekran hızlı eylemleri, widgets veya Safari. Ayrıca bakınız **Settings → Kısayollar Kılavuzu**.


