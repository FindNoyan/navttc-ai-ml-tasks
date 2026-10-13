# Task 37 - NumPy: Array Splitting
# Source: https://www.w3schools.com/python/numpy_array_split.asp
# This example shows how to split an array with array_split(), and how
# to split a 2D array into left/right parts with hsplit() and into
# top/bottom parts with vsplit().

import numpy as np

# array_split() splits a 1D array into the number of parts we ask for.
arr = np.array([1, 2, 3, 4, 5, 6])
split_into_3 = np.array_split(arr, 3)
print("Original array:", arr)
print("Split into 3 parts:")
for part in split_into_3:
    print(part)

# If the array cannot be split evenly, some parts get one extra element.
split_into_4 = np.array_split(arr, 4)
print("Split into 4 parts (uneven):")
for part in split_into_4:
    print(part)

# 2D array for hsplit() and vsplit().
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("2D array:")
print(arr_2d)

# hsplit() splits horizontally into left and right parts.
left, right = np.hsplit(arr_2d, 2)
print("hsplit() left part:")
print(left)
print("hsplit() right part:")
print(right)

# vsplit() splits vertically into top and bottom parts.
top, bottom = np.vsplit(arr_2d, 2)
print("vsplit() top part:")
print(top)
print("vsplit() bottom part:")
print(bottom)

# Sample output:
# Original array: [1 2 3 4 5 6]
# Split into 3 parts:
# [1 2]
# [3 4]
# [5 6]
# Split into 4 parts (uneven):
# [1 2]
# [3 4]
# [5]
# [6]
# 2D array:
# [[1 2 3 4]
#  [5 6 7 8]]
# hsplit() left part:
# [[1 2]
#  [5 6]]
# hsplit() right part:
# [[3 4]
#  [7 8]]
# vsplit() top part:
# [[1 2 3 4]]
# vsplit() bottom part:
# [[5 6 7 8]]
