import math


class Point(object):
    """Represents a point in two-dimensional geometric coordinates"""

    def __init__(self, x=0.0, y=0.0):
        """Initialize the position of a new point. The x and y coordinates
        can be specified. If they are not, the point defaults to the origin."""
        self.move(x, y)

    def move(self, x, y):
        """Move the point to a new location in two-dimensional space."""
        self.x = x
        self.y = y

    def reset(self):
        """Reset the point back to the geometric origin: 0, 0 """
        self.move(0.0, 0.0)

    def calculate_distance(self, other_point):
        """Calculate the distance from this point to a second point passed as a parameter.

        This function uses the pythagorean theorem to calculate
        the distance  between the two points. The distance is returned as float."""

        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


# Creating instance objects
point_a = Point(2, -2)
point_b = Point(2, 2)

point_x = Point(0, 0)
point_y = Point(7, 1)
# distance entry a and b
distance_a = point_a.calculate_distance(point_b)
distance_b = point_x.calculate_distance(point_y)
print(distance_a)
print(distance_b)
