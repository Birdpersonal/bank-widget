from src.masks import get_date, mask_account_card

card_type_and_number = mask_account_card("Visa Platinum 7000792289606361")
"""Функция принимает тип и номер карты возвращает с замаскированными номером"""
print(card_type_and_number)

new_get_date = get_date("2024-03-11T02:26:18.671407")
"""Функция принимает строчку и возвращает дату"""
print(new_get_date)
