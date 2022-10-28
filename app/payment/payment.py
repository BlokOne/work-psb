import json
from typing import Dict

import requests


token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjY4NCwiZXhwIjo4ODA2NTkyNzc2MX0.LtQT8iM90TthBllEY9ujte58k_uRwTs_vTIvLO0r99s"
headers = {'Content-type': 'application/json',
           'Accept': 'application/json', 'authorization': f'Token {token}'}


def auth(price, order_id):    
    params = {"shop_id": "Hz7LH3DF6ddE1WuU", "amount": price, 'order_id': order_id}
    response = requests.post(url="https://api.cryptocloud.plus/v1/invoice/create", json=params, headers=headers)
    data = response.json()
    return data


def check_paid(invoice_id):
	params = {"uuid": "INV-" + str(invoice_id)}
	response = requests.get(url="https://api.cryptocloud.plus/v1/invoice/info", headers=headers, params=params)
	data = response.json()
	# return data.get("status_invoice") == "paid"
	return data.get("status_invoice") == "created"


# testing
import uuid


def test_postback():
	order_id = str(uuid.uuid4())
	price = 100
	head = {'Content-type': 'application/json', 'Accept': 'application/json'}
	params = {
		"status": "success", 
		"invoice_id": "INV-WF5I8ZR9",
		"amount": 100,
		"currency": "USDT",
		"order_id": order_id,
		"token": str(uuid.uuid4())
	}
	response = requests.get(url="http://127.0.0.1:8000/payments/success/", params=params, headers=head)
	data = response.json()
	return data


if __name__ == '__main__':
	print(test_postback())
	#print(auth(10, str(uuid.uuid4())))
