import re


def get_mask_card_number(card_number: int) -> str:
    """принимает на вход номер карты и возвращает ее маску."""
    str_card_number = str(card_number)
    return str_card_number[:4] + " " + str_card_number[4:6] + "**" + " " + "****" + " " + str_card_number[-4:]


# print(get_mask_card_number())


def get_mask_account(account_number: int) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    str_account_number = str(account_number)
    result = "**" + str_account_number[-4:]
    return result


# print(get_mask_account())

def is_cirillic(mem: str) -> bool:
    """фильтрация на русский типа карт"""
    return bool(re.search("[а-яА-Я]", mem))


def mask_account_card(card_type_and_number: str) -> str:
    """Функция принимает тип и номер карты возвращает с замаскированными номером"""
    card_type = ""
    number_card = ""
    for i in card_type_and_number:
        for item in i:
            if not item.isdigit():
                card_type += item
            else:
                number_card += item
    new_card_type = ""
    for mem in card_type:
        if  is_cirillic(mem):

            return card_type + get_mask_account(number_card)
        else:

            return card_type + get_mask_card_number(number_card)


def get_date(numbers: str) -> str:
    """Функция принимает строчку и возвращает дату"""
    new_get_date = numbers[8:10]+numbers[4:8]+numbers[0:4]

    return new_get_date

