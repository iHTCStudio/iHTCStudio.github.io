**최종 업데이트:** 2026년 9월 9일

iHTC Studio(「당사」)는 **iMusic**(「爱音乐」/「愛音樂」, Bundle ID `com.iHTCboy.iMusic`)을 개발했습니다. 이 페이지는 앱 및 위젯 확장 사용 시 어떤 데이터가 처리되는지(또는 처리되지 않는지) 설명합니다. **Apple App Review** 및 사용자는 본 페이지를 공개 개인정보 처리방침으로 참고할 수 있습니다. App Store Connect: 브라우저에서 본 [Privacy Policy](../privacy)를 열고 주소창 URL을 복사하세요(공개 도메인은 변경될 수 있음).

## 요약(Apple Privacy Nutrition Label 정렬)

| 항목 | 당사 방침 |
|-------|----------------|
| 계정 | **불필요** — 가입, 이메일, 전화번호 없음 |
| iHTC Studio 데이터 수집 | **Data Not Collected** — 개인 데이터를 받는 backend **미운영** |
| 네트워크 | **가이드**는 설치 후 **오프라인** 열람; **재생**·**곡 인식**은 허용 후 Apple 서비스 |
| 분석/광고/추적 | **없음** — 제3자 analytics/광고/추적 SDK 없음; ATT 미사용 |
| 선택 Apple 서비스 | **Apple Music/MusicKit**, **ShazamKit**, **iCloud**(private KVS), 공유 카드용 **사진(추가만)**, 선택 **StoreKit** 팁, **로컬 알림**, 선택 **Live Activities** |

## 데이터 수집

광고·분석 목적으로 개인정보를 수집·판매·공유**하지 않습니다**.

- **계정 없음** — iHTC Studio 계정 없이 동봉 가이드 전부 이용.
- **분석·광고 없음** — 당사로 전화하는 제3자 analytics/광고/크래시 SDK 없음.
- **가이드 업로드 없음** — 즐겨찾기, 리스트, 나중에 듣기, 메모, 기록, 설정은 기기(및 선택 시 **귀하의** iCloud)에만; iHTC Studio 서버로 전송 안 함(**본 앱용 such 서버 미운영**).
- **곡 호스팅 없음** — 전체 오디오 미포함. 매칭 재생은 **Apple Music**. 미가입 시 최대 **30초 카탈로그 미리듣기**가 기기에 캐시될 수 있음.

## 앱 동작

- **동봉 라이브러리** — 곡 색인, 가이드, 아티스트 노트, 카테고리, 컬렉션, 명구, 일일 달력 App/Widget 동봉; 가이드는 네트워크 불필요.
- **Apple Music(MusicKit)** — 재생 허용 시 큐레이션 카탈로그 매칭(ISRC 우선, 아티스트+제목) 후 Apple 플레이어. 구독 상태는 Apple 문의; 타임아웃은 **알 수 없음**. 커버용 artwork URL. Apple ID/결제 정보는 당사에 없음.
- **30초 미리듣기** — 미가입 시 Apple 미리듣기가 `Caches`에 저장될 수 있음(LRU; 전체 트랙 아님). 셀룰러/저전력/저데이터 모드에서 다음 미리듣기 선로드 안 함. 설정에서 artwork·미리듣기 캐시 개별 삭제, 즐겨찾기/리스트는 유지.
- **곡 인식(ShazamKit)** — Recognize 열 때만; 마이크는 **Apple** 처리; 녹음 아카이브 없음. 히트 시 기기 내 가이드.
- **기기 내 음성** — 가이드 낭독 **AVSpeechSynthesizer**; 본문 iHTC Studio 미전송.
- **Widget & App Group** — `group.com.iHTCboy.iMusic` 설정 공유; Live Activity artwork 소형 JPEG+토큰.
- **일일 알림** — 로컬 예약; 탭 시 곡 ID 딥링크.
- **공유 카드** — 기기 렌더링; 저장 시 **사진 추가만**.
- **선택 팁** — **StoreKit** 소모형.
- **선택 Spotlight** — **기본 꺼짐**; 켜면 기기에서 시스템 색인.

## 기기 저장 데이터

| 데이터 | 위치 | 목적 |
|------|-------|---------|
| 가이드 라이브러리 | App/Widget bundle | 오프라인 |
| 즐겨찾기·리스트·나중에 | App Group UserDefaults | 목록 |
| 메모·기록·낭독 진행 | App Group UserDefaults | 이어하기 |
| 스트릭/체크인 | App Group UserDefaults | 습관 |
| 외관·언어·탭 | App Group UserDefaults | 설정 |
| Daily Piece 캐시·알림 | App Group UserDefaults | 오늘 ID |
| 공유 카드 설정 | App Group UserDefaults | 스타일 |
| Artwork URL·이미지 | App Group+캐시 | 커버 |
| 30초 미리듣기 파일 | App Caches | 오프라인 |
| Live Activity 썸네일 | App Group JPEG+토큰 | **낭독** 중 잠금화면 |
| MusicKit/Shazam 허용 | 시스템 | 선택 기억 |
| 온보딩·리뷰 | UserDefaults | 환영/리뷰 |

삭제 시 sandbox·App Group 제거(iOS/macOS 규칙). 선택 iCloud는 **귀하의** iCloud에 잔류. Apple Music 라이브러리·구독은 Apple.

## iCloud 동기화(선택)

**iCloud Sync** 켜면 **Apple ID**의 **`NSUbiquitousKeyValueStore`**에 미러:

- 즐겨찾기, 리스트, 나중에, 메모, 청취/열람 기록, 낭독 진행, 스트릭

가이드 본문은 App 동봉. Artwork·미리듣기 오디오 KVS **미동기**. **Apple iCloud**로만; iHTC Studio 경유 없음. 끄기 가능; 당사는 iCloud 읽기 불가.

## 권한

| 권한 | 시점 | 이유 |
|------------|------|-----|
| **Apple Music/미디어** | MusicKit 또는 재생 | 매칭·재생·커버 |
| **마이크** | Song ID | 주변 음악 인식 |
| **알림** | Daily Piece | 로컬 |
| **사진(추가만)** | 뮤직 카드 저장 | 렌더 이미지 |
| **iCloud** | 동기화 | 목록/메모/기록 |
| **Live Activities** | Reading(기본 켜짐) | **낭독** 중 잠금화면 |
| **백그라운드 오디오** | 옵션 | MusicKit/미리듣기/TTS |

연락처·정밀 위치·카메라·추적 없음. 사진 라이브러리 **읽기** 없음.

## 하지 않는 일

- 개인정보 판매·광고 프로필 없음
- 계정·소셜 로그인 강제 없음
- 데이터 수집 목적 제3자 SDK 없음
- 전체 곡 당사 서버/기기 저장 없음
- Shazam 마이크 버퍼 인식 후 보관 없음
- **음악 재생**용 커스텀 Dynamic Island 없음 — 가이드 낭독만
- StoreKit 카드번호 미수신

## 아동

13세 미만(또는 지역 동등 연령) 포함 고의 수집 없음. 수집 backend 없음 → 아동 프로필 없음. Apple Music·Shazam은 Apple 규정.

## 제3자

- **Apple** — App Store, MusicKit, ShazamKit, StoreKit, iCloud KVS, TTS, 공유, 알림, Live Activities, Siri/Shortcuts
- 데이터 수집 **다른 SDK 없음**

## 국제 사용자

가이드 기기 오프라인. Apple Music·Shazam·iCloud Apple 약관. 카탈로그 매칭은 로그인 Apple ID 스토어프론트.

## 보관·삭제

- **기기** — **설정→저장장치**에서 캐시 삭제; 삭제 시 sandbox/App Group
- **iCloud** — **귀하의** iCloud에 잔류
- **iHTC Studio** — 서버 계정 데이터 없음

## 변경

정책 업데이트 가능; 상단 날짜 변경.

## 문의

- **이메일:** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

보통 48시간 이내 답변.
