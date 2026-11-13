from bug3_logic import find_max


def test_find_max_with_last_score_as_maximum():
    assert find_max([70, 85, 60, 95]) == 95


def test_find_max_with_ascending_scores():
    assert find_max([10, 20, 30]) == 30


def test_find_max_with_descending_scores():
    assert find_max([95, 85, 70, 60]) == 95


def test_find_max_with_single_score():
    assert find_max([42]) == 42
