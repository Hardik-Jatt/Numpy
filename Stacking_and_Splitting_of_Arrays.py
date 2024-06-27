import numpy as np

# Create two 2D arrays
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])

# Stacking arrays vertically
vertical_stack = np.vstack((array1, array2))
print("Vertical Stack:\n", vertical_stack)

# Stacking arrays horizontally
horizontal_stack = np.hstack((array1, array2))
print("Horizontal Stack:\n", horizontal_stack)

# Splitting arrays
# Split the vertical_stack into 2 arrays along rows
split_vertical = np.vsplit(vertical_stack, 2)
print("Vertical Split:")
for i, arr in enumerate(split_vertical):
    print(f"Array {i+1}:\n", arr)

# Split the horizontal_stack into 2 arrays along columns
split_horizontal = np.hsplit(horizontal_stack, 2)
print("Horizontal Split:")
for i, arr in enumerate(split_horizontal):
    print(f"Array {i+1}:\n", arr)
