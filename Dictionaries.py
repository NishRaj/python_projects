#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:34:22 2021

@author: nishank
"""
import pprint
dict_1 = {'name':'nishank', 'age': 40, 'height':'Six feet 1 inch', 'occupation':'Technical Architect'}
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

people = {}
people['a'] = {'Name':'Nishank','Age':41, 'Gender':'M','Planet':'Earth'}
people[2] = {'Name':'Abhyuday','Age':10, 'Gender':'M','Planet':'Mars'}
people[3] = {'Name':'Nirvi','Age':1, 'Gender':'F','Planet':'Venus'}
pprint.pprint(people)