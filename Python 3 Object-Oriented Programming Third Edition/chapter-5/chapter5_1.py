
square = [(1,1), (1,2), (2,2), (2,1)] 

import math 
import os

cls = lambda:os.system('cls')

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def perimeter(polygon):
    perimeter = 0
    points = polygon + [polygon[0]]
    for i in range(len(polygon)):
        perimeter += distance(points[i], points[i+1])
    return perimeter


#_______________________________________________________________________


class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y         

    def distance(self, p2):
        return math.sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2)



class Polygon:
    def __init__(self, points=None):
        points = points if points else []
        self.vertices = [] 
        for point in points:
            if isinstance(point, tuple):
                point = Point(*point)
            self.vertices.append(point)

    def print_point(self):
        for point in self.vertices:
            print("x{0},y{1}".format(point.x, point.y))

    def add_point(self, point):
        self.vertices.append((point))

    def perimeter(self):
        perimeter = 0 
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        return perimeter



#_______________________________________________________________________ 

class Box:
    def __init__(self, length, width, hieght):
        self._length = length 
        self._width = width
        self._hieght = hieght 
        self._dims = [self._length, self._width, self._hieght]

    def getdims(self):
        print('getting dimensions')
        return  self._dims

    def setdims(self, list):
        length, width, hieght = list
        print('setting dimension')
        self._length = int(length) 
        self._width = int(width)
        self._hieght = int(hieght )
        self._dims = [self._length, self._width, self._hieght]

    
    dims = property(getdims, setdims)


#_______________________________________________________________________

class Color:
    def __init__(self, rgb_value, name): 
        self.rgb_value = rgb_value 
        self._name = name 

    def _set_name(self, name): 
        if not name: 
            raise Exception("Invalid Name") 
        self._name = name 
    
    def _get_name(self): 
        return self._name 

    name =  property(_get_name, _set_name) 

#_______________________________________________________________________

# This Class/Code has been rewriten below in the file:

# class Silly: 
#     def _get_silly(self):
#         print("You are getting silly") 
#         return self._silly 

#     def _set_silly(self, value): 
#         print("You are making silly {}".format(value)) 
#         self._silly = value 

#     def _del_silly(self): 
#         print("Whoah, you killed silly!") 
#         del self._silly 

#     silly = property(
#         _get_silly, _set_silly, _del_silly, "This is a silly property"
#     )
#_______________________________________________________________________

class Foo: 

    @property 
    def foo(self):
        return self._foo 

    @foo.setter
    def foo(self, value): 
        self._foo = value

#_______________________________________________________________________

class Silly: 
    @property 
    def silly(self): 
        "This is a silly property" 
        print("You are getting silly") 
        return self._silly 
    
    @silly.setter 
    def silly (self, value):
        print("You are making silly {}".format(value)) 
        self._silly = value 

    @silly.deleter 
    def silly(self):
        print("Whoah, you killed silly!")
        del self._silly

#_______________________________________________________________________


from urllib.request import urlopen 

class WebPage:
    def __init__(self, url): 
        self.url = url 
        self._content = None 

    @property 
    def content(self):
        if not self._content:
            print("Retriving New Page...")  
            self._content = urlopen(self.url).read() 
        return self._content

# Testing the WebPage class:-

import time 

webpage = WebPage("http://ccphillips.net/") 
print("\n\nstart time now:-")
now = time.time() 
content1 = webpage.content
print("finishedin: - ", time.time() - now,"\n") 

print("\n2nd try, restart time now:-")
now = time.time() 
content2 = webpage.content
print("finishedin: - ", time.time() - now,"\n") 

print(content2 == content1,"\nnice ;)")

#_______________________________________________________________________

class AvrageList(list):
    @property 
    def avrage(self):
        return sum(self) / len(self)

# Test AvrageList class

list_a = AvrageList([12,5,6,7,25,8,3,1,8,0])
print('list_a ->', list_a)
print('avr list_a ->', list_a.avrage)

#_______________________________________________________________________

