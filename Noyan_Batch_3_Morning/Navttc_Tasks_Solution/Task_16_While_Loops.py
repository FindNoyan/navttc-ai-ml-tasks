# Task 16 - While Loops in Python
# Source: https://www.geeksforgeeks.org/python-while-loops/
# This example shows two while loops: a countdown from 5 to 1,
# and a loop that adds up the numbers from 1 to 10.

# Example 1: Countdown using a while loop
# The loop keeps running as long as the condition (count > 0) is True.
print("Countdown:")
count = 5
while count > 0:
    print(count)
    count = count - 1  # Decrease count by 1 each time

print("Blast off!")

print()  # Blank line to separate the examples

# Example 2: Sum of numbers from 1 to 10 using a while loop
total = 0
number = 1

while number <= 10:
    total = total + number  # Add the current number to the total
    number = number + 1     # Move to the next number

print("Sum of numbers from 1 to 10 is:", total)

# Sample output:
# Countdown:
# 5
# 4
# 3
# 2
# 1
# Blast off!
#
# Sum of numbers from 1 to 10 is: 55
