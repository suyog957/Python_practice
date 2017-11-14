# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 15:36:08 2017

@author: SHELASU
"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_list = []

b = [number for number in a if number % 2 == 0]
print(b)

#------------- random list------------

import random

numlist = []
list_length = random.randint(5,15)


while len(numlist) < list_length:
    numlist.append(random.randint(1,75))
    

evenlist = [number for number in numlist if number % 2 == 0] 

print(numlist)
print(evenlist)