# Task 44 - Pandas DataFrame
# Source: https://www.w3schools.com/python/pandas_dataframes.asp
# This example shows how to create a DataFrame from a dictionary, list
# its columns, read rows with loc[] and iloc[], and add a new column.

# A DataFrame is a two-dimensional table: rows and columns,
# like a spreadsheet. Each column is a Series.

import pandas as pd

# Create a DataFrame from a dictionary.
# Each key becomes a column name; each list becomes that column.
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha"],
    "Subject": ["Math", "Math", "Math", "Math"],
    "Marks": [85, 92, 78, 88]
}
df = pd.DataFrame(data)

print("Full DataFrame:")
print(df)
print()

# The columns attribute lists all column names.
print("Column names (df.columns):")
print(df.columns.tolist())
print()

# loc[] selects rows by LABEL (the index value).
# Row 0 is Ali's row.
print("Row 0 with loc[] (by label):")
print(df.loc[0])
print()

# loc[] can also select a single cell: row label, then column name.
print("One cell with loc[] - df.loc[1, 'Marks'] (Sara's marks):")
print(df.loc[1, "Marks"])
print()

# iloc[] selects rows by POSITION (0 = first row, 1 = second row...).
# Here position 2 is Ahmed's row, the same row as label 2.
print("Row at position 2 with iloc[] (by position):")
print(df.iloc[2])
print()

# Add a new column: Result is "Pass" if Marks >= 50, else "Fail".
# This works on the whole column at once, row by row.
df["Result"] = ["Pass" if mark >= 50 else "Fail" for mark in df["Marks"]]

print("DataFrame after adding a new 'Result' column:")
print(df)

# Sample output:
# Full DataFrame:
#      Name Subject  Marks
# 0     Ali    Math     85
# 1    Sara    Math     92
# 2   Ahmed    Math     78
# 3  Ayesha    Math     88
#
# Column names (df.columns):
# ['Name', 'Subject', 'Marks']
#
# Row 0 with loc[] (by label):
# Name        Ali
# Subject    Math
# Marks        85
# Name: 0, dtype: object
#
# One cell with loc[] - df.loc[1, 'Marks'] (Sara's marks):
# 92
#
# Row at position 2 with iloc[] (by position):
# Name       Ahmed
# Subject     Math
# Marks         78
# Name: 2, dtype: object
#
# DataFrame after adding a new 'Result' column:
#      Name Subject  Marks Result
# 0     Ali    Math     85   Pass
# 1    Sara    Math     92   Pass
# 2   Ahmed    Math     78   Pass
# 3  Ayesha    Math     88   Pass
