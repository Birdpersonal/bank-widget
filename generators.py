import random
from typing import Any, Generator, Iterator


def filter_by_currency(transactions: Any, currency: str = "USD") -> Iterator[dict]:
    """функция принимает список словарей и валюту, выдает список отфильтрованых транзакций"""
    for x in transactions:
        if x["operationAmount"]["currency"]["code"] != currency:
            raise FileNotFoundError("Нет операций по данной валюте")
        if x["operationAmount"]["currency"]["code"] == currency:
            yield x


result = filter_by_currency(
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]
)

print(*result)


def transaction_descriptions(transactions: list) -> Any:
    """функция принимает список словарей и возвращает типы операций"""
    gen_descriptions = (x["description"] for x in transactions)
    yield gen_descriptions


descriptions = transaction_descriptions(
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]
)
print(next(*descriptions))


def card_number_generator(start: int = 1, stop: int = 9999999999999999) -> Generator:
    """функция принимает стартовое и конечное значиение,
     выдает рандомный номер карты по указаному диапазону"""
    number = str(random.randint(start, stop))

    while len(number) < 16:
        number = "0" + number

    formatted_number = " ".join([number[i : i + 4] for i in range(0, len(number), 4)])
    yield formatted_number


for card_number in card_number_generator(12, 4896):
    print(list(card_number))
