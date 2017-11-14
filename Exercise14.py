# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:11:30 2017

@author: SHELASU
"""
num = 0
original_list = []
fresh_list =[]
catch_element = 0

def create_list(num):
    for i in range(num):
        catch_element = int(input("enter your list element:"))
        original_list.append(catch_element)
    return(original_list)

def remove_duplicates():
    fresh_list = set(original_list)
    fresh_list = list(fresh_list)
    return(fresh_list)

    
        
        
    