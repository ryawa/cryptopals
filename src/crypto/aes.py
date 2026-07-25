from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from .xor import xorcrypt


# TODO: rewrite this from scratch
def decrypt_ebc(ct: bytes, key: bytes) -> bytes:
    cipher = Cipher(algorithms.AES128(key), modes.ECB())
    decryptor = cipher.decryptor()
    pt = decryptor.update(ct)
    pt += decryptor.finalize()
    return pt

def encrypt_ebc(pt: bytes, key: bytes) -> bytes:
    cipher = Cipher(algorithms.AES128(key), modes.ECB())
    encryptor = cipher.encryptor()
    ct = encryptor.update(pt)
    ct += encryptor.finalize()
    return ct

def decrypt_cbc(ct: bytes, key: bytes, iv: bytes) -> bytes:
    assert len(ct) % 16 == 0

    pt = bytearray()
    for i in range(0, len(ct), 16):
        pt_block = decrypt_ebc(ct[i:i+16], key)
        if i == 0:
            prev_ct_block = iv
        else:
            prev_ct_block = bytes(ct[i-16:i])
        pt.extend(xorcrypt(pt_block, prev_ct_block))
    return bytes(pt)

def encrypt_cbc(pt: bytes, key: bytes, iv: bytes) -> bytes:
    assert len(pt) % 16 == 0

    ct = bytearray()
    for i in range(0, len(pt), 16):
        if i == 0:
            prev_ct_block = iv
        else:
            prev_ct_block = bytes(ct[i-16:i])
        pt_block = xorcrypt(pt[i:i+16], prev_ct_block)
        ct.extend(encrypt_ebc(pt_block, key))
    return bytes(ct)
