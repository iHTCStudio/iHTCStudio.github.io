iConverter prend en charge `iconverter://` Des liens profonds du schéma d'URL – ouvrez l'un des 101 outils des applications externes, des pages web, des codes QR (générés ou **scan dans l'application**), Safari ou des raccourcis Apple, en option pré-remplissant les champs d'entrée via les paramètres de requête.

> **Note générale:** Le sélectionneur d'outils de widget **Launcher** inclut tous les outils pris en charge, sauf **Browser Web**. L'interface utilisateur de configuration Widget suit **iOS language système**, et non la langue in-app sous Paramètres.

## Spécification du protocole


```
iconverter://tool/<ToolItem.rawValue>?key=value&key2=value2
```


- `<ToolItem.rawValue>` partage le même nom que widget deep links.
- Les noms de paramètres supportent à la fois les clés courtes et les alias synonymes (par exemple `text` est équivalent à `input`).
- Booléens: `1/true/yes/on` → true; `0/false/no/off` → false.
- Dates: prend en charge `aaaa-MM-dd`, ISO8601, Unix timestamp (secondes).
- Les convertisseurs d'unités partagent un format commun: `v` = valeur, `from` = unité source (rawValue ou symbole, insensible à la casse), `to` = unité cible.

---

## 1. Calculatrice

**Calculateur** — ouvert uniquement


```
iconverter://tool/calculator
```


**Calculatrice scientifique** — ouvert uniquement


```
iconverter://tool/scientific
```


** Calculatrice de programme** – ouverte uniquement


```
iconverter://tool/programmer
```


---

## 2. Financement

** Calculatrice de masse** `iconverter://` = montant du prêt, `<ToolItem.rawValue>` = taux annuel %, `text` = années, `input` = 0 = montant égal / 1 = principal égal.


```
iconverter://tool/mortgage?p=1000000&r=3.7&y=30&mode=0
```


** Impôt sur le revenu** `iconverter://` = salaire mensuel, `<ToolItem.rawValue>` = assurance sociale, `text` = déduction spéciale, `input` = seuil, `1/true/yes/on` = prime annuelle.


```
iconverter://tool/incomeTax?salary=20000&insurance=3000&deduction=1000&threshold=5000&bonus=50000
```


** Intérêts composés** `iconverter://` = principal, `<ToolItem.rawValue>` = cotisation mensuelle, `text` = taux annuel %, `input` = années, `1/true/yes/on` = 0 = annuel / 1 = mensuel / 2 = quotidien, `0/false/no/off` = inflation %.


```
iconverter://tool/compoundInterest?p=100000&m=1000&r=7&y=10&freq=1
```


** Calculatrice de réduction** `iconverter://` = 0–4, `<ToolItem.rawValue>` = prix initial, `text` = taux d'actualisation, `input` = seuil, `1/true/yes/on` = montant de réduction.


```
iconverter://tool/discount?mode=0&p=299&r=8.5
```


Exemple complet:


```
iconverter://tool/discount?mode=3&p=350&t=300&u=50
```


**Conseil & AA Split** `iconverter://` = 0 = pointe / 1 = AA fractionné, `<ToolItem.rawValue>` = facture, `text` = pointe %, `input` = taxe %, `1/true/yes/on` = nombre de personnes.


```
iconverter://tool/tipAA?mode=0&bill=200&tip=15&tax=0&ppl=4
```


**Prépaiement anticipé** `iconverter://` = prêt initial, `<ToolItem.rawValue>` = taux annuel %, `text` = durée totale (années), `input` = durées payées, `1/true/yes/on` = montant prépayé, `0/false/no/off` = 0 = raccourci / 1 = réduction mensuelle / 2 = comparaison.


```
iconverter://tool/mortgagePrepay?p=800000&r=3.7&total=30&paid=5&prepay=100000&mode=2
```


**Impôt immobilier** — ouvert uniquement


```
iconverter://tool/realEstateTax
```


---

## 3. Date et heure

**Âge et anniversaire** `iconverter://` = anniversaire `<ToolItem.rawValue>` , `text` = date de référence.


```
iconverter://tool/ageAnniversary?birth=1990-05-01&ref=2026-05-17
```


**Date Arithmétique** `iconverter://` = 0 = addition/soustraction / 1 = différence de date.

Mode de sous-traction ( `iconverter://` = date de début, `<ToolItem.rawValue>` = ± jours, `text` = ± semaines, `input` = ± mois, `1/true/yes/on` = ± années):


```
iconverter://tool/dateArithmetic?mode=0&d1=2026-05-17&d=100
```


Mode de différence ( `iconverter://` = date 1, `<ToolItem.rawValue>` = date 2) :


```
iconverter://tool/dateArithmetic?mode=1&d1=2026-01-01&d2=2026-12-31
```


** Calendrier lunaire** `iconverter://` = date grégorien `<ToolItem.rawValue>` ```
iconverter://tool/lunarCalendar?date=2026-05-17
```


**Conditions solaires** — ouvert uniquement


```
iconverter://tool/solarTerms
```


** Compte à rebours** `iconverter://` = nom de l'événement, `<ToolItem.rawValue>` = date cible `text` , `input` = indiquer l'heure `1/true/yes/on` .


```
iconverter://tool/countdown?label=Holiday&target=2026-10-01&time=0
```


** Calculatrice de grossesse** `iconverter://` = 0 = PMT / 1 = conception / 2 = FIV, `<ToolItem.rawValue>` = date de référence, `text` = FIV embryon jour 0 = D3 / 1 = D5.


```
iconverter://tool/pregnancy?method=0&ref=2026-03-01
```



```
iconverter://tool/pregnancy?method=2&ref=2026-03-15&ivf=1
```


** Cycle menstruel** `iconverter://` = date de la dernière période menstruelle, `<ToolItem.rawValue>` = jours de cycle, `text` = jours de période.


```
iconverter://tool/menstrual?lmp=2026-05-01&cycle=28&period=5
```


** Horloge mondiale** `iconverter://` = mot clé de la recherche de ville, `<ToolItem.rawValue>` ```
iconverter://tool/worldClock?q=Tokyo
```



```
iconverter://tool/worldClock?now=0&ref=2026-05-17T20:00:00
```


**Zodiac** – ouvert uniquement


```
iconverter://tool/zodiac
```


---

## 4. Mathématiques

** Calculatrice du pourcentage** `iconverter://` = 0–4, `<ToolItem.rawValue>` = valeur A, `text` = valeur B.


```
iconverter://tool/percentage?mode=0&a=75&b=120
```


** Calculatrice de fraction** — ouverte uniquement


```
iconverter://tool/fraction
```


** Factorisation primaire** — ouvert uniquement


```
iconverter://tool/primeFactor
```


** SolveurQuadratique** — ouvert uniquement


```
iconverter://tool/quadraticSolver
```


**Statistiques** `iconverter://` = ensemble de données, séparé par espace / virgule / point-virgule.


```
iconverter://tool/statistics?data=1,2,3,4,5,6,7,8,9,10
```


**Combinations et permutations** — ouvert uniquement


```
iconverter://tool/combinations
```


**Géométrie** `iconverter://` = forme, `<ToolItem.rawValue>` / `text` / `input` = paramètres de dimension.

Formes disponibles : `iconverter://` · `<ToolItem.rawValue>` · `text` · `input` · `1/true/yes/on` · `0/false/no/off` · `yyyy-MM-dd` · `v` · `from` · `to` · `p` · `r` · `y` · `mode` · `salary` · `insurance` · `deduction` .

Circle (   C     = rayon):


```
iconverter://tool/geometry?shape=circle&v1=5
```


Rectangle ( `iconverter://` = longueur, `<ToolItem.rawValue>` = largeur):


```
iconverter://tool/geometry?shape=rectangle&v1=10&v2=5
```


Sphère ( `iconverter://` = rayon):


```
iconverter://tool/geometry?shape=sphere&v1=3
```


Cylindre ( `iconverter://` = rayon, `<ToolItem.rawValue>` = hauteur):


```
iconverter://tool/geometry?shape=cylinder&v1=4&v2=10
```


---

## 5. Codage

**Numéro romain** `iconverter://` = numéro arabe (1–3999); ou `<ToolItem.rawValue>` = chaîne de chiffres romains.


```
iconverter://tool/roman?n=2026
```



```
iconverter://tool/roman?roman=MMXXVI
```


**Encodeur / décoder de base64** `iconverter://` = encode/décode, `<ToolItem.rawValue>` = mode sans danger pour l'URL `text` , `input` = texte d'entrée.


```
iconverter://tool/base64?mode=encode&text=Hello%2C+World!
```



```
iconverter://tool/base64?mode=decode&urlSafe=0&text=SGVsbG8sIFdvcmxkIQ%3D%3D
```


**Encodeur URL / Décoder** `iconverter://` = encode/décode, `<ToolItem.rawValue>` = mode composant 0 = complet / 1 = requête / 2 = chemin, `text` = entrée.


```
iconverter://tool/urlCoder?mode=encode&comp=0&text=https://example.com/path?q=hello world
```



```
iconverter://tool/urlCoder?mode=decode&text=https%3A%2F%2Fexample.com%2F%3Fq%3Dhello%20world
```


** Calculatrice de masse** `iconverter://` ```
iconverter://tool/hashing?text=Hello+World&algo=sha256&upper=0
```



```
iconverter://tool/hashing?text=data&algo=md5&hmac=1&key=secret
```


**Teneur de mots** `iconverter://` = texte à analyser.


```
iconverter://tool/wordCount?text=The+quick+brown+fox+jumps+over+the+lazy+dog.
```


**Convertisseur de couleurs** `iconverter://` = couleur hexagonale; ou `<ToolItem.rawValue>` / `text` / `input` = composants RGB (0–255).


```
iconverter://tool/colorConverter?hex=%23FF8800
```



```
iconverter://tool/colorConverter?r=255&g=136&b=0
```


**Couleur Palette** – ouvert uniquement


```
iconverter://tool/colorPalette
```


**Code RRQ** `iconverter://` = contenu, `<ToolItem.rawValue>` = `text` , etc., `input` = niveau de correction des erreurs `1/true/yes/on` .


```
iconverter://tool/qrcode?text=https%3A%2F%2Fexample.com&ecc=H
```



```
iconverter://tool/qrcode?text=Hello+iConverter&format=qr&ecc=M
```


**JSON Matière** `iconverter://` = chaîne JSON (encodée par l'URL), `<ToolItem.rawValue>` = espaces de tirets 2/4.


```
iconverter://tool/jsonFormatter?text=%7B%22name%22%3A%22Alice%22%2C%22age%22%3A30%7D&indent=2
```


**Horodatage** `iconverter://` = Unix timestamp (secondes), `<ToolItem.rawValue>` = unité 0 = sec / 1 = ms; ou `text` = chaîne de date ISO8601.


```
iconverter://tool/timestamp?ts=1747440000
```



```
iconverter://tool/timestamp?iso=2026-05-17T12:00:00
```


**Validateur de carte bancaire** `iconverter://` = numéro de carte.


```
iconverter://tool/bankCard?num=6214830172816734
```


**Convertisseur de cas de texte** `iconverter://` = texte d'entrée.


```
iconverter://tool/textCase?text=hello+world+from+iConverter
```


**Diffuseur de texte** – ouvert uniquement


```
iconverter://tool/textDiff
```


** Demande de PTTS** `iconverter://` = URL de la requête, `<ToolItem.rawValue>` = GET/POST/PUT/PATCH/DELETE, `text` = corps de la requête, `input` = `1/true/yes/on` , `0/false/no/off` = en-têtes JSON.


```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=GET
```



```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=POST&body=%7B%22name%22%3A%22Alice%22%7D&bodyKind=json
```


**Télécharger le fichier** `iconverter://` = URL de téléchargement, `<ToolItem.rawValue>` = nom de fichier (facultatif).


```
iconverter://tool/fileDownload?url=https%3A%2F%2Fexample.com%2Freport.pdf&name=report.pdf
```


**Codes de statut du PTTS** `iconverter://` = code d'état; ou `<ToolItem.rawValue>` = mot-clé de recherche.


```
iconverter://tool/httpStatusCodes?code=404
```



```
iconverter://tool/httpStatusCodes?q=redirect
```


**Utilitaire IP** `iconverter://` = sous-net/cidr/range, `<ToolItem.rawValue>` = adresse IP, `text` = masque subnet; ou `input` = longueur du préfixe du CIDR.


```
iconverter://tool/ipUtility?mode=subnet&ip=192.168.1.0&mask=255.255.255.0
```



```
iconverter://tool/ipUtility?ip=10.0.0.0&prefix=24
```


**Tableau ASCII** `iconverter://` = point de code décimal; ou `<ToolItem.rawValue>` = point de code hexagonal; ou `text` = recherche.


```
iconverter://tool/asciiTable?dec=65
```



```
iconverter://tool/asciiTable?q=space
```


** Générateur de mots de passe** `iconverter://` = longueur, `<ToolItem.rawValue>` = majuscule, `text` , `input` = minuscule, `1/true/yes/on` , `0/false/no/off` = chiffres, `yyyy-MM-dd` , `v` = symboles, `from` , `to` = pas d'ombles ambigus, `p` , `r` = générer immédiatement, `y` .


```
iconverter://tool/passwordGenerator?length=20&upper=1&lower=1&digits=1&symbols=1&unambiguous=1&go=1
```


** Générateur de nombre de randos** `iconverter://` = minimum, `<ToolItem.rawValue>` = maximum, `text` = nombre, `input` = décimales, `1/true/yes/on` = unique `0/false/no/off` , `yyyy-MM-dd` = 0 = aucun / 1 = asc / 2 = desc, `v` = générer immédiatement `from` .


```
iconverter://tool/randomNumber?min=1&max=100&n=10&unique=1&sort=1&go=1
```



```
iconverter://tool/randomNumber?min=0&max=1&n=5&decimals=4&go=1
```


**Code principal** `iconverter://` = encode/décode, `<ToolItem.rawValue>` = texte d'entrée.


```
iconverter://tool/morseCode?mode=encode&text=SOS
```



```
iconverter://tool/morseCode?mode=decode&text=...+---+...
```


**Décoder JWT** `iconverter://` = chaîne de jeton JWT.


```
iconverter://tool/jwtParser?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```


**Essayez l'expression en direct** `iconverter://` = Expression Cron (les espaces peuvent être remplacés par `<ToolItem.rawValue>` ).


```
iconverter://tool/cronParser?expr=0+9+*+*+1-5
```



```
iconverter://tool/cronParser?expr=0+0+*+*+*
```


** Testeur Regex** `iconverter://` = motif régex (encodé par l'URL), `<ToolItem.rawValue>` = texte d'essai, `text` = remplacement, `input` = insensible à la casse, `1/true/yes/on` , `0/false/no/off` = multiligne, `yyyy-MM-dd` , `v` = dotall, `from` .


```
iconverter://tool/regexTester?pattern=%5Cd%2B&haystack=abc123def456&i=0
```



```
iconverter://tool/regexTester?pattern=%28%5Cw%2B%29&haystack=hello+world&replacement=%5B%241%5D&i=1
```


** Navigateur Web** `iconverter://` = ouvrir l'URL directement; ou `<ToolItem.rawValue>` = requête de recherche (utilise le moteur de recherche par défaut).


```
iconverter://tool/webBrowser?url=https%3A%2F%2Fexample.com
```



```
iconverter://tool/webBrowser?q=SwiftUI+deep+link+2026
```


---

## 6. Mode de vie

** Calculatrice de l'IMC** `iconverter://` = hauteur cm, `<ToolItem.rawValue>` = poids kg, `text` = norme 0 = Chinois adulte / 1 = OMS.


```
iconverter://tool/bmi?h=175&w=70&std=0
```


** Calculatrice BMR** `iconverter://` = hauteur cm, `<ToolItem.rawValue>` = poids kg, `text` = âge, `input` = m = mâle / f = femelle, `1/true/yes/on` = niveau d'activité 0–4, `0/false/no/off` = 0 = Harris-Benedict / 1 = Mifflin-St Jeor.


```
iconverter://tool/bmr?h=175&w=70&age=30&sex=m&act=1&formula=1
```


**Taille du vêtement** — ouvert uniquement


```
iconverter://tool/clothingSize
```


** Taille de la bague** — ouvert uniquement


```
iconverter://tool/ringSize
```


**Convertisseur de hauteur** — ouvert uniquement


```
iconverter://tool/heightConverter
```


** Calculatrice du coût du carburant** `iconverter://` = 0 = métrique / 1 = impérial, `<ToolItem.rawValue>` = distance, `text` = consommation par 100 km, `input` = prix du carburant, `1/true/yes/on` = personnes.


```
iconverter://tool/fuelCost?unit=0&d=500&c=8.5&p=7.8&n=1
```


** Calculatrice des frais d'expédition** `iconverter://` = poids réel kg, `<ToolItem.rawValue>` = premier poids kg, `text` = prix de premier poids, `input` = poids d'échelon kg, `1/true/yes/on` = prix d'échelon.


```
iconverter://tool/shippingFee?w=3.5&fw=1&ff=12&sw=1&sf=8
```


Avec le poids volumétrique ( `iconverter://` = activer `<ToolItem.rawValue>` , `text` / `input` / `1/true/yes/on` = trois côtés cm, `0/false/no/off` = diviseur):


```
iconverter://tool/shippingFee?w=2&vol=1&l=50&wd=40&h=30&div=6000&fw=1&ff=12&sw=1&sf=8
```


** Teneur en alcool (BAC)** `iconverter://` = m = mâle / f = femelle, `<ToolItem.rawValue>` = poids kg, `text` = volume mL, `input` = ABV %, `1/true/yes/on` = heures depuis la consommation.


```
iconverter://tool/alcoholBac?sex=m&w=70&v=500&abv=5&h=0.5
```


**Relations** `iconverter://` = chaîne de relations (séparée par un coma), `<ToolItem.rawValue>` = sexe ego 0 = mâle / 1 = femelle, `text` = afficher l'inverse `input` .


```
iconverter://tool/relationship?chain=f,os&sex=0&reverse=1
```



```
iconverter://tool/relationship?chain=m,ob&sex=1&reverse=0
```


**Parseur de cartes d'identité** `iconverter://` = numéro de carte d'identité.


```
iconverter://tool/idCard?id=110101199003073010
```


**Flip de monnaie** – ouvert uniquement


```
iconverter://tool/coinFlip
```


**Rouleau de dés** – ouvert uniquement


```
iconverter://tool/diceRoller
```


**Random Draw** – ouvert uniquement


```
iconverter://tool/randomDraw
```


**Spin Wheel** – ouvert uniquement


```
iconverter://tool/spinWheel
```


**Exportation de cadres vidéo** — ouvert uniquement


```
iconverter://tool/videoFrameExport
```


---

## 7. Capteurs

**Compas** – ouvert uniquement


```
iconverter://tool/compass
```


**Niveau** – ouvert uniquement


```
iconverter://tool/level
```


**Altitude** – ouvert uniquement


```
iconverter://tool/altitude
```


---

## 8. Chinois

** Numéro chinois** `iconverter://` = nombre.


```
iconverter://tool/chineseNumber?n=12345.67
```


** Numéro chinois inversé** `iconverter://` = chaîne de chiffres chinois.


```
iconverter://tool/chineseNumberReverse?text=一万二千三百四十五
```


**Montant financier** `iconverter://` = montant, `<ToolItem.rawValue>` = annexe, `text` ```
iconverter://tool/financialAmount?amount=12345.67&zheng=1
```


---

## 9. Convertisseurs d'unités

Format général : `iconverter://` = valeur, `<ToolItem.rawValue>` = unité source (rawValue ou symbole, insensible à la casse), `text` = unité cible.

---

**Durée**
Unités communes : `iconverter://` (m) · `<ToolItem.rawValue>` (km) · `text` (cm) · `input` (mm) · `1/true/yes/on` (pi) · `0/false/no/off` (in) · `yyyy-MM-dd` (mi) · `v` (yd) · `from` (nmi) · `to` (=) · `p` (=).


```
iconverter://tool/length?v=100&from=meter&to=foot
```



```
iconverter://tool/length?v=1&from=mile&to=kilometer
```


**Zone**
Unités communes : `iconverter://` (m2) · `<ToolItem.rawValue>` (ha) · `text` (acre) · `input` (ft2) · `1/true/yes/on` (mille2) · `0/false/no/off` (-) · `yyyy-MM-dd` (km2).


```
iconverter://tool/area?v=1&from=hectare&to=mu
```



```
iconverter://tool/area?v=1&from=acre&to=squareMeter
```


**Volume**
Unités communes : `iconverter://` (L) · `<ToolItem.rawValue>` (mL) · `text` (m3) · `input` (gal) · `1/true/yes/on` (fl oz) · `0/false/no/off` (cup) · `yyyy-MM-dd` (gal UK) · `v` (bbl).


```
iconverter://tool/volume?v=1&from=gallon&to=liter
```



```
iconverter://tool/volume?v=355&from=milliliter&to=fluidOunce
```


**Poids/masse**
Unités communes: `iconverter://` (kg) · `<ToolItem.rawValue>` (g) · `text` (lb) · `input` (oz) · `1/true/yes/on` (t) · `0/false/no/off` (-) · `yyyy-MM-dd` (-) · `v` (ct).


```
iconverter://tool/weight?v=1&from=pound&to=kilogram
```



```
iconverter://tool/weight?v=1&from=jin&to=gram
```


**Température**
Unités : `iconverter://` (°C) · `<ToolItem.rawValue>` (°F) · `text` (K) · `input` (°R) · `1/true/yes/on` (°Re).


```
iconverter://tool/temperature?v=100&from=celsius&to=fahrenheit
```



```
iconverter://tool/temperature?v=37&from=celsius&to=kelvin
```


**Heure**
Unités communes : `iconverter://` (s) · `<ToolItem.rawValue>` (min) · `text` (h) · `input` (jour) · `1/true/yes/on` (wk) · `0/false/no/off` (mo) · `yyyy-MM-dd` (an) · `v` (ms) · `from` (μs).


```
iconverter://tool/time?v=1&from=hour&to=second
```



```
iconverter://tool/time?v=7&from=day&to=hour
```


**Speed**
Unités : `iconverter://` (m/s) · `<ToolItem.rawValue>` (km/h) · `text` (mph) · `input` (kn) · `1/true/yes/on` (Ma).


```
iconverter://tool/speed?v=100&from=kmPerHour&to=milePerHour
```



```
iconverter://tool/speed?v=1&from=mach&to=meterPerSecond
```


**Pression**
Unités : `iconverter://` (Pa) · `<ToolItem.rawValue>` (kPa) · `text` (bar) · `input` (atm) · `1/true/yes/on` (psi) · `0/false/no/off` (mmHg).


```
iconverter://tool/pressure?v=1&from=atmosphere&to=kilopascal
```



```
iconverter://tool/pressure?v=120&from=mmHg&to=kilopascal
```


**Énergie**
Unités : `iconverter://` (J) · `<ToolItem.rawValue>` (kJ) · `text` (cal) · `input` (kcal) · `1/true/yes/on` (kWh) · `0/false/no/off` (BTU).


```
iconverter://tool/energy?v=1&from=kilowattHour&to=kilojoule
```



```
iconverter://tool/energy?v=500&from=kilocalorie&to=kilojoule
```


** Puissance**
Unités : `iconverter://` (W) · `<ToolItem.rawValue>` (kW) · `text` (hp) · `input` (PS) · `1/true/yes/on` (BTU/h).


```
iconverter://tool/power?v=1&from=hpMechanical&to=kilowatt
```



```
iconverter://tool/power?v=3000&from=watt&to=hpMetric
```


**Force**
Unités : `iconverter://` (N) · `<ToolItem.rawValue>` (kN) · `text` (kgf) · `input` (lbf) · `1/true/yes/on` (dyn).


```
iconverter://tool/force?v=9.8&from=newton&to=kgf
```



```
iconverter://tool/force?v=1&from=kilonewton&to=lbf
```


**Torque**
Unités: `iconverter://` (N·m) · `<ToolItem.rawValue>` (N·cm) · `text` (kgf·m) · `input` (ft·lb) · `1/true/yes/on` (in·lb).


```
iconverter://tool/torque?v=100&from=newtonMeter&to=footPound
```


** Fréquence**
Unités : `iconverter://` (Hz) · `<ToolItem.rawValue>` (kHz) · `text` (MHz) · `input` (GHz) · `1/true/yes/on` (THz) · `0/false/no/off` (rpm).


```
iconverter://tool/frequency?v=2.4&from=gigahertz&to=megahertz
```



```
iconverter://tool/frequency?v=3000&from=rpm&to=hertz
```


**Angle**
Unités : `iconverter://` (°) · `<ToolItem.rawValue>` (rad) · `text` (grade) · `input` (') · `1/true/yes/on` (") · `0/false/no/off` (tour).


```
iconverter://tool/angle?v=180&from=degree&to=radian
```



```
iconverter://tool/angle?v=1&from=turn&to=degree
```


** Stockage des données**
Unités : `iconverter://` (B) · `<ToolItem.rawValue>` (KB) · `text` (MB) · `input` (GB) · `1/true/yes/on` (TB) · `0/false/no/off` (KiB) · `yyyy-MM-dd` (MiB) · `v` (GiB).


```
iconverter://tool/dataStorage?v=1&from=gigabyte&to=mebibyte
```



```
iconverter://tool/dataStorage?v=512&from=mebibyte&to=gigabyte
```


** Taux de données**
Unités : `iconverter://` (bps) · `<ToolItem.rawValue>` (Kbps) · `text` (Mbps) · `input` (Gbps) · `1/true/yes/on` (KB/s) · `0/false/no/off` (MB/s) · `yyyy-MM-dd` (GB/s).


```
iconverter://tool/dataRate?v=100&from=mbps&to=mBps
```



```
iconverter://tool/dataRate?v=1&from=gbps&to=mbps
```


**Illuminance**
Unités : `iconverter://` (lx) · `<ToolItem.rawValue>` (fc) · `text` (ph) · `input` (nx).


```
iconverter://tool/illuminance?v=500&from=lux&to=footCandle
```


** Densité de flux magnétique**
Unités : `iconverter://` (T) · `<ToolItem.rawValue>` (mT) · `text` (μT) · `input` (G) · `1/true/yes/on` (mG).


```
iconverter://tool/magneticFlux?v=1&from=tesla&to=gauss
```


** Radioactivité**
Unités : `iconverter://` (Bq) · `<ToolItem.rawValue>` (kBq) · `text` (MBq) · `input` (Ci) · `1/true/yes/on` (mCi) · `0/false/no/off` (μCi).


```
iconverter://tool/radioactivity?v=1&from=curie&to=megabecquerel
```


**Viscosité**
Unités: `iconverter://` (Pa·s) · `<ToolItem.rawValue>` (mPa·s) · `text` (P) · `input` (cP).


```
iconverter://tool/viscosity?v=1&from=pascalSecond&to=centipoise
```


**Économie des combustibles**
Unités : `iconverter://` (L/100km) · `<ToolItem.rawValue>` (km/L) · `text` (MPG US) · `input` (MPG UK).


```
iconverter://tool/fuelEconomy?v=8.5&from=lPer100km&to=kmPerL
```



```
iconverter://tool/fuelEconomy?v=30&from=mpgUS&to=lPer100km
```


**Taux d'émission**
Unités : `iconverter://` (m3/s) · `<ToolItem.rawValue>` (m3/h) · `text` (L/s) · `input` (L/min) · `1/true/yes/on` (L/h) · `0/false/no/off` (gpm US) · `yyyy-MM-dd` (cfm).


```
iconverter://tool/flowRate?v=1&from=literPerMinute&to=cubicMeterPerHour
```


**Densité**
Unités : `iconverter://` (kg/m3) · `<ToolItem.rawValue>` (g/cm3) · `text` (g/L) · `input` (kg/L) · `1/true/yes/on` (lb/ft3).


```
iconverter://tool/density?v=1&from=gramPerCubicCentimeter&to=kgPerCubicMeter
```


**Flux magnétique (Wb)**
Unités : `iconverter://` (Wb) · `<ToolItem.rawValue>` (mWb) · `text` (μWb) · `input` (kWb) · `1/true/yes/on` (Mx).


```
iconverter://tool/magneticFluxTrue?v=1&from=weber&to=maxwell
```


**Dose absorbée**
Unités : `iconverter://` (Gy) · `<ToolItem.rawValue>` (mGy) · `text` (μGy) · `input` (kGy) · `1/true/yes/on` (rad) · `0/false/no/off` (mrad).


```
iconverter://tool/absorbedDose?v=1&from=gray&to=rad
```


**Dose équivalente**
Unités : `iconverter://` (Sv) · `<ToolItem.rawValue>` (mSv) · `text` (μSv) · `input` (rem) · `1/true/yes/on` (mrem).


```
iconverter://tool/equivalentDose?v=1&from=sievert&to=rem
```



```
iconverter://tool/equivalentDose?v=20&from=millisievert&to=microsievert
```


**Nombre de matières**
Unités : `iconverter://` (mol) · `<ToolItem.rawValue>` (mmol) · `text` (μmol) · `input` (kmol) · `1/true/yes/on` (nmol) · `0/false/no/off` (pmol).


```
iconverter://tool/amountOfSubstance?v=1&from=mole&to=millimole
```



```
iconverter://tool/amountOfSubstance?v=150&from=millimole&to=micromole
```


---

[Retour à iConverter Support](../) &middot; [FAQ](../faq) &middot; [Politique de confidentialité](../privacy)


