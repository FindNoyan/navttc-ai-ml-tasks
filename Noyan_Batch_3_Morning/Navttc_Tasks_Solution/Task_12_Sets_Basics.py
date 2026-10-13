# Task 12 — Sets Basics
# Source: Week 1 syllabus, AI_NAVTTC_Outline_Tasks.pdf
# This example shows set basics — create, add, remove, union, intersection,
# difference — and using a set to remove duplicates from a list.

# --- Create a set ---
# A set uses curly brackets { } like a dict, but with values only, no keys.
# Two rules: (1) no duplicates — each value appears once.
# (2) no order — items are not stored in a fixed position.
fruits = {"apple", "banana", "mango"}
print("Fruits set:", fruits)

# Duplicates are removed automatically when a set is created.
numbers = {1, 2, 2, 3, 3, 3}
print("Set with duplicates removed:", numbers)

# --- add(): put one new item into the set ---
fruits.add("orange")
print("After add('orange'):", fruits)

# Adding a value that is already there does nothing (no duplicate).
fruits.add("apple")
print("After add('apple') again (no change):", fruits)

# --- remove(): take one item out of the set ---
fruits.remove("banana")
print("After remove('banana'):", fruits)

# --- Set operations with two sets ---
group_a = {"Math", "English", "Science"}
group_b = {"Science", "Urdu", "Computer"}
print("Group A:", group_a)
print("Group B:", group_b)

# union: all items from BOTH sets (no duplicates).
print("Union (A | B):", group_a | group_b)

# intersection: only the items in BOTH sets.
print("Intersection (A & B):", group_a & group_b)

# difference: items in A but NOT in B.
print("Difference (A - B):", group_a - group_b)

# --- Dedup: remove duplicates from a list using a set ---
marks_with_duplicates = [85, 78, 85, 92, 78, 90]
print("List with duplicates:", marks_with_duplicates)
unique_marks = list(set(marks_with_duplicates))
print("Unique marks (duplicates removed):", sorted(unique_marks))

# Sample output (set order may vary — sets have no fixed order):
# Fruits set: {'apple', 'banana', 'mango'}
# Set with duplicates removed: {1, 2, 3}
# After add('orange'): {'apple', 'banana', 'mango', 'orange'}
# After add('apple') again (no change): {'apple', 'banana', 'mango', 'orange'}
# After remove('banana'): {'apple', 'mango', 'orange'}
# Group A: {'Math', 'English', 'Science'}
# Group B: {'Science', 'Urdu', 'Computer'}
# Union (A | B): {'Math', 'English', 'Science', 'Urdu', 'Computer'}
# Intersection (A & B): {'Science'}
# Difference (A - B): {'Math', 'English'}
# List with duplicates: [85, 78, 85, 92, 78, 90]
# Unique marks (duplicates removed): [78, 85, 90, 92]
