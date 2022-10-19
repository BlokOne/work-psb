import json
from typing import Dict

import requests


def auth(price, order_id):
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjY4NCwiZXhwIjo4ODA2NTkyNzc2MX0.LtQT8iM90TthBllEY9ujte58k_uRwTs_vTIvLO0r99s"
    headers = {'Content-type': 'application/json',
               'Accept': 'application/json', 'authorization': f'Token {token}'}
    params = {"shop_id": "Hz7LH3DF6ddE1WuU", "amount": price, 'order_id': order_id}
    response = requests.post(url="https://api.cryptocloud.plus/v1/invoice/create", json=params, headers=headers)
    data = response.json()
    return data['pay_url']
