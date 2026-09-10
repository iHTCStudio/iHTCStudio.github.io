---
layout: doc
title: iConverter — URL Scheme Reference
app_id: iConverter
doc_title_en: URL Scheme Reference
doc_title_zh_cn: URL Scheme 深度链接文档
doc_title_zh_tw: URL Scheme 深度連結文件
description: Complete reference of iconverter:// deep links supported by iConverter.
---

<section lang="en" markdown="1">

iConverter supports `iconverter://` URL scheme deep links — open any of the 98 tools from external apps, web pages, QR codes (generate or **scan in-app**), Safari, or Apple Shortcuts, optionally pre-filling input fields via query parameters.

> **Widget note:** The **Launcher** widget tool picker includes all supported tools except **Web Browser**. Widget configuration UI follows **iOS system language**, not the in-app language override under Settings.

## Protocol Specification

```
iconverter://tool/<ToolItem.rawValue>?key=value&key2=value2
```

- `<ToolItem.rawValue>` shares the same naming as widget deep links.
- Parameter names support both short keys and synonymous aliases (e.g. `text` is equivalent to `input`).
- Booleans: `1/true/yes/on` → true; `0/false/no/off` → false.
- Dates: supports `yyyy-MM-dd`, ISO8601, Unix timestamp (seconds).
- Unit converters share a common format: `v` = value, `from` = source unit (rawValue or symbol, case-insensitive), `to` = target unit.

---

## 1. Calculator

**Calculator** — open only

```
iconverter://tool/calculator
```

**Scientific Calculator** — open only

```
iconverter://tool/scientific
```

**Programmer Calculator** — open only

```
iconverter://tool/programmer
```

---

## 2. Finance

**Mortgage Calculator**
`p` = loan amount, `r` = annual rate %, `y` = years, `mode` = 0 = equal installment / 1 = equal principal.

```
iconverter://tool/mortgage?p=1000000&r=3.7&y=30&mode=0
```

**Income Tax**
`salary` = monthly salary, `insurance` = social insurance, `deduction` = special deduction, `threshold` = threshold, `bonus` = annual bonus.

```
iconverter://tool/incomeTax?salary=20000&insurance=3000&deduction=1000&threshold=5000&bonus=50000
```

**Compound Interest**
`p` = principal, `m` = monthly contribution, `r` = annual rate %, `y` = years, `freq` = 0 = annual / 1 = monthly / 2 = daily, `i` = inflation %.

```
iconverter://tool/compoundInterest?p=100000&m=1000&r=7&y=10&freq=1
```

**Discount Calculator**
`mode` = 0–4, `p` = original price, `r` = discount ratio, `t` = threshold, `u` = reduction amount.

```
iconverter://tool/discount?mode=0&p=299&r=8.5
```

Full-minus example:

```
iconverter://tool/discount?mode=3&p=350&t=300&u=50
```

**Tip & AA Split**
`mode` = 0 = tip / 1 = AA split, `bill` = bill, `tip` = tip %, `tax` = tax %, `ppl` = people count.

```
iconverter://tool/tipAA?mode=0&bill=200&tip=15&tax=0&ppl=4
```

**Mortgage Prepayment**
`p` = original loan, `r` = annual rate %, `total` = total term (years), `paid` = paid terms, `prepay` = prepay amount, `mode` = 0 = shorten / 1 = reduce monthly / 2 = compare.

```
iconverter://tool/mortgagePrepay?p=800000&r=3.7&total=30&paid=5&prepay=100000&mode=2
```

**Real Estate Tax** — open only

```
iconverter://tool/realEstateTax
```

---

## 3. Date & Time

**Age & Anniversary**
`birth` = birthday `yyyy-MM-dd`, `ref` = reference date.

```
iconverter://tool/ageAnniversary?birth=1990-05-01&ref=2026-05-17
```

**Date Arithmetic**
`mode` = 0 = add/subtract / 1 = date difference.

Add-subtract mode (`d1` = start date, `d` = ± days, `w` = ± weeks, `mo` = ± months, `y` = ± years):

```
iconverter://tool/dateArithmetic?mode=0&d1=2026-05-17&d=100
```

Difference mode (`d1` = date 1, `d2` = date 2):

```
iconverter://tool/dateArithmetic?mode=1&d1=2026-01-01&d2=2026-12-31
```

**Lunar Calendar**
`date` = Gregorian date `yyyy-MM-dd`.

```
iconverter://tool/lunarCalendar?date=2026-05-17
```

**Solar Terms** — open only

```
iconverter://tool/solarTerms
```

**Countdown**
`label` = event name, `target` = target date `yyyy-MM-dd`, `time` = include time `0/1`.

```
iconverter://tool/countdown?label=Holiday&target=2026-10-01&time=0
```

**Pregnancy Calculator**
`method` = 0 = LMP / 1 = conception / 2 = IVF, `ref` = reference date, `ivf` = IVF embryo day 0 = D3 / 1 = D5.

```
iconverter://tool/pregnancy?method=0&ref=2026-03-01
```

```
iconverter://tool/pregnancy?method=2&ref=2026-03-15&ivf=1
```

**Menstrual Cycle**
`lmp` = last menstrual period date, `cycle` = cycle days, `period` = period days.

```
iconverter://tool/menstrual?lmp=2026-05-01&cycle=28&period=5
```

**World Clock**
`q` = city search keyword, `now` = use current time `0/1`, `ref` = custom datetime.

```
iconverter://tool/worldClock?q=Tokyo
```

```
iconverter://tool/worldClock?now=0&ref=2026-05-17T20:00:00
```

**Zodiac** — open only

```
iconverter://tool/zodiac
```

---

## 4. Math

**Percentage Calculator**
`mode` = 0–4, `a` = value A, `b` = value B.

```
iconverter://tool/percentage?mode=0&a=75&b=120
```

**Fraction Calculator** — open only

```
iconverter://tool/fraction
```

**Prime Factorization** — open only

```
iconverter://tool/primeFactor
```

**Quadratic Solver** — open only

```
iconverter://tool/quadraticSolver
```

**Statistics**
`data` = dataset, separated by space / comma / semicolon.

```
iconverter://tool/statistics?data=1,2,3,4,5,6,7,8,9,10
```

**Combinations & Permutations** — open only

```
iconverter://tool/combinations
```

**Geometry**
`shape` = shape, `v1` / `v2` / `v3` = dimension parameters.

Available shapes: `rectangle` · `square` · `circle` · `triangle` · `triangleSSS` · `parallelogram` · `trapezoid` · `sector` · `ellipse` · `regularPolygon` · `sphere` · `hemisphere` · `cylinder` · `cone` · `frustum` · `cube` · `cuboid`.

Circle (`v1` = radius):

```
iconverter://tool/geometry?shape=circle&v1=5
```

Rectangle (`v1` = length, `v2` = width):

```
iconverter://tool/geometry?shape=rectangle&v1=10&v2=5
```

Sphere (`v1` = radius):

```
iconverter://tool/geometry?shape=sphere&v1=3
```

Cylinder (`v1` = radius, `v2` = height):

```
iconverter://tool/geometry?shape=cylinder&v1=4&v2=10
```

---

## 5. Encoding

**Roman Numeral**
`n` = Arabic number (1–3999); or `roman` = Roman numeral string.

```
iconverter://tool/roman?n=2026
```

```
iconverter://tool/roman?roman=MMXXVI
```

**Base64 Encoder / Decoder**
`mode` = encode/decode, `urlSafe` = URL-safe mode `0/1`, `text` = input text.

```
iconverter://tool/base64?mode=encode&text=Hello%2C+World!
```

```
iconverter://tool/base64?mode=decode&urlSafe=0&text=SGVsbG8sIFdvcmxkIQ%3D%3D
```

**URL Encoder / Decoder**
`mode` = encode/decode, `comp` = component mode 0 = full / 1 = query / 2 = path, `text` = input.

```
iconverter://tool/urlCoder?mode=encode&comp=0&text=https://example.com/path?q=hello world
```

```
iconverter://tool/urlCoder?mode=decode&text=https%3A%2F%2Fexample.com%2F%3Fq%3Dhello%20world
```

**Hash Calculator**
`text` = input, `algo` = md5/sha1/sha256/sha512, `upper` = uppercase `0/1`, `hmac` = enable HMAC `0/1`, `key` = HMAC key.

```
iconverter://tool/hashing?text=Hello+World&algo=sha256&upper=0
```

```
iconverter://tool/hashing?text=data&algo=md5&hmac=1&key=secret
```

**Word Count**
`text` = text to analyze.

```
iconverter://tool/wordCount?text=The+quick+brown+fox+jumps+over+the+lazy+dog.
```

**Color Converter**
`hex` = hex color; or `r` / `g` / `b` = RGB components (0–255).

```
iconverter://tool/colorConverter?hex=%23FF8800
```

```
iconverter://tool/colorConverter?r=255&g=136&b=0
```

**Color Palette** — open only

```
iconverter://tool/colorPalette
```

**QR Code**
`text` = content, `format` = `qr/aztec/code128/pdf417` etc., `ecc` = error correction level `L/M/Q/H`.

```
iconverter://tool/qrcode?text=https%3A%2F%2Fexample.com&ecc=H
```

```
iconverter://tool/qrcode?text=Hello+iConverter&format=qr&ecc=M
```

**JSON Formatter**
`text` = JSON string (URL-encoded), `indent` = indent spaces 2/4.

```
iconverter://tool/jsonFormatter?text=%7B%22name%22%3A%22Alice%22%2C%22age%22%3A30%7D&indent=2
```

**Timestamp**
`ts` = Unix timestamp (seconds), `u` = unit 0 = sec / 1 = ms; or `iso` = ISO8601 date string.

```
iconverter://tool/timestamp?ts=1747440000
```

```
iconverter://tool/timestamp?iso=2026-05-17T12:00:00
```

**Bank Card Validator**
`num` = card number.

```
iconverter://tool/bankCard?num=6214830172816734
```

**Text Case Converter**
`text` = input text.

```
iconverter://tool/textCase?text=hello+world+from+iConverter
```

**Text Diff** — open only

```
iconverter://tool/textDiff
```

**HTTP Request**
`url` = request URL, `method` = GET/POST/PUT/PATCH/DELETE, `body` = request body, `bodyKind` = `json/form/text`, `headers` = headers JSON.

```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=GET
```

```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=POST&body=%7B%22name%22%3A%22Alice%22%7D&bodyKind=json
```

**File Download**
`url` = download URL, `name` = filename (optional).

```
iconverter://tool/fileDownload?url=https%3A%2F%2Fexample.com%2Freport.pdf&name=report.pdf
```

**HTTP Status Codes**
`code` = status code; or `q` = search keyword.

```
iconverter://tool/httpStatusCodes?code=404
```

```
iconverter://tool/httpStatusCodes?q=redirect
```

**IP Utility**
`mode` = subnet/cidr/range, `ip` = IP address, `mask` = subnet mask; or `prefix` = CIDR prefix length.

```
iconverter://tool/ipUtility?mode=subnet&ip=192.168.1.0&mask=255.255.255.0
```

```
iconverter://tool/ipUtility?ip=10.0.0.0&prefix=24
```

**ASCII Table**
`dec` = decimal codepoint; or `hex` = hex codepoint; or `q` = search.

```
iconverter://tool/asciiTable?dec=65
```

```
iconverter://tool/asciiTable?q=space
```

**Password Generator**
`length` = length, `upper` = uppercase `0/1`, `lower` = lowercase `0/1`, `digits` = digits `0/1`, `symbols` = symbols `0/1`, `unambiguous` = no ambiguous chars `0/1`, `go` = generate immediately `1`.

```
iconverter://tool/passwordGenerator?length=20&upper=1&lower=1&digits=1&symbols=1&unambiguous=1&go=1
```

**Random Number Generator**
`min` = minimum, `max` = maximum, `n` = count, `decimals` = decimal places, `unique` = unique `0/1`, `sort` = 0 = none / 1 = asc / 2 = desc, `go` = generate immediately `1`.

```
iconverter://tool/randomNumber?min=1&max=100&n=10&unique=1&sort=1&go=1
```

```
iconverter://tool/randomNumber?min=0&max=1&n=5&decimals=4&go=1
```

**Morse Code**
`mode` = encode/decode, `text` = input text.

```
iconverter://tool/morseCode?mode=encode&text=SOS
```

```
iconverter://tool/morseCode?mode=decode&text=...+---+...
```

**JWT Decoder**
`token` = JWT token string.

```
iconverter://tool/jwtParser?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

**Cron Expression Parser**
`expr` = Cron expression (spaces can be replaced with `+`).

```
iconverter://tool/cronParser?expr=0+9+*+*+1-5
```

```
iconverter://tool/cronParser?expr=0+0+*+*+*
```

**Regex Tester**
`pattern` = regex pattern (URL-encoded), `haystack` = test text, `replacement` = replacement, `i` = case-insensitive `0/1`, `m` = multiline `0/1`, `s` = dotall `0/1`.

```
iconverter://tool/regexTester?pattern=%5Cd%2B&haystack=abc123def456&i=0
```

```
iconverter://tool/regexTester?pattern=%28%5Cw%2B%29&haystack=hello+world&replacement=%5B%241%5D&i=1
```

**Web Browser**
`url` = open URL directly; or `q` = search query (uses default search engine).

```
iconverter://tool/webBrowser?url=https%3A%2F%2Fexample.com
```

```
iconverter://tool/webBrowser?q=SwiftUI+deep+link+2026
```

---

## 6. Lifestyle

**BMI Calculator**
`h` = height cm, `w` = weight kg, `std` = standard 0 = Chinese adult / 1 = WHO.

```
iconverter://tool/bmi?h=175&w=70&std=0
```

**BMR Calculator**
`h` = height cm, `w` = weight kg, `age` = age, `sex` = m = male / f = female, `act` = activity level 0–4, `formula` = 0 = Harris-Benedict / 1 = Mifflin-St Jeor.

```
iconverter://tool/bmr?h=175&w=70&age=30&sex=m&act=1&formula=1
```

**Clothing Size** — open only

```
iconverter://tool/clothingSize
```

**Ring Size** — open only

```
iconverter://tool/ringSize
```

**Height Converter** — open only

```
iconverter://tool/heightConverter
```

**Fuel Cost Calculator**
`unit` = 0 = metric / 1 = imperial, `d` = distance, `c` = consumption per 100 km, `p` = fuel price, `n` = people.

```
iconverter://tool/fuelCost?unit=0&d=500&c=8.5&p=7.8&n=1
```

**Shipping Fee Calculator**
`w` = actual weight kg, `fw` = first weight kg, `ff` = first-weight fee, `sw` = step weight kg, `sf` = step fee.

```
iconverter://tool/shippingFee?w=3.5&fw=1&ff=12&sw=1&sf=8
```

With volumetric weight (`vol` = enable `0/1`, `l` / `wd` / `h` = three sides cm, `div` = divisor):

```
iconverter://tool/shippingFee?w=2&vol=1&l=50&wd=40&h=30&div=6000&fw=1&ff=12&sw=1&sf=8
```

**Blood Alcohol Content (BAC)**
`sex` = m = male / f = female, `w` = weight kg, `v` = volume mL, `abv` = ABV %, `h` = hours since drinking.

```
iconverter://tool/alcoholBac?sex=m&w=70&v=500&abv=5&h=0.5
```

**Relationship**
`chain` = relationship chain (comma-separated), `sex` = ego sex 0 = male / 1 = female, `reverse` = show reverse `0/1`.

```
iconverter://tool/relationship?chain=f,os&sex=0&reverse=1
```

```
iconverter://tool/relationship?chain=m,ob&sex=1&reverse=0
```

**ID Card Parser**
`id` = ID card number.

```
iconverter://tool/idCard?id=110101199003073010
```

**Coin Flip** — open only

```
iconverter://tool/coinFlip
```

**Dice Roller** — open only

```
iconverter://tool/diceRoller
```

**Random Draw** — open only

```
iconverter://tool/randomDraw
```

**Spin Wheel** — open only

```
iconverter://tool/spinWheel
```

**Video Frame Export** — open only

```
iconverter://tool/videoFrameExport
```

---

## 7. Sensors

**Compass** — open only

```
iconverter://tool/compass
```

**Level** — open only

```
iconverter://tool/level
```

**Altitude** — open only

```
iconverter://tool/altitude
```

---

## 8. Chinese

**Chinese Number**
`n` = number.

```
iconverter://tool/chineseNumber?n=12345.67
```

**Chinese Number Reverse**
`text` = Chinese numeral string.

```
iconverter://tool/chineseNumberReverse?text=一万二千三百四十五
```

**Financial Amount**
`amount` = amount, `zheng` = append 整 `0/1`.

```
iconverter://tool/financialAmount?amount=12345.67&zheng=1
```

---

## 9. Unit Converters

General format: `v` = value, `from` = source unit (rawValue or symbol, case-insensitive), `to` = target unit.

---

**Length**
Common units: `meter` (m) · `kilometer` (km) · `centimeter` (cm) · `millimeter` (mm) · `foot` (ft) · `inch` (in) · `mile` (mi) · `yard` (yd) · `nauticalMile` (nmi) · `chineseLi` (里) · `chineseChi` (尺).

```
iconverter://tool/length?v=100&from=meter&to=foot
```

```
iconverter://tool/length?v=1&from=mile&to=kilometer
```

**Area**
Common units: `squareMeter` (m²) · `hectare` (ha) · `acre` (acre) · `squareFoot` (ft²) · `squareMile` (mile²) · `mu` (亩) · `squareKilometer` (km²).

```
iconverter://tool/area?v=1&from=hectare&to=mu
```

```
iconverter://tool/area?v=1&from=acre&to=squareMeter
```

**Volume**
Common units: `liter` (L) · `milliliter` (mL) · `cubicMeter` (m³) · `gallon` (gal) · `fluidOunce` (fl oz) · `cup` (cup) · `ukGallon` (gal UK) · `oilBarrel` (bbl).

```
iconverter://tool/volume?v=1&from=gallon&to=liter
```

```
iconverter://tool/volume?v=355&from=milliliter&to=fluidOunce
```

**Weight / Mass**
Common units: `kilogram` (kg) · `gram` (g) · `pound` (lb) · `ounce` (oz) · `tonne` (t) · `jin` (斤) · `liang` (两) · `carat` (ct).

```
iconverter://tool/weight?v=1&from=pound&to=kilogram
```

```
iconverter://tool/weight?v=1&from=jin&to=gram
```

**Temperature**
Units: `celsius` (°C) · `fahrenheit` (°F) · `kelvin` (K) · `rankine` (°R) · `reaumur` (°Re).

```
iconverter://tool/temperature?v=100&from=celsius&to=fahrenheit
```

```
iconverter://tool/temperature?v=37&from=celsius&to=kelvin
```

**Time**
Common units: `second` (s) · `minute` (min) · `hour` (h) · `day` (day) · `week` (wk) · `month` (mo) · `year` (yr) · `millisecond` (ms) · `microsecond` (μs).

```
iconverter://tool/time?v=1&from=hour&to=second
```

```
iconverter://tool/time?v=7&from=day&to=hour
```

**Speed**
Units: `meterPerSecond` (m/s) · `kmPerHour` (km/h) · `milePerHour` (mph) · `knot` (kn) · `mach` (Ma).

```
iconverter://tool/speed?v=100&from=kmPerHour&to=milePerHour
```

```
iconverter://tool/speed?v=1&from=mach&to=meterPerSecond
```

**Pressure**
Units: `pascal` (Pa) · `kilopascal` (kPa) · `bar` (bar) · `atmosphere` (atm) · `psi` (psi) · `mmHg` (mmHg).

```
iconverter://tool/pressure?v=1&from=atmosphere&to=kilopascal
```

```
iconverter://tool/pressure?v=120&from=mmHg&to=kilopascal
```

**Energy**
Units: `joule` (J) · `kilojoule` (kJ) · `calorie` (cal) · `kilocalorie` (kcal) · `kilowattHour` (kWh) · `btu` (BTU).

```
iconverter://tool/energy?v=1&from=kilowattHour&to=kilojoule
```

```
iconverter://tool/energy?v=500&from=kilocalorie&to=kilojoule
```

**Power**
Units: `watt` (W) · `kilowatt` (kW) · `hpMechanical` (hp) · `hpMetric` (PS) · `btuPerHour` (BTU/h).

```
iconverter://tool/power?v=1&from=hpMechanical&to=kilowatt
```

```
iconverter://tool/power?v=3000&from=watt&to=hpMetric
```

**Force**
Units: `newton` (N) · `kilonewton` (kN) · `kgf` (kgf) · `lbf` (lbf) · `dyne` (dyn).

```
iconverter://tool/force?v=9.8&from=newton&to=kgf
```

```
iconverter://tool/force?v=1&from=kilonewton&to=lbf
```

**Torque**
Units: `newtonMeter` (N·m) · `newtonCentimeter` (N·cm) · `kgfMeter` (kgf·m) · `footPound` (ft·lb) · `inchPound` (in·lb).

```
iconverter://tool/torque?v=100&from=newtonMeter&to=footPound
```

**Frequency**
Units: `hertz` (Hz) · `kilohertz` (kHz) · `megahertz` (MHz) · `gigahertz` (GHz) · `terahertz` (THz) · `rpm` (rpm).

```
iconverter://tool/frequency?v=2.4&from=gigahertz&to=megahertz
```

```
iconverter://tool/frequency?v=3000&from=rpm&to=hertz
```

**Angle**
Units: `degree` (°) · `radian` (rad) · `gradian` (grad) · `arcminute` (') · `arcsecond` (") · `turn` (turn).

```
iconverter://tool/angle?v=180&from=degree&to=radian
```

```
iconverter://tool/angle?v=1&from=turn&to=degree
```

**Data Storage**
Units: `byte` (B) · `kilobyte` (KB) · `megabyte` (MB) · `gigabyte` (GB) · `terabyte` (TB) · `kibibyte` (KiB) · `mebibyte` (MiB) · `gibibyte` (GiB).

```
iconverter://tool/dataStorage?v=1&from=gigabyte&to=mebibyte
```

```
iconverter://tool/dataStorage?v=512&from=mebibyte&to=gigabyte
```

**Data Rate**
Units: `bps` (bps) · `kbps` (Kbps) · `mbps` (Mbps) · `gbps` (Gbps) · `kBps` (KB/s) · `mBps` (MB/s) · `gBps` (GB/s).

```
iconverter://tool/dataRate?v=100&from=mbps&to=mBps
```

```
iconverter://tool/dataRate?v=1&from=gbps&to=mbps
```

**Illuminance**
Units: `lux` (lx) · `footCandle` (fc) · `phot` (ph) · `nox` (nx).

```
iconverter://tool/illuminance?v=500&from=lux&to=footCandle
```

**Magnetic Flux Density**
Units: `tesla` (T) · `millitesla` (mT) · `microtesla` (μT) · `gauss` (G) · `milligauss` (mG).

```
iconverter://tool/magneticFlux?v=1&from=tesla&to=gauss
```

**Radioactivity**
Units: `becquerel` (Bq) · `kilobecquerel` (kBq) · `megabecquerel` (MBq) · `curie` (Ci) · `millicurie` (mCi) · `microcurie` (μCi).

```
iconverter://tool/radioactivity?v=1&from=curie&to=megabecquerel
```

**Viscosity**
Units: `pascalSecond` (Pa·s) · `millipascalSecond` (mPa·s) · `poise` (P) · `centipoise` (cP).

```
iconverter://tool/viscosity?v=1&from=pascalSecond&to=centipoise
```

**Fuel Economy**
Units: `lPer100km` (L/100km) · `kmPerL` (km/L) · `mpgUS` (MPG US) · `mpgUK` (MPG UK).

```
iconverter://tool/fuelEconomy?v=8.5&from=lPer100km&to=kmPerL
```

```
iconverter://tool/fuelEconomy?v=30&from=mpgUS&to=lPer100km
```

**Flow Rate**
Units: `cubicMeterPerSecond` (m³/s) · `cubicMeterPerHour` (m³/h) · `literPerSecond` (L/s) · `literPerMinute` (L/min) · `literPerHour` (L/h) · `usGallonPerMinute` (gpm US) · `cubicFootPerMinute` (cfm).

```
iconverter://tool/flowRate?v=1&from=literPerMinute&to=cubicMeterPerHour
```

**Density**
Units: `kgPerCubicMeter` (kg/m³) · `gramPerCubicCentimeter` (g/cm³) · `gramPerLiter` (g/L) · `kgPerLiter` (kg/L) · `poundPerCubicFoot` (lb/ft³).

```
iconverter://tool/density?v=1&from=gramPerCubicCentimeter&to=kgPerCubicMeter
```

**Magnetic Flux (Wb)**
Units: `weber` (Wb) · `milliweber` (mWb) · `microweber` (μWb) · `kiloweber` (kWb) · `maxwell` (Mx).

```
iconverter://tool/magneticFluxTrue?v=1&from=weber&to=maxwell
```

**Absorbed Dose**
Units: `gray` (Gy) · `milligray` (mGy) · `microgray` (μGy) · `kilogray` (kGy) · `rad` (rad) · `millirad` (mrad).

```
iconverter://tool/absorbedDose?v=1&from=gray&to=rad
```

**Equivalent Dose**
Units: `sievert` (Sv) · `millisievert` (mSv) · `microsievert` (μSv) · `rem` (rem) · `millirem` (mrem).

```
iconverter://tool/equivalentDose?v=1&from=sievert&to=rem
```

```
iconverter://tool/equivalentDose?v=20&from=millisievert&to=microsievert
```

**Amount of Substance**
Units: `mole` (mol) · `millimole` (mmol) · `micromole` (μmol) · `kilomole` (kmol) · `nanomole` (nmol) · `picomole` (pmol).

```
iconverter://tool/amountOfSubstance?v=1&from=mole&to=millimole
```

```
iconverter://tool/amountOfSubstance?v=150&from=millimole&to=micromole
```

---

[Back to iConverter Support](./) &middot; [FAQ](faq) &middot; [Privacy Policy](privacy)

</section>

<section lang="zh-CN" markdown="1">

爱计算（iConverter）支持 `iconverter://` URL Scheme 深度链接——可从其他应用、网页、二维码（QR Code 工具内 **生成或扫描**）、Safari 或苹果快捷指令打开全部 98 个工具，并通过查询参数预填输入框。

> **小组件配置：** iOS 添加/编辑小组件时的工具选择器跟随 **设备系统语言**。**设置 → 语言** 中的 App 内语言不会改变小组件配置界面。

## 协议规范

```
iconverter://tool/<ToolItem.rawValue>?key=value&key2=value2
```

- `<ToolItem.rawValue>` 与小组件深度链接共用同一套命名。
- 参数键名支持短键与同义别名二选一，例如 `text` 与 `input` 等效。
- 布尔参数：`1/true/yes/on` → true；`0/false/no/off` → false。
- 日期参数：支持 `yyyy-MM-dd`、ISO8601、Unix 时间戳（秒）。
- 单位换算通用：`v` = 数值，`from` = 源单位（rawValue 或 symbol，大小写不敏感），`to` = 目标单位。

---

## 1. 计算器

**标准计算器** — 仅打开

```
iconverter://tool/calculator
```

**科学计算器** — 仅打开

```
iconverter://tool/scientific
```

**程序员计算器** — 仅打开

```
iconverter://tool/programmer
```

---

## 2. 财务

**房贷计算器**
`p` = 贷款金额，`r` = 年利率 %，`y` = 年数，`mode` = 还款方式 0 = 等额本息 / 1 = 等额本金。

```
iconverter://tool/mortgage?p=1000000&r=3.7&y=30&mode=0
```

**个人所得税**
`salary` = 月工资，`insurance` = 社保公积金，`deduction` = 专项扣除，`threshold` = 起征点，`bonus` = 年终奖。

```
iconverter://tool/incomeTax?salary=20000&insurance=3000&deduction=1000&threshold=5000&bonus=50000
```

**复利计算**
`p` = 本金，`m` = 月定投，`r` = 年利率 %，`y` = 年数，`freq` = 复利频率 0 = 年 / 1 = 月 / 2 = 日，`i` = 通胀率 %。

```
iconverter://tool/compoundInterest?p=100000&m=1000&r=7&y=10&freq=1
```

**折扣计算**
`mode` = 模式 0–4，`p` = 原价，`r` = 折扣率，`t` = 满减门槛，`u` = 减免金额。

```
iconverter://tool/discount?mode=0&p=299&r=8.5
```

满减示例：

```
iconverter://tool/discount?mode=3&p=350&t=300&u=50
```

**小费 / AA**
`mode` = 0 = 小费 / 1 = AA，`bill` = 账单，`tip` = 小费 %，`tax` = 税率 %，`ppl` = 人数。

```
iconverter://tool/tipAA?mode=0&bill=200&tip=15&tax=0&ppl=4
```

**提前还款**
`p` = 原贷款额，`r` = 年利率 %，`total` = 总期数（年），`paid` = 已还期数，`prepay` = 提前还款额，`mode` = 方案 0 = 缩期 / 1 = 减月供 / 2 = 对比。

```
iconverter://tool/mortgagePrepay?p=800000&r=3.7&total=30&paid=5&prepay=100000&mode=2
```

**二手房税费** — 仅打开

```
iconverter://tool/realEstateTax
```

---

## 3. 日期时间

**年龄 / 纪念日**
`birth` = 生日 `yyyy-MM-dd`，`ref` = 参考日期。

```
iconverter://tool/ageAnniversary?birth=1990-05-01&ref=2026-05-17
```

**日期计算**
`mode` = 0 = 日期加减 / 1 = 两日期差。

加减模式（`d1` = 起始日期，`d` = ± 天数，`w` = ± 周，`mo` = ± 月，`y` = ± 年）：

```
iconverter://tool/dateArithmetic?mode=0&d1=2026-05-17&d=100
```

差值模式（`d1` = 日期 1，`d2` = 日期 2）：

```
iconverter://tool/dateArithmetic?mode=1&d1=2026-01-01&d2=2026-12-31
```

**农历查询**
`date` = 公历日期 `yyyy-MM-dd`。

```
iconverter://tool/lunarCalendar?date=2026-05-17
```

**节气** — 仅打开

```
iconverter://tool/solarTerms
```

**倒计时**
`label` = 事件名，`target` = 目标日期 `yyyy-MM-dd`，`time` = 含时分 `0/1`。

```
iconverter://tool/countdown?label=Holiday&target=2026-10-01&time=0
```

**孕期计算**
`method` = 方式 0 = 末次月经 / 1 = 受孕日 / 2 = IVF，`ref` = 日期，`ivf` = IVF 胚胎天数 0 = D3 / 1 = D5。

```
iconverter://tool/pregnancy?method=0&ref=2026-03-01
```

```
iconverter://tool/pregnancy?method=2&ref=2026-03-15&ivf=1
```

**月经周期**
`lmp` = 末次月经日期，`cycle` = 周期天数，`period` = 行经天数。

```
iconverter://tool/menstrual?lmp=2026-05-01&cycle=28&period=5
```

**世界时钟**
`q` = 城市搜索关键词，`now` = 使用当前时间 `0/1`，`ref` = 自定义时间。

```
iconverter://tool/worldClock?q=Tokyo
```

```
iconverter://tool/worldClock?now=0&ref=2026-05-17T20:00:00
```

**星座** — 仅打开

```
iconverter://tool/zodiac
```

---

## 4. 数学

**百分比计算**
`mode` = 模式 0–4，`a` = 数值 A，`b` = 数值 B。

```
iconverter://tool/percentage?mode=0&a=75&b=120
```

**分数计算** — 仅打开

```
iconverter://tool/fraction
```

**质因数分解** — 仅打开

```
iconverter://tool/primeFactor
```

**一元二次方程** — 仅打开

```
iconverter://tool/quadraticSolver
```

**统计计算**
`data` = 数据集，空格 / 逗号 / 分号分隔。

```
iconverter://tool/statistics?data=1,2,3,4,5,6,7,8,9,10
```

**排列组合** — 仅打开

```
iconverter://tool/combinations
```

**几何计算**
`shape` = 形状，`v1` / `v2` / `v3` = 各边参数。

可选形状：`rectangle` · `square` · `circle` · `triangle` · `triangleSSS` · `parallelogram` · `trapezoid` · `sector` · `ellipse` · `regularPolygon` · `sphere` · `hemisphere` · `cylinder` · `cone` · `frustum` · `cube` · `cuboid`。

圆形（`v1` = 半径）：

```
iconverter://tool/geometry?shape=circle&v1=5
```

矩形（`v1` = 长，`v2` = 宽）：

```
iconverter://tool/geometry?shape=rectangle&v1=10&v2=5
```

球体（`v1` = 半径）：

```
iconverter://tool/geometry?shape=sphere&v1=3
```

圆柱（`v1` = 半径，`v2` = 高）：

```
iconverter://tool/geometry?shape=cylinder&v1=4&v2=10
```

---

## 5. 编码

**罗马数字**
`n` = 阿拉伯数字（1–3999）；或 `roman` = 罗马数字字符串。

```
iconverter://tool/roman?n=2026
```

```
iconverter://tool/roman?roman=MMXXVI
```

**Base64 编解码**
`mode` = encode/decode，`urlSafe` = URL 安全模式 `0/1`，`text` = 输入文本。

```
iconverter://tool/base64?mode=encode&text=Hello%2C+World!
```

```
iconverter://tool/base64?mode=decode&urlSafe=0&text=SGVsbG8sIFdvcmxkIQ%3D%3D
```

**URL 编解码**
`mode` = encode/decode，`comp` = 组件模式 0 = 全部 / 1 = 查询参数 / 2 = 路径，`text` = 输入。

```
iconverter://tool/urlCoder?mode=encode&comp=0&text=https://example.com/path?q=hello world
```

```
iconverter://tool/urlCoder?mode=decode&text=https%3A%2F%2Fexample.com%2F%3Fq%3Dhello%20world
```

**哈希计算**
`text` = 输入文本，`algo` = 算法 md5/sha1/sha256/sha512，`upper` = 大写输出 `0/1`，`hmac` = 启用 HMAC `0/1`，`key` = HMAC 密钥。

```
iconverter://tool/hashing?text=Hello+World&algo=sha256&upper=0
```

```
iconverter://tool/hashing?text=data&algo=md5&hmac=1&key=secret
```

**字数统计**
`text` = 待统计文本。

```
iconverter://tool/wordCount?text=The+quick+brown+fox+jumps+over+the+lazy+dog.
```

**颜色换算**
`hex` = 十六进制颜色；或 `r` / `g` / `b` = RGB 分量（0–255）。

```
iconverter://tool/colorConverter?hex=%23FF8800
```

```
iconverter://tool/colorConverter?r=255&g=136&b=0
```

**色板** — 仅打开

```
iconverter://tool/colorPalette
```

**二维码**
`text` = 内容，`format` = 格式 `qr/aztec/code128/pdf417` 等，`ecc` = 纠错级别 `L/M/Q/H`。

```
iconverter://tool/qrcode?text=https%3A%2F%2Fexample.com&ecc=H
```

```
iconverter://tool/qrcode?text=Hello+iConverter&format=qr&ecc=M
```

**JSON 格式化**
`text` = JSON 字符串（需 URL 编码），`indent` = 缩进空格数 2/4。

```
iconverter://tool/jsonFormatter?text=%7B%22name%22%3A%22Alice%22%2C%22age%22%3A30%7D&indent=2
```

**时间戳**
`ts` = Unix 时间戳（秒），`u` = 单位 0 = 秒 / 1 = 毫秒；或 `iso` = ISO8601 日期字符串。

```
iconverter://tool/timestamp?ts=1747440000
```

```
iconverter://tool/timestamp?iso=2026-05-17T12:00:00
```

**银行卡号**
`num` = 银行卡号。

```
iconverter://tool/bankCard?num=6214830172816734
```

**文本大小写**
`text` = 输入文本。

```
iconverter://tool/textCase?text=hello+world+from+iConverter
```

**文本对比** — 仅打开

```
iconverter://tool/textDiff
```

**HTTP 请求**
`url` = 请求 URL，`method` = GET/POST/PUT/PATCH/DELETE，`body` = 请求体，`bodyKind` = body 类型 `json/form/text`，`headers` = 请求头 JSON。

```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=GET
```

```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=POST&body=%7B%22name%22%3A%22Alice%22%7D&bodyKind=json
```

**文件下载**
`url` = 下载链接，`name` = 保存文件名（可选）。

```
iconverter://tool/fileDownload?url=https%3A%2F%2Fexample.com%2Freport.pdf&name=report.pdf
```

**HTTP 状态码**
`code` = 状态码；或 `q` = 搜索关键词。

```
iconverter://tool/httpStatusCodes?code=404
```

```
iconverter://tool/httpStatusCodes?q=redirect
```

**IP 工具**
`mode` = subnet/cidr/range，`ip` = IP 地址，`mask` = 子网掩码；或 `prefix` = CIDR 前缀长度。

```
iconverter://tool/ipUtility?mode=subnet&ip=192.168.1.0&mask=255.255.255.0
```

```
iconverter://tool/ipUtility?ip=10.0.0.0&prefix=24
```

**ASCII 码表**
`dec` = 十进制码点；或 `hex` = 十六进制；或 `q` = 搜索。

```
iconverter://tool/asciiTable?dec=65
```

```
iconverter://tool/asciiTable?q=space
```

**密码生成器**
`length` = 长度，`upper` = 大写 `0/1`，`lower` = 小写 `0/1`，`digits` = 数字 `0/1`，`symbols` = 符号 `0/1`，`unambiguous` = 排除歧义字符 `0/1`，`go` = 立即生成 `1`。

```
iconverter://tool/passwordGenerator?length=20&upper=1&lower=1&digits=1&symbols=1&unambiguous=1&go=1
```

**随机数生成**
`min` = 最小值，`max` = 最大值，`n` = 数量，`decimals` = 小数位，`unique` = 不重复 `0/1`，`sort` = 排序 0 = 不排 / 1 = 升序 / 2 = 降序，`go` = 立即生成 `1`。

```
iconverter://tool/randomNumber?min=1&max=100&n=10&unique=1&sort=1&go=1
```

```
iconverter://tool/randomNumber?min=0&max=1&n=5&decimals=4&go=1
```

**摩斯电码**
`mode` = encode/decode，`text` = 输入文本。

```
iconverter://tool/morseCode?mode=encode&text=SOS
```

```
iconverter://tool/morseCode?mode=decode&text=...+---+...
```

**JWT 解码**
`token` = JWT 令牌字符串。

```
iconverter://tool/jwtParser?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

**Cron 表达式**
`expr` = Cron 表达式（空格可用 `+` 代替）。

```
iconverter://tool/cronParser?expr=0+9+*+*+1-5
```

```
iconverter://tool/cronParser?expr=0+0+*+*+*
```

**正则测试**
`pattern` = 正则表达式（需 URL 编码），`haystack` = 测试文本，`replacement` = 替换内容，`i` = 忽略大小写 `0/1`，`m` = 多行 `0/1`，`s` = 点匹配换行 `0/1`。

```
iconverter://tool/regexTester?pattern=%5Cd%2B&haystack=abc123def456&i=0
```

```
iconverter://tool/regexTester?pattern=%28%5Cw%2B%29&haystack=hello+world&replacement=%5B%241%5D&i=1
```

**网页工具**
`url` = 直接打开 URL；或 `q` = 搜索关键词（使用默认搜索引擎）。

```
iconverter://tool/webBrowser?url=https%3A%2F%2Fexample.com
```

```
iconverter://tool/webBrowser?q=SwiftUI+deep+link+2026
```

---

## 6. 生活

**BMI 计算**
`h` = 身高 cm，`w` = 体重 kg，`std` = 标准 0 = 中国成人 / 1 = WHO。

```
iconverter://tool/bmi?h=175&w=70&std=0
```

**基础代谢率**
`h` = 身高 cm，`w` = 体重 kg，`age` = 年龄，`sex` = 性别 m = 男 / f = 女，`act` = 活动指数 0–4，`formula` = 公式 0 = Harris-Benedict / 1 = Mifflin-St Jeor。

```
iconverter://tool/bmr?h=175&w=70&age=30&sex=m&act=1&formula=1
```

**服装尺码** — 仅打开

```
iconverter://tool/clothingSize
```

**戒指尺码** — 仅打开

```
iconverter://tool/ringSize
```

**身高换算** — 仅打开

```
iconverter://tool/heightConverter
```

**油费计算**
`unit` = 单位 0 = 公制 / 1 = 英制，`d` = 行驶距离，`c` = 百公里油耗,`p` = 油价，`n` = 人数。

```
iconverter://tool/fuelCost?unit=0&d=500&c=8.5&p=7.8&n=1
```

**运费计算**
`w` = 实重 kg，`fw` = 首重 kg，`ff` = 首重费用，`sw` = 续重步长 kg，`sf` = 续重费用。

```
iconverter://tool/shippingFee?w=3.5&fw=1&ff=12&sw=1&sf=8
```

含体积重（`vol` = 启用 `0/1`，`l` / `wd` / `h` = 三边 cm，`div` = 抛比）：

```
iconverter://tool/shippingFee?w=2&vol=1&l=50&wd=40&h=30&div=6000&fw=1&ff=12&sw=1&sf=8
```

**酒精血液浓度**
`sex` = 性别 m = 男 / f = 女，`w` = 体重 kg，`v` = 饮酒量 mL，`abv` = 酒精度 %，`h` = 饮酒后小时数。

```
iconverter://tool/alcoholBac?sex=m&w=70&v=500&abv=5&h=0.5
```

**亲戚称呼**
`chain` = 关系链逗号分隔，`sex` = 本人性别 0 = 男 / 1 = 女，`reverse` = 显示互称 `0/1`。

```
iconverter://tool/relationship?chain=f,os&sex=0&reverse=1
```

```
iconverter://tool/relationship?chain=m,ob&sex=1&reverse=0
```

**身份证查询**
`id` = 身份证号码。

```
iconverter://tool/idCard?id=110101199003073010
```

**抛硬币** — 仅打开

```
iconverter://tool/coinFlip
```

**骰子模拟** — 仅打开

```
iconverter://tool/diceRoller
```

**随机抽签** — 仅打开

```
iconverter://tool/randomDraw
```

**转盘抽奖** — 仅打开

```
iconverter://tool/spinWheel
```

**视频关键帧** — 仅打开

```
iconverter://tool/videoFrameExport
```

---

## 7. 传感器

**指南针** — 仅打开

```
iconverter://tool/compass
```

**水平仪** — 仅打开

```
iconverter://tool/level
```

**海拔仪** — 仅打开

```
iconverter://tool/altitude
```

---

## 8. 中文

**大写数字**
`n` = 阿拉伯数字。

```
iconverter://tool/chineseNumber?n=12345.67
```

**汉字数字反查**
`text` = 汉字数字字符串。

```
iconverter://tool/chineseNumberReverse?text=一万二千三百四十五
```

**金额大写**
`amount` = 金额，`zheng` = 末尾「整」`0/1`。

```
iconverter://tool/financialAmount?amount=12345.67&zheng=1
```

---

## 9. 单位换算

通用格式：`v` = 数值，`from` = 源单位（rawValue 或 symbol，大小写不敏感），`to` = 目标单位。

---

**长度**
常用单位：`meter`(m) · `kilometer`(km) · `centimeter`(cm) · `millimeter`(mm) · `foot`(ft) · `inch`(in) · `mile`(mi) · `yard`(yd) · `nauticalMile`(nmi) · `chineseLi`(里) · `chineseChi`(尺)。

```
iconverter://tool/length?v=100&from=meter&to=foot
```

```
iconverter://tool/length?v=1&from=mile&to=kilometer
```

**面积**
常用单位：`squareMeter`(m²) · `hectare`(ha) · `acre`(acre) · `squareFoot`(ft²) · `squareMile`(mile²) · `mu`(亩) · `squareKilometer`(km²)。

```
iconverter://tool/area?v=1&from=hectare&to=mu
```

```
iconverter://tool/area?v=1&from=acre&to=squareMeter
```

**体积**
常用单位：`liter`(L) · `milliliter`(mL) · `cubicMeter`(m³) · `gallon`(gal) · `fluidOunce`(fl oz) · `cup`(cup) · `ukGallon`(gal UK) · `oilBarrel`(bbl)。

```
iconverter://tool/volume?v=1&from=gallon&to=liter
```

```
iconverter://tool/volume?v=355&from=milliliter&to=fluidOunce
```

**重量 / 质量**
常用单位：`kilogram`(kg) · `gram`(g) · `pound`(lb) · `ounce`(oz) · `tonne`(t) · `jin`(斤) · `liang`(两) · `carat`(ct)。

```
iconverter://tool/weight?v=1&from=pound&to=kilogram
```

```
iconverter://tool/weight?v=1&from=jin&to=gram
```

**温度**
单位：`celsius`(°C) · `fahrenheit`(°F) · `kelvin`(K) · `rankine`(°R) · `reaumur`(°Re)。

```
iconverter://tool/temperature?v=100&from=celsius&to=fahrenheit
```

```
iconverter://tool/temperature?v=37&from=celsius&to=kelvin
```

**时间**
常用单位：`second`(s) · `minute`(min) · `hour`(h) · `day`(day) · `week`(wk) · `month`(mo) · `year`(yr) · `millisecond`(ms) · `microsecond`(μs)。

```
iconverter://tool/time?v=1&from=hour&to=second
```

```
iconverter://tool/time?v=7&from=day&to=hour
```

**速度**
单位：`meterPerSecond`(m/s) · `kmPerHour`(km/h) · `milePerHour`(mph) · `knot`(kn) · `mach`(Ma)。

```
iconverter://tool/speed?v=100&from=kmPerHour&to=milePerHour
```

```
iconverter://tool/speed?v=1&from=mach&to=meterPerSecond
```

**压强**
单位：`pascal`(Pa) · `kilopascal`(kPa) · `bar`(bar) · `atmosphere`(atm) · `psi`(psi) · `mmHg`(mmHg)。

```
iconverter://tool/pressure?v=1&from=atmosphere&to=kilopascal
```

```
iconverter://tool/pressure?v=120&from=mmHg&to=kilopascal
```

**能量**
单位：`joule`(J) · `kilojoule`(kJ) · `calorie`(cal) · `kilocalorie`(kcal) · `kilowattHour`(kWh) · `btu`(BTU)。

```
iconverter://tool/energy?v=1&from=kilowattHour&to=kilojoule
```

```
iconverter://tool/energy?v=500&from=kilocalorie&to=kilojoule
```

**功率**
单位：`watt`(W) · `kilowatt`(kW) · `hpMechanical`(hp) · `hpMetric`(PS) · `btuPerHour`(BTU/h)。

```
iconverter://tool/power?v=1&from=hpMechanical&to=kilowatt
```

```
iconverter://tool/power?v=3000&from=watt&to=hpMetric
```

**力**
单位：`newton`(N) · `kilonewton`(kN) · `kgf`(kgf) · `lbf`(lbf) · `dyne`(dyn)。

```
iconverter://tool/force?v=9.8&from=newton&to=kgf
```

```
iconverter://tool/force?v=1&from=kilonewton&to=lbf
```

**扭矩**
单位：`newtonMeter`(N·m) · `newtonCentimeter`(N·cm) · `kgfMeter`(kgf·m) · `footPound`(ft·lb) · `inchPound`(in·lb)。

```
iconverter://tool/torque?v=100&from=newtonMeter&to=footPound
```

**频率**
单位：`hertz`(Hz) · `kilohertz`(kHz) · `megahertz`(MHz) · `gigahertz`(GHz) · `terahertz`(THz) · `rpm`(rpm)。

```
iconverter://tool/frequency?v=2.4&from=gigahertz&to=megahertz
```

```
iconverter://tool/frequency?v=3000&from=rpm&to=hertz
```

**角度**
单位：`degree`(°) · `radian`(rad) · `gradian`(grad) · `arcminute`(') · `arcsecond`(") · `turn`(turn)。

```
iconverter://tool/angle?v=180&from=degree&to=radian
```

```
iconverter://tool/angle?v=1&from=turn&to=degree
```

**数据存储**
单位：`byte`(B) · `kilobyte`(KB) · `megabyte`(MB) · `gigabyte`(GB) · `terabyte`(TB) · `kibibyte`(KiB) · `mebibyte`(MiB) · `gibibyte`(GiB)。

```
iconverter://tool/dataStorage?v=1&from=gigabyte&to=mebibyte
```

```
iconverter://tool/dataStorage?v=512&from=mebibyte&to=gigabyte
```

**数据速率**
单位：`bps`(bps) · `kbps`(Kbps) · `mbps`(Mbps) · `gbps`(Gbps) · `kBps`(KB/s) · `mBps`(MB/s) · `gBps`(GB/s)。

```
iconverter://tool/dataRate?v=100&from=mbps&to=mBps
```

```
iconverter://tool/dataRate?v=1&from=gbps&to=mbps
```

**光照强度**
单位：`lux`(lx) · `footCandle`(fc) · `phot`(ph) · `nox`(nx)。

```
iconverter://tool/illuminance?v=500&from=lux&to=footCandle
```

**磁感应强度**
单位：`tesla`(T) · `millitesla`(mT) · `microtesla`(μT) · `gauss`(G) · `milligauss`(mG)。

```
iconverter://tool/magneticFlux?v=1&from=tesla&to=gauss
```

**放射性活度**
单位：`becquerel`(Bq) · `kilobecquerel`(kBq) · `megabecquerel`(MBq) · `curie`(Ci) · `millicurie`(mCi) · `microcurie`(μCi)。

```
iconverter://tool/radioactivity?v=1&from=curie&to=megabecquerel
```

**黏度**
单位：`pascalSecond`(Pa·s) · `millipascalSecond`(mPa·s) · `poise`(P) · `centipoise`(cP)。

```
iconverter://tool/viscosity?v=1&from=pascalSecond&to=centipoise
```

**燃油经济性**
单位：`lPer100km`(L/100km) · `kmPerL`(km/L) · `mpgUS`(MPG US) · `mpgUK`(MPG UK)。

```
iconverter://tool/fuelEconomy?v=8.5&from=lPer100km&to=kmPerL
```

```
iconverter://tool/fuelEconomy?v=30&from=mpgUS&to=lPer100km
```

**流量**
单位：`cubicMeterPerSecond`(m³/s) · `cubicMeterPerHour`(m³/h) · `literPerSecond`(L/s) · `literPerMinute`(L/min) · `literPerHour`(L/h) · `usGallonPerMinute`(gpm US) · `cubicFootPerMinute`(cfm)。

```
iconverter://tool/flowRate?v=1&from=literPerMinute&to=cubicMeterPerHour
```

**密度**
单位：`kgPerCubicMeter`(kg/m³) · `gramPerCubicCentimeter`(g/cm³) · `gramPerLiter`(g/L) · `kgPerLiter`(kg/L) · `poundPerCubicFoot`(lb/ft³)。

```
iconverter://tool/density?v=1&from=gramPerCubicCentimeter&to=kgPerCubicMeter
```

**磁通量**
单位：`weber`(Wb) · `milliweber`(mWb) · `microweber`(μWb) · `kiloweber`(kWb) · `maxwell`(Mx)。

```
iconverter://tool/magneticFluxTrue?v=1&from=weber&to=maxwell
```

**吸收剂量**
单位：`gray`(Gy) · `milligray`(mGy) · `microgray`(μGy) · `kilogray`(kGy) · `rad`(rad) · `millirad`(mrad)。

```
iconverter://tool/absorbedDose?v=1&from=gray&to=rad
```

**等效剂量**
单位：`sievert`(Sv) · `millisievert`(mSv) · `microsievert`(μSv) · `rem`(rem) · `millirem`(mrem)。

```
iconverter://tool/equivalentDose?v=1&from=sievert&to=rem
```

```
iconverter://tool/equivalentDose?v=20&from=millisievert&to=microsievert
```

**物质的量**
单位：`mole`(mol) · `millimole`(mmol) · `micromole`(μmol) · `kilomole`(kmol) · `nanomole`(nmol) · `picomole`(pmol)。

```
iconverter://tool/amountOfSubstance?v=1&from=mole&to=millimole
```

```
iconverter://tool/amountOfSubstance?v=150&from=millimole&to=micromole
```

---

[返回 iConverter 支持页](./) &middot; [常见问题](faq) &middot; [隐私政策](privacy)

</section>

<section lang="zh-TW" markdown="1">

愛計算（iConverter）支援 `iconverter://` URL Scheme 深度連結——可從其他應用、網頁、QR Code（QR Code 工具內 **產生或掃描**）、Safari 或 Apple 捷徑開啟全部 98 個工具，並透過查詢參數預填輸入框。

> **小工具設定：** iOS 新增/編輯小工具時的工具選擇器跟隨 **裝置系統語言**。**設定 → 語言** 中的 App 內語言不會改變小工具設定介面。

## 協議規範

```
iconverter://tool/<ToolItem.rawValue>?key=value&key2=value2
```

- `<ToolItem.rawValue>` 與小工具深度連結共用同一套命名。
- 參數鍵名支援短鍵與同義別名二選一，例如 `text` 與 `input` 等效。
- 布林參數：`1/true/yes/on` → true；`0/false/no/off` → false。
- 日期參數：支援 `yyyy-MM-dd`、ISO8601、Unix 時間戳（秒）。
- 單位換算通用：`v` = 數值，`from` = 來源單位（rawValue 或 symbol，大小寫不敏感），`to` = 目標單位。

---

## 1. 計算器

**標準計算器** — 僅開啟

```
iconverter://tool/calculator
```

**科學計算器** — 僅開啟

```
iconverter://tool/scientific
```

**程式設計師計算器** — 僅開啟

```
iconverter://tool/programmer
```

---

## 2. 財務

**房貸計算器**
`p` = 貸款金額，`r` = 年利率 %，`y` = 年數，`mode` = 還款方式 0 = 等額本息 / 1 = 等額本金。

```
iconverter://tool/mortgage?p=1000000&r=3.7&y=30&mode=0
```

**個人所得稅**
`salary` = 月薪，`insurance` = 社保公積金，`deduction` = 專項扣除，`threshold` = 起徵點，`bonus` = 年終獎。

```
iconverter://tool/incomeTax?salary=20000&insurance=3000&deduction=1000&threshold=5000&bonus=50000
```

**複利計算**
`p` = 本金，`m` = 月定投，`r` = 年利率 %，`y` = 年數，`freq` = 複利頻率 0 = 年 / 1 = 月 / 2 = 日,`i` = 通脹率 %。

```
iconverter://tool/compoundInterest?p=100000&m=1000&r=7&y=10&freq=1
```

**折扣計算**
`mode` = 模式 0–4，`p` = 原價，`r` = 折扣率，`t` = 滿減門檻,`u` = 減免金額。

```
iconverter://tool/discount?mode=0&p=299&r=8.5
```

滿減範例：

```
iconverter://tool/discount?mode=3&p=350&t=300&u=50
```

**小費 / AA**
`mode` = 0 = 小費 / 1 = AA，`bill` = 帳單，`tip` = 小費 %，`tax` = 稅率 %，`ppl` = 人數。

```
iconverter://tool/tipAA?mode=0&bill=200&tip=15&tax=0&ppl=4
```

**提前還款**
`p` = 原貸款額，`r` = 年利率 %，`total` = 總期數（年），`paid` = 已還期數，`prepay` = 提前還款額，`mode` = 方案 0 = 縮期 / 1 = 減月供 / 2 = 對比。

```
iconverter://tool/mortgagePrepay?p=800000&r=3.7&total=30&paid=5&prepay=100000&mode=2
```

**二手房稅費** — 僅開啟

```
iconverter://tool/realEstateTax
```

---

## 3. 日期時間

**年齡 / 紀念日**
`birth` = 生日 `yyyy-MM-dd`，`ref` = 參考日期。

```
iconverter://tool/ageAnniversary?birth=1990-05-01&ref=2026-05-17
```

**日期計算**
`mode` = 0 = 日期加減 / 1 = 兩日期差。

加減模式（`d1` = 起始日期，`d` = ± 天數，`w` = ± 週，`mo` = ± 月，`y` = ± 年）：

```
iconverter://tool/dateArithmetic?mode=0&d1=2026-05-17&d=100
```

差值模式（`d1` = 日期 1，`d2` = 日期 2）：

```
iconverter://tool/dateArithmetic?mode=1&d1=2026-01-01&d2=2026-12-31
```

**農曆查詢**
`date` = 公曆日期 `yyyy-MM-dd`。

```
iconverter://tool/lunarCalendar?date=2026-05-17
```

**節氣** — 僅開啟

```
iconverter://tool/solarTerms
```

**倒數日**
`label` = 事件名，`target` = 目標日期 `yyyy-MM-dd`，`time` = 含時分 `0/1`。

```
iconverter://tool/countdown?label=Holiday&target=2026-10-01&time=0
```

**孕期計算**
`method` = 方式 0 = 末次月經 / 1 = 受孕日 / 2 = IVF，`ref` = 日期,`ivf` = IVF 胚胎天數 0 = D3 / 1 = D5。

```
iconverter://tool/pregnancy?method=0&ref=2026-03-01
```

```
iconverter://tool/pregnancy?method=2&ref=2026-03-15&ivf=1
```

**月經週期**
`lmp` = 末次月經日期，`cycle` = 週期天數，`period` = 行經天數。

```
iconverter://tool/menstrual?lmp=2026-05-01&cycle=28&period=5
```

**世界時鐘**
`q` = 城市搜尋關鍵字，`now` = 使用目前時間 `0/1`，`ref` = 自訂時間。

```
iconverter://tool/worldClock?q=Tokyo
```

```
iconverter://tool/worldClock?now=0&ref=2026-05-17T20:00:00
```

**星座** — 僅開啟

```
iconverter://tool/zodiac
```

---

## 4. 數學

**百分比計算**
`mode` = 模式 0–4，`a` = 數值 A，`b` = 數值 B。

```
iconverter://tool/percentage?mode=0&a=75&b=120
```

**分數計算** — 僅開啟

```
iconverter://tool/fraction
```

**質因數分解** — 僅開啟

```
iconverter://tool/primeFactor
```

**一元二次方程** — 僅開啟

```
iconverter://tool/quadraticSolver
```

**統計計算**
`data` = 資料集，空格 / 逗號 / 分號分隔。

```
iconverter://tool/statistics?data=1,2,3,4,5,6,7,8,9,10
```

**排列組合** — 僅開啟

```
iconverter://tool/combinations
```

**幾何計算**
`shape` = 形狀，`v1` / `v2` / `v3` = 各邊參數。

可選形狀：`rectangle` · `square` · `circle` · `triangle` · `triangleSSS` · `parallelogram` · `trapezoid` · `sector` · `ellipse` · `regularPolygon` · `sphere` · `hemisphere` · `cylinder` · `cone` · `frustum` · `cube` · `cuboid`。

圓形（`v1` = 半徑）：

```
iconverter://tool/geometry?shape=circle&v1=5
```

矩形（`v1` = 長，`v2` = 寬）：

```
iconverter://tool/geometry?shape=rectangle&v1=10&v2=5
```

球體（`v1` = 半徑）：

```
iconverter://tool/geometry?shape=sphere&v1=3
```

圓柱（`v1` = 半徑，`v2` = 高）：

```
iconverter://tool/geometry?shape=cylinder&v1=4&v2=10
```

---

## 5. 編碼

**羅馬數字**
`n` = 阿拉伯數字（1–3999）；或 `roman` = 羅馬數字字串。

```
iconverter://tool/roman?n=2026
```

```
iconverter://tool/roman?roman=MMXXVI
```

**Base64 編解碼**
`mode` = encode/decode，`urlSafe` = URL 安全模式 `0/1`，`text` = 輸入文字。

```
iconverter://tool/base64?mode=encode&text=Hello%2C+World!
```

```
iconverter://tool/base64?mode=decode&urlSafe=0&text=SGVsbG8sIFdvcmxkIQ%3D%3D
```

**URL 編解碼**
`mode` = encode/decode，`comp` = 元件模式 0 = 全部 / 1 = 查詢參數 / 2 = 路徑，`text` = 輸入。

```
iconverter://tool/urlCoder?mode=encode&comp=0&text=https://example.com/path?q=hello world
```

```
iconverter://tool/urlCoder?mode=decode&text=https%3A%2F%2Fexample.com%2F%3Fq%3Dhello%20world
```

**雜湊計算**
`text` = 輸入文字，`algo` = 演算法 md5/sha1/sha256/sha512，`upper` = 大寫輸出 `0/1`，`hmac` = 啟用 HMAC `0/1`，`key` = HMAC 金鑰。

```
iconverter://tool/hashing?text=Hello+World&algo=sha256&upper=0
```

```
iconverter://tool/hashing?text=data&algo=md5&hmac=1&key=secret
```

**字數統計**
`text` = 待統計文字。

```
iconverter://tool/wordCount?text=The+quick+brown+fox+jumps+over+the+lazy+dog.
```

**顏色換算**
`hex` = 十六進制顏色；或 `r` / `g` / `b` = RGB 分量（0–255）。

```
iconverter://tool/colorConverter?hex=%23FF8800
```

```
iconverter://tool/colorConverter?r=255&g=136&b=0
```

**色板** — 僅開啟

```
iconverter://tool/colorPalette
```

**QR Code**
`text` = 內容，`format` = 格式 `qr/aztec/code128/pdf417` 等，`ecc` = 糾錯等級 `L/M/Q/H`。

```
iconverter://tool/qrcode?text=https%3A%2F%2Fexample.com&ecc=H
```

```
iconverter://tool/qrcode?text=Hello+iConverter&format=qr&ecc=M
```

**JSON 格式化**
`text` = JSON 字串（需 URL 編碼），`indent` = 縮排空格數 2/4。

```
iconverter://tool/jsonFormatter?text=%7B%22name%22%3A%22Alice%22%2C%22age%22%3A30%7D&indent=2
```

**時間戳**
`ts` = Unix 時間戳（秒），`u` = 單位 0 = 秒 / 1 = 毫秒；或 `iso` = ISO8601 日期字串。

```
iconverter://tool/timestamp?ts=1747440000
```

```
iconverter://tool/timestamp?iso=2026-05-17T12:00:00
```

**銀行卡號**
`num` = 銀行卡號。

```
iconverter://tool/bankCard?num=6214830172816734
```

**文字大小寫**
`text` = 輸入文字。

```
iconverter://tool/textCase?text=hello+world+from+iConverter
```

**文字比對** — 僅開啟

```
iconverter://tool/textDiff
```

**HTTP 請求**
`url` = 請求 URL，`method` = GET/POST/PUT/PATCH/DELETE，`body` = 請求體，`bodyKind` = body 類型 `json/form/text`，`headers` = 請求頭 JSON。

```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=GET
```

```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=POST&body=%7B%22name%22%3A%22Alice%22%7D&bodyKind=json
```

**檔案下載**
`url` = 下載連結，`name` = 儲存檔名（可選）。

```
iconverter://tool/fileDownload?url=https%3A%2F%2Fexample.com%2Freport.pdf&name=report.pdf
```

**HTTP 狀態碼**
`code` = 狀態碼；或 `q` = 搜尋關鍵字。

```
iconverter://tool/httpStatusCodes?code=404
```

```
iconverter://tool/httpStatusCodes?q=redirect
```

**IP 工具**
`mode` = subnet/cidr/range，`ip` = IP 位址，`mask` = 子網路遮罩；或 `prefix` = CIDR 前綴長度。

```
iconverter://tool/ipUtility?mode=subnet&ip=192.168.1.0&mask=255.255.255.0
```

```
iconverter://tool/ipUtility?ip=10.0.0.0&prefix=24
```

**ASCII 碼表**
`dec` = 十進制碼點；或 `hex` = 十六進制；或 `q` = 搜尋。

```
iconverter://tool/asciiTable?dec=65
```

```
iconverter://tool/asciiTable?q=space
```

**密碼產生器**
`length` = 長度，`upper` = 大寫 `0/1`，`lower` = 小寫 `0/1`，`digits` = 數字 `0/1`，`symbols` = 符號 `0/1`，`unambiguous` = 排除歧義字元 `0/1`，`go` = 立即產生 `1`。

```
iconverter://tool/passwordGenerator?length=20&upper=1&lower=1&digits=1&symbols=1&unambiguous=1&go=1
```

**亂數產生**
`min` = 最小值，`max` = 最大值，`n` = 數量，`decimals` = 小數位，`unique` = 不重複 `0/1`，`sort` = 排序 0 = 不排 / 1 = 升序 / 2 = 降序，`go` = 立即產生 `1`。

```
iconverter://tool/randomNumber?min=1&max=100&n=10&unique=1&sort=1&go=1
```

```
iconverter://tool/randomNumber?min=0&max=1&n=5&decimals=4&go=1
```

**摩斯電碼**
`mode` = encode/decode，`text` = 輸入文字。

```
iconverter://tool/morseCode?mode=encode&text=SOS
```

```
iconverter://tool/morseCode?mode=decode&text=...+---+...
```

**JWT 解碼**
`token` = JWT 令牌字串。

```
iconverter://tool/jwtParser?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

**Cron 表達式**
`expr` = Cron 表達式（空格可用 `+` 代替）。

```
iconverter://tool/cronParser?expr=0+9+*+*+1-5
```

```
iconverter://tool/cronParser?expr=0+0+*+*+*
```

**正則測試**
`pattern` = 正則表達式（需 URL 編碼），`haystack` = 測試文字，`replacement` = 取代內容，`i` = 忽略大小寫 `0/1`，`m` = 多行 `0/1`，`s` = 點匹配換行 `0/1`。

```
iconverter://tool/regexTester?pattern=%5Cd%2B&haystack=abc123def456&i=0
```

```
iconverter://tool/regexTester?pattern=%28%5Cw%2B%29&haystack=hello+world&replacement=%5B%241%5D&i=1
```

**網頁工具**
`url` = 直接開啟 URL；或 `q` = 搜尋關鍵字（使用預設搜尋引擎）。

```
iconverter://tool/webBrowser?url=https%3A%2F%2Fexample.com
```

```
iconverter://tool/webBrowser?q=SwiftUI+deep+link+2026
```

---

## 6. 生活

**BMI 計算**
`h` = 身高 cm，`w` = 體重 kg，`std` = 標準 0 = 中國成人 / 1 = WHO。

```
iconverter://tool/bmi?h=175&w=70&std=0
```

**基礎代謝率**
`h` = 身高 cm，`w` = 體重 kg，`age` = 年齡，`sex` = 性別 m = 男 / f = 女，`act` = 活動指數 0–4，`formula` = 公式 0 = Harris-Benedict / 1 = Mifflin-St Jeor。

```
iconverter://tool/bmr?h=175&w=70&age=30&sex=m&act=1&formula=1
```

**服裝尺碼** — 僅開啟

```
iconverter://tool/clothingSize
```

**戒指尺碼** — 僅開啟

```
iconverter://tool/ringSize
```

**身高換算** — 僅開啟

```
iconverter://tool/heightConverter
```

**油費計算**
`unit` = 單位 0 = 公制 / 1 = 英制，`d` = 行駛距離，`c` = 每百公里油耗，`p` = 油價，`n` = 人數。

```
iconverter://tool/fuelCost?unit=0&d=500&c=8.5&p=7.8&n=1
```

**運費計算**
`w` = 實重 kg，`fw` = 首重 kg，`ff` = 首重費用，`sw` = 續重步長 kg，`sf` = 續重費用。

```
iconverter://tool/shippingFee?w=3.5&fw=1&ff=12&sw=1&sf=8
```

含體積重（`vol` = 啟用 `0/1`，`l` / `wd` / `h` = 三邊 cm，`div` = 拋比）：

```
iconverter://tool/shippingFee?w=2&vol=1&l=50&wd=40&h=30&div=6000&fw=1&ff=12&sw=1&sf=8
```

**酒精血液濃度**
`sex` = 性別 m = 男 / f = 女，`w` = 體重 kg，`v` = 飲酒量 mL，`abv` = 酒精度 %，`h` = 飲酒後小時數。

```
iconverter://tool/alcoholBac?sex=m&w=70&v=500&abv=5&h=0.5
```

**親戚稱呼**
`chain` = 關係鏈逗號分隔，`sex` = 本人性別 0 = 男 / 1 = 女，`reverse` = 顯示互稱 `0/1`。

```
iconverter://tool/relationship?chain=f,os&sex=0&reverse=1
```

```
iconverter://tool/relationship?chain=m,ob&sex=1&reverse=0
```

**身分證查詢**
`id` = 身分證號碼。

```
iconverter://tool/idCard?id=110101199003073010
```

**拋硬幣** — 僅開啟

```
iconverter://tool/coinFlip
```

**骰子模擬** — 僅開啟

```
iconverter://tool/diceRoller
```

**隨機抽籤** — 僅開啟

```
iconverter://tool/randomDraw
```

**轉盤抽獎** — 僅開啟

```
iconverter://tool/spinWheel
```

**影片關鍵幀** — 僅開啟

```
iconverter://tool/videoFrameExport
```

---

## 7. 感測器

**指南針** — 僅開啟

```
iconverter://tool/compass
```

**水平儀** — 僅開啟

```
iconverter://tool/level
```

**海拔儀** — 僅開啟

```
iconverter://tool/altitude
```

---

## 8. 中文

**大寫數字**
`n` = 阿拉伯數字。

```
iconverter://tool/chineseNumber?n=12345.67
```

**漢字數字反查**
`text` = 漢字數字字串。

```
iconverter://tool/chineseNumberReverse?text=一万二千三百四十五
```

**金額大寫**
`amount` = 金額，`zheng` = 末尾「整」`0/1`。

```
iconverter://tool/financialAmount?amount=12345.67&zheng=1
```

---

## 9. 單位換算

通用格式：`v` = 數值，`from` = 來源單位（rawValue 或 symbol，大小寫不敏感），`to` = 目標單位。

---

**長度**
常用單位：`meter`(m) · `kilometer`(km) · `centimeter`(cm) · `millimeter`(mm) · `foot`(ft) · `inch`(in) · `mile`(mi) · `yard`(yd) · `nauticalMile`(nmi) · `chineseLi`(里) · `chineseChi`(尺)。

```
iconverter://tool/length?v=100&from=meter&to=foot
```

```
iconverter://tool/length?v=1&from=mile&to=kilometer
```

**面積**
常用單位：`squareMeter`(m²) · `hectare`(ha) · `acre`(acre) · `squareFoot`(ft²) · `squareMile`(mile²) · `mu`(亩) · `squareKilometer`(km²)。

```
iconverter://tool/area?v=1&from=hectare&to=mu
```

```
iconverter://tool/area?v=1&from=acre&to=squareMeter
```

**體積**
常用單位：`liter`(L) · `milliliter`(mL) · `cubicMeter`(m³) · `gallon`(gal) · `fluidOunce`(fl oz) · `cup`(cup) · `ukGallon`(gal UK) · `oilBarrel`(bbl)。

```
iconverter://tool/volume?v=1&from=gallon&to=liter
```

```
iconverter://tool/volume?v=355&from=milliliter&to=fluidOunce
```

**重量 / 質量**
常用單位：`kilogram`(kg) · `gram`(g) · `pound`(lb) · `ounce`(oz) · `tonne`(t) · `jin`(斤) · `liang`(两) · `carat`(ct)。

```
iconverter://tool/weight?v=1&from=pound&to=kilogram
```

```
iconverter://tool/weight?v=1&from=jin&to=gram
```

**溫度**
單位：`celsius`(°C) · `fahrenheit`(°F) · `kelvin`(K) · `rankine`(°R) · `reaumur`(°Re)。

```
iconverter://tool/temperature?v=100&from=celsius&to=fahrenheit
```

```
iconverter://tool/temperature?v=37&from=celsius&to=kelvin
```

**時間**
常用單位：`second`(s) · `minute`(min) · `hour`(h) · `day`(day) · `week`(wk) · `month`(mo) · `year`(yr) · `millisecond`(ms) · `microsecond`(μs)。

```
iconverter://tool/time?v=1&from=hour&to=second
```

```
iconverter://tool/time?v=7&from=day&to=hour
```

**速度**
單位：`meterPerSecond`(m/s) · `kmPerHour`(km/h) · `milePerHour`(mph) · `knot`(kn) · `mach`(Ma)。

```
iconverter://tool/speed?v=100&from=kmPerHour&to=milePerHour
```

```
iconverter://tool/speed?v=1&from=mach&to=meterPerSecond
```

**壓強**
單位：`pascal`(Pa) · `kilopascal`(kPa) · `bar`(bar) · `atmosphere`(atm) · `psi`(psi) · `mmHg`(mmHg)。

```
iconverter://tool/pressure?v=1&from=atmosphere&to=kilopascal
```

```
iconverter://tool/pressure?v=120&from=mmHg&to=kilopascal
```

**能量**
單位：`joule`(J) · `kilojoule`(kJ) · `calorie`(cal) · `kilocalorie`(kcal) · `kilowattHour`(kWh) · `btu`(BTU)。

```
iconverter://tool/energy?v=1&from=kilowattHour&to=kilojoule
```

```
iconverter://tool/energy?v=500&from=kilocalorie&to=kilojoule
```

**功率**
單位：`watt`(W) · `kilowatt`(kW) · `hpMechanical`(hp) · `hpMetric`(PS) · `btuPerHour`(BTU/h)。

```
iconverter://tool/power?v=1&from=hpMechanical&to=kilowatt
```

```
iconverter://tool/power?v=3000&from=watt&to=hpMetric
```

**力**
單位：`newton`(N) · `kilonewton`(kN) · `kgf`(kgf) · `lbf`(lbf) · `dyne`(dyn)。

```
iconverter://tool/force?v=9.8&from=newton&to=kgf
```

```
iconverter://tool/force?v=1&from=kilonewton&to=lbf
```

**扭矩**
單位：`newtonMeter`(N·m) · `newtonCentimeter`(N·cm) · `kgfMeter`(kgf·m) · `footPound`(ft·lb) · `inchPound`(in·lb)。

```
iconverter://tool/torque?v=100&from=newtonMeter&to=footPound
```

**頻率**
單位：`hertz`(Hz) · `kilohertz`(kHz) · `megahertz`(MHz) · `gigahertz`(GHz) · `terahertz`(THz) · `rpm`(rpm)。

```
iconverter://tool/frequency?v=2.4&from=gigahertz&to=megahertz
```

```
iconverter://tool/frequency?v=3000&from=rpm&to=hertz
```

**角度**
單位：`degree`(°) · `radian`(rad) · `gradian`(grad) · `arcminute`(') · `arcsecond`(") · `turn`(turn)。

```
iconverter://tool/angle?v=180&from=degree&to=radian
```

```
iconverter://tool/angle?v=1&from=turn&to=degree
```

**資料儲存**
單位：`byte`(B) · `kilobyte`(KB) · `megabyte`(MB) · `gigabyte`(GB) · `terabyte`(TB) · `kibibyte`(KiB) · `mebibyte`(MiB) · `gibibyte`(GiB)。

```
iconverter://tool/dataStorage?v=1&from=gigabyte&to=mebibyte
```

```
iconverter://tool/dataStorage?v=512&from=mebibyte&to=gigabyte
```

**資料速率**
單位：`bps`(bps) · `kbps`(Kbps) · `mbps`(Mbps) · `gbps`(Gbps) · `kBps`(KB/s) · `mBps`(MB/s) · `gBps`(GB/s)。

```
iconverter://tool/dataRate?v=100&from=mbps&to=mBps
```

```
iconverter://tool/dataRate?v=1&from=gbps&to=mbps
```

**照度**
單位：`lux`(lx) · `footCandle`(fc) · `phot`(ph) · `nox`(nx)。

```
iconverter://tool/illuminance?v=500&from=lux&to=footCandle
```

**磁感應強度**
單位：`tesla`(T) · `millitesla`(mT) · `microtesla`(μT) · `gauss`(G) · `milligauss`(mG)。

```
iconverter://tool/magneticFlux?v=1&from=tesla&to=gauss
```

**放射性活度**
單位：`becquerel`(Bq) · `kilobecquerel`(kBq) · `megabecquerel`(MBq) · `curie`(Ci) · `millicurie`(mCi) · `microcurie`(μCi)。

```
iconverter://tool/radioactivity?v=1&from=curie&to=megabecquerel
```

**黏度**
單位：`pascalSecond`(Pa·s) · `millipascalSecond`(mPa·s) · `poise`(P) · `centipoise`(cP)。

```
iconverter://tool/viscosity?v=1&from=pascalSecond&to=centipoise
```

**燃油經濟性**
單位：`lPer100km`(L/100km) · `kmPerL`(km/L) · `mpgUS`(MPG US) · `mpgUK`(MPG UK)。

```
iconverter://tool/fuelEconomy?v=8.5&from=lPer100km&to=kmPerL
```

```
iconverter://tool/fuelEconomy?v=30&from=mpgUS&to=lPer100km
```

**流量**
單位：`cubicMeterPerSecond`(m³/s) · `cubicMeterPerHour`(m³/h) · `literPerSecond`(L/s) · `literPerMinute`(L/min) · `literPerHour`(L/h) · `usGallonPerMinute`(gpm US) · `cubicFootPerMinute`(cfm)。

```
iconverter://tool/flowRate?v=1&from=literPerMinute&to=cubicMeterPerHour
```

**密度**
單位：`kgPerCubicMeter`(kg/m³) · `gramPerCubicCentimeter`(g/cm³) · `gramPerLiter`(g/L) · `kgPerLiter`(kg/L) · `poundPerCubicFoot`(lb/ft³)。

```
iconverter://tool/density?v=1&from=gramPerCubicCentimeter&to=kgPerCubicMeter
```

**磁通量**
單位：`weber`(Wb) · `milliweber`(mWb) · `microweber`(μWb) · `kiloweber`(kWb) · `maxwell`(Mx)。

```
iconverter://tool/magneticFluxTrue?v=1&from=weber&to=maxwell
```

**吸收劑量**
單位：`gray`(Gy) · `milligray`(mGy) · `microgray`(μGy) · `kilogray`(kGy) · `rad`(rad) · `millirad`(mrad)。

```
iconverter://tool/absorbedDose?v=1&from=gray&to=rad
```

**等效劑量**
單位：`sievert`(Sv) · `millisievert`(mSv) · `microsievert`(μSv) · `rem`(rem) · `millirem`(mrem)。

```
iconverter://tool/equivalentDose?v=1&from=sievert&to=rem
```

```
iconverter://tool/equivalentDose?v=20&from=millisievert&to=microsievert
```

**物質的量**
單位：`mole`(mol) · `millimole`(mmol) · `micromole`(μmol) · `kilomole`(kmol) · `nanomole`(nmol) · `picomole`(pmol)。

```
iconverter://tool/amountOfSubstance?v=1&from=mole&to=millimole
```

```
iconverter://tool/amountOfSubstance?v=150&from=millimole&to=micromole
```

---

[返回 iConverter 支援頁](./) &middot; [常見問題](faq) &middot; [隱私政策](privacy)

</section>
