import hashlib
import hmac
import json
import requests


vid = 'demo'
payload = {
    'vid': 'demo',
    'id': "112",
    'ivm': "112",
    'qwh': "628755907",
    'afd': "1442038774",
    'poi': "1183484641",
    'uyt': "676473947",
    'ifd': "676528027",
    "oid": "112",
    "inv": "112020102292999",
    "vid": "demo",
    "curr": "KES",
    "p1": "airtel",
    "p2": "020102292999",
    "p3": "",
    "p4": "900",
}

#'/callback?status=aei7p7yrx4ae34&txncd=413399979770&msisdn_id=JOHN+DOE&msisdn_idnum=0704845041&p1=airtel&p2=020102292999&p3=&p4=900&uyt=676473947&agt=1761033663&qwh=628755907&ifd=676528027&afd=1442038774&poi=1183484641&id=112&ivm=112&mc=100.00&channel=VISA'
updated_payload = ''.join('&' + str(key) + '=' + str(val) for key, val in payload.items())
url = "https://www.ipayafrica.com/ipn/?vendor=" + vid

verification_url = url + updated_payload

validation_response = requests.get(verification_url)
print(validation_response.text)