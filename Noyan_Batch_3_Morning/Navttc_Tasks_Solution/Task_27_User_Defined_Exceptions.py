# Task 27 - User Defined Exceptions in Python
# Source: https://www.programiz.com/python-programming/user-defined-exception
# This example defines a custom exception class that inherits from
# Exception, raises it when an age is too small, and catches it.

# 1. Define a custom exception class.
# It inherits from Exception, so Python treats it like any other error.
class AgeTooSmallError(Exception):
    # A short message explaining the problem.
    pass

# 2. A function that checks the age and raises our custom error.
def check_age(age):
    if age < 18:
        # raise creates the error and stops the function here.
        raise AgeTooSmallError("Age must be 18 or older to register.")
    return "Registration allowed. Welcome!"

# 3. Catch the custom exception with try/except.
print("Example 1: age 15 (too small)")
try:
    message = check_age(15)
    print(message)
except AgeTooSmallError as error:
    print("Caught AgeTooSmallError:", error)

print()
print("Example 2: age 22 (old enough)")
try:
    message = check_age(22)
    print(message)
except AgeTooSmallError as error:
    print("Caught AgeTooSmallError:", error)

print()
print("Done. The program kept running after catching the error.")

# Sample output:
# Example 1: age 15 (too small)
# Caught AgeTooSmallError: Age must be 18 or older to register.
#
# Example 2: age 22 (old enough)
# Registration allowed. Welcome!
#
# Done. The program kept running after catching the error.
