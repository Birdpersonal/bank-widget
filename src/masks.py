import logging
import re
from typing import Any

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s:%(filename)s:%(levelname)s:%(message)s",
    encoding="utf-8",
    filename="C:/Users/user/PycharmProjects/bank_widget/logs/masks.log",
    filemode="w",
)

logger = logging.getLogger()


def get_mask_card_number(card_number: int) -> str:
    """принимает на вход номер карты и возвращает ее маску."""
    logging.info("Старт функции get_mask_card_number")
    if len(str(card_number)) != 16:
        raise ValueError("Недопустимые символы")
    logging.error("Недопустимые символы")
    str_card_number = str(card_number)
    if str_card_number.isdigit():
        result = str_card_number[:4] + " " + str_card_number[4:6] + "**" + " " + "****" + " " + str_card_number[-4:]
        logging.info("приведение номера карты к необходимому формату")
    return result


if __name__ == "__main__":
    get_mask_card_number(7000792289606361)


def get_mask_account(account_number: int) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    logging.info("Старт функции get_mask_account")
    if len(str(account_number)) < 20 or len(str(account_number)) > 20:
        raise ValueError("Несоответсвующее количество символов")
    logging.error("Несоответсвующее количество символов")
    str_account_number = str(account_number)
    if str_account_number.isdigit():
        result = "**" + str_account_number[-4:]
        logging.info("приведение счета к необходимому формату")
    return result


if __name__ == "__main__":
    get_mask_account(64686473678894779589)


def is_cirillic(mem: str) -> bool:
    """фильтрация на русский типа карт"""
    logging.info("Старт функции get_mask_account")
    return bool(re.search("[а-яА-Я]", mem))


def mask_account_card(card_type_and_number: Any) -> Any:
    """Функция принимает тип и номер карты возвращает с замаскированными номером"""
    logging.info("Старт функции mask_account_card")
    card_type = ""
    number_card = ""
    for i in card_type_and_number:
        for item in i:
            if not item.isdigit():
                card_type += item
                logging.info("запись типа продукта")
            else:
                number_card += item
                logging.info("запись номера продукта")

    for mem in card_type:
        logging.info("условие на выбор карты или счета ")
        if is_cirillic(mem):
            logging.info("номер счета")
            return card_type + get_mask_account(int(number_card))

        else:
            logging.info("номер карты")

            return card_type + get_mask_card_number(int(number_card))


def get_date(numbers: str) -> str:
    """Функция принимает строчку и возвращает дату"""
    logging.info("начало работы get_date")
    new_get_date = numbers[8:10] + "." + numbers[5:7] + "." + numbers[0:4]
    logging.info("приведение времени и даты к нужному формату")

    return new_get_date
