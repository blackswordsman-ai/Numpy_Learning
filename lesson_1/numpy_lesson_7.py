import numpy as np
import time

# Create one million numbers
numbers = list(range(1_000_000))
array = np.arange(1_000_000)

# Python list
start = time.perf_counter()

result_list = [number * 2 for number in numbers]

python_time = time.perf_counter() - start

# NumPy array
start = time.perf_counter()

result_array = array * 2

numpy_time = time.perf_counter() - start

print("Python list time:", python_time)
print("NumPy time:", numpy_time)