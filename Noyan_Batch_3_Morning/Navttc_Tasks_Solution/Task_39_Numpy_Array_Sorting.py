# Task 39 - NumPy: Array Sorting
# Source: https://www.w3schools.com/python/numpy_array_sort.asp
# This example shows how to sort 1D and 2D arrays with np.sort() and
# how argsort() gives the indexes that would sort an array.

import numpy as np

# np.sort() returns a sorted copy; the original array is unchanged.
arr_1d = np.array([5, 2, 8, 1, 9])
print("Original 1D array:", arr_1d)
print("Sorted 1D array:", np.sort(arr_1d))
print("Original is unchanged:", arr_1d)

# Sorting strings puts them in alphabetical order.
arr_strings = np.array(["banana", "apple", "cherry"])
print("Sorted strings:", np.sort(arr_strings))

# For a 2D array, np.sort() sorts each row separately.
arr_2d = np.array([[3, 2, 1], [6, 5, 4]])
print("Original 2D array:")
print(arr_2d)
print("2D array with each row sorted:")
print(np.sort(arr_2d))

# argsort() returns the INDEXES that would sort the array.
# This is useful when we want to sort one array by another's order,
# for example sorting names by their scores.
scores = np.array([50, 90, 70])
names = np.array(["Ali", "Sara", "Bilal"])
order = np.argsort(scores)
print("Scores:", scores)
print("Indexes that would sort the scores:", order)
print("Names in score order (lowest to highest):", names[order])

# Sample output:
# Original 1D array: [5 2 8 1 9]
# Sorted 1D array: [1 2 5 8 9]
# Original is unchanged: [5 2 8 1 9]
# Sorted strings: ['apple' 'banana' 'cherry']
# Original 2D array:
# [[3 2 1]
#  [6 5 4]]
# 2D array with each row sorted:
# [[1 2 3]
#  [4 5 6]]
# Scores: [50 90 70]
# Indexes that would sort the scores: [0 2 1]
# Names in score order (lowest to highest): ['Ali' 'Bilal' 'Sara']
