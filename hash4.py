import requests
#Import libraries
import hashlib
import hmac
import json

payload = {
    "live": 0,
    "oid": "112",
    "inv": "112020102292999",
    "ttl": 900,
    "tel": "256712375678",
    "eml": "kajuej@gmailo.com",
    "vid": "demo",
    "curr": "KES",
    "p1": "airtel",
    "p2": "020102292999",
    "p3": "",
    "p4": "900",
    "cbk": "https://",
    "cst": 1,
    "crl": 2,
}

res = ''.join(str(val) for key, val in payload.items())
payload = bytes(res, encoding='utf-8')
print(payload)

key = b'demoCHANGED'
my_hmac = hmac.new(key, payload, hashlib.sha1).hexdigest()

payload = {
    "live": 0,
    "oid": "112",
    "inv": "112020102292999",
    "ttl": 900,
    "tel": "256712375678",
    "eml": "kajuej@gmailo.com",
    "vid": "demo",
    "curr": "KES",
    "p1": "airtel",
    "p2": "020102292999",
    "p3": "",
    "p4": "900",
    "cbk": "https://",
    "cst": 1,
    "crl": 2,
    "hsh": my_hmac
}


response = requests.post('https://payments.ipayafrica.com/v3/ke', data=payload)
print(response.text)