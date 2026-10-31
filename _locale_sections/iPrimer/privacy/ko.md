**마지막 업데이트:** 2026년 8월 18일

iHTC Studio("당사")는 **iPrimer**("爱小学" / "爱小学", Bundle ID `com.iHTCboy.iPrimer`)을(를) 개발했습니다. 본 개인정보 처리방침은 앱 사용 시 어떤 데이터가 처리되고 처리되지 않는지 설명합니다. **Apple App Review**와 사용자는 **이 페이지**를 공개 개인정보 처리방침으로 사용할 수 있습니다. App Store Connect에는 브라우저에서 본 개인정보 처리방침을 열고 주소창의 URL을 복사하세요(공개 사이트 도메인은 변경될 수 있습니다).

## 요약 (Apple 개인정보 영양성분표 정렬)

| 주제 | 당사의 정책 |
|-------|----------------|
| 계정 | **필요 없음** — 등록, 이메일 로그인, 전화번호 필요 없음 |
| iHTC 스튜디오의 데이터 수집 | **데이터 수집 없음** — 개인 데이터를 받는 백엔드를 운영하지 않습니다 |
| 네트워크 | 라이브러리, reading, recite, Character Study, meditation, Life Guidance, widgets, and daily notifications work **offline** after install는 설치 후 **오프라인**으로 동작합니다 |
| 분석 / 광고 / 추적 | **없음** — 타사 분석, 광고, 추적 SDK 없음; 앱 추적 투명성(App Tracking Transparency) 사용 없음 |
| 선택적 Apple 서비스 | **iCloud** (개인 KVS), **사진 라이브러리(추가만 가능)** 공유 카드용, **StoreKit** 선택적 후원용, **로컬 알림**, 선택적 **라이브 활동(Live Activities)** |

## 데이터 수집

개인 정보를 광고나 분석 목적으로 **수집, 판매, 공유하지 않습니다**.

- **계정 불필요** — 계정을 만들지 않아도 모든 핵심 기능을 사용할 수 있습니다.
- **분석 및 광고 없음** — 앱 바이너리는 당사로 데이터를 전송하는 타사 분석, 광고, 크래시 리포트 SDK를 통합하지 않습니다.
- **콘텐츠 업로드 없음** — 사용자의 reading history, favorites, study lists, reflection journal entries, habit check-ins, meditation streaks, study progress, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## 앱 작동 방식

- **번들 라이브러리** — 텍스트 JSON, vernacular/English, 색인, 학습 보조 자료가 앱/위젯 번들에 포함됩니다. 탐색과 학습에 네트워크가 필요하지 않습니다.
- **기기 내 음성** — 암송은 Apple 시스템 **AVSpeechSynthesizer**(TTS)를 사용합니다. iHTC Studio에는 장 텍스트를 보내지 않습니다.
- **위젯 및 App Group** — 위젯과 앱은 기기의 App Group `group.com.iHTCboy.iPrimer`을 통해 설정과 가벼운 상태를 공유합니다.
- **일일 알림** — 사용자 알림을 통해 로컬로 예약됩니다. 알림을 탭하면 기기의 챕터 ID에 대한 딥 링크가 열립니다. 서버 팬아웃이 없습니다.
- **카드 공유** — 이미지가 장치에서 렌더링됩니다. 저장은 저장을 탭한 경우에만 **사진 라이브러리 추가 전용**을 사용합니다. 시스템 공유 시트는 **귀하가** 선택한 앱으로 이미지를 보낼 수 있습니다. 그러면 해당 목적지의 개인정보 보호정책이 적용됩니다.
- **선택 팁** — “Tip Developer”(`com.iHTCboy.iPrimer.6`) Apple **StoreKit** 구매. 카드 정보 미수신.
- **Siri / 바로가기 / 제어 센터** — 선택적 시스템 통합으로 기기 내 딥 링크가 열립니다. 그들은 귀하의 라이브러리를 우리에게 보내지 않습니다.
- **선택적 스포트라이트** — 인덱싱을 활성화하면 로컬 검색을 위해 장치의 시스템에서 콘텐츠를 인덱싱합니다. 우리는 검색 백엔드를 운영하지 않습니다.

## 귀하의 장치에 저장된 데이터

| 데이터 | 어디 | 목적 |
|------|-------|---------|
| Chapter 데이터베이스 | App / Widget 번들 | 오프라인 읽기 및 학습 |
| 즐겨찾기·학습 목록 | App Group UserDefaults | 별표 작품·목록 |
| 읽은 이력/마지막 읽은 내용 | 앱 그룹 UserDefaults | 계속 읽기, 기록 UI |
| 학습 진행 및 숙달 | App Group UserDefaults | Character Study state, quiz / Hunt progress |
| 학습 연속 / 체크인 | App Group UserDefaults | Daily Study 습관 |
| 성찰 저널 | App Group UserDefaults | Life Guidance 저널 |
| 습관 체크인(洒扫应对) | App Group UserDefaults | Life Guidance 일일 습관 |
| 명상 연속·세션 설정 | App Group UserDefaults | 명상 연속 |
| 공유 카드 설정 | App Group UserDefaults | 마지막으로 선택한 스타일 / 비율 |
| Daily Study cache & notification prefs | App Group UserDefaults | 오늘 ID, 시간, contextual toggle |
| 공유 카드 환경 설정 | 앱 그룹 UserDefaults | 마지막 스타일/비율 선택 |
| 온보딩 및 TipKit 상태 | 표준 UserDefaults(장치) | 환영 가이드/탐색 팁 |
| 홈 화면 빠른 작업 | 시스템 + 로컬 환경설정 | 구성한 바로가기 |
| 위젯/실시간 활동 스냅샷 | 앱 그룹/ActivityKit | 이미 열어본 텍스트 표시 |

앱을 삭제하면 앱과 연관된 샌드박스 및 앱 그룹 데이터가 제거됩니다(iOS/macOS 동작에 따라 다름). 선택적으로 iCloud에 저장된 복사본은 사용자가 삭제하거나 동기화를 끄고 다른 곳에서 삭제할 때까지 **귀하의** iCloud에 남아 있습니다.

## iCloud 동기화 (선택 사항)

설정에서 **iCloud 동기화**를 활성화하면, 앱은 **귀하의 Apple ID**와 연결된 Apple의 **`NSUbiquitousKeyValueStore`**를 통해 선택한 사용자 데이터를 미러링합니다:

- 즐겨찾기
- 학습 목록
- 읽기 기록
- 학습 진행/숙련도
- 학습 연속
- 성찰 저널
- 습관 체크인 기록

동기화 트래픽은 iHTC Studio가 아닌 **Apple iCloud**로 전송됩니다. 설정에서 동기화를 비활성화할 수 있습니다. 우리는 귀하의 iCloud 내용을 읽을 수 없습니다.

## 권한

iLiezi는 기능에 필요한 경우에만 권한을 요청합니다.

| 허가 | 언제 | 왜? |
|------------|------|-----|
| 알림 | Daily Study or meditation reminders 사용 | 로컬 예약 |
## iCloud 동기화(선택)
| iCloud | 동기화 사용 | 즐겨찾기/목록/기록/진행/연속/저널/습관 |
| Live Activities(iOS) | Reading/Meditation Live Activity | 잠금 화면 / Dynamic Island |
| 배경 오디오 | 배경 낭송 사용 | 백그라운드 TTS |

우리는 연락처, 정확한 위치, 카메라, 마이크(시스템 TTS 재생 이외) 또는 추적을 요청하지 **않습니다**.

## 아동 개인정보 보호

iPrimer **12+**, **Kids Category 아님**. 아동 개인정보 고의 수집 안 함. 계정 불필요.

## 제3자

일반 사용 시 제3자는 **Apple**만(App Store, iCloud, StoreKit, TTS, 알림, Live Activities).

## 데이터 보존 및 삭제

- **기기에서:** 앱 삭제 시 로컬 sandbox·App Group 데이터 제거(시스템 동작에 따름).
- **iCloud:** 설정에서 동기화 끄기. 시스템 설정에서 iCloud 저장공간 관리.
- **보관하지 않습니다** — 읽기·저널·습관 데이터 사본을 iHTC Studio 서버에 두지 않습니다.

## 이 정책의 변경

법적, 제품 또는 App Store 준수 사유로 본 페이지를 업데이트할 수 있습니다. 상단의 「최종 업데이트」 날짜가 변경됩니다. 업데이트 후 계속 사용하면 개정된 정책에 동의하는 것입니다.

## 연락처

개인정보 관련 문의: [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
