#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 08:05:28 2021

@author: nishank
"""

score = int(input('Please key in the score: '));
print(type(score));
passing = 40;
distinction = 90;
if(score == 100):
    print("Perfect score");
elif(90<=score<100):
    print("You have got distinction");
elif(passing<=score<distinction):
    print("You have passed");
elif(score < passing):
    print("You have failed");

num = int(input('Enter the number: '));
if(num%2==0):
    print('Number is even');
    if(num%4==0):
        print('Number is divisible by 4');
    else:
        print('Number is not divisible by 4');
else:
    print('Number is odd');
    if(num%3 ==0):
        print('Number is divisible by 3');
    else:
        print('Number is not divisible by 3');
input_str = input('Key in the word ');
if(input_str.startswith('a') or input_str.startswith('e')
   or input_str.startswith('o') or input_str.startswith('u')):
    print('The string starts with vowel');
else:
    print("no");