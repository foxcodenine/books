import os

cls = lambda: os.system('cls')


class MyFirstClass:
    pass

#________________________________________

import math

class Point1:
    def move(self, x, y):
        self.x = x 
        self.y = y

    def reset(self): 
        self.move(0, 0)

    def calculate_distance(self, other_point):
        return math.sqrt(
            (self.x - other_point.x) ** 2
            + (self.y - other_point.y) ** 2
    ) 


# Testing Point1 Class:
point1 = Point1()
point2 = Point1()

point1.reset()
point2.move(5, 0)
print('\ndist from p2 to p1 ->', point2.calculate_distance(point1))
assert point2.calculate_distance(point1) == point1.calculate_distance(
    point2
)
#result: dist from p2 to p1 -> 5.0


point1.move(3, 4)
print('\nnew dist from p1 to p2 ->', point1.calculate_distance(point2))
#result: new dist from p1 to p2 -> 4.47213595499958

print('\ndist from p1 to p1 ->', point1.calculate_distance(point1))
#result: dist from p1 to p1 -> 0.0

# point = Point1()
# point.x = 5
# print(point.x)
# #result: 5



#________________________________________


class Point2:
    def __init__(self, x, y):
        self.move(x, y )

    def move(self, x, y):
        self.x = x
        self.y = y 

    def reset(self):
        self.move(0, 0)

# Constructing a Point
point = Point2(3, 5)
print("\nx{}, y{}".format(point.x, point.y))
#result: x3, y5

#________________________________________

class Point:
    "Represents a point in two_dimentional geometric coordinates"

    def __init__(self, x=0, y=0):
        """Initialize the position of a new point. The x and y
           coordinates can be specified. If they are not, the 
           point default to the origin."""
        self.move(x, y)

    def move(self, x, y):
        "Move the point to a new location in 2D space."
        self.x = x
        self.y = y 

    def reset(self):
        "Reset the point back to the geometric origin: 0, 0"
        self.move(0, 0)

    def calculate_distance(self, other_point):
        """Calculate the distance from this point to a second
            point passed as a parameter.
            
            This function uses the Pythagorean Theorem to calculate
            the distance between the two points. The distance is
            returned as a float."""

        return math.sqrt(
            (self.x - other_point.x) ** 2
            + (self.y - other_point.y) ** 2
        )


#________________________________________