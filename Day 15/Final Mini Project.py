'''Final Mini Project
Perform the following in one script:

Create a 5x5 array of random integers between 1–100.

Find the min, max, mean, and sum of the array.

Replace all numbers > 50 with -1.

Save the array to a .npy file.

Load it back and print the contents.'''

import numpy as np

arr = np.random.randint(1,100 ,(5,5))
print(arr)
print(np.min(arr))
print(np.max(arr))
print(np.mean(arr))
print(np.sum(arr))

arr[arr > 50] = -1
print(arr)

np.save("array.npy" , arr)
