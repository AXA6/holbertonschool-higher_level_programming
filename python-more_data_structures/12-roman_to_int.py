#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    d = {'I': 1, 'X': 10, 'C': 100, 'M': 1000, 'D': 500, 'L': 50, 'V': 5}
    total = 0
    for i in range(len(roman_string)):
        current = d.get(roman_string[i], 0)
        nex = d.get(roman_string[i + 1], 0) if i + 1 < len(roman_string) else 0
        if current < nex:
            total -= current
        else:
            total += current
    return total
