from sys import argv
from base91 import encode
from random import randint


if len(argv) <= 1:
    print("Usage: \n    python3 encoder.py '''input'''")
    exit()

text = argv[1]

empty_chars = [0, 1, 2, 3, 4, 5, 6, 7, 14, 15, 16, 17, 18, 19, 20,21,22,23,24,25,28,29,30,31]
for i in range(len(text) * 2):
    r = randint(0, len(text))
    rc = empty_chars[randint(0, len(empty_chars) - 1)]
    text = text[:r] + chr(rc) + text[r:]

raw = encode(text.encode())
print(raw)
