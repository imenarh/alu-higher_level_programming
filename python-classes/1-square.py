#!/usr/bin/python3
"""Defines a class Square with a private instance attribute size."""


class Square:
    """Represents a square with a private instance attribute size."""

    def __init__(self, size):
        """Initializes a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
