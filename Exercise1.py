# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:11:35 2017

@author: SHELASU
"""
name = input(" Enter your name :")
print("Hi " + name + ", How are you doing today ?")
age = int(input("How old are you ?"))
no_of_year = 100 - age

import datetime as dt
now = dt.datetime.now()
print(name + " , you are " + str(age) + " years old as of " + str(now.month) + "/" + str(now.day) + "/" + str(now.year))

print(name + " , you will be 100 years old in  " + str(now.month) + "/" + str(now.day) + "/" + str(now.year + no_of_year))

message = name + " , you will be 100 years old in  " + str(now.month) + "/" + str(now.day) + "/" + str(now.year + no_of_year)

repeat_times = int(input("How many times you would like to see this message again ?"))

for i in range(repeat_times):
    print(message, "\n")




