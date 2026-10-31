iTer, ** `iTer://` ** URL programı **iPhone ve iPad** üzerinde destekler. Kısayollarda, Safari, widgets veya bir soru açmak için diğer uygulamalar, günlük sınav, favoriler veya yanlış cevap kitabı.

**Home Ekran Hızlı Eylemler ** (Uygulama ikonunu uzun baskı) aynı `iTer://` dizeleri tekrarlayın. **4 **'ye kadar seçin **7** seçeneklerinden **Sings → Ev Ekran kısayolları**.

> **Not: ** Deep Links **navigate** in the app. Test ayarlarını değiştirmiyor veya uzaktan soru işaret ediyor. **Mac**, Home Ekran Hızlı Eylemleri kaydetmez; widgets ve in-app navigation hala Mac üzerinde çalışır.

## Protokol Protokolü


```
iTer://<host>[?query]
```


| Rule | Detaylı Bilgi |
|------|--------|
| **Scheme** | "iTer" (case-in sensitive) |
| **Question detail** | Host "question" - query **'id=<questionID>' ** veya **'q=<questionID>'** (required) |
| **Daily Quiz** | Host "quiz" |
| **Favourites** | Host ‘favorites’ → Ayarlar |
| **Wrong book** | Host "wrong", "mistakes", ya da "wrongquestions" - Seçmeli **'record =<UID>"** bir hata açar |
| **Search** | Host "search" - Quick Action / kısayol sadece (yalnızca küresel arama sekmesini açın) |
| **Categories** | Host "categories" - Quick Action / kısayol sadece (opens Kategoriler sekme) |
| **Feedback** | Host "Liveback" – Quick Action sadece (mail oluşturma veya "mailto:' fallback) |
| **Rate app** | Host "Rekre" - Quick Action sadece (oyunKit in-app review). “star” da içeren Legacy türleri. |

Ev sahibi boş ve yol segment maçlarında `iTer://` gibi yollar kabul edilir.

## Örnekler


```
iTer://question?id=94c34bb2bdef11e6a0e100163e0021c8
iTer://quiz
iTer://favorites
iTer://wrong
iTer://wrong?record=550E8400-E29B-41D4-A716-446655440000
```


## Home Screen Quick Actions

| Type | Tipik kullanım kullanımı |
|------|-------------|
| `iTer://search` | Global arama |
| `iTer://quiz` | Daily Quiz sekmesi |
| `iTer://favorites` | Favourites listesi |
| `iTer://wrong` | Yanlış cevap kitabı |
| `iTer://categories` | Kategoriler sekmesi |
| `iTer://feedback` | Geri bildirimler gönder |
| `iTer://review` | Uygulamayı paylaşın ( MağazaKit) |

Varsayılan seçim: Arama, Quiz, Favourites, Feedback. Reorder veya **Settings → Home Ekran kısayolları** (max 4). Uygulama maçları, ** ile kısayollar ile kısayollar **, bu yolları hala doğru rotayı içeren bu tür değişiklikler.

## Widget derin bağlantılar

| Widget | Tipik URL URL URL |
|--------|-------------|
| Daily Question | "iTer http://question?id=" |
| Quiz Glance | "iTer httpquiz" |
| Favourites Glance | "iTer https://favorites" |
| Wrong Book Glance | "iTer httpwrong" veya "iTer http://wrong?record=<UID>" |

---

[Geride iTer Support](./) · [FAQ](./faq) · [Privacy Policy](./privacy)


