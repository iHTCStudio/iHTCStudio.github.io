İngilizce, ** `ienglish://` ** URL planı derin bağlantıları - bir kelime açın, Daily Quiz, Favourites, yanlış Book, listeler veya Safari, Shortcuts, widgets veya başka bir uygulama.

**Home Ekran Hızlı Eylemler ** (Uygulama ikonunu bastırın) Arama, Geri bildirim ve Puan ekleyin - bu tipler ** değil ** `ienglish://` tarafından yorumlanır, ancak hala uygulamayı kısayol gözlemci aracılığıyla açın.

> **Not:** Linkler sadece **navigate** uygulama içinde. Uzaktan olarak telaffuz etmeye veya araştırma ayarlarını değiştirmeye başlamazlar.

## Protokol Protokolü


```
ienglish://<host>[?query]
```


| Rule | Detaylı Bilgi |
|------|--------|
| **Scheme** | "Sürekli" (sağlıklı) |
| **Word detail** | Host "word" - query **'id=<wordID>'** (gereksiz, boş olmayan) |
| **Quiz** | Host "quiz" |
| **Favourites** | Host "favorites" |
| **Wrong book** | Host "wrong" veya "mistakes" - Seçmeli "record=<UUID>" bir hata açar |
| **Playlist** | Host "playlist" |
| **Categories** | Host "categories" |

## Örnekler


```
ienglish://word?id=apple
ienglish://quiz
ienglish://favorites
ienglish://wrong
ienglish://wrong?record=550E8400-E29B-41D4-A716-446655440000
ienglish://playlist
ienglish://categories
```


## Home Screen Quick Actions

**4 **'e kadar yapılandırın **Settings → Home Ekran kısayolları**. Türler `ienglish://` , `IEnglishDeepLink` , `word` , `id=<wordID>` , `quiz` , `favorites` - Search / Feedback / Review sadece Quick Actions olarak teslim edilir.

## Widget derin bağlantılar

Widget aynı `ienglish://` ev sahipliği kullanır (e.g. Daily Quiz → `IEnglishDeepLink` , Favourites view → `ienglish` ).

[Genellikle] (.) · [FAQ](./faq) · [Privacy] (./privacy)


