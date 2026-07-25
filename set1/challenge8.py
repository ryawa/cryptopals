import crypto


def detect_ecb(ct: bytes) -> bool:
    seen: set[bytes] = set()
    for i in range(0, len(ct), 16):
        if ct[i:i+16] in seen:
            return True
        seen.add(ct[i:i+16])
    return False

with open("8.txt", "r") as f:
    while True:
        line = f.readline().rstrip("\n")
        if not line:
            break
        ct = crypto.decode_hex(line)
        if detect_ecb(ct):
            print(crypto.encode_hex(ct))
