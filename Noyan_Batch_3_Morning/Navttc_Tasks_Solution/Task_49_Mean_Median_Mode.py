# Task 49 - Mean, Median and Mode in Python
# Source: https://www.w3schools.com/python/python_ml_mean_median_mode.asp
# This example uses a small dataset of student marks to compute
# the mean, median and mode using the statistics module.
# It also shows one manual mean calculation (sum / count).

import statistics

# Small dataset: marks of 10 students out of 100.
marks = [70, 80, 90, 70, 85, 70, 95, 80, 75, 70]
print("Student marks:", marks)

# Mean: the average. Add all values, then divide by how many there are.
# Manual calculation, step by step:
total = sum(marks)        # Add all the marks together
count = len(marks)        # Count how many marks there are
manual_mean = total / count
print("Manual mean: sum =", total, "/ count =", count, "=", manual_mean)

# Same result using the statistics module:
mean_value = statistics.mean(marks)
print("Mean (statistics.mean):", mean_value)

# Median: the middle value when the data is sorted.
# With an even count, it is the average of the two middle values.
median_value = statistics.median(marks)
print("Median (statistics.median):", median_value)
print("Sorted marks:", sorted(marks))

# Mode: the value that appears most often.
mode_value = statistics.mode(marks)
print("Mode (statistics.mode):", mode_value)

# Sample output:
# Student marks: [70, 80, 90, 70, 85, 70, 95, 80, 75, 70]
# Manual mean: sum = 785 / count = 10 = 78.5
# Mean (statistics.mean): 78.5
# Median (statistics.median): 77.5
# Sorted marks: [70, 70, 70, 70, 75, 80, 80, 85, 90, 95]
# Mode (statistics.mode): 70
