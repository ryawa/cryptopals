from .utils import score as score_fn

def xorcrypt(input: bytes, key: bytes) -> bytes:
    result = bytearray()
    for i in range(len(input)):
        result.append(input[i] ^ key[i % len(key)])
    return bytes(result)

def crack_xor(b: bytes) -> bytes:
    # key, score
    best = (None, 0)
    for key in range(256):
        # Need [] to prevent bytes(0) from being empty
        key = bytes([key])
        guess = xorcrypt(b, key)
        score = score_fn(guess)
        if best[0] == None or score > best[1]:
            best = (key, score)
    # The best key can never be None
    assert best[0]
    return best[0]
