#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_a_dictionary = a_dictionary.copy()
    for key in new_a_dictionary:
        new_a_dictionary[key] *= 2
    return new_a_dictionary
