# Task 07 — Input and Type Casting
# Source: Week 1 syllabus, AI_NAVTTC_Outline_Tasks.pdf
# This example shows input() with a safe fallback, and int()/float()/str()
# type casting by adding two numbers that start out as strings.

# --- input(): ask the user for text ---
# input() always gives back a STRING, even if the user types digits.
# The try/except below lets the file run without typing anything:
# if there is no user to type (EOFError), we use a default value instead.
try:
    user_name = input("Enter your name: ")
except EOFError:
    user_name = "Noyan"
print("Hello,", user_name + "!")

try:
    first_number_text = input("Enter first number: ")
except EOFError:
    first_number_text = "15"
try:
    second_number_text = input("Enter second number: ")
except EOFError:
    second_number_text = "25"

# --- Type casting: change a value from one type to another ---
# int() turns a string of digits into an integer.
first_number = int(first_number_text)
second_number = int(second_number_text)

# Without casting, "15" + "25" would join as text: "1525".
# With casting, 15 + 25 adds as numbers: 40.
print("As strings, joined:", first_number_text + second_number_text)
print("As numbers, added:", first_number + second_number)

# float() turns a string into a decimal number.
price_text = "99.5"
price = float(price_text)
print("Price as float:", price, "-> type:", type(price))

# str() turns a number into a string, so we can join it with other text.
total = first_number + second_number
result_message = "The total is " + str(total)
print(result_message)

# int() also works on a float: it drops the decimal part.
print("int(9.8) =", int(9.8))
print("float(10) =", float(10))

# Sample output:
# (If run without typing, the defaults Noyan, 15, 25 are used.)
# Hello, Noyan!
# As strings, joined: 1525
# As numbers, added: 40
# Price as float: 99.5 -> type: <class 'float'>
# The total is 40
# int(9.8) = 9
# float(10) = 10.0
