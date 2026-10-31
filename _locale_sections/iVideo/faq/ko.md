### iVideo는 어떤 동영상 형식을 지원하나요?

iOS와 macOS가 네이티브로 디코드하는 형식(MP4, MOV, M4V 등)을 모두 지원합니다. 내보내기는 MP4 또는 MOV, 선택한 화질 프리셋.

### 동영상은 어디에 저장되나요?

모두 기기 로컬:

- **녹화** — App Group 공유 컨테이너
- **가져오기** — `Documents/ImportedVideos`
- **내보내기** — `Documents/Exports`

클라우드 업로드는 없습니다.

### 4K 편집이 가능한가요?

예. 4K 가져오기·편집·내보내기 지원. Ultra HD (4K) 프리셋과 Original, 2K, 1080p, 720p, 540p.

### 가변 속도는?

**0.05×~8×**. 8개 프리셋, 사용자 슬라이더, 최근 사용자 지정 2개, JKL 단축키, iPhone 핀치 조절. 설정은 세션 간 유지되며 iCloud 동기화 가능.

### JKL 단축키는?

- **L** — 정방향, 연타로 2×→4×→8×
- **J** — 역재생
- **K** — 일시정지·속도 리셋
- **K+J/L** — 0.5× 슬로우
- **Space** — 재생/일시정지
- **← →** — 1프레임, **Shift+← →** 10초

JKL HUD 및 선택 Live Activity(iOS 16.1+).

### 화면 녹화는?

- **iOS** — Record 탭 → **Broadcast Picker** → **iVideo** → **Start Broadcast**. 설정에서 자동 스냅샷 간격.
- **macOS** — **ScreenCaptureKit**. 처음에는 **시스템 설정 → 개인정보 보호 및 보안 → 화면 기록**.

iOS 녹화는 **실기기** 필요(Simulator 불가).

### Live Activity란?

JKL 사용 시 현재 속도 단계를 잠금 화면/Dynamic Island에 표시(iOS 16.1+, **설정 → 모양 → Live Activity**, 외장 키보드 권장).

### 기기 간 동기화는?

iCloud KVS로 가벼운 설정만(테마, 언어, 속도, 음소거, 사용자 속도 기록, 즐겨찾기 도구栏). **동영상 파일 자체는 동기화하지 않습니다.**

### Metadata Strip이란?

EXIF, GPS, 기기 정보 등 임베딩 메타데이터 제거 — 공개 공유 시 프라이버시.

### 콜라주 사용법?

라이브러리에서 2~4개 다중 선택 → Collage → 레이아웃 → 1920×1080 단일 동영상. 길이는 최단 클립, aspect-fill.

### Live Photo / GIF 변환?

Live Photo Studio에서 양방향 변환, 일괄 모드.

### 기기 내 자막은?

Apple Speech, `requiresOnDeviceRecognition` — 오디오 업로드 없음. Speech / Sound Events / 복합, 60+ 언어, SRT/ASS 또는 번인, Apple Translation 이중 언어.

### 얼굴 블러는?

Vision 전 프레임 자동 검출, Gaussian/Mosaic, 수동 사각형(번호판 등). 모두 기기 내.

### 배치 처리는?

다중 선택 → Batch Process → 레시피(rotate→speed→mute→watermark→metadata strip→compress 등).

### Edit Projects란?

**Edit Projects** 탭의 멀티트랙 NLE — 클립, 오버레이, PiP, BGM+내레이션, Stabilize/Smart Reframe/Slow-Mo/Multicam, Publish Wizard.

### 내보내기 큐는?

백그라운드 직렬 처리, pending/running/completed/failed, iOS 백그라운드 유지, 완료 알림(**설정 → Export**).

### 내보내기 프리셋은?

내장 4 + 사용자(화질+MP4/MOV).

### 컬러 그레이딩은?

7 매개변수, LUT 6종, 필터 11, `.cube` 가져오기.

### Speed Ramp / Beat Sync / Social Format?

Speed Ramp, Beat Sync(4 전환), Social Format(9:16 등).

### 피드백은?

**설정 → About → Feedback** 또는 [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com).

### iVideo는 무료인가요?

무료 다운로드. 선택 Tip Jar.
