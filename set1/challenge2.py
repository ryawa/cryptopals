import crypto

s1 = "1c0111001f010100061a024b53535009181c"
s2 = "686974207468652062756c6c277320657965"
b1 = crypto.decode_hex(s1)
b2 = crypto.decode_hex(s2)
res = bytearray()
for i in range(len(b1)):
    res.append(b1[i] ^ b2[i])
print(crypto.encode_hex(bytes(res)))
