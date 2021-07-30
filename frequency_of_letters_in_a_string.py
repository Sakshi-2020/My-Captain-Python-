# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 21:38:36 2021

@author: ssing
"""
str = input('Enter a string: ')
def create_dict(x):
    dictionary = {}
    for letter in x:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary


def most_frequent(text):
    letters = [letter.lower() for letter in text if letter.isalpha()]
    dictionary = create_dict(letters)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print (letter, count)

most_frequent(str) #function is called