'''Abstract Classes in Python
An abstract class can be considered as a blueprint for other classes.

Abstract classes are not able to instantiated and it needs subclasses 
to provide implementations.

 A class which contains one or abstract methods is called an abstract 
 class. An abstract method is a method that has declaration but not 
 has any implementation. 
 
 A define subclass of an ABS must implement all the abstract methods 
 contains by the ABS class'''


from abc import ABC, abstractmethod 
import abc

class Shape(ABC):
    @abstractmethod
    def area(self): pass 

    @abstractmethod
    def perimeter(self): pass

#_______________________________________________________________________


class Square(Shape):
    def __init__(self, side):
        self.__side = side 

    def area(self):
        return self.__side**2

    def perimeter(self):
        return self.__side * 4

my_sq = Square(6)

print('area of my_sq ->', my_sq.area())
print('peri of my_sq ->', my_sq.perimeter())
print('is Square a subclass of Shape:', issubclass(Square,Shape))
print('___________________________________\n')

#_______________________________________________________________________

# Here class Triangle have all the abstract method of Shape but it is 
# not a subclass of it because it does not explicitly extend it

class Triangle:
    def __init__(self, side):
        self.__side = side 

    def center(self):
        return self.__side/2

    def area(self):
        return self.__side**2 * 0.433012701892219

    def perimeter(self):
        return self.__side * 3


my_tri = Triangle(6)
print('center of my_tri ->', my_tri.center())
print('is Triangle a subclass of Shape:', issubclass(Triangle,Shape))
print('___________________________________\n')

#_______________________________________________________________________

# Here __subclasshook__ method to allow a class to be perceived as a 
# subclass without havingto explicitly extend it. 

class PolyShape(ABC):
    @abstractmethod
    def area(self): pass 

    @abstractmethod
    def perimeter(self): pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is PolyShape:                     # <-- name of ABS class
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented


class Hexagon:
    def __init__(self, side):
        self.__side = side 

    def area(self):
        return self.__side**2 * 0.4330127018922193 * 6

    def perimeter(self):
        return self.__side * 6

my_hex = Square(6)

print('area of my_hex ->', my_hex.area())
print('peri of my_hex ->', my_hex.perimeter())
print(
    'is Hexagon a subclass of PolyShape:', issubclass(Hexagon,PolyShape)
)
print('___________________________________\n')  

#_______________________________________________________________________



# print(type(Square(4)))
# print(type(Shape))
# print(type(int))
# print('__________\n')

# print(Shape.__bases__)
# print(Square.__bases__)

# print('__________\n')

# print(Shape.__name__)
# print(Square.__name__)

# print('__________\n')

# print(Shape.__dict__)
# print(Square.__dict__)

# print('__________\n')

