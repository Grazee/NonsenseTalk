from sys import argv
from base91 import decode


if len(argv) <= 1:
    print("Usage: \n    python3 decoder.py '''input'''")
    exit()

raw = argv[1]
empty_chars = [0, 1, 2, 3, 4, 5, 6, 7, 14, 15, 16, 17, 18, 19, 20,21,22,23,24,25,28,29,30,31]

a = decode(raw).decode()
plain = ''
for i in a:
    if ord(i) not in empty_chars:
        plain += i
print(plain)
