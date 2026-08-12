# tuples:
import datetime 

def middle(stock, date):
    symbol, current, high, low = stock 
    return (((high + low) / 2), date) 

mid_value, date = middle(
    ("FB", 177.46, 178.67, 175.79), datetime.date(2018, 8, 27)
)

print('\nmid value:', mid_value)
print('date:', date)

#_______________________________________________________________________

# namedtuples:
from collections import namedtuple 

Stock = namedtuple("Stock", ["symbol","current", "high", "low"])
stock = Stock("FB", 177.346, high=178.67, low=175.79)
print('\nstock[0]:',stock[0])
print('stock[1]:',stock[1])
print('stock[2]:',stock[2])
print('stock[3]:',stock[3])


print('\nhigh ->', stock.high)
print('low ->', stock.low)

symbol, current, high, low = stock
print('current >', current)

#_______________________________________________________________________

# Dataclass:


from dataclasses import make_dataclass

Stock = make_dataclass("Stock", ["symbol", "current", "high", "low"]) 
stock = Stock("FB", 177.46, high=178.67, low=175.79) 

print('\nprinting stock:\n\t', stock)
print('stock.current', stock.current)

stock.current = 178.25 
print('stock.current', stock.current, '\n')

stock.unexpected_attribute = 'allowed'
print('stock.unexpected_attribute >>',stock.unexpected_attribute)

print('\nprinting stock:\n\t', stock)

#_______________________________________________________________________

# Comparing Data Class with regular Class

class StockRegClass: 
    def __init__(self, name, current, high, low):
        self. name = name 
        self .current = current 
        self.high = high 
        self.low = low 
    
stock_A = Stock("FB", 177.46, high=178.67, low=175.79)

stock_B = StockRegClass("FB", 177.46, 178.67, 175.79)

print('stock_A >',stock_A)
print('stock_B >',stock_B)

print('StockA == StockB ?',stock_A == stock_B)

stock_C = Stock("FB", 177.46, high=178.67, low=175.79)

print('StockA == StockC ?',stock_A == stock_C)

#_______________________________________________________________________

# An alternative (and more common) way to define a dataclass. 

from dataclasses import dataclass  

@dataclass  
class StockDecorated:
    name: str 
    current: float 
    high: float 
    low: float 

@dataclass 
class StockDefaults:
    name: str 
    current: float = 0.0 
    high: float = 0.0 
    low: float = 0.0 

facebook = StockDefaults('FB')
print(facebook)

# or 

print(StockDefaults('FB'))

apple = StockDecorated('AAPL', 208.74, 210.45, 207.20)
print(apple)

#_______________________________________________________________________

