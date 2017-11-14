# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 15:00:43 2017

@author: SHELASU
"""
string_string = str(input(" Enter your string in here:"))

string_rev = string_string[::-1]  # reverse the entered string
print(string_rev)

if(string_string == string_rev):print("It's a palindrome")
else: print("It's not a pallindrome")