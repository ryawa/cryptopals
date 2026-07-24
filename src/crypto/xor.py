from .utils import score as score_fn

def xorcrypt(input: bytes, key: bytes) -> bytes:
    result = bytearray()
    for i in range(len(input)):
        result.append(input[i] ^ key[i % len(key)])
    return bytes(result)

def crack_xor(b: bytes) -> tuple[bytes, int]:
    best = b""
    best_key = -1
    best_score = 0
    for i in range(256):
        guess = bytearray()
        for byte in b:
            c = byte ^ i
            guess.append(c)
        guess = bytes(guess)
        score = score_fn(guess)
        if best == b"" or score > best_score:
            best = guess
            best_key = i
            best_score = score
    return best, best_key
