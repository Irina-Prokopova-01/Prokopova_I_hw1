from src.generators import filter_by_currency, transaction_descriptions, card_number_generator, transactions


def test_filter_by_currency():
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == 939719570
    assert next(generator) == 142264268
    assert next(generator) == 895315941


def test_transaction_descriptions():
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


def test_card_number_generator():
    generator = card_number_generator(0, 2)
    assert next(generator) == "0000 0000 0000 0000"
    assert next(generator) == "0000 0000 0000 0001"


# def test_card_number_generator1():
#     assert next(card_number_generator(0, 1)) == '0000 0000 0000 0000'
