iWuBi, ** `iWuBi://` ** (case-in sensitive program `iwubi` ) derin bağlantılar - açık göz atın, günlük test, favoriler, yanlış kitap, kod uzunluğu seviyeleri, Safari, kısa kesimler, widgets veya başka bir uygulamadan hub veya yazma.

## Protokol Protokolü


```
iWuBi://<host>[?query]
iWuBi:///path-style   ← host empty; first path segment is the action
```


| Host / action | Opens | Sorgu Sorgulama |
|---------------|-------|-------|
| `search` | Lookup tab, focus search | "q", "word" ya da "isim" öncesi |
| `word`, `char`, `character` | Word detail (or search if query empty) | "q" / "word" / "name" = karakter |
| `quiz`, `test` | Learn → Daily Quiz | — |
| `favorites`, `favorite` | Settings → Favourites | — |
| `wrong`, `mistakes`, `wrongbook` | Wrong book | "record=<UUID>" → bir rekor |
| `levels`, `level`, `codes` | Levels tab | — |
| `learn`, `study` | Learn tab | — |
| `typing`, `type`, `practice` | Typing tab | — |

## Örnekler


```
iWuBi://search?q=你好
iWuBi://word?q=好
iWuBi://quiz
iWuBi://wrong?record=550E8400-E29B-41D4-A716-446655440000
iWuBi://levels
iWuBi://typing
```


## Home Screen Quick Actions

**4** in **Settings → Home Ekran kısayolları**: `iWuBi://` , `iwubi` , `q` , `word` , `name` , `word` . **Feedback** ve **

[Genellikle] (.) · [FAQ](./faq) · [Privacy] (./privacy)


