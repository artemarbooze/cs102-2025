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

    new_keyword = ""
    while len(new_keyword) < len(plaintext):
        new_keyword += keyword
    keyword = new_keyword.lower()

    for i in range(len(plaintext)):
        char = plaintext[i]

        if not char.isalpha():
            ciphertext += char
            continue

        shift = ord(keyword[i]) - ord("a")
        if char.islower():
            x = ord(char)
            new_x = (((x - ord("a")) + shift) % (ord("z") - ord("a") + 1)) + ord("a")
            ciphertext += chr(new_x)
        else:
            x = ord(char)
            new_x = (((x - ord("A")) + shift) % (ord("z") - ord("a") + 1)) + ord("A")
            ciphertext += chr(new_x)

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

    new_keyword = ""
    while len(new_keyword) < len(ciphertext):
        new_keyword += keyword
    keyword = new_keyword.lower()

    for i in range(len(ciphertext)):
        char = ciphertext[i]

        if not char.isalpha():
            plaintext += char
            continue

        shift = ord(keyword[i]) - ord("a")
        if char.islower():
            x = ord(char)
            new_x = (((x - ord("a")) - shift) % (ord("z") - ord("a") + 1)) + ord("a")
            plaintext += chr(new_x)
        else:
            x = ord(char)
            new_x = (((x - ord("A")) - shift) % (ord("z") - ord("a") + 1)) + ord("A")
            plaintext += chr(new_x)

    return plaintext
