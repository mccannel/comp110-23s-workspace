"""EX05- List Utility Functions Test."""
__author__ = "730463845"

from exercises.ex05.utils import only_evens, sub, concat


def test_empty() -> None:
    """Tests an empty list."""
    assert only_evens([]) == []


def test_all_evens() -> None: 
    """Tests all even numbers in a list."""
    test_list: list[int] = [2, 4, 6]
    assert only_evens(test_list) == [2, 4, 6]


def test_count_up() -> None: 
    """Tests numbers 1-5."""
    test_list: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(test_list) == [2, 4]


def test_contains_repeats() -> None: 
    """Tests concat function when lists contain repeats."""
    a_test_list: list[int] = [1, 2]
    b_test_list: list[int] = [1, 2, 3, 4, 5]
    assert concat(a_test_list, b_test_list) == [1, 2, 1, 2, 3, 4, 5]


def test_one_empty() -> None: 
    """Tests concat when one list is empty."""
    a_test_list: list[int] = []
    b_test_list: list[int] = [1, 2, 3, 4, 5]
    assert concat(a_test_list, b_test_list) == [1, 2, 3, 4, 5]


def test_contains_diff_ints() -> None:
    """Tests concat with two lists containing no overlapping numbers."""
    a_test_list: list[int] = [1, 2, 3, 4, 5]
    b_test_list: list[int] = [6, 7, 8, 9, 10]
    assert concat(a_test_list, b_test_list) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_idxs_out_of_range() -> None: 
    """Tests sub function when one index is negative and the other is longer than the length of the list."""
    a_list: list[int] = [10, 20, 30]
    start_idx: int = -1
    end_idx: int = 4
    assert sub(a_list, start_idx, end_idx) == [10, 20, 30]


def test_list_single_int() -> None: 
    """Tests sub function when there is only 1 int in the list."""
    a_list: list[int] = [10]
    start_idx: int = 2
    end_idx: int = 4
    assert sub(a_list, start_idx, end_idx) == [10]


def test_idx_positive() -> None: 
    """Tests sub function when both indexs are in range."""
    a_list: list[int] = [10, 20, 30, 40]
    start_idx: int = 1
    end_idx: int = 3
    assert sub(a_list, start_idx, end_idx) == [20, 30]