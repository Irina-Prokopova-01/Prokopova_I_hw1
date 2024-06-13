def filter_by_state(data_list: list[dict], state: str="EXECUTED") -> list[dict]:
    """Функция фильтрующая словари по ключу state"""
    filter_dict = []
    for item in data_list:
        if item.get("state") == state:
            filter_dict.append(item)
    return filter_dict


def sort_by_date(data_list: list[dict], ascending: bool=False) -> list[dict]:
    """Функция сортирующая словари по дате"""
    sorted_date_list = sorted(data_list, key=lambda x: x["date"], reverse=ascending)
    return sorted_date_list
