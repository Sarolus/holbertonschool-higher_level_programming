#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None or type(roman_string) is not str):
        return 0
    Value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    SubValue = {"IV": 2, "IX": 2, "XL": 20, "XC": 20, "CD": 200, "CM": 200}

    int = sum(Value[char] for char in roman_string)
    int -= sum(value for key, value in SubValue.items() if key in roman_string)

    return int
