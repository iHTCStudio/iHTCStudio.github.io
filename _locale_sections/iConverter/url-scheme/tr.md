iConverter, `iconverter://` URL planı derin bağlantıları - dış uygulamalardan 101 araç herhangi birini açın, web sayfaları, QR kodları (generate veya **scan in-app**), Safari veya Apple Shortcuts, opsiyonel olarak önceden teslimat giriş alanları sorgu parametreleri aracılığıyla.

> **Widget notu:** **Launcher** widget aracı seçici, **Web Browser** dışında tüm desteklenen araçları içerir. Widget yapılandırma UI, **iOS sistemi dilini takip eder, ayarlar altında in-app dilinde değil.

## Protokol Doğrulaması


```
iconverter://tool/<ToolItem.rawValue>?key=value&key2=value2
```


- "<ToolItem.rawValue>", aynı ismi widget derin bağlantıları olarak paylaşıyor.
- Parametre isimleri hem kısa anahtarlar hem de eş anlamlı aliazlar (e.g. "text" 'input'a eşdeğerdir).
- Booleans: "1 / gerçek /evet /on" → gerçek; "0/false/no/off' → false.
- Tarihler: "yy.-MM-dd", ISO8601, Unix zamanıtamp (saniyeler).
- Unit dönüştürücüler ortak bir format paylaşıyor: “v’ = değer, “= kaynak ünitesinden (rawValue veya sembolü, case-in sensitive), “to’ = hedef ünitesi.

---

## 1.

**Calculator** - sadece açık sadece


```
iconverter://tool/calculator
```


**Bilimsel Hesaplama** - sadece açık


```
iconverter://tool/scientific
```


**Programmer Hesap** - sadece açık


```
iconverter://tool/programmer
```


---

## 2. Finans

**Mortgage Computing `iconverter://` = kredi miktarı, `<ToolItem.rawValue>` = yıllık oranı %, `text` = 0 = eşit taksit / 1 = eşit ana.


```
iconverter://tool/mortgage?p=1000000&r=3.7&y=30&mode=0
```


**Income Tax** `iconverter://` = aylık maaş, `<ToolItem.rawValue>` = sosyal sigorta, `text` = özel kesinti, `input` = eş, `1/true/yes/on` = yıllık bonus.


```
iconverter://tool/incomeTax?salary=20000&insurance=3000&deduction=1000&threshold=5000&bonus=50000
```


**Compound Interest** `iconverter://` = ana, `<ToolItem.rawValue>` = aylık katkı, `text` = yıllık oranı %, `input` = 0 = yıllık / 1 = aylık / 2 = günlük, `0/false/no/off` =% =%


```
iconverter://tool/compoundInterest?p=100000&m=1000&r=7&y=10&freq=1
```


**Discount `iconverter://` = 0-4, `<ToolItem.rawValue>` = orijinal fiyat, `text` = indirim oranı, `input` = eş, `1/true/yes/on` = azaltma miktarı.


```
iconverter://tool/discount?mode=0&p=299&r=8.5
```


Full-minus örneği:


```
iconverter://tool/discount?mode=3&p=350&t=300&u=50
```


**Tip & AA Split** `iconverter://` = 0 = ipucu / 1 = AA bölünmüş, `<ToolItem.rawValue>` = fatura, `text` = ipucu, `input` = vergi%, `1/true/yes/on` = insanlar say.


```
iconverter://tool/tipAA?mode=0&bill=200&tip=15&tax=0&ppl=4
```


**Mortgage Prevac** `iconverter://` = orijinal kredi, `<ToolItem.rawValue>` = yıllık oran%, `text` = toplam terim (yıllar), `input` = ücretli terimler, `1/true/yes/on` = prepay miktar, `0/false/no/off` = 0 = kısa = 1 = 1 = aylık / 2 = karşılaştırma.


```
iconverter://tool/mortgagePrepay?p=800000&r=3.7&total=30&paid=5&prepay=100000&mode=2
```


**Real Estate Tax** - sadece açık


```
iconverter://tool/realEstateTax
```


---

## 3. Tarih & Zaman

**Age & Yıldönümü** `iconverter://` = doğum günü `<ToolItem.rawValue>` , `text` = referans tarihi.


```
iconverter://tool/ageAnniversary?birth=1990-05-01&ref=2026-05-17
```


**Date Arithmetic** `iconverter://` = 0 = Add /subtract / 1 = tarih farkı.

Add-subtract modu ( `iconverter://` = başlangıç tarihi, `<ToolItem.rawValue>` = ± days, `text` = ± haftalar, `input` = ± ay, `1/true/yes/on` = ± yıl):


```
iconverter://tool/dateArithmetic?mode=0&d1=2026-05-17&d=100
```


Fark modu ( `iconverter://` = tarih 1, `<ToolItem.rawValue>` = tarih 2):


```
iconverter://tool/dateArithmetic?mode=1&d1=2026-01-01&d2=2026-12-31
```


**Lunar Takvim** `iconverter://` = Gregorian date `<ToolItem.rawValue>` .


```
iconverter://tool/lunarCalendar?date=2026-05-17
```


**Solar Şartlar** - sadece açık


```
iconverter://tool/solarTerms
```


**Countdown** `iconverter://` = event name, `<ToolItem.rawValue>` = hedef tarih `text` , `input` = zaman `1/true/yes/on` ```
iconverter://tool/countdown?label=Holiday&target=2026-10-01&time=0
```


**Pregnancy `iconverter://` = 0 = LMP / 1 = konsept / 2 = IVF, `<ToolItem.rawValue>` = referans tarihi, `text` = IVF embriyo günü 0 = D3 / 1 = D5.


```
iconverter://tool/pregnancy?method=0&ref=2026-03-01
```



```
iconverter://tool/pregnancy?method=2&ref=2026-03-15&ivf=1
```


**Erkeklertrual Cycle** `iconverter://` = son menajer dönem tarihi, `<ToolItem.rawValue>` = döngü günleri, `text` = dönem günleri.


```
iconverter://tool/menstrual?lmp=2026-05-01&cycle=28&period=5
```


**World Clock** `iconverter://` = şehir arama anahtar kelime, `<ToolItem.rawValue>` = mevcut zaman `text` , `input` = custom datetime.


```
iconverter://tool/worldClock?q=Tokyo
```



```
iconverter://tool/worldClock?now=0&ref=2026-05-17T20:00:00
```


**Zodiyak** - sadece açık


```
iconverter://tool/zodiac
```


---

## 4. Matematik 4.

**Percentage Computing** `iconverter://` = 0-4, `<ToolItem.rawValue>` = değer A, `text` = değer B.


```
iconverter://tool/percentage?mode=0&a=75&b=120
```


**Fraction Computing - sadece açık


```
iconverter://tool/fraction
```


**Prime Factorization** - sadece açık


```
iconverter://tool/primeFactor
```


**Quadratic Solver** - sadece açık


```
iconverter://tool/quadraticSolver
```


**Statistics** `iconverter://` = dataset, space / comma / yarıkol tarafından ayrı.


```
iconverter://tool/statistics?data=1,2,3,4,5,6,7,8,9,10
```


**Combinations & Permutations** - sadece açık


```
iconverter://tool/combinations
```


**Geometry** `iconverter://` = şekli, `<ToolItem.rawValue>` / `text` / `input` = boyut parametreleri.

Mevcut şekiller: `iconverter://` · `<ToolItem.rawValue>` · `text` · `1/true/yes/on` · `yyyy-MM-dd` · `v` · `v` · `to` ·  C  · `p` C   C `r` · `y` · `salary` Circle ( `iconverter://` = yarıçap):


```
iconverter://tool/geometry?shape=circle&v1=5
```


Rect Fukushima ( `iconverter://` = uzunluk, `<ToolItem.rawValue>` = genişlik):


```
iconverter://tool/geometry?shape=rectangle&v1=10&v2=5
```


Sphere ( `iconverter://` = yarıçap):


```
iconverter://tool/geometry?shape=sphere&v1=3
```


Silindir ( `iconverter://` = yarıçap, `<ToolItem.rawValue>` = yükseklik):


```
iconverter://tool/geometry?shape=cylinder&v1=4&v2=10
```


---

## 5.

**Roman Numeral** `iconverter://` = Arapça sayı (1-3999); veya `<ToolItem.rawValue>` = Roman numeral dize.


```
iconverter://tool/roman?n=2026
```



```
iconverter://tool/roman?roman=MMXXVI
```


**Base64 Encoder / Decoder** `iconverter://` = encode/decode, `<ToolItem.rawValue>` = URL-güven mod `text` , `input` = giriş text.


```
iconverter://tool/base64?mode=encode&text=Hello%2C+World!
```



```
iconverter://tool/base64?mode=decode&urlSafe=0&text=SGVsbG8sIFdvcmxkIQ%3D%3D
```


**URL Encoder / Decoder** `iconverter://` = encode/decode, `<ToolItem.rawValue>` = bileşen modu 0 = tam / 1 = sorgu / 2 = yol, `text` = giriş.


```
iconverter://tool/urlCoder?mode=encode&comp=0&text=https://example.com/path?q=hello world
```



```
iconverter://tool/urlCoder?mode=decode&text=https%3A%2F%2Fexample.com%2F%3Fq%3Dhello%20world
```


**Hash Hesaplaması** `iconverter://` = giriş, `<ToolItem.rawValue>` = md5/sha1/sha256/sha512, `text` = üstcase `input` , `1/true/yes/on` = HMAC    C  C  5               ,    C  = HMAC anahtar.


```
iconverter://tool/hashing?text=Hello+World&algo=sha256&upper=0
```



```
iconverter://tool/hashing?text=data&algo=md5&hmac=1&key=secret
```


**Word Count** `iconverter://` = analiz etmek için metin.


```
iconverter://tool/wordCount?text=The+quick+brown+fox+jumps+over+the+lazy+dog.
```


**Renk paketi ** `iconverter://` = hex color; veya `<ToolItem.rawValue>` / `text` / `input` = RGB bileşenleri (0-255).


```
iconverter://tool/colorConverter?hex=%23FF8800
```



```
iconverter://tool/colorConverter?r=255&g=136&b=0
```


**Renk Yakıtı** - sadece açık


```
iconverter://tool/colorPalette
```


**QR Kodu** `iconverter://` = içerik, `<ToolItem.rawValue>` = `text` vs., `input` = hata düzeltme seviyesi `1/true/yes/on` .


```
iconverter://tool/qrcode?text=https%3A%2F%2Fexample.com&ecc=H
```



```
iconverter://tool/qrcode?text=Hello+iConverter&format=qr&ecc=M
```


**JSON Formatter** `iconverter://` = JSON dize (URL-encoded), `<ToolItem.rawValue>` = indent Space 2/4.


```
iconverter://tool/jsonFormatter?text=%7B%22name%22%3A%22Alice%22%2C%22age%22%3A30%7D&indent=2
```


**Timestamp** `iconverter://` = Unix timestamp (saniyeler), `<ToolItem.rawValue>` = ünite 0 = gizli / 1 = ms; veya `text` = ISO8601 tarih dizesi.


```
iconverter://tool/timestamp?ts=1747440000
```



```
iconverter://tool/timestamp?iso=2026-05-17T12:00:00
```


**Bank Card Validator** `iconverter://` = kart numarası.


```
iconverter://tool/bankCard?num=6214830172816734
```


**Text Case Converter `iconverter://` = giriş metni.


```
iconverter://tool/textCase?text=hello+world+from+iConverter
```


**Text Diff ** - sadece açık


```
iconverter://tool/textDiff
```


**HTTP Request** `iconverter://` = istek URL, `<ToolItem.rawValue>` = GET/POST/PUT/PATCH/DELETE, `text` = istek vücut, `input` = `1/true/yes/on` , `0/false/no/off` = Başlıklar JSON.


```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=GET
```



```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=POST&body=%7B%22name%22%3A%22Alice%22%7D&bodyKind=json
```


**File Download** `iconverter://` = URL indir, `<ToolItem.rawValue>` = dosya adı (isteğe bağlı).


```
iconverter://tool/fileDownload?url=https%3A%2F%2Fexample.com%2Freport.pdf&name=report.pdf
```


**HTTP Durum Kodu** `iconverter://` = durum kodu; veya `<ToolItem.rawValue>` = arama anahtar kelime.


```
iconverter://tool/httpStatusCodes?code=404
```



```
iconverter://tool/httpStatusCodes?q=redirect
```


** `iconverter://` = subnet/cid/range, `<ToolItem.rawValue>` = IP adresi, `text` = subnet maskesi; veya `input` = CIDR prefix uzunluğu.


```
iconverter://tool/ipUtility?mode=subnet&ip=192.168.1.0&mask=255.255.255.0
```



```
iconverter://tool/ipUtility?ip=10.0.0.0&prefix=24
```


**ASCII Table** `iconverter://` = decimal codepoint; veya `<ToolItem.rawValue>` = hex codepoint; veya `text` = arama.


```
iconverter://tool/asciiTable?dec=65
```



```
iconverter://tool/asciiTable?q=space
```


**Password Jeneratör** `iconverter://` = uzunluk, `<ToolItem.rawValue>` = üstcase `text` , `input` = altcase `1/true/yes/on` , `0/false/no/off` = basamaklar `yyyy-MM-dd` C7       sembolleri = `to` = no ambiguous chars `to` = `to` = hemen `y` ```
iconverter://tool/passwordGenerator?length=20&upper=1&lower=1&digits=1&symbols=1&unambiguous=1&go=1
```


**Random Number Jeneratör ** `iconverter://` = minimum, `<ToolItem.rawValue>` = maksimum, `text` = say, `input` = decimal yerler, `1/true/yes/on` = eşsiz `yyyy-MM-dd` = 0 = 0 = 0 = 1 = asc / 2 = desc, `v` = hemen `from` = 0 = 0 = 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 = 0 0 0 = 1 = 1 = 1 = 1 = 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0


```
iconverter://tool/randomNumber?min=1&max=100&n=10&unique=1&sort=1&go=1
```



```
iconverter://tool/randomNumber?min=0&max=1&n=5&decimals=4&go=1
```


**Morse Code** `iconverter://` = encode/decode, `<ToolItem.rawValue>` = giriş metni.


```
iconverter://tool/morseCode?mode=encode&text=SOS
```



```
iconverter://tool/morseCode?mode=decode&text=...+---+...
```


**JWT Decoder** `iconverter://` = JWT token string.


```
iconverter://tool/jwtParser?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```


**Cron Expression Parser** `iconverter://` = Cron ifadesi (spaces, `<ToolItem.rawValue>` ile değiştirilebilir).


```
iconverter://tool/cronParser?expr=0+9+*+*+1-5
```



```
iconverter://tool/cronParser?expr=0+0+*+*+*
```


**Regex Tester** `iconverter://` = regex pattern (URL-encoded), `<ToolItem.rawValue>` = test text, `text` = değiştirme, `input` = case-in sensitive `1/true/yes/on` , `0/false/no/off` = multiline `v` = dotall    C `from` .


```
iconverter://tool/regexTester?pattern=%5Cd%2B&haystack=abc123def456&i=0
```



```
iconverter://tool/regexTester?pattern=%28%5Cw%2B%29&haystack=hello+world&replacement=%5B%241%5D&i=1
```


**Web Browser** `iconverter://` = open URL direkt olarak; veya `<ToolItem.rawValue>` = arama sorgusu (olas varsayılan arama motoru).


```
iconverter://tool/webBrowser?url=https%3A%2F%2Fexample.com
```



```
iconverter://tool/webBrowser?q=SwiftUI+deep+link+2026
```


---

## 6. Yaşam tarzı

**BMI Hesaplayıcısı `iconverter://` = yükseklik cm, `<ToolItem.rawValue>` = ağırlık kg, `text` = standart 0 = Çin yetişkin / 1 = WHO.


```
iconverter://tool/bmi?h=175&w=70&std=0
```


**BMR Hesaplaması** `iconverter://` = yükseklik cm, `<ToolItem.rawValue>` = ağırlık kg, `text` = yaş, `input` = m = erkek / f = kadın, `1/true/yes/on` = aktivite seviyesi 0-4, `0/false/no/off` = 0 = 0 = Harris-Benedict / 1 = Mifflin-St.


```
iconverter://tool/bmr?h=175&w=70&age=30&sex=m&act=1&formula=1
```


**Clothing Boyut** - sadece açık


```
iconverter://tool/clothingSize
```


**Ring Dimension** – sadece açık


```
iconverter://tool/ringSize
```


**Height Converter** - sadece açık


```
iconverter://tool/heightConverter
```


**Fuel Maliyet Hesaplayıcısı** `iconverter://` = 0 = metric / 1 = emperyal, `<ToolItem.rawValue>` = mesafe, `text` = 100 km, `input` = yakıt fiyatı, `1/true/yes/on` = insanlar.


```
iconverter://tool/fuelCost?unit=0&d=500&c=8.5&p=7.8&n=1
```


**Shipping Fee `iconverter://` = gerçek ağırlık kg, `<ToolItem.rawValue>` = ilk ağırlık kg, `text` = ilk ağırlık ücreti, `input` = adım ağırlık kg, `1/true/yes/on` = step ücreti.


```
iconverter://tool/shippingFee?w=3.5&fw=1&ff=12&sw=1&sf=8
```


volumetrik ağırlık ( `iconverter://` = `<ToolItem.rawValue>` , `text` / `input` / `1/true/yes/on` = 3 side cm, `0/false/no/off` = divisor):


```
iconverter://tool/shippingFee?w=2&vol=1&l=50&wd=40&h=30&div=6000&fw=1&ff=12&sw=1&sf=8
```


**Kan Alkol İçerik (BAC)** `iconverter://` = m = erkek / f = kadın, `<ToolItem.rawValue>` = ağırlık kg, `text` = hacim mL, `input` = ABV%, `1/true/yes/on` = saatler çünkü içki.


```
iconverter://tool/alcoholBac?sex=m&w=70&v=500&abv=5&h=0.5
```


**Relationship** `iconverter://` = ilişki zinciri (comma-separated), `<ToolItem.rawValue>` = ego seks 0 = erkek / 1 = kadın, `text` = şovu ters `input` ```
iconverter://tool/relationship?chain=f,os&sex=0&reverse=1
```



```
iconverter://tool/relationship?chain=m,ob&sex=1&reverse=0
```


**ID Card Parser** `iconverter://` = kimlik kartı numarası.


```
iconverter://tool/idCard?id=110101199003073010
```


**Coin Flip** - sadece açık


```
iconverter://tool/coinFlip
```


**Dice Roller** - sadece açık


```
iconverter://tool/diceRoller
```


**Random Draw** – sadece açık


```
iconverter://tool/randomDraw
```


**Spin Wheel** - sadece açık


```
iconverter://tool/spinWheel
```


**Video Frame Export** - sadece açık


```
iconverter://tool/videoFrameExport
```


---

## 7. Sensörler

**Compass** - sadece açık


```
iconverter://tool/compass
```


**Level** - sadece açık


```
iconverter://tool/level
```


**Altitude** - sadece açık


```
iconverter://tool/altitude
```


---

## 8. Çin Çin

**Çin Sayısı ** `iconverter://` = sayı.


```
iconverter://tool/chineseNumber?n=12345.67
```


** Çin Sayıları Ters** `iconverter://` = Çin numeral dize.


```
iconverter://tool/chineseNumberReverse?text=一万二千三百四十五
```


** Amount $** `iconverter://` = miktar, `<ToolItem.rawValue>` = append . `text` .


```
iconverter://tool/financialAmount?amount=12345.67&zheng=1
```


---

## 9. Unit Converter

Genel format: `iconverter://` = değer, `<ToolItem.rawValue>` = kaynak ünitesi (rawValue veya sembolü, case-in sensitive), `text` = hedef ünitesi.

---

**Length**
Ortak birimler: `iconverter://` (m) · `<ToolItem.rawValue>` (km) · `v` (yd) ·    C  (nmi) · `to` (ft)


```
iconverter://tool/length?v=100&from=meter&to=foot
```



```
iconverter://tool/length?v=1&from=mile&to=kilometer
```


** Area**
Ortak birimler: `iconverter://` (m2) · `<ToolItem.rawValue>` (ha) · `text` (acre) · `input` (ft2)


```
iconverter://tool/area?v=1&from=hectare&to=mu
```



```
iconverter://tool/area?v=1&from=acre&to=squareMeter
```


**Volume**
Ortak birimler: `iconverter://` (L) · `<ToolItem.rawValue>` (mL) · `text` (m3) · `input` (gal) · `1/true/yes/on` (fl oz)


```
iconverter://tool/volume?v=1&from=gallon&to=liter
```



```
iconverter://tool/volume?v=355&from=milliliter&to=fluidOunce
```


**Weight / Mass**
Ortak birimler: `iconverter://` (kg) · `<ToolItem.rawValue>` (g) · `text` (lb) · `input` (oz) · `1/true/yes/on` (t) · `0/false/no/off` (斤)


```
iconverter://tool/weight?v=1&from=pound&to=kilogram
```



```
iconverter://tool/weight?v=1&from=jin&to=gram
```


**Temperature**
Birimler: `iconverter://` (°C) · `<ToolItem.rawValue>` (°F) · `text` (K) · `input` (°R)


```
iconverter://tool/temperature?v=100&from=celsius&to=fahrenheit
```



```
iconverter://tool/temperature?v=37&from=celsius&to=kelvin
```


**Time**
Ortak birimler: `iconverter://` (s) · `<ToolItem.rawValue>` (min) · `text` (h) · `input` (gün) · `1/true/yes/on` (wk) · `0/false/no/off` (mo) · `yyyy-MM-dd` C7  (yr)


```
iconverter://tool/time?v=1&from=hour&to=second
```



```
iconverter://tool/time?v=7&from=day&to=hour
```


**Speed**
Birimler: `iconverter://` (m/s) · `<ToolItem.rawValue>` (km/h) · `text` (mph) · `input` (kn)


```
iconverter://tool/speed?v=100&from=kmPerHour&to=milePerHour
```



```
iconverter://tool/speed?v=1&from=mach&to=meterPerSecond
```


**Basın
Birimler: `iconverter://` (Pa) · `<ToolItem.rawValue>` (kPa) · `text` (bar) · `input` (atm) · `1/true/yes/on` (psi)


```
iconverter://tool/pressure?v=1&from=atmosphere&to=kilopascal
```



```
iconverter://tool/pressure?v=120&from=mmHg&to=kilopascal
```


**Energy**
Birimler: `iconverter://` (J) · `<ToolItem.rawValue>` (kJ) · `text` (cal) · `1/true/yes/on` (kWh) · `0/false/no/off` (BTU).


```
iconverter://tool/energy?v=1&from=kilowattHour&to=kilojoule
```



```
iconverter://tool/energy?v=500&from=kilocalorie&to=kilojoule
```


**Power**
Birimler: `iconverter://` (W) · `<ToolItem.rawValue>` (kW) · `text` (hp) · `input` (PS) · `1/true/yes/on` (BTU/h).


```
iconverter://tool/power?v=1&from=hpMechanical&to=kilowatt
```



```
iconverter://tool/power?v=3000&from=watt&to=hpMetric
```


**Force**
Birimler: `iconverter://` (N) · `<ToolItem.rawValue>` (kN) · `text` (kgf) · `input` (lbf) · `1/true/yes/on` (dyn).


```
iconverter://tool/force?v=9.8&from=newton&to=kgf
```



```
iconverter://tool/force?v=1&from=kilonewton&to=lbf
```


**Torque**
Birimler: `iconverter://` (N·m) · `<ToolItem.rawValue>` (N·cm) · `text` (kgf·m)


```
iconverter://tool/torque?v=100&from=newtonMeter&to=footPound
```


**Frequency**
Birimler: `iconverter://` (Hz) · `<ToolItem.rawValue>` (kHz) · `text` (fil) · `input` (gir) · `1/true/yes/on` (THz)


```
iconverter://tool/frequency?v=2.4&from=gigahertz&to=megahertz
```



```
iconverter://tool/frequency?v=3000&from=rpm&to=hertz
```


**Angle**
Birimler: `iconverter://` (°) · `<ToolItem.rawValue>` (rad) · `text` (grad) · `input` () · `1/true/yes/on` ()


```
iconverter://tool/angle?v=180&from=degree&to=radian
```



```
iconverter://tool/angle?v=1&from=turn&to=degree
```


**Data Storage**
Birimler: `iconverter://` (B) · `<ToolItem.rawValue>` (KB) · `text` (MB) · `input` (GB) · `1/true/yes/on` (TB)


```
iconverter://tool/dataStorage?v=1&from=gigabyte&to=mebibyte
```



```
iconverter://tool/dataStorage?v=512&from=mebibyte&to=gigabyte
```


**Data Rate**
Birimler: `iconverter://` (bps) · `<ToolItem.rawValue>` C2    (Mbps) · `input` (Gbps) · `1/true/yes/on` (KB/ `0/false/no/off` )


```
iconverter://tool/dataRate?v=100&from=mbps&to=mBps
```



```
iconverter://tool/dataRate?v=1&from=gbps&to=mbps
```


**Illuminance**
Birimler: `iconverter://` (lx) · `<ToolItem.rawValue>` (fc) · `text` (ph) · `input` (nx).


```
iconverter://tool/illuminance?v=500&from=lux&to=footCandle
```


**Magnetic Flux Mechanic**
Birimler: `iconverter://` (T) · `<ToolItem.rawValue>` (mT) · `text` (μT) · `input` (G) · `1/true/yes/on` ```
iconverter://tool/magneticFlux?v=1&from=tesla&to=gauss
```


** Radyoaktivite**
Birimler: `iconverter://` (Bq) · `<ToolItem.rawValue>` (kBq) · `text` C3    (Ci) · `1/true/yes/on` (mC)


```
iconverter://tool/radioactivity?v=1&from=curie&to=megabecquerel
```


**Viscosity**
Birimler: `iconverter://` (Pa·s) · `<ToolItem.rawValue>` (mPa·s) · `text` (P) · `input` (cP).


```
iconverter://tool/viscosity?v=1&from=pascalSecond&to=centipoise
```


**Fuel Ekonomisi**
Birimler: `iconverter://` (L/100km) · `<ToolItem.rawValue>` (km/L) · `text` (MPG US) · `input` (MPG UK).


```
iconverter://tool/fuelEconomy?v=8.5&from=lPer100km&to=kmPerL
```



```
iconverter://tool/fuelEconomy?v=30&from=mpgUS&to=lPer100km
```


**Flow Oranı**
Birimler: `iconverter://` (m3/s) · `<ToolItem.rawValue>` C2    (L/s) · `input` (L/min)


```
iconverter://tool/flowRate?v=1&from=literPerMinute&to=cubicMeterPerHour
```


**Density**
Birimler: `iconverter://` (kg/m3) · `<ToolItem.rawValue>` (g/cm3) · `text` (g/L) · `input` (kg/L)


```
iconverter://tool/density?v=1&from=gramPerCubicCentimeter&to=kgPerCubicMeter
```


**Magnetic Flux (Wb)**
Birimler: `iconverter://` (Wb) · `<ToolItem.rawValue>` (mWb)


```
iconverter://tool/magneticFluxTrue?v=1&from=weber&to=maxwell
```


**Absorbed Dose**
Birimler: `iconverter://` (Gy) · `<ToolItem.rawValue>` (mGy) · `text` (μGy) · `input` (kGy)


```
iconverter://tool/absorbedDose?v=1&from=gray&to=rad
```


**Equivalent Dose**
Birimler: `iconverter://` (Sv) · `<ToolItem.rawValue>` (mSv) · `text` (μSv) · `input` (rem)


```
iconverter://tool/equivalentDose?v=1&from=sievert&to=rem
```



```
iconverter://tool/equivalentDose?v=20&from=millisievert&to=microsievert
```


** Substance**
Birimler: `iconverter://` (mol) · `<ToolItem.rawValue>` (mmol) · `text` (μmol) · `1/true/yes/on` (nmol)


```
iconverter://tool/amountOfSubstance?v=1&from=mole&to=millimole
```



```
iconverter://tool/amountOfSubstance?v=150&from=millimole&to=micromole
```


---

[Back to iConverter Support](./) &middot; [FAQ](./faq) &middot; [Privacy Policy](./privacy)


