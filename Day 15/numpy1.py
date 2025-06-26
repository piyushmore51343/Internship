'''Creating Arrays
Create a 1D array of numbers from 1–10.

Create an array of 10 zeros.

Create an array of 5 ones.

Create an array of even numbers from 2–20.

Create an array with random numbers between 0 and 1.

Create an array of shape (3, 3) filled with the number 7.

Create an identity matrix of size 4x4.'''
import numpy as np
import random as rp

# Create a 1D array of numbers from 1–10.
arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr1)

# Create an array of 5 ones.
zeros = np.zeros(10)
print(zeros)

# Create an array of 5 ones.
ones = np.ones((1,5))
print(ones)

# Create an array of even numbers from 2–20.
even = np.arange(2, 21, 2)
print(even)

# Create an array with random numbers between 0 and 1.
random_num = np.array([rp.random()])
print(random_num)

# Create an array of shape (3, 3) filled with the number 7.
#
shape = np.full((3,3),7)
print(shape)
# Create an identity matrix of size 4x4.
four = np.eye(4)
print(four)