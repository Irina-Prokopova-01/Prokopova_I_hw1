from typing import Iterable


def filter_by_state(dict_1: Iterable[list[dict]], state='EXECUTED') -> Iterable[list[dict]]:
    filter_dict = []
    for i in dict_1:
        if i.get('state') == state:
            filter_dict.append(i)
    return filter_dict

