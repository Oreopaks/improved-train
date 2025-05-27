def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    result = ""
    shift %= 26
    for ch in plaintext:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += ch
    return result

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    return encrypt_caesar(ciphertext, -shift)