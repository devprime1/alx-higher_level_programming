#!/usr/bin/python3


def new_in_list(my_list, num, element):

    if (num < 0) or (num > (len(my_list)-1)):
        return my_list

    copy = [x for x in my_list]
    copy[num] = element
    return copy
