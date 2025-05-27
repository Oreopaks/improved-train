import pytest
from src.lab1_2.caesar import encrypt_caesar, decrypt_caesar

def test_encrypt_caesar():
    assert encrypt_caesar("PYTHON") == "SBWKRQ"
    assert encrypt_caesar("python") == "sbwkrq"
    assert encrypt_caesar("Python3.6") == "Sbwkrq3.6"
    assert encrypt_caesar("", 5) == ""

def test_decrypt_caesar():
    assert decrypt_caesar("SBWKRQ") == "PYTHON"
    assert decrypt_caesar("sbwkrq") == "python"
    assert decrypt_caesar("Sbwkrq3.6") == "Python3.6"
    assert decrypt_caesar("", 5) == ""

def test_caesar_roundtrip():
    text = "Hello World 123!"
    assert decrypt_caesar(encrypt_caesar(text, 7), 7) == text