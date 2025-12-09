import numpy as np

# ==================================================
# NumPy Version Check
# ==================================================
print(np.__version__)

# ==================================================
# List vs NumPy Array
# ==================================================
my_list = [1, 2, 3, 4]
print("Original Python list:", my_list)

# Multiplying a list duplicates the elements
my_list = my_list * 2
print("List multiplied by 2:", my_list)

# NumPy array
array = np.array([1, 2, 3, 4])
print("Original NumPy array:", array)

# Multiplying an array scales each element
array = array * 2
print("Array multiplied by 2:", array)

# ==================================================
# Multidimensional Arrays
# ==================================================
# 0-dimensional array (scalar)
array = np.array('A')
print("0D array ndim:", array.ndim)

# 1-dimensional array
array = np.array(['A', 'B', 'C'])
print("1D array ndim:", array.ndim)

# 2-dimensional array (matrix)
array = np.array([['A', 'B'],
                  ['C', 'D'],
                  ['E', 'F']])
print("2D array ndim:", array.ndim)

# 3-dimensional array
array = np.array([[['A', 'B'],
                   ['C', 'D'],
                   ['E', 'F']]])
print("3D array ndim:", array.ndim)

# 3D array with multiple layers
array = np.array([[['A', 'B'], ['C', 'D'], ['E', 'F']],
                  [['A', 'B'], ['C', 'D'], ['E', 'F']],
                  [['A', 'B'], ['C', 'D'], ['E', 'F']]])
print("3D array ndim:", array.ndim)
print("Array shape:", array.shape)

# ==================================================
# Array Accessing
# ==================================================
# Chain indexing
print("First element via chain indexing:", array[0][0][0])

# Multidimensional indexing
print("First element via multi-dimensional indexing:", array[0, 0, 0])

# Combining elements
word = array[0, 0, 0] + array[0, 0, 1] + array[0, 0, 1]
print("Combined elements:", word)

# ==================================================
# Notes
# ==================================================
'''
💡 Important Notes:
- All elements in a NumPy array must have the same data type.
- The total size of a NumPy array cannot change once created.
- The shape must be rectangular (e.g., all rows in a 2D array must have the same number of columns).
- NumPy arrays are mutable like Python lists.
'''
