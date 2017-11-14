# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:18:57 2017

@author: SHELASU
"""
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

#------------- simple function ---------
def get_integer():
    return int(input(" Enter the number : "))
    
age = get_integer()
school_year = get_integer()

if(age > 15):
    print("You are over the age of 15")
print(" you are in grade "  + str(school_year))

#-------------- function with an argument-----

def get_integer(help_text):
    return int(input(help_text))

age = get_integer("Tell me your age: ")
school_year = get_integer("What grade are you in? ")
if age > 15:
    print("You are over the age of 15")
print("You are in grade " + str(school_year))

#-------------- function with default argument ----

def get_integer(help_text="Give me a number: "):
    return int(input(help_text))

age = get_integer("Tell me your age: ")
school_year = get_integer()
if age > 15:
    print("You are over the age of 15")
print("You are in grade " + str(school_year))