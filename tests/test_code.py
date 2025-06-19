import pytest
from mypy.types import AnyType

from generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_date, get_mask_account, get_mask_card_number, mask_account_card


@pytest.mark.parametrize("card_number, expected", [(7000792289606361, "7000 79** **** 6361")])
def test_get_mask_card_number(card_number: int, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number", [12347000792289606361])
def test_get_mask_card_number_len(card_number: int) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize("card_number", [()])
def test_get_mask_card_number_letters(card_number: int) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize("card_number, expected", [(64686473678894779589, "**9589"), (35383033474447895560, "**5560")])
def test_get_mask_account(card_number: int, expected: str) ->None:
    assert get_mask_account(card_number) == expected


@pytest.mark.parametrize("card_number", [(12347000792289606361), (123412347000792289606361)])
def test_get_mask_account_len(card_number: int) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize("card_number", ["1234792289606361qwe"])
def test_get_mask_account_letters(card_number: int) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ],
)
def test_mask_account_card(card_number: int, expected: str) -> None:
    assert mask_account_card(card_number) == expected


@pytest.fixture
def test_mask_account_card_letters(card_type_and_number: AnyType) -> None:
    with pytest.raises(FileNotFoundError):
        mask_account_card(card_type_and_number)


@pytest.mark.parametrize(
    "numbers,expected",
    [
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ("2018-09-12T21:27:25.241689", "12.09.2018"),
        ("2018-10-14T08:21:33.419441", "14.10.2018"),
    ],
)
def test_get_date(numbers: str, expected: str) -> None:
    assert get_date(numbers) == expected


transactions_start = [
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
transactions_end = [
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


@pytest.mark.parametrize("transactions, expected", [(transactions_start, transactions_end)])
def test_filter_by_currency(transactions: list, expected: list) -> None:
    assert list(filter_by_currency(transactions)) == expected


@pytest.fixture
def test_filter_by_currency_not_currency(transactions: list) -> None:
    with pytest.raises(FileNotFoundError):
        filter_by_currency(transactions)


@pytest.fixture
def test_transaction_descriptions(transactions: list, expected: list) -> None:
    assert transaction_descriptions(transactions) == expected


@pytest.mark.parametrize(
    "start, finish, expected",
    [
        (3493341234, 3493341234, "0000 0034 9334 1234"),
        (35, 35, "0000 0000 0000 0035"),
        (0, 0, "0000 0000 0000 0000"),
        (9999999999999999, 9999999999999999, "9999 9999 9999 9999"),
    ],
)
def test_positive_card_number_generator(start: int, finish: int, expected: str) -> None:
    """Тестируем выдачу правильных номеров карт в заданном диапазоне + граничные значения"""

    card_num = card_number_generator(start, finish)

    assert next(card_num) == expected
