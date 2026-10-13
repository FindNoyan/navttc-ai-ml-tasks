# Task 36 - NumPy: Array Joining
# Source: https://www.w3schools.com/python/numpy_array_join.asp
# This example shows how to join arrays with concatenate(), stack(),
# hstack() (side by side), and vstack() (one on top of the other).

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# concatenate() joins arrays end to end along an axis (axis 0 by default).
joined = np.concatenate((arr1, arr2))
print("concatenate():", joined)

# stack() joins arrays along a NEW axis.
# axis=0 stacks them as rows of a 2D array.
stacked = np.stack((arr1, arr2), axis=0)
print("stack() along a new axis:")
print(stacked)

# hstack() stacks arrays horizontally (side by side).
h_stacked = np.hstack((arr1, arr2))
print("hstack() side by side:", h_stacked)

# vstack() stacks arrays vertically (one on top of the other).
v_stacked = np.vstack((arr1, arr2))
print("vstack() one on top of the other:")
print(v_stacked)

# Sample output:
# concatenate(): [1 2 3 4 5 6]
# stack() along a new axis:
# [[1 2 3]
#  [4 5 6]]
# hstack() side by side: [1 2 3 4 5 6]
# vstack() one on top of the other:
# [[1 2 3]
#  [4 5 6]]
