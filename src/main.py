# Импортирование необходимых для программы функций из разработанных модулей
from src.processing import filter_by_state, sort_by_date
from src.searching_str_in_transaction import searching_str_in_transacnions
from src.utils import get_transactions_json_csv_xlsx_file
from src.widget import get_data, mask_account_card


def main() -> None:
    """Функция, отвечает за основную логику проекта и работу с пользователем в
    формате вопрос/ответ."""
    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""
    )
    while True:
        users_menu_choise = input("Введите номер пункта в меню: ")
        if users_menu_choise in ("1", "2", "3"):
            break
        else:
            print('Введён некорректный ответ. Введите "1", "2" или "3"')
    menu = {
        "1": "Для обработки выбран JSON-файл",
        "2": "Для обработки выбран CSV-файл",
        "3": "Для обработки выбран XLSX-файл",
    }
    print(f"{menu[users_menu_choise]}")
    if users_menu_choise == "1":
        transaction_data_list = get_transactions_json_csv_xlsx_file("../data/operations.json")
    elif users_menu_choise == "2":
        transaction_data_list = get_transactions_json_csv_xlsx_file("../data/transactions.csv")
    elif users_menu_choise == "3":
        transaction_data_list = get_transactions_json_csv_xlsx_file("../data/transactions_excel.xlsx")
    # Фильтрация по статусу
    while True:
        print("""Введите статус интересующей вас опреации:  EXECUTED, CANCELED, PENDING""")
        users_status = input("Введите выбранный статус: ").upper()
        if users_status in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        else:
            print('Введён некорректный ответ. Введите "EXECUTED", "CANCELED" или "PENDING"')

    filtred_transaction_data = filter_by_state(transaction_data_list, users_status)
    print(f"Операции отфильтрованы по статусу {users_status}.")
    # Фильтрация по дате

    while True:
        print("Отфильтровать операции по дате?")
        users_choise_date_sort = input("Введите да/нет: ").lower()
        if users_choise_date_sort in ("да", "нет"):
            break
        else:
            print("Введён некорректный ответ. Повторите ввод ответа.")
    if users_choise_date_sort == "да":

        while True:
            print("Отфильтровать по возрастанию или убыванию?")
            users_choise_sort_direction = input("Введите по возрастанию/по убыванию сюда: ").lower()
            if users_choise_sort_direction in ("по возрастанию", "по убыванию"):
                break
            else:
                print('Введён некорректный ответ. Введите "по возрастанию" или "по убыванию"')
        if users_choise_sort_direction == "по возрастанию":
            direction = False
        elif users_choise_sort_direction == "по убыванию":
            direction = True
        # print(transaction_data_list)
        date_sorted_transactions = sort_by_date(transaction_data_list, direction)
    elif users_choise_date_sort == "нет":
        date_sorted_transactions = filtred_transaction_data
    # Фильтрация по рублёвым транзакция

    while True:
        print("Выводить только рублёвые транзакции?")
        users_choise_rub = input("Введите да/нет: ").lower()
        if users_choise_rub in ("да", "нет"):
            break
        else:
            print('Введён некорректный ответ. Введите "да" или "нет"')
    if users_choise_rub == "да":
        # print(date_sorted_transactions)
        rub_transactions = [
            transaction
            for transaction in date_sorted_transactions
            if transaction["operationAmount"]["currency"]["code"] == "RUB"
        ]

    elif users_choise_rub == "нет":
        rub_transactions = date_sorted_transactions
    # Фильтрация по определённому слову в описании

    while True:
        print("Отфильтровать список по определённому слову в описании?")
        users_choise_description = input("Введите да/нет сюда: ").lower()
        if users_choise_description in ("да", "нет"):
            break
        else:
            print('Введён некорректный ответ. Введите "да" или "нет"')
    if users_choise_description == "да":
        users_word_to_filter = input("Введите слово для сортировки: ").lower()
        sorted_by_description = searching_str_in_transacnions(rub_transactions, users_word_to_filter)
        result_transactions = sorted_by_description
    elif users_choise_description == "нет":
        result_transactions = rub_transactions
    # Работа с итоговым списком
    count_of_transactions = len(result_transactions)
    # Вывод результатов, если список не пустой
    if count_of_transactions > 0:
        print("Распечатываю итоговый список транзакций...\n")
        print(f"Всего банковских операций в выборке {count_of_transactions}.\n")
        for item in result_transactions:
            if item["description"] == "Открытие вклада":
                date_str = get_data(item["date"])
                descr_str = item["description"]
                summa_str = item["operationAmount"]["amount"]
                currency_str = item["operationAmount"]["currency"]["code"]
                print(
                    f"""{date_str} {descr_str}
Сумма: {summa_str} {currency_str}\n"""
                )
            else:
                date_str = get_data(item["date"])
                descr_str = item["description"]
                from_str = mask_account_card(item["from"])
                to_str = mask_account_card(item["to"])
                summa_str = item["operationAmount"]["amount"]
                currency_str = item["operationAmount"]["currency"]["code"]
                print(
                    f"""{date_str} {descr_str}
{from_str} -> {to_str}
Сумма: {summa_str} {currency_str}\n"""
                )
    # Вывод результата с пустым списком
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
