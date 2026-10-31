iConverter unterstützt `iconverter://` URL-Schema Deep Links - Öffnen Sie eines der 101 Tools von externen Apps, Webseiten, QR-Codes (generieren oder **scannen in-App **), Safari oder Apple Shortcuts, optional Vorfüllen von Eingabefeldern über Abfrageparameter.

> **Widget Note:** Der **Launcher ** Widget Tool Picker enthält alle unterstützten Tools außer **Web Browser **. Widget-Konfigurations-Benutzeroberfläche folgt ** iOS-Systemsprache **, nicht die In-App-Sprache überschreibt unter Einstellungen.

## Protokollspezifikation


```
iconverter://tool/<ToolItem.rawValue>?key=value&key2=value2
```


- „<ToolItem.rawValue> teilt die gleiche Benennung wie Widget Deep Links.
- Parameternamen unterstützen sowohl kurze Schlüssel als auch synonyme Aliase (z. B. `text` entspricht `input`).
- Booleaner: `1/true/yes/on` → true; `0/false/no/off` → false.
- Daten: unterstützt `yyyy-MM-dd`, ISO8601, Unix-Zeitstempel (Sekunden).
- Einheitenkonverter haben ein gemeinsames Format: `v` = Wert, `from` = Quelleinheit (rawValue oder Symbol, case-insensitive), `to` = Zieleinheit.

---

## 1. Rechner

**Rechner** — nur geöffnet


```
iconverter://tool/calculator
```


**Wissenschaftlicher Rechner** — nur geöffnet


```
iconverter://tool/scientific
```


**Programmer Calculator** — nur geöffnet


```
iconverter://tool/programmer
```


---

## 2. Finanzen

**Hypothekenrechner** `iconverter://` = Kreditbetrag, `<ToolItem.rawValue>` = Jahreszinssatz %, `text` = Jahre, `input` = 0 = gleiche Rate / 1 = gleiches Kapital.


```
iconverter://tool/mortgage?p=1000000&r=3.7&y=30&mode=0
```


**Einkommensteuer** `iconverter://` = Monatsgehalt, `<ToolItem.rawValue>` = Sozialversicherung, `text` = Sonderabzug, `input` = Schwelle, `1/true/yes/on` = Jahresbonus.


```
iconverter://tool/incomeTax?salary=20000&insurance=3000&deduction=1000&threshold=5000&bonus=50000
```


**Zinssatz** `iconverter://` = Hauptforderung, `<ToolItem.rawValue>` = monatlicher Beitrag, `text` = Jahreszinssatz %, `input` = Jahre, `1/true/yes/on` = 0 = jährlich / 1 = monatlich / 2 = täglich, `0/false/no/off` = Inflation %.


```
iconverter://tool/compoundInterest?p=100000&m=1000&r=7&y=10&freq=1
```


**Rabattrechner** `iconverter://` = 0-4, `<ToolItem.rawValue>` = Originalpreis, `text` = Abzinsungsverhältnis, `input` = Schwellenwert, `1/true/yes/on` = Minderungsbetrag.


```
iconverter://tool/discount?mode=0&p=299&r=8.5
```


Voll minus Beispiel:


```
iconverter://tool/discount?mode=3&p=350&t=300&u=50
```


**Tipp & AA Split** `iconverter://` = 0 = Spitze / 1 = AA Split, `<ToolItem.rawValue>` = Rechnung, `text` = Spitze %, `input` = Steuer %, `1/true/yes/on` = Menschen zählen.


```
iconverter://tool/tipAA?mode=0&bill=200&tip=15&tax=0&ppl=4
```


** Hypothekenzahlung** `iconverter://` = ursprüngliches Darlehen, `<ToolItem.rawValue>` = Jahreszinssatz %, `text` = Gesamtlaufzeit (Jahre), `input` = bezahlte Konditionen, `1/true/yes/on` = Vorauszahlungsbetrag, `0/false/no/off` = 0 = Verkürzung / 1 = monatliche Reduzierung / 2 = vergleichen.


```
iconverter://tool/mortgagePrepay?p=800000&r=3.7&total=30&paid=5&prepay=100000&mode=2
```


**Immobiliensteuer** - nur offen


```
iconverter://tool/realEstateTax
```


---

## 3. Datum und Uhrzeit

** Alter & Jubiläum ** `iconverter://` = Geburtstag `<ToolItem.rawValue>` , `text` = Stichtag.


```
iconverter://tool/ageAnniversary?birth=1990-05-01&ref=2026-05-17
```


**Datum Arithmetik** `iconverter://` = 0 = add/subtract / 1 = Datumsdifferenz.

Add-Subtraktionsmodus ( `iconverter://` = Startdatum, `<ToolItem.rawValue>` = ± Tage, `text` = ± Wochen, `input` = ± Monate, `1/true/yes/on` = ± Jahre):


```
iconverter://tool/dateArithmetic?mode=0&d1=2026-05-17&d=100
```


Differenzmodus ( `iconverter://` = Datum 1, `<ToolItem.rawValue>` = Datum 2):


```
iconverter://tool/dateArithmetic?mode=1&d1=2026-01-01&d2=2026-12-31
```


** Mondkalender** `iconverter://` = Gregorianisches Datum `<ToolItem.rawValue>` .


```
iconverter://tool/lunarCalendar?date=2026-05-17
```


**Solar Terms** — nur offen


```
iconverter://tool/solarTerms
```


**Countdown** `iconverter://` = Ereignisname, `<ToolItem.rawValue>` = Zieldatum `text` , `input` = Einschlusszeit `1/true/yes/on` .


```
iconverter://tool/countdown?label=Holiday&target=2026-10-01&time=0
```


**Schwangerschaftsrechner** `iconverter://` = 0 = LMP / 1 = Konzeption / 2 = IVF, `<ToolItem.rawValue>` = Stichtag, `text` = IVF-Embryotag 0 = D3 / 1 = D5.


```
iconverter://tool/pregnancy?method=0&ref=2026-03-01
```



```
iconverter://tool/pregnancy?method=2&ref=2026-03-15&ivf=1
```


**Menstrueller Zyklus** `iconverter://` = Datum der letzten Menstruation, `<ToolItem.rawValue>` = Zyklustage, `text` = Periodentage.


```
iconverter://tool/menstrual?lmp=2026-05-01&cycle=28&period=5
```


** Weltuhr** `iconverter://` = city search keyword, `<ToolItem.rawValue>` = use current time `text` , `input` = custom datetime.


```
iconverter://tool/worldClock?q=Tokyo
```



```
iconverter://tool/worldClock?now=0&ref=2026-05-17T20:00:00
```


** Tierkreis** — nur geöffnet


```
iconverter://tool/zodiac
```


---

## 4. Mathe

**Prozentsatzrechner** `iconverter://` = 0-4, `<ToolItem.rawValue>` = Wert A, `text` = Wert B.


```
iconverter://tool/percentage?mode=0&a=75&b=120
```


**Fraktionsrechner** — nur geöffnet


```
iconverter://tool/fraction
```


**Prime Factorization** — nur offen


```
iconverter://tool/primeFactor
```


**Quadratischer Solver** – nur offen


```
iconverter://tool/quadraticSolver
```


**Statistik** `iconverter://` = Datensatz, getrennt durch Leerzeichen / Komma / Semikolon.


```
iconverter://tool/statistics?data=1,2,3,4,5,6,7,8,9,10
```


**Kombinationen & Permutationen** – nur offen


```
iconverter://tool/combinations
```


**Geometrie** `iconverter://` = Form, `<ToolItem.rawValue>` / `text` / `input` = Dimensionsparameter.

Verfügbare Formen: `iconverter://` · `<ToolItem.rawValue>` · `text` · `input` · `1/true/yes/on` · `0/false/no/off` · `yyyy-MM-dd` · `v` · `from` · `to` · `r` · `y` · `mode` · `salary` · `insurance` · `deduction` .

Kreis ( `iconverter://` = Radius):


```
iconverter://tool/geometry?shape=circle&v1=5
```


Rechteck ( `iconverter://` = Länge, `<ToolItem.rawValue>` = Breite):


```
iconverter://tool/geometry?shape=rectangle&v1=10&v2=5
```


Kugel ( `iconverter://` = Radius):


```
iconverter://tool/geometry?shape=sphere&v1=3
```


Zylinder ( `iconverter://` = Radius, `<ToolItem.rawValue>` = Höhe):


```
iconverter://tool/geometry?shape=cylinder&v1=4&v2=10
```


---

## 5. Kodierung

**Roman Numeral** `iconverter://` = arabische Zahl (1-3999); oder `<ToolItem.rawValue>` = römische Zahlenfolge.


```
iconverter://tool/roman?n=2026
```



```
iconverter://tool/roman?roman=MMXXVI
```


**Base64 Encoder / Decoder** `iconverter://` = Code/Decode, `<ToolItem.rawValue>` = URL-sicherer Modus `text` , `input` = Eingabetext.


```
iconverter://tool/base64?mode=encode&text=Hello%2C+World!
```



```
iconverter://tool/base64?mode=decode&urlSafe=0&text=SGVsbG8sIFdvcmxkIQ%3D%3D
```


**URL Encoder / Decoder** `iconverter://` = encode/decode, `<ToolItem.rawValue>` = Component Mode 0 = full / 1 = query / 2 = path, `text` = input.


```
iconverter://tool/urlCoder?mode=encode&comp=0&text=https://example.com/path?q=hello world
```



```
iconverter://tool/urlCoder?mode=decode&text=https%3A%2F%2Fexample.com%2F%3Fq%3Dhello%20world
```


**Hash Calculator** `iconverter://` = Input, `<ToolItem.rawValue>` = md5/sha1/sha256/sha512, `text` = Großbuchstaben `input` , `1/true/yes/on` = HMAC `0/false/no/off` , `yyyy-MM-dd` = HMAC-Schlüssel aktivieren.


```
iconverter://tool/hashing?text=Hello+World&algo=sha256&upper=0
```



```
iconverter://tool/hashing?text=data&algo=md5&hmac=1&key=secret
```


**Word Count** `iconverter://` = Text zur Analyse.


```
iconverter://tool/wordCount?text=The+quick+brown+fox+jumps+over+the+lazy+dog.
```


**Farbwandler ** `iconverter://` = Hexfarbe; oder `<ToolItem.rawValue>` / / `text` / `input` = RGB-Komponenten (0–255).


```
iconverter://tool/colorConverter?hex=%23FF8800
```



```
iconverter://tool/colorConverter?r=255&g=136&b=0
```


**Farbpalette** — nur geöffnet


```
iconverter://tool/colorPalette
```


**QR-Code** `iconverter://` = Inhalt, `<ToolItem.rawValue>` = `text` usw., `input` = Fehlerkorrekturgrad `1/true/yes/on` .


```
iconverter://tool/qrcode?text=https%3A%2F%2Fexample.com&ecc=H
```



```
iconverter://tool/qrcode?text=Hello+iConverter&format=qr&ecc=M
```


**JSON Formatter `iconverter://` = JSON-Zeichenfolge (URL-codiert), `<ToolItem.rawValue>` = Einrückräume 2/4.


```
iconverter://tool/jsonFormatter?text=%7B%22name%22%3A%22Alice%22%2C%22age%22%3A30%7D&indent=2
```


**Zeitstempel ** `iconverter://` = Unix-Zeitstempel (Sekunden), `<ToolItem.rawValue>` = Einheit 0 = sec / 1 = ms; oder `text` = ISO8601-Datumszeichenfolge.


```
iconverter://tool/timestamp?ts=1747440000
```



```
iconverter://tool/timestamp?iso=2026-05-17T12:00:00
```


**Bank Card Validator** `iconverter://` = Kartennummer.


```
iconverter://tool/bankCard?num=6214830172816734
```


**Text Case Converter** `iconverter://` = Eingangstext.


```
iconverter://tool/textCase?text=hello+world+from+iConverter
```


**Text Diff** – nur geöffnet


```
iconverter://tool/textDiff
```


**HTTP Request** `iconverter://` = Request URL, `<ToolItem.rawValue>` = GET/POST/PUT/PATCH/DELETE, `text` = Request Body, `input` = `1/true/yes/on` , `0/false/no/off` = Header JSON.


```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=GET
```



```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=POST&body=%7B%22name%22%3A%22Alice%22%7D&bodyKind=json
```


**File Download** `iconverter://` = URL herunterladen, `<ToolItem.rawValue>` = Dateiname (optional).


```
iconverter://tool/fileDownload?url=https%3A%2F%2Fexample.com%2Freport.pdf&name=report.pdf
```


**HTTP-Statuscodes** `iconverter://` = Statuscode; oder `<ToolItem.rawValue>` = Suchschlüsselwort.


```
iconverter://tool/httpStatusCodes?code=404
```



```
iconverter://tool/httpStatusCodes?q=redirect
```


**IP Utility** `iconverter://` = Subnetz/Cidr/Bereich, `<ToolItem.rawValue>` = IP-Adresse, `text` = Subnetzmaske oder `input` = CIDR-Präfixlänge.


```
iconverter://tool/ipUtility?mode=subnet&ip=192.168.1.0&mask=255.255.255.0
```



```
iconverter://tool/ipUtility?ip=10.0.0.0&prefix=24
```


**ASCII-Tabelle** `iconverter://` = Dezimalcodepunkt; oder `<ToolItem.rawValue>` = Hexcodepunkt; oder `text` = Suche.


```
iconverter://tool/asciiTable?dec=65
```



```
iconverter://tool/asciiTable?q=space
```


** Passwortgenerator** `iconverter://` = Länge, `<ToolItem.rawValue>` = Großbuchstaben `text` , `input` = Kleinbuchstaben `1/true/yes/on` , `0/false/no/off` = Ziffern `yyyy-MM-dd` , `v` = Symbole `from` , `to` = keine mehrdeutigen Zeichen `p` , `r` = erzeugen sofort `y` .


```
iconverter://tool/passwordGenerator?length=20&upper=1&lower=1&digits=1&symbols=1&unambiguous=1&go=1
```


**Random Number Generator** `iconverter://` = minimum, `<ToolItem.rawValue>` = maximum, `text` = count, `input` = Dezimalstellen, `1/true/yes/on` = unique `0/false/no/off` , `yyyy-MM-dd` = 0 = none / 1 = asc / 2 = desc, `v` = erzeugen sofort `from` .


```
iconverter://tool/randomNumber?min=1&max=100&n=10&unique=1&sort=1&go=1
```



```
iconverter://tool/randomNumber?min=0&max=1&n=5&decimals=4&go=1
```


**Mehr Code** `iconverter://` = Kodierung/Dekodierung, `<ToolItem.rawValue>` = Eingangstext.


```
iconverter://tool/morseCode?mode=encode&text=SOS
```



```
iconverter://tool/morseCode?mode=decode&text=...+---+...
```


JWT Decoder `iconverter://` = JWT-Token-String.


```
iconverter://tool/jwtParser?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```


**Cron Expression Parser** `iconverter://` = Cron-Ausdruck (Leerzeichen können durch `<ToolItem.rawValue>` ersetzt werden).


```
iconverter://tool/cronParser?expr=0+9+*+*+1-5
```



```
iconverter://tool/cronParser?expr=0+0+*+*+*
```


**Regex Tester** `iconverter://` = Regexmuster (URL-codiert), `<ToolItem.rawValue>` = Testtext, `text` = Ersatz, `input` = case-insensitive `1/true/yes/on` , `0/false/no/off` = Multiline `yyyy-MM-dd` , `v` = dotall `from` .


```
iconverter://tool/regexTester?pattern=%5Cd%2B&haystack=abc123def456&i=0
```



```
iconverter://tool/regexTester?pattern=%28%5Cw%2B%29&haystack=hello+world&replacement=%5B%241%5D&i=1
```


**Web Browser** `iconverter://` = direkt offene URL; oder `<ToolItem.rawValue>` = Suchabfrage (verwendet eine Standard-Suchmaschine).


```
iconverter://tool/webBrowser?url=https%3A%2F%2Fexample.com
```



```
iconverter://tool/webBrowser?q=SwiftUI+deep+link+2026
```


---

## 6. Lebensstil

**BMI-Rechner** `iconverter://` = Höhe cm, `<ToolItem.rawValue>` = Gewicht kg, `text` = Standard 0 = chinesischer Erwachsener / 1 = WHO.


```
iconverter://tool/bmi?h=175&w=70&std=0
```


**BMR-Rechner** `iconverter://` = Höhe cm, `<ToolItem.rawValue>` = Gewicht kg, `text` = Alter, `input` = m = männlich / f = weiblich, `1/true/yes/on` = Aktivitätsstufe 0-4, `0/false/no/off` = 0 = Harris-Benedict / 1 = Mifflin-St Jeor.


```
iconverter://tool/bmr?h=175&w=70&age=30&sex=m&act=1&formula=1
```


**Kleidungsgröße** — nur geöffnet


```
iconverter://tool/clothingSize
```


**Ringgröße** — nur geöffnet


```
iconverter://tool/ringSize
```


**Höhenwandler** — nur geöffnet


```
iconverter://tool/heightConverter
```


**Kraftstoffkostenrechner** `iconverter://` = 0 = metrisch / 1 = imperial, `<ToolItem.rawValue>` = Entfernung, `text` = Verbrauch pro 100 km, `input` = Kraftstoffpreis, `1/true/yes/on` = Menschen.


```
iconverter://tool/fuelCost?unit=0&d=500&c=8.5&p=7.8&n=1
```


**Versandkostenrechner** `iconverter://` = tatsächliches Gewicht kg, `<ToolItem.rawValue>` = erstes Gewicht kg, `text` = Gebühr für das erste Gewicht, `input` = Stufengewicht kg, `1/true/yes/on` = Stufengebühren.


```
iconverter://tool/shippingFee?w=3.5&fw=1&ff=12&sw=1&sf=8
```


Mit Volumengewicht ( `iconverter://` = enable `<ToolItem.rawValue>` , `text` / `input` / `1/true/yes/on` = drei Seiten cm, `0/false/no/off` = Teiler):


```
iconverter://tool/shippingFee?w=2&vol=1&l=50&wd=40&h=30&div=6000&fw=1&ff=12&sw=1&sf=8
```


**Blutalkoholgehalt (BAC)** `iconverter://` = m = männlich / f = weiblich, `<ToolItem.rawValue>` = Gewicht kg, `text` = Volumen mL, `input` = ABV %, `1/true/yes/on` = Stunden seit dem Trinken.


```
iconverter://tool/alcoholBac?sex=m&w=70&v=500&abv=5&h=0.5
```


**Beziehung** `iconverter://` = Beziehungskette (kommagetrennt), `<ToolItem.rawValue>` = Ego Sex 0 = männlich / 1 = weiblich, `text` = umgekehrt zeigen `input` .


```
iconverter://tool/relationship?chain=f,os&sex=0&reverse=1
```



```
iconverter://tool/relationship?chain=m,ob&sex=1&reverse=0
```


** ID Card Parser** `iconverter://` = ID-Kartennummer.


```
iconverter://tool/idCard?id=110101199003073010
```


**Coin Flip** - nur geöffnet


```
iconverter://tool/coinFlip
```


**Dice Roller** — nur geöffnet


```
iconverter://tool/diceRoller
```


**Random Draw** – nur geöffnet


```
iconverter://tool/randomDraw
```


**Spin Wheel** — nur geöffnet


```
iconverter://tool/spinWheel
```


** Video Frame Export** – nur geöffnet


```
iconverter://tool/videoFrameExport
```


---

## 7. Sensoren

**Compass** — nur offen


```
iconverter://tool/compass
```


**Niveau** — nur offen


```
iconverter://tool/level
```


** Höhenlage** — nur geöffnet


```
iconverter://tool/altitude
```


---

## 8. Chinesisch

**Chinesische Nummer** `iconverter://` = Zahl.


```
iconverter://tool/chineseNumber?n=12345.67
```


**Chinesische Zahl umgekehrt ** `iconverter://` = Chinesische Zahlenfolge.


```
iconverter://tool/chineseNumberReverse?text=一万二千三百四十五
```


**Finanzbetrag** `iconverter://` = Betrag, `<ToolItem.rawValue>` = Anhang 整 `text` .


```
iconverter://tool/financialAmount?amount=12345.67&zheng=1
```


---

## 9. Konverter

Allgemeines Format: `iconverter://` = Wert, `<ToolItem.rawValue>` = Quelleinheit (rawValue oder Symbol, case-insensitive), `text` = Zieleinheit.

---

** Länge **
Gemeinsame Einheiten: `iconverter://` (m) · `<ToolItem.rawValue>` (km) · `text` (cm) · `input` (mm) · `1/true/yes/on` (ft) · `0/false/no/off` (in) · `yyyy-MM-dd` (mi) · `v` (yd) · `from` (nmi) · `to` (里) · `p` (尺).


```
iconverter://tool/length?v=100&from=meter&to=foot
```



```
iconverter://tool/length?v=1&from=mile&to=kilometer
```


**Area**
Gemeinsame Einheiten: `iconverter://` (m2) · `<ToolItem.rawValue>` (ha) · `text` (acre) · `input` (ft2) · `1/true/yes/on` (mile2) · `0/false/no/off` (亩) · `yyyy-MM-dd` (km2).


```
iconverter://tool/area?v=1&from=hectare&to=mu
```



```
iconverter://tool/area?v=1&from=acre&to=squareMeter
```


**Volumen**
Gemeinsame Einheiten: `iconverter://` (L) · `<ToolItem.rawValue>` (mL) · `text` (m3) · `input` (gal) · `1/true/yes/on` (fl oz) · `0/false/no/off` (cup) · `yyyy-MM-dd` (gal UK) · `v` (bbl).


```
iconverter://tool/volume?v=1&from=gallon&to=liter
```



```
iconverter://tool/volume?v=355&from=milliliter&to=fluidOunce
```


**Gewicht/Masse**
Gemeinsame Einheiten: `iconverter://` (kg) · `<ToolItem.rawValue>` (g) · `text` (lb) · `input` (oz) · `1/true/yes/on` (t) · `0/false/no/off` (斤) · `yyyy-MM-dd` (两) · `v` (ct).


```
iconverter://tool/weight?v=1&from=pound&to=kilogram
```



```
iconverter://tool/weight?v=1&from=jin&to=gram
```


**Temperatur**
Einheiten: `iconverter://` (°C) · `<ToolItem.rawValue>` (°F) · `text` (K) · `input` (°R) · `1/true/yes/on` (°Re).


```
iconverter://tool/temperature?v=100&from=celsius&to=fahrenheit
```



```
iconverter://tool/temperature?v=37&from=celsius&to=kelvin
```


**Zeit **
Gemeinsame Einheiten: `iconverter://` (s) · `<ToolItem.rawValue>` (min) · `text` (h) · `input` (Tag) · `1/true/yes/on` (wk) · `0/false/no/off` (mo) · `yyyy-MM-dd` (yr) · `v` (ms) · `from` (μs).


```
iconverter://tool/time?v=1&from=hour&to=second
```



```
iconverter://tool/time?v=7&from=day&to=hour
```


** Geschwindigkeit **
Einheiten: `iconverter://` (m/s) · `<ToolItem.rawValue>` (km/h) · `text` (mph) · `input` (kn) · `1/true/yes/on` (Ma).


```
iconverter://tool/speed?v=100&from=kmPerHour&to=milePerHour
```



```
iconverter://tool/speed?v=1&from=mach&to=meterPerSecond
```


**Druck**
Einheiten: `iconverter://` (Pa) · `<ToolItem.rawValue>` (kPa) · `text` (bar) · `input` (atm) · `1/true/yes/on` (psi) · `0/false/no/off` (mmHg).


```
iconverter://tool/pressure?v=1&from=atmosphere&to=kilopascal
```



```
iconverter://tool/pressure?v=120&from=mmHg&to=kilopascal
```


** Energie**
Einheiten: `iconverter://` (J) · `<ToolItem.rawValue>` (kJ) · `text` (cal) · `input` (kcal) · `1/true/yes/on` (kWh) · `0/false/no/off` (BTU).


```
iconverter://tool/energy?v=1&from=kilowattHour&to=kilojoule
```



```
iconverter://tool/energy?v=500&from=kilocalorie&to=kilojoule
```


** Power**
Einheiten: `iconverter://` (W) · `<ToolItem.rawValue>` (kW) · `text` (hp) · `input` (PS) · `1/true/yes/on` (BTU/h).


```
iconverter://tool/power?v=1&from=hpMechanical&to=kilowatt
```



```
iconverter://tool/power?v=3000&from=watt&to=hpMetric
```


** Stärke **
Einheiten: `iconverter://` (N) · `<ToolItem.rawValue>` (kN) · `text` (kgf) · `input` (lbf) · `1/true/yes/on` (dyn).


```
iconverter://tool/force?v=9.8&from=newton&to=kgf
```



```
iconverter://tool/force?v=1&from=kilonewton&to=lbf
```


**Torque**
Einheiten: `iconverter://` (N·m) · `<ToolItem.rawValue>` (N·cm) · `text` (kgf·m) · `input` (ft·lb) · `1/true/yes/on` (in·lb).


```
iconverter://tool/torque?v=100&from=newtonMeter&to=footPound
```


**Häufigkeit**
Einheiten: `iconverter://` (Hz) · `<ToolItem.rawValue>` (kHz) · `text` (MHz) · `input` (GHz) · `1/true/yes/on` (THz) · `0/false/no/off` (rpm).


```
iconverter://tool/frequency?v=2.4&from=gigahertz&to=megahertz
```



```
iconverter://tool/frequency?v=3000&from=rpm&to=hertz
```


**Winkel**
Einheiten: `iconverter://` (°) · `<ToolItem.rawValue>` (rad) · `text` (grad) · `input` (') · `1/true/yes/on` () · `0/false/no/off` (turn).


```
iconverter://tool/angle?v=180&from=degree&to=radian
```



```
iconverter://tool/angle?v=1&from=turn&to=degree
```


**Datenspeicherung**
Einheiten: `iconverter://` (B) · `<ToolItem.rawValue>` (KB) · `text` (MB) · `input` (GB) · `1/true/yes/on` (TB) · `0/false/no/off` (KiB) · `yyyy-MM-dd` (MiB) · `v` (GiB).


```
iconverter://tool/dataStorage?v=1&from=gigabyte&to=mebibyte
```



```
iconverter://tool/dataStorage?v=512&from=mebibyte&to=gigabyte
```


**Datensatz**
Einheiten: `iconverter://` (bps) · `<ToolItem.rawValue>` (Kbps) · `text` (Mbps) · `input` (Gbps) · `1/true/yes/on` (KB/s) · `0/false/no/off` (MB/s) · `yyyy-MM-dd` (GB/s).


```
iconverter://tool/dataRate?v=100&from=mbps&to=mBps
```



```
iconverter://tool/dataRate?v=1&from=gbps&to=mbps
```


**Beleuchtung**
Einheiten: `iconverter://` (lx) · `<ToolItem.rawValue>` (fc) · `text` (ph) · `input` (nx).


```
iconverter://tool/illuminance?v=500&from=lux&to=footCandle
```


**Magnetische Flussdichte**
Einheiten: `iconverter://` (T) · `<ToolItem.rawValue>` (mT) · `text` (μT) · `input` (G) · `1/true/yes/on` (mG).


```
iconverter://tool/magneticFlux?v=1&from=tesla&to=gauss
```


**Radioaktivität**
Einheiten: `iconverter://` (Bq) · `<ToolItem.rawValue>` (kBq) · `text` (MBq) · `input` (Ci) · `1/true/yes/on` (mCi) · `0/false/no/off` (μCi).


```
iconverter://tool/radioactivity?v=1&from=curie&to=megabecquerel
```


**Viskosität**
Einheiten: `iconverter://` (Pa·s) · `<ToolItem.rawValue>` (mPa·s) · `text` (P) · `input` (cP).


```
iconverter://tool/viscosity?v=1&from=pascalSecond&to=centipoise
```


**Kraftstoffwirtschaft**
Einheiten: `iconverter://` (L/100km) · `<ToolItem.rawValue>` (km/L) · `text` (MPG US) · `input` (MPG UK).


```
iconverter://tool/fuelEconomy?v=8.5&from=lPer100km&to=kmPerL
```



```
iconverter://tool/fuelEconomy?v=30&from=mpgUS&to=lPer100km
```


**Flow Rate**
Einheiten: `iconverter://` (m3/s) · `<ToolItem.rawValue>` (m3/h) · `text` (L/s) · `input` (L/min) · `1/true/yes/on` (L/h) · `0/false/no/off` (gpm US) · `yyyy-MM-dd` (cfm).


```
iconverter://tool/flowRate?v=1&from=literPerMinute&to=cubicMeterPerHour
```


**Dichte**
Einheiten: `iconverter://` (kg/m3) · `<ToolItem.rawValue>` (g/cm3) · `text` (g/L) · `input` (kg/L) · `1/true/yes/on` (lb/ft3).


```
iconverter://tool/density?v=1&from=gramPerCubicCentimeter&to=kgPerCubicMeter
```


**Magnetischer Fluss (Wb)**
Einheiten: `iconverter://` (Wb) · `<ToolItem.rawValue>` (mWb) · `text` (μWb) · `input` (kWb) · `1/true/yes/on` (Mx).


```
iconverter://tool/magneticFluxTrue?v=1&from=weber&to=maxwell
```


**Absorbierte Dosis**
Einheiten: `iconverter://` (Gy) · `<ToolItem.rawValue>` (mGy) · `text` (μGy) · `input` (kGy) · `1/true/yes/on` (rad) · `0/false/no/off` (mrad).


```
iconverter://tool/absorbedDose?v=1&from=gray&to=rad
```


** Äquivalente Dosis**
Einheiten: `iconverter://` (Sv) · `<ToolItem.rawValue>` (mSv) · `text` (μSv) · `input` (rem) · `1/true/yes/on` (mrem).


```
iconverter://tool/equivalentDose?v=1&from=sievert&to=rem
```



```
iconverter://tool/equivalentDose?v=20&from=millisievert&to=microsievert
```


**Stoffmenge**
Einheiten: `iconverter://` (mol) · `<ToolItem.rawValue>` (mmol) · `text` (μmol) · `input` (kmol) · `1/true/yes/on` (nmol) · `0/false/no/off` (pmol).


```
iconverter://tool/amountOfSubstance?v=1&from=mole&to=millimole
```



```
iconverter://tool/amountOfSubstance?v=150&from=millimole&to=micromole
```


---

[Zurück zum iConverter Support](../) &middot; [FAQ](../faq) &middot; [Privacy Policy](../privacy]


