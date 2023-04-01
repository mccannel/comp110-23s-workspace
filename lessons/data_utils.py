from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str,str]]: 
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader: 
        result.append(row)
    file_handle.close()
    return result


def column_vals(table: list[dict[str,str]], header: str) -> list[str]:
    result: list[str] = []
    for row in table: 
        result.append(row[header])


def columnar(table: list[dict[str,str]]) -> dict[str,list[str]]:
    result: dict[str, list[str]] = {}
    first_row: dict[str,str]= table[0]
    for key in first_row:
        result[key]= column_vals(table, key)
    return result