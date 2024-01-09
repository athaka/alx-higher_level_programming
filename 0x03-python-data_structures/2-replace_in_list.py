#!/usr/bin/python3
# Author: Jonathan Esokawu


def replace_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        my_list.pop(idx)
        my_list.insert(idx, element)
    return my_list
