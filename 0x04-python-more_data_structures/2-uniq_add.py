#!/usr/bin/python3
def uniq_add(my_list=[]):
    uiqList = []
    for item in my_list:
        uiqList.append(item) if item not in uiqList else item
    return sum(uiqList)
