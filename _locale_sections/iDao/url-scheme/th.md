idao รองรับ} `idao://` BAR ลิงก์ลัด (RUL scheme) การเริ่มหน้าจอหน้าจอเย็นและหน้าจอบ้าน จะถูกส่งไปผ่านระบบบัฟเฟอร์แบบรวม ดังนั้นลิงก์จึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
idao://{host}?{params}
```


## การค้นพบในบท

| URL | เปิด |
|-----|-------|
| `idao://home` | หน้าแรก |
| `idao://daily` | ทุก วัน นี้ |
| `idao://random` | หมุน & 90 |
| `idao://chapter?id={id}` | รายละเอียดในบท |
| `idao://recite` / `idao://recite?id={id}` | โฟลว์การท่อง |
| `idao://favorites` | รายการโปรด |
| `idao://famous` | บรรทัดขึ้นชื่อ |
| `idao://search` / `idao://search?q={query}` | ค้นหา |
| `idao://study` | หอ ประชุม ศึกษา |
| `idao://hunt` | สืบค้นเทา (寻道) |
| `idao://mastered` | สําเร็จการศึกษาแล้ว |
| `idao://categories` / `?section=` | เรียกดู (ส่วนตัวเลือก) |
| `idao://book?id=` | คอลเลกชันหนังสือ ('Dju' / hugging) |
| `idao://author` | ภาษาลาวซีName |
| `idao://last-read` | รายการที่อ่านล่าสุด |
| `idao://reading-history` | ประวัติการอ่าน |
| `idao://notes` | บันทึก |

> นามแฝงที่เข้ากันได้: `idao://` BAR `idao://home` c1 c saw;  c2 → การศึกษา;  c3  สืบค้น; `idao://chapter?id={id}` s   s      s. สืบค้น; c        ////s/s/s. parort;   BAR s s/s s/s/s.p.p. parm.

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `idao://settings` | การตั้งค่า |
| `idao://usage-guide` | คู่มือการใช้งาน |
| `idao://widget-guide` | คู่มือวิดเจ็ต |
| `idao://shortcuts-guide` | คู่มือทางลัด |
| `idao://feature-guide` | เล่นทัวร์แนะนำอีกครั้ง |
| `idao://feedback` | อีเมลข้อเสนอแนะ |
| `idao://in-app-review` | รีวิวในแอป / App Store |

## ตัวอย่าง


```
idao://daily
idao://chapter?id=1
idao://recite?id=1
idao://study
idao://hunt
idao://famous
idao://book?id=ddj
idao://author
idao://search?q=上善若水
```


ใช้เหล่านี้ในโปรแกรมปุ่มพิมพ์ลัด, การกระทําของหน้าจอส่วนตัวอย่างรวดเร็ว, วิดเจ็ต, ศูนย์ควบคุม, หรือซาฟารี ดูใน-apps ด้วย


