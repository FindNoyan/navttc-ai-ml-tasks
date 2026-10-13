# Task 03 — Values, Expressions and Statements
# Source: Week 1 syllabus, AI_NAVTTC_Outline_Tasks.pdf
# This example shows assignment statements, expressions, and printing results
# by calculating a student's total and average marks.

# An assignment statement stores a VALUE in a variable.
# The part on the right is an EXPRESSION that Python calculates first.
english_marks = 78
math_marks = 85
science_marks = 92

# An expression combines values with operators (+, -, *, /).
# Here we add three marks to get the total.
total_marks = english_marks + math_marks + science_marks

# Another expression: divide the total by 3 to get the average.
average_marks = total_marks / 3

# A statement that prints (shows) a result on the screen.
print("English:", english_marks)
print("Math:", math_marks)
print("Science:", science_marks)
print("Total marks:", total_marks)
print("Average marks:", average_marks)

# We can also print an expression directly, without storing it first.
print("Total + 10 bonus marks:", total_marks + 10)

# Sample output:
# English: 78
# Math: 85
# Science: 92
# Total marks: 255
# Average marks: 85.0
# Total + 10 bonus marks: 265
