iHTC Studio ("biz" veya "bizim"), iCangJie'yi (aynı zamanda "爱仓颉" / "愛倉頡" olarak bilinir) geliştirmiştir. Bu sayfa, uygulamamızı kullandığınızda veri toplama, kullanma ve ifşa etme ile ilgili politikalarımızı açıklar.

## Özet

**iCangJie herhangi bir kişisel veri toplamaz, saklamaz veya iletmez.** Tüm karakter aramaları, testler, yazma alıştırması ve öğrenme ilerlemesi tamamen cihazınızda işlenir. Hesap gerekmez ve hiçbir temel özellik için internet bağlantısına ihtiyaç yoktur.

## Veri Toplama

Hiçbir veri toplamıyoruz. Özellikle:

- **Kişisel bilgi toplanmaz** (ad, e-posta, telefon numarası veya hesap yoktur).
- **Kullanım verisi** veya analiz toplanmaz.
- Reklam, analiz veya çökme raporlama için **üçüncü taraf SDK'sı entegre edilmemiştir**.
- **Çerez veya izleme teknolojileri kullanılmaz.**

## iCloud Senkronizasyonu

iCangJie, isteğe bağlı bir iCloud senkronizasyon özelliği sunar (Ayarlar'da açılıp kapatılabilir). Etkinleştirildiğinde, aşağıdaki veriler tamamen Apple tarafından sağlanan ve yönetilen bir hizmet olan **iCloud Anahtar-Değer Depolaması (iCloud KVS)** üzerinden senkronize edilir:

| Senkronize Edilen Veri | Amaç |
|-------------|---------|
| Favoriler | Yer imi eklediğiniz karakterler |
| Öğrenme durumu | Her karakter için ilerleme seviyesi |
| Yanlış soru defteri | Testte yanlış cevaplanan sorular |
| Test puanları ve seri | Günlük test performansınız |
| Yazma istatistikleri | Yazma alıştırmasından doğruluk, seri ve oturum sayıları |
| Günlük yazma kayıtları | Güne göre karakter sayıları ve kod uzunluğu histogramları (~120 gün) |
| Yerleşik metin ilerlemesi | Yerleşik yazma metinlerinde devam konumu |

Bu veriler, Apple'ın iCloud altyapısı üzerinden doğrudan cihazlarınız arasında iletilir. iHTC Studio herhangi bir sunucu işletmez ve iCloud verilerinize erişimi yoktur. Apple'ın iCloud verilerini ele alışı [Apple'ın Gizlilik Politikası](https://www.apple.com/privacy/) kapsamındadır.

iCloud senkronizasyonunu Ayarlar'dan istediğiniz zaman devre dışı bırakabilirsiniz. Devre dışı bırakıldığında tüm veriler her cihazda yerel olarak kalır.

Yazma arayüzü tercihleri (yanlış tuşları koruma, metin pinyin'i) her cihazda yerel olarak saklanır ve iCloud ile senkronize **edilmez**.

## Cihazınızda Yerel Olarak Saklanan Veriler

iCangJie'nin oluşturduğu tüm veriler cihazınızda kalır:

| Veri | Depolama | Kullanıcı Kontrolü |
|------|---------|--------------|
| Favoriler | Yerel (UserDefaults / App Group) | Uygulamada tek tek öğeleri kaldırın veya hepsini temizleyin |
| Öğrenme durumu | Yerel (UserDefaults) | Uygulama ayarlarından sıfırlayın |
| Yanlış soru defteri | Yerel (UserDefaults) | Uygulamada temizleyin |
| Test puanları ve seri | Yerel (UserDefaults) | Uygulama ayarlarından sıfırlayın |
| Yazma istatistikleri ve günlük kayıtlar | Yerel (UserDefaults / App Group); isteğe bağlı iCloud KVS | Öğrenme verileri sıfırlandığında temizlenir |
| Metin ilerlemesi | Yerel (UserDefaults / App Group); isteğe bağlı iCloud KVS | Öğrenme verileri sıfırlandığında temizlenir |
| Yazma arayüzü tercihleri | Yerel (UserDefaults) | Ayarlar → Yazma bölümünden değiştirin |
| Tanıtım ve yeni başlayan yolu işaretleri | Yerel (UserDefaults) | Yalnızca uygulama verilerini sıfırlarsanız yeniden gösterilir |
| Test tercihleri | Yerel (UserDefaults) | Test ayarlarından değiştirin |
| Spotlight dizinleme tercihi | Yerel (UserDefaults) | Ayarlar → Ana Ekran kısayolları bölümünden açıp kapatın |
| Uygulama tercihleri ve tema | Yerel (UserDefaults) | Uygulamayı silerek sıfırlayın |

Widget'lar, ana uygulama ile widget uzantıları arasında veri paylaşmak için bir **App Group** kapsayıcısı kullanır. Bu kapsayıcı cihazınızda kalır ve hiçbir üçüncü tarafça erişilemez.

### JSON Yedekleme (kullanıcı tarafından başlatılır)

Öğrenme verilerini içeren bir JSON yedek dosyasını (`.icangjie-backup`) **dışa aktarabilirsiniz**. Dosya, **sizin seçtiğiniz** bir konuma (Dosyalar, AirDrop vb.) yazılır. **İçe aktarma**, sizin seçtiğiniz bir dosyayı okur. iHTC Studio yedek dosyalarını yüklemez, barındırmaz veya bunlara erişmez.

### Spotlight Dizinleme (iOS, isteğe bağlı)

Etkinleştirildiğinde iCangJie, **cihaz üzerindeki** iOS Spotlight dizinine (alan adı `com.iHTCboy.iCangJie.words`) en fazla **80** favori ve son karakteri dizinler. Girdiler 30 gün sonra sona erer. Bu veriler, iPhone/iPad'inizdeki Apple'ın Spotlight sistemi dışında cihazınızdan asla çıkmaz. Ayarlar'dan istediğiniz zaman devre dışı bırakabilirsiniz.

## İzinler

iCangJie **yalnızca bir isteğe bağlı izin** ister:

| İzin | Ne zaman istenir | Amaç |
|------------|----------------|---------|
| **Fotoğraf Kitaplığı (Yalnızca Ekleme)** | Bir eğitimdeki kök tablosu görselinde **Fotoğraflar'a Kaydet**'e dokunduğunuzda | Görseli fotoğraf kitaplığınıza kaydetmek |

iCangJie mevcut fotoğraflarınızı **okumaz**. Temel özellikler için kameranıza, mikrofonunuza, kişilerinize, konumunuza veya yerel ağınıza erişim yoktur.

Harici web sitelerini açan isteğe bağlı özellikler (Youdao çevrimiçi arama, eğitim bağlantıları) sistem tarayıcısını kullanır ve iCangJie'ye gezinti geçmişinize erişim vermez.

## Çocukların Gizliliği

iCangJie, 13 yaşın altındaki çocuklar dahil hiç kimseden bilerek kişisel veri toplamaz. Hiç veri toplanmadığı için özel bir düzenleme gerekmez.

## Bu Politikadaki Değişiklikler

Bu Gizlilik Politikası'nı zaman zaman güncelleyebiliriz. Değişiklikler, güncellenmiş bir tarihle bu sayfada yayımlanacaktır. Bu sayfayı düzenli olarak gözden geçirmenizi öneririz.

## Bize Ulaşın

Bu Gizlilik Politikası hakkında sorularınız varsa lütfen bizimle iletişime geçin:

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
