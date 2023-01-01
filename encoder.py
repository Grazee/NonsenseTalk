import sys
import json
import nonsense
from sys import argv


import base64


if len(argv) <= 1:
    print("Usage: \n    python3 encoder.py '''input'''")
    exit()

raw = argv[1]

## base64
enc_64 = base64.b64encode(raw.encode()).decode()
result_64 = {
    "title": enc_64,
    "subtitle": "Base64 encode",
    "arg": enc_64
}

## nosense
enc_nonsense = nonsense.encode_nosense(raw)
    
result_nosense = {
    "title": enc_nonsense,
    "subtitle": "Nonsense encode",
    "arg": enc_nonsense
}

## output
items = {"items": [
    result_64,
    result_nosense,
]}
sys.stdout.write(json.dumps(items))
