#!/usr/bin/env python3
"""Render _locale_sections/{App}/privacy/{locale}.md from English privacy bodies."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC_ROOT = ROOT / "_locale_sections"
LOCALES = ("ja", "ko", "ru", "th", "de", "fr", "tr")
APPS = [
    "iBaiJia",
    "iGuanZhi",
    "iGuige",
    "iHanFei",
    "iLvShi",
    "iMencius",
    "iMoZi",
    "iPrecepts",
    "iPrimer",
    "iRhyme",
    "iSage",
    "iShangYang",
    "iSiShu",
    "iSutra",
    "iThousand",
    "iWuJing",
    "iXin",
    "iXunZi",
    "iZen",
    "iZengZi",
    "iZhuangZi",
    "iZiSi",
]

SECTION_RE = re.compile(
    r'<section lang="en"[^>]*>\n?(?P<body>.*?)(?=\n<section lang=|\Z)',
    re.DOTALL,
)
SEC_ANY = re.compile(
    r'<section lang="([^"]+)"[^>]*>\n?(?P<body>.*?)(?=\n<section lang=|\Z)',
    re.DOTALL,
)

PLACEHOLDER_RE = re.compile(
    r"\{APP\}|\{APPID\}|\{BUNDLE\}|\{GROUP\}|\{CNNAME\}|\{HAN\}|\{TIPID\}"
)


def extract_en(app: str) -> str:
    text = (ROOT / app / "privacy.md").read_text(encoding="utf-8")
    m = SECTION_RE.search(text)
    if not m:
        raise SystemExit(f"no en section: {app}")
    body = m.group("body").strip()
    if body.endswith("</section>"):
        body = body[: -len("</section>")].strip()
    return body


def build_exact_map() -> dict[str, dict[str, str]]:
    exact: dict[str, dict[str, str]] = {}

    def ingest_sections(sections: dict[str, list[str]]) -> None:
        en = sections.get("en")
        if not en:
            return
        for lang in LOCALES:
            tr = sections.get(lang)
            if not tr or len(tr) != len(en):
                continue
            for el, tl in zip(en, tr):
                el, tl = el.rstrip(), tl.rstrip()
                if el.strip() and tl.strip():
                    exact.setdefault(el, {})[lang] = tl

    for p in ROOT.glob("**/privacy.md"):
        if "_locale_sections" in p.parts:
            continue
        sections: dict[str, list[str]] = {}
        for m in SEC_ANY.finditer(p.read_text(encoding="utf-8")):
            sections[m.group(1)] = m.group("body").strip().splitlines()
        ingest_sections(sections)

    for loc in SEC_ROOT.glob("*/privacy/*.md"):
        app = loc.parent.parent.name
        lang = loc.stem
        if app in APPS or lang not in LOCALES:
            continue
        main = ROOT / app / "privacy.md"
        if not main.exists():
            continue
        en_m = SECTION_RE.search(main.read_text(encoding="utf-8"))
        if not en_m:
            continue
        en_lines = en_m.group("body").strip().splitlines()
        tr_lines = loc.read_text(encoding="utf-8").strip().splitlines()
        if len(en_lines) != len(tr_lines):
            continue
        for el, tl in zip(en_lines, tr_lines):
            el, tl = el.rstrip(), tl.rstrip()
            if el.strip() and tl.strip():
                exact.setdefault(el, {})[lang] = tl

    def merge_hand_map(data: dict[str, dict[str, str]]) -> None:
        """Hand-curated maps override aligned sections (often English placeholders)."""
        for el, langs in data.items():
            bucket = exact.setdefault(el, {})
            for lang, tl in langs.items():
                if lang in LOCALES and tl.strip():
                    bucket[lang] = tl.rstrip()

    gaps = ROOT / "scripts" / "_privacy_gaps_22.json"
    if gaps.exists():
        merge_hand_map(json.loads(gaps.read_text(encoding="utf-8")))

    partial = ROOT / "scripts" / "_privacy_line_map_partial.json"
    if partial.exists():
        merge_hand_map(json.loads(partial.read_text(encoding="utf-8")))

    return exact


def normalize(line: str) -> str:
    s = line
    # Preserve brand / Apple service names before app-id templating.
    s = s.replace("iHTC Studio", "\0IHTC_STUDIO\0")
    s = s.replace("**iCloud**", "\0ICLOUD_BOLD\0")
    s = s.replace("iCloud", "\0ICLOUD\0")
    s = s.replace("iOS", "\0IOS\0")
    s = s.replace("iPadOS", "\0IPADOS\0")
    s = re.sub(r"\*\*i[A-Z][A-Za-z0-9]*\*\*", "**{APP}**", s)
    s = re.sub(r"`group\.com\.iHTCboy\.\w+`", "`{GROUP}`", s)
    s = re.sub(r"`com\.iHTCboy\.\w+\.\d+`", "`{TIPID}`", s)
    s = re.sub(r"`com\.iHTCboy\.\w+`", "`{BUNDLE}`", s)
    s = re.sub(r'"[^"]*[\u4e00-\u9fff][^"]*"', '"{CNNAME}"', s)
    s = re.sub(r"(?<![A-Za-z0-9])i[A-Z][A-Za-z0-9]*(?![A-Za-z0-9])", "{APPID}", s)
    s = re.sub(r"[\u4e00-\u9fff]+(?: / [\u4e00-\u9fff]+)?", "{HAN}", s)
    s = re.sub(r"\| [A-Za-z\u4e00-\u9fff /+–\-]+ database \|", "| {DB} database |", s)
    s = re.sub(
        r"recite, [^,|]+, widgets, and daily notifications",
        "recite, {STUDY}, widgets, and daily notifications",
        s,
    )
    s = re.sub(
        r"recite, [^,|]+, meditation, Life Guidance, widgets",
        "recite, {STUDY}, meditation, Life Guidance, widgets",
        s,
    )
    s = re.sub(
        r"\| Network \| Library, [^|]+\|",
        "| Network | Library, {NET_FEATURES} |",
        s,
    )
    s = re.sub(
        r"\| Network \| [^|]*work \*\*offline\*\* after install \|",
        "| Network | {NET_BODY} |",
        s,
    )
    s = re.sub(
        r"- \*\*Bundled library\*\* — [^\.]+\.",
        "- **Bundled library** — {LIB_DESC}.",
        s,
    )
    s = re.sub(
        r"- \*\*(Precept|Rhyme|Sage|Insight) cards\*\* —",
        r"- **{CARD_KIND} cards** —",
        s,
    )
    s = re.sub(
        r"- \*\*Ask [A-Za-z]+\*\* —",
        "- **Ask {ASK}** —",
        s,
    )
    s = re.sub(
        r"\| Optional Apple services \| \*\*iCloud\*\* \(your private KVS\), \*\*Photo Library \(Add Only\)\*\* for [^,]+,",
        "| Optional Apple services | **iCloud** (your private KVS), **Photo Library (Add Only)** for {PHOTO_FOR},",
        s,
    )
    s = re.sub(
        r"\| iCloud \| You enable sync \| Sync [^|]+\|",
        "| iCloud | You enable sync | Sync {SYNC_SCOPE} |",
        s,
    )
    s = re.sub(
        r"\| Notifications \| You enable [^|]+\| Local scheduling[^|]*\|",
        "| Notifications | You enable {NOTIF_FEATURE} | Local scheduling{NOTIF_SUFFIX} |",
        s,
    )
    s = re.sub(
        r"\| [^|]+ cache & notification prefs \| App Group UserDefaults \| Today['']s ID[^|]+\|",
        "| {DAILY_CACHE} cache & notification prefs | App Group UserDefaults | {DAILY_PREFS} |",
        s,
    )
    s = re.sub(
        r"\| Study progress & mastery \| App Group UserDefaults \| [^|]+ \|",
        "| Study progress & mastery | App Group UserDefaults | {STUDY_STATE} |",
        s,
    )
    s = re.sub(
        r"- \*\*No content upload\*\* — Your .+",
        "- **No content upload** — Your {UPLOAD_SCOPE}",
        s,
    )
    s = re.sub(
        r"- \*\*On-device speech\*\* — [^\.]+\.",
        "- **On-device speech** — {SPEECH_DESC}.",
        s,
    )
    s = s.replace("\0IHTC_STUDIO\0", "iHTC Studio")
    s = s.replace("\0ICLOUD_BOLD\0", "**iCloud**")
    s = s.replace("\0ICLOUD\0", "iCloud")
    s = s.replace("\0IOS\0", "iOS")
    s = s.replace("\0IPADOS\0", "iPadOS")
    return s


def extract_tokens(line: str) -> dict[str, str]:
    tokens: dict[str, str] = {}

    m = re.search(r"\*\*(i[A-Z][A-Za-z0-9]*)\*\*", line)
    if m:
        tokens["{APP}"] = m.group(1)

    m = re.search(r"`(group\.com\.iHTCboy\.\w+)`", line)
    if m:
        tokens["{GROUP}"] = m.group(1)

    m = re.search(r"`(com\.iHTCboy\.\w+\.\d+)`", line)
    if m:
        tokens["{TIPID}"] = m.group(1)
    else:
        m = re.search(r"`(com\.iHTCboy\.\w+)`", line)
        if m:
            tokens["{BUNDLE}"] = m.group(1)

    m = re.search(r'"([^"]*[\u4e00-\u9fff][^"]*)"', line)
    if m:
        tokens["{CNNAME}"] = m.group(1)
        tokens['"{CNNAME}"'] = f'"{m.group(1)}"'

    m = re.search(r"(?<![A-Za-z0-9])(i[A-Z][A-Za-z0-9]*)(?![A-Za-z0-9])", line)
    if m:
        tokens["{APPID}"] = m.group(1)

    han = re.findall(r"[\u4e00-\u9fff]+(?: / [\u4e00-\u9fff]+)?", line)
    if han:
        tokens["{HAN}"] = han[0]

    m = re.search(r"\| ([A-Za-z\u4e00-\u9fff /+–\-]+) database \|", line)
    if m:
        tokens["{DB}"] = m.group(1)

    m = re.search(
        r"recite, ([^,|]+), widgets, and daily notifications",
        line,
    )
    if m:
        tokens["{STUDY}"] = m.group(1).strip()
    else:
        m = re.search(
            r"recite, ([^,|]+), meditation, Life Guidance, widgets",
            line,
        )
        if m:
            tokens["{STUDY}"] = m.group(1).strip()

    m = re.search(r"\| Network \| Library, (.+?) \|", line)
    if m:
        tokens["{NET_FEATURES}"] = m.group(1).strip()

    m = re.search(r"\| Network \| (.+?) \|", line)
    if m and "offline" in m.group(1).lower():
        tokens["{NET_BODY}"] = m.group(1).strip()

    m = re.search(r"- \*\*Bundled library\*\* — (.+)\.", line)
    if m:
        tokens["{LIB_DESC}"] = m.group(1).strip()

    m = re.search(r"- \*\*(Precept|Rhyme|Sage|Insight|Dharma) cards", line)
    if m:
        tokens["{CARD_KIND}"] = m.group(1)

    m = re.search(r"- \*\*Ask ([A-Za-z]+)\*\* —", line)
    if m:
        tokens["{ASK}"] = m.group(1)

    m = re.search(
        r"\| Optional Apple services \| \*\*iCloud\*\* \(your private KVS\), \*\*Photo Library \(Add Only\)\*\* for ([^,]+),",
        line,
    )
    if m:
        tokens["{PHOTO_FOR}"] = m.group(1).strip()

    m = re.search(r"\| iCloud \| You enable sync \| Sync (.+) \|", line)
    if m:
        tokens["{SYNC_SCOPE}"] = m.group(1).strip()

    m = re.search(r"\| Notifications \| You enable (.+?) \| Local scheduling(.*?) \|", line)
    if m:
        tokens["{NOTIF_FEATURE}"] = m.group(1).strip()
        tokens["{NOTIF_SUFFIX}"] = m.group(2)

    m = re.search(
        r"\| ([^|]+) cache & notification prefs \| App Group UserDefaults \| (.+) \|",
        line,
    )
    if m and "Today" in m.group(2):
        tokens["{DAILY_CACHE}"] = m.group(1).strip()
        tokens["{DAILY_PREFS}"] = m.group(2).strip()

    m = re.search(
        r"\| Study progress & mastery \| App Group UserDefaults \| (.+) \|",
        line,
    )
    if m:
        tokens["{STUDY_STATE}"] = m.group(1).strip()

    m = re.search(r"- \*\*No content upload\*\* — Your (.+)", line)
    if m:
        tokens["{UPLOAD_SCOPE}"] = m.group(1).strip()

    m = re.search(r"- \*\*On-device speech\*\* — (.+)\.", line)
    if m:
        tokens["{SPEECH_DESC}"] = m.group(1).strip()

    return tokens


def apply_tokens(tmpl: str, tokens: dict[str, str]) -> str:
    out = tmpl
    for key in (
        "{APP}",
        "{APPID}",
        "{BUNDLE}",
        "{GROUP}",
        "{TIPID}",
        "{CNNAME}",
        '"{CNNAME}"',
        "{HAN}",
        "{DB}",
        "{STUDY}",
        "{NET_FEATURES}",
        "{NET_BODY}",
        "{LIB_DESC}",
        "{CARD_KIND}",
        "{ASK}",
        "{PHOTO_FOR}",
        "{SYNC_SCOPE}",
        "{NOTIF_FEATURE}",
        "{NOTIF_SUFFIX}",
        "{DAILY_CACHE}",
        "{DAILY_PREFS}",
        "{STUDY_STATE}",
        "{UPLOAD_SCOPE}",
        "{SPEECH_DESC}",
    ):
        if key in tokens:
            out = out.replace(key, tokens[key])
    return out


# Hand-maintained normalized templates (professional translations).
NORM_TEMPLATES: dict[str, dict[str, str]] = {
    '{APPID} requests permissions only when a feature needs them:': {
        "ja": "{APPID} は、機能が必要な場合にのみ権限を要求します。",
        "ko": "{APPID}은(는) 기능에 필요할 때에만 권한을 요청합니다.",
        "ru": "{APPID} запрашивает разрешения только тогда, когда они нужны функции:",
        "th": "{APPID} ขอสิทธิ์เฉพาะเมื่อฟีเจอร์ต้องการเท่านั้น:",
        "de": "{APPID} fordert Berechtigungen nur an, wenn eine Funktion sie benötigt:",
        "fr": "{APPID} ne demande des autorisations que lorsqu’une fonctionnalité en a besoin :",
        "tr": "{APPID}, yalnızca bir özellik gerektirdiğinde izin ister:",
    },
    '- **Widgets & App Group** — Widgets and the app share preferences and lightweight state via App Group `{GROUP}` on your device.': {
        "ja": "- **ウィジェットと App Group** — ウィジェットとアプリは、端末上の App Group `{GROUP}` を通じて設定と軽量な状態を共有します。",
        "ko": "- **위젯 및 App Group** — 위젯과 앱은 기기의 App Group `{GROUP}`을 통해 설정과 가벼운 상태를 공유합니다.",
        "ru": "- **Виджеты и App Group** — виджеты и приложение обмениваются настройками и лёгким состоянием через App Group `{GROUP}` на вашем устройстве.",
        "th": "- **วิดเจ็ตและ App Group** — วิดเจ็ตและแอปใช้การตั้งค่าและสถานะขนาดเล็กร่วมกันผ่าน App Group `{GROUP}` บนอุปกรณ์ของคุณ",
        "de": "- **Widgets und App Group** — Widgets und App teilen Einstellungen und leichten Zustand über die App Group `{GROUP}` auf Ihrem Gerät.",
        "fr": "- **Widgets et App Group** — Les widgets et l’app partagent des préférences et un état léger via l’App Group `{GROUP}` sur votre appareil.",
        "tr": "- **Widget'lar ve App Group** — Widget'lar ve uygulama, cihazınızdaki `{GROUP}` App Group'u üzerinden tercihleri ve hafif durumu paylaşır.",
    },
    '- **Widgets & App Group** — Widgets and the app share preferences via App Group `{GROUP}` on your device.': {
        "ja": "- **ウィジェットと App Group** — ウィジェットとアプリは、端末上の App Group `{GROUP}` を通じて設定を共有します。",
        "ko": "- **위젯 및 App Group** — 위젯과 앱은 기기의 App Group `{GROUP}`을 통해 설정을 공유합니다.",
        "ru": "- **Виджеты и App Group** — виджеты и приложение обмениваются настройками через App Group `{GROUP}` на вашем устройстве.",
        "th": "- **วิดเจ็ตและ App Group** — วิดเจ็ตและแอปแชร์การตั้งค่าผ่าน App Group `{GROUP}` บนอุปกรณ์ของคุณ",
        "de": "- **Widgets und App Group** — Widgets und App teilen Einstellungen über die App Group `{GROUP}` auf Ihrem Gerät.",
        "fr": "- **Widgets et App Group** — Les widgets et l’app partagent des préférences via l’App Group `{GROUP}` sur votre appareil.",
        "tr": "- **Widget'lar ve App Group** — Widget'lar ve uygulama, cihazınızdaki `{GROUP}` App Group'u üzerinden tercihleri paylaşır.",
    },
    '{APPID} is an educational literacy app for a general audience and is **not** in the Kids Category. We do not knowingly collect personal information from children. The app does not require an account. Families may use reading and study features offline on their own devices.': {
        "ja": "{APPID} は一般向けの教育・読書アプリであり、**Kids Category には属しません**。当社は児童から故意に個人情報を収集しません。アカウントは不要です。家族は各自の端末で、オフラインの読書・学習機能をご利用いただけます。",
        "ko": "{APPID}은(는) 일반 대중을 위한 교육용 독서 앱이며 **Kids Category에 해당하지 않습니다**. 당사는 아동으로부터 고의로 개인정보를 수집하지 않습니다. 계정이 필요하지 않습니다. 가족은 각자의 기기에서 오프라인으로 읽기·학습 기능을 사용할 수 있습니다.",
        "ru": "{APPID} — образовательное приложение для широкой аудитории и **не относится к Kids Category**. Мы сознательно не собираем персональные данные детей. Приложение не требует учётной записи. Семьи могут пользоваться чтением и обучением офлайн на своих устройствах.",
        "th": "{APPID} เป็นแอปการอ่านเชิงการศึกษาสำหรับผู้ใช้ทั่วไป และ**ไม่ได้**อยู่ใน Kids Category เราไม่เก็บข้อมูลส่วนบุคคลจากเด็กโดยเจตนา แอปไม่ต้องมีบัญชี ครอบครัวสามารถใช้การอ่านและการเรียนแบบออฟไลน์บนอุปกรณ์ของตนเอง",
        "de": "{APPID} ist eine Bildungs- und Lese-App für ein allgemeines Publikum und **nicht** in der Kids Category. Wir erheben wissentlich keine personenbezogenen Daten von Kindern. Die App erfordert kein Konto. Familien können Lese- und Lernfunktionen offline auf eigenen Geräten nutzen.",
        "fr": "{APPID} est une application éducative de lecture pour le grand public et **n’est pas** dans la Kids Category. Nous ne collectons pas sciemment d’informations personnelles auprès d’enfants. L’app ne nécessite pas de compte. Les familles peuvent utiliser lecture et étude hors ligne sur leurs propres appareils.",
        "tr": "{APPID}, genel kitleye yönelik bir eğitim/okuma uygulamasıdır ve **Kids Category**’de değildir. Çocuklardan bilerek kişisel bilgi toplamayız. Uygulama hesap gerektirmez. Aileler kendi cihazlarında okuma ve çalışma özelliklerini çevrimdışı kullanabilir.",
    },
    '| {DB} database | App / Widget bundle | Offline reading & study |': {
        "ja": "| {DB} データベース | App / Widget バンドル | オフライン閲読と学習 |",
        "ko": "| {DB} 데이터베이스 | App / Widget 번들 | 오프라인 읽기 및 학습 |",
        "ru": "| База {DB} | Пакет App / Widget | Офлайн-чтение и обучение |",
        "th": "| ฐานข้อมูล {DB} | App / Widget bundle | การอ่านและเรียนแบบออฟไลน์ |",
        "de": "| {DB}-Datenbank | App-/Widget-Bundle | Offline-Lesen und -Lernen |",
        "fr": "| Base {DB} | Bundle App / Widget | Lecture et étude hors ligne |",
        "tr": "| {DB} veritabanı | App / Widget paketi | Çevrimdışı okuma ve çalışma |",
    },
    '| Network | Library, reading, recite, {STUDY}, widgets, and daily notifications work **offline** after install |': {
        "ja": "| ネットワーク | ライブラリ、閲読、朗誦、{STUDY}、ウィジェット、毎日の通知は、インストール後 **オフライン** で動作します |",
        "ko": "| 네트워크 | 라이브러리, 읽기, 낭송, {STUDY}, 위젯, 일일 알림은 설치 후 **오프라인**으로 동작합니다 |",
        "ru": "| Сеть | Библиотека, чтение, декламация, {STUDY}, виджеты и ежедневные уведомления работают **офлайн** после установки |",
        "th": "| เครือข่าย | คลังข้อมูล การอ่าน การท่อง {STUDY} วิดเจ็ต และการแจ้งเตือนรายวันทำงาน **แบบออฟไลน์** หลังติดตั้ง |",
        "de": "| Netzwerk | Bibliothek, Lesen, Rezitation, {STUDY}, Widgets und tägliche Benachrichtigungen funktionieren nach der Installation **offline** |",
        "fr": "| Réseau | Bibliothèque, lecture, récitation, {STUDY}, widgets et notifications quotidiennes fonctionnent **hors ligne** après l’installation |",
        "tr": "| Ağ | Kütüphane, okuma, seslendirme, {STUDY}, widget’lar ve günlük bildirimler kurulumdan sonra **çevrimdışı** çalışır |",
    },
    'iHTC Studio ("we", "us" or "our") built **{APP}** (also known as "{CNNAME}", Bundle ID `{BUNDLE}`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on **this page** as the public privacy policy for the app. For App Store Connect, open this Privacy Policy in your browser and copy the address from the address bar (the public site domain may change over time).': {
        "ja": 'iHTC Studio（「当社」）は **{APP}**（「{CNNAME}」、Bundle ID `{BUNDLE}`）を開発しました。本プライバシーポリシーは、本アプリの利用時にどのデータが取り扱われ、取り扱われないかを説明します。**Apple App Review** とユーザーは、**本ページ**を公開のプライバシーポリシーとして参照できます。App Store Connect では、ブラウザで本プライバシーポリシーを開き、アドレスバーから URL をコピーしてください（公開サイトのドomainは将来変更される場合があります）。',
        "ko": 'iHTC Studio("당사")는 **{APP}**("{CNNAME}", Bundle ID `{BUNDLE}`)을(를) 개발했습니다. 본 개인정보 처리방침은 앱 사용 시 어떤 데이터가 처리되고 처리되지 않는지 설명합니다. **Apple App Review**와 사용자는 **이 페이지**를 공개 개인정보 처리방침으로 사용할 수 있습니다. App Store Connect에는 브라우저에서 본 개인정보 처리방침을 열고 주소창의 URL을 복사하세요(공개 사이트 도메인은 변경될 수 있습니다).',
        "ru": 'iHTC Studio («мы») создала **{APP}** («{CNNAME}», Bundle ID `{BUNDLE}`). Настоящая Политика конфиденциальности объясняет, какие данные обрабатываются (и не обрабатываются) при использовании приложения. **Apple App Review** и пользователи могут использовать **эту страницу** как публичную политику конфиденциальности. Для App Store Connect откройте эту страницу в браузере и скопируйте URL из адресной строки (домен публичного сайта может измениться).',
        "th": 'iHTC Studio ("เรา") พัฒนา **{APP}** ("{CNNAME}", Bundle ID `{BUNDLE}`) นโยบายความเป็นส่วนตัวนี้อธิบายว่าข้อมูลใดถูกจัดการและไม่ถูกจัดการเมื่อคุณใช้แอป **Apple App Review** และผู้ใช้สามารถใช้**หน้านี้**เป็นนโยบายความเป็นส่วนตัวสาธารณะ สำหรับ App Store Connect ให้เปิดนโยบายนี้ในเบราว์เซอร์แล้วคัดลอก URL จากแถบที่อยู่ (โดเมนสาธารณะอาจเปลี่ยนได้)',
        "de": 'iHTC Studio („wir“) hat **{APP}** („{CNNAME}“, Bundle-ID `{BUNDLE}`) entwickelt. Diese Datenschutzerklärung erläutert, welche Daten bei der Nutzung verarbeitet werden (und welche nicht). **Apple App Review** und Nutzer können sich auf **diese Seite** als öffentliche Datenschutzerklärung stützen. Für App Store Connect öffnen Sie diese Seite im Browser und kopieren Sie die URL aus der Adressleiste (die Domain kann sich ändern).',
        "fr": 'iHTC Studio (« nous ») a développé **{APP}** (« {CNNAME} », Bundle ID `{BUNDLE}`). Cette politique de confidentialité explique quelles données sont (ou ne sont pas) traitées lorsque vous utilisez l’app. **Apple App Review** et les utilisateurs peuvent s’appuyer sur **cette page** comme politique publique. Pour App Store Connect, ouvrez cette page dans le navigateur et copiez l’URL depuis la barre d’adresse (le domaine public peut changer).',
        "tr": 'iHTC Studio ("biz"), **{APP}** ("{CNNAME}", Bundle ID `{BUNDLE}`) uygulamasını geliştirdi. Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlendiğini (ve işlenmediğini) açıklar. **Apple App Review** ve kullanıcılar **bu sayfayı** herkese açık gizlilik politikası olarak kullanabilir. App Store Connect için tarayıcıda bu sayfayı açın ve adres çubuğundan URL’yi kopyalayın (genel site alan adı zamanla değişebilir).',
    },
    'iHTC Studio ("we", "us" or "our") built **{APP}** (also known as "{CNNAME}" / "{CNNAME}", Bundle ID `{BUNDLE}`). This Privacy Policy explains what data is (and is not) handled when you use the app. **Apple App Review** and users may rely on **this page** as the public privacy policy for the app. For App Store Connect, open this Privacy Policy in your browser and copy the address from the address bar (the public site domain may change over time).': {
        "ja": 'iHTC Studio（「当社」）は **{APP}**（「{CNNAME}」／「{CNNAME}」、Bundle ID `{BUNDLE}`）を開発しました。本プライバシーポリシーは、本アプリの利用時にどのデータが取り扱われ、取り扱われないかを説明します。**Apple App Review** とユーザーは、**本ページ**を公開のプライバシーポリシーとして参照できます。App Store Connect では、ブラウザで本プライバシーポリシーを開き、アドレスバーから URL をコピーしてください（公開サイトのドメインは将来変更される場合があります）。',
        "ko": 'iHTC Studio("당사")는 **{APP}**("{CNNAME}" / "{CNNAME}", Bundle ID `{BUNDLE}`)을(를) 개발했습니다. 본 개인정보 처리방침은 앱 사용 시 어떤 데이터가 처리되고 처리되지 않는지 설명합니다. **Apple App Review**와 사용자는 **이 페이지**를 공개 개인정보 처리방침으로 사용할 수 있습니다. App Store Connect에는 브라우저에서 본 개인정보 처리방침을 열고 주소창의 URL을 복사하세요(공개 사이트 도메인은 변경될 수 있습니다).',
        "ru": 'iHTC Studio («мы») создала **{APP}** («{CNNAME}» / «{CNNAME}», Bundle ID `{BUNDLE}`). Настоящая Политика конфиденциальности объясняет, какие данные обрабатываются (и не обрабатываются) при использовании приложения. **Apple App Review** и пользователи могут использовать **эту страницу** как публичную политику конфиденциальности. Для App Store Connect откройте эту страницу в браузере и скопируйте URL из адресной строки (домен публичного сайта может измениться).',
        "th": 'iHTC Studio ("เรา") พัฒนา **{APP}** ("{CNNAME}" / "{CNNAME}", Bundle ID `{BUNDLE}`) นโยบายความเป็นส่วนตัวนี้อธิบายว่าข้อมูลใดถูกจัดการและไม่ถูกจัดการเมื่อคุณใช้แอป **Apple App Review** และผู้ใช้สามารถใช้**หน้านี้**เป็นนโยบายความเป็นส่วนตัวสาธารณะ สำหรับ App Store Connect ให้เปิดนโยบายนี้ในเบราว์เซอร์แล้วคัดลอก URL จากแถบที่อยู่ (โดเมนสาธารณะอาจเปลี่ยนได้)',
        "de": 'iHTC Studio („wir“) hat **{APP}** („{CNNAME}“ / „{CNNAME}“, Bundle-ID `{BUNDLE}`) entwickelt. Diese Datenschutzerklärung erläutert, welche Daten bei der Nutzung verarbeitet werden (und welche nicht). **Apple App Review** und Nutzer können sich auf **diese Seite** als öffentliche Datenschutzerklärung stützen. Für App Store Connect öffnen Sie diese Seite im Browser und kopieren Sie die URL aus der Adressleiste (die Domain kann sich ändern).',
        "fr": 'iHTC Studio (« nous ») a développé **{APP}** (« {CNNAME} » / « {CNNAME} », Bundle ID `{BUNDLE}`). Cette politique de confidentialité explique quelles données sont (ou ne sont pas) traitées lorsque vous utilisez l’app. **Apple App Review** et les utilisateurs peuvent s’appuyer sur **cette page** comme politique publique. Pour App Store Connect, ouvrez cette page dans le navigateur et copiez l’URL depuis la barre d’adresse (le domaine public peut changer).',
        "tr": 'iHTC Studio ("biz"), **{APP}** ("{CNNAME}" / "{CNNAME}", Bundle ID `{BUNDLE}`) uygulamasını geliştirdi. Bu Gizlilik Politikası, uygulamayı kullandığınızda hangi verilerin işlendiğini (ve işlenmediğini) açıklar. **Apple App Review** ve kullanıcılar **bu sayfayı** herkese açık gizlilik politikası olarak kullanabilir. App Store Connect için tarayıcıda bu sayfayı açın ve adres çubuğundan URL’yi kopyalayın (genel site alan adı zamanla değişebilir).',
    },
    "| Network | Library, {NET_FEATURES} |": {
        "ja": "| ネットワーク | ライブラリ、{NET_FEATURES}は、インストール後 **オフライン** で動作します |",
        "ko": "| 네트워크 | 라이브러리, {NET_FEATURES}는 설치 후 **오프라인**으로 동작합니다 |",
        "ru": "| Сеть | Библиотека, {NET_FEATURES} работают **офлайн** после установки |",
        "th": "| เครือข่าย | คลังข้อมูล {NET_FEATURES} ทำงาน **แบบออฟไลน์** หลังติดตั้ง |",
        "de": "| Netzwerk | Bibliothek, {NET_FEATURES} funktionieren nach der Installation **offline** |",
        "fr": "| Réseau | Bibliothèque, {NET_FEATURES} fonctionnent **hors ligne** après l’installation |",
        "tr": "| Ağ | Kütüphane, {NET_FEATURES} kurulumdan sonra **çevrimdışı** çalışır |",
    },
    "| Network | {NET_BODY} |": {
        "ja": "| ネットワーク | {NET_BODY} |",
        "ko": "| 네트워크 | {NET_BODY} |",
        "ru": "| Сеть | {NET_BODY} |",
        "th": "| เครือข่าย | {NET_BODY} |",
        "de": "| Netzwerk | {NET_BODY} |",
        "fr": "| Réseau | {NET_BODY} |",
        "tr": "| Ağ | {NET_BODY} |",
    },
    "- **Bundled library** — {LIB_DESC}.": {
        "ja": "- **同梱ライブラリ** — {LIB_DESC}。閲覧と学習にネットワークは不要です。",
        "ko": "- **번들 라이브러리** — {LIB_DESC}. 탐색과 학습에 네트워크가 필요하지 않습니다.",
        "ru": "- **Встроенная библиотека** — {LIB_DESC}. Просмотр и обучение не требуют сети.",
        "th": "- **ไลบรารีในชุดแอป** — {LIB_DESC} การเรียกดูและการเรียนไม่ต้องใช้เครือข่าย",
        "de": "- **Mitgelieferte Bibliothek** — {LIB_DESC}. Durchsuchen und Lernen erfordern kein Netzwerk.",
        "fr": "- **Bibliothèque intégrée** — {LIB_DESC}. La consultation et l’étude ne nécessitent pas de réseau.",
        "tr": "- **Paketlenmiş kitaplık** — {LIB_DESC}. Gezinme ve çalışma ağ gerektirmez.",
    },
    "- **{CARD_KIND} cards** — Images are rendered on device. Saving uses **Photo Library add-only** only when you tap save. System Share Sheet may send the image to an app **you** choose; that destination’s privacy policy then applies.": {
        "ja": "- **{CARD_KIND}カード** — 画像は端末上で生成されます。保存は「保存」をタップしたときのみ **写真ライブラリ（追加のみ）** を使用します。共有シートは**お客様が選んだ**アプリに画像を送ることがあり、その場合は送信先のプライバシーポリシーが適用されます。",
        "ko": "- **{CARD_KIND} 카드** — 이미지는 기기에서 생성됩니다. 저장은 저장을 탭할 때만 **사진 보관함(추가 전용)** 을 사용합니다. 시스템 공유 시트는 **사용자가 선택한** 앱으로 이미지를 보낼 수 있으며, 해당 앱의 개인정보 처리방침이 적용됩니다.",
        "ru": "- **Карточки {CARD_KIND}** — изображения создаются на устройстве. Сохранение использует **Фототеку (только добавление)** лишь при нажатии «Сохранить». «Поделиться» может передать изображение приложению, **которое вы выберете**; тогда действует политика получателя.",
        "th": "- **การ์ด {CARD_KIND}** — สร้างภาพบนอุปกรณ์ การบันทึกใช้ **คลังรูปภาพ (เพิ่มอย่างเดียว)** เมื่อแตะบันทึกเท่านั้น ชีตแชร์อาจส่งภาพไปแอปที่**คุณเลือก** ซึ่งใช้นโยบายความเป็นส่วนตัวของปลายทาง",
        "de": "- **{CARD_KIND}-Karten** — Bilder werden auf dem Gerät erzeugt. Speichern nutzt **Fotomediathek (nur Hinzufügen)** nur beim Tippen auf Speichern. Das Teilen-Blatt kann das Bild an eine App senden, **die Sie wählen**; dann gilt deren Datenschutzerklärung.",
        "fr": "- **Cartes {CARD_KIND}** — Les images sont générées sur l’appareil. L’enregistrement utilise **Photothèque (ajout uniquement)** seulement lorsque vous touchez Enregistrer. Le partage peut envoyer l’image à une app **que vous choisissez** ; la politique de cette destination s’applique.",
        "tr": "- **{CARD_KIND} kartları** — Görseller cihazda oluşturulur. Kaydetme yalnızca kaydet’e dokunduğunuzda **Fotoğraf Kitaplığı (yalnızca ekleme)** kullanır. Paylaşım Sayfası görseli **sizin seçtiğiniz** bir uygulamaya gönderebilir; o hedefin gizlilik politikası geçerli olur.",
    },
    "- **Ask {ASK}** — On supported devices (iOS 26+ / macOS 26+ with Apple Intelligence), the optional guide uses Apple **on-device Foundation Models**. Passage context and your question stay on the device; we do **not** upload them to iHTC Studio. If the model is unavailable, the app falls back to bundled commentary.": {
        "ja": "- **Ask {ASK}** — 対応端末（Apple Intelligence 搭載の iOS 26+ / macOS 26+）では、任意のガイドが Apple **端末内 Foundation Models** を使用します。篇の文脈と質問は端末に留まり、iHTC Studio へ**アップロードしません**。モデルが利用できない場合は同梱解説にフォールバックします。",
        "ko": "- **Ask {ASK}** — 지원 기기(iOS 26+ / macOS 26+, Apple Intelligence)에서 선택 가이드는 Apple **기기 내 Foundation Models**를 사용합니다. 구절 맥락과 질문은 기기에 남으며 iHTC Studio로 **업로드하지 않습니다**. 모델을 사용할 수 없으면 번들 해설로 대체됩니다.",
        "ru": "- **Ask {ASK}** — на поддерживаемых устройствах (iOS 26+ / macOS 26+ с Apple Intelligence) необязательный помощник использует **Foundation Models на устройстве** Apple. Контекст фрагмента и ваш вопрос остаются на устройстве; мы **не** загружаем их в iHTC Studio. Если модель недоступна, приложение использует встроенные комментарии.",
        "th": "- **Ask {ASK}** — บนอุปกรณ์ที่รองรับ (iOS 26+ / macOS 26+ พร้อม Apple Intelligence) คู่มือเสริมใช้ **Foundation Models บนอุปกรณ์** ของ Apple บริบทข้อความและคำถามอยู่บนอุปกรณ์ เรา **ไม่** อัปโหลดไป iHTC Studio หากโมเดลไม่พร้อม แอปจะใช้คำอธิบายในชุดแอป",
        "de": "- **Ask {ASK}** — Auf unterstützten Geräten (iOS 26+ / macOS 26+ mit Apple Intelligence) nutzt der optionale Guide Apples **Foundation Models auf dem Gerät**. Passage-Kontext und Frage bleiben auf dem Gerät; wir laden sie **nicht** zu iHTC Studio hoch. Ist das Modell nicht verfügbar, greift die App auf mitgelieferte Kommentare zurück.",
        "fr": "- **Ask {ASK}** — Sur les appareils pris en charge (iOS 26+ / macOS 26+ avec Apple Intelligence), le guide optionnel utilise les **Foundation Models sur l’appareil** d’Apple. Le contexte du passage et votre question restent sur l’appareil ; nous ne les **envoyons pas** à iHTC Studio. Si le modèle est indisponible, l’app utilise les commentaires intégrés.",
        "tr": "- **Ask {ASK}** — Desteklenen cihazlarda (Apple Intelligence ile iOS 26+ / macOS 26+) isteğe bağlı rehber, Apple **cihaz içi Foundation Models** kullanır. Pasaj bağlamı ve sorunuz cihazda kalır; iHTC Studio’ya **yüklemez**. Model yoksa uygulama paketlenmiş yorumlara döner.",
    },
    "| iCloud | You enable sync | Sync {SYNC_SCOPE} |": {
        "ja": "| iCloud | 同期を有効にする | {SYNC_SCOPE} を同期 |",
        "ko": "| iCloud | 동기화 사용 | {SYNC_SCOPE} 동기화 |",
        "ru": "| iCloud | Вы включаете синхронизацию | Синхронизация: {SYNC_SCOPE} |",
        "th": "| iCloud | คุณเปิดซิงค์ | ซิงค์ {SYNC_SCOPE} |",
        "de": "| iCloud | Sie aktivieren Sync | {SYNC_SCOPE} synchronisieren |",
        "fr": "| iCloud | Vous activez la synchronisation | Synchroniser {SYNC_SCOPE} |",
        "tr": "| iCloud | Senkronizasyonu açarsınız | {SYNC_SCOPE} senkronize edilir |",
    },
    "| Notifications | You enable {NOTIF_FEATURE} | Local scheduling{NOTIF_SUFFIX} |": {
        "ja": "| 通知 | {NOTIF_FEATURE} を有効にする | ローカルスケジュール{NOTIF_SUFFIX} |",
        "ko": "| 알림 | {NOTIF_FEATURE} 사용 | 로컬 예약{NOTIF_SUFFIX} |",
        "ru": "| Уведомления | Вы включаете {NOTIF_FEATURE} | Локальное планирование{NOTIF_SUFFIX} |",
        "th": "| การแจ้งเตือน | คุณเปิด {NOTIF_FEATURE} | กำหนดเวลาในเครื่อง{NOTIF_SUFFIX} |",
        "de": "| Benachrichtigungen | Sie aktivieren {NOTIF_FEATURE} | Lokale Planung{NOTIF_SUFFIX} |",
        "fr": "| Notifications | Vous activez {NOTIF_FEATURE} | Planification locale{NOTIF_SUFFIX} |",
        "tr": "| Bildirimler | {NOTIF_FEATURE} etkinleştirirsiniz | Yerel zamanlama{NOTIF_SUFFIX} |",
    },
    "| {DAILY_CACHE} cache & notification prefs | App Group UserDefaults | {DAILY_PREFS} |": {
        "ja": "| {DAILY_CACHE} キャッシュと通知設定 | App Group UserDefaults | {DAILY_PREFS} |",
        "ko": "| {DAILY_CACHE} 캐시 및 알림 설정 | App Group UserDefaults | {DAILY_PREFS} |",
        "ru": "| Кэш {DAILY_CACHE} и настройки уведомлений | UserDefaults App Group | {DAILY_PREFS} |",
        "th": "| แคช {DAILY_CACHE} และการตั้งค่าการแจ้งเตือน | UserDefaults ของ App Group | {DAILY_PREFS} |",
        "de": "| {DAILY_CACHE}-Cache und Benachrichtigungseinstellungen | UserDefaults der App Group | {DAILY_PREFS} |",
        "fr": "| Cache {DAILY_CACHE} et prefs de notification | UserDefaults de l’App Group | {DAILY_PREFS} |",
        "tr": "| {DAILY_CACHE} önbelleği ve bildirim tercihleri | App Group UserDefaults | {DAILY_PREFS} |",
    },
    "| Study progress & mastery | App Group UserDefaults | {STUDY_STATE} |": {
        "ja": "| 学習進捗と習熟 | App Group UserDefaults | {STUDY_STATE} |",
        "ko": "| 학습 진행 및 숙달 | App Group UserDefaults | {STUDY_STATE} |",
        "ru": "| Прогресс и mastery | UserDefaults App Group | {STUDY_STATE} |",
        "th": "| ความคืบหน้าและความเชี่ยวชาญ | UserDefaults ของ App Group | {STUDY_STATE} |",
        "de": "| Lernfortschritt und Beherrschung | UserDefaults der App Group | {STUDY_STATE} |",
        "fr": "| Progression d’étude et maîtrise | UserDefaults de l’App Group | {STUDY_STATE} |",
        "tr": "| Çalışma ilerlemesi ve ustalık | App Group UserDefaults | {STUDY_STATE} |",
    },
    "- **No content upload** — Your {UPLOAD_SCOPE}": {
        "ja": "- **コンテンツのアップロードなし** — お客様の{UPLOAD_SCOPE}",
        "ko": "- **콘텐츠 업로드 없음** — 사용자의 {UPLOAD_SCOPE}",
        "ru": "- **Без загрузки контента** — Ваши {UPLOAD_SCOPE}",
        "th": "- **ไม่อัปโหลดเนื้อหา** — {UPLOAD_SCOPE} ของคุณ",
        "de": "- **Kein Hochladen von Inhalten** — Ihre {UPLOAD_SCOPE}",
        "fr": "- **Aucun envoi de contenu** — Vos {UPLOAD_SCOPE}",
        "tr": "- **İçerik yüklenmez** — {UPLOAD_SCOPE}",
    },
    "- **On-device speech** — {SPEECH_DESC}.": {
        "ja": "- **端末内音声** — {SPEECH_DESC}。iHTC Studio へテキストを送信しません。",
        "ko": "- **기기 내 음성** — {SPEECH_DESC}. iHTC Studio로 텍스트를 보내지 않습니다.",
        "ru": "- **Речь на устройстве** — {SPEECH_DESC}. Мы не отправляем текст в iHTC Studio.",
        "th": "- **เสียงบนอุปกรณ์** — {SPEECH_DESC} เราไม่ส่งข้อความไป iHTC Studio",
        "de": "- **Sprache auf dem Gerät** — {SPEECH_DESC}. Wir senden keinen Text an iHTC Studio.",
        "fr": "- **Synthèse vocale sur l’appareil** — {SPEECH_DESC}. Nous n’envoyons pas de texte à iHTC Studio.",
        "tr": "- **Cihaz içi konuşma** — {SPEECH_DESC}. Metni iHTC Studio’ya göndermiyoruz.",
    },
    '- **{HAN} cards** — Images are rendered on device. Saving uses **Photo Library add-only** only when you tap save. System Share Sheet may send the image to an app **you** choose; that destination’s privacy policy then applies.': {
        "ja": "- **{HAN}カード** — 画像は端末上で生成されます。保存は「保存」をタップしたときのみ **写真ライブラリ（追加のみ）** を使用します。共有シートは**お客様が選んだ**アプリに画像を送ることがあり、その場合は送信先のプライバシーポリシーが適用されます。",
        "ko": "- **{HAN} 카드** — 이미지는 기기에서 생성됩니다. 저장은 저장을 탭할 때만 **사진 보관함(추가 전용)** 을 사용합니다. 시스템 공유 시트는 **사용자가 선택한** 앱으로 이미지를 보낼 수 있으며, 해당 앱의 개인정보 처리방침이 적용됩니다.",
        "ru": "- **Карточки {HAN}** — изображения создаются на устройстве. Сохранение использует **Фототеку (только добавление)** лишь при нажатии «Сохранить». Меню «Поделиться» может передать изображение приложению, **которое вы выберете**; тогда действует политика конфиденциальности получателя.",
        "th": "- **การ์ด{HAN}** — รูปภาพสร้างบนอุปกรณ์ การบันทึกใช้ **คลังรูปภาพ (เพิ่มอย่างเดียว)** เฉพาะเมื่อแตะบันทึก ชีตแชร์ของระบบอาจส่งรูปไปยังแอปที่**คุณเลือก** ซึ่งจะใช้นโยบายความเป็นส่วนตัวของปลายทางนั้น",
        "de": "- **{HAN}-Karten** — Bilder werden auf dem Gerät erzeugt. Speichern nutzt **Fotomediathek (nur Hinzufügen)** nur beim Tippen auf Speichern. Das Share Sheet kann das Bild an eine App senden, **die Sie wählen**; dann gilt deren Datenschutzerklärung.",
        "fr": "- **Cartes {HAN}** — Les images sont générées sur l’appareil. L’enregistrement utilise **Photothèque (ajout uniquement)** seulement lorsque vous touchez Enregistrer. La feuille de partage peut envoyer l’image à une app **que vous choisissez** ; la politique de confidentialité de cette destination s’applique alors.",
        "tr": "- **{HAN} kartları** — Görseller cihazda oluşturulur. Kaydetme yalnızca kaydet’e dokunduğunuzda **Fotoğraf Kitaplığı (yalnızca ekleme)** kullanır. Paylaşım Sayfası görseli **sizin seçtiğiniz** bir uygulamaya gönderebilir; o hedefin gizlilik politikası geçerli olur.",
    },
    '| Favorites & lists ({HAN}) | App Group UserDefaults | Starred passages and user lists |': {
        "ja": "| お気に入りとリスト（{HAN}） | App Group UserDefaults | 星付きの篇目とユーザーリスト |",
        "ko": "| 즐겨찾기 및 목록({HAN}) | App Group UserDefaults | 별표 표시한 구절과 사용자 목록 |",
        "ru": "| Избранное и списки ({HAN}) | UserDefaults App Group | Отмеченные фрагменты и пользовательские списки |",
        "th": "| รายการโปรดและรายการ ({HAN}) | UserDefaults ของ App Group | ข้อความที่ติดดาวและรายการผู้ใช้ |",
        "de": "| Favoriten und Listen ({HAN}) | UserDefaults der App Group | Markierte Abschnitte und Nutzerlisten |",
        "fr": "| Favoris et listes ({HAN}) | UserDefaults de l’App Group | Passages favoris et listes utilisateur |",
        "tr": "| Favoriler ve listeler ({HAN}) | App Group UserDefaults | Yıldızlı pasajlar ve kullanıcı listeleri |",
    },
    '| Favorites & lists ({HAN} lists) | App Group UserDefaults | Starred passages and user lists |': {
        "ja": "| お気に入りとリスト（{HAN} lists） | App Group UserDefaults | 星付きの篇目とユーザーリスト |",
        "ko": "| 즐겨찾기 및 목록({HAN} lists) | App Group UserDefaults | 별표 표시한 구절과 사용자 목록 |",
        "ru": "| Избранное и списки ({HAN} lists) | UserDefaults App Group | Отмеченные фрагменты и пользовательские списки |",
        "th": "| รายการโปรดและรายการ ({HAN} lists) | UserDefaults ของ App Group | ข้อความที่ติดดาวและรายการผู้ใช้ |",
        "de": "| Favoriten und Listen ({HAN} lists) | UserDefaults der App Group | Markierte Abschnitte und Nutzerlisten |",
        "fr": "| Favoris et listes ({HAN} lists) | UserDefaults de l’App Group | Passages favoris et listes utilisateur |",
        "tr": "| Favoriler ve listeler ({HAN} lists) | App Group UserDefaults | Yıldızlı pasajlar ve kullanıcı listeleri |",
    },
    '- Lists ({HAN})': {
        "ja": "- リスト（{HAN}）",
        "ko": "- 목록({HAN})",
        "ru": "- Списки ({HAN})",
        "th": "- รายการ ({HAN})",
        "de": "- Listen ({HAN})",
        "fr": "- Listes ({HAN})",
        "tr": "- Listeler ({HAN})",
    },
    '- Lists ({HAN} lists)': {
        "ja": "- リスト（{HAN} lists）",
        "ko": "- 목록({HAN} lists)",
        "ru": "- Списки ({HAN} lists)",
        "th": "- รายการ ({HAN} lists)",
        "de": "- Listen ({HAN} lists)",
        "fr": "- Listes ({HAN} lists)",
        "tr": "- Listeler ({HAN} lists)",
    },
    "## How the app works": {
        "ja": "## アプリの仕組み",
        "ko": "## 앱 작동 방식",
        "ru": "## Как работает приложение",
        "th": "## วิธีการทำงานของแอป",
        "de": "## So funktioniert die App",
        "fr": "## Fonctionnement de l’app",
        "tr": "## Uygulama Nasıl Çalışır",
    },
    "## Stored locally": {
        "ja": "## 端末内の保存",
        "ko": "## 기기에 저장됨",
        "ru": "## Хранится локально",
        "th": "## เก็บในเครื่อง",
        "de": "## Lokal gespeichert",
        "fr": "## Stocké localement",
        "tr": "## Cihazda saklanır",
    },
    "## What stays on your device": {
        "ja": "## 端末に残るデータ",
        "ko": "## 기기에 남는 데이터",
        "ru": "## Что остаётся на устройстве",
        "th": "## สิ่งที่อยู่บนอุปกรณ์ของคุณ",
        "de": "## Was auf Ihrem Gerät bleibt",
        "fr": "## Ce qui reste sur votre appareil",
        "tr": "## Cihazınızda kalan veriler",
    },
    "## Medical disclaimer": {
        "ja": "## 医療に関する免責事項",
        "ko": "## 의료 면책 조항",
        "ru": "## Медицинский отказ от ответственности",
        "th": "## ข้อจำกัดความรับผิดชอบทางการแพทย์",
        "de": "## Medizinischer Haftungsausschluss",
        "fr": "## Avertissement médical",
        "tr": "## Tıbbi sorumluluk reddi",
    },
    "- **iCloud** — Turn off sync and clear related keys from your iCloud account / devices as needed; we cannot erase your iCloud for you.": {
        "ja": "- **iCloud** — 同期をオフにし、必要に応じて iCloud アカウント／端末から関連キーを削除してください。当社がお客様の iCloud を代わりに消去することはできません。",
        "ko": "- **iCloud** — 동기화를 끄고 필요 시 iCloud 계정/기기에서 관련 키를 삭제하세요. iCloud를 대신 지울 수 없습니다.",
        "ru": "- **iCloud** — Отключите синхронизацию и при необходимости удалите связанные ключи из учётной записи iCloud / устройств; мы не можем стереть ваш iCloud за вас.",
        "th": "- **iCloud** — ปิดการซิงค์และลบคีย์ที่เกี่ยวข้องจากบัญชี iCloud / อุปกรณ์ตามต้องการ เราไม่สามารถลบ iCloud ของคุณแทนคุณได้",
        "de": "- **iCloud** — Deaktivieren Sie die Synchronisierung und löschen Sie bei Bedarf zugehörige Schlüssel aus Ihrem iCloud-Konto / Ihren Geräten; wir können Ihr iCloud nicht für Sie löschen.",
        "fr": "- **iCloud** — Désactivez la synchronisation et effacez les clés associées de votre compte iCloud / appareils si nécessaire ; nous ne pouvons pas effacer votre iCloud à votre place.",
        "tr": "- **iCloud** — Senkronizasyonu kapatın ve gerektiğinde iCloud hesabınızdan / cihazlarınızdan ilgili anahtarları temizleyin; iCloud’unuzu sizin adınıza silemeyiz.",
    },
    'We may update this Privacy Policy. The “Last updated” date at the top will change. Continued use after an update means you accept the revised policy. Material changes may also be noted in the App Store “What’s New” text when appropriate.': {
        "ja": "本プライバシーポリシーは更新される場合があります。上部の「最終更新日」が変更されます。更新後も利用を続ける場合、改訂版に同意したものとみなされます。重要な変更は、適宜 App Store の「新機能」にも記載されることがあります。",
        "ko": "본 개인정보 처리방침은 업데이트될 수 있습니다. 상단의 「최종 업데이트」 날짜가 변경됩니다. 업데이트 후 계속 사용하면 개정된 정책에 동의하는 것입니다. 중요한 변경은 App Store 「새로운 기능」에도 적절히 안내될 수 있습니다.",
        "ru": "Мы можем обновлять эту Политику конфиденциальности. Дата «Последнего обновления» вверху изменится. Продолжение использования после обновления означает принятие пересмотренной политики. Существенные изменения также могут быть указаны в разделе App Store «Что нового», когда это уместно.",
        "th": "เราอาจปรับปรุงนโยบายความเป็นส่วนตัวนี้ วันที่ 「อัปเดตล่าสุด」 ด้านบนจะเปลี่ยน การใช้งานต่อหลังอัปเดตถือว่าคุณยอมรับนโยบายที่แก้ไข การเปลี่ยนแปลงสำคัญอาจระบุในข้อความ App Store 「มีอะไรใหม่」 เมื่อเหมาะสม",
        "de": "Wir können diese Datenschutzerklärung aktualisieren. Das Datum „Zuletzt aktualisiert“ oben ändert sich. Fortgesetzte Nutzung nach einer Aktualisierung gilt als Zustimmung zur überarbeiteten Richtlinie. Wesentliche Änderungen können gegebenenfalls auch im App Store unter „Was ist neu“ vermerkt werden.",
        "fr": "Nous pouvons mettre à jour cette politique de confidentialité. La date « Dernière mise à jour » en haut changera. L’utilisation continue après une mise à jour vaut acceptation de la politique révisée. Les changements importants peuvent aussi figurer dans « Nouveautés » de l’App Store le cas échéant.",
        "tr": "Bu Gizlilik Politikasını güncelleyebiliriz. Üstteki 「Son güncelleme」 tarihi değişir. Güncellemeden sonra kullanıma devam etmek, revize edilmiş politikayı kabul ettiğiniz anlamına gelir. Önemli değişiklikler uygun olduğunda App Store 「Yenilikler」 metninde de belirtilebilir.",
    },
}

# Full short-app overrides (hand translated).
CUSTOM: dict[str, dict[str, str]] = {}


def load_custom_short() -> None:
    """Populate CUSTOM for iSiShu, iWuJing, iZen from hand translations."""
    # iSiShu — see render output; filled below in main after reading EN
    pass


def translate_line(line: str, lang: str, exact: dict[str, dict[str, str]]) -> str:
    if line in exact and lang in exact[line]:
        return exact[line][lang]

    norm = normalize(line)
    if norm in NORM_TEMPLATES and lang in NORM_TEMPLATES[norm]:
        return apply_tokens(NORM_TEMPLATES[norm][lang], extract_tokens(line))

    # Last resort: keep line (should be rare); caller logs
    return line


def render_app(app: str, exact: dict[str, dict[str, str]]) -> dict[str, list[str]]:
    en = extract_en(app)
    if app in CUSTOM:
        return {loc: CUSTOM[app][loc].strip().splitlines() for loc in LOCALES if loc in CUSTOM[app]}

    out: dict[str, list[str]] = {loc: [] for loc in LOCALES}
    missing: dict[str, int] = {loc: 0 for loc in LOCALES}
    for line in en.splitlines():
        for loc in LOCALES:
            tr = translate_line(line, loc, exact)
            if tr == line and line.strip() and re.search(r"[A-Za-z]{4,}", line):
                missing[loc] += 1
            out[loc].append(tr)
    if any(missing.values()):
        print(f"  {app} untranslated lines:", missing)
    return out


def main() -> None:
    exact = build_exact_map()
    written = 0
    for app in APPS:
        print("render", app)
        by_lang = render_app(app, exact)
        key = Path(app) / "privacy"
        out_dir = SEC_ROOT / key
        out_dir.mkdir(parents=True, exist_ok=True)
        for loc in LOCALES:
            body = "\n".join(by_lang[loc]).strip() + "\n"
            (out_dir / f"{loc}.md").write_text(body, encoding="utf-8")
            written += 1
    print("render_hand_privacy_22: wrote", written, "files")


if __name__ == "__main__":
    main()
