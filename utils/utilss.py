import json
import os


def road_to_json(path: str) -> list[dict]:
    """Принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях"""
    if not os.path.isfile(path):
        return []
    try:
        with open(path, encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []


if __name__ == "__main__":
    lol = road_to_json("data/operations.json")
    print(lol)
