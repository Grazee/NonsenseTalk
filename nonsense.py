import base91
from random import randint

def encode_nosense(text):

    empty_chars = [0, 1, 2, 3, 4, 5, 6, 7, 14, 15, 16, 17, 18, 19, 20,21,22,23,24,25,28,29,30,31]
    for i in range(len(text) * 2):
        r = randint(0, len(text))
        rc = empty_chars[randint(0, len(empty_chars) - 1)]
        text = text[:r] + chr(rc) + text[r:]

    return base91.encode(text.encode())
    
def decode_nosense(text):
    empty_chars = [0, 1, 2, 3, 4, 5, 6, 7, 14, 15, 16, 17, 18, 19, 20,21,22,23,24,25,28,29,30,31]

    a = base91.decode(text).decode()
    plain = ''
    for i in a:
        if ord(i) not in empty_chars:
            plain += i

    return plain
