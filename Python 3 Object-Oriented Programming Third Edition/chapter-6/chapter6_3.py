# Lists 

# new function and methods

import string 

# checking string
print('string :',string)

CHARACTERS = list(string.ascii_letters) + [" "]

# checking string.ascii_letters
print('string.ascii_letters :', string.ascii_letters) 

def letter_frequency(sentence): 
    frequency = [(c, 0) for c in CHARACTERS]
    for letter in sentence: 
        index = CHARACTERS.index(letter) 
        frequency[index] = (letter, frequency[index][1]+1)
    return frequency
          
test_sting = "The red fox is the largest of the true foxes and one of \
the most widely distributed members of the order Carnivora"

# Testing above code:
test_list = letter_frequency(test_sting)
print(test_list)

#_______________________________________________________________________ 

# Sorting lists: 

print('\n\n')

class WeirdSortee: 
    def __init__(self, string, number, sort_num): 
        self.string = string 
        self.number = number 
        self.sort_num = sort_num 
         
    def __lt__(self, object): 
        if self.sort_num: 
            return self.number < object.number 
        return self.string < object.string  

    def __repr__(self):
        return f"{self.string}:{self.number}"

# Testing class: 

a = WeirdSortee('a', 4, True) 
b = WeirdSortee('b', 3, True) 
c = WeirdSortee('c', 2, True) 
d = WeirdSortee('d', 1, True) 

l = [a, b, c, d]
print('list l :', l) 

l.sort() 
print('list l.sort (by number) :', l) 

for i in l:
    i.sort_num = False 

l.sort()
print('list l.sort :', l)

#_______________________________________________________________________ 

print('\n\n')

class Foobar:
    def __init__(self, idx):
        self.idx = idx
    
    def __repr__(self):
        if isinstance(self.idx, int):
            self.idx = str(self.idx)
        return self.idx
    
    def __lt__(self, _object):
        return self.idx < _object.idx


# Testing class Foobar:
_list = ['chris', 'dorothy', 'aa', 'Z', 9, 0]
new_list = []

for _ in _list:
    new_list.append(Foobar(_))
print(new_list)

new_list.sort()
print(new_list)

print('is chris < dorothy',_list[1] < _list[0])
print('is chris > dorothy',_list[1] > _list[0])



#_______________________________________________________________________ 

print('\n\n')

'''The __lt__ method is the only one weneed to implement to enable 
sorting. 

Technically, however, if it is implemented, the class should normally 
also implement the similar __gt__, __eq__, __ne__, __ge__, and __le__ 
methods so that all of the <, >, ==, !=, >=, and <= operators 
also work properly.

You can get this for free by implementing __lt__ and __eq__, and then 
applying the @total_ordering class decorator to supply the rest:''' 

from functools import total_ordering 

@total_ordering 
class WeirdSortee: 
    def __init__(self, string, number, sort_num=False): 
        self.string = string 
        self.number = number 
        self.sort_num = sort_num 

    def __lt__(self, object): 
        if self.sort_num:
            return self.number < object.number 
        return self.string < object.string 

    def __repr__(self): 
        return f"{self.string}:{self.number}" 
    
    def __eq__(self, object): 
        return all((
            self.string == object.string,
            self.number == object.number,
            self.sort_num == object.sort_num
        )) 


# Test class WeirdSortee
chris = WeirdSortee('chris', 7)
dorothy = WeirdSortee('dorothy', 0)
double_a = WeirdSortee('aa', 0)
ax2 = WeirdSortee('aa', 0)
nine = WeirdSortee('9', 100)
zero = WeirdSortee('0', 0.5)
Z =    WeirdSortee('z', -7)

list_of_things = [chris, dorothy, double_a, nine, zero, Z, ax2] 
print(list_of_things)

list_of_things.sort()
print(list_of_things)


for i in list_of_things:
    i.sort_num = True
list_of_things.sort()
print(list_of_things)

print(chris == zero) 
print(double_a != dorothy) 
print(double_a == ax2) 


#_______________________________________________________________________ 