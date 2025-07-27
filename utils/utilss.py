import json
import logging
import os

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s:%(filename)s:%(levelname)s:%(message)s",
    encoding="utf-8",
    filename="C:/Users/user/PycharmProjects/bank_widget/logs/utilss.log",
    filemode="w",
)

logger = logging.getLogger()


def road_to_json(path: str) -> list[dict]:
    """Принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях"""
    logging.info("Начало работы road_to_json")
    if not os.path.isfile(path):
        logging.info("проверка JSON-файла")
        return []
    try:
        with open(path, encoding="utf-8") as file:
            data = json.load(file)
            logging.info("Чтение файла")
            return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        logging.error("Ошибка декодирования файла")
        return []
