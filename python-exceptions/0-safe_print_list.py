#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        check = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            check += 1
        print("\n", end="")
    except IndexError:
        print("\n", end="")
    return check
