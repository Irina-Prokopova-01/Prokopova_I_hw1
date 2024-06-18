import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'
    assert get_mask_card_number('700079228960636') == None
    assert get_mask_card_number('jkghjhgjhgjhhjh') == None

def test_get_mask_card_number_TypeError():
    with pytest.raises(TypeError):
        get_mask_card_number(678)


def test_get_mask_account():
    assert get_mask_account('73654108430135874305') == '**4305'
    assert get_mask_account('736541084301358') == None
    assert get_mask_account('kgjjkgkjjhjkjjh') == None

def test_get_mask_account_TypeError():
    with pytest.raises(TypeError):
        get_mask_account(596)

