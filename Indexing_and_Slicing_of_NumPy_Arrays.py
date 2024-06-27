import numpy as np

# Create a 2D array (matrix)
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Indexing: accessing elements
element_1_2 = matrix[1, 2]  # Access element at row 1, column 2
print("Element at (1, 2):", element_1_2)

# Slicing: accessing subarrays
row_slice = matrix[1, :]  # Access entire row 1
column_slice = matrix[:, 2]  # Access entire column 2
submatrix = matrix[0:2, 1:3]  # Access submatrix from rows 0-1 and columns 1-2

print("Row slice:", row_slice)
print("Column slice:", column_slice)
print("Submatrix:\n", submatrix)

# Modifying elements using indexing
matrix[0, 0] = 99  # Modify element at (0, 0)
print("Modified matrix:\n", matrix)

# Modifying elements using slicing
matrix[1:, 1:] = 0  # Set bottom-right 2x2 submatrix to 0
print("Matrix after modifying submatrix:\n", matrix)