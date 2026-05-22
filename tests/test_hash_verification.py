import hashlib
import os
import pytest

SCHARDT_DIR = "/Users/yunji/Desktop/schardt"

# Autopsy에서 확인한 전체 이미지 해시값
AUTOPSY_MD5 = "4b206f734d857c72654abad73e435a33"
AUTOPSY_SHA1 = "4dbbeb5b5314a71054097569d570f0fcfe244d6b"
AUTOPSY_SHA256 = "a82fb41bb4ec46ab7de185600488882bed1baa268de6174e780f48320dbe9391"

def get_hash_multiple_files(directory, filenames, algorithm):
    """여러 분할 파일을 순서대로 읽어서 해시값 계산"""
    h = hashlib.new(algorithm)
    for filename in filenames:
        filepath = os.path.join(directory, filename)
        with open(filepath, "rb") as f:
            while chunk := f.read(8192):
                h.update(chunk)
    return h.hexdigest()

# 분할 파일 목록
SCHARDT_FILES = [f"SCHARDT.00{i}" for i in range(1, 6)]

def test_full_image_md5_matches_autopsy():
    """5개 분할 파일 MD5가 Autopsy 결과와 일치하는지 검증"""
    result = get_hash_multiple_files(SCHARDT_DIR, SCHARDT_FILES, "md5")
    assert result == AUTOPSY_MD5

def test_full_image_sha1_matches_autopsy():
    """5개 분할 파일 SHA1이 Autopsy 결과와 일치하는지 검증"""
    result = get_hash_multiple_files(SCHARDT_DIR, SCHARDT_FILES, "sha1")
    assert result == AUTOPSY_SHA1

def test_full_image_sha256_matches_autopsy():
    """5개 분할 파일 SHA256이 Autopsy 결과와 일치하는지 검증"""
    result = get_hash_multiple_files(SCHARDT_DIR, SCHARDT_FILES, "sha256")
    assert result == AUTOPSY_SHA256

def test_partial_image_differs_from_full():
    """001 파일만 계산했을 때 전체 이미지 해시와 다른지 검증"""
    partial = get_hash_multiple_files(SCHARDT_DIR, ["SCHARDT.001"], "md5")
    assert partial != AUTOPSY_MD5

def test_file_order_matters():
    """파일 순서가 바뀌면 해시값도 달라지는지 검증"""
    correct_order = get_hash_multiple_files(SCHARDT_DIR, SCHARDT_FILES, "md5")
    reversed_order = get_hash_multiple_files(SCHARDT_DIR, list(reversed(SCHARDT_FILES)), "md5")
    assert correct_order != reversed_order
