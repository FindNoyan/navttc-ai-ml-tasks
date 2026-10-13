# Task 09 — Lists Basics
# Source: Week 1 syllabus, AI_NAVTTC_Outline_Tasks.pdf
# This example shows list basics — create, indexing, slicing, append, len,
# and looping — using a list of subjects and a list of marks.

# --- Create a list ---
# A list uses square brackets [ ] and can hold many values in one variable.
subjects = ["Math", "English", "Science", "Urdu", "Computer"]
marks = [85, 78, 92, 70, 88]

print("Subjects:", subjects)
print("Marks:", marks)

# --- Indexing: get one item by its position (counting starts at 0) ---
print("First subject [0]:", subjects[0])
print("Third subject [2]:", subjects[2])
print("Last subject [-1]:", subjects[-1])
print("First mark [0]:", marks[0])

# --- Slicing: get part of a list with [start:end] ---
print("First three subjects [0:3]:", subjects[0:3])
print("Last two subjects [-2:]:", subjects[-2:])

# --- len(): how many items are in the list ---
print("Number of subjects:", len(subjects))
print("Number of marks:", len(marks))

# --- append(): add one new item to the END of the list ---
subjects.append("Islamiat")
marks.append(80)
print("After append, subjects:", subjects)
print("After append, marks:", marks)

# --- Loop through a list: do something with each item, one by one ---
print("All subjects and marks:")
for i in range(len(subjects)):
    print(subjects[i], ":", marks[i])

# A simpler loop: go through the marks and add them up.
total = 0
for mark in marks:
    total = total + mark
print("Total marks:", total)
print("Average marks:", total / len(marks))

# Sample output:
# Subjects: ['Math', 'English', 'Science', 'Urdu', 'Computer']
# Marks: [85, 78, 92, 70, 88]
# First subject [0]: Math
# Third subject [2]: Science
# Last subject [-1]: Computer
# First mark [0]: 85
# First three subjects [0:3]: ['Math', 'English', 'Science']
# Last two subjects [-2:]: ['Urdu', 'Computer']
# Number of subjects: 5
# Number of marks: 5
# After append, subjects: ['Math', 'English', 'Science', 'Urdu', 'Computer', 'Islamiat']
# After append, marks: [85, 78, 92, 70, 88, 80]
# All subjects and marks:
# Math : 85
# English : 78
# Science : 92
# Urdu : 70
# Computer : 88
# Islamiat : 80
# Total marks: 493
# Average marks: 82.16666666666667
