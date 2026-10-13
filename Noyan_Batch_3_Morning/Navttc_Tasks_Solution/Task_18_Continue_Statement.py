# Task 18 - Continue Statement in Python
# Source: https://www.geeksforgeeks.org/python-continue-statement/
# This example loops from 1 to 10 and uses continue to skip
# the even numbers, so only the odd numbers are printed.

print("Odd numbers from 1 to 10:")

for number in range(1, 11):
    # If the number is even, skip the rest of this round
    # and jump to the next number.
    if number % 2 == 0:
        continue
    print(number)

print("Done! Only odd numbers were printed.")

# Sample output:
# Odd numbers from 1 to 10:
# 1
# 3
# 5
# 7
# 9
# Done! Only odd numbers were printed.
