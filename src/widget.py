from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card: str) -> str | None:
    """Функция возвращает строку с замаскированным счетом или номером карты"""
    cards = card.split()
    number = cards[-1]
    name = " ".join(cards[:-1])
    if name == 'Счет':
        number = get_mask_account(number)
    else:
        number = get_mask_card_number(number)
    return f"{name} {number}"









