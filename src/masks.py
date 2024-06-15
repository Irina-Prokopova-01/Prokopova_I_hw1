def get_mask_card_number(card_number: str) -> str | None:
    """Функция маскирующая номер карты"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:5]} {card_number[5:7]} ** **** {card_number[12:]}"
    return None


def get_mask_account(bank_account: str) -> str | None:
    """Функция маскирующая номер счета"""
    if bank_account.isdigit() and len(bank_account) == 20:
        return f"**{bank_account[-4::]}"
    else:
        return None
