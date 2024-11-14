import pytest

from scr.masks import get_mask_account, get_mask_card_number


def test_mask_card_number(numbers):
    assert get_mask_card_number("1250 8988 8888 5255") == numbers


def test_get_wrong_card_number():
    with pytest.raises(ValueError):
        get_mask_card_number("12345678901234567")

    with pytest.raises(ValueError):
        get_mask_card_number("123456789012345e")


def test_mask_account(account):
    assert get_mask_account("2554 52448974 6521 22 55") == account


def test_get_wrong_account():
    with pytest.raises(ValueError):
        get_mask_account("123456789012345678905")

def test_get_wrong_account():
    with pytest.raises(ValueError):
        get_mask_account("123456789012345672589")

    with pytest.raises(ValueError):
        get_mask_account("123456789012345e")

