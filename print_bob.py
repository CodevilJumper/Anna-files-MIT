# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 16:21:47 2021

@author: Anna Grzyb
"""

# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2

s = 'azcbobobegghakl'

counter = 0


for i in range(len(s)):
    if s[i:i+3] == 'bob':
        counter = counter + 1
                
print('Number of times bob occurs is: ' + str(counter))

