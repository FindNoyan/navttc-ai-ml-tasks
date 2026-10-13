# Task 29 - NumPy: Array Indexing
# Source: https://www.w3schools.com/python/numpy_array_indexing.asp
# This example shows how to access single elements in 1D and 2D
# arrays, including negative indexing (counting from the end).

import numpy as np

# 1D array: indexing starts at 0
arr_1d = np.array([10, 20, 30, 40])
print("1D array:", arr_1d)
print("First element (index 0):", arr_1d[0])
print("Third element (index 2):", arr_1d[2])
print("Last element (index -1):", arr_1d[-1])
print("Second last element (index -2):", arr_1d[-2])

# 2D array: use [row, column] to pick one element
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:")
print(arr_2d)
print("Element at row 0, column 0:", arr_2d[0, 0])
print("Element at row 0, column 2:", arr_2d[0, 2])
print("Element at row 1, column 1:", arr_2d[1, 1])
print("Last element using negative indexing:", arr_2d[-1, -1])

# Sample output:
# 1D array: [10 20 30 40]
# First element (index 0): 10
# Third element (index 2): 30
# Last element (index -1): 40
# Second last element (index -2): 30
# 2D array:
# [[1 2 3]
#  [4 5 6]]
# Element at row 0, column 0: 1
# Element at row 0, column 2: 3
# Element at row 1, column 1: 5
# Last element using negative indexing: 6
