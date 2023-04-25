"""Contains functions to use for data."""
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str,str]]: 
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    result: list[str] = []
    for row in table:
        result.append(row[header])
    return result


def columnar(table: list[dict[str,str]]) -> dict[str,list[str]]:
    result: dict[str, list[str]] = {}
    first_row: dict[str,str] = table[0]
    for key in first_row:
        result[key]= column_values(table, key)
    return result


def head(table: dict[str, list[str]], num_rows: int) -> dict[str,list[str]]:
    result: dict[str, list[str]] = {}
    for column in table:
        if num_rows >= len(table[column]):
            result[column] = table[column]
        else: 
            col_val: list[str] = []
            for item in range(0, num_rows):
                col_val.append(table[column][item])
            result[column] = col_val
    return result


def select(table: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for item in col_names:
        result[item]= table[item]
    return result


def concat(table_a: dict[str, list[str]], table_b: dict[str, list[str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for column in table_a:
        result[column]= table_a[column]
    for column in table_b: 
        if column in result:
            result[column] += table_b[column]
        else: 
            result[column] = table_b[column]
    return result


def count(input: list[str]) -> dict[str, int]:
    result: dict[str,int] = {}
    for item in input: 
        if item in result:
            result[item] += 1
        else: 
            result[item] = 1
    return result