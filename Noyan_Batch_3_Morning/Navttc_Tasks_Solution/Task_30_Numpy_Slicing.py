# Task 30 - NumPy: Array Slicing
# Source: https://www.w3schools.com/python/numpy_array_slicing.asp
# This example shows how to slice (take a part of) 1D and 2D arrays,
# including steps and negative slicing.

import numpy as np

# 1D slicing: arr[start:stop:step]
# The start is included, the stop is NOT included.
arr_1d = np.array([1, 2, 3, 4, 5, 6, 7])
print("1D array:", arr_1d)
print("Slice [1:5]:", arr_1d[1:5])
print("Slice from start to index 4 [:4]:", arr_1d[:4])
print("Slice from index 4 to end [4:]:", arr_1d[4:])
print("Every second element [::2]:", arr_1d[::2])
print("Reversed with negative step [::-1]:", arr_1d[::-1])
print("Negative slice [-3:-1]:", arr_1d[-3:-1])

# 2D slicing: arr[row_start:row_stop, column_start:column_stop]
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D array:")
print(arr_2d)
print("First two rows, first two columns [0:2, 0:2]:")
print(arr_2d[0:2, 0:2])
print("All rows, column 1 [:, 1]:", arr_2d[:, 1])
print("Row 1, all columns [1, :]:", arr_2d[1, :])

# Sample output:
# 1D array: [1 2 3 4 5 6 7]
# Slice [1:5]: [2 3 4 5]
# Slice from start to index 4 [:4]: [1 2 3 4]
# Slice from index 4 to end [4:]: [5 6 7]
# Every second element [::2]: [1 3 5 7]
# Reversed with negative step [::-1]: [7 6 5 4 3 2 1]
# Negative slice [-3:-1]: [5 6]
# 2D array:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# First two rows, first two columns [0:2, 0:2]:
# [[1 2]
#  [4 5]]
# All rows, column 1 [:, 1]: [2 5 8]
# Row 1, all columns [1, :]: [4 5 6]
