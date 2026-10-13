# Task 22 - Tuple Operations in Python
# Source: https://www.programiz.com/python-programming/tuple
# This example shows tuple operations: count(), index(), concatenation,
# repetition, unpacking, and returning a tuple from a function.
# A tuple is like a list, but it cannot be changed after it is created.

# Create a tuple of favourite colours.
colours = ("red", "blue", "green", "blue", "yellow")
print("Tuple:", colours)

# count() - how many times a value appears in the tuple
print("Count of 'blue':", colours.count("blue"))

# index() - position (index) of the first occurrence of a value
print("Index of 'green':", colours.index("green"))

# Concatenation (+) - joining two tuples makes a NEW tuple
more_colours = ("purple", "orange")
all_colours = colours + more_colours
print("After concatenation:", all_colours)

# Repetition (*) - repeating a tuple makes a NEW tuple
repeated = ("red", "blue") * 2
print("After repetition:", repeated)

# Unpacking - assigning each tuple item to its own variable
# The number of variables must match the number of items.
point = (3, 4)
x, y = point
print("Unpacked point:", "x =", x, "y =", y)

# Returning a tuple from a function
# A function can return several values at once as one tuple.
def get_min_max(numbers):
    # min() gives the smallest value, max() gives the largest value.
    return (min(numbers), max(numbers))

scores = [55, 90, 70, 85]
smallest, largest = get_min_max(scores)
print("Scores:", scores)
print("Smallest:", smallest, "Largest:", largest)

# Tuples cannot be changed - the line below would give an error,
# so it is left as a comment:
# colours[0] = "pink"  # TypeError: 'tuple' object does not support item assignment

# Sample output:
# Tuple: ('red', 'blue', 'green', 'blue', 'yellow')
# Count of 'blue': 2
# Index of 'green': 2
# After concatenation: ('red', 'blue', 'green', 'blue', 'yellow', 'purple', 'orange')
# After repetition: ('red', 'blue', 'red', 'blue')
# Unpacked point: x = 3 y = 4
# Scores: [55, 90, 70, 85]
# Smallest: 55 Largest: 90
