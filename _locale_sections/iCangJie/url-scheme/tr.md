iCangJie ** `iCangJie://` ** URL planı derin bağlantıları - açık arama, kelime detayı, Daily Quiz, Typing, Favorites, Wrong Book, Levels, or Learn from Safari, another app, a QR code, a item, or Apple Shortcuts.

Paralel bir dizi **Home Ekran Hızlı Eylemler ** (Uygulama ikonunu uzun süreli baskı) Arama, geri bildirim ve Puan gibi ek destinasyonları kapsar. 2018'de 4 kısayolu yapılandırın **Settings → App Ayarları → Ev Ekran kısayolları**.

## Protokol Doğrulaması


```
iCangJie://<host>[?query]
```


| Rule | Detaylı Bilgi |
|------|--------|
| **Scheme** | "icangjie" / "iCangJie" - vakaya duyarlı olarak karşılaştırıldığında |
| **Host routing** | Birincil yönlendirici URL **host** |
| **Query aliases** | "q", "word" ve "name" arama / kelime ev sahipliği için değiştirilebilir |
| **Parser** | "ICangJie DeepLink.parse ( :)" - "onOpenURL" → "AppRouter.pending DeepLink" |

** Üç teslimat kanalı**

| Channel | Handled by | Örnekler |
|---------|------------|----------|
| **Universal deep link** (`onOpenURL`) | `ICangJieDeepLink.parse` → `RootTabView` | "Arapça", "quiz", "favorites", "wrong", " seviyeler", " |
| **Home Screen Quick Action** | `ShortcutObserver.dispatch` | "Arapçalar", "wrong", " seviyeler", "feedback", " |
| **App Intents / Siri / Widget pending URL** | Writes `AppGroup.pendingDeepLinkURL` → `RootTabView.consumePendingDeepLinkFromAppGroup()` | Lookup kodu, başlangıç testi, açık arama |

Hızlı aksiyon türleri ** `iCangJie://` ** tipi dizede eşleşen, bu yüzden hem de `icangjie` ve mirası seçenekleri hala doğru rotayı doğru şekilde rotalar.

---

## 1. Lookup Search

**Bakup** sekmesi açın. Seçmeli olarak arama alanını önceden doldur.

| Parameter | Required | Açıklama |
|-----------|----------|-------------|
| `q` | No | Arama sorgusu (Ek olarak, karakter, pinyin veya Jyutping) |
| `word` | No | "q" için eş anlamlı |
| `name` | No | "q" için eş anlamlı |

**Open Lookup (boş arama)**


```
iCangJie://search
```


** Kodu önceden ek olarak arayın `iCangJie://` **


```
iCangJie://search?q=ab
```


** Karakter için ara


```
iCangJie://search?q=颉
```


---

## 2. Word Detayları

Tek bir karakter için detay sayfasını açın. Boş olmayan bir sorgu gerektirir.

| Parameter | Required | Açıklama |
|-----------|----------|-------------|
| `q` | One of `q` / `word` / `name` | Hedef Han karakteri |
| `word` | One of `q` / `word` / `name` | "q" için eş anlamlı |
| `name` | One of `q` / `word` / `name` | "q" için eş anlamlı |

**Hosts kabul etti: ** `iCangJie://` , `icangjie` , `iCangJie` **  for** için açık detay


```
iCangJie://word?q=倉
```


Alternatif ev sahibi:


```
iCangJie://character?word=颉
```


Soru ** Eksik veya karakter sözlükte değilse, bağlantı ** olarak göz ardı edilir**.

---

## 3. Günlük Quiz

Doğrudan **Daily Quiz**'e gidin. Auto-start veya soruları atlamayın.


```
iCangJie://quiz
```


Aliases: `iCangJie://` ---

## 4. Typing Practice

**Typing ** sekme merkezi açın.


```
iCangJie://typing
```


Aliases: `iCangJie://` , `icangjie` ---

## 5. Favoriler

**Favorites ** listesi açın.


```
iCangJie://favorites
```


Alias: `iCangJie://` ---

## 6. Yanlış Cevap Kitabı

### 6.1 Listesi

**Wrong Cevap Kitabı** listesi açın.


```
iCangJie://wrong
```


Aliases: `iCangJie://` , `icangjie` ### 6.2 Tek kayıt `iCangJie://` , kurtarılmış bir yanlış cevap girişinin geçerli bir UUID'si olduğunda, uygulama bu rekorun kelime detayını açar (eğer kayıt hala varsa).

| Parameter | Required | Format |
|-----------|----------|--------|
| `record` | Yes | UUID string |
| `id` | Yes | "record" için Synonym |


```
iCangJie://wrong?record=550e8400-e29b-41d4-a716-446655440000
```


---

## 7. Seviyeler (Kolay uzunluğu)

**Levels ** sekmesi açın.


```
iCangJie://levels
```


Aliases: `iCangJie://` , `icangjie` ---

## 8. Öğrenme (yardım)

**Learn ** merkezi açın.


```
iCangJie://learn
```


Aliases: `iCangJie://` ---

## 9. Geri bildirim (Quick Action sadece)

Tamamlanmış geri bildirimler e-posta bestecisi açın (veya `iCangJie://` geri dönüş).


```
iCangJie://feedback
```


**Home Ekran Hızlı Aksiyon ** / `iCangJie://` , `icangjie` .

---

## 10. App Store Review (Quick Action sadece)

Bir in-app App Store incelemesini talep edin.


```
iCangJie://review
```


Alias eşleştirme ayrıca hızlı tepki türü dizesinde `iCangJie://` 'i kabul eder.

---

## 11. App niyetleri ve Siri (iOS 16+)

Yerleşik **App Kısa kesimler ** Kısa kesimler uygulamasında ve Siri'de görünür. Her niyet, App Grubu'nda `iCangJie://` ayarlar; uygulama bunu başlatıyor.

| Intent | Action | Pending URL |
|--------|--------|-------------|
| **Look up Cangjie code** | Opens word detail for the given character | "iCangJie httpword?q=<char>" |
| **Start daily quiz** | Opens Daily Quiz | "iCangJie httpquiz" |
| **Open lookup search** | Opens Lookup tab | "iCangJie httpsearch" |

**Example Siri cümleleri (İngilizce)**

- * "Bak up Cangjie code for 颉 in iCangJie"*
- *"ICangJie'de günlük sınava başlayın"*
- *"Ara Cangjie in iCangJie"*

**Shortcuts **, iCangJie uygulama bölümünden eylem ekleyin. **Bakın** niyeti ** Çin karakteri ** parametresi ( `iCangJie://` ).

> App niyetleri **iOS sadece**.OS, `iCangJie://` URL'lere ve menü navigasyona dayanmaktadır.

---

## Widget Deep Links

Widgets aynı `iCangJie://` URL'leri ele alır. Örnekler:

| Widget | Tipik URL URL URL |
|--------|-------------|
| Daily Character | "iCangJie httpword?q=<char>" |
| Code Length | “iCangJie: |
| Daily Quiz | "iCangJie httpquiz" |
| Typing Glance | "iCangJie #typing" |
| Favorites | "iCangJie httpfavorites" |
| Wrong Book | "iCangJie httpwrong" |
| Recent | "iCangJie httpsearch" |
| Learning Progress | “iCangJie: |

---

## Kısaltmalar Örnekler

**Bugünün sınavı**


```
iCangJie://quiz
```


**Singboard'dan bir karaktere bakın**

Kısa bir kesim kullanın ** Clipboard ** aksiyon alın, sonra **Open URL** ile:


```
iCangJie://word?q=[Clipboard]
```


** Uygulamayı yazmaya başlayın**


```
iCangJie://typing
```


---

## Home Screen Quick Actions

ICangJie app i. Varsayılan seçenekler ( Ayarları 4'e kadar):

| Action | URL URL URL URL |
|--------|-----|
| Search | "iCangJie httpsearch" |
| Daily Quiz | "iCangJie httpquiz" |
| Favorites | "iCangJie httpfavorites" |
| Wrong Book | "iCangJie httpwrong" |
| Code Length | “iCangJie: |
| Feedback | "iCangJie https |
| Rate App | "iCangJie http |


