# Task 40 - NumPy: Random Numbers
# Source: https://www.w3schools.com/python/numpy_random.asp
# This example shows NumPy random numbers with a fixed seed, so the
# results are the same every time we run the file. That makes the
# output easy to check and easy to explain in a viva.

import numpy as np

# Set a fixed seed: the "random" numbers below will be the same
# on every run, which is what we want for coursework.
np.random.seed(42)

# randint() gives random whole numbers.
# randint(low, high, size): values from low up to (but not including) high.
random_ints = np.random.randint(1, 10, size=5)
print("Random integers between 1 and 9:", random_ints)

# rand() gives random decimal numbers between 0.0 and 1.0.
random_floats = np.random.rand(3)
print("Random floats between 0 and 1:", random_floats)

# choice() picks random elements from a list or array.
fruits = np.array(["apple", "banana", "cherry", "mango"])
random_fruit = np.random.choice(fruits)
print("Random fruit:", random_fruit)

# shuffle() mixes up an array in place (it changes the original).
numbers = np.array([1, 2, 3, 4, 5])
np.random.shuffle(numbers)
print("Shuffled array:", numbers)

# Sample output:
# Random integers between 1 and 9: [7 4 8 5 7]
# Random floats between 0 and 1: [0.44583275 0.09997492 0.45924889]
# Random fruit: apple
# Shuffled array: [1 2 3 5 4]
