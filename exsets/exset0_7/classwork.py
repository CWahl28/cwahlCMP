import math
# Import math module for finding distance.

class Point:
    # Establish the class.
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Define variables.

    def distance(self, other):
        """
          >>> p1 = Point(1, 2)
          >>> p2 = Point(4, 6)
          >>> p1.distance(p2)
          5.0
          >>> p3 = Point(16, 11)
          >>> p2.distance(p3)
          13.0
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    # Return the variables plugged into the pythagorean theorem to find the distance.

if __name__ == '__main__':
    import doctest
    doctest.testmod()
