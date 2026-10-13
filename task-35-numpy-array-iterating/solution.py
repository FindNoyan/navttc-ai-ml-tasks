# Task 35 - NumPy: Array Iterating
# Source: https://www.w3schools.com/python/numpy_array_iterating.asp
# This example shows how to loop through a 1D array, loop through
# the rows of a 2D array, and use np.nditer() to visit every element.

import numpy as np

# Iterate a 1D array: the loop gives us one element at a time.
arr_1d = np.array([10, 20, 30])
print("Iterating a 1D array:")
for value in arr_1d:
    print(value)

# Iterate a 2D array: the loop gives us one row at a time.
arr_2d = np.array([[1, 2], [3, 4]])
print("Iterating rows of a 2D array:")
for row in arr_2d:
    print("Row:", row)

# Iterate every element of a 2D array with a nested loop.
print("Iterating every element of a 2D array (nested loop):")
for row in arr_2d:
    for value in row:
        print(value)

# np.nditer() is a helper that visits every element of an array,
# no matter how many dimensions it has, without nested loops.
print("Iterating every element with np.nditer():")
for value in np.nditer(arr_2d):
    print(value)

# Sample output:
# Iterating a 1D array:
# 10
# 20
# 30
# Iterating rows of a 2D array:
# Row: [1 2]
# Row: [3 4]
# Iterating every element of a 2D array (nested loop):
# 1
# 2
# 3
# 4
# Iterating every element with np.nditer():
# 1
# 2
# 3
# 4
