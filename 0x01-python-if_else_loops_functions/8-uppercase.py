#!/usr/bin/python3
def uppercase(str):
    uppercase_var = ""
    for char_ in str:
        if ord(char_) > 96:
            x = ord(char_) - 32
            uppercase_var += chr(x)
        else:
            uppercase_var += char_
    print(uppercase_var)
