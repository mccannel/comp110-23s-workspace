"""EX05- List Utility Functions."""
__author__ = "730463845"


def only_evens(input_list: list[int]) -> list[int]:
    """Returns even numbers in given list."""
    even_list: list[int] = []
    for item in input_list: 
        if (item % 2) == 0: 
            even_list.append(item)
    return even_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Combines two lists together."""
    mega_list: list[int] = []
    for item in first_list: 
        mega_list.append(item)
    for item in second_list: 
        mega_list.append(item)
    return mega_list


def sub(a_list: list[int], start_idx: int, end_idx: int) -> list[int]: 
    """Returns a subset of a list given specified indices."""
    if (start_idx < 0) or (start_idx > len(a_list)): 
        start_idx = 0
    if end_idx > len(a_list): 
        end_idx = (len(a_list))
    subset: list[int] = []
    for item in range(start_idx, end_idx):
        subset.append(a_list[item])
    return subset