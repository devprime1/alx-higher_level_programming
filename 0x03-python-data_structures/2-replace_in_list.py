#!/usr/bin/python3


def replace_in_list(my_list, num, element):
    if (num < 0) or (num > len(my_list) - 1):
        return my_list
    else:
        my_list[num] = element
        return my_list
