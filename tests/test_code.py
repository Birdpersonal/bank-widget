import pytest

from src.masks import get_date, get_mask_account, get_mask_card_number, mask_account_card


@pytest.mark.parametrize("card_number, expected", [(7000792289606361, "7000 79** **** 6361")])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number", [12347000792289606361])
def test_get_mask_card_number_len(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize("card_number", [()])
def test_get_mask_card_number_letters(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize("card_number, expected", [(64686473678894779589, "**9589"), (35383033474447895560, "**5560")])
def test_get_mask_account(card_number, expected):
    assert get_mask_account(card_number) == expected


@pytest.mark.parametrize("card_number", [(12347000792289606361), (123412347000792289606361)])
def test_get_mask_account_len(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize("card_number", ["1234792289606361qwe"])
def test_get_mask_account_letters(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ],
)
def test_mask_account_card(card_number, expected):
    assert mask_account_card(card_number) == expected


@pytest.fixture
def test_mask_account_card_letters(card_type_and_number):
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
def test_get_date(numbers, expected):
    assert get_date(numbers) == expected
