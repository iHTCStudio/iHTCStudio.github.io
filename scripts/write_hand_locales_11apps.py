#!/usr/bin/env python3
"""Write hand-maintained _locale_sections bodies for 11 classic apps (faq + privacy)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC = ROOT / "_locale_sections"
LANGS = ("ja", "ko", "ru", "th", "de", "fr", "tr")
APPS = (
    "iBaiJia",
    "iGuanZhi",
    "iGuige",
    "iHanFei",
    "iLiezi",
    "iLvShi",
    "iMencius",
    "iMoZi",
    "iPrimer",
    "iRhyme",
    "iSage",
)


def w(app: str, doc: str, lang: str, body: str) -> None:
    p = SEC / app / doc / f"{lang}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body.strip() + "\n", encoding="utf-8")


def faq_footer(lang: str, store_line: str) -> str:
    foot = {
        "ja": (
            "### データを収集していますか？\n\n"
            "**いいえ。** [プライバシーポリシー](../privacy)をご覧ください。"
            "iHTC Studio はデータを収集せず、広告・分析 SDK もなく、アカウントも不要です。\n\n"
            "### App Store Connect 用のプライバシーポリシー URL はどこですか？\n\n"
            "本サイトの[プライバシーポリシー](../privacy)ページを開き、"
            "ブラウザのアドレスバーから URL をコピーしてください。\n\n"
            f"### App Store に掲載されていますか？\n\n{store_line}\n\n"
            "### システム要件は？\n\n"
            "iPhone / iPad **iOS 17.0+**、Mac **macOS 14.0+**。\n\n"
            "### サポートへの連絡方法は？\n\n"
            "[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 通常 48 時間以内に返信します。"
        ),
        "ko": (
            "### 내 데이터를 수집하나요?\n\n"
            "**아니요.** [개인정보 처리방침](../privacy)을 참고하세요. "
            "iHTC Studio는 데이터를 수집하지 않으며, 광고·분석 SDK가 없고 계정도 필요하지 않습니다.\n\n"
            "### App Store Connect용 개인정보 처리방침 URL은 어디에 있나요?\n\n"
            "이 사이트의 [개인정보 처리방침](../privacy) 페이지를 열고 "
            "브라우저 주소창에서 URL을 복사하세요.\n\n"
            f"### App Store에 있나요?\n\n{store_line}\n\n"
            "### 시스템 요구 사항은?\n\n"
            "iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+**.\n\n"
            "### 지원팀에 어떻게 문의하나요?\n\n"
            "[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 보통 48시간 이내에 답변합니다."
        ),
        "ru": (
            "### Вы собираете мои данные?\n\n"
            "**Нет.** См. [Политику конфиденциальности](../privacy): "
            "данные не собираются iHTC Studio; нет рекламных/аналитических SDK; аккаунт не нужен.\n\n"
            "### Где URL политики конфиденциальности для App Store Connect?\n\n"
            "Откройте на этом сайте страницу [Политика конфиденциальности](../privacy) "
            "и скопируйте URL из адресной строки браузера.\n\n"
            f"### Приложение уже в App Store?\n\n{store_line}\n\n"
            "### Системные требования?\n\n"
            "iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+**.\n\n"
            "### Как связаться с поддержкой?\n\n"
            "[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — обычно в течение 48 часов."
        ),
        "th": (
            "### คุณเก็บข้อมูลของฉันหรือไม่?\n\n"
            "**ไม่** ดู [นโยบายความเป็นส่วนตัว](../privacy): "
            "iHTC Studio ไม่เก็บข้อมูล ไม่มี SDK โฆษณา/วิเคราะห์ และไม่ต้องมีบัญชี\n\n"
            "### URL นโยบายความเป็นส่วนตัวสำหรับ App Store Connect อยู่ที่ไหน?\n\n"
            "เปิดหน้า [นโยบายความเป็นส่วนตัว](../privacy) ของไซต์นี้ "
            "แล้วคัดลอก URL จากแถบที่อยู่ของเบราว์เซอร์\n\n"
            f"### มีใน App Store แล้วหรือยัง?\n\n{store_line}\n\n"
            "### ความต้องการของระบบ?\n\n"
            "iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+**.\n\n"
            "### ติดต่อฝ่ายสนับสนุนได้อย่างไร?\n\n"
            "[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — โดยปกติภายใน 48 ชั่วโมง"
        ),
        "de": (
            "### Sammeln Sie meine Daten?\n\n"
            "**Nein.** Siehe [Datenschutzerklärung](../privacy): "
            "Daten werden von iHTC Studio nicht erhoben; keine Anzeigen-/Analyse-SDKs; kein Konto.\n\n"
            "### Wo ist die Datenschutz-URL für App Store Connect?\n\n"
            "Öffnen Sie auf dieser Website die Seite [Datenschutzerklärung](../privacy) "
            "und kopieren Sie die URL aus der Adressleiste.\n\n"
            f"### Ist die App schon im App Store?\n\n{store_line}\n\n"
            "### Systemanforderungen?\n\n"
            "iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+**.\n\n"
            "### Wie kontaktiere ich den Support?\n\n"
            "[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — in der Regel innerhalb von 48 Stunden."
        ),
        "fr": (
            "### Collectez-vous mes données ?\n\n"
            "**Non.** Voir la [Politique de confidentialité](../privacy) : "
            "données non collectées par iHTC Studio ; pas de SDK publicitaire/analytique ; pas de compte.\n\n"
            "### Où est l’URL de la politique de confidentialité pour App Store Connect ?\n\n"
            "Ouvrez la page [Politique de confidentialité](../privacy) de ce site "
            "et copiez l’URL depuis la barre d’adresse du navigateur.\n\n"
            f"### L’app est-elle déjà sur l’App Store ?\n\n{store_line}\n\n"
            "### Configuration requise ?\n\n"
            "iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+**.\n\n"
            "### Comment contacter l’assistance ?\n\n"
            "[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — en général sous 48 heures."
        ),
        "tr": (
            "### Verilerimi topluyor musunuz?\n\n"
            "**Hayır.** [Gizlilik Politikası](../privacy) bölümüne bakın: "
            "iHTC Studio tarafından veri toplanmaz; reklam/analiz SDK’sı yok; hesap gerekmez.\n\n"
            "### App Store Connect gizlilik politikası URL’si nerede?\n\n"
            "Bu sitenin [Gizlilik Politikası](../privacy) sayfasını açın "
            "ve URL’yi tarayıcı adres çubuğundan kopyalayın.\n\n"
            f"### App Store’da mı?\n\n{store_line}\n\n"
            "### Sistem gereksinimleri?\n\n"
            "iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+**.\n\n"
            "### Destek ile nasıl iletişime geçerim?\n\n"
            "[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — genellikle 48 saat içinde."
        ),
    }
    return foot[lang]


def store_yes(lang: str, url: str, extra: str = "") -> str:
    lines = {
        "ja": f"はい — [App Store でダウンロード]({url}).{extra}",
        "ko": f"예 — [App Store에서 다운로드]({url}).{extra}",
        "ru": f"Да — [Загрузить в App Store]({url}).{extra}",
        "th": f"ใช่ — [ดาวน์โหลดบน App Store]({url}){extra}",
        "de": f"Ja — [Im App Store laden]({url}).{extra}",
        "fr": f"Oui — [Télécharger sur l’App Store]({url}).{extra}",
        "tr": f"Evet — [App Store’dan indir]({url}).{extra}",
    }
    return lines[lang]


def store_prep(lang: str, url: str) -> str:
    lines = {
        "ja": (
            f"現在ストア掲載を準備中です。このサポートページをブックマークしてください。"
            f"Apple が公開すると [App Store のリンク]({url}) が開きます。"
        ),
        "ko": (
            f"현재 스토어 등록을 준비 중입니다. 이 지원 페이지를 북마크해 두세요. "
            f"Apple이 공개하면 [App Store 링크]({url})가 열립니다."
        ),
        "ru": (
            f"Мы готовим публикацию в магазине. Добавьте эту страницу поддержки в закладки; "
            f"после публикации Apple откроется [ссылка App Store]({url})."
        ),
        "th": (
            f"กำลังเตรียมขึ้น App Store โปรดบันทึกหน้าสนับสนุนนี้ "
            f"ลิงก์ [App Store]({url}) จะใช้งานได้เมื่อ Apple เผยแพร่แอป"
        ),
        "de": (
            f"Die Store-Veröffentlichung wird vorbereitet. Bookmarken Sie diese Support-Seite; "
            f"der [App Store-Link]({url}) funktioniert, sobald Apple die App veröffentlicht."
        ),
        "fr": (
            f"La fiche App Store est en préparation. Ajoutez cette page d’assistance à vos favoris ; "
            f"le [lien App Store]({url}) s’ouvrira une fois l’app publiée par Apple."
        ),
        "tr": (
            f"Mağaza listesi hazırlanıyor. Bu destek sayfasını yer imlerine ekleyin; "
            f"Apple yayımladığında [App Store bağlantısı]({url}) açılacaktır."
        ),
    }
    return lines[lang]


# --- FAQ bodies loaded from companion module ---
from hand_locale_faq_bodies import FAQ_BODIES  # noqa: E402
from hand_locale_privacy_bodies import PRIVACY_BODIES  # noqa: E402


def main() -> None:
    n = 0
    for app in APPS:
        for doc, bodies in (("faq", FAQ_BODIES.get(app, {})), ("privacy", PRIVACY_BODIES.get(app, {}))):
            for lang in LANGS:
                body = bodies.get(lang)
                if body:
                    w(app, doc, lang, body)
                    n += 1
    print("write_hand_locales_11apps: wrote", n, "files")


if __name__ == "__main__":
    main()
