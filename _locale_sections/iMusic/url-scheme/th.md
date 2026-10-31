iMusic รองรับ} `imusic://` BAR ลิงก์ลัด เริ่มต้นแบบเย็นและแสดงทางลัดหน้าจอบ้าน ผ่านการรวมกันของบัฟเฟอร์ ดังนั้นการเชื่อมโยงจึงไม่ถูกเปิดสองครั้งหลังจากขึ้นเครื่อง

## รูปแบบลิงก์


```
imusic://{host}?{params}
```


ชุดสีคือ ~ BAR `imusic://` BAR เท่านั้น

## ส่วนตัวและวันนี้

| URL | เปิด |
|-----|-------|
| `imusic://` / `imusic://home` | หน้าแรก |
| `imusic://daily` / `imusic://today` | Daily Bart (เป็นเพลงของเพลงเท่านั้น) |
| `imusic://random` | รอม (ใคร) |
| `imusic://play` | เล่น |
| `imusic://last` / `imusic://lastheard` | ได้ยินครั้งสุดท้าย |

## ชิ้นส่วนและศิลปิน

| URL | เปิด |
|-----|-------|
| `imusic://piece?id={id}` | ไกด์ชิ้น ('passage' / 'song' ก็ตอบรับด้วย) |
| `imusic://artist?id={id}` / `imusic://artist?name={name}` | โต๊ะศิลปิน |
| `imusic://artists` / `imusic://singers` | ไดเรกทอรีศิลปิน |
| `imusic://famous` / `imusic://lines` | บรรทัดขึ้นชื่อ |

เครื่องวางไพ่ร่วมอาจเพิ่ม c0     (ชื่อศิลปิน) สําหรับมนุษย์ การจับคู่ยังคงใช้~ `imusic` BAR อย่างเดียว ~

## เรียกดู, ค้นหาและรับฟัง

| URL | เปิด |
|-----|-------|
| `imusic://categories` / `imusic://browse` | เรียกดู (รายการ) |
| `imusic://collection?id={id}` | ชุดสะสม ('id=colall' is the return all bits list) |
| `imusic://search` / `imusic://search?q={query}` | ค้นหา |
| `imusic://favorites` | รายการโปรด |
| `imusic://later` | รายการโปรด, เลื่อนไปทีหลัง |
| `imusic://lists` / `imusic://listenlists` | ชื่อรายการ: |
| `imusic://history` | ประวัติ |
| `imusic://notes` | บันทึก |
| `imusic://mastered` | เรียบร้อยแล้ว |
| `imusic://streak` / `imusic://footprint` | สไตรก |

เปิดชิ้นเดียว, มินิบาร์, หรือ ID ของเพลง ~ ลําดับการอ่านคิวของชิ้นส่วนนั้น การเปิดจากชุดสะสม, สืบค้น หรือศิลปิน จะคงรายการดังกล่าวไว้ต่อไปและก่อนหน้าจะยังคงอยู่

## หมายเลขเพลง, อารมณ์ของโรงเรียน

| URL | เปิด |
|-----|-------|
| `imusic://recognize` / `imusic://shazam` | หมายเลขเพลง |
| `imusic://school` / `imusic://earschool` | โรงเรียนหู |
| `imusic://timeline` / `imusic://corridor` | เส้นพริ้วไหว |
| `imusic://compare` | เปรียบ เทียบ การ ฟัง |
| `imusic://mood?id={id}` | เริ่มที่อารมณ์ ('part=' / 'partid=' เป็นร่องเริ่มต้นเท่านั้น; อารมณ์ยังคงตรงกับ 'id') |

## การตั้งค่าและคู่มือ

| URL | เปิด |
|-----|-------|
| `imusic://settings` | การตั้งค่า |
| `imusic://usageguide` / `imusic://featureguide` | คํา แนะ นํา ที่ ใช้ ได้ จริง |
| `imusic://widgetguide` | คู่มือวิดเจ็ต |
| `imusic://shortcutsguide` | คู่มือทางลัด |
| `imusic://feedback` | แหล่งป้อน |
| `imusic://review` / `imusic://in-app-review` | In-app review (เมื่อรายการร้านค้าสด) |

## หน้าจอส่วนตัว

จง ถาม ซีรี สําหรับ งาน ประจํา วัน, การ ท่อง เที่ยว, การ ค้น หา, หรือ สิ่ง ที่ คุณ ชอบ หลัง จาก คุณ เพิ่ม ทางลัด. ปรับแต่งการกระทําอย่างรวดเร็วของหน้าจอส่วนตัวใน~. ตั้งค่าปุ่มพิมพ์ลัด~ ตัวอย่างเต็มรูปแบบ อาศัยอยู่ในคู่มือทางลัด

[FAQ](./faq). สืบค้นเมื่อ 20 พฤษภาคม พ.ศ.


