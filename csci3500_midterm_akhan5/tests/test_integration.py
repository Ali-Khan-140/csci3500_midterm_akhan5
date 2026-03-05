from src.lost_items import LostItem, check_missing

def test_system_interaction():
    item = LostItem("TV", 10, 6)
    missing = item.expected - item.actual

    assert missing == 4