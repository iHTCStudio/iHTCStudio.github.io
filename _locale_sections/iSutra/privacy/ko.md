**마지막 업데이트:** 2026년 8월 18일

iHTC Studio("당사")는 **iSutra**("爱佛经" / "爱佛经", Bundle ID `com.iHTCboy.iSutra`)을(를) 개발했습니다. 본 개인정보 처리방침은 앱 사용 시 어떤 데이터가 처리되고 처리되지 않는지 설명합니다. **Apple App Review**와 사용자는 **이 페이지**를 공개 개인정보 처리방침으로 사용할 수 있습니다. App Store Connect에는 브라우저에서 본 개인정보 처리방침을 열고 주소창의 URL을 복사하세요(공개 사이트 도메인은 변경될 수 있습니다).

## 요약 (Apple 개인정보 영양성분표 정렬)

| 주제 | 당사의 정책 |
|-------|----------------|
| 계정 | **필요 없음** — 등록, 이메일 로그인, 전화번호 필요 없음 |
| iHTC 스튜디오의 데이터 수집 | **데이터 수집 없음** — 개인 데이터를 받는 백엔드를 운영하지 않습니다 |
| 네트워크 | 라이브러리, reading, recite, Study Hall, Hunt, chant, practice, widgets, and daily notifications work **offline** after install는 설치 후 **오프라인**으로 동작합니다 |
| 분석 / 광고 / 추적 | **없음** — 타사 분석, 광고, 추적 SDK 없음; 앱 추적 투명성(App Tracking Transparency) 사용 없음 |
| 선택 Apple 서비스 | **iCloud** (your private KVS), **Photo Library (Add Only)** for Dharma cards / exports, **StoreKit** for optional tipping, **local notifications**, optional **Live Activities**, optional **Spotlight** (off by default) |

## 데이터 수집

개인 정보를 광고나 분석 목적으로 **수집, 판매, 공유하지 않습니다**.

- **계정 불필요** — 계정을 만들지 않아도 모든 핵심 기능을 사용할 수 있습니다.
- **분석 및 광고 없음** — 앱 바이너리는 당사로 데이터를 전송하는 타사 분석, 광고, 크래시 리포트 SDK를 통합하지 않습니다.
- **콘텐츠 업로드 없음** — 사용자의 reading history, favorites, lists, notes, mastery, streaks, chant counts, practice checklists, and preferences stay on your device (and optionally in **your** iCloud). They are never uploaded to iHTC Studio servers because **we do not run such servers for this app**.

## 앱 작동 방식

- **번들 라이브러리** — 텍스트 JSON, vernacular/English, 색인, 학습 보조 자료가 앱/위젯 번들에 포함됩니다. 탐색과 학습에 네트워크가 필요하지 않습니다.
- **기기 내 음성** — **AVSpeechSynthesizer**로 낭송. 경전 텍스트 미전송.
- **위젯 및 App Group** — 위젯과 앱은 기기의 App Group `group.com.iHTCboy.iSutra`을 통해 설정과 가벼운 상태를 공유합니다.
- **일일 알림** — 사용자 알림을 통해 로컬로 예약됩니다. 알림을 탭하면 기기의 통로 ID에 대한 딥 링크가 열립니다. 서버 팬아웃이 없습니다.
- **법 카드 / 내보내기** — 이미지·PDF는 기기에서 생성. 저장 시 **사진 보관함(추가 전용)**. **공유 시트**는 **사용자가 선택한** 앱으로 보낼 수 있습니다.
- **필경(iOS)** — PencilKit 획은 Application Support(`CopySutra/…`)에 저장됩니다. **App Group에 두지 않으며** **iCloud 동기화되지 않습니다**.
- **선택적 팁** — "팁 개발자"는 Apple에서 처리하는 소모품 **StoreKit** 구매입니다. 귀하의 결제 카드 정보는 수신되지 않습니다.
- **Siri / 바로가기 / 제어 센터** — 선택적 시스템 통합으로 기기 내 딥 링크가 열립니다. 그들은 귀하의 라이브러리를 우리에게 보내지 않습니다.
- **선택적 스포트라이트** — 기본적으로 꺼져 있습니다. 인덱싱을 활성화하면 로컬 검색을 위해 장치의 시스템이 콘텐츠를 인덱싱합니다. 우리는 검색 백엔드를 운영하지 않습니다.

## 귀하의 장치에 저장된 데이터

| 데이터 | 어디 | 목적 |
|------|-------|---------|
| 불경 DB(색인·샤드) | App / Widget 번들 | 오프라인 읽기·학습 |
| 즐겨찾기 및 목록(经单) | App Group UserDefaults | 별표 표시한 구절과 사용자 목록 |
| 읽은 이력/마지막 읽은 내용 | 앱 그룹 UserDefaults | 계속 읽기, 기록 UI |
| 학습 진행 및 숙달 | App Group UserDefaults | Study Hall state, quiz / Hunt progress |
| 메모 | App Group UserDefaults | 구절 메모 |
| 연속연습/체크인 | 앱 그룹 UserDefaults | 일상습관 |
| 염불 횟수·음향 설정 | App Group UserDefaults | 목어 합계·목표·음색 |
| 아침·저녁 수행 | App Group UserDefaults | 일과 체크리스트 |
| 모양 및 읽기 기본 설정 | 앱 그룹 UserDefaults | 테마, 악센트, 언어, 레이아웃, TTS, 탭, 위젯 |
| Daily Sutra cache & notification prefs | App Group UserDefaults | 오늘 ID, 시간 |
| 공유 카드 환경 설정 | 앱 그룹 UserDefaults | 마지막 스타일/비율 선택 |
| 필경 데이터(iOS) | Application Support(`CopySutra/`) | 줄별 따라쓰기 초안 |
| 온보딩 및 TipKit 상태 | 표준 UserDefaults(장치) | 환영 가이드/탐색 팁 |
| 홈 화면 빠른 작업 | 시스템 + 로컬 환경설정 | 구성한 바로가기 |
| Widget / Live Activity 스냅샷 | App Group / ActivityKit | 연 텍스트/chant 상태 표시 |

앱을 삭제하면 앱과 연관된 샌드박스 및 앱 그룹 데이터가 제거됩니다(iOS/macOS 동작에 따라 다름). 선택적으로 iCloud에 저장된 복사본은 사용자가 삭제하거나 동기화를 끄고 다른 곳에서 삭제할 때까지 **귀하의** iCloud에 남아 있습니다.

## iCloud 동기화 (선택 사항)

설정에서 **iCloud Sync** 사용 시 **Apple ID**의 **`NSUbiquitousKeyValueStore`**로 미러(즐겨찾기·목록·기록 등). **Apple iCloud**로만. 필경 그림 **미포함**. iCloud 내용 읽을 수 없음.

## 권한

iLiezi는 기능에 필요한 경우에만 권한을 요청합니다.

| 허가 | 언제 | 왜? |
|------------|------|-----|
| 알림 | Daily Sutra reminders 사용 | 로컬 예약 of reminder notifications |
| 사진 보관함(추가 전용) | 법 카드 저장/내보내기 | 렌더 이미지/PDF 기록(전체 읽기 불필요) |
| iCloud | 동기화 사용 | 즐겨찾기/목록/기록/숙달/메모/chant·수행 설정 |
| Live Activities(iOS) | Reading/Chant Live Activity | 읽기/chant 진행 표시 |
| 배경 오디오(기능) | 배경 암송을 활성화합니다 | 앱이 포그라운드가 아닐 때 TTS 계속 |

우리는 연락처, 정확한 위치, 카메라, 마이크(시스템 TTS 재생 이외) 또는 추적을 요청하지 **않습니다**.

## 우리가 하지 않는 일

- 당사는 개인 데이터를 판매하지 **않습니다**.
- 우리는 광고 프로필을 작성하지 **않습니다**.
- 계정이나 소셜 로그인이 필요하지 **않습니다**.
- 당사는 데이터 수집을 위해 제3자 광고, 분석 또는 소셜 SDK를 삽입하지 **않습니다**.
- 저장 선택 시 **추가 전용** 외 사진 보관함 접근 없음.
- 저희는 StoreKit 결제 카드 번호를 받지 **않습니다**(Apple에서 결제를 처리함).
- 종교 콘텐츠를 점술·유료 축복 상업으로 **바꾸지 않습니다**.

## 아동 개인정보 보호

iSutra는 13세 미만 포함 고의 수집 없음. backend 없어 아동 프로필 없음. 가족 오프라인 이용 가능.

## 제3자

- **Apple** — App Store 배포, 선택적 StoreKit 구매, 선택적 iCloud KVS, 시스템 TTS, 사용자가 선택한 공유 시트 대상, OS 수준의 알림 / 라이브 액티비티 / Siri / 단축키 전달.
- 광고, 분석, 소셜 로그인 등을 위한 **기타 제3자 SDK**는 데이터 수집을 위해 포함되지 않았습니다.

## 국제 사용자

앱은 사용자의 장치에서 오프라인 기능이 가능하도록 설계되었습니다. 선택적 Apple 서비스는 Apple의 이용 약관 및 지역 가용성을 따릅니다.

## 데이터 보존 및 삭제

- **기기 내** — 로컬 환경설정 및 진행 상황은 앱 내에서 삭제하지 않거나, 기기를 초기화하거나, 앱을 제거하지 않는 한 그대로 남아 있습니다(해당 기능이 제공되는 경우).
- **iCloud (선택 사항)** — 동기화한 데이터는 동기화를 해제하거나 Apple의 도구를 통해 삭제할 때까지 Apple 정책에 따라 **귀하의** iCloud 계정에 남아 있습니다.
- **iHTC Studio** — 당사는 서버에 개인 데이터를 수집하지 않기 때문에 이메일 문의에 답변하는 것을 제외하고 요청 시 삭제할 계정 데이터셋이 없습니다.

## 이 정책의 변경

본 개인정보처리방침은 수시로 업데이트될 수 있습니다. 상단의 '마지막 업데이트' 날짜가 변경되며, 수정된 정책은 이 개인정보처리방침 페이지에 게시됩니다.

## 문의하기

본 개인정보처리방침이나 개인정보 처리 관행에 대해 질문이 있는 경우:

- **이메일:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

일반적으로 48시간 이내에 회신합니다.
