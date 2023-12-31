#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, TypeError):
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        else:
            new_list.append(result)
        finally:
            if type(result) != (int or float):
                print("wrong type")
    return new_list
