# Task 50 - Standard Deviation in Python
# Source: https://www.w3schools.com/python/python_ml_standard_deviation.asp
# This example computes the standard deviation of a small dataset
# with statistics.pstdev() and statistics.stdev().
# Standard deviation tells us how spread out the values are:
# a small value means the numbers are close to the average,
# a large value means they are spread far apart.

import statistics

# Small dataset: 5 numbers.
data = [10, 12, 14, 16, 18]
print("Data:", data)
print("Mean:", statistics.mean(data))

# Population standard deviation: use this when the data is the
# WHOLE population (every value you care about is in the list).
population_sd = statistics.pstdev(data)
print("Population standard deviation (pstdev):", population_sd)

# Sample standard deviation: use this when the data is only a
# SAMPLE taken from a larger population. It divides by (n - 1)
# instead of n, so it is slightly larger than pstdev().
sample_sd = statistics.stdev(data)
print("Sample standard deviation (stdev):", sample_sd)

print("Note: stdev() is a little larger than pstdev() for the same data.")

# Sample output:
# Data: [10, 12, 14, 16, 18]
# Mean: 14
# Population standard deviation (pstdev): 2.8284271247461903
# Sample standard deviation (stdev): 3.1622776601683795
# Note: stdev() is a little larger than pstdev() for the same data.
