# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:20:34 2017

@author: SHELASU
"""

x = [1, 2, 3]
y = [5, 10, 15]

allproducts = [a*b for a in x for b in y]

customlist = [a*b for a in x for b in y if a*b%2 != 0]


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = [x for x in a if x in b]   
d = [x for x in a if x not in b]   

import random
 
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
result = [i for i in a if i in b] 

