isutrra รองรับ... `isutra://` BAR ลิงก์ลัด (URL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
isutra://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `isutra://passage?id={id}` | รายละเอียด |
| `isutra://couplet?id={id}` / `isutra://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `isutra://author?id={id}` | รายละเอียดผู้แปล/ ผู้เขียน |
| `isutra://recite` / `isutra://recite?id={id}` | โฟลว์การท่อง |
| `isutra://large?id=diamond` / `isutra://large?id=dizang` | แคตตาล็อกระดับเสียงขนาดใหญ่ |

## การท่องเว็บ

| URL | เปิด |
|-----|-------|
| `isutra://home` | หน้าแรก |
| `isutra://daily` | ทุก วัน นี้ |
| `isutra://random` | ข้อความแบบสุ่ม |
| `isutra://favorites` | รายการโปรด |
| `isutra://famous` | บรรทัดขึ้นชื่อ |
| `isutra://search` / `isutra://search?q={query}` | ค้นหา |
| `isutra://study` | หอ ประชุม ศึกษา |
| `isutra://hunt` | ล่า (寻经; สืบค้นเมื่อ 'คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน' |
| `isutra://count` | เสียงร้องของปลาวู้ดเซ่น ('Chant' / 'Muuu' /'ผู้นับ') |
| `isutra://copy` / `isutra://copy?id={id}` | คัดลอก- สุตรา (ไอOS) |
| `isutra://practice` | เช้า / ฝึก ตอน เย็น |
| `isutra://mastered` | สําเร็จการศึกษาแล้ว |
| `isutra://categories` / `isutra://categories?section=` | เรียกดู |
| `isutra://collection?id=` | ชุดสะสม (e.g. `rajna', 'porty-2'; และชื่อด้วย'=') |
| `isutra://theme?id=` | ชุดตกแต่ง (e.g. สืบค้นเมื่อ '%sing yoan', asaishi', `partiform') |
| `isutra://last-read` | รายการที่อ่านล่าสุด |
| `isutra://reading-history` | ประวัติการอ่าน |
| `isutra://notes` | บันทึก |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `isutra://settings` | การตั้งค่า |
| `isutra://usage-guide` | คู่มือการใช้งาน |
| `isutra://widget-guide` | คู่มือวิดเจ็ต |
| `isutra://shortcuts-guide` | คู่มือทางลัด |
| `isutra://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `isutra://privacy` | ความเป็นส่วนตัว |
| `isutra://feedback` | อีเมลข้อเสนอแนะ |
| `isutra://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
isutra://daily
isutra://passage?id=1
isutra://large?id=diamond
isutra://count
isutra://copy?id=1
isutra://practice
isutra://collection?id=prajna
isutra://theme?id=xingyuan
isutra://study
isutra://hunt
```


ใช้เหล่านี้ในโปรแกรมปุ่มพิมพ์ลัด, การกระทําของหน้าจอส่วนตัวอย่างรวดเร็ว, วิดเจ็ต, หรือ Saveri ดูใน-apps ด้วย


