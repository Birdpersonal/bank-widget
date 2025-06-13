def filter_by_state(list_dick: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей. Возвращает новый список,
    содержащий только те словари, у которых ключ state соответствует указанному значению"""
    new_list = []
    for i in list_dick:
        if i[state] == state:
            new_list.append(i)
        else:
            continue
    return new_list


def sort_by_date(list_dicktionary: list, reverse: bool = True) -> list:
    """Функция принимает список словарей, возвращать новый список, отсортированный по дате"""
    if reverse:
        return sorted(list_dicktionary, key=lambda x: x["date"], reverse=True)
    else:
        return sorted(list_dicktionary, key=lambda x: x["date"], reverse=False)
