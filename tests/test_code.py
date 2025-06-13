import pytest

from src.masks import get_mask_card_number, get_mask_account, mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("card_number, expected", [(7000792289606361, "7000 79** **** 6361")])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number", [(12347000792289606361)])
def test_get_mask_card_number_len(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize("card_number", [()])
def test_get_mask_card_number_letters(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize("card_number, expected", [(64686473678894779589, "**9589"),
                                                   (35383033474447895560, "**5560")])
def test_get_mask_account(card_number, expected):
    assert get_mask_account(card_number) == expected

@pytest.mark.parametrize("card_number", [(12347000792289606361),
                                         (123412347000792289606361)])
def test_get_mask_account_len(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize("card_number", [("1234792289606361qwe")])
def test_get_mask_account_letters(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize("card_number, expected", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                                   ("MasterCard 7158300734726758" , "MasterCard 7158 30** **** 6758")])
def test_mask_account_card(card_number, expected):
    assert mask_account_card(card_number) == expected

@pytest.fixture
def test_mask_account_card_letters(card_type_and_number):
    with pytest.raises(FileNotFoundError):
        mask_account_card(card_type_and_number)

@pytest.mark.parametrize("numbers,expected",[("2018-06-30T02:08:58.425572", "30.06.2018"),
                                             ("2018-09-12T21:27:25.241689", "12.09.2018"),
                                             ("2018-10-14T08:21:33.419441","14.10.2018")])
def test_get_date(numbers,expected):
    assert get_date(numbers) == expected


# @pytest.mark.parametrize("my_list, expected ",[({"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}, {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}),
#                                               ({"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}, {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"})])
#
# def test_filter_by_state(my_list, expected):
#     assert filter_by_state(my_list) == expected
# @pytest.mark.parametrize("list_dicktionary,reverse, expected ", [(
#                                                                  {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#                                                                  {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#                                                                  {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}),
#
#                                                                  ({"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
# {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
# {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"})])
# def test_sort_by_date(list_dicktionary, reverse, expected):
#     assert sort_by_date(list_dicktionary) == expected
    