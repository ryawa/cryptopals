import crypto

best = ""
best_score = 0
with open("4.txt", "r") as f:
    while True:
        s = f.readline().rstrip("\n")
        if not s:
            break
        guess, key = crypto.crack_xor(crypto.decode_hex(s))
        score = crypto.score(guess)
        if best == "" or score > best_score:
            best = guess
            best_score = score
print(best)
