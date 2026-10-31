iCoder, ** `iLeetCoder://` ** (case-in sensitive) derin bağlantıları destekler - bir problem açın, günlük bir sınav, favoriler, yanlış kitap veya filtre: tag / şirket Safari, Shortcuts, widgets veya başka bir uygulama.

## Protokol Protokolü

| Host | Opens | Sorgu Sorgulama |
|------|-------|-------|
| `problem` | Problem detail | "Et=" veya "id=" (e.g. "1', "206") |
| `quiz` | Daily Quiz tab | — |
| `favorites` | Favourites list | — |
| `wrong`, `mistakes`, `wrongquestions` | Wrong book | "record=<UUUID>" → bağlantılı problem |
| `tag` | Problems filtered by tag | "isim=" |
| `company` | Problems filtered by company | "isim=" |

## Örnekler


```
iLeetCoder://problem?leetId=1
iLeetCoder://problem?id=206
iLeetCoder://quiz
iLeetCoder://tag?name=Array
iLeetCoder://company?name=Google
iLeetCoder://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## Home Screen Quick Actions

**4** in **Settings → Home Ekran kısayolları**: `iLeetCoder://` , `problem` , `leetId=` , `id=` , `1` , `quiz` Arama / kategoriler / geri bildirimler / inceleme Hızlı Eylem kanallarıdır.

[Genellikle] (.) · [FAQ](./faq) · [Privacy] (./privacy)


