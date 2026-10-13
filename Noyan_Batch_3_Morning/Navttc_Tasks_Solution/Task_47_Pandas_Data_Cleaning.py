# Task 47 - Pandas Data Cleaning
# Source: https://www.w3schools.com/python/pandas_cleaning.asp
# This example shows basic data cleaning: handling missing values,
# removing a duplicate row, replacing a wrong value, and dropping a
# column you do not need. It prints the table before and after.

import pandas as pd

# Small messy dataset on purpose:
# - Sara's marks are missing (None).
# - Ali's row appears twice (a duplicate).
# - "Maths" is spelled differently from "Math" (an inconsistent value).
# - The Notes column is extra information we do not need.
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ali", "Ayesha"],
    "Subject": ["Math", "Math", "Maths", "Math", "Math"],
    "Marks": [85, None, 78, 85, 88],
    "Notes": ["ok", "ok", "ok", "ok", "ok"]
}
df = pd.DataFrame(data)

print("BEFORE cleaning:")
print(df)
print()

# Step 1 - Handle missing values.
# dropna() would delete rows with missing values.
# fillna() keeps the row and fills the gap instead.
# Here we fill Sara's missing marks with the average of the other marks,
# because deleting a student just for one missing value wastes data.
average_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(average_marks)
print("After fillna() - missing Marks filled with the average:")
print(df)
print()

# Step 2 - Remove duplicate rows.
# drop_duplicates() keeps the first copy and deletes the rest.
df = df.drop_duplicates()
print("After drop_duplicates() - the repeated Ali row is gone:")
print(df)
print()

# Step 3 - Fix an inconsistent value.
# replace() changes "Maths" to "Math" so all subjects match.
df["Subject"] = df["Subject"].replace("Maths", "Math")
print("After replace() - 'Maths' fixed to 'Math':")
print(df)
print()

# Step 4 - Drop a column we do not need.
# drop(columns=[...]) removes the Notes column.
df = df.drop(columns=["Notes"])
print("AFTER cleaning - Notes column dropped:")
print(df)

# Sample output:
# BEFORE cleaning:
#     Name Subject  Marks Notes
# 0    Ali    Math   85.0    ok
# 1   Sara    Math    NaN    ok
# 2  Ahmed   Maths   78.0    ok
# 3    Ali    Math   85.0    ok
# 4  Ayesha    Math   88.0    ok
#
# After fillna() - missing Marks filled with the average:
#     Name Subject  Marks Notes
# 0    Ali    Math  85.0    ok
# 1   Sara    Math  84.0    ok
# 2  Ahmed   Maths  78.0    ok
# 3    Ali    Math  85.0    ok
# 4  Ayesha    Math  88.0    ok
#
# After drop_duplicates() - the repeated Ali row is gone:
#     Name Subject  Marks Notes
# 0    Ali    Math  85.0    ok
# 1   Sara    Math  84.0    ok
# 2  Ahmed   Maths  78.0    ok
# 4  Ayesha    Math  88.0    ok
#
# After replace() - 'Maths' fixed to 'Math':
#     Name Subject  Marks Notes
# 0    Ali    Math  85.0    ok
# 1   Sara    Math  84.0    ok
# 2  Ahmed    Math  78.0    ok
# 4  Ayesha    Math  88.0    ok
#
# AFTER cleaning - Notes column dropped:
#     Name Subject  Marks
# 0    Ali    Math  85.0
# 1   Sara    Math  84.0
# 2  Ahmed    Math  78.0
# 4  Ayesha    Math  88.0
