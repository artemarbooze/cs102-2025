def encrypt_transposition(plaintext, block_size, id1, id2):
    """Encrypts text by replacing characters"""

    if id1 >= block_size or id2 >= block_size or id1 < 0 or id2 < 0:
        raise ValueError("Index must be in range from 0 to block_size-1")

    blocks = []
    for i in range(0, len(plaintext), block_size):
        blocks.append(plaintext[i:i + block_size])

    encrypted_blocks = []
    for block in blocks:
        if len(block) < block_size:
            encrypted_blocks.append(block)
            continue

        list_block = list(block)
        list_block[id1], list_block[id2] = list_block[id2], list_block[id1]
        encrypted_blocks.append("".join(list_block))

    return "".join(encrypted_blocks)


print(encrypt_transposition("Hello World", 3, 0, 2))