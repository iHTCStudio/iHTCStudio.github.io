iWidget รองรับ **`iwidget://`** บน **iPhone, iPad และ Mac** ใช้ใน Safari คำสั่งลัด แอปอื่น หรือ QR คำถามปฏิทินจันทรคติด้วยเสียงโดยไม่เปิดแอปใช้ Siri วันทำงานใช้ Workday Intent ไม่ใช่ URL

`iwidget://<host>[?query]` — host ที่ไม่รู้จักจะถูกละเว้น

| Host | เปิด | Query |
|------|------|-------|
| `today` | วันนี้ | — |
| `day` | วันนี้ → รายวัน | `y` `m` `d` |
| `library` | คลัง | `preset=` / `set=`, `detail=1` |
| `mine` | วิดเจ็ตของฉัน | `design=` / `id=`, `preset=` / `set=` |
| `editor` | ตัวแก้ไข | `design=` / `id=` (ไม่ระบุ = ล่าสุด) |
| `import` | นำเข้า | — |
| `settings` | การตั้งค่า | `scroll=festivals` · `weather` · `editor` · `access` |
| `membership` | สมาชิก | วิดเจ็ตที่หยุดชั่วคราวจะเปิดลิงก์นี้ |
| `launch` | ส่งต่อจากบล็อกทางลัด (iOS) | จากวิดเจ็ต |

ตัวอย่าง: `iwidget://today` · `iwidget://library?set=small.calendar&detail=1` · `iwidget://membership`

[กลับหน้าสนับสนุน](../) · [FAQ](../faq) · [สมาชิก](../membership) · [ความเป็นส่วนตัว](../privacy)
