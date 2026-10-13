# Task 24 - Set Operations in Python
# Source: https://www.programiz.com/python-programming/set
# This example shows set operations with two small sets:
# students in the Coding Club and students in the Art Club.
# A set stores unique items only (no duplicates) and has no order.

coding_club = {"Ali", "Sara", "Ahmed", "Ayesha"}
art_club = {"Sara", "Ayesha", "Bilal", "Hassan"}

print("Coding Club:", coding_club)
print("Art Club:", art_club)

# union() - all students in either club (no duplicates)
print("Union (in either club):", coding_club.union(art_club))

# intersection() - students in BOTH clubs
print("Intersection (in both clubs):", coding_club.intersection(art_club))

# difference() - students in Coding Club but NOT in Art Club
print("Difference (Coding only):", coding_club.difference(art_club))

# symmetric_difference() - students in exactly ONE club (not both)
print("Symmetric difference (in only one club):", coding_club.symmetric_difference(art_club))

# issubset() - check if every item of one set is inside another set
small_group = {"Ali", "Sara"}
print("Is {'Ali', 'Sara'} a subset of Coding Club?", small_group.issubset(coding_club))
print("Is Art Club a subset of Coding Club?", art_club.issubset(coding_club))

# Sample output (set order may vary, but the members are the same):
# Coding Club: {'Ali', 'Sara', 'Ahmed', 'Ayesha'}
# Art Club: {'Sara', 'Ayesha', 'Bilal', 'Hassan'}
# Union (in either club): {'Ali', 'Sara', 'Ahmed', 'Ayesha', 'Bilal', 'Hassan'}
# Intersection (in both clubs): {'Sara', 'Ayesha'}
# Difference (Coding only): {'Ali', 'Ahmed'}
# Symmetric difference (in only one club): {'Ali', 'Ahmed', 'Bilal', 'Hassan'}
# Is {'Ali', 'Sara'} a subset of Coding Club? True
# Is Art Club a subset of Coding Club? False
