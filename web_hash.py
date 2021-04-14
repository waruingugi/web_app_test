
import requests
#Import libraries
import hashlib
import hmac
import json

payload = {
    "vid": "demo",
    "sid":"SOMDEM315771615239383186100633DEMO",
}

res = ''.join(str(val) for key, val in payload.items())
payload = bytes(res, encoding='utf-8')
print(payload)

key = b'demoCHANGED'
my_hmac = hmac.new(key, payload, hashlib.sha256).hexdigest()
print(my_hmac)

payload = {
    "vid": "demo",
    "sid":"SOMDEM315771615239383186100633DEMO",
    "hash": my_hmac
}


response = requests.post('https://apis.ipayafrica.com/payments/v2/transact/mobilemoney', data=payload)
print(response.text)