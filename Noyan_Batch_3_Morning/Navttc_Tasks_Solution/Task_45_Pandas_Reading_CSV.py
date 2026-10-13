# Task 45 - Pandas Reading CSV
# Source: https://www.w3schools.com/python/pandas_csv.asp
# This example shows how to read CSV (comma-separated values) data into
# a DataFrame. The CSV text is written inline with io.StringIO, so no
# file download or external file is needed.

# In real work you would write: pd.read_csv("students.csv")
# Here the same idea is shown with inline text, so this file
# runs anywhere without downloading anything.

import io

import pandas as pd

# Inline CSV text: first line = column names, then one row per line.
csv_text = """Name,Subject,Marks
Ali,Math,85
Sara,Math,92
Ahmed,Math,78
Ayesha,Math,88
Bilal,Math,65
Hira,English,90
Usman,English,74
"""

# StringIO makes the text behave like a file, so read_csv can read it.
# This is exactly like pd.read_csv("students.csv") for a real file.
df = pd.read_csv(io.StringIO(csv_text))

print("Full DataFrame read from CSV:")
print(df)
print()

# head() shows the first 5 rows - a quick peek at the start.
print("head() - first 5 rows:")
print(df.head())
print()

# tail() shows the last 5 rows - a quick peek at the end.
print("tail() - last 5 rows:")
print(df.tail())

# Sample output:
# Full DataFrame read from CSV:
#      Name  Subject  Marks
# 0     Ali     Math     85
# 1    Sara     Math     92
# 2   Ahmed     Math     78
# 3  Ayesha     Math     88
# 4   Bilal     Math     65
# 5    Hira  English     90
# 6   Usman  English     74
#
# head() - first 5 rows:
#      Name Subject  Marks
# 0     Ali    Math     85
# 1    Sara    Math     92
# 2   Ahmed    Math     78
# 3  Ayesha    Math     88
# 4   Bilal    Math     65
#
# tail() - last 5 rows:
#      Name  Subject  Marks
# 2   Ahmed     Math     78
# 3  Ayesha     Math     88
# 4   Bilal     Math     65
# 5    Hira  English     90
# 6   Usman  English     74
