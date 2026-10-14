Yanıtlar **güncel uygulama davranışını** yansıtır (kurtarılabilir duraklat/devam, dışa aktarma kuyruğu, Live Activity, cihaz kapısı, 繁體中文, uygulama içi kılavuzlar). Adım adım: [Kullanıcı Kılavuzu](index).

---

## Cihaz ve gereksinimler

### Hangi iPhone'lar desteklenir?

TwinPolarCam **`AVCaptureMultiCamSession`** — Apple eşzamanlı çoklu kamera API'si gerektirir. Genelde **iPhone XS/XR ve sonrası**; yetenek donanıma bağlıdır.

- **Desteklenmeyen cihazlar** — özel ekran; kamera UI başlamaz.
- **Simülatör desteklenmez.**
- **Gerçek iPhone** gerekir.

### Neden tek kamera yedeği yok?

Eşzamanlı çift kayıt ürünün özüdür. Desteklenmeyen cihazda **iade** veya destek.

### Maksimum çözünürlük?

**720p–4K** kamera başına. **iPhone 12+** genelde dual 4K. **60 fps yok** — **24/30 fps**.

### iPad/Mac?

**Hayır** — **yalnızca iPhone**.

### iOS?

**En az 15.0** · Live Activity **16.2+**

---

## Kayıt ve PiP

**Switch/Flip** main/PiP değiştirir — her iki iz devam eder. PiP sürükle/pinch; **App Settings → Picture-in-Picture** — **dışa aktarmaya gömülür**. Önizleme duraklatma **aktif kayıtta yok**.

---

## Kesintiler ve güvenilirlik

Arama: **duraklat**, sonra **aynı segment** (`.mov`). Control Center **tek başına duraklatmaz**. Arka plan: **~25 sn** → **Pending**. Acil kayıt oturumu **sonlandırır**. Duraklama **PTS jump-cut**.

---

## Live Activity

**iOS 16.2+** **Background waiting** / **Saved**. Kapat: **General → Recording Live Activity**.

---

## Dışa aktarma ve Pending

Auto Export açık/kapalı; **seri kuyruk**; yalnızca **`TwinPolarCam_*.mov`**; **H.264/AAC**; `Application Support/...` **iCloud yedek dışı**.

---

## Ayarlar ve dil

**English / 简体中文 / 繁體中文**. Auto-Delete Original varsayılan **kapalı**. Müzik yalnızca **kayıtta** durur.

---

## İzinler ve gizlilik

**Veri toplanmaz.** [Gizlilik](../privacy). Fotoğraflar **Yalnızca Ekle**.

---

## İpuçları ve destek

**Send Feedback**, **Help**, `twinpolarcam://`. [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

[Kılavuz](index) · [Bağlantılar](../url-scheme) · [Gizlilik](../privacy)

---

## Tam kılavuz

Part 1–10: başlangıç, kontroller, PiP, ses, oturum, güvenilirlik, dışa aktarma, genel, yardım, sorun giderme.

---

## Part 1 — İlk başlatma {#part-1}

6 sayfa onboarding; Kamera/Mikro/Fotoğraf Add Only; Multi-Cam **XS/XR+**.

---

## Part 2 — Ana ekran {#part-2}

Yatay; Record, Pause, Stop, Switch.

---

## Part 3 — Kamera & PiP {#part-3}

720p–4K, 24/30 fps.

---

## Part 4 — Ses {#part-4}

AAC/PCM; oturum **Record** ile başlar.

---

## Part 5 — Kayıt oturumu {#part-5}

`.mov` çoklu iz.

---

## Part 6 — Güvenilirlik {#part-6}

~25 sn arka plan; Interruption Coordinator.

---

## Part 7 — Dışa aktarma {#part-7}

MultiCamVideoComposer; seri kuyruk.

---

## Part 8 — Genel {#part-8}

Görünüm, Live Activity, diller.

---

## Part 9 — Yardım {#part-9}

Spotlight, deep link.

---

## Part 10 — Sorun giderme {#part-10}

| Belirti | Neden | Çözüm |
|---------|--------------|------------|
| Siyah ekran | Simülatör/destek yok | Gerçek Multi-Cam iPhone |
| Pending kilit sonrası | ~25 sn kayıt | Pending'den dışa aktar |
| Dışa aktarma hatası | Alan/Fotoğraflar | Add Photos |
| Boş liste | indeks | **Rescan Cache** |

---
