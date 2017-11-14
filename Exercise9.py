# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 10:27:05 2017

@author: SHELASU
"""

import random 
number = random.randint(1,10)
user=0
counter=0
print("  write exit to end or press any key and enter ")

while(user != "exit" and user!=number):
    user = input("  Guess the number: ")
    if(user=="exit"):
        break
    counter = counter + 1
    if(number == int(user)):
        print(" Exactly right !" + " in total attempts of " + str(counter))
    elif(number - int(user) < 0):
            print(" Too High ! ")
    elif(number - int(user) > 0):
                print(" Too low ! ")
    
    
