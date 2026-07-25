from math import ceil


# From https://www.maltron.com/character-usage-by-percentage.html
LETTER_FREQ: dict[str, float] = {
    " ": 0.17460,
    "e": 0.09781,
    "E": 0.00053,
    "t": 0.06819,
    "T": 0.00285,
    "a": 0.06207,
    "A": 0.00180,
    "o": 0.05686,
    "O": 0.00058,
    "n": 0.05304,
    "N": 0.00077,
    "h": 0.04898,
    "H": 0.00205,
    "i": 0.04761,
    "I": 0.00298,
    "s": 0.04630,
    "S": 0.00212,
    "r": 0.04472,
    "R": 0.00057,
    "d": 0.03694,
    "D": 0.00064,
    "l": 0.03251,
    "L": 0.00053,
    "u": 0.02212,
    "U": 0.00016,
    "c": 0.01772,
    "C": 0.00099,
    "m": 0.01735,
    "M": 0.00127,
    "w": 0.01687,
    "W": 0.00103,
    "g": 0.01632,
    "G": 0.00066,
    "f": 0.01541,
    "F": 0.00065,
    "y": 0.01418,
    "Y": 0.00058,
    "p": 0.01241,
    "P": 0.00051,
    "b": 0.01107,
    "B": 0.00140,
    ",": 0.01211,
    "<": 0.00001,
    ".": 0.01192,
    ">": 0.00001,
    "k": 0.00781,
    "K": 0.00044,
    "2": 0.00005,
    "\"": 0.00753,
    "v": 0.00681,
    "V": 0.00020,
    "\n": 0.00446,
    "'": 0.00235,
    "@": 0.00000,
    "j": 0.00093,
    "J": 0.00024,
    "/": 0.00001,
    "?": 0.00109,
    "z": 0.00105,
    "Z": 0.00004,
    "x": 0.00102,
    "X": 0.00001,
    "-": 0.00062,
    "_": 0.00028,
    "q": 0.00058,
    "Q": 0.00004,
    "1": 0.00005,
    "!": 0.00052,
    ";": 0.00043,
    ":": 0.00009,
    "0": 0.00005,
    ")": 0.00005,
    "9": 0.00001,
    "(": 0.00005,
    "8": 0.00001,
    "*": 0.00006,
    "5": 0.00003,
    "%": 0.00000,
    "3": 0.00003,
    "£": 0.00000,
    "4": 0.00002,
    "$": 0.00000,
    "7": 0.00001,
    "&": 0.00000,
    "^": 0.00001,
    "#": 0.00000,
    "~": 0.00000,
    "=": 0.00000,
    "+": 0.00000,
    "]": 0.00000,
    "}": 0.00000,
    "[": 0.00000,
    "{": 0.00000,
    "\\": 0.00000,
    "|": 0.00000,
    "`": 0.00000,
    "¬": 0.00000,
}

# Bhattacharyya coefficient = Σ_x sqrt(P(x)Q(x))
# See more at https://en.wikipedia.org/wiki/Bhattacharyya_distance
def score(s: bytes, freq: dict[str, float]=LETTER_FREQ) -> float:
    text_freq: dict[str, int] = {}
    for c in s.decode("latin-1"):
        text_freq[c] = text_freq.setdefault(c, 0) + 1
    total = sum(text_freq.values())
    result = 0.0
    for k in text_freq:
        result += (text_freq[k]/total * freq.get(k, 0.0))**0.5
    return result

def hamming_dist(a: bytes, b: bytes) -> int:
    assert len(a) == len(b)
    dist = 0
    for i in range(len(a)):
        dist += (a[i] ^ b[i]).bit_count()
    return dist

def pad_pkcs7(pt: bytes, block_size: int) -> bytes:
    padding = ceil(len(pt) / block_size)*block_size - len(pt)
    padded = bytearray(pt)
    padded.extend([padding] * padding)
    return bytes(padded)
