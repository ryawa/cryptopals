import secrets
from typing import Callable

import crypto

UNKNOWN_STRING = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"

def _encryption_oracle(pt: bytes, key: bytes) -> bytes:
    pt = pt + crypto.decode_base64(UNKNOWN_STRING)
    pt = crypto.pad_pkcs7(pt, 16)
    ct = crypto.aes.encrypt_ecb(pt, key)
    return ct

key = secrets.token_bytes(16)
encryption_oracle: Callable[[bytes], bytes] = lambda pt: _encryption_oracle(pt, key)

ct0 = encryption_oracle(b"")
block_size = 1
while True:
    cti = encryption_oracle(b"A" * block_size)
    if ct0[:block_size] == cti[block_size:2*block_size]:
        break
    block_size += 1
print(f"{block_size=}")
print()

recovered = bytearray()
recovered_block = bytearray()
prev_recovered_block = bytearray(b"A" * block_size)
lookup: dict[bytes, bytes] = {}
for i in range(0, len(ct0), block_size):
    for probe_len in range(block_size - 1, -1, -1):
        ct_block = encryption_oracle(b"A" * probe_len)[i:i+block_size]
        for guess in range(256):
            k = prev_recovered_block[block_size-probe_len:] + recovered_block + bytes([guess])
            lookup[
                encryption_oracle(bytes(k))[:block_size]
            ] = bytes([guess])
        if ct_block not in lookup:
            # Hit padding
            break
        recovered_block.extend(lookup[ct_block])
    recovered.extend(recovered_block)
    prev_recovered_block = recovered_block
    recovered_block = bytearray()

print(recovered.decode("latin-1"))
