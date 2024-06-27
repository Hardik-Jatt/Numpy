import numpy as np

# Create two arrays
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# Basic arithmetic operations
sum_array = a + b
difference_array = b - a
product_array = a * b
division_array = b / a

print("Sum:", sum_array)
print("Difference:", difference_array)
print("Product:", product_array)
print("Division:", division_array)

# Broadcasting example: adding a scalar to an array
scalar_addition = a + 10
print("Array after adding 10 to each element:", scalar_addition)

# Broadcasting example: multiplying a scalar with an array
scalar_multiplication = b * 2
print("Array after multiplying each element by 2:", scalar_multiplication)