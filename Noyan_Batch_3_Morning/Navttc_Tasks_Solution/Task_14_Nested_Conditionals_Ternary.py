# Task 14 — Nested Conditionals and Ternary Operator
# Source: Week 1 syllabus, AI_NAVTTC_Outline_Tasks.pdf
# This example shows a nested if (an if inside another if) checking that a
# number is positive AND even, and a ternary / conditional expression that
# gives pass/fail in a single line.

# --- Part 1: Nested if ---
# A nested if means: only check the inner condition
# if the outer condition is already True.
number = 12
print("Number:", number)

if number > 0:
    # Outer if: the number is positive. Now check the inner condition.
    if number % 2 == 0:
        # Inner if: positive AND even.
        print(number, "is positive AND even.")
    else:
        # Inner else: positive but NOT even (odd).
        print(number, "is positive but odd.")
else:
    # Outer else: the number is zero or negative, so we never
    # check whether it is even.
    print(number, "is zero or negative.")

# Try a second example so the other branches are clear:
number2 = -7
print("Number:", number2)
if number2 > 0:
    if number2 % 2 == 0:
        print(number2, "is positive AND even.")
    else:
        print(number2, "is positive but odd.")
else:
    print(number2, "is zero or negative.")

# --- Part 2: Ternary / conditional expression ---
# Ternary means "three parts": value_if_true IF condition ELSE value_if_false.
# It gives an if/else answer in ONE line.
marks = 65
result = "Pass" if marks >= 50 else "Fail"
print("Marks:", marks, "-> Result:", result)

# The same idea written as a normal if/else would take 4 lines:
# if marks >= 50:
#     result = "Pass"
# else:
#     result = "Fail"

# Another ternary example: check pass/fail for a second student.
marks2 = 40
result2 = "Pass" if marks2 >= 50 else "Fail"
print("Marks:", marks2, "-> Result:", result2)

# Ternary can also be printed directly, without storing it first.
print("Student with 75 marks:", "Pass" if 75 >= 50 else "Fail")

# Sample output:
# Number: 12
# 12 is positive AND even.
# Number: -7
# -7 is zero or negative.
# Marks: 65 -> Result: Pass
# Marks: 40 -> Result: Fail
# Student with 75 marks: Pass
