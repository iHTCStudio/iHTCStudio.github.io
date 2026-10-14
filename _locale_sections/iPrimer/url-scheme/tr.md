iPrimer ** `iprimer://` ** kısayol bağlantıları (URL planı). Soğuk başlangıç ve Ev Ekran kısayolları birleşik bir tampon aracılığıyla teslim edilir, bu yüzden bağlantılar gemiden sonra iki kez açılmaz.

## Bağlantı biçimi


```
iprimer://{host}?{params}
```


## Bölümler & Yazarlar

| URL | Açar |
|-----|-------|
| `iprimer://chapter?id={id}` | Bölüm detayı |
| `iprimer://passage?id={id}` / `iprimer://poem?id={id}` | Bölüm (compatability) |
| `iprimer://author?id={id}` | Yazar ayrıntısı |
| `iprimer://recite` / `iprimer://recite?id={id}` | Okuma akışı |

## Keşfet

| URL | Açar |
|-----|-------|
| `iprimer://home` | Ana sayfa |
| `iprimer://daily` | Bugünün Günlük Çalışması |
| `iprimer://random` | Random Bölüm |
| `iprimer://favorites` | Favoriler |
| `iprimer://famous` | Ünlü dizeler |
| `iprimer://search` / `iprimer://search?q={query}` | Ara |
| `iprimer://study` | Karakter Çalışması |
| `iprimer://meditation` | Meditasyon kursu listesi |
| `iprimer://meditation?slug={slug}&autostart=1` | Açık oturum ve otomatik başlangıç (foreground) |
| `iprimer://guidance` | Hayat Rehberliği ( muhabir ve alışkanlıklar) |
| `iprimer://hunt` | Hunt (fly); alias "keyword-hunt" / "flyflower" |
| `iprimer://mastered` | Mastered bölümler |
| `iprimer://categories` / `iprimer://categories?section=` | Gözat |
| `iprimer://collection?id=xiaoxue` | Xiaoxue koleksiyonu (isim=' aynı zamanda desteklenen) |
| `iprimer://theme?id=lijiao` | Volume / tema (isim=立教' veya "Relationships" desteklenmektedir) |
| `iprimer://last-read` | Son okunan |
| `iprimer://reading-history` | Okuma geçmişi |
| `iprimer://notes` | Notlar |

## Ayarlar ve kılavuzlar

| URL | Açar |
|-----|-------|
| `iprimer://settings` | Ayarlar |
| `iprimer://usage-guide` | Kullanım kılavuzu |
| `iprimer://widget-guide` | Widget kılavuzu |
| `iprimer://shortcuts-guide` | Kısayol kılavuzu |
| `iprimer://feature-guide` | Tanıtımı yeniden oynat |
| `iprimer://feedback` | Geri bildirim e-postası |
| `iprimer://in-app-review` | Uygulama içi / App Store değerlendirme |

## Örnekler


```
iprimer://daily
iprimer://chapter?id=3
iprimer://collection?id=xiaoxue
iprimer://theme?id=lijiao
iprimer://study
iprimer://meditation?slug=emotion_calm&autostart=1
iprimer://guidance
iprimer://hunt
```


Bunları kısa kesimlerde kullanın, Home Ekran hızlı eylemleri, widgets veya Safari. Mevcut olduğunda istikrarlı `iprimer://` parametreleri tercih edin. Ayrıca bakınız **Settings → Kısayollar Kılavuzu**.


