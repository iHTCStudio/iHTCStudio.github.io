igusand รองรับ~ `ithousand://` BAR ลิงก์ลัด (RUL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
ithousand://{host}?{params}
```


## Passage, ผู้เขียนและอักขระ

| URL | เปิด |
|-----|-------|
| `ithousand://passage?id={id}` | รายละเอียดข้อความ |
| `ithousand://passage?id={id}&open=study` | Passage → ไพรเซอร์ฮอลล์ |
| `ithousand://passage?id={id}&open=characters` | Passage → ตารางอักขระ |
| `ithousand://passage?id={id}&open=note` | Passage log |
| `ithousand://author?id={id}` | รายละเอียดผู้แต่ง |
| `ithousand://recite` / `ithousand://recite?id={id}` | โฟลว์การท่อง |
| `ithousand://characters` | ไลบรารีอักขระ |
| `ithousand://character?char=天` | โฟกัสไพ่อักขระ |
| `ithousand://characters?id={id}` | บัตรอักขระโดยหมายเลข |
| `ithousand://saved-characters` | บันทึกอักขระ |
| `ithousand://saved-famous` | บันทึกบรรทัดที่มีชื่อเสียง |

## ค้นพบ

| URL | เปิด |
|-----|-------|
| `ithousand://home` | หน้าแรก |
| `ithousand://daily` | ข้อ คัมภีร์ ประจํา วัน |
| `ithousand://random` | ข้อความแบบสุ่ม |
| `ithousand://favorites` | รายการโปรด |
| `ithousand://list?id={uuid}` | รายชื่อส่วนตัว (千单) |
| `ithousand://famous` | บรรทัดขึ้นชื่อ |
| `ithousand://search` / `ithousand://search?q={query}` | ค้นหา |
| `ithousand://study` | ห้องโถงหลัก |
| `ithousand://hunt` | ล่า (寻字; สืบค้นเมื่อ 'คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน' |
| `ithousand://mastered` | สําเร็จการศึกษาแล้ว |
| `ithousand://categories` / `ithousand://categories?section=` | เรียกดู |
| `ithousand://collection?id=qianziwen` | คอลเลกชันของไพรม์เซอร์ (ชื่อ=' รองรับด้วย) |
| `ithousand://theme?id=dizigui-filial` | ชุดตกแต่ง |
| `ithousand://last-read` | รายการที่อ่านล่าสุด |
| `ithousand://reading-history` | ประวัติการอ่าน |
| `ithousand://notes` | บันทึก |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `ithousand://settings` | การตั้งค่า |
| `ithousand://privacy` | ความเป็นส่วนตัว |
| `ithousand://usage-guide` | คู่มือการใช้งาน |
| `ithousand://widget-guide` | คู่มือวิดเจ็ต |
| `ithousand://shortcuts-guide` | คู่มือทางลัด |
| `ithousand://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `ithousand://feedback` | อีเมลข้อเสนอแนะ |
| `ithousand://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
ithousand://daily
ithousand://passage?id=1
ithousand://passage?id=1&open=characters
ithousand://character?char=天
ithousand://collection?id=qianziwen
ithousand://study
ithousand://hunt
ithousand://saved-characters
```


ใช้เหล่านี้ในโปรแกรมปุ่มพิมพ์ลัด, การกระทําของหน้าจอส่วนตัวอย่างรวดเร็ว, วิดเจ็ต, หรือ Saveri ค่าคงที่ `ithousand://` พารามิเตอร์เมื่อใช้ได้ ดูใน-apps ด้วย


