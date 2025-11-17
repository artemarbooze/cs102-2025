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
    key_length = len(keyword)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shift = ord(keyword[key_index % key_length]) - ord("A")
            encrypted = (ord(char) - base + shift) % 26
            ciphertext += chr(encrypted + base)
            key_index += 1
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
    key_length = len(keyword)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shift = ord(keyword[key_index % key_length]) - ord("A")
            decrypted = (ord(char) - base - shift) % 26
            plaintext += chr(decrypted + base)
            key_index += 1
        else:
            plaintext += char

    return plaintext
