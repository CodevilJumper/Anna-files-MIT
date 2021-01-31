# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 16:39:10 2021

@author: Anna Grzyb
"""

s = 'abcbcd'

previous = ""
current = ""
longest = ""

for char in s:
    if previous <= char:
        current = current + char
        
    else:
        current = char
    previous = char

print("Longest substring in alphabetical order is: " + current)