#!/usr/bin/python3
def roman_to_int(roman_string):
    Latin = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    index = 0
    for Rome in roman_string:
        if index < len(roman_string) - 1:
            if Rome == 'I' and roman_string[index + 1] == 'X':
                sum -= 2
        sum += Latin[Rome]
        index += 1
    return sum
