# Task 23 - String Methods in Python
# Source: https://www.programiz.com/python-programming/string
# This example shows string methods: find, replace, split, join,
# strip, startswith, and formatting with an f-string.

sentence = "  Python is fun, Python is easy  "
print("Original string:", repr(sentence))

# strip() - remove spaces from the start and end of the string
cleaned = sentence.strip()
print("After strip():", repr(cleaned))

# find() - position (index) of the first occurrence, or -1 if not found
print("find('fun'):", cleaned.find("fun"))
print("find('hard'):", cleaned.find("hard"))

# replace() - replace all occurrences of a word with a new word
replaced = cleaned.replace("Python", "Coding")
print("After replace('Python', 'Coding'):", replaced)

# split() - split a string into a list, using a separator
words = cleaned.split()
print("After split():", words)

# join() - join a list of words back into one string
joined = "-".join(words)
print("After '-'.join(words):", joined)

# startswith() - check if the string starts with given text (True/False)
print("startswith('Python'):", cleaned.startswith("Python"))
print("startswith('Java'):", cleaned.startswith("Java"))

# Formatting with an f-string - put variables inside a string
name = "Ali"
age = 20
message = f"My name is {name} and I am {age} years old."
print("Formatted with f-string:", message)

# Sample output:
# Original string: '  Python is fun, Python is easy  '
# After strip(): 'Python is fun, Python is easy'
# find('fun'): 10
# find('hard'): -1
# After replace('Python', 'Coding'): Coding is fun, Coding is easy
# After split(): ['Python', 'is', 'fun,', 'Python', 'is', 'easy']
# After '-'.join(words): Python-is-fun,-Python-is-easy
# startswith('Python'): True
# startswith('Java'): False
# Formatted with f-string: My name is Ali and I am 20 years old.
