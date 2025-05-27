import pytest
from src.lab1_2.vigenere import encrypt_vigenere, decrypt_vigenere

def test_encrypt_vigenere():
    assert encrypt_vigenere("ATTACKATDAWN", "LEMON") == "LXFOPVEFRNHR"
    assert encrypt_vigenere("python", "a") == "python"
    assert encrypt_vigenere("PYTHON", "A") == "PYTHON"
    assert encrypt_vigenere("", "KEY") == ""

def test_decrypt_vigenere():
    assert decrypt_vigenere("LXFOPVEFRNHR", "LEMON") == "ATTACKATDAWN"
    assert decrypt_vigenere("python", "a") == "python"
    assert decrypt_vigenere("PYTHON", "A") == "PYTHON"
    assert decrypt_vigenere("", "KEY") == ""

def test_vigenere_roundtrip():
    text = "Secret Message 123!"
    key = "KEY"
    assert decrypt_vigenere(encrypt_vigenere(text, key), key) == text