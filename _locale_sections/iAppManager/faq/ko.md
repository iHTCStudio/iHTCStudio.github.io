### iAppManager란?

iPhone, iPad, Mac용 **네이티브 App Store Connect 워크스테이션**입니다. **API Key**로 로그인해 버전, 스크린샷, IAP, TestFlight, 인증서, 보고서, 리뷰를 관리합니다. 트래픽은 **Apple로 직접** 갑니다. iHTC Studio 계정은 필요 없습니다.

### API Key는 어떻게 받나요?

1. [App Store Connect](https://appstoreconnect.apple.com) → **Users and Access** → **Integrations** → **App Store Connect API**
2. 키 생성(Admin 또는 App Manager 권장)
3. `.p8` **한 번만** 다운로드, **Issuer ID**와 **Key ID** 기록
4. iAppManager에 붙여넣기(또는 파일 선택). 앱 내 가이드가 스크린샷과 함께 안내합니다.

### `.p8`이 iHTC Studio에 업로드되나요?

**아니요.** 개인 키는 **기기 Keychain**에만 저장됩니다. 요청은 로컬에서 서명되어 `api.appstoreconnect.apple.com`으로 전송됩니다. 계정 제거 시 로컬 키도 삭제됩니다.

### 앱 안에서 Apple ID 비밀번호가 필요한가요?

**아니요.** 인증은 **API Key만**(Issuer ID + Key ID + `.p8`)입니다. 공개 API가 없는 기능(프라이버시 영양 라벨, 무료 App 프로모 코드 등)은 Safari/ASC에서 Apple ID를 사용합니다——앱이 Apple 사이트를 엽니다.

### Transporter 없이 IPA / PKG를 업로드할 수 있나요?

**예.** iAppManager는 Apple **Build Upload REST**(WWDC25)를 사용합니다. 큰 파일은 **Mac** 권장. iOS도 동일 API지만 대용량 업로드는 불편합니다.

### 필터 / 위젯의 "on sale"은 무엇을 뜻하나요?

**최소 하나의 App Store 지역에서 이용 가능**합니다. 파이프라인(waiting / in review / rejected / pending developer release)은 별도로 추적합니다. 위젯 **Needs attention** = waiting + in review + rejected + pending release(로컬 합계, ASC 필드 아님).

### 제출 전 hard / soft 체크?

**Hard blockers**는 제출을 막습니다(예: 빌드 미준비, 데모 계정 필요하지만 없음). **Soft checks**는 경고(주 스크린샷 크기, 저작권, 연령 등급 등)이며 확인 후 계속할 수 있습니다. Overview / Versions / Submissions의 `?` 또는 `iappmanager://release-guide` 참고.

### 지원 언어는?

**English · 简体中文 · 繁體中文**. 시스템 따르기 또는 설정에서 고정. 언어 핫스왑 시 루트를 **다시 마운트하지 않음**(내비게이션과 초안 유지).

### 위젯에 실시간 ASC 숫자가 안 보이는 이유?

위젯은 **ASC를 호출하지 않습니다**. 메인 앱이 스캔 후 스냅샷 기록(약 10분 TTL, My Apps와 동일 버킷). 앱을 열고 목록 새로고침(또는 상태 강제 새로고침)하세요.

### macOS vs iOS 차이?

둘 다 스토어, 수익화, TestFlight, Game Center, 사용자, 보고서, 리뷰, Webhooks 지원. **대용량 IPA**와 인증서를 시스템 Keychain에 설치는 **Mac** 권장. 대체 앱 아이콘은 **iOS만**.

### App Store Connect용 프라이버시 정책 URL?

본 사이트 [Privacy Policy](../privacy) 페이지를 열고 브라우저 주소창에서 URL을 복사하세요.

### 시스템 요구 사항?

iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+**.

### 지원 문의?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — 보통 48시간 이내 답변.
