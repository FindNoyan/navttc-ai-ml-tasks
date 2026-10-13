# Task 31 - NumPy: Data Types
# Source: https://www.w3schools.com/python/numpy_data_types.asp
# This example shows how to check an array's data type with .dtype
# and how to convert it to another type with astype().

import numpy as np

# NumPy guesses the data type from the values we give it.
arr_int = np.array([1, 2, 3])
print("Integer array:", arr_int)
print("Data type:", arr_int.dtype)

arr_float = np.array([1.5, 2.5, 3.5])
print("Float array:", arr_float)
print("Data type:", arr_float.dtype)

arr_string = np.array(["apple", "banana", "cherry"])
print("String array:", arr_string)
print("Data type:", arr_string.dtype)

# We can set the data type when creating the array.
arr_forced = np.array([1, 2, 3], dtype="float")
print("Array created with dtype='float':", arr_forced)
print("Data type:", arr_forced.dtype)

# Convert an existing array to a new type with astype().
arr_to_int = arr_float.astype(int)
print("Float array converted to int:", arr_to_int)
print("Data type:", arr_to_int.dtype)

arr_to_float = arr_int.astype(float)
print("Int array converted to float:", arr_to_float)
print("Data type:", arr_to_float.dtype)

# Sample output:
# Integer array: [1 2 3]
# Data type: int64
# Float array: [1.5 2.5 3.5]
# Data type: float64
# String array: ['apple' 'banana' 'cherry']
# Data type: <U6
# Array created with dtype='float': [1. 2. 3.]
# Data type: float64
# Float array converted to int: [1 2 3]
# Data type: int64
# Int array converted to float: [1. 2. 3.]
# Data type: float64
