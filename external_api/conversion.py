import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")


def conversion_currency(transaction: dict) -> float:
    """принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    url = "https://api.apilayer.com/exchangerates_data/convert"
    get_amount = transaction["operationAmount"]["amount"]
    get_currency = transaction["operationAmount"]["currency"]["code"]

    params = {"to": "RUB", "from": get_currency, "amount": get_amount}
    headers = {"apikey": API_KEY}
    if get_currency == "RUB":
        return float(get_amount)
    response = requests.get(url, params=params, headers=headers)
    result = response.json()["result"]
    print(response.text)
    return float(round(result, 2))
