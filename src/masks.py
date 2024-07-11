import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("../logs/masks.log", encoding="utf8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str | None:
    logger.info(f'Передан номер карты: {card_number}.')
    if type(card_number) is not str:
        logger.error(f'Передан не корректный тип данных.')
        raise TypeError
    """Функция маскирующая номер карты"""
    if card_number.isdigit() and len(card_number) == 16:
        logger.warning(f'Введеный номер должен состоять из 16 цифр')
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
        logger.debug(f'Замаскированный номер карты: {masked_number}.')
        return masked_number
    return None


def get_mask_account(bank_account: str) -> str | None:
    logger.info(f"Передан номер счета: {bank_account}.")
    if type(bank_account) is not str:
        logger.error(f"Передан не корректный тип данных.")
        raise TypeError
    """Функция маскирующая номер счета"""
    if bank_account.isdigit() and len(bank_account) == 20:
        logger.warning(f"Введеный номер должен состоять из 20 цифр")
        masked_number = f"**{bank_account[-4::]}"
        logger.debug(f"Замаскированный номер карты: {masked_number}.")
        return masked_number
    else:
        return None
