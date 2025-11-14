#!/usr/bin/python3
"""Module 1-my_list: Defines a MyList class inheriting from list.
Provides a method to print the list in sorted order without
modifying the original list.
"""


class MyList(list):
    """MyList class that inherits from list.
    Provides a method to print the list in ascending order.
    """

    def print_sorted(self):
        """Print the list in ascending order.
        This method prints the elements of the list sorted in
        ascending order. It does not modify the original list.
        """
        print(sorted(self))
