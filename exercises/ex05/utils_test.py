"""EX05- List Utility Functions Test."""
__author__ = "730463845"

from exercises.ex05.utils import only_evens, sub, concat

def test_empty() -> None:
    assert only_evens([]) == []

def test_all_evens() -> None: 
    test_list: list[int] = [2, 4, 6]
    assert only_evens(test_list) == [2, 4, 6]

def test_count_up() -> None: 
    test_list: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(test_list) == [2, 4]

def test_contains_repeats() -> None: 
    a_test_list: list[int] = [1, 2]
    b_test_list: list[int] = [1, 2, 3, 4, 5]
    assert concat(a_test_list, b_test_list) == [1, 2, 1, 2, 3, 4, 5]

def test_one_empty() -> None: 
    a_test_list: list[int] = []
    b_test_list: list[int] = [1, 2, 3, 4, 5]
    assert concat(a_test_list, b_test_list) == [1, 2, 3, 4, 5]

def test_contains_diff_ints() -> None:
    a_test_list: list[int] = [1, 2, 3, 4, 5]
    b_test_list: list[int] = [6, 7, 8, 9, 10]
    assert concat(a_test_list, b_test_list) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_idxs_negative_and_longer_than_len() -> None: 
    a_list: list[int] = [10, 20, 30]
    start_idx: int = -1
    end_idx: int = 4
    assert sub(a_list, start_idx, end_idx) == [10, 20, 30]

def test_list_single_int() -> None: 
    a_list: list[int] = [10]
    start_idx: int = 2
    end_idx: int = 4
    assert sub(a_list, start_idx, end_idx) == [10]

def test_idx_positive() -> None: 
    a_list: list[int] = [10, 20, 30, 40]
    start_idx: int = 1
    end_idx: int = 3
    assert sub(a_list, start_idx, end_idx) == [20, 30]


