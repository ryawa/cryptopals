def pad_pkcs7(pt: bytes, length: int) -> bytes:
    assert length >= len(pt)
    padding = length - len(pt)
    padded = bytearray(pt)
    padded.extend([padding] * padding)
    return bytes(padded)

print(pad_pkcs7(b"YELLOW SUBMARINE", 20))
