# Task 28 - NumPy: Creating Arrays
# Source: https://www.w3schools.com/python/numpy_creating_arrays.asp
# This example shows different ways to create NumPy arrays:
# from a Python list, with zeros, ones, arange, and with ndmin.

import numpy as np

# 1. Create an array from a Python list
arr_from_list = np.array([1, 2, 3, 4])
print("Array from a list:", arr_from_list)

# 2. Create an array filled with zeros
# np.zeros(4) makes 4 zeros. The default type is float.
arr_zeros = np.zeros(4)
print("Array of zeros:", arr_zeros)

# 3. Create an array filled with ones
# np.ones((2, 3)) makes 2 rows and 3 columns, all ones.
arr_ones = np.ones((2, 3))
print("Array of ones (2 rows, 3 columns):")
print(arr_ones)

# 4. Create an array with a range of numbers
# np.arange(1, 10, 2) starts at 1, stops before 10, steps by 2.
arr_range = np.arange(1, 10, 2)
print("Array from arange(1, 10, 2):", arr_range)

# 5. Create an array with a minimum number of dimensions
# ndmin=3 forces the array to have 3 dimensions.
arr_ndmin = np.array([1, 2, 3], ndmin=3)
print("Array with ndmin=3:")
print(arr_ndmin)
print("Number of dimensions:", arr_ndmin.ndim)

# Sample output:
# Array from a list: [1 2 3 4]
# Array of zeros: [0. 0. 0. 0.]
# Array of ones (2 rows, 3 columns):
# [[1. 1. 1.]
#  [1. 1. 1.]]
# Array from arange(1, 10, 2): [1 3 5 7 9]
# Array with ndmin=3:
# [[[1 2 3]]]
# Number of dimensions: 3
