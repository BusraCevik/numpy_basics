import numpy as np

# ==================================================
# NumPy Slicing & Indexing Examples
# ==================================================

# Creating a 4x4 NumPy array
matrix = np.array([[1,  2,  3,  4],
                   [5,  6,  7,  8],
                   [9,  10, 11, 12],
                   [13, 14, 15, 16]])

# ==================================================
# Row Selection & Slicing
# ==================================================
print("Single row (returns 1D):", matrix[0])
print("Last row via negative indexing:", matrix[-1])

# Slicing syntax -> start:stop:step (stop is exclusive)
print("\nSlice rows 0 to 2:\n", matrix[0:3])
print("\nRows with step 2 (Rows 0 and 2):\n", matrix[0:4:2])
print("\nReverse all rows vertically:\n", matrix[::-1])

# ==================================================
# Column Selection & Slicing (The Dimension Trap)
# ==================================================
# Selecting a column with a scalar index drops the dimension to 1D
column_1d = matrix[:, 0]
print("\nFirst column (Scalar index -> 1D shape):", column_1d.shape)

# Selecting a column with a slice preserves the 2D structural shape
column_2d = matrix[:, 0:1]
print("First column (Slice index -> 2D shape):\n", column_2d.shape)

# Slicing a specific subarray (Row 1, columns 0 and 1)
print("\nSubarray slice:\n", matrix[1, :2])

# ==================================================
# The Critical Interview Trap: View vs Copy
# ==================================================
# Creating a view (slicing)
matrix_view = matrix[0:2, 0:2]

# Modifying the view modifies the original matrix because they share the same memory layout
matrix_view[0, 0] = 99
print("\nOriginal matrix after modifying its VIEW (Element [0,0] changed):")
print(matrix)

# To prevent this, explicitly create a deep copy in memory
matrix_copy = matrix[0:2, 0:2].copy()
matrix_copy[0, 1] = 88  # This will NOT affect the original matrix

# ==================================================
# Notes
# ==================================================
'''
Notes:

1. Memory Mechanics (Views vs. Deep Copies):
   - Python List Slicing: Allocates brand new memory space and copies elements (Deep Copy).
   - NumPy Array Slicing: Creates a internal pointer mapping to the original memory layout (View).
   - Core Reason: Performance-driven design. Copying giant multi-gigabyte datasets during data 
     preprocessing would cause memory overhead and performance bottlenecks.
   - Guardrail: Always use the `.copy()` method if the extracted subset needs safe modifications.

2. Structural Integrity (Dimensionality Preservation):
   - Standard indexing using an integer like `matrix[:, 0]` flattens the output shape into a 1D vector.
   - Slicing syntax like `matrix[:, 0:1]` forces NumPy to retain the explicit 2D structure (N rows, 1 column).
   - Keeping dimensions uniform is crucial when passing arrays into Scikit-Learn or Deep Learning layers.

3. Multi-Axis Slicing Syntax:
   - Evaluated as `matrix[row_axis_slice, column_axis_slice]`.
   - Each axis strictly abides by the standard logical protocol -> `start:stop:step`.
'''