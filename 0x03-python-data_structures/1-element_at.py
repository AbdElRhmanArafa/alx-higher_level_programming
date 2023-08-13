#!/usr/bin/python3
def element_at(my_list, idx):
    if 0 <= idx < len(idx):
        return my_list[idx]
    else:
        return "None"

if __name__ == "__main__":
    my_list = [1, 2, 3, 4]
    index = 2
    result = element_at(my_list, index)
    if result is not None:
        print(result)
    else:
        print("Index out of range")
