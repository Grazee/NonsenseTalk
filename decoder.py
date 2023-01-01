import sys
import json
import base64
from sys import argv
from base91 import decode


if len(argv) <= 1:
    print("Usage: \n    python3 decoder.py '''input'''")
    exit()
raw = argv[1]

## base64
dec_64 = base64.b64decode(raw).decode()
result_64 = {
    "title": dec_64,
    "subtitle": "Base64 decode",
    "arg": dec_64
}

## nosense

result91 = {
    "title": plain,
    "subtitle": "Nonsense decode",
    "arg": plain
}

## output
items = {"items": [
    result_64
    # result91
]}

sys.stdout.write(json.dumps(items))
