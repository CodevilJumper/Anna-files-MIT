# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 11:04:38 2021

@author: Anna Grzyb
"""

s = 'abcabc'

previous = ""
current = ""
longest = ""

for char in s:
    if previous <= char:
        current = current + char
        if len(current) > len(longest):
            longest = current
    else:
        current = char
    previous = char
    
print('Longest substring in alphabetical order is: ' + longest )