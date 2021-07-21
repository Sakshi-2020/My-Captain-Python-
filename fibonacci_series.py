# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 20:45:39 2021

@author: ssing
"""

# Program to display the Fibonacci sequence up to n-th term

no_of_terms = int(input("Enter the number of terms: "))

n1 = 0              # first term
n2 = 1              # second term
cnt = 0

# check if the number of terms is valid
if no_of_terms <= 0:
   print("Please enter a positive integer")
   
# if number of terms is one then print n1
elif no_of_terms == 1:
   print("Fibonacci sequence upto",no_of_terms,"term:")
   print(n1)
   
else:
   print("Fibonacci sequence upto",no_of_terms,"terms:")
   while cnt < no_of_terms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       cnt += 1
    