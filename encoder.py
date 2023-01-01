import sys
import json
import nonsense
import base64
import base91
import urllib.parse


if len(sys.argv) <= 1:
    print("Usage: \n    python3 encoder.py '''input'''")
    exit()

raw = sys.argv[1]

## base64
enc_64 = base64.b64encode(raw.encode()).decode()
result_64 = {
    "title": enc_64,
    "subtitle": "Base64 encode",
    "arg": enc_64
}

## url encode
enc_url = urllib.parse.quote(raw)
result_url = {
    "title": enc_url,
    "subtitle": "URL encode",
    "arg": enc_url
}

## base91
enc_91 = base91.encode(raw.encode())
result_91 = {
    "title": enc_91,
    "subtitle": "Base91 encode",
    "arg": enc_91
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
    result_url,    
    result_64,
    result_91,
    result_nosense,
]}
sys.stdout.write(json.dumps(items))
