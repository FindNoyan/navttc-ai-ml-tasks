# Task 46 - Pandas Analyzing Data
# Source: https://www.w3schools.com/python/pandas_analyzing.asp
# This example shows the basic steps for analyzing a DataFrame: peek at
# the rows, check the structure, get summary statistics, count values
# in a column, and find missing values.

import pandas as pd

# Small inline dataset. One marks value is missing (None),
# so we can see how pandas reports missing values.
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Bilal", "Hira", "Usman"],
    "Subject": ["Math", "Math", "Math", "Math", "Math", "English", "English"],
    "Marks": [85, 92, 78, 88, 65, 90, None]
}
df = pd.DataFrame(data)

# head() shows the first 5 rows.
print("head() - first 5 rows:")
print(df.head())
print()

# info() shows column names, data types, and non-null counts.
print("info() - structure of the DataFrame:")
print(df.info())
print()

# describe() gives summary statistics for numeric columns.
print("describe() - summary statistics:")
print(df.describe())
print()

# value_counts() counts how many times each value appears in a column.
print("value_counts() - number of students per Subject:")
print(df["Subject"].value_counts())
print()

# isnull().sum() counts the missing values in each column.
print("isnull().sum() - missing values per column:")
print(df.isnull().sum())

# Sample output:
# head() - first 5 rows:
#      Name Subject  Marks
# 0     Ali    Math   85.0
# 1    Sara    Math   92.0
# 2   Ahmed    Math   78.0
# 3  Ayesha    Math   88.0
# 4   Bilal    Math   65.0
#
# info() - structure of the DataFrame:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 7 entries, 0 to 6
# Data columns (total 3 columns):
#  #   Column   Non-Null Count  Dtype
# ---  ------   --------------  -----
#  0   Name     7 non-null      object
#  1   Subject  7 non-null      object
#  2   Marks    6 non-null      float64
# dtypes: float64(1), object(2)
# memory usage: 300.0+ bytes
# None
#
# describe() - summary statistics:
#            Marks
# count   6.000000
# mean   83.000000
# std    10.079683
# min    65.000000
# 25%    79.750000
# 50%    86.500000
# 75%    89.500000
# max    92.000000
#
# value_counts() - number of students per Subject:
# Subject
# Math       5
# English    2
# Name: count, dtype: int64
#
# isnull().sum() - missing values per column:
# Name       0
# Subject    0
# Marks      1
# dtype: int64
