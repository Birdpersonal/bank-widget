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
