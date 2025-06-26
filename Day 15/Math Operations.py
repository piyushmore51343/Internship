'''Math Operations
Perform element-wise addition, subtraction, multiplication, and division between two arrays.

Perform power and square root operations.

Use np.sum(), np.mean(), np.min(), np.max(), and np.std().'''

import numpy as np

arr1 = np.array([10,20,30,40,50,60])
arr2 = np.array([1,2,3,4,5,6,])

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)

print(np.power(arr2,3))
print(np.square(arr2))

arr3 = np.arange(1,10)
print(np.sum(arr3))
print(np.mean(arr3))
print(np.min(arr3))
print(np.max(arr3))
print(np.std(arr3))