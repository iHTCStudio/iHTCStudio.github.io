iWidget, ** `iwidget://` ** URL programı **iPhone, iPad ve Mac** üzerinde destekler. Bunu **Safari**, ** Apple Shortcuts**, başka bir uygulama veya QR kodu ana uygulamaya atlamak için kullanın. Bu bağlantılar ** sadece** - widget tasarım kimlikleri veya düzenleme kurulu düzeni geçmiyorlar.

Konuşmak için Ay / festival cevapları ** Uygulamayı açmadan, kullanın **Siri App Shortcuts ** (see [FAQ] (./faq) → Siri). **Bir tarihteki iş/rest, ayrı **Workday ** Kısayollarda App Niyet.

## Format


```
iwidget://<host>[?query]
```


| Rule | Detaylı Bilgi |
|------|--------|
| **Scheme** | "iwidget" (düşük) |
| **Host** | Pat segmenti - aşağıdaki tabloyu görmek |
| **Query** | Seçmeli; sadece belgelenmiş anahtarlar okunur |

Bilinmeyen evler güvenli bir şekilde göz ardı edilir (öldürülemez).

---

## Hosts

| Host | Opens | Sorgu Sorgulama |
|------|--------|-------|
| `today` | **Today** tab | — |
| `day` | **Today** tab and queues **day detail** for the given date | **'y'** year · **'m'** ay · **'d' ** gün (entegers) |
| `settings` | **Settings** tab | **'scroll =festivals' ** Festival filtresi bölümüne kaydırıyor |

Eğer `iwidget://` sorgu değerleri eksik veya geçersiz ise, uygulama bugün bir gün sayfası açmadan hala anahtarlar.

---

## Örnekler

**Open Today**


```
iwidget://today
```


**Açık 1 Ocak 2026 detay**


```
iwidget://day?y=2026&m=1&d=1
```


**Açık Ayarlar → festival filtreleri**


```
iwidget://settings?scroll=festivals
```


---

## Widget & Control Center davranışı

- Bir **ev ekran kurulu** **intercept muslukları ** kapalı olabilir (ya da yapılandırılmış açık davranışınızı widget niyetiyle).
- **Lock Ekran** ve ** Kontrol Merkezi ** girişleri App niyetlerini kullanır; ek URL barındırmazlar.
- **Mac menüsü bar ** takvim, bir tarihe tıkladığınızda aynı "gün URL modelini kullanır.

---

## Shortcuts ipuçları

1. Ekle **Açık URL** ve bir `iwidget://` bağlantısını yapıştırın.
2. **Workday ** checks, iWidget'in ** işi/rest day** niyeti ve bir tarih tedarik etmek için Kısayollar aksiyon kütüphanesini ara. - It is **not ** available as a URL query.

[Back to iWidget Support](./) · [FAQ](./faq) · [Privacy Policy](./privacy)


