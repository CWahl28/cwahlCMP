import math

class Point:
    def distance(self, x, y):
        """
        >>> p1 = Point(1, 2)
        >>> p2 = Point(4, 6)
        >>> p1.distance(p2)
        5.0
        >>> p3 = Point(16, 11)
        >>> p2.distance(p3)
        13.0
        """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    return(sqrt((self.x)**2 + (self.y)**2))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
