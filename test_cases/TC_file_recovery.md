# TC_FILE_RECOVERY - 삭제 파일 복구 검증

## 테스트 목적
포렌식 이미지에서 삭제된 파일이 정확히 복구되는지 검증

## 관련 기능
GMDSOFT MD-RED - Deleted File Recovery

## 테스트 환경
- OS: Windows 10
- Tool: Autopsy 4.23.1
- Image: SCHARDT.001 (NIST CFReDS Hacking Case)

## 테스트 케이스

| TC ID | 테스트 항목 | 입력값 | 기대 결과 | 실제 결과 | 상태 |
|---|---|---|---|---|---|
| TC-REC-001 | 삭제 파일 목록 추출 | SCHARDT.001 | 삭제된 파일 목록 반환 | | |
| TC-REC-002 | 삭제 파일 복구 가능 여부 | 삭제된 파일 | 파일 내용 복구 성공 | | |
| TC-REC-003 | 복구 파일 무결성 검증 | 복구된 파일 | 원본과 해시값 일치 | | |

## 참고
Autopsy Deleted Files 섹션에서 확인 가능
