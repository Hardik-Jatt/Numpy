import numpy as np

# Create a 1D array
array = np.array([1, 2, 3, 4, 5])

# Adding elements
# Append element at the end
array_with_append = np.append(array, 6)
print("Array after append:", array_with_append)

# Insert element at a specific position
array_with_insert = np.insert(array, 2, 99)  # Insert 99 at index 2
print("Array after insert:", array_with_insert)

# Concatenate two arrays
array_to_concatenate = np.array([7, 8, 9])
concatenated_array = np.concatenate((array, array_to_concatenate))
print("Concatenated array:", concatenated_array)

# Removing elements
# Delete element at a specific position
array_with_delete = np.delete(array, 1)  # Delete element at index 1
print("Array after delete:", array_with_delete)

# Delete multiple elements
array_with_multiple_delete = np.delete(array, [1, 3])  # Delete elements at indices 1 and 3
print("Array after deleting multiple elements:", array_with_multiple_delete)

# Reshape the array (method of array manipulation)
reshaped_array = array.reshape((5, 1))
print("Reshaped array:\n", reshaped_array)
