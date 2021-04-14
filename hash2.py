import requests
#Import libraries
import hashlib
import hmac
import json

payload = {
    "live": 0,
	"oid": "some-fictitious-id1",
	"inv": "some-fictitious-in1",
	"amount": 100,
    "tel": "254704845041",
    "eml": "test@gmail.com",
	"vid":"demo",
	"curr": "KES"
}

res = ''.join(str(val) for key, val in payload.items())
payload = bytes(res, encoding='utf-8')
print(payload)

key = b'demoCHANGED'
my_hmac = hmac.new(key, payload, hashlib.sha256).hexdigest()
print(my_hmac)

payload = {
    "live": 0,
	"oid": "some-fictitious-id1",
	"inv": "some-fictitious-in1",
	"amount": 100,
    "tel": "254704845041",
    "eml": "test@gmail.com",
	"vid":"demo",
	"curr": "KES",
    "hash": my_hmac
}


response = requests.post('https://apis.ipayafrica.com/payments/v2/transact', data=payload)
print(response.text)