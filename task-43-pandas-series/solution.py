# Task 43 - Pandas Series
# Source: https://www.w3schools.com/python/pandas_series.asp
# This example shows how to create a Series from a list and from a
# dictionary, how to give it custom index labels, and how to read a
# value back by its label.

# A Series is a one-dimensional labeled array: one column of values,
# where each value has an index label (like a row name).

import pandas as pd

# 1) Series from a list.
# Without a custom index, pandas uses 0, 1, 2, ... as labels.
marks_list = [85, 92, 78, 88]
marks_series = pd.Series(marks_list)
print("Series from a list (default index 0, 1, 2, ...):")
print(marks_series)
print()

# 2) Series from a list with custom index labels.
# The index labels make each value easy to find by name.
marks_named = pd.Series(marks_list, index=["Ali", "Sara", "Ahmed", "Ayesha"])
print("Series from a list with custom index labels:")
print(marks_named)
print()

# 3) Access one value by its label.
print("Access by label - marks_named['Sara']:")
print(marks_named["Sara"])
print()

# 4) Series from a dictionary.
# The dictionary keys become the index labels automatically.
marks_dict = {"Ali": 85, "Sara": 92, "Ahmed": 78, "Ayesha": 88}
marks_from_dict = pd.Series(marks_dict)
print("Series from a dictionary (keys become the index):")
print(marks_from_dict)
print()

# 5) Access one value by label from the dict-based Series.
print("Access by label - marks_from_dict['Ahmed']:")
print(marks_from_dict["Ahmed"])

# Sample output:
# Series from a list (default index 0, 1, 2, ...):
# 0    85
# 1    92
# 2    78
# 3    88
# dtype: int64
#
# Series from a list with custom index labels:
# Ali       85
# Sara      92
# Ahmed     78
# Ayesha    88
# dtype: int64
#
# Access by label - marks_named['Sara']:
# 92
#
# Series from a dictionary (keys become the index):
# Ali       85
# Sara      92
# Ahmed     78
# Ayesha    88
# dtype: int64
#
# Access by label - marks_from_dict['Ahmed']:
# 78
