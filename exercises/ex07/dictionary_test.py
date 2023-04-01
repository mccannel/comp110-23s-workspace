"""EX07 - Dictionary Function - Unit Tests."""
__author__ = "730463845"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_same_keys() -> None:
    """Tests when two of same values exist in the original list."""
    test_dict: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'y'}
    assert invert(test_dict) == "KeyError: 'This key already exists'"


def test_one_item() -> None:
    """Tests function with one key and corresponding value."""
    test_dict: dict[str, str] = {'orange': 'apple'}
    assert invert(test_dict) == {'apple': 'orange'}


def test_multiple_items() -> None:
    """Tests function with multiple keys and corresponding values."""
    test_dict: dict[str, str] = {'e': 'm', 'n': 'b', 'a': 'w', 's': 'j'}
    assert invert(test_dict) == {'m': 'e', 'b': 'n', 'w': 'a', 'j': 's'}


def test_tie() -> None:
    """Tests function when there is tie for most popular color."""
    assert favorite_color({'Ellie': 'blue', 'Ali': 'blue', 'Avery': 'green', 'Emma': 'green', 'Sally': 'pink'}) == 'blue'


def test_fav_appears_twice() -> None:
    """Tests function when every color appears only once except for one."""
    assert favorite_color({'Ellie': 'pink', 'Ali': 'blue', 'Avery': 'green', 'Emma': 'green', 'Sally': 'orange'}) == 'green'


def test_clear_winner() -> None: 
    """Tests function when everyone has the same favorite color except one."""
    assert favorite_color({'Ellie': 'pink', 'Ali': 'blue', 'Avery': 'blue', 'Emma': 'blue', 'Sally': 'blue'}) == 'blue'


def test_empty_list() -> None: 
    """Tests function when given an empty list."""
    assert count([]) == {}


def test_items_appear_once() -> None:
    """Tests function when list items appear only once."""
    assert count(['Ellie', 'Ali', 'Emma', 'Sally', 'Avery']) == {'Ellie': 1, 'Ali': 1, 'Emma': 1, 'Sally': 1, 'Avery': 1}


def test_some_items_repeat() -> None:
    """Tests function when list items appear more than once."""
    assert count(['x', 'y', 'y', 'z', 'w', 'x']) == {'x': 2, 'y': 2, 'z': 1, 'w': 1}
