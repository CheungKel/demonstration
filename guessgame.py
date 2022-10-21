#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 15:15:22 2021

@author: keke
"""

import random as random

random_number = random.randint(1, 10)
guess = 0
print("random number = ", random_number)
while guess != random_number:
    print("Enter the guess number between 1 to 10")
    guess = int(input()) 
    if guess < random_number:
       print("Too low") 
    elif guess > random_number:
        print("Too high")
       
    print("You get it right!") 
print("Computer wins!")                           
