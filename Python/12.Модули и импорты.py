import math
print(math.sqrt(16)) 

import datetime as dt
now = dt.datetime.now()

# Импорт конкретных функций
from random import randint, choice
print(randint(1, 10))          
print(choice(["а", "б", "в"]))


# В файле calculator.py:
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b


print(add(5, 3))        
print(multiply(5, 3))  