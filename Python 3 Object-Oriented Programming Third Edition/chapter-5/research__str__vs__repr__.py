class Car: 
    def __init__(self, color, mileage): 
        self.color = color 
        self.mileage = mileage  

my_car = Car('red', 37281)
print(my_car) 
#return   <__main__.Car object at 0x03970A70> 
my_car 
#return   <__main__.Car object at 0x03970A70> 
print(my_car.color, my_car.mileage)
#return   red 37281

class Car: 
    def __init__(self, color, mileage): 
        self.color = color 
        self.mileage = mileage 

    def __str__(self):
        return f'a {self.color} car with {self.mileage} miles'

your_car = Car('blue', 75)

print(your_car)
#return   a blue car with 75 miles
your_car
#return   <lesson__str__.Car object at 0x033C9990> 
str(your_car)
#return   a blue car with 75 miles

#_______________________________________________________________________

class Robot:
    def __init__(self, _type, language):
        self._type = _type 
        self.language = language 

    def __str__(self):
        return '__str__  for Robot' 

    def __repr__(self): 
        return '__repr__ for Robot'

bb8 = Robot('Astromech droid', 'JavaScript') 

print(bb8)
#return   __str__  for Robot
bb8
#return   __repr__ for Robot

print(str(bb8))
#return   __str__  for Robot
print(repr(bb8))
#return   __repr__ for Robot

#_______________________________________________________________________

# __str__ vs __repr__

import datetime 

today = datetime.date.today()
print(today)
#return  2019-09-01

print(str(today))
#return  2019-09-01

print(repr(today))
#return  datetime.date(2019, 9, 1) 