# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:19:52 2017

@author: SHELASU
"""
x = range(2, 100)

num = int(input(" Enter a number:" ))
for element in x:
    if (num % element ==0): print(element)   # check condition

#------------ using list append  ----------

num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)