# Task 33 - NumPy: Array Shape
# Source: https://www.w3schools.com/python/numpy_array_shape.asp
# This example shows .shape (size of each dimension), .ndim (number of
# dimensions), and .size (total number of elements) for 1D, 2D and 3D arrays.

import numpy as np

# 1D array: 5 elements in one row
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D array:", arr_1d)
print("Shape:", arr_1d.shape)
print("Number of dimensions (ndim):", arr_1d.ndim)
print("Total elements (size):", arr_1d.size)
print()

# 2D array: 2 rows, 3 columns
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:")
print(arr_2d)
print("Shape:", arr_2d.shape)
print("Number of dimensions (ndim):", arr_2d.ndim)
print("Total elements (size):", arr_2d.size)
print()

# 3D array: 2 blocks, each with 2 rows and 3 columns
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("3D array:")
print(arr_3d)
print("Shape:", arr_3d.shape)
print("Number of dimensions (ndim):", arr_3d.ndim)
print("Total elements (size):", arr_3d.size)

# Sample output:
# 1D array: [1 2 3 4 5]
# Shape: (5,)
# Number of dimensions (ndim): 1
# Total elements (size): 5
#
# 2D array:
# [[1 2 3]
#  [4 5 6]]
# Shape: (2, 3)
# Number of dimensions (ndim): 2
# Total elements (size): 6
#
# 3D array:
# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[ 7  8  9]
#   [10 11 12]]]
# Shape: (2, 2, 3)
# Number of dimensions (ndim): 3
# Total elements (size): 12
