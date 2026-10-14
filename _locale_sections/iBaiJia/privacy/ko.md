**마지막 업데이트:** 2026년 8월 18일

iHTC Studio("당사")는 **iBaiJia**("爱百家姓" / "爱百家姓", Bundle ID `com.iHTCboy.iBaiJia`)을(를) 개발했습니다. 본 개인정보 처리방침은 앱 사용 시 어떤 데이터가 처리되고 처리되지 않는지 설명합니다. **Apple App Review**와 사용자는 **이 페이지**를 공개 개인정보 처리방침으로 사용할 수 있습니다. App Store Connect에는 브라우저에서 본 개인정보 처리방침을 열고 주소창의 URL을 복사하세요(공개 사이트 도메인은 변경될 수 있습니다).

## 요약 (Apple 개인정보 영양성분표 정렬)

| 주제 | 당사의 정책 |
|-------|----------------|
| 계정 | **필요 없음** — 등록, 이메일 로그인, 전화번호 필요 없음 |
| iHTC 스튜디오의 데이터 수집 | **데이터 수집 없음** — 개인 데이터를 받는 백엔드를 운영하지 않습니다 |
| 네트워크 | Surname library, detail reading, recite, Study Hall, naming inspiration, widgets, and daily notifications work **offline** after install |
| 분석 / 광고 / 추적 | **없음** — 타사 분석, 광고, 추적 SDK 없음; 앱 추적 투명성(App Tracking Transparency) 사용 없음 |
| 선택 Apple 서비스 | **iCloud** (your private KVS), **Photo Library (Add Only)** for share cards, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default), optional **system speech / translation** |

## 데이터 수집

개인 정보를 광고나 분석 목적으로 **수집, 판매, 공유하지 않습니다**.

- **계정 불필요** — 계정을 만들지 않아도 모든 핵심 기능을 사용할 수 있습니다.
- **분석 및 광고 없음** — 앱 바이너리는 당사로 데이터를 전송하는 타사 분석, 광고, 크래시 리포트 SDK를 통합하지 않습니다.
- **콘텐츠 업로드 없음** — 사용자의 favorites, surname lists, notes, reading history, study progress, streaks, naming preferences, and settings stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## 앱 작동 방식

- **번들 라이브러리** — 텍스트 JSON, vernacular/English, 색인, 학습 보조 자료가 앱/위젯 번들에 포함됩니다. 탐색과 학습에 네트워크가 필요하지 않습니다.
- **기기 내 음성** — 읽기·낭송은 Apple **AVSpeechSynthesizer**(TTS). 성씨 텍스트를 iHTC Studio로 보내지 않습니다.
- **선택 시스템 번역** — Apple Translation(iOS 17.4+) 사용 시 Apple OS에서 처리. 번역 백엔드 없음.
- **작명 영감** — 번들 데이터로 기기에서만 생성. 이름·설정 업로드 없음.
- **위젯 및 App Group** — 위젯과 앱은 기기의 App Group `group.com.iHTCboy.iBaiJia`을 통해 설정과 가벼운 상태를 공유합니다.
- **매일 알림** — User Notifications로 로컬 예약. 탭하면 기기 딥 링크, 서버 fan-out 없음.
- **카드 공유** — 이미지가 장치에서 렌더링됩니다. 저장은 저장을 탭한 경우에만 **사진 라이브러리 추가 전용**을 사용합니다. 시스템 공유 시트는 **귀하가** 선택한 앱으로 이미지를 보낼 수 있습니다. 그러면 해당 목적지의 개인정보 보호정책이 적용됩니다.
- **선택 팁** — “Tip Developer”(`com.iHTCboy.iBaiJia.6`) Apple **StoreKit** 구매. 카드 정보 미수신.
- **Siri / 바로가기 / 제어 센터** — 선택적 시스템 통합으로 기기 내 딥 링크가 열립니다. 그들은 귀하의 라이브러리를 우리에게 보내지 않습니다.
- **선택 Spotlight** — 성씨를 기기에서 색인. 검색 백엔드 없음.
- **피드백 이메일** — 보내신 글과 문제 해결용 기기/앱 진단(버전, OS, 언어)이 포함될 수 있습니다.

## 귀하의 장치에 저장된 데이터

| 데이터 | 어디 | 목적 |
|------|-------|---------|
| 성씨 DB·획순 | App 번들 | 오프라인·따라쓰기·학습 |
| 즐겨찾기·성씨 목록 | App Group UserDefaults | 별표 성씨·목록 |
| 메모 | App Group UserDefaults | 성씨 메모 |
| 내 성씨 | App Group UserDefaults | 홈·위젯 개인화 |
| 읽기 기록 / 마지막 읽기 | App Group UserDefaults | 탐색 계속·기록 UI |
| 학습 진행·최고 점수 | App Group UserDefaults | Study Hall 상태 |
| 체크인 연속 | App Group UserDefaults | 매일 습관 |
| 모양 및 읽기 기본 설정 | 앱 그룹 UserDefaults | 테마, 악센트, 언어, 레이아웃, TTS, 탭, 위젯 |
| Daily Surname cache & notification prefs | App Group UserDefaults | 오늘 ID, 시간 |
| 공유 카드 설정 | App Group UserDefaults | Last style choices |
| 온보딩 및 TipKit 상태 | 표준 UserDefaults(장치) | 환영 가이드/탐색 팁 |
| 홈 화면 빠른 작업 | 시스템 + 로컬 환경설정 | 구성한 바로가기 |
| 위젯/실시간 활동 스냅샷 | 앱 그룹/ActivityKit | 이미 열어본 텍스트 표시 |

앱을 삭제하면 앱과 연관된 샌드박스 및 앱 그룹 데이터가 제거됩니다(iOS/macOS 동작에 따라 다름). 선택적으로 iCloud에 저장된 복사본은 사용자가 삭제하거나 동기화를 끄고 다른 곳에서 삭제할 때까지 **귀하의** iCloud에 남아 있습니다.

## iCloud 동기화 (선택 사항)

설정에서 **iCloud 동기화**를 활성화하면, 앱은 **귀하의 Apple ID**와 연결된 Apple의 **`NSUbiquitousKeyValueStore`**를 통해 선택한 사용자 데이터를 미러링합니다:

- 즐겨찾기
- 성씨 목록
- 메모
- 읽기 기록
- 학습 진행 / 최고 점수
- 체크인 연속
- 관련 설정

동기화 트래픽은 iHTC Studio가 아닌 **Apple iCloud**로 전송됩니다. 설정에서 동기화를 비활성화할 수 있습니다. 우리는 귀하의 iCloud 내용을 읽을 수 없습니다.

## 권한

iLiezi는 기능에 필요한 경우에만 권한을 요청합니다.

| 허가 | 언제 | 왜? |
|------------|------|-----|
| 알림 | Daily Surname reminders 사용 | 로컬 예약 |
## iCloud 동기화(선택)
| iCloud | 동기화 사용 | 즐겨찾기/목록/기록/진행/연속/메모 |
설정에서 **iCloud 동기화**를 켜면 앱은 **사용자의 Apple ID**에 연결된 Apple의 **`NSUbiquitousKeyValueStore`**를 통해 일부 사용자 데이터를 미러링합니다.
| 배경 오디오(iOS) | 배경 낭송 사용 | 백그라운드 TTS |

우리는 연락처, 정확한 위치, 카메라, 마이크(시스템 TTS 재생 이외) 또는 추적을 요청하지 **않습니다**.

## 아동 개인정보 보호

iBaiJia는 일반 대중을 위한 문화 학습 앱이며 **Kids Category에 해당하지 않습니다**. 당사는 아동으로부터 고의로 개인정보를 수집하지 않습니다. 계정이 필요하지 않습니다. 가족은 각자의 기기에서 오프라인으로 읽기·학습 기능을 사용할 수 있습니다.

## 제3자

제3자는 **Apple**만. 성씨 데이터셋에 CC BY 4.0·LGPL/Arphic 획순(앱 About에 표기).

## 데이터 보존 및 삭제

- **기기에서:** 진행·기록·메모 삭제. 설정에서 내보내기/가져오기. 앱 삭제로 sandbox/App Group 제거.
- **iCloud:** 설정에서 동기화 끄기. 시스템 설정에서 iCloud 저장공간 관리.
- **보관하지 않습니다** — 읽기·메모·즐겨찾기 사본 없음.

## 이 정책의 변경

법적, 제품 또는 App Store 준수 사유로 본 페이지를 업데이트할 수 있습니다. 상단의 「최종 업데이트」 날짜가 변경됩니다. 업데이트 후 계속 사용하면 개정된 정책에 동의하는 것입니다.

## 연락처

개인정보 관련 문의: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
