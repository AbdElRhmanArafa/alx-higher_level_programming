#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        newT = len(sentence), "None"
    else:
        newT = len(sentence), sentence[0]
    return newT
