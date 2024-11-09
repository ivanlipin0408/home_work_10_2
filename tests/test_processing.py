import pytest
from scr.processing import filter_by_state, sort_by_date

def test_filter_by_state():
    with pytest.raises(TypeError):
        filter_by_state("123", "123")
    with pytest.raises(TypeError):
        filter_by_state(123, "123")
    with pytest.raises(TypeError):
        filter_by_state([], 123)

def test_sort_by_date():
    with pytest.raises(TypeError):
        sort_by_date("123", "123")
    with pytest.raises(TypeError):
        sort_by_date(123, "123")
    with pytest.raises(TypeError):
        sort_by_date([], 123)

def test_filter_by_state_wrong_state():
    assert filter_by_state([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": " ", "date": "2018-06-30T02:08:58.425572"}]) == "Неверный статус"

