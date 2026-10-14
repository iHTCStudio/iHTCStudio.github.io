iHTC Studio ("biz", "bize" veya "bizim") iExcel'i ("爱表格" / "愛表格" olarak da bilinir) oluşturdu. Bu sayfa, uygulamamızı kullandığınızda kişisel verilerinizin toplanması, kullanılması ve ifşa edilmesine ilişkin politikalarımız hakkında sizi bilgilendirir.

## Özet

**iExcel bir hesap gerektirmez ve iHTC Studio sunucularında kişisel veri toplamaz.** Tüm öğrenme içeriği uygulamada paketlenir ve tamamen çevrimdışı çalışır. İsteğe bağlı **iCloud Senkronizasyonu**, favorilerinizi, ilerleme durumunuzu ve tercihlerinizi Apple Kimliğinizin altındaki **iCloud Anahtar-Değer Depolama Alanınızda** saklar. **Reklam yok. Takip yok.**

## Veri Toplama

Analitik, reklam veya izleme işletmiyoruz. Özellikle:

- **Hiçbir kişisel bilgi** iHTC Studio tarafından toplanmaz (isim, e-posta, telefon numarası veya iHTC Studio hesabı yok).
- **Kullanım analitiği yoktur** veya kilitlenme raporlama SDK'ları entegre değildir.
- **Öğrenim verileriniz** cihazlarınızda kalır ve senkronizasyonu etkinleştirirseniz iHTC Studio sunucularında değil **Apple iCloud**'da kalır.
- **Uygulamada çerez veya üçüncü taraf izleyici yoktur**.

## Uygulama Nasıl Çalışır?

iExcel, kullanıcı tarafından oluşturulan verileri cihazınızda yerel olarak saklar:

- Tüm öğrenme içeriği (işlevler, ipuçları, dersler, testler, kısayollar) **uygulamanın içinde paketlenmiştir** ve hiçbir zaman harici bir içerik sunucusundan getirilmemiştir.
- Göz atmak, aramak, pratik yapmak veya sınavlara girmek için internet bağlantısı gerekmez.
- İsteğe bağlı **iCloud senkronizasyonu**, iCloud'da oturum açtığınızda ve senkronizasyonu etkin bıraktığınızda Apple'ın **NSUbiquitousKeyValueStore** özelliğini kullanır. Ayarlar'da her cihaz için bunu kapatabilirsiniz.
- Harici bağlantıların açılması (ör. geri bildirim e-postası, App Store sayfaları) standart sistem ağını kullanır; sayfalar herhangi bir iHTC Studio sunucusu aracılığıyla değil, doğrudan ana bilgisayarlarından yüklenir.

## Cihazınızda Saklanan Veriler

| Veri | Amaç |
|------|---------|
| Öğrenim içeriği kütüphanesi | Paketlenmiş işlevler, ipuçları, dersler, testler, kısayollar |
| Favoriler | Yıldız eklediğiniz öğeler |
| Son Kullanılanlar | Son görüntülenen öğeler (en fazla 30) |
| Uzmanlaşılan öğeler | Öğrenildi olarak işaretlediğiniz öğeler; sınav tamamlama otomatik işaretleri |
| Testin en iyi puanları | Test başına en yüksek puan |
| Öğrenme serisi ve son öğrenme tarihi | Ardışık gün takibi |
| Günlük İşlev kimliği ve tarihi | Geçerli takvim günü için öne çıkan işlev |
| Tercihler | Dil, görünüm, sekme görünürlüğü, widget teması |
| Widget anlık görüntüsü | Ana Sayfa / Kilit Ekranı widget'ları için Uygulama Grubu aracılığıyla paylaşıldı |
| İlk katılımın tamamlanması | Karşılama kılavuzunun tamamlanıp tamamlanmadığı |

## iCloud Senkronizasyonu (İsteğe bağlı)

**iCloud Senkronizasyonu** etkinleştirildiğinde ve iCloud'da oturum açtığınızda:

- **Senkronize edildi:** favoriler, son arananlar, ustalaşılan öğeler, test puanları, öğrenme serisi, son öğrenme tarihi ve tercihler (dil, görünüm, kategori/favoriler sekmesi görünürlüğü, temayı takip eden widget, senkronizasyon bayrağı).
- **Senkronize edilmedi:** Günlük İşlev seçimi (her cihazda bağımsız olarak seçilir).
- **Depolama:** Apple **iCloud Anahtar-Değer Depolama Alanı**, Apple Kimliğinizle ilişkilendirilir.
- **Devre dışı bırakma:** herhangi bir cihazda **Ayarlar → iCloud Senkronizasyonu** bölümünden devre dışı bırakın; bu cihaz yüklemeyi ve birleştirmeyi durdurur ancak yerel verileri tutar.
- iHTC Studio, iCloud kapsayıcınızı okuyamıyor.

## Uygulama Grubu (Widget Uzantısı)

iExcel, widget uzantısıyla küçük bir anlık görüntüyü paylaşmak için bir Uygulama Grubu (`group.com.iHTCboy.iExcel`) kullanır:

- Günlük İşlev ve Favoriler için yerelleştirilmiş başlıklar ve özetler
- İlerleme widget'ı için ilerleme sayıları ve seriler
- Widget kromu için görünümü geçersiz kılma

Bu veriler **yalnızca cihazınızda** paylaşılan bir konteynere yazılır ve hiçbir zaman iHTC Studio tarafından iletilmez.

## İzinler

iExcel, temel öğrenme özellikleri için kamera, mikrofon, konum, kişiler veya fotoğraf kitaplığı erişimi **gerektirmez**.

## Uygulama İçi Satın Alma

iExcel, isteğe bağlı bir **ipucu / geliştiriciyi destekleme** satın alımını içerir. Tüm ödeme işlemleri yalnızca **Apple'ın StoreKit çerçevesi** tarafından gerçekleştirilir. iHTC Studio, herhangi bir ödeme kartı bilgisini veya fatura ayrıntısını almaz, işlemez veya saklamaz.

## iExcel Ne Değildir?

iExcel bir **öğrenme referansı ve pratik aracıdır**. Excel çalışma kitaplarınızı açmaz, düzenlemez veya eşitlemez. Formül Bahçesi, sabit örnek veriler üzerindeki sınırlı sayıda modeli değerlendirir ve bir elektronik tablo motoru değildir. Excel, Microsoft'un ticari markasıdır; Bu uygulama Microsoft'a bağlı değildir.

## Çocukların Gizliliği

iExcel, 13 yaşın altındaki çocuklar da dahil olmak üzere hiç kimseden bilerek herhangi bir kişisel veri toplamaz. Kişisel veri toplamadığımız için özel hükümlere gerek yoktur.

## Bu Politikadaki Değişiklikler

Bu Gizlilik Politikasını zaman zaman güncelleyebiliriz. Herhangi bir değişiklik güncellenmiş bir tarihle bu sayfada yayınlanacaktır. Bu sayfayı periyodik olarak incelemenizi öneririz.

**Son güncelleme:** 4 Temmuz 2026

## Bize Ulaşın

Bu Gizlilik Politikası hakkında herhangi bir sorunuz varsa lütfen bizimle iletişime geçin:

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
