import crypto

freq = {
    "A": 7.8,
    "B": 2.0,
    "C": 4.0,
    "D": 3.8,
    "E": 11.0,
    "F": 1.4,
    "G": 3.0,
    "H": 2.3,
    "I": 8.6,
    "J": 0.25,
    "K": 0.97,
    "L": 5.3,
    "M": 2.7,
    "N": 7.2,
    "O": 6.1,
    "P": 2.8,
    "Q": 0.19,
    "R": 7.3,
    "S": 8.7,
    "T": 6.7,
    "U": 3.3,
    "V": 1.0,
    "W": 0.91,
    "X": 0.27,
    "Y": 1.6,
    "Z": 0.44,
}

s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
b = crypto.decode_hex(s)

best = ""
best_score = 0
for i in range(256):
    guess = ""
    score = 0
    for byte in b:
        c = chr(byte ^ i)
        guess += c
        if c.upper() in freq:
            score += freq[c.upper()]
        else:
            score -= 10
    if best == "" or score > best_score:
        best = guess
        best_score = score

print(best)
