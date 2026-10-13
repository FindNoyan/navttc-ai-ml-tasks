# Task 25 - Dictionary Methods in Python
# Source: https://www.programiz.com/python-programming/dictionary
# This example shows dictionary methods using a student record:
# get, update, pop, keys/values/items, and setdefault.
# A dictionary stores key-value pairs, e.g. "name": "Ali".

student = {"name": "Ali", "age": 20, "course": "AI/ML"}
print("Student record:", student)

# get() - safely get a value by key (returns None if the key is missing)
print("Name (get):", student.get("name"))
print("Grade (get, missing key):", student.get("grade"))
print("Grade with default (get):", student.get("grade", "Not assigned yet"))

# update() - add new pairs or change existing values
student.update({"grade": "A", "age": 21})
print("After update({'grade': 'A', 'age': 21}):", student)

# setdefault() - add a key only if it is NOT already present
student.setdefault("city", "Lahore")
print("After setdefault('city', 'Lahore'):", student)
student.setdefault("name", "Someone Else")  # Does nothing, "name" already exists
print("After setdefault('name', 'Someone Else'):", student)

# keys() - all the keys in the dictionary
print("Keys:", list(student.keys()))

# values() - all the values in the dictionary
print("Values:", list(student.values()))

# items() - all the key-value pairs
print("Items:")
for key, value in student.items():
    print(key, "->", value)

# pop() - remove a key and return its value
removed_age = student.pop("age")
print("pop('age') removed:", removed_age)
print("After pop('age'):", student)

# Sample output:
# Student record: {'name': 'Ali', 'age': 20, 'course': 'AI/ML'}
# Name (get): Ali
# Grade (get, missing key): None
# Grade with default (get): Not assigned yet
# After update({'grade': 'A', 'age': 21}): {'name': 'Ali', 'age': 21, 'course': 'AI/ML', 'grade': 'A'}
# After setdefault('city', 'Lahore'): {'name': 'Ali', 'age': 21, 'course': 'AI/ML', 'grade': 'A', 'city': 'Lahore'}
# After setdefault('name', 'Someone Else'): {'name': 'Ali', 'age': 21, 'course': 'AI/ML', 'grade': 'A', 'city': 'Lahore'}
# Keys: ['name', 'age', 'course', 'grade', 'city']
# Values: ['Ali', 21, 'AI/ML', 'A', 'Lahore']
# Items:
# name -> Ali
# age -> 21
# course -> AI/ML
# grade -> A
# city -> Lahore
# pop('age') removed: 21
# After pop('age'): {'name': 'Ali', 'course': 'AI/ML', 'grade': 'A', 'city': 'Lahore'}
