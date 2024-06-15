from src.masks import get_mask_card_number, get_mask_account

# from typing import Optional


def mask_account_card(card: str) -> str:
    """Функция возвращает строку с замаскированным счетом или номером карты"""
    cards = card.split()
    number = cards[-1]
    name = " ".join(cards[:-1])
    if name != 'Счет':
        number = get_mask_card_number(number)
    else:
        number = get_mask_account(number)
    return f"{name} {number}"


# print(mask_account_card("Maestro 1596837868705199"))


def get_data(date: str) -> str | None:
    """Функция преобразования даты"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
