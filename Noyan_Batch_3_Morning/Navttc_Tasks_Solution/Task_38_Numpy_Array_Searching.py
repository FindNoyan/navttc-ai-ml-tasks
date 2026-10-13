# Task 38 - NumPy: Array Searching
# Source: https://www.w3schools.com/python/numpy_array_search.asp
# This example shows how to find elements with np.where() and how to
# find insertion points (where a value would fit in sorted order)
# with searchsorted().

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
print("Array:", arr)

# np.where() returns the indexes where a condition is True.
positions_of_4 = np.where(arr == 4)
print("Indexes where the value is 4:", positions_of_4)

# We can also search for even numbers.
even_positions = np.where(arr % 2 == 0)
print("Indexes of even numbers:", even_positions)

# searchsorted() needs a SORTED array.
# It tells us where a value should be inserted to keep the order.
sorted_arr = np.array([1, 3, 5, 7])
print("Sorted array:", sorted_arr)
print("Where would 4 fit?", np.searchsorted(sorted_arr, 4))
print("Where would 6 fit?", np.searchsorted(sorted_arr, 6))

# With side="right", an existing value goes after the equal values.
print("Where would 5 fit with side='right'?",
      np.searchsorted(sorted_arr, 5, side="right"))
print("Where would 5 fit with side='left' (default)?",
      np.searchsorted(sorted_arr, 5, side="left"))

# Sample output:
# Array: [1 2 3 4 5 4 4]
# Indexes where the value is 4: (array([3, 5, 6]),)
# Indexes of even numbers: (array([1, 3, 5, 6]),)
# Sorted array: [1 3 5 7]
# Where would 4 fit? 2
# Where would 6 fit? 3
# Where would 5 fit with side='right'? 3
# Where would 5 fit with side='left' (default)? 2
