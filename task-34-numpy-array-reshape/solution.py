# Task 34 - NumPy: Array Reshape
# Source: https://www.w3schools.com/python/numpy_array_reshape.asp
# This example shows how to change an array's shape with reshape(),
# how -1 lets NumPy work out one dimension for us, and how to turn
# a multi-dimensional array back into 1D with flatten() and ravel().

import numpy as np

# Start with a 1D array of 12 numbers.
arr_1d = np.arange(1, 13)
print("Original 1D array:", arr_1d)

# Reshape to 2D: 3 rows, 4 columns (3 x 4 = 12 elements).
arr_2d = arr_1d.reshape(3, 4)
print("Reshaped to 2D (3 rows, 4 columns):")
print(arr_2d)

# Reshape to 3D: 2 blocks, 3 rows, 2 columns (2 x 3 x 2 = 12).
arr_3d = arr_1d.reshape(2, 3, 2)
print("Reshaped to 3D (2 blocks, 3 rows, 2 columns):")
print(arr_3d)

# Use -1: NumPy calculates that dimension for us.
# Here we ask for 4 rows and let NumPy work out the columns (3).
arr_auto = arr_1d.reshape(4, -1)
print("Reshaped with -1 (4 rows, columns worked out):")
print(arr_auto)

# flatten() returns a 1D copy of the array.
flat = arr_2d.flatten()
print("flatten() of the 2D array:", flat)

# ravel() returns a 1D view of the array (shares data when possible).
raveled = arr_2d.ravel()
print("ravel() of the 2D array:", raveled)

# Sample output:
# Original 1D array: [ 1  2  3  4  5  6  7  8  9 10 11 12]
# Reshaped to 2D (3 rows, 4 columns):
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
# Reshaped to 3D (2 blocks, 3 rows, 2 columns):
# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]]
#
#  [[ 7  8]
#   [ 9 10]
#   [11 12]]]
# Reshaped with -1 (4 rows, columns worked out):
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
# flatten() of the 2D array: [ 1  2  3  4  5  6  7  8  9 10 11 12]
# ravel() of the 2D array: [ 1  2  3  4  5  6  7  8  9 10 11 12]
