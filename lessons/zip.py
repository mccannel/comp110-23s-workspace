"""CQ04- Dict Function Writing"""


def zip(keys: list[str], values: list[int]) -> dict[str,int]:
    result: dict[str, int]= {}
    if len(keys)==len(values): 
        idx= 0
        while idx < len(keys):
            result[keys[idx]]= values[idx]
            idx += 1
    return result
