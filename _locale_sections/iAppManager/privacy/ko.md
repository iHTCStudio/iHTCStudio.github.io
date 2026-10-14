iHTC Studio(당사)는 iAppManager(爱应用者 / 愛應用者)를 개발했습니다.

## 요약

**iHTC Studio는 App Store Connect 데이터용 백엔드를 운영하지 않습니다.** **API Key**로 로그인하며 키는 **기기 Keychain**에 저장됩니다. 업무 요청은 **Apple로 직접**(`api.appstoreconnect.apple.com`) 전송됩니다. **iHTC Studio 계정 불필요. 광고 없음. 분석 / 크래시 SDK 없음.** 선택적 StoreKit 팁은 **Apple**이 처리합니다.

## 기기에 저장되는 데이터

| 데이터 | 용도 |
|------|------|
| API Key 계정(Issuer ID, Key ID, `.p8` PEM) | App Store Connect API 인증 — Keychain |
| 계정 색인 / 현재 계정 / 환경설정 | 다중 계정, 모양, 언어, 강조색 |
| 원격 이미지 캐시 | App 아이콘 및 미디어 썸네일(설정에서 삭제 가능) |
| 리뷰 답글 템플릿, 보고서 프리셋 / 별표 | 계정별 로컬 생산성 도구 |
| App Group 위젯 스냅샷 | 파이프라인 건수, 테마 / 언어 — **기기 내부만** |

## 네트워크

| 대상 | 이유 |
|-------------|-----|
| `api.appstoreconnect.apple.com` | 모든 ASC 관리(JWT는 기기에서 서명) |
| Apple iTunes Lookup(다중 지역) | 선택적 App 아이콘 보강 |
| Apple CDN / 사전 서명 업로드 URL | 스크린샷, 미리보기, IPA/PKG 청크 업로드(PUT에 Bearer 없음) |
| `apps.apple.com` / App Store | 제품 페이지 열기(시스템 / 외부) |
| 메일 클라이언트 | 사용자가 보내기를 선택한 피드백 |

iHTC Studio는 API 개인 키, App 메타데이터, IPA 내용, 판매 보고서, 고객 리뷰를 **받지 않습니다**.

## 권한 및 플랫폼

| 기능 | 시점 | 이유 |
|------------|------|-----|
| 아웃바운드 네트워크 | ASC 기능 사용 중 | Apple API 통신 |
| 사용자가 선택한 파일 | IPA/스크린샷 업로드, 보고서 내보내기 | 사용자가 파일 선택 |
| Keychain | API Key 저장 / 제거 | 안전한 로컬 저장 |
| App Group | 위젯 | 로컬 요약만 공유 |
| 사진 / 공유 시트(OS 제공 시) | 사용자가 내보내기 / 저장할 때 | 사용자 주도 |

인증서 **시스템 Keychain 설치**는 **macOS**용입니다. iOS는 목록 / 다운로드 / 공유 중심입니다.

## 하지 않는 일

- ASC 데이터용 iHTC Studio 클라우드 계정 없음
- 광고 또는 서드파티 추적 없음
- 개인 데이터 판매 없음
- 위젯이 스스로 ASC를 호출하지 않음

## 문의

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
