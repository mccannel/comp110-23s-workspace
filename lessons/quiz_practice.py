"""Practice for Quiz 2/23"""

def odd_and_even(input_list: list[int]) -> list[int]: 
    result: list[int] = []
    idx: int = 0
    while idx < len(input_list):
        if (input_list[idx] % 2 != 0) and (idx % 2 == 0): 
            result.append(input_list[idx])
        idx += 1
    return result 

def value_exits(dict_1: dict[str,int], x: int) -> bool: 
    exists: bool = False
    for item in dict_1: 
        if dict_1[item]== x: 
            exists = True 
    return exists 

def short_words(list_1: list[str]) -> list[str]: 
    new_list: list[str]= []
    for word in list_1: 
        if len(word) <= 5: 
            new_list.append(word)
        else:
            print(f"{word} is too long!")
    return new_list
