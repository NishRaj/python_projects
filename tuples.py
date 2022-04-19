#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 13:25:44 2021

@author: nishank
"""

first_tuple = ('hi', 1,3,3,'Nishank');
print(first_tuple);
print(first_tuple[0]);
#first_tuple[0] = 'bye';
list_tuple = list(first_tuple);
list_tuple[0] = 'bye'
print(list_tuple);
print((True, 1, 2)[1])