iLunYu รองรับ~ `ilunyu://` BAR * ลิงก์ลัด (RUL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
ilunyu://{host}?{params}
```


## บทและผู้เขียน

| URL | เปิด |
|-----|-------|
| `ilunyu://passage?id={id}` | รายละเอียดในบท |
| `ilunyu://couplet?id={id}` / `ilunyu://poem?id={id}` | เช่นเดียวกันกับเนื้อเรื่อง (ความเข้ากันได้) |
| `ilunyu://author?id={id}` | รายละเอียดผู้แต่ง |
| `ilunyu://recite` | โฟลว์การท่อง |
| `ilunyu://recite?id={id}` | เปิดและปรับอัตโนมัติ |

## ค้นพบ

| URL | เปิด |
|-----|-------|
| `ilunyu://home` | แท็บหน้าแรก |
| `ilunyu://daily` | ข้อ คัมภีร์ ประจํา วัน |
| `ilunyu://random` | หมุน & 90 |
| `ilunyu://favorites` | รายการโปรด |
| `ilunyu://famous` | บรรทัดขึ้นชื่อ |
| `ilunyu://search` / `ilunyu://search?q={query}` | ค้นหา |
| `ilunyu://study` | ห้องเรียนเรียน |
| `ilunyu://hunt` | ล่า (寻章; สืบค้นเมื่อ 'คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน' |
| `ilunyu://mastered` / `ilunyu://progress` | ประมวลผล / คืบหน้า |
| `ilunyu://categories` / `ilunyu://categories?section=` | เรียกดู |
| `ilunyu://collection?id=lunyu` | คอลเลกชันหนังสือ (อัลบั้ม ''' / ฟอร์ม'; และยัง 'ชื่อ=') |
| `ilunyu://theme?id=` | ชุดตกแต่ง หรือ ระดับเสียง (เช่น 'hunzi', 'xue-er'; นามแฝง an suffe' / 'volume') |
| `ilunyu://last-read` | รายการที่อ่านล่าสุด |
| `ilunyu://reading-history` | ประวัติการอ่าน |
| `ilunyu://notes` | บันทึก |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `ilunyu://settings` | การตั้งค่า |
| `ilunyu://usage-guide` | คู่มือการใช้งาน |
| `ilunyu://widget-guide` | คู่มือวิดเจ็ต |
| `ilunyu://shortcuts-guide` | คู่มือทางลัด |
| `ilunyu://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `ilunyu://feedback` | อีเมลข้อเสนอแนะ |
| `ilunyu://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
ilunyu://daily
ilunyu://passage?id=1
ilunyu://recite?id=20
ilunyu://theme?id=junzi
ilunyu://study
ilunyu://hunt
```


ใช้เหล่านี้ในโปรแกรมปุ่มพิมพ์ลัด, การกระทําของหน้าจอส่วนตัวอย่างรวดเร็ว, วิดเจ็ต, หรือ Saveri ดูใน-apps ด้วย


