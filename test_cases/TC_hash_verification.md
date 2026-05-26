# TC_HASH - 파일 무결성 검증

## 테스트 목적
포렌식 증거 파일의 해시값이 Autopsy와 Python에서 동일하게 계산되는지 교차 검증

## 관련 기능
GMDSOFT MD-RED - Data Source Integrity

## 테스트 환경
- OS: Windows 10
- Tool: Autopsy 4.23.1
- Image: SCHARDT.001~005 (NIST CFReDS Hacking Case)
- Python: 3.9.6

## 테스트 케이스

| TC ID | 테스트 항목 | 입력값 | 기대 결과 | 실제 결과 | 상태 |
|---|---|---|---|---|---|
| TC-HASH-001 | 전체 이미지 MD5 교차 검증 | SCHARDT.001~005 | Autopsy와 Python 결과 일치 | 4b206f734d857c72654abad73e435a33 | ✅ PASS |
| TC-HASH-002 | 전체 이미지 SHA1 교차 검증 | SCHARDT.001~005 | Autopsy와 Python 결과 일치 | 4dbbeb5b5314a71054097569d570f0fcfe244d6b | ✅ PASS |
| TC-HASH-003 | 전체 이미지 SHA256 교차 검증 | SCHARDT.001~005 | Autopsy와 Python 결과 일치 | a82fb41bb4ec46ab7de185600488882bed1baa268de6174e780f48320dbe9391 | ✅ PASS |
| TC-HASH-004 | 분할 파일 일부만 계산 시 차이 검증 | SCHARDT.001만 | 전체 이미지 해시와 달라야 함 | 28a9b613d6eefe8a0515ef0a675bdebd (불일치 확인) | ✅ PASS |
| TC-HASH-005 | 파일 순서 변경 시 해시값 변화 검증 | SCHARDT.005~001 (역순) | 정순과 해시값 달라야 함 | 역순 계산 시 다른 값 반환 확인 | ✅ PASS |

## 결론
Autopsy와 Python이 동일한 해시값을 계산함을 확인.
SCHARDT 이미지는 변조되지 않은 상태임이 두 툴 모두에서 검증됨.
