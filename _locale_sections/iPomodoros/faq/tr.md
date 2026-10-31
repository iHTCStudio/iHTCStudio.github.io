### Neden diğer Pomodoro uygulamaları yerine iPomodoro'yu seçmeliyim?

iPomodoro, Apple platformları için geliştirilmiş **yerel SwiftUI** bir uygulamadır — sarmalanmış bir web zamanlayıcı değil. **Beş entegre sekme** (Pomodoro, Çalışma Zamanlayıcısı, Görevler, İstatistikler, Ayarlar), **çift Canlı Aktiviteler**, **beş widget ailesi**, **9 başarı rozeti**, **1000+ cihaz içi alıntı**, **Siri ve URL kısayolları** ve **isteğe bağlı iCloud senkronizasyonu** elde edersiniz — hem de **sıfır analiz** ve **hesap gerekmeksizin**. Tek bir sakin uygulama ile odaklanma, son tarih ve ilerleme takibini baştan sona kapsar.

### Zamanlayıcı ve görev ayarları nerede?

Zamanlayıcı süreleri, sesler, Canlı Aktivite, sayfa tema renkleri, isteğe bağlı **Odak Modu hatırlatıcısı** ve (yalnızca Pomodoro için) isteğe bağlı **Aşama tamamlamayı onayla**, her sekmenin **dişli simgesi** altında bulunur (Pomodoro, Çalışma Zamanlayıcısı, Görevler veya **İstatistikler**). Genel **Ayarlar** sekmesi; görünüm, dil, **Ana Ekran kısayolları**, **Uygulama Rehberi**, bildirim izni, motivasyonel alıntılar (günlük motivasyon bildirimi dahil), widget rehberi, geri bildirim ve hakkında bölümünü içerir — mod başına süreleri içermez. **İstatistikler** ayarları (sayfa teması, hedefler, isteğe bağlı iCloud senkronizasyonu, başarılar, sayım kuralları, CSV, saklama) **İstatistikler sekmesi → dişli** altında bulunur.

### Ana Ekran kısayolları ve Siri nasıl çalışır?

Hızlı İşlemler için **uygulama simgesine uzun basın**; Pomodoro'yu, Çalışma Zamanlayıcısını, Görevleri, İstatistikleri, motivasyon teklifini veya geri bildirimi açın. **Ayarlar → Uygulama ayarları → Ana Ekran kısayolları** altında hangi dördünün görüneceğini özelleştirin (yeniden sıralamak için sürükleyin). Aynı hedefleri **`iPomodoro://`_** URL'ler aracılığıyla da açabilirsiniz (`pomodoro`, `study`, `tasks`, `stats`, `motivation`, `feedback`; `iPomodoros://` de çalışır). [URL Şeması Referansı](../url-şeması)'nın tamamına bakın. **Siri / Kısayollar uygulaması** yerleşik Uygulama Kısayolları aracılığıyla sekmeleri açabilir veya *"Bugün iPomodoro'da ne kadar süre odaklandım?"* yanıtını verebilir. 

### Uygulama içi Uygulama Kılavuzu nedir? 

**Ayarlar → Uygulama ayarları → Uygulama Kılavuzu** — beş sekmenin, widget'ların, kısayolların, iCloud'un ve SSS'nin tamamını kapsayan daraltılabilir bir eğitim (Widget kılavuzuna benzer stil). 

### iPomodoro benim için Odak Modu'nu açabilir mi? 

Hayır — iOS, üçüncü taraf uygulamaların Focus'u doğrudan etkinleştirmesine izin vermez. İsteğe bağlı **Odak Modu hatırlatıcısı** (Pomodoro veya Çalışma Zamanlayıcısı dişli ayarları), bir zamanlayıcıyı başlattığınızda Odak'ın kapalı olup olmadığını kontrol eder ve bir uyarı gösterir; uyarıdan **Ayarlar**'ı açabilirsiniz ancak Odak'ı kendiniz açmanız gerekir. 

### Her geri sayım görevi için bir renk seçebilir miyim?

Evet. Bir görev eklerken veya düzenlerken, **9 vurgu renginden** birini seçin. Liste ve **Geri Sayım Görevleri** widget'ı bu rengi her satır için kullanır. Görev senkronizasyonu etkinleştirildiğinde renkler iCloud üzerinden senkronize edilir.

### İstatistikleri özel bir tarih aralığına göre filtreleyebilir miyim?

Evet. İstatistikler sekmesinde (veya dönem raporunda), dönem çubuğunda **Özel**i seçin, ardından başlangıç ve bitiş tarihlerini ayarlayın. Aralık, İstatistikler ayarlarında **Filtreyi hatırla** açık olduğunda kaydedilir.

### Günlük motivasyon bildirimi alabilir miyim?

Evet. **Ayarlar → Motivasyonel Alıntı Ayarları**, isteğe bağlı bir **günlük motivasyon bildirimi** içerir — bir zaman seçin ve iPomodoro, cihazdaki bildirim alıntı havuzundan rastgele bir satır ile tekrarlayan bir **yerel bildirim** planlar (ağ bağlantısı yok). Zamanlayıcı bitiş uyarılarından ayrıdır.

### Günlük alıntılar ile bildirim alıntıları arasındaki fark nedir?

**Diyalog/günlük alıntılar** (**Tüm filtreleme olduğunda 1000+ toplam — basitleştirilmiş Çince + İngilizce) uygulama başlatma açılır penceresini, ayarlar tarayıcısını, Canlı Aktivite ipucunu ve Motivasyon widget'ını besler. **Bildirim alıntıları** ayrı bir cihaz içi havuzdur (**her dil için 365 genel satır**) ve yalnızca arka plan zamanlayıcı tamamlanma uyarıları için kullanılır. Her ikisi de Ayarlar'daki alıntı dili filtrenize saygı gösterir.

### Pomodoro Tekniği Nedir?

Pomodoro Tekniği bir zaman yönetimi yöntemidir: odaklanmış aralıklarla çalışın (klasik olarak 25 dakika), ardından kısa bir mola verin. Birkaç döngüden sonra daha uzun bir mola verin. iPomodoro bu ritmi otomatikleştirir, böylece saate değil işe odaklanabilirsiniz.

### iPomodoro eski Flutter versiyonundan nasıl farklıdır?

Bu, Apple platformları için **tam bir SwiftUI yeniden yazımıdır**. Aynı temel fikirler — Pomodoro, çalışma zamanlayıcısı, geri sayım görevleri — ama yerel performans, Canlı Aktivite, modern widget'lar ve daha sıkı iOS entegrasyonu vardır.

### Bir hesaba veya internet bağlantısına ihtiyacım var mı?

iPomodoro hesabı gerekmez. Zamanlayıcılar, çalışma istatistikleri, temalar ve widget'lar cihazınızda **tamamen çevrimdışı** çalışır. **İsteğe bağlı:** Verileri aynı Apple kimliğiyle oturum açan cihazlar arasında birleştirmek için **Görevleri iCloud ile senkronize et** (Görevler → dişli) ve/veya **Çalışma istatistiklerini iCloud ile senkronize et** (İstatistikler → dişli) özelliğini etkinleştirin; bu, sunucularımızı değil, Apple CloudKit'i kullanır. İnternet aynı zamanda App Store güncellemeleri veya geri bildirim e-postaları için de kullanılır. 

### Çalışma İstatistikleri nasıl çalışır? 

**İstatistikler** sekmesini açın. Tümü / Pomodoro / Çalışma Zamanlayıcısı ve Bugün / Hafta / Ay / Yıl / Tüm zamanlar / **Özel tarih aralığı**'na göre filtreleyin. Kontrol panelinde **bugünün özeti**, **hedef ilerlemesi**, haftadan haftaya karşılaştırma, **aylık ısı haritası**, **başarılar**, hafta içi/günün saati grafikleri ve **bağlantılı göreve göre döküm** gösterilir. Hedefler, isteğe bağlı **iCloud senkronizasyonu**, sayma kuralları, **CSV dışa aktarma/içe aktarma** ve veri saklama için **dişli simgesine** dokunun. İstatistikler **asla sunucularımıza yüklenmez** (isteğe bağlı iCloud, Apple Kimliğiniz altında Apple CloudKit'i kullanır). 

### Çalışma istatistiklerini dışa veya içe aktarabilir miyim?

Evet. **İstatistikler sekmesi → dişli → Dışa aktar**, sistem paylaşım sayfası aracılığıyla bir CSV dosyasını paylaşır. **İçe aktar** aynı biçimi kabul eder (`kind,started_at,ended_at,duration_seconds,outcome` artı isteğe bağlı `task_id,task_title,cloud_id`) — **birleştir** (kopyaları atla) veya **tümünü değiştir** seçeneğini seçin. Yedekleme veya manuel geçiş için kullanışlıdır. Otomatik cihazlar arası senkronizasyon için bunun yerine **Çalışma istatistiklerini iCloud ile senkronize et** seçeneğini etkinleştirin. 

### İstatistiklerimi resim olarak paylaşabilir miyim? 

Evet. iPomodoro, **İstatistik kontrol paneli** (araç çubuğu paylaşımı), **dönem raporları**, **inceleme yılı** özetleri ve **başarılar** (tam liste veya tek rozet) için **markalı anlık görüntü kartları** (odak ölçümleri + App Store QR kodu) oluşturabilir. İstatistik paylaşım kartları **İstatistikler sekmesi sayfa temanızı** renklerinizi kullanır. Ayrıca Ayarlar → Uygulamayı Paylaş bölümünden de **uygulama tanıtım kartını** paylaşabilirsiniz. 

### Çalışma istatistiklerini iCloud ile senkronize edebilir miyim? 

Evet — **İstatistikler sekmesi → dişli → Çalışma istatistiklerini iCloud ile senkronize edin**. Bu, görev iCloud senkronizasyonundan **ayrıdır**. Oturumlar, CloudKit kayıt türü `StudySession` aracılığıyla Apple ID cihazlarınızda `cloudId` kadar birleştirilir. **Günlük hedef ayarları** (`StatsGoals`) ve **başarı kilidini açma/kutlama durumu** (`StatsAchievements`) etkinleştirildiğinde aynı geçiş altında senkronize edilir.

### Günlük odaklanma hedefleri nasıl çalışır? 

**İstatistikler → donanım → Hedefler**: günlük pomodoro sayısını, günlük odaklanma dakikalarını ve haftalık odaklanma dakikalarını ayarlayın. İlerleme durumu, etkinleştirildiğinde İstatistik kontrol panelinde ve **Günün İstatistikleri** widget'ında görünür. 

### Geri sayım görevini odaklanma oturumuna nasıl bağlarım? 

Pomodoro veya Çalışma Zamanlayıcısı ekranında **Görevi bağla**'ya dokunun ve bir görev seçin. Veya **Görevler**'den bir göreve uzun basın → **Pomodoro ile Odaklan** veya **Çalışma Zamanlayıcısı ile Odaklan**. Tamamlanan oturumlar, İstatistikler'de **göreve göre döküm** için görev başlığını saklar. 

### Görevleri nasıl sabitleyebilirim veya yeniden sıralayabilirim? 

**Görevler** sekmesinde, **Sabitlemek** için bir satırı kaydırın veya gezinme çubuğundaki sıralama menüsünü kullanın. Görevleri **sürüklemek** için yeniden sıralama moduna girin; anahtarları otomatik olarak özel sıraya göre sıralayın. Sabitlenen görevler üst kısımda kendi bölümünde görünür. 

### iCloud görev senkronizasyonu nasıl çalışır? 

Görevler sekmesi → dişli → **Görevleri iCloud ile senkronize et** seçeneğini açın. Görevler, Apple Kimliği aygıtlarınızda son değiştirilme zamanına göre birleştirilir. Pomodoro / çalışma zamanlayıcıları yerel kalır. **Çalışma istatistikleri** isteğe bağlı olarak ayrı olarak senkronize edilebilir (İstatistikler → dişli). İOS Ayarlarında iCloud'da oturum açmış olmanız gerekir. Senkronizasyon, uygulamaya döndüğünüzde de çalışır.

### İstatistikler panosu paylaşım görselinde neler bulunur?

İstatistikler sekmesi araç çubuğunda **Paylaş**a dokunun. Uzun kart, **geçerli kapsam ve dönem** filtrelerinizi yansıtır — bugünün kahramanı, hedef ilerlemesi, ısı haritası, hafta içi/saat grafikleri, görev dağılımı, trend çubukları ve son oturumlar — ayrıca marka ve bir App Store QR kodu içerir. Renkler, **İstatistikler sekmesi sayfa temasıyla** eşleşir.

### İstatistikler sekmesi temasını özelleştirebilir miyim?

Evet. **İstatistikler sekmesi → ayar simgesi → Tema** — Pomodoro, Çalışma Zamanlayıcısı ve Görevlerdeki ile aynı başlık çubuğu ve arka plan gradyan kontrolleri. Varsayılan tema odak kırmızısıdır (`#E53935` / `#EF9A9A`). İstatistikler sekmesi rengi, gezinme çubuğu ve **istatistik paylaşım kartları** bu sayfa teması renklerini takip eder.

### Başarılar nasıl çalışır?

Dokuz yerel rozet, kilometre taşlarına ulaştığınızda açılır: ilk pomodoro, seriler, toplam pomodorolar, odaklanma saatleri, günlük hedef tamamlama ve daha fazlası. Yeni bir rozetin kilidini açtığınızda, İstatistikler sekmesinde **tam ekran kutlama** görünür (kapatmak için **Devam**'a dokunun). Tabloya göz atmak için **İstatistikler → dişli → Başarılar**'ı açın. Ayrıntı sayfası için **bir rozete dokunun**; Başarılar araç çubuğundan **tam listeyi** veya ayrıntılar ekranından **tek bir rozeti** paylaşın. Rozetler cihazda saklanır; iCloud senkronizasyonu etkinken, kilidi açma ve kutlama durumu CloudKit aracılığıyla cihazlarınız arasında birleştirilir; sunucularımıza yüklenmez. 

### Odak ısı haritasında geçmiş aylara nasıl göz atabilirim? 

İstatistik panosunda, ısı haritası kartındaki **Önceki / Gelecek ay** oklarını kullanın, **yıl + ay seçici** sayfasını açmak için **ay başlığına** dokunun veya geçerli aya geri dönmek için **Bu ay**'a dokunun. 

### Isı haritasındaki gelecek tarihler neden farklı görünüyor? 

Geçerli ayda bugünden sonraki günler, daha açık dolgulu **kesik çizgili yer tutucular** olarak görünür; bunlar odak günleri olarak sayılmaz. Geçmiş günler ve bugün normal yoğunluktaki renkleri kullanıyorlar. 

### Bugünün İstatistikleri widget'ını nasıl eklerim?

Ana Ekrana uzun basın → **+** → **iPomodoro**'yu arayın → **Bugünün İstatistikleri** ekleyin (Küçük, **Orta, Büyük** veya Kilit Ekranı dikdörtgen / satır içi). Bugünün odağını, pomodoroyu ve **haftalık** hedef ilerlemesini ve galibiyet serisini gösterir. 

### Görevler widget'ını nasıl eklerim? 

Ana Ekrana uzun basın → **+** → **iPomodoro**'yu arayın → **Geri Sayım Görevleri** (Küçük / Orta / Büyük) ekleyin. Yaklaşan sabitlenmiş görevleri ve kalan günleri gösterir. En hızlı yenileme için görevleri düzenledikten sonra uygulamayı açın. 

### Motivasyon widget'ının teklifini yenileyebilir miyim? 

**iOS 17+**'de, uygulamayı açmadan anında başka bir alıntı seçmek için Günlük Motivasyon widget'ındaki **yenile** düğmesine dokunun. 

### Bildirimler neden çalışmıyor? 

Mevcut iOS izin durumunuz için **Ayarlar sekmesi → Bildirimler**'i kontrol edin. Zamanlayıcı ve görev hatırlatıcıları bildirim erişimi gerektirir. İzin reddedilirse Sistem Ayarlarını açın. 

### Çalışma ve mola sürelerini nasıl özelleştirebilirim? 

Bir süre seçiciyi açmak için Pomodoro sekmesindeki **dişli simgesine** dokunun → adım satırlarını ayarlayın veya ana ekranda **büyük zamanlayıcı rakamlarına dokunun**. Uzun mola aralığı (her N pomodoro) da yapılandırılabilir. 

### Aşamanın tamamlandığını onaylama nedir?

**Pomodoro sekmesi → ayarlar → Faz tamamlamayı onayla**. **Açık** olduğunda, iPomodoro bir sonraki faz başlamadan önce her iş veya mola segmentinden sonra bir iletişim kutusu gösterir. **Kapalı** olduğunda (varsayılan), bir sonraki faz tamamlanma alarmından sonra otomatik olarak başlar — klasik eller serbest Pomodoro akışı.

### Canlı Aktivite ve Dinamik Ada nasıl çalışır?

**Canlı Aktivite**yi Pomodoro ve Çalışma Zamanlayıcı ayarlarında (dişli simgesi) ayrı ayrı açın. Her mod kendi **kilit ekranı** ve Dinamik Ada geri sayımına sahiptir — birbirlerini asla geçersiz kılmazlar. Bir oturum çalışırken canlı bir geri sayım görürsünüz; oturum tamamlandığında kısa bir kutlama 10 saniye gösterilir. iOS, zamanlayıcınız hâlâ Kilit Ekranda görünürken uygulamayı kapatırsa, iPomodoro'yu tekrar açmak oturumu **geri yükler** ve aktif sekmeye gider — **ancak**, uygulamayı bir **Ana Ekran Hızlı İşlemi** üzerinden başlattıysanız, bu önceliklidir.

### Widget'ları nasıl eklerim?

Ana Ekrana uzun basın → **+** → **iPomodoro** (veya 爱番茄 / 愛番茄) arayın. Sayaç geri sayımları için **iPomodoro · Pomodoro** veya **iPomodoro · Study Timer**i seçin (bunlar ayrı widgetlardır), günlük odak ilerlemesi için **Today's Stats**, son tarihler için **Countdown Tasks** veya günlük alıntı için **Daily Motivational Quote**. Adım adım yardım için **Ayarlar → Widgetlar → Nasıl Kullanılır**ı açın.

### Neden zamanlayıcı widget'ım güncellenmiyor?

Pomodoro ve Study Timer **ayrı widgetlardır**. Bir oturumu başlatın veya duraklatın **uygun sekmede** ve doğru widget'ı eklediğinizden emin olun. iOS pil tasarrufu için güncellemeleri geciktirebilir — daha hızlı senkronizasyon için uygulamayı bir kez açın.

### Eski zamanlayıcı widget nerede?

Zamanlayıcılar artık **iPomodoro · Pomodoro** ve **iPomodoro · Study Timer**. Eski zamanlayıcı widget'ları kaldırın ve yeni olanları widget galerisinden ekleyin.

### Günlük motivasyon alıntısı nasıl çalışır?

`(year × 400 + dayOfYear) % total` kullanılarak her gün deterministik olarak bir teklif seçilir. **Ayarlar → Motivasyonel Alıntı Ayarları → Motivasyonel Alıntı Dilleri** (Tümü / Basitleştirilmiş / Geleneksel / İngilizce) altında alıntı dilini filtreleyin. Aynı alıntı Motivasyon widget'ında ve Canlı Etkinlik ipucunda gece yarısına kadar görünür. **Ayarlar → Motivasyonel Alıntı Ayarları → Motivasyonel Alıntı Antolojisinde** (tam ekran, birer birer) rastgele alıntılara göz atın. 

### Widget arka planları temamı takip edebilir mi? 

Evet. **Ayarlar → Widget'lar → Widget arka planı temayı takip eder**, Ana Ekran ve Kilit Ekranı widget'larındaki genel vurgu degradenizi yansıtır. Başlıklarda vurgu renklerini korurken temiz beyaz (açık) veya sistem koyu arka planı için bu özelliği kapatın. 

### Görev zamanı hatırlatıcıları nasıl çalışır? 

Bir görevi oluştururken veya düzenlerken **Son tarih hatırlatıcısını** etkinleştirin ve gelecekteki bir hedef tarih/saati ayarlayın. Tam o anda yerel bir bildirim tetikleniyor. **Görevler sekmesi → dişli → Görev zamanı hatırlatıcıları** altında bekleyen hatırlatıcıları yönetin — görevi düzenlemek için bir satıra dokunun veya düzenleme sayfasının alt kısmından **silin**. Görev listesindeki silmek için hızlıca kaydırma özelliği de hâlâ çalışıyor. 

### Düzenleme sırasında bir görevi nasıl silerim?

Listeden veya **Görev zamanı hatırlatıcılarından** bir görevi açın, ardından düzenleme sayfasının en altına gidin ve **Sil**'e dokunun. Uyarıyı onaylayın. Yeni görevler (akış oluşturma) silme düğmesi göstermez. 

### Neden geçmiş bir tarih için hatırlatıcıyı etkinleştiremiyorum? 

Hedef tarihsaat zaten geçmişse, hatırlatıcı geçişi gizlenir ve mevcut hatırlatıcılar otomatik olarak devre dışı bırakılır; planlanacak anlamlı bir şey kalmaz. 

### Sistemimden farklı bir dil kullanabilir miyim? 

Evet. **Ayarlar sekmesi → Dil**'e gidin ve İngilizce, Basitleştirilmiş Çince veya Geleneksel Çince'yi seçin. Ana Ekranınızdaki uygulama adı sistem dilini takip eder; uygulama içi kullanıcı arayüzü, uygulama içi seçiminizi takip eder. 

### Uygulama verilerimi topluyor mu? 

Analitik yok, izleme yok. Zamanlayıcılar ve çalışma istatistikleri varsayılan olarak cihazınızda kalır. Görevler ve çalışma oturumları yalnızca ayrı geçiş düğmelerini etkinleştirdiğinizde **iCloud'unuzla** senkronize edilir. Görevinizi veya zamanlayıcı verilerinizi sunucularımıza almıyoruz. Tüm ayrıntılar için [Gizlilik Politikamıza](../privacy) bakın. 

### MacOS desteklenecek mi? 

macOS desteği planlanıyor. Xcode projesi zaten macOS SDK yapılandırmasını içeriyor; App Store'daki güncellemeler için bizi takip etmeye devam edin. 

### Hala yardıma mı ihtiyacınız var?

Bize ulaşın [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com). Genellikle 48 saat içinde cevap veririz.

&lt;/section&gt;
