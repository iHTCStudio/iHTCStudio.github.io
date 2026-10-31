iHTC Studio ("biz", "bize" veya "bizim") iLinux'u ("Linux" olarak da bilinir) oluşturdu. Bu sayfa, uygulamamızı kullandığınızda kişisel verilerinizin toplanması, kullanılması ve ifşa edilmesine ilişkin politikalarımız hakkında sizi bilgilendirir.

## Özet

**iLinux analiz toplamaz veya kişisel verileri satmaz.** Komut kitaplıkları cihazınızda tamamen çevrimdışı çalışır. İsteğe bağlı **iCloud senkronizasyonu** (etkinleştirildiğinde ve iCloud'da oturum açtığınızda) favorileri, sınav ilerlemesini, temayı ve görüntüleme tercihlerini Apple Kimliğiniz altındaki **iCloud Anahtar-Değer Depolama alanınızda** saklar — iHTC Studio bu veriler için bir arka uç sunucusu çalıştırmaz.

## Veri Toplama

Analitik, reklam veya izleme işletmiyoruz. Özellikle:

- **Hiçbir kişisel bilgi** iHTC Studio tarafından toplanmaz (isim, e-posta, telefon numarası veya iHTC Studio hesabı yok).
- **Kullanım analitiği yoktur** veya kilitlenme raporlama SDK'ları entegre değildir.
- **Öğrenim verileriniz** (favoriler, sınav puanları, yanlış cevaplar) cihazlarınızda kalır ve senkronizasyonu etkinleştirirseniz iHTC Studio sunucularında değil **Apple iCloud**'da kalır.
- **Uygulamada çerez veya üçüncü taraf izleyici yoktur**.

## Uygulama Nasıl Çalışır?

iLinux, kullanıcı tarafından oluşturulan tüm verileri (favoriler, son görünümler, sınav oturumu sonuçları, yanlış cevap kayıtları, kabuk platformu tercihi, favori kapsamı, widget komut kitaplığı ve uygulama tercihleri) yerel olarak cihazınızda saklar:

- Tüm komut verileri (**Linux, CMD ve PowerShell** için JSON özetleri ve Markdown belgeleri) uygulamanın içinde paketlenir ve hiçbir zaman herhangi bir harici sunucudan getirilmez.
- Komutlara göz atmak veya sınavlara girmek için internet bağlantısı gerekmez.
- İsteğe bağlı **iCloud senkronizasyonu**, iCloud'da oturum açtığınızda ve senkronizasyonu etkin bıraktığınızda Apple'ın **NSUbiquitousKeyValueStore** özelliğini kullanır. Ayarlar'da her cihaz için bunu kapatabilirsiniz.
- Uygulamanın içinden harici bağlantıları açmak (ör. Geri Bildirim bölümünde bir URL'ye dokunmak) standart iOS ağ oluşturma davranışını kullanır; bağlantılı sayfa herhangi bir iHTC Studio sunucusu aracılığıyla değil, cihazınız tarafından doğrudan ana bilgisayardan yüklenir.
- The optional **App Store version check** (`AppStoreVersionChecker`) makes a single read-only request to the public iTunes Lookup API to compare the installed version with the latest release. No personal data is sent in this request.

## İzinler

iLinux, **Fotoğraf Kitaplığı** erişimini yalnızca Fotoğraflar'a **bir paylaşım kartı kaydetmeyi veya ekran görüntüsünü komut etmeyi** seçtiğinizde ister. Hiçbir kamera, mikrofon, konum veya kişi erişimi gerekmez.

## Veri Depolama

| Veri | Depolama Konumu |
|------|-----------------|
| Favoriler, son görüntülemeler, yanlış cevap kayıtları, öğrenme durumu (platform başına) | Cihazınızdaki Yerel Kullanıcı Varsayılanları / Uygulama Grubu |
| Sınav ilerlemesi ve günlük oturum sonuçları (tarihe ve kabuk platformuna göre anahtarlanmıştır) | Cihazınızdaki yerel uygulama sanal alanı |
| Tema, dil, liste/ızgara düzeni, kabuk platformu, sık kullanılanlar kapsamı, widget kitaplığı | Cihazınızdaki Yerel Kullanıcı Varsayılanları / Uygulama Grubu |
| iCloud senkronizasyon aynası (isteğe bağlı) | Apple iCloud Anahtar-Değer Depolaması (`crossSync.*` tuşları) — favoriler, test ilerleme durumu, tema, uygulama tercihleri |
| Widget anlık görüntüsü (yalnızca iOS/iPad) | Uygulama Grubu kapsayıcısı (`group.com.iHTCboy.iLinuxs`) |

iHTC Studio tarafından çalıştırılan herhangi bir sunucuda hiçbir veri depolanmaz. İsteğe bağlı iCloud verileri, Apple'ın iCloud koşullarına tabidir.

## iCloud Senkronizasyonu (İsteğe bağlı)

**iCloud Senkronizasyonu** etkinleştirildiğinde ve iCloud'da oturum açtığınızda:

- Senkronize edilen veriler: **öğrenme ilerlemesi** (favoriler, en son olanlar, öğrenme durumu, test puanları, yanlış cevap kayıtları), **tema** ve **uygulama tercihleri** (dil, kabuk platformu, favorilerin kapsamı, liste/tablo ayarları).
- Depolama: Apple Kimliğinizle ilişkili Apple **iCloud Anahtar-Değer Depolama Alanı**.
- Birleştirme: Çakışan güncellemeler cihazda birleştirilir (ör. favoriler birliği, en son zaman damgaları).
- Devre dışı bırakma: herhangi bir cihazda **Ayarlar → iCloud Senkronizasyonu** bölümünden devre dışı bırakın; bu cihaz yüklemeyi ve birleştirmeyi durdurur ancak yerel verileri tutar.
- iHTC Studio, iCloud kapsayıcınızı okuyamıyor.

## Uygulama Grubu (Widget Uzantısı — yalnızca iOS/iPad)

iLinux, Ana Ekran widget uzantısıyla az miktarda veri paylaşmak için bir Uygulama Grubu (`group.com.iHTCboy.iLinuxs`) kullanır. Bu veriler şunları içerir:

- Seçilen içerik dili kodu (ör. `en`, `zh-Hans`)
- Bir tema rengi anlık görüntüsü (vurgu onaltılı ve degrade değerleri)
- Widget ekranı için öğrenme ilerlemenizin bir özeti (favoriler sayısı, sınav istatistikleri)
- Seçilen **widget komut kitaplığı** (Linux / CMD / PowerShell)
- Günlük Komut widget'ı karıştırma sayacı (sonraki öne çıkan komutu seçmek için kullanılan basit bir tamsayı)

Bu veriler yalnızca cihazınızdaki paylaşılan bir kaba yazılır ve hiçbir zaman hiçbir yere iletilmez.

## iLinux Ne Değildir?

iLinux kabuk komutlarını çalıştırmaz, SSH oturumlarını açmaz veya uzak sistemlere erişmez. Başka bir yere yazabileceğiniz hiçbir komut satırı girişi bu uygulama tarafından toplanmaz.

## Uygulama İçi Satın Alma

iLinux isteğe bağlı bir ipucu/satın alma seçeneği içerir. Tüm ödeme işlemleri yalnızca **Apple'ın StoreKit çerçevesi** tarafından gerçekleştirilir. iHTC Studio, herhangi bir ödeme kartı bilgisini veya fatura ayrıntısını almaz, işlemez veya saklamaz.

## Çocukların Gizliliği

iLinux, 13 yaşın altındaki çocuklar da dahil olmak üzere hiç kimseden bilerek herhangi bir kişisel veri toplamaz. Hiçbir şekilde veri toplamadığımız için özel hükümlere gerek yoktur.

## Bu Politikadaki Değişiklikler

Bu Gizlilik Politikasını zaman zaman güncelleyebiliriz. Herhangi bir değişiklik güncellenmiş bir tarihle bu sayfada yayınlanacaktır. Bu sayfayı periyodik olarak incelemenizi öneririz.

## Bize Ulaşın

Bu Gizlilik Politikası hakkında herhangi bir sorunuz varsa lütfen bizimle iletişime geçin:

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
