import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("700079228960636") is None
    assert get_mask_card_number("jkghjhgjhgjhhjh") is None


def test_get_mask_card_number_TypeError() -> None:
    with pytest.raises(TypeError):
        get_mask_card_number(678)  # type: ignore


def test_get_mask_account() -> None:
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("736541084301358") is None
    assert get_mask_account("kgjjkgkjjhjkjjh") is None


def test_get_mask_account_TypeError() -> None:
    with pytest.raises(TypeError):
        get_mask_account(596)  # type: ignore
