#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_value = my_list[0]

    for n in my_list:
        if n > max_value:
            max_value = n

    return max_value
