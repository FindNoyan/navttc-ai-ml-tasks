# Task 10 — Tuples Basics
# Source: Week 1 syllabus, AI_NAVTTC_Outline_Tasks.pdf
# This example shows tuple basics — create, index, unpacking — and a
# try/except demo proving a tuple cannot be changed (it is immutable).

# --- Create a tuple ---
# A tuple uses round brackets ( ) and looks like a list,
# but it CANNOT be changed after it is created.
student = ("Noyan", 20, "AI/ML")
print("Student tuple:", student)

# --- Indexing: same as lists (counting starts at 0) ---
print("Name [0]:", student[0])
print("Age [1]:", student[1])
print("Course [2]:", student[2])
print("Last item [-1]:", student[-1])

# --- Slicing: get part of a tuple ---
print("First two items [0:2]:", student[0:2])

# --- len(): how many items are in the tuple ---
print("Number of items:", len(student))

# --- Unpacking: split a tuple into separate variables in one line ---
# The number of variables must match the number of items.
name, age, course = student
print("Unpacked name:", name)
print("Unpacked age:", age)
print("Unpacked course:", course)

# --- Tuples cannot be changed ---
# Trying to change an item raises a TypeError. We catch it and
# print a friendly message instead of crashing.
try:
    student[0] = "Ali"
except TypeError as error:
    print("Cannot change a tuple! Error:", error)

# Proof the tuple is still unchanged:
print("Student tuple after the attempt:", student)

# Sample output:
# Student tuple: ('Noyan', 20, 'AI/ML')
# Name [0]: Noyan
# Age [1]: 20
# Course [2]: AI/ML
# Last item [-1]: AI/ML
# First two items [0:2]: ('Noyan', 20)
# Number of items: 3
# Unpacked name: Noyan
# Unpacked age: 20
# Unpacked course: AI/ML
# Cannot change a tuple! Error: 'tuple' object does not support item assignment
# Student tuple after the attempt: ('Noyan', 20, 'AI/ML')
