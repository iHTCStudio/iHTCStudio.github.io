iHTC Studio ("biz", "bizi" veya "bizim") **iPomodoro**'yu ("爱番茄" / "愛番茄" olarak da bilinir) iPhone ve iPad için bir üretkenlik uygulaması olarak geliştirdi. Bu sayfada, uygulamayı kullandığınızda bilgileri nasıl işlediğimiz açıklanmaktadır. 

## Özet 

**iPomodoro kişisel verileri sunucularımıza toplamaz, saklamaz veya iletmez.** Zamanlayıcılar, çalışma istatistikleri, ayarlar ve motivasyon içeriği cihazınızda çalışır. Görevler ve/veya çalışma istatistikleri için isteğe bağlı **iCloud senkronizasyonu**, Apple Kimliğiniz altında Apple CloudKit'i kullanır; bu bulut hizmetini biz çalıştırmıyoruz. 

## Toplamadığımız Veriler 

- İsim, e-posta, telefon numarası veya kullanıcı hesabı yok (destek için bize gönüllü olarak e-posta göndermediğiniz sürece). 
- Kullanım analitiği, kilitlenme raporlama SDK'ları veya reklam tanımlayıcıları yoktur. 
- Konum takibi yok. 
- Zamanlayıcı oturumları veya çalışma istatistikleri **sunucularımıza** yüklenmez (isteğe bağlı iCloud senkronizasyonu, verileri Apple iCloud hesabınızda saklar). 
- Görev listeleri bize **yüklenmez**; isteğe bağlı iCloud senkronizasyonu, etkinleştirdiğinizde Apple CloudKit aracılığıyla doğrudan cihazlarınız arasında gider. 

## Cihazınızda Saklanan Veriler 

Aşağıdakiler iPhone veya iPad'inizde **yerel olarak** kalır:

| Veri | Depolama | Amaç | 
|------|---------|---------| 
| Pomodoro ve çalışma zamanlayıcı ayarları | Kullanıcı Varsayılanları | Süreler, sesler, temalar, bildirim tercihleri, isteğe bağlı **Aşamanın tamamlandığını onaylayın** (Pomodoro) | 
| Geri sayım görevleri (başlık, tarih, notlar, hatırlatma bayrağı, raptiye, sıra, **vurgu rengi**) | SQLite veritabanı | Görev listesi, son tarih hatırlatıcıları, widget renkleri | 
| Çalışma oturumu geçmişi | SQLite veritabanı | İstatistikler sekmesi (odaklanma süresi, grafikler, görev dökümü) | 
| İstatistik görüntüleme tercihleri ​​| Kullanıcı Varsayılanları | Varsayılan filtreler, **özel tarih aralığı**, sayma kuralları, İstatistik sekmesi tema renkleri | 
| Odaklanma hedefi ve başarı tercihleri ​​| Kullanıcı Varsayılanları | Günlük/haftalık hedefler, açılan rozetler | 
| Ana Ekran kısayol tercihleri ​​| Kullanıcı Varsayılanları | Uygulama simgesine uzun basıldığında hangi Hızlı İşlemler görünür (en fazla 4) | 
| Odak Modu hatırlatıcısı geçiş yapar | Kullanıcı Varsayılanları | Odaklanma etkin olmadan bir zamanlayıcı başlatıldığında isteğe bağlı istem | 
| Günlük motivasyon bildirim programı | Kullanıcı Varsayılanları | İsteğe bağlı yinelenen yerel bildirim zamanı | 
| Bugünkü istatistikler ilerleme anlık görüntüsü | Uygulama Grubu Kullanıcı Varsayılanları | Bugünün İstatistikleri widget'ı | 
| Motivasyon teklifi külliyatı (diyalog/günlük + bildirim) | Uygulama paketi JSON | Cihazdaki fiyat teklifi havuzları (**1000+** iletişim kutusu/günlük birleştirilmiş); bildirim havuzu ayrıdır | 
| Tema ve dil tercihleri ​​| Kullanıcı Varsayılanları | Görünüm ve yerelleştirme | 
| Günlük motivasyon teklif endeksi | Uygulama Grubu Kullanıcı Varsayılanları | Motivasyon widget'ı ve Canlı Etkinlik ipucu senkronizasyonu | 
| Motivasyon alıntı dili filtresi | Uygulama Grubu Kullanıcı Varsayılanları | Widget fiyat teklifi havuzu uygulama içi ayarlarla eşleşiyor | 
| Widget'lar için küresel tema aynası | Uygulama Grubu Kullanıcı Varsayılanları | Widget vurgu renkleri ve isteğe bağlı degrade arka plan | 
| Pomodoro zamanlayıcı anlık görüntüsü | Uygulama Grubu paylaşılan kapsayıcısı | Pomodoro widget'ı ve Canlı Etkinlik | 
| Çalışma zamanlayıcısının anlık görüntüsü | Uygulama Grubu paylaşılan kapsayıcısı | Çalışma Zamanlayıcısı widget'ı ve Canlı Etkinlik | 
| Görevler widget'ının anlık görüntüsü | Uygulama Grubu paylaşılan kapsayıcısı | Geri Sayım Görevleri widget'ı |

Bu verilere bizim erişimimiz yoktur. Uygulamanın kaldırılması yerel depolamayı kaldırır (etkinleştirmiş olabileceğiniz iOS sistem yedeklemeleri hariç). 

## İsteğe Bağlı iCloud Senkronizasyonu (Görevler ve Çalışma İstatistikleri) 

**Görevler:** **Görevleri iCloud ile senkronize et** seçeneğini etkinleştirirseniz, geri sayım görevleri CloudKit (`iCloud.com.iHTCboy.iPomodoros`) aracılığıyla senkronize edilir. 

**Çalışma istatistikleri:** **Çalışma istatistiklerini iCloud ile senkronize et** (İstatistik ayarları) seçeneğini etkinleştirirseniz, odak oturumu kayıtları, isteğe bağlı bağlı görev başlığı/kimliği ve birleştirme için bir `cloudId` dahil olmak üzere `StudySession` türündeki CloudKit kayıtları olarak senkronize edilir. **Günlük hedef ayarları** (`StatsGoals`) ve **başarı kilidini açma/kutlama durumu** (`StatsAchievements`) aynı açma/kapama düğmesi altında senkronize edilir. Senkronizasyon, ilk tam çekmeden sonra artımlı CloudKit değişiklik belirteçlerini kullanır. Bu, görev senkronizasyonundan **bağımsızdır**. 

Her iki durumda da veriler, iHTC Studio sunucuları değil, Apple'ın altyapısı aracılığıyla **özel iCloud hesabınızda** kalır. Her iki geçişi de istediğiniz zaman devre dışı bırakın; yerel kopyalar her cihazda kalır. 

## Bildirimler 

Bildirim izni verirseniz iPomodoro, cihazınızda aşağıdakiler için **yerel bildirimler** planlar:

- Zamanlayıcı tamamlama ve arka plan çalışması hatırlatıcıları (ayarlarda etkinleştirildiğinde) — mesaj metni, paket halindeki cihaz üzeri bildirim fiyat teklifi havuzundan seçilir; ağ getirilmiyor 
- **Günlük motivasyon bildirimi** (isteğe bağlı, Ayarlar) — seçtiğiniz saatte tekrarlanan yerel bildirim 
- Görev son tarihi hatırlatıcıları (görev başına etkinleştirildiğinde) 

Bu bildirimler cihazdaki iOS tarafından oluşturulup iletilir. Bir anlık bildirim sunucusu işletmiyoruz veya sunucularımızdan fiyat teklifi metni indirmiyoruz. 

## Uygulama Grubu (Widget'lar ve Canlı Etkinlik) 

Ana uygulama ve Widget Uzantısı, Apple'ın Uygulama Grubu (`group.com.iHTCboy.iPomodoros`) aracılığıyla minimum zamanlayıcı, motivasyon, tema, **görevler** ve **bugünün istatistik ilerlemesi** anlık görüntülerini paylaşır. Pomodoro ve Çalışma Zamanlayıcısı, cihaz üzerinde **ayrı** anlık görüntü anahtarları kullanır, böylece her iki widget bir arada bulunabilir. Bu kapsayıcı cihazınızda kalır ve yalnızca widget'ları ve Canlı Etkinliği görüntülemek için kullanılır; üçüncü taraf erişimi için kullanılmaz. 

## Uygulama İçi Satın Alma 

İsteğe bağlı uygulama içi destek satın alımı tamamen **Apple StoreKit** tarafından gerçekleştirilir. Apple aracılığıyla yalnızca standart App Store satın alma makbuzlarını alıyoruz; Ödeme ayrıntılarını doğrudan toplamıyoruz. 

## Üçüncü Taraf Hizmetleri

iPomodoro, üçüncü taraf analiz, reklam veya sosyal giriş SDK'larını **entegre etmez**.

**Geri Bildirim**e dokunduğunuzda, uygulama cihaz modeli ve uygulama sürümü gibi önceden doldurulmuş bir şablonla mail istemcinizi açabilir — göndermeye karar vermek size kalmıştır.

## Çocukların Gizliliği

Çocuklardan bilinçli olarak kişisel bilgi toplamıyoruz. Uygulama üzerinden kişisel veri toplamadığımız için, standart App Store yaş derecelendirmelerinin ötesinde özel çocuklara yönelik düzenlemeler uygulanmaz.

## Bu Politikadaki Değişiklikler

Bu Gizlilik Politikasını zaman zaman güncelleyebiliriz. Değişiklikler bu sayfada yayınlanacaktır.

## İletişim

Gizlilikle ilgili sorularınız mı var?

- **E-posta:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
