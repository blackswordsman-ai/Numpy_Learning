# NumPy array creation methods
import numpy as np

# a = np.arange(1, 6)
# print(a)

# a = np.zeros((2, 3))

# print(a)

# a = np.ones((3, 4))
# print(a)

# a= np.full((2, 3), 7)
# print(a)

# Question 4 — Coding exercise

# Write a program to:
# 1. Create an array containing numbers from 1 to 10 using np.arange().
# 2. Create a 2D array with 3 rows and 4 columns filled with zeros.
# 3. Create a 2D array with 2 rows and 3 columns filled with ones.
# 4. Print all three arrays and their shapes.

array_1 = np.arange(1, 11)
array_2 = np.zeros((3, 4))
array_3 = np.ones((2, 3))
print("Array 1:\n", array_1)
print("Shape of Array 1:", array_1.shape)
print("\nArray 2:\n", array_2)
print("Shape of Array 2:", array_2.shape)
print("\nArray 3:\n", array_3)
print("Shape of Array 3:", array_3.shape)