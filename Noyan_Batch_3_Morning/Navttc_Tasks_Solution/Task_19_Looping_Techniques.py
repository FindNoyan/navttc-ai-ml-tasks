# Task 19 - Looping Techniques in Python
# Source: https://www.geeksforgeeks.org/looping-techniques-python/
# This example shows five useful looping techniques:
# enumerate(), zip(), reversed(), sorted(), and looping over dict items.

# 1. enumerate() - get index and value together
print("1. enumerate():")
names = ["Ali", "Sara", "Ahmed"]
for index, name in enumerate(names):
    print(index, name)

print()

# 2. zip() - loop over two lists together, pair by pair
print("2. zip():")
subjects = ["Math", "English", "Science"]
marks = [85, 90, 78]
for subject, mark in zip(subjects, marks):
    print(subject, ":", mark)

print()

# 3. reversed() - loop over a list backwards
print("3. reversed():")
for number in reversed([1, 2, 3, 4, 5]):
    print(number)

print()

# 4. sorted() - loop over a list in sorted (ascending) order
# sorted() does NOT change the original list.
print("4. sorted():")
scores = [55, 90, 70, 85]
for score in sorted(scores):
    print(score)
print("Original list is unchanged:", scores)

print()

# 5. Looping over dictionary items with .items()
print("5. Looping over dictionary items:")
student = {"name": "Ali", "age": 20, "city": "Lahore"}
for key, value in student.items():
    print(key, "->", value)

# Sample output:
# 1. enumerate():
# 0 Ali
# 1 Sara
# 2 Ahmed
#
# 2. zip():
# Math : 85
# English : 90
# Science : 78
#
# 3. reversed():
# 5
# 4
# 3
# 2
# 1
#
# 4. sorted():
# 55
# 70
# 85
# 90
# Original list is unchanged: [55, 90, 70, 85]
#
# 5. Looping over dictionary items:
# name -> Ali
# age -> 20
# city -> Lahore
