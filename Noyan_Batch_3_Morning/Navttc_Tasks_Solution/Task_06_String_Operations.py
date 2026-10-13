# Task 06 — String Operations
# Source: Week 1 syllabus, AI_NAVTTC_Outline_Tasks.pdf
# This example shows concatenation, repetition, slicing, upper/lower, strip,
# replace, split, and f-strings using a student's name and course.

# --- Concatenation: joining strings with + ---
first_name = "Noyan"
last_name = "Khan"
full_name = first_name + " " + last_name
print("Full name (concatenation):", full_name)

# --- Repetition: repeating a string with * ---
print("Repetition:", "Hi! " * 3)

# --- Slicing: taking part of a string with [start:end] ---
# Counting starts at 0. [0:5] means characters 0,1,2,3,4.
course = "Artificial Intelligence"
print("Course:", course)
print("First 10 characters [0:10]:", course[0:10])
print("From index 11 onwards [11:]:", course[11:])
print("Last 4 characters [-4:]:", course[-4:])

# --- upper() and lower(): change the case of a string ---
message = "Hello, Python"
print("Original:", message)
print("upper():", message.upper())
print("lower():", message.lower())

# --- strip(): remove spaces from both ends of a string ---
messy = "   hello world   "
print("Before strip: '" + messy + "'")
print("After strip: '" + messy.strip() + "'")

# --- replace(): swap one piece of text for another ---
sentence = "I like Java"
print("Before replace:", sentence)
print("After replace:", sentence.replace("Java", "Python"))

# --- split(): break a string into a list of words ---
subjects = "Math, English, Science"
print("Split by comma:", subjects.split(","))

# --- f-strings: put variables inside a string with { } ---
name = "Noyan"
marks = 85
print(f"{name} scored {marks} marks in the test.")
print(f"{name} scored {marks + 5} marks after 5 bonus marks.")

# Sample output:
# Full name (concatenation): Noyan Khan
# Repetition: Hi! Hi! Hi!
# Course: Artificial Intelligence
# First 10 characters [0:10]: Artificial
# From index 11 onwards [11:]: Intelligence
# Last 4 characters [-4:]: ence
# Original: Hello, Python
# upper(): HELLO, PYTHON
# lower(): hello, python
# Before strip: '   hello world   '
# After strip: 'hello world'
# Before replace: I like Java
# After replace: I like Python
# Split by comma: ['Math', ' English', ' Science']
# Noyan scored 85 marks in the test.
# Noyan scored 90 marks after 5 bonus marks.
