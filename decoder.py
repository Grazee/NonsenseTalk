import sys
import json
import base64
import base91
import nonsense

from base91 import decode


if len(sys.argv) <= 1:
    print("Usage: \n    python3 decoder.py '''input'''")
    exit()
raw = sys.argv[1]

item_list = []

## base64
try:
    dec_64 = base64.b64decode(raw).decode()
    result_64 = {
        "title": dec_64,
        "subtitle": "Base64 decode",
        "arg": dec_64
    }
    item_list.append(result_64)
except:
    pass

## base91
try:
    dec_91 = base91.decode(raw).decode()
    result_91 = {
        "title": dec_91,
        "subtitle": "Base91 decode",
        "arg": dec_91
    }
    item_list.append(result_91)
except:
    pass

## nosense
try:
    dec_nosense = nonsense.decode_nosense(raw)
    result_nosense = {
        "title": dec_nosense,
        "subtitle": "Nosense decode",
        "arg": dec_nosense
    }
    item_list.append(result_nosense)
except:
    pass

## output
if len(item_list) < 1:
    result_null = {
        "title": "No result",
        "subtitle": "All decoding failed.",
        "arg": "No result"
    }
    item_list.append(result_null)

items = {"items": item_list}
sys.stdout.write(json.dumps(items))
