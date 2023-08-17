#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        sorted_dict = dict(sorted(a_dictionary.items(), key=lambda x: x[1]))
        key, _ = sorted_dict.popitem()
        return key
    return None
