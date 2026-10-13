# Task 32 - NumPy: Copy vs View
# Source: https://www.w3schools.com/python/numpy_copy_vs_view.asp
# This example shows the difference between copy(), view(), and plain
# assignment: changing the original affects a view and an assignment,
# but NOT a copy.

import numpy as np

original = np.array([1, 2, 3, 4])
print("Original array:", original)

# copy() makes a brand new, independent array.
copy_arr = original.copy()

# view() makes a new array object that shares the same data.
view_arr = original.view()

# Plain assignment only gives a new name to the SAME array.
assigned_arr = original

# Change the first element of the original array.
original[0] = 99

print("After changing original[0] to 99:")
print("Original:", original)
print("Copy (not affected):", copy_arr)
print("View (affected, shares data):", view_arr)
print("Assigned (affected, same array):", assigned_arr)

# We can also check whether an array owns its data with .base.
# If .base is None, the array owns its data (a copy).
# If .base is not None, it shares data with another array (a view).
print("Copy owns its data (base is None):", copy_arr.base is None)
print("View shares data (base is not None):", view_arr.base is not None)

# Sample output:
# Original array: [1 2 3 4]
# After changing original[0] to 99:
# Original: [99  2  3  4]
# Copy (not affected): [1 2 3 4]
# View (affected, shares data): [99  2  3  4]
# Assigned (affected, same array): [99  2  3  4]
# Copy owns its data (base is None): True
# View shares data (base is not None): True
