# Python Data Structures - Dictionaries:

# new function or methods:
# dictionanery.setdefault(key, default_value) 
# from module collections:      defaultdict()

stocks = {
    "GOOG": (1235.20, 1242.54, 1231.06),
    "MSFT": (110.41, 110.45, 109.84),
 } 

print("\nstocks[GOOG] >>>", stocks["GOOG"]) 

try:
    print("\nstocks[RIM] >>>", stocks["RIM"])
except Exception as e:
    print("\nstocks[RIM] >>>",  e.__class__.__name__) 

print("\nstocks[RIM] >>>", stocks.get("RIM"))
print("\nstocks[RIM] >>>", stocks.get("RIM", "NOT FOUND"))

#_______________________________________________________________________

# .setdefault 

print(
'\nstocks.setdefault("GOOG","INVALID")\n >>>',
stocks.setdefault("GOOG", "INVALID")
)

print(
'\nstocks.setdefault("BBRY", (10.87, 10.76, 10.90))\n >>>',
stocks.setdefault("BBRY", (10.87, 10.76, 10.90))
)

print("\nstock:")
from pprint import pprint
pprint(stocks)

#_______________________________________________________________________ 

# key(), values() and items():

for stock, values in stocks.items():
    print(f"\n{stock} last value is {values[0]}") 

stocks['ADA'] = (0.0412, 0.0409 , 0.0415 )
print("\nstocks['ADA']:", stocks['ADA'])

#_______________________________________________________________________ 

random_keys = {} 
random_keys["astring"] = "somestring" 
random_keys[5] = "aninteger" 
random_keys[25.2] = "floats work too" 
random_keys[("abc, 123")] = "so do tuples"

print("\n random_keys ->")
pprint(random_keys) 

class AnObject:
    def __init__(self, avalue): 
        self.avalue = avalue 

my_object = AnObject(14) 
random_keys[my_object] = "We can even store objects" 
my_object.avalue = 12 
try: 
    random_keys[[1,2,3]] = "we can't store lists though" 
except:
    print("\nunable to store list \n") 
for key, value in random_keys.items(): 
    print("{} has value {}".format(key, value))

#_______________________________________________________________________ 

# Using defaultdict:

def letter_frequency(sentence): 
    frequencies = {} 
    for letter in sentence: 
        frequency = frequencies.setdefault(letter, 0) 
        frequencies[letter] = frequency + 1 
    return frequencies 


string = """As with all language expressions, sentences might contain 
function and content words and contain properties such as characteristic 
intonation and timing patterns."""

string_dict = letter_frequency(string)
print('\nstring_dict ->', string_dict) 


from collections import defaultdict 

def letter_frequency2(sentence): 
    frequencies = defaultdict(int) 
    for letter in sentence:
        frequencies[letter] += 1 
    return frequencies

string_dict2 = letter_frequency2(string) 
print('\nstring_dict2 ->', string_dict2,'\n') 

#_______________________________________________________________________ 

from collections import defaultdict 

num_items = 0 

def tuple_counter(): 
    global num_items 
    num_items += 1 
    return (num_items, []) 

d = defaultdict(tuple_counter)  

d['a'][1].append("hello") 
d['b'][1].append("world")

# explain the above code: 
# in d = defaultdict(tuple_counter) 
# d is set to be a dict with a default value of tuple (item number, [])
# so d['a'] is set to have a value of  (1, [])
# and therefore d['a'][1] = []   and   d['a'][0] = 1 
# finally we r appending a string in the tuple's list that have index 1.

pprint(d)
print('\n\n')

#_______________________________________________________________________ 

from collections import Counter

responses = [
    "vanilla",
    "chocolate",
    "chocolate",
    "vanilla",
    "vanilla",
    "caramel",
    "strawberry",
    "strawberry",
    "strawberry",
    "vanilla"
]



ice_cream = Counter(responses)
print(ice_cream,'\n')

favorite  = ice_cream.most_common()
print(favorite,'\n')

print("The children voted for {} ice cream".format(
    Counter(responses).most_common(1)[0][0])
)