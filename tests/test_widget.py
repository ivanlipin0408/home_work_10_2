import pytest
from scr.widget import get_date, mask_account_card

def test_mask_account_card_wrong_input():
    assert mask_account_card("Карта 2552255") == "К сожалению, не удалось распознать вашу карту или счет"

def test_get_date():
    assert mask_account_card("Visa Gold 5525 5551 4555 5222") == "Visa Gold 5525 55** **** 5222"

def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2024-12-30T02:26:18.671407") == "30.12.2024"

def test_get_date():
    with pytest.raises(ValueError):
        get_date("2024-12-32T02:26:18.671407")
    with pytest.raises(ValueError):
        get_date("2024-14-32T02:26:18.671407")

def test_get_date_wrong_type():
    with pytest.raises(TypeError):
        mask_account_card(123)
    with pytest.raises(TypeError):
        mask_account_card([1, 2 ,3])
    with pytest.raises(TypeError):
        mask_account_card({})

def test_get_date_wrong_date():
    with pytest.raises(ValueError):
        get_date("20w4-03-11T02:26:18.671407")
        get_date("20w4 03-11T02:26:18.671407")
        get_date(" 20w4-03-11T02:26:18.671407")


# "2024-03-11T02:26:18.671407"