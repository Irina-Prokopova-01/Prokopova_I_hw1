# import pytest
#
# from src.widget import mask_account_card, get_data
#
# @pytest.mark.parametrize('number, expected', [('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
#                                               ('Счет 73654108430135874305', 'Счет **4305')])
# def test_mask_account_card(number, expected):
#     assert mask_account_card(number) == expected
#
#
# def test_get_data():
#     assert get_data('2018-07-11T02:26:18.671407') == '11.07.2018'

import pytest

from src.widget import mask_account_card, get_data

@pytest.mark.parametrize('number, expected', [('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                                              ('Счет 73654108430135874305', 'Счет **4305')])
def test_mask_account_card(number, expected):
    assert mask_account_card(number) == expected


def test_get_data():
    assert get_data('2018-07-11T02:26:18.671407') == '11.07.2018'

print(test_get_data())