from src.masks import get_mask_account, get_mask_card_number

card_mask = get_mask_card_number()
"""вызывается функция, вводятся данные и готово"""
print(card_mask)

mask_account = get_mask_account()
"""вызывается функция, вводятся данные и готово"""
print(mask_account)
