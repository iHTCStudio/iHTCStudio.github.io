iArtofwar รองรับ ** `iartofwar://` BAR * ลิงก์ลัด (URL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
iartofwar://{host}?{params}
```


## ผู้เขียน

| URL | เปิด |
|-----|-------|
| `iartofwar://passage?id={id}` | รายละเอียดข้อความ |
| `iartofwar://couplet?id={id}` / `iartofwar://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `iartofwar://author?id={id}` | รายละเอียดผู้แต่ง |
| `iartofwar://recite` / `iartofwar://recite?id={id}` | โฟลว์การท่อง |

## ค้นพบ

| URL | เปิด |
|-----|-------|
| `iartofwar://home` | หน้าแรก |
| `iartofwar://daily` | ทุก วัน นี้ |
| `iartofwar://random` | ข้อความแบบสุ่ม |
| `iartofwar://favorites` | รายการโปรด |
| `iartofwar://famous` | เส้น เสียง ที่ มี ชื่อ เสียง / เส้น เสียง |
| `iartofwar://search` / `iartofwar://search?q={query}` | ค้นหา |
| `iartofwar://study` | ห้องเรียนช่างวางแผน |
| `iartofwar://hunt` | ล่า (寻谋; สืบค้นเมื่อ 'คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน' |
| `iartofwar://mastered` | สําเร็จการศึกษาแล้ว |
| `iartofwar://categories` / `iartofwar://categories?section=` | เรียกดู ('theme', 'volume', ...) |
| `iartofwar://collection?id=` | คอลเลกชันหนังสือ (e.g. `Sunzi', 'woujing', 'wuzi'; และยังมี 'ชื่อ=' / eme=') |
| `iartofwar://theme?id=` | statagem set หรือ volum (e.g. usn-tao', ~ ชนะ ', 'Sunbin-a') |
| `iartofwar://last-read` | รายการที่อ่านล่าสุด |
| `iartofwar://reading-history` | ประวัติการอ่าน |
| `iartofwar://notes` | บันทึก |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `iartofwar://settings` | การตั้งค่า |
| `iartofwar://usage-guide` | คู่มือการใช้งาน |
| `iartofwar://widget-guide` | คู่มือวิดเจ็ต |
| `iartofwar://shortcuts-guide` | คู่มือทางลัด |
| `iartofwar://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `iartofwar://feedback` | อีเมลข้อเสนอแนะ |
| `iartofwar://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
iartofwar://daily
iartofwar://passage?id=1
iartofwar://collection?id=wuzi
iartofwar://theme?id=wen-tao
iartofwar://study
iartofwar://hunt
```


ใช้เหล่านี้ในโปรแกรมปุ่มพิมพ์ลัด, การกระทําของหน้าจอส่วนตัวอย่างรวดเร็ว, วิดเจ็ต, หรือ Saveri ดูใน-apps ด้วย


