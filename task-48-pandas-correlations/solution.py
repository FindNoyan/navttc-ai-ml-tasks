# Task 48 - Pandas Correlations
# Source: https://www.w3schools.com/python/pandas_correlations.asp
# This example shows how to measure correlation between numeric columns
# with df.corr(), using study hours, exam marks, and sleep hours.

# Correlation measures how two columns move together, on a scale
# from -1 to +1:
#   Near +1: when one goes up, the other usually goes up too
#            (for example, more study hours -> higher marks).
#   Near -1: when one goes up, the other usually goes down
#            (for example, more study hours -> less free time).
#   Near  0: no clear straight-line relationship between the two.
# Correlation does NOT prove that one thing causes the other;
# it only says the two tend to move together.

import pandas as pd

# Small inline dataset: each row is one student.
data = {
    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [35, 42, 50, 55, 62, 70, 78, 85],
    "SleepHours": [8, 8, 7, 7, 6, 6, 5, 5]
}
df = pd.DataFrame(data)

print("DataFrame:")
print(df)
print()

# corr() returns a table where each cell is the correlation
# between one row column and one column column.
print("Correlation matrix (df.corr()):")
print(df.corr())
print()

# Read single pairs out of the table for a plain-English summary.
print("StudyHours vs Marks (strong positive, near +1):")
print(df["StudyHours"].corr(df["Marks"]))
print()
print("StudyHours vs SleepHours (strong negative, near -1):")
print(df["StudyHours"].corr(df["SleepHours"]))

# Sample output:
# DataFrame:
#    StudyHours  Marks  SleepHours
# 0           1     35           8
# 1           2     42           8
# 2           3     50           7
# 3           4     55           7
# 4           5     62           6
# 5           6     70           6
# 6           7     78           5
# 7           8     85           5
#
# Correlation matrix (df.corr()):
#             StudyHours     Marks  SleepHours
# StudyHours    1.000000  0.998966 -0.975900
# Marks         0.998966  1.000000 -0.977341
# SleepHours   -0.975900 -0.977341  1.000000
#
# StudyHours vs Marks (strong positive, near +1):
# 0.9989662776940782
#
# StudyHours vs SleepHours (strong negative, near -1):
# -0.9759000729485332
