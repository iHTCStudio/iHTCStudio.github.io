**ปล่อยแอปเร็วขึ้น ออกจากเขาวงกตเบราว์เซอร์**

iAppManager (爱应用者) คือ **สถานีงาน App Store Connect แบบ native** สำหรับ iPhone, iPad และ Mac ลงชื่อด้วย **API Key** เก็บข้อมูลใน **Keychain** และคุย **ตรงกับ Apple** — เวอร์ชัน สกรีนช็อต IAP TestFlight ใบรับรอง รายงานยอดขาย และรีวิวลูกค้าในที่เดียว **ไม่ต้องมีบัญชี iHTC Studio ไม่มีโฆษณา ไม่มี analytics SDK ไม่มี backend บุคคลที่สามสำหรับข้อมูล ASC**

**สรุป:** ล็อกอิน API Key หลายบัญชี · รายการแอปพร้อม filt แพลตฟอร์มและ pipeline · checklist ความพร้อม Overview · เวอร์ชันและ review submissions · Build Upload REST (IPA/PKG) · metadata และสื่อพร้อมคัดลอกข้าม locale · Custom Product Pages · In-App Events · App Clips · store experiments · featuring · availability และราคา · เรตติ้งอายุ · accessibility · App Tags · IAP และสมาชิก · Game Center · TestFlight · รีวิว · ใบรับรองและอุปกรณ์ · ผู้ใช้และบทบาท · รายงาน sales/finance/Analytics · Webhooks · วิดเจ็ตและ deep link `iappmanager://` · English / 简体 / 繁體

> สำหรับนักพัฒนาอินดีและทีมเล็กที่อยู่ใน App Store Connectทุกสัปดาห์ — โต๊ะทำงานที่รู้สึกเหมือนแอป Mac ไม่ใช่ฟาร์มแท็บ

## เริ่มต้น

1. สร้าง **App Store Connect API Key** (แนะนำ Admin หรือ App Manager): App Store Connect → **Users and Access** → **Integrations** → **App Store Connect API** → สร้างคีย์ ดาวน์โหลด **`.p8` ครั้งเดียว** จด **Issuer ID** + **Key ID**
2. เปิด iAppManager → วาง Issuer ID / Key ID / PEM (หรือเลือก `.p8`) → ตรวจสอบ (`GET /v1/apps`) คีย์อยู่ใน **Keychain** ของเครื่องนี้
3. ทำ **onboarding** สั้น (ใบรับรอง · รายงาน · วิดเจ็ต · ความเป็นส่วนตัว) ดู guide ซ้ำที่ **Settings → Help**
4. ใน **My Apps** เลือก **list / grid / cards** ปักหมุดรายการโปรด filt **แพลตฟอร์ม** (iOS / macOS / tvOS / visionOS) หรือ **สถานะ** (on sale · off sale · waiting · in review · rejected · pending developer release)
5. เปิดแอป → เริ่มที่ **Overview** (เวอร์ชัน/build ล่าสุด shortcuts checklist แบบ soft submissions ล่าสุด)
6. เส้นทาง release: **Versions** → แนบ **Build** → **Metadata / Media** → **Review Detail** → ส่งผ่าน **Review Submissions** (หรือ "send now")
7. เพิ่ม **วิดเจ็ต Home Screen** (Account Hub, Apps Pulse, Review Desk, Quick Actions) และลอง `iappmanager://` จาก Shortcuts

> คู่มือ **Release / IAP / TestFlight / Reports** ในแอปแตะครั้งเดียว (deep link ด้านล่าง)

## ทำไมควรดาวน์โหลด

- **โต๊ะ native เดียวสำหรับการปล่อยทั้งหมด** — หยุดสลับแท็บ ASC สำหรับเวอร์ชัน assets IAP TestFlight certs และรายงาน
- **API Key ไม่ใช่รำแ dance รหัสผ่าน** — Issuer ID + Key ID + `.p8` ใน Keychain หลายบัญชี ลบบัญชีลบคีย์ local
- **อัปโหลด build โดยไม่ใช้ Transporter** — WWDC25 **Build Upload REST** สำหรับ IPA/PKG pipeline เดียวกันบน iOS (ไฟล์ใหญ่ยังแนะนำ Mac)
- **คู่มือละเอียดในแอป** — release readiness IAP TestFlight และ reports อธิบาย hard vs soft checks
- **เห็น pipeline บน Lock Screen** — วิดเจ็ตสะท้อน on sale / waiting / in review / rejected / pending release
- **ความเป็นส่วนตัวโดยสถาปัตยกรรม** — ASC ไปที่ `api.appstoreconnect.apple.com` iHTC Studio ไม่โฮสต์แอป คีย์ หรือรายงานของคุณ

## ฟีเจอร์

### ล็อกอินและบัญชี

- **API Key เท่านั้น** (Issuer ID / Key ID / `.p8`) — ไม่มี Apple ID OAuth ในแอป
- Keychain **หลายบัญชี** sign-out / remove ลบ secret local
- คู่มือ **"วิธีรับ API Key"** ในแอป

### My Apps

- **List / grid / cards** (ค่าเริ่ม list) ควบคุมคอลัมน์
- **Pin** ต่อบัญชี filt **platform** และ **status** cache ~10 นาที (force refresh)
- **On sale = มีอย่างน้อยหนึ่ง territory** pipeline buckets แยกจาก storefront
- Context menu: pin ไปโมดูล คัดลอก name / Bundle ID / Apple ID / SKU เปิด App Store หรือ ASC
- ไอคอน: ASC build artwork → iTunes Lookup → monogram cache

### Overview และความพร้อม release

- สรุปเวอร์ชัน/build shortcuts submissions ล่าสุด
- **Soft checklist** (ขนาด screenshot หลัก copyright age rating ฯลฯ)
- **Hard blockers** ใน Versions / Submissions
- Guide: `iappmanager://release-guide`

### เวอร์ชัน builds และ submissions

- สร้างเวอร์ชัน แนบ build submit / cancel โหมด release phased **Release Now**
- **Build Upload REST** IPA/PKG Background Assets encryption declarations
- **Review Submissions** และ **Review Detail**

### Store listing และการเติบโต

- **Metadata** screenshots previews batch assets download-size workbench
- **Custom Product Pages** In-App Events App Clips store experiments featuring
- **Availability** **pricing** age rating accessibility App Tags
- **⌘S** บันทึกบน Mac

### การสร้างรายได้และ Game Center

- IAP / subscription groups offers CSV
- Guide: `iappmanager://iap-guide`
- **Game Center**

### TestFlight

- กลุ่ม ลิงก์สาธารณะ metrics feedback export
- Guide: `iappmanager://testflight-guide`

### ใบรับรอง ผู้ใช้ รายงาน รีวิว

- Certificates profiles devices users reports customer reviews webhooks
- Guide: `iappmanager://reports-guide`

### วิดเจ็ต shortcuts

- Account Hub Apps Pulse Review Desk Quick Actions
- `iappmanager://` — [Shortcut Links](url-scheme)

### ความเป็นส่วนตัว

- API secrets ใน **Keychain** เรียก **Apple** เท่านั้น
- รายละเอียด: [Privacy Policy](privacy)

## ดาวน์โหลด

| ช่องทาง | ลิงก์ |
|---------|------|
| App Store | [Download on the App Store](https://apps.apple.com/app/id6794497110) |

## ความต้องการระบบ

| ส่วน | ขั้นต่ำ |
|------|---------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |
| Widgets | iOS 17.0+ |
| IPA ใหญ่ | แนะนำ **Mac** |

## ติดต่อ

- **Email:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

มักตอบภายใน 48 ชั่วโมง

[FAQ](faq) · [Shortcut Links](url-scheme) · [Privacy Policy](privacy)
