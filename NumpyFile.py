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
arr1 = np.array([[10,11,12,13],[15,12,13,14], [12,12,11, 12]])
print(arr1.shape)
print(arr1.ndim)
print(arr1)
arr2 = np.ones((4,4), dtype=float)
print(arr2*10)
print(arr2 + arr2)
print(arr2.ndim)
arr3 = np.empty((2,3,2))
print(arr3)
print(arr3.ndim)

arr4 = np.ones_like(arr3)
print(arr4)

arr5 = np.eye(3)
print(arr5)
# Convert one type to another
print(arr5.astype(complex))

#Convert first array type to second array type where you don't know type of second array
int_arr = np.arange(10)
float_arr = np.array([.1, .2, .3, .4, .5], dtype=np.float64)
print(int_arr.astype(float_arr.dtype))

#Operations between two similar sized arrays.
print(arr5*arr5)
print(arr5 + arr5)