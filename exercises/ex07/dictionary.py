"""EX07- Dictionary Functions!"""
__author__ = "730463845"


def invert(input: dict[str, str]) -> dict[str, str]: 
    """Switches the keys and values from a given dict."""
    result: dict[str, str] = {}
    for key in input: 
        if input[key] in result:
            raise KeyError("This key already exists!")
        else: 
            result[input[key]] = key
    return result


def favorite_color(input: dict[str, str]) -> str:
    """Given a dictionary of colors, returns the color that appears most frequently."""
    color_count: dict[str, int] = {}
    fav_color: str = ""
    for item in input: 
        if input[item] in color_count: 
            color_count[input[item]] += 1
        else: 
            color_count[input[item]] = 1
    for color in color_count:
        if fav_color == "" or color_count[color] > color_count[fav_color]: 
            fav_color = color
    return fav_color


def count(input: list[str]) -> dict[str, int]:
    """Counts the number of time an item appears in a list."""
    result: dict[str, int] = {}
    for item in input: 
        if item in result:
            result[item] += 1
        else: 
            result[item] = 1
    return result
