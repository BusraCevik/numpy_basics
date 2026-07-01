import numpy as np

# ==================================================
# NumPy Version Check
# ==================================================
print(np.__version__)

# ==================================================
# List vs NumPy Array (Memory and Vectorization)
# ==================================================
my_list = [1, 2, 3, 4]
print("Original Python list:", my_list)

# Multiplying a list duplicates the elements (creates a longer list)
my_list = my_list * 2
print("List multiplied by 2:", my_list)

# NumPy array
array = np.array([1, 2, 3, 4])
print("Original NumPy array:", array)

# Multiplying an array scales each element (Vectorized operation)
array = array * 2
print("Array multiplied by 2:", array)

# ==================================================
# Multidimensional Arrays & Key Attributes
# ==================================================
# 0-dimensional array (scalar)
array_0d = np.array('A')
print("0D array ndim:", array_0d.ndim)

# 1-dimensional array (vector)
array_1d = np.array(['A', 'B', 'C'])
print("1D array ndim:", array_1d.ndim)

# 2-dimensional array (matrix)
array_2d = np.array([['A', 'B'],
                     ['C', 'D'],
                     ['E', 'F']])
print("2D array ndim:", array_2d.ndim)

# 3-dimensional array (tensor)
array_3d = np.array([[['A', 'B'],
                      ['C', 'D'],
                      ['E', 'F']]])
print("3D array ndim:", array_3d.ndim)

# 3D array with multiple layers
array_3d_layers = np.array([[['A', 'B'], ['C', 'D'], ['E', 'F']],
                            [['A', 'B'], ['C', 'D'], ['E', 'F']],
                            [['A', 'B'], ['C', 'D'], ['E', 'F']]])
print("3D layers array ndim:", array_3d_layers.ndim)
print("3D layers array shape:", array_3d_layers.shape)
print("3D layers array size (total elements):", array_3d_layers.size)

# ==================================================
# Array Initialization Functions
# ==================================================
zeros_array = np.zeros((3, 4), dtype=np.float32)
ones_array = np.ones((2, 2), dtype=np.int32)
range_array = np.arange(0, 10, 2)
linspace_array = np.linspace(0, 1, 5)

# ==================================================
# Implicit Upcasting Trap
# ==================================================
mixed_array = np.array([1, 2.5, "A"])
print("Mixed array automatically upcasted dtype:", mixed_array.dtype)

# ==================================================
# Array Accessing (Performance Comparison)
# ==================================================
# Chain indexing (Creates intermediate copies in memory, slower)
print("First element via chain indexing:", array_3d_layers[0][0][0])

# Multidimensional indexing (Direct memory pointer access, faster and preferred)
print("First element via multi-dimensional indexing:", array_3d_layers[0, 0, 0])

# Combining elements
word = array_3d_layers[0, 0, 0] + array_3d_layers[0, 0, 1] + array_3d_layers[0, 0, 1]
print("Combined elements:", word)

# ==================================================
# Notes
# ==================================================
'''
Notes:

1. Homogeneous Data & Upcasting:
   - All elements in a NumPy array must have the identical data type (dtype).
   - If you provide mixed types, NumPy triggers "Implicit Upcasting" to the most complex type 
     without raising an error (e.g., mixing int, float, and string converts everything to string).
   - Always enforce explicitly using the 'dtype' parameter to prevent unnecessary memory bloating.

2. Memory Allocation (Python List vs. NumPy Array):
   - Python Lists: Store pointers to scattered object locations in memory (Referential Array). 
     This causes high overhead and poor cache utilization.
   - NumPy Arrays: Store data in contiguous blocks of memory (Contiguous Memory Allocation). 
     This allows SIMD (Single Instruction, Multiple Data) processing and vectorization, making it lightning fast.

3. Structural Properties:
   - Fixed Size: The total allocated size of a NumPy array cannot change post-creation. 
     Appending or deleting elements under the hood creates an entirely new array copy.
   - Rectangular Shape: The structure must be balanced (e.g., a 2D array cannot have jagged rows).
   - Mutability: Arrays are mutable, meaning you can modify individual items in place without changing the memory reference.

4. Core Metadata Attributes:
   - ndim: Total number of dimensions/axes (axes count).
   - shape: A tuple showing the size of the array along each axis (e.g., (layers, rows, columns)).
   - size: Total number of individual elements across all dimensions (product of shape elements).

5. Access Mechanics (Chain vs. Multidimensional Indexing):
   - matrix[0][0] executes two sequential operations: fetches the first row object, then extracts the element.
   - matrix[0, 0] executes a single highly optimized coordinate lookup using strides directly in C, maximizing efficiency.
'''