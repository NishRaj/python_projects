#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:34:22 2021

@author: nishank
"""

dict_1 = {'name':'nishank', 'age': 40, 'height':'Six feet 1 inch', 'occupation':'Technical Architect'};
print (dict_1)
# Get the value from dictionary. If not exists then return the defualt value.
print(dict_1.get('name1','NA'));
dict_1['name'] = 'Abhyuday';
dict_1['occupation'] = 'Scientist';
dict_1['sister']='Nirvi';
print(dict_1);
#check if key is present
val = 'name' in dict_1;
print(val);
#create dictionary using dict keyword
new_dict = dict(name = 'Neha', parents = ['Father','Mother']);
print(new_dict.get('parents','NA'));