#!/usr/bin/python3
# 11-delete_at.py

def delete_at(my_list=[], idx=0):
    """Delete an item at a specific position in a list"""
    n = len(my_list)
    if idx < 0:
        return my_list
    elif idx > n - 1:
        return my_list
    else:
        del my_list[idx]
        return my_list
