import numpy as np

arr = np.arange(10)
print(arr)
# Slicing does not copy the array rather changes the original array.
arr[5:8] = 12
print(arr)
# Slicing always create a view and not the copy
arr_slice = arr[5:8]
print(arr_slice)
arr_slice[1] = 12345
# Arr will be merged with the view arr_slice
print(arr)
arr_slice[:] = 64
#arr_slice view will be replaced by 64 in the original array
print(arr)
# Always use copy() method to create a new copy of an ndarray.
#Create a slice object to slice the list, nparray
s = slice(2,7)
input_lst = [1,2,3,4,5,6,7,8,9]
print(input_lst[s])
