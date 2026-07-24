import crypto

best = ("", 0)
with open("4.txt", "r") as f:
    while True:
        line = f.readline().rstrip("\n")
        if not line:
            break
        c = crypto.decode_hex(line)
        key = crypto.crack_xor(c)
        guess = crypto.xorcrypt(c, key)
        score = crypto.score(guess)
        if best[0] == "" or score > best[1]:
            best = (guess, score)
print(best[0])
