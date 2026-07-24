import crypto

s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
b = crypto.decode_hex(s)
key = crypto.crack_xor(b)
print(crypto.xorcrypt(b, key))
