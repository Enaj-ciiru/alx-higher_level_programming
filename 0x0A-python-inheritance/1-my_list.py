#!/usr/bin/python3
"""Module 1-my_list.
Creates a class inheriting from the list class.
"""


class MyList(list):
    """
    Uses buitin list methods to print sorted list
    """

    def print_sorted(self):
        """ Prints a sorted list """
        print(sorted(self, reverse=False))
