# Task 15 - For Loops in Python
# Source: https://www.geeksforgeeks.org/python-for-loops/
# This example shows three common ways to use a for loop:
# looping over a list, looping over range(), and looping with enumerate().

# Example 1: for loop over a list
# The loop visits each item in the list, one by one.
fruits = ["apple", "banana", "mango", "orange"]

print("Fruits in the list:")
for fruit in fruits:
    print(fruit)

print()  # Blank line to separate the examples

# Example 2: for loop over range()
# range(1, 6) gives the numbers 1, 2, 3, 4, 5.
# The last number (6) is not included.
print("Numbers from 1 to 5 using range():")
for number in range(1, 6):
    print(number)

print()  # Blank line to separate the examples

# Example 3: for loop with enumerate()
# enumerate() gives us both the position (index) and the item.
# Index starts at 0 by default.
print("Fruits with their position using enumerate():")
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Sample output:
# Fruits in the list:
# apple
# banana
# mango
# orange
#
# Numbers from 1 to 5 using range():
# 1
# 2
# 3
# 4
# 5
#
# Fruits with their position using enumerate():
# 0 apple
# 1 banana
# 2 mango
# 3 orange
