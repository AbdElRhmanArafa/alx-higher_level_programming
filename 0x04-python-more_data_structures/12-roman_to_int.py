#!/usr/bin/python3
def roman_to_int(roman_string):
    Latin = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    pre_value = 0
    for Rome in reversed(roman_string):
        if Latin[Rome] >= pre_value:
            sum += Latin[Rome]
        else:
            sum -= Latin[Rome]
        pre_value = Latin[Rome]
    return sum
