# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:53:07 2017

@author: SHELASU
"""

string_list = " My name is Michelle "
string_num = string_list.split()
print(string_num)
len(string_num)
print(" ".join(string_num))

def reverse_string():
    string_list = input("Enter your string:")
    return(' '.join(string_list.split()[::-1]))