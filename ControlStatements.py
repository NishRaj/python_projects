#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 09:30:47 2021

@author: nishank
"""

# For loop using range built in keyword
for i in range (1,10):
    print(i);

for i in range(1,10,3):
    print(i);

input_str = input("Type in the string: ");
for alphabet in input_str:
    print(alphabet);

for alphabet,n in enumerate(input_str):
    print(n,alphabet);

star_str = '';
for i in range(0,9):
    if(i<5):
       star_str += '* ';
       print(star_str);
    elif(i >=5):
        star_str = star_str[:-2];
        print(star_str);
        
        
    