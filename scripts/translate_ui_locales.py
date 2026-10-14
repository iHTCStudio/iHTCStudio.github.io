#!/usr/bin/env python3
"""Generate _data/i18n/{locale}.yml from en.yml (optional machine translation).

Prefer hand-maintained locale files when APIs rate-limit. Use --provider memory only for batch runs.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
I18N_DIR = ROOT / "_data" / "i18n"
SOURCE = I18N_DIR / "en.yml"
CACHE_PATH = ROOT / "scripts" / ".locale_translate_cache.json"
TARGETS = ["ja", "ko", "ru", "th", "de", "fr", "tr"]

MYMEMORY_PAIR: dict[str, tuple[str, str]] = {
    "ja": ("english", "japanese"),
    "ko": ("english", "korean"),
    "ru": ("english", "russian"),
    "th": ("english", "thai"),
    "de": ("english", "german"),
    "fr": ("english", "french"),
    "tr": ("english", "turkish"),
}

LANGUAGE_SET: dict[str, str] = {
    "ja": "言語を日本語に設定しました。",
    "ko": "언어가 한국어로 설정되었습니다.",
    "ru": "Язык интерфейса: русский.",
    "th": "ตั้งภาษาเป็นไทยแล้ว",
    "de": "Sprache auf Deutsch gestellt.",
    "fr": "Langue définie sur le français.",
    "tr": "Dil Türkçe olarak ayarlandı.",
}

GLOSSARY: list[tuple[str, str]] = [
    ("iHTC Studio", "___IHTC_STUDIO___"),
    ("iPhone", "___IPHONE___"),
    ("iPad", "___IPAD___"),
    ("Mac", "___MAC___"),
    ("iOS", "___IOS___"),
    ("iPadOS", "___IPADOS___"),
    ("macOS", "___MACOS___"),
    ("SwiftUI", "___SWIFTUI___"),
    ("App Store", "___APP_STORE___"),
    ("App Store Connect", "___APP_STORE_CONNECT___"),
    ("TestFlight", "___TESTFLIGHT___"),
    ("GitHub", "___GITHUB___"),
    ("Wi-Fi", "___WIFI___"),
    ("iCloud", "___ICLOUD___"),
    ("Keychain", "___KEYCHAIN___"),
    ("Apple", "___APPLE___"),
    ("URL Scheme", "___URL_SCHEME___"),
    ("Data Not Collected", "___DATA_NOT_COLLECTED___"),
    ("%current% / %total%", "___SHOT_COUNTER___"),
]


def protect(text: str) -> str:
    for original, token in GLOSSARY:
        text = text.replace(original, token)
    return text


def restore(text: str) -> str:
    for original, token in GLOSSARY:
        text = text.replace(token, original)
    return text


def load_cache() -> dict[str, str]:
    if not CACHE_PATH.exists():
        return {}
    return json.loads(CACHE_PATH.read_text(encoding="utf-8"))


def save_cache(cache: dict[str, str]) -> None:
    CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=0), encoding="utf-8")


def cache_key(dest: str, text: str) -> str:
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]
    return f"{dest}:{digest}"


_PROVIDER = "google-then-memory"


def _translate_chunk(protected: str, dest: str, cache: dict[str, str]) -> str:
    from deep_translator.exceptions import TooManyRequests
    from deep_translator import GoogleTranslator, MyMemoryTranslator

    ck = cache_key(dest, protected)
    if ck in cache:
        return cache[ck]

    last_err: Exception | None = None
    if _PROVIDER in ("google", "google-then-memory"):
        for attempt in range(8):
            try:
                time.sleep(1.4 + attempt * 0.75)
                result = GoogleTranslator(source="en", target=dest).translate(protected)
                cache[ck] = result
                return result
            except TooManyRequests as e:
                last_err = e
                time.sleep(4.0 * (attempt + 1))
            except Exception as e:  # noqa: BLE001
                last_err = e
                time.sleep(2.0 * (attempt + 1))

    pair = MYMEMORY_PAIR.get(dest)
    if pair and _PROVIDER in ("memory", "google-then-memory"):
        if len(protected) > 450:
            pieces: list[str] = []
            buf = ""
            for word in protected.split(" "):
                next_buf = f"{buf} {word}".strip() if buf else word
                if len(next_buf) > 450:
                    if buf:
                        pieces.append(buf)
                    buf = word
                else:
                    buf = next_buf
            if buf:
                pieces.append(buf)
            result = " ".join(_translate_chunk(p, dest, cache) for p in pieces)
            cache[ck] = result
            return result
        for attempt in range(5):
            try:
                time.sleep(1.2 + attempt * 0.8)
                result = MyMemoryTranslator(source=pair[0], target=pair[1]).translate(protected)
                cache[ck] = result
                return result
            except Exception as e:  # noqa: BLE001
                last_err = e
                time.sleep(2.0 * (attempt + 1))

    raise RuntimeError(f"translate failed for {dest}: {last_err}")


def translate_text(text: str, dest: str, cache: dict[str, str]) -> str:
    if not text or not str(text).strip():
        return text
    if dest == "en":
        return text
    protected = protect(str(text))
    if len(protected) <= 4500:
        return restore(_translate_chunk(protected, dest, cache))

    parts: list[str] = []
    chunk = ""
    for line in protected.split("\n"):
        if len(chunk) + len(line) + 1 > 4000:
            parts.append(chunk)
            chunk = line + "\n"
        else:
            chunk += line + "\n"
    if chunk:
        parts.append(chunk)
    translated = [_translate_chunk(part, dest, cache) for part in parts]
    return restore("\n".join(translated))


def walk_translate(obj, dest: str, cache: dict[str, str]):
    if isinstance(obj, str):
        return translate_text(obj, dest, cache)
    if isinstance(obj, list):
        return [walk_translate(x, dest, cache) for x in obj]
    if isinstance(obj, dict):
        return {k: walk_translate(v, dest, cache) for k, v in obj.items()}
    return obj


def build_locale(code: str, cache: dict[str, str]) -> None:
    en_data = yaml.safe_load(SOURCE.read_text(encoding="utf-8"))
    out_path = I18N_DIR / f"{code}.yml"
    print(f"Translating UI → {code} …", flush=True)
    data = copy.deepcopy(en_data)
    data = walk_translate(data, code, cache)
    names = en_data.get("language_names", {})
    if isinstance(data.get("language_names"), dict):
        data["language_names"].update(names)
    data["notice"]["language_set"] = LANGUAGE_SET.get(code, f"Language: {code}")
    save_cache(cache)
    out_path.write_text(
        yaml.dump(data, allow_unicode=True, sort_keys=False, width=120),
        encoding="utf-8",
    )
    print(f"  wrote {out_path.relative_to(ROOT)}", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--locale",
        action="append",
        choices=TARGETS,
        help="Translate one or more locales (default: all missing files).",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing locale files.")
    parser.add_argument(
        "--provider",
        choices=("google", "memory", "google-then-memory"),
        default="google-then-memory",
    )
    args = parser.parse_args()
    global _PROVIDER  # noqa: PLW0603
    _PROVIDER = args.provider

    cache = load_cache()
    todo = args.locale or TARGETS
    for code in todo:
        out_path = I18N_DIR / f"{code}.yml"
        if out_path.exists() and not args.force:
            print(f"skip {code} (exists)", flush=True)
            continue
        build_locale(code, cache)
    save_cache(cache)


if __name__ == "__main__":
    main()
