# Task 05 — Operators, Variables and Keywords
# Source: Week 1 syllabus, AI_NAVTTC_Outline_Tasks.pdf
# This example shows arithmetic, comparison, logical and assignment operators,
# good variable naming, and prints Python's reserved keywords.

import keyword

# --- Variable naming ---
# Good names are clear and use lowercase letters with underscores.
student_name = "Noyan"
total_marks = 85
# Variable names cannot start with a number, and cannot have spaces.
# Bad examples (do NOT use): 1name = "x", student name = "x"

# --- Arithmetic operators: + - * / % ** // ---
a = 10
b = 3
print("a =", a, ", b =", b)
print("a + b =", a + b)   # addition
print("a - b =", a - b)   # subtraction
print("a * b =", a * b)   # multiplication
print("a / b =", a / b)   # division (always gives a float)
print("a % b =", a % b)   # remainder (10 divided by 3 leaves 1)
print("a ** b =", a ** b)  # power (10 to the power 3)
print("a // b =", a // b)  # floor division (whole part only)

# --- Comparison operators: == != > < >= <= ---
# A comparison gives True or False.
print("a == b:", a == b)  # equal to?
print("a != b:", a != b)  # not equal to?
print("a > b:", a > b)    # greater than?
print("a < b:", a < b)    # less than?
print("a >= 10:", a >= 10)  # greater than or equal to?
print("a <= b:", a <= b)    # less than or equal to?

# --- Logical operators: and, or, not ---
# 'and' is True only if BOTH sides are True.
# 'or' is True if AT LEAST ONE side is True.
# 'not' flips True to False and False to True.
is_adult = True
has_id_card = False
print("is_adult and has_id_card:", is_adult and has_id_card)
print("is_adult or has_id_card:", is_adult or has_id_card)
print("not is_adult:", not is_adult)

# --- Assignment operators: = += -= *= /= ---
# These change a variable using its old value.
score = 50
print("Starting score:", score)
score += 10   # same as: score = score + 10
print("After score += 10:", score)
score -= 5    # same as: score = score - 5
print("After score -= 5:", score)
score *= 2    # same as: score = score * 2
print("After score *= 2:", score)
score /= 4    # same as: score = score / 4
print("After score /= 4:", score)

# --- Python keywords ---
# Keywords are words Python reserves (if, for, while, ...).
# We cannot use them as variable names.
print("Python keywords:")
print(keyword.kwlist)
print("Total number of keywords:", len(keyword.kwlist))

# Sample output:
# a = 10 , b = 3
# a + b = 13
# a - b = 7
# a * b = 30
# a / b = 3.3333333333333335
# a % b = 1
# a ** b = 1000
# a // b = 3
# a == b: False
# a != b: True
# a > b: True
# a < b: False
# a >= 10: True
# a <= b: False
# is_adult and has_id_card: False
# is_adult or has_id_card: True
# not is_adult: False
# Starting score: 50
# After score += 10: 60
# After score -= 5: 55
# After score *= 2: 110
# After score /= 4: 27.5
# Python keywords:
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# Total number of keywords: 35
