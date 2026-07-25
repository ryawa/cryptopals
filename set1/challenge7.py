import crypto

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


with open("7.txt", "r") as f:
    contents = f.read().replace("\n", "")
ciphertext = crypto.decode_base64(contents)

key = b"YELLOW SUBMARINE"
cipher = Cipher(algorithms.AES128(key), modes.ECB())
decryptor = cipher.decryptor()
plaintext = decryptor.update(ciphertext)
plaintext += decryptor.finalize()
print(plaintext)
