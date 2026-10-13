# Task 26 - Exception Handling in Python
# Source: https://www.programiz.com/python-programming/exception-handling
# This example shows try/except/else/finally using a safe division
# function, with ZeroDivisionError and ValueError examples.

def safe_divide(a, b):
    # try: put the risky code here.
    try:
        result = a / b
    # except: runs only if a matching error happens.
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    # else: runs only if NO error happened in try.
    else:
        print("Division worked, no error.")
        return result
    # finally: ALWAYS runs, whether there was an error or not.
    finally:
        print("Finished this division attempt.")

print("Example 1: 10 / 2")
print("Result:", safe_divide(10, 2))

print()
print("Example 2: 10 / 0 (ZeroDivisionError)")
print("Result:", safe_divide(10, 0))

print()
# ValueError example: converting text that is not a number
print("Example 3: converting 'abc' to an integer (ValueError)")
try:
    number = int("abc")
    print("Converted number:", number)
except ValueError:
    print("Error: 'abc' is not a valid number!")
else:
    print("Conversion worked, no error.")
finally:
    print("Finished this conversion attempt.")

# Sample output:
# Example 1: 10 / 2
# Division worked, no error.
# Finished this division attempt.
# Result: 5.0
# 
# Example 2: 10 / 0 (ZeroDivisionError)
# Error: Cannot divide by zero!
# Finished this division attempt.
# Result: None
# 
# Example 3: converting 'abc' to an integer (ValueError)
# Error: 'abc' is not a valid number!
# Finished this conversion attempt.
