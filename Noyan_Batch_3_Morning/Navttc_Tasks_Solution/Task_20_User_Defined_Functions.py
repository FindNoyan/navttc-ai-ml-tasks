# Task 20 - User Defined Functions in Python
# Source: https://www.geeksforgeeks.org/functions-in-python/
# This example shows how to define your own functions: parameters,
# return values, a default argument, local vs global scope,
# plus a small lambda with map() and filter().

# A global variable - it lives outside any function and can be
# read from anywhere in the file.
school_name = "Netsol"

# 1. A simple function with parameters and a return value
def add(a, b):
    # a and b are parameters. The function returns their sum.
    return a + b

print("add(3, 5) =", add(3, 5))

# 2. A function with a default argument
# If the caller does not pass a greeting, "Hello" is used.
def greet(name, greeting="Hello"):
    return greeting + ", " + name + "!"

print(greet("Ali"))
print(greet("Sara", "Assalam-o-Alaikum"))

# 3. Local vs global scope
def show_scope():
    # This variable is LOCAL - it only exists inside this function.
    local_message = "I am local to show_scope()"
    print(local_message)
    # This function can READ the global variable school_name.
    print("School (global):", school_name)

show_scope()
print("School (global, outside function):", school_name)
# print(local_message) would give an error here, because
# local_message only exists inside show_scope().

# 4. Lambda with map()
# lambda is a short, one-line function without a name.
# map() applies a function to every item in a list.
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print("Original numbers:", numbers)
print("Squared with map + lambda:", squared)

# 5. Lambda with filter()
# filter() keeps only the items where the function returns True.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers with filter + lambda:", even_numbers)

# Sample output:
# add(3, 5) = 8
# Hello, Ali!
# Assalam-o-Alaikum, Sara!
# I am local to show_scope()
# School (global): Netsol
# School (global, outside function): Netsol
# Original numbers: [1, 2, 3, 4, 5]
# Squared with map + lambda: [1, 4, 9, 16, 25]
# Even numbers with filter + lambda: [2, 4]
