# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 16:12:34 2017

@author: SHELASU
"""

number = int(input(" Enter a Number:" ))

if (number % 2 == 0) :
    print(" It's an even number")
elif (number % 2 != 0):
    print(" It's an Odd number")
elif (number % 4 ==0):
    print(" It's a multiple of 4")
    
num = int(input(" Enter a new number:" ))
check = int(input(" Enter another number:" ))

if (num % check ==0) :
    print(num + " is completely divisible by " + check)
else : print(num + " sorry , it's NOT completely divisible by  " + check)
    