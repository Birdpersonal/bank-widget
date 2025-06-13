import re
from typing import Any


def get_mask_card_number(card_number: int) -> str:
    """принимает на вход номер карты и возвращает ее маску."""
    if len(str(card_number)) != 16:
        raise ValueError("Недопустимые символы")
    str_card_number = str(card_number)
    if str_card_number.isdigit():
        result = str_card_number[:4] + " " + str_card_number[4:6] + "**" + " " + "****" + " " + str_card_number[-4:]
    return result


def get_mask_account(account_number: int) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    if len(str(account_number)) < 20 or len(str(account_number)) > 20:
        raise ValueError("Несоответсвующее количество символов")
    str_account_number = str(account_number)
    if str_account_number.isdigit():
        result = "**" + str_account_number[-4:]
    return result


def is_cirillic(mem: str) -> bool:
    """фильтрация на русский типа карт"""
    return bool(re.search("[а-яА-Я]", mem))


def mask_account_card(card_type_and_number: Any) -> Any:
    """Функция принимает тип и номер карты возвращает с замаскированными номером"""
    card_type = ""
    number_card = ""
    for i in card_type_and_number:
        for item in i:
            if not item.isdigit():
                card_type += item
            else:
                number_card += item

    for mem in card_type:
        if is_cirillic(mem):

            return card_type + get_mask_account(int(number_card))
        else:

            return card_type + get_mask_card_number(int(number_card))


def get_date(numbers: str) -> str:
    """Функция принимает строчку и возвращает дату"""
    new_get_date = numbers[8:10] + "." + numbers[5:7] + "." + numbers[0:4]

    return new_get_date
