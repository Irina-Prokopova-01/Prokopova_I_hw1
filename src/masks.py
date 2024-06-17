def get_mask_card_number(card_number: str) -> str | None:
    if type(card_number) != str:
        raise TypeError
    """Функция маскирующая номер карты"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return None

# print(get_mask_card_number('7000792289606361'))


def get_mask_account(bank_account: str) -> str | None:
    if type(bank_account) != str:
        raise TypeError
    """Функция маскирующая номер счета"""
    if bank_account.isdigit() and len(bank_account) == 20:
        return f"**{bank_account[-4::]}"
    else:
        return None
