#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """Fgiinds all multiples of 2 in a list"""
    return [True if n % 2 == 0 else False for n in my_list]
