from src.masks import get_date, mask_account_card

card_type_and_number = mask_account_card()
"""Функция принимает тип и номер карты возвращает с замаскированными номером"""
print(card_type_and_number)

new_get_date = get_date()
"""Функция принимает строчку и возвращает дату"""
print(new_get_date)
