HEX_DIGITS = "0123456789abcdef"
BASE64_DIGITS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# Equivalent to bytes.fromhex()
def decode_hex(hex_str: str) -> bytes:
    if len(hex_str) % 2 != 0:
        raise ValueError("Input must have even length")
    lookup = { char: digit for digit, char in enumerate(HEX_DIGITS) }
    result = bytearray()
    for i in range(0, len(hex_str), 2):
        result.append(lookup[hex_str[i]]*16 + lookup[hex_str[i+1]])
    return bytes(result)

def encode_hex(b: bytes) -> str:
    result = ""
    for byte in b:
        d1 = (byte >> 4) & 0b1111
        d2 = (byte >> 0) & 0b1111
        result += HEX_DIGITS[d1] + HEX_DIGITS[d2]
    return result

def decode_base64(base64_str: str) -> bytes:
    lookup = { char: digit for digit, char in enumerate(BASE64_DIGITS) }
    lookup["="] = 0
    result = bytearray()
    for i in range(0, len(base64_str), 4):
        chunk  = lookup[base64_str[i + 0]] << 18
        chunk += lookup[base64_str[i + 1]] << 12
        chunk += lookup[base64_str[i + 2]] << 6
        chunk += lookup[base64_str[i + 3]] << 0
        num_bytes = 3
        if base64_str[i + 2] == "=":
            num_bytes -= 1
            chunk >>= 8
        if base64_str[i + 3] == "=":
            num_bytes -= 1
            chunk >>= 8
        result.extend(chunk.to_bytes(num_bytes, "big"))
    return bytes(result)

# Encode bytes to base64 string
def encode_base64(b: bytes) -> str:
    result = ""
    for i in range(0, len(b), 3):
        chunk = b[i:i+3]
        # If len(b) is not a multiple of 3, add either 1 or 2 bytes of padding to get 3 bytes for the last chunk
        padding_len = max(0, i+3 - len(b))
        chunk += padding_len * b'\x00'
        chunk = int.from_bytes(chunk, "big")
        result += BASE64_DIGITS[(chunk >> 18) & 0b111111]
        result += BASE64_DIGITS[(chunk >> 12) & 0b111111]
        if padding_len <= 1:
            result += BASE64_DIGITS[(chunk >>  6) & 0b111111]
        if padding_len == 0:
            result += BASE64_DIGITS[(chunk >>  0) & 0b111111]
        result += "=" * padding_len
    return result
