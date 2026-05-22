# TC_HASH_001 - 파일 무결성 검증

## 테스트 목적
포렌식 증거 파일의 SHA-256 해시값이 수집 전후 동일한지 검증

## 관련 기능
GMDSOFT MD-RED - Data Source Integrity

## 테스트 환경
- OS: Windows 10
- Tool: Autopsy 4.23.1
- Image: SCHARDT.001 (NIST CFReDS Hacking Case)

## 테스트 케이스

| TC ID | 테스트 항목 | 입력값 | 기대 결과 | 실제 결과 | 상태 |
|---|---|---|---|---|---|
| TC-HASH-001 | 이미지 파일 해시 일관성 | SCHARDT.001 | 동일한 SHA-256 값 반환 | | |
| TC-HASH-002 | 파일 변조 감지 | 변조된 파일 | 해시값 불일치 감지 | | |
| TC-HASH-003 | 손상 파일 해시 계산 | corrupted_file.raw | 해시값 반환 성공 | | |

## 참고
Autopsy Data Source Integrity 모듈에서 자동으로 해시값 계산 수행
