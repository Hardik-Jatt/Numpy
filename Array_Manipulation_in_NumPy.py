import numpy as np

# Create an initial array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Array:\n", array)

# Reshaping the array
reshaped_array = array.reshape((1, 9))
print("Reshaped Array (1x9):\n", reshaped_array)

# Transposing the array
transposed_array = array.T
print("Transposed Array:\n", transposed_array)

# Flattening the array
flattened_array = array.flatten()
print("Flattened Array:\n", flattened_array)

# Modifying elements
# Setting all elements greater than 5 to 0
modified_array = np.where(array > 5, 0, array)
print("Modified Array (elements > 5 set to 0):\n", modified_array)

# Adding a new row
new_row = np.array([10, 11, 12])
array_with_new_row = np.vstack((array, new_row))
print("Array with New Row:\n", array_with_new_row)

# Adding a new column
new_column = np.array([[13], [14], [15], [16]])
array_with_new_column = np.hstack((array_with_new_row, new_column))
print("Array with New Column:\n", array_with_new_column)

# Removing a row
array_with_row_removed = np.delete(array_with_new_column, 1, axis=0)
print("Array with Row Removed:\n", array_with_row_removed)

# Removing a column
array_with_column_removed = np.delete(array_with_row_removed, 2, axis=1)
print("Array with Column Removed:\n", array_with_column_removed)
