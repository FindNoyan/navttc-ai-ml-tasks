# Task 41 - Pandas Basics
# Source: https://www.w3schools.com/python/pandas_tutorial.asp
# This example shows what pandas is and how to create a simple DataFrame
# (a table of rows and columns) from a dictionary, then inspect it.

# Pandas is a Python library for working with tabular data
# (rows and columns, like a spreadsheet or a database table).
# Its two main data structures are Series (one column) and
# DataFrame (a whole table). We use DataFrame here.

import pandas as pd

# Small inline dataset: students and their marks.
# A dictionary maps each column name to a list of values.
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Bilal"],
    "Subject": ["Math", "Math", "Math", "Math", "Math"],
    "Marks": [85, 92, 78, 88, 65]
}

# Create a DataFrame (table) from the dictionary.
df = pd.DataFrame(data)

# Print the whole table.
print("Full DataFrame:")
print(df)
print()

# head() shows the first 5 rows (default). Useful for a quick peek.
print("head() - first rows:")
print(df.head())
print()

# describe() gives summary statistics for the numeric columns,
# such as count, mean, min, and max.
print("describe() - summary statistics:")
print(df.describe())
print()

# info() shows the column names, data types, and non-null counts.
print("info() - structure of the DataFrame:")
print(df.info())

# Sample output:
# Full DataFrame:
#      Name Subject  Marks
# 0     Ali    Math     85
# 1    Sara    Math     92
# 2   Ahmed    Math     78
# 3  Ayesha    Math     88
# 4   Bilal    Math     65
#
# head() - first rows:
#      Name Subject  Marks
# 0     Ali    Math     85
# 1    Sara    Math     92
# 2   Ahmed    Math     78
# 3  Ayesha    Math     88
# 4   Bilal    Math     65
#
# describe() - summary statistics:
#            Marks
# count   5.000000
# mean   81.600000
# std    10.597169
# min    65.000000
# 25%    78.000000
# 50%    85.000000
# 75%    88.000000
# max    92.000000
#
# info() - structure of the DataFrame:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5 entries, 0 to 4
# Data columns (total 3 columns):
#  #   Column   Non-Null Count  Dtype
# ---  ------   --------------  -----
#  0   Name     5 non-null      object
#  1   Subject  5 non-null      object
#  2   Marks    5 non-null      int64
# dtypes: int64(1), object(2)
# memory usage: 252.0+ bytes
# None
