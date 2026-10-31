คำตอบสะท้อน**พฤติกรรมแอปปัจจุบัน** (หยุด/ต่อได้, คิวส่งออก, Live Activity, ตรวจอุปกรณ์, 繁體中文, คู่มือในแอป) ดูขั้นตอนใน [คู่มือผู้ใช้](index)

---

## อุปกรณ์และข้อกำหนด

### iPhone รุ่นใดรองรับ TwinPolarCam?

ต้องใช้ **`AVCaptureMultiCamSession`** — API มัลติแคมของ Apple โดยทั่วไป **iPhone XS/XR ขึ้นไป** ขึ้นกับร поколениеฮาร์ดแวร์

- **ไม่รองรับ** — หน้าจอเฉพาะตอนเปิด ไม่เริ่ม UI กล้อง
- **Simulator ไม่รองรับ**
- ต้องเป็น **iPhone จริง**

### ทำไมไม่ถอยเป็นกล้องเดียว?

การบันทึกสองกล้องพร้อมกันคือแกนผลิตภัณฑ์ ไม่มี fallback — ใช้ **คืนเงิน** หรือติดต่อซัพพอร์ต

### ความละเอียดสูงสุด?

**720p–4K** ต่อกล้อง (Main/PiP แยก) **iPhone 12+** มัก dual 4K ได้ รุ่นเก่าอาจจำกัด 1080p/2K

### ทำไมไม่มี 60 fps?

Multi-Cam ส่วนใหญ่ **สูงสุด 30 fps** TwinPolarCam มี **24/30** **ไม่รองรับ 60 fps**

### iPad/Mac?

**ไม่** — **iPhone เท่านั้น**

### iOS?

**ขั้นต่ำ 15.0** · Live Activity **16.2+**

---

## การบันทึกและ PiP

สลับ Main/PiP ด้วยปุ่ม **Switch/Flip** — ทั้งสองแทร็กบันทึกต่อ PiP ลาก/บีบ ตั้งค่าใน **App Settings → Picture-in-Picture** **ฝังในไฟล์ส่งออก** Preview pause ใช้ได้เมื่อ**ไม่ได้บันทึก** แฟลชเมื่อกล้องหลังเป็น Main

---

## การขัดจังหวะและความน่าเชื่อถือ

โทรศัพท์: **หยุดชั่วคราว** แล้ว**ต่อ segment เดิม** (`.mov`) Control Center อย่างเดียว**ไม่หยุด** พื้นหลัง: หยุด → Live Activity → **~25 วิ** → **Pending** บันทึกฉุกเฉินจบเซสชัน ช่วงหยุด**ตัดออก** (PTS jump-cut)

---

## Live Activity

**iOS 16.2+** **Background waiting** / **Saved** ปิดที่ **General → Recording Live Activity**

---

## ส่งออกและ Pending

Auto Export เปิด/ปิด คิว**เรียงตามเก่าสุด** ยกเลิกได้ ไฟล์ **`TwinPolarCam_*.mov`** **H.264/AAC** เก็บที่ `Application Support/...` **ไม่สำรอง iCloud**

---

## การตั้งค่าและภาษา

**English / 简体中文 / 繁體中文** Auto-Delete Original ค่าเริ่ม **ปิด** เพลงหยุด**เฉพาะตอนบันทึก**

---

## สิทธิ์และความเป็นส่วนตัว

**ไม่เก็บข้อมูล** [นโยบาย](../privacy) รูปภาพ **เพิ่มเท่านั้น**

---

## เคล็ดลับและซัพพอร์ต

**Send Feedback** **Help** `twinpolarcam://` [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

[คู่มือ](index) · [ลิงก์](../url-scheme) · [นโยบาย](../privacy)

---

## คู่มือฉบับเต็ม

Parts 1–10: เริ่มต้น, ควบคุม, PiP, เสียง, เซสชัน, ความน่าเชื่อถือ, ส่งออก, ทั่วไป, ช่วยเหลือ, แก้ปัญหา

---

## Part 1 — เริ่มต้น {#part-1}

Onboarding 6 หน้า สิทธิ์กล้อง/ไมค์/รูป Add Only Multi-Cam **XS/XR+**

---

## Part 2 — หน้าหลัก {#part-2}

แนวนอน Record Pause Stop Switch Screenshot

---

## Part 3 — กล้อง & PiP {#part-3}

720p–4K 24/30 fps

---

## Part 4 — เสียง {#part-4}

AAC/PCM เริ่ม session เมื่อ Record

---

## Part 5 — เซสชัน {#part-5}

`.mov` multi-track

---

## Part 6 — ความน่าเชื่อถือ {#part-6}

~25 วิ พื้นหลัง Interruption Coordinator

---

## Part 7 — ส่งออก {#part-7}

คิวเรียง MultiCamVideoComposer

---

## Part 8 — ทั่วไป {#part-8}

ธีม Live Activity ภาษา

---

## Part 9 — ช่วยเหลือ {#part-9}

Spotlight deep links

---

## Part 10 — แก้ปัญหา {#part-10}

| อาการ | สาเหตุ | แก้ |
|--------|--------|-----|
| จอดำ | Simulator/ไม่รองรับ | iPhone จริง |
| Pending หลังล็อก | ~25 วิ | ส่งออกจาก Pending |
| ส่งออกล้ม | พื้นที่/รูป | Add Photos |
| รายการว่าง | index | **Rescan Cache** |

---
