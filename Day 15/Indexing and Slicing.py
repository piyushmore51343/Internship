'''Indexing and Slicing
Extract the first 5 elements of an array.

Extract the last 3 elements.

Change every second element of an array.

Extract an element from a 2D array.

Slice a 2D array to get its first 2 rows and first 2 columns.'''
import numpy as np

arr = np.array([10,2,55,1,3,0,1,2,])
print(arr)

print(arr[:5])  
print(arr [-3:])

arr[::2] = 10
print(arr)

arr2d = np.array([[10,20,30,],[40,50,60]])
print(arr2d[1][1])

print(arr2d[:2,:2])