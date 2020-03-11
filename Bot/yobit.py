# создает запрос на биржу биткоинов и получает ответ

import requests


def get_btc():
    url = "https://yobit.net/api/2/bts_usd/ticker"
    response = requests.get(url).json()
    price = response["ticker"]["last"]
    return str(price) + " usd"





