import hashlib
import os
import pytest

SCHARDT_DIR = "/Users/yunji/Desktop/schardt"

# NIST SCHARDT.LOG 공식 해시값 (8개 파일 합산)
NIST_MD5    = "aee4fcd9301c03b3b054623ca261959a"
NIST_SHA1   = "4dbbeb5b5314a71054097569d570f0fcfe244d6b"
NIST_SHA256 = "a82fb41bb4ec46ab7de185600488882bed1baa268de6174e780f48320dbe9391"

# 분할 파일 목록 (8개)
SCHARDT_FILES = [f"SCHARDT.00{i}" for i in range(1, 9)]


def get_hash_multiple_files(directory, filenames, algorithm):
    """여러 분할 파일을 순서대로 읽어서 해시값 계산"""
    h = hashlib.new(algorithm)
    for filename in filenames:
        filepath = os.path.join(directory, filename)
        with open(filepath, "rb") as f:
            while chunk := f.read(8192):
                h.update(chunk)
    return h.hexdigest()


def test_full_image_md5_matches_nist():
    """8개 분할 파일 합산 MD5가 NIST 공식값과 일치하는지 검증"""
    result = get_hash_multiple_files(SCHARDT_DIR, SCHARDT_FILES, "md5")
    assert result == NIST_MD5


def test_full_image_sha1_matches_nist():
    """8개 분할 파일 합산 SHA1이 NIST 공식값과 일치하는지 검증"""
    result = get_hash_multiple_files(SCHARDT_DIR, SCHARDT_FILES, "sha1")
    assert result == NIST_SHA1


def test_full_image_sha256_matches_nist():
    """8개 분할 파일 합산 SHA256이 NIST 공식값과 일치하는지 검증"""
    result = get_hash_multiple_files(SCHARDT_DIR, SCHARDT_FILES, "sha256")
    assert result == NIST_SHA256


def test_partial_image_differs_from_full():
    """5개 파일만 계산했을 때 전체 이미지(8개) 해시와 다른지 검증
    → 분할 파일 누락 시 해시값이 달라짐을 확인"""
    partial = get_hash_multiple_files(SCHARDT_DIR, SCHARDT_FILES[:5], "md5")
    assert partial != NIST_MD5


def test_file_order_matters():
    """파일 순서가 바뀌면 해시값도 달라지는지 검증
    → 수사관이 올바른 순서로 분석해야 함을 증명"""
    correct_order = get_hash_multiple_files(SCHARDT_DIR, SCHARDT_FILES, "md5")
    reversed_order = get_hash_multiple_files(SCHARDT_DIR, list(reversed(SCHARDT_FILES)), "md5")
    assert correct_order != reversed_order


def test_individual_file_md5_matches_nist():
    """각 분할 파일의 MD5가 NIST LOG 공식값과 일치하는지 검증"""
    # NIST SCHARDT.LOG 공식 개별 파일 MD5값
    nist_individual = {
        "SCHARDT.001": "28a9b613d6eefe8a0515ef0a675bdebd",
        "SCHARDT.002": "c7227e7eea82d218663257397679a7c4",
        "SCHARDT.003": "ebba35acd7b8aa85a5a7c13f3dd733d2",
        "SCHARDT.004": "669b6636dcb4783fd5509c4710856c59",
        "SCHARDT.005": "c46e5760e3821522ee81e675422025bb",
        "SCHARDT.006": "99511901da2dea772005b5d0d764e750",
        "SCHARDT.007": "99511901da2dea772005b5d0d764e750",
        "SCHARDT.008": "8194a79a5356df79883ae2dc7415929f",
    }
    for filename, expected_md5 in nist_individual.items():
        result = get_hash_multiple_files(SCHARDT_DIR, [filename], "md5")
        assert result == expected_md5, f"{filename} MD5 불일치: {result} != {expected_md5}"
