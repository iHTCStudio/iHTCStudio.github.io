### iAppManager คืออะไร?

**สถานีงาน App Store Connect แบบ native** สำหรับ iPhone, iPad และ Mac ลงชื่อด้วย **API Key** จัดการเวอร์ชัน ภาพหน้าจอ IAP TestFlight ใบรับรอง รายงาน และรีวิว — ทรaffic **ไปที่ Apple โดยตรง** ไม่ต้องมีบัญชี iHTC Studio

### ขอ API Key อย่างไร?

1. เปิด [App Store Connect](https://appstoreconnect.apple.com) → **Users and Access** → **Integrations** → **App Store Connect API**
2. สร้างคีย์ (แนะนำ Admin หรือ App Manager)
3. ดาวน์โหลด `.p8` **ครั้งเดียว** จด **Issuer ID** และ **Key ID**
4. วางใน iAppManager (หรือเลือกไฟล์) คู่มือในแอปมีภาพหน้าจอแนะนำทีละขั้น

### `.p8` ถูกอัปโหลดไป iHTC Studio ไหม?

**ไม่** คีย์ส่วนตัวอยู่ใน **Keychain บนอุปกรณ์** เท่านั้น คำขอถูกเซ็นบนเครื่องแล้วส่งไป `api.appstoreconnect.apple.com` ลบบัญชีจะลบคีย์ในเครื่อง

### ต้องใส่รหัส Apple ID ในแอปไหม?

**ไม่** ยืนยันตัวตนด้วย **API Key เท่านั้น** (Issuer ID + Key ID + `.p8`) ฟีเจอร์ที่ไม่มี public API (เช่น privacy nutrition labels โค้ดโปรโม App ฟรี) แอปจะเปิดเว็บ Apple ให้คุณใช้ Apple ID ใน Safari/ASC

### อัปโหลด IPA / PKG โดยไม่ใช้ Transporter ได้ไหม?

**ได้** iAppManager ใช้ **Build Upload REST** ของ Apple (WWDC25) ไฟล์ใหญ่แนะนำ **Mac** iOS ใช้ API เดียวกันแต่อัปโหลดใหญ่ไม่สะดวก

### "on sale" ในตัวกรอง / วิดเจ็ต หมายถึงอะไร?

**พร้อมจำหน่ายอย่างน้อยหนึ่งประเทศใน App Store** สถานะ pipeline (waiting / in review / rejected / pending developer release) ติดตามแยก วิดเจ็ต **Needs attention** = waiting + in review + rejected + pending release (รวมในเครื่อง ไม่ใช่ฟิลด์ ASC)

### hard vs soft ก่อนส่ง?

**Hard blockers** หยุดการส่ง (เช่น build ยังไม่พร้อม ต้องมี demo account แต่ไม่มี) **Soft checks** เตือน (ขนาดภาพหลัก ลิขสิทธิ์ เรตตингอายุ ฯลฯ) ยืนยันแล้วดำเนินต่อได้ ดู Overview / Versions / Submissions `?` หรือ `iappmanager://release-guide`

### รองรับภาษาอะไร?

**English · 简体中文 · 繁體中文** ตามระบบหรือบังคับใน Settings สลับภาษาแบบ hot-swap **ไม่** remount root (นำทางและ draft คงอยู่)

### ทำไมวิดเจ็ตไม่แสดงตัวเลข ASC สด?

วิดเจ็ต **ไม่เรียก ASC** แอปหลักสแกนแล้วเขียน snapshot (~10 นาที TTL ชุดเดียวกับ My Apps) เปิดแอปแล้วรีเฟรชรายการ (หรือบังคับรีเฟรชสถานะ)

### ความต่าง macOS กับ iOS?

ทั้งคู่ครอบคลุม store monetization TestFlight Game Center users reports reviews Webhooks **IPA ใหญ่** และติดตั้งใบรับรองใน system Keychain แนะนำ **Mac** ไอคอนแอปสำรอง **เฉพาะ iOS**

### URL นโยบายความเป็นส่วนตัวสำหรับ App Store Connect?

เปิด [Privacy Policy](../privacy) บนไซต์นี้แล้วคัดลอก URL จากแถบที่อยู่เบราว์เซอร์

### ความต้องการระบบ?

iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+**

### ติดต่อฝ่ายสนับสนุน?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — โดยทั่วไปภายใน 48 ชั่วโมง
