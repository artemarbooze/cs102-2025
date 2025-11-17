def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = keyword.upper()
    keyword_index = 0

    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                base = ord("A")
                key_char = keyword[keyword_index % len(keyword)]
                shift = ord(key_char) - ord("A")
            else:
                base = ord("a")
                key_char = keyword[keyword_index % len(keyword)].lower()
                shift = ord(key_char) - ord("a")

            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext += encrypted_char

            keyword_index += 1
        else:
            ciphertext += char

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = keyword.upper()
    keyword_index = 0

    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                base = ord("A")
                key_char = keyword[keyword_index % len(keyword)]
                shift = ord(key_char) - ord("A")
            else:
                base = ord("a")
                key_char = keyword[keyword_index % len(keyword)].lower()
                shift = ord(key_char) - ord("a")

            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            plaintext += decrypted_char

            keyword_index += 1
        else:
            plaintext += char

    return plaintext
