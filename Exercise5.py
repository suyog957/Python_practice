# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:43:36 2017

@author: SHELASU
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_element = []

for element in b:
    if (element in a): common_element.append(element)
 
print(common_element)

#------------ create random list   ----------
import random    

random_list_a=[]    
for i in range (10):    
    random_list_a.append(random.randrange(1,101,1))    
    print (random_list_a)    
    
random_list_b=[]    
for i in range (50):    
    random_list_b.append(random.randrange(1,100,1))    
    print (random_list_b)    

common_element_random = []
duplicate_element = []

for element in random_list_a:
    if (element in random_list_b ): common_element_random.append(element)
 
common_element_random = set(common_element_random)     # set returns unique value of list
print(common_element_random)
    