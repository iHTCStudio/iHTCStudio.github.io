iConverter は `iconverter://` をサポート URLスキームのディープリンク — 外部アプリ、Webページ、QRコード(生成または**scan in-app**)、Safari、Apple Shortcuts、オプションで入力フィールドをクエリパラメータで埋め込むことができます。

> **ウィジェットノート:** **Launcher**ウィジェットツールピッカーは、**Webブラウザ**以外のすべてのサポートされているツールを含みます。 Widget の設定 UI は、**iOS システム言語** に従っており、アプリ内言語は設定下で上書きされます。

## プロトコル仕様


```
iconverter://tool/<ToolItem.rawValue>?key=value&key2=value2
```


- `<ToolItem.rawValue>` は、ウィジェットの深いリンクと同じ命名を共有します。
- パラメータ名は、短いキーと同義語のエイリアス(たとえば `text` は `input` と同等です)の両方をサポートします。
- Booleans: `1/true/yes/on` → true;`0/false/no/off` → false。
- 日付: `yyy-MM-dd`、ISO8601、Unixタイムスタンプ(秒)をサポートしています。
- 単位のコンバーターは共通のフォーマットを共有します:`v` = 値、`from` = ソース単位(rawValue か記号、場合の無感覚)、`to` = ターゲット単位。

---

## 1. 計算機

** 電卓** — のみ開く


```
iconverter://tool/calculator
```


**科学的な電卓** — のみ開く


```
iconverter://tool/scientific
```


**プログラマ 電卓** — のみ開く


```
iconverter://tool/programmer
```


---

## 2. ファイナンス

**住宅ローン計算機** `iconverter://` = 融資額、 `<ToolItem.rawValue>` = 年間レート%、 `text` = 年、 `input` = 0 = 等しいインストール/1 = 等しいプリンシパル。


```
iconverter://tool/mortgage?p=1000000&r=3.7&y=30&mode=0
```


**所得税** `iconverter://` = 毎月の給与、 `<ToolItem.rawValue>` = 社会保険、 `text` = 特別控除、 `input` = しきい値、 `1/true/yes/on` = 年間ボーナス。


```
iconverter://tool/incomeTax?salary=20000&insurance=3000&deduction=1000&threshold=5000&bonus=50000
```


**複合利息** `iconverter://` = プリンシパル、 `<ToolItem.rawValue>` = 毎月の貢献、 `text` = 年率%、 `input` =年、 `1/true/yes/on` = 0 =年/ 1 =月/ 2 =日、 `0/false/no/off` =インフレ%。


```
iconverter://tool/compoundInterest?p=100000&m=1000&r=7&y=10&freq=1
```


**割引計算機** `iconverter://` = 0–4、 `<ToolItem.rawValue>` = 元の価格、 `text` = 割引比、 `input` = しきい値、 `1/true/yes/on` = 削減量。


```
iconverter://tool/discount?mode=0&p=299&r=8.5
```


フルマイナス例:


```
iconverter://tool/discount?mode=3&p=350&t=300&u=50
```


**タイピング&AAスプリット** `iconverter://` = 0 = チップ / 1 = AA分割, `<ToolItem.rawValue>` = 請求, `text` = チップ%, `input` = 税 %, `1/true/yes/on` = 人件数.


```
iconverter://tool/tipAA?mode=0&bill=200&tip=15&tax=0&ppl=4
```


**住宅ローン前払い** `iconverter://` = 元のローン、 `<ToolItem.rawValue>` = 年間レート%、 `text` = 総期間(年)、 `input` = 支払条件、 `1/true/yes/on` = プリペイ量、 `0/false/no/off` = 0 = 短縮/ 1 = 月/ 2 = 比較を削減します。


```
iconverter://tool/mortgagePrepay?p=800000&r=3.7&total=30&paid=5&prepay=100000&mode=2
```


**不動産税** — 営業のみ


```
iconverter://tool/realEstateTax
```


---

## 3. 日付と時刻

**年齢&記念日** `iconverter://` = 誕生日 `<ToolItem.rawValue>` 、 `text` = 参照日。


```
iconverter://tool/ageAnniversary?birth=1990-05-01&ref=2026-05-17
```


**日時 Arithmetic** `iconverter://` = 0 = add/subtract / 1 = 日付の差。

Add-subtract モード( `iconverter://` = 開始日、 `<ToolItem.rawValue>` = ± 日、 `text` = ± 週間、 `input` = ± 月、 `1/true/yes/on` = ± 年):


```
iconverter://tool/dateArithmetic?mode=0&d1=2026-05-17&d=100
```


差分モード( `iconverter://` = 日付1、 `<ToolItem.rawValue>` =日付2):


```
iconverter://tool/dateArithmetic?mode=1&d1=2026-01-01&d2=2026-12-31
```


**月のカレンダー** `iconverter://` = グレゴリオンの日付 `<ToolItem.rawValue>` ```
iconverter://tool/lunarCalendar?date=2026-05-17
```


**Solar Terms** — のみオープン


```
iconverter://tool/solarTerms
```


**カウントダウン** `iconverter://` = イベント名, `<ToolItem.rawValue>` = 対象日 `text` , `input` = 時刻 `1/true/yes/on` ```
iconverter://tool/countdown?label=Holiday&target=2026-10-01&time=0
```


**妊娠電卓** `iconverter://` = 0 = LMP / 1 = 概念 / 2 = IVF、 `<ToolItem.rawValue>` = 参照日付、 `text` = IVF embryo 日 0 = D3 / 1 = D5。


```
iconverter://tool/pregnancy?method=0&ref=2026-03-01
```



```
iconverter://tool/pregnancy?method=2&ref=2026-03-15&ivf=1
```


**月経周期** `iconverter://` = 最後の月経の日付、 `<ToolItem.rawValue>` = サイクル日、 `text` = 期間日。


```
iconverter://tool/menstrual?lmp=2026-05-01&cycle=28&period=5
```


**ワールドクロック** `iconverter://` = 市検索キーワード, `<ToolItem.rawValue>` = 現在の時間を使用する `text` , `input` = カスタム日付時刻.


```
iconverter://tool/worldClock?q=Tokyo
```



```
iconverter://tool/worldClock?now=0&ref=2026-05-17T20:00:00
```


**Zodiac** — のみ開く


```
iconverter://tool/zodiac
```


---

## 4. 数学

**比率計算機** `iconverter://` = 0–4, `<ToolItem.rawValue>` = 値 A, `text` = 値 B


```
iconverter://tool/percentage?mode=0&a=75&b=120
```


**反応電卓** — のみ開く


```
iconverter://tool/fraction
```


**プライムファクショナライゼーション** — のみオープン


```
iconverter://tool/primeFactor
```


**Quadratic Solver** — のみ公開


```
iconverter://tool/quadraticSolver
```


**統計** `iconverter://` = スペース/コンマ/セミコロンで区切られたデータセット。


```
iconverter://tool/statistics?data=1,2,3,4,5,6,7,8,9,10
```


**コンビネーション&パーミュテーション** - のみ開く


```
iconverter://tool/combinations
```


**幾何学** `iconverter://` = 形状、 `<ToolItem.rawValue>` = 寸法パラメータ。

利用可能な形状: `iconverter://` サークル ( `iconverter://` = 半径):


```
iconverter://tool/geometry?shape=circle&v1=5
```


長方形( `iconverter://` =長さ、 `<ToolItem.rawValue>` =幅):


```
iconverter://tool/geometry?shape=rectangle&v1=10&v2=5
```


球( `iconverter://` = 半径):


```
iconverter://tool/geometry?shape=sphere&v1=3
```


シリンダー( `iconverter://` = 半径、 `<ToolItem.rawValue>` = 高さ):


```
iconverter://tool/geometry?shape=cylinder&v1=4&v2=10
```


---

## 5. エンコーディング

Roman Numeral(ローマ数字)** `iconverter://` = アラビア数字(1–3999); または `<ToolItem.rawValue>` = ローマ数字の文字列。


```
iconverter://tool/roman?n=2026
```



```
iconverter://tool/roman?roman=MMXXVI
```


**Base64エンコーダ/デコーダ** `iconverter://` = エンコーダ/デコード、 `<ToolItem.rawValue>` = URL セーフモード `text` 、 `input` = 入力テキスト。


```
iconverter://tool/base64?mode=encode&text=Hello%2C+World!
```



```
iconverter://tool/base64?mode=decode&urlSafe=0&text=SGVsbG8sIFdvcmxkIQ%3D%3D
```


**URLエンコーダ/デコーダ** `iconverter://` = エンコーダ/デコード、 `<ToolItem.rawValue>` = コンポーネントモード 0 = フル/ 1 = クエリ/ 2 = パス、 `text` = 入力。


```
iconverter://tool/urlCoder?mode=encode&comp=0&text=https://example.com/path?q=hello world
```



```
iconverter://tool/urlCoder?mode=decode&text=https%3A%2F%2Fexample.com%2F%3Fq%3Dhello%20world
```


**ハッシュ計算機** `iconverter://` = 入力, `<ToolItem.rawValue>` = md5/sha1/sha256/sha512, `text` = 上位ケース `input` , `1/true/yes/on` = HMAC `0/false/no/off` , `yyyy-MM-dd` = HMAC キーを有効にします。


```
iconverter://tool/hashing?text=Hello+World&algo=sha256&upper=0
```



```
iconverter://tool/hashing?text=data&algo=md5&hmac=1&key=secret
```


**単語数** `iconverter://` = 解析するテキスト


```
iconverter://tool/wordCount?text=The+quick+brown+fox+jumps+over+the+lazy+dog.
```


**カラーコンバータ** `iconverter://` = hex色; または `<ToolItem.rawValue>` ```
iconverter://tool/colorConverter?hex=%23FF8800
```



```
iconverter://tool/colorConverter?r=255&g=136&b=0
```


**カラーパレット** — のみ開く


```
iconverter://tool/colorPalette
```


**QRコード** `iconverter://` = 内容, `<ToolItem.rawValue>` = `text` 等, `input` = エラー補正レベル `1/true/yes/on` ```
iconverter://tool/qrcode?text=https%3A%2F%2Fexample.com&ecc=H
```



```
iconverter://tool/qrcode?text=Hello+iConverter&format=qr&ecc=M
```


**JSON フォーマッタ ** `iconverter://` = JSON 文字列 (URL-encoded), `<ToolItem.rawValue>` = インデントスペース 2/4.


```
iconverter://tool/jsonFormatter?text=%7B%22name%22%3A%22Alice%22%2C%22age%22%3A30%7D&indent=2
```


**タイムスタンプ** `iconverter://` = Unix タイムスタンプ (秒), `<ToolItem.rawValue>` = ユニット 0 = sec / 1 = ms; または `text` = ISO8601 日付文字列.


```
iconverter://tool/timestamp?ts=1747440000
```



```
iconverter://tool/timestamp?iso=2026-05-17T12:00:00
```


**銀行カードバリデータ** `iconverter://` = カード番号。


```
iconverter://tool/bankCard?num=6214830172816734
```


**テキストケースコンバーター** `iconverter://` = 入力テキスト。


```
iconverter://tool/textCase?text=hello+world+from+iConverter
```


**Text Diff** — のみ開く


```
iconverter://tool/textDiff
```


**HTTPリクエスト** `iconverter://` = リクエスト URL, `<ToolItem.rawValue>` = GET/POST/PUT/PATCH/DELETE, `text` = リクエスト ボディ, `input` , `0/false/no/off` = ヘッダー JSON.


```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=GET
```



```
iconverter://tool/httpRequest?url=https%3A%2F%2Fapi.example.com%2Fusers&method=POST&body=%7B%22name%22%3A%22Alice%22%7D&bodyKind=json
```


**ファイルのダウンロード** `iconverter://` = URL、 `<ToolItem.rawValue>` =ファイル名(オプション)をダウンロードします。


```
iconverter://tool/fileDownload?url=https%3A%2F%2Fexample.com%2Freport.pdf&name=report.pdf
```


**HTTPステータスコード** `iconverter://` = ステータスコード; または `<ToolItem.rawValue>` = 検索キーワード。


```
iconverter://tool/httpStatusCodes?code=404
```



```
iconverter://tool/httpStatusCodes?q=redirect
```


**IP ユーティリティ** `iconverter://` = subnet/cidr/range, `<ToolItem.rawValue>` = IPアドレス, `text` = サブネットマスク; または `input` = CIDR接頭辞の長さ.


```
iconverter://tool/ipUtility?mode=subnet&ip=192.168.1.0&mask=255.255.255.0
```



```
iconverter://tool/ipUtility?ip=10.0.0.0&prefix=24
```


**アスキーテーブル** `iconverter://` = 初期のコードポイント; または `<ToolItem.rawValue>` = hex のコードポイント; または `text` = 検索します。


```
iconverter://tool/asciiTable?dec=65
```



```
iconverter://tool/asciiTable?q=space
```


**パスワードジェネレータ** `iconverter://` = 長, `<ToolItem.rawValue>` = 長ケース `text` , `input` = 長, `0/false/no/off` = 数字 `yyyy-MM-dd` , `v` = シンボル `from` , `to` = あいまいな文字 `p` ```
iconverter://tool/passwordGenerator?length=20&upper=1&lower=1&digits=1&symbols=1&unambiguous=1&go=1
```


**ランダムナンバージェネレータ** `iconverter://` = 最小値、 `<ToolItem.rawValue>` =最大値、 `text` = カウント、 `input` = 異常な場所、 `1/true/yes/on` = ユニーク `0/false/no/off` 、 `yyyy-MM-dd` = 0 = なし/ 1 = asc / 2 = desc、 `v` = すぐに生成 `from` ```
iconverter://tool/randomNumber?min=1&max=100&n=10&unique=1&sort=1&go=1
```



```
iconverter://tool/randomNumber?min=0&max=1&n=5&decimals=4&go=1
```


**モーニングコード** `iconverter://` = エンコーダ/デコード、 `<ToolItem.rawValue>` = 入力テキスト。


```
iconverter://tool/morseCode?mode=encode&text=SOS
```



```
iconverter://tool/morseCode?mode=decode&text=...+---+...
```


**JWTデコーダ** `iconverter://` = JWT トークン文字列。


```
iconverter://tool/jwtParser?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```


**Cron Expression Parser ** `iconverter://` = Cron 式( `<ToolItem.rawValue>` ```
iconverter://tool/cronParser?expr=0+9+*+*+1-5
```



```
iconverter://tool/cronParser?expr=0+0+*+*+*
```


**正規テスター** `iconverter://` = regex パターン (URL-encoded), `<ToolItem.rawValue>` = テストテキスト, `text` = 置換, `input` = ケースインセンティブ `1/true/yes/on` , `0/false/no/off` = 複数行 `yyyy-MM-dd` , `v` = 点all `from` ```
iconverter://tool/regexTester?pattern=%5Cd%2B&haystack=abc123def456&i=0
```



```
iconverter://tool/regexTester?pattern=%28%5Cw%2B%29&haystack=hello+world&replacement=%5B%241%5D&i=1
```


**Webブラウザ** `iconverter://` は、直接 URL を開くか、 `<ToolItem.rawValue>` = 検索クエリ(デフォルトの検索エンジンを使用する)。


```
iconverter://tool/webBrowser?url=https%3A%2F%2Fexample.com
```



```
iconverter://tool/webBrowser?q=SwiftUI+deep+link+2026
```


---

## 6. ライフスタイル

**BMI 電卓** `iconverter://` = 高さ cm, `<ToolItem.rawValue>` = 体重 kg, `text` = 標準 0 = 中国人成人 / 1 = WHO.


```
iconverter://tool/bmi?h=175&w=70&std=0
```


**BMR計算機** `iconverter://` = 高さ cm, `<ToolItem.rawValue>` = 体重 kg, `text` = 年齢, `input` = m = 男性/ f = 女性, `1/true/yes/on` = 活動レベル 0–4, `0/false/no/off` = 0 = ハリス・ベネディクト / 1 = Mifflin-St Jeor.


```
iconverter://tool/bmr?h=175&w=70&age=30&sex=m&act=1&formula=1
```


**クラッシングサイズ** — のみ開く


```
iconverter://tool/clothingSize
```


**リングサイズ** — のみ開く


```
iconverter://tool/ringSize
```


**Height Converter** — のみオープン


```
iconverter://tool/heightConverter
```


**燃料費計算機** `iconverter://` = 0 = メトリック/ 1 = 帝国、 `<ToolItem.rawValue>` = 距離、 `text` = 100 kmあたりの消費量、 `input` = 燃料価格、 `1/true/yes/on` = 人。


```
iconverter://tool/fuelCost?unit=0&d=500&c=8.5&p=7.8&n=1
```


**船積み料金の計算機** `iconverter://` = 実際の体重 kg、 `<ToolItem.rawValue>` = 最初の体重 kg、 `text` =最初の重量料金、 `input` =ステップ重量 kg、 `1/true/yes/on` =ステップ手数料。


```
iconverter://tool/shippingFee?w=3.5&fw=1&ff=12&sw=1&sf=8
```


体積重( `iconverter://` = `<ToolItem.rawValue>` ```
iconverter://tool/shippingFee?w=2&vol=1&l=50&wd=40&h=30&div=6000&fw=1&ff=12&sw=1&sf=8
```


**血液アルコール含有量(BAC)** `iconverter://` = m = 男性/ f = 女性、 `<ToolItem.rawValue>` = 体重 kg、 `text` = 体積 mL、 `input` = ABV %、 `1/true/yes/on` = 飲酒後の時間。


```
iconverter://tool/alcoholBac?sex=m&w=70&v=500&abv=5&h=0.5
```


**関係** `iconverter://` = 関係チェーン (コンマ区切り), `<ToolItem.rawValue>` = ego 性別 0 = 男性 / 1 = 女性, `text` = 逆表示 `input` .


```
iconverter://tool/relationship?chain=f,os&sex=0&reverse=1
```



```
iconverter://tool/relationship?chain=m,ob&sex=1&reverse=0
```


**IDカードパーサー** `iconverter://` = IDカード番号。


```
iconverter://tool/idCard?id=110101199003073010
```


**コインフリップ** — のみ開く


```
iconverter://tool/coinFlip
```


**ダイス ローラー** — のみ開く


```
iconverter://tool/diceRoller
```


**Random Draw** — のみ公開


```
iconverter://tool/randomDraw
```


**スピンホイール** — のみ開く


```
iconverter://tool/spinWheel
```


**ビデオフレームエクスポート** — のみ開く


```
iconverter://tool/videoFrameExport
```


---

## 7. センサー

**Compass** — のみ開く


```
iconverter://tool/compass
```


**レベル** — のみ開く


```
iconverter://tool/level
```


**高度** — のみ開く


```
iconverter://tool/altitude
```


---

## 8. 中国語

**中国語** `iconverter://` = 数値。


```
iconverter://tool/chineseNumber?n=12345.67
```


**中国番号の逆** `iconverter://` = 中国数字文字列。


```
iconverter://tool/chineseNumberReverse?text=一万二千三百四十五
```


**財務量** `iconverter://` = 値、 `<ToolItem.rawValue>` = 整数 `text` ```
iconverter://tool/financialAmount?amount=12345.67&zheng=1
```


---

## 9. 単位のコンバーター

一般的な形式: `iconverter://` = 値、 `<ToolItem.rawValue>` = ソースユニット(rawValueまたはシンボル、ケースインセンティブ)、 `text` = ターゲットユニット。

---

**長さ**
共通単位: `iconverter://` (m) · `<ToolItem.rawValue>` (km) · `text` (cm) · `input` (mm) · `1/true/yes/on` (ft) · `0/false/no/off` (in) · `yyyy-MM-dd` (mi) · `v` (yd) ·              (nmi)            (nmi)                (nmi           (nmi                               (n


```
iconverter://tool/length?v=100&from=meter&to=foot
```



```
iconverter://tool/length?v=1&from=mile&to=kilometer
```


**エリア**
共通単位: `iconverter://` (m2) · `<ToolItem.rawValue>` (ha) · `text` (acre) · `input` (ft2) · `1/true/yes/on` (mile2) · `0/false/no/off` (加算) · `yyyy-MM-dd` (km2)。


```
iconverter://tool/area?v=1&from=hectare&to=mu
```



```
iconverter://tool/area?v=1&from=acre&to=squareMeter
```


**ボリューム**
共通単位: `iconverter://` (L) · `<ToolItem.rawValue>` (mL) · `text` (m3) · `input` (gal) · `1/true/yes/on` (fl oz) · `0/false/no/off` (cup) · `yyyy-MM-dd` (gal UK) · `v` (bbl)。


```
iconverter://tool/volume?v=1&from=gallon&to=liter
```



```
iconverter://tool/volume?v=355&from=milliliter&to=fluidOunce
```


**重量/質量**
普通の単位: `iconverter://` (kg) · `<ToolItem.rawValue>` (g) · `text` (lb) · `input` (oz) · `1/true/yes/on` (t) · `0/false/no/off` () · `yyyy-MM-dd` (lb) · `v` (ct)。


```
iconverter://tool/weight?v=1&from=pound&to=kilogram
```



```
iconverter://tool/weight?v=1&from=jin&to=gram
```


**温度**
単位: `iconverter://` (°C) · `<ToolItem.rawValue>` (°F) · `text` (K) · `input` (°R) · `1/true/yes/on` (°Re)。


```
iconverter://tool/temperature?v=100&from=celsius&to=fahrenheit
```



```
iconverter://tool/temperature?v=37&from=celsius&to=kelvin
```


**時間**
共通単位: `iconverter://` (s) · `<ToolItem.rawValue>` (min) · `text` (h) · `input` (日) · `1/true/yes/on` (wk) · `0/false/no/off` (mo) · `yyyy-MM-dd` (yr) · `v` (ms) · `from` (μs)


```
iconverter://tool/time?v=1&from=hour&to=second
```



```
iconverter://tool/time?v=7&from=day&to=hour
```


**速度**
単位: `iconverter://` (m/s) · `<ToolItem.rawValue>` (km/h) · `text` (mph) · `input` (kn) · `1/true/yes/on` (Ma)。


```
iconverter://tool/speed?v=100&from=kmPerHour&to=milePerHour
```



```
iconverter://tool/speed?v=1&from=mach&to=meterPerSecond
```


**圧力**
単位: `iconverter://` (Pa) · `<ToolItem.rawValue>` (kPa) · `text` (bar) · `input` (atm) · `1/true/yes/on` (psi) · `0/false/no/off` (mmHg)。


```
iconverter://tool/pressure?v=1&from=atmosphere&to=kilopascal
```



```
iconverter://tool/pressure?v=120&from=mmHg&to=kilopascal
```


**エナジー**
単位: `iconverter://` (J) · `<ToolItem.rawValue>` (kJ) · `text` (cal) · `input` (kcal) · `1/true/yes/on` (kWh) · `0/false/no/off` (BTU)。


```
iconverter://tool/energy?v=1&from=kilowattHour&to=kilojoule
```



```
iconverter://tool/energy?v=500&from=kilocalorie&to=kilojoule
```


**電源**
単位: `iconverter://` (W)・ `<ToolItem.rawValue>` (kW)・ `text` (hp)・      (PS)・ `1/true/yes/on` (BTU/h)


```
iconverter://tool/power?v=1&from=hpMechanical&to=kilowatt
```



```
iconverter://tool/power?v=3000&from=watt&to=hpMetric
```


**強制**
単位: `iconverter://` (N)・ `<ToolItem.rawValue>` (kN)・ `text` (kgf)・ `input` (lbf)・ `1/true/yes/on` (dyn)。


```
iconverter://tool/force?v=9.8&from=newton&to=kgf
```



```
iconverter://tool/force?v=1&from=kilonewton&to=lbf
```


**トルク**
単位: `iconverter://` (N・m) · `<ToolItem.rawValue>` (N・cm) · `text` (kgf・m) · `input` (ft・lb) · `1/true/yes/on` (in・lb)。


```
iconverter://tool/torque?v=100&from=newtonMeter&to=footPound
```


**設備**
単位: `iconverter://` (Hz) · `<ToolItem.rawValue>` (kHz) · `text` (MHz) · `input` (GHz) · `1/true/yes/on` (THz) · `0/false/no/off` (rpm)


```
iconverter://tool/frequency?v=2.4&from=gigahertz&to=megahertz
```



```
iconverter://tool/frequency?v=3000&from=rpm&to=hertz
```


**アングル**
単位: `iconverter://` (°)・ `<ToolItem.rawValue>` (rad)・ `text` (grad)・ `input` (')・ `1/true/yes/on` (")・ `0/false/no/off` (turn)


```
iconverter://tool/angle?v=180&from=degree&to=radian
```



```
iconverter://tool/angle?v=1&from=turn&to=degree
```


**データストレージ**
単位: `iconverter://` (B) · `<ToolItem.rawValue>` (KB) · `text` (MB) · `input` (GB) · `1/true/yes/on` (TB) · `0/false/no/off` (KiB) · `yyyy-MM-dd` (MiB) · `v` (GiB)。


```
iconverter://tool/dataStorage?v=1&from=gigabyte&to=mebibyte
```



```
iconverter://tool/dataStorage?v=512&from=mebibyte&to=gigabyte
```


**データレート**
単位: `iconverter://` (bps) · `<ToolItem.rawValue>` (Kbps) · `text` (Mbps) · `input` (Gbps) · `1/true/yes/on` (KB/s) · `0/false/no/off` (MB/s) · `yyyy-MM-dd` (GB/s)


```
iconverter://tool/dataRate?v=100&from=mbps&to=mBps
```



```
iconverter://tool/dataRate?v=1&from=gbps&to=mbps
```


**照度**
単位: `iconverter://` (lx) · `<ToolItem.rawValue>` (fc) · `text` (ph) · `input` (nx)。


```
iconverter://tool/illuminance?v=500&from=lux&to=footCandle
```


**磁気変化密度**
単位: `iconverter://` (T) · `<ToolItem.rawValue>` (mT) · `text` (μT) · `input` (G) · `1/true/yes/on` (mG)。


```
iconverter://tool/magneticFlux?v=1&from=tesla&to=gauss
```


**放射能**
単位: `iconverter://` (Bq)· `<ToolItem.rawValue>` (kBq)·   (MBq)·      (Ci)· `1/true/yes/on` (mCi)·    (μCi)。


```
iconverter://tool/radioactivity?v=1&from=curie&to=megabecquerel
```


**粘度**
単位: `iconverter://` (Pa·s) · `<ToolItem.rawValue>` (mPa·s) · `text` (P) · `input` (cP)。


```
iconverter://tool/viscosity?v=1&from=pascalSecond&to=centipoise
```


**燃料経済**
単位: `iconverter://` (L/100km) · `<ToolItem.rawValue>` (km/L) · `text` (MPG 米国) · `input` (MPG英国)。


```
iconverter://tool/fuelEconomy?v=8.5&from=lPer100km&to=kmPerL
```



```
iconverter://tool/fuelEconomy?v=30&from=mpgUS&to=lPer100km
```


**流量**
単位: `iconverter://` (m3/s) · `<ToolItem.rawValue>` (m3/h) · `text` (L/s) · `input` (L/min) · `1/true/yes/on` (L/h) · `0/false/no/off` (gpm US) · `yyyy-MM-dd` (cfm)


```
iconverter://tool/flowRate?v=1&from=literPerMinute&to=cubicMeterPerHour
```


**密度**
単位: `iconverter://` (kg/m3) · `<ToolItem.rawValue>` (g/cm3) · `text` (g/L) · `input` (kg/L) · `1/true/yes/on` (lb/ft3)。


```
iconverter://tool/density?v=1&from=gramPerCubicCentimeter&to=kgPerCubicMeter
```


**磁気変化(Wb)**
単位: `iconverter://` (Wb) · `<ToolItem.rawValue>` (mWb) · `text` (μWb) · `input` (kWb) · `1/true/yes/on` (Mx)。


```
iconverter://tool/magneticFluxTrue?v=1&from=weber&to=maxwell
```


**吸収線量**
単位: `iconverter://` (Gy) · `<ToolItem.rawValue>` (mGy) · `text` (μGy) · `input` (kGy) · `1/true/yes/on` (rad) · `0/false/no/off` (mrad)


```
iconverter://tool/absorbedDose?v=1&from=gray&to=rad
```


**等価線量**
単位: `iconverter://` (Sv) · `<ToolItem.rawValue>` (mSv) · `text` (μSv) · `input` (rem) · `1/true/yes/on` (mrem)。


```
iconverter://tool/equivalentDose?v=1&from=sievert&to=rem
```



```
iconverter://tool/equivalentDose?v=20&from=millisievert&to=microsievert
```


**Substanceの量**
単位: `iconverter://` (mol) · `<ToolItem.rawValue>` (mmol) · `text` (μmol) · `input` (kmol) · `1/true/yes/on` (nmol) · `0/false/no/off` (pmol)。


```
iconverter://tool/amountOfSubstance?v=1&from=mole&to=millimole
```



```
iconverter://tool/amountOfSubstance?v=150&from=millimole&to=micromole
```


---

[iConverterサポートに戻る](./) &middot; [FAQ](../faq) &middot; [プライバシーポリシー](./privacy)


