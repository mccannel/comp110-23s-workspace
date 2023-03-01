"""EX03 - 'list' Utility Functions"""
__author__ = "730463846"

def all(xs: list[int], x: int) -> bool: 
    idx: int = 0
    iterations: int = 0 
    while idx < len(xs): 
        if xs[idx] == x:
            iterations += 1
        idx += 1
    if iterations == len(xs) and iterations != 0: 
        return True
    else: 
        return False

def max(input: list[int]) -> int: 
    if len(input) == 0: 
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    max_number: int = input[0]
    while idx < len(input):
        if input[idx] > max_number:
            max_number = input[idx]
        idx += 1

def is_equal(x: list[int], y: list[int]) -> bool: 
    idx: int = 0
    matches: int = 0
    while len(x) == len(y) and idx < len(x): 
        if x[idx] == y[idx]: 
            matches += 1
        idx += 1
    if matches == len(x): 
        return True
    else: 
        return False
            

