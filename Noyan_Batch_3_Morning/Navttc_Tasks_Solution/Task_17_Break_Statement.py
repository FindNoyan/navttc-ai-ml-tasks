# Task 17 - Break Statement in Python
# Source: https://www.geeksforgeeks.org/python-break-statement/
# This example searches a list for a target number.
# When the number is found, break stops the loop immediately.

numbers = [3, 7, 11, 15, 22, 30]
target = 15

# We use a variable to remember whether we found the target.
found = False

for number in numbers:
    if number == target:
        print("Found", target, "in the list!")
        found = True
        break  # Stop the loop at once; no need to check the rest
    print("Checked", number, "- not the target")

# After the loop, report the final result.
if found:
    print("Search finished: number was found.")
else:
    print("Search finished: number was NOT found.")

# Sample output:
# Checked 3 - not the target
# Checked 7 - not the target
# Checked 11 - not the target
# Found 15 in the list!
# Search finished: number was found.
