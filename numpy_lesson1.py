import numpy as np

# Task 1: Create a 1D array
sales = np.array([1000, 1500, 2000, 2500])

print("Sales:", sales)
print("Dimensions:", sales.ndim)
print("Shape:", sales.shape)
print("Total elements:", sales.size)

# Task 2: Create a 2D array
weekly_sales = np.array([
    [1000, 1500, 2000],
    [1200, 1800, 2200]
])

print("\nWeekly sales:")
print(weekly_sales)
print("Dimensions:", weekly_sales.ndim)
print("Shape:", weekly_sales.shape)
print("Total elements:", weekly_sales.size)
