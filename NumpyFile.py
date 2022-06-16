from turtle import clear
import numpy as np
import random
array1 = np.array([1,2,3,4,5,6,7])
array2 = np.array([2,4])
# Arrays should be of similar size
#print(array1 + array2)
#print(np.ones((5,3,7,8), dtype = np.int))
#print(np.zeros(10))
randArr = np.random.random([10,100])
#print(randArr[1,])
# arange is similar to range
#np.arange(0,100, 10)
#print(np.arange(0,100, 10))
#linspace - similar to arange , only difference it gives the number of elements between start and end and not the interval
#print(np.linspace(5,10,20))
# Inspect an array
shape = np.shape(randArr)
#print(shape)
#Create an array using list list_1 = [10,11,12,13] and list_2 = [15,12,13,14] 
# and print the shape and dimension of the array created.
arr1 = np.array([[10,11,12,13],[15,12,13,14]])
print(arr1.shape)
print(arr1.ndim)
print(arr1)