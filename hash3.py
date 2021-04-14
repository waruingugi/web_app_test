import requests
#Import libraries
import hashlib
import hmac
import json

payload = {
    "sid":"SOMDEM3157716152351107143322DEMO",
    "vid":"demo",
    "cardno": 1234567812345678,
    "cvv": "0000",
    "month": 12,
    "year": 2022,
    "cust_address": "NGONG",
    "cust_city": "NGONG",
    "cust_country": "KENYA",
    "cust_postcode": "NGONG",
    "cust_stateprov": "NGONG",
    "fname": "WARUI",
    "lname": "NGUGI"
}
res = ''.join(str(val) for key, val in payload.items())
payload = bytes(res, encoding='utf-8')
print(payload)

key = b"demoCHANGED"
my_hmac = hmac.new(key, payload, hashlib.sha256).hexdigest()
print(my_hmac)

payload = {
	"sid":"SOMDEM3157716152351107143322DEMO",
    "vid":"demo",
    "cardno": 1234567812345678,
    "cvv": "0000",
    "month": 12,
    "year": 2022,
    "cust_address": "NGONG",
    "cust_city": "NGONG",
    "cust_country": "KENYA",
    "cust_postcode": "NGONG",
    "cust_stateprov": "NGONG",
    "fname": "WARUI",
    "lname": "NGUGI",
    "hash": "7a980251920eb40a9d245deca31657f815438d5be603746a511a5295667ff1dd"
}

response = requests.post('https://apis.ipayafrica.com/payments/v2/transact/cc', data=payload)
print(response.text)
