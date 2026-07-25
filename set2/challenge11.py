import random
import secrets

import crypto


def encryption_oracle(pt: bytes) -> bytes:
    key = secrets.token_bytes(16)

    prefix_len = random.randint(5, 10)
    prefix = secrets.token_bytes(prefix_len)
    suffix_len = random.randint(5, 10)
    suffix = secrets.token_bytes(suffix_len)
    pt = prefix + pt + suffix
    pt = crypto.pad_pkcs7(pt, 16)

    if random.random() < 0.5:
        ct = crypto.aes.encrypt_ecb(pt, key)
    else:
        iv = secrets.token_bytes(16)
        ct = crypto.aes.encrypt_cbc(pt, key, iv)
    return ct


def detect_ecb(ct: bytes) -> bool:
    seen: set[bytes] = set()
    for i in range(0, len(ct), 16):
        if ct[i:i+16] in seen:
            return True
        seen.add(ct[i:i+16])
    return False

while True:
    ct = encryption_oracle(b"A" * 48)
    print(f"{"ECB" if detect_ecb(ct) else "CBC"}")
