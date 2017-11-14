# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 13:30:34 2017

@author: SHELASU
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 13:23:18 2017

@author: SHELASU
"""
def fibonacci():
    num = int(input("How many numbers that generates?:"))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib
print(fibonacci())
