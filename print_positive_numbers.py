# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 21:00:51 2021

@author: ssing
"""

list1 = []
n = int(input("Enter number of terms you want to feed: "))
#loop to enter the list
for x in range(0, n):
    term = int(input("Enter your number: "))
    list1.append(term)    #adds term to the list 

print("Positive numbers in the list: ")
#loop to print positive numbers
for x in range(0, n):
    if list1[x] > 0:
        print(list1[x])
