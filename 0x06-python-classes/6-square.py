  
#!/usr/bin/python3
"""
 Area of Square
"""


class Square:
    """ Square stuff """

    def __init__(self, size=0, position=(0, 0)):
        """ initializes a square with attributes """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ gets the size """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size with error handeling """
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """ position getter """
        return self._position

    @position.setter
    def position(self, value):
        """ sets the position and error checking """
        s = "position must be a tuple of 2 positive integers"
        if type(value) is tuple:
            if len(value) != 2:
                raise TypeError(s)
            else:
                for i in range(len(value)):
                    if value[i] < 0:
                        raise TypeError(s)
            self.__position = value
        else:
            raise TypeError(s)

    def area(self):
        """ finds the area of the square """
        return self.__size * self.__size

    def my_print(self):
        """ prints the square """
        if self.size == 0:
            print("")
        else:
            for num in range(self.__position[1]):
                print("")
            for y in range(self.__size):
                for x in range(self.__size + self.__position[0]):
                    if x < self.__position[0]:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print("")
