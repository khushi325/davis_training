import numpy as np

# Input number
n = int(input("Enter a number: "))

# Find even factors
even_factors = []
for i in range(1, n + 1):
    if n % i == 0 and i % 2 == 0:
        even_factors.append(i)

# Convert to NumPy array
even_array = np.array(even_factors)

# Output
print("Even factors:", even_factors)
print("NumPy array:", even_array)