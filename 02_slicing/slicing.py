import numpy as np

# ==================================================
# NumPy Slicing & Indexing Examples
# ==================================================

'''
💡 Important Note:
- Slicing a Python list creates a new list (a copy).
- Slicing a NumPy array returns a view: changes in the view reflect in the original array.
'''

# Creating a 4x4 NumPy array
array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

# ==================================================
# Row selection
# ==================================================
print("Single rows:")
print(array[0])   # First row
print(array[1])   # Second row
print(array[2])   # Third row
print(array[3])   # Fourth row
print(array[-1])  # Last row (negative indexing)

# ==================================================
# Slicing rows
# ==================================================
print("\nSlice rows (0:3 means rows 0, 1, 2):")
print(array[0:3])   # From row 0 to 2 (end exclusive)

print("\nSlice rows (1:4):")
print(array[1:4])   # Rows 1, 2, 3

# ==================================================
# Step in 02_slicing
# ==================================================
print("\nRows with step 2 (0:4:2):")
print(array[0:4:2]) # Rows 0 and 2

print("\nReverse all rows:")
print(array[::-1])  # Reverse all rows

# ==================================================
# Column selection
# ==================================================
print("\nSelect first column:")
print(array[:, 0])  # All rows, first column

print("\nSelect single element (row 1, column 2):")
print(array[1:2, 2])  # Second row, third element

print("\nSlice subarray (row 1, first two columns):")
print(array[1:2, :2])  # Second row, columns 0 and 1
