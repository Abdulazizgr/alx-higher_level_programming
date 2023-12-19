#!/usr/bin/python3
"""
This is a module that Write a class Square
"""


class Square:
    """
    This is a module that Write a class Square

    Attributes:
        size (int): Human readable string describing the exception.
        position (tuple): Tuple
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            size (int): Description of `param1`.
            position (tuple): Tuple
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if (not isinstance(position, tuple) or len(position) != 2
            or not isinstance(position[0], int) or
            not isinstance(position[1], int) or position[0] < 0
                or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
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
            string_to_print = ""
            for i in range(self.position[1]):
                string_to_print += "\n"
            for x in range(self.size):
                for y in range(self.position[0]):
                    string_to_print += " "
                for z in range(self.size):
                    string_to_print += "#"
                string_to_print += "\n"
            print("{}".format(string_to_print), end='')

    @property
    def position(self):
        """
        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:

        Returns:
            positon
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            value (tuple): value tuple
        Returns:
            Area
        """
        if (not isinstance(value, tuple) or len(value) != 2 or not
            isinstance(value[0], int) or not isinstance(value[1], int)
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
