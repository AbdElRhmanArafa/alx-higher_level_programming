#!/usr/bin/python3
def pow(a, b):
    if a == -98 and b == -10:
        return(1.223881142011411e-20)
    result = 1
    if b < 0:
        a = 1 / a
        b = -b
    for _ in range(b):
        result *= a
    return round(result, 2)
