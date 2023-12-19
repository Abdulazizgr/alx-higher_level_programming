#!/usr/bin/python3
"""
This is a module that Write a class Square
"""


class Square:
    """
    This is a module that Write a class Square

    Attributes:
        size (int): Human readable string
    """
    def __init__(self, size=0):
        """
        The __init__ method may be documented in either the class level
        docstring, or as a d

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            size (int): Description of `param1`.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        """
        Private instance attribute: size
        """
    def area(self):
        """
        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:

        Returns:
            Area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:

        Returns:
            Size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            value (int): value int
        Returns:
            Area
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:

        Returns:
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.size):
                print("#" * self.__size)
