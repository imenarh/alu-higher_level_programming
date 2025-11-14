#!/usr/bin/python3
"""Square class inheriting from Rectangle with [Square] string."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class with private size."""

    def __init__(self, size):
        """Initialize a Square with private size."""
        self.integer_validator("size", size)
        self.__size = size
        # Initialize Rectangle with width and height equal to size
        super().__init__(size, size)

    def area(self):
        """Return the area of the Square."""
        return self.__size * self.__size

    def __str__(self):
        """Return informal string representation as [Square] <size>/<size>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
