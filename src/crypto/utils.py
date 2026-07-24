from math import log10

# From https://en.wikipedia.org/wiki/Letter_frequency
LETTER_FREQ = {
    "A": 8.2,
    "B": 1.5,
    "C": 2.8,
    "D": 4.3,
    "E": 12.7,
    "F": 2.2,
    "G": 2.0,
    "H": 6.1,
    "I": 7.0,
    "J": 0.16,
    "K": 0.77,
    "L": 4.0,
    "M": 2.4,
    "N": 6.7,
    "O": 7.5,
    "P": 1.9,
    "Q": 0.12,
    "R": 6.0,
    "S": 6.3,
    "T": 9.1,
    "U": 2.8,
    "V": 0.98,
    "W": 2.4,
    "X": 0.15,
    "Y": 2.0,
    "Z": 0.074,
}

def score(s: bytes, freq: dict[str, float]=LETTER_FREQ, penalty: float=-1):
    result = 0
    for c in s.decode("latin-1"):
        result += log10(freq.get(c.upper(), 10**penalty))
    return result

def hamming_dist(a: bytes, b: bytes) -> int:
    assert len(a) == len(b)
    dist = 0
    for i in range(len(a)):
        dist += (a[i] ^ b[i]).bit_count()
    return dist

