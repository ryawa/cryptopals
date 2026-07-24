from crypto.codec import encode_hex

p = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal".encode("ascii")
key = "ICE".encode("ascii")

def encrypt(p: bytes, k: bytes) -> bytes:
    result = bytearray()
    for i in range(len(p)):
        result.append(p[i] ^ k[i % len(k)])
    return bytes(result)

c = encrypt(p, key)
print(encode_hex(c))
