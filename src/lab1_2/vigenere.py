def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    keyword = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]
    ciphertext = ""
    shift_i = 0
    for ind in range(len(plaintext)):
        shift = ord(keyword[shift_i])
        if 65 <= shift <= 90: shift -= 65
        elif 97 <= shift <= 122: shift -= 97
        i = plaintext[ind]
        if i.isupper():
            ciphertext += chr((ord(i) - 65 + shift) % 26 + 65)
            shift_i += 1
        elif i.islower():
            ciphertext += chr((ord(i) - 97 + shift) % 26 + 97)
            shift_i += 1
        else:
            ciphertext += i
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    keyword = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]
    plaintext = ""
    shift_i = 0
    for ind in range(len(ciphertext)):
        shift = ord(keyword[shift_i])
        if 65 <= shift <= 90: shift -= 65
        elif 97 <= shift <= 122: shift -= 97
        i = ciphertext[ind]
        if i.isupper():
            c = (ord(i) - 65 - shift) % 26
            plaintext += chr(c + 65)
            shift_i += 1
        elif i.islower():
            c = (ord(i) - 97 - shift) % 26
            plaintext += chr(c + 97)
            shift_i += 1
        else:
            plaintext += i
    return plaintext