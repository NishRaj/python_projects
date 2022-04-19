#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 08:53:29 2021

@author: nishank
"""

print("Welcome to GPA calculator");
print("Enter your grades one per line");
print("Enter blank space to mark the end of input");
#map for grades with points
map_grade_points = {'E':5.0,'A':4.0,'B':3.0,'C':2.0,'D':1.0,'F':0};
num_courses = 0;
total_points = 0;
done = False;
while not done:
    grade = input();
    if(grade == ''):
        done = True;
    elif(grade not in map_grade_points):
        print("Unrecognized grade '{0}' being ignored".format(grade));
    else:
        num_courses +=1;
        total_points += map_grade_points[grade];
if num_courses > 0:
    grade_point_average = total_points/num_courses;
    print("Your GPA is  {0:.3}".format(grade_point_average))