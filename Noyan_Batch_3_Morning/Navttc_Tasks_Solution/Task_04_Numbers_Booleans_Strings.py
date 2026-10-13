# Task 04 — Numbers, Booleans and Strings
# Source: Week 1 syllabus, AI_NAVTTC_Outline_Tasks.pdf
# This example shows int, float, complex numbers, booleans and strings,
# and uses type() to show what kind of value each variable holds.

# int: a whole number (no decimal point).
age = 20

# float: a number with a decimal point.
height = 5.6

# complex: a number with a real part and an imaginary part (ends with j).
complex_number = 3 + 4j

# bool (boolean): only True or False. Used for yes/no questions.
is_student = True
has_passed = False

# str (string): text inside single or double quotes.
name = "Noyan"
course = 'AI/ML'

# type() tells us the data type of a value.
print("age =", age, "-> type:", type(age))
print("height =", height, "-> type:", type(height))
print("complex_number =", complex_number, "-> type:", type(complex_number))
print("is_student =", is_student, "-> type:", type(is_student))
print("has_passed =", has_passed, "-> type:", type(has_passed))
print("name =", name, "-> type:", type(name))
print("course =", course, "-> type:", type(course))

# Sample output:
# age = 20 -> type: <class 'int'>
# height = 5.6 -> type: <class 'float'>
# complex_number = (3+4j) -> type: <class 'complex'>
# is_student = True -> type: <class 'bool'>
# has_passed = False -> type: <class 'bool'>
# name = Noyan -> type: <class 'str'>
# course = AI/ML -> type: <class 'str'>
