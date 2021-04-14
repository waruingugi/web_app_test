import requests
import hashlib
import hmac
import json

payload = {
    "oid": "112",
    "vid": "demo",
}
res = ''.join(str(val) for key, val in payload.items())
payload = bytes(res, encoding='utf-8')

key = b'demoCHANGED'
my_hmac = hmac.new(key, payload, hashlib.sha256).hexdigest()

payload = {
    "oid": "112",
    "vid": "demo",
    "hash": my_hmac
}

response = requests.post('https://apis.ipayafrica.com/payments/v2/transaction/search', data=payload)

print(response.json()['status'])
