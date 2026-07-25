import crypto

with open("10.txt", "r") as f:
    contents = f.read().replace("\n", "")

ct = crypto.decode_base64(contents)
pt = crypto.aes.decrypt_cbc(ct, b"YELLOW SUBMARINE", b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
print(pt.decode("latin-1"))
