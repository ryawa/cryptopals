import crypto

p = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal".encode("latin-1")
key = "ICE".encode("latin-1")

c = crypto.xorcrypt(p, key)
print(crypto.encode_hex(c))
