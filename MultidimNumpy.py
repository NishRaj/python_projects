import numpy as np

arr2d = np.array([[1,2,3],[2,3,4]])
print(arr2d[1,2])
arr3d = np.empty((2,2,3))
print(arr3d)
#print(arr3d[0])
print(arr3d[1, 0])

'''
Numpy axes start from 0 and goes till dim-1 like 2d aray will have 0, 1 dimension.

'''
arr = np.arange(6).reshape(2,3)
print(arr)
print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))