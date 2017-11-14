# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:22:49 2017

@author: SHELASU
"""
import random
import string

string.ascii_lowercase   # returns complete lowercase string
string.ascii_letters    # returns omplete string both lower and upper case
string.digits           # returns complete digits
string.punctuation      # returns complete special characters 

pswd_len = 0            # password length

def password_gen():
    pswd_len = random.randint(5,12)  # create a passowrd of minum length =5 and max llength =21
    string.ascii_letters    # returns omplete string both lower and upper case
    string.digits           # returns complete digits
    string.punctuation      # returns complete special characters 
    random_string = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(random_string) for _ in range(pswd_len))
    return(password)
    
    