# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 15:51:40 2017

@author: SHELASU
"""
import random
game =  ["Rock","Paper","Scissor"]
for element in game:print(element)  # valid choices

user = input("--- Rock --- Paper --- Scissor , enter your input:")

computer = random.choice(game)

if(user=="Rock" and computer=="Scissor"):
    print("computer :" + str(computer) +"  Congratulations.... you won !! ")
elif(user=="Scissor" and computer=="paper"):
    print("computer :" + str(computer) +"  Congratulations.... you won !! ")
elif(user=="Paper" and computer=="Rock"):
    print("computer :" + str(computer) +"  Congratulations.... you won !! ")
else: print("computer :" + str(computer) + " Try Again , Start a new game ")
    
    
