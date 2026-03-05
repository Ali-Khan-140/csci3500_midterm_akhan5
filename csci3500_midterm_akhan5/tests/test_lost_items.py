from src.lost_items import LostItem, check_missing

def test_missing_items():
    item = LostItem("TV", 10, 8)
    assert item.expected - item.actual == 2

def test_no_missing_items():
    item = LostItem("MILK", 5, 5)
    assert item.expected - item.actual == 0


import pytest
from src.lost_items import LostItem

@pytest.mark.parametrize(
    "expected,actual,missing",
    [
        (10,8,2),
        (5,5,0),
        (20,15,5)
    ]
)

def test_multiple_cases(expected, actual, missing):
    item = LostItem("TEST", expected, actual)
    assert expected - actual == missing

    