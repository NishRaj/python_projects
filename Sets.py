#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 12:44:00 2021

@author: nishank
"""

student_list = ['A','a','B','B','C','c','D','D'];
student_set = set(student_list);

student_set.add('7')
print(student_set)
student_list2 = ['A','B','c','d'];
student_set2 = set(student_list2);
print(student_set2);
print(student_set2.intersection(student_set));
print(student_set2.union(student_set));
print(student_set2.difference(student_set));
#Always use symmetric difference to find which element is in one set and missing
#in another.
print(student_set.symmetric_difference(student_set2));