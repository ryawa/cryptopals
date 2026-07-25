import crypto

with open("6.txt", "r") as f:
    contents = f.read().replace("\n", "")

c = crypto.decode_base64(contents)

# Score keysizes between 2-40 with the edit distance between the first and second keysize worth of bytes in the ciphertext.
keysizes: list[tuple[int, float]] = []
for keysize in range(2, 40):
    keysizes.append((
        keysize,
        crypto.hamming_dist(c[:keysize], c[keysize:2*keysize]) / keysize +
        crypto.hamming_dist(c[keysize:2*keysize], c[2*keysize:3*keysize]) / keysize +
        crypto.hamming_dist(c[2*keysize:3*keysize], c[3*keysize:4*keysize]) / keysize +
        crypto.hamming_dist(c[3*keysize:4*keysize], c[4*keysize:5*keysize]) / keysize
    ))
keysizes.sort(key=lambda a: a[1])

def decrypt_hint_keysize(c: bytes, keysize: int) -> bytes:
    blocks = [c[i:i+keysize] for i in range(0, len(c), keysize)]

    # Transpose the blocks so we have blocks that were entirely XORed with a single character.
    transposed_blocks = [bytearray() for _ in range(keysize)]
    for block in blocks:
        for i in range(keysize):
            if i < len(block):
                transposed_blocks[i].append(block[i])

    key = bytearray()
    for block in transposed_blocks:
        k = crypto.crack_xor(bytes(block))
        key.extend(k)
    return bytes(key)

for i in range(3):
    key = decrypt_hint_keysize(c, keysizes[i][0])
    print(f"KEY: {key}")
    print(crypto.xorcrypt(c, key).decode("latin-1"))
    print("---------------")
    print()
