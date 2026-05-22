# TC_METADATA - 메타데이터 추출 검증

## 테스트 목적
포렌식 이미지에서 파일 메타데이터가 정확히 추출되는지 검증

## 관련 기능
GMDSOFT MD-RED - File Metadata Extraction

## 테스트 환경
- OS: Windows 10
- Tool: Autopsy 4.23.1
- Image: SCHARDT.001 (NIST CFReDS Hacking Case)

## 테스트 케이스

| TC ID | 테스트 항목 | 입력값 | 기대 결과 | 실제 결과 | 상태 |
|---|---|---|---|---|---|
| TC-META-001 | 파일 생성 시간 추출 | SCHARDT.001 | Created Time 정확히 반환 | | |
| TC-META-002 | 파일 수정 시간 추출 | SCHARDT.001 | Modified Time 정확히 반환 | | |
| TC-META-003 | 파일 크기 추출 | SCHARDT.001 | 실제 크기와 일치 | | |
| TC-META-004 | 파일 확장자 분류 | SCHARDT.001 | 확장자별 정확히 분류 | | |

## 참고
Autopsy File Metadata 탭에서 확인 가능
