# Новый виджет для банковских операций.

## Описание:

В проекте разработана новая фича для личного кабинета клиента банка. Это виджет для удобства визуализации и сохранности данных пользователя, который показывает несколько последних успешных банковских операций клиента с картами и счетами. 


## Структура проекта:

* src/masks.py модуль отвечающий за кодировку счета/карты 
* src/widget.py модуль отвечающий за преобразования даты
* src/processing.py модуль отвечающий за фильтрацию словарей по дате/ключу

## Установка:
   ```
   poetry install
   ```

Клонируйте репозиторий
    ```
    https://github.com/Irina-Prokopova-01/Prokopova_I_hw1/pull/1
    ```
    
## Установите зависимости:

В проекте не используются внешние библиотеки, только встроенные, поэтому ничего устанавливать дополнительно не нужно. 

## Примеры использования кода:

```def mask_account_card(card: str) -> str:
    """Функция возвращает строку с замаскированным счетом или номером карты"""
    cards = card.split()
    number = cards[-1]
    name = " ".join(cards[:-1])
    if name == 'Счет':
        number = get_mask_account(number)
    else:
        number = get_mask_card_number(number)
    return f"{name} {number}"
```

## Документация

## Лицензия


