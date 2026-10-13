# Task 11 — Dictionaries Basics
# Source: Week 1 syllabus, AI_NAVTTC_Outline_Tasks.pdf
# This example shows dict basics — create, access by key, add/update a pair,
# keys()/values()/items(), and looping — using a student's record.

# --- Create a dictionary ---
# A dict uses curly brackets { } and stores KEY: VALUE pairs.
# The key is the label; the value is the information for that label.
student = {
    "name": "Noyan",
    "age": 20,
    "course": "AI/ML",
    "marks": 85
}
print("Student dict:", student)

# --- Access by key: dict[key] gives the value for that key ---
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Marks:", student["marks"])

# --- Add a new pair: just assign a value to a new key ---
student["city"] = "Lahore"
print("After adding city:", student)

# --- Update an existing pair: assign a new value to an existing key ---
student["marks"] = 90
print("After updating marks:", student)

# --- keys(): all the labels ---
print("Keys:", list(student.keys()))

# --- values(): all the values ---
print("Values:", list(student.values()))

# --- items(): all the (key, value) pairs ---
print("Items:", list(student.items()))

# --- Loop through a dictionary ---
print("Loop through keys and values:")
for key, value in student.items():
    print(key, "->", value)

# Loop through keys only:
print("Keys only:")
for key in student.keys():
    print(key)

# Sample output:
# Student dict: {'name': 'Noyan', 'age': 20, 'course': 'AI/ML', 'marks': 85}
# Name: Noyan
# Age: 20
# Course: AI/ML
# Marks: 85
# After adding city: {'name': 'Noyan', 'age': 20, 'course': 'AI/ML', 'marks': 85, 'city': 'Lahore'}
# After updating marks: {'name': 'Noyan', 'age': 20, 'course': 'AI/ML', 'marks': 90, 'city': 'Lahore'}
# Keys: ['name', 'age', 'course', 'marks', 'city']
# Values: ['Noyan', 20, 'AI/ML', 90, 'Lahore']
# Items: [('name', 'Noyan'), ('age', 20), ('course', 'AI/ML'), ('marks', 90), ('city', 'Lahore')]
# Loop through keys and values:
# name -> Noyan
# age -> 20
# course -> AI/ML
# marks -> 90
# city -> Lahore
# Keys only:
# name
# age
# course
# marks
# city
