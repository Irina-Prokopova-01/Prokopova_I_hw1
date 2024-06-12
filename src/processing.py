from typing import Iterable


def filter_by_state(dict_1: Iterable[list[dict]], state='EXECUTED') -> Iterable[list[dict]]:
    """Функция сортирующая словари по ключу state"""
    filter_dict = []
    for i in dict_1:
        if i.get('state') == state:
            filter_dict.append(i)
    return filter_dict


def sort_by_date(dict_1: Iterable[list[dict]], ascending=True) -> Iterable[list[dict]]:
    """Функция сортирующая словари по убыванию даты"""
    sorted_date_list = sorted(dict_1, key=lambda x: x['date'], reverse=ascending)
    return sorted_date_list



