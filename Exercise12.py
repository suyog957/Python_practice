# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 13:00:08 2017

@author: SHELASU
"""
custom_list = []
new_list = []
element_no = 0

def get_list(element_no):
    for i in range(element_no):
        n = int(input(" write your next number in list "))
        custom_list.append(n)
    return custom_list

def customize(custom_list):
    new_list.append(custom_list[0])
    new_list.append(custom_list[(element_no - 1)])
    return new_list


#---------------- To find it's a primenumber --------
def get_integer(help_text):
    return int(input(help_text))

def prime_or_not():
    num = get_integer("Give me a number: ")
    listRange = list(range(1,num+1))
    divisorList = []
    for number in listRange:
        if num % number == 0:
            divisorList.append(number)
            print(divisorList)
    if(len(divisorList) == 2 ):
        print(str(num) + " This is a a prime number ")
    else: print(str(num) +  " This is NOT a prime number " )


#------------- exercise 4 part------------------
num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)