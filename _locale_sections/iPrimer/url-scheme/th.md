iPrimiter รองรับ ** `iprimer://` BAR * ลิงก์ลัด (URL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
iprimer://{host}?{params}
```


## บทและผู้เขียน

| URL | เปิด |
|-----|-------|
| `iprimer://chapter?id={id}` | รายละเอียดในบท |
| `iprimer://passage?id={id}` / `iprimer://poem?id={id}` | เหมือนกับบท (ความเข้ากันได้) |
| `iprimer://author?id={id}` | รายละเอียดผู้แต่ง |
| `iprimer://recite` / `iprimer://recite?id={id}` | โฟลว์การท่อง |

## ค้นพบ

| URL | เปิด |
|-----|-------|
| `iprimer://home` | หน้าแรก |
| `iprimer://daily` | การ ศึกษา ประจํา วัน |
| `iprimer://random` | หมุน & 90 |
| `iprimer://favorites` | รายการโปรด |
| `iprimer://famous` | บรรทัดขึ้นชื่อ |
| `iprimer://search` / `iprimer://search?q={query}` | ค้นหา |
| `iprimer://study` | การศึกษาอักขระ |
| `iprimer://meditation` | พิจารณารายการหลักสูตร |
| `iprimer://meditation?slug={slug}&autostart=1` | เปิดวาระการใช้งานและเริ่มอัตโนมัติ (จากก่อน) |
| `iprimer://guidance` | การนําทางชีวิต (นิสัยต่าง ๆ) |
| `iprimer://hunt` | ล่า (寻句; สืบค้นเมื่อ 'คีย์เวิร์ด-ฮันต์' / 'ดอกไม้แมลงวัน' |
| `iprimer://mastered` | บทหลัก |
| `iprimer://categories` / `iprimer://categories?section=` | เรียกดู |
| `iprimer://collection?id=xiaoxue` | คลังภาพ Sublicue (ชื่อ'=' รองรับด้วย) |
| `iprimer://theme?id=lijiao` | ระดับเสียง / ชุดตกแต่ง (ชื่อ) |
| `iprimer://last-read` | รายการที่อ่านล่าสุด |
| `iprimer://reading-history` | ประวัติการอ่าน |
| `iprimer://notes` | บันทึก |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `iprimer://settings` | การตั้งค่า |
| `iprimer://usage-guide` | คู่มือการใช้งาน |
| `iprimer://widget-guide` | คู่มือวิดเจ็ต |
| `iprimer://shortcuts-guide` | คู่มือทางลัด |
| `iprimer://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `iprimer://feedback` | อีเมลข้อเสนอแนะ |
| `iprimer://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
iprimer://daily
iprimer://chapter?id=3
iprimer://collection?id=xiaoxue
iprimer://theme?id=lijiao
iprimer://study
iprimer://meditation?slug=emotion_calm&autostart=1
iprimer://guidance
iprimer://hunt
```


ใช้เหล่านี้ในโปรแกรมปุ่มพิมพ์ลัด, การกระทําของหน้าจอส่วนตัวอย่างรวดเร็ว, วิดเจ็ต, หรือ Saveri ค่าคงที่ `iprimer://` พารามิเตอร์เมื่อใช้ได้ ดูใน-apps ด้วย


