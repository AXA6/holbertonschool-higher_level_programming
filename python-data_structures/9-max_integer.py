#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max1 = my_list[0]

    for n in my_list:
        if n > max1:
            max_value = n

    return max1
