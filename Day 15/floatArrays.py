'''Inspecting Arrays

Create a sample array of float64

Find the shape, size, and dtype of an array.

Change the dtype of an array from float64 to int32.

Find the number of dimensions (ndim) of an array'''

import numpy as np

arr = np.array([10.10,20.10,30.20,50.60] , dtype=np.float64)
print(arr)

shape = np.shape(arr)
print(shape)

size = np.size(arr)
print(size)

dtype = np.int32(arr)
print(dtype)

dimen = np.ndim(arr)
print(dimen)