# Task 21 - List Methods in Python
# Source: https://www.programiz.com/python-programming/list
# This example practices list methods using a shopping list:
# append, extend, insert, remove, pop, sort, reverse, count, index, copy.

# Start with a small shopping list.
shopping_list = ["milk", "bread", "eggs"]
print("Starting list:", shopping_list)

# append() - add one item to the end of the list
shopping_list.append("butter")
print("After append('butter'):", shopping_list)

# extend() - add several items to the end of the list
shopping_list.extend(["cheese", "apples"])
print("After extend(['cheese', 'apples']):", shopping_list)

# insert() - add one item at a chosen position (index 1)
shopping_list.insert(1, "rice")
print("After insert(1, 'rice'):", shopping_list)

# remove() - remove the first item with this value
shopping_list.remove("bread")
print("After remove('bread'):", shopping_list)

# pop() - remove and return the item at an index (last item if no index given)
removed_item = shopping_list.pop()
print("pop() removed:", removed_item)
print("After pop():", shopping_list)

# Add a duplicate item so we can use count() and index()
shopping_list.append("milk")
print("After append('milk') again:", shopping_list)

# count() - how many times a value appears in the list
print("Count of 'milk':", shopping_list.count("milk"))

# index() - position (index) of the first occurrence of a value
print("Index of 'cheese':", shopping_list.index("cheese"))

# sort() - arrange items in alphabetical order (changes the list)
shopping_list.sort()
print("After sort():", shopping_list)

# reverse() - reverse the order of the list (changes the list)
shopping_list.reverse()
print("After reverse():", shopping_list)

# copy() - make a separate copy of the list
backup_list = shopping_list.copy()
print("Copy of the list:", backup_list)

# Changing the copy does NOT change the original list.
backup_list.append("tea")
print("After adding 'tea' to the copy:")
print("Original list:", shopping_list)
print("Copy list:", backup_list)

# Sample output:
# Starting list: ['milk', 'bread', 'eggs']
# After append('butter'): ['milk', 'bread', 'eggs', 'butter']
# After extend(['cheese', 'apples']): ['milk', 'bread', 'eggs', 'butter', 'cheese', 'apples']
# After insert(1, 'rice'): ['milk', 'rice', 'bread', 'eggs', 'butter', 'cheese', 'apples']
# After remove('bread'): ['milk', 'rice', 'eggs', 'butter', 'cheese', 'apples']
# pop() removed: apples
# After pop(): ['milk', 'rice', 'eggs', 'butter', 'cheese']
# After append('milk') again: ['milk', 'rice', 'eggs', 'butter', 'cheese', 'milk']
# Count of 'milk': 2
# Index of 'cheese': 4
# After sort(): ['butter', 'cheese', 'eggs', 'milk', 'milk', 'rice']
# After reverse(): ['rice', 'milk', 'milk', 'eggs', 'cheese', 'butter']
# Copy of the list: ['rice', 'milk', 'milk', 'eggs', 'cheese', 'butter']
# After adding 'tea' to the copy:
# Original list: ['rice', 'milk', 'milk', 'eggs', 'cheese', 'butter']
# Copy list: ['rice', 'milk', 'milk', 'eggs', 'cheese', 'butter', 'tea']
