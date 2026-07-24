__all__ = ["decode_hex", "encode_base64"]

# Equivalent to bytes.fromhex()
def decode_hex(hex_str: str) -> bytes:
    if len(hex_str) % 2 != 0:
        raise ValueError("Input must have even length")

    digits = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
    }
    result = bytearray()
    for i in range(0, len(hex_str) - 1, 2):
        result.append(digits[hex_str[i]]*16 + digits[hex_str[i+1]])
    return bytes(result)

# Encode bytes to base64 string without padding
def encode_base64(b: bytes) -> str:
    result = ""
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    for i in range(0, len(b), 3):
        chunk = b[i:i+3]
        # If len(b) is not a multiple of 3, add either 1 or 2 bytes of padding to get 3 bytes for the last chunk
        padding_len = max(0, i+3 - len(b))
        chunk += padding_len * b'\x00'
        chunk = int.from_bytes(chunk, "big")
        result += digits[(chunk >> 18) & 0b111111]
        result += digits[(chunk >> 12) & 0b111111]
        if padding_len <= 1:
            result += digits[(chunk >>  6) & 0b111111]
        if padding_len == 0:
            result += digits[(chunk >>  0) & 0b111111]
    return result
