**더 빠르게 출시하세요. 브라우저 미로에서 벗어나세요.**

iAppManager(爱应用者)는 iPhone, iPad, Mac용 **네이티브 App Store Connect 워크스테이션**입니다. **API Key**로 로그인하고 자격 증명은 **Keychain**에 보관하며 Apple과 **직접** 통신합니다 — 버전, 스크린샷, IAP, TestFlight, 인증서, 판매 보고서, 고객 리뷰를 한곳에서.**iHTC Studio 계정 없음. 광고 없음. analytics SDK 없음. ASC 데이터용 제3자 backend 없음.**

**한눈에:** 다중 계정 API Key · 플랫폼/파이프라인 filt 앱 목록 · Overview 준비 체크리스트 · 버전 및 리뷰 제출 · Build Upload REST(IPA/PKG) · cross-locale 메타데이터/미디어 · Custom Product Pages · In-App Events · App Clips · 스토어 실험 · featuring · 가용성/가격 · 연령 · 접근성 · App Tags · IAP/구독 · Game Center · TestFlight · 리뷰 · 인증서/기기 · 사용자/역할 · sales/finance/Analytics · Webhooks · 위젯 및 `iappmanager://` · EN/简体/繁體

> 매주 App Store Connect에 사는 인디 개발자와 소규모 팀 — 탭 농장이 아닌 Mac 앱 같은 책상.

## 시작하기

1. **App Store Connect API Key** 생성(Admin/App Manager 권장) → `.p8` **한 번** 다운로드, **Issuer ID** + **Key ID**
2. iAppManager → 붙여넣기 → 검증(`GET /v1/apps`). **Keychain** 저장
3. **온보딩** 완료. **설정 → 도움말**에서 가이드 재생
4. **My Apps** — list/grid/cards, pin, platform/status filt
5. **Overview**에서 시작
6. **Versions** → Build → Metadata/Media → Review Detail → **Review Submissions**
7. 홈 화면 **위젯** 및 `iappmanager://`

## 다운로드 이유

- **하나의 네이티브 책상** — ASC 웹 탭 전환 중단
- **API Key** — Keychain의 Issuer/Key/`.p8`; 다중 계정
- **Transporter 없이 업로드** — WWDC25 Build Upload REST
- **앱 내 가이드** — hard/soft 체크
- **잠금 화면 파이프라인** — 위젯
- **아키텍처 프라이버시** — `api.appstoreconnect.apple.com`

## 기능

(Sign-in, My Apps, Overview, Versions, Store listing, Monetization, TestFlight, Certificates/Reports, Widgets, Privacy — EN index와 동일 범위; deep links: `iappmanager://release-guide`, `iappmanager://iap-guide`, `iappmanager://testflight-guide`, `iappmanager://reports-guide`)

### 개인정보

키는 **Keychain**; 호출은 **Apple**만. [Privacy Policy](privacy)

## 앱 받기

| App Store | [Download](https://apps.apple.com/app/id6794497110) |

## 시스템 요구 사항

iOS 17.0+, macOS 14.0+, 위젯 iOS 17.0+, 대용량 IPA는 Mac 권장.

## 문의

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 보통 48시간 이내.

[FAQ](faq) · [Shortcut Links](url-scheme) · [Privacy Policy](privacy)
