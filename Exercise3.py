# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:47:56 2017

@author: SHELASU
"""

my_list = [1, 3, "Michele", [5, 6, 7]]
for element in my_list:
  print(element)
  
  
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#------------ using for standard for loop to print a > 5 ----------

for i in range(len(a)):
    if (a[i] < 5): print(a[i])

#------------ using for custom for loop for lists to print a > 5 ----------

for element in a:
    if (element < 5): print(element)
  
#------------ create new list to print a > 5 ----------

sub_list =[]
for i in range(len(a)):
    if (a[i] < 5): sub_list.append(a[i])

sub_list =[]
for element in a:
    if (element < 5): sub_list.append(element)   # using list functions

#------------ user input and custom list ----------

num = int(input(" Enter a number:" ))
for element in a:
    if (element < num): print(element)   # check condition
