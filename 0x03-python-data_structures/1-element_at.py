#!/usr/bin/python3


def element_at(my_list, num):
    if (num < 0) or (num > len(my_list) - 1):
        return None
    return(my_list[num])
